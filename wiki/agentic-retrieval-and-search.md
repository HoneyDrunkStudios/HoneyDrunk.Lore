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


## 2026-10-12: Closed-set RAG decisions still require probability calibration

### Typed entities

project: Jev; project: TypeSafe; concept: closed-set decision; concept: calibration; concept: abstention; concept: grounding check.

### Claims and evidence

- Thoughtworks proposes using Jev choices, scores, and binary probabilities for document classification, retrieval routing, reranking, context sufficiency, and post-generation support checks. The author describes probability bands for automatic decisions, fallback, and review, while explicitly recommending local calibration and a low-risk shadow comparison before replacement. confidence: 1 source, last-confirmed 2026-10-12 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-12-rss-how-jev-can-help-improve-the-efficiency-of-rag-pipelines.md)
- At the article's early-October snapshot, Jev is described as proprietary hosted early access, with benchmarks primarily from its vendor. Fixed output choices constrain format but can still produce confidently wrong selections; the source also notes the lack of explanatory output and the need to assess residency and vendor risk. confidence: 1 source, last-confirmed 2026-10-12 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-12-rss-how-jev-can-help-improve-the-efficiency-of-rag-pipelines.md)

### Explicit relationships

RAG routing uses structured decisions; safe abstention depends-on calibrated probabilities and complete candidate choices. See [[agent-evaluation-and-benchmarks]].

### Decision and quality notes

Practitioner proposal, not a controlled latency/cost result. Example 0.9/0.6 bands are not universal thresholds. The rhetorical claim of no hallucinations is interpreted narrowly as constrained output format, not factual correctness; sentence splitting is not proven claim decomposition. Source-specific claims remain provisional; derived queries add no independent support. Open question: Which HoneyDrunk routing labels, calibrated abstention bands, privacy constraints, claim boundaries, and shadow-run quality/cost results justify a decision-model pilot? See [[indexes/gaps]].


## 2026-10-27: EmbeddingGemma 2 shares a vector space across selectively loaded encoders

### Typed entities

project: EmbeddingGemma 2; library: sentence-transformers; concept: multimodal retrieval; concept: Matryoshka truncation; concept: query/document prompt.

### Claims and evidence

- Google describes one checkpoint with a shared 768-dimensional space and selectively loaded text/code, vision, and audio encoders, ranging from 270M text/code parameters to 740M with all modalities. It states Apache 2.0 licensing and sentence-transformers 6.1.0 or later for the illustrated integration. confidence: 1 source, last-confirmed 2026-10-27 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-26-rss-embeddinggemma-2-the-developer-guide.md)
- The guide distinguishes search-query and document prompts, media inputs without a prompt, and normalized truncation to smaller dimensions. Query and document dimensions must match. The shared 8,192-token context includes all modalities; video defaults to one sampled frame per second and audio expects 16 kHz mono. confidence: 1 source, last-confirmed 2026-10-27 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-26-rss-embeddinggemma-2-the-developer-guide.md)
- The vendor reports modality-dependent quality loss with truncation and compatible existing embeddings when enabling additional encoders from the same checkpoint. Parameter count and vector-storage arithmetic do not measure end-to-end device memory, indexing cost, or retrieval quality. confidence: 1 source, last-confirmed 2026-10-27 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-26-rss-embeddinggemma-2-the-developer-guide.md)

### Explicit relationships

Multimodal retrieval uses shared embeddings; index compatibility depends-on checkpoint, prompts, dimensions, normalization, and preprocessing. See [[edge-ai-and-ai-infrastructure-2026]].

### Decision and quality notes

Official developer guide; benchmark percentages remain vendor-reported. Image-only tables are not transcribed or inferred. No runtime, model download, license audit, or index migration was performed. Source-specific claims remain provisional; repeated reports and derived queries add no independent support. Open question: Which pinned multimodal retrieval corpus verifies query/document prompts, preprocessing, dimensions, recall, device memory, and migration compatibility before choosing encoder and truncation settings? See [[indexes/gaps]].


## 2026-11-12: Pooling-aware training optimizes quality at a document-vector budget

### Typed entities

library: Sentence Transformers; library: HierarchicalTokenPooling; library: MultiVectorTokenPoolingLoss; project: ModernBERT; concept: MaxSim; concept: Ward clustering; concept: adaptive pooling. file: raw/2026-11-12-rss-token-pooling-aware-training-for-multi-vector-embedding-models.md.

