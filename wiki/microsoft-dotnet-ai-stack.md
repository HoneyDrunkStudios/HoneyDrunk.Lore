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

## 2026-05-30 compile additions

### Claims
- Microsoft/.NET Blog guidance says .NET developers should choose Copilot surfaces by task: Visual Studio for solution-local understanding/refactors/tests, VS Code when changes cross code/config/docs, Copilot CLI for terminal build/test loops, and the cloud coding agent for bounded multi-file tasks that can return a reviewable draft. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-doing-more-with-github-copilot-as-a-net-developer.md]
- The same source frames useful .NET Copilot prompts around goal, code/command output, constraints, and expected answer shape; agentic tasks should have bounded scope, constraints, a clear definition of done, and verification such as rerunning relevant tests. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-doing-more-with-github-copilot-as-a-net-developer.md]
- .NET MAUI 10 can opt Android apps into Material 3 styling with `<UseMaterial3>true</UseMaterial3>` when targeting `net10.0-android`; Microsoft recommends Microsoft.Maui.Controls 10.0.60+ for the broadest current control coverage. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-give-your-net-maui-android-apps-a-material-3-makeover.md; page: [[dotnet-runtime-and-mobile-2026]]]
- Azure Container Apps dynamic shell sessions can be exposed as a platform-managed MCP server and connected to GitHub Copilot in VS Code through `.vscode/mcp.json`; the API key must be treated as a secret and should not be committed. confidence: 1 Microsoft Learn source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-tutorial-use-mcp-with-dynamic-sessions-shell.md]

### Typed entities
- product: GitHub Copilot
- IDE: Visual Studio
- IDE/editor: Visual Studio Code
- tool: Copilot CLI
- product: Copilot cloud coding agent
- framework: .NET MAUI 10
- property: `<UseMaterial3>`
- package: `Microsoft.Maui.Controls` 10.0.60+
- platform: Azure Container Apps dynamic sessions
- file: `.vscode/mcp.json`

### Explicit relationships
- Copilot chat supports understanding, planning, explanation, and targeted generation; Copilot agentic workflows use bounded tasks to change, verify, update, rerun, and produce reviewable diffs.
- .NET MAUI Material 3 belongs under runtime/mobile tracking, but it also affects .NET developer platform adoption.
- Azure dynamic-session MCP can connect cloud shell execution to Copilot, but depends-on secret-safe configuration and preview API behavior.

### HoneyDrunk implications
- For .NET repos, standardize agent task wording around scope, constraints, no-change boundaries, tests to run, and expected summary.
- Do not store MCP session-pool API keys in committed VS Code MCP config; use environment indirection or local ignored files.
- If HoneyDrunk has MAUI Android prototypes, treat Material 3 as a branch-level UI validation task rather than a blind default switch until control gaps are checked.

## 2026-06-01 compile additions

### Claims
- The dotnet/runtime Copilot Coding Agent report is a large-scale .NET ecosystem case study: 878 CCA PRs in dotnet/runtime over ten months, 535 merged, 67.9% success excluding open PRs, and 3 detected reverts among merged CCA PRs. confidence: 1 Microsoft/.NET source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ten-months-with-copilot-coding-agent-in-dotnet-runtime.md]
- The report says dotnet/runtime's early CCA failures were caused partly by missing `.github/copilot-instructions.md` guidance and default sandbox/firewall rules blocking package feeds needed for builds; repo-specific build/test instructions were a major improvement lever. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ten-months-with-copilot-coding-agent-in-dotnet-runtime.md]
- In dotnet/runtime, CCA was strongest for bounded managed-code tasks such as removal/cleanup, tests, refactoring, and clear bug fixes, while native C++ and cross-platform runtime work remained harder because the agent could not verify all target OS/architecture/toolchain combinations. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-ten-months-with-copilot-coding-agent-in-dotnet-runtime.md]

### Typed entities
- repository: dotnet/runtime
- product: Copilot Coding Agent / CCA
- file: `.github/copilot-instructions.md`
- language/runtime: C#
- language/runtime: C++
- component: CoreCLR
- concept: cross-platform verification

### Explicit relationships
- .NET coding-agent workflows depend-on repo-specific build instructions and dependency/network access.
- CCA complements .NET maintainers for bounded, reviewable work but does not supersede maintainer ownership.
- Cross-platform .NET runtime work depends-on target-specific verification that a Linux-only agent environment may not provide.

