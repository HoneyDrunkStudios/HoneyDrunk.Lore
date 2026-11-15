---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/durable-task-extension-for-microsoft-agent-framework-is-now-generally-available/4571100"
title: "Durable Task extension for Microsoft Agent Framework is now Generally Available"
author: "NickGreenfield"
date_published: "2026-11-09"
date_clipped: "2026-11-15"
category: "Software Architecture"
source_type: "web"
---

# Durable Task extension for Microsoft Agent Framework is now Generally Available

## Building an agent that gives a great answer is one thing. Building one that can recover from failures and interruptions and pick up long-running work without starting over is another...

Today, we’re excited to announce the general availability of the [Durable Task extension for Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/hosting/azure-functions?tabs=bash&pivots=programming-language-csharp). It brings the reliable execution model of [Durable Task](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler) to [Agent Framework](https://learn.microsoft.com/en-us/agent-framework/), helping agents and agentic workflows recover from failures and interruptions without losing their progress.

Saving a conversation is only part of the story. When an agent is doing work, your application also needs to know which steps have finished, which jobs are still running, and whether it’s waiting for someone’s approval. If the application restarts, that information makes the difference between continuing the work and figuring out where to begin again.

The Durable Task extension keeps track of that state for you. Agents can continue the same conversation after a worker restart, and workflows can pick up interrupted work without repeating steps whose results have already been saved. They can also wait for approvals or external events without keeping a worker running. You can focus on what your agents do, with less state management and recovery code to build yourself.

Run durable agents and workflows in [Azure Functions](https://learn.microsoft.com/azure/azure-functions/functions-overview), or self-host them in your own .NET or Python application.

## Key capabilities of the Durable Task extension

The Durable Task extension adds two capabilities to [Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/) that work together: durable agents and durable workflows.

**Durable agents** keep conversation and session state between requests. Each agent call runs through Durable Task, so saved session state stays available even if a worker restarts or another application instance handles the next request. The conversation can continue without relying on the original process.

**Durable workflows** keep track of work that takes multiple steps or runs over time. You can write [Durable Task orchestrations](https://learn.microsoft.com/azure/durable-task/sdks/durable-task-overview) to coordinate agent calls, application activities, and external events. If you prefer [Agent Framework’s graph-based workflows](https://learn.microsoft.com/agent-framework/workflows/), the extension runs those graphs as Durable Task orchestrations and handles registration of their agents and executors.

The two come together when an interactive agent needs to start work that won’t finish in a single request. The agent can launch a workflow and return its instance ID rather than keep the user waiting. The workflow continues independently, including waiting for results or approvals. The agent can use that ID later to check progress or send an event, such as an approval decision.

The examples below show how this works in practice: continuing a conversation, coordinating work across multiple steps, waiting for someone’s input, and managing session state and model context. Later in the post, we’ll show how to set up the host that runs these examples.

### Agent sessions that survive interruptions

Suppose a customer starts a support conversation, then comes back with their order number. In between, your application restarts or another worker takes over. The agent should be able to pick up the conversation where it left off.

Agent Framework can keep sessions in memory or use a persistent history provider to save messages between requests. A durable agent builds on that with a managed path for running agent calls and restoring session state, so you don’t have to wire that together yourself.

With the Durable Task extension, each conversation has a stable durable session ID, and saved session state lives outside the worker process. Your application keeps the session reference. When the customer returns, another compatible worker can use that reference to continue the same conversation.

The examples below show two separate requests. The first starts the conversation and serializes its session reference, which your application must save for later use. Serialization alone does not save it. The later request loads that reference and reconnects to the same durable session, without needing the original session object. Both requests use the same Durable Task backend, with SupportAgent registered through the extension.

#### C#

```
using System.Text.Json;
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.DurableTask;

// First request: start the conversation and return its session object.
static async Task<JsonElement> StartConversationAsync(
    IServiceProvider services)
{
    AIAgent agent = services.GetDurableAgentProxy("SupportAgent");
    AgentSession session = await agent.CreateSessionAsync();

    await agent.RunAsync(
        "I need help with my order.",
        session: session);

    // SerializeSessionAsync returns only the lightweight JSON session reference
    // (containing the durable session ID); Durable Task already stores the
    // conversation history in the backend.
    return await agent.SerializeSessionAsync(session);
}

// Later request, after a restart or on another compatible worker.
// Load savedSession from your application's durable storage before calling.
static async Task<AgentResponse> ContinueConversationAsync(
    IServiceProvider services,
    JsonElement savedSession)
{
    AIAgent agent = services.GetDurableAgentProxy("SupportAgent");
    AgentSession session = await agent.DeserializeSessionAsync(savedSession);

    return await agent.RunAsync(
        "The order number is 12345.",
        session: session);
}
```

#### Python

```
from typing import Any

from agent_framework import AgentResponse
from agent_framework_durabletask import (
    DurableAIAgentClient,
    DurableAgentSession,
)

# First request: start the conversation and return its serialized session reference.
def start_conversation(
    durable_client: DurableAIAgentClient,
) -> dict[str, Any]:
    agent = durable_client.get_agent("SupportAgent")
    session = agent.create_session()

    agent.run("I need help with my order.", session=session)

    # to_dict() returns only the lightweight session reference dict (containing
    # durable_session_id); Durable Task already stores the conversation history
    # in the backend.
    return session.to_dict()

# Later request, after a restart or on another compatible worker.
def continue_conversation(
    durable_client: DurableAIAgentClient,
    saved_session: dict[str, Any],
) -> AgentResponse:
    agent = durable_client.get_agent("SupportAgent")
    session = DurableAgentSession.from_dict(saved_session)

    return agent.run("The order number is 12345.", session=session)
```

### Coordinate multi-step agentic workflows reliably

A simple customer question can lead to several steps: look up records, prepare a response, and send it to the right person or system. If something interrupts the process halfway through, your application needs to know what has already finished and what still needs to happen.

Durable Task saves the results of agent calls and activities as the workflow progresses. After an interruption, the orchestration replays its history, reuses saved results, and continues with unfinished work. Completed agent calls whose results have been recorded don’t need to call the model again during replay, avoiding unnecessary token usage and inference costs during recovery.

#### C#

```
// Registered as the Durable Task orchestration for this workflow.
static async Task<string> RunOrderResponseWorkflowAsync(
    TaskOrchestrationContext context,
    string orderNumber)
{
    DurableAIAgent agent = context.GetAgent("OrderAgent");
    AgentSession session = await agent.CreateSessionAsync();

    AgentResponse<TextResponse> summary = await agent.RunAsync<TextResponse>(
        message: $"Summarize order {orderNumber}.",
        session: session);

    AgentResponse<TextResponse> reply = await agent.RunAsync<TextResponse>(
        message: $"Draft a customer reply: {summary.Result.Text}",
        session: session);

    return reply.Text;
}
```

#### Python

```
# Registered as the Durable Task orchestration for this workflow.
def run_order_response_workflow(
    context: OrchestrationContext,
    order_number: str,
):
    agent_context = DurableAIAgentOrchestrationContext(context)
    agent = agent_context.get_agent("OrderAgent")
    session = agent.create_session()

    summary = yield agent.run(
        messages=f"Summarize order {order_number}.",
        session=session,
    )

    reply = yield agent.run(
        messages=f"Draft a customer reply: {summary.text}",
        session=session,
    )

    return reply.text
```

### Make graph-based workflows durable

If you prefer to build workflows as graphs in Agent Framework, you can use that approach too. The Durable Task extension runs your graph as a durable orchestration, keeping track of its progress so it can recover from failures and interruptions.

You only need to register the graph. The extension takes care of registering its agents, activities for the other executors, and the orchestration that runs it.

#### C#

```
Workflow expertTeamWorkflow = new WorkflowBuilder(questionParser)
    .WithName("ExpertTeamReview")
    .AddFanOutEdge(questionParser, [biologist, physicist])
    .AddFanInBarrierEdge([biologist, physicist], responseAggregator)
    .Build();

services.ConfigureDurableWorkflows(
    options => options.AddWorkflow(expertTeamWorkflow));
```

#### Python

```
expert_team_workflow = (
    WorkflowBuilder(
        name="ExpertTeamReview",
        start_executor=question_parser,
    )
    .add_fan_out_edges(
        source=question_parser,
        targets=[biologist, physicist],
    )
    .add_fan_in_edges(
        sources=[biologist, physicist],
        target=response_aggregator,
    )
    .build()
)

# agent_worker wraps the Durable Task worker.
agent_worker.configure_workflow(expert_team_workflow)
```

As agents and executors finish their work, Durable Task saves their results and reuses them during replay. You define how the work connects in the graph, and Durable Task handles preserving progress and recovering execution.

### Human in the loop

Sometimes an agent needs someone to review a draft, approve an action, or provide more information before the work can continue. That response might take an hour, a day, or longer. Keeping a worker running just to wait can add cost and prevent the application from scaling down.

With the Durable Task extension, the workflow can save its progress and wait for an external event without keeping a worker active. When the person responds, an HTTP endpoint, agent tool, or other application code sends the event to the matching workflow instance. The orchestration picks up from its saved state and continues the work.

#### C#

```
// Registered as the Durable Task orchestration for this workflow.
static async Task<string> RunContentReviewWorkflowAsync(
    TaskOrchestrationContext context,
    GeneratedContent draft)
{
    await context.CallActivityAsync(nameof(NotifyReviewer), draft);

    HumanApprovalResponse decision = await context.WaitForExternalEvent<HumanApprovalResponse>(
        eventName: "HumanApproval",
        timeout: TimeSpan.FromHours(24));

    if (!decision.Approved)
        return "Content was not approved.";

    await context.CallActivityAsync(nameof(PublishContent), draft);

    return "Content published.";
}

// From the approval endpoint or agent tool, outside the orchestration:
await client.RaiseEventAsync(instanceId, "HumanApproval", approvalResponse);
```

#### Python

```
# Registered as the Durable Task orchestration for this workflow.
def run_content_review_workflow(
    context: OrchestrationContext,
    draft: dict[str, str],
):
    yield context.call_activity("notify_reviewer", input=draft)

    decision = yield context.wait_for_external_event("HumanApproval")

    if not decision["approved"]:
        return {"status": "not-approved"}

    yield context.call_activity("publish_content", input=draft)

    return {"status": "published"}

# From the approval endpoint or agent tool, outside the orchestration:
client.raise_orchestration_event(
    instance_id=instance_id,
    event_name="HumanApproval",
    data={"approved": True},
)
```

## Observe agents and workflows in one place

When your application uses the Durable Task Scheduler as the durable backend, you can see what your agents and workflows are doing in the [Durable Task Scheduler dashboard](https://learn.microsoft.com/azure/durable-task/scheduler/durable-task-scheduler-dashboard), whether they run in Azure Functions or a self-hosted application.

Open an agent session to review its conversation history, see the timeline of its execution, and check reported token usage.

For workflows, you can check their status and see how the work has progressed through the timeline, event history, and flow views. Open an individual step to inspect its inputs and outputs, understand what happened, or investigate a failure.

# Build with the Durable Task extension

You can run durable agents and workflows in [Azure Functions](https://learn.microsoft.com/azure/azure-functions/functions-overview), or host them in your own .NET or Python application.

The examples below show how to register your agents and workflows with the host that runs them. They assume you’ve already defined the agents, workflow graphs, and orchestration functions.

| Hosting environment | .NET | Python |
| --- | --- | --- |
| Azure Functions | [Microsoft.Agents.AI.Hosting.AzureFunctions](https://www.nuget.org/packages/Microsoft.Agents.AI.Hosting.AzureFunctions) | [agent-framework-azurefunctions](https://pypi.org/project/agent-framework-azurefunctions/) |
| Self-hosted applications | [Microsoft.Agents.AI.DurableTask](https://www.nuget.org/packages/Microsoft.Agents.AI.DurableTask) | [agent-framework-durabletask](https://pypi.org/project/agent-framework-durabletask/) |

### Azure Functions

Azure Functions gives you managed HTTP endpoints and scales with demand. To get started, add Microsoft.Agents.AI.Hosting.AzureFunctions for .NET or agent-framework-azurefunctions for Python to your Functions project, and configure its Durable Task backend.

#### C# example for Azure Functions

Register standalone agents and agents used by your own orchestrations with ConfigureDurableAgents. For Agent Framework workflow graphs, use ConfigureDurableWorkflows. You can use either method on its own or combine them to host agents and graphs in the same application.

```
using IHost app = FunctionsApplication
    .CreateBuilder(args)
    .ConfigureFunctionsWebApplication()
    .ConfigureDurableAgents(options => options.AddAIAgent(agent))
    .ConfigureDurableWorkflows(options => options.AddWorkflow(workflow))
    .Build();

app.Run();
```

For a Durable Task orchestration, mark its entry point with [Function] and [OrchestrationTrigger] so Azure Functions can discover it. If you register an Agent Framework graph, the extension creates the supporting orchestration for you.

#### Python

Pass standalone agents and agents used by your own orchestrations to AgentFunctionApp through the agents argument. For an Agent Framework graph, use the workflow argument. You can provide either or both.

```
from agent_framework_azurefunctions import AgentFunctionApp

app = AgentFunctionApp(
    agents=[agent],
    workflow=workflow,
)
```

For a Durable Task orchestration, mark its entry point with [app​](javascript:void(0)).orchestration\_trigger(context\_name="context"). For an Agent Framework graph, AgentFunctionApp adds that trigger for you.

The [C# Functions samples](https://github.com/microsoft/agent-framework-durable-extension/tree/main/dotnet/samples/DurableAgents/AzureFunctions) and [Python Functions samples](https://github.com/microsoft/agent-framework-durable-extension/tree/main/python/samples/azure_functions) show the full project setup and how to call your agents and workflows.

### Self-hosted applications

You can also run durable agents and workflows in your own application with Microsoft.Agents.AI.DurableTask for .NET or agent-framework-durabletask for Python. You choose where the application runs and how users or other systems call it. Durable Task handles saving execution state and recovering work after interruptions.

#### C# example for self-hosted applications

Configure the Durable Task worker and client, register your agents, and add any Agent Framework graphs.

```
using IHost host = Host.CreateDefaultBuilder(args)
    .ConfigureServices(services =>
    {
        services.ConfigureDurableAgents(
            options => options.AddAIAgent(agent),
            workerBuilder: builder => builder.UseDurableTaskScheduler(connectionString),
            clientBuilder: builder => builder.UseDurableTaskScheduler(connectionString));

        services.ConfigureDurableWorkflows(
            options => options.AddWorkflow(workflow));
    })
    .Build();

await host.RunAsync();
```

For a Durable Task orchestration, also register it through AddTasks in the workerBuilder callback. For example, this registers the earlier order-response function and passes it the orchestration input:

```
workerBuilder: builder =>
{
    builder.UseDurableTaskScheduler(connectionString);

    builder.AddTasks(registry => registry.AddOrchestratorFunc(
        "RunOrderResponseWorkflow",
        (TaskOrchestrationContext context) => RunOrderResponseWorkflowAsync(
            context,
            context.GetInput<string>() ?? throw new ArgumentException(
                "An order number is required."))));
}
```

The scheduler integration requires Microsoft.DurableTask.Worker.AzureManaged and Microsoft.DurableTask.Client.AzureManaged alongside the extension.

#### Python example for self-hosted applications

Pass your configured Durable Task worker to DurableAIAgentWorker, then register your agents, orchestrations, and workflow graphs before starting the worker.

```
from agent_framework_durabletask import DurableAIAgentWorker

agent_worker = DurableAIAgentWorker(worker)

# Register an agent and an orchestration you wrote directly.
agent_worker.add_agent(order_agent)
worker.add_orchestrator(run_order_response_workflow)

# Register a graph and let the extension configure its components.
agent_worker.configure_workflow(workflow)

worker.start()
```

Register only the components your application needs, or combine them in the same worker. Your application keeps the worker running and calls worker.stop() when it shuts down.

When you deploy, configure your Durable Task Scheduler endpoint, task hub, and authentication. [Durable Task Scheduler](https://learn.microsoft.com/azure/durable-task/scheduler/durable-task-scheduler) is the recommended backend for Durable Functions and the Durable Task SDKs.

### Start with a sample

You don’t have to start from scratch. Pick a sample for your language and hosting environment, and build from there:

- [.NET Azure Functions samples](https://github.com/microsoft/agent-framework-durable-extension/tree/main/dotnet/samples/DurableAgents/AzureFunctions)

- [.NET self-hosted samples](https://github.com/microsoft/agent-framework-durable-extension/tree/main/dotnet/samples/DurableAgents/ConsoleApps)

- [Python Azure Functions samples](https://github.com/microsoft/agent-framework-durable-extension/tree/main/python/samples/azure_functions)

- [Python Durable Task samples](https://github.com/microsoft/agent-framework-durable-extension/tree/main/python/samples)

Read the [Durable Task extension documentation](https://learn.microsoft.com/agent-framework/hosting/azure-functions) to get started, and share feedback or contribute in the [Microsoft Agent Framework Durable Task extension repository](https://github.com/microsoft/agent-framework-durable-extension)
