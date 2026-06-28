---
source: "https://devblogs.microsoft.com/azure-sdk/functions-mcp-updates-build-2026/"
title: "Azure Functions MCP Extension: What's New at Build 2026"
author: "Lily Ma"
date_published: "2026-06-24"
date_clipped: "2026-06-28"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure Functions MCP Extension: What's New at Build 2026

Source: https://devblogs.microsoft.com/azure-sdk/functions-mcp-updates-build-2026/

The Azure Functions MCP extension provides simple abstractions to help you build and host MCP servers without having to learn the protocol details yourself. You can use the triggers and bindings model to expose any function as an MCP tool, resource, or prompt. Since its initial preview, the extension has grown from supporting a single trigger type into a full-featured platform for building remote MCP servers: with tool, resource, and prompt triggers across multiple languages, MCP Apps for interactive UIs, built-in MCP authentication, and many feature enhancements. Here’s what’s new and what it means for developers building MCP servers on Azure Functions.
The full MCP primitive set: Tools, resources, and prompts 
When the MCP extension first shipped, it supported tool triggers. Declare a function as an MCP tool, and any MCP client can discover and call it. That was the starting point.
Since then, we’ve shipped the remaining MCP primitives:
Resource triggers : expose a function as an MCP resource . Resources serve context to clients: file contents, database schemas, UI components, or any data an agent needs to understand before acting. This is also the foundation for MCP Apps (more on that below). 
Prompt triggers : expose a function as an MCP prompt , letting clients request structured prompt templates from your server. 
Like tool triggers, resource and prompt triggers are supported in multiple languages including .NET, Java, Python, TypeScript, and JavaScript.
MCP Apps: interactive UI from your MCP server 
MCP Apps let your tools return interactive user interfaces instead of plain text. Combine tool triggers with resource triggers, and your MCP server can serve rich, rendered experiences to MCP-aware clients.
The Azure Functions MCP extension supports MCP Apps natively, meaning the same function app that exposes tools and resources can also serve UI components. The launch blog post on the Azure Apps Blog walked through the pattern in detail.
For .NET developers, the new fluent builder API (available in the latest NuGet release ) makes it easier to compose MCP Apps by chaining tool and resource definitions in a declarative style.
MCP authentication 
The extension supports built-in MCP authentication , implementing the requirements of the MCP auth spec. All samples in the aka.ms/remote-mcp repo enable built-in MCP auth by default with Microsoft Entra ID as the identity provider.
Samples have also been updated to demonstrate how to exchange tokens in the On-Behalf-Of (OBO) flow, so your MCP tools can access downstream APIs using the invoking user’s identity.
Auth configuration in the Azure portal : Preview at Build is a one-click experience in the Azure portal for configuring built-in MCP auth. No more manual app registration creating, configuration and wiring to the server. Just open your server app on the portal and click to enable MCP auth. Try it out !
Feature enhancements 
Beyond the headline primitives and auth, the extension has shipped a steady stream of capabilities the past few months. The following are the notable additions.
Structured content 
Structured content lets you return machine-readable JSON metadata alongside your tool’s response via the structuredContent field. Clients that support it can programmatically consume the data (e.g. parse fields, render tables, drive downstream logic) rather than just displaying text. Clients that don’t support it still get the regular content blocks as a fallback.
Rich content types 
Tools aren’t limited to returning plain text. The extension supports the full set of MCP content block types, e.g. TextContent , ImageContent , AudioContent , ResourceLink , and EmbeddedResource , so your tools can return images, audio clips, references to resources, and inline file content alongside text.
Input and output schemas 
WithInputSchema and WithOutputSchema give you explicit control over the JSON schemas advertised for your tools. This is especially useful when the auto-generated schema from function parameters doesn’t capture the full contract. For example, when your tool accepts a complex nested object or returns a specific shape that clients depend on. Input and output schemas are currently supported in .NET, with support for other languages coming soon.
builder.ConfigureMcpTool("SearchDocs")
.WithOutputSchema("""
{
"type": "object",
"properties": {
"results": { "type": "array", "items": { "type": "string" } },
"query": { "type": "string" }
},
"required": ["results", "query"]
}
"""); 
Fluent configuration APIs in .NET 
A set of fluent builder APIs that let you configure MCP primitives declaratively in Program.cs :
ConfigureMcpTool : add properties, metadata, input/output schemas, or promote a tool to an MCP App 
ConfigureMcpResource : attach metadata to resources 
ConfigureMcpPrompt : define prompt arguments and metadata 
builder.ConfigureMcpTool("sayhello")
.WithProperty("name", McpToolPropertyType.String, "Name of the user", required: true)
.WithMetadata("ui", new { resourceUri = "ui://index.html" }); 
What’s next 
Usage of the MCP extension has grown steadily since its preview launch. Tool execution volume has increased 15x over the past six months as more customers move from experimentation to production. As adoption grows, so do the expectations. Developers building production MCP servers are hitting real friction around auth complexity, client configuration, and observability. We’re continuing to invest in the extension to address these gaps and help customers be more successful building and hosting MCP servers on Azure Functions. Here’s where we’re focusing next.
Continued auth simplification 
Auth remains the biggest barrier to getting an MCP server into production. We’ll work on:
Smoother client setup : making it easier to connect any MCP client to an authenticated Azure Functions MCP server, not just VS Code. 
Simplified OBO flow : streamlining the experience of On-Behalf-Of authentication so developers can delegate user identity to downstream services with less configuration. 
Our goal: the secure path should be the easy path.
Deeper integration with Microsoft Foundry 
We’ll build tighter integration between Azure Functions MCP servers and Microsoft Foundry . This includes surfacing MCP servers in Foundry Toolbox , a new feature introduced to help Foundry agents discover and consume tools from a single endpoint. Developers will be able to publish an MCP server from Functions and have it available to Foundry agents through Toolbox without manual endpoint configuration.
Continued feature enhancement 
We prioritize based on feedback from the community raised in our GitHub repo . For example, support for streaming output and pagination are top items in our backlog today based on user demand.
We also track the MCP spec’s evolution closely and will continue shipping support for strategic features as they land. Examples of proposals we’re eyeing on:
MCP Tasks : the Tasks extension (SEP-1686) defines a standard pattern for async, long-running tool calls with durable task handles. This replaces hand-rolled polling patterns and aligns well with Functions’ execute-and-return model. 
Stateless MCP : SEP-2575 proposes removing the mandatory initialization handshake, which is a natural fit for serverless platforms like Azure Functions where fresh instances can handle any request. 
Have something you’d like us to prioritize? Let us know by filing a request on GitHub .
Get started 
Samples : Samples showcasing most up-to-date features: aka.ms/remote-mcp 
Documentation : Model Context Protocol for Azure Functions 
MCP Extension GitHub repo : Azure Functions MCP Extension
