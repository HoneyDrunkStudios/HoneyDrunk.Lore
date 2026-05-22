# Microsoft .NET AI Stack

## Decision-useful summary
Microsoft's .NET AI story is converging around composable abstractions: `Microsoft.Extensions.AI` for provider-agnostic chat/model access, `Microsoft.Extensions.DataIngestion` and `Microsoft.Extensions.VectorData` for knowledge/RAG layers, MCP for external context/tool exposure, and Microsoft Agent Framework / Foundry agent tooling for agent orchestration. The May 2026 additions make the stack more production-shaped: Microsoft Agent Framework 1.0 supports sessions, tools, context providers, graph workflows, human approvals, and durable execution through Durable Task/Azure Functions hosting. Copilot Studio's .NET 10 WebAssembly migration adds a second signal: .NET is also viable as a browser-side agent/runtime substrate when deployment packaging and AOT/JIT tradeoffs are explicit. Microsoft is also steering developers toward ready-to-run MCP/OpenAI app samples with UI widgets/live previews rather than hand-rolling every MCP app from scratch. .NET 11 Preview 4 adds an MCP Server template directly in the SDK and continues AI-adjacent runtime/platform improvements, while the May 2026 servicing train fixes four CVEs across supported .NET/.NET Framework versions. The pattern is attractive for HoneyDrunk .NET services because it reduces direct provider lock-in and makes app-level AI features feel like normal dependency-injected infrastructure. [sources: raw/2026-05-03-rss-dotnet-ai-conference-app-composable-stack.md; raw/2026-05-07-youtube-microsoft-developer-youtube-foundry-toolkit-series-3-building-an-agent.md; raw/2026-05-09-rss-net-blog-microsoft-agent-framework-building-blocks-for-ai-part-3.md; raw/2026-05-09-rss-net-blog-durable-workflows-in-the-microsoft-agent-framework.md; raw/2026-05-10-rss-net-blog-copilot-studio-gets-faster-with-net-10-on-webassembly.md; raw/2026-05-10-youtube-microsoft-developer-youtube-dataverse-and-the-agentic-shift.md; raw/2026-05-11-youtube-microsoft-developer-youtube-don-t-build-mcp-apps-from-scratch-use-this.md; raw/2026-05-13-rss-net-blog-net-11-preview-4-is-now-available.md; raw/2026-05-13-rss-net-blog-net-and-net-framework-may-2026-servicing-releases-updates.md]

