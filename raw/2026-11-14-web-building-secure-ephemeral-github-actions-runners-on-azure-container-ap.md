---
source: "https://techcommunity.microsoft.com/blog/azureinfrastructureblog/building-secure-ephemeral-github-actions-runners-on-azure-container-apps/4569209"
title: "Building Secure, Ephemeral GitHub Actions Runners on Azure Container Apps"
author: "ibrahimbaig"
date_published: "2026-11-01"
date_clipped: "2026-11-14"
category: "DevOps & CI/CD"
source_type: "web"
---

# Building Secure, Ephemeral GitHub Actions Runners on Azure Container Apps

**A practical architecture using KEDA autoscaling, GitHub App authentication, private Key Vault access, Microsoft Container Registry, and GitHub OIDC**

*Implementation guide and field learnings*

|  |
| --- |
| **What this architecture delivers**  ·       **A repository-scoped runner that exists only for one workflow**  ·       **Automatic scale-from-zero with an Azure Container Apps Event Job and KEDA**  ·       **GitHub App authentication instead of a personal access token**  ·       **Private secret retrieval using a managed identity, private endpoint and private DNS**  ·       **Secretless Azure deployment from workflows through GitHub OIDC**  ·       **No customer-managed Azure Container Registry for the runner image** |

**This article focuses on the final event-driven architecture and the implementation decisions that made it secure, repeatable and useful for real infrastructure workflows.**

# Why this pattern?

GitHub-hosted runners are the simplest option for many teams, but some workflows need private network access, organization-approved tooling or tighter control over the execution boundary. Long-running self-hosted virtual machines solve those needs, but introduce patching, capacity planning and idle cost.

Azure Container Apps Jobs provide a serverless execution boundary for finite tasks. With the KEDA GitHub runner scaler, an execution can start when a matching workflow is queued, register one ephemeral runner, process one job and terminate. Setting the minimum execution count to zero preserves scale-to-zero when the queue is empty.

The important design work begins around that lifecycle: how the runner image is prepared, how GitHub is authenticated, where secrets are stored, how private access is enforced, and which identity is allowed to deploy Azure resources.

# Reference architecture

Figure 1. End-to-end event-driven architecture and trust boundaries.

A matching GitHub Actions workflow enters the queue. The KEDA github-runner scaler polls GitHub using GitHub App authentication and starts an Azure Container Apps Event Job when the queue length reaches the configured target.

The event job pulls a Microsoft-maintained base image from Microsoft Container Registry. At startup, the container installs or verifies the required toolchain, obtains GitHub App material from a private Azure Key Vault, generates short-lived GitHub credentials and registers a repository-level ephemeral runner.

The workflow executes on that runner. When Azure access is needed, the workflow obtains a GitHub OIDC token and exchanges it through a federated credential on a separate Microsoft Entra deployment identity. Azure RBAC limits that identity to the intended deployment scope.

After one workflow, the runner exits and the Container Apps job completes. With no remaining matching work, the solution returns to zero executions.

# Secure authentication flow

Figure 2. Private secret retrieval and short-lived GitHub token exchange.

1. **Queue detection:** KEDA queries GitHub for jobs matching the configured owner, repository and label.
2. **Job startup:** Azure Container Apps starts one event-job execution for eligible queue demand, subject to the configured maximum executions.
3. **Private secret retrieval:** The job authenticates with its user-assigned managed identity. Private DNS resolves the vault hostname to the private endpoint, and Key Vault returns only the permitted GitHub App secrets.
4. **GitHub App JWT:** The bootstrap signs a short-lived RS256 JWT with the GitHub App private key.
5. **Installation token:** The JWT is exchanged for an installation access token scoped to the installed GitHub App.
6. **Runner registration token:** The installation token requests a repository-level runner registration token.
7. **Ephemeral registration:** The runner is configured unattended, with updates disabled for that execution, an explicit custom label and ephemeral mode.
8. **Credential cleanup:** Temporary private-key files, JWTs and bootstrap tokens are removed before workflow code begins wherever possible.
9. **One workflow:** The runner accepts one matching job, reports the result, deregisters and exits.
10. **Scale to zero:** The Container Apps execution completes; no idle runner remains.

# MCR runtime bootstrap versus a pre-baked image

