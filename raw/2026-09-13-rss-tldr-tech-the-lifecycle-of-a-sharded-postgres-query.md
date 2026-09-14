---
source: "https://planetscale.com/blog/the-lifecycle-of-a-sharded-postgres-query"
title: "The lifecycle of a sharded Postgres query"
author: "unknown"
date_published: "2026-09-10"
date_clipped: "2026-09-13"
category: "Software Architecture"
source_type: "rss"
discovered_via: "https://tldr.tech/tech/2026-09-11"
capture_mode: "attributed-summary"
full_text_fetched: "true"
---

# The lifecycle of a sharded Postgres query

Original source: [The lifecycle of a sharded Postgres query](https://planetscale.com/blog/the-lifecycle-of-a-sharded-postgres-query)

## Source-content summary

PlanetScale follows a query through its Neki sharded PostgreSQL router, covering authentication, protocol handling, parsing, planning, connection management, and distributed execution. The router supports both simple and extended PostgreSQL protocols so ordinary client drivers can communicate with the distributed service.

The worked example initially distributes customers and orders by independent primary keys. Joining them therefore requires additional work across shards and in the router. Distributing orders by customer_id using the customer's shard mapping instead keeps related rows together and enables local joins.

The query still contacts every shard because it requests recent orders across all customers; colocation removes the distributed join without eliminating fan-out. HoneyDrunk relevance: choose partition keys from access patterns and relationships, account for protocol compatibility beyond SQL syntax, and distinguish efficient local computation from genuinely single-shard routing. This is a vendor architecture explanation, not an independent performance comparison.

Capture note: This is an attributed summary of the fetched article, not a verbatim full-text archive. The original source retains the complete examples and discussion.
