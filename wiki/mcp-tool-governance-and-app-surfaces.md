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

## 2026-05-22 compile additions

### Claims
- Microsoft.AgentGovernance.Extensions.ModelContextProtocol is a Public Preview .NET 8+ package for the official MCP C# SDK that adds `WithGovernance(...)` to `IMcpServerBuilder` for startup scanning, policy enforcement, runtime tool-call governance, response sanitization, audit, and metrics. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-announcing-agent-governance-toolkit-mcp-extensions-for-net.md]
- The MCP governance extension is designed to fail closed by default: startup tool scanning, unsafe-tool failure, response sanitization, fallback-handler governance, audit, and metrics are enabled by default in the described options. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-announcing-agent-governance-toolkit-mcp-extensions-for-net.md]
- The built-in scanner targets MCP tool-definition risks including tool poisoning, typosquatting, hidden instructions, rug pulls, schema abuse, cross-server attacks, and description injection; detection still depends on threshold tuning and threat model. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-announcing-agent-governance-toolkit-mcp-extensions-for-net.md]
- Runtime MCP policy can allow, deny, or rate-limit tool calls using YAML-backed Agent Governance policies and authenticated/default agent identities. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-announcing-agent-governance-toolkit-mcp-extensions-for-net.md]
- The response sanitizer scans tool output for prompt-injection tags, override phrasing, credential leakage patterns, and exfiltration-oriented URLs before model return, but sanitizer effectiveness depends on local pattern tuning. confidence: 1 vendor source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-announcing-agent-governance-toolkit-mcp-extensions-for-net.md]

### Typed entities
- package: `Microsoft.AgentGovernance.Extensions.ModelContextProtocol`
- SDK: official MCP C# SDK
- API: `IMcpServerBuilder.WithGovernance(...)`
- config: `McpGovernanceOptions`
- policy format: YAML Agent Governance policy
- identity: agent DID
- control: startup tool-definition scanning
- control: runtime policy enforcement
- control: response sanitization
- control: audit and metrics
- threat: tool poisoning
- threat: typosquatting
- threat: description injection
- threat: schema abuse

### Explicit relationships
- `WithGovernance(...)` extends MCP C# SDK builder pipelines without requiring a forked SDK or proxy process.
- Startup scanning supersedes exposing unvetted MCP tool metadata to clients when unsafe definitions are detected.
- Runtime policy enforcement depends-on agent identity and YAML policy rules.
- Response sanitization complements, but does not replace, execution-layer sandboxing and least-privilege tool design.
- [[microsoft-dotnet-ai-stack]] uses MCP governance extensions as .NET-specific production-hardening signal.

### HoneyDrunk implications
- If HoneyDrunk builds .NET MCP servers, governance should be a default builder-layer concern, not ad hoc per-tool checks.
- Keep policy files outside application code so agent/tool authorization can change without redeploying binaries.
- Treat Microsoft defaults as a baseline; tune risk thresholds and sanitizer patterns with HoneyDrunk-specific false-positive/false-negative tests.

## 2026-05-30 compile additions

### Claims
- OpenAI Secure MCP Tunnel lets supported OpenAI surfaces reach private MCP servers without public inbound access by running `tunnel-client` inside the network; the client long-polls OpenAI over outbound HTTPS, forwards JSON-RPC requests to a local stdio or HTTP MCP server, and returns responses through the same tunnel. confidence: 1 official vendor docs source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-openai-secure-mcp-tunnel.md]
- Secure MCP Tunnel requires tunnel identity, a runtime API key with tunnel read/use permissions, outbound HTTPS to OpenAI, and local reachability to the private MCP server; optional controls include outbound proxies, custom CA bundles, control-plane mTLS, and MCP-side mTLS. confidence: 1 official vendor docs source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-openai-secure-mcp-tunnel.md]
- OpenAI's Harpoon embedded MCP server can expose narrowly allowlisted private HTTP targets through the tunnel, but is explicitly not a general-purpose proxy because callers cannot choose arbitrary hosts and request/response limits are bounded. confidence: 1 official vendor docs source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-openai-secure-mcp-tunnel.md]
- Azure Container Apps dynamic sessions can expose a platform-managed MCP server for shell session pools in preview, with built-in `launchShell` and `runShellCommandInRemoteEnvironment` tools authenticated by an `x-ms-apikey` header. confidence: 1 Microsoft Learn source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-tutorial-use-mcp-with-dynamic-sessions-shell.md]

### Typed entities
- product: OpenAI Secure MCP Tunnel
- binary/tool: `tunnel-client`
- endpoint family: `/v1/tunnel/*`
- control: outbound-only HTTPS
- control: control-plane mTLS
- embedded MCP server: Harpoon
- platform: Azure Container Apps dynamic sessions
- tool: `launchShell`
- tool: `runShellCommandInRemoteEnvironment`
- auth header: `x-ms-apikey`

### Explicit relationships
- Secure MCP Tunnel uses an outbound client to keep private MCP servers off the public internet while exposing a supported OpenAI MCP request path.
- Tunnel runtime keys depend-on scoped tunnel read/use permissions and should be treated as secrets.
- Allowlisted HTTP callouts complement MCP tools but do not supersede proper private API authorization.
- Azure dynamic-session MCP uses platform-managed shell execution environments rather than custom MCP server code.
- [[ai-agent-harnesses]] depends-on private-tool connectivity patterns when agents need network-internal tools.

### HoneyDrunk implications
- For private HoneyDrunk MCP servers, compare OpenAI Secure MCP Tunnel, Cloudflare-style self-managed sandboxes, and Azure Container Apps dynamic sessions by trust boundary, logging, mTLS, key handling, and local Windows/dev ergonomics.
- Do not commit local MCP API keys or tunnel runtime keys in `.vscode/mcp.json` or equivalent project files; prefer environment variables or secret stores.
- Treat tunneled private HTTP targets as a small allowlist with explicit method and response limits, not a backdoor proxy into the network.

## 2026-05-31 compile additions

### Claims
- Azure MCP Server is now distributed as platform-specific MCP Bundles (`.mcpb`) that package a manifest, server binary, and dependencies so Claude Desktop and compatible clients can install the server without Node.js, Python, .NET SDK, or Docker. confidence: 1 Microsoft Azure blog source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-azure-blog-azure-mcp-server-now-available-as-an-mcp-bundle-mcpb.md]
- Azure MCP Server MCPB exposes the same Azure MCP Server capabilities as other install methods, including 100+ Azure service tools, Azure CLI command generation, infrastructure guidance, architecture recommendations, and diagnostics. confidence: 1 Microsoft Azure blog source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-azure-blog-azure-mcp-server-now-available-as-an-mcp-bundle-mcpb.md]
- The MCPB installation path improves end-user setup but increases the importance of bundle provenance, platform matching, client extension trust, Azure credential scope, and tool/profile governance because the server can reach real Azure resources after authentication. confidence: 1 Microsoft Azure blog source plus compile judgment, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-azure-blog-azure-mcp-server-now-available-as-an-mcp-bundle-mcpb.md]
- Hugging Face community discussion in the agent glossary frames MCP as a protocol that standardizes the tool-use to harness connection, reinforcing MCP as a harness/tool-call interface rather than the agent itself. confidence: 1 source with community discussion, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-hugging-face-blog-harness-scaffold-and-the-ai-agent-terms-worth-gettin.md]

### Typed entities
- package format: MCP Bundle / `.mcpb`
- product: Azure MCP Server
- client: Claude Desktop
- runtime: Node.js
- runtime: Python
- runtime: .NET SDK
- runtime: Docker Engine
- concept: bundle provenance
- concept: MCP as tool-use interface

### Explicit relationships
- MCP Bundles package MCP servers and dependencies into client-installable artifacts.
- Azure MCP Server MCPB supersedes runtime-specific setup for Claude Desktop users who need low-friction installation.
- Easy MCP installation depends-on stronger catalog/profile governance because install friction is no longer a meaningful safety barrier.
- MCP standardizes tool-call interoperability between a harness and external capabilities.

