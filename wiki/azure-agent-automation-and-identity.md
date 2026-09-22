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

## 2026-06-10 compile additions: Foundry gateway and baseline chat architecture

### Source-backed claims
- Microsoft Foundry model endpoints are commonly consumed through HTTP APIs by clients or orchestrators such as Agent Framework, Semantic Kernel, LangChain, and Foundry Agent Service; direct access pushes retry, circuit breaking, failover, model selection, throttling, and telemetry into every client. Source: `raw/2026-06-10-web-microsoft-learn-access-foundry-models-and-other-language-models-through-a-gateway-azure.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft guidance presents a gateway/reverse-proxy layer as a way to centralize model-level authorization, API-key hiding, routing, failover, rate limits, logging, and policy. Source: `raw/2026-06-10-web-microsoft-learn-access-foundry-models-and-other-language-models-through-a-gateway-azure.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft's baseline Foundry chat architecture places the chat application in front of Foundry Agent Service as the access boundary, authenticates users with Microsoft Entra ID, and enforces per-user conversation and agent authorization in the application layer. Source: `raw/2026-06-10-web-microsoft-learn-baseline-microsoft-foundry-chat-reference-architecture-azure-architectur.md`. confidence: 1 source, last-confirmed 2026-06-10.
- The baseline notes that any principal with the Foundry User role on a project can interact with all agents in that project, so project RBAC alone is not sufficient for consumer-facing per-agent authorization. Source: `raw/2026-06-10-web-microsoft-learn-baseline-microsoft-foundry-chat-reference-architecture-azure-architectur.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Foundry Agent Service lacks built-in blue-green or canary agent deployment, so progressive rollout and failback require routing/API-gateway/application logic outside the managed service. Source: `raw/2026-06-10-web-microsoft-learn-baseline-microsoft-foundry-chat-reference-architecture-azure-architectur.md`. confidence: 1 source, last-confirmed 2026-06-10.

### Typed entities
- project: Microsoft Foundry
- project: Foundry Agent Service
- project: Microsoft Entra ID
- project: Azure API Management
- concept: reverse proxy
- concept: project-level RBAC
- decision: Foundry app access-boundary pattern

### Explicit relationships
- Foundry direct model access depends-on every client implementing resilience and policy.
- Gateway access centralizes auth, routing, failover, telemetry, and throttling.
- Foundry project RBAC contradicts fine-grained per-agent consumer authorization requirements.
- Progressive agent rollout depends-on application or gateway routing outside Foundry Agent Service.

### HoneyDrunk implications
- If HoneyDrunk adopts Foundry agents, put user authorization, conversation scoping, rollout, and fallback in HoneyDrunk-owned app/gateway code.
- Avoid broad project credentials in clients or low-trust tools.
- Compare Foundry baseline complexity against lighter self-hosted agent patterns before committing.

### Quality notes
- Microsoft Learn is authoritative for Microsoft architectural guidance, but current service limits, role behavior, and region support must be checked before implementation.

## 2026-06-18 compile additions: Azure service-selection checklist and AWS MCP diagnostics pattern

### Source-backed claims
- Microsoft Architecture Center recommends prebuilt AI services and Foundry Tools/Models for many intelligent workload features, while Azure Machine Learning is the custom-model path when existing services cannot support the required function or exclusive data/model control. Source: `raw/2026-06-18-web-learn-microsoft-com-choose-an-azure-ai-technology-azure-architecture-c.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-18.
- The same source identifies Foundry Local as an on-device inference option for performance, privacy, customization, and cost cases. Source: `raw/2026-06-18-web-learn-microsoft-com-choose-an-azure-ai-technology-azure-architecture-c.md`. confidence: 1 source, last-confirmed 2026-06-18.
- AWS DevOps Agent can be extended through custom MCP servers for diagnostic data outside native integrations; the EKS node diagnostics pattern uses SSM Automation to collect node logs, stores/extracts them through S3, pre-indexes findings, and exposes structured tools through AgentCore Gateway. Source: `raw/2026-06-18-web-aws-amazon-com-diagnose-eks-node-issues-faster-with-aws-devops-agent-a.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 AWS DevOps Blog source, last-confirmed 2026-06-18.

### Typed entities
- service: Foundry Tools
- service: Foundry Models
- service: Foundry Local
- service: Azure Machine Learning
- service: AWS DevOps Agent
- service: Amazon EKS
- service: AWS Systems Manager Automation / SSM Automation
- service: Amazon Bedrock AgentCore Gateway
- concept: diagnostic MCP bridge
- control: non-interactive audited execution

### Explicit relationships
- Azure prebuilt services complement custom ML by reducing setup for common capabilities; custom ML supersedes them when capability or data-control requirements exceed prebuilt offerings.
- On-device inference complements cloud AI services when privacy, latency, offline behavior, customization, or recurring cost dominate.
- AWS diagnostic MCP bridges agent visibility gaps while SSM Automation mediates the host boundary.

### HoneyDrunk implications
- For AI service choices, write the workload need first: agent, RAG, targeted language, speech, image/video, content safety, custom model, or local inference.
- If HoneyDrunk builds operations agents, copy the pattern of structured diagnostic tools plus auditable host mediation rather than broad shell access.

### Quality notes
- Microsoft and AWS sources are platform-authored architecture/product guidance. Validate current service availability, pricing, auth, and operational constraints before adopting.

## 2026-06-19 compile additions: Azure SRE Agent networking and code interpreter sessions

### Source-backed claims
- Azure SRE Agent supports egress modes including Unrestricted, Limited, and Azure VNet; selecting Azure VNet routes agent traffic through a delegated subnet and disables the other mode cards until the VNet is disconnected. Source: `raw/2026-06-19-web-learn-microsoft-com-configure-network-controls-for-azure-sre-agent.md`. confidence: 1 Microsoft Learn source with access warning in capture, last-confirmed 2026-06-19.
- Azure SRE Agent VNet integration requires a `/28` or larger subnet delegated to `Microsoft.App/environments`, Network Contributor-equivalent subnet join permission, and SRE Agent Administrator permission on the agent resource. Source: `raw/2026-06-19-web-learn-microsoft-com-configure-network-controls-for-azure-sre-agent.md`. confidence: 1 source, last-confirmed 2026-06-19.
  - superseded-by: [GA network requirements](#2026-09-19-sre-agent-ga-network-scope-and-subnet-requirements); timestamp: 2026-09-19T12:29:11-04:00; reason: the August 25 official GA announcement requires an empty dedicated /27-or-larger subnet in the agent region. It is newer than the June Learn capture with an access warning and unknown publication date; prefer /27 for planning and verify the target deployment. The older /28 claim remains as history; unrelated permission prerequisites are not withdrawn. confidence: 1 source, last-confirmed 2026-09-19 (archived capture reviewed). [captured source](../raw/2026-09-19-rss-azure-sre-agent-vnet-boundaries.md)
- Azure Container Apps code interpreter sessions provide Hyper-V-isolated Python execution sessions for LLM-generated or user-submitted code, with session pools controlling maximum concurrency and idle stop behavior. Source: `raw/2026-06-19-web-learn-microsoft-com-serverless-code-interpreter-sessions-in-azure-container-apps.md`. confidence: 1 Microsoft Learn source with access warning in capture, last-confirmed 2026-06-19.
- Code interpreter session access uses Microsoft Entra tokens for identities with Azure ContainerApps Session Executor and Contributor roles on the session pool, and direct API calls require an audience claim of `https://dynamicsessions.io`. Source: `raw/2026-06-19-web-learn-microsoft-com-serverless-code-interpreter-sessions-in-azure-container-apps.md`. confidence: 1 source, last-confirmed 2026-06-19.
- Code interpreter sessions expose file upload/download/list metadata endpoints and execution endpoints; file uploads are stored under `/mnt/data`, individual executions are capped at 220 seconds, and service metrics are returned in response headers rather than Log Analytics. Source: `raw/2026-06-19-web-learn-microsoft-com-serverless-code-interpreter-sessions-in-azure-container-apps.md`. confidence: 1 source, last-confirmed 2026-06-19.

