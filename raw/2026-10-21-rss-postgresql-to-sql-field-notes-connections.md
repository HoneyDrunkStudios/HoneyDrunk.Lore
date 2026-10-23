---
source: "https://devblogs.microsoft.com/azure-sql/pg-to-sql-connections/"
title: "PostgreSQL to SQL Field Notes: Connections"
author: "Jerry Nixon"
date_published: "2026-10-06"
date_clipped: "2026-10-21"
category: "Azure & Cloud"
source_type: "rss"
---

# PostgreSQL to SQL Field Notes: Connections

## Welcome to SQL

First, welcome to SQL! You’re going to like this.

Upgrading from PostgreSQL is real work, and depending on your old database, this process will vary widely in complexity. I am confident that you’re going to love the mindful and modern features of SQL. Take your time, make the most of the resources built to help you in Microsoft Learn, and know there is a huge community of SQL developers ready to help along the way.

[![database connections image](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2026/10/database-connections.webp)](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2026/10/database-connections.webp)

### This blog is for the PG developer

Good news! The SQL standard is shared across both engines; that should help you get up to speed quickly. However, there are differences, and there aren’t always equivalents. To help fast-track your learning, this series will highlight some differences worth knowing. Although some may surprise you, I believe most will be a delight.

SQL, in this article and elsewhere in Microsoft documentation, means T-SQL (Transact-SQL), Microsoft’s variant of the SQL standard shared across all Microsoft SQL database engines. In the Microsoft SQL world, T-SQL is referred to simply as SQL.

## PostgreSQL connections

**Let’s start with the prerequisite of prerequisites:** *connecting to the database*. A user or system attempting to interact with any database must first connect.

```
using Npgsql;


using var connection = new NpgsqlConnection(connectionString);

connection.Open();


// Use the connection
```

This C# snippet makes it look easy to create a connection to a PostgreSQL database. It is! But there’s a lot you’ve had to pay attention to, too. Let’s talk through the high-level concerns you’ve had to manage.

## Unfortunately, you already know the caveat

In PostgreSQL, developers always have connection management on their minds. This is because PostgreSQL uses one operating-system process per connection, making connections relatively expensive.

### 1) PostgreSQL connections are expensive

PostgreSQL connections are dedicated backend processes with private memory and execution state, plus OS scheduling and context-switching overhead. It’s a lot, and there’s a practical ceiling on the number of connections a server can handle before performance starts degrading.

> **Processor + Memory + Overhead = Connection Cost**

This isn’t just theory. PostgreSQL’s own documentation says the default `max_connections` is typically only 100. Increasing it also causes PostgreSQL to allocate more resources, including shared memory. PostgreSQL is designed around the idea that connections are a resource you manage carefully.

### 2) PostgreSQL connections must be managed

A long-lived PostgreSQL connection isn’t necessarily a problem, but a lot of them can become a problem quickly. Idle connections still consume resources, while idle transactions trigger bigger concerns.

You’ve probably used `pg_stat_activity` for this. It’s a built-in PostgreSQL system view used to monitor sessions, their state, current queries, and transaction duration to identify connections that are `active`, `idle`, or, most importantly, `idle in transaction`.

```
SELECT *

FROM pg_stat_activity;
```

You might also deploy PgBouncer, the popular PostgreSQL connection pooler, to reduce the number of physical connections reaching the server.

You will certainly already know commands like these for ongoing management of problematic connections:

- `pg_cancel_backend()`
- `pg_terminate_backend()`

**All of this is really a matter of constant vigilance**

All of this is really a matter of constant vigilance to ensure connections are properly managed and idle transactions do not accumulate. You can fire-and-forget your databases, but as reliability and scale start to dominate the conversation, you will pay far more attention to connection and transaction management.

### Preventing connection exhaustion

We also know that PostgreSQL connection limits are cluster-wide, not database-level. Each connection corresponds to a separate backend process, and **the server’s finite capacity matters**. When you move a database, the connection calculus must account for all the other databases on that server.

**Think about that for a moment**

The typical PostgreSQL default is 100 concurrent connections, and those connections are shared across its databases. PostgreSQL lets you raise that limit, of course, but raising it increases resource requirements.

---

**Spoiler alert:** SQL’s connection limit is more than *32 thousand*!

### PostgreSQL behavior forces developer behavior

Unfortunately, app developers designing apps and agents must account for the cost and limitations of PostgreSQL connections in their architecture and code. Generally, this translates to limiting concurrent connections and keeping transactions short.

Long-running transactions can retain old row versions, interfere with VACUUM cleanup, increase table bloat, and contribute to transaction ID wraparound pressure.