Figure 3. Image strategy trade-offs. Both options are valid; choose by operating requirements.

This implementation intentionally pulls a Microsoft base image from MCR and installs the required tools when the job starts. That removes Azure Container Registry, an image build pipeline and registry access configuration from the runner platform.

The cost of that simplification is startup latency. A pre-baked image can begin runner registration almost immediately because Git, Terraform, PowerShell and the GitHub runner are already present. Runtime bootstrap must download and install missing components before the runner becomes available. The observed delay will vary with image-pull time, package endpoint latency, tool size and regional network conditions, so measure queue-to-ready time with representative workflows rather than relying on a generic estimate.

Runtime bootstrap also introduces external dependencies. If a package repository, GitHub release endpoint or download source is unavailable, the runner cannot become ready. Pin versions, validate downloads, use bounded retries and record each bootstrap phase in logs.

A pre-baked image is preferable when startup time is strict, workflows run frequently, software must be scanned before execution, or image promotion and rollback are required. The MCR-plus-bootstrap model is attractive when the goal is to avoid a dedicated registry and custom image lifecycle, while accepting additional cold-start time.

| **Decision factor** | **MCR + runtime bootstrap** | **Pre-baked image + ACR** |
| --- | --- | --- |
| **Ready time** | Higher cold-start latency | Typically faster |
| **Artifact control** | Depends on base-image and bootstrap pinning | Immutable tag/digest and release promotion |
| **Platform footprint** | No dedicated ACR | Requires ACR and image-pull authorization |
| **Maintenance** | Bootstrap script and download endpoints | Dockerfile, build, scan, patch and publish |
| **Best fit** | Lower-frequency or simpler runner platform | High-frequency or controlled enterprise image supply chain |

# Step-by-step implementation guide

Replace the example values with approved environment-specific names and scopes. Run the PowerShell-oriented Azure CLI commands from Cloud Shell or a current Azure CLI workstation.

|  |
| --- |
| **Security boundary before you begin**  **Use a private GitHub repository. Do not place a GitHub App private key, installation token, runner registration token, Azure access token or client secret in source control. The only long-lived GitHub credential in this design is the GitHub App private key, which is stored in Azure Key Vault and used only to mint short-lived tokens.** |

## 1. Prerequisites and permissions

- An Azure subscription in which you can create resource groups, virtual networks, private endpoints, managed identities, Key Vault resources, Container Apps environments and event jobs.
- Permission to assign Azure RBAC roles at the Key Vault and workload deployment scopes. If you cannot create Entra applications or federated credentials, request those objects from the tenant identity team before the OIDC step.
- A private GitHub repository and permission to create and install a GitHub App for that repository.
- Azure CLI with the Container Apps extension, Git, and an editor. Docker and an Azure Container Registry are not required for this implementation.
- Outbound HTTPS connectivity from the Container Apps environment to GitHub APIs, GitHub Actions endpoints, Microsoft identity/Azure APIs, MCR and the package/download sources used by the bootstrap.

```
az login --tenant "<tenant-id>"
az account set --subscription "<subscription-id>"
az extension add --name containerapp --upgrade --allow-preview true
az provider register --namespace Microsoft.App
az provider register --namespace Microsoft.OperationalInsights
az provider register --namespace Microsoft.KeyVault
```

## 2. Define reusable variables

Use one naming block throughout the deployment. The values below are examples only.

```
$SubscriptionId = "<subscription-id>"
$TenantId       = "<tenant-id>"
$Location       = "centralindia"
$ResourceGroup  = "rg-aca-github-runner"

$VnetName       = "vnet-aca-github-runner"
$VnetCidr       = "10.50.0.0/16"
$AcaSubnetName  = "snet-aca"
$AcaSubnetCidr  = "10.50.1.0/27"
$PeSubnetName   = "snet-private-endpoints"
$PeSubnetCidr   = "10.50.2.0/27"

$EnvironmentName = "cae-github-runner"
$JobName         = "caj-github-runner-event"
$IdentityName    = "id-github-runner"
$KeyVaultName    = "<globally-unique-key-vault-name>"
$LogWorkspace    = "law-aca-github-runner"

$GitHubOwner     = "<github-owner>"
$GitHubRepo      = "<repository-name>"
$RunnerLabel     = "aca-linux"
$RunnerVersion   = "<tested-runner-version>"
$TerraformVersion = "<tested-terraform-version>"
$PowerShellVersion = "<tested-powershell-version>"

az account set --subscription $SubscriptionId
az group create --name $ResourceGroup --location $Location
```