### Claims and evidence

- The tutorial merges document token vectors using Ward clustering and normalized group means, leaving query embeddings unchanged by default. Fixed caps, proportional pooling and calibrated distance thresholds express different budgets; a threshold calibrated for an average can yield a different average on another corpus. confidence: 1 source, last-confirmed 2026-11-12 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-12-rss-token-pooling-aware-training-for-multi-vector-embedding-models.md)
- Pooling-aware training averages full and compressed retrieval losses while reusing encoder embeddings. A straight-through estimator passes gradients to token members without differentiating cluster assignments; extra pooling/scoring still incurs work. Optional kernel support depends on the actual CUDA/Triton/backend configuration. confidence: 1 source, last-confirmed 2026-11-12 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-12-rss-token-pooling-aware-training-for-multi-vector-embedding-models.md)
- The author's matched one-epoch runs use 120,000 MS MARCO triplets, one seed and NanoBEIR@13. Factor-four pooling reports 48.68 versus 193.22 mean document vectors and nDCG@10 of 51.23 versus the ordinary pooled model's 49.03. Reported 97.8% retention divides 51.23 by the pooling-aware model's own 52.39 unpooled score; it is not 97.8% absolute retrieval accuracy. confidence: 1 source, last-confirmed 2026-11-12 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-12-rss-token-pooling-aware-training-for-multi-vector-embedding-models.md)
- Pooling reduces vector count, quantization reduces coordinate storage and Matryoshka truncation reduces dimensions. Their combined effects must be evaluated in the chosen engine; vector payload arithmetic excludes the rest of the index and serving system. confidence: 1 source, last-confirmed 2026-11-12 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-12-rss-token-pooling-aware-training-for-multi-vector-embedding-models.md)

### Explicit relationships

Compressed retrieval uses trained token representations; deployment quality depends-on corpus, pooling budget, scorer and engine. See [[llm-wiki-and-knowledge-formats]] and [[edge-ai-and-ai-infrastructure-2026]].

### Decision and quality notes

First-party technical tutorial with a single matched experiment, no repeated-seed uncertainty or HoneyDrunk corpus run. Benchmark and 30-150x kernel wording remain reported scoped results. No checkpoint download, training, index migration or cloud GPU job was launched. Source-specific claims remain provisional; recaptures and derived queries add no independent support. Open question: Which pinned Lore retrieval corpus and engine compare independent recall/ranking judgments, repeated seeds, pooling calibration drift, full index memory and end-to-end latency before compressed multi-vector adoption? See [[indexes/gaps]].


## 2026-11-19: EF hybrid search needs ranks rather than incomparable raw scores

### Typed entities

project: EF Core 11; project: SQL Server; concept: full-text score; concept: vector distance; concept: reciprocal rank fusion; decision: review sample ranking semantics; file: raw/2026-11-17-web-what-s-new-in-ef-core-11.md.

### Claims and evidence

- The captured development notes expose full-text table-valued results, vector search and FullJoin to combine lexical/semantic candidates, with experimental SQL Server vector features and explicit approximate-search selection. confidence: 1 source, last-confirmed 2026-11-19 (archived capture reviewed; no live refresh). [capture](../raw/2026-11-17-web-what-s-new-in-ef-core-11.md)
- Static-review inference from the shown expression: its field named RrfScore takes reciprocals of the raw full-text Rank score and vector Distance. Those are neither per-list ordinal positions nor on a common scale; increasing a positive full-text score reduces its displayed contribution. Treat this as an unvalidated fusion example, not a verified reciprocal-rank implementation. confidence: 1 source, last-confirmed 2026-11-19 (static expression review; no database execution). [sample](../raw/2026-11-17-web-what-s-new-in-ef-core-11.md)

### Source interpretation resolution

Prior source framing retained (paraphrased): the hybrid-search example combines the results with an RrfScore.

