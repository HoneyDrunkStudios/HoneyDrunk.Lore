# Cloud Data Platforms and Analytics

This page tracks managed analytics, ETL, lakehouse, and data-platform runtime changes when they affect architecture, cost, schema evolution, or operational governance.

## 2026-08-26 compile additions: AWS Glue 6.0 and Iceberg v3

### Source-backed claims
- AWS announced AWS Glue 6.0 general availability with 30% lower pricing than previous Glue versions, a runtime based on Apache Spark 4.1, Python 3.13, Scala 2.13, and full Apache Iceberg v3 support through Iceberg 1.11.0. Source: `raw/2026-08-26-rss-tldr-devops-aws-glue-6-0-now-available-with-30-lower-price-and-full-ap.md`. confidence: 1 AWS News Blog source, last-confirmed 2026-08-26.
- Glue 6.0's Iceberg v3 support includes VARIANT with shredding for semi-structured data, Geometry and Geography data types, nanosecond-precision timestamps, and unknown-type handling for evolving schemas. Source: `raw/2026-08-26-rss-tldr-devops-aws-glue-6-0-now-available-with-30-lower-price-and-full-ap.md`. confidence: 1 source, last-confirmed 2026-08-26.
- AWS says Glue 6.0 adds Spark declarative pipelines, Arrow-native Python UDFs/UDTFs, and real-time streaming mode for stateless streaming use cases with single-digit millisecond latency. Source: `raw/2026-08-26-rss-tldr-devops-aws-glue-6-0-now-available-with-30-lower-price-and-full-ap.md`. confidence: 1 source, last-confirmed 2026-08-26.
- Existing Glue jobs can select version 6.0 through existing create/update APIs, Glue Studio, SageMaker Unified Studio, notebooks, auto-upgrade, or the Spark upgrade agent; no API changes are required to select the version. Source: `raw/2026-08-26-rss-tldr-devops-aws-glue-6-0-now-available-with-30-lower-price-and-full-ap.md`. confidence: 1 source, last-confirmed 2026-08-26.

### Typed entities
- service: AWS Glue
- version: AWS Glue 6.0
- table format: Apache Iceberg v3
- library/version: Iceberg 1.11.0
- runtime: Apache Spark 4.1
- runtime: Python 3.13
- runtime: Scala 2.13
- data type: VARIANT
- data type: Geometry
- data type: Geography
- feature: Spark Declarative Pipelines
- feature: Arrow-native Python UDFs
- feature: Arrow-native Python UDTFs
- feature: real-time streaming mode
- service: Amazon SageMaker Unified Studio

### Explicit relationships
- AWS Glue 6.0 depends-on Spark 4.1 and Iceberg 1.11.0 for its updated managed ETL runtime.
- Iceberg v3 VARIANT shredding complements semi-structured event/log pipelines by reducing forced flattening and duplicate transformed copies.
- Declarative pipelines complement ETL authoring by shifting some execution-order and optimization work to the Spark runtime.
- Real-time streaming mode complements batch ETL only for stateless streaming paths; stateful semantics and downstream idempotency remain application concerns.
- Glue version selection can supersede older Glue runtime versions where cost, Iceberg v3, or Spark 4.1 compatibility is required.

### HoneyDrunk implications
- If HoneyDrunk builds AWS-hosted analytics pipelines, evaluate Glue 6.0 only against actual data volume, schema evolution, streaming latency, and region/cost requirements.
- Do not assume Iceberg v3 features remove data-contract work; producers still need schema ownership, compatibility tests, and downstream query validation.
- Treat the 30% price claim as service-version pricing signal requiring current AWS pricing and workload-cost verification before architecture decisions.

### Quality notes
- AWS News Blog is authoritative for service availability and stated features. Price, region support, and migration behavior are live vendor facts and need current AWS-console or documentation verification before implementation.

## 2026-09-14: Colocated joins can still fan out

### Typed entities

