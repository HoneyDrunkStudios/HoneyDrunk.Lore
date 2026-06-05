---
source: "https://azure.microsoft.com/en-us/blog/foundry-iq-build-smarter-agents-faster-with-unified-knowledge-and-serverless-retrieval/"
title: "Foundry IQ: Build smarter agents faster with unified knowledge and serverless retrieval | Microsoft Foundry Blog"
author: "Pablo Castro"
date_published: "2026-06-02"
date_clipped: "2026-06-05"
category: "Azure & Cloud"
source_type: "web"
---

# Foundry IQ: Build smarter agents faster with unified knowledge and serverless retrieval | Microsoft Foundry Blog

Source: https://azure.microsoft.com/en-us/blog/foundry-iq-build-smarter-agents-faster-with-unified-knowledge-and-serverless-retrieval/

Developers building agent fleets keep hitting the same pattern: the agent logic is ready, but the knowledge infrastructure underneath is complex to do well. Getting to production means solving for stability, scale, data access, answer quality, security, and content ingestion all at once. Today, we are enabling developers to have faster impact by simplifying the enterprise knowledge platform.

Your company’s IQ, [powered by Microsoft IQ](http://aka.ms/iq), is the collective intelligence locked in documents, emails, meetings, operational data, and the live web. This is where your true competitive edge lives. Foundry IQ grounds agents with the knowledge from these sources and continuously improves based on your business goals.

The announcements today are designed to help customers provision knowledge bases faster, unify enterprise and external sources, and expose that knowledge through the Foundry IQ Model Context Protocol (MCP) server for any agent framework or MCP-compatible hosts.

## What’s new

**Foundry IQ Serverless in preview:**Provision instant, no-friction context retrieval with scale to zero pricing. Developer tier now available in public preview with more coming soon.[Docs](https://learn.microsoft.com/en-us/azure/search/search-sku-tier)|[Create a Foundry IQ resource](https://ai.azure.com/nextgen/goto/build/knowledge)**New knowledge sources in preview:**Ground agents across Work IQ, Fabric IQ (including Data agents and Ontology), File Search, Azure SQL, and MCP through a multi-source knowledge base, with no custom integrations required.[Docs](https://aka.ms/FoundryIQ-new)|[Cookbook](https://microsoft-foundry.github.io/forgebook/notebook/mastering-foundry-iq/)**Web IQ in Foundry IQ is now available:**Extend agent context to the web, honoring publisher preferences, and marketplace data with sub-165 ms latency and zero data retention.[Blog](https://aka.ms/nextgengrounding)|[Website](https://aka.ms/webiq)**Foundry IQ knowledge bases are generally available:**Ship production agents on a fully SLA-backed knowledge layer with stable APIs, compliance certifications, and the Foundry IQ MCP server for any MCP-compatible host.[Docs](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/foundry-iq-connect?tabs=foundry%2Cpython)|[Quickstart](https://microsoft-foundry.github.io/forgebook/notebook/mastering-foundry-iq/#20-talk-to-the-knowledge-base-directly-over-mcp)**Agentic retrieval quality improvements:**The latest updates to the agentic retrieval engine improve answer performance across datasets, effort tiers, and model sizes while spending fewer tokens.[Blog](https://aka.ms/FoundryIQ-evals)|[Quickstart](https://learn.microsoft.com/en-us/azure/search/search-get-started-agentic-retrieval?tabs=windows&pivots=csharp)**Data pipeline updates in preview:**Automatic layout-aware ingestion of documents, image enrichment, and broader SharePoint indexing ground agents in complete documents, not just raw text.[Blog](https://aka.ms/FoundryIQ-data)|[Quickstart](https://aka.ms/FoundryIQ-data-samples)**Security updates in preview:**New controls for encryption, permissions sync, and sensitivity-label governance keep enterprise policy intact as content flows into agents.[Blog](https://aka.ms/FoundryIQ-security)|[Quickstart](https://github.com/Azure-Samples/azure-search-openai-demo-purviewdatasecurity)

## Foundry IQ Serverless in public preview

We know agent workloads are bursty and event-driven: an agent might execute hundreds of steps in seconds, then go idle for hours. Serverless eliminates infrastructure friction: no clusters to manage, no capacity to reserve, no idle costs. Go from zero to production fast, with instant retrieval-augmented generation (RAG) and state-of-the-art retrieval quality built in.

Foundry IQ Serverless (Developer tier) is available in public preview. You are billed for compute resources and storage used, and the service scales to zero when idle.

Serverless tiers use Compute Units (CU) to measure resource consumption, including CPU utilization, memory and storage I/O. Usage is calculated each minute in increments of 0.25 CUs.

For large-scale serverless deployments, [contact us](https://aka.ms/FoundryIQ-serverless-contact) for additional options.

| Capability | Developer tier |
|---|---|
| Compute usage | $0.24 CU / hour |
| Indexed storage | Up to $0.29 GB / month; GB cost is region dependent |
| Indexed storage per index | 1 GB / index |
| Indexes per service | 30 indexes / service |
| Services per subscription per region | 5 services / subscription / region |

*Billing is expected to begin in late 2026 with details provided at least 30 days in advance. Customers using Serverless Developer won’t be charged before billing is enabled. Current Compute Unit measurements are estimates only and subject to change before billing is enabled.*

Next steps: [create a Foundry IQ Serverless resource](https://ai.azure.com/nextgen/goto/build/knowledge) in the Foundry portal.

## New knowledge sources in preview

*How do I give an agent access to organizational knowledge and structured business data without building a custom connector for every system?*

Bringing enterprise knowledge into agent workflows often means stitching together custom integrations across each data source. Developers must account for different data formats, permission models, retrieval patterns, and source-specific logic before an agent could reliably use that knowledge.

Foundry IQ simplifies this by bringing enterprise content and structured systems into a single knowledge base for multi-source, agentic retrieval. Developers can give agents access to that knowledge without building and maintaining separate connectors or source-specific retrieval strategies.

New knowledge sources in preview:

**Work IQ**brings organizational signals like emails, meetings, files, and Teams messages into one enriched, AI-ready source, all while respecting user permissions. Agents can answer questions about how the organization operates, what decisions were made, and what is top of mind for teams.**Fabric IQ**lets agents query data agents and company ontologies: formal models of business entities, relationships, and rules linked to live data in OneLake and a specialized semantic layer. This returns structured answers alongside unstructured document context for a query.**File Search**allows you to directly upload files to a knowledge base.**Azure SQL**brings structured relational data into a knowledge base.**MCP Server**connects knowledge served over the Model Context Protocol.

Next steps: use the [Foundry IQ Forgebook](https://microsoft-foundry.github.io/forgebook/notebook/mastering-foundry-iq/) to try out additional knowledge sources.

## Microsoft Web IQ in Foundry IQ now available

*When an answer needs fresh, real-world context, how do I reach the open web without paying a latency or compliance penalty?*

Microsoft Web IQ is available in limited access through the Foundry IQ MCP knowledge source. It gives agents access to external retrieval across web, news, images, video, and shopping sources while honoring publisher preferences. It is designed for large language model (LLM) workflows rather than traditional search pages, with industry-leading low-latency ranking.

Combined with Foundry IQ, agents can plan, search, reason, and synthesize answers that draw on both internal knowledge and real-world external context in one retrieval engine.

Next steps: read the [blog announcement](https://aka.ms/nextgengrounding) for Microsoft Web IQ.

## Knowledge bases in Foundry IQ are generally available

*What does it actually take to move a prototype into production?*

Production means guarantees: stable contracts, predictable performance, and security that holds under audit. Foundry IQ knowledge bases and select knowledge sources, and security capabilities are generally available: with full SLA coverage, compliance certifications, stable APIs, and enterprise-grade network isolation with identity and policy enforced by default.

What is included in GA:

**Knowledge bases:**agentic retrieval references, output and activity logs, the Foundry IQ MCP server, and minimal retrieval reasoning effort.**Foundry IQ MCP server:**exposes Foundry IQ knowledge bases as a remote MCP server, making them accessible from any MCP-compatible host or client, including Claude, ChatGPT, LangChain, and the Microsoft Agent Framework. Network isolation, document-level security, cross-source ranking, and agentic retrieval all work over the open MCP standard, making it available for the broader agent ecosystem.**Knowledge sources:**Azure Blob Storage (with a status API to check indexing progress), search indexes, Web, and OneLake.**Security:**network isolation and managed identity support.

*“We’ve been using Foundry IQ in our research and prototyping work, and the reusable knowledge base approach has cut a lot of the setup overhead we’d normally expect. Being able to ground agents in trusted enterprise content from day one, without rebuilding retrieval logic each time, has made early-stage experimentation noticeably faster and higher quality.”* — **Jane Chen**, Lead AI Developer, Baringa Partners

Next steps: use the [Mastering Foundry IQ cookbook](https://microsoft-foundry.github.io/forgebook/notebook/mastering-foundry-iq/#11-talk-to-the-knowledge-base-directly-over-mcp) to get started building with the Foundry IQ MCP server.

## Agentic retrieval quality improvements

The latest retrieval enhancements improved our answer quality benchmarks by up to 20%, across our evaluated datasets, effort tiers, and model sizes. Compared to single-shot RAG, knowledge bases [improved recall by up to 54%](https://aka.ms/FoundryIQ-evals).

Foundry IQ improved its iterative agentic retrieval loop to batch queries more effectively, surface more relevant passages via semantic ranker, and apply server-side token caching to reduce redundant consumption across multi-turn conversations. This results in meaningfully fewer tokens spent without sacrificing answer quality, while beating previous benchmarks on answer quality.

Next steps: [read our blog](https://aka.ms/FoundryIQ-evals) for more on the latest evaluations and Foundry IQ benchmarks.

## Security updates in preview

*How do I keep enterprise data permissions intact as content flows into agents?*

Security belongs at the data layer, not approximated in application code. Several security capabilities are now in preview, including cross-tenant customer-managed keys (CMK) using federated identity credentials — eliminating shared secrets — Purview sensitivity-label auditing, incremental SharePoint permissions sync, APIM support for Foundry model integrations, and surfacing Purview sensitivity labels inside knowledge sources so label-based access controls are honored end to end.

Private connectivity between Foundry IQ and Foundry products, via Shared Private Link and Network Security Perimeter, is generally available.

*“By integrating Foundry IQ, we provide a managed, permission-aware business context layer that connects marketing and brand knowledge into every agent so they can access the right information, at the right time, with the right governance.”* — **Andrei Pop**, Director of PM, Innovation, Sitecore

Next steps: [read more](https://aka.ms/FoundryIQ-security) about the latest Foundry IQ security announcements.

## Data pipeline updates in preview

*How do I make sure agents are grounded in the whole document (tables, diagrams, and images) not just the raw text?*

Ingestion quality sets the ceiling on retrieval quality. New data pipeline capabilities in preview include first-class SharePoint indexing for ASPX pages and Lists alongside document libraries and document enrichment to process images plus serve them at query time in knowledge bases, so agents and users can reference original visuals and ask follow-up questions about them. We are also introducing Azure Content Understanding chunking with image verbalization — a layout-aware ingestion pipeline that converts diagrams, charts, and scanned images into meaningful text so agents are grounded in complete, semantically accurate representations of source documents.

Next steps: read Foundry IQ’s data pipeline [deep dive blog post](https://aka.ms/FoundryIQ-data).

## Get started today

Build once, reuse everywhere: Foundry IQ enables you to ground multiple agents with the same knowledge base, connecting and unifying data from anywhere. Foundry IQ is designed for agent workloads to deliver better results from your company’s IQ. With Foundry IQ, accelerate agent delivery, deliver context without blind spots, and ensure every answer respects your organization’s security by default.

The easiest way to explore Foundry IQ is through the [Microsoft Foundry portal](https://ai.azure.com/). From there you can create a knowledge base, access the [documentation](https://learn.microsoft.com/en-us/azure/foundry/), and follow the [Microsoft Foundry Learn courses](https://learn.microsoft.com/en-us/training/paths/develop-generative-ai-apps/), all in a few clicks.

Be sure to check out the latest news from Foundry IQ at Microsoft Build 2026:

## 0 comments

Be the first to start the discussion.
