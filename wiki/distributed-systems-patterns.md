# Distributed Systems Patterns

## Decision-useful summary
Gossip protocol is a useful distributed-systems pattern when large clusters need highly available, decentralized membership, failure detection, dissemination, or aggregation and can tolerate eventual/probabilistic consistency. It is not a generic replacement for strongly consistent coordination systems: network partitions, non-determinism, duplicated messages, and malicious nodes still require design controls. [source: raw/2026-06-04-web-high-scalability-gossip-protocol-explained-high-scalability.md]

## Claims
- Gossip protocol is a decentralized peer-to-peer communication technique where nodes periodically exchange state with a random subset of peers; over rounds, information reaches the whole system with high probability. confidence: 1 architecture explainer source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-high-scalability-gossip-protocol-explained-high-scalability.md]
- Gossip is commonly used for cluster membership, failure detection, database replication, information dissemination, aggregation, overlay networks, and leader-election support in systems that favor availability and eventual consistency. confidence: 1 architecture explainer source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-high-scalability-gossip-protocol-explained-high-scalability.md]
- Broadcast alternatives have different costs: point-to-point broadcast is simple but loses messages when producer and consumer fail together; eager reliable broadcast improves fault tolerance but can require O(n^2) messages; gossip bounds per-node load by spreading messages probabilistically over rounds. confidence: 1 architecture explainer source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-high-scalability-gossip-protocol-explained-high-scalability.md]
- Gossip variants include anti-entropy for replica repair, rumor-mongering/dissemination for recent updates, and aggregation for system-wide values; push, pull, and push-pull strategies trade bandwidth, latency, and convergence behavior. confidence: 1 architecture explainer source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-high-scalability-gossip-protocol-explained-high-scalability.md]
- Gossip's practical caveats include eventual consistency, partition unawareness, duplicate/bandwidth overhead, latency until the next round, debugging/testing difficulty, and corruption risk from malicious nodes unless data is authenticated or self-verifying. confidence: 1 architecture explainer source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-high-scalability-gossip-protocol-explained-high-scalability.md]

## Typed entities
- concept: gossip protocol
- concept: epidemic protocol
- concept: anti-entropy gossip
- concept: rumor-mongering gossip
- concept: aggregation gossip
- strategy: push model
- strategy: pull model
- strategy: push-pull model
- concept: fanout
- concept: gossip cycle
- data structure: Merkle tree
- system: Apache Cassandra
- system: Consul
- system: CockroachDB
- system: Riak
- system: Amazon Dynamo
- system: Redis Cluster
- system: Bitcoin
- coordination service: Apache ZooKeeper

## Explicit relationships
- Gossip protocol uses random peer selection and periodic state exchange to build a global view from local interactions.
- Anti-entropy gossip uses checksums, recent update lists, or Merkle trees to reduce replica differences without transferring full datasets every time.
- Gossip failure detection depends-on multiple nodes observing heartbeat/version changes rather than one client declaring failure.
- Gossip protocol complements strong coordination services when availability and scale matter more than immediate consistency.
- Malicious-node risk contradicts using unauthenticated gossip for security-sensitive state.

## HoneyDrunk implications
- Consider gossip for local agent/worker presence, health, or low-stakes telemetry where eventual convergence is acceptable and central coordination would be fragile or overbuilt.
- Do not use gossip alone for money, authority, secrets, permissions, or irreversible state. Those need stronger consistency, authenticated messages, and audit.
- If OpenClaw/Grid ever uses peer membership, define fanout, interval, state size, authentication, partition behavior, and observability before implementation.

## Confidence and quality notes
- Quality posture: useful as a stable architecture primer. The source is an explainer, not a primary paper or implementation manual.
- Weak spots: exact performance examples are secondary and should be validated in any HoneyDrunk implementation.
- Privacy filter: no private data or unsafe implementation payloads copied.

## 2026-06-29 compile additions: near-real-time fan reaction aggregation

