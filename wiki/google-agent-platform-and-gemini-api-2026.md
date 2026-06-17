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

## 2026-06-03 compile additions

### Claims
- Google AI Edge Gallery added experimental MCP support over Streamable HTTP in the Android app, letting an on-device Gemma 4 model import tool/resource schemas into the prompt, choose tools locally, and call a configured MCP server on a home computer or secure cloud endpoint. confidence: 1 Google Developers source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-google-developers-blog-a-smarter-google-ai-edge-gallery-mcp-integratio.md]
- The same release adds a Schedule Notification skill, persistent chat history, fast prefill via LiteRT-LM, and custom system prompt editing, making AI Edge Gallery a mobile/on-device agent experimentation surface rather than only a one-shot model demo. confidence: 1 Google Developers source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-google-developers-blog-a-smarter-google-ai-edge-gallery-mcp-integratio.md]

### Typed entities
- app: Google AI Edge Gallery
- model: Gemma 4
- protocol: Model Context Protocol
- transport: Streamable HTTP
- skill: Schedule Notification
- feature: persistent chat history
- runtime/backend: LiteRT-LM
- concept: custom system prompt

### Explicit relationships
- Google AI Edge Gallery uses MCP to connect local mobile reasoning to external tools.
- LiteRT-LM fast prefill enables persistent session restoration on device.
- Local notification skills turn reactive chat sessions into scheduled mobile routines.

### HoneyDrunk implications
- For Android/on-device agent prototypes, Google AI Edge Gallery is now a useful scouting app for MCP, local reminders, and session continuity.
- Treat mobile MCP as a privacy boundary exercise: local reasoning does not guarantee local data handling if the MCP server retrieves or sends external data.

## 2026-06-11 compile additions: I/O 2026 Antigravity, Android agents, and WebMCP

### Source-backed claims
- Google I/O 2026 Developer keynote announced Gemini 3.5 series models, Antigravity 2.0, Antigravity CLI, and Antigravity SDK as Google's agent-first development platform surfaces. Source: `raw/2026-06-11-web-google-developers-blog-all-the-news-from-the-google-i-o-2026-developer-keynote.md`. confidence: 1 Google source, last-confirmed 2026-06-11.
- Antigravity 2.0/CLI can spin up specialized subagents and includes built-in cross-platform terminal sandboxing, credential masking, and hardened Git policies. Source: `raw/2026-06-11-web-google-developers-blog-all-the-news-from-the-google-i-o-2026-developer-keynote.md`. confidence: 1 Google source, last-confirmed 2026-06-11.
- Managed Agents in the Gemini API provide a fully provisioned agent with a remote sandbox through a single API call, while Antigravity SDK gives programmatic control for self-hosting the harness. Source: `raw/2026-06-11-web-google-developers-blog-all-the-news-from-the-google-i-o-2026-developer-keynote.md`. confidence: 1 Google source, last-confirmed 2026-06-11.
- Google announced Android CLI, open-source Android skills, Android Bench, and a preview Android Studio migration agent that can migrate React Native, web-framework, or iOS app code toward native Kotlin Android. Source: `raw/2026-06-11-web-google-developers-blog-all-the-news-from-the-google-i-o-2026-developer-keynote.md`. confidence: 1 Google source, last-confirmed 2026-06-11.
- Google announced WebMCP, Modern Web Guidance, Chrome DevTools for agents, and HTML-in-Canvas as web-development surfaces for browser-based agents and accessible high-performance WebGL/WebGPU experiences. Source: `raw/2026-06-11-web-google-developers-blog-all-the-news-from-the-google-i-o-2026-developer-keynote.md`. confidence: 1 Google source, last-confirmed 2026-06-11.

### Typed entities
- model family: Gemini 3.5
- product: Google Antigravity 2.0
- CLI: Antigravity CLI
- SDK: Antigravity SDK
- feature/API: Gemini API Managed Agents
- tool: Android CLI
- benchmark: Android Bench
- proposed standard: WebMCP
- guidance package: Modern Web Guidance
- tool: Chrome DevTools for agents
- API: HTML-in-Canvas

