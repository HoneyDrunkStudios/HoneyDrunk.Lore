---
source: "https://dev.to/nabeelbaghoor/standalone-vr-gives-you-11-milliseconds-a-frame-the-editor-will-not-warn-you-3pk2"
title: "Standalone VR Gives You 11 Milliseconds a Frame. The Editor Will Not Warn You."
author: "Nabeel Hassan"
date_published: "2026-10-11"
date_clipped: "2026-10-12"
category: "Game Development / Unity"
source_type: "rss"
---

# Standalone VR Gives You 11 Milliseconds a Frame. The Editor Will Not Warn You.

If you have only ever shipped Unity to desktops and phones, a standalone VR headset will humble you. The editor says 200 fps. The headset says 61, then 58, then, twenty minutes into a session on a warm forehead, something worse.

I spent a good part of my career in XR before moving into AI engineering: a clinical eye-tracking app on the Vive Focus 3 at Nystag, and XR work like the ERIS platform at ARCortex. The single habit that carried across all of it was treating the frame as a budget, not a goal. This post is the practical version of that habit.

## A phone chip, rendering everything twice

A tethered headset borrows a desktop GPU. A standalone headset runs everything on a mobile chip inside the headset itself (the Focus 3 uses a Snapdragon XR2). That is exactly what makes standalone devices practical for real deployments, and exactly what makes them hard to render for.

Three things stack on top of each other:

* **You render the scene twice.** Once per eye, at high resolution, because the lenses magnify every pixel.
* **The frame rate is not negotiable.** On a phone you can sag to 30 fps and most users shrug. A headset display refreshes at a fixed rate (90 Hz on the Focus 3), and missing it is felt physically. The runtime will reproject old frames to cover gaps, but reprojection is a safety net, not a strategy.
* **The device is sealed and strapped to a head.** It cannot shed heat like a desktop. Run it hot for twenty minutes and the chip throttles, so your budget shrinks while the user is still mid-session.

So the useful question is never "is it fast on my machine." It is "does it hold frame rate, on the device, at minute thirty."

## The editor is decoration

Your desktop GPU is far faster than the headset and has no thermal limit, so I treat editor frame times as decoration. What I actually look at:

1. **A device build in week one,** so the baseline is known before there is much to render.
2. **The Unity Profiler attached to a development build on the headset.** The first thing it tells you, whether a slow frame is CPU-bound or GPU-bound, decides everything after it.
3. **The chip vendor's GPU tools.** For Snapdragon headsets, Qualcomm's profiling tools show GPU load, clocks and temperature, which Unity's profiler does not.
4. **A tiny on-device overlay** with frame time, dropped frame count and a throttle or temperature indicator where the platform exposes one.

The overlay can be very small. Something roughly like this, illustrative rather than lifted from a codebase:

```
// Illustrative: count frames that blew the budget, no per-frame allocations.
public class FrameBudgetOverlay : MonoBehaviour
{
    [SerializeField] float targetHz = 90f;
    [SerializeField] TMPro.TMP_Text label;
    int dropped;
    float worstMs;

    void Update()
    {
        float ms = Time.unscaledDeltaTime * 1000f;
        float budgetMs = 1000f / targetHz;
        if (ms > budgetMs * 1.5f) dropped++;
        if (ms > worstMs) worstMs = ms;
        if (Time.frameCount % 45 == 0)
            label.SetText("{0:1} ms  worst {1:1}  dropped {2}", ms, worstMs, dropped);
    }
}
```

Enter fullscreen mode

Exit fullscreen mode

Note the `SetText` with format arguments instead of string interpolation. An overlay that allocates every frame is an overlay that causes the stutter it is measuring.

## Write the budget down, then split it

At 90 Hz the whole frame is about 11.1 ms. At 72 Hz, about 13.9 ms. You do not get all of it, because the runtime needs its share for compositing and reprojection, so I plan to use noticeably less than the theoretical number and treat anything near the edge as a failure.

The move that actually changes team behaviour is splitting that budget between CPU and GPU. They run in parallel and the slower one sets your frame rate. Once the split is written down, every feature request gets one question: which side does this cost, and what are we removing to pay for it?

I later used the exact same discipline on voice agents, where the budget is milliseconds of silence on a phone line instead of milliseconds per frame. Different medium, same arithmetic.

## The CPU side: draw calls and garbage