### HoneyDrunk implications
- For HoneyDrunk .NET repos, keep copilot/agent instructions specific about build subsets, test commands, package feeds, and no-change boundaries.
- Do not route platform-specific runtime/native work to unattended agents unless target verification is available in CI or a local harness.

## 2026-06-03 compile additions

### Claims
- `azure-functions-skills` makes Azure Functions agent scaffolding a .NET/Microsoft-stack concern as well as an Azure tooling concern: it installs skills, MCP config, hooks, `AGENTS.md`/`CLAUDE.md`/Copilot instructions, and a `doctor` validator for secure-by-default Functions workspaces. confidence: 1 Microsoft Azure SDK Blog source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-azure-blog-introducing-azure-functions-skills-an-ai-era-workspace-for-.md]
- The preview skill catalog includes setup, create, deploy, diagnostics, best-practices, health-status, inventory, doctor, feedback, and agents skills; the agents skill targets the Azure Functions serverless agents runtime. confidence: 1 Microsoft source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-azure-blog-introducing-azure-functions-skills-an-ai-era-workspace-for-.md]
- The `doctor` validator checks Azure Functions project shape, runtime pinning, trigger configuration, extension bundles, deprecated settings, lockfiles, tracked `.env` files, supply-chain risks, and optional semantic code issues through an agent. confidence: 1 Microsoft source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-azure-blog-introducing-azure-functions-skills-an-ai-era-workspace-for-.md]
- Azure Cosmos DB MCP Toolkit v1.1.2 GA uses .NET-hosted MCP server patterns to expose Cosmos DB discovery, text search, vector search, schema inference, and document lookup to agents with enterprise Azure identity controls. confidence: 1 Microsoft Azure Cosmos DB Blog source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-azure-cosmos-db-blog-azure-cosmos-db-mcp-toolkit-is-now-generally-avai.md]

### Typed entities
- package/plugin: `@azure/functions-skills`
- skill: `azure-functions-doctor`
- skill: `azure-functions-create`
- skill: `azure-functions-deploy`
- skill: `azure-functions-agents`
- runtime: Azure Functions serverless agents runtime
- product: Azure Cosmos DB MCP Toolkit
- API/abstraction: `IEmbeddingClient`
- provider: Azure AI Services
- provider: Azure AI Foundry
- provider: OpenAI native API

### Explicit relationships
- Azure Functions skills complement Microsoft Agent Framework by packaging current Functions-specific scaffold/deploy/validation guidance for coding agents.
- `doctor` uses deterministic checks before optional semantic agent checks, making validation part of the .NET/Azure agent workspace rather than a separate review convention.
- Cosmos DB MCP Toolkit depends-on embedding-provider abstraction for vector search portability.
- .NET MCP server patterns increasingly combine data-plane tools with Azure identity and Foundry catalog integration.

### HoneyDrunk implications
- For .NET/Azure repositories, treat generated agent instruction files and MCP configs as source-controlled infrastructure requiring review.
- Add Functions `doctor` or equivalent deterministic checks before relying on agent-generated Functions deployments.
- If HoneyDrunk builds RAG over Cosmos DB, evaluate the MCP Toolkit separately from the database itself: tool granularity, auth behavior, schema sampling, vector-search quality, and error handling all affect agent safety.

### Quality notes
- Microsoft sources are implementation-specific but vendor-authored. Preview skill behavior can change; pin versions when testing.

## 2026-06-07 compile additions

### Claims
- Microsoft.Extensions.AI tool calling describes available .NET methods, external APIs, MCP servers, or other executable operations to a model; the model returns structured tool-call requests and the application invokes them, with `FunctionInvokingChatClient` handling the invocation loop automatically. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-ai-tool-calling-net.md]
- MEAI tool calling uses provider-agnostic `AIFunction`, `AIFunctionFactory`, and `FunctionInvokingChatClient` abstractions over any `IChatClient`, including Azure OpenAI, OpenAI, Ollama, and other providers that implement the interface. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-ai-tool-calling-net.md]
- Function-calling support includes automatic parallel function calling where the model/provider supports it, while tool descriptions count against token limits and should be scoped to the conversation. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-ai-tool-calling-net.md]
- Microsoft Agent Framework evaluation in .NET builds on `Microsoft.Extensions.AI.Evaluation`, with `IAgentEvaluator`, `EvalItem`, `EvalResults`, local evaluators, custom function evaluators, Foundry evaluators, expected outputs/tool calls, repetitions, and conversation splitters. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-evaluation.md]
- Azure Functions serverless agents runtime uses markdown agent definitions, `agents.config.yaml`, and `mcp.json` to deploy serverless agents through standard Azure Functions infrastructure. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-quickstart-build-serverless-agents-using-azure-functions.md]

