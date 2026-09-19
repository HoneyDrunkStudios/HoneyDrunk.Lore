# AI Agent Identity and Workload Auth

## Decision-useful summary
Agent identity is now a first-order security design choice. An agent can act as the user, act through a service account/API token, or act as its own workload identity. The first is easiest and fits local interactive work, the second is common but creates non-human identity sprawl, and the third gives better attribution and runtime proof but requires stronger identity infrastructure. Brokered short-lived tokens and governance control planes can improve any of the three, but they do not erase the underlying model. [source: raw/2026-07-08-rss-tldr-infosec-three-ways-to-give-an-ai-agent-an-identity-17-minute-read.md]

## Source-backed claims
- Acting as the user is useful for short, interactive, local-dev-style tasks because there is little to provision, but it fails for long-running work, team ownership, and detection because downstream logs often cannot distinguish the human from the agent. confidence: 1 source, last-confirmed 2026-07-08. [source: raw/2026-07-08-rss-tldr-infosec-three-ways-to-give-an-ai-agent-an-identity-17-minute-read.md]
- Giving an agent its own service account or API token supports production and team workflows, but the source argues it is often risky because static API keys are long-lived, hard to inventory, over-privileged, and commonly shared through environment variables or password vaults. confidence: 1 source, last-confirmed 2026-07-08. [source: raw/2026-07-08-rss-tldr-infosec-three-ways-to-give-an-ai-agent-an-identity-17-minute-read.md]
- Giving the agent its own workload identity through SPIFFE/SPIRE-style attestation can provide unique agent identity, short-lived credentials, and better multiplayer/lifecycle ownership, but it has high setup cost and still depends on downstream SaaS authorization granularity. confidence: 1 source, last-confirmed 2026-07-08. [source: raw/2026-07-08-rss-tldr-infosec-three-ways-to-give-an-ai-agent-an-identity-17-minute-read.md]
- Identity brokers such as Okta Cross App Access/ID-JAG can sit above user or service-account models to issue short-lived, scoped tokens for each interaction with central visibility. confidence: 1 source, last-confirmed 2026-07-08. [source: raw/2026-07-08-rss-tldr-infosec-three-ways-to-give-an-ai-agent-an-identity-17-minute-read.md]
- Uber's described SPIFFE-based pattern adds a token service that carries actor-chain provenance across agent hops, because workload identity alone identifies what workload is acting but not always which user or upstream actor caused the action. confidence: 1 source, last-confirmed 2026-07-08. [source: raw/2026-07-08-rss-tldr-infosec-three-ways-to-give-an-ai-agent-an-identity-17-minute-read.md]
- Governance products such as Entra Agent ID and Okta for AI Agents are control planes around existing identities: they discover agents, assign ownership, vault/rotate credentials, enforce policy, provide kill switches, and preserve audit trails. confidence: 1 source, last-confirmed 2026-07-08. [source: raw/2026-07-08-rss-tldr-infosec-three-ways-to-give-an-ai-agent-an-identity-17-minute-read.md]
- AWS Bedrock AgentCore Identity and Google Agent Identity are described as cloud-provider moves toward managed workload identity for agents, bundling identity, brokering, registry/gateway, and governance closer to the infrastructure where agents run. confidence: 1 practitioner source, last-confirmed 2026-07-08. [source: raw/2026-07-08-rss-tldr-infosec-three-ways-to-give-an-ai-agent-an-identity-17-minute-read.md]

## Typed entities
- concept: agent identity
- identity model: acting as user
- identity model: service account / API token
- identity model: workload identity
- identity standard: SPIFFE
- implementation: SPIRE
- artifact: SVID
- protocol/extension: ID-JAG / Identity Assertion Authorization Grant
- product/control: Okta Cross App Access
- product/control: Entra Agent ID
- product/control: Okta for AI Agents
- product/control: AWS Bedrock AgentCore Identity
- product/control: Google Agent Identity
- pattern: actor chain
- pattern: credential broker
- organization: Uber
- organization: Canva

## Explicit relationships
- Acting-as-user depends-on the user's session, permissions, and lifecycle; it is fragile for unattended or team-owned automation.
- Service-account identity complements production automation but can cause non-human identity sprawl when ownership, expiry, rotation, and least privilege are weak.
- Workload identity uses attestation and short-lived credentials to supersede static API tokens where infrastructure support exists.
- Token brokers complement identity models by issuing scoped credentials at request time.
- Actor-chain provenance complements workload identity because it links an agent action back to the originating human or upstream agent.
- Governance control planes complement identity brokering by managing lifecycle, ownership, discovery, policy, kill switches, and audit evidence.

