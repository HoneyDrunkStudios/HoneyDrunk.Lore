---
"source": "https://devblogs.microsoft.com/azure-sql/diskann-vector-index-search-are-now-generally-available-in-azure-sql"
"title": "DiskANN Vector Index and Vector Search Are Now Generally Available in Azure\
  \ SQL"
"author": "Pooja Kamath"
"date_published": "2026-09-29"
"date_clipped": "2026-10-05"
"category": "Azure & Cloud"
"source_type": "rss"
---

# DiskANN Vector Index and Vector Search Are Now Generally Available in Azure SQL

Today, we are announcing the general availability of DiskANN Vector Index & Search across **Azure SQL Database**, **Azure SQL Managed Instance with the always-up-to-date update policy**, and **SQL database in Microsoft Fabric**.

[DiskANN](https://www.microsoft.com/en-us/research/project/project-akupara-approximate-nearest-neighbor-search-for-large-scale-semantic-search/) brings scalable approximate nearest-neighbor search directly to the SQL engine. Developers can store vectors alongside relational data and combine vector similarity with the filters, joins, security policies, and transactional data their applications already rely on.

## Why Vector indexes matter

Applications use embeddings to represent the semantic meaning of text, images, products, documents, and other content as vectors. Vector similarity search can then find results that are conceptually related to a user’s query, even when they do not contain the same keywords.

Without a vector index, exact vector search calculates the distance between the query vector and every qualifying vector. It must then identify and order the closest matches.

This approach can work well for smaller datasets or workloads that require exact results, but its computational cost increases as the number of vectors grows.


## Efficient similarity search with DiskANN

A DiskANN vector index provides an approximate nearest-neighbor search path designed to identify relevant candidates efficiently as the dataset grows.

Instead of evaluating every vector, the index builds a navigable graph so that the database engine can navigate toward the most promising candidates. This reduces the amount of work required to identify similar results while maintaining high search quality.

## Why is it called DiskANN?

The way I like to remember it – ANN means don’t search everything, and Disk means don’t keep everything in memory
More specifically the name **DiskANN** describes two important aspects of its design:

**ANN Approximate Nearest Neighbor:**The search does not compare the query vector with every vector in the dataset. Instead, it efficiently explores the index to identify likely nearest neighbors.**Disk:**DiskANN was designed so that large vector indexes don’t have to depend entirely on expensive RAM. It can use SSD-backed storage while maintaining a relatively small memory footprint, which is what helps it scale to massive datasets


## From preview to production

When we introduced DiskANN vector indexes in public preview, we invited customers to begin building vector-search applications directly on their operational data. Customer feedback helped shape the experience that is generally available today:

- DiskANN-based approximate nearest-neighbor search for large vector collections
- Full INSERT, UPDATE, and DELETE support, with asynchronous vector-index maintenance
- Iterative filtering to find the requested number of qualifying results while applying relational predicates
- Optimizer-driven execution, allowing SQL to choose between exact and approximate vector-search strategies based on the query context
- Composable T-SQL, so vector search works with existing filters, joins, business logic, and security controls

The result is vector search that behaves like part of SQL not a separate retrieval system that applications must operate and reconcile with their database. Read more [here](https://devblogs.microsoft.com/azure-sql/diskann-vector-index-improvements/)

## One query from development to production

Applications can express that approximate results are acceptable using **TOP (N) WITH APPROXIMATE**:

```
SELECT TOP (10) WITH APPROXIMATE
p.ProductId,
p.Name,
s.distance
FROM VECTOR_SEARCH(
TABLE = dbo.Products AS p,
COLUMN = Embedding,
SIMILAR_TO = @query_vector,
METRIC = 'cosine'
) AS s
WHERE p.IsActive = 1
ORDER BY s.distance;
```


The same query can continue to work as the application and its data grow. The optimizer evaluates the complete query including the data size, predicates, available indexes, and requested result count and selects an appropriate execution strategy.

Applications can therefore combine similarity search with familiar relational requirements, such as:

- Returning only products currently in stock
- Searching documents the current user is authorized to access
- Restricting recommendations by region or category
- Joining vector-search results with operational tables
- Applying existing row-level security policies

This allows developers to add semantic retrieval without giving up the relational and transactional capabilities already used by their applications. Read more [here](https://devblogs.microsoft.com/azure-sql/beyond-vector-indexes-azure-sql-brings-optimizer-intelligence-to-vector-search/)

## See the evolution of vector search

In a new Data Exposed episode, we trace how Azure SQL vector search evolved as customer applications moved from prototypes toward production. The episode also demonstrates vector search across one billion vectors in Azure SQL Database Hyperscale.

**Watch it here **

## Get started

Ready to add vector search to your application?
