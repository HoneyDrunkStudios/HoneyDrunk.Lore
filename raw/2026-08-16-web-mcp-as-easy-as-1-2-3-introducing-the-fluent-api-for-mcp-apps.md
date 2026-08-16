---
source: "https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/"
title: "MCP as Easy as 1-2-3: Introducing the Fluent API for MCP Apps"
author: "Lilian Kasem"
date_published: "2026-04-07"
date_clipped: "2026-08-16"
category: "Azure & Cloud"
source_type: "web"
---

# MCP as Easy as 1-2-3: Introducing the Fluent API for MCP Apps

Source: https://devblogs.microsoft.com/azure-sdk/mcp-as-easy-as-1-2-3-introducing-the-fluent-api-for-mcp-apps/

Earlier this year, we introduced MCP Apps in the Azure Functions MCP extension. These are tools that go beyond text and render full UI experiences, serve static assets, and integrate seamlessly with AI agents. If you haven’t tried them yet, the MCP Apps quickstart is a great place to start.
Today, we’re making Model Context Protocol (MCP) Apps even easier to build. We’re introducing a fluent configuration API for the .NET isolated worker that lets you promote any MCP tool to a full MCP App complete with views, permissions, and security policies in just a few lines of code.
What are MCP Apps?
MCP Apps extend the Model Context Protocol tool model by allowing individual tools to be configured as apps. Tools that come with their own UI views, static assets, and fine-grained security controls. Think of them as MCP tools that can present rich, interactive experiences to users while still being invocable by AI agents.
With MCP Apps, you can:
Attach HTML views to your tools, rendered by the MCP client.
Serve static assets (HTML, CSS, JavaScript, images) alongside your tool.
Control permissions like clipboard access, allowing your app to interact with the user’s environment in a controlled way.
Define Content Security Policies (CSP) to lock down what your app can load and connect to.
Why a Fluent API?
One of the key goals of the Fluent API is to abstract away the MCP spec so you don’t need to know the protocol details to build an app. In the MCP protocol, connecting a tool to a UI view requires precise coordination: a resource endpoint at a ui:// URI, a special mime type ( text/html;profile=mcp-app ) that tells clients to render the content as an interactive app, and _meta.ui metadata on both the tool and resource to wire everything together. For example, the tool metadata carries a resourceUri and visibility so the client knows the tool has a UI, while the resource response carries the CSP, permissions, and rendering hints so the client knows how to display it securely.
The Fluent API handles all of this coordination for you. When you call AsMcpApp , the extension automatically generates the synthetic resource function, sets the correct mime type, and injects the metadata that connects your tool to its view. You just write your function, point it at an HTML file, and configure the security policies you need.
Get started
The Fluent API for MCP Apps is available in the Microsoft.Azure.Functions.Worker.Extensions.Mcp NuGet package. If you’re already building MCP tools with Azure Functions, you’re just a package update away:
dotnet add package Microsoft.Azure.Functions.Worker.Extensions.Mcp --version 1.5.0
This package includes all the fluent configuration APIs covered in this post.
The Fluent API
Here’s the complete setup for a simple “Hello App”:
Step 1: Define your function
Start with a standard Azure Functions MCP tool. The [McpToolTrigger] attribute wires up your function as an MCP tool, just like before:
[Function(nameof(HelloApp))]
public string HelloApp(
[McpToolTrigger("HelloApp", "A simple MCP App that says hello.")] ToolInvocationContext context)
{
return "Hello from app";
}
Step 2: Configure it as an MCP App
In your program startup, use the Fluent API to promote your tool to a full MCP App:
builder.ConfigureMcpTool("HelloApp")
.AsMcpApp(app => app
.WithView("assets/hello-app.html")
.WithTitle("Hello App")
.WithPermissions(McpAppPermissions.ClipboardWrite | McpAppPermissions.ClipboardRead)
.WithCsp(csp =>
{
csp.AllowBaseUri("https://www.microsoft.com")
.ConnectTo("https://www.microsoft.com");
}));
Step 3: Add your view
Create an HTML file at assets/hello-app.html in your project. This is the UI that MCP clients render when your app tool is invoked. You have full control over the markup, styling, and client-side behavior.
That’s it. Three steps and your MCP tool is now an MCP App with a rich UI.
Breaking down the API
Let’s walk through each part of the fluent configuration.
ConfigureMcpTool("HelloApp")
Selects the MCP tool you want to configure. The name must match the function name registered with [McpToolTrigger] .
.AsMcpApp(app => ...)
Promotes the tool to an MCP App. Everything inside the lambda configures the app-specific behavior via the IMcpAppBuilder interface.
.WithView(...)
Sets the view for the app. You can provide a file path directly, or use one of the McpViewSource factory methods for more control:
// File on disk (relative to output directory)
app.WithView("assets/hello-app.html")
// Explicit file source
app.WithView(McpViewSource.FromFile("assets/hello-app.html"))
// Embedded resource from an assembly
app.WithView(McpViewSource.FromEmbeddedResource("MyApp.Resources.view.html"))
The McpViewSource abstraction lets you choose where your HTML lives: on disk alongside your function, or embedded directly in your assembly for self-contained deployment.
.WithTitle("Hello App")
Sets a human-readable title for the view, displayed by MCP clients in their UI.
.WithBorder()
Hints to the MCP client that it should render a border around the view. Pass false to explicitly opt out, or omit it entirely to let the client decide:
.WithBorder() // prefer border
.WithBorder(false) // prefer no border
.WithDomain("myapp.example.com")
Sets a domain hint for the view, used by the host to scope cookies and storage for your app.
.WithPermissions(...)
Controls what the app is allowed to do in the client environment. Permissions are defined as flags on McpAppPermissions :
Permission
Description
ClipboardRead
Allows the app to read from the clipboard
ClipboardWrite
Allows the app to write to the clipboard
Permissions are opt-in, so your app only gets the access it explicitly requests.
.WithCsp(csp => ...)
Defines the Content Security Policy for the app’s view. The CSP builder ( IMcpCspBuilder ) provides four methods, each mapping to standard CSP directives:
Method
CSP Directive
Purpose
ConnectTo(origin)
connect-src
Network requests (fetch, XMLHttpRequest, WebSocket)
LoadResourcesFrom(origin)
img-src , script-src , style-src , font-src , media-src
Static resources (scripts, images, styles, fonts, media)
AllowFrame(origin)
frame-src
Nested iframes
AllowBaseUri(origin)
base-uri
Base URI for the document
.WithCsp(csp =>
{
csp.ConnectTo("https://api.example.com")
.LoadResourcesFrom("https://cdn.example.com")
.AllowFrame("https://youtube.com")
.AllowBaseUri("https://www.microsoft.com");
})
You can call WithCsp multiple times. Origins accumulate across calls, so you can compose CSP configuration from multiple sources. By default, the CSP is restrictive; you explicitly allowlist the origins your app needs, following the principle of least privilege.
.WithVisibility(...)
Controls who can see the tool. The McpVisibility flags enum has two values:
Visibility
Description
Model
Visible to the large language model (LLM) during tool selection
App
Visible to the host UI for rendering
By default, tools are visible to both ( Model | App ). You can restrict visibility if, for example, you want a tool that only renders UI and shouldn’t be invoked by the model directly:
.ConfigureApp()
.WithVisibility(McpVisibility.App) // UI-only, hidden from the model
.WithStaticAssets(...)
Configures a directory from which static assets (CSS, JS, images) are served alongside your view:
.ConfigureApp()
.WithStaticAssets("assets/dist")
// Or with options
.WithStaticAssets("assets/dist", options =>
{
options.IncludeSourceMaps = true; // default: false, to avoid leaking internal paths
})
By default, .map files are excluded from serving to avoid leaking internal paths and implementation details.
Builder navigation
The Fluent API uses three builder levels (tool, app, and view), and you can navigate between them:
builder.ConfigureMcpTool("Dashboard")
.AsMcpApp(app => app
.WithView("ui/dashboard.html") // returns IMcpViewBuilder
.WithTitle("Dashboard")
.WithPermissions(McpAppPermissions.ClipboardRead)
.ConfigureApp() // back to IMcpAppBuilder
.WithStaticAssets("ui/dist")
.WithVisibility(McpVisibility.Model | McpVisibility.App))
.WithProperty("dataset", McpToolPropertyType.String, "The dataset to display"); // back to tool builder
Summary
The new Fluent API for MCP Apps in the .NET isolated worker makes it straightforward to build MCP tools with rich UI experiences. With just a few lines of configuration, you can attach views, control permissions, and enforce security policies on your tools without needing to know the details of the MCP protocol. Under the covers, the extension handles synthetic resource generation, metadata wiring, mime type management, and secure asset serving, so you can focus on building great tool experiences for AI agents and users alike.
Useful links
Building MCP Apps with Azure Functions MCP Extension : the original MCP Apps announcement blog post
MCP Apps quickstart : step-by-step guide to building your first MCP App
Azure Functions MCP extension documentation : full reference for the MCP extension