### Typed entities
- service: Azure SRE Agent
- egress mode: Azure VNet
- subnet delegation: `Microsoft.App/environments`
- service: Azure Container Apps code interpreter sessions
- resource: session pool
- role: Azure ContainerApps Session Executor
- role: Contributor
- endpoint: `dynamicsessions.io`
- directory: `/mnt/data`

### Explicit relationships
- Azure SRE Agent private endpoint access depends-on VNet integration and private DNS zone linking.
- Managed-path toggles complement VNet egress by allowing specific public service categories such as package registries or code repositories.
- Code interpreter sessions depend-on session identifiers for reuse; session identifiers must be scoped to user, tenant, or conversation boundaries.
- ACA session-pool APIs use Entra authorization and role assignments rather than raw shared API keys in the captured code-interpreter path.

### HoneyDrunk implications
- If Azure SRE Agent is tested, document whether remote MCP, package registry, and code repository traffic use VNet egress or managed paths.
- If ACA code interpreter sessions are evaluated for OpenClaw/Honeyclaw, define session-id derivation, tenant isolation, file retention, cleanup calls, response-header metric capture, and app-side request/response logging first.
- Do not assume Log Analytics has full execution traces for code interpreter sessions; collect request IDs, inputs, outputs, and metrics at the calling application boundary where policy permits.

### Quality notes
- The captures include Microsoft Learn authorization warnings and may reflect preview/protected documentation. Verify current public docs, API versions, pricing, and telemetry before implementation.

## 2026-06-23 compile additions: Azure AI Search knowledge bases and Agent Server preview

### Source-backed claims
- Azure SDK May 2026 says Azure AI Search .NET 12.0.0 and Python `azure-search-documents` 12.0.0 add knowledge bases and `KnowledgeBaseRetrievalClient` support for agentic retrieval over Blob storage, search indexes, OneLake, and web sources on service version 2026-04-01. Source: `raw/2026-06-23-rss-azure-blog-azure-sdk-release-may-2026.md`; page: [[microsoft-dotnet-ai-stack]]. confidence: 1 Microsoft Azure SDK release source, last-confirmed 2026-06-23.
- The same release announces preview Azure AI Agent Server libraries with `AgentServerHost`, health probes, graceful shutdown, request-ID middleware, centralized platform headers, and consolidated .NET hosting extension methods. Source: `raw/2026-06-23-rss-azure-blog-azure-sdk-release-may-2026.md`. confidence: 1 Microsoft Azure SDK release source, last-confirmed 2026-06-23.

### Typed entities
- service: Azure AI Search
- concept: knowledge base
- API/client: `KnowledgeBaseRetrievalClient`
- source backend: Azure Blob Storage
- source backend: OneLake
- library: `Azure.AI.AgentServer.Core`
- library: `azure-ai-agentserver-core`
- host abstraction: `AgentServerHost`
- middleware: request ID middleware

### Explicit relationships
- Azure AI Search knowledge bases complement agent automation by packaging retrieval sources behind a managed client.
- Agent Server preview packages complement custom agent hosts with health, shutdown, correlation, and platform-header plumbing.
- Managed retrieval and hosted-agent packages depend-on identity, network, logging, and preview-stability review before production use.

### HoneyDrunk implications
- Track Azure AI Search knowledge bases as a possible managed retrieval backend for Lore/Knowledge, but preserve raw/wiki citations as authority.
- Do not adopt Agent Server preview libraries in production until package stability, auth model, logging, cost, and operational hooks are verified.

### Quality notes
- Microsoft release notes are authoritative for release direction but time-sensitive. Recheck package/API status before a spike.

## 2026-06-28 compile additions: azd execution, tool management, and Functions MCP

