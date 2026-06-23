---
source: "https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale"
title: "Making secret scanning more trustworthy: Reducing false positives at scale (4 minute read)"
author: "TLDR InfoSec"
date_published: "Mon, 22 Jun 2026 00:00:00 GMT"
date_clipped: "2026-06-23"
category: "Security & Ethical Hacking"
source_type: "rss"
discovered_via: "https://tldr.tech/infosec/2026-06-22"
source_role: "primary-via-tldr"
---

# Making secret scanning more trustworthy: Reducing false positives at scale (4 minute read)

Source: https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale

GitHub added context-aware LLM reasoning to the verification step of its secret-scanning pipeline, working with Microsoft Security & AI's Agents Offense team and applying the approach from Agentic Secret Finder to reduce noise from AI-detected generic secrets. Rather than feeding whole files to the model, the system extracts high-signal usage context, such as whether a value flows into an API request, authentication header, database client, or cloud SDK call, which lets it separate real exposures from placeholders, test data, and random UUIDs at low latency. Evaluated against hundreds of customer-confirmed false positives, it reached a 75.76% reduction against a 65% target while leaving upstream detection logic and coverage unchanged, so defenders gain higher alert precision without retuning detection.
