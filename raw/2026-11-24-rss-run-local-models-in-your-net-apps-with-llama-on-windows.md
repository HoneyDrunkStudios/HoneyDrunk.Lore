---
source: "https://devblogs.microsoft.com/dotnet/local-models-dotnet-llama-windows/"
title: "Run local models in your .NET apps with Llama on Windows"
author: "Luis Quintanilla"
date_published: "2026-11-23"
date_clipped: "2026-11-24"
category: ".NET Ecosystem"
source_type: "rss"
---

# Run local models in your .NET apps with Llama on Windows

Source: https://devblogs.microsoft.com/dotnet/local-models-dotnet-llama-windows/

Running AI models locally lets you keep your prompts and responses on your PC, work offline after downloading a model, and experiment without paying per request. Getting started can take some setup: finding a model that fits your hardware, downloading it, and running a server your apps can call.

Llama on Windows takes care of that for you. It’s a tray app that helps you find, download, and chat with open models on your PC. Once a model is running, your .NET apps can use it too.

In this post, you’ll install Llama, download a model, and call it from a .NET 11 C# file-based app.

You can find the complete code in the [Llama on Windows .NET sample repository](https://github.com/luisquintanilla/llama-windows-dotnet).

## What is Llama on Windows?

Llama is a Windows 11 app that lives in your system tray. It’s built with .NET 10 and WinUI 3, it’s powered by llama.cpp, and it’s brought to you by the Hugging Face and llama.cpp teams. From the tray, you can:

- Browse models recommended for your hardware and download them in one click.
- Search the Hugging Face Hub for thousands of other models.
- Chat with a model in the browser, or press `Alt+Space` from any app to open a chat overlay.

![Llama tray flyout showing Gemma 4 running locally and other model families available to browse](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/llama-windows-tray.webp)

Under the hood, Llama manages a llama.cpp server for you. Models run on your PC and are stored in the standard Hugging Face cache, so other tools like the `llama` command line can use them too.

Llama is open source and free to download at [llama.app](https://llama.app/). You can find the source code in the [Llama-Windows repository on GitHub](https://github.com/ggml-org/Llama-Windows).

## Install Llama

Llama is available in the [Microsoft Store](https://apps.microsoft.com/detail/9PPPSM6Q21Q6), which means you can install it with winget from a terminal:

```
winget install 9PPPSM6Q21Q6 --source msstore
```

You can also get Llama from [llama.app](https://llama.app/).

Once it’s installed, open **Llama** from the Start menu. The Llama icon appears in your system tray.

## Download a model and start chatting

1. Select the Llama icon in the system tray.
2. Pick a model family from the catalog, then choose a size and version that fit your PC. Llama shows a hardware-fit indicator next to each version. For this walkthrough, I’m using **Gemma 4**, **E4B**, **Balanced (Q4\_0)**.
3. Select the download arrow. The download can be several GB, depending on the model you choose.

![Gemma 4 model page showing E4B selected and the Q8_0 and Q4_0 download options](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/llama-windows-model-download.webp)

When the download completes, select the model to see its details. Choose a context length, using the memory-fit indicators as a guide, then select **Chat with model**.

![Downloaded Gemma 4 showing context-length choices and the Chat with model action](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/llama-windows-model-details.webp)

Try asking a question in the browser chat. For example, ask for ideas for a small .NET app you could build with a local model.

![Llama browser chat with Gemma 4 suggesting a local CLI chat, a document summarizer, and a code explainer](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/llama-windows-local-chat.webp)

That’s it! You’re chatting with a model running on your PC.

Llama loads models when you use them and unloads them after they’ve been idle for five minutes, so you don’t have to manage memory yourself. You can change the idle timeout in Llama’s settings.

## Use Llama from your .NET apps

Chatting in the tray is a great way to try out models. When you’re ready to build something with them, you can call the same models from your code.

Llama runs a llama.cpp server on `http://localhost:9931`. The server provides endpoints that follow the OpenAI API format, such as `/v1/chat/completions` and `/v1/models`. That means you can use the OpenAI client libraries you already know. Your requests go to the server running on your machine, not to OpenAI, and you don’t need an API key.

In .NET, you can use the [OpenAI](https://www.nuget.org/packages/OpenAI) library together with [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai) to work with Llama through `IChatClient`. This shared interface lets you build chat, streaming, and tool calling into your app without coupling that code to a specific model provider.

### What you’ll need

- [Llama](https://llama.app/), running, with at least one model downloaded
- [.NET 11 SDK](https://dotnet.microsoft.com/download/dotnet/11.0)

You can install the .NET 11 SDK with winget as well:

```
winget install Microsoft.DotNet.SDK.11
```

### Create the app

The [sample repository](https://github.com/luisquintanilla/llama-windows-dotnet) includes the complete app. With file-based apps, you don’t need a project file. Create a file called *llama-chat.cs* and add the following code:

```
#!/usr/bin/env dotnet
#:package Microsoft.Extensions.AI@11.0.0
#:package Microsoft.Extensions.AI.OpenAI@11.0.0

using System.ClientModel;
using System.ComponentModel;
using System.Runtime.InteropServices;
using System.Text.Json;
using Microsoft.Extensions.AI;
using OpenAI;

// Llama serves an OpenAI-compatible API on localhost. Set LLAMA_ENDPOINT if you changed the port.
var endpoint = Environment.GetEnvironmentVariable("LLAMA_ENDPOINT") ?? "http://localhost:9931/v1";
using var http = new HttpClient();

// Ask Llama which models it can serve. This also tells us whether it's running.
List<string> models;
try
{
    models = [.. (await GetLlamaModelsAsync()).Select(m => m.GetProperty("id").GetString()!)];
}
catch (HttpRequestException)
{
    Console.WriteLine($"Couldn't reach Llama at {endpoint}. Open Llama from the Start menu and try again.");
    return 1;
}

if (models.Count == 0)
{
    Console.WriteLine("Llama doesn't have any models yet. Open Llama from the system tray and download a model.");
    return 1;
}

Console.WriteLine("Models available in Llama:");
models.ForEach(m => Console.WriteLine($"  {m}"));

// Use the model passed as an argument, or the first one Llama reports.
var model = args.Length > 0 ? args[0] : models[0];
Console.WriteLine($"\nChatting with {model}. Press Enter on an empty line to exit.");

// No API key is required by default, but the OpenAI client expects a value.
IChatClient client = new OpenAIClient(new ApiKeyCredential("no-key-required"), new OpenAIClientOptions { Endpoint = new Uri(endpoint) })
    .GetChatClient(model)
    .AsIChatClient()
    .AsBuilder()
    .UseFunctionInvocation()
    .Build();

var options = new ChatOptions
{
    Tools = [AIFunctionFactory.Create(GetMachineInfo), AIFunctionFactory.Create(ListModels)]
};

List<ChatMessage> history = [new(ChatRole.System, "You are a helpful assistant running locally on the user's PC. Keep answers short.")];

while (true)
{
    Console.Write("\nYou: ");
    var prompt = Console.ReadLine();
    if (string.IsNullOrWhiteSpace(prompt))
    {
        break;
    }

    history.Add(new(ChatRole.User, prompt));

    Console.Write("Llama: ");
    List<ChatResponseUpdate> updates = [];
    await foreach (var update in client.GetStreamingResponseAsync(history, options))
    {
        Console.Write(update.Text);
        updates.Add(update);
    }
    Console.WriteLine();

    history.AddMessages(updates);
}

return 0;

// Calls GET /v1/models. Llama adds details such as load status to the standard OpenAI response.
async Task<List<JsonElement>> GetLlamaModelsAsync()
{
    using var json = JsonDocument.Parse(await http.GetStringAsync($"{endpoint}/models"));
    return [.. json.RootElement.GetProperty("data").EnumerateArray().Select(m => m.Clone())];
}

[Description("Lists the models downloaded in Llama on this PC, whether each one is loaded in memory, and which one the user is chatting with.")]
async Task<string> ListModels()
{
    var lines = (await GetLlamaModelsAsync()).Select(m =>
    {
        var id = m.GetProperty("id").GetString();
        var status = m.TryGetProperty("status", out var s) ? s.GetProperty("value").GetString() : "unknown";
        return $"{id} ({status}){(id == model ? ", current chat" : "")}";
    });
    return string.Join(Environment.NewLine, lines);
}

[Description("Gets the name, operating system, processor count, and .NET version of the computer the user is chatting from.")]
static string GetMachineInfo() =>
    $"{Environment.MachineName}, {RuntimeInformation.OSDescription}, {Environment.ProcessorCount} logical processors, .NET {Environment.Version}";
```

### Run the app

Make sure Llama is running, then run the app:

```
dotnet run llama-chat.cs
```

The app lists the models Llama has and starts a chat with the first one. To pick a different model, pass its ID as an argument. You can copy a model’s ID from its details in the Llama tray.

```
dotnet run llama-chat.cs -- ggml-org/gemma-4-E4B-it-GGUF:Q4_0
```

You don’t need to load the model first. Llama loads it on the first request, so that first response might take a little longer.

The app gives the model two tools: `GetMachineInfo` and `ListModels`. It can call these tools to answer questions about your computer and downloaded models, or answer general questions without a tool. Here’s an excerpt from my run, with the computer name replaced by `MYPC`:

```
You: Which models do I have, and which one am I talking to? Use your tool.
Llama: You have the following model: `ggml-org/gemma-4-E4B-it-GGUF:Q4_0`.

You are currently chatting with **gemma-4-E4B-it**.

You: What computer am I on? Use your tool.
Llama: You are on a **MYPC** running **Microsoft Windows 10.0.26200** with **16 logical processors** and **.NET 11.0.0**.

You: Why is the sky blue?
Llama: The sky appears blue due to a phenomenon called **Rayleigh scattering**.
```

Tool calling depends on the model you choose. If a model ignores the tools, try a larger model or one that lists tool support on its Hugging Face model card.

### How it works

Let’s walk through the main parts of the app.

**Find the models.** The app calls `GET /v1/models` to list the models Llama can serve. If the request fails, the app asks you to check that Llama is running. Llama adds a few details to the standard response, such as whether each model is loaded in memory.

**Create the chat client.** The app creates an `OpenAIClient` that points at Llama’s endpoint instead of OpenAI. `AsIChatClient()` turns it into an `IChatClient`, and `UseFunctionInvocation()` adds automatic tool calling.

**Add tools.** `AIFunctionFactory.Create` turns `GetMachineInfo` and `ListModels` into tools the model can call, and uses each method’s `Description` attribute to tell the model what the tool does. When the model asks to call a tool, `Microsoft.Extensions.AI` runs the method and sends the result back to the model for you. Both tools run on your PC, so the model can answer questions about your machine without anything leaving it.

**Chat.** `GetStreamingResponseAsync` streams the response so you see text as the model generates it. The app adds each response to the chat history so the model remembers the conversation.

Because the chat loop only depends on `IChatClient`, it stays the same if you use a different model or provider later.

## Watch the announcement

Watch the announcement of Llama on Windows in the .NET Conf 2026 keynote.

Run local models in your .NET apps with Llama on Windows

## Next steps

We’re excited to see what you build with local models and .NET. Here’s where to go next:

- Install [Llama](https://llama.app/) and download your first model.
- [Try the .NET sample](https://github.com/luisquintanilla/llama-windows-dotnet): run `dotnet run llama-chat.cs` to chat with your local model and try the tools.
- Read the [Llama API documentation](https://llama.app/docs/api) to learn about other endpoints, such as embeddings and structured output.
- Explore the [Microsoft.Extensions.AI documentation](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai) to learn more about `IChatClient`.
- Take it further by combining Llama with cloud models using [Routing and Failover for Microsoft.Extensions.AI](https://devblogs.microsoft.com/dotnet/routing-and-failover-for-microsoft-extensions-ai/).

Thanks to the Hugging Face and llama.cpp teams for building Llama on Windows. For issues or feature requests for Llama itself, open an issue in the [Llama-Windows repository](https://github.com/ggml-org/Llama-Windows/issues). Share what you’re building with local models and .NET in the comments below.