## Claims
- ConferencePulse, a Blazor Server conference assistant, used `Microsoft.Extensions.AI`, `Microsoft.Extensions.DataIngestion`, `Microsoft.Extensions.VectorData`, MCP, and Microsoft Agent Framework together for polls, Q&A, insights, and summaries. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-dotnet-ai-conference-app-composable-stack.md]
- `Microsoft.Extensions.AI` presents a stable `IChatClient` abstraction across model providers, allowing application code to avoid binding directly to one provider client. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-dotnet-ai-conference-app-composable-stack.md]
- The .NET AI conference-app pattern uses ingestion plus vector storage as the knowledge layer for RAG across multiple sources. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-dotnet-ai-conference-app-composable-stack.md]
- Azure MCP Server 2.0 exposes Azure resources as MCP tools; it reports 276 tools across 57 Azure services and adds self-hosted remote MCP server support. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-azure-blog-announcing-azure-mcp-server-2-0-stable-release-for-self-hos.md]
- A Microsoft Developer YouTube short says Foundry Toolkit Agent Builder can create an agent by naming it, choosing a model, writing a system prompt, optionally connecting an MCP server, testing with a real question, and exporting to code by SDK/language. confidence: 1 source, last-confirmed 2026-05-07. [source: raw/2026-05-07-youtube-microsoft-developer-youtube-foundry-toolkit-series-3-building-an-agent.md]
- Daily Discord announcement captures for Aspire, Microsoft Community, Microsoft Foundry, and .NET/C# were ingested but contained mostly browser/UI scaffolding rather than decision-grade announcement content. confidence: 12 sources, last-confirmed 2026-05-07. [sources: raw/2026-05-04..2026-05-07 clipper Discord Aspire/Microsoft/.NET snapshots]
- Microsoft Agent Framework 1.0 builds on `IChatClient` and can wrap Azure OpenAI, OpenAI, GitHub Models, Microsoft Foundry, Foundry Local, or Ollama clients as `AIAgent` instances with tools, sessions, streaming, and context providers. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-net-blog-microsoft-agent-framework-building-blocks-for-ai-part-3.md]
- Microsoft Agent Framework workflows use typed executors and `WorkflowBuilder` graphs for sequential chains, fan-out/fan-in, conditional routing, feedback loops, sub-workflows, and human-in-the-loop approvals. confidence: 2 sources, last-confirmed 2026-05-09. [sources: raw/2026-05-09-rss-net-blog-microsoft-agent-framework-building-blocks-for-ai-part-3.md; raw/2026-05-09-rss-net-blog-durable-workflows-in-the-microsoft-agent-framework.md]
- `Microsoft.Agents.AI.DurableTask` can run the same Microsoft Agent Framework workflow definition durably with checkpointing, restart survival, distributed execution, and Durable Task Scheduler dashboard observability. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-net-blog-durable-workflows-in-the-microsoft-agent-framework.md]
- `Microsoft.Agents.AI.Hosting.AzureFunctions` can expose registered workflows as generated HTTP triggers and optionally as MCP tools at the Functions MCP webhook endpoint. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-net-blog-durable-workflows-in-the-microsoft-agent-framework.md]
- Copilot Studio migrated a production .NET WebAssembly engine from .NET 8 to .NET 10 mainly by retargeting and dependency compatibility work; .NET 10 automatic WASM asset fingerprinting let the team remove custom SHA256 renaming/integrity loader plumbing. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-rss-net-blog-copilot-studio-gets-faster-with-net-10-on-webassembly.md]
- .NET 10 enables `WasmStripILAfterAOT` by default for AOT builds; Copilot Studio saw fewer deduplicated files between JIT and AOT packages, about a 15% package-size increase, but reported ~20% faster first-call execution and ~5% faster warm execution for large agent workloads. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-rss-net-blog-copilot-studio-gets-faster-with-net-10-on-webassembly.md]
- Microsoft Developer YouTube describes Dataverse's agentic shift as business-context grounding: Microsoft 365 Copilot access to Dataverse business data, Business Skills that encode processes/rules, Dataverse MCP server discovery, and an open-source Dataverse plugin for coding agents such as Claude Code and GitHub Copilot. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-youtube-microsoft-developer-youtube-dataverse-and-the-agentic-shift.md]
- A Microsoft Developer YouTube short points developers to open-source MCP app samples with interactive UI widgets, live previews, README docs, and OpenAI SDK-based app samples intended to work across Claude, ChatGPT, and Microsoft 365 Copilot surfaces. confidence: 1 source, last-confirmed 2026-05-11. [source: raw/2026-05-11-youtube-microsoft-developer-youtube-don-t-build-mcp-apps-from-scratch-use-this.md]

- .NET 11 Preview 4 includes an MCP Server template in the .NET SDK, plus runtime/library/SDK/ASP.NET Core/MAUI/C#/EF Core improvements including process API expansion, span-based compression APIs, runtime-async-compiled runtime libraries, `dotnet watch` device selection for MAUI/mobile, OpenTelemetry CLI telemetry, HTTP QUERY in OpenAPI output, Blazor circuit pause, SQL Server 2025 approximate vector search, and deeper EF Core JSON mapping. confidence: 1 source, last-confirmed 2026-05-16. [source: raw/2026-05-13-rss-net-blog-net-11-preview-4-is-now-available.md]
- The May 2026 .NET servicing updates ship .NET 10.0.8, .NET 9.0.16, and .NET 8.0.27 plus .NET Framework updates, fixing CVE-2026-32177, CVE-2026-35433, CVE-2026-32175, and CVE-2026-42899 across the affected supported versions. confidence: 1 source, last-confirmed 2026-05-16. [source: raw/2026-05-13-rss-net-blog-net-and-net-framework-may-2026-servicing-releases-updates.md]
- A Microsoft Developer YouTube short demonstrates a consumer prompt pattern for turning face/beauty inputs into a structured salon-style visual counseling sheet; useful only as weak prompt/UI-brief evidence, not as .NET or agent-platform evidence. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-17-youtube-microsoft-developer-youtube-fun-with-ai-make-your-chat-into-a-professi.md]

