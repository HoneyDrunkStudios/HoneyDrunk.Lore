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
