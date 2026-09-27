---
source: "https://www.datadoghq.com/blog/ai/investigate-production-alerts/"
title: "Teaching a 9B model to investigate production alerts"
author: "Scott Kramer; Junaid Ahmed"
date_published: "2026-09-23"
date_clipped: "2026-09-27"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
discovered_via: "https://tldr.tech/devops/2026-09-25"
---

# Teaching a 9B model to investigate production alerts

Source: [Teaching a 9B model to investigate production alerts](https://www.datadoghq.com/blog/ai/investigate-production-alerts/)

Capture note: Original summary of the fetched article; full text is not reproduced.

Datadog fine-tuned Qwen3.5-9B using successful GLM-5.3 investigation traces. Teacher runs used five tools and an eight-turn budget. Matching traces were selected using labels derived from prior investigation conclusions; these labels represent agreement, not independently established incident causality.

Training grew from 100 to 186 internal examples. Evaluation used 326 later incidents, including 139 customer incidents outside the training population. Direct teacher comparison covered internal incidents only: student Recall@5 was 0.55 versus 0.63 for the teacher. Customer Recall@5 was 0.62 versus 0.52 for the base model.

The reported $0.003 student serving cost versus $0.06 teacher API cost depends on the stated GPU utilization and deployment assumptions. Fine-tuning shifted behavior toward targeted evidence collection.

HoneyDrunk relevance: specialize a repeatable investigation workflow using bounded traces and time-separated evaluation. Preserve label uncertainty and measure complete operating cost before adopting the cost claim. These are vendor-reported results.
