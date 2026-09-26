---
source: "https://www.canva.dev/blog/engineering/worker-backpressure-part-1-how-we-taught-our-queue-workers-to-slow-down/"
title: "Worker Backpressure (Part 1): teaching queue workers to slow down"
author: "Mikalai Barysau"
date_published: "2026-09-17"
date_clipped: "2026-09-24"
category: "Software Architecture"
source_type: "rss"
capture_method: "attributed-summary"
discovered_via: "https://tldr.tech/dev/2026-09-23"
---

# Worker Backpressure (Part 1): teaching queue workers to slow down

Attributed summary of the fetched article.

Canva describes a local feedback controller that reduces queue-worker concurrency when processing failures exceed a configured set point. Outcomes update a backoff factor; polling uses that factor to limit permits. Work stays queued rather than repeatedly hammering an unhealthy dependency.

The mechanism needs no external coordinator. Two production incidents illustrate reduced dead-letter accumulation during intermittent failure and sustained overload. These are observational case studies; estimates of an unprotected fleet are counterfactual calculations.

Trade-offs include lower throughput and reliance on a simple success/failure signal that may not fit every workload. This first article leaves recovery from complete backoff and controller tuning details to a later installment.

HoneyDrunk application: evaluate dependency-aware concurrency control for ingestion and background workers, measuring queue age and recovery as well as errors. Source confidence: firsthand engineering account with explicit limitations, not a complete ready-to-copy control algorithm.

Source: [Original article](https://www.canva.dev/blog/engineering/worker-backpressure-part-1-how-we-taught-our-queue-workers-to-slow-down/).