### Source-backed claims
- Azure Developer CLI releases 1.24.3 through 1.26.0 added an `azd tool` command group for discovering, installing, checking, and upgrading development tools such as language SDKs, Bicep, Docker, GitHub CLI, VS Code extensions, and supported agentic CLI host skills. Source: `raw/2026-06-28-rss-azure-sdk-blog-azure-developer-cli-azd.md`. confidence: 1 Microsoft Azure SDK Blog source, last-confirmed 2026-06-28.
- The same source introduces `azd exec`, a cross-platform command/script runner that inherits the full `azd` environment, including environment variables and Key Vault secret resolution. Source: `raw/2026-06-28-rss-azure-sdk-blog-azure-developer-cli-azd.md`. confidence: 1 source, last-confirmed 2026-06-28.
- The `azd` source says parallel `azd up` work required fixes for concurrent map writes, ACR remote-build image contamination, per-request correlation IDs, parallel `.NET` publish races, and service-detail progress rendering. Source: `raw/2026-06-28-rss-azure-sdk-blog-azure-developer-cli-azd.md`. confidence: 1 source, last-confirmed 2026-06-28.
- `azd pipeline config` now accounts for customized GitHub OIDC subject formats when creating federated credentials, reducing AADSTS700213 mismatch failures for organizations with custom claims. Source: `raw/2026-06-28-rss-azure-sdk-blog-azure-developer-cli-azd.md`. confidence: 1 source, last-confirmed 2026-06-28.
- Azure Functions MCP Extension adds tool/resource/prompt triggers, MCP Apps, built-in MCP auth, OBO examples, structured content, rich content, and output schemas for Azure-hosted MCP servers. Source: `raw/2026-06-28-rss-azure-sdk-blog-azure-functions-mcp-extension-what-s-new-at-build-2026.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 Microsoft source, last-confirmed 2026-06-28.

### Typed entities
- CLI: Azure Developer CLI / `azd`
- command group: `azd tool`
- command: `azd exec`
- secret store: Azure Key Vault
- config field: `dependsOn` in `azure.yaml`
- service: Azure Container Registry / ACR
- auth mechanism: GitHub OIDC federated credential
- error: AADSTS700213
- product: Azure Functions MCP Extension
- page: [[mcp-tool-governance-and-app-surfaces]]

### Explicit relationships
- `azd tool` complements template onboarding by turning prerequisite discovery into a first-class command.
- `azd exec` depends-on `azd` environment and Key Vault resolution, so scripts run through it inherit a stronger secret boundary than ordinary shell scripts.
- Parallel deploy speed depends-on per-service artifact isolation, unique upload blobs, thread-safe environment access, and per-request correlation IDs.
- GitHub OIDC federated credential creation depends-on organization-specific subject claims when defaults are customized.
- Functions-hosted MCP depends-on Entra/OBO and tool schemas to move from demo server to governed remote tool surface.

### HoneyDrunk implications
- For HoneyDrunk `azd` workflows, prefer `azd exec` only when the inherited environment and secret resolution are intentional and logged.
- If using parallel `azd up`, audit services for shared build output paths, shared ACR upload names, and ambiguous progress/log correlation.
- For GitHub-to-Azure federation, record the exact OIDC subject format rather than assuming GitHub defaults.
- Functions MCP is a viable Azure-hosted tool surface candidate, but HoneyDrunk should require auth, schema, observability, and per-tool capability review before exposing it to agents.

### Quality notes
- Microsoft source is authoritative for release notes. Validate installed `azd` version and preview status before relying on a feature in CI.

## 2026-07-06 compile additions: Azure SDK June 2026

### Source-backed claims
- Azure SDK June 2026 release notes announce Python `azure-ai-transcription` 1.0.0 GA as the first stable client library for Azure AI Transcription. Source: `raw/2026-07-06-rss-azure-blog-azure-sdk-release-june-2026.md`. confidence: 1 Microsoft Azure SDK release source, last-confirmed 2026-07-06.
- The same release announces Python `azure-planetarycomputer` 1.0.0 GA with richer response models and a breaking rename from `StacOperations.list_collections` to `StacOperations.get_collections`. Source: `raw/2026-07-06-rss-azure-blog-azure-sdk-release-june-2026.md`. confidence: 1 Microsoft source, last-confirmed 2026-07-06.
- June 2026 initial beta packages include Agent Server - Optimization and AI Discovery for Python plus Discovery and File Shares management libraries, reinforcing that Azure agent/data-plane SDKs are still adding preview surfaces around optimization and discovery. Source: `raw/2026-07-06-rss-azure-blog-azure-sdk-release-june-2026.md`. confidence: 1 release-note source, last-confirmed 2026-07-06.

### Typed entities
- package: `azure-ai-transcription` 1.0.0
- package: `azure-planetarycomputer` 1.0.0
- operation: `StacOperations.get_collections`
- preview package: Agent Server - Optimization 1.0.0b1
- preview package: AI Discovery 1.0.0b1
- management package: Resource Management - Discovery 1.0.0b1
- management package: Resource Management - File Shares 1.0.0b1

### Explicit relationships
- Stable Azure SDK clients supersede preview client assumptions for transcription and Planetary Computer integrations.
- Agent Server optimization and AI Discovery beta packages complement earlier Agent Server preview notes but do not supersede the need for preview-stability review.

### HoneyDrunk implications
- If HoneyDrunk needs speech transcription or geospatial/planetary data workflows, use the GA Python clients as the baseline and check breaking API names before upgrading.
- Keep Agent Server optimization and AI Discovery on the watchlist, but do not promote preview SDKs into production agent infrastructure without auth, logging, and package-stability review.

### Quality notes
- Microsoft release notes are authoritative for package release posture as of 2026-07-06. Recheck package docs before implementation because SDK releases are monthly and preview packages can churn.

## 2026-08-12 compile additions: azd extension framework GA and July SDK management releases

### Source-backed claims
- Azure Developer CLI extension framework is GA as of the captured Azure Blog source, with stabilized extension interfaces, lifecycle/provider integration points, project-level extension requirements, and authoring/publishing support through `azd x developer`. Source: `raw/2026-08-12-rss-azure-blog-azure-developer-cli-extension-framework-is-ga-build-dev-wor.md`. confidence: 1 Microsoft Azure Blog source, last-confirmed 2026-08-12.
- The GA framework lets extensions add command namespaces, lifecycle handlers, custom service targets, language/framework support, provisioning providers, validation providers, and MCP tools; the GA posture applies to the extension framework rather than automatically production-hardening every extension built on it. Source: `raw/2026-08-12-rss-azure-blog-azure-developer-cli-extension-framework-is-ga-build-dev-wor.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 source, last-confirmed 2026-08-12.
- Azure SDK July 2026 release notes announced GA Python management packages for App Service Domain Registration, App Service Certificate Registration, Resource Health, and Data Boundaries, including tenant-level data boundary management for EU Data Boundary compliance workflows. Source: `raw/2026-08-12-rss-azure-blog-azure-sdk-release-july-2026.md`. confidence: 1 Microsoft Azure SDK release source, last-confirmed 2026-08-12.

### Typed entities
- CLI: Azure Developer CLI / `azd`
- framework: Azure Developer CLI extension framework
- command group: `azd x developer`
- concept: project-level extension requirement
- integration point: lifecycle handler
- integration point: provisioning provider
- integration point: validation provider
- tool surface: MCP tool
- package family: Python App Service Domain Registration
- package family: Python App Service Certificate Registration
- package family: Python Resource Health
- package family: Python Data Boundaries
- compliance concept: EU Data Boundary

