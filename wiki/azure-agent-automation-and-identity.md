# Azure Agent Automation and Identity

## Decision-useful summary
Azure's May 2026 agent/developer tooling signal is that agent automation is moving into `azd` and Azure templates, but production use hinges on non-interactive reliability, preflight checks, layered infrastructure, and explicit token-based authorization. For HoneyDrunk, `azd` is useful as an agent-operable deployment surface only when prompts are eliminated, environment scope is explicit, and agent/API access is mediated by short-lived, least-privilege credentials. [sources: raw/2026-05-09-rss-azure-blog-azure-developer-cli-azd-april-2026.md; raw/2026-05-09-rss-azure-blog-least-privilege-ai-agents-a-new-azd-template-from-curity-an.md]

## Claims
- Azure Developer CLI April 2026 releases added multi-language hooks for Python, JavaScript, TypeScript, and .NET, with automatic dependency/runtime handling and executor-specific hook configuration in `azure.yaml`. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-azure-blog-azure-developer-cli-azd-april-2026.md]
- `azd provision` added AI model quota preflight checks that inspect Bicep snapshots for Azure Cognitive Services model deployments and warn before provisioning when quota or model-name problems are detected. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-azure-blog-azure-developer-cli-azd-april-2026.md]
- `azd` standardized `--no-prompt` behavior, added a global `--non-interactive` alias plus `AZD_NON_INTERACTIVE`, and now returns structured failures when required inputs cannot be resolved automatically, which is important for CI/CD and AI-agent operation. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-azure-blog-azure-developer-cli-azd-april-2026.md]
- `azd update` graduated to public preview and now verifies Windows MSI code signing against the expected publisher, closing a tampered/substituted MSI update path. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-azure-blog-azure-developer-cli-azd-april-2026.md]
- The April 2026 `azd` security fixes included an environment-selection leak fix for extension subprocesses where extension commands could receive secrets/configuration from the wrong `azd` environment. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-azure-blog-azure-developer-cli-azd-april-2026.md]
- The Curity/Microsoft `azd` AI agent template deploys a C# Microsoft Foundry backend agent, MCP portfolio API server, Curity Identity Server, Entra ID authentication, internal/external gateways, audit logging, and Azure infrastructure through Bicep. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-azure-blog-least-privilege-ai-agents-a-new-azd-template-from-curity-an.md]
- The Curity/Microsoft pattern uses token exchange to give agents short-lived OAuth 2.0 access tokens with narrow scope, user attributes such as `customer_id`/`region`, `client_type=ai-agent`, `agent_id`, and an MCP-server audience so APIs can filter data independently of model behavior. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-azure-blog-least-privilege-ai-agents-a-new-azd-template-from-curity-an.md]
- The Curity/Microsoft template separates authentication from authorization: Entra ID handles user sign-in/identity storage, while Curity issues short-lived internal JWTs designed for API authorization and agent delegation. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-azure-blog-least-privilege-ai-agents-a-new-azd-template-from-curity-an.md]

## Typed entities
- project/tool: Azure Developer CLI (`azd`)
- feature: multi-language `azd` hooks
- feature: `azd` AI model quota preflight
- feature: `AZD_NON_INTERACTIVE`
- feature: `azd` extension framework custom provisioning providers
- project/template: `curityio/azd-ai-autonomous-agent`
- product/service: Curity Identity Server
- product/service: Microsoft Entra ID
- product/service: Microsoft Foundry
- protocol: OAuth 2.0 token exchange
- protocol/tooling: Model Context Protocol
- concept: least-privilege AI agents
- concept: short-lived delegated access tokens
- file: raw/2026-05-09-rss-azure-blog-azure-developer-cli-azd-april-2026.md
- file: raw/2026-05-09-rss-azure-blog-least-privilege-ai-agents-a-new-azd-template-from-curity-an.md

