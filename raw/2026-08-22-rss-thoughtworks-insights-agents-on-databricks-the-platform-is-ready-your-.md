---
source: "https://www.thoughtworks.com/insights/blog/technology-strategy/agents-on-databricks-the-platform-is-ready-your-business-context-is-not"
title: "Agents on Databricks: The platform is ready, your business context is not"
author: "Arun Srinivasan"
date_published: "2026-08-21"
date_clipped: "2026-08-22"
category: "Software Architecture"
source_type: "rss"
---

# Agents on Databricks: The platform is ready, your business context is not

Source: https://www.thoughtworks.com/insights/blog/technology-strategy/agents-on-databricks-the-platform-is-ready-your-business-context-is-not

Agents on Databricks: The platform is ready, your business context is not
Blogs
Back
Blogs
Back
Close
Data engineering
Data strategy
Blog
By
Arun Srinivasan
Published: August 21, 2026
Take a seemingly simple scenario, like asking an AI agent for last quarter's revenue. Before it can answer, it has to decide whether ‘revenue’ means booked, billed or recognized? Your estate has 47 tables with revenue in the name, so which one is the trusted source? Does the definition your finance team uses in North America also apply to the APAC business? And when the number comes back, can the agent show you where it came from? The agent will answer. It just won't tell you which of those choices it made.
Access is no longer the hard part. If you’re building agents on Databricks, that was solved by Unity Catalog and the governance layers around it. Your agent can reach the data but it cannot reliably understand your business; that gap is where most agent programs stall between a convincing demo and something a business will trust with a decision.
Databricks has moved quickly here. Genie Ontology is in public preview. Alongside it sit two Databricks Labs projects: OntoBricks, which builds formal ontologies and materializes them as a knowledge graph on the lakehouse, and Ontos, a business catalog that puts data products and contracts around your definitions. Together they cover more of the meaning layer than the platform has offered before. All three are designed to build on definitions your business has agreed, which is where the preparation work comes in.
This means the work is now split in two: what the platform supplies and what your teams supply to it.
Three paths, three questions
All three address business meaning, but at different layers of the architecture and for different consumers. That distinction matters, because it determines which one fits a given use case and how they combine when you need more than one.
Genie Ontology is the bottom-up path, and the one now in Public Preview. Genie continuously scans your notebooks, dashboards, pipelines, files and catalog lineage, extracts knowledge snippets, scores each for authority and injects the relevant ones into the agent loop at query time under your existing permissions. Genie Ontology maintains itself. That is the part worth pausing on. Metric and term definitions are the artifact enterprises hand-build and then watch drift, and one that stays current from sources you already govern is a real advance.
OntoBricks is the top-down path, a Databricks Labs project and so exploration-grade rather than SLA-backed. You design formal ontologies or import industry standards such as FIBO, FHIR and CDISC, then materialize and reason over them on the lakehouse. We have incorporated it into our internal accelerators for clients in regulated domains, where teams have to import a standard, run inference and prove the result is correct.
Ontos is the curated path, also Labs. It puts a business catalog over Unity Catalog with data products, data contracts and compliance rules, built for organizations whose gap is ownership and agreements rather than technology.
Pick by the question you are answering. Trustworthy natural-language analytics, quickly and with little configuration, points to Genie Ontology. Formal semantics, inference and regulated standards point to OntoBricks. Ownership, contracts and data products point to Ontos. They compose. They do not compete.
What each path builds on
All three work from the definitions your organization has agreed, so the quality of what you put in sets the ceiling on what you get out. Five disciplines carry most of that weight, and each has a business component and an engineering one.
Agree what your metrics mean. Settle revenue, margin, churn, active customer and service level first. For each, fix the formula, the owner, the allowed dimensions, the system of record, the temporal rule for when the definition applies and the exceptions you permit. Then give those definitions somewhere to live that’s not a prompt or a single agent's code. Context belongs in its own platform layer, shared across every agent, app and model you run.
Define your business language. Customer, account, household, product and supplier mean different things to different teams, and the relationships between them carry meaning too. A customer may own several accounts. An account may hold several products. Engineering's job is to make those relationships explicit and honest about their status. Two tables sharing a customer_id column is a candidate for a join, not proof of one. Label it inferred until someone verifies it.
Name what is trusted. Conflicting versions of the same fact are not a new problem. Usage across dashboards is a useful signal, but the most-used dashboard is not always the correct one. Popularity is not the truth. Let the platform compute authority and do the discovery, then have owners confirm the source of record for the metrics that matter. Discovered meaning and approved meaning are both valuable, and they belong in separate lanes. Model suggestions start as candidates. They should never quietly become business truth, least of all where they touch financial reporting, customer treatment or compliance.
Attach evidence to every claim. If an agent asserts something, it should point back to a document passage, a table row, a policy or a recorded decision. Models hallucinate confidently. Citation is what grounds them, and it is also what makes an answer defensible six months later.
Version the meaning your decisions depend on. A continuously learning context layer updates as your data and usage change, which is precisely what discovery needs. A high-risk decision you may have to defend later needs something different: a fixed reference point. The two are complementary. Keep a versioned layer of approved definitions alongside the learned one, pin your agents to a named release, and test against that release rather than against shifting current records. This is where the formal path earns its place, and it is the reason the three paths are worth understanding together rather than choosing between.
Then test meaning, not just code. Start with a golden question-answer pair -  the business questions your agent must answer correctly, with the answer you expect, and run them the way you would run a unit test suite. Assert on the substance, not the prose: that the answer used the approved revenue metric, that it joined through an approved relationship, that every claim came back with a citation, that a question with unresolved conflicting definitions returns a flag rather than a confident number. Version those cases with your definitions, so a change to a metric breaks the tests that depend on it. This is a regression suite for meaning, and it belongs in your pipeline next to the ones you already run for code.
Find where you actually are
None of this arrives at once. A checklist assumes you are starting from zero, and almost nobody is, so a maturity model is the more useful instrument. Five stages, tracked on two axes: what your catalog knows, and what your agents can use.
Raw. Catalog objects carry no descriptions or tags. No knowledge is being extracted.
Enriched. Governed tags and rich descriptions on the tables that matter. Knowledge accumulating from your sources.
Defined. Glossary pages drafted, steward approval workflows running, extracted knowledge feeding your glossary and metric definitions.
Curated. Metric views driving dashboards and agents. Domains organizing the catalog. Domain-specific agents in real use.
Verified. Assets certified, deprecated and classified. Agent answers consistently rated to produce high-quality signal.
The goal is not to reach Verified everywhere. It is to be able to say where you stand on both tracks, and name the next concrete move. Most teams find they are further along on the catalog than on the agent side, which is a useful thing to discover, because it means the next move is smaller than they feared.
Start with a decision, not a chatbot
Pick a business process where the decisions carry weight, then find the decision where meaning is expensive. The tell is a question that should take five minutes and take an hour, because someone has to confirm which definition applies, find who owns the metric, or reconcile two reports that disagree. Following the time cost instead of the difficulty would be a solid indicator in picking the right domain.
"Which customer contracts are at risk, why, and what evidence supports that view?" is a far better test of readiness than a general chat interface, because answering it demands current data, business rules, metrics, relationships and source evidence at the same time. It will show you exactly which of the five disciplines to work on next.
That is what it takes to rewire for agents. The platform side is moving fast and getting stronger. The definitional side moves at the pace your organization sets, and it is what turns an impressive demo into AI that works.
Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
Related content
Data engineering
Backstage with Lakebase: Exploring the concept with Databricks
Learn more
Data engineering
Backstage with Databricks Lakebase: Bringing the operational database into Unity Catalog
Learn more
Data engineering
Backstage with Lakebase | Part 3: The one-query FinOps solution
Learn more
Gain a fresh perspective on tech today with the Technology Podcast
Listen now
