# Azure SDK for Rust

## Decision-useful summary
Azure SDK for Rust reached a stable production-ready milestone in May 2026 for core Azure identity, Key Vault, and Storage workloads. This makes Rust a more credible option for small, low-memory, high-throughput Azure services, containers, and edge agents when the needed service coverage fits the stable crates. Missing coverage such as Event Hubs and Cosmos DB remains roadmap-dependent. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md]

superseded-by: [October Cosmos DB stability](#2026-11-01-cosmos-db-rust-stability-supersedes-the-earlier-roadmap-constraint); timestamp: 2026-11-01T09:05:10-05:00; reason: the newer Microsoft release explicitly lists Cosmos DB Rust 1.0.0 stable. Only the Cosmos roadmap restriction is superseded; the earlier statement and Event Hubs uncertainty are retained.


## Claims
- Azure SDK for Rust is stable with production-ready APIs, semver guarantees, and stable crates for Core, Identity, Key Vault Secrets/Keys/Certificates, Storage Blobs, and Storage Queues. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md]
- The stable Rust SDK includes unified core primitives such as a redesigned `Pager`, awaitable `Poller`, `ManagedIdentityCredential`, and `DeveloperToolsCredential` that can fall through local developer tools like Azure CLI and Azure Developer CLI. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md]
- The SDK includes automatic retries on transient failures, challenge-based authentication for sovereign/private cloud scenarios, distributed tracing through `azure_core_opentelemetry`, and HTTP logging that sanitizes secrets by default. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md]
- Event Hubs (`azure_messaging_eventhubs` and blob checkpoint store) and Cosmos DB (`azure_data_cosmos`) were not part of the stable wave but were described as priority/active development targets, with Cosmos DB expected in 2026. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md]