### Typed entities
- project/library: Microsoft.Extensions.AI
- type: `AIFunction`
- type: `AIFunctionFactory`
- type: `FunctionInvokingChatClient`
- interface: `IChatClient`
- package/namespace: `Microsoft.Extensions.AI.Evaluation`
- interface: `IAgentEvaluator`
- type: `EvalItem`
- type: `EvalResults`
- runtime: Azure Functions serverless agents runtime

### Explicit relationships
- MEAI tool calling uses `IChatClient` and function abstractions to separate provider choice from tool invocation logic.
- FunctionInvokingChatClient supersedes hand-written tool-call loops for common .NET chat clients, while provider/model capability still determines actual function-call behavior.
- Token budgets depend-on registered tool definitions, so broad always-on tool lists contradict efficient .NET agent calls.
- Agent Framework evaluation uses MEAI evaluation primitives to connect .NET agent workflows to local and Foundry scoring.
- Azure Functions serverless agents complement Microsoft Agent Framework hosting by making trigger-based agents deployable as Functions workloads.

### HoneyDrunk implications
- For .NET agents, start with narrow `AIFunction` sets per workflow and avoid registering every possible tool by default.
- Add local `LocalEvaluator`/function checks for expected tool calls before relying on Foundry LLM-as-judge evaluation.
- Treat serverless agent markdown/config files as source-controlled runtime configuration that needs review like code.

### Quality notes
- Microsoft Learn pages are implementation guidance but may change with package versions. Verify API names and package versions before coding.

## 2026-06-09 compile additions

### Claims
- Microsoft Build 2026 .NET sessions position .NET 11 around AI-era runtime, library, SDK, diagnostics, performance, and developer-productivity improvements. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-net-at-microsoft-build-2026-must-watch-sessions-net-blog.md]
- C# union types are presented as a coming language feature for modeling closed sets of data shapes, especially useful for wire protocols and domain modeling. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-net-at-microsoft-build-2026-must-watch-sessions-net-blog.md]
- ASP.NET Core and Blazor in .NET 11 are framed as faster, more secure, Aspire-integrated, and gaining agentic web building blocks such as agents, tools, skills, and components. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-net-at-microsoft-build-2026-must-watch-sessions-net-blog.md]
- .NET MAUI sessions emphasize local/on-device AI across mobile and desktop, with privacy, performance, UX, and AI-assisted app-development workflow implications. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-net-at-microsoft-build-2026-must-watch-sessions-net-blog.md; page: [[dotnet-runtime-and-mobile-2026]]]
- Build 2026 related sessions tie .NET to Foundry Agent Service, Microsoft Agent Framework, Foundry multi-agent/Claw patterns, GitHub Copilot SDK multi-client agents, Aspire for agents, and modernization agents for legacy .NET apps. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-net-at-microsoft-build-2026-must-watch-sessions-net-blog.md]

### Typed entities
- platform/runtime: .NET 11
- language feature: C# union types
- framework: ASP.NET Core
- framework: Blazor
- framework: Aspire
- framework: .NET MAUI
- tool: dotnetup
- product: GitHub Copilot SDK
- platform: Microsoft Foundry Agent Service
- framework: Microsoft Agent Framework

### Explicit relationships
- .NET 11 uses runtime/library/SDK improvements to support cloud-connected and agent-driven apps.
- Union types complement protocol/domain modeling by representing closed data-shape sets.
- ASP.NET Core/Blazor agentic web features depend-on Aspire and agent/tool/skill/component building blocks.
- .NET MAUI edge AI depends-on local models and device capability rather than cloud-only inference.
- Foundry and Copilot SDK sessions connect .NET app development to hosted agents and multi-device agent surfaces.

### HoneyDrunk implications
- Track C# union types for HoneyDrunk protocol and domain-model code once available; do not prematurely simulate with awkward abstractions unless needed.
- For .NET web apps, evaluate agent/tool/skill patterns alongside ordinary ASP.NET/Blazor security and performance work.
- Treat .NET MAUI edge AI as a privacy/performance spike requiring target-device testing, not a default mobile architecture.

### Quality notes
- Source is a Microsoft session roundup, so it is roadmap/session signal rather than detailed API documentation. Verify APIs and preview status before implementation.

