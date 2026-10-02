---
source: "https://blog.cloudflare.com/cloudflare-cf-cli-launch"
title: "Introducing cf: the agentic CLI for the entire Cloudflare API"
author: "unknown"
date_published: "2026-09-30"
date_clipped: "2026-09-30"
category: "DevOps & CI/CD"
source_type: "rss"
capture_format: "attributed-summary"
---

# Source capture

Capture: attributed summary of the fetched written article; not a full-text reproduction.

Cloudflare introduces the open-beta cf CLI, generated from API schemas to cover substantially more operations than Wrangler. JSON is the default output, with command discovery intended for agents. Typed cloudflare.config.ts configuration centralizes bindings and triggers, and Vite becomes the default Workers development path. Migration can retain delegation to Wrangler for projects that need existing build behavior. For HoneyDrunk, the portable pattern is schema-derived automation interfaces plus typed configuration, rather than hand-maintained command surfaces. Evaluate actual permissions, migration behavior, and target-runtime tests before relying on a beta CLI.

Source: [Original article](https://blog.cloudflare.com/cloudflare-cf-cli-launch).
