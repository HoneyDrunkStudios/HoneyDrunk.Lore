---
source: "https://dev.to/gameoptim/how-can-unity-developers-track-managed-heap-allocations-on-worker-threads-2d4e"
title: "How Can Unity Developers Track Managed Heap Allocations on Worker Threads?"
author: "GameOptim"
date_published: "2026-10-09"
date_clipped: "2026-10-12"
category: "Game Development / Unity"
source_type: "rss"
---

# How Can Unity Developers Track Managed Heap Allocations on Worker Threads?

Moving work that does not require Unity APIs to worker threads can reduce main-thread pressure and help improve frame rates. However, identifying managed heap allocations on these threads can be challenging because Unity Profiler may not show their `GC.Alloc` activity.

GOT Online's Mono mode now supports **multithreaded allocation statistics**, allowing developers to inspect managed heap allocations made by non-main threads, investigate potential memory leaks, and compare heap growth between snapshots.

[New users can get 2 hours of free GOT Online testing time after completing registration.](https://www.gameoptim.com/?fopt=dev)

## Introduction

To reduce main-thread workload and improve frame rates, Unity developers often move operations that do not depend on Unity APIs to worker threads.

However, when analyzing managed heap usage, it can be difficult to identify exactly where allocations occur on these threads. This makes memory profiling and leak investigation more challenging.

To address this issue, GOT Online supports multithreaded statistics in **Mono mode**. Combined with GOT Online's flexible workflow for testing changes and checking results, this feature helps developers investigate memory allocation issues more efficiently.

## Why Should Unity Developers Track Heap Allocations on Worker Threads?

Consider a component that starts two worker threads in `Start()`. Both threads periodically allocate managed heap memory.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fdgtut3ow59ua31mzdrle.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Farticles%2Fdgtut3ow59ua31mzdrle.png)

In this scenario, Unity Profiler may not display the `GC.Alloc` activity associated with these worker-thread allocations.

However, these allocations still matter. Like allocations on the main thread, they can contribute to garbage collection overhead when allocations occur frequently. If objects remain referenced longer than intended, they can also contribute to sustained heap growth or memory leaks.

Being able to identify where these allocations originate is therefore important when investigating managed memory usage in multithreaded Unity projects.

## How Can GOT Online Identify Managed Allocations on Worker Threads?

Run a test using **Mono mode** in GOT Online, then open the **Detailed Heap Allocations** page in the performance report.

Functions associated with allocations on non-main threads appear with the `Thread` prefix. This indicates that the function was called on a non-main thread and performed managed heap allocations.

Select a function to inspect its allocation details.

This allows developers to investigate allocation activity that may otherwise be difficult to identify when focusing only on the main thread.

## How Can Developers Investigate Heap Growth and Potential Memory Leaks?

Allocations on worker threads can also be relevant when investigating managed heap growth.

If objects remain referenced and cannot be reclaimed by the garbage collector, the corresponding memory growth can be examined in the **Heap Memory Leak Analysis** panel.

Developers can locate the relevant function and compare two selected nodes to inspect changes in heap usage between them.

This comparison helps developers investigate whether heap usage is increasing over time and narrow down the functions associated with that growth.

## How Can Developers Inspect the Objects Behind Heap Allocations?

After identifying a function of interest, click the blue button on the right to view the associated managed heap object types.

The report displays the allocation size and object count for each type, helping developers understand which objects account for the observed memory usage.

This additional detail can help developers determine whether a function is allocating too frequently or contributing significantly to heap growth.

## What Should Unity Developers Take Away?

* Moving work to worker threads can reduce main-thread pressure, but managed heap allocations on those threads still need to be monitored.
* Unity Profiler may not expose all worker-thread allocation activity through the expected `GC.Alloc` view.
* GOT Online Mono mode identifies non-main-thread allocation functions with the `Thread` prefix.
* The Detailed Heap Allocations page provides function-level allocation details.
* Heap Memory Leak Analysis helps developers investigate memory growth and compare selected nodes.
* Object type, allocation size, and object count provide additional clues for diagnosing memory issues.

By including worker-thread allocations in managed memory analysis, Unity teams can investigate heap usage more comprehensively instead of focusing exclusively on the main thread.

## FAQ

### Can worker threads allocate managed heap memory in Unity?

Yes. Worker-thread code can allocate managed objects, depending on the operations it performs. These allocations can contribute to garbage collection overhead and sustained heap growth.

### Why might Unity Profiler not show worker-thread allocations in the expected `GC.Alloc` view?

The allocation activity described here may not be visible in the usual Unity Profiler view. GOT Online Mono mode provides additional statistics for investigating managed heap allocations made by non-main threads.

### How does GOT Online identify worker-thread allocation functions?

In the Detailed Heap Allocations page, functions associated with allocations on non-main threads are marked with the `Thread` prefix.

### Can GOT Online help investigate memory leaks involving worker threads?

Yes. Developers can use Heap Memory Leak Analysis to examine heap growth associated with relevant functions and compare two selected nodes. Object types, allocation sizes, and object counts provide further information for investigation.

## About GameOptim GOT Online

**GameOptim GOT Online** is a cloud-based performance analysis platform for Unity game development. It provides tools for investigating CPU, GPU, and memory performance, helping development teams identify bottlenecks and analyze issues using detailed test reports.

Its Mono mode supports managed heap allocation analysis, including multithreaded allocation statistics, to help developers investigate memory behavior beyond the main thread.