### HoneyDrunk implications
- If HoneyDrunk uses `.mcpb` packages, require source, release, platform, hash/signature if available, and approved-tool profile review before broad use.
- For Azure MCP, authenticate with least-privilege Azure identities; a convenient bundle still exposes powerful cloud-management tools.

## 2026-06-01 compile additions

### Claims
- Microsoft Learn distinguishes two Azure Container Apps MCP hosting/auth models: standalone container apps use built-in authentication backed by Microsoft Entra ID and bearer tokens, while platform-managed dynamic-session MCP uses an opaque API key in the `x-ms-apikey` header scoped to the session pool. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-secure-mcp-servers-on-azure-container-apps.md]
- For standalone MCP servers, Microsoft recommends network restrictions or VNet integration, rate limiting, tool-argument validation, trusted CORS origins for web clients, and bearer-token client configuration that keeps tokens out of committed config. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-secure-mcp-servers-on-azure-container-apps.md]
- For dynamic-session MCP, Microsoft warns that the API key grants access to all tools and sessions in the pool; recommended controls include Hyper-V-isolated sessions, egress control, short idle cooldowns, Key Vault or Container Apps secret storage, and key rotation awareness because validation results can be cached briefly after regeneration. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-secure-mcp-servers-on-azure-container-apps.md]

### Typed entities
- platform: Azure Container Apps
- hosting model: standalone MCP server
- hosting model: dynamic sessions MCP
- auth mechanism: Microsoft Entra ID bearer token
- auth mechanism: `x-ms-apikey`
- control: CORS trusted origins
- control: VNet integration / IP restrictions
- control: session-pool API key rotation
- control: Hyper-V-isolated container session

### Explicit relationships
- Standalone MCP servers depend-on application-owned auth, authorization, rate limiting, and input validation.
- Dynamic-session MCP depends-on session-pool API-key custody because one key can create environments and execute code across the pool.
- Auth-header choice depends-on MCP hosting model; `x-ms-apikey` and bearer-token authentication are not interchangeable.

### HoneyDrunk implications
- For private HoneyDrunk MCP servers, document the hosting model and auth header explicitly in profile/catalog metadata.
- Treat session-pool API keys as high-risk secrets; never commit them to `.vscode/mcp.json`, repo settings, or shared wiki pages.

## 2026-06-02 compile additions

### Claims
- Google announced a Google Pay & Wallet Developer MCP server that lets AI development assistants search official Pay/Wallet documentation, access integration/account details, validate or amend Wallet pass JWT/JSON definitions, inspect integration metrics/errors, and create/configure integrations from the development environment. confidence: 1 Google Developers source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-google-developers-blog-supercharge-your-integration-workflow-with-the-.md]
- The Google Pay & Wallet MCP server reinforces a pattern where vendor MCP servers are not generic docs search: they may combine RAG documentation, authenticated account state, validation tools, metrics, and mutating setup actions, so catalog/profile governance must distinguish read-only and write-capable tools. confidence: 1 source plus compile judgment, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-google-developers-blog-supercharge-your-integration-workflow-with-the-.md]

### Typed entities
- product: Google Pay & Wallet Developer MCP server
- protocol: Model Context Protocol
- tool: `search_documentation`
- capability: Wallet pass JWT/JSON validation
- capability: merchant/integration account inspection
- capability: integration metrics/error inspection
- capability: merchant account and integration creation
- assistant clients: Antigravity, Cursor, Visual Studio Code

### Explicit relationships
- Vendor MCP servers use authenticated account state and official documentation to ground agent output.
- Pay/Wallet MCP validation tools complement integration testing by catching pass-definition errors before application use.
- Mutating MCP tools depend-on profile-level approval, identity scope, and audit logging because they can create or configure payment integrations.

### HoneyDrunk implications
- Catalog vendor MCP servers with per-tool capability labels: docs-only, account-read, validation, metrics, and mutating configuration.
- Do not expose payment or wallet setup tools to broad coding profiles without scoped credentials and explicit approval gates.

## 2026-06-03 compile additions

### Claims
- Google AI Edge Gallery now supports experimental MCP over Streamable HTTP on Android, dynamically importing tool definitions and resource schemas into an on-device model prompt while reasoning/tool selection happens locally on the phone. confidence: 1 Google Developers source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-google-developers-blog-a-smarter-google-ai-edge-gallery-mcp-integratio.md]
- Google recommends short MCP tool descriptions and bite-sized returned data for on-device models because mobile context windows and latency budgets are smaller than server-side frontier models. confidence: 1 Google Developers source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-google-developers-blog-a-smarter-google-ai-edge-gallery-mcp-integratio.md]
- Azure Cosmos DB MCP Toolkit v1.1.2 is generally available with Microsoft Foundry catalog integration, Entra ID/RBAC/managed identity support, multi-provider embeddings, structured 403 responses, startup validation, and `/mcp` HTTP transport compatibility. confidence: 1 Microsoft Azure Cosmos DB Blog source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-azure-cosmos-db-blog-azure-cosmos-db-mcp-toolkit-is-now-generally-avai.md]
- The Cosmos DB MCP Toolkit exposes database discovery, container listing, recent-document retrieval, ID lookup, text search, vector search, and approximate-schema sampling tools, making production databases directly reachable by agents through MCP. confidence: 1 Microsoft source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-azure-cosmos-db-blog-azure-cosmos-db-mcp-toolkit-is-now-generally-avai.md]
- DigitalOcean Serverless Inference supports remote MCP tools in inference requests, including authenticated MCP servers and `allowed_tools` constraints, which reinforces MCP as a provider-level tool-routing surface as well as a local agent-client protocol. confidence: 1 DigitalOcean source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-digitalocean-digitalocean-serverless-inference-a-deep-dive.md]

### Typed entities
- app: Google AI Edge Gallery
- protocol transport: MCP Streamable HTTP
- model: Gemma 4
- product: Azure Cosmos DB MCP Toolkit v1.1.2
- product/platform: Microsoft Foundry
- service: Azure Cosmos DB
- auth: Microsoft Entra ID / RBAC / managed identity
- tool: `list_databases`
- tool: `list_collections`
- tool: `get_recent_documents`
- tool: `find_document_by_id`
- tool: `text_search`
- tool: `vector_search`
- tool: `get_approximate_schema`
- product: DigitalOcean Serverless Inference
- request field: `allowed_tools`

### Explicit relationships
- On-device MCP uses external servers for execution while local models decide tool selection, so privacy depends-on both local reasoning boundaries and remote tool/data policy.
- MCP tool descriptions and response size depend-on the model context/latency budget of the client, especially on mobile.
- Cosmos DB MCP Toolkit uses RBAC/managed identity to constrain database access but still depends-on profile-level capability governance because database tools can reveal or mutate production context depending on implementation.
- Provider-hosted inference APIs can act as MCP clients, so MCP governance must cover both local desktop clients and model-provider request surfaces.

### HoneyDrunk implications
- Label MCP tools by execution location and data sensitivity: local-device reasoning, local server, cloud server, production database read, production database write, and external network action.
- Do not connect production Cosmos DB MCP tools to broad coding profiles without read/write separation, scoped identities, schema/data redaction rules, and audit logging.
- For on-device/mobile agent experiments, keep tool descriptions compact and return summarized data; mobile MCP usability will fail if server tools dump large records into small contexts.

### Quality notes
- Microsoft and Google sources are vendor-authored but concrete implementation signals. Validate current toolkit versions, Foundry catalog behavior, and auth defaults before production database access.

## 2026-06-04 compile additions

