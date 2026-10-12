---
source: "https://devblogs.microsoft.com/azure-sdk/azure-functions-agent-binding"
title: "Bring agentic reasoning to Python function apps with Azure Functions Agent bindings (preview)"
author: "Victoria Hall"
date_published: "2026-10-06"
date_clipped: "2026-10-12"
category: "Azure & Cloud"
source_type: "rss"
---

# Bring agentic reasoning to Python function apps with Azure Functions Agent bindings (preview)

Azure Functions applications already have a strong model for event-driven work: a trigger starts the function, bindings connect it to other services, and application code validates input and controls the result. AI reasoning doesn’t need to replace that model.

Agent bindings for Python function apps add reasoning as a bounded step inside it. The binding constructs a Microsoft Agent Framework `Agent` from Markdown instructions and injects it into a Python handler. The handler still decides what data the Agent sees, when to invoke it, and what to do with the response.

The same model also works in Durable Functions. An orchestrator can schedule replay-safe Agent calls alongside regular activities, allowing a workflow to persist progress and continue after its original request ends.

> **Note**
>
> Agent bindings are in preview. Microsoft Agent Framework is currently the only supported provider, and Python 3.13 or later is required.

## Why use an Agent binding?

Most production AI workflows contain two different classes of work.

Deterministic code should own operations with a precise contract: parsing a request, validating a schema, enforcing authorization, calculating values, selecting fields, branching on known state, and writing a response. Agent reasoning is useful when the application needs to interpret context, classify content, summarize evidence, or make a bounded recommendation.

Consider an order-processing API. The function can validate the order and reduce it to the fields relevant to fulfillment. An Agent can then assess operational risk and identify missing context. The function owns the HTTP contract and decides how that assessment affects later processing.

This separation has practical benefits:

* Existing HTTP, queue, timer, Event Grid, and Service Bus triggers continue to work as they do in any Python v2 function app.
* Deterministic code controls the trust boundary and limits the data sent to the model.
* Agent instructions remain separate from runtime and model configuration.
* The handler can invoke the Agent conditionally, inspect its response, combine it with other results, or skip it entirely.
* The same Agent definition can participate in a Durable Functions orchestration when the process becomes stateful or long-running.

## Project anatomy

An Agent-enabled project is a standard Python v2 function app with a provider package and one or more instruction files:

```
agent-binding-app/
├── function_app.py
├── host.json
├── requirements.txt
├── local.settings.json
├── order-fulfillment.agent.md
├── skills/                         # Optional skills Agent Skills
│   └── fulfillment-policy/
│       └── SKILL.md
└── mcp.json                        # Optional remote MCP servers
```

The main pieces have distinct responsibilities:

| Component | Responsibility |
| --- | --- |
| `function_app.py` | Defines triggers, deterministic logic, the client factory, and Agent invocation. |
| `order-fulfillment.agent.md` | Contains raw UTF-8 instructions for one Agent. |
| `requirements.txt` | Selects the Agent provider and client packages. |
| `local.settings.json` | Supplies local storage, Foundry project, and model settings. Don’t commit this file. |
| `skills/` | Optionally provides file-based Skills discovered by the provider. |
| `mcp.json` | Optionally configures remote MCP servers and tool allowlists. |

An Agent name resolves to exactly one instruction file. For example, `agent_name="order-fulfillment"` resolves either `order-fulfillment.agent.md` in the app root or `agents/order-fulfillment.agent.md`.

## Add an Agent to an HTTP-triggered function

This approach is useful when Agent reasoning can complete within the current function invocation and its result belongs in the immediate response.

Before starting the walkthrough, you need an Azure subscription and a Microsoft Foundry project with a deployed model. You also need Azure Functions Core Tools, Azurite or an Azure Storage account, and the Azure CLI. Your local identity must have access to the Foundry project.

### Install the provider and client packages

The example uses Python 3.13 or later and a Microsoft Foundry model through Microsoft Agent Framework. Its `requirements.txt` contains:

```
azure-functions
azurefunctions-agents-extensions-agent-framework[mcp]
agent-framework-foundry
azure-identity
```

`azurefunctions-agents-extensions-agent-framework` integrates the binding with Microsoft Agent Framework, and its `mcp` extra installs the optional dependencies used to discover remote MCP servers from `mcp.json`. `agent-framework-foundry` supplies `FoundryChatClient`, while `azure-identity` supplies the credential used to authenticate during local development.

Configure the corresponding values in `local.settings.json`:

```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "FOUNDRY_PROJECT_ENDPOINT": "https://<resource-name>.services.ai.azure.com/api/projects/<project-name>",
    "FOUNDRY_MODEL": "<model-deployment-name>"
  }
}
```

`AzureWebJobsStorage` points the local Functions host to Azurite.

### Define the Agent instructions

Create `order-fulfillment.agent.md` in the app root:

```
You are an order fulfillment specialist.
The supplied order has already been validated and minimized by application code.
Treat the supplied fields as trusted facts. Explain operational risk, identify
missing fulfillment context, and return a concise, actionable response.
```