## 3. Create the network boundary

Use separate, non-overlapping subnets for the delegated Container Apps environment and the Key Vault private endpoint.

```
az network vnet create `
  --resource-group $ResourceGroup `
  --name $VnetName `
  --location $Location `
  --address-prefixes $VnetCidr

az network vnet subnet create `
  --resource-group $ResourceGroup `
  --vnet-name $VnetName `
  --name $AcaSubnetName `
  --address-prefixes $AcaSubnetCidr `
  --delegations Microsoft.App/environments

az network vnet subnet create `
  --resource-group $ResourceGroup `
  --vnet-name $VnetName `
  --name $PeSubnetName `
  --address-prefixes $PeSubnetCidr `
  --disable-private-endpoint-network-policies true

$AcaSubnetId = az network vnet subnet show `
  --resource-group $ResourceGroup `
  --vnet-name $VnetName `
  --name $AcaSubnetName `
  --query id --output tsv
```

**Validation:** Confirm that the ACA subnet shows delegation to Microsoft.App/environments and that the private-endpoint subnet has private endpoint network policies disabled.

## 4. Create the runtime managed identity

```
az identity create `
  --resource-group $ResourceGroup `
  --name $IdentityName `
  --location $Location

$IdentityId = az identity show `
  --resource-group $ResourceGroup `
  --name $IdentityName `
  --query id --output tsv

$IdentityPrincipalId = az identity show `
  --resource-group $ResourceGroup `
  --name $IdentityName `
  --query principalId --output tsv

$IdentityClientId = az identity show `
  --resource-group $ResourceGroup `
  --name $IdentityName `
  --query clientId --output tsv
```

This identity is the bootstrap identity. Its steady-state purpose is to read the GitHub App material from Key Vault. Do not use it as the Terraform deployment identity.

## 5. Create private Key Vault access

```
az keyvault create `
  --resource-group $ResourceGroup `
  --name $KeyVaultName `
  --location $Location `
  --enable-rbac-authorization true `
  --public-network-access Disabled

$KeyVaultId = az keyvault show `
  --resource-group $ResourceGroup `
  --name $KeyVaultName `
  --query id --output tsv

az role assignment create `
  --assignee-object-id $IdentityPrincipalId `
  --assignee-principal-type ServicePrincipal `
  --role "Key Vault Secrets User" `
  --scope $KeyVaultId

az network private-dns zone create `
  --resource-group $ResourceGroup `
  --name "privatelink.vaultcore.azure.net"

az network private-dns link vnet create `
  --resource-group $ResourceGroup `
  --zone-name "privatelink.vaultcore.azure.net" `
  --name "link-$VnetName" `
  --virtual-network $VnetName `
  --registration-enabled false

az network private-endpoint create `
  --resource-group $ResourceGroup `
  --name "pep-$KeyVaultName" `
  --location $Location `
  --vnet-name $VnetName `
  --subnet $PeSubnetName `
  --private-connection-resource-id $KeyVaultId `
  --group-id vault `
  --connection-name "peconn-$KeyVaultName"

$PrivateEndpointId = az network private-endpoint show `
  --resource-group $ResourceGroup `
  --name "pep-$KeyVaultName" `
  --query id --output tsv

az network private-endpoint dns-zone-group create `
  --resource-group $ResourceGroup `
  --endpoint-name "pep-$KeyVaultName" `
  --name "default" `
  --private-dns-zone "privatelink.vaultcore.azure.net" `
  --zone-name "privatelink.vaultcore.azure.net"
