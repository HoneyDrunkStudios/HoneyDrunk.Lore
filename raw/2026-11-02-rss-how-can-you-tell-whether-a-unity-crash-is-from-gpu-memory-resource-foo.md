---
source: "https://dev.to/gameoptim/how-can-you-tell-whether-a-unity-crash-is-from-gpu-memory-resource-footprint-or-mono-heap-1cgh"
title: "How Can You Tell Whether a Unity Crash Is From GPU Memory, Resource Footprint, or Mono Heap Retention?"
author: "GameOptim"
date_published: "2026-11-02"
date_clipped: "2026-11-02"
category: "Game Development / Unity"
source_type: "rss"
---

# How Can You Tell Whether a Unity Crash Is From GPU Memory, Resource Footprint, or Mono Heap Retention?

**One high memory number hides three different root causes. GameOptim GOT Online's new PSS GPU trend, per-resource snapshots, and IL2CPP heap dumps split that single signal into three diagnosable metrics — so you can fix the right subsystem instead of guessing.**

Memory pressure crashes are one of the most common reasons a Unity build fails device certification or gets refunded on release. The frustrating part is that "memory is high" is almost never the whole story — GPU memory, general resource footprint, and Mono heap retention all contribute to the final OOM kill, and fixing the wrong one wastes days of iteration.

GameOptim GOT Online's latest release adds three new diagnostics that let you read each subsystem separately, instead of guessing from a single total memory number. This article explains what each new metric actually measures, how to read it correctly, and the caveats you need to know before acting on the data.

## Summary

* A single high memory value is useless unless you split it into **PSS GPU memory**, **resource memory**, and **Mono Reserved** — each points to a different subsystem with a different root cause.
* PSS GPU memory, newly added to GOT Online's Overview mode, shows the rendering memory the graphics driver reports; Android 10 and 11 refresh this value only every 5 minutes, so the curve appears stepped.
* The new **Memory Usage** page combines an overview table (PSS, Mono Reserved, resource, Lua heap) with per-resource breakdowns and frame-level snapshots marked on the time axis.
* **IL2CPP Mono heap snapshots** are now available without a separate Mono build, provided you build with Unity 2019.4+ and **Script Debugging** enabled.
* Sampling strategy matters: manual resource snapshots capture every resource in a frame, while periodic snapshots and Resource-mode data have lower resolution by design to keep instrumentation overhead acceptable.

## What Does "High Memory" Actually Mean in Unity?

Unity games draw memory from three distinct pools, and each pool grows for different reasons. Fixing a Mono leak with asset compression, or vice versa, never works.

| Subsystem | What it measures | Typical failure mode |
| --- | --- | --- |
| **PSS GPU Memory** | Rendering memory reported by the graphics driver — textures, meshes, driver libraries | OOM kills on Android when GPU memory spikes past the device threshold |
| **Resource Memory** | Total memory consumed by textures, meshes, animations, audio, and 7 other categories | Scene transitions that push total resources past device limits |
| **Mono Reserved** | Managed heap capacity held by the Mono runtime | Slow growth over a session that eventually exhausts process memory |

These three pools are independent. A game with moderate PSS can still crash from GPU memory; a game with stable resource memory can still leak Mono references. The new GOT Online features let you inspect each one without running three separate test passes.

## PSS GPU Memory: Reading the Driver's Number

The new PSS GPU memory trend appears in the Overview mode's **Runtime Info** page. GPU memory is the memory consumed by rendering resources at the driver level — texture data, mesh buffers, and memory allocated by the libraries that parse those resources. Unlike process PSS memory, this value is reported directly by the graphics driver rather than by the OS memory manager.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fabjopcof3zr97q9aa4x7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fabjopcof3zr97q9aa4x7.png)

When GPU memory rises near the device limit, the kernel kills the process — so tracking this number is critical for crash-risk management alongside PSS memory.

