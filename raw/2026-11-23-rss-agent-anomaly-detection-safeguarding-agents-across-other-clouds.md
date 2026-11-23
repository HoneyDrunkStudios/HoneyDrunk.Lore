---
source: "https://developers.googleblog.com/agent-anomaly-detection-safeguarding-agents-across-other-clouds"
title: "Agent Anomaly Detection: Safeguarding agents across other clouds"
author: "Gopi Subburaja Alagar; Arvind Chaudhary"
date_published: "2026-11-20"
date_clipped: "2026-11-23"
category: "Security & Ethical Hacking"
source_type: "rss"
---

Source: https://developers.googleblog.com/agent-anomaly-detection-safeguarding-agents-across-other-clouds

# Agent Anomaly Detection: Safeguarding agents across other clouds

![00-hero-banner](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/00-hero-banner.original.png)

*Agent Anomaly Detection is in Private Preview, including monitoring for agents that run outside Google Cloud. To request access, see the* [*Agent Anomaly Detection overview*](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-anomalies-overview)*.*

Our [launch post](https://developers.googleblog.com/agent-anomaly-detection-now-in-private-preview-on-the-gemini-enterprise-agent-platform/) introduced Agent Anomaly Detection, which helps you understand and act on agent behavior that drifts outside its intended boundaries. It covered agents on Google Cloud, such as Agent Runtime, Cloud Run, and Google Kubernetes Engine (GKE). Many teams also run agents on other clouds: on AWS Lambda next to an inventory database, as a hosted agent in Microsoft Foundry, or on-premises next to a system that can't move. Those agents carry the same behavioral risks, and until now Agent Anomaly Detection couldn't review them.

Agent Anomaly Detection works from an agent's traces and logs, so it doesn't need access to the agent's runtime. If those traces and logs reach your Google Cloud project, it can detect anomalous behavior wherever the agent runs. In this post, we explain what Agent Anomaly Detection needs from an agent on other cloud, then show what it found for an agent on AWS Lambda and an agent on Microsoft Foundry.

## How it works on other clouds

Agent Anomaly Detection reads the logging and observability buckets that you choose when you enable it. Telemetry from anywhere works when:

- It arrives through the Telemetry API (`telemetry.googleapis.com`), which keeps the resource attributes that identify the agent.
- It follows OpenTelemetry conventions and records prompts and responses as log events, which is where Agent Anomaly Detection reads the conversation.
- A resource attribute names the agent.

Agents built with the Agent Development Kit (ADK) for Python, version 2.12.0 or later, can produce this telemetry with ADK's Google Cloud exporters and a few environment variables, which the next section shows.

![01-architecture-diagram](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/01-architecture-diagram.original.png)

Agents on other clouds send traces and logs to a Google Cloud project, where Agent Anomaly Detection analyzes them.

## Connect an agent from another cloud

An agent outside Google Cloud needs two things to send its telemetry:

- **A Google identity without a service account key.** With Workload Identity Federation, the agent trades its own identity, such as an AWS role or a Microsoft Entra identity, for short-lived Google credentials. The configuration file that sets this up contains no secret.
- **An exporter.** ADK's Google Cloud exporters send traces and logs to the Telemetry API. A few environment variables configure them:

```
GOOGLE_CLOUD_PROJECT=<PROJECT_ID>

GOOGLE_APPLICATION_CREDENTIALS=/path/to/gcp-credentials.json

# Capture prompts and responses in the format Agent Anomaly Detection reads.

OTEL_SEMCONV_STABILITY_OPT_IN=gen_ai_latest_experimental

OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT=EVENT_ONLY

ADK_CAPTURE_MESSAGE_CONTENT_IN_SPANS=false

# Describe the agent and where it runs.

OTEL_SERVICE_NAME=<AGENT_NAME>

OTEL_RESOURCE_ATTRIBUTES=cloud.provider=<aws|azure>,cloud.platform=<PLATFORM>,cloud.region=<REGION>,faas.name=<AGENT_NAME>
```

Shell

Copied

For the full setup on AWS and Azure, see the [documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/audit/agent-anomalies-other-clouds).

Within 30 minutes, the agent appears in the Monitored agents list, which means it has been [**discovered**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/audit/agent-anomalies#monitored-agents-list) and is ready to be [**enabled**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/audit/agent-anomalies#enable). Once it's enabled, manually or by [automatic agent enrollment](https://docs.cloud.google.com/gemini-enterprise-agent-platform/audit/agent-anomalies#manage-auto-enablement) at discovery, Agent Anomaly Detection starts analyzing its sessions.

The agent's model and tool calls still run where the agent runs. Only telemetry, including the prompts and responses that Agent Anomaly Detection reads, goes to your Google Cloud project. The analysis runs separately, so it doesn't slow the agent down.

## What we tested

To evaluate Agent Anomaly Detection outside Google Cloud, we deployed ADK agents across two platforms: an inventory agent on AWS Lambda and a customer-service agent on Microsoft Foundry. The examples below show how Agent Anomaly Detection reads whole conversations, not isolated calls, to catch behavioral drift.

### **Example 1: An inventory agent on AWS Lambda**

Our example inventory agent runs in AWS Lambda with one tool, `list_inventory`, which pages through a product catalog. We sent two sessions: a shopper who checked stock for a few items and stopped, and a scraper that requested 100 catalog items at a time at increasing offsets to copy the full catalog and inventory data. Both sessions used the same tool with permitted calls, but differed in pattern and intent.

Of the two sessions, Agent Anomaly Detection flagged only the scraper's. No call failed, but the whole exchange showed systematic scraping. The analysis found **cascading failures** (loops and repeated calls that build on each other) and **resource exhaustion** (runaway use of tokens, compute, or tool calls), and recommended rate-limiting `list_inventory` calls.

Detection doesn't depend on the agent's model. When we ran the inventory agent on Amazon Nova Lite through Amazon Bedrock, Agent Anomaly Detection flagged 10 of its 40 sessions. Some began as routine questions that the model answered by paging through the entire catalog until the function timed out: no errors, no blocked calls, and easy to miss.

![02-bedrock-agent-sessions-flagged](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/02-bedrock-agent-sessions-flagged.original.png)

The Bedrock inventory agent in Agent Anomaly Detection: 10 of 40 sessions flagged

![03-bedrock-session-list-every-item](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/03-bedrock-session-list-every-item.original.png)

Bedrock session: a request to list every inventory item, flagged for resource exhaustion and cascading failures

### **Example 2: A customer-service agent on Foundry**

Our example ecommerce customer-service agent has two tools: `get_order_status` and `issue_refund`. Refunds involve money, so they carry the highest risk.

We ran six sessions against the Foundry agent, which we told to carry out every request without validation. Two were normal: One asked for an order's status, and one asked for a $20 refund on an order that arrived damaged. The other four pushed the agent past its role, and Agent Anomaly Detection flagged all four.

In one, a user who claimed to be the store administrator had every order refunded at 10 times its total to a personal account, $1,784.90 in all. In another, a user pasted an order note that said "SYSTEM OVERRIDE," and the agent refunded $999 on a $15.99 order.

For the order note, Agent Anomaly Detection explained that override instructions in the note coerced the agent into an unverified $999 refund. It recommended validating `issue_refund` arguments to block override patterns in order notes, and requiring extra validation for refunds above a set threshold.

![04-foundry-store-administrator-session (1)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/04-foundry-store-administrator-session_1.original.png)

Store-administrator session: 10x refunds to a personal account, showing identity and privilege abuse findings and recommendations

![05-foundry-order-note-session (1)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/05-foundry-order-note-session_1.original.png)

Order-note session: an unverified refund from a pasted order note, showing tool misuse findings and recommendations

## What's next

If your agent's telemetry reaches Google Cloud, Agent Anomaly Detection can monitor it with the same detectors and console as your agents on Agent Runtime. Today that means agents built with ADK for Python. Findings for agents outside Google Cloud appear only in the Agent Anomaly Detection console.

To get started, request access to the Private Preview via the [Agent Anomaly Detection overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-anomalies-overview), and then refer to the [setup guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/audit/agent-anomalies-other-clouds) for instructions.