### Claims
- Foundry Toolboxes give agents a managed endpoint for tool types, with skills as versioned project-scoped catalog entries discoverable as MCP resources and tool search for selecting task-relevant tools instead of exposing the full surface. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-and-run-agents-at-scale-with-microsoft-fo.md]
- Foundry IQ is generally available as a knowledge layer behind Foundry agents, unifying Work IQ, Fabric IQ, Azure SQL, File Search, and MCP sources behind a retrieval endpoint; this makes retrieval sources part of the governed tool surface. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-and-run-agents-at-scale-with-microsoft-fo.md]
- Azure Cosmos DB Build 2026 announcements reinforce that database MCP governance is expanding beyond connection: MCP Toolkit is GA, Agent Kit adds 100+ coding-agent best-practice rules, Agent Memory Toolkit is in public preview, and semantic reranking improves RAG retrieval quality. confidence: 1 Microsoft Azure Cosmos DB source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-azure-cosmos-db-blog-announced-at-ms-build-2026-azure-cosmos-db-mcp-to.md]
- Cosmos DB Global Secondary Indexes are GA and can isolate query/vector/full-text workloads from transactional source containers, which matters when agents use operational databases for retrieval or memory. confidence: 1 Microsoft Azure Cosmos DB source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-azure-cosmos-db-blog-announced-at-ms-build-2026-azure-cosmos-db-mcp-to.md]

### Typed entities
- product: Foundry Toolboxes
- feature: Skills in Toolboxes
- feature: Tool search
- product: Foundry IQ
- product: Work IQ
- product: Fabric IQ
- product: Azure Cosmos DB Agent Kit
- product: Azure Cosmos DB Agent Memory Toolkit
- feature: Semantic Reranking
- feature: Global Secondary Indexes / GSI

### Explicit relationships
- Toolboxes use managed endpoints and project-scoped catalogs to govern agent tool discovery.
- Tool search reduces tool-surface exposure by selecting relevant tools per task.
- Foundry IQ uses MCP and enterprise data sources as governed retrieval inputs.
- Cosmos DB Agent Kit uses rule-based guidance to steer coding agents toward database best practices.
- Global Secondary Indexes complement agent retrieval by isolating secondary query patterns from transactional containers.

### HoneyDrunk implications
- Catalog MCP/tool entries with capability class, data source, identity scope, mutability, and retrieval size limits.
- Treat "tool search" as a governance feature only if the underlying catalog is already curated; search over unsafe tools still exposes unsafe tools.
- For database-backed agents, separate operational writes, read-only retrieval, schema sampling, memory storage, and vector/full-text workloads by identity and container/index policy.

## 2026-06-05 compile additions

### Claims
- Foundry IQ knowledge bases are generally available with a Foundry IQ MCP server that exposes governed knowledge bases to any MCP-compatible host, including Claude, ChatGPT, LangChain, and Microsoft Agent Framework. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-foundry-iq-build-smarter-agents-faster-with-unified-knowledge-and-server.md]
- Foundry IQ can treat MCP servers themselves as knowledge sources inside a multi-source knowledge base, so MCP is both an access protocol for agents and an ingest/retrieval source inside Microsoft's knowledge layer. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-foundry-iq-build-smarter-agents-faster-with-unified-knowledge-and-server.md]
- Microsoft Fabric Build 2026 says Fabric IQ tools and skills are accessible through GitHub Copilot CLI via Agent Skills for Fabric, letting terminal agents query Power BI reports and semantic models through governed Fabric context. confidence: 1 Microsoft Fabric source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-mic.md]
- Anthropic's Agent SDK credit article states third-party apps can authenticate with a user's Claude subscription through the Agent SDK, which makes app/SDK authentication mode part of tool-governance and billing policy. confidence: 1 Anthropic Help Center source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-use-the-claude-agent-sdk-with-your-claude-plan.md]

### Typed entities
- product: Foundry IQ MCP server
- product: Fabric IQ
- tool package: Agent Skills for Fabric
- client: GitHub Copilot CLI
- data product: Power BI semantic model
- SDK: Claude Agent SDK
- concept: subscription-authenticated third-party app

### Explicit relationships
- Foundry IQ MCP server uses MCP as a governed retrieval interface.
- MCP servers can also serve as inputs to multi-source knowledge bases, so provenance and capability metadata matter on both ingress and egress.
- Agent Skills for Fabric expose governed Fabric/Power BI context to coding-agent CLIs.
- Third-party Agent SDK apps depend-on user subscription authentication and plan-specific billing/credit rules.

### HoneyDrunk implications
- Catalog knowledge MCP servers separately from action MCP servers: retrieval-only knowledge sources still need source provenance, sensitivity labels, indexing status, and citation behavior.
- If using Fabric/Power BI agent skills, label them as business-data tools with strict identity, audit, and export controls rather than generic coding helpers.
- For third-party Agent SDK apps, record whether the app bills through individual subscription credits or an organization API key before team use.

### Quality notes
- Microsoft and Anthropic claims are product/platform documentation. Verify current auth headers, workspace admin controls, and data-retention terms before connecting private HoneyDrunk data.

## 2026-06-07 compile additions

### Claims
- Reachy Mini remote tools show a narrow MCP governance pattern: built-in robot tools remain local/trusted, shareable stateless capabilities can run as public Hugging Face Gradio Spaces, and profiles decide which local or remote tools are active. confidence: 1 Hugging Face/Pollen Robotics source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-adding-mcp-tools-to-reachy-mini.md]
- Reachy Mini remote Space installation validates the Space on the Hub, probes the standard Gradio `/gradio_api/mcp/` endpoint, discovers tools, namespaces local tool IDs, persists installed sources, and fails fast on name collisions. confidence: 1 source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-adding-mcp-tools-to-reachy-mini.md]
- The current Reachy Mini remote-tool path supports public MCP-compatible Gradio Spaces but not private/authenticated Spaces, non-Gradio Spaces, arbitrary raw MCP URLs, or guaranteed parallel tool orchestration. confidence: 1 source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-adding-mcp-tools-to-reachy-mini.md]
- GitHub enterprise-managed plugins can automatically install plugins and enforce hooks/MCP configurations for VS Code and Copilot CLI users licensed through Copilot Business or Enterprise, using enterprise-managed client settings. confidence: 1 GitHub changelog source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-enterprise-managed-plugins-in-vs-code-in-public-preview.md]

### Typed entities
- product: Reachy Mini conversation app
- platform: Hugging Face Gradio Spaces
- endpoint: `/gradio_api/mcp/`
- file: `tools.txt`
- file: `installed_tool_spaces.json`
- product: GitHub Copilot CLI
- editor: Visual Studio Code
- config file: `.github-private/.github/copilot/settings.json`
- concept: enterprise-managed client settings

### Explicit relationships
- Profile-level tool lists govern whether a discovered MCP tool is actually callable.
- Namespaced remote tool IDs prevent collisions between local tools and multiple remote Spaces.
- Public remote MCP tools complement local custom tools but do not supersede private-tool authentication requirements.
- Enterprise-managed plugin settings use central configuration to enforce always-on hooks and MCP configurations across client surfaces.

### HoneyDrunk implications
- For OpenClaw profiles, require namespace/provenance metadata for remote tools and keep public unauthenticated tools separate from private/internal MCP tools.
- Do not treat remote MCP installability as trust; catalog public Spaces by owner, endpoint behavior, tool mutability, data returned, and whether they call external networks.
- If HoneyDrunk adopts enterprise-managed plugins, review auto-installed hooks and MCP configs as organization-wide execution policy.

### Quality notes
- Reachy Mini source is a concrete product implementation but public-only and canary-oriented. GitHub enterprise plugin support is public preview and should be verified in the actual plan/client versions.

## 2026-06-08 compile additions

### Claims
- OWASP's MCP Tool Poisoning page frames malicious MCP responses as an indirect prompt-injection channel: safe-looking tool names/descriptions can pass connect-time review, but runtime tool outputs may smuggle instructions into model context. confidence: 1 OWASP security source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-mcp-tool-poisoning.md]
- OWASP recommends constraining MCP tool responses to fixed schemas where possible, isolating privileged tools from external MCP context, enforcing tool restrictions server-side, maintaining an approved MCP server allowlist, and requiring out-of-model confirmation for sensitive operations. confidence: 1 OWASP security source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-mcp-tool-poisoning.md]
- The OWASP Agent Observability Standard MCP extension proposes routing MCP messages through AOS as a transport to a guardian agent before and after calls so requests and responses can receive allow/modify/deny decisions that the agent must enforce. confidence: 1 OWASP AOS source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-instrument-mcp-agent-observability-standard.md; page: [[opentelemetry-genai-observability-and-ecosystem]]]
- GitHub Copilot SDK GA supports registering custom tools, connecting MCP servers, overriding built-in tools, and hooking pre/post tool use, session start, MCP tool calls, and permission requests. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-copilot-sdk-is-now-generally-available.md; page: [[github-copilot-and-app-token-changes]]]
- Copilot code review public preview lets repositories configure MCP servers and agent skills for review context; existing MCP configurations for Copilot cloud agent automatically apply to Copilot code review. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-shape-copilot-code-review-around-your-team.md]
- FinBot CTF includes MCP tool-server configuration and tampered tool-description scenarios, reinforcing MCP tool supply and runtime-response trust as hands-on agent-security topics. confidence: 1 OWASP GenAI source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-finbot-ctf-is-live-a-hands-on-companion-to-the-owasp-genai-security-pr.md]

