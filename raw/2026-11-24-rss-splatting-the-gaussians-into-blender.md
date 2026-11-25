---
source: "https://code.blender.org/2026/10/splatting-the-gaussians-into-blender/"
title: "Splatting the Gaussians into Blender"
author: "Anastasia Rudina"
date_published: "2026-10-30"
date_clipped: "2026-11-24"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# Splatting the Gaussians into Blender

Source: https://code.blender.org/2026/10/splatting-the-gaussians-into-blender/

In Blender 5.3, we are introducing initial support for 3D Gaussian splats! This enables importing, editing, and rendering of fast, high-quality scene captures.

A lot of groundwork has been done to integrate 3D Gaussian splats (gsplats) into Blender natively, and we’ll continue to refine our implementation in upcoming releases. In this post, we’ll outline how to use gsplats, how they’re implemented in Blender, and what the current limitations are.

[](https://code.blender.org/wp-content/uploads/2026/10/Start-dogwalk_rotate.mp4)

A photoscan of [DOGWALK](https://store.steampowered.com/app/3775050/DOGWALK/) assets as physical objects, rendered as Gaussian splats in Blender 5.3

[](https://code.blender.org/wp-content/uploads/2026/10/Start-overgrown_rotate.mp4)

A 3D scene from [OVERGROWN](https://studio.blender.org/projects/overgrown/), rendered as Gaussian splats in Blender 5.3

**What are Gaussian splats?**

3D Gaussian splatting is a recent rendering technique in which sets of photos are turned into a specific 3D reconstruction. This doesn’t produce a mesh, but a radiance field made of many tiny Gaussian blobs. It’s similar to a point cloud, but able to represent more varied structures. Gsplats can describe complex scenes with materials, lighting, transparency, hair, and fine details, all in a single object.

[## Getting Started](https://code.blender.org/2026/10/splatting-the-gaussians-into-blender/#getting-started)

Blender supports importing gsplats in the `.PLY` and `.SPZ` formats, and additionally can load them from USDs. Example gsplats files can be found online, created with professional capture tools, or even made with your phone. To showcase this, we made a demo file that captures the [DOGWALK](https://store.steampowered.com/app/3775050/DOGWALK/) game assets – which are real! – here at Blender HQ.

[Download dogwalk\_assets\_capture.ply](https://code.blender.org/wp-content/uploads/2026/10/dogwalk__assets_capture.ply_.zip?x95207)

To begin, simply drag a supported file format into the viewport and confirm your import.

![](https://code.blender.org/wp-content/uploads/2026/10/dogwalk_splat_in_blender-1024x642.webp?x95207)

A `.PLY` capture of DOGWALK assets, imported into Blender 5.3

[## Representation in Blender](https://code.blender.org/2026/10/splatting-the-gaussians-into-blender/#representation-in-blender)

In Blender, gsplats are implemented as a type of point cloud. To expose this, there is now a `Pointcloud Type` geometry node. In general, gsplats require a different set of attributes than point clouds. We use the following:

- **Position.** This is the same as the point cloud attribute.
- **Scaling.** This differs from point cloud radius and is a 3D vector, as splats can scale and stretch in three dimensions.
- **Rotation.** This is a quaternion rotation. Combined with scaling, this means they can form complex, non-uniform shapes.
- **Radiance.** This is not a color, but instead data that produces an emissive color in every direction. Under the hood, each splat stores spherical harmonics, which are coefficients that encode view-dependent lighting. For setting attributes in Geometry Nodes, be aware that these are split into `radiance:base` and `radiance:sh`, which contain the constant and view-dependent spherical harmonics coefficients respectively. Splat color can also be set directly when writing to the `radiance` attribute in Geometry Nodes.

By default gsplats use an emissive material, using the output of the `radiance` attribute. You can modify this in the shader editor for relighting or other purposes, though we should note that support for relighting – as shown below – is currently in an early stage.

![](https://code.blender.org/wp-content/uploads/2026/10/Representations-0-1024x677.png?x95207)

Geometry Nodes setup for splats set generation

![](https://code.blender.org/wp-content/uploads/2026/10/Representations-1-740x1024.png?x95207)

Relighting in EEVEE

All the built-in renderers support gsplats. They generally produce the same result, but there are technical differences you should be aware of.

[## EEVEE & Viewport](https://code.blender.org/2026/10/splatting-the-gaussians-into-blender/#eevee-viewport)

EEVEE and Workbench are rasterization-based, so their implementation is comparable to that of other gsplats renderers. In effect, the 3D Gaussian are projected towards the camera, each turning into a 2D quad for which a comparable 2D Gaussian is calculated. These transparent billboards are then drawn on top of each other, back to front, effectively “splatting” them into the camera.

[](https://code.blender.org/wp-content/uploads/2026/10/EEVEE-overgrown_backtofront.mp4)

We chose to use EEVEE’s `dithered` transparency mode for the initial implementation. This was much easier to get working than the usual sorting/tiling done by other renderers, and had far less friction with EEVEE’s architecture. It also promises better performance once we implement proper culling. For now, though, this stochastic approach is quite noisy, so you should increase EEVEE’s sample count (**Render > Sampling > Viewport/Render**) a bit when dealing with gsplats.

For Workbench, note that **Viewport Shading** settings are applied to all objects. In order for gsplats to look as you would expect them to in the Viewport, be sure to select **Viewport Shading > Lighting > Flat**.

![](https://code.blender.org/wp-content/uploads/2026/10/EEVEE-Settings-1024x639.png?x95207)

Setting Viewport Shading to Flat in Workbench gives the expected look during preview

[## Cycles](https://code.blender.org/2026/10/splatting-the-gaussians-into-blender/#cycles)

Cycles is a path-tracing engine, so the tricks that work for EEVEE (and other rasterization-based engines) don’t work that well: we can’t project splats towards the camera as this wouldn’t work for secondary rays. Instead, Cycles finds an intersection between every ray and a gsplat, at the point where it has maximum opacity along that ray.

![](https://code.blender.org/wp-content/uploads/2026/10/Cycles-Ray-to-Gaussian-Splat-point-intersection-edited-1-1024x747.png?x95207)

Visualization of ray-to-Gaussian splat point intersection

For opacity, we use a stochastic approach. Gsplats point opacity at the intersection is interpreted as a probability: the higher the opacity, the higher the likelihood of the intersection being accepted. This avoids memory-intensive state tracking, making it GPU-friendly.

**Learn more about the implemented approach**

More details on ray tracing for gsplats can be found in the papers [*3D Gaussian Ray Tracing: Fast Tracing of Particle Scenes*](https://gaussiantracer.github.io/) by Nicolas Moenne-Loccoz et al., and [*Stochastic ray tracing of transparent 3D Gaussians*](https://iliyan.com/publications/GaussianRayTracing/) by Xin Sun et al.

While working on this project, we made an interesting observation: implementing point opacity naively (by explicitly calculating a covariance matrix) leads to artifacts on large but very flat splats, which appear in some training scenes such as [‘Bicycle’](https://github.com/graphdeco-inria/gaussian-splatting/). We solved this by reordering the multiplications, similar to how we handled the intersection point calculation.

![](https://code.blender.org/wp-content/uploads/2026/04/Cycles-bicycle-numerical-issue-1024x576.webp?x95207)

Naive opacity evaluation

![](https://code.blender.org/wp-content/uploads/2026/04/Cycles-bicycle-numerical-solved-1024x576.webp?x95207)

Reshuffle the evaluation terms

Our approach allows for native integration of gsplats into Cycles (while supporting reflections, indirect lighting, etc.), but it impacts how render results appear across EEVEE and Cycles. Below is a comparison of a single splat, rendered from a shallow angle, as well as an actual 3D Gaussian volume.

![](https://code.blender.org/wp-content/uploads/2026/10/Single-Splat-Cycles.png?x95207)

Cycles, single splat

![](https://code.blender.org/wp-content/uploads/2026/10/Single-Splat-Volume.png?x95207)

Cycles, volume fitted to look like splat

![](https://code.blender.org/wp-content/uploads/2026/10/Single-Splat-EEVEE.png?x95207)

EEVEE, single splat

As you can see, this is very close to a volume (it has the same perspective transform), but differs from the rasterized approach. This has the advantage of being fully compatible with global illumination algorithms, but differs slightly from most rasterized gsplat implementations, such as the one in EEVEE.

Cycles also implements initial support for re-lighting, as shown below. On the left is the original scene, and on the right is a diffuse shader applied on the gsplat, which is lit by a point light.

Original splat
![Original splat](https://code.blender.org/wp-content/uploads/2026/04/Cycles-Scene-Original.webp?x95207)

Splat lit by an artificial light
![Splat lit by an artificial light](https://code.blender.org/wp-content/uploads/2026/04/Cycles-Scene-Relit.webp?x95207)

In order to support this, both Cycles and EEVEE need to estimate the gsplat’s “normal”. To avoid querying neighbor information (which would be too slow anyway) we estimate gsplat normals at the shading point. The idea is simple: assume the surface is represented by squished splats (think of a pancake 🙂); its normal then points in the direction of the smallest scale:

![](https://code.blender.org/wp-content/uploads/2026/10/Cycles-3D-Gaussian-Splat-Point-Normal-edited.png?x95207)

This is a very basic approach to calculating normals, but it allows for simple relighting. The idea is similar to the one described in the *Flattening 3D Gaussian* section of [*PGSR: Planar-based Gaussian Splatting for Efficient and High-Fidelity Surface Reconstruction*](https://zju3dv.github.io/pgsr/) by Danpeng Chen et al.

[## Render Comparisons](https://code.blender.org/2026/10/splatting-the-gaussians-into-blender/#render-comparisons)

Under the hood, Cycles and EEVEE use fundamentally different approaches to rendering splats. Generally, they look the same, but there are a few small differences. Splats in EEVEE are drawn as camera-oriented billboards, whereas in Cycles they are ray-oriented. While Cycles’ approach is perspective-correct on paper, most gsplat data is fitted with EEVEE’s approach in mind, and this is visible in some scenes. The images below, showing a [scene by Renderbricks](https://superspl.at/scene/04caae8c), present a worst-case scenario of the differences.

EEVEE
![EEVEE](https://code.blender.org/wp-content/uploads/2026/04/lego_eevee-1024x576.webp?x95207)

Cycles
![Cycles](https://code.blender.org/wp-content/uploads/2026/04/lego_cycles-1024x576.webp?x95207)

[Download Blender 5.3 Beta](https://builder.blender.org/download/daily/)

[## Future plans](https://code.blender.org/2026/10/splatting-the-gaussians-into-blender/#future-plans)

While having native integration of 3D Gaussian splats is great, there’s plenty of work that remains to be done.

- Render performance in EEVEE can be improved; splats behind other splats are often drawn unnecessarily. This is especially bad on low-powered devices which can’t handle high overdraw. It is a good motivation to improve our GPU culling in future versions of Blender.
- Editing tools in Blender are the same as they’ve always been for point clouds, and are starting to feel somewhat clunky in this regard.
- Relighting currently uses the splat radiance, which is view-dependent. For improved relighting, we might want to look into albedo extraction.

EEVEE & Cycles

[## [Gaussian Splatting Improvements](https://fund.blender.org/?roadmap_project=gaussian-splatting-improvements)](https://code.blender.org/2026/10/splatting-the-gaussians-into-blender/#gaussian-splatting-improvements)
![](https://code.blender.org/wp-content/uploads/2026/10/gsplat_improvements_thumb.webp?x95207)

Performance and tool improvements to the 3D Gaussian Splats features added in Blender 5.3.

[See more roadmap projects](https://www.blender.org/roadmap/)

---
