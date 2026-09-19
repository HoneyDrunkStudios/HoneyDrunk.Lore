---
source: "https://code.blender.org/2026/05/cycles-texture-cache"
title: "Cycles Texture Cache"
author: "Brecht Van Lommel"
date_published: "2026-05-01"
date_clipped: "2026-09-19"
category: "Technical Art & Creator Tools"
source_type: "rss"
capture_format: "attributed-summary"
---

# Cycles Texture Cache

Source: [Cycles Texture Cache](https://code.blender.org/2026/05/cycles-texture-cache)

*Attributed summary of the fetched written article; not a verbatim reproduction.*

Brecht Van Lommel describes a Cycles texture cache being developed for Blender 5.2 LTS. It loads needed image tiles and mip levels from generated tx files rather than keeping every full texture resident.

The May article explains automatic cache generation, controls for production pipelines, and command-line conversion. GPU misses are accumulated, missing tiles are loaded in batches, and kernels are relaunched. Wavefront path tracing helps hide loading latency; replayed kernels must avoid unintended side effects.

Cache eviction uses render-tile progress. Smaller render tiles can reduce memory pressure at a performance cost. Lower texture-resolution settings also help viewport memory and load time. Benefits depend on scene composition and how much memory textures consume relative to geometry.

HoneyDrunk implication: evaluate cache generation and storage as explicit asset-pipeline steps, then measure representative scenes and hardware. This capture preserves the publication's development status and listed unfinished work; it does not independently establish current release availability or support for every texture configuration.
