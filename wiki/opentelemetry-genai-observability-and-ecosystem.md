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

## 2026-05-19 compile additions

### Claims
- OpenTelemetry Blueprints and Reference Implementations are an End User SIG + Developer Experience SIG initiative to provide prescriptive, opinionated adoption guidance without replacing component-level docs. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-opentelemetry-blog-introducing-otel-blueprints-and-reference-implement.md]
- The OTel blueprint structure is intended to include Summary, Common Challenges, General Guidelines, and Implementation sections, scoping only the observability problems in scope and pointing to existing docs for component-level steps. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-opentelemetry-blog-introducing-otel-blueprints-and-reference-implement.md]
- Initial blueprint focus areas include non-Kubernetes infrastructure/process instrumentation, Kubernetes observability, and centralized telemetry platforms; blueprints can relate, overlap, or extend each other. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-opentelemetry-blog-introducing-otel-blueprints-and-reference-implement.md]
- Reference implementations are snapshots of real-world OpenTelemetry adoption that implement one or more blueprints; Adobe, Mastodon, and Skyscanner are cited as already-published examples. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-opentelemetry-blog-introducing-otel-blueprints-and-reference-implement.md]
- The source explicitly warns that AI-assisted development can increase accidental OTel complexity by adding duplicated or inconsistent configuration/deployment patterns unless teams share a strategy. confidence: 1 source, last-confirmed 2026-05-19. [source: raw/2026-05-19-rss-opentelemetry-blog-introducing-otel-blueprints-and-reference-implement.md]

### Typed entities
- project: OpenTelemetry Blueprints
- project: OpenTelemetry Reference Implementations
- SIG: OpenTelemetry End User SIG
- SIG: OpenTelemetry Developer Experience SIG
- organization/reference implementer: Adobe
- organization/reference implementer: Mastodon
- organization/reference implementer: Skyscanner
- concept: essential complexity
- concept: accidental complexity
- pattern: centralized telemetry platform
- pattern: Kubernetes observability
- pattern: non-Kubernetes infrastructure instrumentation

### Explicit relationships
- OTel Blueprints complement, not supersede, existing OpenTelemetry component documentation.
- Reference Implementations implement one or more Blueprints and ground prescriptive guidance in real deployments.
- AI-assisted configuration can cause accidental OTel complexity unless observability strategy is shared and enforced.

### HoneyDrunk implications
- For OpenClaw/Grid observability, write an internal “HoneyDrunk OTel blueprint” before allowing agents to add telemetry config piecemeal.
- Prefer one shared collector/exporter/context-propagation pattern per environment; duplicated agent-added variants should be linted out.

## 2026-05-20 compile additions

### Claims
- In legacy/industrial environments, OpenTelemetry security controls often shift from source instrumentation to Collector/intermediary placement because source systems may not support modern agents, TLS/auth, or regular patching. confidence: 1 official OTel blog source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-opentelemetry-blog-applying-opentelemetry-security-practices-in-legacy.md]
- The OTel legacy-environment guidance prefers running the Collector as an external bridge where possible, so the telemetry boundary can be patched independently of long-lived or change-restricted systems. confidence: 1 official OTel blog source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-opentelemetry-blog-applying-opentelemetry-security-practices-in-legacy.md]
- Sensitive operational telemetry in manufacturing/legacy environments can include production processes, machine configuration, asset identifiers, operational states, and plant-level performance data; it is not limited to typical PII. confidence: 1 official OTel blog source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-opentelemetry-blog-applying-opentelemetry-security-practices-in-legacy.md]

### Typed entities
- component: OpenTelemetry Collector
- pattern: external Collector bridge
- environment type: legacy industrial system
- concept: telemetry pipeline as control boundary
- control: bind Collector endpoints narrowly
- control: data minimization
- control: redaction/filter/transform processors
- concept: sensitive operational data

