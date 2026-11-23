---
source: "https://developer.blender.org/docs/release_notes/5.3/assets"
title: "Blender 5.3: Assets"
author: "Blender Foundation"
date_published: "unknown"
date_clipped: "2026-11-23"
category: "Technical Art & Creator Tools"
source_type: "web"
---

Source: https://developer.blender.org/docs/release_notes/5.3/assets

# Blender 5.3: Assets

## Highlights

Asset Libraries can now be shared as extensions, making assets in online libraries easier to maintain across Blender
versions. Online libraries can also require authentication, and the Asset Browser/Shelves receive several usability improvements.

### Extension Integration

Asset Libraries meet Extensions. Extensions can now reference remote asset libraries and optionally share authentication
tokens to control access.

The Extensions platform now accepts Asset Libraries containing Public Domain (CC0) assets. Learn more in the [announcement](https://forum.blender.org/t/asset-libraries-extensions-platform/45779).

### Asset Replacement for Online Libraries

Assets in online/remote libraries can now be 'replaced' with versions for newer Blender releases. For example, an asset
originally made for Blender 5.2 can be replaced with one for Blender 5.3. This works by saving the new version in a
separate blend file with `@b5_3` added to its name:

- `my_asset.blend`: the original asset for Blender 5.2
- `my_asset@b5_3.blend`: the replacement for Blender 5.3

When the [library listing is generated](https://docs.blender.org/manual/en/5.3/files/asset_libraries/remote_asset_libraries.html#creating-a-remote-asset-library), it will mark the assets in `my_asset.blend` for use up to (but not including) Blender 5.3, and those in `my_asset@b5_3.blend` for use from Blender 5.3 onwards. This can be extended indefinitely: a third file,
`my_asset@b47_0.blend`, will become available in Blender 47.0, while the assets in `my_asset@b5_3.blend` will continue to be used in earlier versions.

### Authentication

Remote Asset Libraries can now specify an access token to require [authentication](https://docs.blender.org/manual/en/5.3/files/asset_libraries/remote_asset_libraries.html#access-token) when accessing and downloading their content.

---

## Changelog

### Online/Remote Libraries

- **Extension Integration**: Asset Library extensions are now supported. Extensions can reference remote asset libraries, optionally sharing the authentication token from the extension repository. ([fbf13b7378](https://projects.blender.org/blender/blender/commit/fbf13b73789638a4913f3a27a31aa502bc3017e1))

### Asset Browser

- **Catalogs**: Assets in external (`.asset.blend`) files can now be moved between catalogs by dragging them to the catalog in the Asset Browser. ([83c9c7ee12](https://projects.blender.org/blender/blender/commit/83c9c7ee12cba342e6cb66b8803a8e3ec156c0c2))
- **Rename**: Assets in external (`.asset.blend`) files can now be renamed from the *Asset* pulldown menu, and from the Sidebar in the Asset Browser. ([06493bc4f0](https://projects.blender.org/blender/blender/commit/06493bc4f0))
- **Essentials Library**: The *Unassigned* catalog no longer shows up, since it would always be empty. ([9812445b18](https://projects.blender.org/blender/blender/commit/9812445b18))

### Asset Shelves

- **Empty Shelves**: Asset shelves that don't show any assets now show a label indicating why, for example because there are no assets or because a filter setting is active. ([06e66393d3](https://projects.blender.org/blender/blender/commit/06e66393d3))

### General

- **Asset Menu**: General asset operators are now also available in the "Asset" menu in the header. ([1807650fcd](https://projects.blender.org/blender/blender/commit/1807650fcd))
