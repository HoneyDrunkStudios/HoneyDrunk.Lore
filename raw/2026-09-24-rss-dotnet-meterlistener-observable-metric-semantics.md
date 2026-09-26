---
source: "https://andrewlock.net/recording-metrics-in-process-using-meterlistener/"
title: "Recording metrics in-process using MeterListener: System.Diagnostics.Metrics APIs - Part 4"
author: "Andrew Lock"
date_published: "2026-02-24"
date_clipped: "2026-09-24"
category: ".NET Ecosystem"
source_type: "rss"
capture_method: "attributed-summary"
---

# Recording metrics in-process using MeterListener: System.Diagnostics.Metrics APIs - Part 4

Attributed summary of the fetched article.

Andrew Lock demonstrates in-process consumption of System.Diagnostics.Metrics using MeterListener and a small ASP.NET Core example. The listener selects instruments, enables their measurements, and registers callbacks for each supported numeric type. Passing state avoids closures and repeated lookups.

Synchronous counters report increments, whereas observable counters report current totals when RecordObservableInstruments is invoked. Confusing these contracts causes incorrect aggregation. Tags distinguish series such as heap generations; concurrent callbacks require appropriate atomic updates or synchronization. Histograms need an explicit aggregation policy, and locking can create contention.

HoneyDrunk application: use these distinctions when testing or debugging custom metric consumers. The author recommends established telemetry libraries for production aggregation rather than copying the demonstration wholesale. This February article is an intentional evergreen backfill, not a new framework announcement. Source confidence: detailed practitioner example, not executed during sourcing.

Source: [Original article](https://andrewlock.net/recording-metrics-in-process-using-meterlistener/).