The extension passes the entire file to the provider as Agent instructions. It doesn’t parse YAML front matter, model configuration, or tool declarations from this file. Model selection belongs in the client factory, and Python tools remain explicit application configuration.

### Configure the chat client

`AgentFunctionApp` accepts a zero-argument client factory. This example creates a Foundry client from environment settings and authenticates with `DefaultAzureCredential`:

```
def create_chat_client():
    from agent_framework.foundry import FoundryChatClient
    from azure.identity.aio import DefaultAzureCredential

    return FoundryChatClient(
        project_endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
        model=os.environ["FOUNDRY_MODEL"],
        credential=DefaultAzureCredential(),
    )
```

The extension invokes this factory for each function invocation. That gives each invocation its own live client, Agent, and credential resources, which the extension closes when execution ends.

### Keep deterministic preparation in code

Before invoking the Agent, select the fields needed for the assessment:

```
def prepare_order(payload: dict, order_id: str) -> dict:
    return {
        "order_id": order_id,
        "customer_id": payload["customer"]["id"],
        "currency": str(payload.get("currency", "USD")).upper(),
        "shipping_country_or_region": payload["shipping"]["country_or_region"],
        "shipping_method": payload["shipping"]["method"],
        "items": payload["items"],
    }
```

This helper is intentionally ordinary Python. It creates an explicit boundary between incoming application data and model input. Production applications can apply schema validation, authorization, calculated fields, and stricter data minimization at this point.

### Bind and invoke the Agent

Create `AgentFunctionApp`, retain the standard HTTP trigger, and add `markdown_agent`:

```
app = AgentFunctionApp(client_factory=create_chat_client)

@app.route(route="orders/{orderId}", methods=["POST"])
@app.markdown_agent(
    arg_name="order_agent",
    agent_name="order-fulfillment",
)
async def process_order(
    req: func.HttpRequest,
    order_agent: Agent,
) -> func.HttpResponse:
    try:
        prepared_order = prepare_order(
            req.get_json(),
            req.route_params["orderId"],
        )
    except (KeyError, TypeError, ValueError):
        return func.HttpResponse(
            body=json.dumps({"error": "Order failed validation."}),
            status_code=400,
            mimetype="application/json",
        )

    response = await order_agent.run(
        json.dumps(
            {
                "order": prepared_order,
                "task": "assess fulfillment readiness",
            }
        )
    )
    return func.HttpResponse(
        body=json.dumps(
            {
                "order_id": prepared_order["order_id"],
                "assessment": response.text,
            }
        ),
        mimetype="application/json",
    )
```

Two names connect the decorator to the function:

* `arg_name="order_agent"` must match the injected handler parameter.
* `agent_name="order-fulfillment"` identifies the instruction file without the `.agent.md` suffix.

The Agent doesn’t run automatically when the function starts. The handler explicitly calls `await order_agent.run(...)`, which makes the reasoning boundary visible and testable in application code.

## What happens during an invocation

When the Functions host compiles the binding, it validates the handler shape and Agent definition. At invocation time, the extension:

1. Resolves and loads the requested instruction file.
2. Calls the configured factory to create the chat client.
3. Combines the instructions with explicitly configured Python tools and any discovered Skills or MCP servers.
4. Constructs the Microsoft Agent Framework `Agent` and injects it into the named handler parameter.
5. Closes invocation-owned resources after success, failure, or cancellation.

Compiled definitions and provider discovery can be cached, but live clients and credentials aren’t reused across function invocations. The function continues to own its trigger, validation, control flow, error handling, and output.

## Move the Agent into a durable workflow

A direct call fits a bounded request-response operation. The order process can eventually require more: prepare the order, assess fulfillment risk, run inventory or policy checks, wait for an external system, and publish a final result after the initiating request has ended.

Durable Functions provides persisted orchestration state for that workflow. To enable the integration, install the provider with its Durable extra:

```
azure-functions
azurefunctions-agents-extensions-agent-framework[durable,mcp]
agent-framework-foundry
azure-identity
```

The `durable` extra installs the Durable Functions support used by `AgentFunctionApp`, while `mcp` retains the optional MCP discovery support from the direct scenario.

### Start the orchestration

The HTTP starter uses the standard Durable client binding. It validates that the request contains JSON, starts `order_orchestrator`, and returns the management payload:

```
@app.route(route="orders/orchestrations", methods=["POST"])
@app.durable_client_input(client_name="client")
async def start_order_orchestration(
    req: func.HttpRequest,
    client: df.DurableFunctionsClient,
) -> func.HttpResponse:
    try:
        order = req.get_json()
    except ValueError:
        return func.HttpResponse(
            body=json.dumps({"error": "Order failed validation."}),
            status_code=400,
            mimetype="application/json",
        )

    instance_id = await client.start_new(
        "order_orchestrator",
        client_input=order,
    )
    management = client.create_http_management_payload(req, instance_id)
    return func.HttpResponse(
        body=json.dumps(management),
        status_code=202,
        mimetype="application/json",
        headers={
            "Location": management["statusQueryGetUri"],
            "Retry-After": "10",
        },
    )
```

