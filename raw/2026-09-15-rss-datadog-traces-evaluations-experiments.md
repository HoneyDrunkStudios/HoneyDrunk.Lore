---
source: "https://www.datadoghq.com/blog/from-traces-to-experiments-a-loop-for-improving-ai-agents/"
title: "From traces to experiments: A loop for improving AI agents"
author: "Adam Virani; Lukas Goetz-Weiss; Natasha Silva"
date_published: "2026-09-01"
date_clipped: "2026-09-15"
category: "DevOps & CI/CD"
source_type: "rss"
capture_format: "attributed-summary"
extraction_status: "full written page fetched; readable body reviewed"
discovered_via: "https://tldr.tech/devops/2026-09-14"
---

# From traces to experiments: A loop for improving AI agents

Source: [From traces to experiments: A loop for improving AI agents](https://www.datadoghq.com/blog/from-traces-to-experiments-a-loop-for-improving-ai-agents/)

## Attributed content summary

Datadog proposes a feedback loop connecting production traces, explicit hypotheses, offline evaluation, controlled online experiments, and continued monitoring. Traces should include tool behavior and downstream outcomes as well as latency and cost.

The article separates a production-weighted regression dataset from a coverage dataset that deliberately emphasizes difficult cases. Score them separately so aggregate performance cannot hide subgroup regressions. Compare baseline and candidate on identical records, repeat nondeterministic runs, and calibrate model-based judges against human review.

Before an online experiment, define its primary metric, regression limits, and stopping rule. Maintain consistent variant assignment and monitor latency, cost, errors, and secondary quality measures. New production failures should become future evaluation cases.

The product-specific implementation joins observability, feature flags, and experimentation. The general workflow is portable. Examples of support-ticket improvements are illustrative rather than demonstrated results. Redact sensitive production fields before retaining interactions as evaluation data, and scale the testing effort to the proposed change.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