### Explicit relationships
- `azd` extensions depend-on project-level requirements and version constraints when a template needs a repeatable toolchain.
- Extension lifecycle and provider hooks complement `azd exec` and `azd tool` by moving custom workflow behavior into a governed CLI extension surface.
- Data Boundaries management complements Azure governance by making tenant-level data-boundary configuration programmable.
- MCP-capable `azd` extensions overlap-with [[mcp-tool-governance-and-app-surfaces]] and should inherit the same provenance, auth, logging, and approval controls as other agent tools.

### HoneyDrunk implications
- Treat `azd` extension authoring as a viable packaging path for HoneyDrunk Azure workflows, but require owner, version, source, and capability review before project templates depend on an extension.
- If EU Data Boundary concerns appear in HoneyDrunk Azure tenants, prefer the GA management package as a governance automation candidate after a tenant-scope permissions review.
- Keep private/dev/nightly extension sources out of unattended CI unless their source registry, signature or checksum posture, and rollback path are explicit.

### Quality notes
- Microsoft sources are authoritative for release posture. Validate installed `azd` and SDK package versions before using these features in production automation.

## 2026-08-13 compile additions: azd July 2026 releases

### Source-backed claims
- Azure Developer CLI July 2026 shipped releases 1.27.0 through 1.29.0, adding `azd tool uninstall`, direct extension install from registry locations with `-s/--source`, `--no-dependencies`, Azure AI Foundry modeling in `azure.yaml`, container deployment for Azure App Service, provider-agnostic provision validation, and automatic non-interactive mode in CI/CD or AI-agent environments. Source: `raw/2026-08-13-rss-azure-blog-azure-developer-cli-azd-july-2026.md`. confidence: 1 Microsoft Azure SDK Blog source, last-confirmed 2026-08-13.
- The same release renamed the `azd tool` `--host` flag to `--agent`, changed JSON output shape for installed skills, and fixed several extension/tool behaviors including functional host probing, uninstall handling, Windows extension replacement file locks, serialized `azure.yaml` writes, and project extension requirement resolution. Source: `raw/2026-08-13-rss-azure-blog-azure-developer-cli-azd-july-2026.md`. confidence: 1 source, last-confirmed 2026-08-13.
- July 2026 `azd` templates include Azure Functions Timer and Durable Functions fan-out/fan-in quickstarts across several languages, remote MCP Functions samples with Entra auth and Durable Functions long-running MCP tools, and secure-by-default managed identity/VNet patterns. Source: `raw/2026-08-13-rss-azure-blog-azure-developer-cli-azd-july-2026.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 source, last-confirmed 2026-08-13.

### Typed entities
- CLI: Azure Developer CLI / `azd`
- version range: `azd` 1.27.0-1.29.0
- command: `azd tool uninstall`
- flag: `--agent`
- former flag: `--host`
- flag: `--no-dependencies`
- option: `-s` / `--source`
- config file: `azure.yaml`
- service host: Azure App Service containers
- host/resource: Azure AI Foundry project and agent
- environment: CI/CD or AI-agent environment
- sample: Remote MCP Functions
- auth mechanism: Microsoft Entra
- workflow: Durable Functions long-running MCP tool

### Explicit relationships
- `azd tool uninstall` completes the install/upgrade/uninstall lifecycle introduced by earlier `azd tool` releases.
- Direct extension-source installation depends-on provenance review because URL/local-path sources become persisted extension sources.
- Automatic non-interactive mode complements scheduled and AI-agent automation by failing fast instead of waiting on prompts.
- The `--agent` rename supersedes `--host` for `azd tool` scripts and JSON consumers.
- Remote MCP Functions samples connect Azure Functions, Entra auth, Durable Functions, and `azd` deployment into an MCP hosting path.

### HoneyDrunk implications
- Audit any HoneyDrunk scripts that call `azd tool --host` or parse `azd tool list --output json` before upgrading to these releases.
- For unattended `azd` runs, rely on non-interactive failure behavior but keep explicit validation and rollback around destructive operations such as `azd down`.
- Do not allow arbitrary extension `--source` URLs/paths in CI without owner, checksum/signature, channel, and dependency policy.
- Remote MCP Functions templates are worth a scoped spike only when Entra auth, long-running task polling, observability, and cost controls are part of the acceptance criteria.

### Quality notes
- Microsoft release notes are authoritative for feature existence. Validate installed `azd` version, runner environment detection, and breaking-output changes before migration.

## 2026-08-24 compile additions: MCP-capable azd extensions and ACA status-source caveat

### Source-backed claims
- Microsoft Learn says an `azd` extension can declare the `mcp-server` capability in `extension.yaml`, optionally configure MCP startup args/env, and expose tools to agents by adding an MCP server command such as `mcp start` that serves over stdio. Source: `raw/2026-08-24-web-microsoft-learn-add-an-mcp-server-to-an-extension.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 Microsoft Learn source, last-confirmed 2026-08-24.
- The `azd` extension example uses a Go MCP server library to register a `suggest_tags` tool for standardized Azure resource tags; this is a pattern for extension-owned tools rather than proof that all extension commands are safe for agent use. Source: `raw/2026-08-24-web-microsoft-learn-add-an-mcp-server-to-an-extension.md`. confidence: 1 source, last-confirmed 2026-08-24.
- The Azure Container Apps "what's new" source captured on 2026-08-24 lists dynamic sessions as May 2024 public preview and points newer updates to GitHub, so current ACA feature status should be verified from targeted docs or release notes rather than this stale index. Source: `raw/2026-08-24-web-microsoft-learn-what-s-new-in-azure-container-apps-azure-container-app.md`. confidence: 1 stale Microsoft Learn index source, last-confirmed 2026-08-24.

### Typed entities
- CLI: Azure Developer CLI / `azd`
- manifest: `extension.yaml`
- capability: `mcp-server`
- command: `mcp start`
- tool example: `suggest_tags`
- platform: Azure Container Apps dynamic sessions

### Explicit relationships
- MCP-capable `azd` extensions combine deployment lifecycle extension risk with agent tool-surface risk.
- Extension-owned MCP tools depend-on extension provenance, command authorization, input validation, and audit logging.
- Stale product-index pages should not supersede targeted current documentation for preview/GA status.

### HoneyDrunk implications
- If HoneyDrunk builds Azure workflow extensions, decide separately which commands become MCP tools; do not expose whole extension command surfaces by default.
- Add source/version/owner/capability metadata for any `azd` extension that a repo requires or an agent can invoke.
- Recheck ACA dynamic-session current status before any production session-pool design.