The `202 Accepted` response decouples the workflow lifetime from the HTTP request. Callers can use `statusQueryGetUri` to observe the instance and retrieve its final output.

### Prepare model input in an activity

Move order preparation into a standard activity:

```
@app.activity_trigger(input_name="order")
def prepare_order_activity(order: dict) -> dict:
    return {
        "order_id": order["order_id"],
        "customer_id": order["customer"]["id"],
        "currency": str(order.get("currency", "USD")).upper(),
        "shipping_country_or_region": order["shipping"]["country_or_region"],
        "shipping_method": order["shipping"]["method"],
        "items": order["items"],
    }
```

Activities are the correct place for validation, calculations, data minimization, and other work that shouldn’t run in the orchestrator itself.

### Schedule Agent reasoning from the orchestrator

The orchestrator coordinates the activity and Agent call:

```
@app.orchestration_trigger(context_name="context")
def order_orchestrator(context: DurableAgentContext):
    prepared_order = yield context.call_activity(
        "prepare_order_activity",
        context.get_input(),
    )

    assessment = yield context.call_agent(
        "order-fulfillment",
        {
            "order": prepared_order,
            "task": "assess fulfillment risk",
        },
    )
    return {
        "order_id": prepared_order["order_id"],
        "risk_assessment": assessment,
    }
```

`context.call_agent()` takes the logical Agent name and a JSON-compatible input. The orchestration can use its result in later activities, pass it to another bounded reasoning step, or return it as the workflow output.

## How Agent calls work in an orchestration

Durable Functions orchestrators replay to reconstruct state, so model and network operations can’t run directly in orchestrator code. `context.call_agent()` handles this boundary by scheduling an extension-managed activity that loads the Agent instructions, creates the client and Agent, invokes the model, and returns a JSON-serializable result.

The result is recorded in orchestration history and reused during replay instead of repeating the model call. This makes Agent reasoning a natural fit within a durable workflow: activities can prepare trusted data, the Agent can perform a bounded reasoning task, and later steps can act on the result while the orchestrator remains deterministic.

## Run the examples locally

Before starting the app, run `az login` so `DefaultAzureCredential` can use your Azure CLI identity to access the Foundry project. Start Azurite for local storage and then start the host:

```
azurite --silent --location .azurite
```

In another terminal:

```
func start
```

Invoke the direct HTTP function:

```
curl -X POST http://localhost:7071/orders/42 \
  -H "Content-Type: application/json" \
  -d '{"customer":{"id":"C-1007"},"currency":"usd","shipping":{"country_or_region":"ca","method":"overnight"},"items":[{"sku":"A-100","quantity":2,"unit_price":"24.95"}]}'
```

The response includes the route order ID and model-generated assessment:

```
{
  "order_id": "42",
  "assessment": "<model-generated fulfillment assessment>"
}
```

For the Durable path, include the order ID in the request body because the starter doesn’t receive it as a route parameter:

```
curl -X POST http://localhost:7071/orders/orchestrations \
    -H "Content-Type: application/json" \
    -d '{"order_id":"42","customer":{"id":"C-1007"},"currency":"usd","shipping":{"country_or_region":"ca","method":"overnight"},"items":[{"sku":"A-100","quantity":2,"unit_price":"24.95"}]}'
```

The starter returns the instance ID and management URLs. Poll `statusQueryGetUri` until `runtimeStatus` becomes `Completed`, and then read the `risk_assessment` from the orchestration output.

## Get started

Agent bindings let a Python function keep deterministic code in control while delegating a clearly defined reasoning task to Microsoft Agent Framework. Start with direct invocation when the result belongs in the current function execution. Add Durable Functions when the surrounding process must persist progress, coordinate multiple steps, or continue after the original request ends.

To explore the preview:

* File an issue or feature request on the [Agent Extension Repository](https://github.com/Azure/azure-functions-python-extensions).
* Read [Agent bindings for Python in Azure Functions](https://learn.microsoft.com/azure/azure-functions/functions-agent-bindings).
* Follow [Use a Microsoft Agent Framework agent in a Python function](https://learn.microsoft.com/azure/azure-functions/functions-agent-bindings-agent-framework?tabs=windows).
* Build the durable scenario in [Use a Microsoft Agent Framework agent binding in a Durable orchestration](https://learn.microsoft.com/azure/azure-functions/functions-agent-bindings-agent-framework-durable?tabs=windows).
* Explore the [complete direct sample](https://github.com/Azure/azure-functions-python-extensions/tree/dev/azurefunctions-agents-extensions-agent-framework/samples/agent_samples_agent-framework) and [complete Durable sample](https://github.com/Azure/azure-functions-python-extensions/tree/dev/azurefunctions-agents-extensions-agent-framework/samples/agent_samples_agent-framework_durable).

Try the preview, bring Agent reasoning to an existing function, and tell us what you build.