## Typed entities
- project/library: Microsoft.Extensions.AI
- project/library: Microsoft.Extensions.DataIngestion
- project/library: Microsoft.Extensions.VectorData
- project/library: Microsoft Agent Framework
- project/library: Microsoft.Agents.AI.DurableTask
- project/library: Microsoft.Agents.AI.Hosting.AzureFunctions
- project/service: Durable Task Scheduler
- project/service: Azure MCP Server 2.0
- product/tool: Microsoft Foundry Toolkit Agent Builder
- product/platform: Microsoft Copilot Studio
- platform/runtime: .NET 10 WebAssembly
- platform/service: Microsoft Dataverse
- feature/tool: Dataverse MCP server
- feature/tool: Dataverse plugin for coding agents
- resource: MCP app samples
- SDK/template: .NET 11 MCP Server template
- runtime/platform: .NET 11 Preview 4
- release: .NET 10.0.8
- release: .NET 9.0.16
- release: .NET 8.0.27
- vulnerability: CVE-2026-32177
- vulnerability: CVE-2026-35433
- vulnerability: CVE-2026-32175
- vulnerability: CVE-2026-42899
- SDK: OpenAI SDK
- concept: Business Skills
- concept: structured prompt-to-infographic brief
- protocol: Model Context Protocol
- project/framework: Blazor Server
- concept: RAG
- file: raw/2026-05-03-rss-dotnet-ai-conference-app-composable-stack.md
- file: raw/2026-05-03-rss-azure-blog-announcing-azure-mcp-server-2-0-stable-release-for-self-hos.md

## Explicit relationships
- Microsoft.Extensions.AI abstracts model providers through `IChatClient`.
- Microsoft.Extensions.DataIngestion and Microsoft.Extensions.VectorData provide the knowledge layer that supports RAG.
- Azure MCP Server 2.0 uses Model Context Protocol to expose Azure service operations to agents.
- Azure MCP Server 2.0 depends-on Azure service APIs and self-hosted remote deployment surfaces.
- Foundry Toolkit Agent Builder uses optional MCP servers as tool/context connectors and can export agents to code.
- Microsoft Agent Framework uses `IChatClient` as its provider abstraction and `AIFunctionFactory`/descriptions as its tool binding mechanism.
- Microsoft Agent Framework workflows depend-on typed executor contracts and graph edges for orchestration.
- Microsoft.Agents.AI.DurableTask uses Durable Task Scheduler to persist workflow checkpoints and coordinate distributed execution.
- Microsoft.Agents.AI.Hosting.AzureFunctions exposes Microsoft Agent Framework workflows as HTTP triggers and optionally MCP tools.
- .NET 10 WebAssembly uses automatic asset fingerprinting to simplify browser deployment integrity/cache-busting.
- Copilot Studio uses JIT plus AOT WebAssembly packaging to trade initial interactivity against steady-state execution speed.
- Dataverse MCP server and Business Skills use business data, relationships, and process rules to ground agents in organizational context.
- Dataverse plugin uses natural-language coding agents to build and manage Dataverse solutions.
- Microsoft MCP app samples package ready-to-run MCP/OpenAI app patterns for cross-assistant surfaces.
- .NET 11 SDK uses an MCP Server template to make MCP server creation a first-class ASP.NET/.NET developer workflow.
- May 2026 .NET servicing releases supersede earlier supported patch levels for .NET 10, 9, and 8 when security posture matters.
- [[dotnet-runtime-and-mobile-2026]] supersedes this page for detailed .NET 11 MAUI/CoreCLR and Process API tracking.
- [[AI Agent Harnesses]] uses MCP servers as a tool/context integration layer.
- [[Azure Agent Automation and Identity]] uses Microsoft Foundry, MCP, and Azure infrastructure as deployment context for C# agents.

