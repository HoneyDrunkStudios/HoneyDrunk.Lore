---
"source": "https://www.datadoghq.com/blog/datadog-code-execution"
"title": "Cut AI agent cost and improve accuracy with Code Execution in the Datadog\
  \ MCP Server"
"author": "Kit Freddura; Amy Zhou"
"date_published": "2026-09-22"
"date_clipped": "2026-10-03"
"category": "AI / LLM Research & Tooling"
"source_type": "rss"
"capture_method": "full-readable-extraction"
---

# Cut AI agent cost and improve accuracy with Code Execution in the Datadog MCP Server

Kit Freddura

Senior Software Engineer

Amy Zhou

Product Manager

[Code Execution](https://docs.datadoghq.com/mcp_server/code_execution/) is now generally available in the [Datadog MCP Server](https://docs.datadoghq.com/mcp_server/). Instead of calling tools one at a time, your AI agent can write JavaScript that queries Datadog directly, run that code in a Datadog-managed sandbox, and get back only the result it needs.

When we ran our evals against four different models, agents using Code Execution cut costs by sending 73% fewer input tokens to the model. The agents also were more accurate, getting the right answer 90% of the time (up from 74%), and taking 40% fewer tool calls to get there.

**How Code Execution works**

**How Code Execution works**

Most complex queries require accessing multiple sources of data. For example, you see an error spike, check the traces behind it, and then look for the deploy that lines up with it. With standard MCP tools, each of those steps is a round trip: The agent calls a tool, reads the full raw response, decides what to do next, and calls another tool. By the time the agent answers, most of the model’s context window is filled with intermediate data that the agent needed only for that step.

Code Execution removes much of the intermediate data from the context window. The agent writes a script that directly queries Datadog APIs, and the Datadog-managed sandbox runs the queries in parallel and joins the results. The model sees only the results.

Without Code Execution, the agent would pull both full result sets into the conversation and do the join itself.

Because the agent is writing code against your data, the sandbox never gets your credentials. When the code calls a Datadog API, the MCP Server makes the request on your behalf with your existing permissions and returns only the result.

**Get more accurate answers while spending less**

**Get more accurate answers while spending less**

To measure how Code Execution affects investigation quality and cost, we compared it with Datadog’s [Core toolset](https://docs.datadoghq.com/mcp_server/tools/#core-tools). We ran 25 observability tasks related to metrics, logs, traces, [Datadog Error Tracking](https://docs.datadoghq.com/error_tracking/), and investigations. Each task ran three times per model with each toolset, on GPT-5.6 Terra, GPT-5.6 Sol, Claude Sonnet 5, and Claude Opus 4.8, and we scored the final answers for correctness.

The results showed that all four models improved in answer accuracy with Code Execution. The biggest increase was for Claude Sonnet 5, which went from 67% to 89% correctness.

Code Execution also reduced how much each agent had to read. Averaged across the four models, input tokens per task dropped from 159k to 43k, and tool calls fell from 4.1 to 2.5. The models averaged between 107k and 197k tokens with the Core toolset, but all four models ended up between 38k and 46k tokens with Code Execution. Since many providers bill by the token, fewer input tokens can mean that each investigation costs less to run.

**Get started with Code Execution**

**Get started with Code Execution**

To get started with Code Execution, [connect the Datadog MCP Server to your AI client](https://docs.datadoghq.com/mcp_server/setup/) and [enable the code-exec toolset](https://docs.datadoghq.com/mcp_server/code_execution/#enable-code-execution).

When Code Execution is enabled, ask your agent a question that requires it to correlate multiple kinds of observability data. For example: “Find the services whose error rate changed after last night’s deployments, then show me the trace patterns that changed with them.” The agent can use Code Execution to gather the relevant data, correlate it, and return the evidence behind its answer.

To learn more, see the [Code Execution documentation](https://docs.datadoghq.com/mcp_server/code_execution/), the [toolset configuration guide](https://docs.datadoghq.com/mcp_server/setup/#toolsets), and the [Datadog MCP Server documentation](https://docs.datadoghq.com/mcp_server/).

If you’re new to Datadog, you can [sign up for a 14-day free trial](#) to try Code Execution for your investigations.
