---
source: "https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-october-2026"
title: "Everything released in October 2026 for Azure Developer CLI"
author: "Kristen Womack"
date_published: "2026-10-30"
date_clipped: "2026-10-31"
category: "Azure & Cloud"
source_type: "rss"
---

# Everything released in October 2026 for Azure Developer CLI

Welcome to the October 2026 edition of the Azure Developer CLI (`azd`) release blog. This post covers releases [1.35.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.35.0), [1.35.1](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.35.1), [1.36.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.36.0), [1.37.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.37.0), [1.37.1](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.37.1), and [1.37.2](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.37.2). Have a question or feedback? Post it in the [Azure Developer CLI discussions on GitHub](https://github.com/Azure/azure-dev/discussions/).

**Highlights:**

- Preview service deployment operations with `azd deploy --preview` before making changes.
- Deploy container images to Azure Container Apps express environments with the existing `containerapp` host.
- Remove stored environment values with the beta `azd env unset` command.
- Generate pipelines that install extensions required by extension-defined infrastructure providers.
- Build extensions with stable deployment-preview, usage telemetry, and current Azure principal contracts.

## New features

### 🚀 Deployment previews and Container Apps express

To inspect deployment operations without deploying, run:

```
azd deploy --preview
```

- Preview deployment operations for App Service, Container Apps, Functions, Static Web Apps, Azure Kubernetes Service, and AI endpoints. Results describe the resolved Azure target, with structured target and host details available in JavaScript Object Notation (JSON) output. [[#10204]](https://github.com/Azure/azure-dev/pull/10204)
- Deploy images to Azure Container Apps express environments using `host: containerapp`. `azd` detects the environment’s express mode and updates the image without setting a custom revision suffix or traffic weights. Use the image-based deployment strategy; express doesn’t support multiple revisions or traffic splitting. [[#10223]](https://github.com/Azure/azure-dev/pull/10223)

### ⚙️ Environment management and pipelines

- Remove one or more exact, case-sensitive stored environment keys with the beta `azd env unset` command. It asks for confirmation, protects `AZURE_ENV_NAME`, and leaves other environments and process variables unchanged. Non-interactive removal requires `--force`. [[#10362]](https://github.com/Azure/azure-dev/pull/10362)
- Use extension-defined infrastructure providers with `azd pipeline config`. Generated GitHub Actions and Azure Pipelines definitions install the required extensions. [[#9878]](https://github.com/Azure/azure-dev/pull/9878)

For example, to remove two stored values from your development environment:

```
azd env unset OLD_API_URL OLD_FEATURE_FLAG --environment dev
```

### 🔌 Extension APIs and command behavior

Extensions add commands and integrate with `azd` project and deployment workflows. This month’s updates give extension authors stable contracts and more control over command output.

- Build read-only service-target deployment previews with the extension software development kit (SDK). The contracts and SDK application programming interfaces (APIs) graduate to stable v1 in 1.37.0, while existing beta routes and source remain compatible. Contributed by [@Siglud](https://github.com/Siglud) for the initial SDK support. [[#10055]](https://github.com/Azure/azure-dev/pull/10055) [[#10628]](https://github.com/Azure/azure-dev/pull/10628)
- Use stable v1 APIs for extension usage telemetry and current Azure principal lookup. Existing beta routes remain available. [[#10439]](https://github.com/Azure/azure-dev/pull/10439)
- Discover project-service save capabilities and confirm completed service additions with typed acknowledgments through preview APIs. [[#10334]](https://github.com/Azure/azure-dev/pull/10334)
- Return structured informational and warning messages from extension service `predeploy` and `postdeploy` handlers. `azd deploy` and `azd up` include these messages in terminal and JSON results, including failed deployments. This API remains beta-only. [[#9950]](https://github.com/Azure/azure-dev/pull/9950)
- Contribute follow-up guidance to successful core command completion messages through a preview API. Guidance appears after handlers finish and doesn’t change JSON output. [[#9794]](https://github.com/Azure/azure-dev/pull/9794)
- Mark individual extension commands with `launch.noAzdEnvironment` to skip loading the selected `azd` environment and resolving its Key Vault references. Inherited process variables and explicit environment API calls remain unchanged. [[#10479]](https://github.com/Azure/azure-dev/pull/10479)

## Breaking changes

- **Environment and state Go API migration:** Exported environment and state path APIs now return errors. Update custom implementations and mocks, check and propagate errors before using returned paths, and pass an `*azdcontext.AzdContext` to `state.NewStateCacheManager` instead of an environment-directory string. Construct the context from the project directory, not its `.azure` directory. These changes make path-validation failures explicit. See the [environment-state API migration guide](https://github.com/Azure/azure-dev/blob/main/cli/azd/docs/environment-state-api-migration.md) for the affected signatures.

## 🪲 Bugs fixed

### Extension installation and execution

- Restore the previously installed extension’s files and metadata when an upgrade fails or is cancelled. [[#10315]](https://github.com/Azure/azure-dev/pull/10315)
- Propagate Ctrl+C cancellation across extension processes, remote procedure calls, and extension-started workflows. Report cancellations and timeouts distinctly instead of as generic failures. [[#10353]](https://github.com/Azure/azure-dev/pull/10353)
- Return an error when a non-interactive extension install can’t apply an explicit version pin without confirmation, and keep file-based extension sources available after changing working directories. [[#10181]](https://github.com/Azure/azure-dev/pull/10181)
- Improve selected-file validation in the Foundry SDK. [[#10181]](https://github.com/Azure/azure-dev/pull/10181)
- Preserve parent and sibling registrations when creating nested dependency injection scopes, and respect the selected output format in extension installation diagnostics. [[#10254]](https://github.com/Azure/azure-dev/pull/10254)
- Preserve process exit codes for directly invoked extension commands. [[#10282]](https://github.com/Azure/azure-dev/pull/10282)
- Avoid repeating unchanged progress lines during extension installs and updates when output isn’t a terminal. [[#10280]](https://github.com/Azure/azure-dev/pull/10280)
- Open the correct documentation for extension namespace `--docs` requests. [[#10304]](https://github.com/Azure/azure-dev/pull/10304)
- Resolve extension command metadata, canonical paths, and flags correctly when commands use parent or child aliases and global flags. [[#10479]](https://github.com/Azure/azure-dev/pull/10479)
- Keep extension selection prompts on stderr so terminal output doesn’t mix into JSON results. [[#10479]](https://github.com/Azure/azure-dev/pull/10479)

### Project configuration and environments

- Preserve unrelated `azure.yaml` settings during extension service edits, including empty mappings, large integers, and environment templates. [[#10479]](https://github.com/Azure/azure-dev/pull/10479)
- Restore in-memory project configuration when an extension service addition fails. [[#10334]](https://github.com/Azure/azure-dev/pull/10334)
- Restore environment access after project initialization when an earlier lookup found no project. [[#10294]](https://github.com/Azure/azure-dev/pull/10294)
- Complete environment configuration updates reliably and fix a race in task-list rendering. [[#10191]](https://github.com/Azure/azure-dev/pull/10191)
- Clear stale in-memory authentication entries during re-login cache cleanup. [[#10317]](https://github.com/Azure/azure-dev/pull/10317)

### Deployment and developer workflows

- Make provisioning warnings clearer about which scope permissions were checked. Critical warnings default to No and require explicit confirmation; `--no-prompt` or unanswered critical confirmations return an error. Cancellation skips post-provision hooks without hiding failures in parallel layers. Contributed by [@hyoshis](https://github.com/hyoshis). [[#10396]](https://github.com/Azure/azure-dev/pull/10396)
- Validate unresolved or empty environment variables embedded in Deployment Stacks deny-list values before sending the configuration to Azure when the `deployment.stacks` alpha feature is enabled. Contributed by [@saikeerthan-14](https://github.com/saikeerthan-14). [[#10516]](https://github.com/Azure/azure-dev/pull/10516)
- Show deployment timeouts clearly instead of displaying them as skipped steps or obscuring them with underlying errors. [[#10157]](https://github.com/Azure/azure-dev/pull/10157)
- Handle cancelled deployment progress updates and closed progress channels without hanging or stopping unexpectedly. [[#10304]](https://github.com/Azure/azure-dev/pull/10304)
- Accept inline shell expressions with operators, assignments, or expansions without spaces in `azd exec --shell`, and stop mistaking inline commands with path arguments for missing script files. Contributed by [@jongio](https://github.com/jongio). [[#10376]](https://github.com/Azure/azure-dev/pull/10376) [[#10375]](https://github.com/Azure/azure-dev/pull/10375)
- Retain file changes and remove stale entries during file-watch registration and shutdown. [[#10300]](https://github.com/Azure/azure-dev/pull/10300)
- Stop showing a question-mark hint when prompt hint keys are disabled. [[#10445]](https://github.com/Azure/azure-dev/pull/10445)

## Other changes

- Update Go dependencies across core and first-party extensions, including gRPC v1.84.0 and OpenTelemetry v1.47.0. [[#10572]](https://github.com/Azure/azure-dev/pull/10572)
- Update the bundled GitHub CLI to v2.102.0. [[#10456]](https://github.com/Azure/azure-dev/pull/10456)
- Update Microsoft Authentication Library for Go to v1.10.1. [[#10251]](https://github.com/Azure/azure-dev/pull/10251)
- Update the bundled Bicep CLI to v0.48.1. [[#10322]](https://github.com/Azure/azure-dev/pull/10322)
- This release includes security improvements. Users are encouraged to upgrade.

## New docs

New and updated `azd` documentation on Microsoft Learn:

- **[Deploy to Azure Container Apps using the Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/container-apps-workflows)** (September 30)—Configure image-based deployments to Container Apps express, including the environment mode, service tags, and supported deployment strategy.
- **[Azure Developer CLI reference](https://learn.microsoft.com/azure/developer/azure-developer-cli/reference)** (October 27)—Updated command reference includes `azd deploy --preview`, extension management options, and a clarification that non-interactive `azd env unset` removal requires `--force`.

## New templates

Community-authored templates help you get started faster, solve real-world scenarios, and showcase best practices for deploying solutions with Azure Developer CLI.

- **[Text Semantic Search using embedding models in Microsoft Foundry and Azure PostgreSQL](https://github.com/massimobonanni/DBSemanticSearch)** by [Massimo Bonanni](https://info.massimobonanni.it/): A .NET application that generates text embeddings with Microsoft Foundry, stores them in Azure Database for PostgreSQL with pgvector, and searches for semantically similar text. It provisions a Blazor Server frontend and Azure Functions API using Bicep.
- **[LangChain AG-UI Chat with Angular, Hono, and LangGraph on Azure Container Apps](https://github.com/JayChase/langchain-ag-ui-angular)** by [Jay Chase](https://github.com/JayChase): A streaming AI chat application with generative UI tool components, connecting an Angular (@copilotkit/angular) frontend to a LangGraph Server via the AG-UI protocol and @ag-ui/langgraph on a Hono API. Demonstrates a fully self-hosted deployment on Azure Container Apps using official AG-UI and CopilotKit packages.

The Azure Developer CLI template gallery continues to grow with contributions from the community. Thank you!

## 🙋‍♀️ New to azd?

If you’re new to the Azure Developer CLI, `azd` is an open-source command-line tool that helps you get your application from your local development environment to Azure faster. It provides developer-friendly commands that map to key stages in your workflow, whether you’re working in the terminal, your editor, or continuous integration and delivery.

- [Install azd](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)
- **Explore templates:** Browse the [Awesome azd template gallery](https://azure.github.io/awesome-azd/) and [AI App Templates](https://aka.ms/ai-gallery)
- **Learn more:** Visit the [official documentation](https://learn.microsoft.com/azure/developer/azure-developer-cli/) and [troubleshooting guide](https://learn.microsoft.com/azure/developer/azure-developer-cli/troubleshoot)
- **Get help:** Visit the [GitHub repository](https://github.com/Azure/azure-dev) to file issues or start discussions
