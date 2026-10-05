---
"source": "https://thenewstack.io/when-to-use-graph-rag"
"title": "Use Graph RAG when relationships are part of the evidence"
"author": "Jeremy Daly"
"date_published": "2026-10-01"
"date_clipped": "2026-10-05"
"category": "Software Architecture"
"source_type": "rss"
---

# Use Graph RAG when relationships are part of the evidence

# Use Graph RAG when relationships are part of the evidence

[Oracle](https://www.oracle.com?utm_content=sponsor+disclosure)sponsored this post.

Which team owns the service that depends on the vulnerable library? Which customers use that service, and what does each customer’s contract require you to tell them?

A vector search can return the security advisory and service description, along with an ownership page or notification policy. Each result may be relevant. The answer may still lack the context needed to establish the correct relationship.

The missing evidence is in the connections. A particular version of the service uses the library. That service supports a particular customer environment. The contract in force for that customer defines a notification window. If the agent has to infer those relationships from a handful of similar passages, it may not have enough evidence to distinguish the relevant relationships from similar but unrelated ones.

“Use it when the relationships among facts are part of the evidence behind the answer.”


This is where [Graph RAG](https://thenewstack.io/graphrag-multi-hop-reasoning-python/) justifies the additional work it requires. Use it when the relationships among facts are part of the evidence behind the answer. Keep vector retrieval because it remains very good at finding the documents and records that matter. Add a graph when similarity alone can’t prove why one fact applies to another.

## Where vector retrieval works best

Vector retrieval finds text or records whose meaning is similar to a question, even when they use different words. A query about “ending a subscription” can find a support article about “account cancellation.” A question about memory eviction can find a paper that calls the same idea “context pruning.”

That makes [vector search](https://thenewstack.io/how-to-store-embeddings-in-vector-search-and-implement-rag/) a good default for a large class of RAG applications. Documentation, support articles, product descriptions, and other unstructured knowledge often contain answers in one or two passages. The data is mostly text, the question has a limited scope, and the application doesn’t need to prove a path between several business records.

Similarity has a defined job in that design: rank likely evidence. It doesn’t establish ownership, dependency, authorization, or policy scope. Two records can be semantically close and have no operational connection. Another pair can be directly connected while sharing almost no language.

“A similarity score is an opinion about relevance, while a tenant boundary, effective date, or account identifier is a condition the system must enforce.”


This is why hard metadata constraints must be enforced independently of vector ranking. A similarity score is an opinion about relevance, while a tenant boundary, effective date, or account identifier is a condition the system must enforce. Relationships deserve the same distinction when the question depends on them.

## Questions that depend on relationships

Questions about connected systems appear everywhere once an agent moves beyond a self-contained knowledge base:

- Which services depend on this component?
- Who can approve an exception for this account?
- Which customers are affected by this deployment?
- Which controls apply to the data in this environment?

Consider the vulnerability example. A package advisory identifies a library. A deployment record says a service uses that library. A service catalog connects the service to a customer environment. A contract record connects that customer to a notification policy. The answer requires four records and three relationships between them.

Text can describe every step, but an agent assembling the chain implicitly can join the vulnerable library to an unintended service version or associate a shared service with the wrong customer. It can also retrieve a policy that expired last month or miss a dependency updated in the service catalog after the documentation was published.

A graph makes those connections explicit by turning each record into a node. Typed, directed edges can record that a service `USES`

a library or `SUPPORTS`

an environment. A `GOVERNED_BY`

edge ties the contract to the policy. Each connection carries its source and owner, with confidence scores or effective dates added when those details matter.

Start with the relationship types that answer an important question. Mapping the whole company is a long detour with no guarantee of a useful destination.

## Graph RAG adds relationship evidence

Graph RAG is an overloaded term. Microsoft’s [GraphRAG](https://microsoft.github.io/graphrag/) uses an LLM to extract a knowledge graph from unstructured text, builds a community hierarchy, and supports both corpus-level and entity-focused queries. This article means something narrower: a graph built from relationships your systems already record, where every edge traces to an operational source rather than being inferred from a model’s interpretation of the documents.

The approach combines content retrieval with traversal over known relationships. One practical flow begins by finding candidate entities and passages for the question. The application resolves those candidates to specific records, follows only the permitted relationships, and then retrieves the source documents needed to explain the result. That resolution step is the hardest part of the flow. A question about “the payments service” has to land on the right record when the catalog lists three services with similar names, and an incorrect match can affect every hop that follows. When the match is ambiguous, the application should surface the candidates rather than pick the closest name.

“The graph answers ‘What is connected?’ The source material answers ‘What does the policy say?’ You need both.”


The graph answers “What is connected?” The source material answers “What does the policy say?” You need both. A path from a customer to a contract does not contain the notification terms unless those terms are modeled there, and copying every paragraph into the graph creates another version of the truth to maintain.

Traversal also needs limits. Specify which edge types the request may follow, how many hops it can take, which tenant or account boundary applies, how current each connection must be, and what confidence is acceptable. Apply those limits as query and access constraints before the results reach the model, not as suggestions in the prompt.

Missing edges matter, too. If the service has no recorded owner, or two records disagree about which contract is active, the agent should report that condition. It should report that condition rather than infer a path between the available facts. “I can identify the affected service, but I can’t verify its current owner” is a useful answer. An unsupported conclusion during an incident can send notifications to the wrong customers.

The graph therefore needs an owner and a defined update path, just like the operational data behind it. Its access rules must also preserve enough provenance for an audit history. Otherwise, you risk presenting undocumented assumptions as authoritative-looking edges.

## Keep the graph near operational data

Many relationships already exist in relational tables. A foreign key connects a service to a team. A deployment table connects a service version to an environment. An entitlement table connects a customer to a product. Copying those facts into a separate graph system creates update delays and another permission model. It also leaves an uncomfortable question during every investigation: Which copy is current?

Oracle AI Database can be a useful option when graph and vector search need to stay near the relational records they depend on. [SQL property graphs](https://docs.oracle.com/en/database/oracle/oracle-database/26/sqlrf/create-property-graph.html?source=:ex:pw:::::TNS_GraphRAG_A&SC=:ex:pw:::::TNS_GraphRAG_A&pcode=) can be defined over existing tables and views, then queried through `GRAPH_TABLE`

. [AI Vector Search](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/?source=:ex:pw:::::TNS_GraphRAG_B&SC=:ex:pw:::::TNS_GraphRAG_B&pcode=) can rank related text in the same database. This lets an application use graph patterns against current business data, then add semantic retrieval without turning every lookup into a reconciliation job across several stores.

The query itself is plain SQL. Finding every service that uses OpenSSL, along with the customer environments those services support, is a single pattern match:

```
SELECT *
FROM GRAPH_TABLE (ops_graph
MATCH (lib IS library WHERE lib.name = 'openssl')
<-[IS USES]- (svc IS service) -[IS SUPPORTS]-> (env IS customer_environment)
COLUMNS (svc.name AS service_name, env.customer_id AS customer_id)
);
```

The decision rule matters more than the specific database. The platform should let the team inspect the exact path the agent used and trace each node and edge to its source, under the same access rules that protect the underlying records. If moving the relationships breaks those properties, the copy makes the answer harder to validate.

## Choose Graph RAG for defined questions

Ask one question before adding a graph: Does the answer require joining facts across entities, following dependencies, or proving why one record applies to another?

Repeated multi-hop questions are a strong signal. So are decisions controlled by ownership, entitlements, dependencies, or policies. Incidents caused by missing or stale connections give an even clearer starting point because the consequences of an unsupported path are already understood.

A self-contained knowledge base probably doesn’t need Graph RAG. Neither does a workload where one document usually answers the question. And if no operational system owns the relationships, building a graph won’t fix the underlying data problem. It may only hide it behind a nicer query interface.

“Evaluate the path as carefully as the prose it produces, because a fluent response may not reveal an incomplete join.”


Pilot one decision instead. Impact analysis is a good candidate: given a component change, identify the affected services and customers, then cite the records that establish each connection. Entitlement-aware support is another: determine which product and policy apply to an account before retrieving the support guidance.

Use known source [data and define success](https://thenewstack.io/four-data-infrastructure-shifts-defining-ai-success-in-2026/) before building. Check whether the agent resolved the right entities and followed current relationships within the allowed boundary. Verify that the retrieved documents support the answer. Evaluate the path as carefully as the prose it produces, because a fluent response may not reveal an incomplete join.

## Better context needs better evidence

A graph is useful only if it supplies evidence the agent cannot reliably retrieve in another way. Start with relationships people already use to make a decision, then prove that making those connections explicit improves the result.

Vector retrieval will still find the advisory and the contract language. The graph explains why they belong in the same answer. If the agent cannot show both the facts and the connections behind its conclusion, it should communicate the remaining uncertainty.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)
