# LLM Wiki and Knowledge Formats

## Purpose

This page tracks durable patterns for agent-readable, human-readable knowledge stores such as Lore, LLM wikis, and portable markdown knowledge bundles.

## 2026-06-16 compile additions: Open Knowledge Format

### Source-backed claims
- Google Cloud introduced Open Knowledge Format (OKF) v0.1 as an open specification that formalizes the LLM-wiki pattern into a portable directory of markdown files with YAML frontmatter and normal markdown cross-links. Source: `raw/2026-06-16-web-google-introducing-the-open-knowledge-format.md`. confidence: 1 official Google Cloud source, last-confirmed 2026-06-16.
- OKF is designed as a format rather than a platform: bundles are just files, markdown, and small structured frontmatter fields so humans, search tools, git repos, and agents can consume the same artifact without a proprietary SDK. Source: `raw/2026-06-16-web-google-introducing-the-open-knowledge-format.md`. confidence: 1 official Google Cloud source, last-confirmed 2026-06-16.
- OKF v0.1 requires each concept document to include a `type` field and defines optional structured fields such as `title`, `description`, `resource`, `tags`, and `timestamp`; the detailed content model remains producer-defined. Source: `raw/2026-06-16-web-google-introducing-the-open-knowledge-format.md`. confidence: 1 official Google Cloud source, last-confirmed 2026-06-16.
- OKF bundles can include hierarchy `index.md` files and chronological `log.md` files, and relationships are represented through markdown links that turn the bundle into a graph of concepts. Source: `raw/2026-06-16-web-google-introducing-the-open-knowledge-format.md`. confidence: 1 official Google Cloud source, last-confirmed 2026-06-16.

### Typed entities
- specification: Open Knowledge Format / OKF v0.1
- pattern: LLM wiki
- artifact: markdown concept document
- metadata: YAML frontmatter
- field: `type`
- field: `title`
- field: `description`
- field: `resource`
- field: `tags`
- field: `timestamp`
- reserved file: `index.md`
- reserved file: `log.md`
- organization: Google Cloud
- concept: producer/consumer independence
- concept: format-not-platform

### Explicit relationships
- OKF formalizes LLM-wiki conventions for portability across agents, catalogs, repositories, and viewers.
- Markdown bodies complement YAML frontmatter by keeping knowledge readable while preserving queryable metadata.
- Producer/consumer independence depends-on a stable file-format contract rather than a shared runtime service.
- OKF complements HoneyDrunk.Lore because Lore is already a flat-file, markdown-first wiki with indexes, graph-ready links, and agent compile rules.

### HoneyDrunk implications
- Compare Lore's current schema with OKF v0.1 before adding heavier graph/vector infrastructure; frontmatter fields may be a low-cost compatibility step.
- Preserve Lore's source citations and confidence notes even if an OKF export is added, because OKF defines interoperability fields rather than HoneyDrunk's decision-support quality bar.
- If HoneyDrunk exports Lore for external tools, consider an OKF-compatible bundle or adapter rather than making tools parse Lore-specific indexes directly.

### Quality notes
- Official Google Cloud/spec announcement. Use as compatibility scouting evidence until the OKF repository/spec is reviewed directly and stability is proven.

## 2026-06-21 compile additions: agent memory as wiki-adjacent retrieval

### Source-backed claims
- Elastic's agent-memory source describes a persistent memory layer with hybrid retrieval, reranking, supersession, decay, and document-level security. Although it is not a markdown wiki format, it reinforces Lore's need to preserve source provenance, supersession, and access boundaries if retrieval infrastructure is added later. Source: `raw/2026-06-21-web-elastic-agent-memory-on-elasticsearch-hybrid-retrieval-and-dls-elastic.md`. confidence: 1 vendor engineering source, last-confirmed 2026-06-21.
- Thoughtworks' organizational-memory source argues that useful agent memory must encode the organization's implicit patterns, decisions, and context rather than only retrieve documents. Source: `raw/2026-06-21-web-thoughtworks-the-agent-unconscious-embedding-organizational-memory-in-.md`. confidence: 1 practice source, last-confirmed 2026-06-21.

