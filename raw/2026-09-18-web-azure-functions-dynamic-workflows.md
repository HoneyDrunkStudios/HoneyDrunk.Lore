---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/enable-dynamic-workflows-in-azure-functions-hosted-skills/4551993"
title: "Enable Dynamic Workflows in Azure Functions hosted skills"
author: "greenie-msft"
date_published: "2026-09-17"
date_clipped: "2026-09-18"
category: "Azure & Cloud"
source_type: "web"
---

# Enable Dynamic Workflows in Azure Functions hosted skills

Capture format: attributed summary of fetched public written content; not a full-text reproduction.

Microsoft describes Dynamic Workflows for Azure Functions hosted skills, formerly Serverless Agents. The model produces a structured plan using explicitly allowed workflow tools and subagents; the runtime validates it and starts a Durable Functions orchestration.

Execution can outlive the initiating request and worker restarts. Dependency scheduling supports parallel tasks, intermediate outputs remain in workflow storage, and durable timers allow waits without occupying a worker. Queue-triggered workloads must explicitly deliver their final result because they lack an HTTP response channel.

Enable workflows in the skill's Markdown configuration. The runtime supplies start, status, list, cancel, and terminate management tools. Workflow handlers must be synchronous, accept one dictionary argument, return JSON-serializable data, and be idempotent because failures can cause repeated execution.

Microsoft reports token reductions of 56% and 93% in two sample sizes with gpt-5.4-mini; workload and planning overhead affect those results.

Lore relevance: separate agent planning from durable execution for scheduled sourcing and reconciliation jobs.

Source: [Original article](https://techcommunity.microsoft.com/blog/appsonazureblog/enable-dynamic-workflows-in-azure-functions-hosted-skills/4551993).
