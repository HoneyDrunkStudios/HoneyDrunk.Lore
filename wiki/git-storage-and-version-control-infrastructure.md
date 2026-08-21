# Git Storage and Version Control Infrastructure

## Purpose

This page tracks architecture patterns for hosting Git repositories and version-control infrastructure at agent scale, especially where repository traffic, CI fan-out, and autonomous coding agents change storage and consistency requirements.

## 2026-08-21 compile additions: WAL-backed Git hosting at agent scale

### Source-backed claims
- Cursor's "Git at Any Scale" source argues that hosting Git at scale is hard because packfiles and Git's content-addressed DAG create random logical and physical read patterns that behave poorly on network filesystems and naive object-level distributed stores. Source: `raw/2026-08-21-rss-tldr-ai-git-at-any-scale-27-minute-read.md`. confidence: 1 primary-via-TLDR engineering source, last-confirmed 2026-08-21.
- The source says GitHub-style Spokes architectures store normal Git repositories on local NVMe disks and replicate packfile/reference transactions consistently, but three-phase commit creates a high replica floor for tiny repositories and tail-latency limits for large monorepos. Source: `raw/2026-08-21-rss-tldr-ai-git-at-any-scale-27-minute-read.md`. confidence: 1 source, last-confirmed 2026-08-21.
- Cursor describes Continuity as a WAL-first Git storage system where pushed packfiles are persisted to S3-compatible object storage before acknowledgement, pushes are linearized through a WAL index compare-and-swap, local repositories act as warm caches, and replicas verify freshness against object-store ETags before serving reads. Source: `raw/2026-08-21-rss-tldr-ai-git-at-any-scale-27-minute-read.md`. confidence: 1 source, last-confirmed 2026-08-21.
- The source reports that Continuity uses rendezvous hashing for healthy-path routing, allows any server to act as primary under failover, replicates through best-effort gossip with object-store freshness checks, and compacts on the primary so replicas can download compacted packs instead of independently repacking. Source: `raw/2026-08-21-rss-tldr-ai-git-at-any-scale-27-minute-read.md`; page: [[distributed-systems-patterns]]. confidence: 1 source, last-confirmed 2026-08-21.
- Cursor reports synthetic tests up to 100 replicas with linear read scaling, all clones fully consistent, all pushes persisted externally before acknowledgement, and push-throughput figures tied to S3 Standard or S3 Express One Zone latency; treat the performance numbers as vendor/product evidence until independently reproduced. Source: `raw/2026-08-21-rss-tldr-ai-git-at-any-scale-27-minute-read.md`. confidence: 1 vendor/product engineering source, last-confirmed 2026-08-21.

### Typed entities
- system/pattern: Git hosting
- storage format: Git packfile
- data model: content-addressed DAG
- architecture: Spokes
- architecture/product: Cursor Continuity
- product/platform: Cursor Origin
- primitive: write-ahead log / WAL
- storage service: S3-compatible object storage
- control: atomic compare-and-swap / CAS
- routing method: rendezvous hashing
- consistency mechanism: ETag freshness check
- protocol: gossip replication
- storage medium: local NVMe disk
- coordination algorithm: three-phase commit / 3PC

### Explicit relationships
- Git hosting depends-on normal Git protocol compatibility because clients still exchange packfiles even if the server stores data differently.
- Local NVMe Git repositories complement object-store durability by keeping ordinary Git operations fast while treating disk copies as rebuildable caches.
- WAL-backed object storage supersedes repository-location databases as the source of truth in Continuity's design.
- Gossip replication complements strong object-store freshness checks: gossip accelerates catch-up, while ETag verification preserves consistency when packets are lost.
- Three-phase commit consensus contradicts unlimited replica fan-out because slow replicas cap push throughput at scale.

### HoneyDrunk implications
- Agent-driven coding increases pressure on Git infrastructure through many small repositories, more PRs, and CI clone/fetch fan-out; treat version-control capacity as part of agent-platform design, not only developer tooling.
- If HoneyDrunk evaluates alternate Git hosting or agent sandbox repository storage, ask how pushes are durably acknowledged, how reads stay consistent, how repositories recover from corruption, and how compaction affects availability.
- Do not copy performance claims into capacity plans without local load tests that include HoneyDrunk repo sizes, CI clone patterns, branch churn, and agent-created throwaway repositories.

### Quality notes
- Source is Cursor-authored engineering/product material. The architecture mechanisms are decision-useful, but performance and product-readiness claims should be independently validated before procurement or migration decisions.
