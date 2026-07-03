---
source: "https://devblogs.microsoft.com/azure-sdk/mcp-apps-on-azure-functions-quickstart-with-typescript/"
title: "MCP Apps on Azure Functions: Quickstart with TypeScript"
author: "Azure SDK Blog"
date_published: "2026-04-06"
date_clipped: "2026-07-03"
category: "Azure & Cloud"
source_type: "web"
---

# MCP Apps on Azure Functions: Quickstart with TypeScript

Source: https://devblogs.microsoft.com/azure-sdk/mcp-apps-on-azure-functions-quickstart-with-typescript/

Swapnil Nagar
Senior Software Engineer
Azure Functions makes hosting MCP apps simple: build locally, create a secure endpoint, and deploy fast with Azure Developer CLI (azd).
This guide shows you how using a weather app example.
What are MCP Apps?
MCP Apps
let MCP servers return interactive HTML interfaces such as data visualizations, forms, dashboards that render directly inside MCP-compatible hosts (Visual Studio Code Copilot, Claude, ChatGPT, etc.). Learn more about MCP Apps in the
official documentation
.
Having an interactive UI removes many restrictions that plain texts have, such as if your scenario has:
Interactive Data
: Replacing lists with clickable maps or charts for deep exploration.
Complex Setup
: Use one-page forms instead of long, back-and-forth questioning.
Rich Media
: Embed native viewers to pan, zoom, or rotate 3D models and documents.
Live Updates
: Maintain real-time dashboards that refresh without new prompts.
Workflow Management
: Handle multi-step tasks like approvals with navigation buttons and persistent state.
Hosting MCP Apps on Azure Functions
Azure Functions provides an easy abstraction to help you build MCP servers without having to learn the nitty-gritty of the MCP protocol. When hosting your MCP App on Functions, you get:
MCP tools
(server logic): Handle client requests, call backend services, return structured data – Azure Functions manages the MCP protocol details for you
MCP resources
(UI payloads such as app widgets): Serve interactive HTML, JSON documents, or formatted content – just focus on your UI logic
Secure HTTPS access
: Built-in authentication using Azure Functions keys, plus
built-in MCP authentication with OAuth support
for enterprise-grade security
Easy deployment
with Bicep and azd: Infrastructure as Code for reliable deployments
Local development
: Test and debug locally before deploying
Auto-scaling
: Azure Functions handles scaling, retries, and monitoring automatically
The weather app in this repo is an example of this feature, not the only use case.
Architecture overview
Example: The classic weather app
The sample implementation includes:
A
GetWeather MCP tool
that fetches weather by location (calls Open-Meteo geocoding and forecast APIs)
A
Weather Widget MCP resource
that serves interactive HTML/JS code (runs in the client; fetches data via GetWeather tool)
A TypeScript service layer that abstracts API calls and data transformation (runs on the server)
Local and remote testing flow for MCP clients (via MCP Inspector, Visual Studio Code, or custom clients)
How UI rendering works in MCP Apps
In the Weather App example
:
Azure Functions serves
getWeatherWidget
as a resource → returns
weather-app.ts
compiled to HTML/JS
Client renders the Weather Widget UI
User interacts with the widget or requests are made internally
The widget calls the
getWeather
tool → server processes and returns weather data
The widget renders the weather data on the client side
This architecture keeps the UI
responsive locally
while using
server-side logic and data
on demand.
Quickstart
Clone the repository:
git clone https://github.com/Azure-Samples/remote-mcp-functions-typescript.git
cd remote-mcp-functions-typescript
Run locally:
npm install
npm run build
func start
Local endpoint:
http://0.0.0.0:7071/runtime/webhooks/mcp
Deploy to Azure:
azd provision
azd deploy
Remote endpoint:
https://<function-app-name>.azurewebsites.net/runtime/webhooks/mcp
TypeScript MCP tools snippet (Get Weather service)
In Azure Functions, you define MCP tools using
app.mcpTool()
. The
toolName
and
description
tell clients what this tool does,
toolProperties
defines the input arguments (like
location
as a string), and
handler
points to your function that processes the request.
app.mcpTool("getWeather", {
toolName: "GetWeather",
description: "Returns current weather for a location via Open-Meteo.",
toolProperties: {
location: arg.string().describe("City name to check weather for")
},
handler: getWeather,
});
TypeScript MCP Resource trigger snippet (Weather App Hook)
MCP resources are defined using
app.mcpResource()
. The
uri
is how clients reference this resource,
resourceName
and
description
provide metadata,
mimeType
tells clients what type of content to expect, and
handler
is your function that returns the actual content (like HTML for a widget).
app.mcpResource("getWeatherWidget", {
uri: "ui://weather/index.html",
resourceName: "Weather Widget",
description: "Interactive weather display for MCP Apps",
mimeType: "text/html;profile=mcp-app",
handler: getWeatherWidget,
});
Sample repos and references
Complete sample repository with TypeScript implementation:
Azure-Samples/remote-mcp-functions-typescript
Official MCP extension documentation:
Azure Functions MCP bindings
Java sample:
Azure-Samples/remote-mcp-functions-java
.NET sample:
Azure-Samples/remote-mcp-functions-dotnet
Python sample:
Azure-Samples/remote-mcp-functions-python
MCP Inspector:
modelcontextprotocol/inspector
Final takeaway
MCP Apps are just MCP servers but they represent a paradigm shift by transforming the AI from a text-based chatbot into a functional interface. Instead of forcing users to navigate complex tasks through back-and-forth conversations, these apps embed interactive UIs and tools directly into the chat, significantly improving the user experience and the usefulness of MCP servers.
Azure Functions
allows developers to quickly build and host an MCP app by providing an
easy abstraction and deployment experience
. The platform also provides built-in features to
secure and scale
your MCP apps, plus a serverless pricing model so you can just focus on the business logic.
Category
Azure SDK
Topics
azure
Azure Functions
azure-developer-cli
javascript
MCP
mcp-resources
mcp-tools
model-context-protocol
python
serverless
typescript
Share
Author
Swapnil Nagar
Senior Software Engineer
Senior Software Engineer
0
comments
Discussion is closed.
Read next
April 6, 2026
Announcing the end of support for Node.js 20.x in the Azure SDK for JavaScript
Minh-Anh Phan
April 7, 2026
MCP as Easy as 1-2-3: Introducing the Fluent API for MCP Apps
Lilian Kasem (she/her)
Stay informed
Get notified when new posts are published.
Follow this blog
Are you sure you wish to delete this
comment?
