---
source: "https://www.docker.com/blog/docker-sandbox-kit-spec/"
title: "From Dockerfile to Kit: the Docker Sandboxes Kit Specification"
author: "Christian Dupuis"
date_published: "2026-09-24"
date_clipped: "2026-09-24"
category: "Software Architecture"
source_type: "rss"
capture_method: "attributed-summary"
---

# From Dockerfile to Kit: the Docker Sandboxes Kit Specification

Attributed summary of the fetched article.

Docker describes Sandbox Kit Specification v3 as an OCI-image contract containing workload content and requested capabilities. Pinning an image digest binds declarations and content together. Workloads and mixins compose through declared dependencies; missing requirements and conflicting providers fail resolution rather than silently changing behavior.

Capability declarations request authority rather than granting it. Enforcement requires a conforming runtime; ordinary image execution does not make annotations a security boundary. Proxy-managed credentials and network policies are examples of that runtime contract. An update gate can compare normalized grants and require review when authority expands, including removal of a deny rule.

HoneyDrunk application: treat agent environment updates as both software and permission changes, with versioned contracts and explicit runtime conformance. The article metadata credits Christian Dupuis while its RSS entry credits Jin Kim; this capture preserves that attribution discrepancy. Source confidence: vendor specification explanation, not a conformance test.

Source: [Original article](https://www.docker.com/blog/docker-sandbox-kit-spec/).
