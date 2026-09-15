---
source: "https://code.blender.org/2026/07/geometry-nodes-physics/"
title: "Geometry Nodes Physics"
author: "Jacques Lucke"
date_published: "2026-07-30"
date_clipped: "2026-09-15"
category: "Technical Art & Creator Tools"
source_type: "rss"
capture_format: "attributed-summary"
extraction_status: "full written page fetched; readable body reviewed"
---

# Geometry Nodes Physics

Source: [Geometry Nodes Physics](https://code.blender.org/2026/07/geometry-nodes-physics/)

## Attributed content summary

Jacques Lucke describes Blender 5.2 LTS hair and cloth dynamics built from Geometry Nodes assets around an XPBD solver. The source marks the new systems experimental while their design evolves.

High-level groups expose cloth controls and hair attachment behavior. Hair setup uses rest geometry to relate a surface's original and deformed states. Effectors include closed-mesh colliders, custom forces, and custom behavior injected at simulation stages. Collections or bundles supply effectors, and tags can limit which geometry they influence.

Advanced users can modify the supplied node groups or build directly around the solver, with the latter requiring more knowledge of typed bundles and attributes. The architecture aims to support multiple solvers beneath approachable assets rather than forcing every physical effect into one algorithm.

Fluid and rigid-body integration, solver interoperability, and additional collision work are described as ongoing development. Distinguish these plans from released capability. This is useful source material for procedural asset simulation and pipeline experiments, with production adoption dependent on stability and validation.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
