# MCP Tool Governance and App Surfaces

## Decision-useful summary
MCP adoption is moving from “connect any server” toward governed, portable tool surfaces. Docker's Custom MCP Catalogs and Profiles separate organization-approved MCP server supply from individual/team work-mode composition, and both can be distributed as OCI artifacts. Microsoft’s MCP Inspector signal reinforces the complementary developer loop: test tools and app widgets locally before binding them into assistant clients. For HoneyDrunk, the useful pattern is catalog → profile → local validation → client deployment, with secrets/network/tool-surface controls handled outside the prompt. [sources: raw/2026-05-21-rss-docker-blog-custom-mcp-catalogs-and-profiles-advancing-enterprise-mcp-.md; raw/2026-05-21-youtube-microsoft-developer-youtube-test-your-mcp-app-ui-locally-react-fluent-.md]

## Claims
- Docker Custom MCP Catalogs let organizations curate approved MCP servers, including Docker MCP Catalog entries, community servers, and internally built servers, and distribute them as immutable OCI artifacts via container registries. confidence: 1 vendor source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-docker-blog-custom-mcp-catalogs-and-profiles-advancing-enterprise-mcp-.md]
- Custom catalogs can reference Docker catalog servers such as Playwright, GitHub, Context7, Atlassian, Notion, and Markitdown, plus a custom server described by YAML metadata and packaged as a Docker image. confidence: 1 vendor source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-docker-blog-custom-mcp-catalogs-and-profiles-advancing-enterprise-mcp-.md]
- Docker MCP Profiles are named groupings of MCP servers for workflows such as coding or planning; profiles can persist server configuration, connect to agent clients, disable individual tools to reduce context, and be pushed/pulled as OCI artifacts. confidence: 1 vendor source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-docker-blog-custom-mcp-catalogs-and-profiles-advancing-enterprise-mcp-.md]
- Docker frames future MCP governance around policy controls restricting usage to approved catalogs/trusted sources, profile-scoped secrets/configuration, better discoverability/sharing, and pairing profiles with agent skills. confidence: 1 vendor source, last-confirmed 2026-05-21. [source: raw/2026-05-21-rss-docker-blog-custom-mcp-catalogs-and-profiles-advancing-enterprise-mcp-.md]
- Microsoft Developer's MCP Inspector short says developers can run `npx @modelcontextprotocol/inspector`, connect local or hosted MCP servers, validate raw tool calls, and load/interact with a React Fluent UI app widget locally. confidence: 1 YouTube metadata source, last-confirmed 2026-05-21. [source: raw/2026-05-21-youtube-microsoft-developer-youtube-test-your-mcp-app-ui-locally-react-fluent-.md]

## Typed entities
- protocol: Model Context Protocol
- product: Docker MCP Catalog
- feature: Custom MCP Catalogs
- feature: Docker MCP Profiles
- product/tool: Docker Desktop
- command group: `docker mcp catalog`
- command group: `docker mcp profile`
- artifact format: OCI artifact
- registry: Docker Hub / container registry
- MCP server: Playwright
- MCP server: GitHub official
- MCP server: Context7
- MCP server: Atlassian
- MCP server: Notion
- MCP server: Markitdown
- example MCP server: roll-dice
- assistant client: Claude Code
- tool: MCP Inspector
- UI framework: React Fluent UI
- concept: MCP app widget
- concept: profile-scoped secrets
- concept: tool-surface minimization

## Explicit relationships
- Custom MCP Catalogs use OCI registries to distribute approved MCP server lists.
- MCP Profiles depend-on catalogs and server configuration to compose workflow-specific tool surfaces.
- MCP Profiles reduce context pressure by disabling irrelevant tools for a task/profile.
- Organization governance uses Custom Catalogs; day-to-day developer workflow uses Profiles.
- MCP Inspector uses local/hybrid MCP server connections to validate tool calls and app widgets before client deployment.
- Profile-scoped secrets supersede ad-hoc project-level `mcp.json` secrets when stronger isolation/configuration reuse is needed.
- [[AI Agent Harnesses]] uses MCP governance as part of tool, context, and permission management.
- [[microsoft-dotnet-ai-stack]] uses MCP app samples and Inspector-style validation for app-surface development.

## HoneyDrunk implications
- Define small OpenClaw/Grid profiles for modes like coding, planning, sourcing, Lore ingest, and browser QA; avoid loading every tool into every session.
- If using external MCP servers, promote trusted ones into an approved catalog and record provenance/version/source before team reuse.
- Validate MCP app widgets with MCP Inspector before integrating them into a client; broken widget/tool round trips should fail locally.
- Keep secrets and network policy as runtime/profile infrastructure, not as prompt instructions.

## Confidence and quality notes
- Quality posture: decision-usable as an MCP governance pattern; Docker claims are vendor-authored and should be validated in the local Windows/OpenClaw environment before standardization.
- Weak spots: Microsoft source is YouTube metadata for a short, not detailed documentation; use it as a pointer to Inspector workflow, then verify against official MCP docs/labs.
- Privacy filter: no secrets or private server names copied; example Docker Hub namespace from raw omitted because it is not decision-relevant.
