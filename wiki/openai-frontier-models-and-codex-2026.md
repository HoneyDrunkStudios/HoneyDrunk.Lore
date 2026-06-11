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
