---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/we-built-ai-control-plane-reduce-LLM-expenses-prevent-data-leaks"
title: "We built an AI control plane to reduce LLM expenses and prevent data leaks"
author: "Rahit Kar; Camila Oliveira; Anshul Kumar"
date_published: "2026-11-10"
date_clipped: "2026-11-11"
category: "Software Architecture"
source_type: "rss"
---

# We built an AI control plane to reduce LLM expenses and prevent data leaks

How an engineering-first governance gateway stops runaway token billing and blocks credential leaks without degrading developer velocity.

## Recognizing the AI control gap

With major LLM providers transitioning from subscription-based models to [token-based pricing](https://www.thoughtworks.com/insights/blog/generative-ai/dangers-token-usage-billing), controlling token usage instantly became a paramount concern for teams leveraging AI at scale.

As Thoughtworkers, AI-assisted development tools are integrated into our daily workflows. Following this pricing model evolution, actively monitoring and managing developer token consumption across various IDEs and utility tools became essential. However, scaling AI adoption quickly revealed a structural challenge: without centralized routing, every prompt, ranging from simple queries like "what is HTTP 429?" to complex tasks like "refactor this system”, defaulted to the highest-tier, most expensive models at uniform per-token rates.

Beyond financial inefficiency, unchecked AI access introduces serious security and data-privacy vulnerabilities. Without audit trails or protective filters, prompts often expose sensitive corporate IP, personal data (PII) and API credentials to external servers, putting organizations and clients at risk.

As part of our goals around innovation, Thoughtworks recently held an internal event, the AI/works Global Hackathon. Our entry in that event — a tool we called **Heimdall** — was designed to tackle these challenges.

## What Heimdall does

Heimdall acts as a control plane and proxy gateway operating seamlessly between client applications, IDE extensions, or agentic frameworks and downstream LLM providers.

It intercepts incoming API calls and directs them through a modular, six-stage pipeline styled after Norse mythological entities ("the Guardians"):

1. **Bifrost (proxy gateway):** Serves an OpenAI-compatible API endpoint. Integration requires changing a base URL string without installing custom SDKs.
2. **Gjallarhorn (PII scrubber/IP protection):** Combines Microsoft Presidio, spaCy NER, and custom regex recognizers to detect and redact sensitive PII (names, emails) or credentials prior to external outbound transmission. Configured as a fail-closed mechanism: if scrubbing encounters an error, the request is halted immediately.
3. **Mimir's Well (semantic cache):** Serves cached responses for semantically identical or equivalent prompts, before they hit external providers, serving instant cached responses at zero token cost.
4. **The Norns (complexity router):** Evaluates prompt complexity dynamically to direct traffic to the most cost-effective capable model. This ranges from on-premise local Ollama models (0)→Haiku(1/M) to tier-one cloud models like Claude Sonnet (3/M)→Opus(5/M).
5. **Wall of Asgard (budget guard):** Enforces per-team, per-model, and per-period token spending thresholds. Instead of abruptly terminating developer queries when a tier's budget is reached, it implements an automated, graceful degradation ladder (Opus → Sonnet → Haiku → Local).

- **Himinbjorg (observability):** Utilizes [OpenTelemetry](https://www.thoughtworks.com/radar/languages-and-frameworks/opentelemetry) integration with platforms like New Relic to deliver fine-grained telemetry spanning cost, latency, cache hit rates, model routing decisions, and PII filtration events.

### Low latency by design

Security and routing guardrails often suffer from latency bloat. Heimdall overcomes this by executing complexity scoring and PII sanitization in parallel via asynchronous workers. The total processing overhead is approximately 14ms, virtually imperceptible when downstream LLM calls take anywhere from two to 15 seconds.

## How Heimdall saves every token it can

Before a single request reaches a cloud LLM, each request passes through multiple cost-defense layers:

- **Avoid the call entirely.**Semantic cache returns previous answers instantly. Simple queries (score < 0.30) route to a local LLM at $0. Smart cache keys strip IDE noise (file paths, cursor positions) to dramatically boost hit rates.

- **Pick the right-sized model.**Complexity routing matches the model to the task. Budget degradation shifts to cheaper models instead of failing. Opus requests auto-degrade to Sonnet as a runaway cost guard.

- **Make each call cheaper.** Anthropic prompt caching gives 11x discounts on repeated system prompts. Output token caps and context trimming reduce what gets sent and received.

## Results from a four week pilot

To validate Heimdall under real conditions, we conducted a four-week internal production pilot with six Thoughtworkers across diverse delivery streams.

| Metric | Without Heimdall | With Heimdall |
| --- | --- | --- |
| Requests hitting paid API | 100% | 36.4% (63.6% reduction) |
| Model selection | Always expensive | Dynamic (Local / Haiku / Sonnet) |
| PII protection | None | 4,170 leaks prevented |
| Cost visibility | Blind spend | Per-request tracing |
| Cache hit rate | — | 34.2% |





## What surprised us

The results were certainly interesting, but there were two things in particular that surprised us.

- **Smart cache keys mattered more than smart caching algorithms.** Two IDE prompts that are semantically identical look completely different as raw strings because of metadata noise. Stripping that noise was a simple change with outsized impact.

- **14ms for PII scrubbing is effectively free.** When your LLM call takes two to 15 seconds, 14ms of safety is invisible.

## Impact at Thoughtworks and beyond

**Plug-and-Play Architecture:** Designed with modularity in mind, Heimdall's individual Guardians are completely decoupled. Any organization or internal team can easily deploy the full suite or adopt individual components, such as the PII scrubber or semantic cache, into their existing AI architecture with minimal overhead. It can also be used in Thoughtworks' AI/works platform.

## Policy doesn’t scale: Engineering controls do

Every organization scaling generative AI eventually confronts the same dual challenge: how to rein in explosive token expenditure, and how to prevent sensitive data from leaking into third-party foundation models.

Most answer with policy. *"Don't paste sensitive data into ChatGPT."* But policy doesn't scale. Engineering controls do. Heimdall is an engineering answer to a governance problem. And now [every token has a price tag](https://www.thoughtworks.com/insights/blog/generative-ai/does-every-feature-build-ai-token-budget), that answer matters more than ever. Furthermore, Heimdall can be easily extended to AI/works to provide seamless control and governance across workflows.


## Lessons Learned from the AI/works Hackathon

Our journey in the AI/works Global Hackathon — where Heimdall took 2nd Place in LATAM and earned the Best Collaboration Award — was a testament to what happens when team members collaborate seamlessly across borders.

With invaluable guidance and mentorship from Thiago Gregorio and others, we tried to emphasize several core principles that shaped both the project and our approach to engineering:

1. **Experiment boldly and fail fast.** Rapid prototyping allowed us to validate key hypotheses quickly. When testing different routing mechanisms and caching strategies, testing ideas without fear of failure helped us land on an optimized architecture within days.
2. **Maintain a builder’s mindset.** Focusing on practical implementation rather than purely theoretical solutions ensured every component solved a real, observable problem faced by developers in production workflows.
3. **Plug-and-play and modular flexibility.** From day one, Heimdall was designed so its components are completely modular. Teams can selectively deploy individual features—such as PII scrubbing or semantic caching—into any existing infrastructure or seamlessly extend them into the broader AI/works platform.

**Ultimately, these principles demonstrate that effective AI governance is best achieved through engineering solutions rather than passive guidelines. By building modular, developer-centric plug and play controls organizations can foster rapid innovation while maintaining robust security and cost efficiency.**
