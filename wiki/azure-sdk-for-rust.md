# Azure SDK for Rust

## Decision-useful summary
Azure SDK for Rust reached a stable production-ready milestone in May 2026 for core Azure identity, Key Vault, and Storage workloads. This makes Rust a more credible option for small, low-memory, high-throughput Azure services, containers, and edge agents when the needed service coverage fits the stable crates. Missing coverage such as Event Hubs and Cosmos DB remains roadmap-dependent. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md]

## Claims
- Azure SDK for Rust is stable with production-ready APIs, semver guarantees, and stable crates for Core, Identity, Key Vault Secrets/Keys/Certificates, Storage Blobs, and Storage Queues. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md]
- The stable Rust SDK includes unified core primitives such as a redesigned `Pager`, awaitable `Poller`, `ManagedIdentityCredential`, and `DeveloperToolsCredential` that can fall through local developer tools like Azure CLI and Azure Developer CLI. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md]
- The SDK includes automatic retries on transient failures, challenge-based authentication for sovereign/private cloud scenarios, distributed tracing through `azure_core_opentelemetry`, and HTTP logging that sanitizes secrets by default. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md]
- Event Hubs (`azure_messaging_eventhubs` and blob checkpoint store) and Cosmos DB (`azure_data_cosmos`) were not part of the stable wave but were described as priority/active development targets, with Cosmos DB expected in 2026. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md]

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
- [[azure-agent-automation-and-identity]] and Rust Azure services share identity/credential concerns around Entra ID and managed identity.

## HoneyDrunk implications
- Consider Rust for Azure queue/blob/key-vault workers only when the stable crate set covers the workload.
- Prefer managed identity in deployed Rust services; keep developer-tool credentials local only.
- Do not plan Event Hubs/Cosmos Rust production work until the relevant crates reach the needed maturity.

## Confidence and quality notes
- Quality posture: decision-usable for language/runtime scouting and service-coverage checks.
- Weak spots: vendor-authored release announcement; validate crate versions/docs and sovereign-cloud behavior before production.
- Privacy filter: sample URLs/placeholders retained only as public/example patterns; no credentials copied.
