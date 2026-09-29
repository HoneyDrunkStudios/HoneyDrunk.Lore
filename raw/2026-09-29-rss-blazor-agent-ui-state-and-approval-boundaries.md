---
source: "https://devblogs.microsoft.com/dotnet/build-agentic-ui-blazor/"
title: "Build Agentic UI with the new Blazor AI components"
author: "Daniel Roth"
date_published: "2026-09-28"
date_clipped: "2026-09-29"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Microsoft introduces experimental Blazor components that turn streamed agent responses into observable UI blocks. UIAgent wraps IChatClient; typed variants expose application state, while AGUIChatClient connects remote agents without making the rendering layer depend directly on AG-UI.

The sample distinguishes server tools, application-local tools, and actions that pause for user input. Approval blocks gate consequential server calls. Shared state uses snapshots and patches; proposed document changes remain separate from committed state until accepted. Unresolved proposals are rejected when execution fails, is cancelled, or finishes without a decision.

For HoneyDrunk, the useful pattern is application-owned rendering and explicit commit boundaries around agent-generated state. Evaluate cancellation, failed streams, and state reconciliation before adopting the experimental package. The article requires .NET 11 RC1 and a prerelease package; it demonstrates integration, not production stability.

Source: [Original article](https://devblogs.microsoft.com/dotnet/build-agentic-ui-blazor/).
