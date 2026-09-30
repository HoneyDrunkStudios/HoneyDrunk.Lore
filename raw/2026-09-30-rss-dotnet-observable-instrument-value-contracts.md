---
source: "https://andrewlock.net/creating-standard-and-observable-instruments"
title: "Creating standard and \"observable\" instruments: System.Diagnostics.Metrics APIs - Part 3"
author: "Andrew Lock"
date_published: "2026-02-17"
date_clipped: "2026-09-30"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

The article explains seven System.Diagnostics.Metrics instrument types with examples from .NET and ASP.NET Core. Ordinary counters report increments; observable counters return the cumulative total when a consumer polls. Ordinary up/down counters emit signed deltas, while their observable counterparts return the current value. Request-start and request-end measurements need matching tags so active-request series reconcile. For HoneyDrunk telemetry, choose instruments based on whether the measurement is an event, total, current state, or distribution, then verify what the consumer observes. Treating observed totals as increments can produce misleading aggregation.

Source: [Original article](https://andrewlock.net/creating-standard-and-observable-instruments).
