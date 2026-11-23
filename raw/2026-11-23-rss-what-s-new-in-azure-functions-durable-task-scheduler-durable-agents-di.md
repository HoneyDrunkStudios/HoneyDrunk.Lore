---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/whats-new-in-azure-functions-durable-task-scheduler-durable-agents-disaster-reco/4573351"
title: "What's new in Azure Functions durable task scheduler: Durable agents, disaster recovery, and more"
author: "NickGreenfield"
date_published: "2026-11-17"
date_clipped: "2026-11-23"
category: "Azure & Cloud"
source_type: "rss"
---

Source: https://techcommunity.microsoft.com/blog/appsonazureblog/whats-new-in-azure-functions-durable-task-scheduler-durable-agents-disaster-reco/4573351

# What's new in Azure Functions durable task scheduler: Durable agents, disaster recovery, and more

There's been a lot happening with the [Azure Functions durable task scheduler](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler) lately. Here's a quick look at what's new:

- **Durable agents:** The [Durable Extension for Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/hosting/durable-extension) is generally available, [durable execution with DTS for LangGraph](https://docs.langchain.com/oss/python/integrations/providers/azure_ai#durable-langgraph-execution-with-azure-durable-task-scheduler) is in preview, and [Pydantic AI](https://pydantic.dev/docs/ai/harness/azure-durable-task/) now includes Azure Durable Task as a built-in durability option.
- **[Native disaster recovery](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/disaster-recovery) and [task queues](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler-task-queues):** Both are now in public preview.
- **[Private endpoints](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler-private-endpoints) and [customer-managed keys](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler-customer-managed-keys):** Both are now generally available.

  **[Durable Task Go SDK](https://github.com/microsoft/durabletask-go#readme):** Now available in preview.

Whether you're running business workflows, processing event-driven pipelines, or coordinating AI agents, here's what these updates mean for your apps and how to get started.

# What is the Durable Task Scheduler?

If you're new to the [Durable Task Scheduler](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler), it's a fully managed durable execution backend for workflows and agents on Azure. It saves progress as work runs, so applications can recover from interruptions without starting over. Completed steps whose results have been saved can be reused, and workflows can wait for human input or external events without keeping a worker active just to wait.

DTS handles task scheduling, state persistence, and recovery. Its built-in dashboard lets you inspect execution history and manage running orchestrations.

*The DTS dashboard shows the execution timeline of a travel-planning workflow, including agent calls and a wait for approval.*

DTS runs separately from your application. Use it with Durable Functions, the Durable Task SDKs, or supported agent framework integrations, including the Durable Extension for Microsoft Agent Framework. Your application code can run anywhere in Azure, including Azure Functions, Azure Container Apps, and Azure Kubernetes Service.

Already using DTS? Here's what's new.

# Durable execution in agent SDKs

Agents and workflows need more than conversation history to recover from interruptions. They might call several tools, start a long-running job, or wait for someone's approval. If a worker restarts halfway through, the application needs to know which steps completed and what should happen next.

Durable execution saves that progress, so agents and workflows can run for minutes, days, or weeks and resume from recorded progress after worker or container restarts, scaling events, or infrastructure failures. Retry policies help handle transient errors such as rate limits and timeouts.

Completed model calls, tool calls, and activities whose results have been saved can be reused during recovery, reducing repeated work and token costs. Conversation context remains available, and workflows can wait for approvals or external events for hours or days without keeping a worker active just to wait.

You can bring these durable execution capabilities to agents and workflows built with Microsoft Agent Framework, LangGraph, or Pydantic AI. Here's how to get started with each:

- **[Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/hosting/durable-extension):** The Durable Extension is generally available for .NET and Python. Keep your core agent logic and coordinate durable agents and multi-agent workflows with Durable Task orchestrations or Agent Framework graphs. See the [GA blog post](https://techcommunity.microsoft.com/blog/appsonazureblog/durable-task-extension-for-microsoft-agent-framework-is-now-generally-available/4571100) and [samples](https://github.com/Azure-Samples/Durable-Task-Scheduler/tree/main/samples/durable-extension-for-agent-framework).
- **[LangGraph](https://docs.langchain.com/oss/python/integrations/providers/azure_ai#durable-langgraph-execution-with-azure-durable-task-scheduler):** In public preview. Add DTS to existing Python graphs, ReAct agents, and Deep Agents on Azure without rewriting your graph logic.
- **[Pydantic AI](https://pydantic.dev/docs/ai/harness/azure-durable-task/):** Azure Durable Task is now available as a durability capability in Pydantic AI Harness. Use it with Durable Task orchestration and worker setup to persist model and tool results and recover agent execution without building your own checkpointing or recovery system.

# Native disaster recovery is now in public preview

Native disaster recovery for Azure Functions durable task scheduler is now in public preview. For business-critical workflows and applications with cross-region recovery requirements, it provides a way to resume work in another region from replicated state rather than starting workflows over.

Pair your primary scheduler with a secondary in another Azure region, and DTS replicates orchestration and entity state to the secondary. When you need to fail over, you can promote the secondary and resume work from that replicated state.

**Learn more:** [Disaster recovery documentation](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/disaster-recovery).

# Task queues are now in public preview

Task queues for Azure Functions durable task scheduler are now in public preview. Group orchestration and activity work into named queues within a task hub and control how quickly DTS delivers that work to workers.

This helps teams pace batch processing and give different workloads their own dispatch-rate budgets without creating separate task hubs. For workloads that call downstream services, it provides a way to manage how quickly work is dispatched.

Create a queue, configure its work-item delivery rate, and select it using the DTS\_TaskQueue tag when scheduling work.

For a closer look at how task queues work and an example of how to use them, see [Task queues in Durable Task Scheduler](https://techcommunity.microsoft.com/blog/appsonazureblog/task-queues-in-durable-task-scheduler/4573962).

**Learn more:** [Task queues documentation and SDK examples](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler-task-queues?tabs=cli%2Ccsharp).

## Private endpoints are now generally available

Private endpoints for Azure Functions durable task scheduler are now generally available for both Consumption and Dedicated SKU schedulers. Connect your applications to DTS through a private IP address in your virtual network using Azure Private Link.

Traffic stays on the Microsoft backbone instead of traversing the public internet. You can also disable public network access so your scheduler accepts connections only through private endpoints. Applications continue to use the same scheduler endpoint and Microsoft Entra authentication.

**Learn more:** [Configure private endpoints for DTS](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler-private-endpoints).

## Customer-managed keys are now generally available

Customer-managed keys for Azure Functions durable task scheduler are now generally available for Dedicated SKU schedulers.

Organizations that need to manage their own encryption keys can now use customer-managed keys to protect their workflow data, supporting separation of duties, centralized auditing of key access, and customer-defined key rotation policies.

Use a key you own in Azure Key Vault or Azure Managed HSM to protect scheduler data at rest. Configuration is available through the ARM REST API, Azure CLI using az rest, or Bicep.

**Learn more:** [Configure customer-managed keys for DTS](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler-customer-managed-keys).

# The Durable Task Go SDK is now available in preview

Writing your application in Go? You can now build durable workflows with the [Durable Task Go SDK](https://github.com/microsoft/durabletask-go), available in preview.

Write your orchestrations and activities in Go, and let DTS take care of durable state and dispatching work. You can chain activities, run work in parallel, wait for external events, and use durable timers. Retry policies help you handle failures, and orchestration management APIs let you manage execution.

Start locally with the DTS emulator, then connect your application to a scheduler in Azure when you're ready. You'll need Go 1.25 or later, and DTS is currently the SDK's only supported runtime.

**Get started:** [Go SDK documentation](https://github.com/microsoft/durabletask-go#readme), [DTS quickstart sample](https://github.com/microsoft/durabletask-go/tree/main/samples/durabletaskscheduler), and [Go sample catalog](https://github.com/microsoft/durabletask-go/blob/main/samples/README.md).

# Get started with the Durable Task Scheduler

If you're new to DTS, start with the [documentation](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler) and [samples](https://github.com/Azure-Samples/Durable-Task-Scheduler). You can develop locally with the emulator, then choose the Consumption or Dedicated SKU based on your workload's [pricing and capacity requirements](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler-billing).

We'd love to hear your feedback, especially as you try the new previews. Share questions and feedback through the [Durable Task Scheduler GitHub repository](https://github.com/Azure-Samples/Durable-Task-Scheduler/issues).