### Explicit relationships
- Antigravity uses subagents, sandboxing, credential masking, and Git policy as harness controls.
- Managed Agents depend-on Google-provisioned remote sandboxes; Antigravity SDK enables self-hosted harness control.
- Android CLI and Android skills expose Android Studio heavy-lifting to arbitrary agents.
- WebMCP exposes web functions/forms as structured browser-agent tools.
- HTML-in-Canvas uses DOM integration inside canvas/WebGL/WebGPU experiences to preserve accessibility and interactivity.

### HoneyDrunk implications
- Watch Antigravity Managed Agents as a sandboxed managed-agent reference, but compare against OpenClaw's local repo access, audit, and provider-independence needs.
- For Android app work, benchmark Android CLI/skills and Android Bench before trusting migration-agent claims.
- Treat WebMCP and Chrome DevTools for agents as browser QA/prototyping signals that will need strict session, auth, and action consent controls.

### Quality notes
- This is a Google keynote recap. Feature availability, origin-trial behavior, and pricing should be verified before adoption.

## 2026-06-12 compile additions: DiffusionGemma

### Source-backed claims
- DiffusionGemma is an experimental Gemma 4-based text-generation architecture that uses diffusion-style parallel denoising over a 256-token canvas instead of pure left-to-right autoregressive generation. Source: `raw/2026-06-12-web-google-developers-blog-diffusiongemma-the-developer-guide-google-developers-bl.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-12.
- Google positions DiffusionGemma as a 26B Mixture of Experts model with 3.8B active parameters during inference, designed for quantized deployment within roughly 18 GB VRAM limits. Source: `raw/2026-06-12-web-google-developers-blog-diffusiongemma-the-developer-guide-google-developers-bl.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-12.
- DiffusionGemma combines block-autoregressive prefill/commit behavior with bidirectional denoising inside each 256-token block, enabling self-correction and better handling of constrained non-sequential problems in the cited Sudoku example. Source: `raw/2026-06-12-web-google-developers-blog-diffusiongemma-the-developer-guide-google-developers-bl.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-12.
- Google reports a Sudoku SFT recipe using Hackable Diffusion that raises the source's Sudoku task correctness from approximately 0% for the base model to 80% while reducing inference steps; this is a task-specific demo, not a general reasoning benchmark. Source: `raw/2026-06-12-web-google-developers-blog-diffusiongemma-the-developer-guide-google-developers-bl.md`. confidence: 1 vendor demo source, last-confirmed 2026-06-12.
- DiffusionGemma can be served through vLLM's OpenAI-compatible local server and has weights on Hugging Face under Apache 2.0, with support paths also named for Transformers, SGLang, MLX, Model Garden, and NVIDIA NIM. Source: `raw/2026-06-12-web-google-developers-blog-diffusiongemma-the-developer-guide-google-developers-bl.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-12.

### Typed entities
- model: DiffusionGemma
- model family: Gemma 4
- architecture: diffusion language model
- architecture: sparse Mixture of Experts
- inference engine: vLLM
- framework: Hugging Face Transformers
- framework: SGLang
- framework: MLX
- platform: Google Cloud Model Garden
- platform: NVIDIA NIM
- library/toolkit: Hackable Diffusion
- task: Sudoku solving

### Explicit relationships
- DiffusionGemma contradicts the assumption that developer text-generation models are necessarily token-by-token autoregressive systems.
- Block-autoregressive diffusion uses causal prefill for committed history and bidirectional denoising for the current canvas.
- vLLM integration makes DiffusionGemma usable through OpenAI-compatible serving surfaces despite the nonstandard generation loop.

### HoneyDrunk implications
- Add diffusion language models to the model-eval watchlist for constrained planning, puzzle-like validation, and local GPU inference experiments.
- Do not treat Sudoku gains as general coding-agent quality evidence; benchmark against HoneyDrunk tasks before routing any work to DiffusionGemma.
- If tested locally, capture VRAM, step count, latency, output quality, serving compatibility, and how tool-call/chat formatting behaves through vLLM.

### Quality notes
- Source is vendor-authored developer guidance. Architecture claims are useful; performance and task claims require reproduction.

## 2026-06-17 compile additions: Antigravity CLI transition and older Gemini API baseline