## HoneyDrunk implications
- For each HoneyDrunk agent workflow, record the identity model before implementation: user-delegated, service-account, or workload identity.
- Default local interactive assistants to acting-as-user with tight approval and audit, but do not let those sessions become team-owned scheduled automations.
- Treat static API keys and shared service-account passwords as temporary exceptions that need owner, scope, expiry, rotation, and storage review.
- Prefer WIF/OBO/brokered short-lived credentials for shared automation and cloud-facing tools.
- If multi-agent or long-running production workflows grow, evaluate whether existing Entra/Okta/cloud-provider controls can provide governance before building SPIFFE/SPIRE from scratch.

## Confidence and quality notes
- Quality posture: decision-usable for identity-model vocabulary and tradeoffs. This is practitioner analysis, not a primary standard. Verify current vendor feature names, API behavior, pricing, and availability before implementation.
- Privacy filter: public product names and architecture patterns retained; no private credentials, customer identities, or implementation secrets copied.

## 2026-08-22 compile additions: Agent Access Model

### Source-backed claims
- Cloudflare's Agent Access Model treats a task-scoped agent run as the authorization unit and says credentials should expire with the task, be sender-constrained, and retain attribution to the initiating principal and current actor. Source: `raw/2026-08-22-rss-tldr-infosec-the-agent-access-model-26-minute-read.md`; page: [[ai-coding-agent-security]]. confidence: 1 Cloudflare security architecture source, last-confirmed 2026-08-22.
- The model expects an Agent Identity Broker to issue a verifiable task credential and a Task-Scoped Access Engine to decide each request against the task grant, resource, operation, and accumulated state. Source: `raw/2026-08-22-rss-tldr-infosec-the-agent-access-model-26-minute-read.md`. confidence: 1 source, last-confirmed 2026-08-22.
- Cloudflare maps existing standards to part of the design: OAuth 2.0 Token Exchange can narrow delegated credentials and preserve actor chains, while DPoP can bind a token to a harness-held proof key; neither standard alone defines the task template, Trust Ratchet, or cross-layer enforcement. Source: `raw/2026-08-22-rss-tldr-infosec-the-agent-access-model-26-minute-read.md`. confidence: 1 source, last-confirmed 2026-08-22.

### Typed entities
- model/control: Agent Access Model / AAM
- component: Agent Identity Broker
- component: Task-Scoped Access Engine
- control: sender-constrained token
- claim: actor chain
- standard: OAuth 2.0 Token Exchange / RFC 8693
- standard: DPoP / RFC 9449
- draft: AAuth

### Explicit relationships
- Task-scoped credentials supersede standing service-account credentials for short-lived agent work where infrastructure can issue them.
- Sender-constrained credentials depend-on the harness holding proof material outside model context.
- Actor-chain attribution complements workload identity by preserving who initiated or delegated the work.

### HoneyDrunk implications
- For any HoneyDrunk agent that can reach production data, define the task template, initiating principal, credential lifetime, allowed resources, and actor-chain logging before enabling unattended execution.

### Quality notes
- Cloudflare is a vendor/security-architecture source. Use as design vocabulary and verify standards support against actual identity providers before implementation.

## 2026-08-24 compile additions: signed agent actions and MCP identity direction

