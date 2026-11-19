---
source: "https://techcommunity.microsoft.com/blog/appsonazureblog/-net-11-is-now-generally-available-in-azure-functions/4571176"
title: ".NET 11 is now generally available in Azure Functions"
author: "nzthiago"
date_published: "2026-11-10"
date_clipped: "2026-11-16"
category: ".NET Ecosystem"
source_type: "rss"
discovered_via: "https://techcommunity.microsoft.com/t5/apps-on-azure-blog/net-11-is-now-generally-available-in-azure-functions/ba-p/4571176"
---

# .NET 11 is now generally available in Azure Functions

Today, we're announcing general availability of .NET 11 support in Azure Functions through the [isolated worker model](https://learn.microsoft.com/azure/azure-functions/dotnet-isolated-process-guide). You can build new serverless applications with .NET 11 or update your existing isolated worker apps to target the new release.

This release also introduces a required project SDK for .NET 11 function apps: [Azure.Functions.Sdk](https://www.nuget.org/packages/Azure.Functions.Sdk). Updated Azure Functions tooling templates use the new SDK, giving new projects a simpler project file while preserving the isolated worker programming model.

.NET 11 support in Azure Functions is currently available for C# apps. F# support is temporarily unavailable.

# A simpler project SDK

**Azure.Functions.Sdk** brings the Functions build integration into the project's SDK declaration. Instead of using *Microsoft.NET.Sdk* as the project SDK and adding *Microsoft.Azure.Functions.Worker.Sdk* as a package reference, use *Azure.Functions.Sdk* in the opening Project element and target net11.0.

Keep an explicit package reference to *Microsoft.Azure.Functions.Worker*, which provides the worker runtime, along with the trigger and binding extensions your application uses. Azure.Functions.Sdk replaces the build SDK package; it does not replace the worker runtime package.

The new SDK supplies the underlying .NET worker SDK, defaults AzureFunctionsVersion to v4, and includes the analyzers and source generators that prepare your functions for deployment. It also integrates with Azure Functions tooling so that dotnet run starts the Functions host when Azure Functions Core Tools is installed.

Using a custom container? .NET 11 Functions base images are published as chiseled images. Use  **mcr.microsoft.com/azure-functions/dotnet-isolated:4-dotnet-isolated11.0-chiseled** ; the *4-dotnet-isolated11.0* and *4-dotnet-isolated11.0-appservice* tags aren’t published. Chiseled images don’t include a shell or SSH server. See [Maintaining custom containers](https://learn.microsoft.com/azure/azure-functions/container-concepts#maintaining-custom-containers).

# Get started with .NET 11

1. Install the .NET 11 SDK and update your Azure Functions development tools and templates. Use your preferred [local development experience](https://learn.microsoft.com/azure/azure-functions/functions-develop-local) to create a .NET 11 isolated worker project.

With the updated Azure Functions Core Tools, run:

```
func init --worker-runtime dotnet-isolated --target-framework net11.0
```

For .NET 11, use *Azure.Functions.Sdk* version 1.0.1 or later. We also recommend *Microsoft.Azure.Functions.Worker* version 2.50.0 or later. The versions in the project example below reflect the current template and may differ from these minimum and recommended versions. The generated project file looks like this:

```
<Project Sdk="Azure.Functions.Sdk/1.0.1">
  <PropertyGroup>
    <TargetFramework>net11.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.Azure.Functions.Worker"
      Version="2.52.0" />
    <PackageReference
      Include="Microsoft.Azure.Functions.Worker.OpenTelemetry"
      Version="1.2.0" />
    <PackageReference Include="OpenTelemetry.Extensions.Hosting"
      Version="1.15.3" />
    <PackageReference Include="Azure.Monitor.OpenTelemetry.Exporter"
      Version="1.7.0" />
    <PackageReference
      Include="Microsoft.Azure.Functions.Worker.Extensions.Http.AspNetCore"
      Version="2.1.1" />
  </ItemGroup>
</Project>
```

These package versions reflect the current template example, not minimum requirements for every app. The template includes OpenTelemetry and ASP.NET Core HTTP integration packages; retain or adjust your app's dependencies to match the features and telemetry configuration you use.

2. Check that the generated project uses Azure.Functions.Sdk and targets net11.0. Keep the template's Microsoft.Azure.Functions.Worker reference and add the binding extension packages your functions need.
3. Build and run locally, then deploy to a function app configured for the .NET 11 isolated worker stack. Follow the [deployment guidance](https://learn.microsoft.com/azure/azure-functions/dotnet-isolated-process-guide#deploy-to-azure-functions) and check the [supported versions](https://learn.microsoft.com/azure/azure-functions/dotnet-isolated-process-guide#supported-versions) for hosting restrictions.

.NET 11 is supported only in the isolated worker model, not the in-process model. Support for the in-process model ended on November 10, 2026. If your app still uses this model, follow the migration guide to move to isolated worker before adopting .NET 11.

Linux Consumption does not support .NET 10 or later; if you're moving an app from Linux Consumption, review the [migration guidance for Flex Consumption](https://learn.microsoft.com/azure/azure-functions/migration/migrate-plan-consumption-to-flex) before upgrading.

# Update an existing isolated worker app

For an app that already uses the isolated worker model, start by updating its dependencies and checking compatibility with .NET 11. Then update the project SDK and target framework, remove the Microsoft.Azure.Functions.Worker.Sdk package reference, and retain an explicit Microsoft.Azure.Functions.Worker reference.

You can remove OutputType and AzureFunctionsVersion because the new SDK sets them automatically. Remove FunctionsEnableWorkerIndexing if present; worker indexing is always enabled with the new SDK.

The build SDK migration itself doesn't require changes to Program.cs, function classes, or host.json when you're using a current worker package. Retargeting to .NET 11 is a separate framework upgrade: review dependency compatibility and test your application's triggers, bindings, and deployment before updating production. The [isolated worker guide](https://learn.microsoft.com/azure/azure-functions/dotnet-isolated-process-guide#migrate-to-azurefunctionssdk) walks through the project SDK changes.

If your app still uses the in-process model, follow the [migration guide](https://learn.microsoft.com/azure/azure-functions/migrate-dotnet-to-isolated-model) to move to isolated worker before adopting .NET 11. The isolated worker model gives you control over application startup, standard .NET dependency injection, and separation between your application's dependencies and the Functions host.

# Keep building with us

Thank you to everyone who has shared feedback and helped improve .NET on Azure Functions. Explore the [Azure Functions .NET worker samples](https://github.com/Azure/azure-functions-dotnet-worker/tree/main/samples) as you plan your next application, and share questions or feedback in [GitHub discussions](https://github.com/Azure/azure-functions-dotnet-worker/discussions). If you encounter a problem, [open an issue](https://github.com/Azure/azure-functions-dotnet-worker/issues) so we can investigate.
