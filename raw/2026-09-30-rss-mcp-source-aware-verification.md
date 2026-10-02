---
source: "https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source"
title: "Getting the Source Right, Not Just the Fact: Source-Aware Verification for MCP Agents"
author: "unknown"
date_published: "2026-09-29"
date_clipped: "2026-09-30"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

ProvenanceGuard verifies an MCP agent’s answer claim by claim while retaining the identity of each tool source. It checks factual support and whether the answer attributes that support to the correct source, then allows, blocks, or repairs the answer. The authors report catching 138 of 139 claims requiring rejection in a held-out packet, while also blocking 67 supported claims. Exact source identification fell to 50.3% in a harder multi-source test. For HoneyDrunk, preserve tool-output IDs through retrieval and verification; pooled factuality scores can conceal incorrect attribution. These are results from the authors’ local medical-agent evaluation, requiring fresh calibration for other workloads.

Source: [Original article](https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source).
