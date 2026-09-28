---
source: "https://andrewlock.net/creating-strongly-typed-metics-with-a-source-generator"
title: "Exploring the (underwhelming) System.Diagnostics.Metrics source generators: System.Diagnostics.Metrics APIs - Part 2"
author: "Andrew Lock"
date_published: "2026-02-03"
date_clipped: "2026-09-28"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Andrew Lock compares handwritten metrics helpers with generated wrappers from Microsoft.Extensions.Telemetry.Abstractions 10.2.0. The walkthrough inspects instrument factories, per-meter caching, tag construction, and application call sites instead of assuming that generation improves performance.

In the version examined, descriptions are unavailable through the demonstrated attributes and specifying units requires an experimental API opt-in. Typed tag objects make argument mistakes easier to spot, but their string/enum constraints introduce conversion costs. The generated approach changes the public helper API while retaining much of the underlying work.

HoneyDrunk application: inspect generated output and benchmark representative metric paths before standardizing a generator. Compare API completeness, allocation behavior, and maintenance cost against a small manual helper.

This is a February 2026 backfill with version-specific observations. The author's preference for manual helpers is an assessment of the example, not a universal performance finding.

Source: [Original article](https://andrewlock.net/creating-strongly-typed-metics-with-a-source-generator).

Capture note: Original attributed summary after fetching readable written content; not a full-text reproduction.
