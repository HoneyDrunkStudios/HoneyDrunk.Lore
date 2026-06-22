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

## 2026-06-04 compile additions

### Claims
- Microsoft Foundry extends tracing and evaluations to agents built on LangChain, LangGraph, OpenAI SDK, Microsoft Agent Framework, or custom frameworks through OpenTelemetry, so tool calls, LLM invocations, and handoffs can land in one trace view. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-2026-from-observability-to-roi-for-ai-age.md]
- Foundry's Azure Developer CLI observability experience brings tracing, logging, and evaluation insights into `azd`, terminal, and VS Code workflows for hosted agents. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-2026-from-observability-to-roi-for-ai-age.md]
- Intelligent trace sampling runs evaluations against a curated sample of live production traces instead of every trace, balancing continuous quality monitoring against evaluation cost. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-microsoft-foundry-blog-build-2026-from-observability-to-roi-for-ai-age.md]

### Typed entities
- framework: LangGraph
- SDK: OpenAI SDK
- framework: Microsoft Agent Framework
- product: Microsoft Foundry observability
- tool: Azure Developer CLI / `azd`
- control: intelligent trace sampling
- feature: trace replay
- feature: traces to dataset

### Explicit relationships
- Foundry observability uses OpenTelemetry as the common trace language across agent frameworks.
- Evaluation sampling depends-on trace filtering so production quality checks do not require evaluating every request.
- Trace replay complements ordinary logs by showing prompt, decision, tool call, and model output sequence.

### HoneyDrunk implications
- Keep OpenClaw traces framework-neutral where possible; emit OTel spans for model calls, tool calls, handoffs, retries, and long waits.
- Add sampling rules before high-volume agent deployment; "evaluate everything" will become a cost and privacy problem.
- Use traces-to-dataset only after redaction rules are in place, because production traces may contain private prompt/tool content.

## 2026-06-08 compile additions

### Claims
- GitHub Copilot SDK GA includes OpenTelemetry tracing with W3C trace-context propagation across CLI startup, JSON-RPC calls, session operations, and tool execution. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-copilot-sdk-is-now-generally-available.md]
- The OWASP Agent Observability Standard MCP extension proposes inspecting MCP requests and responses through guardian-agent decisions before continuing tool/model flow, which is adjacent to observability because the security decision point sees the same tool-call sequence that traces should record. confidence: 1 OWASP AOS source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-instrument-mcp-agent-observability-standard.md]
- VS Code Copilot May updates include richer agent terminal/run UX and session sync/history, reinforcing that agent observability includes local IDE/client state as well as backend traces. confidence: 1 GitHub changelog source, last-confirmed 2026-06-08. [source: raw/2026-06-08-web-github-copilot-in-visual-studio-code-may-releases.md]

### Typed entities
- SDK: GitHub Copilot SDK
- standard: W3C Trace Context
- protocol/API: JSON-RPC
- standard: OWASP Agent Observability Standard / AOS
- protocol: Model Context Protocol
- concept: guardian-agent decision
- surface: VS Code Agents window
- feature: session sync

### Explicit relationships
- Copilot SDK uses W3C trace context to connect CLI/session/tool execution spans.
- Guardian-agent mediation complements OTel tracing by adding policy decisions to the tool-call control path.
- Agent observability depends-on client/session state as well as model/tool spans when agents run across IDE, CLI, cloud, and desktop-app surfaces.

### HoneyDrunk implications
- For OpenClaw/Grid, capture both execution telemetry and policy decisions: tool requested, policy result, modified arguments if safe to log, execution result, and verification outcome.
- Keep prompt/tool content redaction aligned with policy logs; a denied exfiltration-like call can still leak data if logged verbatim.

### Quality notes
- GitHub is authoritative for SDK capability. AOS is an OWASP standard source but should be evaluated for implementation maturity and compatibility with existing OTel pipelines.

## 2026-06-09 compile additions

### Claims
- Datadog argues feature-flag rollout decisions need a unified data model that correlates flag state, error rates, traces, session replay, funnel/product data, warehouse metrics, data-quality signals, and LLM evaluation scores without exports or tab switching. confidence: 1 Datadog source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-how-a-unified-data-model-improves-feature-flag-rollout-decisions-datad.md]
- The same source frames fragmented integrations as particularly risky for agentic release workflows because agents lack human judgment for navigating disconnected tabs, ownership, and implicit context. confidence: 1 Datadog source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-how-a-unified-data-model-improves-feature-flag-rollout-decisions-datad.md]
- Datadog's agentic release example uses MCP to let an agent correlate a treatment-group error spike with flag exposure data, traces, Android version, warehouse segment size, and Slack reporting before holding part of a rollout. confidence: 1 source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-how-a-unified-data-model-improves-feature-flag-rollout-decisions-datad.md; page: [[mcp-tool-governance-and-app-surfaces]]]

