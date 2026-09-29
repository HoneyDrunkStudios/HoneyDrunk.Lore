---
source: "https://modal.com/blog/quail-billion-tpm"
title: "Hitting a billion tokens per minute on one GPU by combining a query planner and an inference engine"
author: "Charles Frye; Shreya Shankar"
date_published: "2026-09-24"
date_clipped: "2026-09-29"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
discovered_via: "https://tldr.tech/ai/2026-09-28"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Modal presents Quail, an inference engine that uses an analytical query plan to optimize repeated LLM filters and joins. Knowing future requests enables cache-aware join ordering, deliberate KV eviction, and pretokenization. Boolean decisions can use a single prediction from prefill, avoiding the multi-token decoding workload typical of chat agents.

The reported billion-token throughput is a favorable multi-join case on an H100, not a general interactive-generation rate. Across the released benchmark suite, the authors report a 1.84-fold geometric-mean improvement over their vLLM baseline and explicitly include an agent-trace case where Quail loses. Current limitations include GPU-only KV caching and missing reuse across query lifetimes.

For HoneyDrunk, benchmark workload shape, accuracy, and baseline settings before extrapolating cost claims. The reusable idea is co-designing request scheduling and inference execution when the application controls a batch, rather than treating all inference as arbitrary chat traffic.

Source: [Original article](https://modal.com/blog/quail-billion-tpm).
