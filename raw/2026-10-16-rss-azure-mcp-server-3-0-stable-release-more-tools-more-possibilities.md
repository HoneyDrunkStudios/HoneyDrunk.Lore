---
source: "https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-3-0-stable-release"
title: "Azure MCP Server 3.0 stable release: More tools. More possibilities"
author: "Sandeep Sen"
date_published: "2026-10-14"
date_clipped: "2026-10-16"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure MCP Server 3.0 stable release: More tools. More possibilities

We’re excited to share the stable release of Azure MCP Server 3.0, released on October 12, 2026. From reviewing backup protection to evaluating infrastructure changes, this release brings more everyday Azure operations into your agent workflows. It also introduces clearer tool contracts and security-focused defaults for new resources.

If you’re new to Azure MCP Server, it’s an open-source implementation of the Model Context Protocol (MCP). It gives compatible AI agents and developer environments a consistent way to discover and call Azure tools. Version 3.0 builds on 2.0’s self-hosted remote support, with more operational capabilities and more predictable integration. This third major release brings together 50 beta iterations and hundreds of contributions.

Whether you’re building a custom agent, working in GitHub Copilot, or managing a shared developer platform, 3.0 gives you more ways to connect Azure context with the work you need to do. Let’s look at what’s new.

## Bring operational context into your agents

Listing resources is often just the beginning. Is a workload protected? Is a recovery plan ready? What should you investigate next? New toolsets help your agent gather the context you need to explore those questions:

* **Azure Backup:** Inspect vaults, policies, protectable items and containers, protected items, jobs, and recovery points. Manage protection and governance, including soft delete, immutability, and Resource Guards for Multi-User Authorization. Tools also cover customer-managed key encryption and cross-region restore. Private endpoint tools support Recovery Services vaults, not Data Protection vaults.
* **Azure Resilience Management:** Work with goals, usage plans and enrollments, recovery plans and jobs, readiness checks, failover validation, and drill lifecycles. Failover and reprotect actions extend recovery workflows; plan and review those operations before invoking them.
* **Azure SRE Agent:** Work with investigations, incidents, connectors, safety hooks, and remediation plans to bring your agent into operational workflows. The 55-command toolset also covers agents, skills, threads, scheduled tasks, and workflows.

A useful place to start is a backup review. Ask your agent to help examine a vault’s policies and protected items, then look at jobs and recovery points. Bringing that information together helps you assess protection and decide what to change. The toolset also supports undeleting soft-deleted protected items.

The server’s stable release doesn’t change the availability or prerequisites of underlying Azure services. In particular, SRE Agent tools use the `Microsoft.App/SREAgentPreview` resource provider.

## Turn recommendations into informed changes

If you’re bringing existing resources into infrastructure as code, the new Azure Terraform tools give you a useful starting point. Retrieve AzureRM and AzAPI provider documentation and explore Azure Verified Modules, including pattern modules. Export existing resources with `aztfexport` and validate workspaces or plans with `conftest` as you prepare your changes.

Azure Advisor adds recommendation summaries, metadata, recommendation updates, lifecycle and retirement filters, and remediation guidance or artifacts. The Optimization toolset ranks cost recommendations by impact and estimated annual savings, compares VM and VM Scale Set options, and explains utilization projections. Advisor’s `advisor recommendation apply` tool returns rules for preparing infrastructure-as-code changes rather than applying changes to live resources.

Put these tools together to understand a recommendation, compare alternatives, and validate the proposed configuration. If your team is evaluating a VM resize, for example, use the recommendation and utilization projection to inform an infrastructure-as-code change, then review it through your existing approval process.

You’ll also find new capabilities for infrastructure, data, monitoring, and connected devices:

* **Azure Monitor:** Query metrics across resources and run bounded searches over Basic and Auxiliary log tables.
* **Azure Cosmos DB:** Infer container schemas, retrieve individual or recently modified items, and use full-text and vector search.
* **Azure IoT Hub and Azure IoT Operations:** Inspect IoT Hub device identities, twins, and statistics, query device data, and discover IoT Operations instances.
* **Azure Insights:** Bring infrastructure insights from Azure Resource Graph aggregation and MCP sampling into your workflow.
* **Azure Compute, Azure App Service, and Azure Managed Lustre:** Manage VM power state and validate VM creation inputs, change web app state, and expand Lustre filesystems.

## Make client integration more predictable

