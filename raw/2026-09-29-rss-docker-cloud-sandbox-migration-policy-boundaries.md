---
source: "https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/"
title: "Introducing Cloud Sandboxes: Start on Your Laptop, Finish in the Cloud"
author: "PeiFang Sung"
date_published: "2026-09-24"
date_clipped: "2026-09-29"
category: "Security & Ethical Hacking"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Docker describes managed cloud execution using the same microVM isolation approach as local Sandboxes. Moving a sandbox copies its filesystem and recreates the environment at the destination; this is distinct from promising continuity of running processes.

The platform provides prebuilt environments, MCP connectivity, endpoint policies, and proxy-mediated secret injection. Crucially, the article says local and cloud environments maintain separate secrets, templates, and network policies. A filesystem move therefore does not establish equivalent authorization or network access at the destination.

For HoneyDrunk, evaluate migration as both workload transfer and policy reconfiguration. Verify allowed destinations, credential delivery, task limits, and return of work artifacts before unattended use. The launch requires sbx 0.45.1 or later and an eligible consumption plan. These are vendor-described controls; this capture does not independently validate isolation or prompt-injection resistance.

Source: [Original article](https://www.docker.com/blog/introducing-cloud-sandboxes-start-on-your-laptop-finish-in-the-cloud/).