project: PlanetScale Neki; project: PostgreSQL; concept: shard colocation; concept: distributed query fan-out.

### Claims and evidence

- PlanetScale's captured Neki walkthrough covers simple and extended PostgreSQL protocols and a customers/orders example. Placing orders with customers via customer_id enables local joins, but a query for recent orders across all customers still contacts every shard. confidence: 1 source, last-confirmed 2026-09-14 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-13-rss-tldr-tech-the-lifecycle-of-a-sharded-postgres-query.md)

### Explicit relationships

Local join execution depends-on related-row colocation; single-shard routing depends-on query predicates as well as partitioning.

### Decision and quality notes

Vendor architecture evidence, not an independent performance comparison. Distinguish reducing cross-shard join work from eliminating fan-out when evaluating partition keys. Source count is provisional single-source support; repeated citations and derived summaries add no independent corroboration. Open question: Which query predicates and entity relationships should drive partition keys, and how will HoneyDrunk measure cross-shard joins separately from query fan-out? See [[indexes/gaps]].


## 2026-10-04: Analytics cost follows writes and query shape

### Typed entities

project: Bolna; project: PostgreSQL; project: ClickHouse; library: ClickPipes; concept: CDC.

### Claims and evidence

Bolna reports moving analytics from Datastream/BigQuery to ClickHouse/ClickPipes, replacing repeated dashboard FINAL deduplication with materialized views, limiting BI resources, and selectively using REPLICA IDENTITY FULL to address TOASTed JSONB mismatches at increased WAL cost. Writing final call state plus checkpoints rather than every transient update produced its largest reported saving. The approximately sixfold saving is workload-specific; detailed freshness is one or two minutes after call completion despite the real-time headline. confidence: 1 source, last-confirmed 2026-10-04 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-04-rss-bigquery-to-clickhouse-at-15m-call-minutes-a-day-what-broke-what-we-fi.md)

### Explicit relationships

Analytics cost depends-on producer write volume and deduplication placement.

### Decision and quality notes

Single authored source; source-specific claims remain provisional. Related reports and derived queries add no independent confirmation. No HoneyDrunk integration or independently reproduced outcome is established. Open question: Which durable checkpoints, crash-recovery guarantees, CDC correctness checks, and measured query costs justify reducing HoneyDrunk intermediate writes? See [[indexes/gaps]].


## 2026-10-04: SQL local deployment is GA while local AI remains preview

### Typed entities

project: SQL Server; project: Azure Local; project: Foundry Local; concept: disconnected operations.

### Claims and evidence

Microsoft announces SQL Server on Azure Local GA for connected/disconnected deployments on Windows or Linux VMs. Connected management can use Azure Arc; disconnected operations continue locally. SQL Server licensing is separate from Azure Local infrastructure, with eligible licensing paths differing by connectivity. Foundry Local on Azure Local remains preview in this announcement and is not promoted to GA with SQL Server. confidence: 1 source, last-confirmed 2026-10-04 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-04-web-sql-server-on-azure-local-is-now-generally-available-microsoft-sql-ser.md)

### Explicit relationships

Local SQL uses Azure Local infrastructure; deployment depends-on connectivity and eligible licensing; local AI uses a separate preview service.

### Decision and quality notes

Single authored source; source-specific claims remain provisional. Related reports and derived queries add no independent confirmation. No HoneyDrunk integration or independently reproduced outcome is established. Open question: Which HoneyDrunk connectivity, hardware, high-availability, licensing, and inference requirements justify Azure Local evaluation? See [[indexes/gaps]].


## 2026-10-05: DAB 2.1.5 adds native types and tighter endpoint authorization

### Typed entities

project: Data API builder; library: Microsoft.DataApiBuilder.Core; concept: SQL JSON; concept: SQL vector; concept: MCP authorization.

### Claims and evidence