## 2026-06-10 compile additions: .NET 11 Preview 5 and Foundry agent architecture

### Source-backed claims
- .NET 11 Preview 5 includes updates across runtime, SDK, libraries, ASP.NET Core, MAUI, C#, and EF Core; Microsoft recommends Visual Studio 2026 Insiders for Windows preview work. Source: `raw/2026-06-10-web-dotnet-net-11-preview-5-is-now-available-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Preview 5 library and SDK highlights include System.Text.Json JSON Lines support, LINQ full outer joins, X25519 key agreement, generic numeric `Random` APIs, file-based apps referencing other C# files, build-time SDK vulnerability/EOL checks, and a `dotnet new` MCP Server template. Source: `raw/2026-06-10-web-dotnet-net-11-preview-5-is-now-available-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Preview 5 ASP.NET Core highlights include Blazor SSR client-side validation, QuickGrid without interactivity, Blazor WebAssembly Gateway, and `SupplyParameterFromSession`. Source: `raw/2026-06-10-web-dotnet-net-11-preview-5-is-now-available-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft Foundry gateway guidance and the Foundry chat baseline both reinforce that AI app architecture needs an app/gateway layer for auth, routing, rollout, observability, throttling, and failback rather than direct client access to broad project/model credentials. Sources: `raw/2026-06-10-web-microsoft-learn-access-foundry-models-and-other-language-models-through-a-gateway-azure.md`, `raw/2026-06-10-web-microsoft-learn-baseline-microsoft-foundry-chat-reference-architecture-azure-architectur.md`. confidence: 2 sources, last-confirmed 2026-06-10.

### Typed entities
- project: .NET 11 Preview 5
- library: System.Text.Json
- project: ASP.NET Core
- project: Blazor
- project: .NET MAUI
- project: Microsoft Foundry Agent Service
- concept: MCP Server template
- decision: .NET AI app gateway pattern

### Explicit relationships
- .NET 11 Preview 5 adds MCP server scaffolding to `dotnet new`.
- Blazor and ASP.NET Core preview features support more server-rendered and gateway-style app surfaces.
- Foundry Agent Service depends-on application-layer authorization for per-user access control in chat apps.
- Foundry progressive rollout depends-on routing outside the managed agent service.

### HoneyDrunk implications
- Track the .NET MCP Server template as a possible starting point for internal tool servers, but avoid preview dependency in production.
- For .NET AI apps, design authorization/routing around the app boundary first; do not expose Foundry project credentials directly to clients.
- Use build-time vulnerability/EOL checks as an additional CI signal once .NET 11 tooling stabilizes.

### Quality notes
- .NET 11 is preview. Foundry architecture guidance is Microsoft-authored and should be validated against current Azure region, quota, and identity behavior.

## 2026-06-11 compile additions: App Service agents, OpenTelemetry, modernization, and RT.Assistant

### Source-backed claims
- Azure App Service guidance positions agentic web apps as ordinary App Service applications that add conversational planning/tool usage through frameworks such as Semantic Kernel, LangGraph, or Foundry Agent Service. Source: `raw/2026-06-11-web-microsoft-learn-build-agentic-web-applications-in-azure-app-service-azure-app-service.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-11.
- App Service's AI preview Agents tab uses connected Application Insights plus application-emitted OpenTelemetry GenAI semantic conventions, grouping on `gen_ai.agent.name`, `gen_ai.agent.id`, and `gen_ai.usage.*`. Source: `raw/2026-06-11-web-microsoft-learn-build-agentic-web-applications-in-azure-app-service-azure-app-service.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-11.
- Microsoft's multi-agent .NET monitoring tutorial deploys a Microsoft Agent Framework travel-planner app to App Service, wraps agents with `UseOpenTelemetry`, uses Azure Monitor OpenTelemetry distro, and visualizes tool calls, token usage, agent runs, and errors in Application Insights. Source: `raw/2026-06-11-web-microsoft-learn-monitor-a-multi-agent-app-with-opentelemetry-and-application-insights-ne.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-11.
- The `modernize-dotnet` Copilot custom agent follows an assess-plan-execute workflow and emits assessment, upgrade plan, and upgrade task artifacts directly into the repository for review. Source: `raw/2026-06-11-web-net-blog-modernize-net-anywhere-with-github-copilot-net-blog.md`. confidence: 1 Microsoft/.NET source, last-confirmed 2026-06-11.
- RT.Assistant combines .NET, F#, OpenAI Realtime API over WebRTC, Microsoft.Extensions.AI, .NET MAUI/Fabulous, typed async buses, deterministic state machines, and Prolog-backed query execution for a multi-agent voice app. Source: `raw/2026-06-11-web-net-blog-rt-assistant-a-multi-agent-voice-bot-using-net-and-openai-net-blog.md`. confidence: 1 Microsoft/.NET guest post, last-confirmed 2026-06-11.

