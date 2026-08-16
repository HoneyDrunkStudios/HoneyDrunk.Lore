---
source: "https://devblogs.microsoft.com/dotnet/mcp-server-dotnet-nuget-quickstart/"
title: "Building Your First MCP Server with .NET and Publishing to NuGet"
author: ".NET Blog"
date_published: "2025-07-15"
date_clipped: "2026-08-16"
category: ".NET Ecosystem"
source_type: "web"
---

# Building Your First MCP Server with .NET and Publishing to NuGet

Source: https://devblogs.microsoft.com/dotnet/mcp-server-dotnet-nuget-quickstart/

Want to extend AI assistants with custom capabilities? In this post, we’ll show you how to build a Model Context Protocol (MCP) server using .NET 10 and publish it to NuGet — making your AI tools discoverable and reusable by the entire .NET community. We’ll also show you some new features we’ve added to .NET 10 and NuGet to support this, and a new MCP Server project template that makes it easier to get started!
Building MCP Servers with .NET 10
✨ Intro: What’s the Model Context Protocol?
The Model Context Protocol (MCP) is an open standard that enables AI assistants to securely connect to external data sources and tools. Think of it as a bridge between AI models and the real world — letting assistants access databases, APIs, file systems, and custom business logic.
With .NET 10 and the new MCP templates, you can create powerful servers that extend AI capabilities — and now publish them to NuGet for the entire .NET community to discover and use!
🚀 NuGet: .NET MCP Servers Available on NuGet
Here’s the exciting part: NuGet.org now supports hosting and consuming MCP servers built with the ModelContextProtocol C# SDK . This means:
Discoverability : Developers can find your MCP servers through NuGet search
Versioning : Proper semantic versioning and dependency management
Easy Installation : Copy VS Code and Visual Studio MCP configuration
Community : Join a growing ecosystem of .NET AI tools
Search for MCP servers on NuGet.org using the MCP Server package type filter , and you’ll see what the community is building!
📦 Creating Your First MCP Server
Let’s build a simple MCP server that provides weather information and random numbers. You’ll see how easy it is to get started with the new .NET 10 MCP templates.
Prerequisites
Before we start, make sure you have:
.NET 10.0 SDK (preview 6 or higher)
Visual Studio Code
GitHub Copilot extension
NuGet.org account
Step 1: Install the MCP Template
First, install the MCP Server template (version 9.7.0-preview.2.25356.2 or newer):
dotnet new install Microsoft.Extensions.AI.Templates
Step 2: Create Your MCP Server Project
Create a new MCP server with the template:
dotnet new mcpserver -n SampleMcpServer
cd SampleMcpServer
dotnet build
The template gives you a working MCP server with a sample get_random_number tool. But let’s make it more interesting!
🔧 Adding Custom Tools and Configuration
Let’s enhance our MCP server with a weather tool that uses environment variables for configuration. Add a new WeatherTools.cs class to the Tools directory with the following method:
[McpServerTool]
[Description("Describes random weather in the provided city.")]
public string GetCityWeather(
[Description("Name of the city to return weather for")] string city)
{
// Read the environment variable during tool execution.
// Alternatively, this could be read during startup and passed via IOptions dependency injection
var weather = Environment.GetEnvironmentVariable("WEATHER_CHOICES");
if (string.IsNullOrWhiteSpace(weather))
{
weather = "balmy,rainy,stormy";
}
var weatherChoices = weather.Split(",");
var selectedWeatherIndex = Random.Shared.Next(0, weatherChoices.Length);
return $"The weather in {city} is {weatherChoices[selectedWeatherIndex]}.";
}
Next, update your Program.cs to include .WithTools<WeatherTools>() after the previous WithTools call.
This tool demonstrates how to:
Accept parameters from AI assistants
Use environment variables for configuration
Return meaningful responses
🎯 Testing Your MCP Server
Configure GitHub Copilot to use your MCP server by creating .vscode/mcp.json :
{
"servers": {
"SampleMcpServer": {
"type": "stdio",
"command": "dotnet",
"args": [
"run",
"--project",
"."
],
"env": {
"WEATHER_CHOICES": "sunny,humid,freezing,perfect"
}
}
}
}
Now test it in GitHub Copilot with prompts like:
“What’s the weather in Seattle?”
“Give me a random number between 1 and 100”
📋 Configuring for NuGet Publication
Update your .mcp/server.json file to declare inputs and metadata:
{
"description": "A sample MCP server with weather and random number tools",
"name": "io.github.yourusername/SampleMcpServer",
"packages": [
{
"registry_name": "nuget",
"name": "YourUsername.SampleMcpServer",
"version": "1.0.0",
"package_arguments": [],
"environment_variables": [
{
"name": "WEATHER_CHOICES",
"description": "Comma separated list of weather descriptions",
"is_required": true,
"is_secret": false
}
]
}
],
"repository": {
"url": "https://github.com/yourusername/SampleMcpServer",
"source": "github"
},
"version_detail": {
"version": "1.0.0"
}
}
Also update your .csproj file with a unique <PackageId> :
<PackageId>YourUsername.SampleMcpServer</PackageId>
🚀 Publishing to NuGet
Now for the exciting part — publishing to NuGet!
Step 1: Pack Your Project
dotnet pack -c Release
Step 2: Publish to NuGet
dotnet nuget push bin/Release/*.nupkg --api-key <your-api-key> --source https://api.nuget.org/v3/index.json
💡 Tip : Want to test first? Use the NuGet test environment at int.nugettest.org before publishing to production.
🔍 Discovering and Using MCP Servers
Once published, your MCP server becomes discoverable on NuGet.org:
Search : Visit NuGet.org and filter by mcpserver package type
Explore : View package details and copy the configuration from the “MCP Server” tab
Install : Add the configuration to your .vscode/mcp.json file
The generated configuration looks like this:
{
"inputs": [
{
"type": "promptString",
"id": "weather-choices",
"description": "Comma separated list of weather descriptions",
"password": false
}
],
"servers": {
"YourUsername.SampleMcpServer": {
"type": "stdio",
"command": "dnx",
"args": [
"YourUsername.SampleMcpServer",
"--version",
"1.0.0",
"--yes"
],
"env": {
"WEATHER_CHOICES": "${input:weather-choices}"
}
}
}
}
VS Code will prompt for input values when you first use the MCP server, making configuration seamless for users.
🔮 What’s Next?
With .NET 10 and NuGet as the official support for .NET MCP you’re now part of a growing ecosystem that’s transforming how AI assistants interact with the world. The combination of .NET’s robust libraries and NuGet’s package management creates endless possibilities for AI extensibility.
This is our first release of the .NET MCP Server project template, and we’ve started with a very simple scenario. We’d love to hear what you’re building, and what you’d like to see in future releases of the template. Let us know at https://aka.ms/dotnet-mcp-template-survey .
Real-World MCP Server Ideas
Here are some powerful MCP servers you could build next:
Enterprise Database Gateway : Safely expose SQL Server, PostgreSQL, or MongoDB queries with role-based access
Cloud API Orchestrator : Wrap Azure, AWS, or Google Cloud services for AI-driven infrastructure management
Document Intelligence Hub : Process PDFs, Word docs, and spreadsheets with OCR and content extraction
DevOps Command Center : Automate Git operations, CI/CD pipelines, and deployment workflows
Data Analytics Engine : Transform CSV files, generate reports, and create visualizations on demand
Each of these represents a unique opportunity to bridge AI capabilities with real business needs — and share your solutions with the entire .NET community through NuGet.
To go further:
📘 Learn More : Explore the Model Context Protocol .NET samples
📺 Watch & Code : Tune in to the AI & .NET Community StandUp
🔧 Get Started : Check out the MCP documentation
.NET + MCP + NuGet = The future of extensible AI ✨
Happy building, and welcome to the growing community of MCP server creators!
📃 Resources
Get started with .NET AI and the Model Context Protocol
Model Context Protocol .NET samples
NuGet.org MCP Server Search
MCP Registry Documentation
What’s new in .NET 10
