---
source: "https://devblogs.microsoft.com/dotnet/coreclr-progress-and-mono-timeline-dotnet-maui"
title: "CoreCLR Progress and the Mono Timeline for .NET MAUI"
author: "David Ortinau"
date_published: "2026-07-14"
date_clipped: "2026-09-20"
category: ".NET Ecosystem"
source_type: "web"
capture_format: "attributed-summary"
---

# CoreCLR Progress and the Mono Timeline for .NET MAUI

Source: [CoreCLR Progress and the Mono Timeline for .NET MAUI](https://devblogs.microsoft.com/dotnet/coreclr-progress-and-mono-timeline-dotnet-maui)

Attributed summary of the fetched full written article; not a verbatim reproduction. Claims remain source-specific and have not been independently reproduced.

David Ortinau reports the .NET 11 Preview 6 milestone for moving MAUI Android, iOS, and Mac Catalyst applications to CoreCLR. In that preview, the former Mono-selection build property is removed. Blazor WebAssembly remains on Mono; the announcement does not describe a universal removal of Mono.

The article reports stronger iOS/Mac Catalyst performance and Android startup and package size within ten percent of Mono. These are project-level expectations requiring application measurement, not guarantees for every workload.

Its migration checklist is concrete: build Release artifacts, compare cold and warm startup on actual devices against a .NET 10 baseline, compare package size, exercise platform integrations, and validate libraries that depend on reflection or dynamic code generation. Check debugging and Hot Reload in the team's normal workflow.

This capture preserves a historical preview milestone and acknowledged unfinished scenarios. HoneyDrunk relevance: use its validation dimensions when evaluating mobile runtime upgrades rather than assuming server-runtime convergence eliminates migration work.
