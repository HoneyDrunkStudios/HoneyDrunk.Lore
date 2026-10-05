---
"source": "https://devblogs.microsoft.com/azure-sql/data-api-builder-2-1-5-json-and-vector-data-type-support-and-more"
"title": "Data API builder 2.1.5: JSON and Vector Data Type Support, and More"
"author": "Carlos Robles, Aniruddh Munde, Matt Hyon"
"date_published": "2026-10-02"
"date_clipped": "2026-10-05"
"category": "Azure & Cloud"
"source_type": "rss"
---

# Data API builder 2.1.5: JSON and Vector Data Type Support, and More

Data API builder (DAB) 2.1.5 is now available as a stable release, and it is about meeting modern data where it lives: documents next to rows, embeddings next to both. This release brings native support for the SQL `json`

and `vector`

data types to the REST and GraphQL endpoints, so the same entities that serve your CRUD traffic can now store and expose document-shaped data and embeddings without custom code. It also introduces DAB as an embeddable NuGet library, hardens the MCP endpoint, moves the engine to .NET 10, and ships a set of security and reliability improvements.

Try it today and tell us what you think.

## What’s new in Data API builder 2.1.5

| Feature | Notes |
|---|---|
SQL `json` data type support |
Engine mapping, REST CRUD, OpenAPI and GraphQL coverage |
SQL `vector` data type support |
REST and GraphQL |
| Microsoft.DataApiBuilder.Core NuGet package | Embed the DAB engine in your own .NET app |
| Multi-segment runtime paths | `/api/v2` style base paths for REST and GraphQL |
| MCP endpoint hardening | Host/Origin allowlist, authorization improvements, health probe |
| Non-root container image | Dual image publishing for locked-down environments |
| .NET 10 runtime | Plus Microsoft.Data.SqlClient 6.x and Hot Chocolate 16.6.4 |

## JSON data type support

SQL Server’s native `json`

data type finally has a first-class path through your API. DAB 2.1.5 maps the type end to end: you can create, read, update, and delete rows with `json`

columns through REST, query them through GraphQL, and the generated OpenAPI description documents them correctly.

```
CREATE TABLE dbo.Products (
Id INT PRIMARY KEY,
Name NVARCHAR(100) NOT NULL,
Attributes JSON
);
```


Expose the table as an entity and the `Attributes`

column travels with it. On read, JSON column values are returned as serialized JSON strings. Clients can preserve the value as text or parse the string when they need structured access:

`GET /api/Products/Id/42`


```
{
"value": [
{
"Id": 42,
"Name": "Trailhead Tent",
"Attributes": "{\"capacity\": 2, \"season\": \"3-season\", \"weightKg\": 1.9}"
}
]
}
```


### Key highlights

- Full REST CRUD support for entities with
`json`

columns. - GraphQL and OpenAPI coverage, so generated schemas and API descriptions reflect the type accurately.
- Engine-level type mapping with clear error codes when a payload is not valid JSON.
- No configuration changes required: existing entities pick up the mapping when the column uses the
`json`

type.

## Vector data type support

Embeddings are how modern applications search by meaning, and the SQL `vector`

data type is how they live in the database. With 2.1.5, entities with `vector`

columns work through both REST and GraphQL, which means an AI application, or an AI agent, can read and write embeddings through the same secured, entity-scoped API it already uses for everything else.

```
CREATE TABLE dbo.Articles (
Id INT PRIMARY KEY,
Title NVARCHAR(200) NOT NULL,
Embedding VECTOR(1536)
);
```


```
query {
articles {
items {
Id
Title
Embedding
}
}
}
```


```
{
"data": {
"articles": {
"items": [
{
"Id": 1,
"Title": "DAB vector test article",
"Embedding": [
0.1,
0.2,
0.3,
0.4,
0,
...
0,
0,
0
]
}
]
}
}
}
```


### Key highlights

`vector`

columns are supported in REST and GraphQL read and write operations.- Works with the entity permission model, so access to embedding data is governed like any other column.
- Pairs with this release’s internal text embedding API and Redis-backed embedding cache for end-to-end embedding scenarios.

