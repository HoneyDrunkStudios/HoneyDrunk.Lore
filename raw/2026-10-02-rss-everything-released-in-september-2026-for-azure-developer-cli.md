---
source: "https://devblogs.microsoft.com/azure-sdk/azure-developer-cli-azd-september-2026/"
title: "Everything released in September 2026 for Azure Developer CLI"
author: "Kristen Womack"
date_published: "2026-09-30"
date_clipped: "2026-10-02"
category: "Azure & Cloud"
source_type: "rss"
---

# Everything released in September 2026 for Azure Developer CLI

Welcome to the September 2026 edition of the Azure Developer CLI (`azd`

) release blog. This post covers releases [1.33.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.33.0), [1.34.0](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.34.0), [1.34.1](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.34.1), and [1.34.2](https://github.com/Azure/azure-dev/releases/tag/azure-dev-cli_1.34.2). Have a question or feedback? Post it in the [Azure Developer CLI discussions on GitHub](https://github.com/Azure/azure-dev/discussions/).

**Highlights:**

- Dependency-aware extension uninstall protects required dependencies and helps remove packages that are no longer needed.
- Top-level infrastructure and service layers make complex
`azure.yaml`

projects easier to organize. - Per-phase concurrency limits give you control over parallel package, provision, publish, and deploy operations.
- Versioned extension contracts provide stable and preview application programming interface (API) surfaces while preserving compatibility with existing extensions.
- External authentication hosts can connect through Unix domain sockets and Windows named pipes.

## New features

### 🔌 Extension management

`azd extension uninstall`

now distinguishes extensions you installed directly from dependencies that were installed automatically. It blocks removal when another extension depends on the selected extension and offers to remove dependencies that are no longer needed. Use`--force`

to remove an extension with dependents or`--no-dependencies`

to keep unused dependencies.[[#9866]](https://github.com/Azure/azure-dev/pull/9866)- Stable and preview versioned gRPC contracts let extension authors choose the appropriate API surface while preserving compatibility with existing extensions.
[[#9747]](https://github.com/Azure/azure-dev/pull/9747) - The preview extension contract adds
`Account.GetCurrentPrincipal`

, which lets extensions read the signed-in identity’s object ID and principal type without decoding access tokens.[[#10049]](https://github.com/Azure/azure-dev/pull/10049)

### ⚙️ Project configuration and deployment

- Configure top-level infrastructure and service layers in
`azure.yaml`

to organize provisioning and deployment across complex projects.[[#9913]](https://github.com/Azure/azure-dev/pull/9913) - Set per-phase concurrency limits for package, provision, publish, and deploy operations to control how much work runs in parallel.
[[#9752]](https://github.com/Azure/azure-dev/pull/9752) - Preserve environment templates when project mappings are saved and restored.
[[#9897]](https://github.com/Azure/azure-dev/pull/9897)

### 🔐 Authentication and template safety

- External authentication hosts can connect through Unix domain sockets or Windows named pipes by configuring
`AZD_AUTH_ENDPOINT`

.[[#8371]](https://github.com/Azure/azure-dev/pull/8371) `azd init --template`

now warns when a template repository is archived, so you can cancel before cloning an unmaintained project.[[#9541]](https://github.com/Azure/azure-dev/pull/9541)

## 🪲 Bugs fixed

### Extensions and authentication

- Fix extension install, update, init, and automatic-install flows to select releases compatible with the running
`azd`

version.[[#9733]](https://github.com/Azure/azure-dev/pull/9733) - Fix intermittent extension startup timeouts caused by concurrent initialization.
[[#9987]](https://github.com/Azure/azure-dev/pull/9987) - Follow redirects when installing extension bundles and warn when an HTTPS download redirects to HTTP.
[[#9785]](https://github.com/Azure/azure-dev/pull/9785) - Correct login details for system-assigned managed identities.
[[#10049]](https://github.com/Azure/azure-dev/pull/10049)

### Provisioning and deployment

- Show project-level
`predeploy`

and`postdeploy`

hook output during`azd up`

. Contributed by[@jongio](https://github.com/jongio).[[#10033]](https://github.com/Azure/azure-dev/pull/10033) - Recover Azure Container Registry (ACR) log streaming when a remote build replaces or truncates its log.
[[#9957]](https://github.com/Azure/azure-dev/pull/9957) - Fall back to a local container build when ACR rejects remote task scheduling.
[[#9939]](https://github.com/Azure/azure-dev/pull/9939) - Surface stable, structured diagnostics for ACR remote-build failures while preserving build logs.
[[#9737]](https://github.com/Azure/azure-dev/pull/9737) - Honor service
`condition`

values before initializing disabled services or checking them before a command runs.[[#9678]](https://github.com/Azure/azure-dev/pull/9678) - Show resource-specific quota guidance instead of Foundry recovery steps for unrelated Azure resource providers.
[[#9729]](https://github.com/Azure/azure-dev/pull/9729) - Isolate intermediate artifacts when publishing .NET services concurrently on supported .NET SDKs.
[[#9775]](https://github.com/Azure/azure-dev/pull/9775)

### Interactive and agent environments

- Keep interactive terminals interactive when they inherit stale coding-agent markers, and improve bounded agent detection.
[[#9818]](https://github.com/Azure/azure-dev/pull/9818) - Ignore empty AI coding-agent markers, prioritize active Codex and Cursor sessions, and avoid classifying the Cursor desktop app as an agent.
[[#9764]](https://github.com/Azure/azure-dev/pull/9764) - Return a clear validation error instead of stopping unexpectedly when
`azure.yaml`

contains invalid YAML. Contributed by[@Siglud](https://github.com/Siglud).[[#10038]](https://github.com/Azure/azure-dev/pull/10038) - Shut down cleanly when telemetry is disabled.
[[#10010]](https://github.com/Azure/azure-dev/pull/10010)

## Other changes

`azd extension show`

now displays compatibility, ownership, dependencies, and installed dependents. JSON output uses camel-case keys and omits empty fields.[[#9866]](https://github.com/Azure/azure-dev/pull/9866)- The agentic
`azd init`

flow reports AI credits instead of premium requests.[[#10052]](https://github.com/Azure/azure-dev/pull/10052) - The
`execution.environment`

telemetry field reports`agency`

when`azd`

runs in an Agency session.[[#10061]](https://github.com/Azure/azure-dev/pull/10061) - Published Homebrew casks now use Homebrew’s declarative
`postflight_steps`

.[[#10095]](https://github.com/Azure/azure-dev/pull/10095) - Update the bundled Bicep CLI to v0.47.16.
[[#9909]](https://github.com/Azure/azure-dev/pull/9909) - Update the bundled GitHub CLI to v2.101.0.
[[#10132]](https://github.com/Azure/azure-dev/pull/10132) - Stop exporting ambient OpenTelemetry resource attributes while preserving declared telemetry fields.
[[#9911]](https://github.com/Azure/azure-dev/pull/9911) - This release includes security improvements. Users are encouraged to upgrade.

## New docs

New and updated `azd`

documentation on Microsoft Learn:

(September 16)—Follow the template development workflow and choose whether to start with an existing template, use an AI coding assistant, or author files directly.[Build Azure Developer CLI templates](https://learn.microsoft.com/azure/developer/azure-developer-cli/build-templates-overview)(September 16)—Learn how[Explore and edit Azure Developer CLI template files](https://learn.microsoft.com/azure/developer/azure-developer-cli/explore-edit-templates)`azure.yaml`

, source code, infrastructure files, and environment configuration work together in a template.(September 16)—Add an Azure service to an existing template with a Bicep module and export its outputs as[Extend an Azure Developer CLI template](https://learn.microsoft.com/azure/developer/azure-developer-cli/extend-template)`azd`

environment values.(September 16)—Create a template with GitHub Copilot, another AI coding assistant, or direct file authoring, then provision and deploy it.[Start with a new Azure Developer CLI template](https://learn.microsoft.com/azure/developer/azure-developer-cli/start-with-new-template)(September 15)—Compare container hosting targets, image build locations, registries, and[Choose a container build and deployment workflow](https://learn.microsoft.com/azure/developer/azure-developer-cli/container-build-deploy-options)`azd`

publish and deployment commands.

## New templates

Community-authored templates help you get started faster, solve real-world scenarios, and showcase best practices for deploying solutions with Azure Developer CLI.

**LangGraph hosted-agent templates**by[Microsoft Foundry Team](https://github.com/microsoft-foundry):: A multi-turn LangGraph chat agent with local time and calculator tools, hosted on Foundry over the Responses protocol with server-side conversation state.[Basic Chat (Responses, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/responses/01-langgraph-chat/azure.yaml): A LangGraph deep research agent that plans work, delegates focused research, uses managed web search, consolidates citations, and persists durable checkpoints on Foundry.[Deep Agents (Responses, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/responses/11-deep-agents/azure.yaml): A LangGraph ReAct agent using a Foundry Toolbox for managed web search and Microsoft Learn MCP tools, including OAuth consent handling and schema sanitization.[Foundry Toolbox (Responses, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/responses/02-langgraph-toolbox/azure.yaml): A LangGraph ReAct agent with a Foundry Toolbox that provisions WorkIQ Mail, WorkIQ Calendar, and GitHub MCP integrations using user identity and managed OAuth.[Foundry Toolbox with User Identity (Responses, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/responses/03-langgraph-toolbox-user-identity/azure.yaml): A LangGraph StateGraph workflow that sequentially chains specialized slogan writer, legal reviewer, and formatter LLM nodes while returning only the final formatted result.[Multi-Agent Workflows (Responses, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/responses/05-workflows/azure.yaml): A LangGraph agent that works with uploaded and bundled files using local filesystem tools plus a Foundry Toolbox code interpreter for managed calculations and data analysis.[File Handling (Responses, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/responses/06-files/azure.yaml): A LangGraph proposal workflow that pauses for human review and supports approval, revision with feedback, or rejection through Responses protocol approval and function-call channels.[Human-in-the-Loop (Responses, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/responses/07-human-in-the-loop/azure.yaml): An instrumented LangGraph agent that uses automatic GenAI OpenTelemetry tracing to emit node, model, and tool spans, metrics, and logs to Application Insights.[Observability (Responses, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/responses/08-observability/azure.yaml): A crash-resilient LangGraph trip-planning agent with durable checkpoints, background responses, replayable streaming, human approval, steering, recovery, and cancellation.[Resilient Long Running Agent (Responses, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/responses/09-resilient/azure.yaml): A location-aware LangGraph chat agent that uses a custom ResponsesHostServer to support locale headers and custom location messages while retaining standard Responses behavior.[Custom Host (Responses, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/responses/12-custom-host/azure.yaml): A multi-turn LangGraph chat agent with local time and calculator tools, hosted on Foundry over the Invocations protocol with session state backed by a LangGraph checkpointer.[Basic Chat (Invocations, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/invocations/01-langgraph-chat/azure.yaml): A crash-resilient LangGraph trip-planning agent with durable checkpoints, background invocations, multi-turn sessions, human approval, recovery, and cancellation.[Resilient Long Running Agent (Invocations, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/invocations/02-resilient/azure.yaml): A location-aware LangGraph chat agent that uses a custom InvocationsHostServer to support locale headers and custom location messages while retaining standard Invocations behavior.[Custom Host (Invocations, LangGraph, Python)](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/hosted-agents/langgraph/invocations/04-custom-host/azure.yaml)


The Azure Developer CLI template gallery continues to grow with contributions from the community. Thank you!

## 🙋♀️ New to azd?

If you’re new to the Azure Developer CLI, `azd`

is an open-source command-line tool that helps you get your application from your local development environment to Azure faster. It provides developer-friendly commands that map to key stages in your workflow, whether you’re working in the terminal, your editor, or continuous integration and delivery.

[Install azd](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd)**Explore templates:**Browse the[Awesome azd template gallery](https://azure.github.io/awesome-azd/)and[AI App Templates](https://aka.ms/ai-gallery)**Learn more:**Visit the[official documentation](https://learn.microsoft.com/azure/developer/azure-developer-cli/)and[troubleshooting guide](https://learn.microsoft.com/azure/developer/azure-developer-cli/troubleshoot)**Get help:**Visit the[GitHub repository](https://github.com/Azure/azure-dev)to file issues or start discussions
