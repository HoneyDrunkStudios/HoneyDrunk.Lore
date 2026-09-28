---
source: "https://techcommunity.microsoft.com/blog/azuredevcommunityblog/engineering-agentic-recall-controls-with-mcp-and-microsoft-foundry/4557549"
title: "Engineering Agentic Recall Controls with MCP and Microsoft Foundry"
author: "Lee_Stott"
date_published: "2026-09-24"
date_clipped: "2026-09-28"
category: "Software Architecture"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Lee Stott's synthetic recall demonstration separates agent reasoning from application authority. Specialists receive narrowly scoped read operations; deterministic code controls approval and inventory mutation. Tool annotations describe behavior but do not enforce authorization.

Approval binds an authenticated actor to a resource, operation, session generation, and validity period. Domain logic makes replay idempotent. Actor-specific Blob state uses ETags so conflicting writes fail instead of silently replacing one another.

The hosted path rejects partial or failed responses and does not disguise local fallback as cloud execution. Its interface explicitly acknowledges unavailable workflow traces. Historical evaluations are treated as evidence to rerun against the deployed version.

HoneyDrunk application: adopt these boundaries as review questions for consequential agent actions and state persistence.

This is a developer sample with fictional data, not a production control system. Its local audit trail is not tamper-evident; deployment configuration, recovery, load behavior, and operational evidence remain separate validation tasks.

Source: [Original article](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/engineering-agentic-recall-controls-with-mcp-and-microsoft-foundry/4557549).

Capture note: Original attributed summary after fetching readable written content; not a full-text reproduction.
