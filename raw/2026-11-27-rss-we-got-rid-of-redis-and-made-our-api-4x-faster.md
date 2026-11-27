---
source: "https://useautumn.com/blog/moving-credit-deductions-off-redis-and-onto-kafka"
title: "We got rid of Redis and made our API 4x faster"
author: "Autumn; Owen"
date_published: "2026-11-25"
date_clipped: "2026-11-27"
category: "Software Architecture"
source_type: "rss"
discovered_via: "https://tldr.tech/dev/2026-11-26"
---

# We got rid of Redis and made our API 4x faster

This month, we switched off the Redis store that held our credit balances. We handle roughly 430 million API requests a day at Autumn (a number that is growing quickly). And until this month, the majority of them went through Redis. We spent quite a lot of time fixing bugs in that setup. What convinced us to make the move was spending a Sunday rebuilding a cache that had been inadvertently deleted by our Redis provider.

## How we ended up here

Redis was originally chosen because of how fast it is, and how easy it is to make deduction atomic with Lua. The deduction would be applied in Redis and flushed to Postgres later. This gave us fast writes without updating Postgres on every request.

The problem was that during this window between Redis apply and flush to the db, race conditions are possible in multiple scenarios. For example, a customer uses 30 credits and then gets a grant before the flush. A grant would clear the cache and rebuild from Postgres meaning that usage of 30 credits would be lost.

We fixed this case in September. In 4 months we shipped around 50 Redis-related fixes. At one point I had scoped out every possible race condition and upon seeing how many there were, it was hard to see myself ever getting to the end of the list. Having more than one source of truth is fundamentally flawed.

## Losing the cache

On Sunday 26 July, our Redis provider upgraded our datastore to fix a CPU issue. The new version had a bug and the primary and replica both crashed. Because of this we lost 40 GB of cached balances and most of our API requests failed until we could resolve this.

The rest of the day was spent warming a fresh cache from Postgres as using a backup would've rolled balances back too far.

After this, and seeing the list of possible race conditions, we understood we had to rip out Redis.

## Building the balance workers

The solution that was agreed upon after a lot of discussion and load testing a few options was a set of processes we call 'balance workers'. How this works is:

- Each customer is hashed into one of a set of Kafka partitions
- One balance worker 'owns' each partition at a time
- When the API gets a check or track request, it sends it to the worker that owns the customer partition
- The worker keeps the customer's balances in memory, works out the deduction and then writes the mutation to Kafka

Postgres catches up in batches from the Kafka log, therefore Kafka becomes the sole source of truth (acknowledges aren't returned from the API until the Kafka commit is successful).

## What happens if a worker goes away

Every deploy can move partitions around, so when this happens the incoming worker replays the Kafka log from where Postgres left off while the existing worker is still serving. On takeover we fence off the old worker so it can't keep writing to Kafka. The new worker also warms the balances the old worker had in its own memory (which happens on every deploy, and doesn't need the full team spending a Sunday to do).

The balance worker design also gracefully handles network jitter to Kafka, or general Kafka stalls. If an append to the log is waiting after a certain amount of time, we send the command to SQS and acknowledge the API request. This is called the spool and adds another layer of durability while retaining the single source of truth design.

All healthy

## How it performed

A comparison of a week of API traffic on Redis and the balance workers after full rollout.

| Metric | Redis + Lua (14–21 Sep) | Balance workers (13–20 Nov) | Change |
| --- | --- | --- | --- |
| Track p50 | 30 ms | 10 ms | 3× faster |
| Track p99 | 108 ms | 25 ms | 4.3× faster |
| Check p50 | 11 ms | 3 ms | 3.7× faster |
| Check p99 | 77 ms | 54 ms | 1.4× faster |
| Busiest second of tracks | 5,393 | 7,548 | 40% more |
| Check + track requests that week | 1.8B | 2.3B | 28% more |

The workers handled 28% more check and track requests, and track latency dropped from 30 ms → 10 ms at the median and 108 ms → 25 ms at the tail. Checks also got slightly faster.

## What it cost

This architecture isn't a complete win - we had to give up a few things. Now that every customer has a single writer, each customer's requests are handled one after another rather than concurrently. So if a customer sends a massive burst, it queues behind itself. This is a deliberate trade as ordering per customer is the whole point, and overall latency is still well below the Redis + Lua setup.

The log is now in the hot path - we don't acknowledge tracks until Kafka (or the spool) has it, so if Kafka is slow then track accepts are slow. That's why I built the spool.

There is more to run - partition ownership, worker fencing, safe deploy handoffs and a committer that keeps Postgres caught up from the log are all mechanisms a single Redis call never needed. This is more complex to operate, but the robustness and reliability more than pays for it.

## What it opened up

Now that every balance change is saved as an ordered log of events, other services are able to follow it rather than simply reading from Postgres or from a cache. This enabled us to build a service for sending usage events and webhooks off the back of the log, metering/enforcing usage within a customers own cloud, and a full history of how each customer's balance changed over time. None of these would've been possible with balances sitting in a Redis cache.

## Looking back

The latency improvement was great to see but the change I care about most is what now happens when we tell a customer we have accepted a track. Kafka or SQS has the command, so we have something to replay that we can't lose on worker death. Giving every customer a single writer made the behaviour of balances predictable and easy to explain.
