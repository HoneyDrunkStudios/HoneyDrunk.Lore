# Microsoft .NET AI Stack

## Decision-useful summary
Microsoft's .NET AI story is converging around composable abstractions: `Microsoft.Extensions.AI` for provider-agnostic chat/model access, `Microsoft.Extensions.DataIngestion` and `Microsoft.Extensions.VectorData` for knowledge/RAG layers, MCP for external context/tool exposure, and Microsoft Agent Framework for agent orchestration. The pattern is attractive for HoneyDrunk .NET services because it reduces direct provider lock-in and makes app-level AI features feel like normal dependency-injected infrastructure. [source: raw/2026-05-03-rss-dotnet-ai-conference-app-composable-stack.md]

## Claims
- ConferencePulse, a Blazor Server conference assistant, used `Microsoft.Extensions.AI`, `Microsoft.Extensions.DataIngestion`, `Microsoft.Extensions.VectorData`, MCP, and Microsoft Agent Framework together for polls, Q&A, insights, and summaries. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-dotnet-ai-conference-app-composable-stack.md]
- `Microsoft.Extensions.AI` presents a stable `IChatClient` abstraction across model providers, allowing application code to avoid binding directly to one provider client. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-dotnet-ai-conference-app-composable-stack.md]
- The .NET AI conference-app pattern uses ingestion plus vector storage as the knowledge layer for RAG across multiple sources. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-dotnet-ai-conference-app-composable-stack.md]
- Azure MCP Server 2.0 exposes Azure resources as MCP tools; it reports 276 tools across 57 Azure services and adds self-hosted remote MCP server support. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-azure-blog-announcing-azure-mcp-server-2-0-stable-release-for-self-hos.md]
- Daily Discord announcement captures for Aspire, Microsoft Community, Microsoft Foundry, and .NET/C# were ingested but contained mostly browser/UI scaffolding rather than decision-grade announcement content. confidence: 8 sources, last-confirmed 2026-05-05. [sources: raw/2026-05-04-clipper-discord-aspire.md; raw/2026-05-04-clipper-discord-microsoft-community.md; raw/2026-05-04-clipper-discord-microsoft-foundry.md; raw/2026-05-04-clipper-discord-net-c.md; raw/2026-05-05-clipper-discord-aspire.md; raw/2026-05-05-clipper-discord-microsoft-community.md; raw/2026-05-05-clipper-discord-microsoft-foundry.md; raw/2026-05-05-clipper-discord-net-c.md]

## Typed entities
- project/library: Microsoft.Extensions.AI
- project/library: Microsoft.Extensions.DataIngestion
- project/library: Microsoft.Extensions.VectorData
- project/library: Microsoft Agent Framework
- project/service: Azure MCP Server 2.0
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
- [[AI Agent Harnesses]] uses MCP servers as a tool/context integration layer.

## HoneyDrunk implications
- For .NET services, start with `IChatClient` and ingestion/vector abstractions if provider portability matters.
- Azure MCP Server is a candidate for controlled cloud-automation agents, but it should be permission-scoped and audited before production use.

## Confidence and quality notes
- Quality posture: decision-usable for directional stack choices; implementation details should be verified against package docs before coding.
- Weak spots: Microsoft/Azure blog sources are vendor-authored and optimistic.
- Privacy filter: Discord captures were summarized only at high level; no private chat/user details were copied.
