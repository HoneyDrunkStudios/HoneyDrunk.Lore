# Google Agent Platform and Gemini API 2026

## Decision-useful summary
Google's 2026 agent developer surface is converging on production plumbing: Agents CLI gives coding assistants a machine-readable path from scaffold to eval to deploy; Gemini API webhooks reduce polling for long-running jobs; Gemini Embedding 2 provides unified multimodal retrieval; ADK production lessons emphasize subagents, structured outputs, dynamic RAG, observability, and circuit breakers. [sources: raw/2026-05-08-rss-google-developers-blog-agents-cli-in-agent-platform-create-to-producti.md; raw/2026-05-08-rss-google-ai-blog-reduce-friction-and-latency-for-long-running-jobs-with-.md; raw/2026-05-08-rss-google-developers-blog-building-with-gemini-embedding-2-agentic-multim.md; raw/2026-05-08-rss-google-developers-blog-production-ready-ai-agents-5-lessons-from-refac.md]

## Claims
- Google Agents CLI is positioned as a programmatic backbone for the Agent Development Lifecycle on Google Cloud, giving AI coding assistants machine-readable access to Agent Platform, Cloud Run, A2A Integration, evaluation, infrastructure, deployment, and publishing workflows. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-agents-cli-in-agent-platform-create-to-producti.md]
- Agents CLI supports both agent-mode consumption by coding assistants and human-mode deterministic terminal/script use; example commands include `uvx google-agents-cli setup`, `agents-cli create`, `agents-cli eval run`, `agents-cli infra single-project`, `agents-cli deploy`, and `agents-cli publish gemini-enterprise`. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-agents-cli-in-agent-platform-create-to-producti.md]
- Gemini API webhooks add event-driven completion callbacks for long-running jobs such as Deep Research, long video generation, and Batch API processing, replacing repeated GET polling with signed HTTP POST notifications. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-ai-blog-reduce-friction-and-latency-for-long-running-jobs-with-.md]
- Gemini API webhooks follow the Standard Webhooks specification, include `webhook-signature`, `webhook-id`, and `webhook-timestamp` headers, provide at-least-once delivery, and retry for up to 24 hours. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-ai-blog-reduce-friction-and-latency-for-long-running-jobs-with-.md]
- Gemini Embedding 2 is generally available via Gemini API and Gemini Enterprise Agent Platform; it maps text, images, video, audio, and documents into one semantic space, supports 100+ languages, and accepts up to 8,192 text tokens, 6 images, 120 seconds video, 180 seconds audio, and 6 PDF pages in one call. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-building-with-gemini-embedding-2-agentic-multim.md]
- Gemini Embedding 2 supports task-specific prefixes for retrieval/search/fact-checking/code retrieval/classification/clustering and Matryoshka dimensionality reduction from 3072 dimensions to smaller vectors such as 1536 or 768 for storage efficiency. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-building-with-gemini-embedding-2-agentic-multim.md]
- Google's Agent Clinic refactor lesson says production agents should replace monolithic prompt/scripts with orchestrated subagents, structured Pydantic outputs, dynamic RAG pipelines, OpenTelemetry tracing, and framework-level retries/timeouts/circuit breakers. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-production-ready-ai-agents-5-lessons-from-refac.md]
- Google's free Kaggle AI Agents Intensive course returns June 15-19, 2026 with updated content, speakers, natural-language/vibe-coding workflows, tool/API integration, and a capstone project. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-ai-blog-join-the-new-ai-agents-vibe-coding-course-from-google-a.md]

## Typed entities
- company: Google
- product: Google Agent Platform
- tool: Agents CLI
- product/API: Gemini API
- feature: Gemini API webhooks
- model: Gemini Embedding 2
- framework: Agent Development Kit (ADK)
- protocol/spec: Standard Webhooks
- protocol: A2A Integration
- concept: Agent Development Lifecycle (ADLC)
- concept: multimodal RAG
- concept: dynamic RAG pipeline
- library: Pydantic
- standard/tooling: OpenTelemetry
- training program: Google/Kaggle AI Agents Intensive Course

## Explicit relationships
- Agents CLI uses Google Cloud Agent Platform, Cloud Run, A2A Integration, eval, IaC, deploy, and publish commands to move agents from local creation to production.
- Gemini API webhooks supersede polling for supported long-running jobs by pushing signed completion events.
- Gemini Embedding 2 enables multimodal RAG by mapping text, image, video, audio, and documents into a shared embedding space.
- Production AI agents depend-on structured outputs, specialized subagents, retrieval, observability, and bounded retry/cost controls.
- ADK uses OpenTelemetry to make agent execution traces inspectable.

## HoneyDrunk implications
- HoneyDrunk's Grid/Lore long-running jobs should prefer push/event completion over polling when the platform supports it; Gemini's webhook design is a reference pattern.
- For multimodal Lore or asset retrieval, Gemini Embedding 2 is worth evaluating because it handles mixed images/audio/video/docs in a single semantic space.
- The Agent Clinic lessons match local code-generation hygiene: break agents into narrow roles, make schemas executable, trace tool calls, and turn repeated failures into gates.
- Agents CLI is useful if HoneyDrunk deploys production agents on Google Cloud; otherwise treat it as a design reference for agent-consumable deployment tooling.

