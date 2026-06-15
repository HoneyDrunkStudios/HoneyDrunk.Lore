# OpenAI Frontier Models and Codex 2026

## Decision-useful summary
OpenAI's June 11 raw sources add two durable signals for HoneyDrunk: GPT-5.5 is positioned as a stronger agentic coding, computer-use, professional-work, science, and cybersecurity model, while OpenAI's own Codex deployment emphasizes sandboxing, approvals, managed network policy, secure credential custody, and agent-native telemetry. Treat the model claims as strong vendor capability signal but not local routing policy until HoneyDrunk runs task-specific evals. [sources: raw/2026-06-11-web-openai-introducing-gpt-5-5.md; raw/2026-06-11-web-openai-running-codex-safely-at-openai.md]

## Source-backed claims
- OpenAI says GPT-5.5 and GPT-5.5 Pro were available in the API after the April 24, 2026 update, with GPT-5.5 positioned for agentic coding, computer use, knowledge work, and early scientific research. Source: `raw/2026-06-11-web-openai-introducing-gpt-5-5.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-11.
- OpenAI reports GPT-5.5 in Codex with a 400K context window for Plus, Pro, Business, Enterprise, Edu, and Go plans, plus a Fast mode at higher cost; API pricing in the source lists `gpt-5.5` and `gpt-5.5-pro` tiers with standard, Batch/Flex, and Priority options. Source: `raw/2026-06-11-web-openai-introducing-gpt-5-5.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-11.
- OpenAI says GPT-5.5 improves over GPT-5.4 on agentic coding and long-context tasks while using fewer tokens on Codex tasks; all benchmark and customer examples remain vendor-reported until locally reproduced. Source: `raw/2026-06-11-web-openai-introducing-gpt-5-5.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-11.
- OpenAI treats GPT-5.5 biological/chemical and cybersecurity capabilities as High under its Preparedness Framework, and describes stricter cyber safeguards plus Trusted Access for Cyber for verified defensive users. Source: `raw/2026-06-11-web-openai-introducing-gpt-5-5.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-11.
- OpenAI's internal Codex deployment combines sandbox boundaries, approval policy, auto-review for some requests, managed network allowlists, secure OS keyring credential storage, enterprise workspace pinning, command allow/block rules, OpenTelemetry export, and compliance logs. Source: `raw/2026-06-11-web-openai-running-codex-safely-at-openai.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-11.

## Typed entities
- organization: OpenAI
- model: GPT-5.5
- model: GPT-5.5 Pro
- product: Codex
- mode: Codex Fast mode
- framework: OpenAI Preparedness Framework
- program: Trusted Access for Cyber
- control: sandbox policy
- control: approval policy
- control: managed network allowlist
- control: secure OS keyring
- standard: OpenTelemetry
- product: OpenAI Compliance Platform

## Explicit relationships
- GPT-5.5 supersedes GPT-5.4 in OpenAI's stated Codex/coding positioning, pending local validation.
- GPT-5.5 cybersecurity capability depends-on stronger safeguards and trusted-access pathways for verified defensive use.
- Codex safety depends-on sandbox, approval, network, credential, command-policy, and telemetry controls outside the model.
- OpenTelemetry logs complement compliance logs by preserving agent-specific prompts, approvals, tool results, MCP usage, and network policy decisions where configured.

## HoneyDrunk implications
- Add GPT-5.5 to HoneyDrunk coding-agent and long-context eval queues, but compare against current defaults on actual OpenClaw/Lore/Grid tasks before changing routing.
- Treat higher cyber/science capability as both opportunity and control burden: defensive use should run under verified access, audit, and scope controls.
- Mirror the Codex deployment pattern for OpenClaw where possible: bounded workspace, egress allowlist, credential indirection, blocked dangerous commands, approval gates, and OTel logs.

## Confidence and quality notes
- Quality posture: decision-usable as OpenAI product/safety signal. Benchmarks, customer quotes, and cost-efficiency claims are vendor-authored and need local reproduction.
- Privacy filter: no private prompts, credentials, customer data, or unsafe cyber procedure details were copied from raw sources.

## 2026-06-12 compile additions: One year of Responses