- Microsoft announces stable DAB 2.1.5 with native SQL json/vector support through REST and GraphQL, an embeddable Core NuGet package, multi-segment API base paths, and a .NET 10 engine. JSON column values are returned as serialized JSON strings, rather than automatically nested objects. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-data-api-builder-2-1-5-json-and-vector-data-type-support-and-more.md)
- The release reports MCP Host/Origin allowlists, role-gated entity discovery, shared create/update authorization, a health probe, restricted GraphQL sorting, bounded nested filters, loopback-only configuration writes, stricter production EasyAuth validation, and a separate non-root container variant. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-data-api-builder-2-1-5-json-and-vector-data-type-support-and-more.md)

### Explicit relationships

DAB uses entity permissions for vector exposure; MCP discovery depends-on caller authorization. See [[mcp-tool-governance-and-app-surfaces]].

### Decision and quality notes

Official release report; linked release notes and local policy regressions were not tested. CRUD support for vector columns does not itself prove a similarity-search API. Underlying database native-type support must be checked separately. Source-specific claims remain provisional; related reports and derived queries add no independent confirmation. Open question: Which pinned database/DAB pairs pass JSON serialization, vector CRUD, role-gated discovery, restricted sorting, origin, and configuration-access tests? See [[indexes/gaps]].


## 2026-10-05: DiskANN GA scope remains distinct from every SQL deployment

### Typed entities

project: Azure SQL Database; project: Azure SQL Managed Instance; project: Microsoft Fabric; concept: DiskANN; concept: asynchronous index maintenance.

### Claims and evidence

- Microsoft announces DiskANN vector index/search GA in Azure SQL Database, Azure SQL Managed Instance with the always-up-to-date policy, and SQL database in Microsoft Fabric. It describes approximate graph navigation, asynchronous index maintenance with insert/update/delete support, iterative filtering, and optimizer choice between exact and approximate strategies. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-diskann-vector-index-and-vector-search-are-now-generally-available-in-.md)
- The example uses TOP WITH APPROXIMATE and VECTOR_SEARCH with relational predicates. The article says similarity can compose with joins and row-level security rather than requiring a separately reconciled vector store. confidence: 1 source, last-confirmed 2026-10-05 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-05-rss-diskann-vector-index-and-vector-search-are-now-generally-available-in-.md)

### Explicit relationships

Vector retrieval uses relational filters and security; freshness depends-on asynchronous index maintenance. See [[agentic-retrieval-and-search]].

### Decision and quality notes

Official archived GA report; it does not establish GA for standalone SQL Server or other Managed Instance update policies. A mentioned billion-vector demonstration was not inspected, and no latency/recall guarantee is inferred. Source-specific claims remain provisional; related reports and derived queries add no independent confirmation. Open question: Which HoneyDrunk SQL deployment policy and mutation/freshness, selective-filter, tenant-security, recall, and query-plan tests qualify DiskANN? See [[indexes/gaps]].


## 2026-10-12: Database replay preserves transaction context and exposes its blind spots

### Typed entities

project: Airbnb; project: MySQL; library: ProxySQL; concept: workload replay; concept: transaction ordering; concept: snapshot parity.

### Claims and evidence

- Airbnb describes proxy-level query capture, transaction reconstruction, five-minute log buckets, and synchronized workers that preserve relative timing. Load mode measures errors, latency and resource use against one target; compatibility mode compares two targets restored from the same snapshot. Its migration account identifies incomplete ordering with LIMIT as a source of differing results. confidence: 1 source, last-confirmed 2026-10-12 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-12-rss-beyond-synthetic-testing-capturing-and-replaying-real-database-workloa.md)
- The processor pins captured generated IDs into inserts so dependent queries remain comparable; the source explicitly acknowledges that this bypasses testing the target's native auto-increment generation. Captured SQL is treated as production data with encryption, limited access, bounded capture windows, and production-equivalent replay environments. confidence: 1 source, last-confirmed 2026-10-12 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-12-rss-beyond-synthetic-testing-capturing-and-replaying-real-database-workloa.md)

