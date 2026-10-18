---
source: "https://devblogs.microsoft.com/aspire/building-distributed-multi-agent-systems-with-aspire-and-microsoft-agent-framework"
title: "Distributed multi-agent systems with Aspire and Microsoft Agent Framework"
author: "Tommaso Stocchi"
date_published: "2026-06-09"
date_clipped: "2026-10-18"
category: ".NET Ecosystem"
source_type: "rss"
---

# Distributed multi-agent systems with Aspire and Microsoft Agent Framework

Agentic applications stop being simple very quickly. A useful assistant rarely stays as one model call. It needs tools, live data, specialized agents, orchestration, memory, voice or chat entry points, deployment infrastructure, health checks, and observability.

That is the story behind the [AlpineAI ski resort demo](https://github.com/tommasodotNET/ski-resort-demo). It is a distributed, multi-agent application built with **Microsoft Agent Framework (MAF)**, **Microsoft Foundry**, **A2A**, **Voice Live**, and **Aspire**. The scenario is intentionally realistic: a ski resort concierge that can answer guest questions, reason over live resort telemetry, route requests to specialist agents, search the web for general ski knowledge, and support both chat and voice experiences.

The important part is not that the demo is about skiing. The important part is how Aspire turns a complex multi-agent system into one application graph you can run, observe, and publish.

Before getting into the full demo, it helps to separate the Foundry concepts Aspire is modeling using the [Aspire.Hosting.Foundry integration](https://aspire.dev/integrations/cloud/azure/azure-ai-foundry/azure-ai-foundry-host/).

## Start with Foundry in Aspire

Microsoft Foundry gives agentic apps managed AI infrastructure: projects, model deployments, tools, prompt agents, hosted agents, and realtime capabilities. Aspire lets you describe those pieces in the same AppHost that describes the rest of your application.

### Foundry accounts, projects, and model deployments

A Foundry account is the top-level Microsoft Foundry resource. A Foundry project is the workspace inside it where model deployments, tools, and agents live:

**C# AppHost**

```
var foundry = builder.AddFoundry("ai");
var project = foundry.AddProject("project");

var chat = project.AddModelDeployment("chat", FoundryModel.OpenAI.Gpt41);
var realtime = project.AddModelDeployment("realtime", FoundryModel.OpenAI.GptRealtime);
```

**TypeScript AppHost**

```
const foundry = await builder.addFoundry('ai');
const project = await foundry.addProject('project');

const chat = await foundry.addDeployment('chat', FoundryModels.OpenAI.Gpt41);
const realtime = await foundry.addDeployment('realtime', FoundryModels.OpenAI.GptRealtime);
```

Both versions describe the same shape: a Foundry project plus two model deployments, one for normal chat and one for realtime voice.

### Prompt agents

A prompt agent is useful when the agent does not need custom application code. You define its instructions, model deployment, and tools, and Foundry hosts the agent behavior.

In Aspire, that can be part of the AppHost:

**C# AppHost**

```
var webSearch = project.AddWebSearchTool("websearch");

var researchAgent = project.AddPromptAgent("researcher", chat,
    instructions: """
        Answer product questions. Use web search when current information is needed.
        """)
    .WithTool(webSearch);
```

**TypeScript AppHost**

```
const webSearch = await project.addWebSearchTool('websearch');

const researchAgent = await project.addPromptAgent(chat, 'researcher', {
    instructions: 'Answer product questions. Use web search when current information is needed.',
}).withTool(webSearch);
```

Both snippets create a Foundry prompt agent backed by the chat deployment and give it a Foundry-managed web search tool. There is no separate web service to write for this agent.

### Hosted agents

A hosted agent is different. It is still your application code, but it is exposed through Foundry as an agent endpoint. That is useful when the agent needs custom orchestration, domain logic, framework integrations, or calls to other services.

In Aspire, the app is still modeled like any other project, with normal references to the resources it needs. The hosting choice is one line in the AppHost:

**C# AppHost**

```
var supportAgent = builder.AddProject<Projects.SupportAgent>("supportagent")
    .WithReference(chat).WaitFor(chat)
    .AsHostedAgent(project);
```

**TypeScript AppHost**

```
const supportAgent = await builder.addPythonApp('supportagent', './support-agent', 'support_agent/main.py')
    .withReference(chat).waitFor(chat)
    .asHostedAgent(project);
```

If the hosted agent needs databases, APIs, queues, or other agents, it can still use normal Aspire `WithReference(...)` calls. The sample stays small here because the important part is the hosting shape: this app is custom code, and Foundry can invoke it as an agent.

The agent app then exposes the Foundry Responses endpoint. In C#, that is the hosting layer around an `AIAgent`:

```
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();
```

That is the basic split: prompt agents are configured and hosted by Foundry; hosted agents are custom apps that Foundry can invoke as agents. Aspire keeps both in the same application graph.

## The demo: one resort, many agents

AlpineAI has a real frontend, live synthetic resort data, multiple specialist agents, and two advisor experiences:

```
Frontend dashboard
  ├─ Chat -> Advisor Agent (.NET, Foundry hosted Responses)
  ├─ Voice -> Voice Advisor Agent (.NET, Voice Live WebSocket)
  └─ Live panels -> Data Generator (Go)

Advisor agents
  ├─ Weather Agent (Python, A2A)
  ├─ Lift Traffic Agent (.NET, A2A)
  ├─ Safety Agent (Python, A2A)
  ├─ Ski Coach Agent (Python, A2A)
  └─ Ski Researcher (Microsoft Foundry prompt agent + web search)
```

Each specialist has a narrow responsibility. The weather agent handles current conditions and forecasts. The lift traffic agent handles lift status and wait times. The safety agent handles risk, closures, and slope safety. The ski coach agent turns preferences and skill level into recommendations. The ski researcher is a Foundry prompt agent with web search for general skiing questions.

With those primitives in place, the larger demo is easier to read. The Aspire AppHost is where the distributed system becomes explicit. It declares Microsoft Foundry, model deployments, the prompt agent, Cosmos DB, Go and Python apps, .NET projects, the frontend, Azure Container Apps placement, and every service reference between them.

### Two advisor entry points

AlpineAI has two user-facing advisor agents.

The **advisor agent** is the chat orchestrator. It is custom .NET code published as a Foundry hosted agent, so clients can invoke it through the Foundry Responses surface. It receives the user request, decides which specialists are relevant, invokes only those agents, and synthesizes the answer. For example, “I’m intermediate, I dislike crowds, and wind is strong. Where should I ski?” needs weather, lift traffic, safety, and ski coaching. “What is carving?” should go to the web-backed ski researcher instead.

The **voice advisor agent** is a custom-code agent too, but it is not published as a hosted agent. It is a .NET WebSocket service that connects browser audio to Azure AI Voice Live, uses the realtime model deployment, stores conversation state, and exposes the same specialist network to the voice experience.

### Specialist agents are normal services

The other agents are application code. They need dependencies, endpoints, telemetry, and access to the data generator. Aspire models them as regular resources deployed to Azure Container Apps.

The data generator is a Go app. It produces changing resort telemetry for weather, lifts, slopes, and safety signals:

```
var dataGenerator = builder.AddGolangApp("datagenerator", "./data-generator")
    .WithGoModTidy()
    .WithHttpEndpoint(env: "PORT")
    .WithHttpHealthCheck("/health")
    .WithComputeEnvironment(aca);
```

The Python weather, safety, and ski coach agents are also Uvicorn apps. Each one references the model deployment and the data generator:

```
var weatherAgent = builder.AddUvicornApp("weatheragent", "./weather-agent-python", "weather_agent_python.main:app")
    .WithUv()
    .WithHttpHealthCheck("/health")
    .WithReference(deployment).WaitFor(deployment)
    .WithReference(dataGenerator).WaitFor(dataGenerator)
    .WithComputeEnvironment(aca);
```

The lift traffic agent is .NET, but it sits in the same graph:

```
var liftAgent = builder.AddProject<Projects.LiftTrafficAgent_Dotnet>("lifttrafficagent")
    .WithReference(deployment).WaitFor(deployment)
    .WithReference(dataGenerator).WaitFor(dataGenerator)
    .WithComputeEnvironment(aca);
```

This is where Aspire matters. The AppHost is not just a launch script. It captures the operational truth of the system: which services exist, which runtime they use, which model they depend on, which data source they call, what telemetry they emit, and where they are deployed.

### Agents as tools

The specialist agents expose their capabilities over A2A. The advisor resolves them at startup and turns each remote agent into a tool with MAF:

```
static async Task<AIAgent> ResolveA2AAgentAsync(string serviceName)
{
    var baseUrl = Environment.GetEnvironmentVariable($"services__{serviceName}__https__0")
        ?? Environment.GetEnvironmentVariable($"services__{serviceName}__http__0")
        ?? throw new InvalidOperationException($"{serviceName} endpoint not configured.");

    var endpoint = new Uri(baseUrl);
    var httpClient = new HttpClient { BaseAddress = endpoint };
    var resolver = new A2ACardResolver(endpoint, httpClient);
    var agentCard = await resolver.GetAgentCardAsync();

    return agentCard.AsAIAgent(httpClient);
}
```

The Foundry prompt agent is also wrapped as an `AIAgent`, so the advisor can use it alongside the A2A specialists:

```
var skiResearcherAgentReference = new AgentReference(
    name: Environment.GetEnvironmentVariable("SKIRESEARCHER_AGENTNAME"));

var responseClient = foundryProjectClient.ProjectOpenAIClient
    .GetProjectResponsesClientForAgent(skiResearcherAgentReference);

var skiResearcherAgent = responseClient
    .AsIChatClient("gpt41")
    .AsAIAgent("ski-researcher", description: "Searches the web for skiing questions.");
```

Then the advisor becomes a single MAF agent with five tools:

```
var enableSensitiveTelemetry = bool.TryParse(
    Environment.GetEnvironmentVariable("ENABLE_SENSITIVE_TELEMETRY"),
    out var enabled) && enabled;

var agent = new AIProjectClient(new Uri(projectEndpoint), new DefaultAzureCredential())
    .GetProjectOpenAIClient()
    .GetProjectResponsesClient()
    .AsIChatClient(deploymentName)
    .AsBuilder()
    .ConfigureOptions(options => options.AllowMultipleToolCalls = true)
    .UseOpenTelemetry(
        sourceName: "Foundry.Agents",
        configure: cfg => cfg.EnableSensitiveData = enableSensitiveTelemetry)
    .Build()
    .AsAIAgent(
        name: "advisor-agent",
        instructions: "You are the Ski Resort Advisor.",
        tools:
        [
            weatherAgent.AsAIFunction(),
            liftAgent.AsAIFunction(),
            safetyAgent.AsAIFunction(),
            coachAgent.AsAIFunction(),
            skiResearcherAgent.AsAIFunction()
        ]);
```

This is the core pattern: **specialist agents become tools**. The advisor does not hard-code every data lookup. It delegates to agents that own their domains.

For building the hosted-agent apps themselves, use the official Microsoft Agent Framework hosted-agent Responses samples as the source of truth: [.NET](https://github.com/microsoft/agent-framework/tree/main/dotnet/samples/04-hosting/FoundryHostedAgents/responses) and [Python](https://github.com/microsoft/agent-framework/tree/main/python/samples/04-hosting/foundry-hosted-agents/responses).

### Publishing the orchestrator as a Foundry hosted agent

In AlpineAI, the advisor is not just another local API. Aspire publishes it as a Foundry hosted agent:

```
var advisorAgent = builder.AddProject<Projects.AdvisorAgent_Dotnet>("advisoragent")
    .WithHttpEndpoint(targetPort: 9000)
    .WithReference(deployment).WaitFor(deployment)
    .WithReference(weatherAgent).WaitFor(weatherAgent)
    .WithReference(liftAgent).WaitFor(liftAgent)
    .WithReference(safetyAgent).WaitFor(safetyAgent)
    .WithReference(coachAgent).WaitFor(coachAgent)
    .WithReference(skiResearcher).WaitFor(skiResearcher)
    .AsHostedAgent(project);
```

The relevant app code is the Foundry Responses endpoint:

```
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);

var app = builder.Build();
app.MapFoundryResponses();
app.Run();
```

That gives the advisor a Foundry Responses endpoint and lets Aspire add dashboard affordances for invoking it.

![Aspire dashboard showing the full AlpineAI distributed app graph](https://devblogs.microsoft.com/aspire/wp-content/uploads/sites/90/2026/06/foundry-agents-alpineai-aspire-resources-scaled.webp)

![Aspire dashboard Send Message invocation against the AlpineAI advisor agent](https://devblogs.microsoft.com/aspire/wp-content/uploads/sites/90/2026/06/foundry-agents-alpineai-advisor-send-message-scaled.webp)

### Chat and voice share the same agent network

The demo also includes a voice advisor. It is a .NET WebSocket service that connects browser audio to Azure AI Voice Live and gives Voice Live access to the same downstream tools:

```
var voiceAdvisorAgent = builder.AddProject<Projects.VoiceAdvisorAgent>("voiceadvisoragent")
    .WithReference(project).WaitFor(project)
    .WithReference(deployment).WaitFor(deployment)
    .WithReference(voiceDeployment).WaitFor(voiceDeployment)
    .WithReference(conversations).WaitFor(conversations)
    .WithReference(weatherAgent).WaitFor(weatherAgent)
    .WithReference(liftAgent).WaitFor(liftAgent)
    .WithReference(safetyAgent).WaitFor(safetyAgent)
    .WithReference(coachAgent).WaitFor(coachAgent)
    .WithReference(skiResearcher).WaitFor(skiResearcher)
    .WithComputeEnvironment(aca);
```

This is another place where Aspire earns its keep. The voice service needs the Foundry project, the chat model, the realtime model, Cosmos DB for conversation storage, and all downstream agents. Those dependencies are not hidden in setup scripts or copied between README files; they are represented in the AppHost.

The frontend is also part of the same graph:

```
builder.AddViteApp("frontend", "./frontend", "dev")
    .WithReference(advisorAgent).WaitFor(advisorAgent)
    .WithReference(voiceAdvisorAgent).WaitFor(voiceAdvisorAgent)
    .WithReference(dataGenerator).WaitFor(dataGenerator);
```

Now `aspire run` starts the frontend, data generator, chat advisor, voice advisor, specialist agents, Foundry resources, and Cosmos emulator as one system.

![AlpineAI frontend dashboard with live resort telemetry, chat, and voice advisor experiences](https://devblogs.microsoft.com/aspire/wp-content/uploads/sites/90/2026/06/foundry-agents-alpineai-frontend-dashboard-scaled.webp)

### Observability is part of the design

Distributed agents are hard to debug without traces. You need to know which agent was called, which tool ran, how long each step took, and where failures happened.

Aspire makes that much easier because it gives the app an OpenTelemetry endpoint and a dashboard to view the traces. Instead of guessing what happened inside a multi-agent request, you can follow the request path across the frontend, advisor processing, A2A calls to specialists, Foundry model calls, and downstream HTTP calls to the data generator.

![Aspire dashboard trace waterfall for a multi-agent AlpineAI request](https://devblogs.microsoft.com/aspire/wp-content/uploads/sites/90/2026/06/foundry-agents-alpineai-trace-waterfall-scaled.webp)

![Trace details showing advisor, specialist-agent tool-call, Foundry model, and downstream HTTP spans](https://devblogs.microsoft.com/aspire/wp-content/uploads/sites/90/2026/06/foundry-agents-alpineai-trace-details-scaled.webp)

## Why Aspire is the right abstraction

The AlpineAI demo is not one agent. It is a distributed application:

* Microsoft Foundry account, project, model deployments, and prompt agent.
* Go data generator.
* Python specialist agents.
* .NET specialist agent.
* .NET hosted Responses advisor.
* .NET voice WebSocket advisor.
* Cosmos DB conversation storage.
* React frontend.
* Azure Container Apps deployment environment.
* Health checks, service references, environment variables, ports, and telemetry.

Without Aspire, that becomes a pile of scripts, environment variables, Docker Compose files, deployment notes, and tribal knowledge. With Aspire, the graph is the source of truth. You can run the whole resort locally, see every resource in the dashboard, inspect logs and traces, invoke agents from the dashboard, and keep deployment configuration close to the code.

That is the bigger lesson: as agentic apps become distributed systems, they need distributed-systems tooling. Microsoft Agent Framework gives you the programming model for building agents and composing agents as tools. Microsoft Foundry gives you managed models, prompt agents, tools, hosted agents, and realtime capabilities. Aspire gives you the app model that ties everything together.

## The bottom line

Complex multi-agent systems should not be treated as demos glued together by environment variables. They should be modeled as applications.

AlpineAI shows what that looks like: specialist MAF agents, a Foundry prompt agent, a hosted advisor, a voice advisor, live data, a frontend, cloud resources, and traces all described through Aspire. The result is a system that is easier to run, easier to reason about, easier to observe, and closer to how real agentic applications need to be built.

## Useful links

* [AlpineAI ski-resort demo repository](https://github.com/tommasodotNET/ski-resort-demo)