### Explicit relationships
- OpenTelemetry Collector placement depends-on legacy system modifiability, network segmentation, and patching constraints.
- External Collector bridge supersedes embedded Collector deployment as the preferred pattern when legacy systems cannot be patched quickly.
- Sensitive operational data contradicts a PII-only privacy model for telemetry.

### HoneyDrunk implications
- For any agent/device/industrial-adjacent telemetry, classify operational sensitivity explicitly before exporting traces/logs.
- Treat Collector placement and endpoint binding as architecture decisions, not default config; weak segmentation makes Collector exposure more important.

## 2026-05-22 compile additions

### Claims
- OpenTelemetry graduated from CNCF incubation to a CNCF Graduated Project on 2026-05-21. confidence: 1 official source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-opentelemetry-blog-opentelemetry-is-a-cncf-graduated-project.md]
- The graduation announcement frames OpenTelemetry as an open, vendor-neutral observability framework created from OpenTracing/OpenCensus and supported by thousands of contributors, maintainers, end users, and organizations. confidence: 1 official source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-opentelemetry-blog-opentelemetry-is-a-cncf-graduated-project.md]
- Graduation is a governance/ecosystem maturity signal, not a claim that GenAI semantic conventions or every instrumentation package are final/stable. confidence: 1 official source plus compile judgment, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-opentelemetry-blog-opentelemetry-is-a-cncf-graduated-project.md]

### Typed entities
- project: OpenTelemetry
- foundation: CNCF
- lifecycle state: CNCF Graduated Project
- predecessor project: OpenTracing
- predecessor project: OpenCensus

### Explicit relationships
- OpenTelemetry graduation reinforces vendor-neutral observability as a strategic dependency for agent/runtime telemetry.
- CNCF graduation strengthens ecosystem-confidence posture but does not supersede schema/version validation for specific GenAI instrumentation.

### HoneyDrunk implications
- Treat OTel as the default neutral observability vocabulary for OpenClaw/Grid agents unless a concrete constraint says otherwise.
- Continue pinning semantic-convention and SDK versions; project graduation is not a license for unversioned telemetry assumptions.

## 2026-05-26 compile additions

### Claims
- CNCF TAG guidance frames ingress request tracing for multi-tenant SaaS as a product/platform capability built around generate-or-preserve Trace IDs, per-service Span IDs, parent-child span relationships, and W3C Trace Context propagation. confidence: 1 CNCF source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-devops-designing-end-to-end-ingress-request-tracing-for-multi-ten.md]
- The framework explicitly excludes request payloads, credentials, secrets, tokens, and PII from trace metadata; it recommends operational metadata only: trace/span/parent IDs, service and operation names, timestamps, duration, status, and HTTP code. confidence: 1 CNCF source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-devops-designing-end-to-end-ingress-request-tracing-for-multi-ten.md]
- Trace export should be configuration-only through Kubernetes/operator workflows, and telemetry backend failures must not block customer requests; partial/dropped traces are acceptable while failed requests are not. confidence: 1 CNCF source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-devops-designing-end-to-end-ingress-request-tracing-for-multi-ten.md]
- The hardest part of distributed tracing adoption is complete coverage: if some services fail to propagate context, traces become operationally unreliable; the source recommends CI/CD checks, service onboarding checklists, and adoption tracking. confidence: 1 CNCF source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-devops-designing-end-to-end-ingress-request-tracing-for-multi-ten.md]

### Typed entities
- standard: W3C Trace Context
- header: `traceparent`
- header: `tracestate`
- identifier: Trace ID
- identifier: Span ID
- identifier: Parent Span ID
- platform: Kubernetes
- concept: multi-tenant SaaS ingress tracing
- control: configuration-only telemetry export
- control: non-disruptive tracing failure mode
- control: tracing adoption CI/CD checks

### Explicit relationships
- OpenTelemetry uses W3C Trace Context to propagate trace/span relationships across service boundaries.
- SaaS incident response depends-on trace continuity across ingress, auth, orchestration, data, and downstream services.
- Trace metadata privacy depends-on excluding payloads, credentials, tokens, secrets, and PII by design.
- Complete distributed tracing depends-on organizational enforcement, not only instrumentation libraries.

