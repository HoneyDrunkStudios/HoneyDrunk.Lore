---
source: "https://devblogs.microsoft.com/dotnet/build-your-own-ai-agent-harness-in-csharp-the-maf-claw-live-series"
title: "Build Your Own AI Agent Harness in C#, the MafClaw Live Series"
author: "Bruno Capuano"
date_published: "2026-09-16"
date_clipped: "2026-09-19"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Build Your Own AI Agent Harness in C#, the MafClaw Live Series

Source: [Build Your Own AI Agent Harness in C#, the MafClaw Live Series](https://devblogs.microsoft.com/dotnet/build-your-own-ai-agent-harness-in-csharp-the-maf-claw-live-series)

*Attributed summary of the fetched written article; not a verbatim reproduction.*

Microsoft's written MafClaw walkthrough builds an agent around IChatClient with AsHarnessAgent and configurable harness providers. The article includes code for tools, a rooted file store, approvals, planning, and memory; the capture concerns that written material rather than the accompanying streams.

Read-only file operations can be approved automatically while consequential tools require an explicit decision. A timeout example bounds retries, denies after unanswered attempts, and keeps denial effective for the current prompt. Durable memory requires a confirmed storage operation, suitable scope, and visible failure handling.

The walkthrough separates discoverable skills, shell execution, controlled code execution, and background work. It also describes telemetry, governance, evaluations, and hosted deployment. Filesystem restrictions and approvals do not replace execution isolation.

HoneyDrunk implication: assess the harness as a reusable .NET runtime while retaining application ownership of tools, persistence, and authorization. Local shell or file capabilities should be reconsidered explicitly when moving the same agent definition into a shared hosted environment.
