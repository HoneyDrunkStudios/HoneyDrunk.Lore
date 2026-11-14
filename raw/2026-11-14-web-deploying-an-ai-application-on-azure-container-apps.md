---
source: "https://techcommunity.microsoft.com/blog/azureinfrastructureblog/deploying-an-ai-application-on-azure-container-apps/4572612"
title: "Deploying an AI Application on Azure Container Apps"
author: "Devi Priya"
date_published: "2026-11-11"
date_clipped: "2026-11-14"
category: "Azure & Cloud"
source_type: "web"
---

# Deploying an AI Application on Azure Container Apps

AI applications often start as prototypes running locally on a developer’s machine. A Streamlit application may work perfectly in a development environment, but making it accessible to users introduces a different set of infrastructure and operational considerations.

From an infrastructure engineer’s perspective, the key questions are:

- How do we package the application?
- Where do we store and manage container images?
- How do we securely manage API keys and secrets?
- How do we expose the application to users?
- How do we scale it as usage increases?
- How do we automate deployments and future releases?
- How do we monitor and troubleshoot the application after deployment?

This article walks through the end-to-end deployment lifecycle of an AI application using **Azure Container Apps (ACA)**, focusing on infrastructure, security, deployment and operational responsibilities rather than application development.

## 1. Understanding the Architecture

Before starting the deployment, it is important to understand how the different components fit together.

At a high level, the deployment follows this flow:

**Application Source Code → Container Image → Azure Container Registry → Azure Container Apps → Azure OpenAI**

Additional Azure services provide identity, security, networking and operational capabilities around the application.

### High-level architecture

The responsibilities of the major components are:

| Azure component | Purpose |
| --- | --- |
| Azure Container Registry (ACR) | Stores and manages container images |
| Azure Container Apps Environment | Provides the managed environment for container applications |
| Azure Container Apps | Hosts and runs the application containers |
| Microsoft Entra ID | Provides identity and authentication |
| Managed Identity | Enables passwordless access to supported Azure services |
| Azure Key Vault | Securely stores application secrets |
| Azure Monitor | Provides monitoring and metrics |
| Log Analytics | Stores and supports analysis of application and platform logs |
| Azure OpenAI | Provides AI model inference capabilities |

The overall infrastructure lifecycle can be summarized as:

**Package → Build → Registry → Deploy → Secure → Scale → Automate → Monitor**

## 2. Start with a Clear Application Handoff

As an infrastructure engineer, I should not need to redesign the application before deploying it.

The application team should provide a deployment-ready application package with the following information:

- Application source code
- Dockerfile
- Dependency file, such as requirements.txt
- Application listening port
- Required environment variables
- External service endpoints
- Health-check requirements
- Expected CPU and memory requirements
- Authentication and integration requirements

For example, a Streamlit application commonly uses port 8501.

It is important to establish clear ownership between the teams.

**Application team responsibilities:**

- Application functionality and business logic
- Application dependencies
- Application-level configuration
- Application testing
- Application-level troubleshooting

**Infrastructure team responsibilities:**

- Container build infrastructure
- Container registry
- Azure resource provisioning
- Identity and access management
- Secrets management
- Networking and ingress
- Application deployment
- Scaling and monitoring
- CI/CD infrastructure

This separation prevents an infrastructure deployment activity from unintentionally becoming an application development task.

## 3. Containerize the Application

Before deploying an application to Azure Container Apps, we need to package it as a container image.

The Dockerfile defines how the application is packaged, including its base image, dependencies, working directory and startup command.

From an infrastructure perspective, the following items should be validated:

1. Is the expected base image being used?
2. Are application dependencies installed successfully?
3. Is the correct application port configured?
4. Does the application listen on 0.0.0.0 rather than only localhost?
5. Is the container configured to run as a non-root user wherever possible?
6. Are sensitive files and credentials excluded from the image?

For example, build and test the container locally:

**Build the image:**

docker build -t ai-app:v1 .

**Run the container:**

docker run -p 8501:8501 ai-app:v1

Podman can also be used in environments where Docker is unavailable or not permitted.

For a Streamlit application, ensure that the application startup configuration listens on all interfaces:

