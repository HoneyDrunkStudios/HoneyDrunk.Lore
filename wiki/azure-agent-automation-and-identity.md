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
