---
source: "https://brooker.co.za/blog/2026/11/18/workload-mix.html"
title: "Traffic mix matters"
author: "Marc Brooker"
date_published: "2026-11-18"
date_clipped: "2026-11-20"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-11-20"
---

# Traffic mix matters

The [preliminary report on last week’s M365 outage](https://www.365fanatic.com/wp-content/uploads/2026/11/postincidentreport.pdf) contains one statement that really caught my eye:

Our normal load testing did not detect the latent issue because [of] the traffic mix and SKUs used in our labs.

There’s a lot going on in this report (as there is in any report for a complex system), but I wanted to zoom in on this one issue: *traffic mix*. It’s important, because its the one thing that makes the difference between a great load test and a complete waste of time.

The performance of computer systems is extremely sensitive to workload mix.

Let’s start with a simple simulator, looking at a system with a table of locks. Requests arrive with a key, hold the lock for their key for some period of time, and then free the lock and complete. This isn’t an unreasonable mental model of a relational database, where each transaction takes a lock during its execution.

Keys (N):

Each request takes one of 16 worker threads, waits in a FIFO queue for the lock on its key, holds the lock for an exponentially distributed time (mean 1 ms), then releases it and frees its thread. Keys are drawn from a Zipf distribution over N keys; a coefficient of 0 is uniform.

As we may expect, the more skewed the distribution, the less throughput you get out of the system. A small number of keys are highly contended, leading to under utilization of the rest of the resources of the machine, driven by the global concurrency limit.

Now, let’s consider a different mental model of a relational database (at least a single-system one like Postgres). A fast, local, in-memory cache containing some of the accessed data backed by a slower store containing the rest of the data.

Keys (N): Cache size: % of keys Cache is × faster than storage

Each request takes one of the same 16 worker threads and reads its key. A hit is served from an LRU cache; a miss goes to storage (exponentially distributed, mean 1 ms) and the key is added to the cache. Keys are drawn from a Zipf distribution over N keys; a coefficient of 0 is uniform. Note the log scale on the throughput axis.

This curve goes the other way! The more skewed the distribution, the better the performance, over something of a broad range. This is what makes it so important that workload mix in load tests and benchmarks matches real production traffic: throughput can vary by multiple orders of magnitude, in both directions, depending on things as subtle as key skew in the benchmark workload. This is especially true in relational database-shaped things, but applies to systems of all kinds.

**Aside**: This is also a reason I like optimistic concurrency control, and architectures with a single cost/latency *mode*. [Aurora DSQL](https://aws.amazon.com/rds/aurora/dsql/) reflects this thinking on how to make things less workload sensitive: all reads go to a single fast storage layer, and nobody is holding resources waiting on locks.
