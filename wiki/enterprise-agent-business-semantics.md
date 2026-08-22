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