### Explicit relationships

Compatibility replay depends-on common starting state and transaction context; ID rewriting uses captured values and limits coverage of native ID generation. See [[api-testing-and-verification]].

### Decision and quality notes

First-party engineering account with unknown publication date in the capture. Reported scale and performance are workload-specific. Replay does not prove arbitrary concurrent schedules or all database features equivalent; production data protections remain part of the method. Source-specific claims remain provisional; derived queries add no independent support. Open question: Which HoneyDrunk replay cases preserve snapshot parity, transaction/session semantics, pacing, deterministic ordering, native ID-generation coverage, and production-data access controls? See [[indexes/gaps]].


## 2026-10-16: Schema migration safety spans compatibility, locks, and data correctness

### Typed entities

project: PostgreSQL; concept: expand-contract; concept: bounded backfill; concept: lock acquisition; concept: dual-write reconciliation.

### Claims and evidence

- BoundLayer frames safe schema change as separate expand, migrate, switch, verify, and contract phases that preserve coexisting application versions. Lock acquisition, transaction duration, resource headroom, replica lag, and service outcomes matter even when DDL itself is fast. confidence: 1 source, last-confirmed 2026-10-16 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-13-rss-zero-downtime-postgresql-migrations-a-production-playbook-for-safe-sch.md)
- The guide separates constraint introduction from validation transactions, describes concurrent-index invalid-artifact recovery, and calls for bounded idempotent backfills with observable progress. Mutable source data needs race protection; old/new divergence and unknown consumers must be resolved before contraction. A successful SQL exit or zero remaining rows does not prove business correctness. confidence: 1 source, last-confirmed 2026-10-16 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-13-rss-zero-downtime-postgresql-migrations-a-production-playbook-for-safe-sch.md)

### Explicit relationships

Safe schema evolution depends-on mixed-version compatibility and verified data invariants; backfill uses bounded work and reconciliation. See [[distributed-systems-patterns]].

### Decision and quality notes

Practitioner playbook, not an executed migration or a universal zero-downtime guarantee. Exact PostgreSQL locking/version semantics require primary documentation before implementation; examples are not copied as a HoneyDrunk SQL Server runbook. Recreating dropped schema does not restore lost data. Source-specific claims remain provisional; derived queries add no independent support. Open question: Which HoneyDrunk schema change has mixed-version, lock-wait, concurrent-backfill, data-reconciliation, and recovery evidence before destructive contraction? See [[indexes/gaps]].


## 2026-10-17: Shared protocol caches require one canonical response representation

### Typed entities

project: Cloudflare Hyperdrive; project: MySQL; library: mysql2; concept: capability negotiation; concept: canonical cache encoding; concept: pooled-session reset.

### Claims and evidence

- Cloudflare attributes rare empty results and hangs to Client and Endpoint nodes sharing a datacenter cache while storing differently encoded MySQL responses. Worker-facing capability translation changed result-set terminators; the fix stores canonical Hyperdrive-capability bytes regardless of writer and translates for the receiving client. confidence: 1 source, last-confirmed 2026-10-17 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-17-rss-inside-hyperdrive-how-we-solved-a-rare-hyperdrive-mysql-caching-bug.md)
- The account also reports fixing incomplete Unicode negotiation by using utf8mb4 and restoring that encoding after COM_RESET_CONNECTION, which otherwise reverted to the server default. Reported incident frequency and 99.99% connection success are vendor observations, not guarantees for arbitrary applications. confidence: 1 source, last-confirmed 2026-10-17 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-17-rss-inside-hyperdrive-how-we-solved-a-rare-hyperdrive-mysql-caching-bug.md)

### Explicit relationships

Correct shared caching depends-on canonical wire encoding; connection reuse depends-on restored session invariants. See [[distributed-systems-patterns]].

### Decision and quality notes

