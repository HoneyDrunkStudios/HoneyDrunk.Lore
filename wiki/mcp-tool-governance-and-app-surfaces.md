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