### Typed entities
- product: Elasticsearch
- concept: agent memory
- concept: hybrid retrieval
- concept: document-level security
- concept: supersession
- concept: retention decay
- concept: organizational memory

### Explicit relationships
- Agent memory systems complement LLM wikis when they preserve provenance, security trimming, supersession, and stale-claim decay.
- Organizational memory depends-on explicit capture of decisions and conventions; raw embeddings alone do not make knowledge decision-usable.

### HoneyDrunk implications
- If Lore adds BM25/vector/graph retrieval, keep markdown pages as the semantic source of truth and treat indexes as derived infrastructure.
- Preserve confidence, last-confirmed dates, supersession, and privacy filtering in any future machine-readable export or memory index.

### Quality notes
- Elastic is vendor-authored and Thoughtworks is practice guidance. Use them to shape future Lore retrieval experiments, not as a mandate to adopt Elasticsearch.

## 2026-06-22 compile additions: self-improving agent memory

### Source-backed claims
- Perplexity Brain describes a self-improving memory system for agents that stores work history, corrections, sources, and user feedback, links memories back to sources, builds a context graph, and performs periodic review. Source: `raw/2026-06-22-rss-perplexity-ai-self-improving-memory-for-agents.md`. confidence: 1 vendor product source, last-confirmed 2026-06-22.
- The source says Brain uses a sandboxed LLM wiki-style store and incremental updates from sessions, connectors, source documents, and corrections; this reinforces Lore's crystallization model where episodic outputs can become durable semantic pages when cited and decision-useful. Source: `raw/2026-06-22-rss-perplexity-ai-self-improving-memory-for-agents.md`. confidence: 1 vendor product source, last-confirmed 2026-06-22.
- Perplexity reports improved correctness, recall, and cost on historical-context tasks, but these are vendor preview metrics and should be reproduced on Lore/OpenClaw tasks before architecture changes. Source: `raw/2026-06-22-rss-perplexity-ai-self-improving-memory-for-agents.md`; page: [[agent-evaluation-and-benchmarks]]. confidence: 1 vendor product source, last-confirmed 2026-06-22.

### Typed entities
- product: Perplexity Brain
- concept: self-improving memory
- concept: context graph
- concept: source-linked memory
- pattern: LLM wiki
- concept: correction-derived memory

### Explicit relationships
- Self-improving memory complements LLM wikis when entries retain source links, correction provenance, and review cadence.
- Corrections can strengthen or supersede prior memory only when the supporting source and date are preserved.
- Vendor memory metrics do not supersede local memory evals on Lore/OpenClaw tasks.

### HoneyDrunk implications
- Lore should keep citations, confidence, supersession, and run summaries as first-class memory fields before adding vector/graph retrieval.
- A local memory spike should test whether corrections and previous decisions are retrieved accurately without polluting unrelated tasks.

### Quality notes
- Vendor product source. Useful as a pattern signal, not proof that Perplexity's reported metrics transfer to HoneyDrunk.

## 2026-06-23 compile additions: knowledge-agent structure and codebase graphs

