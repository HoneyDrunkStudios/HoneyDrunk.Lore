---
source: "https://huggingface.co/blog/funes"
title: "Give Your Coding Agents a Memory You Own"
author: "David Corvoysier"
date_published: "2026-09-03"
date_clipped: "2026-09-13"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_mode: "attributed-summary"
full_text_fetched: "true"
---

# Give Your Coding Agents a Memory You Own

Original source: [Give Your Coding Agents a Memory You Own](https://huggingface.co/blog/funes)

## Source-content summary

David Corvoysier introduces funes, which indexes existing coding-agent sessions into a local Lance dataset. Retrieval combines BM25 and vector search, ranking fusion, a cross-encoder, recency weighting, and adjacent context. Results preserve original text and identify the originating session and turn instead of converting traces directly into asserted facts.

The integration provides recall and context-opening tools, incremental indexing, and optional synchronization to a user-owned Hugging Face dataset that defaults to private. Embeddings and reranking run locally. The described publishing path redacts credentials during indexing and scans again before uploading; the linked security documentation defines its limitations.

A two-task benchmark favors recall over written handoffs on cost, but offers limited evidence for general performance. HoneyDrunk relevance: provenance-preserving retrieval and portable session history provide patterns for agent automation while keeping runtime memory conceptually separate from Lore's compiled research wiki.

Capture note: This is an attributed summary of the fetched article, not a verbatim full-text archive. The original source retains the complete examples and discussion.
