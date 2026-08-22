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
