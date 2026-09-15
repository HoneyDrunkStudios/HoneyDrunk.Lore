---
source: "https://isc.sans.edu/diary/33332"
title: "The Self-Expanding Stolen Inference Supply Chain: An AI Agent Harvesting and Re-Serving LLM Access"
author: "SANS Internet Storm Center"
date_published: "2026-09-11"
date_clipped: "2026-09-14"
category: "Security & Ethical Hacking"
source_type: "rss"
capture_mode: "attributed-summary"
content_note: "Substantive summary of the fetched readable article; not a verbatim full-text archive."
discovered_via: "https://tldr.tech/infosec/2026-09-14"
---

# The Self-Expanding Stolen Inference Supply Chain: An AI Agent Harvesting and Re-Serving LLM Access

Source: [The Self-Expanding Stolen Inference Supply Chain: An AI Agent Harvesting and Re-Serving LLM Access](https://isc.sans.edu/diary/33332)

## Attributed article summary

A SANS Internet Storm Center honeypot report describes a human-directed coding agent acquiring poorly protected LLM gateway access, testing available inference, and consolidating working upstreams behind another gateway. The observed loop partially replenished the inference capacity used by the operation; the evidence did not establish a fully autonomous or self-replicating system.

The endpoint also received extensive agent context, illustrating how model requests can disclose project instructions, working history, command output, and credentials to an inference provider. Advertised model names did not verify the identity of the actual backend.

Defensive priorities include server-side authorization, protected account-management endpoints, removal of default credentials, controlled signup credits, bounded billing limits, and monitoring for automated abuse. Inference providers belong inside the agent's data-trust assessment, including cheap or free proxies.

HoneyDrunk relevance: audit gateway access and spending controls, minimize context sent upstream, and treat untrusted model endpoints as potential recipients of operational state. Sensitive indicators, captured credentials, and offensive instructions are omitted.
