---
source: "https://dev.to/gameoptim/ugui-overdraw-optimization-tight-meshes-transparent-culling-and-9-slicing-12jb"
title: "UGUI Overdraw Optimization: Tight Meshes, Transparent Culling, and 9-Slicing"
author: "GameOptim"
date_published: "2026-09-15"
date_clipped: "2026-09-15"
category: "Game Development / Unity"
source_type: "rss"
capture_format: "attributed-summary"
extraction_status: "full written page fetched; readable body reviewed"
---

# UGUI Overdraw Optimization: Tight Meshes, Transparent Culling, and 9-Slicing

Source: [UGUI Overdraw Optimization: Tight Meshes, Transparent Culling, and 9-Slicing](https://dev.to/gameoptim/ugui-overdraw-optimization-tight-meshes-transparent-culling-and-9-slicing-12jb)

## Attributed content summary

GameOptim describes reducing Unity UGUI overdraw by removing geometry that contributes no visible pixels. The case examines irregular background sprites, hidden selection-state graphics, and hollow frames.

Three proposed changes are enabling tight sprite meshes with the Image component's sprite-mesh option, enabling transparent-mesh culling for fully hidden elements, and using sliced frame images with their center fill disabled. The post uses Unity's overdraw visualization to identify candidates and describes the difference between removing transparent corners, excluding a complete hidden element, and omitting a frame's empty center.

These are concrete checks for a mobile UI optimization pass. Preserve appearance while comparing GPU cost and generated geometry on representative hardware.

Evidence limit: this is a practitioner writeup with no numerical before/after timing. Its claims about mesh parameters, alpha propagation, and default rendering behavior were not independently verified. Check those details against the actual Unity version and Canvas configuration before adopting them as general rules.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
