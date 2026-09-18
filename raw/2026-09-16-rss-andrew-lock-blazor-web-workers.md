---
source: "https://andrewlock.net/exploring-the-dotnet-11-preview-1-running-background-tasks-in-blazor-with-web-workers/"
title: "Running background tasks in Blazor with Web Workers: Exploring the .NET 11 preview - Part 1"
author: "Andrew Lock"
date_published: "2026-05-12"
date_clipped: "2026-09-16"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Running background tasks in Blazor with Web Workers: Exploring the .NET 11 preview - Part 1

Source: [Running background tasks in Blazor with Web Workers: Exploring the .NET 11 preview - Part 1](https://andrewlock.net/exploring-the-dotnet-11-preview-1-running-background-tasks-in-blazor-with-web-workers/)

## Attributed content summary

Andrew Lock demonstrates the .NET 11 preview 3 Web Worker template for running CPU-intensive Blazor work away from the browser UI thread. The worker lives in a separate project referenced by the application.

The example exports browser-compatible static methods through JSExport, serializes complex results for the interop boundary, creates a WebWorkerClient, and invokes worker methods asynchronously. Merely making a CPU-bound operation asynchronous does not move its work off the UI thread.

Worker startup initializes an isolated .NET runtime, so repeatedly creating workers adds overhead. Reusing a worker can amortize that cost; application ownership and disposal still need deliberate handling. The article also inspects the generated interop and message-passing implementation.

Use this as a concrete browser-compute architecture example. Its package versions, template behavior, and setup details belong to an early preview and require rechecking on newer SDKs. Benchmark startup, memory use, serialization cost, and UI responsiveness with the intended workload.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
