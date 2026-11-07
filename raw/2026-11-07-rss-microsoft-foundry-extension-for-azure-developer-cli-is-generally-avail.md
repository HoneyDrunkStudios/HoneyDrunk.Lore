---
"source": "https://devblogs.microsoft.com/azure-sdk/microsoft-foundry-azure-developer-cli-ga/"
"title": "Microsoft Foundry extension for Azure Developer CLI is generally available"
"author": "John Miller"
"date_published": "2026-11-05"
"date_clipped": "2026-11-07"
"category": "Azure & Cloud"
"source_type": "rss"
---

# Microsoft Foundry extension for Azure Developer CLI is generally available

Source: https://devblogs.microsoft.com/azure-sdk/microsoft-foundry-azure-developer-cli-ga/

Capture note: Code examples retain the source page's formatting, including blank lines in continued shell commands. Review before reuse.

Today, the Microsoft Foundry extension bundle (`microsoft.foundry`) for Azure Developer CLI (`azd`) reaches version 1.0 and is generally available. `azd` provisions Azure resources and deploys application code; the Foundry extension adds agent setup and local testing. Agent and deployment configuration stays alongside your code in `azure.yaml`.

## What this adds to your development workflow

- Review agent and deployment changes together.
- Inspect local requests and responses in Agent Inspector while changing prompts, tools, or code.
- Use the same deployment configuration locally and in CI/CD.

## Create and run a hosted agent

In Foundry, a [hosted agent](https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agents) runs your own agent code on managed compute. You choose the framework and orchestration logic; Foundry manages the runtime.