## HoneyDrunk implications
- For .NET services, start with `IChatClient` and ingestion/vector abstractions if provider portability matters.
- For multi-step agents that must survive restarts or human waits, prefer Microsoft Agent Framework durable workflows over ad-hoc background loops.
- Azure Functions hosting is promising when a workflow should be callable by HTTP or MCP without hand-written controller/orchestrator glue.
- Azure MCP Server is a candidate for controlled cloud-automation agents, but it should be permission-scoped and audited before production use.
- Foundry Toolkit may be useful for prototype-to-code agent scaffolding if generated code can be inspected and brought under normal HoneyDrunk gates.
- For browser-resident .NET/agent experiences, benchmark .NET 10 WASM package-size tradeoffs against actual startup/interactivity needs before enabling heavy AOT strategies.
- Treat Dataverse as a useful reference architecture for business-context grounding even if HoneyDrunk does not adopt Dataverse directly: agents need data semantics, process skills, and rules, not just table access.
- Before building a custom MCP app surface, inspect Microsoft/open-source samples for UI widgets, app manifests, auth/hosting conventions, and cross-client behavior; sample reuse is cheaper than inventing protocol glue.
- If HoneyDrunk adopts .NET 11 previews, isolate experiments from production services; use the MCP Server template as scouting evidence, not a production version commitment.
- Patch supported .NET services promptly for the May 2026 CVEs; this source is strong enough for update urgency but not for exploitability assessment.

## Confidence and quality notes
- Quality posture: decision-usable for directional stack choices and servicing urgency; implementation details should be verified against package docs/release notes before coding.
- Weak spots: Microsoft/Azure blog and YouTube sources are vendor-authored and optimistic.
- Privacy filter: Discord captures were summarized only at high level; no private chat/user details were copied.

## 2026-05-21 compile additions

### Claims
- Microsoft Developer's MCP Inspector short says MCP app developers can locally test React Fluent UI app widgets by launching `npx @modelcontextprotocol/inspector`, connecting a local or hosted MCP server, validating raw tool calls in the Tools tab, and interacting with the widget in the Apps tab. confidence: 1 YouTube metadata source, last-confirmed 2026-05-21. [source: raw/2026-05-21-youtube-microsoft-developer-youtube-test-your-mcp-app-ui-locally-react-fluent-.md; page: [[mcp-tool-governance-and-app-surfaces]]]

### Typed entities
- tool: MCP Inspector
- UI framework: React Fluent UI
- concept: MCP app widget
- command: `npx @modelcontextprotocol/inspector`

### Explicit relationships
- MCP Inspector uses local or hosted MCP server connections to test tool calls and app widgets before client integration.
- MCP app samples and MCP Inspector together reduce the need to hand-roll untested MCP app/client protocol glue.

### HoneyDrunk implications
- For any HoneyDrunk MCP app UI, require local Inspector validation of tool round trips and widget behavior before wiring into Copilot/Claude/ChatGPT-style clients.
## 2026-05-22 compile additions

### Claims
- Microsoft.AgentGovernance.Extensions.ModelContextProtocol is a Public Preview companion package for official MCP C# SDK servers that adds `WithGovernance(...)` to apply policy enforcement, startup tool scanning, runtime governance, response sanitization, audit, and metrics. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-announcing-agent-governance-toolkit-mcp-extensions-for-net.md; page: [[mcp-tool-governance-and-app-surfaces]]]
- The package wraps the final MCP `ToolCollection` and is intended to govern tools registered before or after the extension is added, avoiding a forked SDK/proxy architecture. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-announcing-agent-governance-toolkit-mcp-extensions-for-net.md]
- The C# caller-unsafe redesign is relevant to .NET AI/tool servers because compiler-enforced unsafe boundaries can prevent agent-generated .NET code from calling unsafe APIs when the new safety model is enabled and `AllowUnsafeBlocks=false`. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md; page: [[csharp-memory-safety-and-unsafe-code]]]

### Typed entities
- package: `Microsoft.AgentGovernance.Extensions.ModelContextProtocol`
- API: `IMcpServerBuilder.WithGovernance(...)`
- collection: `ToolCollection`
- policy: Agent Governance Toolkit policy YAML
- language feature: C# caller unsafe
- page: [[csharp-memory-safety-and-unsafe-code]]

### Explicit relationships
- .NET MCP servers use Agent Governance Toolkit extensions to apply policy and sanitization at the builder/tool-collection layer.
- MCP governance complements Microsoft Agent Framework and .NET MCP Server templates by hardening the exposed tool surface.
- C# memory-safety compiler gates complement .NET AI server governance by constraining unsafe code paths at build time.

### HoneyDrunk implications
- Use the .NET MCP governance package as the default starting point for any internal C# MCP server rather than hand-written filters.
- Keep .NET AI/MCP repositories on safe-code defaults; require explicit review for any `AllowUnsafeBlocks=true` exception.
