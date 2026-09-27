---
source: "https://opentelemetry.io/blog/2026/dont-wrap-opentelemetry/"
title: "Don't Wrap OpenTelemetry — You're Probably Hurting More Than Helping"
author: "Cijo Thomas"
date_published: "2026-06-24"
date_clipped: "2026-09-27"
category: "Software Architecture"
source_type: "rss"
capture_format: "attributed-summary"
canonical_source: "https://medium.com/@cijo.thomas/dont-wrap-opentelemetry-you-re-probably-hurting-more-than-helping-96795803abeb"
---

# Don't Wrap OpenTelemetry — You're Probably Hurting More Than Helping

Source: [Don't Wrap OpenTelemetry — You're Probably Hurting More Than Helping](https://opentelemetry.io/blog/2026/dont-wrap-opentelemetry/)

Capture note: Original summary of the fetched article; full text is not reproduced.

Cijo Thomas argues that instrumentation wrappers can discard the efficiency and interoperability of OpenTelemetry's existing API. Collection-only signatures can force allocations; instrument-name lookup on every measurement adds hashing or locking to hot paths. Holding instrument references and preserving efficient tag representations avoids these particular costs.

The article distinguishes application instrumentation from shared SDK configuration. Standardizing exporters, resource attributes, or sampling setup does not require replacing the measurement API. Legacy dual-write migrations can justify an abstraction, provided its cost and exposed behavior are deliberate.

For governance, generated typed calls can enforce conventions without a general runtime wrapper. The post points to Weaver as related upstream work.

HoneyDrunk relevance: benchmark abstraction overhead before imposing a common metrics facade, and keep configuration reuse separate from per-measurement behavior. This June 2026 evergreen backfill is an architectural argument with examples, not a measured HoneyDrunk regression. The OpenTelemetry page identifies a Medium original via its canonical link.
