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

## 2026-05-30 compile additions

### Claims
- Microsoft Learn's AI agent orchestration guide explicitly recommends using the lowest reliable complexity level: direct model call, single agent with tools, then multiagent orchestration only when cross-domain work, parallel specialization, context/tool overload, or security boundaries justify it. confidence: 1 Microsoft architecture source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-ai-agent-orchestration-patterns.md]
- The guide names five multiagent orchestration patterns: sequential, concurrent, group chat, handoff, and magentic manager-led task-ledger orchestration. confidence: 1 Microsoft architecture source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-ai-agent-orchestration-patterns.md]
- Sequential orchestration suits known ordered transformations and auditability, but should be avoided when stages can run independently, need backtracking, or require dynamic routing. confidence: 1 Microsoft architecture source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-ai-agent-orchestration-patterns.md]
- Concurrent orchestration suits independent perspectives and latency-sensitive fan-out/fan-in work, but requires conflict-resolution and resource controls. confidence: 1 Microsoft architecture source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-ai-agent-orchestration-patterns.md]
- Magentic orchestration uses a manager agent and task/progress ledger for open-ended plans that adapt as new information arrives; the source warns about slow convergence, stalls on ambiguous goals, and the need for audit trails and loop controls. confidence: 1 Microsoft architecture source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-microsoft-learn-ai-agent-orchestration-patterns.md]
- Claude Code dynamic workflows are a concrete vendor product signal for large-scale concurrent/magentic-style work: tasks fan out to tens or hundreds of subagents, are verified before synthesis, and can run for hours or days. confidence: 1 official vendor source, last-confirmed 2026-05-30. [source: raw/2026-05-30-web-anthropic-introducing-dynamic-workflows-in-claude-code.md; page: [[claude-platform-2026]]]

### Typed entities
- pattern: sequential orchestration
- pattern: concurrent orchestration
- pattern: group chat orchestration
- pattern: handoff orchestration
- pattern: magentic orchestration
- concept: task ledger
- concept: progress ledger
- framework: Microsoft Agent Framework
- product: Foundry Agent Service
- framework: Semantic Kernel
- product: Claude Code dynamic workflows

### Explicit relationships
- Multiagent orchestration depends-on explicit routing, context/state management, reliability controls, security trimming, observability, and cost measurement.
- Sequential orchestration supersedes ad hoc agent loops when process order is known and auditability matters.
- Concurrent orchestration uses fan-out/fan-in but depends-on aggregation and contradiction handling.
- Magentic orchestration depends-on a manager-maintained task ledger and loop/stall controls.
- Dynamic workflows are product evidence that parallel subagents are entering mainstream coding tools, but they do not supersede the need for scoped tasks and verification gates.

### HoneyDrunk implications
- Reuse the five-pattern vocabulary when designing OpenClaw/Grid flows so the team can distinguish pipelines, fan-out review, handoffs, and adaptive task-ledger work.
- Default to single-agent-with-tools until there is a hard reason to split agents.
- If using dynamic workflows or magentic-style managers, persist task state and define stop/approval conditions before long runs begin.

## 2026-06-01 compile additions

### Claims
- NVIDIA's Gamma-World research project frames multi-agent world modeling as an interactive-video-generation problem where multiple independently controllable agents act in one evolving environment while preserving temporal and cross-perspective consistency. confidence: 1 research project page, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-gamma-world-generative-multi-agent-world-modeling-beyond-two-players.md]
- Gamma-World introduces Simplex Rotary Agent Encoding to make agents distinct while permutation-equivalent, Sparse Hub Attention to reduce cross-agent attention cost from quadratic to linear in agent count, and teacher-student distillation so a causal model can stream rollouts with KV caching. confidence: 1 research project page, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-gamma-world-generative-multi-agent-world-modeling-beyond-two-players.md]
- Judgment Labs' Agent Judge uses a multi-agent evaluator structure where reader/worker/forked agents inspect targeted trajectory evidence and source-of-truth state rather than pushing the whole trace through one judge prompt. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-agent-judge-solving-long-context-evals-for-production-agents.md; page: [[agent-evaluation-and-benchmarks]]]

### Typed entities
- research project: Gamma-World / gamma-World
- organization: NVIDIA Spatial Intelligence Lab
- concept: generative multi-agent world model
- method: Simplex Rotary Agent Encoding
- method: Sparse Hub Attention
- method: teacher-student distillation
- concept: block-causal student
- concept: KV caching
- pattern: multi-agent evaluator

### Explicit relationships
- Multi-agent world models depend-on independent controllability and shared-environment consistency.
- Sparse Hub Attention reduces cross-agent communication cost compared with full pairwise attention.
- Multi-agent evaluation uses worker specialization to inspect long traces without one oversized judge context.

### HoneyDrunk implications
- For future game/agent simulations, track multi-agent world models as research, not production tooling; validate controllability, runtime cost, and asset/control integration before adoption.
- Use multi-agent evaluators only when evidence search can be partitioned cleanly and synthesis criteria are explicit.