Consequently, PostgreSQL’s connection model dictates quite a bit of how developers must design and manage their applications, particularly in terms of connection handling and transaction management. When your app needs to break out of the box, you often must introduce additional strategies that can increase maintenance costs.

## Great news! You’re using SQL now.

**Things are different in Microsoft SQL, especially with connections.** The biggest difference is that we manage connections and sessions in a way that generally eliminates the need to worry about exhausting server resources simply from their quantity and duration. Idle connections are comparatively inexpensive and generally aren’t an architectural concern.

[![database connections sql image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABogAAAOtAQMAAACISHVKAAAAA1BMVEXW1taWrGEgAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA1UlEQVR4nO3BAQEAAACCIP+vbkhAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwZQQXAAEOBMAVAAAAAElFTkSuQmCC)](https://devblogs.microsoft.com/azure-sql/wp-content/uploads/sites/56/2026/10/database-connections-sql.webp)

### Microsoft SQL uses a worker-based architecture.

A connection does not require a dedicated operating-system process. Instead, Microsoft SQL assigns workers to execute work as needed. Connection pooling is also typically handled automatically by *ADO.NET*, making it easier to scale applications without intricate connection management strategies.

```
using Microsoft.Data.SqlClient;


using var connection = new SqlConnection(connectionString);

connection.Open();


// Use the connection
```

Like the PostgreSQL sample above, this C# code makes connecting to SQL look simple. It is! But unlike the PostgreSQL example, the app generally does not need to worry about exhausting server resources simply because connections remain open or idle. Not at all. You just connect and go.

### Flexible resource assignment

A SQL connection is a physical connection to the logical server. **Unlike PostgreSQL, it is not mapped one-to-one with a separate operating-system process** or dedicated worker for its lifetime. Instead, workers are assigned when requests need to execute, then returned for use by other requests. As a result, idle connections consume relatively few server resources.

#### Microsoft SQL does it for you:

1. Microsoft SQL supports up to 32,767 simultaneous user connections per instance.
2. Microsoft SQL also supports up to 32,767 databases per instance.
3. Each connection does not equate to a proportional increase in server resource consumption.
4. Connection pooling further mitigates the overhead of establishing new physical connections.
5. Applications can safely open and close connections at the pace that is right for the app.

**Yes, you read those first two numbers correctly**

32,767 connections and 32,767 databases. Of course, actual practical capacity depends on workload, hardware, service tier, and other resources. But the architectural difference should be clear. SQL is not designed around a small pool of dedicated backend processes.

### Here’s how it works

Because Microsoft SQL manages workers and resources across connections, it reduces the need for manual resource management, monitoring, and allocation. In fact, most applications should rely on SQL and the client connection pool to do this efficiently. **Manually managing connection counts without a specific reason is generally an antipattern.**

Like PostgreSQL, SQL has connections and sessions. However, Microsoft SQL does not dedicate a separate backend process to each connection. This separation helps disassociate connection count from resource consumption.

As a session begins executing work, Microsoft SQL dynamically assigns the workers and memory necessary to perform that work. As the work completes, those resources can be released for use by other sessions. A connection can remain open without unnecessarily tying up a dedicated process or worker.

### You can still have control

All the management views you would want to see and manage connections are still there for you.

```
SELECT *

FROM sys.dm_exec_sessions

WHERE is_user_process = 1;
```

And you can ask SQL directly how many simultaneous user connections the instance supports:

```
SELECT @@MAX_CONNECTIONS AS MaxConnections;
```

On a normally configured SQL instance, the answer is:

```
32767
```

If you need to terminate a session, use `KILL` with the session ID:

```
KILL <session_id>;
```

#### This is your new default

Monitoring connections and killing sessions should generally be a last resort in Microsoft SQL, not a regular connection-management strategy. It’s far easier and ultimately more effective to rely on SQL and connection pooling to handle most scenarios for your application.

**One less headache, one less maintenance task, one less ongoing cost to worry about.**

Just like any database, when you have a lot of data and a lot of query activity, it still makes sense to monitor resource usage to ensure optimal performance. SQL doesn’t make resources infinite. It simply gives you a connection architecture where idle connections don’t require dedicated server processes.

## Congratulations

**Let me welcome you again to SQL!** I hope it’s clear that you’ve joined a rich and thoughtful ecosystem.

Scaling connections isn’t just different, it’s better. Your application can choose the connection and transaction patterns that are best for your application, rather than designing around the database’s connection architecture. That sort of freedom helps you build better. And that’s a big win for everyone!

Happy querying!