```

|  |
| --- |
| **Important**  **Because public network access is disabled, secret creation must occur from an approved private network path or through an authorized automation process that can reach the vault privately. Adding a laptop public IP does not override PublicNetworkAccess=Disabled.** |

## 6. Create and install the GitHub App

In GitHub, create a GitHub App owned by the account or organization that owns the target repository. Disable webhooks unless another use case requires them. Grant only the permissions required by the KEDA scaler and runner registration APIs.

- Repository permission Actions: Read-only.
- Repository permission Administration: Read and write.
- Repository permission Metadata: Read-only.
- For organization-scoped runners, Self-hosted runners: Read and write at organization level. This guide uses repository scope.
- Install the App only on the repositories that are allowed to use this runner platform.

Record the **App ID** and **installation ID**. Generate a private key and protect the downloaded PEM file. The private key is the long-lived GitHub credential for this architecture.

## 7. Store GitHub App material in Key Vault

Run the following commands only from a trusted system that can reach the Key Vault private endpoint and has temporary secret-management permission. Use separate PEM and base64 forms because the KEDA trigger consumes PEM content while the runtime bootstrap can safely reconstruct the file from base64.

```
$GitHubAppId          = "<github-app-id>"
$GitHubInstallationId = "<github-installation-id>"
$GitHubPrivateKeyPath = "<local-path-to-private-key.pem>"

$GitHubPrivateKeyPem = Get-Content `
  -Path $GitHubPrivateKeyPath `
  -Raw

$GitHubPrivateKeyBase64 = [Convert]::ToBase64String(
  [System.IO.File]::ReadAllBytes($GitHubPrivateKeyPath)
)

az keyvault secret set --vault-name $KeyVaultName `
  --name "github-app-id" --value $GitHubAppId

az keyvault secret set --vault-name $KeyVaultName `
  --name "github-installation-id" --value $GitHubInstallationId

az keyvault secret set --vault-name $KeyVaultName `
  --name "github-app-private-key-pem" --value $GitHubPrivateKeyPem

az keyvault secret set --vault-name $KeyVaultName `
  --name "github-app-private-key-b64" --value $GitHubPrivateKeyBase64
```

**Validation:** List secret names and versions, but never print secret values in logs. Remove any temporary Secrets Officer assignment after the secrets have been written.

## 8. Create Log Analytics and the Container Apps environment

```
az monitor log-analytics workspace create `
  --resource-group $ResourceGroup `
  --workspace-name $LogWorkspace `
  --location $Location

$WorkspaceId = az monitor log-analytics workspace show `
  --resource-group $ResourceGroup `
  --workspace-name $LogWorkspace `
  --query customerId --output tsv

$WorkspaceKey = az monitor log-analytics workspace get-shared-keys `
  --resource-group $ResourceGroup `
  --workspace-name $LogWorkspace `
  --query primarySharedKey --output tsv

az containerapp env create `
  --resource-group $ResourceGroup `
  --name $EnvironmentName `
  --location $Location `
  --infrastructure-subnet-resource-id $AcaSubnetId `
  --logs-workspace-id $WorkspaceId `
  --logs-workspace-key $WorkspaceKey
```

**Validation:** Confirm that the environment provisioning state is Succeeded and that the infrastructure subnet matches the delegated ACA subnet.

## 9. Build the runtime bootstrap

The MCR image is prepared at runtime. Add fail-fast behavior and phase markers for installation, Key Vault, GitHub authentication and runner registration.

```
set -euo pipefail

log() { printf '%s %s\n' "$(date -u +%FT%TZ)" "$*"; }

log "Installing base packages"

tdnf install -y git tar gzip unzip ca-certificates curl openssl

log "Installing pinned Terraform and PowerShell versions"

# Download only approved versions. Validate checksums before installation.
# Install Terraform to /usr/local/bin and PowerShell to an approved path.

log "Retrieving GitHub App material from private Key Vault"

az login --identity --client-id "${UAMI_CLIENT_ID}" --allow-no-subscriptions >/dev/null
APP_ID=$(az keyvault secret show --vault-name "${KEY_VAULT_NAME}" --name github-app-id --query value -o tsv)
INSTALLATION_ID=$(az keyvault secret show --vault-name "${KEY_VAULT_NAME}" --name github-installation-id --query value -o tsv)
PRIVATE_KEY_B64=$(az keyvault secret show --vault-name "${KEY_VAULT_NAME}" --name github-app-private-key-b64 --query value -o tsv)

umask 077
printf '%s' "${PRIVATE_KEY_B64}" | base64 -d > /tmp/github-app-key.pem

log "Generating a short-lived GitHub App JWT"

# Create an RS256 JWT with iat slightly in the past and exp within GitHub limits.
# Do not echo the JWT or private key.

log "Requesting installation and registration tokens"

# POST /app/installations/${INSTALLATION_ID}/access_tokens using the JWT.
# POST /repos/${GITHUB_OWNER}/${GITHUB_REPO}/actions/runners/registration-token
# using the installation token.

log "Downloading and configuring the pinned GitHub Actions runner"

mkdir -p /actions-runner

cd /actions-runner

# Download the tested runner release and validate its checksum before extraction.

export RUNNER_ALLOW_RUNASROOT=1

./config.sh \

  --url "https://github.com/${GITHUB_OWNER}/${GITHUB_REPO}" \
  --token "${REGISTRATION_TOKEN}" \
  --name "aca-${CONTAINER_APP_JOB_EXECUTION_NAME:-runner}" \
  --labels "${RUNNER_LABEL}" \
  --ephemeral \
  --unattended \
  --disableupdate

rm -f /tmp/github-app-key.pem

unset PRIVATE_KEY_B64 JWT INSTALLATION_TOKEN REGISTRATION_TOKEN

log "Starting ephemeral runner"

exec ./run.sh
```

