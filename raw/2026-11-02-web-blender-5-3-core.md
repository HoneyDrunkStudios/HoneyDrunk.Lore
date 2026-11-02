---
source: "https://developer.blender.org/docs/release_notes/5.3/core/"
title: "Blender 5.3: Core"
author: "unknown"
date_published: "unknown"
date_clipped: "2026-11-02"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Blender 5.3: Core

Capture note: Blender 5.3 is an upcoming release (beta per the official compatibility index at capture time). These release notes do not establish shipped behavior.

# Blender 5.3: Core[¶](https://developer.blender.org/docs/release_notes/5.3/core/#blender-53-core "Permanent link")

Blender 5.3 introduces an optional project system that makes Blender aware of a larger context than the open
blend file. Linked packed data is handled more coherently, undo can now be mixed across editors, and Batch Rename
gains timeline marker support.

---

## Highlights[¶](https://developer.blender.org/docs/release_notes/5.3/core/#highlights "Permanent link")

## Project Setup

When working in a production, it is important to have a set of properties and shared variables that are unique to
the ongoing project. To address this, a new project system was implemented. It makes Blender aware of a larger
context than just the currently open blend file, and provides corresponding project-wide features. Each project has
a root directory, and all files under that directory are considered part of the project. The root is identified by a
`.blender_project` directory inside it, which contains a project config file created and managed by Blender.

Blend files inside a project have access to project features and data. Paths can use `{project_root}`
and custom project variables as templates, and project asset libraries make it easy to browse all assets in a
project or to organize a large project into multiple asset libraries. The project also controls the
[OpenColorIO configuration](https://docs.blender.org/manual/en/5.3/render/color_management/opencolorio.html#aces),
choosing between the default Blender configuration, ACES 1.3, ACES 2.0, or a custom configuration.
For further customization, the project system offers a custom splash artwork option and lets you open recent files from the same project directly.

The project system is purely opt-in. Learn more about next steps and features to be implemented from the
[Project Setup design task](https://projects.blender.org/blender/blender/issues/133001).

---

## Linked Packed IDs

**Direct/indirect definition:** a linked packed ID is now considered directly linked if it's used by a local ID,
*or by any other packed ID also directly linked*. The latter part is new: linked packed ID dependencies are
conceptually part of the packed data (as they participate in the deep hash value), so if one is directly used,
all of its dependencies must also be considered as directly used.

**Writing:** with this more useful and coherent definition, code writing linked data now only writes directly
linked packed IDs. The indirectly linked ones are exclusively used by regular linked data from other libraries,
so writing them in the current blend-file is useless and only wastes space (and adds clutter). This is especially
useful in pipelines stacking several layers of linking in production files
(e.g. `assets.blend -> stage.blend -> shot_anim.blend -> shot_lighting.blend`).

[Linked Packed IDs changes.](https://developer.blender.org/docs/release_notes/5.3/core/#linked-packed-ids)

---

## Changelog[¶](https://developer.blender.org/docs/release_notes/5.3/core/#changelog "Permanent link")

### Project Setup[¶](https://developer.blender.org/docs/release_notes/5.3/core/#project-setup "Permanent link")

* **Projects**: New optional project system, with a root directory identified by a `.blender_project` directory. ([563b073381](https://projects.blender.org/blender/blender/commit/563b073381f0381d86ae91880c1f4da251b85025))
* **Path templates**: `{project_root}` and custom project variables for path templates. ([#159770](https://projects.blender.org/blender/blender/issues/159770))
* **Asset libraries**: Project asset libraries to browse all assets in a project, or split a large project into multiple libraries. ([#160226](https://projects.blender.org/blender/blender/issues/160226))
* **OpenColorIO**: Choose between the default Blender configuration, ACES 1.3, ACES 2.0 or a custom configuration. ([#162624](https://projects.blender.org/blender/blender/issues/162624))
* **Splash**: Custom splash artwork set up for the project. ([#164750](https://projects.blender.org/blender/blender/issues/164750))
* **Recent files**: Open recent files from the same project. ([#164736](https://projects.blender.org/blender/blender/issues/164736))

### Linked Packed IDs[¶](https://developer.blender.org/docs/release_notes/5.3/core/#linked-packed-ids "Permanent link")

* **Direct/indirect linking**: A linked packed ID is now directly linked if used by a local ID or by another directly linked packed ID. ([bb67052433](https://projects.blender.org/blender/blender/commit/bb67052433e2ff))
* **Writing**: Only directly linked packed IDs are written, indirectly linked ones are no longer saved in the current blend-file. ([bb67052433](https://projects.blender.org/blender/blender/commit/bb67052433e2ff))
* **Append**: The "Localize All" append option has been renamed to "Make Linked Local". Linked packed data is no longer localized when it is a dependency of the appended data, even if that option is enabled. ([#163799](https://projects.blender.org/blender/blender/issues/163799), [295a5e3fc4](https://projects.blender.org/blender/blender/commit/295a5e3fc4)).

### Undo[¶](https://developer.blender.org/docs/release_notes/5.3/core/#undo "Permanent link")

* **Global undo**: Support for mixing global undo with other undo systems, so edit-mode no longer prevents edits in other areas from being tracked by undo. ([69f5d770c4](https://projects.blender.org/blender/blender/commit/69f5d770c4f17b1688af1f9dceb12bb84d1591af))

### Batch Rename[¶](https://developer.blender.org/docs/release_notes/5.3/core/#batch-rename "Permanent link")

* **Timeline markers**: Support for renaming timeline markers. ([7d930a001d](https://projects.blender.org/blender/blender/commit/7d930a001de2926b3c39574ced35b52e1672c8c7))

### .blend Files[¶](https://developer.blender.org/docs/release_notes/5.3/core/#blend-files "Permanent link")

* **Stable saving**: Initial support for keeping .blend files the same when opening and saving a .blend file. ([cadb3fe5c5](https://projects.blender.org/blender/blender/commit/cadb3fe5c542dcdebab19b4a9369a0581d09a66c))
