---
source: "https://developer.blender.org/docs/release_notes/5.2/assets/"
title: "Assets - Blender Developer Documentation"
author: "Blender Developers"
date_published: "unknown"
date_clipped: "2026-06-12"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Blender 5.2 LTS: Assets[¶](#blender-52-lts-assets "Permanent link")

## Online Asset Libraries[¶](#online-asset-libraries "Permanent link")

It is now possible to register remotely hosted asset libraries, browse them from within Blender, and download assets as needed. This requires *Allow Internet Access* to be enabled in the Preferences.

## Online Essentials[¶](#online-essentials "Permanent link")

The *Essentials* asset library that comes with Blender was extended with a number of online hosted assets. They will appear together with other essentials assets when *Allow Internet Access* is enabled in the Preferences.

## Other Features[¶](#other-features "Permanent link")

- Setting up asset libraries in the Preferences has moved to a dedicated *Asset Libraries* page in the Preferences.
- The list of asset libraries in the Preferences now includes "All Libraries" and "Essentials" as entries. ([625e8c1e9d](https://projects.blender.org/blender/blender/commit/625e8c1e9d))
- Top-level catalogs named "Compositing" or "Geometry Nodes" will be ignored when corresponding menus are built from the catalog hierarchy ([80f0384224](https://projects.blender.org/blender/blender/commit/80f0384224)). For example, geometry nodes assets stored in a *Geometry Nodes > Generate* catalog will be displayed under *Generate* in the *Add Modifier* menu, or the Geometry Node Editor's *Add* menu. Assets directly placed inside *Compositing* or *Geometry Nodes* catalogs will show up under *Unassigned* in the menus.
- The *Follow Preferences* option in the Asset Browser import settings has been renamed to *Follow Asset or Preferences* ([e428159ecc](https://projects.blender.org/blender/blender/commit/e428159ecc))
- It's possible to specify a *Preferred Import Method* to use for individual assets. Importing an asset will use this method if *Follow Asset or Preferences* is selected as *Import Method* in asset browsers. ([e428159ecc](https://projects.blender.org/blender/blender/commit/e428159ecc))
- Asset Shelves behave better when asset libraries get deleted from the Preferences ([a274875eeb](https://projects.blender.org/blender/blender/commit/a274875eeb))

Back to top
