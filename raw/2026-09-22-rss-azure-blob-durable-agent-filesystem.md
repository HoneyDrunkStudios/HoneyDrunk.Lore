---
source: "https://devblogs.microsoft.com/azure-sdk/using-azure-blob-storage-as-a-durable-filesystem-for-langchain-deep-agents-2"
title: "Using Azure Blob Storage as a durable filesystem for LangChain Deep Agents"
author: "Vishnu Charan TJ"
date_published: "2026-09-22"
date_clipped: "2026-09-22"
category: "Azure & Cloud"
source_type: "rss"
capture_format: "attributed-summary"
---

# Using Azure Blob Storage as a durable filesystem for LangChain Deep Agents

Source: [Using Azure Blob Storage as a durable filesystem for LangChain Deep Agents](https://devblogs.microsoft.com/azure-sdk/using-azure-blob-storage-as-a-durable-filesystem-for-langchain-deep-agents-2)

Attributed summary of the fetched written article; not a full reproduction. Source claims have not been independently reproduced.

AzureBlobBackend connects LangChain Deep Agents' file tools to Azure Blob Storage through the public-preview langchain-azure-storage integration. Files can persist beyond an agent process and be read by another agent or inspected through normal Azure storage tools.

The example uses DefaultAzureCredential and container-scoped data access. Local development can use Azure CLI identity, while deployed workloads can use managed or workload identity. Explicit ManagedIdentityCredential narrows authentication when required.

CompositeBackend routes durable evidence, guidance, and results to Blob-backed paths while leaving temporary plans and offloaded context in thread-local state. The mortgage-processing sample separates source evidence, shared instructions, and run-specific outputs, and denies writes to evidence and guidance through filesystem permission rules.

The author recommends distinct containers for access boundaries, least-privilege roles, recovery features, and restricted destructive tools. HoneyDrunk relevance: preserve immutable research evidence and shared agent artifacts independently of worker lifetimes. Storage authorization and tool-level restrictions both matter; a shared path alone is not tenant isolation.
