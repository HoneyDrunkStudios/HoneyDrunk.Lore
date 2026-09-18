---
source: "https://dev.to/flowerfestival/building-a-browser-game-with-astro-cloudflare-workers-and-a-verifiable-d1-leaderboard-1mji"
title: "Building a Browser Game with Astro, Cloudflare Workers, and a Verifiable D1 Leaderboard"
author: "FlowerFestival"
date_published: "2026-09-16"
date_clipped: "2026-09-16"
category: "Game Development / Unity"
source_type: "rss"
capture_format: "attributed-summary"
---

# Building a Browser Game with Astro, Cloudflare Workers, and a Verifiable D1 Leaderboard

Source: [Building a Browser Game with Astro, Cloudflare Workers, and a Verifiable D1 Leaderboard](https://dev.to/flowerfestival/building-a-browser-game-with-astro-cloudflare-workers-and-a-verifiable-d1-leaderboard-1mji)

## Attributed content summary

A browser-game developer describes verifying leaderboard results by replaying an ordered action log on the server. A signed draft token establishes the offered choices; the server reconstructs the seeded draft, rejects illegal actions, calculates the score, and issues a signed result for publication.

Determinism also requires matching data, ordering, and random-number consumption. The author recommends versioning rules and rosters so older browser sessions remain interpretable after deployment. Legal replay does not establish human participation or prevent a bot from optimizing valid moves.

Daily personal bests must be stored separately from lifetime records: a lower score today still belongs on today's board. Historical runs discarded by an earlier schema cannot be reconstructed during migration.

The stack uses Astro, Preact, Workers, and D1, but the durable game-system patterns are server-owned scoring, explicit replay contracts, and time-aware data modeling. Production checks also fetched generated share images; successful builds alone had missed a broken runtime dependency.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