Install [Azure Developer CLI](https://aka.ms/azd) 1.37.0 or later, or upgrade an existing installation with `azd update`. Install a current [uv](https://docs.astral.sh/uv/getting-started/installation/) release (`uv self update` for standalone installations). The sample uses Python 3.13 or later.

You’ll need an Azure subscription, [Foundry permissions](https://learn.microsoft.com/azure/foundry/agents/concepts/hosted-agent-permissions), and model quota in your selected region. Provisioned resources and model usage incur Azure charges.

Sign in and install the Foundry bundle:

```
azd auth login

azd ext install microsoft.foundry
```

If Azure CLI (`az`) is already signed in, use the same account and tenant as `azd`. The sample’s [DefaultAzureCredential](https://learn.microsoft.com/azure/developer/python/sdk/authentication/credential-chains#defaultazurecredential-overview) can use that login for local model calls.

### 1. Initialize the project

Initialize the [basic Python Agent Framework sample](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents/agent-framework/responses/01-basic) in an empty directory. Choose a new or existing Foundry project during setup. To reuse an existing model deployment, add `--model-deployment <existing-deployment-name>` to the command:

```
azd ai agent init \

  --template https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/agent-framework/responses/01-basic/azure.yaml \

  --deploy-mode code \

  --src .
```

![Screenshot of azd initialization offering an existing Foundry project or creating a new one.](https://devblogs.microsoft.com/azure-sdk/wp-content/uploads/sites/58/2026/10/11-05-foundry-project-selection.webp)

`--src .` initializes the project in the current directory.

### 2. Review `azure.yaml`

`azure.yaml` describes the agent and the Azure resources it needs. Keep it with your code so deployment changes are reviewed in the same pull request. Teammates and CI/CD reuse that definition, with each `azd` environment supplying its target subscription, region, and resource settings.

This excerpt from the [sample configuration](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/agent-framework/responses/01-basic/azure.yaml) shows the model deployment, agent source and runtime, compute allocation, and dependency on the Foundry project:

```
services:

  ai-project:

    host: azure.ai.project

    deployments:

      - name: gpt-5.4-mini

        model:

          format: OpenAI

          name: gpt-5.4-mini

          version: '2026-03-17'

        sku:

          name: GlobalStandard

          capacity: 10

  agent-framework-agent-basic-responses:

    host: azure.ai.agent

    project: src/agent-framework-agent-basic-responses

    codeConfiguration:

      runtime: python_3_13

      entryPoint: main.py

    uses:

      - ai-project

    container:

      resources:

        cpu: '0.5'

        memory: 1Gi
```

Start without writing infrastructure files. To customize provisioning, [eject editable Bicep or Terraform files](https://learn.microsoft.com/azure/foundry/agents/concepts/cli-infrastructure), commit them with your code, and keep using `azd provision`.

### 3. Provision Azure resources

`azd provision` creates the declared resources, including missing model deployments in a reused project. Follow the model-configuration prompts and choose an available online deployment type, such as Global Standard or Data Zone Standard. Options and quota vary by subscription and region; [compare deployment types](https://learn.microsoft.com/azure/foundry/foundry-models/concepts/deployment-types) before choosing.

```
azd provision
```

### 4. Test locally

```
azd ai agent run
```

The command installs dependencies and opens Agent Inspector for the local agent. Model calls still use your Azure deployment.

![Screenshot of Agent Inspector showing a local haiku response and a completed model call.](https://devblogs.microsoft.com/azure-sdk/wp-content/uploads/sites/58/2026/10/11-05-foundry-agent-inspector-local-response.webp)

Leave it running and invoke it from a second terminal in the project directory:

```
azd ai agent invoke --local "Write a haiku about deploying cloud applications."
```

### 5. Deploy to Foundry

```
azd deploy
```

`azd` uploads your source to Foundry for a remote build; no local container build is required. Deployment output includes the playground and endpoint links.

Invoke the deployed agent:

```
azd ai agent invoke "Write a haiku about deploying cloud applications."
```

![Screenshot of azd invoking the deployed Foundry agent and returning a haiku response.](https://devblogs.microsoft.com/azure-sdk/wp-content/uploads/sites/58/2026/10/11-05-foundry-agent-remote-invoke.webp)

Use `azd deploy --preview` to review hosted-agent configuration changes, `azd ai agent monitor --follow` to stream logs, and `azd ai agent doctor` to diagnose setup or permission issues.

## Create the project with a coding agent

The [Microsoft Foundry Skill](https://learn.microsoft.com/azure/foundry/how-to/develop/use-microsoft-foundry-skill) gives coding agents such as GitHub Copilot and Claude Code Foundry-specific workflows for project setup and local testing. Install it for your host, open an empty folder, and ask:

```
Use the Microsoft Foundry Skill to scaffold the basic Python Agent Framework

Responses API sample with code deployment. Configure azure.yaml and help me

choose the Foundry project, subscription, region, and model deployment.

Show me the plan and wait for approval before creating Azure resources.

Run and test the agent locally, then stop.
```

Review the generated project, then continue with the deployment steps above.

## Measure and improve quality

Install the Evaluations extension and generate test data and a grading rubric for the deployed agent:

```
azd ext install azure.ai.evaluations

azd ai eval generate
```

Describe what the agent should do, and choose **Dataset and evaluator** and **Turn**. Review the generated dataset and rubric, then configure the evaluation:

```
azd ai eval init --name quality
```

Select the generated dataset and rubric, and confirm the judge model.

Review `evals/azure.eval.yaml` and its service reference in `azure.yaml`. Register the evaluation assets and run the evaluation:

```
azd up

azd ai eval run start --eval quality
```

Keep the configuration and test assets with your code to compare changes and reuse checks in CI/CD. `azd ai agent optimize` can reuse a configured evaluation as its baseline; review candidates before explicitly deploying one.

## Automate deployment with CI/CD

`azd up` packages, provisions, and deploys the project. Run it once before configuring a GitHub Actions or Azure DevOps pipeline:

```
azd up

azd pipeline config
```

`azd pipeline config` sets up authentication, repository settings, and a workflow to review and commit.

Retain the generated checkout, sign-in, and environment settings. This GitHub Actions excerpt shows only installation and deployment; sign-in must precede deployment:

```
- name: Install azd

  uses: Azure/setup-azd@v2

  with:

    version: 1.37.0

- name: Install Foundry extensions

  run: azd ext install microsoft.foundry azure.ai.evaluations

- name: Provision and deploy

  run: azd up --no-prompt
```

Grant the pipeline identity the required Azure permissions, use a separate `azd` environment per stage, and keep runtime credentials in pipeline secrets.

For CI evaluation, commit `evals/azure.eval.yaml` and its required nonsecret assets, and grant the pipeline access to referenced datasets and evaluators. Run `azd ai eval run start --eval quality --no-prompt` after deployment. See the [CI/CD guide](https://learn.microsoft.com/azure/foundry/agents/how-to/set-up-ci-cd-cli) for complete workflows and threshold-based quality gates.

## Clean up a demo environment

If you created a new Foundry project for this demo, `azd down` deletes its resource group and everything in it. Review the deletion before confirming:

```
azd down
```

For a reused project, `azd down` leaves the project and its resources, including the hosted agent, in place. Follow the [quickstart’s cleanup guidance](https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=azd#clean-up-resources) to remove unwanted resources separately.

## Get started

Follow the [hosted-agent quickstart](https://learn.microsoft.com/azure/foundry/agents/quickstarts/quickstart-hosted-agent?pivots=azd) for the complete walkthrough. Update an existing installation with `azd ext upgrade microsoft.foundry`.

Share feedback and requests in the [Azure Developer CLI repository](https://github.com/Azure/azure-dev).
