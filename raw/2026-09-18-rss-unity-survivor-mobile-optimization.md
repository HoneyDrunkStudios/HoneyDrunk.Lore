---
source: "https://unity.com/blog/optimizing-deep-rock-galactic-survivor-for-mobile"
title: "Optimizing Deep Rock Galactic Survivor for mobile"
author: "Adam Axler"
date_published: "2026-09-18"
date_clipped: "2026-09-18"
category: "Game Development / Unity"
source_type: "rss"
---

# Optimizing Deep Rock Galactic Survivor for mobile

Capture format: attributed summary of fetched public written content; not a full-text reproduction.

Unity interviews Piktiv about porting Deep Rock Galactic: Survivor to mobile while supporting thousands of entities. The team targeted a constrained iPad memory budget and automated six performance scenarios across biomes, measuring CPU, GPU, and memory.

Damage numbers moved from repeated text-mesh generation to digit sprites in particles. Flow fields replaced per-agent navigation, bounded to active enemies and the player. A KD-tree reduced physics-query work, though frequent rebuilding remained a tradeoff for moving entities.

Single-animation enemies used texture-baked vertex animation and GPU instancing. Burst jobs, native containers, and custom environment batching reduced CPU work without converting the entire game to ECS.

Addressables separated biome assets to meet memory constraints but introduced asynchronous-loading architecture work. The mobile branch also required ongoing one-way merges from PC development.

Lore relevance: profile systems whose cost grows with entity count, validate on target devices, and adopt data-oriented techniques selectively. These are project-specific engineering outcomes, not universal performance guarantees.

Source: [Original article](https://unity.com/blog/optimizing-deep-rock-galactic-survivor-for-mobile).