**Important caveat for Android 10 and Android 11:** Due to platform-level restrictions, these OS versions refresh the GPU PSS value only once every 5 minutes after boot. On those devices the curve appears as a step function, and a large jump at frame N actually reflects changes that accumulated over the preceding 5 minutes. When GPU memory spikes appear in reports from Android 10/11, trace back through events in the prior 5-minute window before assigning blame to a single frame.

## The Memory Usage Page: One Table, Three Questions

GOT Online's Overview mode now includes a **Memory Usage** page that consolidates memory diagnostics previously scattered across separate reports. The page is organized into two layers.

### Layer 1: The Overview Table

The overview table plots **PSS memory**, **Reserved Mono**, and **total resource memory** on one time axis. When Lua testing is enabled in Overview mode, Lua heap memory is added as a fourth curve. Resource memory here is the sum of all resource memory collected during the test.

GameOptim SDK samples data at five points by default — test start, every 1,000 frames, scene transitions, test end, and manual resource snapshots via the **Dump** operation. Only manual Dumps capture every resource in the current frame with full detail.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fk3lyu4xq1dp9b2xq97mq.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fk3lyu4xq1dp9b2xq97mq.png)

The default view shows three curves — **PSS memory**, **Reserved Mono**, and **total resource memory** — with all resource-object snapshot frames marked on the horizontal axis.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fhyvmdyowfz3ckg3iico9.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fhyvmdyowfz3ckg3iico9.png)

**Resource-mode caveat:** When Resource mode is enabled alongside Overview mode, the SDK collects detailed per-resource data. To keep instrumentation overhead acceptable, different resource categories are sampled on different frames. The resulting total resource memory is a simulated sum with a 60-frame step — lower accuracy, and hidden by default in the table.

**Performance caveat:** Running Overview mode with Resource mode enabled introduces measurable overhead (lower frame rate, stutter during collection). Do not use this combination for general gameplay performance analysis — it's specifically for resource memory diagnosis.

### Layer 2: Per-Resource Breakdown and Snapshots

The **Resource Memory Usage** table breaks resource memory into 11 categories: textures, meshes, animations, audio, and seven others. Each category gets its own trend line so you can see exactly which resource type is driving total memory pressure in each scene, and quickly judge which resource type is responsible for memory pressure in each scene.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fo59ixck85aqw6ga3f62l.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fo59ixck85aqw6ga3f62l.png)

Selecting a resource snapshot frame (in non-Resource mode) or any frame (in Resource mode) generates two artifacts below the table: a pie-chart preview showing resource-type memory share at that frame, and the corresponding resource detail data.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fbziaw4zt6slomzzudgsv.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fbziaw4zt6slomzzudgsv.png)

The resource-object snapshot module does two things at once: it shows the memory-share pie chart of each resource type at the selected frame, and lists every resource type in a table sorted by memory usage (largest first). For each type the table shows the quantity, memory usage, and a recommended-value flag — items exceeding the recommended value are highlighted in red so you can immediately locate categories that need attention.

Clicking the operation column in the table jumps directly to the corresponding tab in the Resource Memory page for deeper analysis. In the Resource Memory page, resource-object snapshot frames are also marked, so selecting any snapshot frame pulls up the detailed resource information for that moment.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Feyozs137zntlq0w9u15w.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Feyozs137zntlq0w9u15w.png)

The Memory Usage page also supports **comparison mode**: toggle it on from the bottom right, select any two snapshot frames (non-Resource mode) or any two frames (Resource mode), and the page shows the per-resource memory delta between them — quantity and size for every resource type.

## IL2CPP Mono Heap Snapshots: No Separate Mono Build Required

For managed memory analysis, GOT Online adds two new pages under **Heap Leak Analysis**: **Resident Heap Allocation Functions** and **Heap Object Snapshot**. These sit alongside the existing IL2CPP Mono heap allocation data collection, which requires Unity 2019.4 or later with **Script Debugging** enabled at build time.

Dump rules are configured before the test run — snapshots are collected either at a fixed frame interval or on manual trigger.

### Reading the Heap Object Snapshot

