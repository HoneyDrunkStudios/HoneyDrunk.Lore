# Voice Agent Platforms 2026

## Decision-useful summary
The May 2026 OpenAI voice-agent signal is that real-time speech agents are moving from turn-taking transcription/chat toward reasoning, streaming tool use, translation, and speech-specific model families. The raw capture for The Rundown included heavy site scaffolding and public client config values, so only the article/schema and re-fetched readable body were distilled; any reusable secrets or client config were excluded. [source: raw/2026-05-10-web-the-rundown-ai-openai-closes-reasoning-gap-in-voice-agents.md]

## Claims
- The Rundown article reports that OpenAI introduced GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper as API voice models for AI voice agents and live speech workflows. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-web-the-rundown-ai-openai-closes-reasoning-gap-in-voice-agents.md]
- The same article says Realtime-2 brings stronger reasoning to live speech, can use multiple tools at once, can talk while thinking, and improves tone control. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-web-the-rundown-ai-openai-closes-reasoning-gap-in-voice-agents.md]
- The article reports a Big Bench Audio result of 96.6% for Realtime-2 versus 81.4% for the predecessor; treat the number as publisher-reported and vendor-linked, not independently validated. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-web-the-rundown-ai-openai-closes-reasoning-gap-in-voice-agents.md]
- The article says OpenAI also shipped a live translator covering 70+ languages and a streaming transcription model, with Zillow, Priceline, and Deutsche Telekom named as early builders. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-web-the-rundown-ai-openai-closes-reasoning-gap-in-voice-agents.md]

## Typed entities
- organization: OpenAI
- publisher: The Rundown AI
- model/product: GPT-Realtime-2
- model/product: GPT-Realtime-Translate
- model/product: GPT-Realtime-Whisper
- benchmark: Big Bench Audio
- company: Zillow
- company: Priceline
- company: Deutsche Telekom
- concept: real-time voice agents
- concept: streaming transcription
- concept: live speech translation
- file: raw/2026-05-10-web-the-rundown-ai-openai-closes-reasoning-gap-in-voice-agents.md

## Explicit relationships
- GPT-Realtime-2 uses real-time speech reasoning and tool use to support voice-agent workflows.
- GPT-Realtime-Translate supports multilingual live translation.
- GPT-Realtime-Whisper supports streaming transcription.
- Voice-agent platforms depend-on low-latency reasoning, interruption handling, speech realism, and tool orchestration.
- [[AI Agent Harnesses]] applies to voice agents because tool calls, state, permissions, and verification remain harness responsibilities even when the interface is spoken.

## HoneyDrunk implications
- Voice-agent experiments should test latency, interruption behavior, tool reliability, and user-flow fit rather than only transcription accuracy.
- For any HoneyDrunk voice workflow, design the harness first: what tools can speech invoke, how approvals work, how partial speech/tool failures recover, and what gets logged.
- Treat newsletter benchmark claims as scouting signal until OpenAI docs or local tests confirm them.

## Confidence and quality notes
- Quality posture: useful scouting signal, but not enough for procurement or model-default decisions.
- Weak spots: source is a newsletter article with vendor-linked claims; raw file included large site scaffolding.
- Privacy filter: raw public Sentry/Stripe/VAPID/client configuration strings and site JavaScript were not copied into wiki content.

## 2026-06-07 compile additions

### Claims
- EVA-Bench Data 2.0 is a voice-agent evaluation dataset with 213 scenarios across Airline CSM, ITSM, and Healthcare HRSD, designed around voice-first enterprise workflows, realistic tool schemas, authentication, adversarial calls, unsatisfiable goals, and reproducibility. confidence: 1 ServiceNow-AI benchmark source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-eva-bench-data-2-0-3-domains-121-tools-213-scenarios.md]
- EVA-Bench's generation/validation process uses jointly generated user goals, initial scenario databases, expected final database states, structural validation, LLM consistency checks, trace verification, manual review, and frontier-model solvability checks. confidence: 1 benchmark source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-eva-bench-data-2-0-3-domains-121-tools-213-scenarios.md]
- The EVA-Bench source says multilingual support is being added by localizing conversation language, names, emails, phone numbers, locations, metrics, and judges rather than translating English-only evals mechanically. confidence: 1 benchmark source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-eva-bench-data-2-0-3-domains-121-tools-213-scenarios.md]

### Typed entities
- benchmark/dataset: EVA-Bench Data 2.0
- dataset split: airline
- dataset split: itsm
- dataset split: medical / HRSD
- concept: voice-first scope
- concept: authentication flow
- concept: adversarial call
- concept: unsatisfiable goal
- pipeline: SyGra

### Explicit relationships
- Voice-agent evaluation depends-on tool execution, authentication, final-state verification, and realistic caller behavior, not just ASR or response wording.
- Multilingual voice evaluation depends-on localized scenario data and judging metrics, not direct text translation alone.
- EVA-Bench complements real-time voice model benchmarks by testing enterprise workflow completion.

### HoneyDrunk implications
- Any HoneyDrunk voice-agent benchmark should include authentication, no-solution cases, tool calls, and final-state checks.
- Treat multilingual voice support as a separate eval dimension with localized data and phone/name/address conventions.

### Quality notes
- Benchmark is open-source per source, but scenario content and leaderboard should be inspected directly before use. No private example phone/email data was copied into the wiki.

## 2026-06-11 compile additions: RT.Assistant .NET voice architecture

### Source-backed claims
- RT.Assistant is a .NET/F# multi-agent voice sample using OpenAI Realtime API over WebRTC for low-latency bidirectional voice, Microsoft.Extensions.AI for portable model access, and .NET MAUI/Fabulous for cross-platform UI. Source: `raw/2026-06-11-web-net-blog-rt-assistant-a-multi-agent-voice-bot-using-net-and-openai-net-blog.md`. confidence: 1 Microsoft/.NET guest post, last-confirmed 2026-06-11.
- RT.Assistant uses multiple specialized agents: Voice Agent, CodeGen Agent, Query Agent, and App Agent, coordinated through RTFlow's typed async bus and deterministic Flow state machine. Source: `raw/2026-06-11-web-net-blog-rt-assistant-a-multi-agent-voice-bot-using-net-and-openai-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-11.
- The sample uses LLM-generated Prolog queries against a structured Prolog knowledge base, so the LLM translates the question while Prolog computes/checks the answer against explicit facts. Source: `raw/2026-06-11-web-net-blog-rt-assistant-a-multi-agent-voice-bot-using-net-and-openai-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-11.

### Typed entities
- project: RT.Assistant
- framework: RTFlow
- library: RTOpenAI
- protocol: WebRTC
- API: OpenAI Realtime API
- framework: .NET MAUI
- framework: Fabulous
- language: F#
- engine: Tau Prolog
- agent role: Voice Agent
- agent role: CodeGen Agent
- agent role: Query Agent
- agent role: App Agent

### Explicit relationships
- RT.Assistant uses WebRTC to reduce realtime voice transport burden versus raw WebSocket audio handling.
- RTFlow uses typed messages and deterministic state machines to constrain multi-agent voice workflows.
- Prolog-backed query execution reduces answer hallucination risk by moving domain fact evaluation into a symbolic engine.

### HoneyDrunk implications
- For voice agents that answer from structured rules/catalogs, prefer LLM-to-query plus deterministic execution over direct answer generation when correctness matters.
- If HoneyDrunk prototypes native voice agents, validate WebRTC device support, typed event handling, interruption behavior, and UI transparency before model choice.

### Quality notes
- Guest post/sample evidence is useful architecture signal; production readiness requires local evals, error handling, and privacy review.
