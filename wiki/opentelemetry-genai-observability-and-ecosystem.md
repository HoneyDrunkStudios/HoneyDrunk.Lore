# OpenTelemetry GenAI Observability and Ecosystem Mapping

## Decision-useful summary
OpenTelemetry is becoming the practical neutral observability layer for LLM/agent systems. The GenAI semantic conventions standardize traces, metrics, events, token usage, model names, tool calls, and optionally prompt/response/tool content; the Ecosystem Explorer maps what instrumentation emits before teams deploy it. For HoneyDrunk, this supports local agent debugging and cost/latency analysis, but content capture must remain opt-in and privacy-filtered. [sources: raw/2026-05-18-rss-opentelemetry-blog-inside-the-llm-call-genai-observability-with-opente.md; raw/2026-05-18-rss-opentelemetry-blog-introducing-the-ecosystem-explorer-project.md]

## Claims
- OpenTelemetry GenAI semantic conventions record LLM operations with attributes such as model name, input/output token counts, finish reasons, and when explicitly opted in, full prompts, completions, tool calls, tool schemas, arguments, and tool results. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-opentelemetry-blog-inside-the-llm-call-genai-observability-with-opente.md]
- VS Code Copilot, OpenAI Codex, and Claude Code are described as emitting OpenTelemetry-compatible GenAI telemetry surfaces: Copilot emits traces/metrics/events, Codex exports structured log events and OTel metrics, and Claude Code exports metrics/log events with trace support in beta. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-opentelemetry-blog-inside-the-llm-call-genai-observability-with-opente.md]
- GenAI content capture is disabled by default in the Copilot example because prompts, tool arguments, and tool results can contain sensitive data; enabling it improves debugging but increases privacy and storage risk. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-opentelemetry-blog-inside-the-llm-call-genai-observability-with-opente.md]
- Aspire Dashboard can receive local OTLP telemetry and visualize traces, metrics, and structured logs for GenAI workloads without requiring a cloud telemetry account. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-opentelemetry-blog-inside-the-llm-call-genai-observability-with-opente.md]
- OpenTelemetry's Ecosystem Explorer is live as a work-in-progress site; it maps Java agent instrumentation first, indexing 240+ Java auto-instrumentations with spans, metrics, attributes, configuration options, and version-change data. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-opentelemetry-blog-introducing-the-ecosystem-explorer-project.md]
- Ecosystem Explorer expansion priorities include Collector components, Java extensions/native instrumentation, Python and JavaScript instrumentation packages, and GenAI/LLM framework telemetry from frameworks such as LangChain, LlamaIndex, OpenAI clients, and Anthropic clients. confidence: 1 source, last-confirmed 2026-05-18. [source: raw/2026-05-18-rss-opentelemetry-blog-introducing-the-ecosystem-explorer-project.md]

## Typed entities
- standard: OpenTelemetry Semantic Conventions for Generative AI
- project: OpenTelemetry Ecosystem Explorer
- site: explorer.opentelemetry.io
- tool: VS Code Copilot
- tool: OpenAI Codex
- tool: Claude Code
- tool: Aspire Dashboard
- protocol: OTLP
- signal: trace
- signal: metric
- signal: structured log event
- attribute: gen_ai.request.model
- attribute: gen_ai.usage.input_tokens
- attribute: gen_ai.usage.output_tokens
- attribute: gen_ai.response.finish_reasons
- library/framework: LangChain
- library/framework: LlamaIndex
- client/library: OpenAI client
- client/library: Anthropic client
- concept: GenAI observability
- concept: content capture privacy risk

## Explicit relationships
- GenAI observability uses OpenTelemetry semantic conventions to make model calls, token usage, tool calls, and retries inspectable.
- Agent harnesses depend-on telemetry to debug latency, cost, retry loops, and tool behavior.
- Full prompt/tool content capture contradicts privacy-by-default operation unless explicitly enabled for safe local debugging.
- Aspire Dashboard uses OTLP to receive local telemetry and visualize traces/metrics/logs.
- Ecosystem Explorer complements the OpenTelemetry Registry by mapping emitted telemetry and version changes, not only component discovery.
- GenAI framework instrumentation depends-on semantic convention adoption and ecosystem mapping before teams can compare emitted signals reliably.

## HoneyDrunk implications
- Add OTel/GenAI telemetry as a first-class harness concern for OpenClaw/Grid agents: trace model calls, tool calls, retries, token cost, and long waits.
- Keep prompt/tool-result content capture off by default; enable only in local/private debugging sessions with redaction and retention limits.
- Use Aspire Dashboard or equivalent local OTLP tooling for agent debugging before sending sensitive telemetry to cloud observability backends.
- Track Ecosystem Explorer maturity for .NET, Collector, JavaScript, Python, and GenAI instrumentation when choosing observability libraries.

## Confidence and quality notes
- Quality posture: decision-usable for observability architecture. Sources are official OpenTelemetry blog posts; still validate exact tool flags and schema versions against current docs before implementation.
- Privacy filter: raw command examples retained only as public local-dev guidance; no prompts, tokens, DSNs, or private telemetry copied.