## Explicit relationships
- Azure Developer CLI uses `azure.yaml` hooks to execute deployment lifecycle automation.
- Azure Developer CLI uses Bicep snapshots to preflight AI model quota before provisioning.
- Azure Developer CLI `--non-interactive` supersedes ad-hoc prompt handling for CI/CD and AI-agent runs.
- `azd` extension subprocesses depend-on correct `-e/--environment` propagation to avoid cross-environment secret/config leakage.
- Curity Identity Server works alongside Microsoft Entra ID rather than replacing it.
- The Curity/Microsoft template uses token exchange to narrow user credentials into short-lived agent/API tokens.
- Internal and external API gateways enforce token exchange, audit logging, and coarse rules between users, agents, and MCP servers.
- Least-privilege AI agents depend-on API-side authorization rules that do not trust the model to behave perfectly.
- [[AI Agent Harnesses]] depends-on non-interactive, auditable deployment/runtime surfaces such as `azd` when agents operate infrastructure.
- [[Microsoft .NET AI Stack]] uses Microsoft Foundry, MCP, and Microsoft Agent Framework as composable agent infrastructure.

## HoneyDrunk implications
- Treat `azd` as a viable agent-facing deployment primitive only after every path runs with `--non-interactive`/`AZD_NON_INTERACTIVE` and structured failure handling.
- For any Grid/Lore agent that touches customer or private data, design authorization in tokens/API filters, not prompts.
- Prefer layered infrastructure templates where external surfaces are minimized and internal gateways produce audit logs.
- If using `azd auth token`, remember the default raw-token output is sensitive; do not capture it into logs or wiki content.

## Confidence and quality notes
- Quality posture: decision-usable for Azure agent deployment and authorization architecture scouting.
- Weak spots: both sources are vendor-authored; validate template maturity, cost, and region/model availability locally before adoption.
- Privacy filter: example token values from the public blog were summarized by field names and purpose only; no reusable token or private user data was copied.

## 2026-05-30 compile additions

### Claims
- Azure Container Apps dynamic sessions can create a shell session pool with a platform-managed MCP server enabled through `Microsoft.App/sessionPools` preview API settings, avoiding custom MCP server deployment for basic remote shell tools. confidence: 1 Microsoft Learn source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-tutorial-use-mcp-with-dynamic-sessions-shell.md]
- The dynamic-session MCP shell tutorial exposes `launchShell` and `runShellCommandInRemoteEnvironment`, with sessions destroyed after a configurable inactivity cooldown in the sample ARM template. confidence: 1 Microsoft Learn source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-tutorial-use-mcp-with-dynamic-sessions-shell.md]
- The platform-managed MCP server uses API-key authentication through the `x-ms-apikey` header rather than standard bearer-token session-pool management APIs; Microsoft warns not to commit this key. confidence: 1 Microsoft Learn source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-tutorial-use-mcp-with-dynamic-sessions-shell.md]
- The tutorial's API version and `mcpServerSettings` properties are preview and subject to change, so production architecture should not depend on stable behavior yet. confidence: 1 Microsoft Learn source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-tutorial-use-mcp-with-dynamic-sessions-shell.md]

### Typed entities
- Azure resource type: `Microsoft.App/sessionPools`
- API version: `2025-02-02-preview`
- property: `mcpServerSettings.isMCPServerEnabled`
- property: `containerType: Shell`
- tool: `launchShell`
- tool: `runShellCommandInRemoteEnvironment`
- auth header: `x-ms-apikey`
- client: GitHub Copilot Chat in VS Code

### Explicit relationships
- Azure dynamic sessions use platform-managed MCP to connect agent clients to ephemeral shell environments.
- Session-pool API keys depend-on secret storage and should not be committed to project MCP config.
- Preview dynamic-session MCP complements, but does not supersede, least-privilege identity patterns for production cloud automation.

### HoneyDrunk implications
- Dynamic shell sessions are a useful candidate for disposable agent compute, but HoneyDrunk must validate egress policy, secrets handling, audit logs, costs, region support, and preview churn.
- Treat remote shell MCP tools as high-risk even when ephemeral; require scoped environments and explicit operator intent.

## 2026-05-31 compile additions

