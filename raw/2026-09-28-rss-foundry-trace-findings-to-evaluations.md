---
source: "https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/insights-in-foundry-turns-agent-traces-into-action/4559634"
title: "Insights in Foundry Turns Agent Traces into Action"
author: "katelynrothney"
date_published: "2026-09-24"
date_clipped: "2026-09-28"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Microsoft describes a public preview that analyzes agent traces in a connected Application Insights resource to identify recurring behavior beyond predefined evaluations. Findings may include representative executions, affected versions, likely causes, and suggested responses.

The article distinguishes an intermediate tool failure from task failure and a plausible cause from a verified diagnosis. Developers inspect evidence, choose a targeted change or new evaluation, route infrastructure problems to their owner, or deliberately start an optimization experiment.

Insights does not independently create pull requests, build evaluators, or deploy repairs. The initial scan covers seven days; subsequent analysis is on demand. Missing identity, versions, spans, or content can limit conclusions, and an empty findings list does not demonstrate correctness.

HoneyDrunk application: compare this evidence-to-regression workflow with existing agent failure analysis. Preserve human review and measure outcomes on fresh traces. Preview support and analysis costs require checking before deployment.

Source: [Original article](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/insights-in-foundry-turns-agent-traces-into-action/4559634).

Capture note: Original attributed summary after fetching readable written content; not a full-text reproduction.