### Typed entities
- attack: MCP Tool Poisoning
- standard: OWASP Agent Observability Standard / AOS
- control actor: guardian agent
- decision: allow
- decision: modify
- decision: deny
- SDK: GitHub Copilot SDK
- hook: pre-tool-use
- hook: post-tool-use
- hook: MCP tool-call hook
- product: Copilot code review
- directory: `.github/skills`
- platform: OWASP FinBot CTF

### Explicit relationships
- MCP response validation complements connect-time tool-description review because runtime output is a separate trust boundary.
- AOS guardian checks use allow/modify/deny decisions to mediate MCP requests and responses before model or tool continuation.
- Copilot SDK hooks depend-on application policy to decide whether MCP tool calls are allowed, modified, denied, logged, or escalated.
- Copilot code review MCP configuration reuses Copilot cloud-agent MCP configuration, so a cloud-agent tool choice can affect review behavior.
- FinBot uses MCP tool-server scenarios to exercise tool-poisoning and agentic supply-chain risks.

### HoneyDrunk implications
- Catalog MCP servers with two trust dimensions: tool metadata provenance and runtime response trust. Both need controls.
- Treat Copilot code review MCP inheritance as a policy risk: a tool configured for cloud-agent work may be inappropriate for PR review context.
- If implementing guardian-style MCP mediation, make the enforcement result deterministic at the tool layer; the model must not be able to ignore a deny/modify decision.
- Prefer schema-bound, small, low-privilege MCP outputs for coding profiles; free-text external tools should not share context with filesystem, database, deployment, or messaging tools.

### Privacy and quality notes
- Privacy filter: OWASP examples with sensitive-looking email/salary/file-exfiltration content were summarized at control level and not copied into wiki prose.
- Quality posture: OWASP pages are strong security-taxonomy sources; AOS implementation maturity should be validated before adopting as a standard.

## 2026-06-09 compile additions

### Claims
- Solo.io's agentgateway is positioned as a unified control plane/proxy data plane for HTTP, gRPC, MCP, A2A, and LLM traffic, avoiding separate AI and API gateway stacks. confidence: 1 Solo.io source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-designing-agentgateway-a-unified-high-performance-gateway-for-ai-and-a.md]
- Agentgateway introduces tool/model/service federation so clients can use a unified endpoint while platform teams apply authentication, authorization, routing, observability, rate limiting, and governance centrally. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-designing-agentgateway-a-unified-high-performance-gateway-for-ai-and-a.md]
- The agentgateway source says the project uses Rust/Tokio/Hyper/Tonic, xDS dynamic configuration, and was donated into vendor-neutral governance under the Agentic AI Infrastructure Foundation as a Growth-stage project. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-designing-agentgateway-a-unified-high-performance-gateway-for-ai-and-a.md]
- Microsoft Foundry Toolboxes provide one managed endpoint for tools, skills, MCP clients, and enterprise data, with skills as versioned project-scoped catalog entries and tool search to select task-relevant tools instead of exposing everything. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-what-s-new-in-microsoft-foundry-build-edition-microsoft-foundry-blog.md]
- Datadog's MCP/CLI exposure for feature flags, product analytics, observability, session replay, warehouse metrics, and LLM evals shows MCP surfaces expanding from developer tools into release-operation and product-decision contexts. confidence: 1 Datadog source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-how-a-unified-data-model-improves-feature-flag-rollout-decisions-datad.md]

### Typed entities
- project: agentgateway
- company: Solo.io
- foundation: Agentic AI Infrastructure Foundation / AAIF
- protocol: A2A
- protocol/config: xDS
- language: Rust
- runtime/library: Tokio
- library: Hyper
- library: Tonic
- product: Foundry Toolboxes
- feature: tool search
- product: Datadog MCP Server

### Explicit relationships
- agentgateway federates MCP, A2A, LLM, HTTP, and gRPC traffic through one policy/observability/routing surface.
- xDS dynamic configuration lets gateway policy and routes evolve without data-plane restarts.
- Foundry Toolboxes use managed endpoints and tool search to govern project tools and skills.
- MCP governance now covers release/product operations, not only coding and documentation lookup.

### HoneyDrunk implications
- If OpenClaw/Grid grows multiple MCP servers and internal APIs, evaluate whether a unified gateway/policy point reduces duplicated auth, logs, and rate limits.
- Do not treat tool search as a safety feature unless the underlying catalog is curated and capability-labeled.
- For release-operation MCP tools, require tighter action gating than docs/search tools because they can affect feature rollouts and user exposure.

### Quality notes
- Solo.io and Microsoft sources are product/vendor authored. Agentgateway performance and adoption claims should be validated with current project benchmarks before architectural commitment.

## 2026-06-10 compile additions: Space tool manifests, OpenEnv MCP, and Foundry gateways

### Source-backed claims
- Hugging Face Spaces `agents.md` files act as plain-text agent-call manifests for model-backed apps, giving agents schemas, request formats, polling instructions, file-upload guidance, and authentication expectations. Source: `raw/2026-06-10-web-hugging-face-how-an-agent-built-a-3d-paris-gallery-by-chaining-two-hugging-face-space.md`. confidence: 1 source, last-confirmed 2026-06-10.
- OpenEnv treats MCP as a first-class interface for environments that can be used in simulation, evaluation, and production modes. Source: `raw/2026-06-10-web-hugging-face-the-open-source-community-is-backing-openenv-for-agentic-rl.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft Foundry gateway guidance recommends a reverse-proxy/API-gateway pattern when teams need centralized model routing, auth, rate limits, retry/failover, observability, and policy rather than duplicating those concerns in each client. Source: `raw/2026-06-10-web-microsoft-learn-access-foundry-models-and-other-language-models-through-a-gateway-azure.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft's Foundry chat baseline says Foundry Agent Service lacks built-in blue-green or canary agent deployment controls, so progressive rollout/failback must be implemented in an application router, API gateway, or custom routing layer. Source: `raw/2026-06-10-web-microsoft-learn-baseline-microsoft-foundry-chat-reference-architecture-azure-architectur.md`. confidence: 1 source, last-confirmed 2026-06-10.

### Typed entities
- file: agents.md
- project: Hugging Face Spaces
- project: OpenEnv
- project: MCP
- project: Microsoft Foundry
- concept: API gateway
- decision: OpenClaw tool catalog and gateway policy

### Explicit relationships
- Spaces `agents.md` exposes remote model apps as agent-callable tools.
- OpenEnv uses MCP to bridge simulation/evaluation and production tool environments.
- Foundry gateway patterns centralize policy that otherwise lives in every model client.
- Foundry progressive rollout depends-on routing outside the managed agent service.

### HoneyDrunk implications
- If OpenClaw consumes remote `agents.md` manifests, require a signed or curated tool catalog rather than arbitrary manifest discovery.
- Treat MCP and API gateways as complementary layers: MCP describes actions, while gateways enforce auth, routing, rate, telemetry, and rollback policy.
- For model APIs with broad resource/project permissions, put a HoneyDrunk-controlled policy layer in front of client tools.

### Quality notes
- Sources are platform-authored. Tool-manifest and gateway patterns are useful design inputs, but security posture depends on local allowlists and credential handling.