### Source-backed claims
- Google's zero-trust ADK source says every state-changing agent write should be signed by the specific agent making the request and verified before commit, so database rows carry immutable evidence tying the payload to the agent identity. Source: `raw/2026-08-24-rss-google-developers-blog-build-zero-trust-ai-agents-with-google-s-agent-.md`; page: [[ai-coding-agent-security]]. confidence: 1 Google Developers source, last-confirmed 2026-08-24.
- The MCP roadmap prioritizes standardized agent identity and delegation using DPoP, Workload Identity Federation, ID-JAG, Enterprise-Managed Authorization, token exchange, and OAuth standards engagement for agents acting as cloud workloads or delegated subagents. Source: `raw/2026-08-24-web-mcp-blog-the-new-mcp-roadmap.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 official MCP blog source, last-confirmed 2026-08-24.

### Typed entities
- control: signed state-changing write
- service: Cloud KMS / HSM-backed signing
- control: database ingress guard
- protocol/control: DPoP
- protocol/control: Workload Identity Federation
- grant: ID-JAG
- control: Enterprise-Managed Authorization

### Explicit relationships
- Signed state-changing writes complement workload identity by making persisted state independently auditable after the agent action.
- MCP agent identity work depends-on existing identity standards and token exchange rather than static API keys.

### HoneyDrunk implications
- For HoneyDrunk agents that mutate ledgers, orders, account records, or other systems of record, design write signatures and verification before relying on audit logs alone.
- Track MCP agent identity support as a prerequisite for production remote MCP services that need unattended or subagent access.

### Quality notes
- Google source includes demo patterns and cloud-specific implementation details; validate against HoneyDrunk identity providers and data stores before adoption.

## 2026-09-10 managed connections and secretless handles

### Sources
- [LangChain: Connections, managed credentials, and per-caller identity for Managed Deep Agents](../raw/2026-09-10-rss-tldr-ai-connections-managed-credentials-and-per-caller-identity-for-ma.md)
- [Microsoft Command Line: Stop restricting the agent, start restricting its world](../raw/2026-09-10-web-microsoft-command-line-stop-restricting-the-agent-start-restricting-it.md)

### Typed entities
- `product`: LangChain Managed Deep Agents
- `feature`: LangSmith Connections
- `identity pattern`: agent-owned credential
- `identity pattern`: user-owned OAuth grant
- `control`: opaque credential handle
- `runtime boundary`: Azure Container Apps Sandbox microVM

### Claims
- Managed Deep Agents v0.7.0+ can use LangSmith Connections so credentials live in the workspace credential store rather than in project `.env` files or deployment images. confidence: 1 source, last-confirmed 2026-09-10
- LangChain separates credential owner from credential type: connections can be agent-owned or user-owned, and can use static secrets or OAuth grants. confidence: 1 source, last-confirmed 2026-09-10
- User-owned OAuth can resolve per caller and pause a run before the first model turn when a required grant is missing. confidence: 1 source, last-confirmed 2026-09-10
- Microsoft's Azure SRE Agent pattern keeps model-authored code inside per-agent sandbox microVMs and exposes secrets through call-bound, destination-locked, scope-limited, single-use handles exchanged by a proxy outside the VM. confidence: 1 source, last-confirmed 2026-09-10

### Explicit relationships
- LangSmith Connections uses workspace-managed credentials to reduce credential sprawl in project files and images.
- User-owned OAuth depends-on caller identity and consent, while agent-owned credentials depend-on shared service authority and tighter audit controls.
- Opaque credential handles complement sandboxing by keeping raw secrets outside the model-authored execution environment.
- Role and caller identity shape tool, MCP, memory, credential, and approval boundaries in production agent systems.

### HoneyDrunk implications
- For hosted agents, require a credential inventory that names owner, credential type, target service, scopes, approval path, and audit attribution.
- Prefer secretless handles and proxy-mediated exchanges for remediation agents instead of handing raw secrets into the sandbox or model context.
- Validate connection grants before the first model turn so missing auth does not turn into partial, ambiguous tool behavior.

### Quality notes
- Vendor sources describe product and architecture patterns; implementation must be verified against HoneyDrunk identity providers, audit retention, and least-privilege policy.

## 2026-09-15: Contextual authorization beyond static roles

### Typed entities

project: n8n; concept: contextual authorization; concept: agent identity; concept: retrieval permission context.

### Claims and evidence

- n8n proposes supplementing broad static roles with identity, declared purpose, explicit tool/data scope, and policy checks outside the model at access boundaries. Retrieved material retains its source permission context in this proposal. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-n8n-blog-rbac-for-ai-agents-why-static-roles-fail-in-agentic-systems.md)
- The article recommends versioned and tested policies, separately scoped child workflows, and audit feedback. Its criticism of static roles is vendor guidance, not proof that every RBAC deployment fails. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-n8n-blog-rbac-for-ai-agents-why-static-roles-fail-in-agentic-systems.md)

### Explicit relationships

Agent authorization depends-on independently enforced policy; scoped child workflows use distinct permissions. Contextual checks extend RBAC rather than establishing a replacement requirement.

### Decision and quality notes

Architecture guidance only. No legal-compliance assertions or incident anecdotes promoted. This is consistent with existing delegated-identity and secretless-handle patterns. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Where should tool/data gateways enforce purpose and source permissions, and which policy tests cover child workflows and injected attempts to widen access? See [[indexes/gaps]].


## 2026-09-19: Worker-scoped deployment authority

### Typed entities

project: Cloudflare Workers; project: Durable Objects; concept: resource-scoped token; concept: Editor role; concept: zone permission.

### Claims and evidence

- Cloudflare’s announcement describes four Worker-level roles for users and API tokens, separating operational metadata, read-only content, content/settings changes, and full administration. Editor can deploy but cannot create or delete resources; Admin includes destructive and access-management operations. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-rss-cloudflare-worker-scoped-agent-permissions.md)
- A token can be scoped to one Worker. Route or custom-domain changes additionally need the zone’s Workers Routes permission; unchanged connections can continue deploying without it. Durable Objects inherit their implementing Worker’s permissions, and Data Studio requires Editor because it can write data. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-rss-cloudflare-worker-scoped-agent-permissions.md)

### Explicit relationships

Agent deployment uses resource-scoped permissions; routing changes depend-on zone authority. Durable Object authorization depends-on its implementing Worker.

### Decision and quality notes

Vendor announcement captured September 18. Legacy assignments remain valid according to the source; granular authorization for other products is future work. This does not supersede the need for contextual checks discussed above. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which Worker, route, Durable Object, and Data Studio operations does each HoneyDrunk agent need, and do negative permission tests prevent unrelated deployments or deletion? See [[indexes/gaps]].