### Quality notes
- Microsoft Learn source is authoritative for the extension authoring pattern. ACA status source is useful as a pointer, not as current product status evidence.

## 2026-09-04 compile additions: azd August 2026 releases and Azure SRE Agent connectors

### Source-backed claims
- Azure Developer CLI August 2026 covered releases 1.30.0 through 1.32.0, including the GA `azd` extension framework, Azure Functions container deploy from Dockerfiles, prebuilt images, or ACR remote builds, layered provisioning dependency inference, HTTPS extension bundles with checksum handling, and improved exact-version install behavior. Source: `raw/2026-09-04-rss-azure-blog-azure-developer-cli-azd-august-2026.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 Microsoft Azure Blog source, last-confirmed 2026-09-04.
- The same `azd` source says automation behavior improved for AI-agent environments by recognizing Codex and Cursor, fixing unsupported non-C# Aspire AppHost handling, improving GitHub immutable OIDC subject claims, supporting Azure DevOps federated auth, and avoiding indefinite Aspire hangs. Source: `raw/2026-09-04-rss-azure-blog-azure-developer-cli-azd-august-2026.md`. confidence: 1 source, last-confirmed 2026-09-04.
- Microsoft describes Azure SRE Agent as an operational agent that can investigate incidents, perform health checks, answer what-changed questions, check compliance, and propose remediations with human approval using native integrations such as GitHub, Datadog, New Relic, and Splunk plus MCP connectors hosted through Connector Namespace. Source: `raw/2026-09-04-rss-azure-blog-power-azure-sre-agent-with-the-tools-it-needs.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 Microsoft Azure Blog source, last-confirmed 2026-09-04.
- Connector Namespace is in preview as a managed MCP hosting surface, with GA estimated by Microsoft for the end of 2026, and supports catalog connectors such as Azure SQL, Cosmos DB, GitLab, Jira, and PagerDuty while bring-your-own MCP server images remain in development. Source: `raw/2026-09-04-rss-azure-blog-power-azure-sre-agent-with-the-tools-it-needs.md`. confidence: 1 source, last-confirmed 2026-09-04.

### Typed entities
- CLI: Azure Developer CLI / `azd`
- version range: `azd` 1.30.0-1.32.0
- product/agent: Azure SRE Agent
- hosting surface: Connector Namespace
- connector: Azure SQL MCP
- connector: Cosmos DB MCP
- connector: GitLab MCP
- connector: Jira MCP
- connector: PagerDuty MCP
- auth mechanism: managed identity
- token scope: `https://apihub.azure.com/.default`
- identity provider: Microsoft Entra

### Explicit relationships
- `azd` extension GA supersedes preview-only extension-framework assumptions, but individual extensions still depend-on source, version, owner, and checksum review.
- AI-agent environment detection complements non-interactive automation by reducing prompt hangs in Codex/Cursor-driven runs.
- Azure SRE Agent depends-on connector identity, access policies, managed identity, and human approval before operational remediation.
- Connector Namespace complements custom MCP hosting by moving connector deployment, identity, and endpoint management into Azure infrastructure.

### HoneyDrunk implications
- For Azure automation templates, update the `azd` watchlist to include Functions container deploy, exact-version install, federated auth, and AI-agent non-interactive behavior.
- If HoneyDrunk evaluates Azure SRE Agent, start with read-only incident investigation and require connector access-policy review, trace capture, approval gates, and rollback notes before any remediation action.
- Treat Connector Namespace as promising but preview: verify region, connector catalog, BYO support, network path, billing, and GA status before production dependency.

### Quality notes
- Microsoft sources are authoritative for product direction. `azd` and Connector Namespace behavior is time-sensitive and needs live version/region verification before implementation.
## 2026-09-08 compile additions: Azure AI Discovery SDK surface

### Source-backed claims
- Azure SDK's August 2026 release says Azure AI Discovery reached 1.0.0 for Python and JavaScript, exposing Workspace conversations, investigations, tasks, tools, Bookshelf knowledge-base lifecycle, indexing, and citation-aware search operations. Source: `raw/2026-09-08-rss-azure-blog-azure-sdk-release-august-2026.md`; page: [[microsoft-dotnet-ai-stack]]. confidence: 1 Microsoft Azure SDK Blog source, last-confirmed 2026-09-08.
- The same release says Document Translation 2.0.0 added support for the 2026-03-01 service API, including translating text embedded in images for batch and single-document requests, custom translation model deployments, and expanded image scan reporting. Source: `raw/2026-09-08-rss-azure-blog-azure-sdk-release-august-2026.md`. confidence: 1 source, last-confirmed 2026-09-08.

### Typed entities
- library/service: Azure AI Discovery
- feature: Workspace conversations
- feature: investigations
- feature: tasks
- feature: tools
- feature: Bookshelf knowledge base
- service: Document Translation
- API version: 2026-03-01

### Explicit relationships
- Azure AI Discovery uses SDK surfaces to connect agent-like workspaces, tools, tasks, and citation-aware knowledge search.
- Document Translation image-text support complements document ingestion workflows where text appears inside images.

### HoneyDrunk implications
- Evaluate Azure AI Discovery only after confirming tenant availability, data retention, pricing, and whether Bookshelf/citation search overlaps with Lore needs.
- If multilingual image/document ingestion becomes important, test Document Translation 2.0.0 against representative PDFs/screenshots before designing a pipeline around it.

### Quality notes
- Microsoft release roundup is authoritative for package availability but not a substitute for service documentation, quotas, or local SDK testing.

## 2026-09-10 Azure SRE Agent sandbox and approval model