|  |
| --- |
| **Implementation note**  **The abbreviated sections above should be implemented as tested functions in the deployment repository. Keep the JWT and API response parsing logic in source control, but never include private-key material or emitted tokens. Pin release URLs and validate checksums.** |

## 10. Configure the ACA Event Job and KEDA scaler

Use an event-triggered job with minimum executions 0. The KEDA scale rule and runner registration must use the same repository and custom label. The following manifest fragment shows the required contract; property names can vary by the Container Apps API version, so generate the final resource through your approved Bicep, Terraform or ARM template and validate the deployed scale rule with Azure CLI.

```
triggerType: Event
eventTriggerConfig:
  replicaCompletionCount: 1
  parallelism: 1
  replicaRetryLimit: 0
  replicaTimeout: 3600
  scale:
    pollingInterval: 30
    minExecutions: 0
    maxExecutions: 3
    rules:
      - name: github-runner
        type: github-runner
        metadata:
          owner: "<github-owner>"
          runnerScope: repo
          repos: "<repository-name>"
          labels: "<custom-runner-label>"
          targetWorkflowQueueLength: "1"
          enableEtags: "true"
          applicationID: "<github-app-id>"
          installationID: "<github-installation-id>"
        authentication:
          appKey: "<ACA secret containing the GitHub App PEM>"

template:
  containers:
    - name: github-runner
      image: mcr.microsoft.com/deploymentenvironments/runners/core:<tested-tag-or-digest>
      resources:
        cpu: 1.0
        memory: 2Gi
      env:
        - name: GITHUB_OWNER
          value: "<github-owner>"
        - name: GITHUB_REPO
          value: "<repository-name>"
        - name: RUNNER_LABEL
          value: "<custom-runner-label>"
        - name: KEY_VAULT_NAME
          value: "<key-vault-name>"
        - name: UAMI_CLIENT_ID
          value: "<runtime-uami-client-id>"
```

The KEDA control plane needs the App ID, installation ID and PEM private key to inspect the queue. The runner container needs the App material independently to obtain its registration token. Treat these as two GitHub authentication consumers even when they use the same GitHub App.

**Validation:** Inspect properties.configuration.eventTriggerConfig.scale.rules and confirm owner, repository, scope, label, queue target, ETags, min/max executions and polling interval. Verify that the job has the UAMI attached.

## 11. Create the separate Azure deployment identity

This identity is used by workflow steps such as Terraform. It is intentionally separate from the runner UAMI.

```
$DeploymentAppName = "app-gh-aca-deployment"
$DeploymentClientId = az ad app create `
  --display-name $DeploymentAppName `
  --query appId --output tsv

az ad sp create --id $DeploymentClientId

$DeploymentSpObjectId = az ad sp show `
  --id $DeploymentClientId `
  --query id --output tsv

$DeploymentScope = az group show `
  --name $ResourceGroup `
  --query id --output tsv

az role assignment create `
  --assignee-object-id $DeploymentSpObjectId `
  --assignee-principal-type ServicePrincipal `
  --role Contributor `
  --scope $DeploymentScope
```

Create the federated credential. Bind the subject to the exact branch or GitHub environment allowed to deploy.

