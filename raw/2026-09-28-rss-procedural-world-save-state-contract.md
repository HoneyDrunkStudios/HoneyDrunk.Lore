---
source: "https://dev.to/krizekster/a-world-seed-is-a-recipe-not-a-save-file-separate-generation-from-progress-1bnf"
title: "A World Seed Is a Recipe, Not a Save File: Separate Generation from Progress"
author: "Krishna Soni"
date_published: "2026-09-28"
date_clipped: "2026-09-28"
category: "Game Development / Unity"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Krishna Soni distinguishes a reproducible generated starting world from a saved world containing player changes. The proposed record stores a seed and generator/content versions separately from changed entities and quest state.

A version label alone does not preserve compatibility. The implementation still needs compatible generation, migration, or enough stored state to restore the world. Stable entity identifiers matter when applying saved changes after an update. Saving random-generator state also does not preserve inventory or player-built objects.

The article proposes acceptance tests for repeatable initial generation, persistence after reload, fresh-world behavior, and explicit handling of generator changes. Accepted model-generated content should be persisted when continuity matters.

HoneyDrunk application: use these distinctions when defining simulation persistence and migration contracts. This article also supplies architecture coverage through baseline-plus-delta persistence and versioned state. Its schema and tests are proposals, not demonstrated production results.

Source: [Original article](https://dev.to/krizekster/a-world-seed-is-a-recipe-not-a-save-file-separate-generation-from-progress-1bnf).

Capture note: Original attributed summary after fetching readable written content; not a full-text reproduction.
