---
source: "https://opentelemetry.io/blog/2026/dual-dotnet-metrics-export-with-otlp-and-prometheus/"
title: "Dual-exporting .NET metrics with OTLP and Prometheus"
author: "Martin Costello (Grafana Labs)"
date_published: "2026-09-18"
date_clipped: "2026-09-18"
category: ".NET Ecosystem"
source_type: "rss"
---

# Dual-exporting .NET metrics with OTLP and Prometheus

Capture format: attributed summary of fetched public written content; not a full-text reproduction.

Martin Costello describes a gradual migration from Prometheus-specific instrumentation to .NET Meter instruments with parallel OpenTelemetry exports. The same measurements can feed an OTLP backend and an application-hosted Prometheus scrape endpoint, allowing comparison before cutover.

The article uses OpenTelemetry.Exporter.OpenTelemetryProtocol and OpenTelemetry.Exporter.Prometheus.AspNetCore. Configure both exporters, register the application meter, and expose the scraping endpoint. Existing prometheus-net instrumentation first needs migration to Meter; changing exporters alone does not replace that instrumentation.

The referenced Prometheus exporter release is a beta. The article identifies Prometheus summaries and native histograms as unsupported in this path, and excludes experimental OpenMetrics 2.0 from exposition support.

An alternative sends HTTP/protobuf OTLP directly to a Prometheus server with its OTLP receiver enabled. That route does not require the scrape exporter.

Lore relevance: stage observability migration by comparing metrics and alerts across backends. Validate package versions and metric semantics before adopting the sample.

Source: [Original article](https://opentelemetry.io/blog/2026/dual-dotnet-metrics-export-with-otlp-and-prometheus/).