```
@"
{
  "name": "github-main",
  "issuer": "https://token.actions.githubusercontent.com",
  "subject": "repo:${GitHubOwner}/${GitHubRepo}:ref:refs/heads/main",
  "description": "GitHub Actions OIDC for the main branch",
  "audiences": ["api://AzureADTokenExchange"]
}

"@ | Set-Content -Path .\github-federated-credential.json

az ad app federated-credential create `
  --id $DeploymentClientId `
  --parameters .\github-federated-credential.json
```

|  |
| --- |
| **Least privilege**  **Contributor at resource-group scope is a practical implementation starting point, not a universal target. Replace it with a narrower built-in or custom role when the workflow’s required Azure operations are known. Do not grant this principal Key Vault secret-reading access unless the workflow genuinely needs it.** |

## 12. Configure GitHub Actions variables and workflow

Store the identifiers as GitHub repository or environment variables/secrets according to your governance model. There is no AZURE_CLIENT_SECRET.

- AZURE_CLIENT_ID = deployment application client ID
- AZURE_TENANT_ID = Microsoft Entra tenant ID
- AZURE_SUBSCRIPTION_ID = target Azure subscription ID

```
name: Terraform through ACA ephemeral runner

on:
  workflow_dispatch:

permissions:
  contents: read
  id-token: write

jobs:
  terraform:
    runs-on: [self-hosted, aca-linux]
    env:
      ARM_USE_OIDC: true
      ARM_CLIENT_ID: ${{ secrets.AZURE_CLIENT_ID }}
      ARM_TENANT_ID: ${{ secrets.AZURE_TENANT_ID }}
      ARM_SUBSCRIPTION_ID: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Sign in to Azure with OIDC
        uses: azure/login@v2
        with:
          client-id: ${{ secrets.AZURE_CLIENT_ID }}
          tenant-id: ${{ secrets.AZURE_TENANT_ID }}
          subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}

      - name: Verify toolchain
        shell: bash
        run: |
          git --version
          az version
          terraform version
          pwsh --version

      - name: Terraform init
        working-directory: terraform
        run: terraform init -input=false

      - name: Terraform plan
        working-directory: terraform
        run: terraform plan -input=false -out=tfplan

      - name: Terraform apply
        working-directory: terraform
        run: terraform apply -input=false -auto-approve tfplan
```

If production deployment requires approvals, target a protected GitHub environment and bind the federated credential subject to that environment instead of directly to a branch.

## 13. Validate the complete lifecycle

**Before triggering:** Confirm that current event-job executions are zero and no repository runner is permanently online.

**Queue detection:** Trigger the workflow and verify that it waits for the custom label rather than running on another self-hosted runner.

**KEDA scale-up:** Within the configured polling and platform startup interval, confirm that Container Apps creates an event-job execution.

**Private bootstrap:** Verify logs show managed identity login, private Key Vault retrieval and successful GitHub token exchange without printing credentials.

**Runner registration:** Confirm the workflow displays the ACA runner name and matching custom label.

**OIDC deployment:** Confirm azure/login succeeds without a client secret and Terraform operates only within the assigned Azure scope.

**Ephemeral cleanup:** After the workflow finishes, confirm the runner deregisters, the Container Apps execution completes and execution count returns to zero.

**Repeatability:**Run the workflow again. A new execution and new ephemeral runner should perform the second run.

```
az containerapp job execution list `
  --resource-group $ResourceGroup `
  --name $JobName `
  --query "[].{Name:name,Status:properties.status,Start:properties.startTime,End:properties.endTime}" `
  --output table

az containerapp job show `
  --resource-group $ResourceGroup `
  --name $JobName `
  --query "properties.configuration.eventTriggerConfig.scale.rules" `
  --output json
```

## 14. Measure cold-start latency

Measure cold-start stages separately to identify where queue-to-ready latency is introduced.

- Workflow queued → KEDA detects demand.
- KEDA detects demand → Container Apps execution starts.
- Execution starts → image pull completes.
- Image is ready → base package installation completes.
- Package installation → Terraform/PowerShell/runner installation completes.
- Tool installation → runner registration completes.
- Runner registration → workflow begins.

If runtime bootstrap repeatedly dominates the workflow duration, move the tested bootstrap into a versioned, scanned pre-baked image. That optimization changes the image supply chain and startup time, but it does not require changing the GitHub App, private Key Vault, KEDA, ephemeral-runner or OIDC trust model.

