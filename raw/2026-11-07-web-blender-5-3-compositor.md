---
"source": "https://developer.blender.org/docs/release_notes/5.3/compositor/"
"title": "Blender 5.3: Compositor"
"author": "Blender contributors"
"date_published": "unknown"
"date_clipped": "2026-11-07"
"category": "Technical Art & Creator Tools"
"source_type": "web"
"release_status": "upcoming release candidate"
"release_status_source": "https://developer.blender.org/docs/release_notes/compatibility/"
---

# Blender 5.3: Compositor

Source: https://developer.blender.org/docs/release_notes/5.3/compositor/

Capture note: These are notes for upcoming Blender 5.3, listed as a release candidate in the [official compatibility index](https://developer.blender.org/docs/release_notes/compatibility/) at clipping. The original publication date is unavailable.

## Highlights

Compositor effects can now be stacked instead of being limited to a single node tree.

Playback caching makes playback more interactive, while bundles and other Geometry Nodes expand
the possibilities for customizing effects. Bloom is now just one click away!

---

### Scene Effects Stack

The Compositor can now use a stack of effects, similar to Geometry Nodes modifiers.
Each effect is its own node group, and its output is passed on to the next effect.

Find them in the Compositor tab of the Properties editor.
See all [Effects Stack](https://developer.blender.org/docs/release_notes/5.3/compositor/#effects-stack-and-viewer) changes.

[![Scene Compositor Effects Stack](https://developer.blender.org/docs/release_notes/5.3/images/compositor_stack_demo.jpg)](https://developer.blender.org/docs/release_notes/5.3/images/compositor_stack_demo.jpg)

The scene compositor effects stack, featuring Storm by [Blender Studio](https://studio.blender.org/).

---

### Caching & Performance

The interactive compositor now supports playback caching, with playback up to 2x faster on GPU.
The **Kuwahara** node is up to 10x faster on some systems.

See all [Playback and Performance](https://developer.blender.org/docs/release_notes/5.3/compositor/#playback-and-performance) changes.

[](https://developer.blender.org/docs/release_notes/5.3/videos/compositorPlaybackCache.mp4)

Playback cache in the Compositor.

---

### Geometry Nodes & Transform Gizmos

Added support for 17 Geometry Nodes, including bundles, math and logic nodes, and other utilities.

Plus, the **Translate**, **Scale** and **Transform** nodes now support gizmos.

See all [supported nodes](https://developer.blender.org/docs/release_notes/5.3/compositor/#nodes-that-are-now-supported), and [editor changes](https://developer.blender.org/docs/release_notes/5.3/compositor/#editor).

[](https://developer.blender.org/docs/release_notes/5.3/videos/compositorTransformGizmo.mp4)

Transform gizmo in the Compositor.

### Built-in Bloom

Bloom, the effect type in the Glare node, is now available as a built-in asset. It can be added as an effect in the
Compositor tab with just one click, bringing back a feature that was previously exclusive to EEVEE (legacy).

---

## Changelog

### Effects Stack and Viewer

- **Effects Stack**: The compositor now uses an effects stack instead of a single compositor node group. ([a45205780d](https://projects.blender.org/blender/blender/commit/a45205780d))
- **Viewer**: The compositor will now use the **Group Output** as a viewer if no viewer node exists. ([de8811526d](https://projects.blender.org/blender/blender/commit/de8811526d))
- **Default Node Tree**: Now a simple **Group Input** connected to a **Group Output**, with no **Render Layers** node. ([fa5c7fd6fd](https://projects.blender.org/blender/blender/commit/fa5c7fd6fd))
- **Node Groups**: The compositor now renders scenes referenced inside node groups. ([a939b4a6a2](https://projects.blender.org/blender/blender/commit/a939b4a6a2))
- **File Output**: The default file name of the **File Output** node is now `{blend_name}`, so rendered images are named by default after the current blend file instead of a hardcoded string. ([f8cb4d4b5f](https://projects.blender.org/blender/blender/commit/f8cb4d4b5f))

### Playback and Performance

- **Playback Caching**: The interactive compositor now supports playback caching. ([0f5669bbfb](https://projects.blender.org/blender/blender/commit/0f5669bbfb))
- **Playback**: Performance is up to 2x faster on GPU. ([431235eb02](https://projects.blender.org/blender/blender/commit/431235eb02))
- **Kuwahara**: Improved performance by 25% (CPU), 2x (Nvidia GPU), 10x (Apple GPU). ([PR#164617](https://projects.blender.org/blender/blender/pulls/164617))
- **Render Result**: No longer updated during preview. ([b11c155d7d](https://projects.blender.org/blender/blender/commit/b11c155d7d))
- **Viewer Images**: Rendering no longer writes to viewer images, but the interactive compositor is executed after rendering if the viewer is visible. ([2a6f98cf62](https://projects.blender.org/blender/blender/commit/2a6f98cf62))

### Editor

- **Gizmos**: Added gizmos for the **Translate**, **Scale** and **Transform** nodes. ([ca1ab1a3a7](https://projects.blender.org/blender/blender/commit/ca1ab1a3a7), [27fae947fe](https://projects.blender.org/blender/blender/commit/27fae947fe))
- **Text Info**: Overlay now supported by node editors. ([908d2a2b4a](https://projects.blender.org/blender/blender/commit/908d2a2b4a))

[![](https://developer.blender.org/docs/release_notes/5.3/images/compositorNodeTextInfo.png)](https://developer.blender.org/docs/release_notes/5.3/images/compositorNodeTextInfo.png)

Text Info overlay in the Compositor

### Assets

- **Bloom**: New built-in asset which, together with layered compositing, brings back EEVEE Bloom. ([91482a60ac](https://projects.blender.org/blender/blender/commit/91482a60ac))

### Geometry Nodes

17 nodes from Geometry Nodes are now supported by the Compositor.

#### Bundles

- Bundle socket and bundle nodes: **Get Bundle Item**, **Store Bundle Item**, **Combine Bundle**, **Typed Bundle**, and **Separate Bundle** ([b2a937ef91](https://projects.blender.org/blender/blender/commit/b2a937ef91))

#### Math and Logic

- **Boolean Math** ([e233152491](https://projects.blender.org/blender/blender/commit/e233152491))
- **Compare** ([19e0672d75](https://projects.blender.org/blender/blender/commit/19e0672d75))
- **Float to Int** ([150fb0cccd](https://projects.blender.org/blender/blender/commit/150fb0cccd))
- **Integer Math** ([fae91bee18](https://projects.blender.org/blender/blender/commit/fae91bee18))
- **Matrix SVD** ([d89c56e21a](https://projects.blender.org/blender/blender/commit/d89c56e21a))
- **Combine Transform** and **Separate Transform** ([d8016f9acf](https://projects.blender.org/blender/blender/commit/d8016f9acf))

#### Utilities

- **Hash Value** ([f09119ea5c](https://projects.blender.org/blender/blender/commit/f09119ea5c))
- **Random Value** ([7bb4c56c40](https://projects.blender.org/blender/blender/commit/7bb4c56c40))
- **Is Viewport** ([55b4559e6b](https://projects.blender.org/blender/blender/commit/55b4559e6b))
- **Import Text** ([65ce9dd801](https://projects.blender.org/blender/blender/commit/65ce9dd801))
- **Bone Info** ([2a704a6f0d](https://projects.blender.org/blender/blender/commit/2a704a6f0d))
