---
source: "https://devblogs.microsoft.com/azure-sdk/long-running-mcp-tools-azure-functions"
title: "How to build long-running MCP tools on Azure Functions"
author: "Azure Blog"
date_published: "2026-07-16"
date_clipped: "2026-08-14"
category: "Azure & Cloud"
source_type: "rss"
---

# How to build long-running MCP tools on Azure Functions

Source: https://devblogs.microsoft.com/azure-sdk/long-running-mcp-tools-azure-functions

Recently, a customer building servers with the Azure Functions Model Context Protocol (MCP) extension reached out and asked: How do I handle tools that take longer than the client is willing to wait? This becomes especially relevant when tool calls move beyond simple request/response into multi-step workflows and long-running operations.
At the same time, MCP is evolving to address exactly this. The Tasks extension is introduced in the 2026-07-28 release candidate , defining a standard way to model long-running work.
In this post, we’ll walk through how to build long-running MCP tools on Azure Functions using Durable Functions , a framework for authoring stateful, long-running workflows as ordinary code, with checkpointing, scaling, and recovery handled automatically.
MCP tools today
Today, MCP tools are fundamentally request/response:
the client issues a tools/call
the server returns a result
This works well for fast operations, but breaks down when:
workflows take minutes
execution depends on multiple steps
latency is unpredictable
In practice, clients enforce their own tool-call timeouts. These aren’t standardized by the MCP spec and vary per client, but they’re often in the ~30–60 second range. If a tool exceeds that window:
the client times out
the agent observes a failed call
the underlying work may still be running
So the core issue is that synchronous tool calls don’t naturally model long-running work.
The MCP Tasks extension
The Tasks extension addresses this. With the extension, a server can respond to a tools/call with an asynchronous task handle instead of a final result, and the client drives the lifecycle from there:
tasks/get : poll the task’s status
tasks/update : submit input back to the server if the task reaches input_required
tasks/cancel : cancel an in-flight task
A task carries a status ( working , input_required , completed , failed , or cancelled ) and, on completion, the final result. Task creation is server-directed, meaning the client advertises support by including the extension in its per-request capabilities, and the server decides per request whether to return a task. A server won’t return a task to a client that hasn’t advertised support.
It’s important to note that Tasks rely on ecosystem support. Clients must advertise the extension, and MCP Software Development Kits (SDKs) must implement the task lifecycle, before servers can use it. So while Tasks is now a defined extension, broad client and SDK support is still in progress.
Implement long-running tasks with Durable Functions today
Until the Tasks extension is broadly supported across clients, we need a pattern that works with existing request/response clients and supports long-running execution. The following samples show how, using Durable Functions:
Python
.NET
The long-running work in this sample mines a short chain of blocks. Each block requires solving a computational puzzle where the system keeps trying different inputs until it finds one that produces a result matching a specific pattern (for example, starting with a certain number of zeros). Because this involves lots of trial and error, it naturally takes time, making it a good example of a long-running workflow.
The server in the sample exposes two tools:
start_mining
Starts a Durable Functions orchestration to mine the blocks
Waits briefly (within a configurable budget)
Returns the result inline if completed within budget, or returns a workflow_id if still running
get_mining_result
Takes the workflow_id
Returns the current state, for example completed , running , failed , or not_found
To ensure that the agent calls the tools in the right order, workflow_id is a required parameter of get_mining_result , so the agent can’t poll without starting a mining run first. Also, the running response carries a poll_after_seconds value and a next instruction, prompting the agent to poll again if work isn’t done rather than give up or assume completion.
Even so, the poll path still relies on the agent correctly remembering, and not hallucinating, the workflow_id it was handed. If it garbles or invents an id, the poll lands on the wrong instance or none at all (which is why get_mining_result returns not_found rather than guessing).
What changes with the Tasks extension
Once the Tasks extension is fully implemented across clients and SDKs, the model becomes simpler and more reliable; the server returns a Task handle, the client manages the polling and lifecycle calls, and the SDK tracks execution state. This removes a key limitation of today’s solution, which requires the agent to remember and correctly pass identifiers like workflow_id .
Call to action
Try out the sample and let us know whether it addresses your MCP needs around long-running or workflow-type tools!
