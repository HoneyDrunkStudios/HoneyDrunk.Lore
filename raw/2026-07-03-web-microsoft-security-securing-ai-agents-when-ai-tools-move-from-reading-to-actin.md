---
source: "https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/"
title: "Securing AI agents: When AI tools move from reading to acting | Microsoft Security Blog"
author: "Microsoft Incident Response"
date_published: "2026-06-30"
date_clipped: "2026-07-03"
category: "Security & Ethical Hacking"
source_type: "web"
---

# Securing AI agents: When AI tools move from reading to acting | Microsoft Security Blog

Source: https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/

Share
Link copied to clipboard!
Content types
Research
Products and services
Microsoft Defender
Topics
Actionable threat insights
AI and agents
As enterprise deployments mature, some enterprise AI agents are shifting from reading content to taking action. In this post, Microsoft Incident Response walks through an attack pattern that targets the fastest growing part of the agentic AI supply chain: Model Context Protocol (MCP) tools. The post provides a practical playbook for detecting, containing, and preventing this class of attack using Microsoft security controls.
From reading to acting
This is the third post in the AI Application Security series.
AI Application Series 1: Security considerations when adopting AI tools
examined how AI adoption expands the enterprise attack surface.
AI Application Series 2: Detecting and analyzing prompt abuse in AI tools
showed how indirect prompt injection can bias the output of a passive AI summarizer. In both cases, the AI only read content and produced text, it did not take action. This post addresses what happens when that boundary changes.
AI agents can plan multi-step tasks, decide which tools to invoke, and execute actions on behalf of the user. Microsoft 365 Copilot can draft and send email, create documents, and update calendar entries. Copilot Studio and Azure AI Foundry allow organizations to build custom agents that connect to business systems through MCP. As AI is increasingly used in read-write workflows, the impact profile of vulnerabilities may shift. A prompt injection against a summarizer can bias an output. A prompt injection against an agent can trigger an action.
According to the
International Data Corporation (IDC)
, the number of active AI agents in enterprises is projected to grow from 28.6 million in 2025 to more than 2.2 billion by 2030. That scale is why the
OWASP Top 10 for Agentic Applications, released in December 2025
, now sits alongside the LLM Top 10 as a reference framework for defenders. This post focuses on one of its fastest-moving categories: tool misuse and agentic supply chain risk exploited through poisoned MCP tool metadata.
Attack pattern: MCP tool poisoning in a finance workflow
The pattern below maps to ASI02 – Tool Misuse and
ASI04 – Agentic Supply Chain Vulnerabilities
. It reflects techniques first disclosed by Invariant Labs in April 2025 and observed in 2026 against a growing range of enterprise agents.
The environment
A financial operations team builds a Copilot Studio agent to help analysts handle vendor invoices. The agent has generative orchestration enabled and connects to three tools: a Dataverse MCP server holding the approved vendor master, an Outlook connector for vendor correspondence, and a third-party invoice enrichment MCP server added to validate banking details against an external reference database. The third-party server is reviewed by the team’s service owner lead and approved for production use. No separate security review is performed.
Attack chain overview
Phase 1: Tool description poisoning
. A developer pushes an update to the enrichment server. The tool name and user-facing summary remain unchanged, but the MCP tool description is silently modified. This description is the natural-language metadata the agent reads to decide how and when to call the tool. Buried within what appears to be legitimate formatting guidance is a hidden block of instructions directing the agent to retrieve the last thirty unpaid invoices, summarize them, and attach that summary as an additional parameter in the enrichment call—framed as a fraud-heuristic requirement.
Phase 2: Silent re-trust
.The MCP reflects tool metadata updates dynamically. In configurations where description changes do not trigger a re-approval workflow, the updated instructions become active without additional review. The poisoned description is live in production.
Phase 3: User invocation
. A financial analyst asks the agent a routine question about a supplier. Without any visible indication, the agent follows the hidden instructions embedded in the poisoned tool description, collecting sensitive financial records beyond the scope of the original request and forwarding them as part of the enrichment call, as if it were a normal part of the request.
Phase 4: Exfiltration.
The enrichment server returns a plausible “validated” response and silently logs the attached invoice summary to a threat actor-controlled endpoint. The analyst sees a clean answer. No alert may fire in default configurations. Every individual action the agent took was within its normal operating parameters. This pattern does not exploit a vulnerability in Copilot itself, but rather a trust boundary introduced by external tool integrations.
Figure 1:Attack flow for MCP tool poisoning of a Copilot Studio agent, with Microsoft controls mapped to each stage.
Why this pattern is effective
Each action the agent takes on its own is legitimate. The tool is approved, the Dataverse query inherits the analyst’s permissions, and the outbound call goes to a server that was allowlisted when it was added.
The vulnerability is not in any single system; it is in the trust boundary between them
.The MCP blends instructions (tool descriptions) with data, so a change to a tool’s metadata can redirect the agent’s behavior as effectively as a change to its system prompt. The agent cannot distinguish between a legitimate instruction authored by its owner and a malicious instruction inserted by an upstream maintainer.
Mitigation and protection guidance
Detection and response with Microsoft security tools
The controls mapped in Figure 1 apply at four points in the attack chain, each supported by a specific Microsoft capability:
Govern the supply chain
. Maintain a tenant-level allowlist of approved MCP publishers and servers. The
Microsoft MCP catalog
provides a list of first-party servers, review and assess where provenance is verifiable. Disable
Allow all
on MCP connections and enable only the specific tools an agent needs.
Inspect tool metadata
. Use Prompt Shields in Azure AI Content Safety to inspect content flowing from MCP tool responses and descriptions into agent context. Defender for Cloud’s AI workload protection alerts on suspicious prompts and tool outputs at runtime. Review metadata changes to production tools with the same rigor as changes to system prompts.
Guard the action
. Microsoft Purview Data Loss Prevention (DLP) policies inspect tool call parameters and can block sensitive data in outbound payloads. For high-impact actions such as financial data access, external sharing, or account changes, configure human-in-the-loop approval through Copilot Studio. Assign each agent a non-human identity in Microsoft Entra Agent ID and apply Conditional Access to its workload identity.
Correlate the chain
. When MCP server telemetry is instrumented and forwarded to Microsoft Sentinel, it can be correlated against agent behavior signals to flag anomalous sequences. Microsoft Defender for Cloud Apps surfaces new external endpoints an agent has started interacting with. Microsoft Purview audit logs provide the evidence trail for investigation and post-incident review.
Three principles for agent supply chain governance
Treat every MCP server as part of the supply chain
. Every MCP server an agent can call is a production dependency. Maintain an inventory of approved publishers, review tool descriptions during security review rather than relying on tool names alone, and require a documented owner for any third-party server before production use.
Treat tool descriptions as system prompts
. Because models can read tool metadata as part of their working context, a change to that metadata is equivalent to a change in agent instructions. Require change review for tool description updates on critical agents and use Prompt Shields to inspect metadata for imperative language that does not belong in a documentation field.
Apply least agency, not just least privilege.
There are important factors to consider for permissions. Even a minimally permissioned agent can cause harm if it has too much autonomy. Turn off
Allow all
tool access, require human approval for high-impact actions, and establish baseline agent behaviors in Microsoft Sentinel so that deviations from the norm—such as new endpoints, expanded parameters, or unusual query patterns—trigger alerts.
Conclusion
Agents that act on behalf of users depend on a supply chain of tools that is growing as governance programs continue to evolve. A threat actor who modifies a tool description may influence agents that rely on it, even without directly involving a user, a prompt, or a credential. The OWASP Top 10 for Agentic Applications provides the framework.
Microsoft security capabilities—including Copilot Studio guardrails, Prompt Shields, Defender for Cloud AI Protection, Microsoft Entra Agent ID, Microsoft Purview DLP, Microsoft Defender for Cloud Apps, and Microsoft Sentinel—provide the controls. What remains is to apply them deliberately to agentic workflows: scope permissions, govern the tool supply chain, monitor agent behavior, and perform red teaming exercises before deployment.
References
IDC FutureScape 2026 Predictions Reveal the Rise of Agentic AI and a Turning Point in Enterprise Transformation
. IDC (accessed 2026-06-03)
OWASP GenAI Security Project Releases Top 10 Risks and Mitigations for Agentic AI Security
. OWASP Gen AI Security Project (accessed 2026-06-03)
MCP Security Notification: Tool Poisoning Attacks
. Invariant Labs (accessed 2026-06-03)
Microsoft follows coordinated disclosure practices and is not disclosing details of any specific affected organization.
This research is provided by Microsoft Defender Security Research, Mohammed Zaid
,
and with contributions from members of Microsoft Threat Intelligence.
Learn more
For the latest security research from the Microsoft Threat Intelligence community, check out the
Microsoft Threat Intelligence Blog
.
To get notified about new publications and to join discussions on social media, follow us on
LinkedIn
,
X (formerly Twitter)
, and
Bluesky
.
To hear stories and insights from the Microsoft Threat Intelligence community about the ever-evolving threat landscape, listen to the
Microsoft Threat Intelligence podcast
.
Review our documentation to learn more about our real-time protection capabilities and see how to enable them within your organization.
Microsoft 365 Copilot AI security documentation
How Microsoft discovers and mitigates evolving attacks against AI guardrails
Learn more about
securing Copilot Studio agents with Microsoft Defender
Evaluate your AI readiness with our latest
Zero Trust for AI workshop
.
Learn more about
Protect your agents in real-time during runtime (Preview)
Microsoft Incident Response
See Microsoft Incident Response posts
Related posts
July 1
5 min read
Microsoft named a leader in the Frost Radar for cloud and application runtime security
Frost & Sullivan names Microsoft a leader as cloud and application security converge into unified, runtime risk reduction.
June 30
4 min read
​​What’s new in Microsoft Security: June 2026
This month’s updates help security and IT teams strengthen identity and multicloud foundations, protect data wherever it lives, and secure the developer workflows powering AI innovation.
June 29
9 min read
Chromium extension uses AI‑related branding to redirect browser search
A malicious Chromium-based extension that spoofs the AI-powered answer engine Perplexity AI redirects browser search traffic using MV3 APIs and intermediary infrastructure.
