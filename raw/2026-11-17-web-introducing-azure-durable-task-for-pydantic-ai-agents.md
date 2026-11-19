---
"source": "https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-durable-task-for-pydantic-ai-agents/4571024"
"title": "Introducing Azure Durable Task for Pydantic AI agents"
"author": "tamirdresher"
"date_published": "2026-11-16"
"date_clipped": "2026-11-17"
"category": "Azure & Cloud"
"source_type": "web"
---

# Introducing Azure Durable Task for Pydantic AI agents

Pydantic AI agents can now use **Azure Durable Task Scheduler** to preserve progress across worker restarts, recover interrupted runs, and wait for human approval without keeping an activity running.

The [new Azure Durable Task integration](https://pydantic.dev/docs/ai/harness/azure-durable-task/) brings durable execution to your existing Pydantic AI agents. Add a capability to the agent, call it from a Durable Task orchestrator, and let the runtime handle recovery.

That means a deployment or worker crash does not have to turn an almost-finished agent run into another full round of model requests. Your agent already did the work. It should not need a motivational speech to remember it.

## What this means for your application

**Keep the progress you have paid for.** Completed model responses and tool results are recorded durably. Recovery reuses those recorded results instead of repeating the same calls and spending tokens again. Work interrupted before its result is recorded can execute again.

**Recover from transient failures.** Configure retry policies for model requests and tool calls, and let the runtime perform those retries automatically. You choose the policy rather than building retry loops around every step.

**Keep people in control.** An agent can prepare a proposal, pause for hours or days for approval, and continue when the decision arrives. No activity execution is held open during the wait. Worker hosting and infrastructure charges still depend on your deployment.

**Coordinate more than one agent.** Use Durable Task workflows to combine specialist agents, sequence their work, and bring their results together. The integration makes their agent runs durable; you decide how they collaborate.

For tools that change external systems, such as creating an order, keep those operations idempotent. Durable recovery does not guarantee exactly-once side effects.

## Add durability without rewriting your agent

A Pydantic AI [Capability](https://pydantic.dev/docs/ai/core-concepts/capabilities/) is a reusable extension that adds behavior to an agent, such as tools, instructions, or lifecycle hooks. **Durability ships as a Capability, not a replacement agent framework.**

Attach `AzureDurableTaskDurability` through `capabilities=[durability]`. By default, model requests, function-tool calls, and MCP calls become checkpointed Durable Task activities. You do not rewrite your prompts or existing tool functions as workflow steps.

Here is the core change, adapted from the [Pydantic AI quickstart](https://pydantic.dev/docs/ai/harness/azure-durable-task/#run-locally):

```python
import os

from pydantic_ai import Agent
from pydantic_ai_harness.azure_durable_task import (
    AzureDurableTaskDurability,
    run_durable,
)

durability = AzureDurableTaskDurability()
agent = Agent(
    os.environ['PYDANTIC_AI_MODEL'],
    name='support_agent',
    capabilities=[durability],
)

def support(ctx, prompt):
    result = yield from run_durable(ctx, lambda: agent.run(prompt))
    return result.output
```

Your model, instructions, and tools stay in Pydantic AI. The complete quickstart registers the agent's bound capability on a worker and adds a client to schedule this orchestrator. This uses the standalone Durable Task Python SDK, without needing an Azure Functions app.

## Try it locally, then connect to Azure

Use Python 3.11 or later and install the integration. This example includes the OpenAI provider:

```bash
pip install "pydantic-ai-harness[azure-durable-task]>=0.66.0" "pydantic-ai-slim[openai]"
```

With Docker running, start the Durable Task Scheduler emulator:

```bash
docker run --rm --pull=always --name dts-emulator -p 127.0.0.1:8080:8080 -p 127.0.0.1:8082:8082 mcr.microsoft.com/dts/dts-emulator:latest
```

Set `OPENAI_API_KEY` securely and set `PYDANTIC_AI_MODEL` to an accessible model in `openai:<model-id>` format. Follow the [complete local example](https://pydantic.dev/docs/ai/harness/azure-durable-task/#run-locally) to start the worker and schedule a run.

## See what your agent actually did

The emulator exposes the SDK on port `8080` and the **DTS Dashboard** at `http://localhost:8082`. Enable auto-refresh to watch orchestration instances move through statuses such as `Pending`, `Running`, `Completed`, or `Failed`.

Open an instance's timeline to see the individual model, tool, and MCP activities created by the capability. Select a step to inspect its inputs and outputs, and use the timeline and history to examine duration and retry attempts. You can see which operation failed without reconstructing the conversation from logs.

For these screenshots, I extended the quickstart with a `lookup_order` tool and ran it against a freshly pulled `latest` emulator with the redesigned dashboard. A deterministic `FunctionModel` supplies the model responses, and the order data is synthetic, so no external model API key is needed. The scheduler execution and dashboard captures are real.

*The completed `support_workflow`: two `support_agent__model.request` activities around a function-tool activity.*

*Open the tool step to see `lookup_order` receive `ORD-1042` and return its shipping details. This run completed normally; it does not demonstrate retries or crash recovery.*

When you are ready for Azure, use the Azure-managed worker and client with `DefaultAzureCredential`. Open the same [DTS Dashboard experience](https://learn.microsoft.com/en-us/azure/durable-task/scheduler/durable-task-scheduler-dashboard) from your task hub in the Azure portal, with the required dashboard access. Your agent and orchestrator stay the same. The [deployment guide](https://pydantic.dev/docs/ai/harness/azure-durable-task/#deploy-to-azure-durable-task-scheduler) covers scheduler setup and permissions; deploy your worker compute separately.

**Start with the agent you already have.** Add durable execution where a restart would otherwise lose useful work, then build in the retries, approvals, and specialist coordination your application needs.

Get started with the [Pydantic AI Azure Durable Task guide](https://pydantic.dev/docs/ai/harness/azure-durable-task/).
