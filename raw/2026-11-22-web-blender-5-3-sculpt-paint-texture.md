---
source: "https://developer.blender.org/docs/release_notes/5.3/sculpt"
title: "Blender 5.3: Sculpt, Paint, Texture"
author: "unknown"
date_published: "unknown"
date_clipped: "2026-11-22"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Blender 5.3: Sculpt, Paint, Texture

## Highlights

Sculpting and painting get better support for detailed meshes: Multires now shows textures and color attributes in Sculpt Mode, and Vertex Paint and Weight Paint gain Automasking. Weight Paint ships with updated brushes and defaults, alongside other improvements in sculpting and painting.

### Multires: Textures & Color Attributes

Meshes with a Multires modifier now display textures in Sculpt Mode.

| Blender 5.2 | Blender 5.3 |
| --- | --- |
| Textures and Color Attributes are black | Displayed properly in EEVEE & Solid rendering |

[All Sculpt Mode changes.](https://developer.blender.org/docs/release_notes/5.3/sculpt/#sculpt-mode)

---

### Automasking in Vertex & Weight Paint

[![](https://developer.blender.org/docs/release_notes/5.3/images/automasking_in_more_modes2.png)](https://developer.blender.org/docs/release_notes/5.3/images/automasking_in_more_modes2.png)

Automasking in Vertex Paint mode

Automasking is now supported in Vertex Paint and Weight Paint modes. The following options can be toggled and customized:

- Topology
- Mesh Boundary
- Cavity & Inverted Cavity
- View Normal
- Area Normal

The *Front Face Falloff* option is now deprecated in favor of the new Automasking settings.

[All Mesh Painting changes.](https://developer.blender.org/docs/release_notes/5.3/sculpt/#mesh-painting)

---

### Weight Paint Defaults

[![](https://developer.blender.org/docs/release_notes/5.3/images/weight-paint-settings.webp)](https://developer.blender.org/docs/release_notes/5.3/images/weight-paint-settings.webp)

Weight Paint Updates

The bundled essential Weight Paint brushes have been updated:

- The default brush is now the "Add Weight" brush, which uses the "Add" blend mode, accumulation, and a low strength.
- The existing "Paint" brush is renamed to "Set Weight" and now has a Constant falloff curve. This brush also has a new icon to distinguish it from the "Add Weight" brush.
- The "Blur" brush has been changed to use accumulation with a low strength.
- For all brushes, the stroke spacing has been changed to 5% to feel more responsive.
- For all brushes which formerly used a Custom falloff curve that approximated a smoothstep function, the built-in "Smooth" curve is now used.
- The brush asset shelf now shows by default.

Weight Paint defaults have also been updated: *Multi-Paint*, *Auto-Normalize*, and *Mirror Vertex Groups* are now enabled by default.

[All Weight Paint changes.](https://developer.blender.org/docs/release_notes/5.3/sculpt/#weight-paint)

---

## Changelog

### General

- **Unified Paint Settings**: Toggles (e.g. size, strength, color) are now stored per brush rather than per scene, allowing individual brushes to opt into using the scene-level settings. ([6ecfe4e810](https://projects.blender.org/blender/blender/commit/6ecfe4e810ee635d9826a326ffe44b218e99bd7b))

### Mesh Painting

- **Automasking**: Now supported in Vertex Paint and Weight Paint, with Topology, Mesh Boundary, Cavity, View Normal, and Area Normal options. ([8704773557](https://projects.blender.org/blender/blender/commit/8704773557367b9955894409616bb13b9d5c064a))
- **Front Face Falloff**: Deprecated in Vertex Paint and Weight Paint in favor of the recently introduced Automasking settings. ([ec438d7429](https://projects.blender.org/blender/blender/commit/ec438d7429e51b33ff8958da0c21def018d43835))
- **Sample Colors**: Color attributes on the *Corner* domain are now sampled accurately, instead of resulting in an interpolated vertex value. ([ea0e364e90](https://projects.blender.org/blender/blender/commit/ea0e364e908ba344a9102ba1b8027ac3d4cbdaa8))

### Sculpt Mode

- **Multires Attributes**: Generic mesh attributes (e.g. color attributes) are now interpolated and displayed when a Multires modifier is used. ([0932e76171](https://projects.blender.org/blender/blender/commit/0932e7617164e93ad370ecb23a1d898f2f7ad32d))
- **Multires Textures**: Textures are now displayed for meshes with a Multires modifier. ([0ad469cb92](https://projects.blender.org/blender/blender/commit/0ad469cb922264c2aa20cec128219410e23c2b2e))
- **Transform Only Pivot**: New option to control the pivot placement with the transform gizmo without affecting the object geometry. ([3b2ab96ff1](https://projects.blender.org/blender/blender/commit/3b2ab96ff1d975ddb4f0f7f2e4e76e976fc36fac))
  [![](https://developer.blender.org/docs/release_notes/5.3/images/move_pivot.png)](https://developer.blender.org/docs/release_notes/5.3/images/move_pivot.png)

  A toggle to only move the Gizmo
- **Cursor**: Brushes with cube tips via the *Roundness* and *Tip Scale X* settings now display a rounded box cursor on the mesh. ([1c2aa3581b](https://projects.blender.org/blender/blender/commit/1c2aa3581b37d89e72f5a3742e8316450b3f1dbb))
  [![](https://developer.blender.org/docs/release_notes/5.3/images/brush_tip_shape.png)](https://developer.blender.org/docs/release_notes/5.3/images/brush_tip_shape.png)

  Soft square brush tip shape for the Clay Strips brush
- **Brush Curves**: *Hardness*, *Auto-Smooth*, and *Spacing* can now use a custom curve; the *Invert Pressure for Hardness* toggle is removed from the UI and deprecated. ([8f909f9abd](https://projects.blender.org/blender/blender/commit/8f909f9abd205f26b43fcd59cb4e61614746a8e5))
    
  [Media reference](https://developer.blender.org/docs/release_notes/5.3/videos/more_pressure_curves.mp4)

### Weight Paint

- **Brushes**: Updated the bundled essential brushes: new default "Add Weight" brush, "Paint" renamed to "Set Weight", and more. ([010b904e5a](https://projects.blender.org/blender/blender/commit/010b904e5ab8e8641bed2667b3e4328721e54c6a))
- **Defaults**: Multi-Paint, Auto-Normalize, and Mirror Vertex Groups are now enabled by default. ([010b904e5a](https://projects.blender.org/blender/blender/commit/010b904e5ab8e8641bed2667b3e4328721e54c6a))

### Texture Paint

- **Undo/Redo**: Optimized for high resolution images and UDIMs. ([#162768](https://projects.blender.org/blender/blender/issues/162768))
- **Image Updates**: Efficient update of image textures and mipmaps is now supported in material draw mode and EEVEE. ([#161392](https://projects.blender.org/blender/blender/issues/161392))

### Curves Sculpting

- **Cut Curves**: New brush for hair sculpt mode. ([8ebfcce398](https://projects.blender.org/blender/blender/commit/8ebfcce398ffdd1a9f3ee0544cb5b66eec55d32f))
    
  [Media reference](https://developer.blender.org/docs/release_notes/5.3/videos/cut_curves_brush.mp4)
