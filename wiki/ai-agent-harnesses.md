# AI Agent Harnesses

## Decision-useful summary
An agent is best treated as `model + harness`: the model supplies probabilistic reasoning, while the harness supplies state, tools, execution constraints, feedback loops, storage, orchestration, and verification. This matters for HoneyDrunk because durable agent value comes less from swapping models and more from making the runtime reliable: filesystem-backed context, safe shell/code execution, sandboxing, memory/search, continuations, lint gates, and background delegation. [source: raw/2026-05-03-web-langchain-agent-harness.md]

## Claims
- Harness engineering is the non-model layer that turns a raw LLM into a work engine by providing prompts, tools, skills/MCPs, bundled infrastructure, orchestration, hooks, and execution policy. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-web-langchain-agent-harness.md]
- Long-horizon agents need durable storage, context management, sandboxed execution, verification, memory/search, and countermeasures for context rot. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-web-langchain-agent-harness.md]
- Background/async subagents address supervisor deadlock and coordination problems by allowing delegated work to continue while the parent agent remains responsive to new information. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-web-langchain-async-subagents.md]
- OpenAI Codex CLI 0.128.0 added `/goal`, a continuation loop that keeps working until goal completion or token-budget exhaustion, apparently driven mainly by continuation and budget-limit prompt templates. confidence: 1 source, last-confirmed 2026-05-05. [source: raw/2026-05-03-rss-simonwillison-codex-cli-goal.md]

## Typed entities
- concept: [[AI Agent Harnesses]]
- concept: Model Context Protocol
- library/platform: LangChain Deep Agents
- library/tool: OpenAI Codex CLI
- feature: `/goal`
- pattern: async subagents
- file: raw/2026-05-03-web-langchain-agent-harness.md
- file: raw/2026-05-03-web-langchain-async-subagents.md
- file: raw/2026-05-03-rss-simonwillison-codex-cli-goal.md

## Explicit relationships
- [[AI Agent Harnesses]] uses tools, filesystems, sandboxes, memory/search, orchestration, and verification to make model output actionable.
- async subagents fixed supervisor deadlock and parent-agent context coordination problems described for traditional subagents.
- OpenAI Codex CLI `/goal` uses continuation prompts and budget-limit prompts to implement a Ralph-style loop.
- [[Azure MCP Server 2.0]] depends-on Model Context Protocol as one harness/tool-integration surface.

## HoneyDrunk implications
- Prefer investing in runtime affordances (state, validation, background workers, resumability, audit logs) before model-specific prompt churn.
- Treat every long-running agent workflow as a harness design problem: define storage, tools, permissions, verification gate, and what happens when budget runs out.

## Confidence and quality notes
- Quality posture: decision-usable; claims are source-cited and non-private.
- Weak spots: LangChain source is vendor-authored; validate operational patterns against local OpenClaw behavior before architecture commitments.
- Privacy filter: no credentials or unsafe PII copied from raw sources.
