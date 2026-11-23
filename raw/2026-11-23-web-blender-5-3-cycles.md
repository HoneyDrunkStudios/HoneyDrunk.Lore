---
source: "https://developer.blender.org/docs/release_notes/5.3/cycles"
title: "Blender 5.3: Cycles"
author: "Blender Foundation"
date_published: "unknown"
date_clipped: "2026-11-23"
category: "Technical Art & Creator Tools"
source_type: "web"
---

Source: https://developer.blender.org/docs/release_notes/5.3/cycles

# Blender 5.3: Cycles

## Highlights

Cycles gains dispersion and roughness anisotropy for glass and transmissive materials, and a new DLSS denoiser
for the viewport on NVIDIA GPUs. Viewport renders now pause during final renders, texture baking quality is improved,
and several GPU render optimizations land alongside support for NVIDIA RTX Spark devices.

### Shader Nodes

The Principled BSDF now supports **Dispersion**, available in the Transmission panel.
It can be used to render glass or diamonds that split white light into rainbow colors. Learn more in the [user manual](https://docs.blender.org/manual/en/5.3/render/shader_nodes/shader/principled.html#transmission).

[](../videos/cycles_dispersion_christopher3d.mp4)

Dispersion showcase by Christopher 3D

**Roughness anisotropy** is now supported by the Glass BSDF and the transmission component of the Principled BSDF.
It works the same as the roughness anisotropy for the specular reflection. See all [Shader Nodes](https://developer.blender.org/docs/release_notes/5.3/cycles/#shader-nodes) changes.

### NVIDIA DLSS

On NVIDIA GPUs, a new DLSS denoiser is available for the viewport. It provides a cleaner image faster through
upscaling and reusing samples from previous frames. [Learn more](https://projects.blender.org/blender/blender/pulls/153077).

**Note: DLSS denoising requires NVIDIA driver version 620 or newer.**

---

## Changelog

### Shader Nodes

- **Dispersion**: Added to the Principled BSDF Transmission panel. ([#162041](https://projects.blender.org/blender/blender/issues/162041))
- **Roughness Anisotropy**: Now supported by the Glass BSDF and the transmission component of the Principled BSDF. ([#163343](https://projects.blender.org/blender/blender/issues/163343))

### Denoising

- **DLSS**: New DLSS denoiser for the viewport on NVIDIA GPUs. ([#153077](https://projects.blender.org/blender/blender/issues/153077))

### Others

- **Viewport**: Viewport renders are automatically paused during final renders. ([#156536](https://projects.blender.org/blender/blender/issues/156536))
- **Baking**: Texture baking quality improved for small or thin triangles and near margins. ([#161752](https://projects.blender.org/blender/blender/issues/161752))
- **GPU**: Minor GPU render optimizations. ([#163436](https://projects.blender.org/blender/blender/issues/163436), [#161876](https://projects.blender.org/blender/blender/issues/161876))
- **NVIDIA RTX Spark**: Support for NVIDIA RTX Spark devices running Windows 11, including unified memory optimizations.
