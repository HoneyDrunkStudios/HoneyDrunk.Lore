---
source: "https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/"
title: "Give your Foundry Agent Custom Tools with MCP Servers on Azure Functions"
author: "Azure SDK Blog"
date_published: "2026-04-10"
date_clipped: "2026-07-03"
category: "Azure & Cloud"
source_type: "web"
---

# Give your Foundry Agent Custom Tools with MCP Servers on Azure Functions

Source: https://devblogs.microsoft.com/azure-sdk/give-your-foundry-agent-custom-tools-with-mcp-servers-on-azure-functions/

Lily Ma
Feature Product Manager
This blog post is for developers who have an MCP server deployed to Azure Functions and want to connect it to Microsoft Foundry agents. It walks through why you’d want to do this, the different authentication options available, and how to get your agent calling your MCP tools.
Connect your MCP server on Azure Functions to Foundry Agent
Azure Functions is a great place to host remote MCP servers with scalable infrastructure, built-in auth, and serverless billing. But hosting an MCP server is only half the picture. The real value comes when something actually uses those tools.
Microsoft Foundry lets you build AI agents that can reason, plan, and take actions. By connecting your MCP server to an agent, you’re giving it access to your custom tools, whether that’s querying a database, calling an API, or running some business logic. The agent discovers your tools, decides when to call them, and uses the results to respond to the user.
Why connect MCP servers to Foundry agents?
You might already have an MCP server that works great with VS Code, Visual Studio, Cursor, or other MCP clients. Connecting that same server to a Foundry agent means you can reuse those tools in a completely different context. For example, in an enterprise AI agent that your team or customers interact with. No need to rebuild anything. Your MCP server stays the same; you’re just adding another consumer.
Prerequisites
Before proceeding, make sure you have the following:
An MCP server deployed to Azure Functions. If you don’t have one yet, you can deploy one quickly by following one of the samples:
Python
TypeScript
.NET
Java
A
Foundry project with a deployed model
and a
Foundry agent
Authentication options
Depending on where you are in development, you can pick what makes sense and upgrade later. Here’s a summary:
Method
Description
Use case
Key-based (default)
Agent authenticates by passing a shared
function access key
in the request header. This method is the default authentication for HTTP endpoints in Functions.
Use during development or when the MCP server doesn’t require Microsoft Entra authentication.
Microsoft Entra
Agent authenticates using either its own identity (
agent identity
) or the shared identity of the Foundry project (
project managed identity
).
Use agent identity for production scenarios, but limit shared identity to development.
OAuth identity passthrough
Agent prompts users to sign in and authorize access, using the provided token to authenticate.
Use in production when each user must authenticate with their own identity and user context must be persisted.
Unauthenticated access
Agent makes unauthenticated calls.
Use during development or when your MCP server accesses only public information.
Connect your MCP server to your Foundry agent
If your server uses key-based auth or is unauthenticated, it should be relatively straightforward to set up the connection from a Foundry agent.
The Microsoft Entra and OAuth identity passthrough are options that require extra steps to set up. Check out
detailed step-by-step instructions
for each authentication method.
At a high level, the process looks like this:
Enable
built-in MCP authentication
: When you deploy a server to Azure Functions, key-based auth is the default. You’ll need to disable that and enable built-in MCP auth instead. If you deployed one of the sample servers in the
Prerequisites
section, this step is already done for you.
Get your MCP server endpoint URL
: For MCP extension-based servers, it’s
https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/mcp
.
Get your credentials based on your chosen auth method
: A managed identity configuration, OAuth credentials, or a function key.
Add the MCP server as a tool in the Foundry portal
by navigating to your agent, adding a new MCP tool, and providing the endpoint and credentials.
Microsoft Entra connection required fields:
Field
Description
Example
Name
A unique identifier for your MCP server. You can use your function app name.
contoso-mcp-tools
Remote MCP Server endpoint
The URL endpoint for your MCP server.
https://contoso-mcp-tools.azurewebsites.net/runtime/webhooks/mcp
Authentication
The authentication method to use.
Microsoft Entra
Type
The identity type the agent uses to authenticate.
Project Managed Identity
Audience
The Application ID URI of your function app’s Entra registration. This value tells the identity provider which app the token is intended for.
api://00001111-aaaa-2222-bbbb-3333cccc4444
OAuth identity passthrough required fields:
Field
Description
Example
Name
A unique identifier for your MCP server. You can use your function app name.
contoso-mcp-tools
Remote MCP Server endpoint
The URL endpoint for your MCP server.
https://contoso-mcp-tools.azurewebsites.net/runtime/webhooks/mcp
Authentication
The authentication method to use.
OAuth Identity Passthrough
Client ID
The client ID of your function app Entra registration.
00001111-aaaa-2222-bbbb-3333cccc4444
Client secret
The client secret of your function app Entra registration.
abcEFGhijKLMNopqRST
Token URL
The endpoint your server app calls to exchange an authorization code or credential for an access token.
https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token
Auth URL
The endpoint where users are redirected to authenticate and grant authorization to your server app.
https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/authorize
Refresh URL
The endpoint used to obtain a new access token when the current one expires.
https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token
Scopes
The specific permissions or resource access levels your server app requests from the authorization server.
api://00001111-aaaa-2222-bbbb-3333cccc4444/user_impersonation
Once the server is configured as a tool, test it in the Agent Builder playground by sending a prompt that triggers one of your MCP tools.
Closing thoughts
What I find exciting about this is the composability. You build your MCP server once and it works everywhere: VS Code, Visual Studio, Cursor, ChatGPT, and now Foundry agents. The MCP protocol is becoming the universal interface for tool use in AI, and Azure Functions makes it easy to host these servers at scale and with security.
Are you building agents with Foundry? Have you connected your MCP servers to other clients? I’d love to hear what tools you’re exposing and how you’re using them. Share with us your thoughts!
What’s next
In the next blog post, we’ll go deeper into other MCP topics and cover new MCP features and developments in Azure Functions. Stay tuned!
Category
Azure SDK
Topics
.NET
ai-agents
azure
Azure Functions
best-practices
foundry
java
MCP
microservices
model-context-protocol
node.js
python
serverless
Share
Author
Lily Ma
Feature Product Manager
I am a PM on the Azure Functions team driving MCP hosting experience and Durable Functions. Previously I was a PM on the Azure SDK team.
2
comments
Discussion is closed.
Login to edit/delete existing comments.
Sort by :
Newest
Newest
Popular
Oldest
Why is .NET second to last again? Python, TypeScript, .NET, Java.
Hi Vladimir, there’s nothing special behind the ordering. All the languages specified are supported.
Read next
April 10, 2026
Announcing Azure MCP Server 2.0 Stable Release for Self-Hosted Agentic Cloud Automation
Sandeep Sen
April 14, 2026
Stop juggling package managers—just run `azd update`
Kristen Womack
Stay informed
Get notified when new posts are published.
Follow this blog
Are you sure you wish to delete this
comment?
