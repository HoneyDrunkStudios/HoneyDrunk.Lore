---
source: "https://devtalk.blender.org/t/8-june-2026-upcoming/45360"
title: "8 June 2026"
author: "Blender Devtalk"
date_published: "2026-06-03"
date_clipped: "2026-06-21"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# 8 June 2026

Source: https://devtalk.blender.org/t/8-june-2026-upcoming/45360

Developer
Roadmap
Projects
Docs
Blog
Forum
Builds
BLENDER.ORG
Download
Get the latest Blender, older versions, or experimental builds.
What's New
Stay up-to-date with the new features in the latest Blender releases.
RESOURCES
Blender Studio
Access production assets and knowledge from the open movies.
Manual
Documentation on the usage and features in Blender.
DEVELOPMENT
Developers Blog
Latest development updates, by Blender developers.
Documentation
Guidelines, release notes and development docs.
Benchmark
A platform to collect and share results of the Blender Benchmark.
Blender Conference
The yearly event that brings the community together.
DONATE
Development Fund
Support core development with a monthly contribution.
One-time Donations
Perform a single donation with more payment options available.
Developer Forum
8 June 2026
Announcements
Weekly Updates
ThomasDinges
June 3, 2026, 11:36am
8 June 2026
Notes for weekly communication of ongoing projects and modules.
Announcements
Release cycle: Now at 5.2 LTS Beta (and 5.3 Alpha)
Modules & Projects
2026-06-02 Animation & Rigging module meeting
2026-06-04 Core Module Meeting
2026-06-04 Pipeline & I/O Module Meeting
2026-06-04 Triaging Module Meeting
2026-06-04 Platforms & Builds module meeting
2026-06-05 Project Updates meeting
2026-06-08 Viewport & EEVEE module meeting
2026-06-08 Grease Pencil Module Meeting Notes
New Features and Changes
This is a selection of changes that happened over the last week. For a full overview including fixes, code only changes and more visit projects.blender.org .
Alembic
Deduplicate data reading between IPolyMesh and ISubD ( commit ) - ( Kévin Dietrich )
Anim
Pose Slide operators for objects ( commit ) - ( Christoph Lendenfeld )
Show posing tools in Object Mode ( commit ) - ( Nika Kutsniashvili )
Assets
Better UX when catalogs in Online Essentials diverge from bundled ( commit ) - ( Sybren A. Stüvel )
Always show ‘Online’ icon ( commit ) - ( Sybren A. Stüvel )
Ignore predefined top-level catalogs (like “Compositing”) in Add menus ( commit ) - ( Julian Eisel )
Update compositor catalogs ( commit ) - ( Habib Gahbiche )
Compositor: Update authors for essential library ( commit ) - ( Habib Gahbiche )
Update Geometry Nodes asset catalogs ( commit ) - ( Sybren A. Stüvel )
Do not download assets when dragging them ( commit ) - ( Julian Eisel )
Show builtin libraries in the Preferences ( commit ) - ( Julian Eisel )
Show banner in asset browser when online access is diabled ( commit ) - ( Julian Eisel )
Add Preferences option to disable online essentials ( commit ) - ( Julian Eisel )
Compositor
Use blend name as default filename in File Output node ( commit ) - ( Pablo Vazquez )
Port Boolean Math node ( commit ) - ( Cristian Ivana )
Core
Recompute indirect linked tag after file load ( commit ) - ( Jacques Lucke )
Project Awareness and UI ( commit ) - ( Nathan Vegdahl )
Add profiling markers for memory usage ( commit ) - ( Sean Kim )
Profile: Use a grey color for the Default Profile category ( commit ) - ( Jonas Holzman )
Cycles
oneAPI: Update message when no oneAPI devices are available ( commit ) - ( Nikita Sirgienko )
Metal: Integrate MTLResidencySets for explicit memory management ( commit ) - ( Michael Jones )
oneAPI: Increase minimal Intel Linux driver after IGC upgrade ( commit ) - ( Nikita Sirgienko )
Split OptiX kernels into smaller modules to improve load time ( commit ) - ( Brecht Van Lommel )
EEVEE
Increase motion blur tests threshold for M1 ( commit ) - ( Clément Foucault )
Enable the gbuffer lib tests ( commit ) - ( Clément Foucault )
Add shading_offset to the test blocklist on intel ( commit ) - ( Clément Foucault )
Scene Time node shadow update optimizations ( commit ) - ( Miguel Pozo )
Extensions
Use consistent tooltip for all online access toggles ( commit ) - ( Julian Eisel )
Shader: Add easier way to check unused parameters ( commit ) - ( Clément Foucault )
Geometry Nodes
Store curves surface data before modifier stack evaluation ( commit ) - ( Hans Goudey )
Support renaming output sockets for Closure to List directly ( commit ) - ( W_Cloud )
Move inputs below outputs for Closure To List node ( commit ) - ( W_Cloud )
Add various profiling markers ( commit ) - ( Hans Goudey )
Bone Info node Exists output ( commit ) - ( Cartesian Caramel )
Integrate existing hair nodes and new hair dynamics assets ( commit ) - ( Simon Thommes )
Remove experimental option for hair dynamics ( commit ) - ( Jacques Lucke )
Bevel Node ( commit ) - ( Howard Trickey )
New Sort List node ( commit ) - ( Brady Johnston )
ImBuf
Implicit sharing for metadata ( commit ) - ( Brecht Van Lommel )
Images
Refactor OpenEXR API and fix some multi-layer issues ( commit ) - ( Brecht Van Lommel )
Keymap
Frame active item in TreeView with Mouse Button 4 ( commit ) - ( Nika Kutsniashvili )
LibOverride
Add a new Outliner ‘remove override operation’ operator/tool. ( commit ) - ( Bastien Montagne )
Add initial support for geonodes packed bakes. ( commit ) - ( Bastien Montagne )
Modeling
Support interpolation of vertex custom data when merging vertices ( commit ) - ( Tariq-Sulley )
Add snap point functionality to the uv editor ( commit ) - ( Tariq-Sulley )
Nodes
Don’t inherit node width for reroutes with Make Group operator ( commit ) - ( quackarooni )
Don’t draw indirectly linked node groups in menu ( commit ) - ( Jacques Lucke )
Optimize Four Color Mix Modes ( commit ) - ( Raiko )
Sculpt
Add profile markers ( commit ) - ( Sean Kim )
Shading
Use Environment Texture node when drag-drop in World editor ( commit ) - ( Oxicid )
Use title instead of upper case for quick fluid modifier name ( commit ) - ( Damien Picard )
Use int to store enum value, avoid float conversion ( commit ) - ( Hans Goudey )
Paint: Adjust brush “Advanced” settings ( commit ) - ( Sean Kim )
Support refreshing sub-menus ( commit ) - ( Julian Eisel )
Reorder context menu in Nodes editors ( commit ) - ( Eitan Traurig )
Right click for asset/file browser context menu with right click select ( commit ) - ( Julian Eisel )
Add missing Copy/Paste icons ( commit ) - ( Eitan Traurig )
Reorganize context and “Key” menus in Dope Sheet ( commit ) - ( Eitan Traurig )
Add missing icons in context and “Object” menus in 3D viewport ( commit ) - ( Eitan Traurig )
Improve tooltips for shape key operators and properties ( commit ) - ( Nika Kutsniashvili )
Improve view item dragdrop near edges ( commit ) - ( Pratik Borhade )
Location Scouting ( commit ) - ( Jonas Holzman )
Add width and height parameter to Solid Color Strips ( commit ) - ( Aleš Jelovčan )
Reorganize and clean up context menu ( commit ) - ( John Kiril Swenson )
Vulkan
Synchronization issues when uploading CPU data to pool texture ( commit ) - ( Jeroen Bakker )
Prevent Selection Operators From Overriding Operator Repeat ( commit ) - ( Tariq-Sulley )
Weight Paint
Update default settings and bundled assets ( commit ) - ( Sean Kim )
Weekly Reports
Aaron Carlisle
Alaska
Bart van der Braak
Bastien Montagne
Campbell Barton
Casey Bianco-Davis
Christoph Lendenfeld
Clément Foucault
Dalai Felinto
Falk David
Guillermo Venegas
Habib Gahbiche
Hans Goudey
Jacques Lucke
Jeroen Bakker
Jesse Yurkovich
John Swenson
Jonas Holzman
Julian Eisel
JulienDuroure
Lukas Tönne
Kévin Dietrich
Mark van de Ruit
Martijn Versteegh
Miguel Pozo
Nathan Vegdahl
Nika Kutsniashvili
Omar Emara
Pablo Vazquez
Philipp Oeser
Pratik Borhade
Richard Antalík
Sean Kim
Sebastian Herholz
Sergey Sharybin
Sybren Stüvel
Tariq Sulley
Thomas Dinges
Weizhen Huang
Wu Yiming
4 Likes
Home
Categories
Guidelines
Terms of Service
Privacy Policy
Powered by Discourse , best viewed with JavaScript enabled
