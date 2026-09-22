---
source: "https://linear.app/now/ci-bottleneck-reworked"
title: "AI coding has made CI a bottleneck, so we reworked ours to keep up"
author: "Mufeez Amjad"
date_published: "2026-09-21"
date_clipped: "2026-09-22"
category: "DevOps & CI/CD"
source_type: "rss"
capture_format: "attributed-summary"
discovered_via: "https://tldr.tech/dev/2026-09-22"
---

# AI coding has made CI a bottleneck, so we reworked ours to keep up

Source: [AI coding has made CI a bottleneck, so we reworked ours to keep up](https://linear.app/now/ci-bottleneck-reworked)

Attributed summary of the fetched written article; not a full reproduction. Source claims have not been independently reproduced.

Linear reports reducing pull-request CI waiting and runner cost despite rapid test-suite growth. The team separately measured wall-clock feedback time and total runner consumption, then improved infrastructure, prerequisite jobs, repeated setup, and test execution.

Changes included fetching less repository history, eliminating unnecessary checkout, using bounded network retries, and moving cache-marker writes off the merge gate. Prepared images, package-scoped installation, and schema snapshots reduced work repeated across shards. Cache restoration was discarded where rebuilding proved faster.

Small checks were grouped into fewer jobs. Large test files were split to improve shard balance; additional sharding became worthwhile only after setup overhead fell. Selected tests shared module state to avoid expensive initialization, but this required explicit opt-in and teardown. Files with unsafe shared state retained isolation.

HoneyDrunk relevance: optimize required-check dependencies and repeated setup before purchasing more concurrency. Preserve test independence when changing execution models. The reported savings belong to Linear's TypeScript workload and are not forecasts for .NET pipelines.