superseded-by: [October Cosmos DB stability](#2026-11-01-cosmos-db-rust-stability-supersedes-the-earlier-roadmap-constraint); timestamp: 2026-11-01T09:05:10-05:00; reason: the newer Microsoft release explicitly lists Cosmos DB Rust 1.0.0 stable. Only the Cosmos roadmap restriction is superseded; the earlier statement and Event Hubs uncertainty are retained.


## Typed entities
- SDK: Azure SDK for Rust
- crate: `azure_core`
- crate: `azure_identity`
- crate: `azure_security_keyvault_secrets`
- crate: `azure_security_keyvault_keys`
- crate: `azure_security_keyvault_certificates`
- crate: `azure_storage_blob`
- crate: `azure_storage_queue`
- planned crate: `azure_messaging_eventhubs`
- planned crate: `azure_messaging_eventhubs_checkpointstore_blob`
- planned crate: `azure_data_cosmos`
- credential: `DeveloperToolsCredential`
- credential: `ManagedIdentityCredential`
- library: `azure_core_opentelemetry`
- runtime: Tokio
- file: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md

## Explicit relationships
- Azure SDK for Rust uses Tokio by default and supports pluggable async runtimes.
- `DeveloperToolsCredential` uses installed developer tools to acquire local-development tokens.
- `ManagedIdentityCredential` supersedes local developer credentials for workloads running in Azure.
- Azure SDK for Rust depends-on stable crate coverage; Event Hubs and Cosmos DB support remain roadmap constraints.

superseded-by: [October Cosmos DB stability](#2026-11-01-cosmos-db-rust-stability-supersedes-the-earlier-roadmap-constraint); timestamp: 2026-11-01T09:05:10-05:00; reason: the newer Microsoft release explicitly lists Cosmos DB Rust 1.0.0 stable. Only the Cosmos roadmap restriction is superseded; the earlier statement and Event Hubs uncertainty are retained.

- [[azure-agent-automation-and-identity]] and Rust Azure services share identity/credential concerns around Entra ID and managed identity.

## HoneyDrunk implications
- Consider Rust for Azure queue/blob/key-vault workers only when the stable crate set covers the workload.
- Prefer managed identity in deployed Rust services; keep developer-tool credentials local only.
- Do not plan Event Hubs/Cosmos Rust production work until the relevant crates reach the needed maturity.

superseded-by: [October Cosmos DB stability](#2026-11-01-cosmos-db-rust-stability-supersedes-the-earlier-roadmap-constraint); timestamp: 2026-11-01T09:05:10-05:00; reason: the newer Microsoft release explicitly lists Cosmos DB Rust 1.0.0 stable. Only the Cosmos roadmap restriction is superseded; the earlier statement and Event Hubs uncertainty are retained.


## Confidence and quality notes
- Quality posture: decision-usable for language/runtime scouting and service-coverage checks.
- Weak spots: vendor-authored release announcement; validate crate versions/docs and sovereign-cloud behavior before production.
- Privacy filter: sample URLs/placeholders retained only as public/example patterns; no credentials copied.

## 2026-06-23 compile additions

### Source-backed claims
- Azure SDK May 2026 confirms Azure SDK for Rust 1.0.0 GA across Core, Core AMQP, Core OpenTelemetry, Identity, Storage Blob/Queue, and Key Vault Secrets/Keys/Certificates crates. Source: `raw/2026-06-23-rss-azure-blog-azure-sdk-release-may-2026.md`; page: [[microsoft-dotnet-ai-stack]]. confidence: 1 Microsoft Azure SDK release source, last-confirmed 2026-06-23.

### Typed entities
- crate: Azure Core
- crate: Azure Core AMQP
- crate: Azure Core OpenTelemetry
- crate: Azure Identity
- crate: Azure Storage Blob
- crate: Azure Storage Queue
- crate: Azure Key Vault Secrets
- crate: Azure Key Vault Keys
- crate: Azure Key Vault Certificates

### Explicit relationships
- Azure SDK for Rust now has GA coverage for the storage, identity, telemetry, AMQP core, and Key Vault primitives named in the May 2026 release.

### HoneyDrunk implications
- Re-evaluate Rust Azure worker feasibility for Blob, Queue, Key Vault, and telemetry tasks where earlier crate maturity was the blocker.

### Quality notes
- Microsoft release-source claim. Verify exact crate names, semver, and service gaps before implementation.

## 2026-08-12 compile additions: storage SAS crate

### Source-backed claims
- Azure SDK July 2026 release notes announced Rust `azure_storage_sas` 0.1.0 as an initial stable release for building service SAS and user-delegation SAS values for Azure Storage Blob, Queue, and related storage services. Source: `raw/2026-08-12-rss-azure-blog-azure-sdk-release-july-2026.md`. confidence: 1 Microsoft Azure SDK release source, last-confirmed 2026-08-12.
- The source frames user-delegation SAS as a way to grant scoped, time-limited storage access without sharing account keys. Source: `raw/2026-08-12-rss-azure-blog-azure-sdk-release-july-2026.md`; page: [[azure-agent-automation-and-identity]]. confidence: 1 source, last-confirmed 2026-08-12.

### Typed entities
- crate: `azure_storage_sas`
- credential pattern: user-delegation SAS
- service: Azure Storage Blob
- service: Azure Storage Queue
- secret type: storage account key

### Explicit relationships
- User-delegation SAS complements managed identity and Entra-backed storage access by narrowing delegated storage permissions and time windows.
- `azure_storage_sas` depends-on the rest of the Rust Azure storage/identity stack when used in production workers.

### HoneyDrunk implications
- For Rust storage tooling, prefer user-delegation SAS over account-key distribution when a short-lived delegated link is the right access model.
- Review SAS generation code for scope, expiry, clock skew, logging, and accidental token persistence before automation emits links.

### Quality notes
- Microsoft release notes are authoritative for package existence. Validate crate docs and storage-service support before implementation.


## 2026-11-01: Cosmos DB Rust stability supersedes the earlier roadmap constraint

### Typed entities

library: azure_data_cosmos; library: azure_data_cosmos_driver; library: azure_data_cosmos_macros; concept: stable release; concept: preview migration. file: raw/2026-10-31-rss-azure-sdk-release-october-2026.md.

### Claims and evidence

- Microsoft lists Cosmos DB 1.0.0 as the first stable Rust release alongside the driver and macro crates. Preview users must rename selected preview feature flags to unstable equivalents and replace MasterKey with AccountKey; selected terminal service errors map to synthetic 503 with the wire error retained as source. confidence: 1 source, last-confirmed 2026-11-01 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-31-rss-azure-sdk-release-october-2026.md)

### Explicit relationships

The October release supersedes the May Cosmos DB roadmap status; migration depends-on exact crate/features and error handling. No Event Hubs graduation is inferred.

### Decision and quality notes

Official release roundup. Its initial-beta table also lists beta.1 versions of the same crates; the explicit 1.0.0 highlight/stable section establishes the newer milestone. Stability is not a HoneyDrunk adoption or complete service-coverage claim. Source-specific claims remain provisional; repeated accounts and derived queries add no independent support.
