---
source: "https://www.langchain.com/blog/langsmith-managed-deep-agents-whats-new"
title: "Managed Deep Agents v0.8: new auth, memory, and channels"
author: "Nathan Drezner; Karthic Subramanian"
date_published: "2026-09-24"
date_clipped: "2026-09-28"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
discovered_via: "https://tldr.tech/ai/2026-09-25"
---

# Source capture

LangChain's Managed Deep Agents 0.8 separates deployment-wide memory from memory associated with the authenticated caller. Access policies govern availability in individual and shared conversations. Credentials similarly belong either to the agent or to a user, allowing shared capabilities alongside services requiring personal permissions.

HTTP channels expose webhook entry points with application-defined verification, parsing, and messaging. The release also adds file transfer through its Slack integration and managed web search with traceable calls, latency, and errors.

HoneyDrunk application: treat identity, memory scope, and credential scope as one integration contract. Test group conversations and webhook identities for accidental exposure of personal context before adopting the pattern.

These are vendor-described capabilities, not verified isolation guarantees. The announcement describes beta availability; behavior and costs should be checked against current documentation before implementation.

Source: [Original article](https://www.langchain.com/blog/langsmith-managed-deep-agents-whats-new).

Capture note: Original attributed summary after fetching readable written content; not a full-text reproduction.
