---
source: "https://andrewlock.net/running-ai-agents-with-customized-templates-in-docker-sandbox"
title: "Running AI agents with customized templates using docker sandbox"
author: "Andrew Lock"
date_published: "2026-04-14"
date_clipped: "2026-09-30"
category: ".NET Ecosystem"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Andrew Lock demonstrates extending Docker sandbox templates with system dependencies and a user-level .NET SDK. Templates must be pushed to an OCI registry because the microVM sandbox does not share the host Docker image store. The article separates the supported extension of a default template from a reverse-engineered alternative base image, which carries compatibility risk. The author also reports unexplained hangs building some personal .NET projects despite successful simple builds. For HoneyDrunk, test actual restore, build, and test workloads in the chosen template before adopting it as the agent environment.

Source: [Original article](https://andrewlock.net/running-ai-agents-with-customized-templates-in-docker-sandbox).
