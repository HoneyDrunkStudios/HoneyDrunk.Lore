# Multi-Agent Architectures

## Decision-useful summary
Multi-agent systems are warranted only when a single agent hits hard limits: context overflow, slow serial work, or incompatible tool/model/permission needs. The System Design Newsletter source frames six architecture families (orchestrator-worker, pipeline, hierarchical, swarm, mesh, handoffs) and emphasizes that extra agents add token cost, latency, coordination overhead, verification burden, and security risk. For HoneyDrunk, default to one well-instrumented agent unless the task needs parallelism, isolation, specialization, or a regulated/auditable workflow shape. [source: raw/2026-05-12-rss-system-design-newsletter-multi-agent-architectures-clearly-explained.md]

## Claims
- A single agent should remain the default when one context window, one tool/permission set, and one loop can handle the task; unnecessary splitting is a common failure mode. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-system-design-newsletter-multi-agent-architectures-clearly-explained.md]
- Multi-agent systems become justified when a task hits context overflow, benefits from parallel independent work, or requires role-specific tools/models/permissions that should not live in one agent. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-system-design-newsletter-multi-agent-architectures-clearly-explained.md]
- Orchestrator-worker architecture uses a central agent to decompose, assign, and synthesize worker outputs; it improves parallel research-style tasks but can bottleneck on the orchestrator and waste tokens if worker instructions overlap. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-system-design-newsletter-multi-agent-architectures-clearly-explained.md]
- Pipeline architecture uses fixed ordered agent stages and explicit output contracts; it trades latency for predictability, auditability, and easier failure localization. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-system-design-newsletter-multi-agent-architectures-clearly-explained.md]
- Hierarchical architecture uses manager/worker layers to limit per-agent context scope; it scales coverage but can lose important details through summarization at each level. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-system-design-newsletter-multi-agent-architectures-clearly-explained.md]
- Multi-agent coordination increases risk: bad instructions, misalignment, weak verification, prompt injection, context contamination, privilege creep, higher tokens, and higher latency. confidence: 1 source, last-confirmed 2026-05-12. [source: raw/2026-05-12-rss-system-design-newsletter-multi-agent-architectures-clearly-explained.md]

## Typed entities
- concept: multi-agent system
- architecture pattern: orchestrator-worker
- architecture pattern: pipeline
- architecture pattern: hierarchical agents
- architecture pattern: swarm
- architecture pattern: mesh
- architecture pattern: handoffs
- protocol/concept: Model Context Protocol (MCP)
- protocol/concept: Agent-to-Agent (A2A)
- concept: shared state
- concept: isolated state
- concept: stopping conditions
- organization/product example: Anthropic Claude Research
- organization/product example: Stripe agent review workflow
- organization/product example: IBM watsonx Orchestrate
- company example: Spotify

## Explicit relationships
- Multi-agent architectures depend-on task decomposition, coordination contracts, verification gates, and scoped permissions.
- Orchestrator-worker uses a central coordinator and worker agents; vague task splitting causes duplicated work.
- Pipeline uses fixed stage contracts and supersedes ad-hoc agent loops where auditability matters.
- Hierarchical agents depend-on summarization and can lose detail as reports move upward.
- Multi-agent systems contradict “more agents is always better” because coordination overhead can exceed benefits.
- [[AI Agent Harnesses]] depends-on these architecture choices when background delegation or specialized agents are introduced.

## HoneyDrunk implications
- Start with one agent plus better harness/context; split only for parallelism, isolation, specialization, or auditability.
- Use orchestrator-worker for research/source ingestion only when workers have non-overlapping scopes and synthesis criteria.
- Use pipelines for regulated or repeatable workflows where traceable stage contracts matter more than latency.
- Treat every added agent as a new security and verification surface: give it narrower context, narrower tools, and a clear stop condition.

## Confidence and quality notes
- Quality posture: decision-usable as architecture framing, but source is a newsletter preview/paywalled excerpt; validate against implementation experience before standardizing.
- Weak claims: named case-study metrics were source-reported and not independently verified here.
- Privacy filter: sponsor material and subscription copy omitted; no secrets or unsafe PII copied.