### Claims
- Azure Developer CLI hooks now support Python, JavaScript, TypeScript, and .NET in addition to Bash and PowerShell; `azd` infers hook language from file extension or an explicit `kind` field in `azure.yaml`. confidence: 1 Microsoft Azure blog source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-azure-blog-write-azd-hooks-in-python-javascript-typescript-or-net.md]
- Python hooks use nearby `requirements.txt` or `pyproject.toml` files, with `azd` creating a virtual environment and installing dependencies before running the script. confidence: 1 Microsoft Azure blog source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-azure-blog-write-azd-hooks-in-python-javascript-typescript-or-net.md]
- JavaScript/TypeScript hooks use nearby `package.json`; TypeScript runs through `npx tsx` without a compile step, and hook config can select package managers such as npm, pnpm, or yarn. confidence: 1 Microsoft Azure blog source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-azure-blog-write-azd-hooks-in-python-javascript-typescript-or-net.md]
- .NET hooks support project mode with restore/build when a project file exists, and single-file `.cs` execution through .NET 10+ script support; hook config can set build configuration and target framework. confidence: 1 Microsoft Azure blog source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-azure-blog-write-azd-hooks-in-python-javascript-typescript-or-net.md]

### Typed entities
- file: `azure.yaml`
- hook language: Python
- hook language: JavaScript
- hook language: TypeScript
- hook language: .NET / C# / F# / VB.NET
- config field: `kind`
- config field: `dir`
- config field: `packageManager`
- config field: `virtualEnvName`
- config field: `framework`
- dependency file: `requirements.txt`
- dependency file: `pyproject.toml`
- dependency file: `package.json`
- runtime tool: `tsx`

### Explicit relationships
- `azd` hooks use language inference and executor-specific config to make deployment lifecycle automation project-language-native.
- Multi-language hooks supersede shell-only hook assumptions for teams whose deployment logic already lives in Python, TypeScript, or .NET.
- Hook dependency installation depends-on nearby project files and can change deploy reproducibility if versions are not pinned.

### HoneyDrunk implications
- For agent-run Azure deployments, prefer hook languages already used by the repo, but pin dependencies and make hooks deterministic under `AZD_NON_INTERACTIVE`.
- Audit hooks as executable deployment code: they can seed data, migrate schemas, create resources, and leak secrets if logging is careless.

## 2026-06-01 compile additions

### Claims
- Azure Container Apps dynamic sessions expose isolated session contexts through a session-pool management endpoint; callers pass a required `identifier` query parameter and Azure allocates a new session automatically when that identifier does not yet exist. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-use-dynamic-sessions-in-azure-container-apps.md]
- Session-pool management API calls require Microsoft Entra authentication and the `Azure ContainerApps Session Executor` role; Microsoft warns that end users should not receive the tokens used to create and access sessions. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-use-dynamic-sessions-in-azure-container-apps.md]
- Dynamic sessions are intended for untrusted code/app isolation, but anything inside one session, including files and environment variables, is accessible to users of that session; secure, unpredictable identifiers and tenant/user access checks are required. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-use-dynamic-sessions-in-azure-container-apps.md]
- The Secure MCP on Container Apps source clarifies that dynamic-session MCP uses API-key auth at the session-pool level, while standalone Container Apps MCP servers should use Microsoft Entra bearer-token auth and app-owned authorization. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-secure-mcp-servers-on-azure-container-apps.md]

### Typed entities
- Azure feature: Container Apps dynamic sessions
- Azure resource: session pool
- role: Azure ContainerApps Session Executor
- query parameter: `identifier`
- auth mechanism: Microsoft Entra token
- auth mechanism: dynamic-session MCP API key
- control: `sessionNetworkConfiguration.status`
- control: `coolDownPeriodInSeconds`
- service: Azure Monitor / Log Analytics

### Explicit relationships
- Dynamic sessions use session identifiers to route requests to isolated execution contexts.
- Session identifiers depend-on entropy and tenant authorization because predictable identifiers can cross user/session boundaries.
- Managed identity can give sessions access to Entra-protected resources, so identity scope must match the session's blast radius.
- Platform-managed MCP auth does not supersede Entra-based management API auth; they are separate surfaces.