## 2026-06-11 compile additions: MCP maturity, tool-chain drift, and WebMCP

### Source-backed claims
- CSA's Agentic MCP Security Best Practices draft treats MCP as critical infrastructure and recommends maturing from basic inventory/auth/TLS toward signed messages, approved registries, SBOM/dependency monitoring, behavioral monitoring, and zero-trust per-invocation authorization. Source: `raw/2026-06-11-web-cloud-security-alliance-agentic-mcp-security-best-practices-guide.md`. confidence: 1 draft whitepaper source, last-confirmed 2026-06-11.
- CSA highlights tool-description integrity as a separate governance problem: organizations should baseline tool descriptions, detect changes between sessions, surface changes to users/security teams, and consider signed tool definitions. Source: `raw/2026-06-11-web-cloud-security-alliance-agentic-mcp-security-best-practices-guide.md`. confidence: 1 draft whitepaper source, last-confirmed 2026-06-11.
- CrowdStrike's tool-chain attack source reinforces that MCP concentrates risk because many agents may inherit one server's poisoned or drifted behavior through central capability advertisement. Source: `raw/2026-06-11-web-crowdstrike-how-agentic-tool-chain-attacks-threaten-ai-agent-security.md`. confidence: 1 vendor security source, last-confirmed 2026-06-11.
- Google I/O 2026 announced WebMCP as a proposed open web standard for exposing structured browser/web tools such as JavaScript functions and HTML forms to browser-based AI agents, with an experimental Chrome 149 origin trial and Gemini in Chrome support planned. Source: `raw/2026-06-11-web-google-developers-blog-all-the-news-from-the-google-i-o-2026-developer-keynote.md`. confidence: 1 Google source, last-confirmed 2026-06-11.

### Typed entities
- framework: CSA MCP Security Maturity Model
- proposed standard: WebMCP
- browser: Chrome 149
- product: Gemini in Chrome
- control: tool-description baseline
- control: approved MCP server registry
- control: SBOM
- control: per-invocation authorization

### Explicit relationships
- MCP governance depends-on inventory, authentication, transport security, tool-definition integrity, supply-chain controls, and runtime monitoring.
- Tool-definition drift can supersede a prior approval decision unless definitions are pinned, signed, or re-reviewed.
- WebMCP extends MCP-style structured tool exposure into browser/web surfaces.
- Browser-exposed tools depend-on the same capability labeling, provenance, auth, and action-gating controls as server-side MCP tools.

### HoneyDrunk implications
- For OpenClaw profiles, store tool metadata baselines and review changes, not just server URLs.
- Separate browser/web tool exposure from repository/cloud tooling; WebMCP-style tools may interact with user sessions and forms, so they need stricter consent and audit.
- Add SBOM/provenance checks to MCP server intake for any server installed from npm/PyPI/container images.

### Quality notes
- CSA's document is marked draft. WebMCP is proposed/experimental. Use both as watchlist and design guidance, not stable implementation contract.

## 2026-06-12 compile additions: OWASP MCP Top 10 beta and AGT sandbox policy

### Source-backed claims
- OWASP's MCP Top 10 is in beta/pilot-testing phase and lists MCP risks including token mismanagement, privilege escalation through scope creep, tool poisoning, supply-chain attacks, command injection, intent/prompt-flow subversion, insufficient authZ/authN, lack of audit/telemetry, shadow MCP servers, and context injection/over-sharing. Source: `raw/2026-06-12-web-owasp-owasp-mcp-top-10-owasp-foundation.md`. confidence: 1 OWASP project source, last-confirmed 2026-06-12.
- The OWASP MCP Top 10 frames MCP as an emerging model interaction layer where context, tool, memory, and role boundaries create protocol-specific attack surfaces beyond ordinary API security. Source: `raw/2026-06-12-web-owasp-owasp-mcp-top-10-owasp-foundation.md`. confidence: 1 OWASP project source, last-confirmed 2026-06-12.
- Microsoft's Agent Governance Toolkit sandbox source shows a single YAML `PolicyDocument` being projected into host-side deny/tool rules, AST subprocess checks, Azure Container Apps sandbox CPU/memory settings, fail-closed egress allowlists, advisory timeout markers, and per-step receipts. Source: `raw/2026-06-12-web-microsoft-techcommunity-govern-ai-agents-using-agent-governance-toolkit-and-az.md`. confidence: 1 Microsoft source, last-confirmed 2026-06-12.
- The same AGT source emphasizes that network policy is enforced inside the ACA sandbox egress proxy while denied code/tool calls are stopped host-side before Azure dispatch, making policy enforcement multi-layered rather than prompt-dependent. Source: `raw/2026-06-12-web-microsoft-techcommunity-govern-ai-agents-using-agent-governance-toolkit-and-az.md`. confidence: 1 Microsoft source, last-confirmed 2026-06-12.

### Typed entities
- framework: OWASP MCP Top 10
- threat: token mismanagement and secret exposure
- threat: privilege escalation via scope creep
- threat: shadow MCP servers
- threat: context injection and over-sharing
- framework: Agent Governance Toolkit / AGT
- package: `agt-sandbox`
- class/API: `SandboxProvider`
- provider: `ACASandboxProvider`
- artifact: YAML `PolicyDocument`
- control: fail-closed egress allowlist
- artifact: per-step receipt

### Explicit relationships
- OWASP MCP Top 10 supersedes ad hoc MCP threat lists by providing a community-reviewed risk taxonomy, but it is still beta and should not be treated as final compliance policy.
- AGT policy projects one reviewed policy document into host and sandbox controls.
- Host-side policy denies complement sandbox egress controls because unsafe code should be blocked before execution and again at the network boundary.
- Per-step receipts connect tool governance with auditability by recording allowed, denied, blocked-at-egress, timeout, or error outcomes.

### HoneyDrunk implications
- Map OpenClaw/Honeyclaw MCP intake and runtime controls against the OWASP MCP Top 10 categories before broad tool expansion.
- Use policy-as-artifact patterns for agent execution: tool allowlists, code deny rules, network allowlists, resource budgets, and receipts should be reviewable diffs.
- Treat shadow MCP servers as a real governance risk; profile/catalog search only helps if the catalog is curated and unauthorized servers are visible.

### Quality notes
- OWASP MCP Top 10 is a beta living document. Microsoft AGT source is implementation/vendor guidance and should be validated against current packages and ACA preview behavior.

## 2026-06-14 compile additions: MCP as protocol, not boundary

### Source-backed claims
- Thoughtworks argues that raw off-the-shelf MCP servers often expose an upstream system's schema and vocabulary directly into the agent prompt, creating a conformist bounded-context relationship rather than an anti-corruption layer. Source: `raw/2026-06-14-web-thoughtworks-your-agent-skill-is-not-an-anti-corruption-layer-thoughtw.md`. confidence: 1 architecture source, last-confirmed 2026-06-14.
- Thoughtworks recommends domain-specific tools with typed validation and code-level translation as the production boundary, while MCP remains useful as an adoption and transport protocol, especially for local development and curated internal tools. Source: `raw/2026-06-14-web-thoughtworks-your-agent-skill-is-not-an-anti-corruption-layer-thoughtw.md`. confidence: 1 source, last-confirmed 2026-06-14.
- InfoQ reports Foundry Toolboxes expose tools, skills, MCP clients, and enterprise data integrations through managed endpoints with versioned skills and runtime tool search, reflecting a platform-level move toward curated tool surfaces. Source: `raw/2026-06-14-web-infoq-microsoft-foundry-adds-runtime-tooling-and-governance-for-produc.md`. confidence: 1 secondary source summarizing Microsoft materials, last-confirmed 2026-06-14.
- Fast-Embedding-MCP-SSE exposes local embedding, similarity, stateless search, and in-memory index operations as MCP tools, showing MCP's value for lightweight local retrieval surfaces. Source: `raw/2026-06-14-web-hugging-face-blog-sse-in-practice-fast-static-embeddings-you-can-train.md`. confidence: 1 community technical source, last-confirmed 2026-06-14.
- Anthropic's LLM ATT&CK Navigator analysis identifies MCP-connected offensive tooling as part of agentic misuse scaffolding in a high-risk campaign, reinforcing that MCP tool access can materially change an actor's operational capability. Source: `raw/2026-06-14-rss-anthropic-red-team-llm-att-ck-navigator-red-anthropic-com.md`. confidence: 1 primary vendor threat-intelligence source, last-confirmed 2026-06-14.