First-party incident analysis without local reproduction. Query equality alone does not prove wire-format compatibility. Test both cache-writer/read directions, negotiated capabilities, reset state, and non-BMP text before extrapolating. Source-specific claims remain provisional; derived summaries add no independent support. Open question: Which HoneyDrunk pool/cache tests cover both writer-reader directions, capability differences, connection-reset defaults, and non-BMP Unicode? See [[indexes/gaps]].


## 2026-10-17: Distributed expression evaluation preserves volatility and cardinality

### Typed entities

project: PlanetScale Neki; project: PostgreSQL; concept: volatile expression; concept: statement cardinality; concept: authoritative sequence shard; concept: session settings.

### Claims and evidence

- PlanetScale describes Neki evaluating sequence operations through the router using an authoritative shard, rather than allowing independent shards to allocate conflicting values. Volatile SELECT expressions need evaluation at the resulting table-expression cardinality; immutable computations can be reused where semantics permit. confidence: 1 source, last-confirmed 2026-10-17 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-17-rss-sequences-and-other-volatiles-in-neki.md)
- For the demonstrated UPDATE with nextval, Neki first reads key/shard columns with FOR UPDATE, evaluates a sequence value for each incoming row, and sends parameterized updates to the owning shards. Stable-expression pushdown must preserve session dependencies; transaction-start time is coordinated in the router. Sequence allocation is not gapless, and reset/cycle behavior is explicitly outside the article's uniqueness discussion. confidence: 1 source, last-confirmed 2026-10-17 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-17-rss-sequences-and-other-volatiles-in-neki.md)

### Explicit relationships

Distributed planning depends-on expression semantics, session state, and cardinality; sequence allocation uses an authoritative shard. See [[distributed-systems-patterns]].

### Decision and quality notes

Implementation explanation, not complete PostgreSQL equivalence or failover proof. Router-only does not mean all work is shard-local. The account acknowledges nondeterministic volatile-predicate outcomes under different valid plans; do not turn its examples into a universal SQL evaluation-order rule. Source-specific claims remain provisional; derived summaries add no independent support. Open question: Which distributed SQL tests verify volatile-call counts, session settings, transaction time, sequence rollback gaps, and failure recovery under cross-shard updates? See [[indexes/gaps]].


## 2026-10-18: SQL time-zone changes have product and historical boundaries

### Typed entities

project: Microsoft SQL; project: Azure SQL Managed Instance; concept: regional time-zone definition; concept: session override; concept: historical conversion.

### Claims and evidence

- Microsoft's October 15 capture distinguishes OS updates for SQL Server on Windows from Linux-to-Windows zone mappings and Azure database/session settings. Interim substitute zones match the affected regions' future offsets, not their complete historical rules; installing a zone update does not rewrite explicit conversion expressions. The interim zone for most of BC does not apply to locations aligned with Alberta. confidence: 1 source, last-confirmed 2026-10-18 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-18-rss-canada-s-2026-time-zone-updates-guidance-for-microsoft-sql.md)
- The capture says Managed Instance instance-level time zones are creation-time choices. Eligible Always-up-to-date instances can instead override supported current-time functions at database/session scope, without changing instance settings or SQL Agent schedules. An interim instance migration may require a second migration when the final zone becomes available; existing stored values are not converted by these settings. confidence: 1 source, last-confirmed 2026-10-18 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-18-rss-canada-s-2026-time-zone-updates-guidance-for-microsoft-sql.md)

### Explicit relationships

Regional conversion depends-on deployed zone definitions and query scope; instance migration depends-on scheduling and dependency validation. See [[distributed-systems-patterns]].

### Decision and quality notes

Archived vendor guidance, not a live confirmation of regional law or service rollout. Exact offsets, availability, syntax, and migration choices require current official documentation and target-deployment checks before use. No migration commands or legal deadline are promoted as an operational instruction. Source-specific claims remain provisional; derived queries add no independent support. Open question: Which HoneyDrunk deployments need regional time-zone handling, and do historical conversions, session reuse, SQL Agent schedules, and target zone availability pass boundary tests? See [[indexes/gaps]].