### Typed entities
- product: Datadog Feature Flags
- product: Datadog Experiments
- product: Datadog Product Analytics
- product: Datadog Session Replay
- product: Datadog MCP Server
- standard: OpenFeature SDK
- concept: warehouse-native experimentation
- metric/context: flag exposure data
- metric/context: LLM evaluation score

### Explicit relationships
- Feature-flag observability depends-on release state, product signals, infrastructure traces, and business metrics sharing identifiers/data model.
- Agentic rollout decisions depend-on complete correlated context because missing telemetry or disconnected ownership can cause unsafe automated action.
- OpenFeature and warehouse-native experimentation complement platform observability by preserving code/data portability.

### HoneyDrunk implications
- Do not allow unattended release/rollout agents until traces, feature exposure, user segment impact, rollback, and notification paths are available as governed tool calls.
- Keep product analytics and LLM eval metrics linkable to trace IDs or release/flag IDs where possible; otherwise agent decisions will be hard to audit.

### Quality notes
- Datadog source is vendor-authored and product-positioned, but the unified-data-model requirement is decision-useful for any agentic release workflow.

## 2026-06-11 compile additions: App Service agent views and Codex telemetry

### Source-backed claims
- Azure App Service's AI preview Agents tab reads Application Insights telemetry from apps that emit OpenTelemetry GenAI semantic conventions, grouping on `gen_ai.agent.name`, `gen_ai.agent.id`, and `gen_ai.usage.*`. Source: `raw/2026-06-11-web-microsoft-learn-build-agentic-web-applications-in-azure-app-service-azure-app-service.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-11.
- Microsoft's .NET multi-agent monitoring tutorial shows Microsoft Agent Framework agents wrapped with `UseOpenTelemetry`, Azure Monitor OpenTelemetry distro export, and Application Insights drilldowns for agent runs, tool calls, token consumption, and GenAI errors. Source: `raw/2026-06-11-web-microsoft-learn-monitor-a-multi-agent-app-with-opentelemetry-and-application-insights-ne.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-11.
- The tutorial explicitly warns that `EnableSensitiveData = true` includes message content in spans, is off by default, and should be disabled or controlled through `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT` in production. Source: `raw/2026-06-11-web-microsoft-learn-monitor-a-multi-agent-app-with-opentelemetry-and-application-insights-ne.md`. confidence: 1 Microsoft Learn source, last-confirmed 2026-06-11.
- OpenAI says Codex supports OpenTelemetry log export for events such as user prompts, tool approval decisions, tool execution results, MCP server usage, and network proxy allow/deny events; Codex activity logs also flow through OpenAI's Compliance Platform for Enterprise/Edu customers. Source: `raw/2026-06-11-web-openai-running-codex-safely-at-openai.md`. confidence: 1 official OpenAI source, last-confirmed 2026-06-11.

### Typed entities
- product: Azure App Service AI Agents tab
- product: Application Insights Agents preview
- package: Azure Monitor OpenTelemetry distro
- method: `UseOpenTelemetry`
- environment variable: `OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT`
- product: OpenAI Codex
- product: OpenAI Compliance Platform
- signal: tool approval decision log
- signal: network proxy allow/deny event

### Explicit relationships
- Application Insights agent views depend-on OpenTelemetry GenAI semantic attributes emitted by application code.
- Message-content capture improves debugging but contradicts privacy-by-default operation unless explicitly approved and redacted.
- Codex telemetry complements endpoint/process logs by exposing user/agent intent, approvals, MCP usage, and network policy decisions.

### HoneyDrunk implications
- For OpenClaw/Grid telemetry, capture both execution spans and policy decisions: tool requested, approval result, network allow/deny, and verification outcome.
- Keep prompt/message/tool-result content capture off by default; allow only local or explicitly approved debugging with retention limits.
- Use GenAI attributes consistently so local dashboards and cloud views can group by agent, model, tool, token usage, and errors.

### Quality notes
- Microsoft and OpenAI sources are authoritative for their own products. Exact attribute names and SDK hooks should still be pinned to package versions before implementation.

## 2026-06-17 compile additions: agentic system observability at scale

### Source-backed claims
- Microsoft's dynamic agents-at-scale pattern uses OpenTelemetry instrumentation, an OpenTelemetry Collector, Application Insights, Azure Monitor, and Log Analytics to correlate orchestrator, agent, model, semantic-cache, and external-call behavior across one conversation trace. Source: `raw/2026-06-17-web-learn-microsoft-com-dynamic-ai-agents-at-scale-pattern-azure-architecture-center.md`. confidence: 1 Microsoft Architecture Center source, last-confirmed 2026-06-17.
- The same source distinguishes ordinary system observability from agentic application observability: teams need to know which agent responded slowly, what sequence of calls led to poor output, which model parameters/prompts were active, and where coordination failed. Source: `raw/2026-06-17-web-learn-microsoft-com-dynamic-ai-agents-at-scale-pattern-azure-architecture-center.md`. confidence: 1 source, last-confirmed 2026-06-17.
- Microsoft recommends tracking system performance, LLM inference performance, usage/engagement, and quality/model-accuracy metrics, including latency, throughput, TTFT, token usage, content-safety triggers, active conversations, intent selection accuracy, instruction adherence, groundedness, and bias. Source: `raw/2026-06-17-web-learn-microsoft-com-dynamic-ai-agents-at-scale-pattern-azure-architecture-center.md`. confidence: 1 source, last-confirmed 2026-06-17.
- The dynamic agents-at-scale source says observability can include system prompts, model parameters, user inputs, conversation history, and outputs for reproducibility, but also lists secure data handling and masking/omission of sensitive information as a best practice. Source: `raw/2026-06-17-web-learn-microsoft-com-dynamic-ai-agents-at-scale-pattern-azure-architecture-center.md`. confidence: 1 source, last-confirmed 2026-06-17.

