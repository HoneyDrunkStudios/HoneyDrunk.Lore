---
source: "https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/"
title: "Least privilege AI agents: A new azd template from Curity and Microsoft"
author: "Azure Blog"
date_published: "Thu, 07 May 2026 21:26:27 +0000"
date_clipped: "2026-05-09"
category: "Azure & Cloud"
source_type: "rss"
---

# Least privilege AI agents: A new azd template from Curity and Microsoft

Source: https://devblogs.microsoft.com/azure-sdk/azd-curity-least-privilege-ai-agents/

If you ever built an AI agent demo, you probably had this moment. Everything works: the agent interprets natural language, calls the right tools, and returns the right data. Then you start designing for the real users of the app. You think about data boundaries: what if someone tries to get data they’re not supposed to see?
For example, imagine a customer support app where users can say “give me a markdown report on the last three months of stock transactions and the value of my portfolio.” Then an agent does the work. First, you need to design for security so the agent doesn’t commingle data from separate customers. What stops the agent from showing one customer another customer’s portfolio?
This scenario is a design question we need to answer now. We spoke with the Curity team about how they think about security and they had a template in mind for building agents. This post walks through what’s in it and why we made the choices we did.
What the template gives you 
The new azd template deploys a full AI agent app to Azure. You get:
A backend agent on Microsoft Foundry , built in C# with the Microsoft A2A and MCP SDKs. 
An MCP server that exposes a sample portfolio API. 
The Curity Identity Server configured as an authorization server, working alongside Microsoft Entra ID for user authentication. 
External and internal API gateways that handle token exchange and audit logging. 
Bicep that provisions the Azure infrastructure (Container Apps, virtual network, container registry, Azure AI Foundry resource, Key Vault, Azure SQL Database, and storage for config files). 
A few azd commands and it’s all running in your subscription. From there, you can explore further and customize it to your customer scenarios.
Why put authorization in the template 
It’s easy to confuse authentication with authorization. The user’s identity doesn’t tell you what data they should see. Most agent samples handle the first part well, but they leave a real question unanswered: when an agent calls your API on behalf of a user, how does the API know what data this user is allowed to see?
This scenario matters more for agents than it does for traditional clients. A regular client app makes predictable API calls. An AI agent is nondeterministic. It interprets natural language and decides what to call. It can be creative. It can also be wrong. And if someone tricks it through prompt injection, you need rules that don’t depend on the AI being perfect.
We like that this template shows a pattern that holds up against creative agents, mistakes, and prompt injection beyond the happy path.
The pattern: Short-lived tokens with the right values inside 
The template uses OAuth 2.0 access tokens. Agents never get permanent access to the APIs. They get short-lived tokens that carry exactly the information the API needs to make a decision.
Here’s what one of those tokens looks like at the Portfolio MCP Server. It’s the third token in the chain, and two token exchanges produce it. The first exchange narrows the scope of the user’s initial token and converts it from an opaque token to a JSON Web Token (JWT). The second exchange adds the agent identity and a new audience for the MCP server hop.
{
"jti": "fc7fbe2a-27d1-4a95-ab05-5a95bd236a07",
"delegationId": "2818695a-949a-4622-b5cb-9c1a9ba49716",
"exp": 1771434954,
"nbf": 1771434054,
"scope": "stocks/read",
"iss": "http://localhost:8443/oauth/v2/oauth-anonymous",
"sub": "62c839b8214aa1fe8cbcd823948a4bc705fbbba69c7666e334ee5c7fb348b60a",
"aud": "https://mcp.demo.example",
"iat": 1771434054,
"purpose": "access_token",
"customer_id": "178",
"region": "USA",
"client_id": "console-client",
"client_type": "ai-agent",
"agent_id": "autonomous-agent"
} 
scope is stocks/read (read-only). customer_id is 178 , which comes from an Entra ID attribute. region is USA , also from Entra ID, and restricts which stocks the user can see. client_type is ai-agent , which lets the API tighten authorization specifically when an agent is in the call chain. The MCP server uses these values to filter the data it returns. So no matter what the agent decides to do, it can only see stocks for customer 178 in the USA region.
For developers, the token-driven filtering is the part we like the most: the API code stays clean. The MCP server pulls values out of the token and uses them in its queries. There’s no custom authorization logic to write. The hard work happens upstream, where someone designs the token in the first place.
Gary and the team at Curity have designed tokens for years. Much of the template came from that expertise: which values to put in, what scopes to define, and how to think about least privilege. For their take from the identity side, see Gary’s post on the Curity blog .
What’s interesting about the deployment 
The template uses a layered Bicep approach:
A base layer with networking, the container registry, and shared services. 
An identity layer with the Curity Identity Server and the API gateways. 
An applications layer with the agent and the MCP server. 
Everything runs on an internal Container Apps network, and the template exposes only the endpoints that need to be public. An external gateway sits in front of the agent and handles token exchange so internet clients never see the rich JWTs that flow internally. An internal gateway sits between the agent and the MCP server, where it writes audit logs and enforces coarse rules. For example, blocking certain scopes from agent-issued tokens. Most teams already deploy APIs and services on Azure in this fashion, so the pattern should feel familiar to your platform team.
The Curity Identity Server runs in containers in Azure that the template pulls from Curity’s container registry. (Outside this template, you can also deploy Curity from the Microsoft Marketplace if that fits your procurement story better.) Entra ID handles user sign-in and identity storage. You’re not replacing Entra ID. You’re adding a token issuer next to it that gives the agents the short-lived, narrowly scoped credentials they need.
Where to take it from here 
The basic template gets you a working agent with proper authorization. From there, the more interesting scenarios are the ones we’re seeing real teams ask about:
Human approval in the loop. A user says “buy 1,000 shares of CONTOSO when the price drops below $50.” When the price hits, the agent pauses for a human to confirm before getting a token with enough scope (say, stocks/write ) to place the trade. 
Working across organizations. An agent at one company calls an agent at a partner company, passing along the right context about who the user is and what they’re allowed to do. 
Both of these scenarios are token design problems more than they’re AI problems, which is why we wanted a template that puts authorization front and center.
Try it 
The template is on GitHub: curityio/azd-ai-autonomous-agent . The README walks you through prerequisites, local-first quickstart, and the layered Azure deployment.
A few tips before you start:
Run it locally first. The template ships with a local end-to-end flow ( ./tools/local/backend.sh ) that runs everything in Docker. It’s the fastest way to see the token exchange in action before you deploy to Azure. 
Pick a region that supports gpt-4.1-mini . East US 2, Sweden Central, and UK South are good choices. Check region availability before you start. 
Use dev as the environment name when azd init prompts you. The deployment scripts and audit-log commands in the README assume it. 
Watch tokens flow. Tail the internal gateway’s audit logs ( az containerapp logs show --resource-group rg-dev --name gateway-internal-dev --follow ) to see scope , customer_id , region , and agent_id on every call. 
If you’d like the deeper identity perspective on the same template, Gary’s post on the Curity blog covers the token design side in more detail. And if you build something with the template, open an issue on the template repo and tell us about it.
Additional resources 
Azure Developer CLI documentation 
awesome-azd template gallery 
Microsoft Foundry documentation 
Curity Identity Server 
OAuth 2.0 authorization framework 
Azure Developer CLI GitHub repository
