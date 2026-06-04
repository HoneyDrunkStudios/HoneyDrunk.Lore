---
source: "https://devblogs.microsoft.com/cosmosdb/announced-at-ms-build-2026-azure-cosmos-db-mcp-toolkit-semantic-reranking-global-secondary-indexes-and-more/"
title: "Announced at MS Build 2026: Azure Cosmos DB MCP Toolkit, Semantic Reranking, Global Secondary Indexes, and more!"
author: "Azure Cosmos DB Team"
date_published: "2026-06-02"
date_clipped: "2026-06-04"
category: "Azure & Cloud"
source_type: "web"
---

# Announced at MS Build 2026: Azure Cosmos DB MCP Toolkit, Semantic Reranking, Global Secondary Indexes, and more!

Source: https://devblogs.microsoft.com/cosmosdb/announced-at-ms-build-2026-azure-cosmos-db-mcp-toolkit-semantic-reranking-global-secondary-indexes-and-more/

Microsoft Build 2026 has officially started and we’re excited to announce new capabilities for Azure Cosmos DB! We’ve launched new features to help developers build AI-powered applications and agents more easily, improve application resilience, and accelerate developer productivity.
These announcements span every stage of the development lifecycle, from local development with the Azure Cosmos DB Linux Emulator, to advanced retrieval and agent memory capabilities for AI applications, to enterprise-grade operational features such as Global Secondary Indexes, Per-Partition Automatic Failover, Distributed Transactions, and Azure Backup.
Whether you’re building modern cloud applications, RAG solutions, or sophisticated multi-agent systems, Azure Cosmos DB continues to evolve as the AI-ready operational and vector database for mission-critical workloads.
AI-powered apps with Azure Cosmos DB 
Don’t miss these related talks at Build:
LTG411: Agentic RAG for fast, low-cost knowledge retrieval on Azure Cosmos DB (in person only) 
DEM310: Ship code faster with AI-powered NoSQL schema design (live and on demand) 
BRK223: From rows to reasoning: Designing databases for AI apps and agents (live and on demand) 
LTG453: Building an End‑to‑End Enterprise AI Platform on Azure (in person only) 
TT621: Build & modernize multi-tenant AI app data planes for planetary scale (in person only) 
OD820: Designing Reliable Multi‑Agent Apps with Azure Cosmos DB (on demand) 
As organizations move beyond traditional applications toward intelligent, agent-driven experiences, databases play a critical role as both operational data stores and long-term memory systems for AI applications.
To help developers build the next generation of AI applications, we’ve introduced several new capabilities that simplify agent development, improve retrieval quality, and accelerate developer workflows.
Generally Available: MCP Toolkit for Azure Cosmos DB 
The Model Context Protocol (MCP) is quickly emerging as a standard way for AI agents to interact with external systems and data sources. With the MCP Toolkit for Azure Cosmos DB, developers can easily expose Azure Cosmos DB data to MCP-compatible AI clients and agent frameworks.
The toolkit simplifies integration with AI-powered applications by providing a secure and standardized way to access operational and vector data stored in Azure Cosmos DB. Developers can connect agents to their data with minimal setup while maintaining the performance, security, and scalability Azure Cosmos DB is known for.
Generally Available: Agent Kit for Azure Cosmos DB 
Your AI coding agents just got smarter about building high-performance Azure Cosmos DB applications.
The Azure Cosmos DB Agent Kit is now generally available, bringing proven Azure Cosmos DB best practices directly into your development workflow. With more than 100 actionable rules covering data modeling, partition key strategies, query optimization, SDK usage, and production resilience, the Agent Kit helps AI coding agents guide developers toward optimized, production-ready application designs.
Whether you are working in Visual Studio Code, GitHub Copilot, or another AI-assisted coding environment, the Agent Kit helps surface Azure Cosmos DB-specific recommendations earlier in the development process. It can help prevent hot partitions, identify query patterns that may drive unnecessary RU consumption, and recommend design choices that improve scalability, performance, and reliability.
By embedding Azure Cosmos DB expertise into AI-assisted development workflows, the Agent Kit helps developers learn best practices faster, avoid common performance pitfalls, and build applications that are better optimized from day one.
You can find Azure Cosmos DB Agent Kit in GitHub. 
Public Preview: Agent Memory Toolkit 
Agents require memory to maintain context, track interactions, and improve decision making over time. The Agent Memory Toolkit for Azure Cosmos DB helps developers implement durable memory patterns for AI agents using Azure Cosmos DB as the persistent storage layer.
The toolkit simplifies memory management across agent interactions and enables developers to build more capable and context-aware agentic systems without creating custom memory infrastructure. Learn more about Agent Memory Toolkit here: https://aka.ms/AgentMemoryToolkit 
Public Preview: Semantic Reranking 
Retrieval quality remains one of the most important factors in AI application performance.
Semantic Reranking improves search relevance by analyzing the meaning and context of both queries and retrieved content. Rather than relying solely on vector similarity or keyword matching, Semantic Reranking reorders results based on contextual relevance, helping applications return more accurate and useful information.
Combined with Azure Cosmos DB’s integrated vector search and full-text search capabilities, Semantic Reranking helps developers build higher-quality RAG apps and AI agents.
Public Preview: AI Assistance in the Azure Cosmos DB Extension for VS Code 
AI Assistance in the Azure Cosmos DB extension for Visual Studio Code helps developers work more efficiently by providing intelligent guidance, recommendations, and assistance directly within their development environment.
By combining AI-powered assistance with Azure Cosmos DB’s developer tools, developers can accelerate application development and reduce time spent on repetitive tasks.
Resilient, enterprise-scale applications 
Don’t miss these related talks at Build:
LTG459 : Anatomy of a cloud based, multi tenant, SaaS product (in person only) 
BRK224: PepsiCo’s blueprint for agentic AI (live and on demand) 
BRK223: From rows to reasoning: Designing databases for AI apps and agents (live and on demand) 
OD820: Building Azure DocumentDB on Open-Source Foundations (on demand) 
Organizations running mission-critical workloads require databases that deliver high availability, operational flexibility, and strong consistency guarantees.
This release introduces several major capabilities designed to help customers build more resilient and scalable applications.
Generally Available: Global Secondary Indexes 
Global Secondary Indexes (GSIs) for Azure Cosmos DB are now generally available, making it easier to optimize query performance without redesigning your data model or changing application code.
A GSI is a read-only container that automatically stays synchronized with a source container using the change feed. Each GSI can have its own partition key, throughput, and indexing policy, allowing you to optimize it for specific query patterns and workload requirements.
By storing data under a different partition key, GSIs can turn expensive cross-partition queries into efficient single-partition lookups, helping reduce RU consumption, lower latency, and improve performance. GSIs also provide workload isolation, enabling scenarios such as vector search and full-text search for AI applications without impacting transactional workloads on the source container.
Whether you’re optimizing existing workloads or supporting new application requirements, GSIs help maintain performance and efficiency as your workloads evolve. Learn more here. 
Generally Available: Per-Partition Automatic Failover 
Per-Partition Automatic Failover (PPAF) is now generally available, helping Azure Cosmos DB applications maintain availability during regional disruptions with a more granular approach to failover.
Traditionally, failover operations occur at the account or regional level. With Per-Partition Automatic Failover, Azure Cosmos DB can automatically detect partitions affected by an outage and fail over only those partitions to healthy replicas in another region. This minimizes disruption, reduces recovery time, and helps maintain application availability while unaffected partitions continue operating normally.
Public Preview: Distributed Transactions 
Many enterprise applications require transactional consistency across multiple operations and data entities.
Distributed Transactions bring transactional capabilities across multiple partitions, simplifying application development and enabling developers to implement more sophisticated business workflows while maintaining data consistency.
This capability helps reduce application complexity and allows developers to focus on business logic rather than implementing custom transactional coordination mechanisms.
Public Preview: Azure Backup for Azure Cosmos DB 
Data protection remains a critical requirement for enterprise applications.
Azure Backup for Azure Cosmos DB provides a managed backup experience that helps organizations protect critical data and improve recovery readiness. By integrating with Azure Backup, customers can simplify operational management while strengthening business continuity and compliance strategies. Read more about Azure Backup for Azure Cosmos DB this in Tech Community blog post. 
Accelerating developer productivity 
Don’t miss these related talks at Build:
BRK223: From rows to reasoning: Designing databases for AI apps and agents (live and on demand) 
OD820: Designing Reliable Multi‑Agent Apps with Azure Cosmos DB (on demand) 
Azure Cosmos DB continues to invest in developer productivity with several new capabilities.
Generally Available: Azure Cosmos DB Linux Emulator 
The Azure Cosmos DB Linux Emulator is now generally available.
Developers can run Azure Cosmos DB locally in Linux environments, containers, CI/CD pipelines, and cloud-based development environments, enabling faster testing and development without requiring a live cloud deployment.
The Linux Emulator simplifies local development workflows while providing a more consistent experience across development environments.
Generally Available: Change Partition Keys 
Data models evolve over time as applications grow and requirements change.
Change Partition Keys enables developers to modify partition key strategies without requiring complex migration projects or application rewrites. This capability provides greater flexibility for evolving workloads and helps teams adapt their data models as business needs change.
Generally Available: All Versions and Deletes Change Feed Mode 
The All Versions and Deletes Change Feed Mode expands the Azure Cosmos DB change feed by capturing all document versions and delete operations.
This enables more sophisticated event-driven architectures, auditing scenarios, data synchronization workflows, compliance use cases, and AI data processing pipelines.
Developers can build richer downstream processing systems while maintaining a complete view of data changes over time.
On the Ground at Build 
We’re at Microsoft Build 2026 and ready to help. If you’re stopping by the Azure NoSQL Databases and Caching booth, be sure to say hello to experts like Marko Hotti, Sergiy Smyrnov, and Phillip Laussermair. Whether you’re exploring AI applications, evaluating NoSQL databases, designing for global scale, or looking for guidance on your next project, they’re here to answer questions, share best practices, and help you get the most out of your Build experience.
Table Talk 
This was a table talk, not a slide deck. People building or modernizing SaaS apps pulled up a chair with Azure engineers and worked through the messy parts of multi-tenancy: how to model tenant-aware data, how far to push tenant isolation, and when a migration is worth the risk.
Most of it happened at the whiteboard, on actual problems people brought from their own production systems. The takeaway wasn’t a checklist — it was a clearer sense of which tradeoffs matter and which ones you can stop losing sleep over.
Get started 
From agent memory and retrieval innovations to enterprise resilience and developer productivity improvements, Azure Cosmos DB provides the capabilities developers need to build intelligent applications at global scale.
Explore the latest features in the Azure portal, download the Azure Cosmos DB Linux Emulator , and start building today.
About Azure Cosmos DB 
Azure Cosmos DB is a fully managed and serverless NoSQL and vector database for modern app development, including AI applications. With its SLA-backed speed and availability as well as instant dynamic scalability, it is ideal for real-time NoSQL and MongoDB applications that require high performance and distributed computing over massive volumes of NoSQL and vector data.
To stay in the loop on Azure Cosmos DB updates, follow us on  X ,  YouTube , and  LinkedIn .