## 2026-10-18: Pipeline efficiency separates traffic reduction from data-fidelity requirements

### Typed entities

project: Cloudflare; project: Logfwdr; project: Buftee; project: ClickHouse; library: zstd; concept: weighted sampling; concept: partial aggregation.

### Claims and evidence

- Cloudflare describes splitting product schemas, changing compression, sending non-regional events once before late replication, and moving sampling/aggregation earlier. Buftee retention supports catch-up after inter-region disruption; data constrained to a region stays within its boundary. confidence: 1 source, last-confirmed 2026-10-18 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-18-rss-rewinding-the-exponential-how-we-keep-hardware-usage-down.md)
- Sampling supports estimates with recorded sampling rates, while rollups preserve selected dimensions and metrics and narrow the questions retained data can answer. The account compares sampled estimates across key frequencies and reports staged measurements of traffic, CPU, and memory; savings are workload-specific and overlapping interventions are not universal additive percentages. confidence: 1 source, last-confirmed 2026-10-18 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-18-rss-rewinding-the-exponential-how-we-keep-hardware-usage-down.md)

### Explicit relationships

Late replication depends-on buffering and recovery; sampling uses weights; aggregation depends-on selected dimensions. See [[distributed-systems-patterns]] and [[opentelemetry-genai-observability-and-ecosystem]].

### Decision and quality notes

First-party engineering account, not a prescription to discard forensic records. Approximate estimates and predetermined aggregates have different fidelity limits; exact distinct-count behavior is not established by the prose. Projections are not observed future capacity savings. Source-specific claims remain provisional; derived queries add no independent support. Open question: Which HoneyDrunk telemetry can tolerate weighted sampling or selected aggregates, and do rare-event fidelity, residency, retention-window recovery, and measured CPU/network cost remain acceptable? See [[indexes/gaps]].


## 2026-10-18: SqlClient Pool V2 targets concurrent cold connection creation

### Typed entities

library: Microsoft.Data.SqlClient; library: System.Threading.Channels; concept: Pool V2; concept: cold-start benchmark; concept: managed thread-pool pressure.

### Claims and evidence

- Microsoft describes Pool V2 as opt-in from SqlClient 7.1.0, enabled before any connections open, allowing concurrent new connections instead of legacy per-pool serial creation. Its benchmark clears the pool and holds all connections until all callers open; measured means cover the whole cold-start operation, not single-open latency, query execution, or warm reuse. confidence: 1 source, last-confirmed 2026-10-18 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-18-rss-try-sqlclient-s-new-connection-pool-for-faster-parallel-connections.md)
- The capture explicitly says OpenAsync still queues synchronous network work onto managed thread-pool threads. Higher network latency can therefore increase thread pressure; representative startup/burst/high-latency measurement and concurrency controls remain relevant. It describes restart with the switch disabled as rollback. confidence: 1 source, last-confirmed 2026-10-18 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-18-rss-try-sqlclient-s-new-connection-pool-for-faster-parallel-connections.md)

### Explicit relationships

Pool V2 uses channels and concurrent creation; realized latency depends-on network delay and thread-pool capacity. See [[dotnet-runtime-and-mobile-2026]].

### Decision and quality notes

Archived release/benchmark description; package availability and current implementation must be checked before adoption. No switch was changed. EF Core/Dapper compatibility claims do not demonstrate a particular application workload or remove server connection limits. Source-specific claims remain provisional; derived queries add no independent support. Open question: Which pinned SqlClient workload verifies cold bursts, warm reuse, cancellation, server limits, high-latency thread pressure, and restart rollback before enabling Pool V2? See [[indexes/gaps]].


## 2026-10-23: SQL connection architecture does not remove finite workload capacity

### Typed entities