### Source-backed claims
- High Scalability's Hotstar emoji architecture source describes a social-feed feature that ingested billions of fan emoji reactions, buffered low-latency HTTP submissions into Kafka-backed infrastructure, computed aggregates with Spark micro-batches, and delivered normalized top emoji streams to clients through PubSub. Source: `raw/2026-06-29-rss-high-scalability-capturing-a-billion-emo-j-i-ons.md`. confidence: 1 architecture case-study source, last-confirmed 2026-06-29.
- The source says Hotstar chose asynchronous write-to-buffer behavior for the emoji path because rare data loss was acceptable relative to latency, while noting synchronous writes are preferable when data is transactional or cannot tolerate loss. Source: `raw/2026-06-29-rss-high-scalability-capturing-a-billion-emo-j-i-ons.md`. confidence: 1 source, last-confirmed 2026-06-29.
- Hotstar reports the infrastructure later generalized from emoji swarms to voting, polls, and trivia contests because the shared problem was processing quantifiable user responses in near real time. Source: `raw/2026-06-29-rss-high-scalability-capturing-a-billion-emo-j-i-ons.md`. confidence: 1 source, last-confirmed 2026-06-29.

### Typed entities
- company/product: Hotstar
- system: Social Feed Emojis
- system: PubSub
- platform: Kafka
- platform: Spark Streaming
- language/runtime: Go
- concept: micro-batching
- concept: asynchronous ingestion
- feature: voting

### Explicit relationships
- Low-latency social reaction systems can trade rare data loss for responsiveness when the data is aggregate sentiment rather than transactional state.
- Kafka-backed ingestion complements Spark micro-batching when aggregate windows are small but not necessarily per-event synchronous.
- Voting, polls, trivia, and emoji reactions share a reusable pattern: collect quantifiable user responses, aggregate them over short windows, and broadcast summarized state.

### HoneyDrunk implications
- For audience/live-event features, decide up front whether each event is telemetry, sentiment, vote, purchase, or authority-bearing state; the allowed loss and consistency model differ.
- Do not copy the asynchronous loss-tolerant pattern into billing, auth, inventory, or moderation decisions.

### Quality notes
- Architecture case study is useful pattern evidence but older than the clip date; implementation details should be revalidated against current platform choices.

## 2026-08-17 compile additions: common system-design scaling patterns

### Source-backed claims
- System Design Newsletter describes cache-aside as a read-performance pattern where the application checks an in-memory cache before querying the database, populating cache entries on misses for data that can tolerate staleness. Source: `raw/2026-08-17-rss-system-design-newsletter-10-system-design-solutions-explained-in-15-mi.md`. confidence: 1 newsletter/explainer source, last-confirmed 2026-08-17.
- The same source frames read replicas as a read-scaling pattern where writes go to the primary database and acceptable eventually consistent reads are routed to replicas, with read-after-write operations kept on the primary when freshness is required. Source: `raw/2026-08-17-rss-system-design-newsletter-10-system-design-solutions-explained-in-15-mi.md`. confidence: 1 source, last-confirmed 2026-08-17.
- The source describes sharding as a write-scaling pattern that distributes records across database nodes by partition key, increasing write capacity but making resharding, cross-shard queries, hot partitions, and partition-key changes operationally expensive. Source: `raw/2026-08-17-rss-system-design-newsletter-10-system-design-solutions-explained-in-15-mi.md`. confidence: 1 source, last-confirmed 2026-08-17.
- The source describes message queues as an asynchronous buffering pattern where producers enqueue work and consumers process at their own pace, absorbing bursts and decoupling services but requiring idempotent consumers, dead-letter handling, queue-depth monitoring, and user-facing async status semantics. Source: `raw/2026-08-17-rss-system-design-newsletter-10-system-design-solutions-explained-in-15-mi.md`. confidence: 1 source, last-confirmed 2026-08-17.