Developers can use the bar chart in the **Heap Object Snapshot** page to quickly identify which scenes retain heap memory worth optimizing. The chart supports two dimensions — **heap object size** and **heap object count** — so you can see whether retention comes from a small number of large objects or a large number of small ones.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fx7z1copa5st2svpg9lro.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fx7z1copa5st2svpg9lro.png)

Heap objects split into two parts: **Managed Objects** and **memory fragmentation**. Fragmentation itself splits further into **free active memory** (used first during allocation) and **free fragment memory** (used only when active memory is insufficient). Allocation always consumes from free active memory before falling back to fragments.

Below the bar chart, the page shows summary stats for the selected frame: total Managed Object size, total type count, total object count, and fragmentation ratio. On the right, a pie chart shows the share of the top 10 object types by memory usage, with the remainder grouped as "other" — giving you an immediate view of where Mono memory is concentrated so you can lock in on the bottleneck.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fp1klxa5810cth8gbx82a.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fp1klxa5810cth8gbx82a.png)

Below the pie chart sits the object-type table, which lists every object type in the selected frame along with its size, share, and object count. Expanding any object type reveals every function that allocated that type, and the inverse call path from those functions upward to your code.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ft15z9dwuxzd1es1xrbdi.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Ft15z9dwuxzd1es1xrbdi.png)

This is the critical diagnostic step: the call path tells you exactly where in your code the allocation originates, so you can search for the sub-function and fix the source rather than masking the symptom.

## Sampling Caveats That Change How You Read the Data

Three properties of GameOptim's sampling strategy are easy to overlook but directly affect what the data means:

1. **Resource-mode step size.** Detailed per-resource data is collected every 60 frames, not every frame. The simulated total curve has deliberate gaps. Do not treat a frame-to-frame dip in the simulated curve as evidence that memory was released.
2. **Dump triggers.** Only manual **Dump** operations capture every resource in the frame. Periodic samples (start, every 1,000 frames, scene transitions, end) are partial snapshots. If you need a complete view of resource state at a specific moment, trigger a manual Dump.
3. **Android 10/11 GPU PSS refresh.** As noted above, GPU PSS values on these devices update every 5 minutes. A spike at frame N is not necessarily caused by an event at frame N.

## Key Takeaways

* **PSS GPU memory, resource memory, and Mono Reserved are three independent signals.** Each one points to a different subsystem; no single number can diagnose a crash.
* **Android 10/11 users** must account for the 5-minute GPU PSS refresh rate when reading GPU memory spikes.
* **IL2CPP Mono analysis** now works from GOT Online — no separate Mono build needed, provided you build with Script Debugging enabled in Unity 2019.4+.
* **Manual Dump captures every resource**; periodic samples do not. Use manual Dumps when you need a complete frame-level picture.
* **Resource mode + Overview mode** has meaningful performance overhead. Use it for resource diagnosis only, not for general gameplay performance measurement.

## FAQ

**Why does my Android 11 report show a single frame where GPU memory jumps by 200 MB?**  
Android 10 and 11 refresh the GPU PSS value only once every 5 minutes. The jump reflects changes accumulated over the preceding 5 minutes, not a single frame's workload.

**Do I still need to build a separate Mono build to analyze heap retention?**  
No. On GOT Online, IL2CPP builds support Mono heap allocation data collection and snapshots, provided you build with Unity 2019.4 or later and have **Script Debugging** enabled.

**The total resource memory in my Resource-mode test looks lower than I expected. Is the report wrong?**  
When Resource mode is enabled alongside Overview mode, total resource memory is a simulated sum with a 60-frame step and lower accuracy. It is hidden by default for this reason.

**How do I compare memory usage between two scenes?**  
Use the comparison mode in the Resource Memory Usage table. Open comparison mode from the bottom right, select two snapshot frames, and the page shows the per-resource memory delta between them.

**Should I always run with Resource mode enabled to get better data?**  
Resource mode introduces significant overhead (lower frame rate, stutter). Enable it only when you specifically need per-resource breakdowns; for general crash-risk assessment, Overview mode with the new PSS GPU and Mono data is sufficient.
