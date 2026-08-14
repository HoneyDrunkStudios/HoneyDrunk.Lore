---
source: "https://www.blender.org/releases/4-5/"
title: "Blender 4.5 LTS"
author: "Blender Foundation"
date_published: "unknown"
date_clipped: "2026-08-12"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Blender 4.5 LTS

Source: https://www.blender.org/releases/4-5/

Blender 4.5 LTS — Blender
Toggle navigation
Features
Download
Support
Get Involved
About
Jobs
Store
Donate
Features
Download
Support
Get Involved
About
Jobs
Store
Donate
All Releases
Blender 4.5 LTS
Initial release: July 15, 2025
Supported until July 2027
Watch Features Video
What's New
Splash artwork by
Blender Studio
Summary
With 2 years of updates, full Vulkan support, and quality-of-life improvements, Blender 4.5 LTS is every Blenderhead’s best friend.
Release Notes
User Manual
Python API
Versions
Blender 4.5.12 LTS July 21, 2026 Changelog
VSE: crash when prefetching frames for a scene strip with sequencer input which scene only contains a sound strip. [ #160559 ]
Assert when undoing Make Single User with a linked mesh. [ #161211 ]
Fix: crash in Armature Edit mode after duplicating animated bone. [ e3d228ac409838aae79559866073e9fa19c2eb83 ]
Fix: Invalid ID name uniqueness code handling of ID name removal. [ 23131d9d2c40cc5cc9114aa49ec9fe087c0a12ee ]
VSE, adding a crossfade between two strips does not set the crossfade inputs based on selection anymore. [ #156207 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.11 LTS June 23, 2026 Changelog
Anim: Backport Camera Marker Selection Logic Fix to 4.5. [ ed347df1e170725c26ffcea574cead9c47e756cb ]
Bug: Constraints Not Properly Cleared When Baking Bones on macOS. [ #159842 ]
Fix: GL Compilation Subprocess file locking. [ 09e3fe90145 ]
Crash while joining strokes (backport request). [ #159292 ]
Clicking in a cleared/uninitialized Video Sequencer Editor with specific keymap causes crash. [ #160021 ]
Rigify: Converting rotation mode from Quaternion to Euler throws an error (fcurve.group is none, probably a missing check). [ #159131 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.10 LTS May 19, 2026 Changelog
Crash When Editing Mesh with Geometry Nodes and Armature. [ #154739 ]
Vulkan: Black renders using NVIDIA driver 595.71. [ #155371 ]
Vulkan affecting the shader result when mixing color and BSDFs. [ #152150 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.9 LTS April 21, 2026 Changelog
Using multiple render layer nodes in GPU compositor fills up VRAM. [ #155639 ]
Fix: FCurve Settings RNA paths broken. [ 007ec77047c ]
Line Art modifier has incorrect boundary on ortographic camera sensor fit vertical. [ #155591 ]
Editing custom prop of ‘Temp’ type in °C/F crashes Blender. [ #155418 ]
Fix #154685: Grease Pencil: Noise modifier creates discontinuity. [ #155370 ]
Quick Favorites: some quick favorites are not removable from the menu. [ #155581 ]
Regression: Compositor: Stereo multilayered OpenEXR doesn’t select the correct image. [ #156200 ]
Compositor: Assert in vulkan code, when rendering compositor in backdrop view. [ #152536 ]
LineArt: Make intersection lines follow face mark filtering. [ fa17e7e6a42 ]
LineArt: Collection intersection flags and priority inheritance not working. [ #156431 ]
Badly filled out Keying Set with Armature causes crash. [ #156643 ]
Fix #154120: Offset setting does not affect surface placement. [ #154157 ]
Normalize in graph editor no longer centers flat curves. [ #156273 ]
Python error in *Quick Liquid* operator with *Shade Auto Smooth* (object_quick_effects.py). [ #156134 ]
Fix: crash when loading file from within asset library. [ 45721454be3 ]
Fix: collection preview lost when writing via bpy.data.libraries.write(). [ b2ac8f0e3d0 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.8 LTS March 17, 2026 Changelog
Regression: Sculpting: Shapekey Solo breaks undo steps. [ #153226 ]
Crash when quickly scrolling objects with modifier panels visible. [ #154087 ]
Assertion Failure: Moving Keyframe in Graph Editor beyond enum range. [ #82669 ]
When picking a focus distance while it’s keyed + auto keyframe on, it doesn’t drop a keyframe automatically. [ #154399 ]
Blender suddenly crashed when trying to join a rig into another a rig that is parented into another a rig. [ #154651 ]
Lineart Modifier seemingly using free()’d/invalid triangle data. [ #154632 ]
Fix: Correctly set new action user count to 0. [ 9663231430f ]
Principled BDSF to Shader to RGB breaks when using both sheen and subsurface scattering. [ #154962 ]
Odd lag with Grease Pencil Hook Modifier – dependency issue?. [ #153137 ]
Error loading SGI image with 2 bytes per pixel, RLE (assertion, potential out of bounds read). [ #155162 ]
Boundary brush symmetry bug. [ #154678 ]
Paint: Linear Burn not supported. [ #155207 ]
Assertion failure while closing Blender after rendering smoke simulation. [ #155341 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.7 LTS February 17, 2026 Changelog
Separate By Selection Issue. [ #153227 ]
VSE: Adding Freeze Frame to either end of a video or image sequences crashed. [ #147374 ]
VSE crashes when doing edits. [ #146493 ]
VSE: Rendering a still preview while using proxies produces a broken image. [ #150166 ]
crashing in sculpt mode, multires, Ctrl+Z. [ #152087 ]
Blender instantly crashes when loading an incomplete exr file. [ #152619 ]
Fix: restore accidentally changed default for ‘Allow Negative Frames’ pref. [ b991f26937f913cb845617d3441ec7752f40ea95 ]
Crash on Redo in Sculpt Mode (Specific to Material Preview/Rendered Viewport). [ #152005 ]
PyAPI: Potential loss of image due to unclear behaviour of `Image.pack()`. [ #152638 ]
Outliner: Remap Users spawns multiple dialogs on top of each other. [ #93814 ]
White artifacts when using Subsurface scattering in EEVEE (LTS 4.5.6). [ #153373 ]
Compositor: Grouping a node with animation data (and removing sockets) leaves values without animation. [ #148664 ]
Hard crash when jumping timeline with this grease pencil object. [ #151908 ]
Dropping images into image editor fails. [ #141496 ]
Very intermittent ‘Writing to ID classes in this context is not allowed’ when updating any property after rendering. [ #114455 ]
Fix: UI: Instanced panels are drawn in incorrect tab. [ 6c7146532fc ]
Freestyle: Crash in FRS_do_stroke_rendering when rendering during geometry updates (mesh batch cache race condition). [ #151868 ]
Can’t drop asset from custom asset shelf if view scrolled. [ #154248 ]
Bind Camera to Marker operator does not update all windows. [ #152250 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.6 LTS January 20, 2026 Changelog
User count corruption by bpy.ops.object.make_single_user. [ #149541 ]
Bone in-between slider is drawn on top of the header. [ #147705 ]
Grease Pencil: Crash when pasting strokes when the object has no materials. [ #149837 ]
VSE: Preview doesn’t update when editing “Frame Number” in Speed Control. [ #149765 ]
Sculpt Mode Crash With Grab 2D Brush While “Grab Active Vertex” Enabled. [ #149795 ]
OSL Custom Camera Rendering has Memory Leak. [ #145985 ]
Default Values on Noise Modifier in the Graph Editor set to 0 instead of 1. [ #149942 ]
Graph Editor goes blank if Preview Range and Normalize are enabled. [ #150036 ]
Remesh converts vertex groups to regular attributes. [ #150016 ]
Curve sculpt mode: Pressing shift to temporarily switch to the Smooth brush doesn’t work. [ #149437 ]
Crash in vertex paint after redoing. [ #150014 ]
Reference Sheres are offset to the bottom and cropped, when tool header and 3d view header are flipped to the bottom. [ #149843 ]
Crash redoing sculpt move. [ #150257 ]
Fix: glTF exporter: Fix lamp temperature convertion. [ d985b2e6ecc ]
Compositor: AOV causes viewport to stop updating. [ #150019 ]
Fix: glTF exporter: Fix exporting not normalized lamp. [ 3a970cff93d ]
Broken selection drawing for flat objects in ortho view. [ #139555 ]
Baking animation removes constraints from linked file. [ #149724 ]
Sculpt Pose brush Squash & Strech deformation sets mesh position to -nan(ind). [ #130465 ]
Action should not be re-used when it comes from linked file. [ #150289 ]
NlaStrip creation doesn’t respect name parameter. [ #150408 ]
[linux] copying on the steam version of blender crashes steam and then blender when you try to re open it. [ #150414 ]
Face Selection doesn’t work properly when mesh is displayed as wire in Solid mode – Vulkan AMD GPU. [ #150336 ]
Fix: Make script_pyapi_bpy_driver_secure_eval pass with python >3.11. [ 56f74eb24f4 ]
Image data-block can not load images on EEVEE (but works in Cycles). [ #149039 ]
Grease Pencil draw on to the surface issue. [ #141896 ]
Undoing brushstrokes in texture paint doesn’t visually happen until viewport camera is moved (in Viewport). [ #150957 ]
Blender crashes on launch, ERROR (17): SharedMemory : handle_: File exists. [ #146596 ]
[Cycles Multi GPU + OSL] Normal mapping causes crash. [ #150441 ]
Grease pencil: Lineart not working at all. [ #149217 ]
LineArt modifier: Simplify > Sample mode crashes blender (segmentation fault). [ #149567 ]
Blender 5.0 crash when rendering with GPU compositor and compositing tree. [ #151033 ]
USD Imports with duplicate blend shape names inside the same skeleton root prim crash. [ #148569 ]
[crash] CompositorNodeKeyingScreen. [ #151572 ]
Geometry Nodes: wrong baked cache frame range when using packed bakes. [ #151676 ]
Asset Browser operators resets Pose Asset preview. [ #151760 ]
Blender breackdowner only affects active rig with 2 rigs linked. [ #150364 ]
Crash when copying Workspace. [ #151744 ]
Core: Fix (unreported) issue in Main merge code with linked data. [ dce5f7904ae ]
Compositor: Denoising EXR sequences accumulates memory with each frame. [ #151940 ]
crash when importing asset. [ #152215 ]
Crashing when trying to use Pose brush. [ #152292 ]
Asset browser screenshot preview is incorrect while in camera view. [ #145599 ]
Viewport render region (can be enabled with Ctrl+B) is broken in blender 5.0 when using Eevee with the walk navigation and fly nagivation modes. [ #151586 ]
UX Issue: Line art ‘Depth Offset’ is far too sensitive. [ #152609 ]
Fix: fix b-bone keying set property identifiers. [ f1193a0bd67 ]
`Copy Driver to Selected` does not overwrite existing driver. [ #152624 ]
Triangles to Quads “Compare Color Attributes” ignores float colors. [ #152040 ]
Fix: renaming pose bones via F2 does not refresh the Outliner. [ ee9f1f4d528 ]
Normals become broken after Separate By Material operation. [ #151083 ]
Geometry Nodes, Python: Linear Arrow Gizmo crashes Blender when python modal operator finishes. [ #151241 ]
Activating a camera from the Outliner “Blender File” view clears the scene camera. [ #151425 ]
Grease Pencil: Crash when weightpainting after Convert to GP from Mesh due to no vertex group selected. [ #151841 ]
Lattice UVW input Glitch. [ #71397 ]
Outliner: Moving collections reorders or deletes them unexpectedly. [ #150676 ]
Hair Curves: Can’t select curves additively with the Select Brush. [ #152228 ]
LTS: Video editor crash with 1055 png sequence. [ #152099 ]
Regression: Copy Global Transform fails when using Available keying set. [ #152216 ]
Texture Paint is NOT SHOWING selected faces, but shows EVERYTHING. [ #144035 ]
Walk navigation causes EEVEE camera view to render incorrectly. [ #153033 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.5 LTS November 18, 2025 Changelog
Intel Arc OpenGL: Light probes don’t interpolate. [ #141165 ]
Python template “ui_tool_simple.py” attempts to show property “mode” that doesn’t exist for “transform.translate”. [ #148490 ]
Collections and the Timeline are sorted in 2 different ways. [ #144460 ]
temp_data().images.load fails to handle relative paths. [ #148683 ]
Fix (unreported) assert on unknown DNA struct `ViewLayerEngineData`. [ 57327d831d2 ]
VSE: keyframed strip not moving to keyed position. [ #141190 ]
ShaderNodeCustomGroup crashes on display in Blender 4.4.0 and higher. [ #148685 ]
bmesh.types.BMFace.calc_tangent_edge_pair() is broken since 4.3. [ #148777 ]
Fix: error in wayland_dynload wl_display_dispatch_pending wrapper. [ 13522fd2945 ]
Fix #148338: Renaming a bone can rename channel in unassociated action. [ #148477 ]
Crash entering new node group in compositor if a “Missing Data-Block” Node Group node is present. [ #148750 ]
Fix #148478: Renaming bone can rename channels in all action slots. [ #148845 ]
Empty Default Eraser Brush Causes Crash. [ #148902 ]
Lineart Modifier – Match Output for Vertex Weight Transfer not working as expected. [ #148736 ]
Adjust Pose Asset does not create undo step resulting in loss of work. [ #148244 ]
GP: Edit mode change Opacity (Shift+F) is absent from the menus. [ #147394 ]
Default Preset protection interacts with custom Presets, leading to them not being deletable. [ #140719 ]
Missing Runtime Libraries if Blender is Built with `py`-Infix in Path. [ #149070 ]
enum values are not correctly generated. [ #141853 ]
Grease Pencil: Reproject Strokes is not working. [ #146795 ]
nla.apply_scale() does not apply scale. [ #143853 ]
Fix: OptiX denoiser showing up on devices without OptiX compatible GPUs. [ e2af0be1aca ]
Broken selection drawing for flat objects in ortho view. [ #139555 ]
FBX export doesn’t preserve geometry order. [ #146700 ]
Cloth Physics Simulation Crash on Free every time after opening project. [ #149201 ]
Depsgraph doesn’t build relations for camera markers. [ #149172 ]
Fix #148979: Grease Pencil: Reproject operator keep radius consistent. [ #149241 ]
Compositor: Grouping a node with animation data (and removing sockets) leaves values without animation. [ #148664 ]
Fix: Nodes: missing undo step when editing node socket items. [ a4c16f57912 ]
Blender Crashes in Potrace library. [ #148792 ]
Fix: Parent type not reset after ‘Clear and Keep Transforms’. [ afc86559f59 ]
Fix: Error when connecting Boolean sockets to Material Output in Material Nodes. [ #147808 ]
Fix: Python API: bpy.app.is_job_running(‘SHADER_COMPILATION’). [ b1fafcf5603 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.4 LTS October 29, 2025 Changelog
Blender 4.5.3 fails to compile with OpenColorIO 2.5.0. [ #147227 ]
OpenEXR: Support reading multipart files with full channel names. [ 138e8fbf1bd85a081682f6d44d8bd73e993560ff ]
Render: Forward compatibility for Blender 5.0 pass renames. [ 738209b2bee5be0ac4946ab5511f1644f2ac3391 ]
Illegal address when rendering with a custom camera in 4.5. [ #145544 ]
UV Editor: Lock Pinned Islands in UV packing not working with UDIMs. [ #141293 ]
Armature Symmetrize not symmetrizing Display Type prop. [ #145190 ]
Crash when Capture Screenshot Preview. [ #145719 ]
Regression: 3D cursor misaligned with axes in certain viewport rotations. [ #145028 ]
Crash when opening old file with undefined node. [ #145675 ]
USD Import: Fails to respect path user preference. [ #145856 ]
VSE: from 4.5 right click select doesn’t work with Blade Tool. [ #145715 ]
Fix: VSE: Metastack channel preview with negative values. [ f974c598f9a ]
Crash on pasting VSE strip with driver. [ #145629 ]
Fix: GPU: Avoid accessing GLContext after it is destroyed. [ e8b7e144e04 ]
VRAM leak when Stereoscopy and motion blur are both enabled. [ #145743 ]
Crash when switching view layer after undoing deleting/unlinking of certain object types. [ #145848 ]
Fix #145932: Relax Face Set brush can corrupt mesh. [ #145952 ]
Crash using playhead snapping in VSE in new scene. [ #145890 ]
Blender 4.5 freezes with blank output colour management settings. [ #146042 ]
Vulkan: Render Preview Error with Multiple 3D Viewports. [ #145961 ]
Blender sometimes crashes when using resize detail button in dyntopo mode on a mesh with resolution higher than 500. [ #146233 ]
Viewport Compositor: Render Layer input will not pass thru. [ #146133 ]
4.2.5 LTS – 5.0.0 alpha: Crashing after using UV Sculpt Tools in New Scene. [ #145879 ]
Rigify: Actions Feature does not use Slotted Actions. [ #144641 ]
.glb file import error on Blender 4.5. [ #142867 ]
OpenGL: Curve control points are extremely small when first displayed. [ #146501 ]
Possible Relax vertices in UV crash (wrong uv_sculpt size, missing defaults). [ #132016 ]
User interface artifacting with Vulkan on Qualcomm. [ #145315 ]
Fix #147340: EEVEE: Crash on failed world material compilation. [ #147445 ]
Grease Pencil: Hardness property doesn’t affect Square line type. [ #147147 ]
Fix: Cycles: MetalRT motion curves setup bug. [ #146568 ]
Can’t select verts/edges/faces behind wire/bounds objects while retopology overlay is on. [ #145993 ]
Crash when exporting alembic with Color Attributes. [ #146822 ]
Moving a empty material after joining objects crashes Blender (backport request). [ #146878 ]
Node Wrangler: Add Principled Setup plugs bump textures into filter width. [ #146679 ]
Fix: VSE: Propagate split to connected strips by default. [ 22d9b4ff719 ]
Fix: USD: Camera FStop of 0 means no depth of field. [ 47368daebe0 ]
Animation is not deleting when Bake Simulation was used. [ #146105 ]
bpy.ops.object.geometry_node_bake_pack_single failing on Windows. [ #147175 ]
Blender crashes when using the Align Bones operator across two armatures with different mirror settings. [ #146242 ]
VSE: “Swap Data” breaks strip alignment, then crashes. [ #146682 ]
Some keymap user preferences do not get imported into Blender 4.5 properly. [ #146670 ]
Crash if Grab and Keep Moving Missing Linked Data Block. [ #147283 ]
Weight painting can easily create NaN. [ #146671 ]
Test for greying out linked images in texture painting is backwards. [ #147568 ]
Crash after dragging any Asset Library Essential into the Compositor (Timings Overlay enabled, invokes the wrong tooltip). [ #147752 ]
Fix #146724: Crash when deleting node group from outliner. [ #147828 ]
Fix #147803: assert triggered on keyframe jump on NLA control curves. [ #147957 ]
Crash deleting library from which the current scene is linked. [ #147759 ]
Crash using Blade or Slip tool in VSE with new scene. [ #145853 ]
Toggle Window Fullscreen, Timeline (4.5.0, 4.5.1, 4.5.2, 4.5.3, 4.5.4). [ #146812 ]
Fix (unreported) Collada: missing `finish` call on some modified attribute. [ 84418a8d16a6846afae0e80cde25027f53fded56 ]
Sequencer: crash with sequencer in sequencer. [ #147477 ]
Crash when dragging outliner object into status bar. [ #144921 ]
anim_transforms_to_deltas resets non-keyframed object transforms values. [ #147796 ]
Collection input is missing the picker on new node group. [ #147860 ]
Unnecessary write operations on blender_assets.cats.txt. [ #111576 ]
Blender freezes on saving/loading of blend files with complex liboverride trees. [ #145894 ]
install_linux_packages: Fix for Fedora ≥ 41 (DNF5). [ e32a8ec884e ]
Grease Pencil: Stroke not visible for specific post processing values. [ #147174 ]
Blender Timeline animation, SHIFT vs CTRL selection difference. [ #147996 ]
Rigify doesn’t check existence of collection properly. [ #148454 ]
Opening old 2012 .blend file crashes blender. [ #148170 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.3 LTS September 9, 2025 Changelog
[4.5 LTS] Fix memory leak when loading libraries fails from Python. [ 0056783a60d11e9eb20d5fbe73d4535989871b02 ]
Fix: Grease Pencil: Smooth sculpt brush not working with handles and mask. [ b1b7360fc2543212c63b66be89536dacae38cce1 ]
Add-on hotkey customizations are not saved for custom operators. [ #143838 ]
[4.5 LTS] Fix: frozen mathutils Vector & Matrix types could be resized. [ 3bb0b4864df761bb3d2db593eea8b5a9ffa797e8 ]
Fix: UVSculpt brush size not converted correctly for 5.0 changes. [ f2c538ae863025869deb9bb3201a4a9bbb32ea56 ]
bpy.context.object.modifiers[“Lineart”].thickness no longer works in 4.5.2. [ #145138 ]
Grease pencil: Divide blend mode doesn’t work. [ #143802 ]
Fix: Vulkan: Submission runner crash on start. [ baa7ba7cbee894d034a59b309923a444b1a1f52c ]
Vulkan: NVIDIA driver 580.76.05 on Wayland freezes at startup. [ #144625 ]
When using the Vulkan backend, material compilation errors directly lead to Blender crashing. [ #144614 ]
Blender Light Probes do not create “mirrors” in 4.5 with Vulkan enabled. [ #142110 ]
Missing display update for unified strength icon. [ #144281 ]
Crash selecting the text on a linked duplicated text object. [ #144970 ]
4.5 Crash with Cycles render w/ Persistent Data + fileview thumbnails sequence. [ #143662 ]
Fix: Workbench: Broken render tests after AA fix. [ df9239608bbc21f23b233c65b2eba6898ada9f18 ]
Fix: Workbench: Broken render tests after AA fix. [ df9239608bbc21f23b233c65b2eba6898ada9f18 ]
Cycles: Add ROCm 7 runtime to hipew search list. [ f6c709f30b23be4fa9618938c2bb3c052a74421d ]
Cycles: Add support for building with CUDA 13.0 and OptiX 9.0. [ 6f6bf2b64d5c8cdec7fb5927fe41eca3818be8ce ]
Vulkan: Weird pink shading with temporal accumlation turned off. [ #144636 ]
Crash switching camera from Camera View to Orthographic view in Material Preview mode. [ #143857 ]
EEVEE: Rendering is incorrect in walk mode with overscan enabled. [ #144441 ]
Fix #144599: Cycles OSL node with external script does not update. [ #144808 ]
Invalid text selection in the Python console. [ #144858 ]
Illegal Address in CUDA queu copy_from_device (integrator_shade surface_raytrace integrator_sorted_paths_arrays_prefix_sum). [ #143841 ]
Cycles OptiX: When adjusting material properties that enables shader ray tracing, the material will momentarily render incorrectly. [ #144910 ]
Dynamic Paint: Bake Image Sequence crash. [ #143958 ]
OSL call for “geom:name” stopped working in Blender 4.5 LTS. [ #144814 ]
Crash when calling any node group from side properties panel. [ #144621 ]
Assert on `Add Texture Paint Slot`. [ #144175 ]
Crash when attempting to Unlink linked IDs from the Unused Data Outliner. [ #144840 ]
Dynamic Paint Crash switching displace factor from positive to negative – FYI New light project OK. [ #142137 ]
Blender crashes when snapping after aligning in edit mode. [ #144916 ]
Fix: EEVEE: Memory leak when drawing Volume objects. [ f6676240896 ]
Python: Modifying Workspaces via Python and ‘Reporting an Error’ Crashes Blender. [ #144958 ]
Cloth simulation presets only save some of the settings. [ #104074 ]
Force fields don’t work on a fire simulation with Flame Smoke 0. [ #86512 ]
Falling fluid simulation has odd behaviour. [ #144701 ]
Crash when scrubbing Scene Strip in Video Sequencer. [ #144982 ]
Fix: ACES 2.0 studio config sets image files to ACES2065-1 incorrectly. [ 820afacf15f ]
crash when moving GP stroke. [ #143635 ]
UI freezes with lots of action slots (in the Outliner). [ #143697 ]
Python: Improve `bpy.data.user_map()` argument documentation. [ cc943ea8145 ]
WORKBENCH with MATCAPS Rendering Issues in Blender 4.5 and 5.0 Alpha. [ #142738 ]
EEVEE: Freeze playing back a certain animation on macOS. [ #142381 ]
Assert fail in Limited Dissolve of flattened cone. [ #144383 ]
gpu.state.line_width_set() Does not work in vulkan. [ #144700 ]
split selection removes vertices. [ #145108 ]
Value Node not changeable in Properties Window. [ #144760 ]
Blender 4.5.2 LTS Clay strips brush – View plane acts like area plane. [ #145070 ]
NDOF/3D mouse: Pan Zoom is reversed in cardinal-orthographic views, in fly mode. [ #144751 ]
Crash when converting multiple objects to grease pencil with shared mesh data. [ #145287 ]
Crash when joining (Ctrl-J) two Grease Pencil objects in Blender 4.5.2 LTS. [ #145297 ]
Crash: 4.5.1 can’t open 5.0 file that contains Closure Zone. [ #144414 ]
Segmentation fault on grease_pencil_export_svg with frame_mode=’SELECTED’. [ #145259 ]
Crash in Viewport Render Animation when GDB is Attached. [ #145375 ]
Fix: incorrect handling of 3×3 matrices with RNA get/set callbacks. [ c01b33593f1 ]
The Greace pencil stroke copying bug. [ #145228 ]
Blender 4.5 unusual slow playback speed compare to B4.4 In large scale geometry nodes. [ #145385 ]
Compositor Cyclic links warning doesn’t disappear. [ #145403 ]
Copy Global Transforms: SKIP_SAVE on paste. [ 1459f185cb8 ]
FBX: new 4.5 importer places (instanced?) objects from Navisworks FBX file at origin. [ #145116 ]
Asset shelf breaks when changing preview size. [ #112936 ]
Anim: fix crash when loading F-Curve with unknown modifier. [ 5844ee62291 ]
Fix: viewer shortcut description mentions compositor only. [ f5e6be7f398 ]
4.5.3 regression – bpy behavior change on evaluated mesh with SK. [ #145340 ]
.glb file importing problem. [ #144980 ]
Python API: GPU module compute shader local group size defaults to -1 instead of 1 on Vulkan/OpenGL. [ #145818 ]
Blender Crashes With Curve Pen Tool While Using With Nurbs Curve. [ #145560 ]
Build: resolve linking error on *BSD systems. [ 0648332ceba ]
[Zh_CN] Driver auto-variable name “变量”causes Python error. [ #145590 ]
FBX: new importer does not import textures from some files. [ #145244 ]
Movie distortion node is more pixelated using the Auto GPU compositor. [ #145439 ]
Cryptomatte shows numeric value instead of picked asset name. [ #145498 ]
Crash on separating hair curves object. [ #145666 ]
Can’t use Intel Arc A770 GPU in Blender 4.5.2 LTS despite having the latest packages installed. [ #145449 ]
Captured attribute not propagated to Set Mesh Normal. [ #145691 ]
Fix: MaterialX export can end up with duplicate node names. [ 5ba56b4c6da ]
VSE – dragging on an image sequence no longer updates the Frame number in the Preview overlay. [ #144332 ]
USDZ in Blender 4.3.0: textures missing on FBX -> USDZ export (new export_textures_mode). [ #145711 ]
Fix: 3D text line end misses last character. [ 3b12157b928 ]
Undo history Unknown Action. [ #144096 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.2 LTS August 20, 2025 Changelog
Cleanup `bpy` builds on PyPI and archive them on Download. [ #146 ]
Vertex/Weight Paint Mask issues with subdivision. [ #143317 ]
Regression: Shading Issue transforming a object with custom normals. [ #142485 ]
Missnamed Built-In Shader. [ #143485 ]
Asset browser capture screenshot preview does not capture Cycles rendered preview. [ #141732 ]
USD: World uses wrong output node. [ #143291 ]
Vertex Weight Proximity sets Normalize Weights checkbox to default state after options switch. [ #143360 ]
UI: grey-out NDOF orbit center settings in “Fly mode”. [ 98596c9bccc ]
Fix: Grease Pencil: Remove fill guide attribute in `remove_fill_guides`. [ 5c1e9125b91 ]
Tool gizmo disappears when resizing regions & areas. [ #143629 ]
Pivot to Active Vertex in Mesh Sculpt mode not working. [ #143630 ]
Fix: `SculptSession#last_active_vert` uses incorrect value. [ fa3bebbbd6f ]
`bpy.ops.grease_pencil.join_selection(type=’JOIN’)` makes existing strokes broken. [ #142325 ]
Action editor with playhead snapping crash. [ #143154 ]
macOS complains about being unable to use Vulkan if a user reuses Vulkan user preferences. [ #143304 ]
[Clipping Region] Multi 3D Views & Alt+B enabled – click selection picks mesh outside region before target in mesh edit mode. [ #142800 ]
Attribute node (Type: View Layer) is not updated during playback in EEVEE when nothing is animated. [ #143323 ]
OpenGL: –debug-gpu doesn’t work in background mode. [ #142620 ]
Field Nodes not outputing values from node groups. [ #142202 ]
Old AMD Drivers: Crashes on startup (4.4.0 and above). [ #143087 ]
Error “Selected faces required” When Using ‘K’ Knife Cut After Confirming Previous Cut with ‘Shift+K’ in Edit Mode. [ #143439 ]
Hydra Storm: Error in console when rendering. [ #143722 ]
Fix: Nodes: restore active node after copy-pasting nodes. [ 0a37bba5a99 ]
Dot dash modifier makes grease pencil disappear. [ #143870 ]
Solidify Algorithm Behaves Strange/Different in 4.5. [ #143789 ]
Vulkan: Assert when sliding vertex. [ #143685 ]
Blender displays a crash popup when OSL camera references oso file that doesn’t exist. [ #143907 ]
Fix: Cycles: Show correct minimum OptiX GPU driver in preferences. [ c1c735dd5a0 ]
Repeated deletion & Ctrl+Z on a linked library may cause crash. [ #143888 ]
Broken Normals when realizing Instances with Geometry Nodes that have an Object with WeightedNormal Modifier (and mirrored). [ #143708 ]
Regression: Crash in Vertex & Weight Paint when applying deform modifier. [ #143238 ]
Fix: Poll function for asset screenshot operator. [ 7a1ad217c69 ]
Intel Arc OpenGL: GPU compositor infill is inconsistent. [ #141173 ]
Volume shader masked by shader with alpha blend transparency. [ #143294 ]
NVIDIA Vulkan: Blender 4.5 crash on startup with MSI Afterburner/RivaTuner Statistic Server. [ #141806 ]
Fix: VSE: Wrong context used when dropping audio files. [ d648f124756 ]
Cryptomatte: Precision issues with matte output. [ #143775 ]
Bevel & Join Geometry crash. [ #143450 ]
Viewport: Blender crashes when entering sculpting mode. [ #142093 ]
Problem with edit lines display on grease pencil object. [ #143952 ]
4.5 LTS: Fix: armature “Auto-Name by Axis” creating invalid UTF8 names. [ b670fad9cb33cb5c0b375826fc684312ab4a844b ]
Cleanup: No longer require VSE Strip struct memory layout to never change [4.5]. [ c4c612ba5337f19f2cbe7eb4854a2babdbce1e65 ]
Intel Windows OpenGL: Dilate node feather mode does not work. [ #141436 ]
Curves in EDIT mode appear thinner than in OBJECT mode on HiDPi displays. [ #141980 ]
Vertex Paint: Subtract blending mode is broken. [ #143399 ]
Regression: Frustum culling is incorrect in Blender 4.5 with older AMD GPU drivers. [ #143336 ]
Transparent background is not fully transparent in Workbench Render Engine. [ #144040 ]
Curves Edit Mode: Redo duplicate move broken. [ #143739 ]
Fix #144014: Driver for data.shape_keys path fails with GPU subdivision. [ #144030 ]
Weight Painting Stroke Falloff Not Rounding. [ #134160 ]
Sculpt: Repeatedly Remeshing causes out of memory crash. [ #143257 ]
Nuked my C: drive accidentally using Blender. [ #139585 ]
Assert browsing a non UTF8 render output path. [ #143018 ]
Creating a face between two edges can result in a bow-tie quad. [ #143905 ]
Running New Scene in an Empty file crashes blender. [ #144086 ]
ASAN error when viewing collection in the spreadsheet. [ #143532 ]
Eevee World Sun Shadow no longer works in 4.5. [ #142046 ]
“Clear Keyframes” Affects All Bones. [ #143818 ]
Compositor Keying node “Feather Size” and “Dilate Size” inputs do nothing when given negative values. [ #144070 ]
Fix: Assert in Keying node with no input. [ d117ef4af3d ]
VSE video thumbnails performance / UI smoothness issues (since 4.3?). [ #142912 ]
Animation FPS progressively slower from Blender 4.3 to 4.5. [ #140706 ]
Assertion: BLI_string_ref.hh operator[](), at ‘index < size_’. [ #143539 ]
Eevee World Sun Shadow no longer works in 4.5. [ #142046 ]
Fix: EEVEE: VolumeProbeModule do_full_update_. [ 20f7bc67506 ]
Cryptomatte picker does not work with sequences. [ #144107 ]
Vulkan AMD: Wireframe overlay renders without occlusion culling when smooth wires is turned off. [ #142537 ]
Grease Pencil Bezier Curves, doesn’t respect Overlay Guides when Grid Snapping is on. [ #143534 ]
Blender has stopped working when copying a Grease-Pencil stroke in Edit-mode. [ #142700 ]
VSE proxies for image sequences do not work (since 4.5). [ #144254 ]
Node tool crashes under specific scenario. [ #144126 ]
4.5 Grease Pencil Light feature doesn’t work anymore. [ #144170 ]
Sculpting Dynotopo R Button display artifact (NOT Critical). [ #142927 ]
EEVEE: Shadows are missing if trasparency of a material is set by Instance or Object attributes. [ #144054 ]
Mesh transforms do not show up in the viewport if Blender is run with –debug-gpu-force-workounds. [ #144174 ]
Blender Project Instant Crash Upon Opening. [ #143720 ]
Grease Pencil 3 Moving Strokes to other layers cause them the lose Parenting. [ #139258 ]
Calling ‘bpy.ops.object.lineart_bake_strokes’ through the Python API in 4.5+ causes the UI to stop responding. [ #144392 ]
Edge slide misbehaves when sliding towards triangle. [ #144270 ]
VSE: Scopes sometimes stop updating during playback. [ #144432 ]
Return value of `bpy.app.translations.locales` changed in 4.5. [ #144306 ]
Vulkan: Disable descriptor buffers. [ 84d0840f0c8 ]
Vulkan: Destroy resources in submission thread. [ 3b081259efc ]
Fix: Compositor: Wrong tooltip for Crop Node. [ 3c2bd8cde6e ]
Removing and then redefining override causes a crash. [ #144373 ]
Fix #144408: Crash when cancelling primitive tool with automerge on empty drawing. [ #144470 ]
Grease Pencil: `Convert Curve Type` operator always creates Bézier curves with free handles. [ #144369 ]
Crash when setting default_value for a color socket on a material node group. [ #143551 ]
Fix: GL Compilation Subprocess race condition. [ 05b26ef4eb8 ]
Compositor crash cycling between inputs in compositor. [ #144411 ]
Crash in texture drawing. [ #143691 ]
Fix: Grease Pencil: Attribute interpolate with randomization. [ 1b6c73b0918 ]
Reprojcting Bezier Grease Pencil Strokes doesn’t move the handles with the strokes. [ #131108 ]
Fix: Grease Pencil: Bézier handles not effected by `Snap To Grid`. [ 0c6941eee39 ]
Fix #139094: Grease Pencil: Primitive Tools not initializing `u_scale` attribute. [ 72bf515e585 ]
Fix: Grease Pencil: `SVG` and `PDF` bounding box size bug. [ 118fe9cd248 ]
Cycles: oneAPI: Disable L0 copy optimization for several dGPUs. [ 4bc473807f7 ]
grease pencil 3.0 subdivision pinches at the stroke’s start point. [ #142644 ]
FBX exporter encounters error when exporting meshes with tangents. [ #144592 ]
Fix: execute_node_group only accepting positive values for arguments. [ bc6bc8f5d51 ]
Animation & Overrides; Keyframe insertion should result in warning/error?. [ #144371 ]
Build: Only link to librt on Linux. [ 41539e4fa80 ]
Fix: Build failure on riscv64 platform. [ 9745245933a ]
Blender crashes opening certain file. [ #144749 ]
ACES 1.3 errors in Blender 4.5.1. [ #144681 ]
LineArt: Backport thickness to radius conversion. [ ae8a273c7afcccae43180596b8970f96c8e6435c ]
Can’t Keyframe or add driver to UV Map active render property. [ #142780 ]
Vulkan Backend Renders Control Points Incorrectly. [ #143231 ]
Vulkan: Swap to system memory for device local memory. [ 92cb40fd2ead492c907704feb24cb99227d60f1a ]
Vulkan: Displaying Bone Keys in Graph Editor Causes VRAM Leak. [ #142305 ]
Fix: Vulkan: Use after free when switching scenes. [ 960e0dae10 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.1 LTS July 29, 2025 Changelog
Fix: Only last tangents layer is exported to fbx when mesh has multiple uv layers. [ 3a16c4995a1 ]
LibraryOverride bug because of Hair Curves. [ #139527 ]
Sculpting “Surface Smooth” causes decimation of Geometry. [ #141753 ]
Back side of rotate gizmo appears when approaching small object. [ #111060 ]
Crash when using cryptomatte node with image sequence having different sizes. [ #141810 ]
Unexpected Behavior on Closed Grease Pencil Curves with Connected Proportional Editing. [ #142025 ]
Geo Nodes Input Panel crashing when name is deleted. [ #141911 ]
Manifold boolean with plane is offset. [ #142326 ]
Light Temperature’s Animate property button keyframes the wrong property. [ #142103 ]
Armature: Copy to Selected not working on Editbone “lock” unlocking. [ #141940 ]
Armature EditBone RNA paths incomplete. [ #142062 ]
Adaptie Subdivision Simple breaks UV. [ #142060 ]
Asset Library : Creating new pose library asset keyframes everything. [ #141909 ]
When reloading a linked character, while a NLA strip is in edit mode, the base action gets un-slotted. [ #139509 ]
Issue building blender 4.5-pre on linux with external manifold 3.1.1. [ #141943 ]
Critical error when importing animation data from previous versions. [ #142106 ]
`batch_for_shader` with custom glsl shader very slow when inputs are optimized out of the shader program. [ #137429 ]
Blender had a crash after exporting Grease Pencil to PDF. [ #142183 ]
Consistent crash: 2 image sequence materials playing from video files. [ #141918 ]
Bevel (selection including border edges) crashes. [ #142045 ]
Broken USD skeletal animation rotations because of quaternion discontinuity. [ #141718 ]
Importing certain USD files crashes Blender. [ #142084 ]
MeshSequenceCache modifier does not read Edge Creases. [ #141633 ]
Blender crashes switching to sculpt mode on a hidden mesh. [ #141827 ]
Memory leak when exporting object(s) with subdivision modifier to FBX. [ #128169 ]
4.5.0 – EEVEE 3D viewport Smudgy animation playback. Different results when multiple 3D viewports are open. [ #142217 ]
Material preview lighting changed between 4.5 and 4.4.3 on old Intel hardware. [ #141781 ]
Crash when skipping outside of simulation cache with Vector Display enabled. [ #142259 ]
Crashes when Scaling a Video and Audio Strip in VSE. [ #142291 ]
Blender crashes switching to sculpt mode. [ #142328 ]
Cycles: oneAPI: Compile only needed device binaries in multi-GPU case. [ 0b5f1491e74 ]
Blender crashes on exit closing a non-focused window (OpenGL backend + Wayland?). [ #141777 ]
Crash adding subsurf with invalid material indices. [ #142245 ]
Manifold Boolean Subtraction causes crash. (And is not retaliative). [ #142494 ]
Blur Attribute after Manifold Boolean crashing, exaggerated by sample nearest surface. [ #142454 ]
FBX: new 4.5 importer produces broken rotation curves in some cases (when angle between two keyframes is large). [ #142333 ]
Fix #142647: Don’t create preset that has the same name as built-in ones. [ #142652 ]
Grease Pencil wrong fill shape when removing fill guides. [ #142649 ]
Release scripts: Packaged test data is missing folders. [ #142489 ]
VSE: Retiming and Speed Control are not automatically updating Sene strip subframes while previewing. [ #141709 ]
Crash if Realized Instance Contains some weird stored named attribute. [ #142163 ]
Crash when use geonode tool on multiple objects. [ #142648 ]
Transfer Mesh Data – Always giving warning even though the operator works as intended. [ #140376 ]
Vulkan, change view to wireframe crash. [ #142097 ]
Vulkan crash when displaying texture on a point generated from geometry node with cycles and eevee views at the same time. [ #142255 ]
Regression: UV Editor – Show Faces – no more working. [ #142557 ]
4.5 – Grease Pencil – Color Jitter still not working. [ #142006 ]
Windows: graphical crash report appears in background mode. [ #142314 ]
Assets Browsers’s Capture Screenshot preview area are not correct on macOS. [ #141982 ]
Regression: Custom Node Socket Types in Node Tree Interface Not Possible in Blender 4.5.0 LTS. [ #142630 ]
Removing keymaps with default names. [ #118035 ]
Regression: UV edit cage no longer has corner scale points. [ #142811 ]
Adaptive Subdivision in the viewport recalculates when the camera moves. [ #142603 ]
4.5 – Grease Pencil – Color Jitter still not working. [ #142006 ]
CompositorNodeVecBlur’s `use_curved` property crashes Blender. [ #141970 ]
Cycles Render: Volume (Before Baked Simulation Starts) still trying to be rendered. [ #105546 ]
Fix: Crash when group node has no Group Output node. [ a1c9bbc17af ]
Hard crash when using bmesh.ops.split (unreachable code @ bmesh_py_types.cc:4372). [ #142633 ]
Vulkan Fails on Windows ARM with Qualcomm Adreno 31.0.112.0+ Driver. [ #142859 ]
PyDoc: Document all app handler arguments. [ 73b2f639a09 ]
When Subdiv is enabled, the size in dimension remain the same (GPU Subdiv off). [ #142399 ]
Can’t add snap points when only using `Grid` as a target. [ #139530 ]
VSE: Adding a new effect displays stale frame (since 4.5). [ #142853 ]
Win: Disable bug report button on crash dialog. [ 4d5328d5daf ]
4.5 backport: Fix: crash displaying negative numbers in WM_cursor_time. [ 74102188b6e459a5adb8453be946f45a7650603e ]
Crash using Cycles with two Intel GPUs. [ #138384 ]
OSL camera fails camera in volume check if the ray is offset too far from the camera. [ #139718 ]
Cycles: Lightgroup passes for environment shaders are incorrect. [ #142953 ]
Fix: Grease Pencil interpolation on cyclic curves shifts end point. [ bf9579e359962a90e73f467ea4535ba551d98792 ]
Bledner 4.5 FBX import crash. [ #142972 ]
Utilities: Add batch files to help launch Blender with different GPU backends. [ 8208e58308f ]
Opening a specific 4.4 file crashes Blender 4.5. [ #142954 ]
4.5 Particle Brushes Lost X-Ray Capability. [ #141741 ]
Blender 4.5 shader nodes is no longer able to read undisplaced normals. [ #142022 ]
Fix: VSE: Copy to selected would interfere with dual handles. [ 1df47953ced ]
Fix: VSE: Cannot ignore connected strips’ handles with alt if already selected. [ c63b96e14c2 ]
Multiresolution: Smooth Mask filter creates patterns. [ #142186 ]
Scrape to Plane brush type versioning handles “Plane Offset” incorrectly. [ #142151 ]
Crash selecting an armature with over 65k objects. [ #143161 ]
Ctrl + H “Hide Other Collections” Pie Menu – Shift to Extend Not Working. [ #140548 ]
The “offset even” option in Extrude Individual Faces and Move does nothing. [ #135908 ]
Fix #143156: “RGB to BW” node not found in link drag search. [ #143174 ]
Fix #142724: Mesh used by boolean modifier missing subdivision in edit mode. [ #143135 ]
Fix #143127: UI: Shading UI shows inactive settings in Matcap mode. [ #142863 ]
Normal Edit Modifier is not behaving predictably in 4.5. [ #143142 ]
Cycles crash on macOS (reproducer blend file included). [ #143128 ]
Fix: Vector.to_tuple didn’t accept precision of -1. [ 3e8fbfab71 ]
Grease Pencil: Dot-dash modifier crash with high Gap values. [ #143420 ]
Cycles OSL: Shader thumbnail generation leads to crash popups. [ #142876 ]
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Blender 4.5.0 LTS July 15, 2025 Changelog Release Notes
Download
Windows Installer 344 MB Windows Portable (.zip) 381 MB Windows Microsoft Store Windows ARM Installer 320 MB Windows ARM Portable (.zip) 390 MB macOS Apple Silicon 295 MB macOS Intel 320 MB Linux 359 MB Linux Snap Store Steam Source Code Blender Source Code Blender + Libraries
About
Blender Foundation
Blender Institute
Blender Studio
License
Logo & Trademark
Credits
Privacy Policy
Code of Conduct
Organization
People
Jobs
Blender Network
Download
Latest Blender
Blender LTS
Previous Versions
Experimental Builds
Source Code
Requirements
Benchmark
Flamenco
Extensions
Add-ons
Themes
Developers
Get Started
Roadmap
Projects
Docs
Blog
Forum
YouTube
Python API
Blender Studio
Films
Training
Tools & Pipeline
Support
Manual
Community
FAQ
Get Involved
Documentation
Education
News
Press Releases
User Stories
Blender Conference
Follow Blender
Support Blender
Donate
One-time Donation
Artistic freedom starts with Blender The Free and Open
Source 3D Creation Suite
