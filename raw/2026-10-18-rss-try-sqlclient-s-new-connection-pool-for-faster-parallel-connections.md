---
source: "https://devblogs.microsoft.com/azure-sql/try-sqlclients-new-connection-pool-for-faster-parallel-connections"
title: "Try SqlClient’s new connection pool for faster parallel connections"
author: "Malcolm Daigle"
date_published: "2026-10-06"
date_clipped: "2026-10-18"
category: ".NET Ecosystem"
source_type: "rss"
---

# Try SqlClient’s new connection pool for faster parallel connections

You told us that applications using `Microsoft.Data.SqlClient` can take too long to establish the database connections they need. When many requests need connections at the same time, waiting for the connection pool to grow can delay application readiness and increase latency. This can happen even in common situations like querying several pieces of metadata during startup or receiving a burst of traffic after a quiet period. `Microsoft.Data.SqlClient`’s new connection pool (Pool V2) is designed to address this problem by establishing new connections concurrently, allowing the pool to respond more quickly when multiple requests need new connections at the same time.

With the legacy connection pool, only one new connection can be opened at a time within a pool. Applications used to work around this limitation in creative ways, such as reserving capacity in advance by increasing `Min Pool Size` or disabling pooling altogether. These workarounds can now be entirely avoided.

Pool V2 is also designed with asynchronous workloads in mind. Its core design uses [System.Threading.Channels](https://learn.microsoft.com/en-us/dotnet/api/system.threading.channels) — a set of producer-consumer data structures with first-class asynchronous support — rather than relying on dedicated background threads. This can reduce thread management overhead for applications that connect to many different databases. Thanks to the Npgsql driver team, who paved the way for this pooling design.

## How does it perform?

We measured how quickly the legacy pool and Pool V2 could establish a set of connections during a cold start. Each test cleared the pool and then timed multiple concurrent callers opening and holding the same number of connections until all opens completed.

The measured time includes connection creation, synchronization, and returning connections to the pool. Pool clearing and test setup are excluded. The results represent the mean time for the complete operation, not the latency of an individual connection open. Lower times are better.

The tests used 10, 25, 50, and 100 concurrent callers with `Max Pool Size=200`. SQL Server ran on the same machine as the benchmark to reduce network variability. These benchmarks measure cold-start connection establishment and coordination. They do not measure SQL query execution or the reuse of connections in an already-warm pool. Results will vary based on workload and network latency.

### Synchronous cold-start results

With 100 concurrent callers on Linux, Pool V2 reduced mean cold-start benchmark time from 630.1 ms to 117.5 ms, a 5.4x speedup.

Synchronous callers use dedicated threads with `SqlConnection.Open()`. Each caller holds its connection until all opens complete. Lower times are better.

[![A graph showing improved cold start times on linux and windows.](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2026/10/01-cold-start-sync.svg)](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2026/10/01-cold-start-sync.svg)

### Asynchronous cold-start results

With 100 concurrent callers on Linux, Pool V2 reduced mean cold-start benchmark time from 604.1 ms to 92.0 ms, a 6.6x speedup.

Asynchronous callers use tasks with `SqlConnection.OpenAsync()`. Each caller holds its connection until all opens complete. Lower times are better.

[![A graph showing improved cold start times on linux and windows.](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2026/10/02-cold-start-async.svg)](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2026/10/02-cold-start-async.svg)

### Test environment

Linux: Ubuntu 22.04.5 LTS on a 16-core, 32-logical-CPU Intel Xeon Platinum 8168 VM, running SQL Server 2022 Developer CU26, .NET 9.0.19, and BenchmarkDotNet 0.15.8.

Windows: Windows Server 2022 Datacenter Azure Edition on a 16-core, 32-logical-CPU Intel Xeon Platinum 8168 VM, running SQL Server 2025 Enterprise Evaluation RTM, .NET 9.0.19, and BenchmarkDotNet 0.15.8.

The full benchmark source code is available in the [dotnet/SqlClient GitHub repository](https://github.com/dotnet/SqlClient).

### Current asynchronous I/O limitation

`SqlConnection.OpenAsync()` is not yet fully asynchronous down to each individual network call. Pool V2 currently queues work items on managed thread-pool threads that perform synchronous network calls. If those network calls experience high latency, the managed thread pool may experience elevated pressure. Waiting for additional threads to spin up can introduce end-user latency.

Applications with high latency to SQL Server should monitor managed thread-pool pressure. If necessary, consider increasing the managed thread-pool size or enforcing a concurrency limit on database operations. Future work will correct these network calls to eliminate the extra managed thread pool pressure.

## Try Pool V2 today

Pool V2 is available starting with `Microsoft.Data.SqlClient` 7.1.0. Enable it once during application startup, before any database connections are opened:

```
AppContext.SetSwitch(

    "Switch.Microsoft.Data.SqlClient.UseConnectionPoolV2", 

    true);
```

Place the switch at the beginning of your application’s entry point, before initializing services that might access the database. In an ASP.NET Core application, place it before creating the application builder.

That is the only code change required. Your existing connection strings and database-access code remain unchanged. Pool V2 also works with EF Core, Dapper, and other libraries that use `Microsoft.Data.SqlClient`.

Evaluate Pool V2 with a representative workload, particularly during:

* Application startup
* Traffic bursts after a quiet period
* High concurrent demand for database connections
* Higher-latency connections to SQL Server

To switch back, set the switch to `false` and restart the application.

We plan to make Pool V2 the default in a future `Microsoft.Data.SqlClient` version, and your experience can provide helpful feedback. Share your results through [dotnet/SqlClient GitHub Issues](https://github.com/dotnet/SqlClient/issues).
