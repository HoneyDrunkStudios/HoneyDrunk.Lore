# Microsoft .NET AI Stack

## Decision-useful summary
Microsoft's .NET AI story is converging around composable abstractions: `Microsoft.Extensions.AI` for provider-agnostic chat/model access, `Microsoft.Extensions.DataIngestion` and `Microsoft.Extensions.VectorData` for knowledge/RAG layers, MCP for external context/tool exposure, and Microsoft Agent Framework / Foundry agent tooling for agent orchestration. The May 2026 additions make the stack more production-shaped: Microsoft Agent Framework 1.0 supports sessions, tools, context providers, graph workflows, human approvals, and durable execution through Durable Task/Azure Functions hosting. The pattern is attractive for HoneyDrunk .NET services because it reduces direct provider lock-in and makes app-level AI features feel like normal dependency-injected infrastructure. [sources: raw/2026-05-03-rss-dotnet-ai-conference-app-composable-stack.md; raw/2026-05-07-youtube-microsoft-developer-youtube-foundry-toolkit-series-3-building-an-agent.md; raw/2026-05-09-rss-net-blog-microsoft-agent-framework-building-blocks-for-ai-part-3.md; raw/2026-05-09-rss-net-blog-durable-workflows-in-the-microsoft-agent-framework.md]

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
- [[AI Agent Harnesses]] uses MCP servers as a tool/context integration layer.
- [[Azure Agent Automation and Identity]] uses Microsoft Foundry, MCP, and Azure infrastructure as deployment context for C# agents.

## HoneyDrunk implications
- For .NET services, start with `IChatClient` and ingestion/vector abstractions if provider portability matters.
- For multi-step agents that must survive restarts or human waits, prefer Microsoft Agent Framework durable workflows over ad-hoc background loops.
- Azure Functions hosting is promising when a workflow should be callable by HTTP or MCP without hand-written controller/orchestrator glue.
- Azure MCP Server is a candidate for controlled cloud-automation agents, but it should be permission-scoped and audited before production use.
- Foundry Toolkit may be useful for prototype-to-code agent scaffolding if generated code can be inspected and brought under normal HoneyDrunk gates.

## Confidence and quality notes
- Quality posture: decision-usable for directional stack choices; implementation details should be verified against package docs before coding.
- Weak spots: Microsoft/Azure blog sources are vendor-authored and optimistic.
- Privacy filter: Discord captures were summarized only at high level; no private chat/user details were copied.
