# Azure Service Bus and Azure Functions Messaging

## Decision-useful summary
Azure Functions batch processing for Azure Service Bus now has a clearer production pattern: use batch cardinality for throughput, disable automatic completion, settle each message independently, and combine application-level exponential backoff with a dependency-level circuit breaker when downstream services degrade. For HoneyDrunk queue workers, this is a strong candidate pattern when throughput matters, messages have mixed failure modes, and serverless scale could amplify retry storms. [sources: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md; raw/2026-05-16-rss-azure-blog-exponential-backoff-and-circuit-breaker-for-service-bus-tri.md]

## Claims
- Azure Functions Service Bus triggers in batch mode can suffer an all-or-nothing failure mode where one failed message causes the entire batch to be retried, duplicating successful work and increasing cost/idempotency burden. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md]
- Per-message settlement lets a single function invocation complete successful messages, abandon transient failures, dead-letter poison messages, or defer messages requiring later retrieval by sequence number. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md]
- In Node.js/TypeScript, the source says manual settlement requires Service Bus SDK bindings, `autoCompleteMessages: false`, `cardinality: 'many'`, and settlement actions such as `complete`, `abandon`, `deadletter`, and `defer`. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md]
- Python V2 functions and .NET isolated worker functions also expose batch messages plus message-action APIs for per-message completion/dead-letter/abandon behavior. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md]
- Exponential backoff answers when to retry a failed message, while a circuit breaker answers whether the function should call an unhealthy downstream dependency at all. Used together, they reduce retry storms, downstream overload, and queue churn. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-exponential-backoff-and-circuit-breaker-for-service-bus-tri.md]
- Azure Functions Service Bus retry scheduling can copy message metadata, increment retry count in application properties, schedule a future message, complete the current message, and dead-letter/quarantine after a maximum retry budget. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-exponential-backoff-and-circuit-breaker-for-service-bus-tri.md]
- Production circuit breaker state for Azure Functions should live in shared state such as Azure Managed Redis or Cosmos DB rather than per-process memory, because Functions can scale out across instances. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-azure-blog-exponential-backoff-and-circuit-breaker-for-service-bus-tri.md]

## Typed entities
- service: Azure Service Bus
- platform: Azure Functions
- feature: Service Bus trigger batch mode
- feature: per-message settlement
- pattern: exponential backoff
- pattern: circuit breaker
- concept: dead-letter queue
- concept: quarantine queue
- service: Azure Managed Redis
- service: Cosmos DB
- action: complete
- action: abandon
- action: dead-letter
- action: defer
- library: `@azure/functions-extensions-servicebus`
- library/API: `ServiceBusMessageActions`
- file: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md
- file: raw/2026-05-16-rss-azure-blog-exponential-backoff-and-circuit-breaker-for-service-bus-tri.md

## Explicit relationships
- Azure Functions uses Service Bus triggers to process Azure Service Bus messages.
- Service Bus batch mode depends-on idempotent consumers when automatic all-or-nothing retry behavior is used.
- Per-message settlement supersedes all-or-nothing batch retry for mixed-success batches when manual settlement is enabled.
- `abandon` can be used with application properties to implement retry/backoff metadata without separate infrastructure.
- Exponential backoff uses Service Bus scheduled messages to delay retries and reduce synchronized dependency pressure.
- Circuit breaker state depends-on shared storage for scale-out Functions apps.
- DLQ and quarantine queues are alternative failed-message paths; DLQ fits broker-owned failure handling, while quarantine fits application-owned inspection/replay workflows.
- [[Microsoft .NET AI Stack]] may use Azure Functions hosting for durable workflows; queue-triggered work should apply the same failure-isolation discipline when backed by Service Bus.

## HoneyDrunk implications
- For queue workers that process independent items, prefer batch + per-message settlement over single-message invocations or whole-batch failure semantics.
- Do not relax idempotency entirely: settlement reduces duplicate redelivery for completed messages, but crashes, lock loss, and downstream retries still require safe handlers.
- Dead-letter malformed messages quickly; reserve abandon/retry for transient failures with explicit retry metadata.
- Add jitter and max retry budgets before using Functions scale-out against weak downstream dependencies.
- If a breaker is needed, design shared state and operator dashboards at the same time as retry code; in-memory state is not enough beyond demos.

## Confidence and quality notes
- Quality posture: decision-usable for Azure Functions/Service Bus implementation scouting; verify package/API names against current docs before coding.
- Weak spots: source is vendor-authored and example-heavy.
- Privacy filter: no credentials or private payload examples copied.