### HoneyDrunk implications
- Before using Azure dynamic sessions for agent compute, define token custody, session ID generation, per-user authorization, egress posture, log retention, cooldown, and managed-identity scope.
- Use dynamic sessions as disposable execution contexts, not as a place to hold durable secrets or cross-tenant state.

## 2026-06-02 compile additions

### Claims
- Microsoft Tech Community's OpenClaw-on-AKS guide recommends a dedicated AKS node pool with `--workload-runtime KataMshvVmIsolation`, `runtimeClassName: kata-vm-isolation`, nested-virtualization-capable VM sizes, Azure Files NFS persistent storage, and Application Gateway for Containers for ingress. confidence: 1 Microsoft community source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-microsoft-tech-community-hardening-openclaw-on-aks-mitigating-containe.md]
- The same guide frames Kata microVM isolation as defense-in-depth for OpenClaw-style agent workloads: containers still look like OCI/Kubernetes workloads, but each pod sandbox gets a VM boundary that reduces shared-kernel escape blast radius. confidence: 1 Microsoft community source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-microsoft-tech-community-hardening-openclaw-on-aks-mitigating-containe.md]
- ACR Artifact Cache is a pull-through proxy, not a redirect: clients pull from downstream ACR, ACR streams from upstream when uncached, and an asynchronous background job stores artifacts locally for later cache hits. confidence: 1 Microsoft Tech Community source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-microsoft-tech-community-how-acr-artifact-cache-handles-multi-arch-ima.md]
- For a multi-architecture image, ACR Artifact Cache copies the manifest list and only the platform-specific manifest that was pulled; other platform manifests are not copied until someone pulls that platform. confidence: 1 Microsoft Tech Community source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-microsoft-tech-community-how-acr-artifact-cache-handles-multi-arch-ima.md]
- ACR push webhooks fire when artifact-cache asynchronous copy completes; a single-platform pull of a multi-arch image can produce three push events: tagged manifest list, untagged manifest list, and the platform manifest. Layer/blob copies do not produce push webhooks. confidence: 1 Microsoft Tech Community source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-microsoft-tech-community-how-acr-artifact-cache-handles-multi-arch-ima.md]

### Typed entities
- platform: Azure Kubernetes Service / AKS
- runtime: KataMshvVmIsolation
- runtime class: `kata-vm-isolation`
- ingress: Application Gateway for Containers
- storage: Azure Files NFS
- service: Azure Container Registry / ACR
- feature: ACR Artifact Cache
- artifact: manifest list / OCI image index
- artifact: platform manifest
- event: ACR push webhook

### Explicit relationships
- OpenClaw on AKS uses Kata node pools to isolate agent pods behind a microVM boundary.
- Kata runtime selection depends-on AKS node-pool runtime and compatible VM sizes.
- ACR Artifact Cache uses asynchronous local copy after proxying the first pull.
- Multi-arch cache completeness depends-on which platforms have actually been pulled.
- ACR webhooks can signal artifact-cache materialization for manifests but not layer/blob copying.

### HoneyDrunk implications
- If using AKS for OpenClaw, validate Kata support, node SKU availability, persistent workspace behavior, ingress auth, and per-pod egress before trusting the design.
- Do not assume one amd64 cache warm-up populates arm64 images; warm each required platform explicitly.
- Use ACR push webhooks as cache-readiness evidence carefully: count manifest-list/platform events and avoid treating blob/layer absence as a failed cache.

### Quality notes
- Microsoft Tech Community posts are useful implementation references but may include duplicated page scaffolding in raw; promoted facts came from article body/key-takeaway sections only.

## 2026-06-03 compile additions