### Typed entities
- service: Application Insights
- service: Azure Monitor
- service: Log Analytics
- component: OpenTelemetry Collector
- protocol: OTLP
- metric: time to first token / TTFT
- metric: intent selection accuracy
- concept: semantic observability
- concept: behavioral observability
- control: telemetry sampling
- control: sensitive-data masking

### Explicit relationships
- Agentic observability extends logs, metrics, and traces with semantic/behavioral signals about prompts, tools, agent selection, and collaboration.
- Trace IDs and span IDs connect orchestrators, agents, caches, models, and external tools into one conversation path.
- Reproducibility depends-on capturing enough prompt/model/context metadata, while privacy depends-on masking, omission, sampling, and retention controls.
- Agent selector evaluation complements observability because production traces alone do not prove that the right agent should have been selected.

### HoneyDrunk implications
- For OpenClaw/Honeyclaw, log enough structure to reconstruct agent routing, tool calls, model IDs, token usage, approval outcomes, and verification results.
- Keep prompt/user-input/output capture behind explicit debug or evaluation modes with retention limits; default telemetry should favor metadata over raw sensitive content.
- Add agent-selection metrics if HoneyDrunk adopts dynamic routing: invoke accuracy, selector precision/recall, and "direct invoke vs orchestrator path" counts.

### Quality notes
- Microsoft source is architecture guidance and Azure-centered. The telemetry categories are broadly useful; product-specific dashboards should not drive HoneyDrunk architecture unless local needs justify Azure Monitor/Application Insights.

## 2026-06-22 compile additions: OTAP/Arrow dataflow for high-volume telemetry

### Source-backed claims
- OpenTelemetry Arrow Phase 2 positions OTAP/Arrow as more than a wire transport: Arrow becomes an in-pipeline columnar representation inside a Rust Dataflow Engine with batched telemetry, bounded channels, backpressure, shared-nothing thread-per-core execution, and live reconfiguration. Source: `raw/2026-06-22-rss-opentelemetry-io-otel-arrow-phase-2-from-efficient-transport-to-effici.md`. confidence: 1 official OpenTelemetry source, last-confirmed 2026-06-22.
- The source reports benchmark examples where rule-processing CPU stayed near flat under high log volume compared with a much higher Collector OTLP path, and it reports 10-20x throughput gains for OTAP over OTLP in the same runtime; treat those as source benchmark snapshots, not HoneyDrunk capacity evidence. Source: `raw/2026-06-22-rss-opentelemetry-io-otel-arrow-phase-2-from-efficient-transport-to-effici.md`. confidence: 1 official source, last-confirmed 2026-06-22.
- The Dataflow Engine is described as incubation-stage, so the strategic signal is future high-volume telemetry architecture rather than an immediate production default. Source: `raw/2026-06-22-rss-opentelemetry-io-otel-arrow-phase-2-from-efficient-transport-to-effici.md`. confidence: 1 official source, last-confirmed 2026-06-22.

### Typed entities
- protocol/project: OpenTelemetry Arrow / OTAP
- data format: Apache Arrow
- component: Rust Dataflow Engine
- concept: columnar telemetry
- control: bounded channel
- control: backpressure
- execution model: thread-per-core shared-nothing
- protocol: OTLP

### Explicit relationships
- OTAP/Arrow complements OTLP by optimizing high-volume telemetry transport and in-pipeline processing.
- Columnar batched telemetry can reduce repeated parsing/allocation work compared with row-oriented processing.
- Backpressure and bounded channels complement telemetry reliability by making overload behavior explicit.
- Incubation status means OTAP/Arrow does not supersede stable Collector pipelines yet.

### HoneyDrunk implications
- Keep OTAP/Arrow on the watchlist for high-volume agent traces, logs, and event streams, especially if OpenClaw/Grid telemetry volume outgrows simple Collector pipelines.
- Do not adopt incubation telemetry infrastructure without local load tests, fallback path, operational ownership, and privacy/redaction parity.

### Quality notes
- Official OpenTelemetry source. Benchmark numbers are useful directional evidence but require local reproduction on HoneyDrunk trace/log shapes.
