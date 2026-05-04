# AGENTS.md — HoneyDrunk.Lore

This file is the schema and operating manual for the Lore wiki. Any OpenClaw/Honeyclaw session pointed at this repo follows the rules below.

## Identity

**HoneyDrunk.Lore is** the compiled research knowledge surface for HoneyDrunk Studios — a flat-file wiki where humans drop raw sources, LLMs compile and maintain structured pages, and Obsidian provides graph visualization.

**HoneyDrunk.Lore is NOT:**
- Agent memory (that lives in agent runtime state)
- Architecture governance (that lives in HoneyDrunk.Architecture)
- Code documentation (that lives next to the code in each Node repo)

## Directory contract

- `raw/` — immutable source documents (articles, papers, repo dumps, notes, clips). **Never edit.** Only add. This is the source of truth for inputs.
- `wiki/` — LLM-maintained structured markdown: articles, concept pages, entity pages. Plain markdown, Obsidian-compatible (`[[wikilinks]]` allowed).
- `wiki/indexes/` — LLM-maintained auto-indexes: `sources.md`, `topics.md`, `gaps.md`. Rebuilt by Compile.
- `output/` — query results filed here as dated markdown. These feed back into `wiki/` on the next Compile pass via Crystallization.
- `tools/` — shell scripts for search and maintenance. Thin wrappers, no business logic.

## Operations

The wiki has four operations. Every action you take in this repo is one of these.

### Ingest

Triggered when a new file appears in `raw/`.

1. Read the source fully.
2. Identify key concepts, **typed entities** (`person`, `project`, `library`, `concept`, `file`, `decision`), and claims.
3. For each concept: check if a `wiki/` page exists; create or update it. Attach a confidence note to each non-trivial claim:
   `confidence: N sources, last-confirmed YYYY-MM-DD`
4. When new info contradicts an existing claim: **supersede, do not overwrite.** Preserve the prior claim with a `superseded-by:` link and timestamp. The wiki keeps its history.
5. Add an entry to `wiki/indexes/sources.md` for the ingested source.
6. Update topic backlinks in `wiki/indexes/topics.md`.
7. Never delete existing wiki content during Ingest — always extend and reconcile.

### Compile

Triggered on demand or on a schedule.

1. Scan `raw/` for sources not yet reflected in `wiki/`.
2. Run Ingest for each unprocessed source.
3. **Crystallize from `output/`**: scan `output/` for `query-*.md` results not yet reflected in `wiki/`. For each one that is well-structured, well-cited, and surfaces durable new facts (not just an in-the-moment answer), treat it as an exploration source — distill those facts into first-class `wiki/` content. Strengthen or challenge existing claims as warranted. Skip outputs that are conversational, redundant, or low-quality.
4. Identify concept pages that reference the same entity — merge into a canonical article.
5. **Consolidate**: claims reinforced across 3+ sources get stronger confidence; unreinforced claims get demoted.
6. **Resolve contradictions** when detected: pick the more-likely claim based on (a) source recency, (b) source authority, (c) supporting count. Mark the loser as superseded with reasoning. Do not just flag — resolve.
7. Rebuild `wiki/indexes/` from current wiki state.

### Query

Triggered when asked a question.

1. Search `wiki/` (keyword + semantic scan; `tools/` may have helpers).
2. Synthesize an answer from wiki content. Cite source pages and report their confidence.
3. Identify gaps (questions the wiki cannot answer) — append them to `wiki/indexes/gaps.md`.
4. File the query result in `output/` as `query-YYYY-MM-DD-<slug>.md`.
5. **Crystallize**: if the query output is well-structured, well-cited, and surfaces new facts, distill it into first-class `wiki/` content on the next Compile. The exploration becomes a source. New facts strengthen or challenge existing claims.

### Lint

Triggered on demand.

1. **Orphan pages** — wiki pages with no backlinks or source attribution. Auto-link where a canonical concept page exists; flag the rest.
2. **Contradictions** — claims across wiki pages that conflict. Attempt auto-resolution per the Compile rules above; flag only what cannot be resolved.
3. **Stale sources** — `raw/` files processed more than 90 days ago. Flag for re-ingest.
4. **Retention decay** — claims not accessed or reinforced in 6+ months get their confidence decayed. Architecture decisions decay slowly; transient bugs decay fast. Decayed claims are not deleted, only deprioritized.
5. **Self-healing** — auto-fix what is safe: repair broken cross-references, link orphans where a canonical page exists, mark stale claims. Log every auto-fix in the lint report.
6. **Gaps** — entries in `wiki/indexes/gaps.md` that have no corresponding wiki page. Flag for sourcing.
7. Output a lint report at `output/lint-YYYY-MM-DD.md`.

## Schema co-evolution

This AGENTS.md **is** the product. It encodes what entities exist in the HoneyDrunk domain, how to ingest different source kinds, when to create vs. update a page, quality standards, and contradiction-handling rules. Update it as the wiki grows. Rough on day one is expected — every Lint pass is a chance to tighten it.

## Extensions (v2 — when the wiki outgrows v1)

The v1 build is flat files plus the four operations above. Reach for the following only when the wiki passes ~100 pages or the minimal layer stops scaling:

- **Knowledge graph layer** — typed-entity extraction into `wiki/graph/entities.json` and `wiki/graph/edges.json`, with typed relationships (`uses`, `depends-on`, `caused`, `fixed`, `supersedes`). Enables traversal queries that keyword search misses.
- **Hybrid search** — BM25 + vector embeddings + graph traversal, fused with reciprocal rank fusion. `wiki/indexes/` stays as the human-readable catalog surface.
- **Consolidation tiers** — working memory (recent observations) → episodic (session digests) → semantic (cross-session facts) → procedural (workflows). Each tier is more compressed, more confident, longer-lived.
- **Event hooks** — auto-ingest on new `raw/` file, context injection on session start, crystallize on session end, contradiction check on every write, scheduled consolidation and retention decay.
- **Quality scoring** — every LLM-generated page gets a score (structure, citations, consistency); below threshold triggers a rewrite.
- **Audit trail** — every wiki mutation logged with timestamp, operator, and diff. Enables bulk reversible operations.
- **Privacy filter on ingest** — strip secrets and PII before anything hits `wiki/`.

Reference: LLM Wiki v2 — https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2

## Conversion note (for future agents)

The flat-file implementation is intentional and temporary. When `HoneyDrunk.Knowledge` and `HoneyDrunk.Agents` exist:

- Ingest delegates to `IDocumentIngester`
- Retrieval delegates to `IRetrievalPipeline`
- Compile agents run on the `HoneyDrunk.Agents` runtime
- This AGENTS.md becomes the agent configuration, not the implementation

The verbs (ingest, compile, query, lint) are deliberately the future contract method names. Keep them stable.
