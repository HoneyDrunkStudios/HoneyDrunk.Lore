---
source: "https://cognition.com/blog/swe-2"
title: "Introducing SWE-2: Pushing the Pareto Frontier"
author: "The Cognition Team"
date_published: "2026-09-10"
date_clipped: "2026-09-14"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_mode: "attributed-summary"
content_note: "Substantive summary of the fetched readable article; not a verbatim full-text archive."
discovered_via: "https://tldr.tech/ai/2026-09-11"
---

# Introducing SWE-2: Pushing the Pareto Frontier

Source: [Introducing SWE-2: Pushing the Pareto Frontier](https://cognition.com/blog/swe-2)

## Attributed article summary

Cognition describes SWE-2 as a coding model post-trained from Kimi K3, with reinforcement learning that trains multiple reasoning-effort levels together. Its objective applies different cost penalties by effort level, aiming to improve the capability/cost frontier rather than maximizing one benchmark score.

The engineering discussion covers length-weighted reward baselines, rollout scheduling, online draft models, quantization-aware training, and a larger collection of executable training environments. Earlier model checkpoints help find weaknesses in verifiers so subsequent training uses stronger checks.

Cognition reports reduced exploration and fewer redundant reads at medium effort, while higher effort spends more on planning and verification. Its FrontierCode and other benchmark comparisons are vendor-reported measurements, not independently reproduced results.

HoneyDrunk relevance: compare coding agents on representative repository tasks using total cost, turns before useful edits, correctness, and regression detection. Effort selection should depend on task difficulty; benchmark rankings alone do not establish suitability for the studio's codebases.
