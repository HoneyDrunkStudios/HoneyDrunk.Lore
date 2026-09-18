---
source: "https://80.lv/articles/3d-artist-on-creating-a-geometry-based-plugin-that-makes-realistic-worn-edges"
title: "3D Artist on Creating a Geometry-Based Plugin That Makes Realistic Worn Edges"
author: "Cornelius Dämmrich"
date_published: "2026-09-16"
date_clipped: "2026-09-16"
category: "Technical Art & Creator Tools"
source_type: "rss"
capture_format: "attributed-summary"
---

# 3D Artist on Creating a Geometry-Based Plugin That Makes Realistic Worn Edges

Source: [3D Artist on Creating a Geometry-Based Plugin That Makes Realistic Worn Edges](https://80.lv/articles/3d-artist-on-creating-a-geometry-based-plugin-that-makes-realistic-worn-edges)

## Attributed content summary

Cornelius Daemmrich explains Edgy, a geometry-based edge-damage tool for Cinema 4D and Blender. Its shared geometry core accepts points and polygons without host-specific types; deterministic inputs and seeds are checked across both integrations. Host adapters handle application-specific presentation and material assignment.

Damage cutters are combined through batched Boolean subtraction so overlapping cuts form coherent cavities. Profiling found cutter count more important than base mesh size in the described workload; adaptive cutter tessellation reduced one test scene from 40 seconds to 13. These are the developer's measurements, not a general performance guarantee.

Preset design separates damage strength from user decisions such as seed and edge eligibility. Parameters tuned in a reference scene generate matching tables for both hosts, reducing drift. The article also describes floating-point changes undermining cache reuse during animation.

The reusable technical-art patterns are a host-independent computational core, deterministic cross-host checks, measured optimization, and presets that preserve intent. Evaluate geometry cost and export requirements before applying the technique to real-time assets.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
