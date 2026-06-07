---
source: "https://learn.microsoft.com/en-us/agents/architecture/multi-agent-workflow-oriented"
title: "Workflow-oriented multi-agent patterns"
author: "Microsoft Learn"
date_published: "2026-05-20"
date_clipped: "2026-06-07"
category: "Software Architecture"
source_type: "web"
---

# Workflow-oriented multi-agent patterns

Source: https://learn.microsoft.com/en-us/agents/architecture/multi-agent-workflow-oriented

Table of contents 
Exit editor mode 
Ask Learn 
Ask Learn 
Reading mode 
Table of contents 
Read in English 
Add 
Add to plan 
Edit 
Copy Markdown 
Print 
Note 
Access to this page requires authorization. You can try signing in or changing directories .
Access to this page requires authorization. You can try changing directories .
Workflow-oriented multi-agent patterns 
Feedback 
Summarize this article for me
In this article
Some common multi-agent business scenarios don't focus on interactive experiences. Instead, they use a more deterministic workflow that chains agent calls in a predefined sequence. In this model, the "multi-agent system" is more scripted. For example, it first calls Agent A, then Agent B, and so on, based on a formal workflow. This approach can be appropriate for processes that require strict ordering, business rule enforcement (such as an approval chain where an agent handles each step), and auditability.
In contrast with the hierarchical multi-agent pattern , this approach depends on deterministic control of agent invocation and thus leads to less variability in interactions. Example scenarios include multistage approvals (each stage is a discrete agent-handled step), compliance and evidence collection, incident triage and remediation, data-centric ETL (extract, transform, and load), and more.
Key architecture components include a workflow engine, such as Power Automate, Logic Apps, Copilot Studio topics, Microsoft Foundry workflows, and others, to orchestrate processes. Agents can span a spectrum of approaches, including declarative, custom-built, or off-stack connected agents, providing flexibility for different scenarios.
Model each step in the workflow with explicit sequencing and guards, including clear preconditions, post-conditions, and numerical thresholds. Design agents for autonomy and re-entrance, ensuring idempotency with robust retry logic and dead-letter handling. Incorporate approval gates and other human-in-the-loop review steps through familiar channels like Teams or Outlook. Finally, enforce security with a least-privilege approach: scope connector permissions, use managed identities and credentials at each step, and apply Model Context Protocol (MCP) tool access policies to maintain compliance and control.
You can execute workflow-oriented multi-agent solutions serially or in parallel, as described in Sequential orchestration and Concurrent orchestration .
Serial workflow multi-agent considerations 
Use this pattern when:
The use case requires or benefits from quality gates at each step of a workflow or process. 
Time to completion tolerates delays or longer processing times due to lack of parallelization or horizontal scaling. 
Example use cases include batch document processing and schedule-based shipping logistics. 
Don't use this pattern when:
The use case benefits from parallel processing. 
The use case is simple enough for a single agent. 
The workflow requires iteration or dynamic routing. 
Concurrent workflow multi-agent considerations 
Use this pattern when:
The workflow benefits from quorum or voting based decisions. 
The process benefits from parallel processing. 
Don't use this pattern when:
The task requires a serial order of tasks or inputs. 
Creating parallel branches increases the complexity or reduces the quality of combining concurrent outputs. 
Agents can't reliably coordinate to shared state or within a common response window. 
Feedback 
Was this page helpful?
Yes 
No 
No 
Need help with this topic?
Want to try using Ask Learn to clarify or guide you through this topic?
Ask Learn 
Ask Learn 
Suggest a fix? 
Additional resources
Last updated on 
2026-05-20
