---
source: "https://80.lv/articles/how-grabbit-2-simulates-physics-inside-the-unity-editor"
title: "How Grabbit 2 Simulates Physics Inside the Unity Editor"
author: "William Besnard"
date_published: "2026-08-03"
date_clipped: "2026-08-13"
category: "Game Development / Unity"
source_type: "web"
---

# How Grabbit 2 Simulates Physics Inside the Unity Editor

Source: https://80.lv/articles/how-grabbit-2-simulates-physics-inside-the-unity-editor

# How Grabbit 2 Simulates Physics Inside the Unity Editor

William Besnard spoke about Grabbit 2, a Unity Editor plugin for level design and set dressing, explaining how it works, the technical challenges, how collisions are handled, the lessons from Grabbit 1, and the five interactive modes.

### Introduction

I'm Will, the Solo Developer behind Jungle, a small family of Unity tools. I just released Grabbit 2, a ground-up rebuild of a plugin that has allowed game devs to design levels and set dress with physics in Unity since 2021. Here's a look at how it works, the things I got wrong the first time, and what changed in the rebuild.

### The Idea, and Why It's Harder Than It Sounds

Grabbit drops your selection into a live physics simulation inside the Editor. Objects are driven by physics just as they would be at runtime, except it happens in edit mode, without the need for any colliders or Rigidbodies attached to your objects.

Once you're done, Grabbit writes the result back to your transforms and cleans everything up. That last part is much trickier than you might expect:

- You have to drive Unity’s physics world yourself, at edit time, without disturbing the rest of the scene or the project’s physics settings.
- You have to generate accurate collisions for arbitrary meshes on the fly, because the objects being placed may not have any.
- You have to do it all non-destructively, so that if anything goes wrong, the scene comes back exactly as it was.
- In large scenes (10k game objects or more), you still want the tool to load fast and act fast: creating colliders and Rigidbodies for all meshes would take a few seconds.

### How Does Grabbit Handle That?

Unity lets you switch its physics into a manual mode where nothing steps on its own, and you own the clock. Grabbit uses that to run its own simulation loop entirely in editor time. When you grab a selection, two things matter: speed and isolation. For speed, Grabbit 2 pre-analyses your scene and only pulls in the objects near your selection, so loading is fast and stays fast however big the scene gets (Grabbit 1 loaded everything up front).

For isolation, Grabbit disables every other Rigidbody and remembers your physics settings before it steps the simulation, then restores them all when you're done, even if something goes wrong. Your other objects never move, and your project settings come back untouched.

### Colliders Are Tricky

The problem with colliders created on the fly is that PhysX only allows convex colliders to exist on dynamic objects, so a chair collides like a wedge and a doughnut collides like a disc. That is not great for set dressing, where the whole point is that things settle believably.

Grabbit covers that with convex decomposition: it breaks concave meshes into several convex pieces that together approximate their true shape. In Grabbit 2, this is done automatically in the background, so there is no visible waiting time for collider baking.

It ships three collider creation strategies, and you pick the one that suits your project:

- Balance uses a fast voxel-based decomposition. A solid all-round default.
- Precision uses a newer, collision-aware decomposition that keeps concave detail much better on tricky shapes.
- Performance skips decomposition and fits simple primitives (box, sphere, capsule, cylinder) to the mesh. Cheapest to simulate, and often all a simple prop needs.

While an accurate bake is still cooking, Grabbit swaps in a quick approximation so you are never blocked.

### New in Grabbit 2: Bake Colliders for Runtime

Once you have generated colliders, there is an obvious next step the original never took: make them permanent. In Grabbit 2, you can right-click any object or prefab in the scene, in Prefab Mode, or straight in the Project window, and choose Bake Convex Colliders. Grabbit writes the baked colliders onto the object.

Those colliders ship in your build and need no Grabbit code at runtime. You can also browse every collider you've baked in the collider library.

### What Went Wrong the First Time, and What I Fixed

Grabbit 1 worked, but structurally it was a single tool of around two thousand lines, and it had the failure modes you would expect from something that grew organically. Since there is growing interest in building editor tools like this, the honest lessons are probably the most useful part of this article.

It could leave a mess. Grabbit's whole model is "add temporary physics, simulate, remove it." If the Editor recompiled your scripts mid-edit or crashed, that cleanup might not run, leaving stray Rigidbodies or altered settings behind. Grabbit 2 records enough state to recognize an interrupted session, and on the next load, it detects the leftover physics and restores your objects automatically. And if it ever misses something, a one-click cleanup is included.

It got slow on big scenes. There was no spatial structure, so cost scaled badly. Grabbit 2 keeps a persistent spatial cache, pools its temporary colliders instead of allocating per grab, bakes in parallel, and only simulates what is near your selection.

Undo was unreliable. Physics-driven edits are exactly what you want to be able to undo with confidence. In Grabbit 2 every change goes through Unity's Undo system, so Ctrl+Z does exactly what you expect.

It lived in an Editor window, and every trip to that window pulled you out of the scene. Switching context costs time. Grabbit 2 integrates with the scene toolbar, so you can dock it and everything stays in context.

None of these are glamorous, but they are the difference between a clever demo and a tool you trust with a real project, and they are why the rebuild was worth doing from scratch.

### Five Modes: A Full Level Design Toolbox

The interactive side is organized into five modes, each a different way of moving objects, and every one is a native Unity Editor tool with its own Scene View overlay. Every shortcut is a real, rebindable Unity binding, and Space is the primary action everywhere.

**Select**builds your working set without touching the Hierarchy: pick by volume, by what is on screen, or from your current selection, then filter by same mesh, similar size or shared resting height.**Create**spawns props from a weighted collection, or duplicates your selection, and lets physics settle them as they land. It can lay copies out along a line, spline, ring or volume.**Place**is the main mode: move objects so they slide along surfaces and avoid overlaps, or grab an object by the exact point you clicked to seat a chair leg precisely.**Arrange**brings order in one tap: align onto a line or curve, level onto a shared plane, orient to a common frame, or fix collisions by pushing overlaps apart, all driven by PhysX.**Scatter**is the opposite: randomize, explode outward from a blast sphere, cram into a heap, or nudge each object a little for subtle variation, also physically driven.

### An Optional AI Hook

For teams that use an AI assistant inside Unity, Grabbit 2 can optionally expose its operations as tools the assistant can call, through the open Model Context Protocol. In practice that means you can ask your assistant to place or scatter a set of props and have Grabbit run the real physics operation and settle them properly, instead of the assistant guessing coordinates. It is entirely opt-in: the integration is inactive unless you have installed an MCP host yourself, it is editor-only, and it adds nothing to your build.

### Where It Is Going

I build Jungle's tools, but I am a game developer first, and I use Grabbit every day to build my own games faster. That is the honest reason it keeps improving: I want it for myself. Grabbit 2 requires Unity 6; Grabbit 1 remains available for projects on Unity 2022.3 and up.

If you do level design in Unity, I would love for you to try it and tell me where it falls short. Feedback is what made Grabbit what it is today!

Useful links:

- Asset Store.
- Discord.
- X/Bluesky: @shrubokrant