### Typed entities
- platform: Azure App Service
- framework: Semantic Kernel
- framework: LangGraph
- framework: Microsoft Agent Framework
- product: Application Insights Agents preview
- method: `UseOpenTelemetry`
- package: Azure Monitor OpenTelemetry distro
- agent: `modernize-dotnet`
- project: RT.Assistant
- library: RTOpenAI
- framework: RTFlow
- language: F#
- engine: Tau Prolog

### Explicit relationships
- App Service agent monitoring depends-on Application Insights and OpenTelemetry GenAI semantic attributes emitted by the app.
- Microsoft Agent Framework agents use `UseOpenTelemetry` to emit per-agent spans and usage metrics.
- `modernize-dotnet` uses Copilot agent surfaces to convert upgrade work into reviewable repo artifacts.
- RT.Assistant uses a deterministic Flow state machine to constrain nondeterministic multi-agent voice behavior.
- Prolog query execution complements LLM query translation by making final plan-selection answers checkable against structured facts.

### HoneyDrunk implications
- For .NET agent apps, add OTel GenAI attributes during first implementation rather than retrofitting observability after deployment.
- Disable or avoid sensitive message-content capture in production unless a redaction and retention policy exists.
- Treat `modernize-dotnet` as a branch-based migration assistant; generated assessments/plans/tasks should be reviewed like architecture artifacts.
- RT.Assistant is a strong design reference for voice apps that need typed orchestration and symbolic/logic-backed answers instead of direct LLM responses.

### Quality notes
- Microsoft Learn pages are concrete implementation guidance but preview UI/API behavior can change. RT.Assistant is a guest/sample post and should be treated as architecture inspiration, not product support guarantee.

## 2026-06-12 compile additions: .NET agentic modernization event

### Source-backed claims
- Microsoft scheduled .NET Day on Agentic Modernization for 2026-06-16, focused on modernizing legacy .NET apps with GitHub Copilot-assisted workflows, Aspire, Microsoft Agent Framework, Microsoft Foundry, and GitHub Copilot for Azure / Azure MCP. Source: `raw/2026-06-12-web-dotnet-blog-join-us-for-net-day-on-agentic-modernization-livestream-net-blog.md`. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-06-12.
- The event agenda emphasizes migration of real-world WinForms and data-heavy line-of-business apps, cloud migration, and adding agentic/AI-powered functionality after modernization rather than rewriting everything from scratch. Source: `raw/2026-06-12-web-dotnet-blog-join-us-for-net-day-on-agentic-modernization-livestream-net-blog.md`. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-06-12.

### Typed entities
- event: .NET Day on Agentic Modernization
- framework: Aspire
- framework: Microsoft Agent Framework
- platform: Microsoft Foundry
- product: GitHub Copilot for Azure
- server/tool: Azure MCP
- app type: WinForms line-of-business app
- concept: agentic modernization

### Explicit relationships
- Agentic modernization uses Copilot, Aspire, Agent Framework, Foundry, and Azure MCP as migration/augmentation tools for existing .NET apps.
- Modernization workflows complement lift-and-shift migration by adding cloud and AI capabilities after mechanical upgrade work.

### HoneyDrunk implications
- If HoneyDrunk touches legacy .NET apps, treat Microsoft’s agentic modernization materials as a scouting source for migration workflows, not a production recipe until session artifacts are reviewed.
- Prefer assess-plan-execute artifacts for modernization agents so architecture choices remain reviewable.

### Quality notes
- This is an event announcement, so it is weak as implementation evidence. It strengthens Microsoft platform direction only.

## 2026-06-15 compile additions: GenAIOps extension over MLOps