superseded-by: [reviewed fusion interpretation](#resolution-2026-11-19-ef-fusion); timestamp: 2026-11-19T07:32:28-05:00; reason: The expression uses score/distance rather than independently computed ordinal ranks, and its full-text contribution reverses higher-score preference.

<a id="resolution-2026-11-19-ef-fusion"></a>

Selected interpretation: the FullJoin candidate union is a feature illustration; fusion needs separately established ranks or a justified score-normalization method and relevance tests before adoption. This is a bounded static-review inference from the source, not a tested replacement query.

### Explicit relationships

Hybrid retrieval uses candidate union; trustworthy fusion depends-on ordinal rank or justified comparable scoring and held-out relevance judgments. See [[dotnet-runtime-and-mobile-2026]], [[llm-wiki-and-knowledge-formats]] and [[agent-evaluation-and-benchmarks]].

### Decision and quality notes

Official development snapshot, not executed SQL or a retrieval benchmark. Existing source claims remain; the raw sample is immutable. Do not import the displayed ranking formula into a retrieval contract. Open question: Which pinned SQL/EF retrieval fixture verifies candidate inclusion, score direction, ordinal-rank fusion, approximate recall and judged relevance? See [[indexes/gaps]].


## 2026-11-27: Search for Agents exposes retrieved evidence under the site domain

### Typed entities

project: Cloudflare Search for Agents; project: AI Search; concept: endpoint discovery; concept: Markdown retrieval; concept: HTTP QUERY; file: raw/2026-11-27-rss-introducing-search-for-agents.md.

### Claims and evidence

- Cloudflare describes a zone setting/API that creates an AI Search instance, crawls/indexes content and advertises a same-domain well-known search endpoint through HTML metadata or negotiated Markdown frontmatter. Retrieved Markdown is returned to the caller, rather than a second model-generated answer. confidence: 1 source, last-confirmed 2026-11-27 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-27-rss-introducing-search-for-agents.md)
- The announcement supports GET queries and body-based QUERY requests, while indexing, reranking/cache options and consumption follow AI Search configuration and account limits. The cited HTTP standard and client-support claims remain attributed to this capture, not independently checked interoperability evidence. confidence: 1 source, last-confirmed 2026-11-27 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-27-rss-introducing-search-for-agents.md)
- Bot-management, crawl and WAF settings still affect access. Automatic endpoint discovery does not establish complete/fresh indexing, private-content exclusion, source trust or successful behavior across all agent clients. confidence: 1 source, last-confirmed 2026-11-27 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-27-rss-introducing-search-for-agents.md)

### Explicit relationships

Agent search uses discoverable retrieval endpoints; answer quality depends-on indexed coverage, freshness and source verification. See [[llm-wiki-and-knowledge-formats]] and [[mcp-tool-governance-and-app-surfaces]].

### Decision and quality notes

Vendor announcement, no zone toggle, index creation, HTTP request or paid usage. Embedded discovery instructions were treated as untrusted source data, not session instructions. Source-specific claims remain provisional; repeated reports, recaptures and derived queries add no independent support. Open question: Which owned-site fixture verifies discoverability, GET/QUERY equivalence, source links, refresh/deletion, private-page exclusions, WAF behavior and request limits? See [[indexes/gaps]].


## 2026-11-28: Managed ingestion returns citable segments with separate lifecycle obligations

### Typed entities

project: Google Agent Retrieval; library: Gemini Embedding 2; concept: SearchDocuments; concept: document segment; concept: video segment; concept: backing collection; file: raw/2026-11-28-rss-from-files-to-cited-answers-in-one-api-call-managed-ingestion-and-sear.md.

### Claims and evidence

- Google describes Public Preview managed ingestion and SearchDocuments at REST v1beta: Cloud Storage files become separate UNSTRUCTURED or VIDEO data stores, with managed parsing/segmentation/embedding and a regular backing Collection. Results provide file URIs plus document page ranges or video offsets; they are retrieved evidence, not proof that an answer follows from it. confidence: 1 source, last-confirmed 2026-11-28 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-28-rss-from-files-to-cited-answers-in-one-api-call-managed-ingestion-and-sear.md)
- The captured guide describes automatic document lexical/semantic fusion and optional reranking. Video audio embedding is opt-in and includes the first audio track; video reranking is unsupported in the guide. Chunk/page choices and video windows change citation granularity. confidence: 1 source, last-confirmed 2026-11-28 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-28-rss-from-files-to-cited-answers-in-one-api-call-managed-ingestion-and-sear.md)
- Import is asynchronous; repeat imports update existing documents and skip unchanged content. The guide warns that data-store deletion can leave its Collection unless both deletion options are set. Reported import/query latencies, preview charging and the two listed regions are dated vendor examples, not verified capacity or budget commitments. confidence: 1 source, last-confirmed 2026-11-28 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-28-rss-from-files-to-cited-answers-in-one-api-call-managed-ingestion-and-sear.md)