On standalone headsets the CPU is the bottleneck more often than people expect, mostly because of draw calls and scripts.

**Single Pass Instanced stereo.** Drawing both eyes in one pass instead of two is usually the single biggest CPU saving available if a project is still on multi-pass. Custom shaders need small changes to support it, which is the best argument for switching on day one instead of after you have written twenty shaders.

**Draw calls.** Every object with its own material is CPU work before the GPU starts. The usual tools all apply: static batching for scenery that never moves, GPU instancing for repeated meshes, texture atlases and shared materials so things can actually batch, merged meshes where objects are always seen together, and the SRP Batcher in URP if your shaders support it.

**Garbage collection.** A GC pause you would never notice in a desktop app is a dropped frame in a headset. The fix is boring: no allocations in Update, no string building per frame, no LINQ in hot paths, pooling instead of Instantiate and Destroy. The profiler's allocation column should read zero in steady state. When it does not, that is a bug, not a nitpick.

## The GPU side: decide what not to draw

Once the CPU is under control, the GPU becomes the wall. Headset displays have a lot of pixels and you fill them twice.

* **No full-screen post-processing by default.** Bloom, depth of field, SSAO and grading passes are expensive on a mobile chip in stereo. Each one has to earn its way back in. The exception is 4x MSAA, which is relatively cheap on tile-based mobile GPUs and stops edges shimmering, which is very visible in a headset.
* **Bake the lighting.** Real-time lights and shadows are some of the most expensive things you can ask of a mobile GPU. Lightmaps and light probes give you most of the look. If a scene needs one real-time light, it gets one, not five.
* **Watch overdraw.** Stacked transparent particles, layered UI panels and glass materials shade the same pixel many times. This is usually an art direction fix more than a code fix.
* **Compress and right-size textures.** ASTC on Android-based headsets, mipmaps on, and question every 4K texture. Bandwidth on a mobile chip is precious.
* **Foveated rendering where the SDK offers it.** The lenses are sharpest in the centre, so rendering the periphery at lower resolution is mostly invisible and saves real GPU time. The Vive Wave SDK and others expose fixed foveation, and with eye tracking it can follow the gaze.

Most of the wins on this list are things you decided not to render, not clever shaders.

## The bug that appears at minute twenty

The most misleading performance test is the short one. A fresh headset at room temperature runs your app better than the same headset twenty minutes in.

So every release gets a soak test: the heaviest scene, thirty minutes or more, overlay recording frame time and temperature. If frame time creeps up as the device warms, you are living too close to the budget. The fix is headroom from the start, and using the platform's CPU and GPU performance level settings instead of always requesting maximum clocks, which only gets you to the thermal wall sooner.

## When a dropped frame is a wrong measurement

This is the part that changed how I think about performance. In a clinical eye-tracking app, the stimulus on screen is effectively the specification of the test. If a target is supposed to move smoothly and the app drops frames, the target jumps. The patient's eyes respond to the jump, the tracker records it faithfully, and the data now describes a test that is not the one you designed.

Nothing crashed. Nothing logged an error. The output just quietly stopped meaning what everyone assumed it meant. That shifts performance from a comfort concern to a correctness concern:

* **Timestamp against the frame actually displayed,** not when your script asked for it.
* **Log dropped frames per session and store them with the measurement,** so whoever reviews the data can see whether the stimulus was delivered as intended.
* **Prefer a simpler scene that never drops** over a richer one that drops occasionally.

## The checklist I actually use

1. Device build in week one, profiler attached, overlay on.
2. Frame budget written down, split between CPU and GPU, with headroom.
3. Single Pass Instanced stereo on.
4. Draw calls batched, materials shared, zero per-frame allocations.
5. No full-screen post by default, 4x MSAA on, lighting baked.
6. Textures compressed and right-sized, overdraw checked.
7. Foveation only where it does not touch what the user must see (in a clinical test, the periphery may be the test).
8. A thirty-minute soak test before every release.

None of this is glamorous. The habit underneath it, refusing to trust any number that did not come from the real device under real conditions, is the one I took with me from XR into AI work, and it has been just as useful there.

The original, slightly longer version of this lives on my site: [Unity performance on standalone VR headsets](https://nabeelbaghoor.com/blog/unity-performance-standalone-vr-headsets/). If you have shipped on Quest, Pico or Focus hardware, I would like to hear what your soak tests caught that a short test never did.
