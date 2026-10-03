---
source: "https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis"
title: "Solving the Identity Crisis for AI Agents"
author: "Matt Mathew; Prasad Borole; Meng Huang; Sergey Burykin; Gaurav Goel; Bayard Walsh"
date_published: "2026-10-02"
date_clipped: "2026-10-02"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-10-02"
---

# Solving the Identity Crisis for AI Agents

# Solving the Identity Crisis for AI Agents

Principal Engineer

Staff Software Engineer

Engineering Manager

# Introduction

Uber is at the forefront of leveraging AI, empowering engineers to build AI solutions to improve productivity. In early 2025, the company built an internal Agent platform that allows teams to compose, deploy, and operate production-grade agents at scale. Additionally, Uber’s microservices tech stack comprising thousands of services was made AI-ready by enabling MCP® (Model Context Protocol) support over existing service APIs.

Increasing agentic autonomy necessitates strict oversight of the agents and the actions they execute. Accountability, the ability to answer “who did what, when and why” is critical for auditing, compliance, and executive trust. Without clear attribution, security controls can be harder to enforce, incident response may slow, and trust may be impacted.

This blog outlines the major updates to Uber’s identity and access technology stack in 2025 to accommodate AI agents. To maintain a proactive stance as AI adoption accelerates, we also offer a glimpse into our strategic roadmap for 2026 within this technical area.

The systems and approaches described reflect Uber’s internal architecture and controlled production environments. Design choices, performance characteristics, and security controls may vary across organizations, use cases, and deployment contexts.

### Motivation

Imagine an on-call engineer using an Oncall Agent to manage and resolve a system alert. In this scenario, the Investigation Agent determined the system was functioning correctly and the alert itself was misconfigured. The Investigation Agent then seamlessly passed the task to the Monitoring Agent to adjust the alert's threshold through a PR (pull request). The pull request shows a Monitoring Agent introducing the change, but the identity of the on-call engineer responsible remains untraceable.

As agentic workflows expand to encompass more agents, tools, and systems, this challenge becomes increasingly pronounced. We distilled this into the following two core problems.

#### Problem 1: Current Identity Model Doesn’t Describe Agency

Today’s identity models are built around humans and workloads (often called non-human identity, or NHI, supported through credentials such as service account or API keys). An agent is best defined as an entity that is authorized to act for or in the place of another. AI agents often run as workloads performing tasks on behalf of a human. In the above example, the Oncall Agent started a session on behalf of the on-call engineer to investigate and fix a specific issue.

#### Problem 2: Original Provenance Isn’t Effectively Carried Forward Across Agents to Systems

Execution context (originating user, intermediate agents) is dropped across agent hops. This leads to incomplete audits across the system and limits our ability to consistently leverage the fine-grained access policies already configured by downstream systems. In the absence of complete audit trails, incident response would require stitching partial audit logs across systems together. The PR opened by the Monitoring Agent should indicate that the on-call engineer requested solving a specific issue and some context around prior agent decisions that led to the PR.

It’s clear that agentic workflows behave differently than traditional automation:

- Delegation is the default mode - agents work on behalf of others
- Workflows are compositional - agents call other agents, tools, and systems
- Behavior is dynamic - plans evolve based on intermediate results as a session progresses

This defined the direction for what we had to build: foundations for agent identity and its propagation across agents that address the above problems.

### Architecture

As AI workflows scale, the interactions between autonomous agents and internal systems become deeply complex. To secure this ecosystem without stifling developer velocity, we decided to extend our existing Zero Trust Architecture for AI agents. Our architecture focuses on establishing verifiable cryptographic identity within the agent ecosystem and enforcing authorization for accessing downstream systems.

#### Agent Registry

