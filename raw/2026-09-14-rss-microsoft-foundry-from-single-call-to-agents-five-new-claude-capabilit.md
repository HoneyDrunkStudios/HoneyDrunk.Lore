---
source: "https://devblogs.microsoft.com/foundry/five-new-claude-capabilities-now-available-in-foundry"
title: "From single call to agents: five new Claude capabilities now available in Microsoft Foundry"
author: "Haoran Cheng"
date_published: "2026-08-17"
date_clipped: "2026-09-14"
category: "Azure & Cloud"
source_type: "rss"
capture_mode: "attributed-summary"
content_note: "Substantive summary of the fetched readable article; not a verbatim full-text archive."
---

# From single call to agents: five new Claude capabilities now available in Microsoft Foundry

Source: [From single call to agents: five new Claude capabilities now available in Microsoft Foundry](https://devblogs.microsoft.com/foundry/five-new-claude-capabilities-now-available-in-foundry)

## Attributed article summary

Microsoft describes five Claude capabilities on Foundry deployments hosted on Azure: schema-constrained outputs, web search, web fetch, an MCP connector, and tool search. The article provides SDK request examples and explains the distinction between controlling response structure and validating tool-call arguments.

Search discovers sources, fetch reads selected documents, and tool search addresses large tool catalogs. Domain restrictions and bounded tool use are practical controls for research workflows. Hosting choice remains a separate architectural decision from model and tool selection.

The article states that Azure-hosted prompts and completions remain within Azure while usage metadata and safety-flagged content can go to Anthropic. That qualification matters when interpreting its residency claims.

HoneyDrunk relevance: evaluate managed agent capabilities before maintaining custom search, fetch, and routing infrastructure. Treat supported model, deployment, and tool-version combinations as release-specific; confirm those combinations before implementation. Schema-valid output still requires business-level validation.