### Source-backed claims
- Google announced that Antigravity CLI is available as the successor terminal experience to Gemini CLI for many consumer/developer workflows, sharing the Antigravity 2.0 server-side harness and retaining critical Gemini CLI concepts such as Agent Skills, Hooks, Subagents, and Extensions as Antigravity plugins. Source: `raw/2026-06-17-web-developers-googleblog-com-an-important-update-transitioning-gemini-cli-to-antigravity-cli-google-developers.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-17.
- Google states that on 2026-06-18 Gemini CLI and Gemini Code Assist IDE extensions stop serving requests for Google AI Pro/Ultra users and free individual Gemini Code Assist users; Gemini Code Assist for GitHub will also stop accepting new GitHub organization installations on that date and requests will stop in following weeks. Source: `raw/2026-06-17-web-developers-googleblog-com-an-important-update-transitioning-gemini-cli-to-antigravity-cli-google-developers.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-17.
- Enterprise customers using Gemini CLI or IDE extensions through Gemini Code Assist Standard/Enterprise or Gemini Code Assist for GitHub through Google Cloud remain supported, and Gemini CLI remains accessible through paid Gemini and Gemini Enterprise Agent Platform API keys. Source: `raw/2026-06-17-web-developers-googleblog-com-an-important-update-transitioning-gemini-cli-to-antigravity-cli-google-developers.md`. confidence: 1 source, last-confirmed 2026-06-17.
- The 2025 Gemini API I/O update is now historical baseline rather than latest model guidance: it introduced 2.5-era thought summaries, thinking budgets, URL Context, browser computer-use tooling, broader JSON Schema support, async Live API function calling, and Batch API plans. Source: `raw/2026-06-17-web-developers-googleblog-com-gemini-api-i-o-updates-google-developers-blog.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-17.
- Later 2026 Lore evidence supersedes the 2025 source for model-routing decisions because the wiki already has newer Gemini 3.5, Antigravity, Gemma 4, and DiffusionGemma sources. Superseded-by: 2026-06-17 - newer Google platform/model pages are more authoritative for current model selection; retain the 2025 source only for API primitive history. Source: `raw/2026-06-17-web-developers-googleblog-com-gemini-api-i-o-updates-google-developers-blog.md`; pages: [[google-agent-platform-and-gemini-api-2026]], [[edge-ai-and-ai-infrastructure-2026]]. confidence: 1 source plus compile reconciliation, last-confirmed 2026-06-17.

### Typed entities
- product: Google Antigravity 2.0
- CLI: Antigravity CLI
- CLI: Gemini CLI
- product: Gemini Code Assist
- feature: Agent Skills
- feature: Hooks
- feature: Subagents
- feature: Antigravity plugins
- API feature: Gemini thought summaries
- API feature: thinking budgets
- tool: URL Context
- tool: computer use
- API: Gemini Live API
- API: Batch API

### Explicit relationships
- Antigravity CLI supersedes Gemini CLI for affected consumer/free/Pro/Ultra workflows after 2026-06-18.
- Antigravity CLI shares a harness with Antigravity 2.0, reducing split-brain behavior across desktop and terminal agent surfaces.
- Gemini CLI enterprise access depends-on paid licenses or Gemini Enterprise Agent Platform API keys.
- Gemini 2.5-era model claims are superseded for routing decisions by later Gemini 3.5/Gemma/DiffusionGemma sources in Lore.
- URL Context and computer-use tools complement agent research/browser workflows but require untrusted-content and action-consent controls.

### HoneyDrunk implications
- Inventory any Gemini CLI, Gemini Code Assist individual, or Gemini Code Assist for GitHub usage immediately because the consumer cutoff is 2026-06-18.
- If Antigravity CLI is tested, evaluate background/asynchronous workflows, plugin provenance, credential masking, sandboxing, and whether logs/artifacts are inspectable.
- Keep older Gemini 2.5 claims out of current model-routing decisions unless revalidated; use them only as API-surface history.

### Quality notes
- Google sources are authoritative for Google product transition dates and feature positioning. Model/API availability remains time-sensitive and should be checked before implementation.