### Typed entities
- pattern: cache-aside
- pattern: read replica
- pattern: database sharding
- pattern: message queue
- concept: Time-to-Live / TTL
- concept: read-after-write consistency
- concept: partition key
- concept: hot partition
- control: idempotent consumer
- control: dead-letter queue
- metric: queue depth

### Explicit relationships
- Cache-aside uses TTL and application-controlled population to trade freshness and memory cost for lower read latency.
- Read replicas complement primary databases when reads can tolerate replication lag.
- Read-after-write freshness contradicts blind replica routing immediately after writes.
- Sharding depends-on partition-key quality; bad keys cause hot partitions and expensive repartitioning.
- Message queues decouple producers and consumers but shift completion semantics from synchronous response to asynchronous state.

### HoneyDrunk implications
- For each HoneyDrunk service, classify the scaling bottleneck before choosing a pattern: repeated reads, high read volume, high write volume, or bursty asynchronous work.
- Do not introduce sharding until partition keys, cross-shard query requirements, resharding cost, and hot-key monitoring are understood.
- Require idempotency and dead-letter handling before queueing customer-impacting work.

### Quality notes
- The source is a concise newsletter primer and only exposes the first five sections of a paid article. Use it as basic architecture reinforcement, not as implementation guidance.

## 2026-08-21 compile additions: durable workflows and Git storage consistency

### Source-backed claims
- System Design Newsletter's durable-agent source reinforces that queues and workflows solve different problems: queues retry work delivery, while durable workflows remember completed steps, waits, retries, and what must happen next. Source: `raw/2026-08-21-rss-system-design-newsletter-how-to-build-ai-agents-that-don-t-start-over-.md`; page: [[ai-agent-harnesses]]. confidence: 1 newsletter/practitioner source, last-confirmed 2026-08-21.
- Cursor's Git storage source describes a WAL-backed object-store design where S3-compatible storage is the durable source of truth, local Git repositories are warm caches, and ETag freshness checks preserve read consistency even when gossip replication hints are lost. Source: `raw/2026-08-21-rss-tldr-ai-git-at-any-scale-27-minute-read.md`; page: [[git-storage-and-version-control-infrastructure]]. confidence: 1 primary-via-TLDR engineering source, last-confirmed 2026-08-21.

### Typed entities
- pattern: durable workflow
- pattern: checkpointing
- pattern: write-ahead log / WAL
- storage service: S3-compatible object storage
- consistency control: ETag freshness check
- routing method: rendezvous hashing
- replication mechanism: gossip

### Explicit relationships
- Durable workflows supersede simple whole-job retries when prior steps are expensive, nondeterministic, or side-effecting.
- Object-store WALs can complement local cache replicas when the source of truth must be durable, linearizable, and recoverable.
- Gossip replication depends-on a stronger freshness check when clients require consistent reads.

### HoneyDrunk implications
- Use queues for independent, idempotent background jobs; use durable workflow semantics when a run must survive waits, partial progress, or side effects.
- Treat gossip as an accelerator or health/membership mechanism, not a source of truth for security-sensitive or consistency-sensitive state.

### Quality notes
- Both sources are practitioner/product evidence. Validate exact platform semantics before adopting a durable workflow or WAL-backed storage design.

## 2026-08-23 compile additions: retry storms and sidecar capacity

### Source-backed claims
- GitHub's 2026-08-17 incident report shows optimistic gateway/client retries can amplify a partial service failure into a much larger load event, including Copilot Token Service traffic rising from normal 7-9K RPS to 70-100K RPS. Source: `raw/2026-08-23-rss-tldr-devops-github-com-incident-5-minute-read.md`; page: [[github-actions-platform-operations]]. confidence: 1 GitHub Status incident report, last-confirmed 2026-08-23.
- The same incident shows service-mesh sidecar concurrency can be the binding capacity limit when autoscaling policy observes host service limits but not sidecar limits. Source: `raw/2026-08-23-rss-tldr-devops-github-com-incident-5-minute-read.md`. confidence: 1 source, last-confirmed 2026-08-23.