When you’re building an agent, clear tool descriptions and consistent responses make a difference. Version 3.0 brings a new tool design, refreshed `ModelContextProtocol` packages, and clearer descriptions for LLM tool selection. The CLI’s `--learn` flag lets you explore commands and parameters without executing Azure operations. Richer, spec-accurate `System.Text.Json` input schemas and corrected value and array-element types give your agent more useful information during discovery. Unknown parameters now produce errors.

Structured responses are opt-in. Use `--structured-output-mode duplicated` or `--structured-output-mode compact` to let tools advertise `outputSchema` and return `structuredContent` across execution modes. Without the flag, responses remain content-only. In all-tools mode, per-command schemas are available for opted-in commands, with App Configuration as the initial implementation.

New `operationPlane` metadata identifies data, control, both, or not-applicable operations. For pipeline integration, the server now supports Azure Pipelines workload identity federation service connections through `AzurePipelinesCredential`. Use `--disable-proxy-tools` to turn off proxy tools when they aren’t needed.

We’ve also worked on the details of the day-to-day experience. Authentication and role-based access control errors are clearer and more actionable, and the npm wrapper no longer edits the calling project’s package or lock files when installing a missing platform package. New regression benchmarks cover startup, concurrency, command dispatch, and resource use. Reported startup gains are about 39% for targeted CLI command invocations only, not server-wide startup or throughput.

Missing resources now return HTTP 404 rather than 500 or 400, and invalid command input returns HTTP 400 rather than 500. Logs and exceptions go to stderr, preserving stdout for JSON and JSON-RPC. Option binding is also fixed for trimmed and packaged tools.

## Review the security defaults

Security is part of getting started, too. When you create new resources through the server, these defaults help limit access from the start:

* New Storage accounts disable Shared Key authentication; HTTPS, TLS 1.2, and disabled anonymous blob access remain the defaults.
* New Event Hubs namespaces disable local authentication.
* New Recovery Services vaults disable public networking.
* New NFS file shares use `RootSquash` and encryption in transit.

Explicit options remain available. These defaults don’t reconfigure existing resources on upgrade; omitted security options preserve existing file-share and Event Hubs namespace settings during updates.

Endpoint validation through `Microsoft.Security.AntiSSRF` now covers more cloud-specific and namespace-specific endpoints across the data and control planes, with namespace-scoped validation overrides. Validation-failure telemetry omits option values. Azure Communication Services email and SMS send tools are excluded in read-only mode, and `--tool` filtering matches exposed names exactly, ignoring case.

## Plan your upgrade

