---
source: "https://developer.blender.org/docs/release_notes/5.3/python_api"
title: "Blender 5.3: Python API"
author: "Blender contributors"
date_published: "unknown"
date_clipped: "2026-11-14"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Blender 5.3: Python API

[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#blender-53-python-api "Permanent link")

## Highlights[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#highlights "Permanent link")

Blender 5.3 brings Python API additions across the UI, GPU, window manager and asset libraries. Color management
gains standard `interop_id` identifiers, and `OpenEXR` and `opentimelineio` are now available as built-in modules.

### Interoperability[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#interoperability "Permanent link")

Color spaces now store an interop ID alongside their name, exposed as `Image.colorspace_settings.interop_id`.
These are standard identifiers defined by the [Color Interop Forum](https://github.com/AcademySoftwareFoundation/ColorInterop),
which makes it possible to write code that works with any modern OpenColorIO configuration.
It also improves compatibility when loading or appending assets from blend files created with another OpenColorIO config:
on file load, color space names are updated from the interop IDs when available.
The existing `name` is kept, so Python API backwards compatibility is preserved.

```
settings.name = 'Non-Color Data'   # Old
settings.interop_id = 'data'       # New

settings.name = "sRGB"                       # Old
settings.interop_id = 'srgb_rec709_display'  # New

if settings.name == 'sRGB'                                               # Old
if settings.interop_id in {'srgb_rec709_scene', 'srgb_rec709_display'}:  # New
```

### Built-in Python Modules[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#built-in-python-modules "Permanent link")

Library dependencies were updated, exposing new Python modules for both existing and new dependencies.
The following modules are now available for Python developers to use:

- `OpenEXR` - see [OpenEXR Python module documentation](https://openexr.com/en/latest/python.html).
- `opentimelineio` - see [OpenTimelineIO Python module documentation](https://opentimelineio.readthedocs.io/en/latest/api/python/opentimelineio.html).

### Extension Asset Libraries[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#extension-asset-libraries "Permanent link")

The Python API can now create and inspect asset libraries that are defined by extensions.

- `asset_libraries.new()`: supports remote and extension defined libraries, with the new `remote_url` & `extension_id` arguments.
- `UserAssetLibrary.extension_id`: the extension defining the library.
- `UserAssetLibrary.is_available()`: checks that the library is enabled, and, if it comes from an extension, that the extension's repository is enabled too.
- `AssetLibrary.user_library`: the preferences entry for the library (or None).
- `UserExtensionRepo.use_access_token_for_asset_libraries`: enables asset libraries to use the repository's access token.

### Change in `bpy.data.all_ids` Order[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#change-in-bpydataall_ids-order "Permanent link")

The [all_ids](https://docs.blender.org/api/5.2/bpy.types.BlendData.html#bpy.types.BlendData.all_ids)
collection property internal implementation has been modified,
which changes the order in which IDs are placed in this collection.
The property's order is also now documented as internal implementation detail
(i.e. scripts should not rely or make assumptions on it).

---

## Changelog[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#changelog "Permanent link")

### Animation[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#animation "Permanent link")

- **Convert Rotation Mode**: New `convert_rotation_mode` function to convert animation between rotation modes, on [bpy.types.Object](https://docs.blender.org/api/5.3/bpy.types.Object.html#bpy.types.Object.convert_rotation_mode) and [bpy.types.PoseBone](https://docs.blender.org/api/5.3/bpy.types.PoseBone.html#bpy.types.PoseBone.convert_rotation_mode).
- **Constraints**: On Objects and PoseBones, `constraints.new(type, name)` now accepts an optional `name` keyword argument.
- **Markers**: New `context.markers` and `context.selected_markers` were added for simplified access to the relevant markers for the editor. ([3048200244](https://projects.blender.org/blender/blender/commit/3048200244b8acb082c5399bd8b2aab8170035dc))

### Asset Libraries[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#asset-libraries "Permanent link")

- **Extensions**: Support for extension defined asset libraries. ([fbf13b7378](https://projects.blender.org/blender/blender/commit/fbf13b73789638a4913f3a27a31aa502bc3017e1))

### Color Management[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#color-management "Permanent link")

- **Interop ID**: New `Image.colorspace_settings.interop_id` alongside the existing `name`. ([PR#164213](https://projects.blender.org/blender/blender/pulls/164213))

### Data[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#data "Permanent link")

- **All IDs Order**: The order of IDs in `bpy.data.all_ids` has changed, and is now documented as an internal implementation detail. ([PR#162179](https://projects.blender.org/blender/blender/pulls/162179), [53ed639726](https://projects.blender.org/blender/blender/commit/53ed639726b4cd1e34e4cd35467e7b1075c83d67))

### GPU[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#gpu "Permanent link")

- **Storage Buffers**: A new `gpu.types.GPUStorageBuf` was added to create and manage Storage Buffers. ([fae3d71db8](https://projects.blender.org/blender/blender/commit/fae3d71db804a569b5ee9bfab7650bd51f57172b))

### mathutils[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#mathutils "Permanent link")

- **KDTree**: Now supports 2D trees with a dimensions argument. ([e81d8ae45a](https://projects.blender.org/blender/blender/commit/e81d8ae45a76813d37b2bd7e204d1c4ae2ccfb2c))

### Node Editor[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#node-editor "Permanent link")

- **Interface**: New [`NodeTreeInterface.root_panel`](https://docs.blender.org/api/5.3/bpy.types.NodeTreeInterface.html#bpy.types.NodeTreeInterface.root_panel) for retrieving the top-level panel in the hierarchy of node tree interface items.

### Render Engine[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#render-engine "Permanent link")

- **Viewport Depth**: New `bl_write_viewport_depth` option that lets a render engine write its own depth buffer in `view_draw`. ([#163684](https://projects.blender.org/blender/blender/issues/163684))

### User Interface[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#user-interface "Permanent link")

- **Multiline Labels**: New [`UILayout.label_multiline()`](https://docs.blender.org/api/5.3/bpy.types.UILayout.html#bpy.types.UILayout.label_multiline) function to place labels that can automatically wrap to multiple lines.
- **Popups**: New `auto_keymap` argument to optionally support key accelerators in `WindowManager.invoke_popup` ([a9beda8c0f](https://projects.blender.org/blender/blender/commit/a9beda8c0ff2c6026d4e601ebeb1c6148181f541)), `WindowManager.popover` ([f4f16d48ea](https://projects.blender.org/blender/blender/commit/f4f16d48ea5b1a452ec6ddac6a79396086d374c7)) and `WindowManager.call_panel` ([e1a676b12b](https://projects.blender.org/blender/blender/commit/e1a676b12b81ca58c76c833873343d6540fa048e)).
- **UILayout**: New `property_split_factor` static value used by the layout system when property split is enabled ([bad8871dc5](https://projects.blender.org/blender/blender/commit/bad8871dc58d458843db2d23de38cd8baf12f529))

### Window Manager[¶](https://developer.blender.org/docs/release_notes/5.3/python_api/#window-manager "Permanent link")

- **Undo Stack**: New `bpy.context.window_manager.undo_stack` gives scripts read-only access to the undo history. ([ae71b51993](https://projects.blender.org/blender/blender/commit/ae71b519937e7a301ec19a9fd4b04cafda1dcb1c))
- **Buttons**: New [`WindowManager.try_activate_rna_button()`](https://docs.blender.org/api/5.3/bpy.types.WindowManager.html#bpy.types.WindowManager.try_activate_rna_button) function to activate UI buttons referencing RNA data.