### Typed entities
- failure mode: retry storm
- component: Istio sidecar
- component: HAProxy
- service: Copilot Token Service
- control: retry budget
- control: backoff
- control: sidecar-aware autoscaling

### Explicit relationships
- Retry policy depends-on budgets, jitter, backoff, and client behavior; retries without limits can worsen the outage they try to mask.
- Autoscaling depends-on all constrained components in the request path, including sidecars and gateways, not only application pods.
- Incident recovery may require deliberately reducing or rejecting selected traffic before gradually ramping back to steady state.

### HoneyDrunk implications
- For HoneyDrunk services and agents, define retry budgets and backoff for token/auth/tool calls instead of letting clients loop indefinitely.
- If service mesh is introduced, include sidecar metrics in autoscaling and load tests before production rollout.

### Quality notes
- GitHub incident report is strong postmortem evidence for the pattern. Apply the lesson, not the exact GitHub topology, unless HoneyDrunk uses comparable components.

## 2026-09-14: Retry identity across workflow restarts

### Typed entities

project: n8n; concept: idempotency key; concept: business operation identity; concept: webhook deduplication.

### Claims and evidence

- The n8n capture distinguishes a workflow execution ID, stable for retries within that run, from a durable business operation ID needed across restarts or retriggers. It describes persisted webhook-delivery deduplication, bounded retries, and failure handling; downstream deduplication support is still required. confidence: 1 source, last-confirmed 2026-09-14 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-13-rss-n8n-blog-how-to-build-reliable-workflows-with-api-idempotency.md)

### Explicit relationships

Retry-safe side effects depends-on stable operation identity and receiving-end deduplication; automatic retries alone do not establish idempotency.

### Decision and quality notes

One vendor explanation refines the existing durable-workflow guidance. Define operation identity and separate delivery/run/side-effect boundaries before implementing retries. Source count is provisional single-source support; repeated citations and derived summaries add no independent corroboration. Open question: Which workflows can restart or retrigger the same business operation, and where are stable keys, atomic deduplication records, retention, and downstream retry guarantees enforced? See [[indexes/gaps]].

## 2026-09-15: Choosing workflow execution by recovery needs

### Typed entities

project: n8n; concept: orchestration; concept: choreography; concept: compensating action; concept: execution history.

### Claims and evidence

- n8n contrasts predefined, feedback-driven, and agent-assisted execution. Central orchestration coordinates state and dependencies while choreography distributes reactions; long processes, human handoffs, and complex recovery can justify coordination overhead. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-n8n-process-orchestration-models.md)
- Its production concerns include bottlenecks, partial completion, schema changes, and cross-service debugging. Proposed responses include event-oriented execution, compensation, versioned schemas, and correlation-rich history. Compensation is not a database rollback, and history alone does not prove recovery correctness. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-n8n-process-orchestration-models.md)

### Explicit relationships

Execution-model choice depends-on state, retries, failure isolation, and observability. Agent-assisted decisions use a larger controlled workflow; choreography uses distributed event reactions.

### Decision and quality notes

Vendor architecture guidance, not a formal guarantee. Simple pipelines may not benefit from extra coordination; recovery needs validation independently of editor choice. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which workflows justify central orchestration, and what partial-completion, compensation, schema-version, and correlation tests demonstrate recovery correctness? See [[indexes/gaps]].


## 2026-09-19: Outbound pacing and inbound admission are separate controls

### Typed entities

project: n8n; concept: token bucket; concept: sliding window; concept: retry pacing; concept: inbound traffic admission.

### Claims and evidence

- The n8n guide contrasts token buckets, leaky buckets, fixed windows, and sliding windows by burst tolerance, steady processing, reset spikes, and state complexity. It proposes batching, explicit cache refresh, and pacing retries using 429 responses and Retry-After information. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-rss-api-rate-limiting-workflow-design.md)
- The captured guide describes retry settings, loops, waits, and explicit exhausted-retry failure paths, while saying exposed n8n webhooks lack built-in inbound rate limiting and need a gateway or reverse proxy for that protection. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-rss-api-rate-limiting-workflow-design.md)

