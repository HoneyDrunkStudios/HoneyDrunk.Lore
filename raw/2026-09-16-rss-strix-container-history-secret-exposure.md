---
source: "https://www.strix.ai/blog/baseten-harbor-github-pat-takeover"
title: "We wanted to use Baseten for inference. We ended up with admin access to Baseten GitHub repos"
author: "Alex Schapiro"
date_published: "2026-09-01"
date_clipped: "2026-09-16"
category: "Security & Ethical Hacking"
source_type: "rss"
capture_format: "attributed-summary"
discovered_via: "https://tldr.tech/dev/2026-09-16"
---

# We wanted to use Baseten for inference. We ended up with admin access to Baseten GitHub repos

Source: [We wanted to use Baseten for inference. We ended up with admin access to Baseten GitHub repos](https://www.strix.ai/blog/baseten-harbor-github-pat-takeover)

## Attributed content summary

Strix reports finding a live, broadly privileged GitHub token in the metadata of an anonymously downloadable container image. The credential appeared in build history after expansion into a build command; removing a secret-bearing file would not remove that separate metadata copy.

The authors say the token dated from a 2023 build and still granted repository administration and push access in July 2026. Their report states that Baseten restricted registry access and rotated the token after disclosure. These are the researchers' reported findings and remediation timeline, not an independent assessment.

The defensive practices are concrete: audit anonymous registry access and old tags, inspect both layers and build configuration/history, use secret mounts without persisting consumed credentials, and give build identities narrow permissions and expiry. Revoke exposed credentials because rebuilding an image cannot invalidate copies already obtained.

This is useful supply-chain evidence for containerized CI. The capture omits exploit payloads, credential material, and unnecessary infrastructure identifiers.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
