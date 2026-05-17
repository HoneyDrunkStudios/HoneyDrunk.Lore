# Query: 2026-05-17 Daily Platform, Runtime, and Source-Quality Signal

## Durable facts crystallized
- Azure Functions Service Bus consumers should combine per-message settlement with exponential backoff and circuit breakers when downstream dependencies degrade; production breaker state needs shared storage, not only in-memory state. [source: raw/2026-05-16-rss-azure-blog-exponential-backoff-and-circuit-breaker-for-service-bus-tri.md; wiki: ../wiki/azure-service-bus-and-functions-messaging.md]
- Azure SDK for Rust is stable for Core, Identity, Key Vault, Blob Storage, and Queue Storage, but Event Hubs and Cosmos DB remain roadmap constraints. [source: raw/2026-05-16-rss-azure-blog-from-beta-to-stable-announcing-the-azure-sdk-for-rust.md; wiki: ../wiki/azure-sdk-for-rust.md]
- GitHub Actions now supports larger concurrency-group queues (`queue: max`) and has June 2026 runner image migrations for Windows/Visual Studio and `macos-latest`; pin/test production workflows before defaults move. [sources: raw/2026-05-16-rss-github-changelog-actions-github-actions-concurrency-groups-now-allow-l.md; raw/2026-05-16-rss-github-changelog-actions-github-actions-upcoming-image-migrations.md; wiki: ../wiki/github-actions-platform-operations.md]
- .NET 11 preview changes are relevant to harnesses and mobile scouting: MAUI moves to CoreCLR by default, and Process APIs add deadlock-free capture plus child-process lifetime controls. [sources: raw/2026-05-16-rss-net-blog-net-maui-moves-to-coreclr-in-net-11.md; raw/2026-05-16-rss-net-blog-process-api-improvements-in-net-11.md; wiki: ../wiki/dotnet-runtime-and-mobile-2026.md]
- TLDR AI/DevOps/InfoSec and Rundown AI captures on 2026-05-16/17 mostly reinforced extraction/privacy-filter gaps rather than adding title-level facts. [wiki: ../wiki/browser-snapshot-source-quality.md]

## Decision implications
- Audit Service Bus consumers for retry storms, shared breaker state, jitter, DLQ/quarantine, and observable retry metadata.
- Pin/test GitHub runner labels before June migrations and use larger concurrency queues only where stale pending runs must not be canceled.
- Treat .NET 11 runtime/process APIs as scout-now/adopt-after-GA unless a prototype specifically needs them.
- Fix TLDR/Rundown extraction before using those feeds as substantive evidence.

## Confidence
Medium-high for vendor platform/runtime facts; implementation details need current docs and local validation. High confidence that the new TLDR/Rundown captures are low-yield/noisy; low confidence for their title-level claims because raw bodies did not contain the article/news item text.