### Sources
- [Microsoft Command Line: Stop restricting the agent, start restricting its world](../raw/2026-09-10-web-microsoft-command-line-stop-restricting-the-agent-start-restricting-it.md)
- [Microsoft Command Line: Your agent's guardrails have a bypass](../raw/2026-09-10-web-microsoft-command-line-your-agent-s-guardrails-have-a-bypass.md)

### Typed entities
- `product`: Azure SRE Agent
- `runtime`: Azure Container Apps Sandbox
- `control`: default-deny egress
- `control`: approval classification
- `standard`: AGENT-HOOKS-0.1
- `framework`: Microsoft Agent Framework

### Claims
- Microsoft describes Azure SRE Agent as splitting trusted orchestration from model-authored tools/code that run inside per-agent Azure Container Apps Sandbox microVMs with default-deny egress and a narrow API. confidence: 1 source, last-confirmed 2026-09-10
- The Azure SRE Agent pattern classifies approval by operation, target, and evidence, with caller role and identity shaping available tools, MCP servers, memory, credentials, and approvals. confidence: 1 source, last-confirmed 2026-09-10
- AGENT-HOOKS-0.1 defines a cooperative lifecycle contract across startup, input, model calls, tool calls, output, and shutdown, returning allow/deny/transform verdicts with fail-closed host obligations. confidence: 1 source, last-confirmed 2026-09-10
- The Microsoft source explicitly frames Agent Hooks as governance and observability rather than a complete sandbox, security boundary, or hostile-host mediation layer. confidence: 1 source, last-confirmed 2026-09-10

### Explicit relationships
- Azure SRE Agent uses sandboxed execution and credential handles to reduce prompt-level safety dependence.
- Agent Hooks complement Azure SRE Agent-style policy by placing checks before and after model and tool activity.
- Hook approvals depend-on `context_identity` hashing to bind approval to exact content and reduce replay risk.
- Cooperative hooks do not supersede sandboxing, identity controls, or server-side authorization.

### HoneyDrunk implications
- Any HoneyDrunk remediation agent should prove sandbox egress controls, credential-handle behavior, approval evidence, and rollback paths before receiving production authority.
- Hook-style governance is useful for audit and consistency, but must be paired with runtime isolation and destination-side authorization.

### Quality notes
- Microsoft architecture sources are useful for control design but should be treated as vendor guidance until tested against concrete Azure tenant policy and incident-runbook workflows.

## 2026-09-14: Foundry July-August availability and SDK boundaries

### Typed entities

project: Microsoft Foundry; project: Foundry Hosted Agents; concept: Toolboxes; library: Foundry SDK.

### Claims and evidence

- Microsoft's September 9 roundup, as captured, reports general availability of Hosted Agents, Voice Live integration, and Toolboxes. Toolboxes place authentication and credentials behind an MCP-compatible endpoint; tool search and agent skills remain preview in this account. confidence: 1 source, last-confirmed 2026-09-14 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-13-rss-microsoft-foundry-what-s-new-in-microsoft-foundry-july-and-august-2026.md)
- At the roundup's August baseline, Python and JavaScript/TypeScript SDKs are stable at 2.5.0 and Java at 2.4.0, while .NET 3.0.0 remains preview. Runtime and management coverage differ by language; platform GA does not establish .NET SDK GA. confidence: 1 source, last-confirmed 2026-09-14 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-13-rss-microsoft-foundry-what-s-new-in-microsoft-foundry-july-and-august-2026.md)

### Explicit relationships

Foundry Hosted Agents uses managed hosting; Toolboxes uses external credential handling. This release account supersedes the earlier Hosted Agents GA forecast in [[ai-agent-harnesses]].

### Decision and quality notes

Vendor summary supports availability at its stated baseline. Verify current SDK, networking, cost, and runtime coverage before migration; no local deployment or current-version verification occurred. Source count is provisional single-source support; repeated citations and derived summaries add no independent corroboration. Open question: Which Foundry hosting, management, private-network, and Toolbox capabilities are available through the exact .NET SDK version HoneyDrunk would deploy? See [[indexes/gaps]].

## 2026-09-15: Extraction confidence calibration

### Typed entities

project: Azure Content Understanding; concept: field confidence; concept: grounding; concept: model deployment mapping.

### Claims and evidence

- Microsoft's August 12 guide compares models by workload and describes changes to grounding and confidence scoring. Vendor dataset, schema, and file-length choices constrain the reported quality and token-use improvements; field confidence distributions need separate calibration. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-microsoft-foundry-azure-content-understanding-gpt-5-series-guide-model.md)
- Its comparison procedure holds analyzer, schema, inputs, and labels fixed while varying modelDeployments, then inspects quality, latency, tokens, and failures. supportedModels, region, throughput, and capacity constrain the experiment. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-microsoft-foundry-azure-content-understanding-gpt-5-series-guide-model.md)

### Explicit relationships

Extraction acceptance depends-on per-field calibration and retained grounding. Model comparisons use controlled inputs; [[agent-evaluation-and-benchmarks]] covers behavioral evaluation.

### Decision and quality notes

Vendor summary with no independent reproduction. Confidence scores support review routing only after calibration; ingestion does not select a model or confirm live availability. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which labeled extraction fields and failure costs should set review thresholds, and how will grounding and confidence calibration be rechecked after deployment changes? See [[indexes/gaps]].


## 2026-09-15: Claude tools and Azure hosting qualifications

### Typed entities

project: Microsoft Foundry; project: Claude; concept: schema-constrained output; concept: MCP connector; concept: tool search.

### Claims and evidence

- Microsoft's August 17 account lists schema-constrained outputs, web search, web fetch, an MCP connector, and tool search for Azure-hosted Claude deployments. It distinguishes response schemas from tool-argument validation and describes domain restrictions and bounded tool use. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-microsoft-foundry-from-single-call-to-agents-five-new-claude-capabilit.md)
- The account says Azure-hosted prompts and completions remain within Azure while usage metadata and safety-flagged content can go to Anthropic. The stated exception prevents interpreting the hosting claim as an unconditional data-residency guarantee. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-microsoft-foundry-from-single-call-to-agents-five-new-claude-capabilit.md)

### Explicit relationships

Managed research uses search, fetch, and tool selection; deployment fit depends-on supported model/tool combinations and qualified data flows. See [[claude-platform-2026]] and [[mcp-tool-governance-and-app-surfaces]].

### Decision and quality notes

Vendor release snapshot, not a current service or residency certification. Schema validity does not establish business correctness. Verify exact deployment and data-flow terms before implementation. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which Foundry Claude model/tool combinations and outbound metadata or safety-content flows are acceptable for the intended HoneyDrunk workload? See [[indexes/gaps]].

## 2026-09-15: Foundry development environment packaging

### Typed entities

project: Foundry Dev Pack; project: Azure CLI; project: Azure Developer CLI; concept: conditional editor integration.

### Claims and evidence

- Microsoft describes Dev Pack as bundling Azure CLI, azd, the Foundry azd extension, and agent guidance. VS Code toolkit installation is conditional on VS Code; hosted-agent editor integration depends on GitHub Copilot App being present. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-foundry-dev-pack.md)
- The source identifies Microsoft.FoundryDevPack as the Windows winget package and azd ai agent init as a template entry point. Toolchain installation does not complete application Azure configuration or establish production readiness. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-foundry-dev-pack.md)