At Uber, AI agents are often deployed as workloads, often managed by Kubernetes®. The [Michelangelo](https://www.uber.com/us/en/blog/from-predictive-to-generative-ai/) platform associates an AI agent to a workload. The Agent Registry serves as the source of truth, storing this registration. This is later used by the Security Token Service to verify the agent.

#### AI Agent Mesh

Analogous to the popular term [service mesh](https://en.wikipedia.org/wiki/Service_mesh), the AI Agent Mesh is the data plane where AI agents communicate with each other to complete tasks assigned to them. Within the Agent Mesh and for outbound calls (such as to MCP tools), AI agents rely on JWT tokens minted by the Security Token Service for authentication.

#### STS (Security Token Service)

Token minting for AI agents is handled by STS. Rather than relying on broad, long-lived service credentials, the STS acts as a dynamic trust broker that issues short-lived, scoped tokens for every hop.

#### MCP Gateway

MCP Gateway is a central system that mediates calls from the AI Agent Mesh to Uber’s systems. This design enables MCP Gateway to be a policy enforcement point for MCP tool invocations.

#### Downstream Systems

Once the MCP Gateway successfully authenticates the caller and authorizes the tool call, it securely proxies the request to the respective downstream services. These are primarily microservice APIs and datastores that execute the actual mutation or data retrieval.

#### AI Gateway

Beyond these components, an AI Gateway mediates all calls outbound from AI agents to AI models. This serves as the central point of integration for Uber with external APIs such as OpenAI®, Anthropic®, and others. The AI Gateway is integrated with security guardrails to detect and handle prompt injection, jailbreaks, content safety, PII redaction, and more. Learn more about Uber’s AI Guard from our recent conference presentation [here](https://cfe5ada20.lwcdn.com/hls/4e490060-3632-4408-9e39-c9565b1768d7/playlist.m3u8).

To empower engineers and operational teams to build agentic solutions, the Michelangelo AI platform provides two options:

**Code:**Write agents in Python using Uber’s internal production SDK. The SDK is orchestration-framework agnostic and supports common agent programming patterns (planning loops, tool use, state and memory), while providing standardized scaffolding, middleware hooks, observability, and evaluation tooling for production deployments.**No-code:**Author agents through the UI without writing any code. This lowers the barrier to entry and opens up the ability to build agents to the entire company beyond engineers.

Regardless of the options, the resulting AI agent gets deployed within Uber’s Kubernetes infrastructure.

Initially we considered building/adopting [agentgateway](https://github.com/agentgateway/agentgateway) that can proxy calls between AI agents. As Uber’s agentic AI ecosystem standardized heavily around the SDK, we instead integrated the solution directly into the SDK. We also found that fully addressing Problem 2 required support in the agent application layer, where execution context is created and propagated end-to-end, rather than relying only on an external proxy.

### Providing Agent Identities

Similar to microservices, AI agents run within workloads. The fundamental challenge to address was how to assign each individual agent a verifiable identity. Figure 3 shows our agent identity model and the process to mint a JWT token for the agent:

- Every workload first fetches its own cryptographically signed workload SVID (SPIFFE Verifiable ID) from
[SPIRE](https://www.uber.com/blog/our-journey-adopting-spiffe-spire). This proves the legitimacy of the underlying compute environment but doesn’t yet identify the agent. - The SDK uses its metadata available locally (like agent config), JWT from inbound calls and outbound destination audience to request a new JWT token from STS authenticated with the workload SVID. Only the STS is permitted to mint tokens for AI agents. By centralizing this process, we ensure that the actor chain carries the cryptographic record of every entity involved in the request.
- STS integrates with the Agent Registry to verify that the requesting
*agent_id*is explicitly authorized to run on that specific workload (from step 1). This prevents a workload from attempting to impersonate an agent that it isn’t authorized to host. - STS mints a JWT token and returns it to the requesting agent. This JWT is used for requests for the next hop of the agentic flow.

Here are some key features of this design:

**Single-hop, short-lived tokens.**Every JWT minted by the STS is intended for a single hop, with a specific Audience claim and a short time-to-live in the order of minutes. A token issued for Agent A to call Agent B can’t be intercepted and replayed to call a database or another service; it’s valid only for that specific destination.**Full contextual attribution.**STS manages the token exchange at every step and embeds the fully attested actor chain into the token. This allows the MCP Gateway or downstream system to have the full context of the request; we see every participant in the lineage (e.g. engineer to Oncall Agent to Investigation Agent …) rather than just the immediate caller. This visibility allows for comprehensive audit logs and advanced workflow authorization that accounts for the full request lineage.**Extensible context.**JWT structure is designed to be extensible; we can seamlessly add additional claims in the future, such as session identifiers and request intent related claims, to provide richer context for policy decisions. This high-fidelity visibility ensures that a tool's execution can be authorized not just by the last hop, but by the verified intent of the entire chain.

By anchoring every agent identity in a SPIRE-backed workload credential and centralizing token exchange, we’re able to provide short-lived tokens while maintaining end-to-end traceability.

### Agent Identities in Action

To understand how agent identity manifests in a real-world workflow, let’s trace a typical request path. As agentic AI workflows involve calling multiple specialized agents to fulfill a complex user request, the identity must evolve at every boundary without losing its original context. Figure 4 shows a multi-hop investigation flow, from an initial user query to the final secure tool invocation:

- An on-call engineer (user1) initiates a session with the Oncall Agent. At this entry point, the request is anchored by the user’s own personnel identity.
- The Oncall Agent can’t reuse the user’s raw credentials to call downstream services. Instead, it contacts the Security Token Service. It presents its SPIRE-issued identity (Workload-1) and the user’s context to request a new JWT specifically scoped for the next-hop audience as Investigation Agent. STS responds with a JWT to the Oncall Agent. This per-hop mechanism for exchanging tokens is conceptually based on OAuth 2.0 Token Exchange (
[RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693)) but is customized to transmit agent identity and provenance in a streamlined way that integrates with Uber's internal auditing and performance requirements.

- The Oncall Agent sends the above JWT to the Investigation Agent (hosted within Workload-2).
- The Investigation Agent verifies the signature and the audience. To call MCP Gateway, Investigation Agent performs its own token exchange with STS audience as MCP Gateway. This step is the same as step 2 above. The newly minted JWT carries a verifiable history of everyone involved: [user1, oncall-agent, investigation-agent].
- The MCP Gateway receives and verifies the JWT. Once verified, the Gateway enforces tool-level policies, which involves tool access checks and redaction of sensitive data if needed (also powered by AI Guard that we mentioned in the Architecture section). Policies are defined based on internal risk classification, and mandated for systems that we consider high risk.

Having identity across the entire call chain of the request enables the system to enforce policies that are flexible enough to evaluate both the personnel identity (the human initiator) and the agent identity (the acting logic) simultaneously. As we evolve our IAM systems to support AI agents, we’re closely tracking emerging standards, particularly the IETF [WIMSE working group drafts](https://datatracker.ietf.org/wg/wimse/about/), along with relevant individual drafts such as “AI Agent Authentication and Authorization” ([draft-klrc-aiagent-auth-01](https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/)), to stay aligned with the broader direction of the industry.

### Establishing a Paved Path

Several agents were built before the architecture was implemented. This posed a challenge: ensuring every agent consistently performs STS token exchanges and preserves the actor chain. To eliminate these gaps, we shifted from manual compliance to an automated, secure-by-default developer experience.

We developed a Standardized A2A (Agent-to-Agent) Client on top of the [A2A protocol](https://github.com/langchain-ai/agent-protocol). This client automates the STS JWT exchange and propagation of the actor chain, ensuring the secure path is also the easiest path for developers to implement A2A calls.

### Observability & Adoption

Our observability system provides a real-time, end-to-end view into agentic traffic, making complex multi-agent workflows transparent and auditable. By capturing each hop in the actor chain from the originating user through multiple agents and downstream tool invocations, it enables precise attribution of actions, along with associated authorization decisions and security context. This level of visibility is a top priority in a Zero Trust environment, where every interaction should be authenticated, authorized, and continuously monitored.

*below 40 milliseconds*. We intend to keep scaling this system as agentic AI adoption grows at Uber.

# Conclusion

As we think about the future of AI identity and access, we frame our direction in the 3 layers shown in Figure 10.

On top of that foundation sits Dynamic Access Control, followed by a Unified Policy Enforcement Plane that enables observability and expresses business-level controls consistently across tools, sessions, and protocols. In an agent-driven world, static human-managed permissions and fragmented enforcements don’t scale.

Our long-term vision is a cohesive architecture where identity, risk, and policy work together seamlessly - so humans and AI agents can collaborate at machine speed while maintaining strong trust and security controls.

## Acknowledgments

*Anthropic is a registered trademark of Anthropic, PBC.*

*Kubernetes®, Model Context Protocol (MCP) and its logo are registered trademarks of The Linux Foundation® in the United States and other countries. No endorsement by The Linux Foundation is implied by the use of these marks.*

*OpenAI® and its logos are registered trademarks of OpenAI®.*

Cover Photo Attribution: Image created by ChatGPT

Stay up to date with the latest from Uber Engineering - follow us on [LinkedIn](https://p.uber.com/eng-linkedin) for our newest blog posts and insights.

Matt Mathew

Principal Engineer

Matt is a Principal Engineer on the Engineering Security team at Uber. He currently works on various projects in the security domain. Previously, he led the initiative to containerize and automate Data infrastructure at Uber.

Prasad Borole

Staff Software Engineer

Prasad is a Staff Software Engineer on the AI Security team within Core Security Engineering at Uber. He leads initiatives in the areas of agent security and risk-adaptive access control.

Meng Huang

Engineering Manager

Meng leads teams within Engineering Security at Uber focused on identity, access control, and infrastructure for securing agentic systems at scale. Previously, he led several 0-to-1 platform initiatives across customer data, sign-up and login, and account management.

Sergey Burykin

Sr Software Engineer

Sergey is on the AI Security team within Core Security Engineering at Uber. He leads the design and development of Uber’s agent security platform, including Agent Identity framework, and MCP Gateway security, establishing secure identity propagation and standardized access for AI agents.

Gaurav Goel

Software Engineer II

Gaurav is a Software Engineer on the AI Security team within Core Security Engineering at Uber. He focuses on the design and development of the Agent Identity framework, ensuring secure and seamless integrations across the Uber ecosystem.

Bayard Walsh

Software Engineer I

Bayard is a Software Engineer on the AI Security team within Core Security Engineering at Uber. He designs and develops Uber’s agent security platform, including Agent Identity framework, MCP Gateway security, and secure third-party MCP access.
