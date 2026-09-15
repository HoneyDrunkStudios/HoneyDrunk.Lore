---
source: "https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic"
title: "Agentic coding is straining CI. Here’s how we scaled test impact analysis at Anthropic"
author: "Sachin Malhotra"
date_published: "2026-09-14"
date_clipped: "2026-09-15"
category: "DevOps & CI/CD"
source_type: "rss"
capture_format: "attributed-summary"
extraction_status: "full written page fetched; readable body reviewed"
discovered_via: "https://tldr.tech/dev/2026-09-15"
---

# Agentic coding is straining CI. Here’s how we scaled test impact analysis at Anthropic

Source: [Agentic coding is straining CI. Here’s how we scaled test impact analysis at Anthropic](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)

## Attributed content summary

Anthropic reports that CI job volume grew 25-fold over six months, straining its deterministic test-selection service. A listener maintained result history that the selector used to choose relevant tests; ingestion lag made selection data stale.

Increasing machine capacity and dividing work by package bought progressively less time. The eventual redesign moved results into a journal in an external in-memory store. Stateless listener workers append results, while a separate consumer aggregates per-test history for selection. This permits horizontal scaling without retaining the entire workload in each listener process.

The article distinguishes missed result ingestion from tests never running: stale selection data caused poor test choices, including repeatedly selecting flaky tests. It recommends measuring input/output job counts, monitoring lag, and making state placement explicit.

This is a first-person infrastructure case study. The redesigned service cost more to operate; the reported growth rate and proposed capacity multipliers are organization-specific, not universal sizing requirements.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
