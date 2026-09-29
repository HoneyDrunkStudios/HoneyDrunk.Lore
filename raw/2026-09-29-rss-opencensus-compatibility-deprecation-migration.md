---
source: "https://opentelemetry.io/blog/2026/deprecating-opencensus-compatibility/"
title: "Deprecating OpenCensus compatibility requirements"
author: "Krishna Chaitanya Balusu"
date_published: "2026-06-23"
date_clipped: "2026-09-29"
category: "DevOps & CI/CD"
source_type: "rss"
capture_format: "attributed-summary"
date_modified: "2026-09-28"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

OpenTelemetry has deprecated the specification requirement to implement OpenCensus compatibility. New SDKs need not add that compatibility, and new instrumentation should use native OpenTelemetry APIs, SDKs, and OTLP. Existing compatibility artifacts are not required to disappear immediately.

The article separates policy stages: deprecation took effect in June 2026; specification removal is scheduled no earlier than June 2027; existing shims retain a maintenance period under SDK stability guarantees. Consumers should inventory shim dependencies and plan migration instead of equating deprecation with immediate breakage.

For HoneyDrunk, this is dependency-lifecycle guidance for telemetry integration. Check the actual language SDK and bridge package before selecting a removal date. The feed surfaced the item in September, but the visible article and publication metadata date it June 23; September 28 is its modification date.

Source: [Original article](https://opentelemetry.io/blog/2026/deprecating-opencensus-compatibility/).