### Typed entities
- protocol: Model Context Protocol / MCP
- concept: bounded context
- concept: anti-corruption layer
- concept: conformist pattern
- platform: Microsoft Foundry Toolboxes
- feature: runtime tool search
- tool/server: Fast-Embedding-MCP-SSE
- risk: MCP-enabled offensive scaffolding

### Explicit relationships
- MCP transport does not itself enforce domain translation, validation, or least-privilege semantics.
- Domain-specific tools complement MCP by exposing curated task language while code translates to upstream APIs.
- Runtime tool search and managed toolboxes reduce tool bloat only if the registered tools are curated and governed.
- Local retrieval MCP tools are useful low-risk surfaces when they run on local data and have no external side effects.
- MCP-connected offensive tooling can increase agentic orchestration capability when tools enable scanning, exploitation, lateral movement, or exfiltration.

### HoneyDrunk implications
- Do not treat a prompt skill or raw MCP server as the architectural boundary for production agents. Put domain translation, validation, and authorization in code.
- For HoneyDrunk MCP profiles, prefer narrow internal tools with names and schemas that match HoneyDrunk workflows.
- Keep generic third-party MCP servers in experiment profiles until provenance, tool list, permissions, and output sanitization are reviewed.
- Local retrieval MCP servers may be good Lore helpers, but still need profile scoping and clear data-retention behavior.

### Quality notes
- Thoughtworks guidance is architectural and decision-useful. InfoQ is secondary coverage and should be checked against Microsoft docs before implementation. SSE MCP tooling requires local evaluation.

## 2026-06-15 compile additions: MCP as agent-native product surface and security bridge

### Source-backed claims
- MotherDuck Flights exposes agent-native data ingest through a MotherDuck MCP server with tools to create, run, schedule, update, inspect logs, version, and delete Flights, plus a `get_flight_guide` instruction surface for consistent agent behavior. Source: `raw/2026-06-15-web-motherduck-introducing-flights-agent-native-ingest-in-motherduck.md`. confidence: 1 vendor product source, last-confirmed 2026-06-15.
- MotherDuck says Flights also expose SQL table functions for the same operations, making agent-created ingest jobs manageable from SQL clients, BI tools, dbt, or other Flights. Source: `raw/2026-06-15-web-motherduck-introducing-flights-agent-native-ingest-in-motherduck.md`. confidence: 1 vendor product source, last-confirmed 2026-06-15.
- MotherDuck states secrets stay in MotherDuck and are injected at Flight runtime so agents do not see them directly. Source: `raw/2026-06-15-web-motherduck-introducing-flights-agent-native-ingest-in-motherduck.md`. confidence: 1 vendor product source, last-confirmed 2026-06-15.
- Dropbox uses Dash's MCP server to retrieve threat models and related design/security context during code review, allowing a foundational model to compare implementation against previously approved requirements. Source: `raw/2026-06-15-web-dropbox-tech-how-dropbox-uses-mcp-and-dash-to-close-the-design-to-code.md`. confidence: 1 Dropbox engineering source, last-confirmed 2026-06-15.
- Microsoft AGT includes an MCP Security Gateway for tool poisoning detection, drift monitoring, typosquatting, hidden instruction scanning, and MCP-specific specifications/conformance tests. Source: `raw/2026-06-15-web-microsoft-agent-governance-toolkit.md`. confidence: 1 official GitHub README source, last-confirmed 2026-06-15.

### Typed entities
- product: MotherDuck Flights
- product: MotherDuck MCP server
- tool: `get_flight_guide`
- function family: Flights SQL table functions
- company/product: Dropbox Dash
- concept: design-to-code traceability
- component: AGT MCP Security Gateway
- control: runtime secret injection
- control: tool drift monitoring

### Explicit relationships
- MotherDuck Flights uses MCP and SQL table functions as parallel control surfaces for agent-created data ingest.
- Runtime secret injection complements MCP tools by preventing agents from directly handling credentials.
- Dropbox Dash MCP retrieval connects organizational design/security documents to PR review.
- MCP Security Gateway controls complement catalog/profile governance by checking tool metadata and runtime drift.

### HoneyDrunk implications
- For Lore/OpenClaw data ingest tools, prefer agent-native APIs that expose create/run/schedule/log/version operations plus deterministic instructions, not only free-form shell scripts.
- Keep secrets in the platform or runner and inject them at execution time; agents should receive handles/capabilities, not raw credentials.
- For review agents, MCP context retrieval should be scoped to the relevant design/security sources and every finding should cite the retrieved requirement.

### Quality notes
- MotherDuck and Microsoft sources are vendor/project-authored. Dropbox is a concrete engineering case study. Validate current MCP tool schemas before implementation.

## 2026-06-16 compile additions: agent-native authorization and Open Knowledge Format

### Source-backed claims
- Dick Hardt argues that agent authorization needs per-call constraints over operation parameters, not only agent/tool grants, and that delegation should produce narrower derived authority rather than inherited full parent permissions. Source: `raw/2026-06-16-web-hello-anthropic-s-zero-trust-for-ai-agents-sets-the-right-test-the-bearer-token-fails-it.md`. confidence: 1 identity-practitioner source, last-confirmed 2026-06-16.
- Google Cloud's Open Knowledge Format (OKF) v0.1 formalizes an LLM-wiki pattern as a directory of markdown files with YAML frontmatter and cross-links, intended to be readable by humans and portable across agents/tools. Source: `raw/2026-06-16-web-google-introducing-the-open-knowledge-format.md`; page: [[llm-wiki-and-knowledge-formats]]. confidence: 1 official vendor/spec announcement, last-confirmed 2026-06-16.
- OKF requires a `type` field and defines a small interoperability surface around fields such as `title`, `description`, `resource`, `tags`, and `timestamp`, while leaving detailed content models to producers. Source: `raw/2026-06-16-web-google-introducing-the-open-knowledge-format.md`; page: [[llm-wiki-and-knowledge-formats]]. confidence: 1 official vendor/spec announcement, last-confirmed 2026-06-16.

### Typed entities
- concept: constrained call
- concept: derived authority
- concept: proof-of-possession credential
- specification: Open Knowledge Format / OKF v0.1
- pattern: LLM wiki
- field: `type`
- field: `resource`
- page: [[llm-wiki-and-knowledge-formats]]

### Explicit relationships
- Per-call constrained authorization complements MCP/tool governance by making operation parameters part of authorization.
- Derived authority mitigates multi-agent delegation risk by narrowing access as tasks move between agents.
- OKF complements Lore's flat-file wiki contract by making markdown knowledge bundles more portable across agent producers and consumers.

### HoneyDrunk implications
- For high-risk MCP tools, model the exact operation and parameters being authorized; do not rely on broad "agent can call tool" grants.
- Track OKF as a possible future compatibility target for Lore exports, especially frontmatter fields and bundle identity rules.

### Quality notes
- Identity-control claims are expert opinion; OKF is a vendor-announced open specification and should be read against the repo/spec before implementation.

## 2026-06-18 compile additions: MCP structured outputs, diagnostics bridges, and IDE semantic tools

