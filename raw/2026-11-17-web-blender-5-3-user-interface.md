---
"source": "https://developer.blender.org/docs/release_notes/5.3/user_interface"
"title": "Blender 5.3: User Interface"
"author": "unknown"
"date_published": "unknown"
"date_clipped": "2026-11-17"
"category": "Technical Art & Creator Tools"
"source_type": "web"
---

# Blender 5.3: User Interface

## Highlights

Blender 5.3 gets more than a layer of polish. Long-awaited quality of life features and improvements that make
this release take a leap in usability.

---

### Outliner

Place your objects anywhere with custom sorting in the Outliner, enabled by default and adjustable from the header popover.

Plus improvements to filtering, drag-and-drop behavior, and hierarchy management.

[All Outliner changes.](https://developer.blender.org/docs/release_notes/5.3/user_interface/#outliner)

[](https://developer.blender.org/docs/release_notes/5.3/videos/ui_outliner_sort.mp4)

Custom sorting for objects in the Outliner.

---

### Search

The sidebars in all editors now support search, making it possible to find any property or operator, even inside tabs created by add-ons.

Press `Ctrl/Cmd + F` while hovering the sidebar and start typing right away, or through the context menu of the tabs and panels.

To clear the search, press `Alt/Option + F`.

[![Search in editor sidebars](https://developer.blender.org/docs/release_notes/5.3/images/ui_sidebar_search.webp)](https://developer.blender.org/docs/release_notes/5.3/images/ui_sidebar_search.webp)

Search in sidebar tabs.

### Markdown, Nodes, and more

The Blender UI now supports rendering basic [Markdown](https://en.wikipedia.org/wiki/Markdown) formatting. Write markdown directly in the new [Comment](https://docs.blender.org/manual/en/5.3/interface/controls/nodes/types/layout/index.html) node, or in regular layouts for scripts/add-ons through the [label\_markdown](https://docs.blender.org/api/5.3/bpy.types.UILayout.html#bpy.types.UILayout.label_markdown) widget.

Another handy new widget for long strings is [label\_multiline](https://docs.blender.org/api/5.3/bpy.types.UILayout.html#bpy.types.UILayout.label_multiline), it behaves just like labels but allows text to wrap.

[![](https://developer.blender.org/docs/release_notes/5.3/images/ui_node_comment.webp)](https://developer.blender.org/docs/release_notes/5.3/images/ui_node_comment.webp)

New Comment node to annotate node trees, with Markdown support. Rendered node on the left, Edit mode on the right.

---

## Changelog

### General

- **Box Select:** Scroll the view when gesture is near area edges ([a2905c4382](https://projects.blender.org/blender/blender/commit/a2905c4382e7293419385a7a74874e4d7e9db2e6))
- **Sidebar**: Search inside any editor sidebars. ([3eaa7c4d96](https://projects.blender.org/blender/blender/commit/3eaa7c4d960a76aca2a89617f945767c71ffb0e8))
- **Move/Link to Collection**: It's now possible to move/link or create a new nested collection at any hierarchy level. ([9b46f00fb9](https://projects.blender.org/blender/blender/commit/9b46f00fb9d21205a32f43a1c2be06b8cc7f42cb))

[![](https://developer.blender.org/docs/release_notes/5.3/images/ui_move_to_collection.webp)](https://developer.blender.org/docs/release_notes/5.3/images/ui_move_to_collection.webp)

Move/Link to Collection: Move inside or create a new nested collection on-the-fly.

#### Widgets

- **Markdown Labels**: Format labels using Markdown syntax. ([docs](https://docs.blender.org/api/5.3/bpy.types.UILayout.html#bpy.types.UILayout.label_markdown)) ([e8c146ed8e](https://projects.blender.org/blender/blender/commit/e8c146ed8e7061b664bd9de00437f15588fe7056))
- **Multiline Labels**: A new widget that allows labels to wrap to multiple lines. ([eee95f8124](https://projects.blender.org/blender/blender/commit/eee95f8124)). Use it through Python via `UILayout.label_multiline()`. ([docs](https://docs.blender.org/api/5.3/bpy.types.UILayout.html#bpy.types.UILayout.label_multiline))
- **Curve Widget**: Improve the selection of corner points. ([3279bedb27](https://projects.blender.org/blender/blender/commit/3279bedb2743aefba8f08d8cda9b9d90c52c2999))

#### Tooltips

- Increased delay between quick and regular tooltips, so there's more time to read before the larger tooltip kicks in. ([7331d5ca1e](https://projects.blender.org/blender/blender/commit/7331d5ca1e))
- Improved readability of the inactive/disabled reason in tooltips, by adding padding, increase color contrast, and removing the redundant "Disabled:" prefix. ([PR#160977](https://projects.blender.org/blender/blender/pulls/160977))
- End sentences for enum labels and disabled text with period. ([f1e357ddb1](https://projects.blender.org/blender/blender/commit/f1e357ddb17ae91268a6b5e22a84541aa90a9213), [7773d02269](https://projects.blender.org/blender/blender/commit/7773d02269a61584048e8fc3664ab9891a37c004))
- **Theme**: The color for the active enum value is now customizable. It used to be hardcoded to blue, it now uses the "Info" state color. The Info's alpha value is used to adjust the blend with the default text color. ([f2f4c1bbfc](https://projects.blender.org/blender/blender/commit/f2f4c1bbfc))

#### Icons

- New icons:
  - **Sequencer**: Strip, Strip Data, and updated Strip Duplicate icon. ([PR#160875](https://projects.blender.org/blender/blender/pulls/160875))
  - **I/O**: `IMPORT_EXPORT`, to be used when a collection has both importers and exporters assigned. ([PR#162450](https://projects.blender.org/blender/blender/pulls/162450))
- Added icons to:
  - **File Browser**: Context menu. ([796fbeca99](https://projects.blender.org/blender/blender/commit/796fbeca99))
  - **Asset Browser**: Library and catalog menus. ([ca6084f980](https://projects.blender.org/blender/blender/commit/ca6084f980))
  - "Delete" and "Duplicate" operators. ([e78cb53426](https://projects.blender.org/blender/blender/commit/e78cb53426), [8360731a9f](https://projects.blender.org/blender/blender/commit/8360731a9f), [b207b277e3](https://projects.blender.org/blender/blender/commit/b207b277e3))
  - "Copy/Paste" icons to all relevant menus. ([09bf85e8de](https://projects.blender.org/blender/blender/commit/09bf85e8de))

### Input & Keymap

- **Number Buttons**: The arrows on number buttons now support using modifier keys (`Shift`, `Ctrl`) to adjust values with precision, in the same way as click-drag does. ([728c8624b3](https://projects.blender.org/blender/blender/commit/728c8624b362e5944cc131965dd4acaa55778285))
- **Strip Modifiers tab**: `Shift+A` now opens the `Add Modifier` menu, just like in object modifiers. ([3ac7f1e9c9](https://projects.blender.org/blender/blender/commit/3ac7f1e9c9))
- **Node Editor**
  - `Ctrl+X` now cuts nodes (dissolve + copy). Dissolve was moved to `Shift+X`. ([53f70d9a10](https://projects.blender.org/blender/blender/commit/53f70d9a10))
  - `Alt+LMB` to connect to Group Output now supports compositor as well. ([449fbc6b39](https://projects.blender.org/blender/blender/commit/449fbc6b39))
- **Search Menu**: Use `Ctrl+Mouse-wheel` to scroll through. ([47f6b41f8e](https://projects.blender.org/blender/blender/commit/47f6b41f8e))
- **Tree and Grid Views** ([cf17ed1020](https://projects.blender.org/blender/blender/commit/cf17ed10204580279fe395d90466241cf6cb5133))
  - Use `Page Up/Down` to scroll to previous/next page.
  - Use `Home/End` keys to jump to the top and bottom pages of pages.

#### Input Method Editor (IME)

- Added IME support for text input in the Text Editor, Python Console, Video Sequencer, and text objects in the 3D Viewport.
  ([c26f81641a](https://projects.blender.org/blender/blender/commit/c26f81641ae35a015d1aace362ca653e2f853312),
  [63fa40151e](https://projects.blender.org/blender/blender/commit/63fa40151e3c5f7ab36446a8117cdde28e5b06ca))

### Theme

- **All Editors**
  - Three unused properties have been removed, simplifying theming. The properties are: `Title` (use Panel Title instead), `Header Text`, and `Header Text Highlight` (use editor's Text and Text Highlight instead). ([c2a37974ac](https://projects.blender.org/blender/blender/commit/c2a37974ac), [f0617f45e2](https://projects.blender.org/blender/blender/commit/f0617f45e2))
  - The arrow to collapse regions now follows the theme colors. ([5cbbd562a1](https://projects.blender.org/blender/blender/commit/5cbbd562a189f12ee88960f0064b61c69dd430b5))
- **Animation**: The "Playhead" setting (under Common → Animation) now supports transparency. This is used by the vertical line under the playhead, so it is possible to see keyframes behind it.
- **File Browser**: Items in the File/Asset Browser now follow the "List Item" theme settings, allowing for a lot more customization such as outlines and rounder corners. ([PR#160853](https://projects.blender.org/blender/blender/pulls/160853))
- **Bone Color Sets**: More compact layout allowing to fit more settings on screen at once. ([PR#161791](https://projects.blender.org/blender/blender/pulls/161791))

### Editors

#### 3D Viewport

- **Attribute Viewer Overlay**: Boolean values are now displayed with a tint, so they're easier to read at a glance. These can be adjusted via the "Success" and "Error" state theme settings. ([802a9e5cbd](https://projects.blender.org/blender/blender/commit/802a9e5cbd))
  [![](https://developer.blender.org/docs/release_notes/5.3/images/ui_attribute_viewer.webp)](https://developer.blender.org/docs/release_notes/5.3/images/ui_attribute_viewer.webp)

  True/False values are now easier to spot at a glance.
- **Statistics**: *Vertex Paint* and *Weight Paint* now show the total count of vertices and faces of the active mesh in with the *Statistics* overlay enabled. ([ca45f2f98d](https://projects.blender.org/blender/blender/commit/ca45f2f98d))
- **Viewport Compositor**: Enabled by default for the startup file in the default 'Layout' workspace, and set to *Always*. ([4a1da15854](https://projects.blender.org/blender/blender/commit/4a1da15854))
- **Falloff**: For *Sculpt Mode*, *Vertex Paint*, *Weight Paint*, and *Texture Paint*, the *Falloff* panel has been renamed to *Shape* and various options have been added to it. ([74143fb470](https://projects.blender.org/blender/blender/commit/74143fb470))

#### Animation

- **Playback Controls**
  - The "Active Keying Set" popover has been merged with the auto-keying popover, to save space. ([24ae1c8d73](https://projects.blender.org/blender/blender/commit/24ae1c8d73))
  - The Time Jump buttons were moved to be in line with the Playback buttons. ([4bdfb6df7a](https://projects.blender.org/blender/blender/commit/4bdfb6df7a))

#### Asset & File Browser

- **Asset Browser**: Asset metadata fields now support multi-line labels. ([f4eca1c3c3](https://projects.blender.org/blender/blender/commit/f4eca1c3c3))
- Standard modifier-key shortcuts were added (not replaced, existing shortcuts are still there). Such as `Ctrl+R` to refresh, `Ctrl+A` to Select All, etc. ([PR#160120](https://projects.blender.org/blender/blender/pulls/160120))

#### Node Editor

- New Comment node supporting basic markdown. ([1a542e4131](https://projects.blender.org/blender/blender/commit/1a542e41319fda83acc6f993e6b8515e250e63c1))
  [![](https://developer.blender.org/docs/release_notes/5.3/images/comment_node.png)](https://developer.blender.org/docs/release_notes/5.3/images/comment_node.png)

  Simple example of the new Comment node, showing bold and links formatting.
- Show warnings in collapsed node headers. ([58f7fe2157](https://projects.blender.org/blender/blender/commit/58f7fe2157a7))
  [![](https://developer.blender.org/docs/release_notes/5.3/images/ui_node_header_warning.webp)](https://developer.blender.org/docs/release_notes/5.3/images/ui_node_header_warning.webp)

  Warnings are now also shown when the node is collapsed. Hover over a warning to quickly read its reason.
- Highlight links through reroute nodes. ([702c14c08a](https://projects.blender.org/blender/blender/commit/702c14c08ad0e8c2e106ca287e258568f15312e4))
- Reorder various entries to follow alphabetical order. ([fc7cb3f5d0](https://projects.blender.org/blender/blender/commit/fc7cb3f5d033ec5a22ee3f35770828678fd87d05))
- Highlight editables labels on hover. ([50d9df48e3](https://projects.blender.org/blender/blender/commit/50d9df48e3c8b0314f446fd5cf0c7bfdf04f7a50))
- Support for disabling outputs through switch nodes. ([1edbfbd2e6](https://projects.blender.org/blender/blender/commit/1edbfbd2e6fffedc1baeb7c7ce65f1f27e7a4e94))
- Use multi-line text box for node group and socket descriptions. ([b006eb9b18](https://projects.blender.org/blender/blender/commit/b006eb9b1893a81096f0d036eec923cde8546535))
- **Context Path**: Quick access to other node groups. ([581828754b](https://projects.blender.org/blender/blender/commit/581828754bdb4e5807624ac1d1e13c762acfe92c))
  [![](https://developer.blender.org/docs/release_notes/5.3/images/ui_node_groups_dropdown.webp)](https://developer.blender.org/docs/release_notes/5.3/images/ui_node_groups_dropdown.webp)

  Click on the chevron to access other node groups at that level.

#### Outliner

- **Sorting**: Objects and collections can now be placed anywhere in the hierarchy. "Custom" sorting is the default and can be adjusted from the header popover. ([a5e564c354](https://projects.blender.org/blender/blender/commit/a5e564c354), [b765a0ee05](https://projects.blender.org/blender/blender/commit/b765a0ee05))
- **Expand on Focus**: New option to automatically uncollapse hierarchy of the focused element in the Outliner. Disabled by default, it can be enabled from the header popover. ([159c5e8b97](https://projects.blender.org/blender/blender/commit/159c5e8b971602156d37a5464e452b4731b4405a))
- **New Collections**
  - When adding a collection, the view now scrolls to focus on it, allowing it to be renamed right away. ([e362cddd4c](https://projects.blender.org/blender/blender/commit/e362cddd4cd51974aede1ae699e1b79f94f32a41), [d817626525](https://projects.blender.org/blender/blender/commit/d817626525bf22b0a7415d99422eeb53ce36c5b0))
  - By default new collections now added to scene collection ([fe6f6e3d36](https://projects.blender.org/blender/blender/commit/fe6f6e3d36b43c9f5d8837c4b0584469159bec80))
  - Use `Shift + C` to add new collection as child of the active collection, or in same hierarchy of active object. ([82024c6ded](https://projects.blender.org/blender/blender/commit/82024c6ded4479948f7dd5d9e4f1cd2e87b227ff), [70d15dc35f](https://projects.blender.org/blender/blender/commit/70d15dc35ff6fe95f8ea6db23cef55fea42a1b8d))
- **Images**: Convenient access to pack images via the context menu. ([64939ff906](https://projects.blender.org/blender/blender/commit/64939ff906))
- **Shortcuts**: Use `Shift + H` to hide unselected objects, just like in the Viewport. ([85fec78335](https://projects.blender.org/blender/blender/commit/85fec7833550e0c84a1a118ac7e1741929fe07cb))
- **Filters**: New options to filter specific data from object hierarchy, such as modifiers, animation data, and more. ([7037997c4d](https://projects.blender.org/blender/blender/commit/7037997c4d6e4186e6065b1276aec71027ccfa39))
- **Drag and Drop**: When moving an object that is parent to other objects, the entire hierarchy will move with. Use `Shift + Ctrl + LMB drag` to only move parent (previous behavior). ([aae30c8a13](https://projects.blender.org/blender/blender/commit/aae30c8a134af6c2aa4060ade10acf4b81382d8e))
- **Columns**
  - New "Users" column in View Layer and Scene mode, showing the user count of a data-block. On click it toggles Fake User. ([e2aaab991b](https://projects.blender.org/blender/blender/commit/e2aaab991bfb11f65d8e6fb11a4a36e1afdcd8ca))
  - "Holdout" and "Indirect Only" toggles now show for objects as well as collections. ([4cf372ccdc](https://projects.blender.org/blender/blender/commit/4cf372ccdc50de7c57dcec1057b5445290c72a90))

#### Properties

- **Sequencer Strip tab**: New strip icon now colored in orange (similar to Object). To better represent hierarchy and ownership, and make it stand out more. ([PR#160864](https://projects.blender.org/blender/blender/pulls/160864))
  [![](https://developer.blender.org/docs/release_notes/5.3/images/ui_sequencer_tab.webp)](https://developer.blender.org/docs/release_notes/5.3/images/ui_sequencer_tab.webp)

  The Strip tab in the Properties Editor is now colored orange, similar to Objects.

### Platforms

#### Linux

- **Wayland**: Blender windows are now drawn with rounded corners. ([e17742004b](https://projects.blender.org/blender/blender/commit/e17742004bfa))

#### macOS

- **Dock**: The app icon no longer shows up in the Dock when running in background mode via the command line. ([076a89d42e](https://projects.blender.org/blender/blender/commit/076a89d42ece9b93261feb784b62d9182fd3f0e0))
