---
"source": "https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/hosting-your-langgraph-application-on-microsoft-foundry-agents/4573342"
"title": "Hosting your LangGraph application on Microsoft Foundry Agents"
"author": "Maira Ladeira Tanke, Muzz Imam"
"date_published": "2026-11-16"
"date_clipped": "2026-11-17"
"category": "Azure & Cloud"
"source_type": "web"
---

# Hosting your LangGraph application on Microsoft Foundry Agents

***This post was co-authored my Maira Ladeira Tanke and Muzz Imam***

Consider a sales team that wants an assistant to handle customer returns. A customer asks, “Can I return my order?” The assistant needs to understand the request, look up the order, and use the available tools to help the customer through the return process.

The engineering team builds it in LangGraph, and for the rest of this post, we’ll take their seat as we bring it to production on Microsoft Foundry Hosted Agents without rewriting the graph. The graph manages the conversation, calls the model, and connects to the order and return tools. For this example, the architecture is straightforward:

The prototype works well. We test different return scenarios, demonstrate the assistant to leadership, and get approval to make it available to customers. Now we need to run it in production.

We start looking at hosting options: AKS, Azure Container Apps, Azure Functions. But agentic applications have their own requirements, and choosing where the code runs needs to consider them. Our sales assistant needs to support multi-turn conversations, keep concurrent customer conversations isolated, and preserve context when a customer leaves halfway through a return and comes back the next day. These requirements need to be part of the hosting decision from the start.

Where do we store conversation history and the state of an unfinished return? How do we connect Microsoft Entra ID and control access to the order system? How do we screen harmful content and check that the assistant follows the return policy as we change prompts or models? When a customer gets the wrong answer, can we inspect the model and tool calls that led to it? We need to plan capacity and scaling, handle concurrent requests, and deploy new versions without interrupting conversations already in progress. If another team wants to reuse the return tools, we need a way to share and manage access to them too.

None of this means we chose the wrong framework. The LangGraph application is doing what we built it to do. But the production plan now includes a conversation store, identity integration, tracing, deployment policies, and infrastructure decisions. We need to decide how much of that platform our team wants to assemble and maintain.

This is where [Microsoft Foundry Hosted Agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents) enters the discussion. We can keep our LangGraph application and run it in a managed agent runtime. In this post, we will follow the sales assistant into production and look at what Foundry takes on, what we still need to configure, and what remains our responsibility.

## Deploying your agent to Foundry Hosted Agents

The good news is that we do not need to rewrite the sales assistant to run it on Foundry Hosted Agents. We keep the graph, prompts, and order and return tools we already built. LangGraph still controls the conversation and the application logic. The hosting integration exposes our existing compiled graph through an endpoint that Foundry can serve; it does not require us to move to a different agent framework. The [Learn hosted-agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent) covers the deployment workflow.

The [langchain-azure-ai package](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/langchain) is the entry point for building LangChain and LangGraph applications with Microsoft Foundry capabilities, including models, tools, and tracing. For hosting, we use its hosting integration to connect the existing graph to the managed runtime. We still need to configure dependencies, credentials, and deployment settings, but the assistant itself remains a LangGraph application.

We can expose the agent through either the [Responses or Invocations protocol](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agent-contract?tabs=python). Responses provides an OpenAI-compatible chat endpoint, including streaming and conversation threading. For our sales assistant, this is a natural starting point. With the hosting dependencies installed, we pass the existing compiled agent to *ResponsesHostServer*:

```python
from langchain_azure_ai.agents.hosting import ResponsesHostServer
# your agent code remains unchanged
# .....
ResponsesHostServer(agent).run()
```

*ResponsesHostServer is currently in preview.*

If the application needs a custom JSON request and response shape instead, we use the Invocations protocol. The setup follows the same pattern, using InvocationsHostServer in place of ResponsesHostServer:

```python
from langchain_azure_ai.agents.hosting import InvocationsHostServer
# your agent code remains unchanged
# ...
InvocationsHostServer(agent).run()
```

These are alternative entry points for the same agent logic. We choose the protocol that fits the application calling it; neither option requires rewriting the graph.

For an existing project with a graph referenced in langgraph.json, we can also use the langchain\_azure\_ai.agents.hosting.run module without adding a server entry-point file. In the Azure Developer CLI configuration, we set codeConfiguration.entryPoint in azure.yaml to run that module with the chosen protocol. For Responses, the relevant configuration looks like this:

```yaml
services:
  my-agent:
    host: azure.ai.agent
    kind: hosted
    env:
      PYTHONNOUSERSITE: "1"
    codeConfiguration:
      runtime: python_3_13
      entryPoint: '-m langchain_azure_ai.agents.hosting.run --protocol responses'
```

### What changes once the agent is deployed

Our sales assistant is now serving customers through a Foundry Hosted Agent endpoint. The LangGraph application still handles the conversation and calls the order and return tools. Around that code, we now have sessions, conversation history, and a place to inspect execution. The architecture looks like this:

You pay for session CPU and memory only while compute is active, with no compute charge once the session scales to zero after its idle timeout; model, tool, and other Azure service charges are separate.

#### Continuing the conversation across turns

A return rarely fits into one message. The assistant might ask for an order number, check the order, and ask which item the customer wants to return. With the Responses protocol, Foundry stores the conversation history. We pass the [same conversation ID](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/manage-hosted-sessions) on subsequent turns so the assistant can use the earlier exchange rather than ask the customer to repeat it. Foundry also associates that conversation with a session, keeping the chat connected to the same working environment.

Foundry also provides a portal playground where we can quickly test conversations with the deployed agent. We can open the sales assistant, ask for help with a return, and follow up with the order details, all in the same chat. This gives the team a way to try the conversation before building a customer-facing interface. For our sales assistant, we can check whether it asks for the information it needs and uses the context we already provided.

A [conversation and a session serve different purposes](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/manage-hosted-sessions): the conversation holds messages, tool calls, and responses; the session provides the sandbox and its persisted filesystem. Reusing a session ID alone does not restore chat history. With Invocations, our application manages that history itself. Any additional LangGraph workflow state that must survive a process restart also needs durable persistence; conversation history is not a checkpoint of the whole graph.

#### Keeping each customer’s work separate

User A and User B can reach the same agent endpoint without sharing a conversation or workspace. For callers authenticated directly with Microsoft Entra ID, Foundry scopes sessions, conversations, and stored data to the calling identity. Each session runs in its own VM-isolated sandbox with a private filesystem. User B’s request for an update belongs to User B’s return, not the conversation User A started.

For a customer-facing application that calls Foundry through a shared backend identity, we [configure end-user identity delegation](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/isolate-sessions-per-user) and maintain separate session and conversation mappings for each customer. [Foundry Toolbox](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/toolbox-overview) lets us define a reusable collection of tools and expose it through a single MCP-compatible endpoint, with authentication and access managed centrally. For our order and return tools, this provides a shared endpoint with centrally managed credentials, versioning, and policies, while carrying user context through to supported tools. Another team can use the same tools in its own assistant instead of rebuilding the connections and authentication in each application. For tools that support [on-behalf-of-user (OBO) access](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/user-delegation), Foundry handles the downstream token exchange outside our agent code. The order service receives the signed-in user’s delegated context and applies its permissions when looking up an order or processing a return. Session isolation keeps the workspaces separate; the order service continues to enforce access to the business data and actions. We configure the [supported authentication method, delegated scopes, and consent](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/configure-user-delegation). Custom MCP tools use the agent-identity OBO configuration, currently in preview. For direct API calls outside this managed tool path, our application remains responsible for consent, token acquisition, and token protection.

For the sales assistant’s order-system connection, we can configure [private networking](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/virtual-networks) and [network egress rules (preview)](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/add-hosted-agent-guardrails) to restrict outbound connections to approved destinations; these controls require explicit configuration.

We also configure [content safety guardrails](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/add-hosted-agent-guardrails) to screen incoming prompts and outgoing responses. We create a Responsible AI policy in Foundry, attach its resource ID to the hosted-agent definition, and test both allowed and blocked requests before release. With Responses, the platform knows where to find the text to screen; with Invocations, we also configure the request and response fields to moderate. A deployed endpoint alone is not proof that filtering is active. These filters complement, rather than replace, our checks on return eligibility and authorization.

#### Seeing what happened inside a request

Suppose a customer says the assistant gave them the wrong return instructions. Reading the final answer is not enough to understand what went wrong. We need to inspect the request: the input the agent received, the model and tool calls it made, and the output at each step. With the [OpenTelemetry integration in langchain-azure-ai](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/langchain-traces), we can capture that execution in Azure Application Insights and inspect it in the Foundry portal. For the sales assistant, we can check whether it called the order lookup tool, what information the tool returned, and how the agent used that information in its response.

