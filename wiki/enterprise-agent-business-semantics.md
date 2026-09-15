# Enterprise Agent Business Semantics

## Decision-useful summary
Enterprise agents that answer business questions need a governed meaning layer, not just data access. The Databricks/Thoughtworks source is useful because it makes "semantic context" concrete: metric definitions, owners, trusted systems of record, relationship status, citations, versioned approved definitions, and tests over golden business questions. For HoneyDrunk, this is the same reliability problem as Lore: source access is necessary, but decision-useful answers require cited, versioned, owner-approved truth. [source: raw/2026-08-22-rss-thoughtworks-insights-agents-on-databricks-the-platform-is-ready-your-.md]

## Source-backed claims
- Thoughtworks argues that Databricks Unity Catalog and governance layers can solve access while leaving agents unable to reliably understand business terms such as revenue, churn, customer, account, product, or the trusted source for a metric. confidence: 1 Thoughtworks practice source, last-confirmed 2026-08-22. [source: raw/2026-08-22-rss-thoughtworks-insights-agents-on-databricks-the-platform-is-ready-your-.md]
- The source says Genie Ontology, OntoBricks, and Ontos address different meaning-layer needs: discovered query-time context, formal ontologies/reasoning, and curated ownership/data contracts. confidence: 1 source, last-confirmed 2026-08-22. [source: raw/2026-08-22-rss-thoughtworks-insights-agents-on-databricks-the-platform-is-ready-your-.md]
- The source recommends keeping discovered meaning and approved meaning in separate lanes so model suggestions can start as candidates without quietly becoming business truth. confidence: 1 source, last-confirmed 2026-08-22. [source: raw/2026-08-22-rss-thoughtworks-insights-agents-on-databricks-the-platform-is-ready-your-.md]
- The source recommends a "meaning regression suite" of golden business questions that assert on approved metrics, approved relationships, citations, and ambiguity handling rather than prose style. confidence: 1 source, last-confirmed 2026-08-22. [source: raw/2026-08-22-rss-thoughtworks-insights-agents-on-databricks-the-platform-is-ready-your-.md; page: [[agent-evaluation-and-benchmarks]]]

## Typed entities
- platform: Databricks
- catalog/governance layer: Unity Catalog
- feature: Genie Ontology
- project: OntoBricks
- project: Ontos
- concept: meaning layer
- concept: approved definition
- concept: discovered meaning
- artifact/control: meaning regression suite
- artifact/control: golden question-answer pair
- standard/domain ontology examples: FIBO, FHIR, CDISC

## Explicit relationships
- Business agents depend-on approved metric definitions, source-of-record ownership, explicit relationships, citations, and versioned meaning.
- Genie Ontology complements OntoBricks and Ontos because discovered context, formal semantics, and curated data contracts address different failure modes.
- Discovered meaning contradicts approved business truth when a model suggestion is used without owner verification.
- Meaning regression suites complement truth contracts by testing semantic correctness at the business-definition layer.

## HoneyDrunk implications
- Treat Lore's confidence notes, source citations, and indexes as a lightweight meaning layer; any future business agent needs the same discipline before answering operational questions.
- For HoneyDrunk analytics or customer/process agents, version approved definitions and test them with golden questions before exposing decision automation.
- Keep inferred relationships explicitly marked until a domain owner verifies them.

## Confidence and quality notes
- Quality posture: decision-useful practice guidance from one Thoughtworks source. It should shape architecture and eval design, not vendor selection.
- Privacy filter: no proprietary data, customer records, credentials, or private business definitions copied.

## 2026-09-11 legacy modernization as context recovery

### Source-backed claims
- Thoughtworks' AWS Transform/AI-works source says the durable enterprise asset for AI-ready modernization is business intent encoded in legacy systems, not just code or data. confidence: 1 Thoughtworks practice/vendor-partner source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-thoughtworks-insights-how-thoughtworks-combines-ai-works-with-aws-tran.md]
- The source frames modernized architectures as easier for AI agents to reason over when business context becomes reusable, governed, and continuously regenerated rather than left as one-time migration documentation. confidence: 1 source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-thoughtworks-insights-how-thoughtworks-combines-ai-works-with-aws-tran.md]

### Typed entities
- `concept`: context recovery
- `artifact`: governed specification
- `artifact`: enterprise context library
- `platform`: AWS Transform
- `platform`: AI/works

### Explicit relationships
- Enterprise-agent reliability depends-on business context recovery and governed specifications.
- Modernization outputs complement semantic layers only when they remain versioned, reusable, and validated as systems evolve.

### HoneyDrunk implications
- For any future business agent, treat legacy workflow/rule extraction as semantic infrastructure that needs citations, owners, and regression tests.

### Quality notes
- Vendor/practice guidance; use for architecture posture, not tool procurement without local validation.

## 2026-09-12 data readiness for agentic AI

### Sources
- [Martin Fowler: Making your data ready for agentic AI](../raw/2026-09-12-rss-martin-fowler-making-your-data-ready-for-agentic-ai.md)
- [Thoughtworks: From specification to production - building enterprise platforms with agentic AI](../raw/2026-09-12-rss-thoughtworks-insights-from-specification-to-production-building-enterp.md)

### Typed entities
- `concept`: data contract
- `standard`: Open Data Contract Standard
- `architecture`: medallion architecture
- `tier`: Bronze
- `tier`: Silver
- `tier`: Gold
- `tier`: Adaptive Gold
- `concept`: context layer
- `concept`: capability model
- `pattern`: confidence-threshold routing
- `pattern`: delegated access / just-in-time credentials
- `practice`: specification-to-production platform generation

