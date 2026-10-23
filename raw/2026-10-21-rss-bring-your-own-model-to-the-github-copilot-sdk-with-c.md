---
source: "https://devblogs.microsoft.com/dotnet/bring-your-own-model-to-the-github-copilot-sdk-with-csharp"
title: "Bring Your Own Model to the GitHub Copilot SDK with C#"
author: "Bruno Capuano"
date_published: "2026-10-19"
date_clipped: "2026-10-21"
category: ".NET Ecosystem"
source_type: "rss"
---

# Bring Your Own Model to the GitHub Copilot SDK with C#

Hi,

I know, I keep coming back to the same theme on this blog: **agent harnesses**. In [Build Your Own AI Agent Harness in C#](https://devblogs.microsoft.com/dotnet/build-your-own-ai-agent-harness-in-csharp-the-maf-claw-live-series/) we built one from scratch. In [From dotnet run to Foundry Hosted Agent in 3 lines of C#](https://devblogs.microsoft.com/dotnet/from-dotnet-run-to-foundry-hosted-agent-in-3-lines-of-csharp/) we took an agent and hosted it. Today we use a harness we do not have to build at all: the one GitHub already ships, through the **GitHub Copilot SDK**.

One of the most popular questions we received during the **Let’s Learn GitHub Copilot SDK** sessions was:

> “Can I use the Copilot SDK with my own model deployment?”

The short answer is **yes**.

The longer answer is, the GitHub Copilot SDK gives your application the Copilot agent runtime, while `ProviderConfig` lets you route model inference to a provider you control. That provider can be any of the [providers officially supported by the Copilot SDK](https://docs.github.com/en/copilot/how-tos/copilot-sdk/auth/byok): OpenAI, Anthropic, Ollama, Microsoft Foundry Local, or any OpenAI-compatible endpoint such as vLLM or LiteLLM. Today’s sample uses **Microsoft Foundry**, authenticated with Microsoft Entra ID or, when needed, an API key.

The complete sample is now part of [Generative AI for Beginners .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet/tree/main/samples/CoreSamples/GitHubCopilotSDK-01-BYOK). It is a small .NET 10 console application: read configuration, create a BYOK provider, start the Copilot runtime, create one session, and ask one question.

[Get the complete BYOK C# sample](https://github.com/microsoft/Generative-AI-for-beginners-dotnet/tree/main/samples/CoreSamples/GitHubCopilotSDK-01-BYOK)

## What BYOK means in this sample

BYOK means **Bring Your Own Key**, but in this context the important idea is broader than the key itself: you bring your own model provider.

The Copilot SDK still supplies the runtime that manages the client, session, system message, and agent configuration. `ProviderConfig` changes the destination and authentication for model inference.

**BYOK is not customer-managed encryption keys**

In this article, BYOK means using your own model endpoint and credentials for inference. It does not refer to customer-managed encryption keys or a storage-encryption configuration.

The sample intentionally keeps the session minimal. It disables tools, skills, configuration discovery, and host Git operations so that the first run demonstrates one thing clearly: a Copilot SDK session can send a model request to your own Foundry-compatible deployment.

![Diagram of a .NET app routing Copilot SDK requests to Microsoft Foundry](https://devblogs.microsoft.com/dotnet/bring-your-own-model-to-the-github-copilot-sdk-with-csharp/github-copilot-sdk-byok-diagram.svg)

*The runtime and the model provider are separate parts of the application.*

## The project

The sample is a regular .NET 10 console application. These are the packages it uses:

```
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net10.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
    <UserSecretsId>genai-beginners-dotnet</UserSecretsId>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Azure.Identity" Version="1.21.0" />
    <PackageReference Include="GitHub.Copilot.SDK" Version="1.0.11" />
    <PackageReference Include="Microsoft.Extensions.Configuration" Version="10.0.3" />
    <PackageReference Include="Microsoft.Extensions.Configuration.UserSecrets" Version="10.0.3" />
  </ItemGroup>
</Project>
```

`GitHub.Copilot.SDK` provides the .NET client for the Copilot runtime. `Azure.Identity` provides `AzureCliCredential`, which lets the sample reuse the identity from `az login`. The configuration packages load development-only secrets without putting endpoints or credentials in source control.

## Step 1: read the model configuration

The sample uses the shared User Secrets values already used by the repository:

```
// User Secrets keeps the endpoint and credentials outside the repository.
var configuration = new ConfigurationBuilder()
    .AddUserSecrets<Program>(optional: true)
    .Build();

// This sample uses the repo's shared AzureOpenAI secrets.
var modelName = GetRequiredValue(configuration, "AzureOpenAI:Deployment");
var endpoint = GetRequiredValue(configuration, "AzureOpenAI:Endpoint");
var apiKey = configuration["AzureOpenAI:ApiKey"]?.Trim();
```

There are two required values:

- `AzureOpenAI:Deployment` is the name of your model deployment in Microsoft Foundry or Azure OpenAI. Choose a deployment that supports the Responses API, because this sample uses `WireApi = "responses"`.
- `AzureOpenAI:Endpoint` is the Foundry or Azure OpenAI resource endpoint.

`AzureOpenAI:ApiKey` is optional. If it is not present, the sample uses Microsoft Entra ID through `AzureCliCredential`. If it is present, the sample sends it in the `api-key` header.

## Step 2: configure the provider

This is the core of the sample:

```
// Microsoft Foundry exposes an API compatible with OpenAI Responses.
var provider = new ProviderConfig
{
    Type = "openai",
    BaseUrl = NormalizeEndpoint(endpoint),
    WireApi = "responses",
    ModelId = modelName,
    WireModel = modelName,
    MaxPromptTokens = 8000,
    MaxOutputTokens = 512
};
```

The configuration tells the Copilot runtime how to communicate with the provider:

- `Type = "openai"` selects the OpenAI-compatible provider shape.
- `BaseUrl` points to the OpenAI-compatible API surface.
- `WireApi = "responses"` selects the Responses API.
- `ModelId` identifies the model to the Copilot runtime.
- `WireModel` is the model name sent to the provider.
- The token limits keep this small example bounded.

For a reasoning model, `MaxOutputTokens` includes reasoning tokens as well as the visible answer. The 512-token limit can be reached before the model produces any answer. Increase or omit the `MaxOutputTokens` override when using a reasoning deployment, then tune the limit for your workload.

In this sample, `ModelId` and `WireModel` have the same value. They are separate properties because the runtime-facing model identifier and the provider-facing model name do not have to be identical in every integration.

The endpoint helper accepts either the resource URL or a URL that already includes `/openai/v1/`:

```
static string NormalizeEndpoint(string endpoint)
{
    var candidate = endpoint.Trim();
    if (!Uri.TryCreate(candidate, UriKind.Absolute, out var uri) ||
        uri.Scheme != Uri.UriSchemeHttps ||
        string.IsNullOrWhiteSpace(uri.Host))
    {
        throw new ArgumentException("The configured AzureOpenAI:Endpoint must be an HTTPS URL.");
    }

    // Accept the resource URL or a URL that already ends in /openai/v1.
    // Trimming first means a trailing slash does not need a separate check.
    var trimmed = candidate.TrimEnd('/');
    if (trimmed.EndsWith("/openai/v1", StringComparison.OrdinalIgnoreCase))
    {
        return trimmed + "/";
    }

    return $"{uri.GetLeftPart(UriPartial.Authority).TrimEnd('/')}/openai/v1/";
}
```

The helper also requires HTTPS. It is better to reject a malformed endpoint before creating a session than to discover it after the first model request.

## Step 3: use Entra ID by default

The default authentication path uses the Azure CLI login:

```
if (string.IsNullOrWhiteSpace(apiKey))
{
    // AzureCliCredential reuses the session created with `az login`.
    var credential = new AzureCliCredential();
    var scope = "https://cognitiveservices.azure.com/.default";
#pragma warning disable GHCP001 // BYOK auth callbacks are experimental in the Copilot SDK.
    provider.BearerTokenProvider = async _ =>
    {
        var token = await credential.GetTokenAsync(
            new TokenRequestContext([scope]),
            cancellation.Token);
        return token.Token;
    };
#pragma warning restore GHCP001
}
```

Before signing in, make sure your identity has the **Cognitive Services OpenAI User** role on the resource. Then run:

```
az login
```

`BearerTokenProvider` is a callback. The SDK can call it when it needs a token instead of receiving one token value that the application has to manage itself.

## Step 4: use an API key when one is configured

Some deployments or environments still require an API key. The sample supports that path without changing the rest of the provider configuration:

```
else
{
    provider.Headers = new Dictionary<string, string>
    {
        ["api-key"] = apiKey
    };
}
```

Set the optional secret:

```
dotnet user-secrets set "AzureOpenAI:ApiKey" "<your-api-key>"
```

When the value exists, the sample uses the `api-key` header and does not require `az login`. The console output reports only the authentication mode; it never prints the endpoint or the credential.

**Keep credentials out of source control**

Use User Secrets for local development, environment-managed configuration for deployed applications, and never paste an API key into the source file or a README.

## Step 5: start the Copilot runtime

The provider controls model inference, but the Copilot runtime is still required:

```
await using var client = new CopilotClient(new CopilotClientOptions
{
    Connection = RuntimeConnection.ForStdio("copilot"),
    WorkingDirectory = AppContext.BaseDirectory
});
await client.StartAsync(cancellation.Token);
```

This is an important distinction. BYOK does not mean “the Copilot SDK without Copilot.” The local Copilot CLI runtime still provides the orchestration process. BYOK changes where the model request goes.

**Prerequisites**

Install the .NET 10 SDK and the GitHub Copilot CLI, and make sure `dotnet --version` reports a .NET 10 SDK and `copilot --version` works. For the default Microsoft Entra ID authentication path, also install the Azure CLI and make sure `az --version` works. The API-key path does not require the Azure CLI. The sample starts the local Copilot runtime through `RuntimeConnection.ForStdio("copilot")`.

## Step 6: create a deliberately small session

The session configuration connects the model name and provider, then disables capabilities that are outside the scope of this first example:

```
// Disable tools, skills, and Git operations to isolate the model request.
await using var session = await client.CreateSessionAsync(new SessionConfig
{
    ClientName = "github-copilot-sdk-byok",
    Model = modelName,
    Provider = provider,
    SystemMessage = new SystemMessageConfig
    {
        Mode = SystemMessageMode.Replace,
        Content = "Answer every user question in English. Be concise and factual."
    },
    AvailableTools = [],
    Tools = [],
    EnableConfigDiscovery = false,
    EnableSkills = false,
    EnableHostGitOperations = false
}, cancellation.Token);
```

The empty tool collections and disabled features are intentional. They make the sample easier to reason about and safer to run while learning the provider configuration.

The system message also makes the output predictable for a multilingual live-learning sample. `SystemMessageMode.Replace` replaces the default system message instead of appending another instruction to it.

## Step 7: send one question

Finally, the application sends one prompt and waits for the final response:

```
var response = await session.SendAndWaitAsync(
    new MessageOptions { Prompt = question },
    TimeSpan.FromMinutes(3),
    cancellation.Token);

var content = response?.Data.Content;
if (string.IsNullOrWhiteSpace(content))
{
    throw new InvalidOperationException("The model returned an empty response.");
}

Console.WriteLine();
Console.WriteLine("Answer:");
Console.WriteLine(content);
```

The default question is:

```
What is Microsoft Foundry, and how does it relate to the GitHub Copilot SDK?
```

You can provide another question as command-line arguments:

```
dotnet run -- "Explain BYOK in one sentence."
```

## Run the sample

From the sample directory, configure the required values:

```
dotnet user-secrets set "AzureOpenAI:Endpoint" "https://<resource>.services.ai.azure.com"
dotnet user-secrets set "AzureOpenAI:Deployment" "<your-deployment-name>"
```

Then use the default Entra ID path:

```
az login
dotnet run
```

The output looks like this:

```
Model: <your-deployment-name>
Authentication: AzureCliCredential
Question: What is Microsoft Foundry, and how does it relate to the GitHub Copilot SDK?

Answer:
<model response>
```

The sample prints the selected model and authentication mode, but not the endpoint or credentials.

## So, what did we actually learn here?

Honestly, the part I like most is how little code this takes. 🙂

The Copilot SDK runtime and the model provider are two different things, and once that clicks, the rest is easy. You keep the runtime that GitHub gives you: the client, the session, the system message, and the agent plumbing. Then you just point inference somewhere else. That “somewhere else” is your Foundry deployment, your OpenAI key, your local Ollama, whatever you need.

Entra ID is the default path here, and I think it should be. No key to rotate, no key to leak, no key to accidentally commit. `az login` and you are done. The API key branch is there for the cases where you really need it, and it stays out of the way until you configure it.

And the session is deliberately boring. No tools, no skills, no MCP, no Git access. That is on purpose: the first run has exactly one job, which is proving that your model is answering. Once you see that answer in the console, you have a working baseline.

That is the fun part. From here you can start adding things one at a time: tools, MCP servers, skills, approvals, and streaming. When something breaks, you will know exactly which piece broke it.

Go try it with your own deployment. 🚀

## Learn more

- [GitHubCopilotSDK-01-BYOK sample](https://github.com/microsoft/Generative-AI-for-beginners-dotnet/tree/main/samples/CoreSamples/GitHubCopilotSDK-01-BYOK)
- [Generative AI for Beginners .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [GitHub Copilot SDK](https://github.com/github/copilot-sdk)
- [Let’s Learn .NET](https://aka.ms/letslearndotnet)
- [Let’s Learn .NET event page](https://dotnet.microsoft.com/live/lets-learn-dotnet)
- [Building Agentic AI Apps with GitHub Copilot SDK (Coursera Professional Certificate)](https://gh.io/coursera)
- [Microsoft Foundry](https://ai.azure.com)

[Explore the complete GitHub Copilot SDK sample](https://github.com/microsoft/Generative-AI-for-beginners-dotnet/tree/main/samples/CoreSamples/GitHubCopilotSDK-01-BYOK)

Happy coding!

Bruno