### Source-backed claims
- OpenAI's one-year Responses API post positions Responses as the foundation for hosted tools and agentic workflows, with customer/developer examples spanning agent monitoring, context engineering, record-collection chat, product-demo generation, and AI-output visibility analytics. Source: `raw/2026-06-12-web-openai-developers-from-prompts-to-products-one-year-of-responses-openai-develo.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-12.
- The Raindrop AI example uses Responses for long-running background analysis workflows that monitor agent behavior, detect anomalies/failures, alert developers, and help inspect reasoning traces/tool calls. Source: `raw/2026-06-12-web-openai-developers-from-prompts-to-products-one-year-of-responses-openai-develo.md`. confidence: 1 official OpenAI customer-story source, last-confirmed 2026-06-12.
- The Repo Prompt example separates context-building agents from a deep reasoning workflow, using Responses background jobs, orchestration, and observability so the final reasoning model analyzes curated context rather than spending context budget gathering it. Source: `raw/2026-06-12-web-openai-developers-from-prompts-to-products-one-year-of-responses-openai-develo.md`. confidence: 1 official OpenAI customer-story source, last-confirmed 2026-06-12.
- The Arcade example uses Responses with the computer-use tool to infer structured interaction steps from screen recordings, then generate guided product-demo walkthroughs; OpenAI reports Arcade reduced median pre-publish actions by 50%. Source: `raw/2026-06-12-web-openai-developers-from-prompts-to-products-one-year-of-responses-openai-develo.md`. confidence: 1 official OpenAI customer-story source, last-confirmed 2026-06-12.
- OpenAI says Responses is adding richer tool ecosystems including hosted containers with networking and shell tools. Source: `raw/2026-06-12-web-openai-developers-from-prompts-to-products-one-year-of-responses-openai-develo.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-12.

### Typed entities
- API: OpenAI Responses API
- feature: background jobs
- feature: hosted tools
- feature: hosted containers with networking
- feature: shell tools
- company/product: Raindrop AI
- company/product: Repo Prompt
- company/product: Collxn
- company/product: Arcade
- company/product: Hexagon
- tool: computer use
- concept: context-building agent
- concept: agent monitoring

### Explicit relationships
- Responses API uses hosted and custom tools to move chat-style interactions toward agentic workflows.
- Agent monitoring uses Responses background analysis to detect and diagnose production agent failures.
- Context-building agents complement deep reasoning models by curating relevant context before long analysis.
- Computer-use tooling converts visual workflows into structured actions when native event capture is unavailable or incomplete.

### HoneyDrunk implications
- For OpenClaw/Lore deep research, preserve the context-builder versus reasoning-worker split: retrieval/curation should be auditable before final synthesis.
- If HoneyDrunk adopts Responses background jobs or hosted containers, require run receipts, egress policy, tool-call telemetry, and cost/time limits.
- Treat OpenAI customer metric claims as product-story evidence only; reproduce workflow improvements locally before changing process.

### Quality notes
- Official OpenAI post is authoritative for product positioning and named examples. Customer outcome metrics and model/tool usage remain vendor-curated and need local validation.

## 2026-06-15 compile additions: Ona acquisition for persistent Codex execution

### Source-backed claims
- OpenAI announced that it will acquire Ona, subject to closing conditions and regulatory approvals, to bring secure cloud execution and orchestration technology into the Codex ecosystem. Source: `raw/2026-06-15-web-openai-openai-to-acquire-ona.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-15.
- OpenAI says Codex has more than 5 million weekly users, up 400% from earlier in 2026; treat the user-count and growth rate as vendor-reported product scale evidence. Source: `raw/2026-06-15-web-openai-openai-to-acquire-ona.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-15.
- OpenAI frames the Ona acquisition around long-running Codex work that can continue for hours or days in secure, persistent environments after the user's local machine or active session is no longer present. Source: `raw/2026-06-15-web-openai-openai-to-acquire-ona.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-15.
- Ona's customer-controlled execution model is intended to let agents operate inside an organization's own cloud environment while OpenAI supplies intelligence and orchestration, preserving customer control over infrastructure, data, credential scope, logging, review, and security boundaries. Source: `raw/2026-06-15-web-openai-openai-to-acquire-ona.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-15.

### Typed entities
- company: Ona
- company: OpenAI
- product: Codex
- concept: secure persistent cloud execution
- concept: customer-controlled execution environment
- control: scoped credentials
- control: activity logging
- control: review workflow

### Explicit relationships
- Ona technology complements Codex by moving agent execution from single-device sessions toward persistent organization-controlled cloud environments.
- Long-running Codex work depends-on execution environments with controlled tool access, credential scope, logging, and review.
- Customer-controlled cloud execution complements OpenAI-hosted intelligence by keeping infrastructure and data boundaries under the customer's control.

### HoneyDrunk implications
- Treat persistent Codex execution as a strong platform-direction signal for OpenClaw/Honeyclaw: long-running agents need resumable state, logs, scoped credentials, and review checkpoints, not only better prompts.
- If HoneyDrunk evaluates hosted/persistent agent environments, compare whether the execution plane remains under HoneyDrunk control and whether logs/reviews are inspectable before adoption.

### Quality notes
- Official acquisition announcement; product claims are vendor-authored and the acquisition had not closed in the source.
