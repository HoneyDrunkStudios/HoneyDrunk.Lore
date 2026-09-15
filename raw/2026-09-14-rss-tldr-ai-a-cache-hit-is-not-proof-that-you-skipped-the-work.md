---
source: "https://siddhantkhare.com/writing/kv-cache-truth-auditor"
title: "A cache hit is not proof that you skipped the work"
author: "Siddhant Khare"
date_published: "2026-09-13"
date_clipped: "2026-09-14"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_mode: "attributed-summary"
content_note: "Substantive summary of the fetched readable article; not a verbatim full-text archive."
discovered_via: "https://tldr.tech/ai/2026-09-14"
---

# A cache hit is not proof that you skipped the work

Source: [A cache hit is not proof that you skipped the work](https://siddhantkhare.com/writing/kv-cache-truth-auditor)

## Attributed article summary

A reported KV-cache hit does not establish that a runtime avoided computation. Khare describes a synthetic token-level auditor that compares expected reusable prefixes against engine attestations and observed prompt work, then separately checks output identity and evaluator results.

The ten cases include cold requests, exact duplicates, interior and boundary edits, equal-length inputs with different token IDs, namespace separation, and eviction. In the duplicate control, eight of nine tokens were reused and one required prompt work. Namespace isolation required all nine tokens to be processed.

The durable pattern is to distinguish cache correctness, avoided work, answer correctness, and measured performance. Checksums, schemas, request order, and independent verification bind evidence to an experiment. The author explicitly does not establish production MLX/vLLM correctness, GPU speedup, latency savings, or memory savings; unavailable measurements remain null.

HoneyDrunk relevance: agent-cost instrumentation should test cache claims against independent controls before turning cached-token counts into savings estimates.