### Claims
- `azure-functions-skills` public preview installs Azure Functions-focused skills, `functions-copilot` agent definition, MCP configuration, hooks, and repo instruction files, splitting user-scope plugin install from workspace-scoped artifacts by default. confidence: 1 Microsoft Azure SDK Blog source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-azure-blog-introducing-azure-functions-skills-an-ai-era-workspace-for-.md]
- The Azure Functions skills steer agents toward managed identity, Key Vault references, Flex Consumption, current binding/concurrency patterns, Azure MCP template service scaffolding, and deployment validation rather than hardcoded keys or stale programming models. confidence: 1 Microsoft source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-azure-blog-introducing-azure-functions-skills-an-ai-era-workspace-for-.md]
- The `azure-functions-agents` skill targets the Azure Functions serverless agents runtime, Microsoft Foundry, Connector Namespaces, remote MCP servers, and Azure Container Apps dynamic sessions for code execution or web browsing. confidence: 1 Microsoft source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-azure-blog-introducing-azure-functions-skills-an-ai-era-workspace-for-.md]
- Azure Cosmos DB MCP Toolkit v1.1.2 GA adds Foundry integration, Entra/RBAC/managed-identity posture, multi-provider embeddings, startup validation, and structured role-denied responses for agent/database access. confidence: 1 Microsoft Azure Cosmos DB Blog source, last-confirmed 2026-06-03. [source: raw/2026-06-03-web-azure-cosmos-db-blog-azure-cosmos-db-mcp-toolkit-is-now-generally-avai.md]

### Typed entities
- package/plugin: `@azure/functions-skills`
- plugin: `azure-functions-skills`
- agent definition: `functions-copilot`
- skill: `azure-functions-agents`
- service/runtime: Azure Functions serverless agents runtime
- service: Azure MCP template service
- service: Azure Cosmos DB MCP Toolkit
- version: Azure Cosmos DB MCP Toolkit v1.1.2
- platform: Microsoft Foundry
- control: managed identity
- control: Key Vault references
- plan: Flex Consumption

### Explicit relationships
- Azure Functions skills use workspace-scoped artifacts to make agent behavior repository-specific while keeping reusable skills discoverable at user scope.
- Managed identity and Key Vault references supersede hardcoded connection strings for agent-generated Azure Functions code.
- Azure Functions agent workflows can depend-on Foundry, Connector Namespaces, remote MCP servers, and dynamic sessions; each adds a separate auth/audit boundary.
- Cosmos DB MCP Toolkit uses Azure identity/RBAC to expose database tools to agents through MCP.

### HoneyDrunk implications
- If HoneyDrunk builds Azure Functions with agents, install skills into a test repo first and inspect generated MCP/hook/instruction artifacts before committing them as standard.
- Treat Azure Functions `doctor` as a pre-deploy gate candidate, but keep `--deep` semantic checks away from untrusted PRs.
- Do not expose Cosmos DB MCP tools to agents without scoped managed identities, read/write tool separation, and audit logs; database tool convenience increases data-exposure blast radius.

### Quality notes
- Azure Functions skills are public preview; Cosmos DB MCP Toolkit is GA. Validate current package behavior, generated files, and role assignments locally before production use.

## 2026-06-04 compile additions

### Claims
- Microsoft Foundry Build 2026 positions hosted agents as a managed runtime for framework-agnostic production agents, including session sandboxing, durable state/file access, long-running agents, routines, and deployment into Microsoft Teams / Microsoft 365 Copilot. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-and-run-agents-at-scale-with-microsoft-fo.md]
- Foundry autopilot agents are described as independently acting agents with Entra Agent ID, email address, Microsoft Teams presence, org-chart placement, attribution, auditability, and governance through Agent 365. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-and-run-agents-at-scale-with-microsoft-fo.md]
- Azure Cosmos DB's 2026 Build release makes several agent/data capabilities GA or preview: MCP Toolkit GA, Agent Kit GA, Agent Memory Toolkit public preview, Semantic Reranking public preview, Linux Emulator GA, GSIs GA, Per-Partition Automatic Failover GA, Distributed Transactions preview, and Azure Backup preview. confidence: 1 Microsoft Azure Cosmos DB source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-azure-cosmos-db-blog-announced-at-ms-build-2026-azure-cosmos-db-mcp-to.md]
- Per-Partition Automatic Failover lets Cosmos DB fail over only affected partitions during regional disruption, while unaffected partitions continue operating; this strengthens Cosmos DB as agent memory/retrieval infrastructure for mission-critical workloads. confidence: 1 Microsoft Azure Cosmos DB source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-azure-cosmos-db-blog-announced-at-ms-build-2026-azure-cosmos-db-mcp-to.md]

