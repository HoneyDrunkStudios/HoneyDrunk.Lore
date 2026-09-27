---
source: "https://unity.com/blog/rust-ltd-hot-dogs-horseshoes-hand-grenades-2"
title: "How RUST LTD built the deep firearm simulation for Hot Dogs, Horseshoes & Hand Grenades 2"
author: "Adam Axler"
date_published: "2026-09-25"
date_clipped: "2026-09-27"
category: "Game Development / Unity"
source_type: "rss"
capture_format: "attributed-summary"
---

# How RUST LTD built the deep firearm simulation for Hot Dogs, Horseshoes & Hand Grenades 2

Source: [How RUST LTD built the deep firearm simulation for Hot Dogs, Horseshoes & Hand Grenades 2](https://unity.com/blog/rust-ltd-hot-dogs-horseshoes-hand-grenades-2)

Capture note: Original summary of the fetched article; full text is not reproduced.

RUST LTD rebuilt H3VR2 around architecture and authoring tools before scaling content production. Small internal component simulations use custom local models, while broader physics and ECS/Burst systems address different workloads. The team describes using data-driven behavior and reusable validation instead of isolated per-object tuning.

Rendering budgets shaped level density, texture use, lighting, and art direction early. Expensive hero assets received budget deliberately; surrounding environments remained lean. Modular levels were tested against probe-based lighting before production scaled.

Custom Inspector tools support calculation, validation, analysis, and hiding irrelevant parameters. Asset configuration becomes the operational source of truth. The team also cautions against simulation detail that neither improves authoring nor produces player-visible value.

HoneyDrunk relevance: build validation and authoring tools alongside simulation, and measure target-device budgets before committing to content volume. This is a practitioner interview, with performance benefits reported by the team rather than independently benchmarked.