streamlit run app.py --server.address=0.0.0.0 --server.port=8501

Before introducing Azure into the troubleshooting process, validate that the container starts and the application is accessible locally.

The objective at this stage is simple:

**Can the application run successfully as a container?**

If not, resolve the container or application startup issue first. Introducing Azure Container Apps at this point adds another troubleshooting layer.

## 4. Store the Container Image in Azure Container Registry

Once the container image has been validated, it needs to be stored in a registry that Azure Container Apps can access.

For an Azure-native deployment, **Azure Container Registry (ACR)** is a suitable option.

The deployment flow now becomes:

**Application Code → Build Container → Test Container → Push Image to ACR → Deploy to Azure Container Apps**

One convenient option is to build the image directly using ACR.

az acr build \ --registry <ACR_NAME> \ --image ai-app:v1 \ .

This command builds the image from the current directory and pushes it to the specified Azure Container Registry.

For production deployments, avoid relying exclusively on a mutable tag such as latest.

Prefer traceable image versions:

ai-app:v1 ai-app:v2 ai-app:v3

For automated deployments, the image can also be tagged using a source commit ID or build number.

For example:

ai-app:build-1025

The complete image reference will look like:

<ACR_NAME>.azurecr.io/ai-app:v1

This makes it easier to identify which application version is deployed and simplifies rollback and troubleshooting.

**Infrastructure consideration:** Ensure that Azure Container Apps has the appropriate permissions to pull images from the private registry. Managed identity with the required ACR permissions can be used instead of maintaining registry credentials.

## 5. Deploy the Application to Azure Container Apps

Once the container image is available in ACR, the next step is deploying it to Azure Container Apps.

Two important concepts need to be understood.

### Azure Container Apps Environment

The Container Apps Environment provides the managed hosting boundary for container applications.

It provides shared capabilities such as networking, logging and integration with the underlying managed platform.

Multiple container apps can run within the same environment.

### Azure Container App

The Container App represents the actual application deployment.

It contains the configuration required to run the workload, including:

- Container image and version
- CPU and memory allocation
- Environment variables
- Ingress configuration
- Target application port
- Secrets
- Scaling configuration
- Health probes

The deployment structure can be visualized as:

For a Streamlit application, the Container Apps target port should match the port on which the application listens inside the container.

At this stage, the infrastructure team owns the hosting configuration while the application code remains within the application team's ownership.

## 6. Secure Application Secrets

This is one of the most important considerations when deploying AI applications.

AI applications frequently require credentials to access Azure OpenAI, external APIs or other services.

A simple rule should always be followed:

**Never store production API keys or credentials inside application source code or container images.**

Avoid hardcoded credentials:

API_KEY = "xxxxxxxx"

Production credentials should also not be committed to source repositories through .env files.

There are three important approaches to consider.

### Option 1: Managed Identity

Where the target Azure service supports Microsoft Entra authentication, use Managed Identity instead of storing application credentials.

For example, an application can authenticate to supported Azure services using its assigned identity.

### Option 2: Azure Key Vault

When an application requires a secret, such as an API key or connection string, store it centrally in Azure Key Vault.

Access should be controlled through Managed Identity and appropriate RBAC permissions.

### Option 3: Azure Container Apps Secrets

Azure Container Apps supports application-level secrets that can be referenced by container environment variables or mounted as files.

It can also reference secrets stored in Azure Key Vault using Managed Identity.

A recommended secret-management flow is:

The objective is to minimize the number of long-lived credentials that application and infrastructure teams need to manage.

## 7. Configure Managed Identity

Managed Identity helps reduce credential-management overhead and eliminates the need to maintain application credentials for supported Azure integrations.

For example, the access pattern can look like this:

Instead of storing a service principal password or application credential, the application uses its assigned identity to authenticate.

For Azure OpenAI, assign the appropriate role, such as **Cognitive Services OpenAI User**, when using Microsoft Entra authentication.

For Key Vault, assign **Key Vault Secrets User** when the application identity needs to retrieve secrets.

The exact role depends on the target service and the operations the application needs to perform.

From an infrastructure perspective, the principle is straightforward:

**Grant only the permissions required by the application.**