### Typed entities
- service: Foundry Agent Service
- product: Microsoft Teams
- product: Microsoft 365 Copilot
- identity: Entra Agent ID
- product/control plane: Agent 365
- service: Azure Cosmos DB
- feature: Agent Memory Toolkit
- feature: Per-Partition Automatic Failover
- feature: Distributed Transactions
- feature: Azure Backup for Azure Cosmos DB
- feature: Azure Cosmos DB Linux Emulator

### Explicit relationships
- Hosted agents depend-on identity, sandboxing, durable state, audit, and distribution policy when they leave local development.
- Autopilot agents use Entra Agent ID and Microsoft 365 presence as accountable enterprise actors.
- Cosmos DB agent memory depends-on database resilience, backup, partition strategy, and retrieval relevance, not only vector search.
- Per-Partition Automatic Failover complements multi-region agent applications by reducing blast radius during regional disruption.

### HoneyDrunk implications
- If HoneyDrunk exposes agents in Teams/M365, treat agent identity as an audited enterprise principal with separate permissions from the human operator.
- For Cosmos-backed agent memory, define partition keys, GSI strategy, backup/restore posture, and failover requirements before storing durable agent state.
- Validate Build 2026 preview features locally before depending on them for production agent memory or data planes.

## 2026-06-05 compile additions

### Claims
- Foundry IQ knowledge bases are generally available as a production knowledge layer with stable APIs, SLA coverage, compliance certifications, output/activity logs, minimal retrieval reasoning effort, and a Foundry IQ MCP server for MCP-compatible hosts. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-foundry-iq-build-smarter-agents-faster-with-unified-knowledge-and-server.md]
- Foundry IQ Serverless Developer tier is in public preview with scale-to-zero pricing, Compute Unit metering, and preview limits such as 1 GB indexed storage per index and 30 indexes per service. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-foundry-iq-build-smarter-agents-faster-with-unified-knowledge-and-server.md]
- Foundry IQ preview sources can unify Work IQ, Fabric IQ, File Search, Azure SQL, and MCP sources into multi-source knowledge bases while respecting permission models; Web IQ adds external web/news/image/video/shopping grounding with zero data retention claims. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-foundry-iq-build-smarter-agents-faster-with-unified-knowledge-and-server.md]
- Microsoft Fabric Build 2026 announced Rayfin, an open-source SDK/CLI that lets developers and coding agents define data models, backend logic, and access policies in code and deploy an enterprise-grade application backend to Microsoft Fabric. confidence: 1 Microsoft Fabric source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-mic.md]
- Azure HorizonDB is in public preview as a managed PostgreSQL-compatible database for AI applications, with claimed zone resilience, 128 TB elastic storage, scale-out compute up to 3,072 vCores, vector search, AI model management, and direct Foundry/Fabric connectivity. confidence: 1 Microsoft source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-mic.md]
- Fabric IQ is generally available as a shared business-context layer, with graph in Fabric generally available and planning in Fabric expected later in June 2026; Ontologies are previewed in Foundry and Agent 365 as knowledge/tool surfaces. confidence: 1 Microsoft Fabric source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-mic.md]

### Typed entities
- product: Foundry IQ
- feature: Foundry IQ Serverless
- product: Work IQ
- product: Fabric IQ
- product: Web IQ
- product: Rayfin
- database: Azure HorizonDB
- service: Microsoft Fabric
- service: OneLake
- feature: Fabric graph
- feature: planning in Fabric
- concept: ontology
- product/control plane: Agent 365

