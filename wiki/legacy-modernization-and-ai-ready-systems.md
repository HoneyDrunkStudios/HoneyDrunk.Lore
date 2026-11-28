# Legacy Modernization and AI-Ready Systems

## Decision-useful summary

AI-ready modernization is not just cloud migration or automated code conversion. The Thoughtworks/AWS source frames the durable work as recovering business intent and operational semantics from legacy systems, then preserving those semantics through governed specifications, reusable context libraries, incremental migration, and behavior validation. For HoneyDrunk, this connects legacy modernization to the same meaning-layer discipline used in [[enterprise-agent-business-semantics]] and [[llm-wiki-and-knowledge-formats]].

## Source-backed claims

- Thoughtworks argues that cloud migration alone does not make a legacy estate AI-ready, and simple transpilation can preserve or amplify brittleness when business context remains hidden. confidence: 1 Thoughtworks practice/vendor-partner source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-thoughtworks-insights-how-thoughtworks-combines-ai-works-with-aws-tran.md]
- The source says modernization for AI agents requires recovering operational semantics: workflows, interacting business rules, data movement across domains, and encoded business intent. confidence: 1 source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-thoughtworks-insights-how-thoughtworks-combines-ai-works-with-aws-tran.md]
- Thoughtworks positions AWS Transform as the modernization execution engine and AI/works as the enterprise context layer, combining decomposition/migration orchestration with governed specifications, reusable modernization intelligence, an enterprise context library, and continuous regeneration. confidence: 1 source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-thoughtworks-insights-how-thoughtworks-combines-ai-works-with-aws-tran.md]
- The case study describes a global manufacturer retiring a mainframe warranty platform by moving four JCL batch jobs to Python on AWS Batch, migrating three Db2 schemas to PostgreSQL, and continuously comparing legacy and modernized behavior with automated data validation. confidence: 1 vendor case-study source, last-confirmed 2026-09-11. [source: raw/2026-09-11-rss-thoughtworks-insights-how-thoughtworks-combines-ai-works-with-aws-tran.md]

## Typed entities

- organization: Thoughtworks
- platform/service: AI/works
- platform/service: AWS Transform
- platform/service: Mechanical Orchard Imogen
- platform/service: AWS Batch
- database: Db2
- database: PostgreSQL
- system type: mainframe warranty platform
- artifact: governed specification
- artifact: enterprise context library
- control: automated data validation framework

## Explicit relationships

- Legacy modernization depends-on context recovery when AI agents must reason over workflows, rules, and data relationships.
- Cloud migration complements, but does not supersede, semantic decomposition and behavior validation.
- Automated code conversion can contradict AI-readiness when it preserves brittle boundaries without exposing business intent.
- Behavior validation uses legacy production behavior as a comparison target during incremental cutover.

## HoneyDrunk implications

- For any HoneyDrunk legacy migration, capture workflows, business rules, data contracts, and validation examples as governed artifacts before asking agents to transform code.
- Treat an AI-ready platform as a maintained semantic surface, not as a one-time generated modernization report.
- Validate modernization claims with behavior-level comparisons, not only static code parity.

## Confidence and quality notes

- Quality posture: Thoughtworks source is vendor/practice guidance with a case study; it is decision-useful for architecture posture but not neutral procurement proof.
- Privacy filter: no customer-private details beyond the public case-study summary were promoted.


## 2026-11-28: App Service Managed Instance placement requires dependency-level validation

### Typed entities

project: Azure App Service Managed Instance; project: Azure Catalyst; project: App Service Environment v3; concept: Windows dependency assessment; decision: non-production migration validation; file: raw/2026-11-28-rss-modernize-more-windows-applications-with-managed-instance-on-azure-app.md.

### Claims and evidence

- Microsoft's November 17 account says Managed Instance became GA in August and adds Catalyst assessment plus Premium v3/memory-optimized availability and Isolated v4 in ASE v3. Availability is being enabled across eligible infrastructure; plan/region compatibility remains conditional. confidence: 1 source, last-confirmed 2026-11-28 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-28-rss-modernize-more-windows-applications-with-managed-instance-on-azure-app.md)
- The source targets eligible Windows web applications with supported installers, services, registry configuration and storage mounts, plus managed identity/Key Vault and Bastion diagnostics. It explicitly excludes Linux/container hosting and arbitrary full-VM administration. Assessment identifies candidates; representative non-production validation must establish actual dependency fit. confidence: 1 source, last-confirmed 2026-11-28 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-11-28-rss-modernize-more-windows-applications-with-managed-instance-on-azure-app.md)

### Explicit relationships

Migration placement depends-on supported OS dependencies, plan/region and validated installation/network behavior; Catalyst uses assessment rather than compatibility proof. See [[windows-component-registration-and-service-boundaries]].

### Decision and quality notes

Vendor modernization guidance, no subscription inventory or migration executed. This complements semantic modernization evidence without claiming equivalent AWS/Azure capabilities. Source-specific claims remain provisional; repeated captures and derived queries add no independent support. Open question: Which representative Windows web app validates installer/service/registry/share dependencies, identity, private networking, restart/scale recovery and rollback on the intended supported plan/region? See [[indexes/gaps]].
