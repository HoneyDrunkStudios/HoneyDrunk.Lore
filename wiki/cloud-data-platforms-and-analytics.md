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
