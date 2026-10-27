---
source: "https://kashi45248-prog.github.io/Blackbox_creations-/tutorial-meta-quest-72fps-mesh-optimization.html"
title: "Meta Quest 72 FPS: The Unity Mesh Optimization Checklist"
author: "Kashif Nazir"
date_published: "unknown"
category: "Game Development / Unity"
source_type: "web"
date_clipped: "2026-10-26"
discovered_via: "https://dev.to/kashifnazir/meta-quest-72-fps-the-mesh-checklist-that-actually-holds-the-frame-budget-4ej7"
---

# Meta Quest 72 FPS: The Unity Mesh Optimization Checklist

72 frames per second means 13.9 milliseconds per frame — for everything: physics, scripts, and rendering, times two eyes. Most Quest games that miss the target don't have a shader problem; they have a mesh problem. This is the exact checklist to fix it.

## The frame budget is non-negotiable

On Quest, dropped frames don't just look bad — they cause motion sickness. Meta's guidance targets 72 FPS minimum (Quest 2/3S) with 90 FPS ideal on Quest 3. That gives you **13.9ms per frame at 72Hz**, and rendering typically gets about half of it once game logic takes its share. Every item below exists to protect those ~7ms of GPU/CPU rendering time.

The good news: hitting it is mostly about discipline, not heroics. The same five mesh optimizations, applied systematically, take most Unity scenes from 45 FPS to a locked 72.

## The checklist

- **1. Draw calls under ~150.** Check the Game view Stats panel → "Batches". Quest's mobile CPU chokes on draw-call overhead long before the GPU breaks a sweat. Combine meshes, bake texture atlases, and enable the SRP Batcher. Single Pass Instanced rendering (not Multi-Pass) halves your stereo draw calls — set it in the XR Plug-in Management settings.
- **2. Visible triangles under ~750k.** This is the widely used Quest comfort zone. Audit with the Frame Debugger or Profiler: find your heaviest meshes and simplify them. Background geometry almost never needs the triangle density it ships with.
- **3. LODs on everything beyond arm's reach.** Use LODGroup with 2–3 levels; aggressive cutoffs are fine in VR because distant detail is genuinely hard to see in a headset. Generate LODs for your whole library in one pass rather than hand-tuning per model.
- **4. Textures: 1024 max for environments, ASTC compression.** Large textures murder mobile fill rate. Walls and floors at 1024, props at 512 or below, and always ASTC — it's the compression format mobile GPUs actually like. Atlases help twice here: fewer draw calls AND fewer texture binds.
- **5. Bake all lighting. Zero realtime lights.** Realtime shadows are one of the most expensive things you can do on Quest. Bake lightmaps, use light probes for dynamic objects, and turn the main directional light's shadows off or to the cheapest possible setting.
- **6. Kill overdraw.** Transparent particles, overlapping UI, and layered alpha geometry destroy tile-based mobile GPUs. Audit with the overdraw view mode; replace alpha-blended particles with alpha-tested or opaque where possible.
- **7. Enable Fixed Foveated Rendering.** Via the Meta XR SDK, render the periphery at lower resolution — up to ~28% pixel shading savings with no perceptible quality loss. It's nearly free performance; there's no reason to ship without it.

## The systematic mesh pass (in order)

Don't optimize randomly. Run this pipeline over your scene and measure after each step:

1. **Simplify** — reduce triangle counts on every mesh that's denser than its on-screen size justifies. Target the worst offenders first (check the Profiler's Rendering module sorted by triangles).
2. **LOD** — generate LOD1/LOD2 for all environment meshes and set screen-relative transition heights. In VR, you can cut LOD0→LOD1 earlier than on flat screens.
3. **Combine + atlas** — merge static geometry per area chunk and bake texture atlases so each chunk draws in a handful of calls instead of hundreds.
4. **Verify** — Stats panel: batches under 150, tris under 750k. Then profile on-device with OVR Metrics — the editor lies about mobile performance.

This order matters: simplifying first means your LODs and combined meshes are built from clean, light geometry instead of garbage-in-garbage-out.

## Why VR multiplies every cost

Everything on this checklist matters more in VR because the headset renders the scene **twice** — once per eye. With the old Multi-Pass stereo mode, that literally meant double the draw calls: 150 batches became 300, and your frame budget died. **Single Pass Instanced (SPI)** rendering fixes this by drawing both eyes in one pass using instanced draw calls, roughly halving the CPU cost of stereo. If your project still uses Multi-Pass, switching to SPI is the single biggest one-setting win available — find it under **Project Settings → XR Plug-in Management → Oculus → Stereo Rendering Mode**.

The SRP Batcher (on by default in URP) further reduces per-draw CPU overhead by caching material state, but it only helps when your materials are compatible — yet another reason the atlas-plus-shared-material workflow pays off on Quest specifically.

## Texture budgets and mip streaming on Quest

Quest's GPU uses tile-based rendering, which means **fill rate** — how many pixels get shaded — is often the real bottleneck, not triangle count. Oversized textures force the GPU to shade more pixels than the headset can display, burning milliseconds for invisible detail. The rules: cap environment textures at 1024, props at 512 or below, UI at whatever's legible (usually 1024 for hero panels), and compress everything with **ASTC** (6×6 or 8×8 block sizes are the sweet spot for quality vs size on Quest).

Enable **Mip Streaming** (Project Settings → Quality → Texture Streaming) so Unity only keeps the mip levels actually visible in memory — this can cut texture memory by 30–50% in large scenes. And audit overdraw with the Scene view's Overdraw shading mode: any area glowing white-hot is pixels being shaded many times over, usually from stacked transparent particles or layered alpha-tested foliage. Replace alpha-blended effects with alpha-tested or opaque geometry wherever the art allows it.

## Automating the pass

Doing this by hand across a real game's asset library is weeks of repetitive work — and it all needs redoing whenever art changes. You can script parts of it; for example, enforcing a global LOD bias at runtime for low-end devices:

```
// Tighten LOD transitions on Quest at startup
void Start()
{
#if UNITY_ANDROID && !UNITY_EDITOR
    // More aggressive LOD switching on standalone VR
    QualitySettings.lodBias = 0.6f;
    // Cap pixel lights (should be 0 anyway on Quest)
    QualitySettings.pixelLightCount = 0;
#endif
}
```

But the heavy lifting — simplification, LOD generation, combining, atlasing — is exactly what One Click Mesh Suite automates: point it at your project and it runs the whole simplify → LOD → combine pipeline in one pass, with settings tuned per platform.


## Verify on device, not in the editor

The Unity editor on your PC tells you almost nothing about Quest performance. Always verify with **OVR Metrics** (the on-headset overlay: FPS, CPU/GPU utilization, thermal state) and the **Unity Profiler** connected to a Quest build. Your targets: locked 72 FPS, GPU utilization under ~80% (headroom for thermal throttling), and frame times consistently under 13.9ms during your heaviest gameplay moments — not just standing in an empty room.

If you're still missing the target after the mesh pass, the next suspects are scripts (GC allocations per frame), physics (too many active rigidbodies), and post-processing (turn it all off on Quest — every effect costs milliseconds you don't have).
