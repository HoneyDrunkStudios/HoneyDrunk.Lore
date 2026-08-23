# Agentic Retrieval and Search

## Decision-useful summary
Agentic retrieval treats search as an investigation loop instead of a single chunk lookup. The Mistral Agentic Search source argues that models answer difficult document questions better when they can search, open, navigate, read, and grep specific evidence across long or table-heavy documents before responding. For HoneyDrunk, the useful decision boundary is not "RAG or no RAG"; it is whether a task needs one-shot indexed lookup or a tool-mediated evidence trail with page, table, clause, and cross-document verification. [source: raw/2026-08-23-rss-tldr-ai-mistral-replaces-one-shot-document-retrieval-with-a-navigable-.md]

## Claims
- Mistral Agentic Search replaces one-shot document retrieval with a multi-step loop over an existing index, giving models tools to search, open documents, navigate within them, read evidence, and grep patterns. confidence: 1 vendor/product source, last-confirmed 2026-08-23. [source: raw/2026-08-23-rss-tldr-ai-mistral-replaces-one-shot-document-retrieval-with-a-navigable-.md]
- The source argues one-shot RAG fails when answers are buried in long reports, tables, footnotes, clauses, or multiple documents because the model cannot decide to inspect a different location after the initial top-k retrieval. confidence: 1 source, last-confirmed 2026-08-23. [source: raw/2026-08-23-rss-tldr-ai-mistral-replaces-one-shot-document-retrieval-with-a-navigable-.md]
- Mistral reports large accuracy gains on FinanceBench and OfficeQA Pro when moving from one-shot retrieval to agentic search with navigation, while also reporting lower token use and lower p90 latency in some configurations; treat numbers as vendor benchmark evidence until locally reproduced. confidence: 1 source, last-confirmed 2026-08-23. [source: raw/2026-08-23-rss-tldr-ai-mistral-replaces-one-shot-document-retrieval-with-a-navigable-.md]
- The source says the tooling does not require model-specific fine-tuning, so retrieval quality can improve as model reasoning/tool-use improves, while the index remains the foundation. confidence: 1 source, last-confirmed 2026-08-23. [source: raw/2026-08-23-rss-tldr-ai-mistral-replaces-one-shot-document-retrieval-with-a-navigable-.md]

## Typed entities
- product/tooling: Mistral Agentic Search
- product/tooling: Mistral Search Toolkit
- product surface: Mistral Libraries
- benchmark: FinanceBench
- benchmark: OfficeQA Pro
- tool: search
- tool: open
- tool: navigate
- tool: read
- tool: grep
- concept: one-shot RAG
- concept: navigable document retrieval
- artifact type: SEC filing
- artifact type: Treasury Bulletin

## Explicit relationships
- Agentic retrieval uses indexed search plus document-navigation tools to verify evidence before final answer generation.
- Navigable retrieval complements, but does not supersede, the underlying index, parser, chunking, embedding, and ranking layer.
- One-shot RAG contradicts complex-document question answering when required evidence is scattered across tables, pages, clauses, or multiple sources.
- Retrieval benchmark results depend-on the model, harness, tool set, corpus, scoring method, latency budget, and document parser.
- [[AI Agent Harnesses]] depends-on retrieval tooling when agents must cite or verify long-document facts.
- [[LLM Wiki and Knowledge Formats]] complements agentic retrieval by preserving source links and page-level claim provenance.

## HoneyDrunk implications
- For Lore and future HoneyDrunk knowledge tools, use simple keyword/semantic retrieval for direct lookups, but add navigable search/read/grep loops for questions that need evidence reconciliation.
- Any retrieval benchmark should report answer accuracy, citation specificity, token use, latency, failed navigation paths, and whether the model could inspect source locations rather than only retrieved chunks.
- Do not promote vendor benchmark deltas into architecture decisions until a HoneyDrunk corpus test compares current Lore search, grep/read workflows, and any Mistral-style agentic loop.

## Confidence and quality notes
- Quality posture: decision-useful for retrieval architecture. Mistral is authoritative for its product claims but not neutral benchmark evidence.
- Weak spots: FinanceBench and OfficeQA Pro numbers need independent reproduction or local task validation before procurement or routing changes.
- Privacy filter: no private enterprise documents, table values beyond source-level examples, credentials, or customer data were promoted.