### Source-backed claims
- Microsoft Learn frames GenAIOps/LLMOps as an extension of existing MLOps investments rather than a replacement, with fine-tuning reusing many traditional MLOps patterns while prompting and RAG add new workload responsibilities. Source: `raw/2026-06-15-web-microsoft-learn-generative-ai-operations-for-organizations-with-mlops-.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-15.
- For RAG and prompt-engineering workloads, Microsoft says the governed system includes the orchestrator, prompts, grounding data stores, indexes, data pipelines, and evaluation process, not only the deployed model. Source: `raw/2026-06-15-web-microsoft-learn-generative-ai-operations-for-organizations-with-mlops-.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-15.
- Microsoft identifies GenAIOps extensions around chunking/embedding pipelines, search-index freshness, prompt/RAG experimentation, use-case-specific evaluation metrics, orchestrator/data-store deployment, gateways, rollout strategies, operational monitoring, production learning, content safety, quotas, and token usage. Source: `raw/2026-06-15-web-microsoft-learn-generative-ai-operations-for-organizations-with-mlops-.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-15.
- Microsoft cautions that software engineers can manage orchestration and metrics setup, but data scientists and subject matter experts should review evaluations because prompting/RAG evaluation still needs scientific and domain judgment. Source: `raw/2026-06-15-web-microsoft-learn-generative-ai-operations-for-organizations-with-mlops-.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-15.

### Typed entities
- concept: GenAIOps / LLMOps
- concept: MLOps
- pattern: prompt engineering
- pattern: retrieval-augmented generation / RAG
- component: orchestrator
- component: vector store
- component: search index maintenance
- product: Azure AI Search
- product: Microsoft Foundry Evaluation SDK
- platform/tool: MLflow

### Explicit relationships
- GenAIOps extends MLOps by adding prompt, orchestrator, grounding-data, index, gateway, and model-service operations.
- RAG reproducibility depends-on versioned documents, chunks, embeddings, indexes, prompts, retrieval configuration, and evaluation data.
- Search-index maintenance complements DataOps because freshness, right-to-be-forgotten, and rollback needs apply to grounding data.
- Gateway deployment complements model deployment by centralizing auth, routing, failover, monitoring, and rollout controls.

### HoneyDrunk implications
- Treat Lore/OpenClaw RAG or retrieval work as deployable software: version source data, chunking, embeddings, index config, prompts, eval sets, and orchestration code.
- Do not score RAG quality only with final-answer vibes. Track groundedness, relevance, completeness, usefulness feedback, and domain review.
- Add quota/token/429 monitoring and content-safety decisions to any production GenAI app plan.

### Quality notes
- Microsoft Learn is strong architecture guidance but Azure-centered. Translate patterns to HoneyDrunk's flat-file and local-runner context before adopting managed services.

## 2026-06-17 compile additions: .NET versioned OpenAPI and Azure agent architecture

### Source-backed claims
- The .NET Blog recommends `Asp.Versioning` v10 for .NET 10 APIs that need official integration with `Microsoft.AspNetCore.OpenApi`, with separate packages for controllers and Minimal APIs and `Asp.Versioning.OpenApi` for versioned OpenAPI documents. Source: `raw/2026-06-17-web-devblogs-microsoft-com-combining-api-versioning-with-openapi-in-net-10-applications-net-blog.md`. confidence: 1 .NET Blog community/MVP source, last-confirmed 2026-06-17.
- In `Asp.Versioning` v10, `AddApiVersioning().AddApiExplorer(...).AddOpenApi()` plus `app.MapOpenApi().WithDocumentPerVersion()` can generate one OpenAPI document per API version without duplicating `AddOpenApi()` calls for every version. Source: `raw/2026-06-17-web-devblogs-microsoft-com-combining-api-versioning-with-openapi-in-net-10-applications-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-17.
- The same .NET source recommends OpenAPI linting and diffing with tools such as Spectral and oasdiff/openapi-diff to catch unversioned endpoints or unintended breaking changes during PR review. Source: `raw/2026-06-17-web-devblogs-microsoft-com-combining-api-versioning-with-openapi-in-net-10-applications-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-17.
- Microsoft Architecture Center says multitenant AI/ML systems should choose explicitly among tenant-specific models, shared models, and tuned shared base models, with tenant data/model isolation and tenant consent as first-class requirements. Source: `raw/2026-06-17-web-learn-microsoft-com-architectural-approaches-for-ai-and-machine-learning-in-multitenant-solutions-azur.md`. confidence: 1 Microsoft Architecture Center source, last-confirmed 2026-06-17.
- The same multitenant guidance distinguishes Foundry/prebuilt AI services from custom Azure Machine Learning architectures: managed platforms reduce setup and operational burden, while custom ML gives more control over training, inference, lineage, and drift management at higher implementation complexity. Source: `raw/2026-06-17-web-learn-microsoft-com-architectural-approaches-for-ai-and-machine-learning-in-multitenant-solutions-azur.md`. confidence: 1 source, last-confirmed 2026-06-17.
- Microsoft's multiple-agent workflow architecture uses Microsoft Agent Framework custom code in Container Apps for deterministic orchestration control, while Foundry Agent Service is the lower-code alternative when prompt-defined behavior, HTTPS-reachable tools, and managed compute are sufficient. Source: `raw/2026-06-17-web-learn-microsoft-com-build-a-multiple-agent-workflow-automation-solution-by-using-microsoft-agent-frame.md`. confidence: 1 Microsoft Architecture Center source, last-confirmed 2026-06-17.