### Explicit relationships

Reliable outbound work depends-on provider quotas and bounded retries; inbound admission uses a separate gateway control. Retry pacing complements operation-identity guidance above.

### Decision and quality notes

Vendor workflow guidance. No current n8n installation or provider quota was verified, and retry settings alone do not establish idempotency. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which Lore providers require shared quota budgets, Retry-After handling, cache refresh, and exhausted-retry reporting, and which exposed workflows need inbound gateway limits? See [[indexes/gaps]].


## 2026-09-19: Outbox durability depends on relay and consumer contracts

### Typed entities

project: n8n; concept: transactional outbox; concept: relay; concept: change-data capture; concept: idempotent consumer.

### Claims and evidence

- n8n describes recording business state and the outbox event in one database transaction so the publication obligation survives the dual-write failure. A relay publishes committed records, retries transient failures, and marks records processed only after successful delivery; polling trades simplicity against CDC infrastructure and latency. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-transactional-outbox-relay-contract.md)
- The operational contract includes consumer idempotency for duplicate delivery, stalled-row alerts, processed-record retention/archival, and ordering where required. Atomic recording does not itself prove eventual delivery if the relay stops or failures remain hidden. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-transactional-outbox-relay-contract.md)

### Explicit relationships

Durable publication uses atomic outbox recording; delivery depends-on an operating relay and visible failure handling. Correct consumer effects depend-on idempotency and required ordering.

### Decision and quality notes

Vendor architecture guidance. Strong delivery wording in the title does not establish exactly-once processing or progress through permanent infrastructure failure. This extends existing retry-identity and recovery guidance without adding a guarantee. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which business events need atomic outbox recording, and how will HoneyDrunk test relay restart, duplicate delivery, ordering, stalled-row alerts, and retention without losing publication obligations? See [[indexes/gaps]].


## 2026-09-22: Definition restoration and execution replay are separate guarantees

### Typed entities

project: n8n; project: Temporal; concept: workflow definition; concept: execution history; concept: environment promotion; concept: restoration test.

### Claims and evidence

- n8n describes JSON workflow snapshots containing nodes, connections, and configuration without execution history or usable credential secrets. The article contrasts definition history with Temporal execution-history compatibility: recovering a definition does not establish safe replay of an existing execution. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-workflow-definition-versioning-boundaries.md)
- The guide separates development, staging, and protected production, with Git review and visual/JSON inspection before synchronization. Pulling can overwrite unpushed edits rather than merge them. Community exports are backups requiring restoration tests, not equivalent to the described paid native environment workflow. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-workflow-definition-versioning-boundaries.md)

### Explicit relationships

Definition recovery uses versioned configuration; execution recovery depends-on runtime history and compatible code. Environment promotion uses reviewed snapshots.

### Decision and quality notes

Vendor architecture guidance; current plan availability was not checked. Secret-free exports can still expose internal structure. Test recovery guarantees independently of successful Git checkout. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent support. Open question: Which workflow definitions, credentials, runtime histories, and compatible code must be restored together, and how will promotion prevent overwriting unpushed local changes? See [[indexes/gaps]].


## 2026-09-22: Latency improvements depend on the measured dependency graph

### Typed entities

project: n8n; concept: critical path; concept: bounded retry; concept: queue contention; concept: prompt-prefix cache; concept: answer cache.

### Claims and evidence

- n8n separates inference, external-tool, and orchestration delay. Independent requests can overlap while dependent work awaits inputs; timeouts and bounded retries protect the end-to-end response budget. Sub-workflow isolation does not make an external service faster. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-workflow-latency-critical-path-design.md)
- Concurrency limits and worker queues address load contention; routing and output limits target inference. Prompt-prefix caching reduces repeated input processing, while an appropriate answer-cache hit can avoid inference. Illustrative timing targets and vendor claims are not service guarantees. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-20-rss-workflow-latency-critical-path-design.md)