### Source-backed claims
- The MCP C# SDK now supports the MCP 2025-06-18 specification with separated authentication/resource-server roles, elicitation, structured tool output schemas, resource links in tool results, expanded `_meta`, and human-friendly titles for tools/resources/prompts. Source: `raw/2026-06-18-web-devblogs-microsoft-com-mcp-c-sdk-gets-major-update-support-for-protoco.md`. confidence: 1 official .NET Blog source, last-confirmed 2026-06-18.
- The MCP C# SDK's structured output support lets tools publish output schemas and return `structuredContent`, reducing the need for clients or models to infer result shapes from free text. Source: `raw/2026-06-18-web-devblogs-microsoft-com-mcp-c-sdk-gets-major-update-support-for-protoco.md`. confidence: 1 source, last-confirmed 2026-06-18.
- Microsoft's Binlog MCP Server wraps MSBuild `.binlog` analysis as 15 MCP tools for build errors, warnings, properties, imports, embedded files, expensive projects/targets/tasks, and two-build comparison. Source: `raw/2026-06-18-web-devblogs-microsoft-com-ai-powered-msbuild-investigation-with-the-micro.md`. confidence: 1 official .NET Blog source, last-confirmed 2026-06-18.
- AWS shows a custom MCP server pattern for AWS DevOps Agent that exposes EKS node diagnostics through SSM Automation and S3-backed extraction, keeping node access mediated rather than giving the agent an interactive shell. Source: `raw/2026-06-18-web-aws-amazon-com-diagnose-eks-node-issues-faster-with-aws-devops-agent-a.md`. confidence: 1 AWS DevOps Blog source, last-confirmed 2026-06-18.
- GitHub's Copilot CLI LSP Setup skill configures language servers so the terminal agent can use semantic code-intelligence requests instead of grepping dependencies or decompiling packages. Source: `raw/2026-06-18-web-github-blog-give-github-copilot-cli-real-code-intelligence-with-langua.md`. confidence: 1 GitHub Blog source, last-confirmed 2026-06-18.

### Typed entities
- specification: MCP 2025-06-18
- library: MCP C# SDK / `ModelContextProtocol`
- concept: elicitation
- concept: structured tool output
- field: `structuredContent`
- tool/server: Microsoft Binlog MCP Server
- file type: MSBuild `.binlog`
- service: AWS DevOps Agent
- service: Amazon EKS
- service: AWS Systems Manager Automation / SSM Automation
- service: Amazon Bedrock AgentCore Gateway
- tool/skill: GitHub Copilot CLI LSP Setup skill
- protocol: Language Server Protocol / LSP

### Explicit relationships
- Structured tool outputs complement MCP governance by making tool result contracts explicit and machine-checkable.
- Elicitation adds an interactive server-to-user request path, which depends-on client capability declarations and input validation.
- Binlog MCP tools translate MSBuild diagnostic structure into agent-readable operations instead of exposing raw binary logs.
- AWS custom MCP diagnostics bridges an agent visibility gap while SSM Automation mediates host access and auditability.
- LSP setup complements agent code search by replacing text heuristics with language-server semantics.

### HoneyDrunk implications
- Prefer MCP tools that publish structured output schemas for durable OpenClaw/Honeyclaw integrations; free-text tools should be treated as less reliable inputs.
- For build and runner diagnostics, expose bounded diagnostic tools and run receipts rather than giving agents direct shell or host access by default.
- Add LSP-backed code intelligence to the agent-tooling watchlist for repositories where agents repeatedly misread APIs or dependencies.

### Quality notes
- Microsoft, AWS, and GitHub sources are vendor-authored but concrete. Validate package versions, authentication behavior, telemetry settings, and host-access boundaries before implementation.

## 2026-06-19 compile additions: ARD discovery, AGT .NET governance, and Azure session controls

### Source-backed claims
- Agentic Resource Discovery / ARD publishes capability catalogs under an organization's domain and lets registries return matching capabilities plus trust metadata before the client connects directly through the capability's native protocol. Source: `raw/2026-06-19-web-developers-googleblog-com-announcing-the-agentic-resource-discovery-specification-goog.md`; page: [[google-agent-platform-and-gemini-api-2026]]. confidence: 1 Google Developers source, last-confirmed 2026-06-19.
- Microsoft.AgentGovernance exposes a .NET governance path for MCP tool calls through `McpSecurityScanner`, `McpGateway`, `McpResponseSanitizer`, and `GovernanceKernel`, with YAML policy, audit events, and OpenTelemetry metrics. Source: `raw/2026-06-19-web-devblogs-microsoft-com-governing-mcp-tool-calls-in-net-with-the-agent-governance-toolk.md`; page: [[microsoft-dotnet-ai-stack]]. confidence: 1 .NET Blog source, last-confirmed 2026-06-19.
- AGT examples scan tool definitions for prompt-injection text, tool-name typosquatting, credential leakage, and exfiltration-oriented URLs, then gate tool registration or calls by risk score and policy. Source: `raw/2026-06-19-web-devblogs-microsoft-com-governing-mcp-tool-calls-in-net-with-the-agent-governance-toolk.md`. confidence: 1 source, last-confirmed 2026-06-19.
- Azure SRE Agent network controls can route agent egress through an Azure VNet, use private DNS for private endpoints, or selectively send categories such as remote MCP server access, package registries, code repositories, and custom hosts through a managed path. Source: `raw/2026-06-19-web-learn-microsoft-com-configure-network-controls-for-azure-sre-agent.md`; page: [[azure-agent-automation-and-identity]]. confidence: 1 Microsoft Learn source with access warning in capture, last-confirmed 2026-06-19.
- Azure Container Apps code interpreter sessions expose REST endpoints for executions and file transfer in Hyper-V-isolated sessions; Microsoft warns that session identifiers are sensitive and must be scoped so users or tenants cannot access each other's sessions. Source: `raw/2026-06-19-web-learn-microsoft-com-serverless-code-interpreter-sessions-in-azure-container-apps.md`; page: [[azure-agent-automation-and-identity]]. confidence: 1 Microsoft Learn source with access warning in capture, last-confirmed 2026-06-19.

### Typed entities
- specification: Agentic Resource Discovery / ARD
- artifact: `ai-catalog.json`
- framework: Microsoft Agent Governance Toolkit / AGT
- component: `McpGateway`
- component: `McpSecurityScanner`
- component: `McpResponseSanitizer`
- component: `GovernanceKernel`
- policy format: YAML governance policy
- service: Azure SRE Agent
- service: Azure Container Apps code interpreter sessions
- control: VNet egress routing
- control: session identifier isolation

### Explicit relationships
- ARD complements MCP catalogs by separating resource discovery and publisher verification from the protocol used after connection.
- AGT MCP governance uses policy, scanner, sanitizer, identity, audit, and metrics controls around tool definitions and tool calls.
- Tool-definition scanning complements catalog approval because a tool can drift or be poisoned after initial discovery.
- Azure SRE Agent VNet routing depends-on delegated subnets and private DNS zone linking for private endpoint access.
- Code interpreter session isolation depends-on Entra authorization, session identifiers, and tenant/user scoping, not only Hyper-V boundaries.

### HoneyDrunk implications
- Treat ARD-discovered tools as untrusted until publisher identity, spec pinning, tool list, egress, and auth scope are reviewed.
- For .NET MCP servers, keep AGT-style policy files and scanner thresholds under version control with tests for expected false positives.
- If Azure SRE Agent or ACA code interpreter sessions are evaluated, record egress mode, session-id custody, file upload/download policy, logging gaps, and per-tenant authorization before use.

### Quality notes
- Microsoft and Google sources are vendor-authored. The Azure Learn captures included authorization warnings, so verify current docs and preview status before implementation.

## 2026-06-20 compile additions: A2UI over MCP, runtime credentials, and server-side tools

