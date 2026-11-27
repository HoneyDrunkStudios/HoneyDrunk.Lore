---
source: "https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/"
title: "DevFlow overview"
author: "davidortinau"
date_published: "unknown"
date_clipped: "2026-11-27"
category: ".NET Ecosystem"
source_type: "web"
discovered_via: "https://devblogs.microsoft.com/dotnet/announcing-dotnet-11/"
date_updated: "2026-09-29"
---

# DevFlow overview

DevFlow is a comprehensive testing, automation, and debugging toolkit for .NET MAUI applications. It provides an in-app HTTP agent for visual tree inspection and element interaction, a CLI with 50+ commands, a Blazor WebView CDP bridge, and an MCP server for AI agent integration.

Important

DevFlow is experimental and will change between releases.

## Architecture

DevFlow consists of three components that work together:

- **Agent**: In-app HTTP server that exposes the visual tree, element interactions, screenshots, and profiling. Runs inside the MAUI app process.
- **CLI**: Command-line interface (`maui devflow`) that communicates with the agent. Integrated into the .NET MAUI CLI.
- **Broker**: Lightweight background daemon that coordinates port assignment and agent discovery when multiple apps run simultaneously. See [Broker architecture](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/broker?view=net-maui-10.0).

## Get started

### Step 1: Install the NuGet packages

Add the DevFlow agent package to your .NET MAUI project. If your app uses Blazor Hybrid, also add the Blazor package:

```
<PackageReference Include="Microsoft.Maui.DevFlow.Agent" />
<PackageReference Include="Microsoft.Maui.DevFlow.Blazor" />  <!-- If using Blazor Hybrid -->
```

### Step 2: Register the agent in MauiProgram.cs

Register the DevFlow agent in your app's startup code:

```
using Microsoft.Maui.DevFlow.Agent;

public static MauiApp CreateMauiApp()
{
    var builder = MauiApp.CreateBuilder();
    builder.UseMauiApp<App>();

    #if DEBUG
    builder.AddMauiDevFlowAgent();
    #endif

    return builder.Build();
}
```

Note

Wrap the `AddMauiDevFlowAgent` call in `#if DEBUG` to ensure the agent isn't included in release builds.

### Step 3: Install the CLI tool

Install the DevFlow CLI as a global .NET tool:

```
dotnet tool install -g Microsoft.Maui.Cli --prerelease
```

### Step 4: Run your app and interact

With your app running, use the CLI to inspect and interact with it:

```
# View the visual tree
maui devflow MAUI tree

# Take a screenshot
maui devflow MAUI screenshot -o screenshot.png

# Tap an element
maui devflow agent interact tap --automationid "MyButton"

# Start MCP server for AI agents
maui devflow mcp
```

## Features

- [Visual tree inspection and screenshots](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/visual-tree-screenshots?view=net-maui-10.0) — query the visual tree and capture PNG screenshots
- [Element interaction and automation](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/element-interaction?view=net-maui-10.0) — tap, fill, scroll, navigate, and mutate element properties
- [Blazor WebView debugging](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/blazor-cdp?view=net-maui-10.0) — Chrome DevTools Protocol bridge for Blazor Hybrid content
- [MCP server for AI agents](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/mcp-server?view=net-maui-10.0) — 15 tool categories for AI agent integration
- [Network monitoring and profiling](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/network-profiling?view=net-maui-10.0) — HTTP interception, CPU/memory/GC profiling, jank detection
- [File storage access](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/storage?view=net-maui-10.0) — discover file storage roots and manage sandboxed app files remotely
- [Broker architecture](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/broker?view=net-maui-10.0) — multi-app port assignment and agent discovery

## Packages

| Package | Description |
| --- | --- |
| `Microsoft.Maui.DevFlow.Agent` | In-app agent for .NET MAUI apps. Exposes visual tree, element interactions, screenshots, and profiling via HTTP/JSON API. |
| `Microsoft.Maui.DevFlow.Agent.Core` | Platform-agnostic core: HTTP server, visual tree walker, CSS selector engine, network capture, profiling. |
| `Microsoft.Maui.DevFlow.Agent.Gtk` | GTK/Linux agent for apps using the current Linux GTK4 backend. |
| `Microsoft.Maui.DevFlow.Blazor` | Blazor WebView CDP bridge. Enables Chrome DevTools Protocol access for Blazor Hybrid content. |
| `Microsoft.Maui.DevFlow.Blazor.Gtk` | Blazor CDP bridge for WebKitGTK on Linux. |
| `Microsoft.Maui.DevFlow.Driver` | Platform-aware app driver for iOS, Android, Mac Catalyst, Windows, and Linux. |
| `Microsoft.Maui.DevFlow.Logging` | Buffered rotating JSONL file logger. No MAUI dependency. |

For GTK/Linux apps, use `Microsoft.Maui.DevFlow.Agent.Gtk` with the current `Microsoft.Maui.Platforms.Linux.Gtk4` backend. See the [Linux GTK4 backend guide](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/platform-backends/linux-gtk4?view=net-maui-10.0) for package setup and automatic agent startup. Don't mix it with the superseded `Platform.Maui.Linux.Gtk4*` backend packages.

## Platform support

| Platform | Agent status | Notes |
| --- | --- | --- |
| Mac Catalyst | ✅ Supported | Direct localhost connectivity |
| iOS Simulator | ✅ Supported | Shares host network |
| Linux/GTK | ✅ Supported | Direct localhost connectivity |
| Android | 🔄 In progress | Requires `adb reverse` for port forwarding |
| Windows | 🔄 In progress | — |

## Platform setup

- [Android setup](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/setup-android?view=net-maui-10.0)
- [Apple platforms setup](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/setup-apple?view=net-maui-10.0)
- [Windows setup](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/devflow/setup-windows?view=net-maui-10.0)
- [Linux GTK4 backend and DevFlow setup](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/platform-backends/linux-gtk4?view=net-maui-10.0)

## See also

- [.NET MAUI CLI overview](https://learn.microsoft.com/en-us/dotnet/maui/developer-tools/cli/?view=net-maui-10.0)