## 15. Production-readiness exit criteria

- The MCR image and downloaded tools are pinned to tested versions or digests, and checksums/signatures are validated.
- The GitHub App installation is restricted and has an owned private-key rotation and recovery procedure.
- The runtime UAMI has only Key Vault Secrets User at the intended vault scope.
- Key Vault public network access is disabled and private DNS is validated from the workload network.
- The deployment identity is separate, federated through OIDC and scoped to the smallest practical Azure boundary.
- Workflow, KEDA and runner registration labels are centrally parameterized and tested together.
- ACA logs are retained outside the ephemeral execution, with alerts for bootstrap, registration, OIDC and repeated execution failures.
- Maximum executions have been tested against GitHub API rate limits, Azure quotas and downstream deployment concurrency.
- Cold-start measurements have been compared with workflow duration and the image strategy has been selected consciously.

# What failed, and what those failures teach

**Assuming common tools existed** — Minimal base images may not include Git, PowerShell, Terraform, Python, jq or even familiar diagnostic commands. Verify the image rather than assuming.

**Root runner configuration** — Runner configuration can reject root execution unless the supported override is set. Treat this as an explicit base-image decision.

**Testing a private vault from a laptop** — A client IP allow-list does not override disabled public network access. Test the private path from the workload network.

**Storage account Terraform smoke test** — A resource can be created successfully through ARM while later provider data-plane checks fail because shared-key authentication is prohibited. Separate control-plane success from data-plane authorization.

**Trying to observe an ephemeral runner manually** — A short workflow may register and disappear too quickly for the runner page to be useful. Use workflow logs and Container Apps execution history as authoritative evidence.

**Conflating runner and deployment identity** — Successful runner registration does not prove Azure deployment authentication. Test GitHub OIDC and Azure RBAC independently.

# Observability and troubleshooting

| **Symptom** | **First checks** |
| --- | --- |
| **Workflow remains queued** | Check workflow labels, KEDA labels, owner, repo, runner scope, GitHub App permissions, installation ID and scaler logs. |
| **Job starts but no runner appears** | Check bootstrap logs, Key Vault DNS resolution, private endpoint connectivity, UAMI attachment, Key Vault RBAC and GitHub token exchange responses. |
| **Runner registers but workflow does not start** | Confirm the custom label and repository scope; verify no alternate self-hosted runner is matching the job. |
| **Azure login fails** | Check id-token: write, federated credential subject/audience/issuer, client ID, tenant ID and branch/environment conditions. |
| **Terraform authorization fails** | Inspect Azure role assignment principal, scope and propagation; distinguish ARM failures from resource data-plane failures. |
| **Cold start is too high** | Measure image pull, OS package installation, Terraform/PowerShell download and runner registration separately; consider a pre-baked image if startup dominates runtime. |

# Conclusion

Running GitHub Actions runners on Azure Container Apps is more than replacing a virtual machine with a container. The durable architecture comes from treating queue detection, runner registration, secret retrieval and Azure deployment as separate trust flows.

The resulting pattern is straightforward: KEDA starts an event job only when matching work exists; a private managed identity path retrieves GitHub App material; short-lived credentials register an ephemeral repository runner; GitHub OIDC provides a separate, secretless path to Azure; and the entire execution disappears after one workflow.

The MCR runtime-bootstrap strategy removes the need for a dedicated runner registry and custom image pipeline, but it increases cold-start latency and dependency on external download endpoints. That trade-off should be measured and revisited as usage grows. The architecture remains the same if a future requirement justifies moving the tested bootstrap into a pre-baked image.

# Sources and implementation references

- Microsoft Learn: Tutorial: Deploy self-hosted CI/CD runners and agents with Azure Container Apps jobs.
- KEDA documentation: GitHub Runner Scaler, including repository scope, labels, ETags and GitHub App authentication.
- GitHub REST API documentation: self-hosted runner registration-token endpoints and GitHub App installation authentication.
- Microsoft Learn: GitHub Actions authentication to Azure using OpenID Connect and federated identity credentials.
- Internal implementation record: Azure Container Apps GitHub Self-Hosted Runner Configuration & Learnings.
- Visuals in this document were generated with Microsoft Copilot.