## Embed DAB in your own application

DAB has always been an engine you run. With the new **Microsoft.DataApiBuilder.Core** NuGet package, it is now also an engine you can reference. .NET developers can host DAB’s capabilities inside their own applications instead of running it as a separate process, which opens the door to custom hosts, tighter integration, and scenarios we frankly expect the community to surprise us with.

### Key highlights

- Reference the engine directly from a .NET application.
- Same configuration model and entity permissions you use today.
- Complements, rather than replaces, the existing container and CLI distributions.

## More flexible API paths

Runtime base paths for REST and GraphQL can now contain multiple segments, such as `/api/v2`

or `/data/api`

. If your organization versions its APIs in the path, or fronts DAB behind a gateway with path-based routing, the configuration now matches how you actually deploy.

## MCP endpoint hardening

The MCP endpoint in DAB continues to mature as a production surface for AI agents, and this release is focused on tightening its security posture:

- A configurable
**Host/Origin allowlist**controls which origins can reach the MCP endpoint. - Entity schema visibility through
`describe_entities`

is now gated by the caller’s role and permissions, so an agent sees only what its role allows. `create_record`

and`update_record`

now flow through the same authorization helper as the rest of the engine.- A dedicated MCP probe was added to the comprehensive health endpoint, so your monitoring can verify the endpoint is healthy alongside REST and GraphQL.

## Security and platform improvements

**.NET 10, Microsoft.Data.SqlClient 6.x, and Hot Chocolate 16.6.4.**The engine moves to the current runtime and driver generation, picking up their performance and security work.**Linux and macOS ARM64 NuGet packages.**Platform-specific packages now cover ARM64 environments on Linux and macOS.DAB now publishes a non-root image variant alongside the standard one, for Kubernetes and Azure Container Apps environments that require containers to run without root.[Non-root container image](https://mcr.microsoft.com/en-us/artifact/mar/azure-databases/data-api-builder/tag/latest-nonroot).**Stricter production validation for EasyAuth.**DAB refuses to start in production when EasyAuth providers are configured without the expected Azure environment signals, turning a silent misconfiguration into a clear startup error.**Configuration endpoint locked to loopback.**The`POST /configuration`

endpoint now accepts loopback connections only.**Column-level authorization for GraphQL**Sorting is now checked against column permissions, closing a gap where restricted columns could be used as sort keys.`orderBy`

.**Bounded GraphQL nested-filter recursion.**Nested filters now have a recursion-depth limit to prevent excessively deep filter expressions.**PostgreSQL improvements.**GraphQL grouping and aggregation, read-only array columns, DateTime filters, and database policy support for PUT and PATCH operations.

## Bug fixes

This release also resolves a set of correctness issues, including typed parameter binding for claim values in database authorization policies, MySQL row-level policy handling on PUT and PATCH, entity descriptions not appearing in GraphQL, column mapping in grouping and aggregation queries, a missing `WHERE`

clause in the DWSQL upsert update path, GraphQL aggregation when the `runtime.graphql`

section is absent, and a `SESSION_CONTEXT`

issue. The full list is in the [release notes](https://github.com/Azure/data-api-builder/releases/tag/v2.1.5).

## Conclusion

DAB 2.1.5 puts documents in `json`

columns, embeddings in `vector`

columns, and agents on the MCP endpoint behind one engine with one permission model and is available now.

**Try it:**grab the[v2.1.5 release](https://github.com/Azure/data-api-builder/releases/tag/v2.1.5)or pull the[latest container image](https://mcr.microsoft.com/en-us/artifact/mar/azure-databases/data-api-builder/tag/latest).**Read the docs:**[Data API builder documentation](https://aka.ms/dab/docs/).**Use it in VS Code:**the MSSQL extension for VS Code includes a built-in[Data API builder experience](https://aka.ms/vscode-mssql-dab-docs), introduced in the[March 2026 MSSQL extension release](https://devblogs.microsoft.com/azure-sql/vscode-mssql-march-2026/).**Tell us what you think:**open an issue or start a discussion in the[GitHub repository](https://github.com/Azure/data-api-builder).
