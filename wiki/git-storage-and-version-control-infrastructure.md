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


## 2026-10-03: Git 2.54 adds limited history editing and configurable hooks

### Typed entities

person: Andrew Lock; library: Git 2.54; concept: git history; concept: configured hook; concept: repository statistics.

### Claims and evidence

Lock describes experimental history reword/split operations that avoid checking out the target branch, with merge-containing history unsupported. Config-defined hooks complement traditional hooks but do not become automatically trusted configuration on clone. Repository structure statistics expose object/reference counts, inflated sizes, and large objects. confidence: 1 source, last-confirmed 2026-10-03 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-03-rss-new-features-in-git-2-54-easier-rebasing-hooks-and-statistics.md)

### Explicit relationships

History editing rewrites descendant commits; hook adoption depends-on explicit local trust and configuration.

### Decision and quality notes

Secondary article published April 28 and captured October 3; later capture does not make it a newer release. A prose/command mismatch around hook listing should be checked against pinned Git documentation before use. No history-editing or hook commands were run. Source-specific claims remain provisional; related reports and derived queries add no independent confirmation. Open question: Which pinned Git versions and merge/history constraints qualify HoneyDrunk history tools and trusted hook installation? See [[indexes/gaps]].


## 2026-10-23: Scion trades offline symmetry for server-side source-control operations

### Typed entities

project: Anthropic; project: Scion; project: Antique; project: Git; project: Spanner; concept: changeset log; concept: content-addressed cache; concept: sparse checkout.

### Claims and evidence

- Anthropic describes Scion as a centralized system for its unusually large, mostly online agent/CI workload. Server-created changesets record changed files relative to the first parent and content-addressed blob references; derived structures answer history, blame, and ancestry queries. Ref updates use a separate compare-and-swap rather than coordinating every changeset through a global branch update. confidence: 1 source, last-confirmed 2026-10-23 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-21-rss-redesigning-source-control-at-anthropic.md)
- Clients fetch requested trees/blobs into bounded caches and sparse or virtualized working copies. Node, regional, and authoritative tiers expose the same object RPCs, while enforced tiering protects failure domains from cache-miss floods. CI can request metadata or make some writes through APIs without a full checkout. confidence: 1 source, last-confirmed 2026-10-23 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-21-rss-redesigning-source-control-at-anthropic.md)
- Reported infrastructure and checkout improvements compare Anthropic's own prior Git deployment and workload. The authors explicitly say Scion is unsuitable as a general Git replacement and requires bespoke review/search/CI migration. Their changed merge-queue/testing approach accepts concurrency conflicts in that environment; it is not evidence to remove HoneyDrunk review or required checks. confidence: 1 source, last-confirmed 2026-10-23 (complete archived capture reviewed; no live refresh). [captured source](../raw/2026-10-21-rss-redesigning-source-control-at-anthropic.md)

### Explicit relationships

Scion uses changeset logs and derived indexes; sparse checkout depends-on immutable object lookup; operational safety depends-on failure-domain isolation. See [[github-actions-platform-operations]] and [[ai-assisted-software-practice]].

### Decision and quality notes

First-party engineering case study, updated October 15, with no independent load or failure tests. Distinguish server-side operation patterns from the much larger product migration. Internal token availability and monorepo scale limit transferability; no alternative forge was selected or configured. Source-specific claims remain provisional single-source evidence; repeated reports and query outputs add no independent support. Open question: Which measured HoneyDrunk clone, metadata-query, and CI bottlenecks justify server-side caching or sparse access, and what failure/permission tests would precede any source-control architecture change? See [[indexes/gaps]].


## 2026-10-28: GitHub narrows serialization while separating durable storage and reads

### Typed entities

project: GitHub; project: Spokes; project: Azure Blob Storage; concept: per-reference serialization; concept: virtual replica; concept: read reconciliation.

### Claims and evidence

- GitHub describes a staged migration: first move repository replicas to Azure, then evolve storage. Per-reference serialization lets disjoint reference writes overlap instead of waiting behind one repository-wide lock; shared-reference contention and cross-region round trips remain. confidence: 1 source, last-confirmed 2026-10-28 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-28-rss-the-bridge-to-agent-scale-git-infrastructure.md)
- A virtual write replica streams changes to object storage and participates in durability acknowledgement, coalescing disjoint transactions. Virtual read replicas warm caches from object storage outside the write quorum. Background reconciliation initially supports only some reads; serving all reads requires inline freshness reconciliation. confidence: 1 source, last-confirmed 2026-10-28 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-28-rss-the-bridge-to-agent-scale-git-infrastructure.md)
- The reported 3-4x throughput improvement comes from GitHub's internal realistic-traffic tests. The bridge retains quorum limits and describes further redesign as upcoming, so it is neither a claim of unlimited writes nor proof that the final architecture is fully deployed. confidence: 1 source, last-confirmed 2026-10-28 (archived capture reviewed; no live refresh). [captured source](../raw/2026-10-28-rss-the-bridge-to-agent-scale-git-infrastructure.md)

### Explicit relationships

Disjoint writes use per-reference serialization; virtual reads depend-on object-store reconciliation; durable acknowledgement depends-on the virtual write replica. See [[distributed-systems-patterns]].

### Decision and quality notes

First-party engineering account published October 21. Architecture evidence is useful for evaluating coordination boundaries; reported traffic, migration percentages, and performance are dated vendor observations, not capacity targets for HoneyDrunk. Source-specific claims remain provisional; derived summaries add no independent support. Open question: Which workload requires stronger Git read/write scale, and what tests prove acknowledged-write durability, read freshness, same-reference contention, failover, and compaction behavior? See [[indexes/gaps]].

### Cross-source consolidation: separate durable state from serving work

The Cursor Continuity, Anthropic Scion, and GitHub Spokes accounts strengthen the architectural rationale for separating durable repository state from cache/serving work and narrowing coordination to the state that requires ordering. This is a compiler inference across different systems, not a shared implementation or replicated performance result. confidence: 3 sources, last-confirmed 2026-10-28; moderate support for the design pattern, provisional for transfer to HoneyDrunk. [Cursor capture](../raw/2026-08-21-rss-tldr-ai-git-at-any-scale-27-minute-read.md), [Anthropic capture](../raw/2026-10-21-rss-redesigning-source-control-at-anthropic.md), [GitHub capture](../raw/2026-10-28-rss-the-bridge-to-agent-scale-git-infrastructure.md).

Each account retains its own acknowledgement, read-freshness, failure, and migration boundaries. Different publishers provide broader design evidence, not three confirmations of any one throughput number. No source-control migration is selected by this synthesis.
