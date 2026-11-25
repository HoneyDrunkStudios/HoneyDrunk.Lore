---
source: "https://blog.n8n.io/production-ai-playbook-audit-trace-for-ai-agents/"
title: "Production AI Playbook: Audit & trace for AI agents"
author: "Elvis Saravia"
date_published: "2026-11-24"
date_clipped: "2026-11-24"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Production AI Playbook: Audit & trace for AI agents

Source: https://blog.n8n.io/production-ai-playbook-audit-trace-for-ai-agents/

*This post is part of a series that explores proven strategies and practical examples for building reliable AI systems. If you are new to n8n, start with the* [*introduction*](https://blog.n8n.io/production-ai-playbook-introduction/)*.*

## Why Audit and Trace Matter for AI Agents

Your refund agent has been live for a month. It reads each customer message, looks up the order, and approves small refunds on its own. Then the finance team flags a $49.99 refund that should never have gone out and asks why the agent approved it. You open the workflow to find out, but the prompt has been edited twice since then, the order record has changed, and nobody recorded which run made that decision. The reality is that the workflow in front of you today cannot explain a decision it made last month.

This is what's called the audit gap. Every team that lets an AI workflow act on its own runs into it once real requests start coming in. A decision you cannot reconstruct is a decision you will end up defending from memory. An audit trail closes the gap by keeping the evidence behind each decision, including the original inputs, the workflow version, and any human approval. Tracing connects the steps of a run across workflows and services and records their timing and status. Together, they give you the records to answer the finance team's question.

The exercises below build up that record in n8n Cloud, starting with one saved execution, then adding decision tags and traces to follow tool calls and a human approval.

****What about the new n8n Agents?**** n8n recently introduced [n8n Agents](https://blog.n8n.io/introducing-n8n-agents/), a new way to build and manage agents alongside workflows. These agents already provide built-in visibility into their sessions, including execution steps and tool activity. n8n Agents can also emit agent and tool-call spans when agent tracing is enabled. This article, however, focuses on AI agents built within n8n workflows using the AI Agent node, and the observability features described here don't necessarily apply to the new n8n Agents in the same way.

## Reading One Execution

When you question a decision, start with the saved execution. It is n8n's record of a single run, and it shows what each node received and returned. In a refund workflow, that means you can see what the order lookup returned and what the agent told the customer. Comparing the two can reveal a reply the data does not support, even when the run reports success.

Try it yourself

Exercise 1: Silent Failure Forensics

![Exercise 1 workflow](https://storage.ghost.io/c/0d/78/0d78b34c-0c5f-4975-900e-61d00ccb1c2d/content/images/2026/09/data-src-image-1f0b0236-73b8-4a08-b83f-605560d009a1.png)

Apply this check to a support agent that generates refund replies from a simulated order lookup. Compare a complete record with two unusable records, then enable validation to route the missing-data cases to human review.

1. Import the Exercise 1 template using the download below. Leave **Validate Lookup** disabled until step 8.

2. In the workflow’s three-dot menu, select **Settings**, set **Save manual executions** to **Save**, then click **Save**. Use this setting for each exercise workflow.

3. Connect your credentials to **OpenRouter - Support**. The template uses OpenRouter with `openai/gpt-4.1-mini`; you can replace the Chat Model sub-node with another supported provider.

4. Open **Webhook - Support Request** and replace `YOUR_WEBHOOK_TEST_URL` below with its Test URL. Return to the canvas, select **Execute workflow**, and wait for **Waiting for trigger event** before sending:

Bash

```
curl -X POST "YOUR_WEBHOOK_TEST_URL" \
  -H "Content-Type: application/json" \
  -d '{"orderId":"ORD-1001","message":"Charged twice, refund the duplicate."}'
```

5. In **Executions**, open the newest run. **Order Lookup** should show one order for 49.99 USD with `lookupComplete: true`. Open **Refund Support Agent**, select **Logs**, then **OpenRouter - Support** to compare the resolved prompt and reply.

6. Return to **Editor**, select **Execute workflow** again, and send the request below. In its saved run, expect `orders: []` and `lookupComplete: false` in **Order Lookup**:

Bash

```
curl -X POST "YOUR_WEBHOOK_TEST_URL" \
  -H "Content-Type: application/json" \
  -d '{"orderId":"ORD-9999","message":"Charged twice, refund the duplicate."}'
```

7. Return to **Editor**, select **Execute workflow** again, and send this request. In its saved run, **Order Lookup** should show one order with null amount and currency, and `lookupComplete: false`:

Bash

```
curl -X POST "YOUR_WEBHOOK_TEST_URL" \
  -H "Content-Type: application/json" \
  -d '{"orderId":"ORD-1004","message":"Charged twice, refund the duplicate."}'
```

Expect HTTP 200, `answeredBy: "agent"`, and a successfully saved execution for each request. Reply wording varies; the agent may ask for details for `ORD-9999` or promise a refund for `ORD-1004` despite the missing amount. Compare each reply with the saved lookup and model logs to judge whether it is supported. This demo generates replies without processing payments.

8. Activate the **Validate Lookup** node and rerun all three cases. The two incomplete lookups should return `answeredBy: "human-review"`, while `ORD-1001` still reaches the agent.

[Download the Exercise 1 workflow template](https://go.n8n.io/PAP-Audit-1)

Pro tip: Each Test URL listener accepts one request. If you get a 404 saying the webhook is not registered, select **Execute workflow** again and resend.

## Tagging Executions for Audit

A saved execution explains one run, but first you have to find it. Custom executions data lets you attach labels such as the order ID and the final decision to each run:

JavaScript

```
$execution.customData.set("caseId", "ORD-1001");
$execution.customData.set("decision", "refund_approved");
```

Use `getAll()` to read the values back during the execution. Pick labels your team already searches by, such as order IDs or ticket numbers. Validate values before writing them, since keys are limited to 50 characters, values to 255, and each execution to 10 entries.

Try it yourself

Exercise 2: Searchable Executions

![Exercise 2 workflow](https://storage.ghost.io/c/0d/78/0d78b34c-0c5f-4975-900e-61d00ccb1c2d/content/images/2026/09/data-src-image-ffd8ada6-e5a8-4724-9140-06da78ff16d0.png)

This template applies a demo refund policy, asks the model to explain its decision, and records that structured decision as custom data.

1. Import the Exercise 2 template.

2. Connect credentials to **OpenRouter - Support**, as in Exercise 1.

3. Inspect **Policy Decision**, an Edit Fields node that selects the outcome from the order record, and **Check Tag Length**, an If node that guards the 255-character limit. **Tag Execution** is an Execution Data node that saves the case details as custom data. After the reply, **Record Decision** saves the final outcome the same way, and **Build Reply** returns it.

4. Copy the Webhook Test URL, select **Execute workflow**, and send:

Bash

```
curl -X POST "YOUR_WEBHOOK_TEST_URL" \
  -H "Content-Type: application/json" \
  -d '{"orderId":"ORD-1001","customerTier":"gold","message":"Please refund this order."}'
```

5. Repeat with `ORD-1002` and `ORD-9999`, restarting the listener each time. The three decisions should be `refund_approved`, `refund_declined`, and `needs_human_review`. Confirm them in **Record Decision**.

6. On Cloud Pro or Enterprise, optionally open the funnel filter in the executions list and use **Highlighted data**, the current name for saved custom data. Enter `decision` as the key and `refund_approved` as the value, and tick **Exact match**. This filter is not included on Starter.

7. Send a `customerTier` longer than 255 characters. **Check Tag Length** should route the run to **Reject Oversized Tag**, a Stop and Error node, before any tag is written.

[Download the Exercise 2 workflow template](https://go.n8n.io/PAP-Audit-2)

## Tracing with OpenTelemetry

The saved execution shows what each node received and produced inside one workflow run. It doesn't show what happened in the sub-workflow the run called, inside the service its HTTP Request node reached, or in the system that sent the request in the first place. Tracing fills that gap. n8n emits a span for the workflow and each node, with timing, status, and parent-child relationships, and sends them to any OpenTelemetry collector. A request that arrives with trace context from another service joins that service's trace, and the calls n8n makes carry the context onward, so one trace can follow a refund from the customer portal, through the workflow and its sub-workflow, to the payment service.

Traces also live outside n8n. The collector keeps them under its own retention and access rules; you can search them by execution ID or trace ID across every workflow, and they remain after the execution record is pruned. Use the execution record when you need the payloads. Use traces when you need to see where the time went, which step failed, and how the run connects to systems beyond the workflow.

Tracing is in Preview. n8n's documentation advises against relying on it in production workflows.

A `workflow.execute` span records the workflow version, execution ID, mode, and status. With node spans enabled, `node.execute` spans add each executed node's name, type, and item counts. Failures can include exception messages and stack traces.

Pro tip: Read item counts with care. One item can hold an empty array, and AI sub-nodes can report zero items after a successful call. Open the saved execution when you need to see the actual payloads.

Instance owners and admins configure tracing in **Settings > OpenTelemetry**. The page below shows it with a tunnel URL entered as the OTLP endpoint and tracing enabled.

![](https://storage.ghost.io/c/0d/78/0d78b34c-0c5f-4975-900e-61d00ccb1c2d/content/images/2026/09/data-src-image-9d3ff2ff-8932-4966-bb09-2f8cebfae621.png)

Before starting Exercise 3, set up a local trace collector on your computer. Exercises 4 and 5 reuse it, so keep it running until you finish all three. You need three tools. Docker Desktop runs the Jaeger collector, the cloudflared command-line tool gives n8n Cloud a temporary HTTPS address for that collector, and curl sends the test requests from your terminal.

Install Docker Desktop from the [Docker documentation](https://docs.docker.com/desktop/) and cloudflared from the [Cloudflare Tunnel downloads page](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/), or with Homebrew on macOS `using brew install cloudflared`. Most systems include curl; otherwise, see the [curl downloads](https://curl.se/download.html). The [Jaeger getting started guide](https://www.jaegertracing.io/docs/latest/getting-started/) covers the collector, and the [n8n OpenTelemetry documentation](https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry) explains each tracing setting. Jaeger keeps traces in memory, so they disappear when you stop it.

Try it yourself

Exercise 3: Your First Trace

![Exercise 3 workflow](https://storage.ghost.io/c/0d/78/0d78b34c-0c5f-4975-900e-61d00ccb1c2d/content/images/2026/09/data-src-image-28bec035-5ba7-4f87-b86e-320896d2f630.png)

This template converts a charge amount to cents and simulates success or failure, without a model or payment provider.

1. With Docker running and cloudflared installed, save this as `docker-compose.yml` and run `docker compose up -d`:

YAML

```
services:
  jaeger:
    image: jaegertracing/jaeger:2.20.0
    ports:
      - "127.0.0.1:16686:16686"
      - "127.0.0.1:4318:4318"
```

2. Run `cloudflared tunnel --url http://localhost:4318` in another terminal and keep it running. The HTTPS URL it prints lets n8n Cloud reach your local collector.

3. In Cloud **Settings > OpenTelemetry**, enter that URL as the **OTLP endpoint**, leaving **Trace path** as `/v1/traces`. Set **Trace sample rate** to 1, keep **Include node spans** and **Inject outbound traceparent** on, and turn **Track published workflows only** off. Enable tracing, save any pending changes, and select **Send test trace**.

4. Open Jaeger at `http://localhost:16686`, select the configured service name (default `n8n`), and find the test trace.

5. Import Exercise 3 and copy its Webhook Test URL. Select **Execute workflow** on the canvas, using the button below the workflow rather than a node’s own Execute step, so that every node runs. Then send:

Bash

```
curl -X POST "YOUR_WEBHOOK_TEST_URL" \
  -H "Content-Type: application/json" \
  -d '{"requestId":"REQ-3001","amount":49.99}'
```

6. In n8n, open **Executions** and note the ID shown next to the new run. In Jaeger’s **Tags** field, enter `n8n.execution.id=YOUR_EXECUTION_ID` with that ID and select **Find Traces**. Expect a workflow span with six node spans, one for each of Webhook - Charge Request, Validate Amount, Normalize Request, Charge Card, Capture Charge, and Respond. If only the webhook span appears, the run started from a node instead of the canvas; select **Execute workflow** on the canvas and resend. In the saved execution, **Normalize Request** should return `amountCents: 4999`.

7. Restart the listener and send `{"requestId":"REQ-3002","amount":49.99,"trigger_failure":true}`. **Charge Card**, an If node, should route the request to **Decline Charge**, a Stop and Error node that fails with `card_declined`, leaving **Capture Charge** and **Respond** unexecuted. Inspect the exception on the **Decline Charge** span and on the workflow span.

Keep Jaeger and the tunnel running through Exercise 5. This demo uses temporary trace storage; restore your Cloud tracing settings before stopping the tunnel and running `docker compose down`.

[Download the Exercise 3 workflow template](https://go.n8n.io/PAP-Audit-3)

Pro tip: Check the execution status in n8n instead of trusting the curl response. A failure before the workflow’s final response node can come back as an empty HTTP 200 or as an HTTP 500 “Error in workflow” message, depending on the n8n version and whether you used the Test URL or the production URL.

## Tracing AI Agents

When an agent gives a wrong answer, the cause can be a tool call that returned bad or empty data. The AI Agent node records its model and tool activity as standard node spans, so the trace shows which tool ran, in what order, and how long it took. The tool arguments and results are in the saved execution logs. When a lookup tool finds nothing, have it return a clear message such as "No order found", since an empty string gives the agent nothing to report.

Try it yourself

Exercise 4: Find the Failing Tool

![Exercise 4 workflow](https://storage.ghost.io/c/0d/78/0d78b34c-0c5f-4975-900e-61d00ccb1c2d/content/images/2026/09/data-src-image-a7e95c66-c752-4915-9fe6-137748ce1018.png)

In this exercise, you will compare a calculator result, a valid order lookup, and an empty lookup across execution logs and traces.

1. Import Exercise 4, connect credentials to **OpenRouter - Agent**, and keep the tracing configuration from Exercise 3. If you change models, choose one with tool-calling support.

2. Copy the Webhook Test URL, select **Execute workflow**, and send:

Bash

```
curl -X POST "YOUR_WEBHOOK_TEST_URL" \
  -H "Content-Type: application/json" \
  -d '{"query":"What is 47 times 89?"}'
```

3. Open the execution and inspect the **Calculator Tool** in the agent logs. Its result should be `4183`; inspect the expression the model supplied. Find the corresponding node span in the trace.

4. Restart the listener and send `{"query":"How much was order ORD-1001? Use the order lookup."}`. Confirm the tool returns a record containing 49.99 USD.

5. Repeat with `{"query":"How much was order ORD-8888? Tell the customer the amount."}`. **Order Lookup Tool** returns an empty string, yet its execution and span can still report success. Check whether the agent’s reply acknowledges the missing order.

6. Compare the two lookup spans with their logs. Use the recorded tool results to distinguish the valid order from the empty lookup.

[Download the Exercise 4 workflow template](https://go.n8n.io/PAP-Audit-4)

## Connecting Traces Across Services

AI workflows usually sit between other systems. A request arrives from a customer portal, and the workflow calls a policy or payment service before it answers. When the incoming request carries a valid `traceparent` header, n8n uses its trace ID and parent span ID, so the workflow joins the caller's trace. With outbound injection enabled, an HTTP Request node forwards the same trace ID with a new span ID, and an instrumented downstream service can record its own work in that trace.

Sub-workflow spans belong under the parent workflow span. After a wait, the resumed workflow can start a new trace with a link back to the earlier span. Search by `n8n.execution.id` to find both parts of the same execution.

Try it yourself

Exercise 5: Trace an Approval

![Exercise 5 workflow](https://storage.ghost.io/c/0d/78/0d78b34c-0c5f-4975-900e-61d00ccb1c2d/content/images/2026/09/data-src-image-e72b0c01-a02f-4a78-9508-c557d3ba3547.png)

This workflow enriches a request, generates a proposal, and waits for a submitted approval or rejection. It records the decision without processing a payment.

1. Import, save, and **publish** the [Exercise 5 enrichment sub-workflow](https://go.n8n.io/PAP-Audit-5-Sub) first. Then import the [Exercise 5 parent workflow](https://go.n8n.io/PAP-Audit-5) and explicitly select that imported sub-workflow in **Enrich Request Sub-workflow**. Both downloads are also linked at the end of this exercise.

2. Connect credentials to **OpenRouter - Approval** and keep tracing enabled. Copy the parent’s Webhook Test URL and select **Execute workflow**.

3. Send this request. Its `traceparent` header supplies the trace ID that the whole run joins, and you will look that ID up in step 5. The amount is in USD cents, so 4999 represents $49.99:

Bash

```
curl -X POST "YOUR_WEBHOOK_TEST_URL" \
  -H "Content-Type: application/json" \
  -H "traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01" \
  -d '{"requestId":"REQ-2001","amount":4999,"reason":"duplicate charge"}'
```

4. Save the returned `executionId` and the complete `resumeUrl`, including any query string. Wait until the execution status is **Waiting**.

5. In Jaeger, paste `4bf92f3577b34da6a3ce929d0e0e4736`, the trace ID from your header, into the **Lookup by Trace ID** box. The parent workflow span should sit under the span from your header, with the enrichment sub-workflow span nested under it. In n8n, open **Policy Service Call** in the waiting execution. Its output shows a `traceparent` with the same trace ID and a different span ID, which confirms that n8n forwarded the trace context. The echo service does nothing else with it.

6. Submit the approval to the resume URL rather than the webhook Test URL. Copy the complete `resumeUrl` value from the step 3 response, including the signature query string, and paste it in place of `YOUR_RESUME_URL` below. The same URL appears when you open **Wait for Human Approval** in the waiting execution. Treat it as a secret, since anyone holding it can approve the request:

Bash

```
curl -X POST "YOUR_RESUME_URL" \
  -H "Content-Type: application/json" \
  -d '{"approved":true,"approver":"Demo reviewer"}'
```

7. Confirm `approved: true` and `submittedApprover: "Demo reviewer"` in **Record Approval**. In Jaeger, search **Tags** for `n8n.execution.id=YOUR_EXECUTION_ID` with this run’s ID. Two traces appear: the original one and a new one for the resumed part, and the resumed workflow span carries a link back to the earlier span.

8. Start a separate run and submit `approved: false` to its new resume URL. Confirm the recorded decision is declined. A missing or non-boolean `approved` value, or a missing `approver`, should fail validation.

[1. Download the Exercise 5 sub-workflow](https://go.n8n.io/PAP-Audit-5-Sub)
[2. Download the Exercise 5 parent workflow](https://go.n8n.io/PAP-Audit-5)

Pro tip: The `approver` field in Exercise 5 is whatever the request sends. In production, take the reviewer’s identity from an authenticated login and restrict access to the resume endpoint. When you test beyond this fixed example, use a fresh trace ID for each run.

## Streaming Audit Events

Executions and traces record what a workflow did. Audit events record what people did to it, such as changing a workflow, publishing it, or signing in. Cloud Enterprise adds **Settings > Log Streaming**, where you can send selected events to a syslog server, a webhook, or Sentry. Audit events cover workflow changes such as created, updated, published, and unpublished, user login successes and failures, and credential changes. AI node events cover tool calls, model responses, and model errors.

Choose the events you need under **Settings > Log Streaming > Events**, inspect their payloads for sensitive data, and verify delivery and retention at the destination. Each destination can strip sensitive payload data from audit events. Log streaming records events as they happen, while the saved execution holds the node data, so keep execution data when you need complete node payloads.

## Proving What Changed

If an agent behaved differently last month, the workflow itself may have changed. Open **Version history** from the workflow's three-dot menu to inspect or download earlier definitions. n8n creates a version each time you save or restore a workflow. Changes to workflow settings do not create a version.

Starter includes the last 24 hours of workflow history, Pro includes five days, and Enterprise includes full history. Pro and Enterprise also support named versions, which n8n does not prune automatically. Name a version each time a workflow goes live so you can show which definition was running on a given date, and export any versions you need to keep longer.

Cloud Enterprise offers two additional controls. With environments enabled, workflow diffs show changes between the instance and its connected Git repository. Workflow reviews let a reviewer approve a saved version before n8n publishes it. They are available from n8n 2.37.0, an instance admin turns them on in **Settings > Security & policies**, and they are in Preview, so evaluate them before production use. A review covers the workflow's nodes and connections. Workflow settings, credentials, variables, data tables, and sub-workflows sit outside the review and change the published workflow as soon as you edit them. Enabling reviews still lets you publish directly when no review is open.

## Design Decisions

You might have questions about your retention. We suggest choosing retention based on how far back an investigation may need to go. Execution data preserves recorded payloads, traces connect workflow activity across services, and audit events record selected changes. Align their retention and access controls.

Lower trace sampling reduces stored volume but leaves some executions unrepresented. n8n samples by trace ID, so it keeps a trace in full or drops it entirely. Keep full sampling for these exercises, then decide whether an investigation could tolerate missing traces.

Traces help investigate individual runs. Use evaluations to assess answer quality, as covered in [Evaluation and Monitoring](https://blog.n8n.io/production-ai-playbook-evaluation-and-monitoring/).

## Production Best Practices

**Validate before acting:** Check required fields before an agent uses a lookup, and record the structured decision your workflow selected.

**Verify retained evidence:** Cloud execution retention depends on your plan. Starter keeps up to 2,500 executions for 7 days, Pro keeps up to 25,000 for 30 days, and Enterprise keeps up to 50,000 with no time limit; n8n removes the oldest runs once it reaches either limit. In workflow **Settings**, choose which successful and failed production executions to save. Preserve required executions, including their workflow versions and external configuration, before records expire, and verify retention in your trace collector.

**Control access:** Protect saved prompts, tool results, and error details in both n8n and the collector. Approval records should identify an authenticated reviewer.

## Tips and Tricks

**Restart the listener:** Select **Execute workflow** before every new request, and keep **Track published workflows only** off while testing traces.

**Check the endpoint:** Cloud needs a reachable collector URL. Enter the base URL once and keep /v1/traces in the **Trace path**.

**Find resumed runs:** Search by execution ID after a wait, since the resumed span may belong to another trace.

## What's Next

This post is part of a series that explores proven strategies and practical examples for building reliable AI systems. Find out what topics are already available in the Production AI Playbook [here](https://blog.n8n.io/tag/production-ai-playbook/), or be the first to know when new topics are added via [RSS](https://blog.n8n.io/tag/production-ai-playbook/rss/), [LinkedIn](https://www.linkedin.com/company/n8n/) or [X](https://x.com/n8n_io).

Next in the series is Publish & Scale, covering deployment options, access controls, environments, and scaling behavior.

## Share with us

n8n users come from a wide range of backgrounds, experience levels, and interests. We have been looking to highlight different users and their projects in our blog posts. If you're working with n8n and would like to inspire the community, [contact us](https://n8n-community.typeform.com/to/VYiRI7WN?ref=blog.n8n.io) 💌

SHARE