### Typed entities
- package: `Asp.Versioning` v10
- package: `Asp.Versioning.OpenApi`
- package: `Microsoft.AspNetCore.OpenApi`
- API: `WithDocumentPerVersion()`
- tool: SwaggerUI
- tool: Scalar
- tool: Spectral
- tool: oasdiff
- concept: tenant-specific model
- concept: shared model
- concept: tuned shared model
- service: Microsoft Foundry
- service: Azure Machine Learning
- framework: Microsoft Agent Framework
- platform: Azure Container Apps

### Explicit relationships
- Versioned OpenAPI depends-on the API explorer grouping and document-per-version generation matching the API versioning strategy.
- OpenAPI diffing complements API versioning by detecting accidental breaking changes before release.
- Tenant-specific models supersede shared-model reuse when tenant data sensitivity, contractual rules, or cross-tenant transfer risk dominate.
- Shared and tuned shared models depend-on tenant consent and data minimization when tenant data contributes to training or adaptation.
- Custom Agent Framework orchestration complements Foundry Agent Service when the workload needs deterministic control over compute, state, and workflow transitions.

### HoneyDrunk implications
- For .NET APIs that publish OpenAPI, make versioning and OpenAPI generation one contract; add schema diff checks before client-facing changes.
- For HoneyDrunk.Payments/NovOutbox-style APIs, prefer explicit versioning over silent default-version behavior when external consumers depend on contracts.
- If HoneyDrunk builds tenant-aware AI features, decide early whether data/model isolation is tenant-specific, shared, or tuned-shared; document data-use consent and opt-out behavior.
- Use managed Foundry-style agents only when prompt-defined behavior is enough; keep custom code orchestration for workflows that need deterministic boundaries and reviewable state.

### Quality notes
- The API-versioning source is a .NET Blog guest post with concrete code and comments; verify package versions at implementation time. Microsoft Architecture Center sources are useful Azure-centered patterns, not a mandate to adopt Azure control planes.

## 2026-06-18 compile additions: MSBuild MCP diagnostics, MCP C# SDK updates, and Azure AI technology selection

### Source-backed claims
- Microsoft Binlog MCP Server gives AI assistants direct MCP access to MSBuild binary logs through tools for overview, errors, warnings, search, projects, properties, items, imports, property explanation, embedded file reading/search, performance hot spots, and two-build comparison. Source: `raw/2026-06-18-web-devblogs-microsoft-com-ai-powered-msbuild-investigation-with-the-micro.md`. confidence: 1 official .NET Blog source, last-confirmed 2026-06-18.
- The Binlog MCP Server is distributed through the `dotnet-msbuild` plugin in the .NET Agent Skills repository and can also be wired directly as a stdio MCP server with `dotnet tool run Microsoft.AITools.BinlogMcp`. Source: `raw/2026-06-18-web-devblogs-microsoft-com-ai-powered-msbuild-investigation-with-the-micro.md`. confidence: 1 source, last-confirmed 2026-06-18.
- The MCP C# SDK update adds support for MCP protocol version 2025-06-18, including elicitation, structured tool output, resource links, metadata improvements, and tool titles. Source: `raw/2026-06-18-web-devblogs-microsoft-com-mcp-c-sdk-gets-major-update-support-for-protoco.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 official .NET Blog source, last-confirmed 2026-06-18.
- Microsoft Architecture Center's AI services selection page groups Foundry Agent Service, Foundry Models, observability, RAG components, targeted language processing, speech, image/video processing, content safety, custom Azure Machine Learning models, and Foundry Local/on-device inference as distinct technology choices. Source: `raw/2026-06-18-web-learn-microsoft-com-choose-an-azure-ai-technology-azure-architecture-c.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-18.