### Source-backed claims
- Google describes three hybrid A2UI/MCP Apps patterns: serving A2UI payloads over MCP resources or tool calls, embedding MCP Apps inside A2UI components, and running an A2UI renderer inside an MCP App for non-A2UI hosts. Source: `raw/2026-06-20-web-google-developers-blog-a2ui-mcp-apps-combining-the-best-of-declarative.md`; page: [[generative-ui-and-a2ui]]. confidence: 1 Google Developers source, last-confirmed 2026-06-20.
- A2UI-over-MCP uses structured resources with `application/a2ui+json` and `a2ui://` URIs, letting MCP provide backend tool/data access while the host renders declarative UI through native components instead of raw iframe UI. Source: `raw/2026-06-20-web-google-developers-blog-a2ui-mcp-apps-combining-the-best-of-declarative.md`. confidence: 1 source, last-confirmed 2026-06-20.
- Vercel Connect provides runtime credential exchange for agent/tool access: connectors are registered once, apps prove identity with deployment OIDC, and tasks request short-lived provider credentials scoped to app/user, environment, installation, repository, permission, or provider-specific authorization details. Source: `raw/2026-06-20-web-vercel-vercel-connect-8-minute-read.md`; page: [[ai-coding-agent-security]]. confidence: 1 Vercel source, last-confirmed 2026-06-20.
- DigitalOcean Inference Engine Server-Side Tools supports MCP servers, DigitalOcean Knowledge Bases, web search/fetch, and compatible Anthropic/OpenAI tool definitions directly in inference requests, making hosted tool support a model-provider feature rather than only an app-owned harness feature. Source: `raw/2026-06-20-web-digitalocean-server-side-tools-are-now-available-for-digitalocean-infe.md`; page: [[ai-agent-harnesses]]. confidence: 1 DigitalOcean source, last-confirmed 2026-06-20.

### Typed entities
- MIME type: `application/a2ui+json`
- URI scheme: `a2ui://`
- protocol: Model Context Protocol / MCP
- framework/spec: A2UI
- concept: MCP Apps
- control: App Bridge
- product: Vercel Connect
- auth mechanism: OIDC
- connector examples: Slack, GitHub, Linear, Discord, Notion, Salesforce, Figma, Snowflake
- feature: trigger forwarding
- platform: DigitalOcean Inference Engine Server-Side Tools

### Explicit relationships
- A2UI-over-MCP separates backend tool/data access from native UI rendering.
- MCP Apps-in-A2UI use iframe delegation for complex stateful widgets while native A2UI components preserve host design and macro-state synchronization.
- Runtime credential exchange supersedes long-lived shared bot tokens for many agent connector flows.
- Provider-hosted server-side tools complement app-owned MCP profiles but shift governance questions to provider trust, per-tool scope, and auditability.

### HoneyDrunk implications
- For agent UI surfaces, prefer structured UI payloads and known components for standard forms/charts/cards; reserve iframe apps for complex custom interactions with explicit state synchronization.
- Catalog MCP and connector tools by auth model: static secret, OIDC runtime exchange, user-delegated token, API key, or provider-hosted tool.
- Do not expose hosted bash/computer-use/apply-patch style tools to private HoneyDrunk context until provider sandbox, logging, and approval controls are documented.

### Quality notes
- Sources are vendor-authored product/architecture announcements. Verify active specs, SDK versions, pricing, token retention, and connector limitations before implementation.

## 2026-06-21 compile additions: social MCP expansion and codebase memory watchlist

### Source-backed claims
- Birdclaw social sources on 2026-06-20 surfaced several MCP/tool-surface leads: codebase-memory-mcp, public MCP server browsing, Solana tools exposed over MCP, and a claimed study of 177,436 public MCP tools. These should be treated as discovery leads until primary repositories, papers, or catalogs are reviewed. Source: `wiki/early-social-ai-agent-signals-2026.md`. confidence: low social-source cluster, last-confirmed 2026-06-20.
- The codebase-memory-mcp post claims a C/MIT-licensed tool indexes codebases into a graph using tree-sitter and JSON-RPC, with a token-reduction positioning for coding assistants; this is unverified social/source-author promotion until the repository is inspected. Source: `raw/2026-06-20-birdclaw-x-x-signal-janifica-deusdata-codebase-memory-mcp-why-it-s-trending-this-new-open-s.md`. confidence: 1 social source, last-confirmed 2026-06-20.
- The MCP public-tool growth post claims a sharp increase in public MCP tools and AI co-authored MCP servers; the numbers require primary study verification before operational use. Source: `raw/2026-06-20-birdclaw-x-x-signal-vbkotecha-a-new-study-analyzed-177-436-public-mcp-tools-and-found-that.md`. confidence: 1 social source citing an unnamed study in the capture, last-confirmed 2026-06-20.

### Typed entities
- project/tool: codebase-memory-mcp
- parser framework: tree-sitter
- protocol: JSON-RPC 2.0
- protocol: Model Context Protocol / MCP
- concept: public MCP server catalog
- concept: MCP tool growth
- concept: AI co-authored tool surface
- page: [[early-social-ai-agent-signals-2026]]

### Explicit relationships
- Codebase memory graphs complement text search and embeddings when they preserve symbol/AST relationships for agents.
- Public MCP server growth increases tool-supply value but also increases provenance, typosquatting, prompt-injection, and permission-review burden.
- Social tool claims depend-on repository inspection, license review, security review, and local benchmark before catalog promotion.

### HoneyDrunk implications
- Add codebase-memory-mcp to the retrieval/tooling watchlist only after repo inspection confirms build, license, language coverage, and security posture.
- Treat public MCP catalogs as untrusted indexes. Approved HoneyDrunk profiles still need explicit server provenance, version/hash, permissions, and network/secret review.

### Quality notes
- Low-confidence social-source batch. No MCP server should be promoted to approved catalog from this evidence alone.

## 2026-06-22 compile additions: Cloudflare stack skills, Datadog MCP, and shared action surfaces

### Source-backed claims
- Cloudflare One stack skills package Zero Trust/SASE migration, evaluation, deployment, management, and troubleshooting knowledge as agent-consumable skill files, including vendor-to-Cloudflare mapping logic for Zscaler, Palo Alto, and Netskope concepts. Source: `raw/2026-06-22-rss-blog-cloudflare-com-introducing-the-cloudflare-one-stack-agent-powered.md`. confidence: 1 Cloudflare product source, last-confirmed 2026-06-22.
- Cloudflare's code-mode MCP server gives agents a typed Cloudflare API interface while keeping credentials out of model context, reinforcing the pattern that MCP tools should mediate API access instead of exposing secrets or raw dashboards to the agent. Source: `raw/2026-06-22-rss-blog-cloudflare-com-introducing-the-cloudflare-one-stack-agent-powered.md`. confidence: 1 source, last-confirmed 2026-06-22.
- Datadog MCP Server GA exposes observability and operations data to AWS DevOps Agent workflows, including logs, metrics, traces, dashboards, monitors, incidents, APM, security scanning, database monitoring, and CI/CD. Source: `raw/2026-06-22-rss-aws-amazon-com-production-ready-autonomous-incident-resolution-with-aw.md`. confidence: 1 AWS/Datadog product signal, last-confirmed 2026-06-22.
- Builder.io's Agent-Native framework exposes the same action definition through MCP, A2A, HTTP, UI, CLI, and agents, turning action contracts into a shared app surface rather than separate agent-only tool schemas. Source: `raw/2026-06-22-rss-github-com-agent-native.md`. confidence: 1 project/repository source, last-confirmed 2026-06-22.

### Typed entities
- product: Cloudflare One
- skill file: `cloudflare-one`
- skill file: `cloudflare-one-migration`
- MCP server: Cloudflare code-mode MCP server
- product: Datadog MCP Server
- service: AWS DevOps Agent
- framework: Agent-Native
- API: `defineAction`
- protocol: A2A

### Explicit relationships
- Cloudflare One skills complement MCP tools by encoding migration/domain knowledge that the API alone does not provide.
- Typed MCP API interfaces reduce prompt/context exposure of credentials but still depend-on runtime credential custody and scoped permissions.
- Datadog MCP tools connect incident agents to observability data, so tool profiles must distinguish read-only diagnosis from mutating incident/remediation actions.
- Shared action definitions can supersede duplicated tool schemas when UI, HTTP, MCP, A2A, CLI, and agent behavior should stay consistent.

### HoneyDrunk implications
- When creating HoneyDrunk MCP profiles, pair tools with skills only when the skill encodes reviewable domain process, not when it merely repeats API docs.
- For Cloudflare or Datadog-like integrations, classify tools by capability: docs/read, account read, diagnostic query, mutating config, incident action, and deployment.
- Prefer typed, source-controlled action contracts for internal tools so the same permission, validation, and audit path applies to humans and agents.

### Quality notes
- Sources are vendor/product/project-authored. Validate active APIs, auth behavior, logging, and per-tool permissions before profile approval.