### HoneyDrunk implications
- For Grid/OpenClaw services, standardize trace headers and response-header lookup keys early; debugging multi-agent requests without stable trace IDs will not scale.
- Add "telemetry must not break requests" and "no payload/secrets in traces by default" as acceptance criteria for any HoneyDrunk tracing rollout.

## 2026-05-31 compile additions

### Claims
- Skyscanner runs over 1,000 microservices across 24 production Kubernetes clusters and manages most OpenTelemetry Collector work with a six-person platform/Hubble team, demonstrating that centralized collector ownership can scale when service teams get strong defaults. confidence: 1 official OpenTelemetry case-study source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-opentelemetry-blog-how-skyscanner-scales-opentelemetry-managing-collec.md]
- Skyscanner uses a central telemetry DNS endpoint with Istio routing to the nearest gateway collector, plus two collector patterns: gateway collectors for bulk OTLP traces/metrics and daemonset agent collectors for Prometheus scraping of platform services. confidence: 1 official OpenTelemetry case-study source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-opentelemetry-blog-how-skyscanner-scales-opentelemetry-managing-collec.md]
- Skyscanner generates platform HTTP/gRPC metrics from Istio service-mesh spans through the span metrics connector, avoiding higher-cardinality native Istio metrics and providing metrics for services without code instrumentation. confidence: 1 official OpenTelemetry case-study source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-opentelemetry-blog-how-skyscanner-scales-opentelemetry-managing-collec.md]
- Skyscanner disables most OpenTelemetry Java auto-instrumentations by default in a shared Java base image, then enables a curated set and allows service teams to opt into more; this provides consistency without forcing every service owner to understand all OTel internals. confidence: 1 official OpenTelemetry case-study source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-opentelemetry-blog-how-skyscanner-scales-opentelemetry-managing-collec.md]
- Skyscanner uses SDK views to drop HTTP/RPC metrics while preserving spans when service-mesh metrics already cover the platform view; individual services can selectively keep/rename app-specific metrics to avoid duplicate counting. confidence: 1 official OpenTelemetry case-study source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-opentelemetry-blog-how-skyscanner-scales-opentelemetry-managing-collec.md]
- The Skyscanner case study recommends starting collectors simply with memory limiter, batch processor, and exporter; adding filter processors early for high-volume false-positive errors; and progressively promoting collector changes across cluster tiers. confidence: 1 official OpenTelemetry case-study source, last-confirmed 2026-05-31. [source: raw/2026-05-31-rss-opentelemetry-blog-how-skyscanner-scales-opentelemetry-managing-collec.md]

### Typed entities
- organization: Skyscanner
- team: Hubble platform team
- component: OpenTelemetry Collector
- deployment pattern: gateway collector ReplicaSet
- deployment pattern: agent collector DaemonSet
- service mesh: Istio
- connector: span metrics connector
- instrumentation: OpenTelemetry Java agent
- control: SDK view file
- control: filter processor
- deployment tool: Argo CD

### Explicit relationships
- Platform-managed base images and wrapper libraries make OpenTelemetry adoption easier for service teams.
- Istio spans can be transformed into lower-cardinality platform metrics when direct SDK metrics would duplicate or overload telemetry.
- SDK metric views complement tracing by dropping selected metric aggregations without disabling span instrumentation.
- Collector configuration quality depends-on progressive rollout because central collector mistakes affect many services.

### HoneyDrunk implications
- For Grid/OpenClaw, define one shared OTel base/wrapper pattern before service-by-service agent-added instrumentation spreads.
- Avoid duplicate HTTP/RPC metrics if a gateway/service-mesh layer already provides platform latency metrics; preserve traces for debugging.
- Add filter processors for expected non-error statuses early to avoid noisy sampling/cost surprises.
