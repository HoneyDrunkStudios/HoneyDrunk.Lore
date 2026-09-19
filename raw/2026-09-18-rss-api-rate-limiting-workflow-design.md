---
source: "https://blog.n8n.io/api-rate-limiting/"
title: "API Rate Limiting for More Reliable Workflows"
author: "n8n team; Yulia Dmitrievna"
date_published: "2026-09-18"
date_clipped: "2026-09-18"
category: "Software Architecture"
source_type: "rss"
---

# API Rate Limiting for More Reliable Workflows

Capture format: attributed summary of fetched public written content; not a full-text reproduction.

The n8n guide compares token buckets, leaky buckets, fixed windows, and sliding windows. Their tradeoffs concern burst allowance, steady processing, reset-boundary spikes, and tracking complexity. Limits can vary by endpoint cost, client, or plan.

Consumers should use 429 responses and Retry-After information to pace retries instead of immediately amplifying load. Batch and delay requests proactively, fetch collections instead of individual records where possible, and cache slowly changing data with an explicit refresh strategy.

In n8n, retry settings, item loops, waits, and error workflows can express this behavior. Exhausted retries should have an explicit failure path.

The article distinguishes outbound pacing from inbound protection: an exposed n8n webhook is not an API gateway and lacks built-in inbound rate limiting. Place a gateway or reverse proxy ahead of public workflows that need traffic control.

Lore relevance: design scheduled ingestion around provider quotas and preserve reliable failure reporting as source volume increases.

Source: [Original article](https://blog.n8n.io/api-rate-limiting/).