project: PostgreSQL; project: Microsoft SQL; library: Microsoft.Data.SqlClient; concept: backend process; concept: connection pool; concept: workload capacity.

### Claims and evidence

- The Microsoft field note contrasts PostgreSQL's dedicated backend processes with Microsoft SQL assigning workers when requests execute. It explains why idle sessions need not reserve a dedicated SQL worker and why client connection pooling changes the cost of opening/closing application connections. confidence: 1 source, last-confirmed 2026-10-23 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-21-rss-postgresql-to-sql-field-notes-connections.md)
- Source contradiction retained: broad prose says applications need not worry about connection quantity/duration and calls manual count management an antipattern. The same source explicitly limits practical capacity by workload, hardware, service tier, and other resources and still recommends resource monitoring. Its 32,767 connection figure is an instance maximum, not a supported simultaneous-workload target for every SQL deployment. confidence: 1 source, last-confirmed 2026-10-23 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-21-rss-postgresql-to-sql-field-notes-connections.md)

### Explicit relationships

Connection behavior depends-on engine architecture, client pooling, and workload limits; request execution uses finite workers and memory. See [[distributed-systems-patterns]] and [[dotnet-runtime-and-mobile-2026]].

### Decision and quality notes

Vendor comparison with promotional framing. superseded-by: [bounded connection interpretation](#2026-10-23-sql-connection-architecture-does-not-remove-finite-workload-capacity), 2026-10-23T18:48:20-04:00; the unbounded reading of the broad prose is superseded by its specific workload/service-tier caveat and the earlier Pool V2 section. The rejected prose interpretation is preserved above. The October 6 publication predates the October 18 Pool V2 report even though captured later; neither source establishes actual HoneyDrunk capacity. Pooling, transaction lifetime, timeouts, and bounded concurrency remain workload questions. Source-specific claims remain provisional single-source evidence; repeated reports and query outputs add no independent support. Open question: Which SQL deployment and client-pool load tests establish session/worker limits, transaction duration, connection leaks, cancellation, cold bursts, and bounded concurrency at the selected service tier? See [[indexes/gaps]].


## 2026-10-23: Cascading deletion couples transaction size to locks and replication

### Typed entities

project: PostgreSQL; project: PlanetScale; concept: cascading delete; concept: lock queue; concept: logical replication; concept: soft delete; concept: bounded reaper.

### Claims and evidence

- PlanetScale describes large cascading deletes holding table locks while producing row/index/WAL work. A queued exclusive schema change can make subsequent writes wait behind it; missing indexes on referencing columns amplify lookup cost. A migration lock timeout bounds one wait but does not remove the large transaction itself. confidence: 1 source, last-confirmed 2026-10-23 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-23-rss-i-don-t-trust-on-delete-cascade.md)
- The article distinguishes publisher child deletes from subscriber trigger behavior under logical replication. Omitted child tables, subscriber-only children, and unusable replica identity can break the assumed cleanup contract. Its alternative combines an immediate logical-delete flag, filtering all relevant reads, and later bounded physical deletion. confidence: 1 source, last-confirmed 2026-10-23 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-23-rss-i-don-t-trust-on-delete-cascade.md)

### Explicit relationships

Deletion safety depends-on transaction bounds, complete relationships, and replication topology; soft deletion uses application visibility rules plus eventual physical cleanup. See [[distributed-systems-patterns]].

### Decision and quality notes

Practitioner database guidance, not a prohibition on every cascade or a tested migration. Soft deletion moves obligations to every read path, uniqueness, restoration, retention, and cleanup; it does not by itself fulfill data removal. Whole-database publication may expose more data and is not an automatic recommendation. No schema, retention rule, or record was changed. Source-specific claims remain provisional; repeated summaries add no independent support. Open question: Which deletion workflow tests cascade fan-out, foreign-key indexes, queued DDL, subscriber-only state, replica identity, soft-delete visibility, and bounded irreversible cleanup? See [[indexes/gaps]].
