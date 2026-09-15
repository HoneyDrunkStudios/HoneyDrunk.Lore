---
source: "https://devblogs.microsoft.com/foundry/building-agents-that-act-on-your-behalf-with-toolboxes-in-foundry/"
title: "Building Agents that Act on Your Behalf with Toolboxes in Foundry"
author: "Linda Li, Maria Naggaga"
date_published: "2026-07-22"
date_clipped: "2026-09-15"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
extraction_status: "full written page fetched; readable body reviewed"
---

# Building Agents that Act on Your Behalf with Toolboxes in Foundry

Source: [Building Agents that Act on Your Behalf with Toolboxes in Foundry](https://devblogs.microsoft.com/foundry/building-agents-that-act-on-your-behalf-with-toolboxes-in-foundry/)

## Attributed content summary

Microsoft's Toolboxes example separates tool authentication configuration from agent implementation. Connections define how tools authenticate; a versioned toolbox combines those tools; an agent consumes the toolbox through an MCP endpoint.

For user delegation, the post describes OAuth2 connections that let private MCP services and Work IQ act with the signed-in user's permissions. Foundry is described as handling per-user token isolation, refresh, and consent, avoiding a separate delegation implementation for every agent harness.

The authentication choices distinguish end-user OAuth, an agent identity, the project's managed identity, stored keys, and anonymous access. Those identities serve different authorization needs and should not be treated as interchangeable. The example also describes boundary-level input/output screening and optional API Management gateways for additional controls.

The reusable architecture is centralized, versioned tool access with explicit identity selection. This is vendor implementation guidance, including a preview Work IQ example; screening claims do not prove prompt-injection immunity. Confirm consent, scopes, caller isolation, and current API availability in the target deployment.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
