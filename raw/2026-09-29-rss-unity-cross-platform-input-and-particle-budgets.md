---
source: "https://unity.com/blog/scaling-scritchy-scratchy-across-platforms"
title: "Scaling Scritchy Scratchy across platforms"
author: "Adam Axler"
date_published: "2026-09-28"
date_clipped: "2026-09-29"
category: "Game Development / Unity"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Unity's interview describes porting Scritchy Scratchy through one shared project rather than long-lived platform branches. This simplified propagation of fixes and content, at the cost of conditional platform code.

The team abstracted hardware input from gameplay but still redesigned controller interaction instead of mapping a pointer mechanically. Mobile haptic strength and tablet aspect ratios required device-specific iteration. Profiling identified texture-derived scratch particles as a mobile bottleneck; GPU instancing addressed that workload. Validation included devices near the supported lower hardware boundary.

For HoneyDrunk, establish input semantics, layout behavior, and performance targets early, then validate the actual interaction on each target. Shared code does not remove platform SDK, signing, store-build, or cloud-save work. The particle optimization is evidence from this game's workload, not a universal remedy for frame-time problems. This interview also supplies technical-art coverage through the rendering and particle pipeline.

Source: [Original article](https://unity.com/blog/scaling-scritchy-scratchy-across-platforms).