This follows the principle of least privilege and reduces unnecessary access across the Azure environment.

## 8. Configure Ingress and Application Connectivity

Once the application is deployed, users need a way to access it.

Azure Container Apps provides managed ingress capabilities, allowing applications to be exposed through HTTPS without manually managing an application gateway for every basic deployment scenario.

The infrastructure team needs to decide whether the application should be accessible through:

- External ingress – Accessible through a public application endpoint, subject to configured access controls.
- Internal ingress – Accessible within the Container Apps Environment and its supported internal networking configuration.

Before enabling ingress, validate the following:

- Is ingress enabled?
- Should the application be internal or external?
- Does the target port match the application listening port?
- Is HTTPS configured correctly?
- Does the application require additional authentication?
- Are network restrictions required?
- Are outbound connections to dependent services permitted?

A common deployment issue is a healthy container that is not reachable because the application listening port and the Container Apps target port do not match.

For connectivity troubleshooting, validate the path in order:

This helps determine whether the issue is related to ingress, networking, container configuration or the application itself.

## 9. Plan Scaling Before Production

Getting one container running is only the first step.

The next question is:

**What happens when multiple users start accessing the application?**

Azure Container Apps supports replica-based scaling using configurable scaling rules, including HTTP traffic and other supported KEDA-based triggers.

Infrastructure teams should consider:

- Minimum replicas
- Maximum replicas
- CPU allocation
- Memory allocation
- Scaling triggers
- Concurrent requests
- Expected user traffic
- Application startup time

For an interactive application, maintaining a minimum replica count may be appropriate when avoiding cold-start latency is important.

However, AI applications introduce another important consideration.

The container application is not necessarily the bottleneck.

Azure OpenAI has its own model deployment capacity, quota and throttling considerations.

Therefore:

**Increasing Container Apps replicas does not automatically increase Azure OpenAI model capacity.**

Scaling decisions should consider two separate layers.

**Application capacity:**

- Container Apps replicas
- CPU and memory
- Request concurrency
- Application-level performance

**AI model capacity:**

- Azure OpenAI deployment capacity
- Model quota
- Token throughput
- Request throttling
- Retry and backoff behavior

Load testing should be performed to establish appropriate limits rather than simply configuring a high maximum replica count.

## 10. Consider Stateful Application Behaviour

Interactive applications may maintain user or session state during execution.

This becomes particularly important when the application scales horizontally.

With a single replica, user interactions are handled by one running application instance.

With multiple replicas, requests may potentially be handled by different instances depending on the ingress and session configuration.

The infrastructure and application teams should establish one important detail:

**Is application state stored only inside the container, or is it persisted externally?**

If application or session state must survive container restarts, scaling events or deployments, an external persistence mechanism should be evaluated.

Container memory and local container storage should not be treated as durable application storage.

For Streamlit and similar interactive applications, the application team should also validate session handling and WebSocket connectivity under the expected ingress and scaling configuration.

This discussion should happen before increasing the application's replica count.

## 11. Validate the Manual Deployment Before Automating It

It can be tempting to start immediately with CI/CD pipelines.

However, from an infrastructure perspective, I prefer validating the complete deployment lifecycle manually before introducing automation.

The initial deployment should establish that the following process works:

Once this process is successful, the same steps can be automated through Azure DevOps or GitHub Actions.

The automated deployment lifecycle then becomes:

This approach makes troubleshooting easier because each deployment stage has already been validated independently.

The CI/CD pipeline simply automates a process that is known to work.

## 12. Authenticate the CI/CD Pipeline Securely

The deployment pipeline also needs access to Azure resources.

Pipeline authentication should receive the same security attention as application authentication.

Where supported, use **Workload Identity Federation (OIDC)** rather than maintaining long-lived client secrets in pipeline variables.

The authentication flow looks like this:

This avoids creating another permanent credential simply to automate deployment.

Pipeline permissions should also follow least privilege.

The deployment identity should have sufficient permissions to perform the required deployment operations without receiving unnecessary access to unrelated subscriptions or resources.

## 13. Manage Application Releases Using Revisions

Application deployment does not end with the first successful release.

There will be a version 2, version 3 and eventually another release that may need to be rolled back.