### Source-backed claims
- Wang's "Knowledge Agents" source describes a source -> concept -> thesis -> primer structure where raw markdown, image/chart descriptions, concept pages, thesis files, and `PRIMER.md` help retrieval agents inject specialized knowledge into smaller or cheaper models. Source: `raw/2026-06-23-rss-tldr-ai-knowledge-agents-beat-frontier-models-with-better-structure-18.md`. confidence: 1 practitioner source, last-confirmed 2026-06-23.
- The same source reports a multi-pass retrieval pattern that often uses literal search plus embeddings, with local BGE-M3 or OpenAI `text-embedding-3-small`, and may short-circuit easy questions before spending more retrieval/model effort. Source: `raw/2026-06-23-rss-tldr-ai-knowledge-agents-beat-frontier-models-with-better-structure-18.md`; page: [[ai-agent-harnesses]]. confidence: 1 source, last-confirmed 2026-06-23.
- The codebase-memory-mcp repository turns source code into a persistent local graph of symbols, call chains, routes, services, ADRs, and cross-service relationships exposed through MCP tools. Source: `raw/2026-06-23-rss-tldr-devops-codebase-memory-mcp-github-repo.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 project README source, last-confirmed 2026-06-23.

### Typed entities
- pattern: source extraction
- artifact: concept page
- artifact: thesis file
- file: `PRIMER.md`
- model/tool: BGE-M3
- model/tool: `text-embedding-3-small`
- tool/server: codebase-memory-mcp
- concept: code knowledge graph
- concept: hybrid retrieval
- protocol: MCP

### Explicit relationships
- Knowledge-agent retrieval depends-on curated source extraction and concept/thesis organization, not only embedding search.
- Multi-pass retrieval complements flat indexes when easy questions can be answered cheaply and hard questions need broader context.
- Code graphs complement LLM wiki pages by representing functions, classes, calls, routes, and architectural relationships as traversable structure.

### HoneyDrunk implications
- Lore's flat-file raw/output/wiki/index tiers already map to the source/concept/thesis/primer idea; a future retrieval spike should preserve citations and confidence notes rather than replacing them with opaque embeddings.
- If codebase graphs are adopted, keep generated graph artifacts separate from authoritative source and document freshness, provenance, and tool version.

### Quality notes
- Knowledge Agents is practitioner/self-reported. codebase-memory-mcp is project README evidence. Both are useful design signals but require local evaluation before infrastructure changes.

## 2026-06-28 compile additions: AI knowledge fabric

### Source-backed claims
- Thoughtworks describes an AI knowledge fabric as a curated, dynamically updated, agent-optimized semantic layer that supplies organizational context, engineering standards, domain boundaries, and integration knowledge to AI agents. Source: `raw/2026-06-28-rss-thoughtworks-insights-build-an-ai-knowledge-fabric-for-your-organizati.md`. confidence: 1 practice source, last-confirmed 2026-06-28.
- The source proposes three knowledge-fabric layers: engineering knowledge for stack defaults and technical guardrails, industry knowledge for bounded vertical context, and institutional knowledge for product specs, ownership, APIs, access levels, and internal integration patterns. Source: `raw/2026-06-28-rss-thoughtworks-insights-build-an-ai-knowledge-fabric-for-your-organizati.md`. confidence: 1 source, last-confirmed 2026-06-28.
- Thoughtworks recommends agent-friendly formats such as Markdown, JSON, YAML, schemas, consistent semantic chunks, incremental context unveiling, continuous event-driven updates, ownership/review, and explicit "do not do" guardrails. Source: `raw/2026-06-28-rss-thoughtworks-insights-build-an-ai-knowledge-fabric-for-your-organizati.md`. confidence: 1 source, last-confirmed 2026-06-28.
- The source cites Open Knowledge Format and LLM-wiki-style approaches as compatible patterns for agent-readable organizational knowledge. Source: `raw/2026-06-28-rss-thoughtworks-insights-build-an-ai-knowledge-fabric-for-your-organizati.md`. confidence: 1 source, last-confirmed 2026-06-28.

### Typed entities
- concept: AI knowledge fabric
- layer: engineering knowledge
- layer: industry knowledge
- layer: institutional knowledge
- format: Markdown
- format: JSON
- format: YAML
- specification: Open Knowledge Format / OKF
- pattern: LLM wiki
- control: ownership and review process
- control: explicit anti-pattern guardrails

### Explicit relationships
- Knowledge fabric complements Lore by turning raw documents and tribal knowledge into curated, cited, agent-consumable context.
- Engineering defaults and "don'ts" reduce agent freedom where standards matter more than generic model creativity.
- Event-driven updates complement scheduled compile because stale institutional knowledge can mislead agents faster than public research pages.
- Ownership and review are required because agent knowledge is operational configuration, not passive documentation.

### HoneyDrunk implications
- Lore's raw/output/wiki/index tiers already implement much of the knowledge-fabric shape; the next improvement should be ownership, frontmatter compatibility, and freshness signals before heavier infrastructure.
- Keep HoneyDrunk-specific architecture rules, repo ownership, API contracts, and "do not use legacy path" constraints short, cited, and easy for agents to retrieve.
- Use the knowledge-fabric framing to distinguish public research pages from institutional operating rules; they should have different confidence and access controls.

### Quality notes
- Thoughtworks is practice guidance, not a measured HoneyDrunk implementation. Use it to refine Lore schema and update cadence, not as proof that a specific platform is required.
