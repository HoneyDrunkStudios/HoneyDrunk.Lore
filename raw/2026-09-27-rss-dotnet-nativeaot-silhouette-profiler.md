---
source: "https://andrewlock.net/creating-a-dotnet-profiler-using-csharp-with-silhouette/"
title: "Creating a .NET CLR profiler using C# and NativeAOT with Silhouette"
author: "Andrew Lock"
date_published: "2025-12-16"
date_clipped: "2026-09-27"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Creating a .NET CLR profiler using C# and NativeAOT with Silhouette

Source: [Creating a .NET CLR profiler using C# and NativeAOT with Silhouette](https://andrewlock.net/creating-a-dotnet-profiler-using-csharp-with-silhouette/)

Capture note: Original summary of the fetched article; full text is not reproduced.

Andrew Lock demonstrates a CLR profiler written in C# and compiled as a native library with NativeAOT. Silhouette supplies callback base classes and generated entry-point plumbing, reducing the manual native-interface work. The example subscribes to runtime events and reports loaded assemblies.

Initialization checks which profiling interface version is available before accessing it. Results still follow native error semantics; convenient exception conversion in the sample is explicitly unsuitable as an unquestioned production pattern. Publishing the target application separately avoids accidentally profiling the .NET SDK through dotnet run.

Activation requires the profiler identifier and native-library path, with different environment-variable families for .NET Framework and CoreCLR. NativeAOT does not remove the need to understand callback behavior and unmanaged APIs.

HoneyDrunk relevance: a focused route for diagnostic prototypes beyond normal application telemetry. This is a December 2025 evergreen backfill, not a new release or production-readiness claim.
