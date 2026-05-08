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