### Explicit relationships
- Foundry IQ uses MCP to expose governed knowledge bases to non-Microsoft agent hosts.
- Foundry IQ Serverless uses scale-to-zero retrieval infrastructure for bursty agent workloads.
- Work IQ, Fabric IQ, File Search, Azure SQL, MCP, and Web IQ act as knowledge sources behind Foundry IQ retrieval.
- Rayfin uses code-defined backend/data/access policy to move agent-created applications from prototype to Fabric-hosted production backends.
- Fabric IQ ontologies and graph features give agents relationship-aware business context rather than raw table/document access alone.
- HorizonDB complements Cosmos DB and Fabric as an AI-application data plane option for PostgreSQL-compatible workloads.

### HoneyDrunk implications
- Treat Foundry IQ as a candidate managed retrieval/MCP layer only after validating tenant permissions, source indexing quality, trace/log export, cost, and local connector fit.
- If HoneyDrunk prototypes agent-created internal apps, Rayfin is a watchlist item for Fabric-backed apps, but lock-in and preview maturity need evaluation.
- Do not put durable agent memory or business context into Microsoft data planes until partitioning, backup, redaction, identity, and retrieval-eval policies are explicit.

### Quality notes
- Microsoft Build claims mix GA and preview features. The exact maturity, pricing, region availability, and admin controls should be verified before architectural commitment.

## 2026-06-07 compile additions

### Claims
- Azure Functions serverless agents quickstart deploys a Flex Consumption function app with Foundry resources, model deployment, storage, monitoring, Azure Container Apps dynamic session pool, and optional Connector Namespace / Microsoft 365 Outlook managed MCP server for email delivery. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-quickstart-build-serverless-agents-using-azure-functions.md]
- The serverless agents sample separates a chat/debug agent from a timer-triggered digest agent; email delivery requires a Microsoft 365 connector authorization, while the debug chat agent uses a function key and can use sandboxed Python and web browsing. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-quickstart-build-serverless-agents-using-azure-functions.md]
- Foundry Managed Compute is a preview model-hosting deployment type for open-source and custom models on dedicated GPU capacity, using Foundry model catalog entries, deployment templates, accelerator-family quota, private networking, Entra/RBAC, Azure Monitor metrics, and one Foundry endpoint/SDK surface. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-announcing-foundry-managed-compute-run-open-models-in-microsoft-foundr.md]
- Foundry Managed Compute routing includes concurrency-aware load balancing, prompt-prefix affinity for KV-cache reuse, and multi-turn session affinity with load bounds. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-announcing-foundry-managed-compute-run-open-models-in-microsoft-foundr.md]

### Typed entities
- service/runtime: Azure Functions serverless agents runtime
- plan: Flex Consumption
- service: Microsoft Foundry
- resource: Azure Container Apps dynamic session pool
- resource: Connector Namespace
- connector: Microsoft 365 Outlook
- service: Foundry Managed Compute
- accelerator families: A100, H100, MI300X
- control: prompt-prefix affinity
- control: multi-turn session affinity

### Explicit relationships
- Azure Functions serverless agents use managed identities and connector authorization to bind Functions-hosted agents to Foundry, dynamic sessions, and managed MCP connectors.
- Connector Namespace authorization complements function-app managed identity; both must be configured before email-capable agent tools work.
- Foundry Managed Compute complements pay-per-token and provisioned throughput by hosting open/custom models under the same Foundry governance surface.
- Prompt-prefix affinity depends-on repeated shared prompts, tool definitions, or RAG context to improve cache locality.

### HoneyDrunk implications
- If HoneyDrunk tests serverless agents, evaluate connector consent, function-key/debug exposure, dynamic-session egress/logging, and managed identity scope before any shared automation.
- Treat Foundry Managed Compute as an open-model hosting candidate only after comparing it with direct Azure VMs, DigitalOcean, local hosting, and existing provider APIs on cost, latency, auth, and rollback.

### Quality notes
- Both Microsoft sources are preview/product documentation. Verify region, quota, pricing, auth behavior, and current deployment-template availability before design commitments.
