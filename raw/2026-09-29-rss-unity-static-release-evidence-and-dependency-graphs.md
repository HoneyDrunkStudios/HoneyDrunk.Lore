---
source: "https://dev.to/thunderdanoae/building-shipcheck-a-static-preflight-scanner-for-unity-projects-3b51"
title: "Building ShipCheck: a static preflight scanner for Unity projects"
author: "Daniel Delgado"
date_published: "2026-09-29"
date_clipped: "2026-09-29"
category: "Game Development / Unity"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

ShipCheck's author separates technical project health, release readiness, and confidence in the available evidence. Legacy scene formats that cannot be reliably inspected should yield an explicit evidence limitation instead of a precise-looking readiness score.

The scanner starts its shipping graph from enabled build scenes and follows serialized references, reducing noise from unused third-party demos. It also considers standard runtime-loading locations because scene references do not capture every runtime dependency. Dependency detection examines declared namespaces and installed packages rather than assuming directory names match code namespaces.

For HoneyDrunk, these are useful requirements for build-preflight tooling: report why a finding affects shipped content and where static analysis cannot prove completeness. Runtime loading and unsupported serialization remain coverage questions. The post describes the author's own tests on several projects; it supplies neither independent accuracy measurements nor evidence that a successful static scan proves a playable release.

Source: [Original article](https://dev.to/thunderdanoae/building-shipcheck-a-static-preflight-scanner-for-unity-projects-3b51).
