---
source: "https://80.lv/articles/former-pixar-fx-artist-reveals-a-smarter-way-to-refine-destruction"
title: "Former Pixar FX Artist Reveals a Smarter Way to Refine Destruction"
author: "Jae Jun Yi; interview by David Jagneaux"
date_published: "2026-09-28"
date_clipped: "2026-09-29"
category: "Technical Art & Creator Tools"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

In this interview, FX artist Jae Jun Yi describes refining an approved Houdini destruction simulation in layers. Selected pieces are fractured again while preserving parent identifiers and transferring position, orientation, velocity, and related motion data. New fragments follow inherited motion until an explicit activation condition starts their own simulation.

This lets artists change local fracture detail or timing without rebuilding every approved movement. Constraints and collisions still require attention: inherited constraints may stretch, and overlapping fragments can produce violent activation responses. The artist describes reducing collision sizes as one mitigation.

For HoneyDrunk, the transferable idea is preserving identity and state across successive procedural refinements. The technique fits baked destruction and controlled cinematic views; it does not establish a general solution for fully interactive destruction. Large changes to overall motion may still require rerunning the base simulation. This is practitioner evidence from the workflow's author, not independent performance validation.

Source: [Original article](https://80.lv/articles/former-pixar-fx-artist-reveals-a-smarter-way-to-refine-destruction).
