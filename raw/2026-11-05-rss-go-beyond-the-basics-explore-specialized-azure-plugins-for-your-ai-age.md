---
source: "https://devblogs.microsoft.com/azure-sdk/explore-specialized-azure-plugins-for-your-ai-agent"
title: "Go beyond the basics: Explore specialized Azure plugins for your AI agent"
author: "Yun Jung Choi"
date_published: "2026-11-03"
date_clipped: "2026-11-05"
category: "Azure & Cloud"
source_type: "rss"
canonical_url: "https://devblogs.microsoft.com/azure-sdk/explore-specialized-azure-plugins-for-your-ai-agent/"
---

# Go beyond the basics: Explore specialized Azure plugins for your AI agent

Investigating an AKS incident, explaining an unexpected Azure bill, and connecting an agent to a knowledge base call for different expertise. With specialized Azure plugins, you can bring guidance for those tasks into your development workflow instead of assembling the context and procedures yourself.

The [Azure plugin catalog](https://github.com/microsoft/azure-skills/tree/main/.github/plugins) now includes six specialized plugins alongside the core Azure plugin. They cover Azure Kubernetes Service (AKS) operations, cost management, Azure Advisor recommendations, Kusto graph analysis, Azure Local, and Foundry IQ knowledge bases.

Use Azure plugins with the AI agent of your choice. In this post, we’ll explore what each plugin helps you do, share example prompts, and show you how to install the plugins you need.

## Start with Azure, then add specialized skills

The core **Azure** plugin, called the `azure` plugin, connects your AI agent to Azure tools and skills for managing resources, deploying applications, and monitoring services. Additional plugins provide focused workflows for specific services and operational needs.

You don’t need to install every plugin. Add only the ones you need for your workflow to help manage your agent’s context window and leave more room for your code, conversations, and task-specific context. For example, add AKS Skills when troubleshooting clusters or Azure Cost when investigating spend, without bringing in unrelated capabilities.

The `azure` plugin also includes a discovery skill that helps you find these additional plugins as your tasks call for them. You can always install any plugin yourself, as described in the installation section below.

The following sections illustrate how specialized plugins complement the `azure` plugin across a range of Azure workflows.

## Investigate AKS incidents with AKS Skills

When a Kubernetes workload fails, the useful evidence can span pods, nodes, networking, and Azure resources. **[AKS Skills](https://github.com/microsoft/azure-skills/tree/main/.github/plugins/aks-skills)** (`aks-skills`) adds deeper operational guidance alongside the core Azure plugin’s cluster planning, setup, deployment, and baseline diagnostics.

Use it to investigate live incidents, match known error signatures to documented fixes, troubleshoot GPU and KAITO inference workloads, or collect bounded packet captures from selected nodes. Its cost-efficiency workflows also examine node scaling, workload placement, and Kubernetes-aware storage.

**Try a prompt like:**

> Investigate why pods in my AKS cluster are stuck in Pending. Collect read-only evidence and explain the likely cause before suggesting changes.

Troubleshooting starts with evidence collection. Resource changes and packet captures require explicit approval. Install this plugin alongside `azure` plugin.

## Understand and manage spend with Azure Cost

An unexpected bill raises several questions: What changed? Where is the spend coming from? What can we do about it?

**[Azure Cost](https://github.com/microsoft/azure-skills/tree/main/.github/plugins/azure-cost)** (`azure-cost`) brings together four areas of cost management: analysis, estimation, optimization, and governance. Backed by the Azure Resource Manager MCP server, it supports investigating billed spend and anomalies, analyzing AKS costs, forecasting spend, estimating planned resources, evaluating commitment options, and working with budgets and cost guardrails.

If you used the cost analysis skill in the core Azure plugin, it has now moved into this standalone plugin. Install Azure Cost to keep using it.

**Try a prompt like:**

> Investigate the increase in this subscription’s costs last month. Identify the main contributors and distinguish observed spend from any forecasts or estimates.

## Turn recommendations into next steps with Azure Advisor

Finding a recommendation is only the beginning. You also need to understand which resources are affected and what remediation involves.

**[Azure Advisor](https://github.com/microsoft/azure-skills/tree/main/.github/plugins/azure-advisor)** (`azure-advisor`) helps you discover and summarize Advisor recommendations, identify resources affected by service retirements, and prepare remediation guidance for individual recommendations.

**Try a prompt like:**

> Show the service-retirement recommendations affecting this subscription, identify the impacted resources, and explain the remediation guidance for one recommendation.

When Advisor doesn’t provide specific remediation guidance, the actionability workflow falls back to relevant public Microsoft Learn documentation. It identifies the source of the guidance and cites the documentation used, helping you distinguish Advisor-provided instructions from documentation-based next steps.

## Explore relationships with Azure Kusto Graph Skills

Some investigations are about connections rather than individual records: how entities relate, which paths connect them, or how a suspicious activity chain develops.

**[Azure Kusto Graph Skills](https://github.com/microsoft/azure-skills/tree/main/.github/plugins/azure-kusto-graph-skills)** (`azure-kusto-graph-skills`) provides guidance for graph analysis in Azure Data Explorer. It covers Kusto Query Language (KQL) graph operators, including graph construction, pattern matching, shortest paths, connected components, and persistent graph models.

It also includes skills for composing Incident Response Query Language (IRQL) security-hunting pipelines and generating graph mappings and visualizations from query results.

**Try a prompt like:**

> Help me build a KQL graph from my entity relationships and find paths between two entities. Explain the query and the required table schema.

## Plan and operate Azure Local deployments

Working across local infrastructure and Azure adds another layer of context. Even similarly named operations can require different procedures depending on the deployment architecture.

[**Azure Local Skills**](https://github.com/microsoft/azure-skills/tree/main/.github/plugins/azure-local-skills) (`azure-local-skills`) covers planning, deployment, day-2 operations, lifecycle updates, workload management, networking, and troubleshooting. Separate skills address standard Azure Local and multi-rack deployments.

**Try a prompt like:**

> Help me plan an Azure Local deployment. Establish whether the requirements fit a standard or multi-rack deployment before recommending procedures.

The distinction matters: standard and multi-rack deployments use separate, non-interchangeable procedures. Multi-rack is in preview. Both skills start read-only and request confirmation before disruptive operations such as updates, reimages, network changes, and VM power operations.

## Build grounded knowledge experiences with Foundry IQ Skills

An agent becomes more useful when it can retrieve relevant information from your content and cite its sources.

[**Foundry IQ Skills**](https://github.com/microsoft/azure-skills/tree/main/.github/plugins/foundry-iq-skills) (`foundry-iq-skills`) helps you create, connect, query, and troubleshoot Foundry IQ knowledge bases using Azure AI Search. You can start with local files, Azure Blob Storage, or Azure Data Lake Storage, validate that content is searchable, and connect an existing knowledge base to an agent.

**Try a prompt like:**

> Create a Foundry IQ knowledge base from my local documentation, reuse compatible Azure resources where possible, and show me the plan before creating anything.

The workflow requests approval before creating resources or connecting a knowledge base to an agent. Its focus is Foundry IQ knowledge-base workflows, not general-purpose search-index development or generic agent creation.

## How to install these plugins

You can ask the core Azure plugin’s discovery skill to recommend plugins, or install them yourself. In **GitHub Copilot CLI, Claude Code, or Cursor**, add the [**`microsoft/azure-skills`**](https://github.com/microsoft/azure-skills) marketplace and install only the plugins you need through your client’s plugin manager. In clients that support `/plugin` commands, copy and paste:

```
/plugin marketplace add microsoft/azure-skills
```

Then choose the install commands for your workflow:

| Plugin | Install command |
| --- | --- |
| Core Azure plugin | `/plugin install azure@azure-skills` |
| AKS Skills | `/plugin install aks-skills@azure-skills` |
| Azure Cost | `/plugin install azure-cost@azure-skills` |
| Azure Advisor | `/plugin install azure-advisor@azure-skills` |
| Azure Kusto Graph Skills | `/plugin install azure-kusto-graph-skills@azure-skills` |
| Azure Local Skills | `/plugin install azure-local-skills@azure-skills` |
| Foundry IQ Skills | `/plugin install foundry-iq-skills@azure-skills` |

Update plugins through your client’s plugin manager, or with a command such as:

```
/plugin update azure-cost@azure-skills
```

**Note:** Individual plugins and skills may have additional requirements. Check each plugin’s README for supported clients and required tools, credentials, and permissions.

## Choose a workflow and share your feedback

Start with a task you already need to complete: investigate an incident, explain a cost increase, review retirement impact, explore connected data, plan local infrastructure, or ground an agent in your documentation.

Explore the [plugin catalog](https://github.com/microsoft/azure-skills) for details, prerequisites, and security considerations. Share issues and suggestions in the [Azure Skills repository](https://github.com/microsoft/azure-skills/issues) to help improve these workflows.
