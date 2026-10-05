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


## 2026-09-22: Multi-vector retrieval trades token detail against storage and truncation

### Typed entities

person: Tom Aarsen; library: Sentence Transformers; concept: late interaction; concept: token embeddings; concept: held-out retrieval evaluation; concept: document truncation.

### Claims and evidence

- Aarsen's training recipe uses domain question/passage pairs, in-batch negatives with gradient caching, query/document prompts, and held-out evaluation with deduplicated distractors. Token-level representations retain detailed matches but enlarge the index; document-length limits can discard evidence before scoring. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-huggingface-multivector-domain-retrieval.md)
- The MIRIAD experiment reports NDCG@10 of 0.9139 after fine-tuning versus 0.8520 zero-shot, and approximately 45 GB of raw token embeddings. A 3.37 GB quantized configuration scores 0.8984. Generated questions favor lexical overlap, limiting generalization beyond this constructed benchmark. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-huggingface-multivector-domain-retrieval.md)

### Explicit relationships

Late-interaction scoring uses token representations; retrieval quality depends-on corpus, truncation, prompts, and evaluation design. Index compression trades storage against measured retrieval quality. See [[llm-wiki-and-knowledge-formats]].

### Decision and quality notes

One author benchmark, not universal superiority. Evaluate held-out Lore questions, evidence truncation, and index cost together if retrieval requirements outgrow flat-file search. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent support. Open question: On held-out Lore questions, how do single-vector and multi-vector retrieval compare after controlling document truncation, lexical overlap, distractors, and compression cost? See [[indexes/gaps]].


## 2026-10-03: Graph retrieval adds relationships but requires canonicalization and validation

### Typed entities

project: n8n; concept: vector RAG; concept: knowledge graph; concept: entity resolution; concept: HybridRAG.

### Claims and evidence

n8n presents vector retrieval for a few semantically related passages and graph traversal for explicit multi-hop relationships, with hybrid orchestration when both are needed. LLM-extracted triples require entity resolution and validation; schema-first construction improves consistency while schema-free discovery increases validation needs. Graph maintenance costs can exceed standard vector retrieval. confidence: 1 source, last-confirmed 2026-10-03 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-02-rss-when-to-use-an-llm-knowledge-graph-or-a-vector-rag.md)

### Explicit relationships

Multi-hop retrieval uses relationships; graph quality depends-on validated entities and sources. See [[llm-wiki-and-knowledge-formats]].

### Decision and quality notes

Vendor design guidance. Graph paths improve inspectability but do not guarantee truthful answers; retrieval, extraction, and canonicalization can each fail. This does not authorize heavier Lore infrastructure below its scaling threshold. Source-specific claims remain provisional; related reports and derived queries add no independent confirmation. Open question: Which HoneyDrunk held-out questions need explicit relationship traversal, and what extraction/canonicalization errors and maintenance costs would justify it? See [[indexes/gaps]].


## 2026-10-05: Code retrieval trades binary storage against relevance calibration

### Typed entities

project: Air Context; project: JetBrains; concept: syntax-aware chunking; concept: binary quantization; concept: Hamming distance.

### Claims and evidence

- JetBrains describes syntax-aware chunking for nine languages with line-based fallback elsewhere, declaration/comment attachment, normalized chunks, abbreviated file paths, and source-file judges plus end-to-end retrieval evaluation. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-building-a-rag-pipeline-for-semantic-code-search-a-developer-diary-and.md)
- Its reported pipeline retains 4,096 dimensions as sign bits and compares Hamming distance, reducing vector payload size 32-fold against float32 while sacrificing recall. Narrower similarity-score ranges limit absolute relevance thresholds, so it retains float16 for that use case. It reports storing coordinates and vectors rather than code content and reconstructing snippets from the local checkout; embeddings run on vendor-operated infrastructure. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-building-a-rag-pipeline-for-semantic-code-search-a-developer-diary-and.md)

### Explicit relationships

Code retrieval uses structure-aware chunks; coordinate reconstruction depends-on checkout consistency; threshold calibration depends-on vector representation. See [[cloud-vector-storage-security]].

### Decision and quality notes

Vendor public-preview design diary, not an independent performance or privacy audit. Local reconstruction does not mean code never reaches vendor embedding infrastructure; vectors and metadata remain sensitive. Embedded directory scope is relevance context, not an authorization filter. Source-specific claims remain provisional; related reports and derived queries add no independent confirmation. Open question: Which HoneyDrunk retrieval tests cover chunk boundaries, binary ranking/abstention, checkout-offset freshness, hard scope filters, and vector/metadata privacy? See [[indexes/gaps]].


## 2026-10-05: HNSW tuning needs measured recall and resource limits

### Typed entities

concept: HNSW; concept: approximate nearest neighbors; concept: Recall@k; concept: quantization.

### Claims and evidence

- The newsletter explains hierarchical graph traversal and the tradeoffs of neighbor count, construction search breadth, and query search breadth. More exploration can improve recall while increasing work; graph links and vector payloads consume memory, and compression changes the accuracy/storage tradeoff. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-how-vector-database-search-billions-of-vectors-in-milliseconds.md)

### Explicit relationships

Approximate retrieval depends-on graph construction, embedding metric, and query exploration; recall evaluation uses exact-neighbor reference results.

### Decision and quality notes

Secondary educational explanation. Its latency/recall numbers are illustrative, and the headline does not establish a billion-vector benchmark. Quantizing float payloads does not imply the same percentage reduction for total index memory. Embedding dimensions are not individually interpretable semantic facts. Source-specific claims remain provisional; related reports and derived queries add no independent confirmation. Open question: Which HoneyDrunk corpus, exact-neighbor reference, mutation rate, total-memory budget, and recall/latency targets justify ANN tuning? See [[indexes/gaps]].


## 2026-10-05: Graph paths need operational provenance and hard boundaries

### Typed entities

concept: Graph RAG; concept: entity resolution; concept: effective date; concept: operational provenance; concept: bounded traversal.

### Claims and evidence

- The sponsored article distinguishes relationship-aware retrieval over operational records from Microsoft GraphRAG extraction/community summarization. Vector ranking finds candidate evidence, while typed sourced relationships establish which service, version, customer, and policy actually connect. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-use-graph-rag-when-relationships-are-part-of-the-evidence.md)
- It recommends resolving ambiguous entities explicitly, enforcing tenant/effective-date/edge/hop constraints before model consumption, citing path sources and policy text, and surfacing missing or contradictory links. Graphs near relational source records can reduce copying and reconciliation, but need owners and update paths. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-use-graph-rag-when-relationships-are-part-of-the-evidence.md)

### Explicit relationships

Relationship-aware answering depends-on entity resolution and current sourced edges; vector relevance does not establish authorization. See [[llm-wiki-and-knowledge-formats]].

### Decision and quality notes

Oracle-sponsored design guidance, not a HoneyDrunk database selection or benchmark. Operationally sourced edges and model-extracted triples have different validation needs. No new Lore graph infrastructure is authorized or required by this capture. Source-specific claims remain provisional; related reports and derived queries add no independent confirmation. Open question: Which HoneyDrunk decision needs verified multi-hop paths, and do tests reject ambiguous identities, expired policies, missing edges, and cross-tenant traversal? See [[indexes/gaps]].