If you’re upgrading from 2.0 or a 3.0 preview, start with the [complete 3.x changelog](https://github.com/microsoft/mcp/blob/release/azure/3.x/servers/Azure.Mcp.Server/CHANGELOG.md) and test your client before updating shared deployments. Here are the main changes to check:

1. **Refresh discovery and saved calls.** Remove obsolete parameters from affected saved calls, scripts, and prompts, including unused subscription, resource-group, tenant, auth-method, user, and sender-name options. Custom retry-policy options are removed in favor of Azure SDK retry defaults, and `sql server delete` no longer accepts the confirmation-only `--force` option. Preview users must replace `azmcp resilience` with `azmcp resiliency` and change `resilience_*` tool-name prefixes to `resiliency_*` in filters and allowlists. Replace `monitor healthmodels entity get` with `monitor healthmodels list` or `monitor healthmodels get`.
2. **Recheck response parsing.** Advisor recommendation listings now use ARM-style `properties`; Monitor log queries and Azure AI Search index queries use `results` wrappers. Named payloads also include `{ bestPractices }` for best practices, `{ servers }` for SQL server listings, and `{ guidance }` for Well-Architected Framework guidance. `functions language list` and `functions project get` now return direct objects. Update parsers and test fixtures accordingly.
3. **Review database access.** MySQL and PostgreSQL query tools are destructive, non-idempotent, and non-read-only. SQL-verb filtering has been removed. In consolidated mode, they move from `get_azure_databases_details` to `execute_azure_database_query`. Use least-privilege database permissions; signed-in database permissions determine allowed operations.
4. **Update configuration and provisioning.** Move server settings in `appsettings.json` under `MicrosoftMcp`. Shared code namespaces move from `Azure.Mcp.Core.*` to `Microsoft.Mcp.Core.*`; update logging categories such as `Logging:LogLevel:Azure.Mcp.Core` to `Logging:LogLevel:Microsoft.Mcp.Core` and any environment log filters. VM and VM Scale Set creation require an explicit `--image`, and the default size is `Standard_D2s_v5`. The `Win2019Datacenter` and `Ubuntu2004` image aliases are removed. Revisit image, sizing, and cost assumptions alongside the resource-creation defaults above.
5. **Check custom HTTP clients.** The server uses the stateless MCP protocol `2026-07-28`; clients using this version must send `Mcp-Method` and `Mcp-Name` headers on every POST. Clients using `2025-11-25` retain automatically negotiated backward compatibility.

## Choose your experience

Choose the experience that fits how you like to build. Bring Azure MCP Server into your editor, use it with a desktop app or command-line agent, or share a server with your team.

* **Build in your preferred editor.** Bring Azure tools into your everyday development workflow through the supported extension, toolkit, or MCP configuration:
  + [Visual Studio Code](https://aka.ms/azmcp/download/vscode)
  + [Visual Studio](https://aka.ms/azmcp/download/vs)
  + [IntelliJ](https://aka.ms/azmcp/download/intellij)
  + [Eclipse](https://aka.ms/azmcp/download/eclipse)
  + [Cursor](https://aka.ms/azmcp/download/cursor)
  + [Claude](https://aka.ms/azmcp/download/claude)
  + [Google Antigravity](https://aka.ms/azmcp/download/antigravity)
* **Try a desktop experience.** Explore the [GitHub Copilot app](https://github.com/features/ai/github-app) and connect Azure MCP Server through its [MCP settings](https://docs.github.com/en/copilot/how-tos/github-copilot-app/customize-github-copilot-app).
* **Stay in your terminal.** Use Azure MCP Server with [GitHub Copilot CLI](https://aka.ms/azmcp/download/github-copilot-cli) or other MCP-compatible command-line agents.
* **Run a standalone local server.** Connect your preferred MCP client or custom agent to Azure MCP Server on your machine for a local setup you control.
* **Share a server with your team.** Self-host a [remote MCP server](https://aka.ms/azmcp/self-host) when you need shared access and centrally managed configuration. This builds on the self-hosting support introduced in 2.0.

## Get started with a read-only workflow

Ready to give it a try? The following VS Code example starts with a read-only workflow so you can get familiar with 3.0. For this local example, you’ll need Node.js LTS, Azure CLI, an Azure subscription, and a compatible MCP client. Sign in and select your intended subscription:

```
az login

az account set --subscription "<subscription-id>"
```

For VS Code, add this server to `.vscode/mcp.json`, merging it with any existing `servers` entries. This example enables read-only mode:

```
{

  "servers": {

    "azure-mcp": {

      "type": "stdio",

      "command": "npx",

      "args": ["-y", "@azure/mcp@3.0.0", "server", "start", "--read-only"]

    }

  }

}
```

Start the server from your MCP client and explore the available tools. Then try a prompt like this:

> List the Azure Advisor recommendations for my subscription and explain one cost recommendation. Don’t apply changes.

Keep this first trial focused on inspection. Use a development subscription and an identity with only the permissions the workflow needs. Before enabling write tools, review the target resources and your team’s approval process; a natural-language prompt isn’t a substitute for access controls.

Use the [authentication guide](https://github.com/microsoft/mcp/blob/release/azure/3.x/docs/Authentication.md) and [setup documentation](https://learn.microsoft.com/azure/developer/azure-mcp-server/) for guidance on your chosen environment.

For 3.x, see the [command reference](https://github.com/microsoft/mcp/blob/release/azure/3.x/servers/Azure.Mcp.Server/docs/azmcp-commands.md), [remote deployment](https://github.com/microsoft/mcp/blob/release/azure/3.x/servers/Azure.Mcp.Server/README.md#remote-mcp-server-preview), [sovereign cloud support](https://github.com/microsoft/mcp/blob/release/azure/3.x/servers/Azure.Mcp.Server/README.md#sovereign-cloud-support), [troubleshooting](https://github.com/microsoft/mcp/blob/release/azure/3.x/servers/Azure.Mcp.Server/TROUBLESHOOTING.md), and [contributing guide](https://github.com/microsoft/mcp/blob/release/azure/3.x/CONTRIBUTING.md).

## Keep building with us

Thank you to the engineering team, partners, and everyone in the open-source community who tested the previews and shared feedback. We’re looking forward to seeing what you build with 3.0. Start with a workflow you know, explore the new tools, and [let us know how it goes](https://aka.ms/azmcp/issues). Your ideas, issue reports, and contributions are welcome in the [Azure MCP repository](https://aka.ms/azmcp).