### Typed entities
- tool/server: Microsoft Binlog MCP Server
- plugin: `dotnet-msbuild`
- tool: `Microsoft.AITools.BinlogMcp`
- file type: `.binlog`
- library: MCP C# SDK
- service: Foundry Agent Service
- service: Foundry Models
- service: Azure AI Search
- service: Azure Document Intelligence
- service: Azure Content Understanding
- service: Foundry Local
- platform: Azure Machine Learning

### Explicit relationships
- Binlog MCP diagnostics complement .NET build troubleshooting by exposing structured MSBuild state to coding agents.
- Structured MCP output in the C# SDK complements .NET agent tools by reducing free-text parsing and clarifying result contracts.
- Foundry prebuilt services complement custom Azure Machine Learning when workloads need low-setup intelligent functions; custom ML supersedes prebuilt services when exclusive data, custom model types, lineage, or training control dominate.
- Foundry Local complements cloud Foundry services when privacy, latency, offline behavior, or cost makes on-device inference preferable.

### HoneyDrunk implications
- For .NET build failures, consider capturing `.binlog` files and using structured analysis before asking agents to infer MSBuild behavior from console output alone.
- Any HoneyDrunk MCP server written in C# should target structured outputs and explicit auth/resource boundaries where the current SDK supports them.
- Use Azure AI service-selection guidance as a decision checklist, not a default architecture: prebuilt service, custom ML, RAG, local inference, and content-safety needs should be chosen per workload.

### Quality notes
- Microsoft Learn and .NET Blog are authoritative for Microsoft tooling direction but time-sensitive for package versions and preview status.

## 2026-06-19 compile additions: AGT MCP governance and Copilot modernization assessment

### Source-backed claims
- The .NET Agent Governance Toolkit examples show MCP governance as a pipeline around tool definitions, tool-call decisions, response sanitization, YAML policy, audit events, and OpenTelemetry metrics. Source: `raw/2026-06-19-web-devblogs-microsoft-com-governing-mcp-tool-calls-in-net-with-the-agent-governance-toolk.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 .NET Blog source, last-confirmed 2026-06-19.
- The captured AGT .NET source says the package targets .NET 8.0+, is MIT-licensed, has a direct `YamlDotNet` dependency in the examples, and requires no external services for local examples. Source: `raw/2026-06-19-web-devblogs-microsoft-com-governing-mcp-tool-calls-in-net-with-the-agent-governance-toolk.md`. confidence: 1 source, last-confirmed 2026-06-19.
- GitHub Copilot modernization for .NET and Java follows an Assess -> Plan -> Execute workflow where assessment documents drive later infrastructure planning, IaC, containerization, and deployment decisions. Source: `raw/2026-06-19-web-devblogs-microsoft-com-your-migration-s-source-of-truth-the-modernization-assessment.md`. confidence: 1 .NET Blog source, last-confirmed 2026-06-19.
- Modernization assessment reports are stored under `.github/modernize/assessment/`, each run creates an independent report, and reports can be exported, imported, compared, and used as the bridge into plan files and task lists under `.github/modernize/{plan-name}/`. Source: `raw/2026-06-19-web-devblogs-microsoft-com-your-migration-s-source-of-truth-the-modernization-assessment.md`. confidence: 1 source, last-confirmed 2026-06-19.

### Typed entities
- framework: Microsoft Agent Governance Toolkit / AGT
- component: `GovernanceKernel`
- package dependency: `YamlDotNet`
- product: GitHub Copilot modernization
- artifact directory: `.github/modernize/assessment/`
- artifact directory: `.github/modernize/{plan-name}/`
- artifact: `plan.md`
- artifact: `tasks.json`
- migration phase: Assess -> Plan -> Execute

### Explicit relationships
- AGT MCP governance complements the MCP C# SDK by adding policy, audit, and sanitizer layers around tool use.
- YAML policy files allow governance decisions to change without scattering security rules through application code.
- Copilot modernization assessment documents feed downstream IaC, containerization, and deployment planning.
- Independent assessment reports create migration history and enable side-by-side target-compute comparison.

### HoneyDrunk implications
- For .NET agent apps, keep governance policy, scanner thresholds, and audit sinks as first-class code review artifacts.
- Treat modernization-agent outputs as generated proposals: require review of assessment findings before allowing plan execution or IaC/container changes.
- If HoneyDrunk migrates legacy .NET apps, preserve assessment reports in-repo only after checking for secrets, internal topology, and customer data.

### Quality notes
- Microsoft sources are implementation/product guidance. Validate package names, licensing, extension behavior, and generated artifact schemas before adopting in active repos.
