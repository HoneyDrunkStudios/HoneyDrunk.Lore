---
source: "https://www.docker.com/blog/docker-sandbox-kit-spec-cncf"
title: "Docker and CNCF partner on an open spec for agent permissions"
author: "Eli Aleyner; Srini Sekaran"
date_published: "2026-09-24"
date_clipped: "2026-09-28"
category: "DevOps & CI/CD"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Docker describes an open specification that packages an agent, its tools, and requested access in an ordinary OCI image. Access requests cover resources such as network hosts, credentials, and mounted volumes. Image pinning therefore binds the software and its declared requests to the same artifact.

Existing registry, signing, and scanning workflows can handle the image. Reviewers can examine permission changes alongside software updates. Docker identifies Sandboxes as the first enforcing runtime and describes bringing the specification to CNCF.

HoneyDrunk application: explore a reviewable permission manifest attached to the deployed agent artifact. Test enforcement at the runtime boundary rather than treating the declaration as authorization by itself.

This is an early specification and vendor announcement. It does not establish universal runtime compatibility or independent proof of enforcement. Inspect the specification and validate the chosen runtime before adopting it.

Source: [Original article](https://www.docker.com/blog/docker-sandbox-kit-spec-cncf).

Capture note: Original attributed summary after fetching readable written content; not a full-text reproduction.
