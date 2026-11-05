---
source: "https://developer.blender.org/docs/release_notes/5.3/eevee/"
title: "Blender 5.3: EEVEE & Viewport"
author: "unknown"
date_published: "unknown"
date_clipped: "2026-11-05"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Blender 5.3: EEVEE & Viewport

Capture note: These are upcoming Blender 5.3 release notes. The official compatibility index lists 5.3 as a November 2026 release candidate at capture time; this is not confirmation of a final release. [Release status](https://developer.blender.org/docs/release_notes/compatibility/).

## Highlights

EEVEE gains Material Lighting nodes for precise control over how materials react to lights, support for panoramic cameras,
and full Sky Texture sun disc support. The Vulkan backend becomes the default on Windows (not ARM) and Linux
with lower minimum requirements, and Workbench can use hardware raytraced shadows on Metal and Vulkan.

---

### Material Lighting Nodes

Material Lighting nodes allow authoring how the Material reacts to Lights.
This can, for example, be used for toon and stylized shading, but also for complex physical effects like iridescence.

The new nodes are:

- Light Accumulation: Evaluates its inputs for each scene light and accumulates the result. ([manual](https://docs.blender.org/manual/en/5.3/render/shader_nodes/shader/light_accumulation.html))
- Light Info: Exposes light data properties (Color, Power, and Position). ([manual](https://docs.blender.org/manual/en/5.3/render/shader_nodes/input/light_info.html#bpy-types-shadernodelightinfo))
- Light Evaluation: Evaluates position dependent light properties (Diffuse/Specular Term, Attenuation Mask, Direction, Distance). ([manual](https://docs.blender.org/manual/en/5.3/render/shader_nodes/input/light_evaluation.html#bpy-types-shadernodelightevaluation))
- Shadow Raycast: Outputs a shadow mask value for the light being shaded. ([manual](https://docs.blender.org/manual/en/5.3/render/shader_nodes/input/shadow_raycast.html#bpy-types-shadernodeshadowraycast))
- Attribute (Light Mode): Queries custom properties from the Light Object/Data being evaluated. ([manual](https://docs.blender.org/manual/en/5.3/render/shader_nodes/input/attribute.html#bpy-types-shadernodeattribute))
- Vector Transform (Light Space): Transforms coordinates from/to the local space of the Light being evaluated. ([manual](https://docs.blender.org/manual/en/5.3/render/shader_nodes/utilities/vector/transform.html#bpy-types-shadernodevectortransform))

[](../videos/cowboi-test_shot-v002-1080p.mp4)

[Cowboi test shot render (by Blender Studio)](https://studio.blender.org/blog/announcing-cowboi/)

---

### Panoramic Camera Support

EEVEE can now render panoramic cameras: Equirectangular, Equiangular Cubemap Face, Fisheye Equidistant,
Fisheye Equisolid, Fisheye Lens Polynomial, Central Cylindrical, and Mirror Ball.

The following are not supported yet:

- Depth of field.
- Raytracing.
- Volumetrics temporal reprojection in viewport.

Fisheye Equisolid:

| EEVEE | Cycles |
| --- | --- |
|  |  |

Equiangular Cubemap Face:

| EEVEE | Cycles |
| --- | --- |
|  |  |

Equirectangular:

| EEVEE | Cycles |
| --- | --- |
|  |  |
| Scene by Aleš Jelovčan. |  |

---

### Sky Texture Sun Disc

Sky textures now fully support the sun disc.

**Breaking change:** scenes using a Sky Texture with **Sun Disc** enabled will look different from earlier versions,
because the sun disc now contributes to the lighting. To restore the previous look, disable Sun Disc.

[![Sun disc rendered in EEVEE](https://developer.blender.org/docs/release_notes/5.3/images/sky_texture_sun_disc_eevee.png)](https://developer.blender.org/docs/release_notes/5.3/images/sky_texture_sun_disc_eevee.png)

---

### Vulkan

The Vulkan backend is now default on Windows (not ARM) and Linux.
Minimum requirements have been lowered to Vulkan 1.1 and some GPU/driver features
have been made optional to support more devices.

| Test | OpenGL / 5.2.2 | OpenGL / 5.3 | Vulkan / 5.2.2 | Vulkan / 5.3 |
| --- | --- | --- | --- | --- |
| barbershop\_interior | 46.514 fps | 42.217 fps | 44.367 fps | 45.641 fps |
| blender290-fox | 18.087 fps | 18.306 fps | 19.302 fps | 19.462 fps |
| blender291-autumn | 179.108 fps | 192.686 fps | 259.255 fps | 282.065 fps |
| hatching | 589.670 fps | 597.090 fps | 930.304 fps | 902.697 fps |
| rain\_restaurant | 23.748 fps | 23.737 fps | 34.657 fps | 35.056 fps |
| shader\_balls | 141.286 fps | 140.205 fps | 238.382 fps | 225.729 fps |
| sponza | 427.552 fps | 416.793 fps | 436.526 fps | 493.228 fps |

Benchmark system: AMD Ryzen 7950X with NVIDIA RTX 6000 (Ada) on Linux 7.0 using 595.91.07 driver.
Timings are an average of 3 runs.

---

### Hardware Raytraced Shadows in Workbench

Available on Metal and Vulkan. They can be enabled in the `Preferences > Viewport > Quality` settings.
The option will be shown as inactive if the current backend/GPU doesn't support hardware ray queries.
A new `gpu.capabilities.ray_query_support_get()` has been added to the Python API to support this UI functionality.

The visual results are the same as the stencil shadows implementation, but it provides a significant performance boost on modern hardware.

---

## Changelog

### EEVEE

- **Material Lighting Nodes**: New nodes to author how the Material reacts to Lights. ([PR#161429](https://projects.blender.org/blender/blender/pulls/161429), [PR#164214](https://projects.blender.org/blender/blender/pulls/164214))
- **Panoramic Cameras**: EEVEE can now render panoramic cameras. ([PR#159474](https://projects.blender.org/blender/blender/pulls/159474))
- **Sky Texture**: The sun disc is now fully supported. ([PR #163132](https://projects.blender.org/blender/blender/pulls/163132))

#### Fixes

- High sample count no longer produces banding on soft shadows. ([PR#161958](https://projects.blender.org/blender/blender/pulls/161958))
- Sphere light probes are now captured using 32 bit float for more precise sun light extraction. ([PR#163132](https://projects.blender.org/blender/blender/pulls/163132))
- Area lights no longer cause light leakage on the backs of objects under high exposure. ([PR#161262](https://projects.blender.org/blender/blender/pulls/161262))
- Light probes are now compatible with Scale Cage tool. ([PR#163793](https://projects.blender.org/blender/blender/pulls/163793))
- Refraction no longer shows discontinuities at high roughness. ([PR#165092](https://projects.blender.org/blender/blender/pulls/165092))
- Dithered transparency no longer shows line artifacts when slightly further from origin. ([PR#164608](https://projects.blender.org/blender/blender/pulls/164608))

### Viewport

- **Overlay**: Anti-aliased mesh normal line drawing. ([PR#161025](https://projects.blender.org/blender/blender/pulls/161025))
- **Overlay**: Anti-aliased mesh lines no longer break in x-ray mode. ([PR#160231](https://projects.blender.org/blender/blender/pulls/160231))
- **Overlay**: Image editor grid is properly centered again. ([PR#165042](https://projects.blender.org/blender/blender/pulls/165042))
- **Workbench**: Hair metallic material property is no longer randomized. ([PR#161291](https://projects.blender.org/blender/blender/pulls/161291))

### Vulkan

- Vulkan backend is now default on Windows (not ARM) and Linux. ([PR#158803](https://projects.blender.org/blender/blender/pulls/158803))
- Vulkan minimum requirements lowered to Vulkan 1.1, with some GPU/driver features made optional to support more devices. ([e3a49cdebc](https://projects.blender.org/blender/blender/commit/e3a49cdebcc7692e495e3309804325771aea38d5))