### Explicit relationships

Foundry setup uses a bundled toolchain; optional integrations depend-on installed editor surfaces. Reproducibility depends-on the selected components and resulting versions.

### Decision and quality notes

Vendor onboarding announcement. Commands are recorded as source facts only; no installation was run. Current package and component behavior needs environment validation. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which Dev Pack components, installed versions, conditional editor integrations, and Azure configuration steps belong in a reproducible HoneyDrunk development setup? See [[indexes/gaps]].


## 2026-09-15: Versioned toolboxes and caller identity

### Typed entities

project: Microsoft Foundry Toolboxes; concept: OAuth2 user delegation; concept: versioned tool access; project: Work IQ; concept: managed identity.

### Claims and evidence

- Microsoft's example defines authentication in connections, combines tools in a versioned toolbox, and exposes it through an MCP endpoint. It describes per-user token isolation, refresh, and consent for OAuth2 delegation to private MCP services and Work IQ. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-foundry-toolboxes-user-delegation.md)
- End-user OAuth, agent identity, project managed identity, stored keys, and anonymous access serve different needs. The example includes boundary screening and optional API Management controls; Work IQ is a preview example and screening is not proof of injection immunity. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-foundry-toolboxes-user-delegation.md)

### Explicit relationships

Toolboxes use centralized authentication configuration and versioned tool surfaces. Correct delegation depends-on explicit caller identity and consent; see [[ai-agent-identity-and-workload-auth]].

### Decision and quality notes

Vendor implementation guidance, consistent with earlier Toolbox coverage. Verify actual scopes, isolation, refresh behavior, and APIs before implementation. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which tool requires end-user, agent, or project identity, and how will Foundry toolbox consent, refresh, caller isolation, and version compatibility be verified? See [[indexes/gaps]].

## 2026-09-18: Content Understanding GA and preview contracts

### Typed entities

project: Azure Content Understanding; concept: CU 1.0; concept: CU 2.0 preview; concept: semantic document chunking; concept: review routing.

### Claims and evidence

- Microsoft distinguishes refreshed CU 1.0 GA API 2025-11-01 from CU 2.0 public preview API 2026-06-01-preview. The GA changes expand model choices and revise grounding/confidence; reported accuracy and token savings are internal evaluation results. confidence: 1 source, last-confirmed 2026-09-18 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-16-rss-azure-content-understanding-ga-preview.md)
- The August announcement places synchronous Read/Layout, contextualization from labeled examples, semantic chunking, finer classification, and agentic document reasoning in the preview. It says contextualization training inputs remain in customer-controlled Azure Storage. confidence: 1 source, last-confirmed 2026-09-18 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-16-rss-azure-content-understanding-ga-preview.md)

### Explicit relationships

Extraction design depends-on the selected API contract; uncertain classification uses confidence as an input to further checks. This extends the field-confidence calibration section without treating preview features as GA.

### Decision and quality notes

Vendor announcement snapshot. Evaluate quality and review thresholds on representative documents; storage placement alone is not a complete data-flow or privacy guarantee. Source-specific claims remain provisional single-source evidence; related sources and derived summaries are not independent confirmation of these details. Open question: Which required Lore extraction features belong to CU GA versus preview, and what versioned corpus tests establish chunk quality, provenance, storage flows, cost, and review thresholds? See [[indexes/gaps]].


## 2026-09-19: Validated plans and durable workflow execution

### Typed entities

project: Azure Functions hosted skills; project: Durable Functions; concept: structured plan; concept: durable timer; concept: idempotent handler.

### Claims and evidence

- Microsoft’s article describes hosted skills, formerly Serverless Agents, producing structured plans from explicitly allowed tools and subagents. Runtime validation precedes Durable Functions orchestration; dependency scheduling, persisted intermediate outputs, and durable timers support execution across request completion and worker restarts. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-web-azure-functions-dynamic-workflows.md)
- The captured handler contract requires synchronous functions with one dictionary argument, JSON-serializable results, and idempotency because execution can repeat after failures. Queue-triggered work must explicitly deliver results, and management tools cover start, status, list, cancel, and terminate. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-web-azure-functions-dynamic-workflows.md)

### Explicit relationships

Agent planning uses allowed workflow tools; reliable side effects depend-on idempotent handlers and durable execution. See [[distributed-systems-patterns]] and [[agent-context-management-and-session-continuity]].

### Decision and quality notes

Vendor implementation snapshot. The reported 56%/93% sample token reductions are not promoted as HoneyDrunk savings; workload and planning overhead matter. Durability does not imply exactly-once external side effects or automatic result delivery. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which hosted-skill version and restart, repeated-handler, cancellation, tool-allowlist, storage, and queue-result tests would qualify dynamic workflows for a Lore job? See [[indexes/gaps]].


## 2026-09-19: Flex certificates protect distinct transport and identity boundaries

### Typed entities

project: Azure Functions Flex Consumption; project: Azure Key Vault; concept: site-scoped certificate; concept: internal-hop TLS; concept: mTLS authorization.

### Claims and evidence

- Microsoft announces site-scoped certificates and end-to-end TLS for Flex Consumption, separating custom-domain HTTPS, front-end-to-worker encryption, outbound certificates, and inbound client authentication. The captured limits are three private and three public certificates per app, with Key Vault/managed-identity imports and renewed-version synchronization within 24 hours. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-web-azure-functions-flex-certificates-tls.md)
- Code access is granted per certificate rather than through WEBSITE_LOAD_CERTIFICATES; Linux files and thumbprint rotation need explicit handling. For inbound mTLS, X-ARR-ClientCert conveys the certificate but application code still validates trust, validity, usage, revocation policy, and authorization. Header presence alone is insufficient. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-web-azure-functions-flex-certificates-tls.md)

### Explicit relationships

Certificate lifecycle uses scoped access and rotation; mTLS authorization depends-on application validation. Transport encryption and caller permission protect different boundaries.

### Decision and quality notes

Vendor September announcement, not a live configuration audit. The source also flags renegotiation constraints with TLS 1.3, HTTP/2, and large requests, and absence of dedicated Azure CLI certificate commands at publication. Verify deployment-specific behavior before implementation. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which Flex TLS boundaries, certificate access/rotation paths, forwarded-certificate trust checks, and protocol/request-size cases need tests before migrating a HoneyDrunk API? See [[indexes/gaps]].


## 2026-09-19: Connector triggers require receiving-app authentication

