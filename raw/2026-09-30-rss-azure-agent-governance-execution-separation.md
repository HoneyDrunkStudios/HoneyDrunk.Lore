---
source: "https://azure.microsoft.com/en-us/blog/designing-agent-first-platforms-what-changes-when-agents-do-the-work"
title: "Designing agent-first platforms: What changes when agents do the work"
author: "Mike Hulme"
date_published: "2026-09-23"
date_clipped: "2026-09-30"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Microsoft describes separating agent governance in Foundry from code execution in Azure Container Apps Sandboxes. Agent identity, scoped permissions, traces, and evaluation remain governance responsibilities, while each execution receives an isolated microVM environment with controlled access and pause/resume support. Customer examples illustrate per-engagement and per-user workspaces. For HoneyDrunk, model agent identity and task execution as separate layers, with explicit policy and trace continuity across the boundary. Isolation, startup performance, scale, and credential handling are vendor-described capabilities; verify them against the selected service configuration and workload.

Source: [Original article](https://azure.microsoft.com/en-us/blog/designing-agent-first-platforms-what-changes-when-agents-do-the-work).
