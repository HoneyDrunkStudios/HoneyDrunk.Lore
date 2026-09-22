---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/dashboards-are-for-ai-agents-too-not-just-humans/4556383"
title: "Dashboards are for AI agents too, not just humans"
author: "Wuyi_Weng"
date_published: "2026-09-14"
date_clipped: "2026-09-20"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
---

# Dashboards are for AI agents too, not just humans

Source: [Dashboards are for AI agents too, not just humans](https://techcommunity.microsoft.com/blog/appsonazureblog/dashboards-are-for-ai-agents-too-not-just-humans/4556383)

Attributed summary of the fetched full written article; not a verbatim reproduction. Claims remain source-specific and have not been independently reproduced.

Wuyi Weng demonstrates Azure SRE Agent investigating Copilot sessions through Azure Managed Grafana's MCP endpoint. Dashboard inspection supplies query text, resource scope, variable values, panel descriptions, and known telemetry pitfalls. The agent uses that material to construct additional session-level queries.

A long active session and a repeated sleep/retry loop initially look similar in duration charts. Aggregated tool activity and captured arguments distinguish their causes. Dashboard descriptions document issues such as different time units, apparent success on timeouts, and double-counting parent spans.

The query tool still requires explicit time filtering and replacement of Grafana macros. Dashboard knowledge guides investigation; actual telemetry tests the proposed explanation.

The native connector uses the agent's managed identity. This is a worked example, not evidence that every dashboard or agent will produce reliable diagnoses.

HoneyDrunk relevance: preserve scope, units, freshness indicators, and interpretation notes alongside observability queries so both operators and agents can investigate the same evidence.