Azure Container Apps provides a revision-based deployment model.

A revision represents a version of the application configuration and container template.

For example:

Depending on the configured revision mode, the application can use single-revision or multiple-revision deployment.

Multiple-revision mode is particularly useful when implementing controlled traffic splitting, blue-green deployments or canary releases.

This allows infrastructure teams to validate a new application version before directing all production traffic to it.

Combined with traceable container image tags, revisions make it easier to answer a common operational question:

**Which application version is actually running?**

A rollback strategy should also be defined before production deployment.

## 14. Monitoring and Operational Visibility

A successful infrastructure deployment should not end with:

"The container is running."

Once users start accessing the application, the infrastructure team needs operational visibility.

At a minimum, consider monitoring the following:

| Monitoring area | What to validate |
| --- | --- |
| Container health | Replica readiness and container restarts |
| Application logs | Startup failures and application exceptions |
| HTTP metrics | Request volume, status codes and response latency |
| Resource utilization | CPU and memory consumption |
| Scaling | Replica count and scaling activity |
| Connectivity | Access to dependent Azure services |
| Azure OpenAI | Authentication errors, throttling and request failures |

Azure Monitor and Log Analytics can provide the operational visibility needed around the deployed workload.

A practical troubleshooting sequence is:

Following this sequence prevents infrastructure, application and downstream-service issues from being mixed together.

For production environments, configure diagnostic settings and appropriate alerts rather than relying only on manual log inspection.

## 15. Common Deployment Issues and Troubleshooting

Here are some common issues that infrastructure engineers may encounter during an Azure Container Apps deployment.

### Issue 1: Container Image Cannot Be Pulled

**Possible causes:**

- Incorrect registry configuration
- Incorrect image name or tag
- Missing registry permissions
- Managed Identity misconfiguration
- Private registry connectivity issues

**What to check:**

- Validate the complete image reference.
- Confirm the image exists in ACR.
- Check the Container App registry configuration.
- Verify the required registry pull permissions.

### Issue 2: Application Starts and Immediately Restarts

**Possible causes:**

- Missing environment variables
- Incorrect startup command
- Missing application dependencies
- Missing secrets
- Insufficient CPU or memory

**What to check:**

- Container console logs
- Container Apps system logs
- Application startup configuration
- Environment variable references
- Resource allocation

### Issue 3: Application Is Deployed but Not Reachable

**Possible causes:**

- Incorrect target port
- Application listening only on localhost
- Ingress disabled
- Incorrect internal or external ingress configuration
- Network restrictions

**What to check:**

- Container Apps ingress configuration
- Application listening port
- Application binding address
- Network connectivity
- HTTPS endpoint

### Issue 4: Azure OpenAI Returns Authentication Errors

**Possible causes:**

- Managed Identity not enabled
- Incorrect role assignment
- Incorrect endpoint configuration
- Unsupported authentication method
- Missing application configuration

**What to check:**

- Managed Identity assignment
- Azure RBAC permissions
- Azure OpenAI endpoint
- Application authentication configuration

### Issue 5: Azure OpenAI Returns HTTP 429 Responses

Do not immediately assume that the Container App needs more replicas.

Investigate:

- Azure OpenAI deployment capacity
- Model quota and throughput
- Request frequency
- Token consumption
- Retry and exponential backoff configuration

The important distinction is:

**Container scaling and AI model capacity are two different things.**

## Final Thoughts

Deploying an AI application is about much more than getting a container to start.

From an infrastructure perspective, the complete lifecycle involves packaging, registry management, identity, deployment, security, scaling, automation and monitoring.

Azure Container Apps provides a managed container platform that allows infrastructure teams to focus on these operational responsibilities without having to manage the underlying Kubernetes infrastructure.

For a Streamlit-based AI application, a practical implementation approach is to start small:

**Get one container running securely → Configure Managed Identity → Validate secrets and connectivity → Configure ingress → Test scaling → Automate deployment → Implement production monitoring.**

This incremental approach keeps application and infrastructure responsibilities clear and makes troubleshooting considerably easier.

The goal is not simply to get an AI application running.

The goal is to make the deployment:

**Secure. Repeatable. Observable. Scalable. Production-ready.**
