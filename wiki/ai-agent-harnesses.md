# AI Agent Harnesses

## Decision-useful summary
An agent is best treated as `model + harness`: the model supplies probabilistic reasoning, while the harness supplies state, tools, execution constraints, feedback loops, storage, orchestration, and verification. This matters for HoneyDrunk because durable agent value comes less from swapping models and more from making the runtime reliable: filesystem-backed context, safe shell/code execution, sandboxing, memory/search, continuations, lint gates, and background delegation. [source: raw/2026-05-03-web-langchain-agent-harness.md]

## Claims
- Harness engineering is the non-model layer that turns a raw LLM into a work engine by providing prompts, tools, skills/MCPs, bundled infrastructure, orchestration, hooks, and execution policy. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-web-langchain-agent-harness.md]
- Long-horizon agents need durable storage, context management, sandboxed execution, verification, memory/search, and countermeasures for context rot. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-web-langchain-agent-harness.md]
- Background/async subagents address supervisor deadlock and coordination problems by allowing delegated work to continue while the parent agent remains responsive to new information. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-web-langchain-async-subagents.md]
- OpenAI Codex CLI 0.128.0 added `/goal`, a continuation loop that keeps working until goal completion or token-budget exhaustion, apparently driven mainly by continuation and budget-limit prompt templates. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-simonwillison-codex-cli-goal.md]
- Google Agents CLI reinforces that agent harnesses now include machine-readable scaffolding, evaluation, infrastructure provisioning, deployment, and publishing commands for coding assistants, not just chat prompts. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-agents-cli-in-agent-platform-create-to-producti.md]
- Gemini API webhooks reinforce push-based completion as a harness primitive for long-running agent jobs, with signed events, idempotency headers, at-least-once delivery, and retries instead of repeated polling. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-ai-blog-reduce-friction-and-latency-for-long-running-jobs-with-.md]
- Google's ADK refactor case study reinforces production-agent harness needs: specialized subagents, executable schemas/structured outputs, dynamic retrieval, traces, retries, timeouts, and cost circuit breakers. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-production-ready-ai-agents-5-lessons-from-refac.md]
- Microsoft Agent Framework durable workflows reinforce that reliable agent harnesses need checkpointing, restart survival, distributed execution, external observability, generated HTTP/MCP entrypoints, and human-in-the-loop wait states. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-net-blog-durable-workflows-in-the-microsoft-agent-framework.md]
- The Curity/Microsoft least-privilege template reinforces that production agent harnesses should push authorization into short-lived tokens, API filters, gateways, and audit logs rather than relying on model behavior or prompt compliance. confidence: 1 source, last-confirmed 2026-05-09. [source: raw/2026-05-09-rss-azure-blog-least-privilege-ai-agents-a-new-azd-template-from-curity-an.md]
- Voice-agent platforms reinforce that the harness must handle low-latency tool orchestration, partial/interrupted speech, permissions, recovery, and logging; stronger real-time models do not remove those responsibilities. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-web-the-rundown-ai-openai-closes-reasoning-gap-in-voice-agents.md]
- Dataverse's agentic-shift framing reinforces that agents need business context, relationships, rules, and process skills in addition to raw data access. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-youtube-microsoft-developer-youtube-dataverse-and-the-agentic-shift.md]
- Microsoft MCP app samples reinforce that app/client harness surfaces increasingly include reusable UI widgets, manifests/docs, previews, and cross-assistant compatibility rather than only raw tool schemas. confidence: 1 source, last-confirmed 2026-05-11. [source: raw/2026-05-11-youtube-microsoft-developer-youtube-don-t-build-mcp-apps-from-scratch-use-this.md]

## Typed entities
- concept: [[AI Agent Harnesses]]
- concept: Model Context Protocol
- library/platform: LangChain Deep Agents
- library/tool: OpenAI Codex CLI
- feature: `/goal`
- feature/tool: Google Agents CLI
- feature/API: Gemini API webhooks
- framework: Google Agent Development Kit (ADK)
- framework: Microsoft Agent Framework
- protocol/security pattern: OAuth 2.0 token exchange
- model/product: GPT-Realtime-2
- platform/service: Microsoft Dataverse
- resource: MCP app samples
- concept: Business Skills
- standard/tooling: OpenTelemetry
- pattern: async subagents
- pattern: structured outputs
- file: raw/2026-05-03-web-langchain-agent-harness.md
- file: raw/2026-05-03-web-langchain-async-subagents.md
- file: raw/2026-05-03-rss-simonwillison-codex-cli-goal.md

## Explicit relationships
- [[AI Agent Harnesses]] uses tools, filesystems, sandboxes, memory/search, orchestration, and verification to make model output actionable.
- async subagents fixed supervisor deadlock and parent-agent context coordination problems described for traditional subagents.
- OpenAI Codex CLI `/goal` uses continuation prompts and budget-limit prompts to implement a Ralph-style loop.
- [[Azure MCP Server 2.0]] depends-on Model Context Protocol as one harness/tool-integration surface.
- Google Agents CLI uses eval, infrastructure, deploy, and publish commands as an agent-consumable harness surface.
- Gemini API webhooks supersede polling for supported long-running jobs.
- Production agent harnesses depend-on structured outputs, observability, and bounded retries/cost controls.
- Durable Microsoft Agent Framework workflows use checkpointing and Durable Task Scheduler to survive process restarts and coordinate distributed executors.
- Least-privilege AI agents use OAuth 2.0 token exchange, gateways, and API-side filters to constrain nondeterministic tool calls.
- Voice agents depend-on the same harness controls as text agents, plus speech-specific latency, interruption, and recovery handling.
- Business-context agents depend-on semantic relationships and process/rule descriptions, not just record retrieval.
- MCP app surfaces depend-on reusable sample patterns, UI widgets, docs, and compatibility testing across assistant clients.

## HoneyDrunk implications
- Prefer investing in runtime affordances (state, validation, background workers, resumability, audit logs) before model-specific prompt churn.
- Treat every long-running agent workflow as a harness design problem: define storage, tools, permissions, verification gate, and what happens when budget runs out.
- Prefer push/completion-event contracts for long jobs where possible; polling is a fallback, not the ideal orchestration shape.
- Treat authorization as harness infrastructure: short-lived scoped tokens, gateway audit logs, and API filters should constrain agents before prompts do.
- For voice or business-process agents, define approval/recovery paths and domain rules before exposing high-impact tools.
- Reuse sample MCP app/client patterns before custom implementation; spend custom effort on permissions, state, and verification rather than protocol boilerplate.

## Confidence and quality notes
- Quality posture: decision-usable; claims are source-cited and non-private.
- Weak spots: LangChain source is vendor-authored; validate operational patterns against local OpenClaw behavior before architecture commitments.
- Privacy filter: no credentials or unsafe PII copied from raw sources.
