---
source: "https://developer.blender.org/docs/release_notes/5.3/modeling"
title: "Blender 5.3: Modeling & UV"
author: "unknown"
date_published: "unknown"
date_clipped: "2026-11-22"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Blender 5.3: Modeling & UV

## Highlights

Blender 5.3 adds a new Quad-Sphere primitive and brings three Loop Tools operators as native operators. Edit mode also gains selected dimensions in the transform panel and snapping to object origins.

### Quad-Sphere

The Quad-Sphere, commonly used in sculpting and subdivision modeling, is now available as a mesh primitive.

[![](https://developer.blender.org/docs/release_notes/5.3/images/modeling_quad_sphere_primitive.webp)](https://developer.blender.org/docs/release_notes/5.3/images/modeling_quad_sphere_primitive.webp)

New Quad-Sphere Primitive

### Native Loop Tools

The complete Loop Tools add-on functionality is now built into Blender. The last three operators are native too, with clearer names that describe their function:

- ‘Relax’ → ‘Relax Edge Loops’
- ‘Curve’ → ‘Curve Edge Loops Between Selected’
- ‘Gstretch’ → ‘Fit Edge Loops To Annotation’

[![](https://developer.blender.org/docs/release_notes/5.3/images/modeling_loop_tools.jpg)](https://developer.blender.org/docs/release_notes/5.3/images/modeling_loop_tools.jpg)

New Loop Tools Operators

---

## Changelog

### Mesh Editing

- **Transform Panel**: Edit mode now shows the selection's dimensions under the median, in the same global/local space. Dimensions can be edited, scaling the selection around the transform pivot point. ([8c212489ab](https://projects.blender.org/blender/blender/commit/8c212489abec1681f32c40530688c0aa81e57f1f))
- **Snapping**: New Origin snapping option, which allows snapping to the origin of objects in the scene. ([b9fe4691da](https://projects.blender.org/blender/blender/commit/b9fe4691da0214244253d516d03256468f611242))

#### Loop Tools

- "Relax" from the Loop Tools add-on is now built in as Relax Edge Loops. ([59a996b74b](https://projects.blender.org/blender/blender/commit/59a996b74ba296d6554760a22aabe801c4049560))
- "Curve" from the Loop Tools add-on is now built in as Curve Edge Loops Between Selected. ([1492833582](https://projects.blender.org/blender/blender/commit/14928335828e2fc6f784291b024f0a689d9a0150))
- "Gstretch" from the Loop Tools add-on is now built in as Fit Edge Loops To Annotation. ([b0eb9c6fc2](https://projects.blender.org/blender/blender/commit/b0eb9c6fc277eae5631b0a1bdedeae3ab3e2a4dd))

### Primitives

- **Quad-Sphere**: Added as a mesh primitive. ([ef062185d5](https://projects.blender.org/blender/blender/commit/ef062185d552718e4e9a927e853486505ca3f443))