## Confidence and quality notes
- Quality posture: decision-usable for platform scouting; vendor-authored benchmarks and claims should be validated before procurement.
- Weak claims: course value and customer metric improvements are directional, not independently audited.
- Privacy filter: no credentials or personal private data copied.

## 2026-05-23 compile additions

### Claims
- Google announced Gemini 3.5 Flash as the first Gemini 3.5 model, positioning it for complex agentic workflows, coding, multimodal understanding, and broad availability through Gemini app/Search AI Mode, Google Antigravity, Gemini API/AI Studio/Android Studio, Gemini Enterprise Agent Platform, and Gemini Enterprise. confidence: 1 vendor source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-ai-gemini-3-5-flash-5-minute-read.md]
- Google says Gemini 3.5 Flash outperforms Gemini 3.1 Pro on named coding/agentic benchmarks and is four times faster by output tokens/sec than the prior Pro comparison; treat benchmark claims as vendor-authored until independently validated. confidence: 1 vendor source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-ai-gemini-3-5-flash-5-minute-read.md]
- Sundar Pichai's I/O 2026 remarks frame Google's AI strategy as a full-stack “agentic Gemini era” across custom silicon, models, products, and platforms, with emphasis on product value rather than raw demos. confidence: 1 vendor keynote transcript, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-ai-google-detailed-the-shift-toward-agentic-gemini-products-19-mi.md]
- The Qwen3.7 raw capture contained only page scaffolding/title-level metadata and no decision-grade article body facts; no Qwen3.7 capability claims were promoted. confidence: 1 low-yield capture, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-tldr-ai-qwen3-7-the-agent-frontier-15-minute-read.md]

### Typed entities
- model: Gemini 3.5 Flash
- model: Gemini 3.5 Pro
- model: Gemini 3.1 Pro
- product/platform: Google Antigravity
- product/platform: Gemini Enterprise Agent Platform
- person: Sundar Pichai
- model family: Qwen3.7
- concept: agentic Gemini era

### Explicit relationships
- Gemini 3.5 Flash supersedes Gemini 3.1 Pro in Google's stated agent/coding positioning, pending local validation.
- Google Antigravity and Gemini API use Gemini 3.5 Flash as a developer-facing agent runtime surface.
- Low-yield Qwen3.7 capture depends-on improved extraction before Lore can compare Qwen3.7 against Gemini/Claude/OpenAI models.

### HoneyDrunk implications
- Put Gemini 3.5 Flash on the benchmark shortlist for cheap/fast coding-agent and multimodal-routing tasks, but do not trust vendor benchmark deltas without representative HoneyDrunk runs.

## 2026-05-31 compile additions

### Claims
- Google released ADK for Kotlin and ADK for Android 0.1.0, after ADK for Java and Go 1.0.0 and ADK for Python 2.0 beta, positioning Kotlin for backend agent workflows and Android for on-device/hybrid mobile agents. confidence: 1 vendor source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-google-developers-blog-announcing-adk-for-kotlin-and-adk-for-android-0.md]
- ADK for Android is designed for hybrid orchestration: a cloud model can act as main orchestrator while on-device subagents use Gemini Nano through Android/AICore paths to retrieve and parse local documents without sending private data off-device. confidence: 1 vendor source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-google-developers-blog-announcing-adk-for-kotlin-and-adk-for-android-0.md]
- The ADK for Kotlin/Android 0.1.0 feature set includes LLM/workflow/custom agents, multi-agent systems, function tools, long-running tools, MCP tools, A2A plugins, session state, memory service, OpenTelemetry telemetry, and a web interface for development/experimentation. confidence: 1 vendor source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-google-developers-blog-announcing-adk-for-kotlin-and-adk-for-android-0.md]
- Google reports Gemini Nano availability on more than 140 million Android devices as the edge-AI motivation for ADK for Android; treat this as platform-reach signal, not a guarantee of capability parity across devices. confidence: 1 vendor source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-google-developers-blog-announcing-adk-for-kotlin-and-adk-for-android-0.md]

### Typed entities
- framework: ADK for Kotlin
- framework: ADK for Android
- model: Gemini Nano
- Android service/surface: AICore
- API/library: ML Kit GenAI
- product: Firebase AI Logic
- protocol: Model Context Protocol
- protocol: A2A
- concept: hybrid cloud/on-device orchestration
- concept: local document retrieval

### Explicit relationships
- ADK for Android uses on-device models to keep sensitive retrieval/parsing local while cloud models can orchestrate broader reasoning.
- Kotlin ADK depends-on Gradle/KSP tooling for typed function tools.
- ADK uses OpenTelemetry to make mobile/backend agent traces inspectable.
- Edge-agent privacy depends-on device capability, model availability, and clear delegation boundaries between cloud and local agents.

### HoneyDrunk implications
- For Android apps with private local documents or user state, evaluate hybrid ADK only after testing device coverage, latency, offline behavior, and what leaves the device.
- Treat ADK for Kotlin/Android 0.1.0 as experimental; useful for prototypes and architecture scouting, not a stable production dependency without version pinning and migration budget.
