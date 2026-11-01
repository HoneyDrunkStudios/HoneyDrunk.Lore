---
source: "https://developer.blender.org/docs/release_notes/5.3/rendering/"
title: "Blender 5.3: Rendering"
author: "unknown"
date_published: "unknown"
date_clipped: "2026-11-01"
category: "Technical Art & Creator Tools"
source_type: "web"
release_channel: "upcoming"
capture_note: "Development release notes captured before Blender 5.3 final; limitations and planned behavior may change."
---

# Blender 5.3: Rendering

Source: https://developer.blender.org/docs/release_notes/5.3/rendering/

Blender 5.3 adds 3D Gaussian Splats: import, point cloud support, Geometry Nodes integration, and rendering in
Workbench, EEVEE, and Cycles. Shader Nodes gain several nodes previously exclusive to Geometry Nodes, and
Color Management improves interoperability between blend files and assets created with different OpenColorIO configurations.

---

## Highlights

[![Gaussian Splat Example](https://developer.blender.org/docs/release_notes/5.3/images/render_gsplat.png)](https://developer.blender.org/docs/release_notes/5.3/images/render_gsplat.png)

Gaussian Splat Example

## 3D Gaussian Splats

3D Gaussian splats are commonly used to reconstruct 3D scenes from photos or video.
They are made up of many small, soft, transparent blobs that together can represent many types of geometry and shading.

Blender can now import them from PLY and SPZ files, store them in point clouds, process them with Geometry Nodes,
and render them with all render engines.

[All Gaussian Splat changes.](https://developer.blender.org/docs/release_notes/5.3/rendering/#gaussian-splats)

---

### Point Cloud Data-Block

Gaussian splats are represented as point clouds. For this, a `Type` option has been added to the PointCloud data-block:

* `Points`: the point cloud behaves the same as before.
* `3D Gaussian Splats`: the point cloud is rendered using the original Gaussian splat technique.
  In the future it will also affect the behavior of transforming the point cloud object (for example, rigging).

Point clouds used as 3D Gaussian splats have extra attributes:

| Attribute | Description | Type |
| --- | --- | --- |
| `scale` | Scale of the Gaussian splat. | Vector |
| `rotation` | Rotation of the Gaussian splat. | Quaternion |
| `radiance:base` | Base (DC) radiance of the splats, followed by opacity. | 4D Vector |
| `radiance:sh_{index}` | Coefficients of the spherical harmonics bands >= 1. The order is `<L=1 M=-1>`, `<L=1 M=0>`, `<L=1 M=1>`, `<L=2 M=-2>` ... where `L` is the band index and `M` is the basis function. | Vector |

---

### Import

Import from PLY and SPZ files is supported. There is currently no export support.

* **PLY**: the importer automatically detects whether the file represents a 3D Gaussian Splat based on the geometry and attributes.
  The typical convention for the coordinate system is `Z` as the Forward axis and `-Y` as the Up axis.
* **SPZ**: all current versions of the format are supported (up to and including 4).
  The importer automatically converts the coordinate system to Blender's Up and Forward convention.
  However, not all software saves SPZ files in its convention, so manual adjustment might be required.

### Geometry Nodes

* New `Set Point Cloud Type` node.
* New `Import SPZ` node.
* The `Import PLY` node now detects whether the file represents a 3D Gaussian Splat and outputs it as a point cloud, otherwise it outputs a mesh.
  For this reason the output socket has been renamed to `Geometry`.

---

### Rendering

All render engines, including Workbench, EEVEE, and Cycles, are able to render 3D Gaussian Splats.

By default, a 3D Gaussian Splat is rendered using an emissive shader. It is not required to create it explicitly.
The `radiance` attribute provides access to the resolved radiance of the splat at the current shading point.

[![Default shader of a Gaussian Splat.](https://developer.blender.org/docs/release_notes/5.3/images/render_gsplat_default_material.png)](https://developer.blender.org/docs/release_notes/5.3/images/render_gsplat_default_material.png)

Default shader of a Gaussian Splat.

There is rudimentary support for making the splat relightable by replacing the `Emission` node with a hard surface BSDF such as `Diffuse BSDF``.

[![](https://developer.blender.org/docs/release_notes/5.3/images/render_gsplat_relight.png)](https://developer.blender.org/docs/release_notes/5.3/images/render_gsplat_relight.png)

Example of relit Gaussian Splat

### Limitations

* Performance is not ideal.
* The current assumption is that the Gaussian splats are trained in sRGB space (which is what most authoring software uses).
* Rendering is not fully correct, as Cycles and EEVEE operate in linear space. This is mainly visible in areas with low opacity/high radiance.
* `Apply Transform` on a Gaussian splat does not work correctly as it does not yet handle the new scale, rotation and spherical harmonics attributes.

---

## Changelog

### Gaussian Splats

* **Import**: Added support for 3D Gaussian Splats import (PLY, SPZ) and rendering. ([PR#163102](https://projects.blender.org/blender/blender/pulls/163102))
* **Geometry Nodes**: Added `Set Point Cloud Type` node. ([PR#163530](https://projects.blender.org/blender/blender/pulls/163530))
* **Geometry Nodes**: The `Import PLY` node now outputs a point cloud for Gaussian Splat files, otherwise a mesh; its output socket is renamed to `Geometry`. ([PR#163624](https://projects.blender.org/blender/blender/pulls/163624))
* **Geometry Nodes**: Added `Import SPZ` node.

### Shader Nodes

Seven nodes, previously only available in Geometry Nodes were added.

* **Index Switch** ([f5381d8e31](https://projects.blender.org/blender/blender/commit/f5381d8e31d156721202718195294c6e17309b78))
* **Switch** ([b4174fbb](https://projects.blender.org/blender/blender/commit/b4174fbb))
* **Boolean Math** ([6c74e82ecb](https://projects.blender.org/blender/blender/commit/6c74e82ecb0dc3ae992219f65439374e9112c349))
* **Integer Math** ([ba82476ade](https://projects.blender.org/blender/blender/commit/ba82476ade3c6762ce6763c2014d5d94a03b83ff))
* **Warning** ([70d2ff933f](https://projects.blender.org/blender/blender/commit/70d2ff933f95e3a750edc27298921972caf2043a))
* **Enable Output** ([ef0d14592f](https://projects.blender.org/blender/blender/commit/ef0d14592fc13958475ba654e461482e3978acf8))
* **Closures**: Recursive closures are now supported, with infinite loops prevented by enforcing a maximum stack limit. ([567c5be3ab](https://projects.blender.org/blender/blender/commit/567c5be3ab0dd77fc92c65efe8c252c4944ec668))
* **String Nodes** ([4fed7c4a27](https://projects.blender.org/blender/blender/commit/4fed7c4a2783d0f2b528be1dcec41b0a7f3c5e07))

  [](https://developer.blender.org/docs/release_notes/5.3/videos/shader_nodes_strings.mp4)

### Color Management

* **OpenColorIO**: Improved interoperability between blend files and assets created with different OpenColorIO configurations. ([#164213](https://projects.blender.org/blender/blender/issues/164213))
* **Projects**: Per project OpenColorIO configuration. ([Release Notes](https://developer.blender.org/docs/release_notes/5.3/core/#projects))