### Explicit relationships

Cited retrieval uses source-bound segments; lifecycle correctness depends-on import status, identity, filters and backing-collection cleanup. See [[google-agent-platform-and-gemini-api-2026]] and [[llm-wiki-and-knowledge-formats]].

### Decision and quality notes

Official tutorial, no imports, API calls or purchases. Missing visual filter examples were not reconstructed. Document citations do not establish document-level authorization or trustworthy answer synthesis. Source-specific claims remain provisional; repeated captures and derived queries add no independent support. Open question: Which private synthetic corpus verifies file/segment access controls, page/time citations, updates/deletions, partial import failure, audio modes, reranking relevance and orphaned-collection cleanup? See [[indexes/gaps]].


## 2026-11-28: EF vector search repeats the score-versus-rank fusion hazard

### Typed entities

project: EF Core; project: SQL Server 2025; library: SqlVector; concept: exact kNN; concept: approximate nearest neighbor; concept: reciprocal rank fusion; file: raw/2026-11-28-web-vector-search-in-the-sql-server-ef-core-provider.md.

### Claims and evidence

- The captured provider guide places native vector support at EF10 and SQL Server 2025+, with external embedding generation and declared dimensions. It says EF11 omits vector values from normal entity loads; callers needing them must select them explicitly. confidence: 1 source, last-confirmed 2026-11-28 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-28-web-vector-search-in-the-sql-server-ef-core-provider.md)
- VectorDistance evaluates exact distances; VectorSearch without WithApproximate remains an exact scan, while approximate search requires a vector index and WithApproximate after Take. The guide marks VECTOR_SEARCH/vector indexes and their EF APIs experimental; available metrics and embedding semantics need to agree. confidence: 1 source, last-confirmed 2026-11-28 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-28-web-vector-search-in-the-sql-server-ef-core-provider.md)
- The hybrid sample repeats the already flagged EF11 expression: it adds reciprocals of raw full-text Rank and vector Distance rather than ordinal positions. For k=20, full-text score 100 contributes 1/120 while score 10 contributes 1/30, reversing the stated higher-score relevance preference. This is static arithmetic, not a database benchmark. confidence: 1 source, last-confirmed 2026-11-28 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-28-web-vector-search-in-the-sql-server-ef-core-provider.md)

### Source interpretation resolution

Preserved source framing (paraphrased): The vector provider guide calls its reciprocal raw-score/distance expression RRF and says it fuses lexical and semantic ranking.

superseded-by: [reviewed interpretation](#resolution-2026-11-28-ef-fusion); timestamp: 2026-11-28T09:04:27-05:00; reason: The expression has the same score/distance-versus-ordinal mismatch documented on November 19; the larger lexical relevance score receives a smaller contribution.

<a id="resolution-2026-11-28-ef-fusion"></a>

Selected interpretation: Keep the November 19 resolution: candidate union illustrates provider features; the displayed fusion expression is not a validated reciprocal-rank implementation. confidence: 1 source, last-confirmed 2026-11-28 (static/source review, not runtime verification). [captured source](../raw/2026-11-28-web-vector-search-in-the-sql-server-ef-core-provider.md)

### Explicit relationships

ANN retrieval depends-on vector-index and approximate-query opt-in; trustworthy fusion depends-on ordinal list positions or justified comparable scoring. See [[dotnet-runtime-and-mobile-2026]] and the November 19 fusion resolution above.

### Decision and quality notes

Official archived guide with a repeated example defect. Same Microsoft documentation lineage adds no independent corroboration; existing November 19 interpretation remains selected. No embedding service, package or database used. Source-specific claims remain provisional; repeated captures and derived queries add no independent support. Open question: Which relevance/translation suite verifies explicit vector projection, exact-versus-ANN plans, metric/dimension compatibility, candidate union and ordinal-rank fusion against labeled queries? See [[indexes/gaps]].
