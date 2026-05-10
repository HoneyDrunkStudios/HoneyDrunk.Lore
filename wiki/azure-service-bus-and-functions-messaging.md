# Azure Service Bus and Azure Functions Messaging

## Decision-useful summary
Azure Functions batch processing for Azure Service Bus now has a clearer production pattern: use batch cardinality for throughput, disable automatic completion, and settle each message independently so one poison/transient failure does not replay an entire successful batch. For HoneyDrunk queue workers, this is a strong candidate pattern when throughput matters and messages have mixed failure modes. [source: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md]

## Claims
- Azure Functions Service Bus triggers in batch mode can suffer an all-or-nothing failure mode where one failed message causes the entire batch to be retried, duplicating successful work and increasing cost/idempotency burden. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md]
- Per-message settlement lets a single function invocation complete successful messages, abandon transient failures, dead-letter poison messages, or defer messages requiring later retrieval by sequence number. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md]
- In Node.js/TypeScript, the source says manual settlement requires Service Bus SDK bindings, `autoCompleteMessages: false`, `cardinality: 'many'`, and settlement actions such as `complete`, `abandon`, `deadletter`, and `defer`. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md]
- Python V2 functions and .NET isolated worker functions also expose batch messages plus message-action APIs for per-message completion/dead-letter/abandon behavior. confidence: 1 source, last-confirmed 2026-05-10. [source: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md]

## Typed entities
- service: Azure Service Bus
- platform: Azure Functions
- feature: Service Bus trigger batch mode
- feature: per-message settlement
- action: complete
- action: abandon
- action: dead-letter
- action: defer
- library: `@azure/functions-extensions-servicebus`
- library/API: `ServiceBusMessageActions`
- file: raw/2026-05-10-rss-azure-blog-the-problem-all-or-nothing-batch-processing-in-azure-servic.md

## Explicit relationships
- Azure Functions uses Service Bus triggers to process Azure Service Bus messages.
- Service Bus batch mode depends-on idempotent consumers when automatic all-or-nothing retry behavior is used.
- Per-message settlement supersedes all-or-nothing batch retry for mixed-success batches when manual settlement is enabled.
- `abandon` can be used with application properties to implement retry/backoff metadata without separate infrastructure.
- [[Microsoft .NET AI Stack]] may use Azure Functions hosting for durable workflows; queue-triggered work should apply the same failure-isolation discipline when backed by Service Bus.

## HoneyDrunk implications
- For queue workers that process independent items, prefer batch + per-message settlement over single-message invocations or whole-batch failure semantics.
- Do not relax idempotency entirely: settlement reduces duplicate redelivery for completed messages, but crashes, lock loss, and downstream retries still require safe handlers.
- Dead-letter malformed messages quickly; reserve abandon/retry for transient failures with explicit retry metadata.

## Confidence and quality notes
- Quality posture: decision-usable for Azure Functions/Service Bus implementation scouting; verify package/API names against current docs before coding.
- Weak spots: source is vendor-authored and example-heavy.
- Privacy filter: no credentials or private payload examples copied.
