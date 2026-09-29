---
source: "https://azure.microsoft.com/en-us/blog/your-architecture-diagram-is-not-your-resilience/"
title: "Your architecture diagram is not your resilience"
author: "Mark Russinovich, Adam Bogobowicz and Molina Sharma"
date_published: "2026-09-23"
date_clipped: "2026-09-29"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Microsoft argues that resilience must be verified as deployments and dependencies change. Zone distribution can coexist with a single-zone health dependency; replicated workloads can still depend on encryption keys available only in the failed region. AI endpoints add failure modes such as throttling, model withdrawal, and unacceptable operating cost.

The article connects application-level health signals, explicit recovery objectives, dependency analysis, safe rollout stages, and exercised failover paths. It also recommends deterministic verification around probabilistic agent behavior wherever practical.

For HoneyDrunk, keep recovery dependencies and model fallback behavior in the same validation scope as infrastructure. Azure Infrastructure Resiliency Manager is described as a public preview, with capabilities varying by workload; the article explicitly acknowledges incomplete assessment coverage. Product availability and generated remediation are not evidence that a particular application's recovery objectives have been met. This capture also provides software-architecture coverage through failure-boundary and dependency analysis.

Source: [Original article](https://azure.microsoft.com/en-us/blog/your-architecture-diagram-is-not-your-resilience/).
