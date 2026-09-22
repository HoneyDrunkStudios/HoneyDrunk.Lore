---
source: "https://newsletter.systemdesign.one/p/system-design-tradeoffs"
title: "50 shades of system design"
author: "Neo Kim"
date_published: "2026-09-03"
date_clipped: "2026-09-22"
category: "Software Architecture"
source_type: "rss"
capture_format: "attributed-summary"
---

# 50 shades of system design

Source: [50 shades of system design](https://newsletter.systemdesign.one/p/system-design-tradeoffs)

Attributed summary of the fetched written article; not a full reproduction. Source claims have not been independently reproduced.

Neo Kim organizes system-design choices around workload constraints rather than a universally preferred architecture. The article compares latency, throughput, consistency, durability, operating cost, and failure recovery across fifty paired choices.

For messaging systems, it distinguishes task distribution from retained event logs, global ordering from per-key ordering, and retry-driven duplicate delivery from stronger processing guarantees. Those choices affect replay, parallelism, consumer coordination, and idempotency requirements.

For service boundaries, it contrasts deployment autonomy with the coordination overhead introduced by separate services and databases. CQRS and event sourcing provide particular read-scaling or historical capabilities while adding synchronization and operational work.

Reliability sections connect retries to load amplification, large queues to stale work, and stronger recovery objectives to replication and testing costs. These are concise design heuristics with references, not a substitute for product-specific guarantees or measurements.

HoneyDrunk relevance: record workload assumptions and the operational price of each architectural choice. Use the comparisons as review prompts, then validate queue, database, and recovery behavior in the selected implementation.