### Explicit relationships

Latency budgeting uses dependency traces; parallel execution depends-on input independence. Cache selection depends-on which processing can safely be reused. See [[opentelemetry-genai-observability-and-ecosystem]].

### Decision and quality notes

Vendor design guidance with workload-specific timing. Measure critical-path and queue behavior before choosing parallelism, isolation, cache policy, or model size. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent support. Open question: Which inference, tool, queue, and orchestration spans dominate HoneyDrunk workflow latency, and what retry budgets and cache-validity rules preserve correctness under load? See [[indexes/gaps]].


## 2026-09-22: Architecture comparisons need explicit workload and recovery assumptions

### Typed entities

person: Neo Kim; concept: task queue; concept: retained event log; concept: per-key ordering; concept: CQRS; concept: recovery objective.

### Claims and evidence

- Kim organizes fifty comparisons around latency, throughput, consistency, durability, cost, and recovery. Messaging distinctions include task distribution versus retained logs, global versus per-key ordering, and duplicate delivery versus stronger processing guarantees. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-22-rss-system-design-workload-tradeoff-checklist.md)
- The guide connects deployment autonomy to coordination overhead, CQRS/event sourcing to synchronization work, retries to load amplification, large queues to stale work, and stronger recovery goals to replication/testing cost. These are design heuristics, not implementation guarantees. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-22-rss-system-design-workload-tradeoff-checklist.md)

### Explicit relationships

Architecture selection depends-on workload assumptions and failure recovery. Ordering and delivery choices affect parallelism, replay, coordination, and idempotency.

### Decision and quality notes

Practitioner taxonomy. Use it as review prompts, then verify selected queue/database/runtime contracts and operational costs. Existing outbox and retry boundaries remain applicable. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent support. Open question: Which workload, ordering, replay, consistency, queue-age, and recovery assumptions justify each HoneyDrunk service boundary and messaging choice, and how are their costs verified? See [[indexes/gaps]].


## 2026-09-26: Local worker backpressure bounds concurrency without a shared coordinator

### Typed entities

project: Canva; concept: worker concurrency; concept: feedback controller; concept: backoff factor; concept: queue age.

### Claims and evidence

- Canva describes a worker-local feedback controller that lowers concurrency when processing failures exceed a configured set point. Outcomes update a backoff factor used to limit polling permits, leaving work queued instead of repeatedly calling an unhealthy dependency; this design needs no external coordinator. confidence: 1 source, last-confirmed 2026-09-26 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-24-rss-queue-worker-local-backpressure-tradeoffs.md)
- Two production incidents illustrate reduced dead-letter accumulation, but estimates for an unprotected fleet are counterfactual. Lower throughput and a simple success/failure signal are tradeoffs; recovery from complete backoff and tuning details are deferred to a later installment. confidence: 1 source, last-confirmed 2026-09-26 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-24-rss-queue-worker-local-backpressure-tradeoffs.md)

### Explicit relationships

Polling concurrency uses local outcome feedback; acceptance depends-on queue age, throughput, and recovery behavior as well as errors. This complements [[azure-service-bus-and-functions-messaging]]: a local concurrency controller does not establish shared circuit-breaker state across scaled Functions instances.

### Decision and quality notes

Firsthand engineering account with incomplete controller/recovery detail. The coordinator-free controller does not contradict the older scoped shared-breaker recommendation; these are different control contracts. No ready-to-copy algorithm or HoneyDrunk incident saving is inferred. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent confirmation of these details. Open question: Which HoneyDrunk worker failure signals and concurrency limits preserve queue-age objectives, and how will a local controller recover from complete backoff without masking persistent failure? See [[indexes/gaps]].
