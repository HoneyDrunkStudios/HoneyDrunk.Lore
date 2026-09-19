---
source: "https://unity.com/blog/hologryph-sand-raiders-of-sophie"
title: "How Hologryph built SAND: Raiders of Sophie for a sustainable live ops cadence"
author: "unknown"
date_published: "2026-08-26"
date_clipped: "2026-09-19"
category: "Game Development / Unity"
source_type: "rss"
capture_format: "attributed-summary"
---

# How Hologryph built SAND: Raiders of Sophie for a sustainable live ops cadence

Source: [How Hologryph built SAND: Raiders of Sophie for a sustainable live ops cadence](https://unity.com/blog/hologryph-sand-raiders-of-sophie)

*Attributed summary of the fetched written article; not a verbatim reproduction.*

Unity's interview with Hologryph describes SAND's live-operations architecture: an authoritative server, matching procedural generation across client and server, entity replication, and continuous world streaming.

Modular Trampler compartments let designers add content through data and configuration. New mechanics require isolated programming work. The game uses a modified Entitas ECS with custom dependency injection and networking, rather than Unity Entities. Burst-compiled jobs handle expensive terrain, movement, and culling paths.

Configurable VFX graphs expose parameters so artists can create weapon variations without rebuilding effects. Addressables support streaming and memory management, while a custom asset-transfer pipeline keeps separate client and server projects aligned. Automated fixed-scenario performance checks complement profiling.

HoneyDrunk implication: separate replication and infrastructure from gameplay, make repeatable content changes data-driven, and continuously measure performance as content grows. This is a studio-reported case study, not a guarantee that the same architecture or performance results transfer unchanged to smaller projects. It also supplies a reusable technical-art workflow pattern.