### Typed entities

project: Azure Managed Connectors; project: Azure App Service; project: Microsoft Entra; concept: authenticated callback; concept: Connector Namespace identity.

### Claims and evidence

- Microsoft adds App Service as a first-class trigger destination within Managed Connectors public preview. The captured configuration supplies a receiving route, Connector Namespace managed identity, and expected Entra audience; new triggers default to POST /api/webhook. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-azure-app-service-connector-triggers.md)
- The wizard configures the connector side, while receiving-app authentication is separate. The sample configures the Entra application, audience, federated credential, allowed managed-identity principal, and required App Service authentication before event handling; configuration can affect the whole app. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-azure-app-service-connector-triggers.md)

### Explicit relationships

Connector callbacks depend-on receiving-app identity validation and route configuration; connector setup alone does not establish endpoint authentication.

### Decision and quality notes

Vendor preview example using one email-triage push workflow. It does not establish support for every connector/operation. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which connector operations support HoneyDrunk callbacks, and do route, audience, principal, token-rejection, and whole-app authentication tests protect the receiving application? See [[indexes/gaps]].


## 2026-09-19: Guided deployment separates planning and execution checkpoints

### Typed entities

project: GitHub Copilot; project: VS Code; project: Azure Developer CLI; concept: architecture approval; concept: deployment cost estimate.

### Claims and evidence

- Microsoft’s preview separates requirements and architecture planning, local development, and Azure deployment. It collects missing inputs, requests plan approval before scaffolding, checks local tools, configures debugging, and presents intended resources, deployment tooling, and estimated cost. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-azure-guided-copilot-checkpoints.md)
- The article describes retained architecture context and infrastructure files for repeatable environments. Initial JavaScript/TypeScript support includes Functions, Container Apps, and Static Web Apps; .NET and Python remain roadmap items in this capture. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-azure-guided-copilot-checkpoints.md)

### Explicit relationships

Guided deployment uses explicit planning and deployment checkpoints; reproducible environments depend-on infrastructure artifacts and prerequisites.

### Decision and quality notes

Vendor preview goals are not independent proof of deterministic output or first-attempt deployment success. This adds a workflow pattern without asserting .NET availability. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which requirement, architecture, prerequisite, infrastructure, and cost checkpoints should a HoneyDrunk deployment agent expose, and does the selected preview support the project language? See [[indexes/gaps]].


## 2026-09-19: SRE Agent GA network scope and subnet requirements

### Typed entities

project: Azure SRE Agent; project: Azure VNet; concept: dedicated delegated subnet; concept: outbound routing; concept: egress-policy audit.

### Claims and evidence

- Microsoft’s August 25 GA announcement distinguishes destination routing, resource identity/permissions, and tool policy/approvals. Integration covers selected outbound traffic only; not every agent flow traverses the VNet. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-azure-sre-agent-vnet-boundaries.md)
- The announcement requires an empty dedicated subnet of /27 or larger, in the agent’s region and delegated to Microsoft.App/environments. It calls for repository-connectivity and private-path tests. The workspace egress-policy audit is not a complete network record and requires infrastructure-log supplementation. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-azure-sre-agent-vnet-boundaries.md)

### Explicit relationships

Private connectivity depends-on routing, DNS, and subnet setup; authorized operations depend-on identity and tool policy. The newer GA requirements supersede the older subnet-size claim below its historical entry.

### Decision and quality notes

Official GA announcement is newer than the June Learn capture, which had an access warning and unknown publication date. Prefer the newer /27 requirement for research planning, with live deployment validation still required. Existing managed-path exceptions remain relevant; VNet integration does not establish total traffic containment. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which SRE Agent traffic uses private versus managed paths, and do the target deployment’s subnet sizing, DNS, repository connectivity, identity controls, and infrastructure logs establish the intended boundary? See [[indexes/gaps]].


## 2026-09-22: Browser credential isolation depends on the complete secret path

### Typed entities

project: Azure Key Vault; project: Browser Automation Tool; project: Foundry Hosted Agents; project: Playwright Workspaces; concept: secret serialization; concept: browser session disposal.

### Claims and evidence

- Microsoft describes narrowly scoped secret retrieval immediately before browser authentication, keeping credentials in application/tool code and returning operation results to the model. The session is isolated and disposed after the authorized task. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-azure-browser-agent-secret-flow.md)
- The article explicitly makes model exposure implementation-dependent: Key Vault alone does not prevent prompt, log, or tool-trace leakage. Identity-based access is preferred where supported; MFA, conditional access, and SSO still require identity design. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-azure-browser-agent-secret-flow.md)

### Explicit relationships

Browser authentication uses a controlled credential path; model isolation depends-on tool result serialization, logs, target restrictions, and session cleanup. See [[ai-coding-agent-security]].

### Decision and quality notes

Vendor implementation guidance, not a demonstrated guarantee for HoneyDrunk. Inspect end-to-end data flow, narrow permissions, rotation, auditing, and sensitive-action approvals. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent support. Open question: Can browser-agent credentials reach prompts, tool results, traces, logs, or retained sessions, and which target restrictions and cleanup tests demonstrate the intended isolation? See [[indexes/gaps]].


## 2026-09-22: Dashboard context guides telemetry-backed diagnosis

### Typed entities

project: Azure SRE Agent; project: Azure Managed Grafana; concept: dashboard context; concept: telemetry units; concept: time filtering.

### Claims and evidence

- The Microsoft worked example uses Grafana MCP dashboard queries, scope, variables, descriptions, and known telemetry pitfalls to guide SRE Agent investigation. Aggregated tool activity and arguments distinguish an active session from a repeated sleep/retry loop that looks similar in duration charts. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-azure-grafana-dashboard-agent-context.md)
- The example still requires explicit time filters and replacement of Grafana macros; descriptions address time-unit differences, timeout success signals, and parent-span double-counting. The native connector uses managed identity. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-azure-grafana-dashboard-agent-context.md)

### Explicit relationships

Agent investigation uses dashboard context; diagnosis depends-on actual scoped telemetry and interpretation rules. See [[opentelemetry-genai-observability-and-ecosystem]].

### Decision and quality notes

A vendor worked example, not general diagnosis accuracy. Preserve units, scope, freshness, and known pitfalls with queries; confirm proposed explanations against telemetry. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent support. Open question: Which agent-readable dashboards document time units, macros, scope, freshness, timeout semantics, and span aggregation well enough to support reproducible investigations? See [[indexes/gaps]].
