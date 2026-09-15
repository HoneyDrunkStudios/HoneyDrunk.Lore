---
source: "https://kubernetes.io/blog/2026/09/11/kubernetes-v1-37-native-histograms-beta"
title: "Kubernetes v1.37: Native Histograms Graduates to Beta"
author: "Richa Banker"
date_published: "2026-09-11"
date_clipped: "2026-09-14"
category: "DevOps & CI/CD"
source_type: "rss"
capture_mode: "attributed-summary"
content_note: "Substantive summary of the fetched readable article; not a verbatim full-text archive."
discovered_via: "https://tldr.tech/devops/2026-09-14"
---

# Kubernetes v1.37: Native Histograms Graduates to Beta

Source: [Kubernetes v1.37: Native Histograms Graduates to Beta](https://kubernetes.io/blog/2026/09/11/kubernetes-v1-37-native-histograms-beta)

## Attributed article summary

The Kubernetes announcement describes native histogram support reaching beta and becoming enabled by default in v1.37. Exponential buckets adapt to observed ranges, avoiding the need to choose all classic histogram boundaries ahead of time.

Native histograms represent bucket information inside a structured series instead of one separate series per classic bucket. The source describes bounded bucket growth and shared implementation in component-base metrics, covering control-plane and node components.

Compatibility is handled through dual exposition: classic buckets remain available while native spans are included for compatible collectors. Existing text-scraped dashboards therefore need not migrate immediately. Consuming native data still requires the appropriate collector and exposition support; merely enabling production does not establish an end-to-end migration.

HoneyDrunk relevance: evaluate native histogram ingestion for Kubernetes observability, checking collector compatibility, queries, alert behavior, cardinality, and storage on actual workloads. The article's reduction estimates describe expected benefits, not measured savings for HoneyDrunk.
