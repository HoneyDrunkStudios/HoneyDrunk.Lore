---
source: "https://learn.microsoft.com/en-us/dotnet/core/extensions/service-discovery"
title: "Service discovery in .NET"
author: "gewarren"
date_published: "unknown"
date_clipped: "2026-10-27"
category: ".NET Ecosystem"
source_type: "web"
---

# Service discovery in .NET

Source: https://learn.microsoft.com/en-us/dotnet/core/extensions/service-discovery

In this article, you learn how to use the `Microsoft.Extensions.ServiceDiscovery` library. Service discovery is a way for developers to use logical names instead of physical addresses (IP address and port) to refer to external services.

## Get started

To get started with service discovery in .NET, install the [Microsoft.Extensions.ServiceDiscovery](https://www.nuget.org/packages/Microsoft.Extensions.ServiceDiscovery) NuGet package.

- [.NET CLI](https://learn.microsoft.com/en-us/dotnet/core/extensions/service-discovery#tabpanel_1_dotnet-cli)
- [PackageReference](https://learn.microsoft.com/en-us/dotnet/core/extensions/service-discovery#tabpanel_1_package-reference)

```
dotnet add package Microsoft.Extensions.ServiceDiscovery
```

Or, if you're using .NET 10+ SDK:

```
dotnet package add Microsoft.Extensions.ServiceDiscovery
```

```
<PackageReference Include="Microsoft.Extensions.ServiceDiscovery" />
```

For more information, see [dotnet package add](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add) or [Manage package dependencies in .NET applications](https://learn.microsoft.com/en-us/dotnet/core/tools/dependencies).

## Example usage

In the *Program.cs* file of your project, call the [AddServiceDiscovery](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.servicediscoveryhttpclientbuilderextensions.addservicediscovery) extension method to add service discovery to the host, configuring default service endpoint resolvers:

```
builder.Services.AddServiceDiscovery();
```

Add service discovery to an individual [IHttpClientBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.ihttpclientbuilder) by calling the `AddServiceDiscovery` extension method:

```
builder.Services.AddHttpClient<CatalogServiceClient>(static client =>
    {
        client.BaseAddress = new("https://catalog");
    })
    .AddServiceDiscovery();
```

Alternatively, you can add service discovery to all [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient) instances by default:

```
builder.Services.ConfigureHttpClientDefaults(static http =>
{
    // Turn on service discovery by default
    http.AddServiceDiscovery();
});
```

## Scheme selection when resolving HTTP(S) endpoints

It is common to use HTTP while developing and testing a service locally and HTTPS when the service is deployed. Service Discovery supports this by allowing for a priority list of URI schemes to be specified in the input string given to Service Discovery. Service Discovery will attempt to resolve the services for the schemes in order and will stop after an endpoint is found. URI schemes are separated by a `+` character, for example: `"https+http://basket"`. Service Discovery will first try to find HTTPS endpoints for the `"basket"` service and will then fall back to HTTP endpoints. If any HTTPS endpoint is found, Service Discovery will not include HTTP endpoints.

Schemes can be filtered by configuring the `AllowedSchemes` and `AllowAllSchemes` properties on `ServiceDiscoveryOptions`. The `AllowAllSchemes` property is used to indicate that all schemes are allowed. By default, `AllowAllSchemes` is `true` and all schemes are allowed. Schemes can be restricted by setting `AllowAllSchemes` to `false` and adding allowed schemes to the `AllowedSchemes` property. For example, to allow only HTTPS:

```
services.Configure<ServiceDiscoveryOptions>(options =>
{
    options.AllowAllSchemes = false;
    options.AllowedSchemes = ["https"];
});
```

To explicitly allow all schemes, set the `ServiceDiscoveryOptions.AllowAllSchemes` property to `true`:

```
services.Configure<ServiceDiscoveryOptions>(
    options => options.AllowAllSchemes = true);
```

## Resolve service endpoints from configuration

The `AddServiceDiscovery` extension method adds a configuration-based endpoint resolver by default.
This resolver reads endpoints from the [.NET configuration system](https://learn.microsoft.com/en-us/dotnet/core/extensions/configuration). The library supports configuration through *appsettings.json*, environment variables, or any other [IConfiguration](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.configuration.iconfiguration) source.

Here's an example demonstrating how to configure endpoints for the service named *catalog* via `appsettings.json`:

```
{
  "Services": {
    "catalog": {
      "https": [
        "localhost:8080",
        "10.46.24.90:80"
      ]
    }
  }
}
```

The preceding example adds two endpoints for the service named *catalog*: `https://localhost:8080`, and `"https://10.46.24.90:80"`. Each time the *catalog* is resolved, one of these endpoints is selected.

If service discovery was added to the host using the [AddServiceDiscoveryCore](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.servicediscoveryservicecollectionextensions.addservicediscoverycore) extension method on [IServiceCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection), the configuration-based endpoint resolver can be added by calling the [AddConfigurationServiceEndpointProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.servicediscoveryservicecollectionextensions.addconfigurationserviceendpointprovider) extension method on `IServiceCollection`.

### Configuration

The configuration resolver is configured using the [ConfigurationServiceEndpointProviderOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.servicediscovery.configurationserviceendpointprovideroptions) class, which offers these configuration options:

- **SectionName**: The name of the configuration section that contains service endpoints. It defaults to `"Services"`.
- **ApplyHostNameMetadata**: A delegate used to determine if host name metadata should be applied to resolved endpoints. It defaults to a function that returns `false`.

To configure these options, you can call the [Configure](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.optionsservicecollectionextensions.configure) extension method on the `IServiceCollection` within your application's `Startup` class or `Program` file:

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.Configure<ConfigurationServiceEndpointProviderOptions>(
    static options =>
    {
        options.SectionName = "MyServiceEndpoints";

        // Configure the logic for applying host name metadata
        options.ApplyHostNameMetadata = static endpoint =>
        {
            // Your custom logic here. For example:
            return endpoint.EndPoint is DnsEndPoint dnsEp
                && dnsEp.Host.StartsWith("internal");
        };
    });
```

The preceding example demonstrates setting a custom section name for your service endpoints and providing custom conditional logic for applying host name metadata.

## Resolve service endpoints using platform-provided service discovery

Certain platforms, like Azure Container Apps and Kubernetes (when configured accordingly), offer service discovery capabilities without necessitating a service discovery client library. In cases where an application is deployed in such environments, using the platform's built-in functionality can be advantageous. The pass-through resolver is designed to facilitate this scenario. It enables the utilization of alternative resolvers, such as configuration, in different environments, such as a developer's machine. Importantly, this flexibility is achieved without the need for any code modifications or the implementation of conditional guards.

The pass-through resolver performs no external resolution and instead resolves endpoints by returning the input service name represented as a [DnsEndPoint](https://learn.microsoft.com/en-us/dotnet/api/system.net.dnsendpoint).

The pass-through provider is configured by-default when adding service discovery via the `AddServiceDiscovery` extension method.

If service discovery was added to the host using the `AddServiceDiscoveryCore` extension method on `IServiceCollection`, the pass-through provider can be added by calling the [AddPassThroughServiceEndpointProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.servicediscoveryservicecollectionextensions.addpassthroughserviceendpointprovider) extension method on `IServiceCollection`.

## See also

- [Service discovery in Aspire](https://aspire.dev/fundamentals/service-discovery/)
