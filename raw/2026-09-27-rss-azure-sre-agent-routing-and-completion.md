---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/getting-the-best-out-of-azure-sre-agent/4559745"
title: "Getting the best out of Azure SRE Agent"
author: "puneetguptams"
date_published: "2026-09-24"
date_clipped: "2026-09-27"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
---

# Getting the best out of Azure SRE Agent

Source: [Getting the best out of Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/getting-the-best-out-of-azure-sre-agent/4559745)

Capture note: Original summary of the fetched article; full text is not reproduced.

Microsoft's SRE Agent guidance emphasizes accessible telemetry, focused incident routing, useful skills, and permissions sufficient to complete the intended handoff. A specialist receiving unrelated incidents may appear ineffective even when it performs its intended task well.

The post recommends response-plan filters for routing, skills that explain applicability and decision steps, and custom agents for distinct recurring problems. An empty custom-agent tool list means default access, not zero access; identity permissions remain the outer boundary.

Approval mode can leave accurate work unfinished. The guide separates routine investigation from consequential changes and recommends testing one scenario through its final delivery step before connecting a live queue.

Its production comparisons are observational examples across different agents, not controlled before-and-after evidence. Scores also depend on task type and evaluation rules.

HoneyDrunk relevance: classify failures as routing, missing evidence, permissions, or approval backlog before rewriting prompts or adding tools.
