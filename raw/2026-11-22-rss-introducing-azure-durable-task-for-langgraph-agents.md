---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-durable-task-for-langgraph-agents/4574019"
title: "Introducing Azure Durable Task for LangGraph agents"
author: "tamirdresher"
date_published: "2026-11-17"
date_clipped: "2026-11-22"
category: "Azure & Cloud"
source_type: "rss"
capture_note: "Embedded binary images omitted; descriptive alt text retained. See the source for images."
---

# Introducing Azure Durable Task for LangGraph agents

LangGraph graphs, LangChain `create_agent` workflows, and Deep Agents built with `create_deep_agent` can now use **Azure Durable Task Scheduler** to survive worker crashes and restarts, retry flaky tools independently, and pause for human approval without holding worker threads open.

The [new durable execution integration](https://docs.langchain.com/oss/python/integrations/providers/azure_ai#durable-langgraph-execution-with-azure-durable-task-scheduler) ships in `langchain-azure-compute[durabletask]` version **0.2.0+**, through `langchain_azure_compute.graph`. It is in **public preview**, so its API may change.

Your agent already looked up the order and worked out the next step. A deployment should not send it back to introductions.

## What this means for your application

**Keep the progress you have paid for.** Completed graph steps and durable tool results are persisted. When a worker restarts mid-run, another worker registered with the same graph and task hub resumes from recorded progress instead of restarting the whole graph from turn one and spending those tokens again. Interrupted work whose result was not recorded can run again.

**Isolate and retry flaky tools.** Use `durable_tool(retries=3)` to give a tool its own retry policy, with up to three attempts, or `durable_node` to isolate a graph node as an activity. One unreliable order service does not need to turn into a hand-written recovery loop around your entire agent.

**Keep people in control.** Standard LangGraph `interrupt()` pauses the orchestration on a Durable Task external event. Read the pending approval with `run.wait_pending()` and continue with `run.resume(pending, value)`. No worker thread is held open while someone takes hours or days to decide. Worker hosting and infrastructure charges still depend on your deployment.

**Separate control plane from state plane.** Keep your LangGraph checkpointer, such as `SqliteSaver`, `PostgresSaver`, or `CosmosDBSaver`. Durable Task Scheduler coordinates execution, retries, failover, and external events. Without an explicit checkpointer, the adapter supplies `InMemorySaver` and carries checkpoint bundles in DTS payloads. Persistent checkpoint storage must be accessible to every worker.

Activities run **at least once**, not exactly once. For tools that mutate external systems, use `runtime.config["metadata"]["durable_call_id"]` as a durable idempotency key and enforce deduplication at the external mutation boundary.

Keeping checkpoints in your own database does not keep every payload out of scheduler history. Durable activity inputs, outputs, and final results still pass through DTS. Review its retention and purge settings independently.

## Add durability without rewriting your graph

Call `attach_durability(agent, name="support_agent")` on an existing compiled `StateGraph`, `create_agent` workflow, or `create_deep_agent` workflow. Your graph structure, prompts, and model choice stay yours; the adapter handles the durable execution boundary.

Install the integration:

```bash
pip install -U "langchain-azure-compute[durabletask]" langchain-azure-ai
```

With Docker running, start the local scheduler emulator:

```bash
docker run --rm --pull=always --name dts-emulator -p 127.0.0.1:8080:8080 -p 127.0.0.1:8082:8082 mcr.microsoft.com/dts/dts-emulator:latest
```

Here is the quickstart, adapted from the [official LangChain documentation](https://docs.langchain.com/oss/python/integrations/providers/azure_ai#durable-langgraph-execution-with-azure-durable-task-scheduler):

```python
import os

from azure.identity import DefaultAzureCredential
from durabletask.azuremanaged.client import DurableTaskSchedulerClient
from durabletask.azuremanaged.worker import DurableTaskSchedulerWorker
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain_azure_ai.chat_models import AzureAIOpenAIApiChatModel
from langchain_azure_compute.graph import attach_durability, durable_tool, sdk_options

@durable_tool(retries=3)
@tool
def get_order_status(order_id: str) -> str:
    """Look up an order's status (replace with your order service)."""
    return f"Order {order_id} has shipped."

model = AzureAIOpenAIApiChatModel(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    use_responses_api=True,
)
agent = create_agent(model=model, tools=[get_order_status])
reg = attach_durability(agent, name="support_agent")

opts = sdk_options("127.0.0.1:8080")
worker = DurableTaskSchedulerWorker(**opts)
sdk = DurableTaskSchedulerClient(**opts)
try:
    reg.register(worker)
    worker.start()
    run = reg.client(sdk).start(
        {"messages": [HumanMessage(content="What is the status of order 42?")]}
    )
    result = run.wait_result(timeout=60)
    print(result["messages"][-1].content_blocks)
finally:
    worker.stop()
    sdk.close()
```

Set `AZURE_AI_PROJECT_ENDPOINT` and `AZURE_AI_MODEL_DEPLOYMENT_NAME` for your deployed model, then authenticate locally with `az login`. Your identity needs the Azure AI Developer role on the Foundry project. This quickstart uses a real model deployment; the screenshots below use a separate deterministic model.

## See what your agent actually did

The emulator serves the SDK on port `8080` and the **DTS Dashboard** at `http://localhost:8082`. Open an orchestration to see its step activities and durations, then select the tool activity to inspect its input and recorded output.

These screenshots were captured from a freshly pulled `latest` DTS emulator using a deterministic model and synthetic order data, `ORD-1042`. No external model API key is required to reproduce that local demonstration. The scheduler execution is real; the model responses are controlled.

[Embedded image: DTS Dashboard timeline for the completed langgraph-support-blog orchestration, named langgraph.support\_agent.run, showing three langgraph.support\_agent.step activities lasting 140 ms, 12 ms, and 34 ms, and one langgraph.support\_agent.tool activity lasting 13 ms.]

*The completed `langgraph-support-blog` (`langgraph.support_agent.run`) timeline shows the recorded `langgraph.support_agent.step` and `langgraph.support_agent.tool` activities and their millisecond durations.*

[Embedded image: DTS Dashboard details drawer for the completed langgraph.support\_agent.tool activity, showing thread langgraph-support-blog, checkpoint reference ckpt, node tools, a deterministic call\_id ending in call\_order\_1042, status ok, and MessagePack-encoded call and output envelopes.]

*The `langgraph.support_agent.tool` drawer shows `thread: "langgraph-support-blog"`, the checkpoint reference (`ckpt`), `node: "tools"`, a deterministic `call_id` ending in `call_order_1042`, and `status: "ok"`. The call and output use MessagePack envelopes (`t: "msgpack"`); the screenshot does not show decoded tool arguments or a readable shipping result. This run completed normally: it illustrates the activity timeline and payload inspection, not crash recovery.*

## Take the same graph to Azure

Connect your worker and client to [Azure Durable Task Scheduler](https://learn.microsoft.com/azure/durable-task/scheduler/durable-task-scheduler) using `sdk_options()` and `DURABLE_TASK_SCHEDULER_CONNECTION_STRING`. Use managed identity in production with the Durable Task Data Contributor role. Host your worker compute separately and open the [DTS Dashboard](https://learn.microsoft.com/azure/durable-task/scheduler/durable-task-scheduler-dashboard) from your Azure task hub.

**Start with the graph you already have.** Explore the [package guide](https://github.com/langchain-ai/langchain-azure/tree/main/libs/azure-compute#durable-langgraph-execution-durable-task-scheduler), try the [10 runnable samples](https://github.com/langchain-ai/langchain-azure/tree/main/samples/langgraph-durabletask), and find related integrations in the [Microsoft integrations hub](https://docs.langchain.com/oss/python/integrations/providers/microsoft).
