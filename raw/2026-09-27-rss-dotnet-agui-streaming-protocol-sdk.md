---
source: "https://devblogs.microsoft.com/dotnet/ag-ui-dotnet-sdk/"
title: "AG-UI Protocol now has a first-class .NET SDK"
author: "Daniel Roth"
date_published: "2026-09-25"
date_clipped: "2026-09-27"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# AG-UI Protocol now has a first-class .NET SDK

Source: [AG-UI Protocol now has a first-class .NET SDK](https://devblogs.microsoft.com/dotnet/ag-ui-dotnet-sdk/)

Capture note: Original summary of the fetched article; full text is not reproduced.

Microsoft's SDK exposes AG-UI through separate client, server, protocol, formatting, and optional protobuf packages. An IChatClient backend can produce typed lifecycle, message, state, and tool events; the frontend chooses how to render them. Server-Sent Events is the default transport. Protobuf covers only a subset of events.

Microsoft Agent Framework now consumes these packages instead of maintaining its own protocol implementation. Migration includes renaming AddAGUI/MapAGUI to AddAGUIServer/MapAGUIServer, moving namespaces, and using an options-based client constructor. The article says the wire format remains compatible with existing frontends.

HoneyDrunk relevance: evaluate a shared streaming contract across agent surfaces while keeping application hosting and rendering separate. Validate interrupts, parallel tools, state changes, and cancellation against the intended client.

Evidence posture: official implementation announcement with examples; no local integration was tested.