When we inspect a recorded request in Foundry, User view shows the exchange as a conversation, including the customer’s messages and the assistant’s replies. We can then inspect the recorded inputs, outputs, and tool execution behind that exchange. Graph view shows the relationships between the captured operations in this run. It is a view of the execution trace, not a replacement for the LangGraph application’s graph definition.

[Trace Replay](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-replay)  lets us step through the recorded interaction in sequence, pause on a particular operation, or jump to the part we want to investigate. We can move from the answer the customer saw to the tool result behind it and review where the behavior diverged from what we expected. Replay is a way to inspect the captured run; it does not rerun the return or execute the tools again.

For our team, this turns a customer-reported issue into a support incident we can investigate. We can distinguish an incorrect tool result from an incorrect interpretation of that result, or see whether a slow response spent its time in the model or a downstream call. The observability connection assumes tracing is enabled and the relevant operations are instrumented. We also control whether [message content and tool arguments are captured](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/langchain-traces), and restrict access to traces that contain customer or order information.

#### Monitoring the agent beyond a single conversation

A trace helps us investigate one customer’s return. Once the assistant is handling many conversations, we also need to know how it is performing across those requests. Are customers waiting longer for an answer? Are more runs failing? Is token usage growing along with traffic, or has the agent started using more tokens to handle similar requests? The [Foundry monitoring dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard) brings token usage, latency, and run success rate into the agent’s Monitor tab, with summaries and charts for the time range we select. This gives us an operational view across conversations, rather than only the details of one run.

For the sales assistant, we read those signals together. If token usage rises, we can investigate whether the change reflects more conversations, longer prompts and responses, or extra model calls. If response times increase or the run success rate drops, we can inspect traces from that period to understand which operations need attention. The dashboard helps us spot the pattern; the trace helps us investigate the individual execution. Token counts are useful for understanding model consumption, but they are not the full cost of running the application.

Operational health is only part of the picture. A run can complete successfully and still give the customer an incorrect answer. When configured, the Monitor experience also brings in [evaluation scores and red-team results](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard), alongside preview options for recurring evaluations and alerts. For our team, that means we can review reliability and usage alongside checks on answer quality and safety, rather than treating a successful request as proof that the return was handled correctly. Agent metrics in this dashboard are currently in preview and use the Application Insights resource connected to the project, with the corresponding access permissions and retention settings.

### Production is the beginning of the improvement cycle

Getting the sales assistant into production is only the first step. To check whether it is doing its job, we define representative return scenarios and expected outcomes: following the return policy, asking for missing order details, selecting the right tools, and refusing unauthorized actions. We use [Foundry evaluations](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app) to score the agent’s responses and conversations with built-in quality and safety evaluators, plus custom checks for our business rules. In the portal, we create an evaluation, select the agent and test data, and choose the evaluators that match those criteria.

Before changing a prompt, tool, or underlying model, we run the current and candidate versions against the same test cases and scoring criteria. We compare task outcomes and safety results alongside latency and token usage, then inspect individual failures rather than relying only on an average score. Production traces and [insights](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/agent-insights) help us identify cases to add to the test set. The [agent optimizer overview](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-optimizer-overview) explains the optional next step of generating and evaluating candidate configurations. Our team still defines success and decides which changes are ready for customers.

### Let Foundry do the heavy lifting

We started with a sales assistant that handled returns well in a prototype. Making it useful to customers also meant supporting ongoing conversations, keeping their work separate, controlling access to orders, and understanding how the agent behaved. Those responsibilities remain important long after the first deployment.

Hosting on Foundry lets us keep the LangGraph application and use managed capabilities around it, rather than assemble every part of the platform ourselves. Our team still owns the return experience, the business rules, and the decision to release a change. Traces, monitoring, evaluations, production insights, and optimization give us evidence to work with as we improve that experience.

If you already have a working LangGraph agent, start with the [Learn hosted-agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent) and explore the [LangGraph examples](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents/langgraph) for multi-turn chat, Toolbox integration, and observability. Test a representative return conversation in the portal, inspect its trace, and turn the expected outcome into an evaluation case. Foundry handles more of the hosting platform so our team can focus on ongoing business value: helping customers complete eligible returns correctly and safely, and checking that each release preserves or improves that experience.
