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
