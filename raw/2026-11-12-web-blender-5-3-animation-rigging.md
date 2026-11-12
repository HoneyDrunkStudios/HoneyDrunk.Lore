---
source: "https://developer.blender.org/docs/release_notes/5.3/animation_rigging"
title: "Blender 5.3: Animation & Rigging"
author: "unknown"
date_published: "unknown"
date_clipped: "2026-11-12"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Blender 5.3: Animation & Rigging

## Highlights

New operators for copying and pasting world-space animation and converting rotation modes.
Friendlier playback and smaller improvements to Posing, Motion Paths, Shape Keys, and Rigify.

### Copy Paste World Space

Showcasing copying animation from a bone to an object.

New operators for copying and pasting world-space animation are available in the Animation tab of the 3D Viewport,
and support multiple selected objects or bones.
The preview range is used as the copy range, falling back to the scene range if none is set. Pasting to
constrained objects or bones is not yet supported.

Learn more in the [manual](https://docs.blender.org/manual/en/5.3/editors/3dview/animation/world_space_animation_copy_paste.html).

### Convert Animation Between Rotation Modes

Demonstrating converting the rotation mode of a bone during playback

A new operator, `anim.rotation_mode_convert`, converts animation between rotation modes,
improving upon now-deprecated Rigify operator (`pose.convert_rotation`).
Find it under *Object ‣ Animation* and *Pose ‣ Animation*, or in the new dropdown next to the
rotation mode property.
It can also be accessed with `Ctrl+R` in Pose Mode.
See the [manual](https://docs.blender.org/manual/en/5.3/scene_layout/object/editing/animation.html#convert-rotation-mode).

The operator works on all selected objects or bones and is also available through Python for objects and pose bones.
See the [Python API](https://developer.blender.org/docs/release_notes/5.3/python_api#animation) release notes.

---

## Changelog

### Animation

- **Copy Paste World Space**: New operators to copy/paste world space animation of objects and bones. ([b988d827b6](https://projects.blender.org/blender/blender/commit/b988d827b62936e6ce4a44f28125308a8e389fa6))
- **Convert Rotation Mode**: New `anim.rotation_mode_convert` operator converts animation between rotation modes, replacing the deprecated Rigify `pose.convert_rotation`. ([db9fd84d4e](https://projects.blender.org/blender/blender/commit/db9fd84d4ee8cffddd437500091f6a5287b9c95f))
- **Replace with Duplicate Action**: Added a new operator. ([323d5a0758](https://projects.blender.org/blender/blender/commit/323d5a07588459b57e1284b15fc196d0cdd1b5e1))
- **Make Markers Local**: Renamed to "Convert to Pose Markers" in the UI. ([ade68c48b6](https://projects.blender.org/blender/blender/commit/ade68c48b65702469aef178981c000e5c3471b0c))
- **Motion Paths**: Faster update when paths are automatically updated from auto keying. ([6f69604f84](https://projects.blender.org/blender/blender/commit/6f69604f84aca01ef08ba538a1a78a57357a6212))
- **Fix to Camera**: Now also covers lens parameters (Focal Length, Field of View, Shift X/Y). ([demo video](https://video.blender.org/w/siQckdy9NyFGpZRThGfNE6)) ([2291b97662](https://projects.blender.org/blender/blender/commit/2291b97662898c2f363014b0c57f7c84b29585a5))
- **Shape Keys**: The Duplicate operator now duplicates all selected shape keys, not just the active one. ([9851c6b1c5](https://projects.blender.org/blender/blender/commit/9851c6b1c5))

### Playback

- **Wrap Playhead**: New option to wrap the playhead to the playback range when navigating the timeline. ([675d94bd4b](https://projects.blender.org/blender/blender/commit/675d94bd4bebef690c1703aef87d90fee84f95ea))

Demonstration of the playhead wrapping in the timeline

- **Scrubbing**: Pauses playback and resumes on release. ([bda97c843c](https://projects.blender.org/blender/blender/commit/bda97c843c8f8571ce9f85b029321eada8e2becf))

Demoing pausing playback on scrub

### Pose

- **Align to Transform Orientation**: The operator is now available in Pose mode as well. ([7c00566f74](https://projects.blender.org/blender/blender/commit/7c00566f74))
- **Paste Pose**: When pasting poses (`Ctrl+V` in Pose mode) the redo panel now has an influence slider to blend in the copied pose. ([668c6b008b](https://projects.blender.org/blender/blender/commit/668c6b008b4c8598162aeebbfd2e4e03a4e40b73))
- **Pose Assets**: When creating a pose asset, the preview no longer becomes transparent if no scene camera is set. No preview is generated and the default action icon is shown instead. ([dc7ff59020](https://projects.blender.org/blender/blender/commit/dc7ff59020))

### Rigify

- **B-Bone Segments**: Spine and Head Rig types now expose a B-Bone Segment Count setting. Defaults match the previously hard-coded values, so existing rigs are unchanged. ([b6085cc8a1](https://projects.blender.org/blender/blender/commit/b6085cc8a1362dbe620556229741bcfdbf75bfd9))

### Forward Compatibility

- **Spline IK**: Chains are now gracefully capped to 255 bones on file read, so Blender 5.3 can read files from a future version that raises the limit without crashing. ([c63d0e8bf3](https://projects.blender.org/blender/blender/commit/c63d0e8bf364c525bc59fe02146f39e7d9f6fb9b))

### Python API

See the changes to markers and constraints [Python API](https://developer.blender.org/docs/release_notes/5.3/python_api/).