### Claims
- Fowler/Thoughtworks argues that agent-ready data must be trusted, contextual, traceable, governed, and operational, with data contracts, freshness SLAs, quarantine paths, lineage, auditability, and clear ownership before agents act on it. confidence: 1 Fowler/Thoughtworks practice source, last-confirmed 2026-09-12. [source: raw/2026-09-12-rss-martin-fowler-making-your-data-ready-for-agentic-ai.md]
- The source recommends agents consume governed Gold-or-better data in a medallion model, with unstructured sources held to similar metadata, freshness, quality, and confidence-routing expectations. confidence: 1 source, last-confirmed 2026-09-12. [source: raw/2026-09-12-rss-martin-fowler-making-your-data-ready-for-agentic-ai.md]
- Thoughtworks' specification-to-production case study claims agentic AI generated a cloud-native enterprise platform from natural-language specifications with generated backend services, frontend, infrastructure, tests, and security; treat this as practitioner case evidence, not a universal benchmark. confidence: 1 Thoughtworks practitioner case source, last-confirmed 2026-09-12. [source: raw/2026-09-12-rss-thoughtworks-insights-from-specification-to-production-building-enterp.md]

### Explicit relationships
- Enterprise-agent reliability depends-on data contracts, semantic context, lineage, access controls, and capability declarations before model reasoning begins.
- Retrieved text informs agent decisions but should not supersede governed capability preconditions, permissions, reversibility, and owner-defined constraints.
- Specification quality can become the bottleneck when agentic implementation capacity increases.

### HoneyDrunk implications
- Treat Lore's citations/confidence notes as a lightweight version of the governed context layer Fowler describes; agent access to business data should require owners, contracts, freshness, lineage, and regression questions.
- For enterprise-agent prototypes, define what the agent may read, what it may mutate, which data tier is authoritative, and who can approve a capability.

### Quality notes
- Fowler/Thoughtworks practice guidance is high-signal architecture evidence but still needs local data-contract inventory before becoming policy. The platform-generation case is vendor/practitioner evidence and should be validated through local scope and quality review.

## 2026-09-15: Data normalization and governed meaning

### Typed entities

concept: data normalization; concept: sensitivity classification; concept: lineage; concept: semantic business layer.

### Claims and evidence

- Thoughtworks argues that moving data to a cloud platform does not resolve ambiguous meaning, quality, or governance. Its foundations include deterministic normalization, sensitivity classification, least privilege, freshness, lineage, metadata catalogs, and shared business definitions. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-thoughtworks-insights-ai-ready-data-the-anthology-part-1.md)

### Explicit relationships

Reliable retrieval depends-on normalized inputs and governed meaning; ingestion uses metadata and lineage to retain provenance. This extends the existing agent-ready data contract discussion.

### Decision and quality notes

Practitioner architectural guidance, with no controlled AI-quality benchmark. Keep funding and ownership of data maintenance explicit; local inventory remains unresolved. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which Lore or business-data fields need deterministic normalization, sensitivity labels, freshness checks, and an owner-approved definition before retrieval? See [[indexes/gaps]].


## 2026-09-15: Semantic guidance paired with constraint checks

### Typed entities

concept: semantic guide; concept: constraint sensor; concept: provisional relationship; concept: semantic regression.

### Claims and evidence

- Thoughtworks describes valid rules applied in the wrong business context, using a latency target that ignores downstream costs as an example. Its proposed guide stores expert-approved concepts and relationships while keeping suggestions provisional until review. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-thoughtworks-insights-harnessing-the-agent-semantic-reliability-at-sca.md)
- Its sensor checks constraints where the risk originates, classifies failures, and re-evaluates after changes. Feedback updates context and regression checks; traces of accessed material alone do not prove semantic correctness. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-thoughtworks-insights-harnessing-the-agent-semantic-reliability-at-sca.md)

### Explicit relationships

Semantic reliability depends-on approved relationships and constraint checks. Failure feedback uses observed mistakes to update retrieval context and [[agent-evaluation-and-benchmarks]].

### Decision and quality notes

Proposed practice pattern, not proof that an ontology or model upgrade guarantees correct decisions. Approval of business meaning is distinct from source ingestion. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which cross-domain constraints need approved relationship records and regression cases, and what changes should trigger their re-evaluation? See [[indexes/gaps]].


## 2026-09-15: Consolidation of governed business meaning

The recurring practice claim is that enterprise-agent reliability depends-on governed business definitions and explicit relationships beyond data access alone. confidence: 3 sources, last-confirmed 2026-09-15 (archived captures and existing cited synthesis; no live refresh). Support: [Databricks meaning layer](../raw/2026-08-22-rss-thoughtworks-insights-agents-on-databricks-the-platform-is-ready-your-.md), [AI-ready data](../raw/2026-09-14-rss-thoughtworks-insights-ai-ready-data-the-anthology-part-1.md), and [semantic guidance and sensors](../raw/2026-09-14-rss-thoughtworks-insights-harnessing-the-agent-semantic-reliability-at-sca.md).

This strengthens the claim from a one-article suggestion to repeated practitioner guidance, with moderate confidence for architectural consideration. All three are Thoughtworks publications, so supporting count is not independent-publisher corroboration or empirical proof of improved outcomes. Product-specific and sensor-specific claims retain their individual support counts. Existing claims and dates are preserved; no supersession is warranted. Local acceptance still depends-on owner-approved definitions and regression evidence.
