---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/azure-sre-agent-brings-on-demand-ai-powered-operations-to-your-aca-workloads/4573380"
title: "Azure SRE Agent brings on-demand, AI-powered operations to your ACA workloads"
author: "Vineela-Suri"
date_published: "2026-11-17"
date_clipped: "2026-11-19"
category: "Azure & Cloud"
source_type: "web"
---

# Azure SRE Agent brings on-demand, AI-powered operations to your ACA workloads

Source: https://techcommunity.microsoft.com/blog/appsonazureblog/azure-sre-agent-brings-on-demand-ai-powered-operations-to-your-aca-workloads/4573380

Today at Microsoft Ignite, we’re introducing on-demand, AI-powered operations help, powered by Azure SRE Agent. Now in preview, this new experience is built right into the Azure Container Apps portal. Developers can start an interactive debugging session directly from any container app and get evidence-backed, actionable insights in minutes. 

Each session is serverless and on demand: it starts in seconds, stays focused on your question, and ends when you’re done. There’s no agent infrastructure for you to set up, run, or maintain. Azure Container Apps is the first service to bring this experience to customers, and we plan to extend it to more Azure services in the future.

### Expert answers, right where you work

Checking a deployment, reviewing how an app scales, or tracking down an issue usually means piecing together configuration, revisions, deployment history, and metrics from several tools. That takes time and operational expertise that isn’t always on hand. The agent brings that expertise directly into the developer workflow, so teams get answers the moment they need them and can get back to building. 

You can ask the agent about any aspect of your app. For example: 

- **Understand your app:** “How is this app configured, and what does it depend on?”
- **Check a deployment:** “Did my last deployment change anything that could affect traffic?”
- **Review scaling and performance:**“Why is my app scaling out so often?”
- **Spot risks early:** “Is anything in this configuration likely to cause problems?”
- **Troubleshoot an issue:**“Why did my latest revision fail to start?”

### How it works

Getting started takes a click. From any app in the Azure Container Apps portal, select **Debug with SRE Agent** and ask your question. The agent already knows which app you’re looking at, so there’s no evidence to gather or context to explain first. 

Before it reads anything, the agent tells you what it wants to look at and asks for your approval. From there, it works through your app’s configuration, revisions, deployment history, Azure Monitor metrics, and logs from Log Analytics, much like an experienced SRE would. If something is unclear, it asks a focused follow-up question. When it’s done, it walks you through what it found, shows the evidence behind it, and recommends what to do next.

Throughout, the agent works with your own Azure identity and sees only what you already have permission to see. Your Azure credentials stay in your browser, and you can review any data before it’s shared with the agent. The agent is **read-only**, so it never changes your resources and only proposes fixes, and each session runs in an isolated sandbox that’s deleted when the session ends.  The sandbox restricts egress and prevents user data from being stored or shared; the only record of the session is a transcript that you can download from the browser after the session has ended.  

### After a session

In most cases, you can act on the agent’s recommendation directly in your app. When an issue requires further assistance, the agent can draft a support request from the session for you to review and submit to Azure Support. Sessions give you answers in the moment. To bring that same intelligence to your entire environment, every day, you can deploy [Azure SRE Agent](https://sre.azure.com/) right from the session. Once deployed, it builds lasting context and automates the longer-running workflows that keep your apps running.

SRE Agent is rolling out in preview in the [Azure Container Apps portal](https://containerapps.azure.com/). Start a session on any of your apps to see what it can do and let us know how it went with the quick “How was your experience” prompt at the end of each session.

### Key benefits

- **No setup:** Start a session from any container app, with nothing to deploy or configure.
- **Answers in minutes:** Get the likely root cause and a recommended fix, backed by evidence from your app.
- **Secure by design:** The agent uses your own Azure identity, only sees the data you approve, and never changes your resources.
- **Right where you work:** Everything begins and ends in the Azure Container Apps portal, with no switching between tools.
- **Faster time to resolution:** Solve common issues on your own without any wait time, and when you need more help, hand off to Azure Support with the context already captured.

We have a lot more to show you. [Explore all Azure SRE Agent announcements from Ignite 2026 here!](https://aka.ms/ignite2026/sreagent)
