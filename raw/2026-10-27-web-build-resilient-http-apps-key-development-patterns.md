---
source: "https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience"
title: "Build resilient HTTP apps: Key development patterns"
author: "gewarren"
date_published: "unknown"
date_clipped: "2026-10-27"
category: ".NET Ecosystem"
source_type: "web"
---

# Build resilient HTTP apps: Key development patterns

Source: https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience

Building robust HTTP apps that can recover from transient fault errors is a common requirement. This article assumes that you've already read [Introduction to resilient app development](https://learn.microsoft.com/en-us/dotnet/core/resilience/), as this article extends the core concepts conveyed. To help build resilient HTTP apps, the [Microsoft.Extensions.Http.Resilience](https://www.nuget.org/packages/Microsoft.Extensions.Http.Resilience) NuGet package provides resilience mechanisms specifically for the [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient). This NuGet package relies on the `Microsoft.Extensions.Resilience` library and *Polly*, which is a popular open-source project. For more information, see [Polly](https://github.com/App-vNext/Polly).

## Get started

To use resilience-patterns in HTTP apps, install the [Microsoft.Extensions.Http.Resilience](https://www.nuget.org/packages/Microsoft.Extensions.Http.Resilience) NuGet package.

- [.NET CLI](https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience#tabpanel_1_dotnet-cli)
- [PackageReference](https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience#tabpanel_1_package-reference)

```
dotnet add package Microsoft.Extensions.Http.Resilience
```

```
<PackageReference Include="Microsoft.Extensions.Http.Resilience" />
```

For more information, see [dotnet package add](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-package-add) or [Manage package dependencies in .NET applications](https://learn.microsoft.com/en-us/dotnet/core/tools/dependencies).

## Add resilience to an HTTP client

To add resilience to an [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient), you chain a call on the [IHttpClientBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.ihttpclientbuilder) type that is returned from calling any of the available [AddHttpClient](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.httpclientfactoryservicecollectionextensions.addhttpclient) methods. For more information, see [IHttpClientFactory with .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/httpclient-factory).

There are several resilience-centric extensions available. Some are standard, thus employing various industry best practices, and others are more customizable. When adding resilience, you should only add one resilience handler and avoid stacking handlers. If you need to add multiple resilience handlers, you should consider using the `AddResilienceHandler` extension method, which allows you to customize the resilience strategies.

Important

All examples within this article rely on the [AddHttpClient](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.httpclientfactoryservicecollectionextensions.addhttpclient) API, from the [Microsoft.Extensions.Http](https://www.nuget.org/packages/Microsoft.Extensions.Http) library, which returns an [IHttpClientBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.ihttpclientbuilder) instance. The [IHttpClientBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.ihttpclientbuilder) instance is used to configure the [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient) and add the resilience handler. If you need to add resilience to a `static` or *singleton* `HttpClient` without a DI container, see [Resilience with static clients](https://learn.microsoft.com/en-us/dotnet/fundamentals/networking/http/httpclient-guidelines#resilience-with-static-clients).

## Add standard resilience handler

The standard resilience handler uses multiple resilience strategies stacked atop one another, with default options to send the requests and handle any transient errors. The standard resilience handler is added by calling the `AddStandardResilienceHandler` extension method on an [IHttpClientBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.ihttpclientbuilder) instance.

```
var services = new ServiceCollection();

var httpClientBuilder = services.AddHttpClient<ExampleClient>(
    configureClient: static client =>
    {
        client.BaseAddress = new("https://jsonplaceholder.typicode.com");
    });
```

The preceding code:

- Creates a [ServiceCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.servicecollection) instance.
- Adds an [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient) for the `ExampleClient` type to the service container.
- Configures the [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient) to use `"https://jsonplaceholder.typicode.com"` as the base address.
- Creates the `httpClientBuilder` that's used throughout the other examples within this article.

A more real-world example would rely on hosting, such as that described in the [.NET Generic Host](https://learn.microsoft.com/en-us/dotnet/core/extensions/generic-host) article. Using the [Microsoft.Extensions.Hosting](https://www.nuget.org/packages/Microsoft.Extensions.Hosting) NuGet package, consider the following updated example:

```
using Http.Resilience.Example;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

HostApplicationBuilder builder = Host.CreateApplicationBuilder(args);

IHttpClientBuilder httpClientBuilder = builder.Services.AddHttpClient<ExampleClient>(
    configureClient: static client =>
    {
        client.BaseAddress = new("https://jsonplaceholder.typicode.com");
    });
```

The preceding code is similar to the manual `ServiceCollection` creation approach, but instead relies on the [Host.CreateApplicationBuilder()](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.host.createapplicationbuilder#microsoft-extensions-hosting-host-createapplicationbuilder) to build out a host that exposes the services.

The `ExampleClient` is defined as follows:

```
using System.Net.Http.Json;

namespace Http.Resilience.Example;

/// <summary>
/// An example client service, that relies on the <see cref="HttpClient"/> instance.
/// </summary>
/// <param name="client">The given <see cref="HttpClient"/> instance.</param>
internal sealed class ExampleClient(HttpClient client)
{
    /// <summary>
    /// Returns an <see cref="IAsyncEnumerable{T}"/> of <see cref="Comment"/>s.
    /// </summary>
    public IAsyncEnumerable<Comment?> GetCommentsAsync()
    {
        return client.GetFromJsonAsAsyncEnumerable<Comment>("/comments");
    }
}
```

The preceding code:

- Defines an `ExampleClient` type that has a constructor that accepts an [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient).
- Exposes a `GetCommentsAsync` method that sends a GET request to the `/comments` endpoint and returns the response.

The `Comment` type is defined as follows:

```
namespace Http.Resilience.Example;

public record class Comment(
    int PostId, int Id, string Name, string Email, string Body);
```

Given that you've created an [IHttpClientBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.ihttpclientbuilder) (`httpClientBuilder`), and you now understand the `ExampleClient` implementation and corresponding `Comment` model, consider the following example:

```
httpClientBuilder.AddStandardResilienceHandler();
```

The preceding code adds the standard resilience handler to the [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient). Like most resilience APIs, there are overloads that allow you to customize the default options and applied resilience strategies.

## Remove standard resilience handlers

There's a method [RemoveAllResilienceHandlers](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.resiliencehttpclientbuilderextensions.removeallresiliencehandlers) which removes all previously registered resilience handlers. It's useful when you need to clear existing resilience handlers to add your custom one.
The following example demonstrates how to configure a custom [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient) using the `AddHttpClient` method, remove all predefined resilience strategies, and replace them with new handlers.
This approach allows you to clear existing configurations and define new ones according to your specific requirements.

```
// By default, we want all HttpClient instances to include the StandardResilienceHandler.
services.ConfigureHttpClientDefaults(builder => builder.AddStandardResilienceHandler());
// For a named HttpClient "custom" we want to remove the StandardResilienceHandler and add the StandardHedgingHandler instead.
services.AddHttpClient("custom")
    .RemoveAllResilienceHandlers()
    .AddStandardHedgingHandler();
```

The preceding code:

- Creates a [ServiceCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.servicecollection) instance.
- Adds the standard resilience handler to all [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient) instances.
- For the "custom" [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient):
  - Removes all predefined resilience handlers that were previously registered. This is useful when you want to start with a clean state to add your own custom strategies.
  - Adds a `StandardHedgingHandler` to the [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient). You can replace `AddStandardHedgingHandler()` with any strategy that suits your application's needs, such as retry mechanisms, circuit breakers, or other resilience techniques.

### Standard resilience handler defaults

The default configuration chains five resilience strategies in the following order (from the outermost to the innermost):

| Order | Strategy | Description | Defaults |
| --- | --- | --- | --- |
| **1** | Rate limiter | The rate limiter pipeline limits the maximum number of concurrent requests being sent to the dependency. | Queue: `0` Permit: `1_000` |
| **2** | Total timeout | The total request timeout pipeline applies an overall timeout to the execution, ensuring that the request, including retry attempts, doesn't exceed the configured limit. | Total timeout: 30s |
| **3** | Retry | The retry pipeline retries the request in case the dependency is slow or returns a transient error. | Max retries: `3` Backoff: `Exponential` Use jitter: `true` Delay:2s |
| **4** | Circuit breaker | The circuit breaker blocks the execution if too many direct failures or timeouts are detected. | Failure ratio: 10% Min throughput: `100` Sampling duration: 30s Break duration: 5s |
| **5** | Attempt timeout | The attempt timeout pipeline limits each request attempt duration and throws if it's exceeded. | Attempt timeout: 10s |

#### Retries and circuit breakers

The retry and circuit breaker strategies both handle a set of specific HTTP status codes and exceptions. Consider the following HTTP status codes:

- HTTP 500 and above (Server errors)
- HTTP 408 (Request timeout)
- HTTP 429 (Too many requests)

Additionally, these strategies handle the following exceptions:

- `HttpRequestException`
- `TimeoutRejectedException`

#### Disable retries for a given list of HTTP methods

By default, the standard resilience handler is configured to make retries for all HTTP methods. For some applications, such behavior could be undesirable or even harmful. For example, if a POST request inserts a new record to a database, then making retries for such a request could lead to data duplication. If you need to disable retries for a given list of HTTP methods you can use the [DisableFor(HttpRetryStrategyOptions, HttpMethod[])](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.http.resilience.httpretrystrategyoptionsextensions.disablefor#microsoft-extensions-http-resilience-httpretrystrategyoptionsextensions-disablefor(microsoft-extensions-http-resilience-httpretrystrategyoptions-system-net-http-httpmethod())) method:

```
httpClientBuilder.AddStandardResilienceHandler(options =>
{
    options.Retry.DisableFor(HttpMethod.Post, HttpMethod.Delete);
});
```

Alternatively, you can use the [DisableForUnsafeHttpMethods(HttpRetryStrategyOptions)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.http.resilience.httpretrystrategyoptionsextensions.disableforunsafehttpmethods#microsoft-extensions-http-resilience-httpretrystrategyoptionsextensions-disableforunsafehttpmethods(microsoft-extensions-http-resilience-httpretrystrategyoptions)) method, which disables retries for `POST`, `PATCH`, `PUT`, `DELETE`, and `CONNECT` requests. According to [RFC](https://www.rfc-editor.org/rfc/rfc7231#section-4.2.1), these methods are considered unsafe; meaning their semantics aren't read-only:

```
httpClientBuilder.AddStandardResilienceHandler(options =>
{
    options.Retry.DisableForUnsafeHttpMethods();
});
```

## Add standard hedging handler

The standard hedging handler wraps the execution of the request with a standard hedging mechanism. Hedging retries slow requests in parallel.

To use the standard hedging handler, call `AddStandardHedgingHandler` extension method. The following example configures the `ExampleClient` to use the standard hedging handler.

```
httpClientBuilder.AddStandardHedgingHandler();
```

The preceding code adds the standard hedging handler to the [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient).

### Standard hedging handler defaults

The standard hedging uses a pool of circuit breakers to ensure that unhealthy endpoints aren't hedged against. By default, the selection from the pool is based on the URL authority (scheme + host + port).

Tip

It's recommended that you configure the way the strategies are selected by calling `StandardHedgingHandlerBuilderExtensions.SelectPipelineByAuthority` or `StandardHedgingHandlerBuilderExtensions.SelectPipelineBy` for more advanced scenarios.

The preceding code adds the standard hedging handler to the [IHttpClientBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.ihttpclientbuilder). The default configuration chains five resilience strategies in the following order (from the outermost to the innermost):

| Order | Strategy | Description | Defaults |
| --- | --- | --- | --- |
| **1** | Total request timeout | The total request timeout pipeline applies an overall timeout to the execution, ensuring that the request, including hedging attempts, doesn't exceed the configured limit. | Total timeout: 30s |
| **2** | Hedging | The hedging strategy executes the requests against multiple endpoints in case the dependency is slow or returns a transient error. Routing is options, by default it just hedges the URL provided by the original [HttpRequestMessage](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httprequestmessage). | Min attempts: `1` Max attempts: `10` Delay: 2s |
| **3** | Rate limiter (per endpoint) | The rate limiter pipeline limits the maximum number of concurrent requests being sent to the dependency. | Queue: `0` Permit: `1_000` |
| **4** | Circuit breaker (per endpoint) | The circuit breaker blocks the execution if too many direct failures or timeouts are detected. | Failure ratio: 10% Min throughput: `100` Sampling duration: 30s Break duration: 5s |
| **5** | Attempt timeout (per endpoint) | The attempt timeout pipeline limits each request attempt duration and throws if it's exceeded. | Timeout: 10s |

### Customize hedging handler route selection

When using the standard hedging handler, you can customize the way the request endpoints are selected by calling various extensions on the `IRoutingStrategyBuilder` type. This can be useful for scenarios such as A/B testing, where you want to route a percentage of the requests to a different endpoint:

```
httpClientBuilder.AddStandardHedgingHandler(static (IRoutingStrategyBuilder builder) =>
{
    // Hedging allows sending multiple concurrent requests
    builder.ConfigureOrderedGroups(static options =>
    {
        options.Groups.Add(new UriEndpointGroup()
        {
            Endpoints =
            {
                // Imagine a scenario where 3% of the requests are 
                // sent to the experimental endpoint.
                new() { Uri = new("https://example.net/api/experimental"), Weight = 3 },
                new() { Uri = new("https://example.net/api/stable"), Weight = 97 }
            }
        });
    });
});
```

The preceding code:

- Adds the hedging handler to the [IHttpClientBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.ihttpclientbuilder).
- Configures the `IRoutingStrategyBuilder` to use the `ConfigureOrderedGroups` method to configure the ordered groups.
- Adds an `EndpointGroup` to the `orderedGroup` that routes 3% of the requests to the `https://example.net/api/experimental` endpoint and 97% of the requests to the `https://example.net/api/stable` endpoint.
- Configures the `IRoutingStrategyBuilder` to use the `ConfigureWeightedGroups` method to configure the

To configure a weighted group, call the `ConfigureWeightedGroups` method on the `IRoutingStrategyBuilder` type. The following example configures the `IRoutingStrategyBuilder` to use the `ConfigureWeightedGroups` method to configure the weighted groups.

```
httpClientBuilder.AddStandardHedgingHandler(static (IRoutingStrategyBuilder builder) =>
{
    // Hedging allows sending multiple concurrent requests
    builder.ConfigureWeightedGroups(static options =>
    {
        options.SelectionMode = WeightedGroupSelectionMode.EveryAttempt;

        options.Groups.Add(new WeightedUriEndpointGroup()
        {
            Endpoints =
            {
                // Imagine A/B testing
                new() { Uri = new("https://example.net/api/a"), Weight = 33 },
                new() { Uri = new("https://example.net/api/b"), Weight = 33 },
                new() { Uri = new("https://example.net/api/c"), Weight = 33 }
            }
        });
    });
});
```

The preceding code:

- Adds the hedging handler to the [IHttpClientBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.ihttpclientbuilder).
- Configures the `IRoutingStrategyBuilder` to use the `ConfigureWeightedGroups` method to configure the weighted groups.
- Sets the `SelectionMode` to `WeightedGroupSelectionMode.EveryAttempt`.
- Adds a `WeightedEndpointGroup` to the `weightedGroup` that routes 33% of the requests to the `https://example.net/api/a` endpoint, 33% of the requests to the `https://example.net/api/b` endpoint, and 33% of the requests to the `https://example.net/api/c` endpoint.

Tip

The maximum number of hedging attempts directly correlates to the number of configured groups. For example, if you have two groups, the maximum number of attempts is two.

For more information, see [Polly docs: Hedging resilience strategy](https://www.pollydocs.org/strategies/hedging).

It's common to configure either an ordered group or weighted group, but it's valid to configure both. Using ordered and weighted groups is helpful in scenarios where you want to send a percentage of the requests to a different endpoint, such is the case with A/B testing.

## Add custom resilience handlers

To have more control, you can customize the resilience handlers by using the `AddResilienceHandler` API. This method accepts a delegate that configures the `ResiliencePipelineBuilder<HttpResponseMessage>` instance that is used to create the resilience strategies.

To configure a named resilience handler, call the `AddResilienceHandler` extension method with the name of the handler. The following example configures a named resilience handler called `"CustomPipeline"`.

```
httpClientBuilder.AddResilienceHandler(
    "CustomPipeline",
    static builder =>
{
    // See: https://www.pollydocs.org/strategies/retry.html
    builder.AddRetry(new HttpRetryStrategyOptions
    {
        // Customize and configure the retry logic.
        BackoffType = DelayBackoffType.Exponential,
        MaxRetryAttempts = 5,
        UseJitter = true
    });

    // See: https://www.pollydocs.org/strategies/circuit-breaker.html
    builder.AddCircuitBreaker(new HttpCircuitBreakerStrategyOptions
    {
        // Customize and configure the circuit breaker logic.
        SamplingDuration = TimeSpan.FromSeconds(10),
        FailureRatio = 0.2,
        MinimumThroughput = 3,
        ShouldHandle = static args =>
        {
            return ValueTask.FromResult(args is
            {
                Outcome.Result.StatusCode:
                    HttpStatusCode.RequestTimeout or
                        HttpStatusCode.TooManyRequests
            });
        }
    });

    // See: https://www.pollydocs.org/strategies/timeout.html
    builder.AddTimeout(TimeSpan.FromSeconds(5));
});
```

The preceding code:

- Adds a resilience handler with the name `"CustomPipeline"` as the `pipelineName` to the service container.
- Adds a retry strategy with exponential backoff, five retries, and jitter preference to the resilience builder.
- Adds a circuit breaker strategy with a sampling duration of 10 seconds, a failure ratio of 0.2 (20%), a minimum throughput of three, and a predicate that handles `RequestTimeout` and `TooManyRequests` HTTP status codes to the resilience builder.
- Adds a timeout strategy with a timeout of five seconds to the resilience builder.

There are many options available for each of the resilience strategies. For more information, see the [Polly docs: Strategies](https://www.pollydocs.org/strategies). For more information about configuring `ShouldHandle` delegates, see [Polly docs: Fault handling in reactive strategies](https://www.pollydocs.org/strategies#fault-handling).

Warning

If you're using both retry and timeout strategies, and you want to configure the `ShouldHandle` delegate in your retry strategy, make sure to consider whether it should handle Polly's timeout exception. Polly throws a `TimeoutRejectedException` (which inherits from [Exception](https://learn.microsoft.com/en-us/dotnet/api/system.exception)), not the standard [TimeoutException](https://learn.microsoft.com/en-us/dotnet/api/system.timeoutexception).

### Dynamic reload

Polly supports dynamic reloading of the configured resilience strategies. This means that you can change the configuration of the resilience strategies at runtime. To enable dynamic reload, use the appropriate `AddResilienceHandler` overload that exposes the `ResilienceHandlerContext`. Given the context, call `EnableReloads` of the corresponding resilience strategy options:

```
httpClientBuilder.AddResilienceHandler(
    "AdvancedPipeline",
    static (ResiliencePipelineBuilder<HttpResponseMessage> builder,
        ResilienceHandlerContext context) =>
    {
        // Enable reloads whenever the named options change
        context.EnableReloads<HttpRetryStrategyOptions>("RetryOptions");

        // Retrieve the named options
        var retryOptions =
            context.GetOptions<HttpRetryStrategyOptions>("RetryOptions");

        // Add retries using the resolved options
        builder.AddRetry(retryOptions);
    });
```

The preceding code:

- Adds a resilience handler with the name `"AdvancedPipeline"` as the `pipelineName` to the service container.
- Enables the reloads of the `"AdvancedPipeline"` pipeline whenever the named `RetryStrategyOptions` options change.
- Retrieves the named options from the [IOptionsMonitor<TOptions>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.options.ioptionsmonitor-1) service.
- Adds a retry strategy with the retrieved options to the resilience builder.

For more information, see [Polly docs: Advanced dependency injection](https://www.pollydocs.org/advanced/dependency-injection#dynamic-reloads).

This example relies on an options section that is capable of change, such as an *appsettings.json* file. Consider the following *appsettings.json* file:

```
{
    "RetryOptions": {
        "Retry": {
            "BackoffType": "Linear",
            "UseJitter": false,
            "MaxRetryAttempts": 7
        }
    }
}
```

Now imagine that these options were bound to the app's configuration, binding the `HttpRetryStrategyOptions` to the `"RetryOptions"` section:

```
var section = builder.Configuration.GetSection("RetryOptions");

builder.Services.Configure<HttpStandardResilienceOptions>(section);
```

For more information, see [Options pattern in .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/options).

## Example usage

Your app relies on [dependency injection](https://learn.microsoft.com/en-us/dotnet/core/extensions/dependency-injection/overview) to resolve the `ExampleClient` and its corresponding [HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient). The code builds the [IServiceProvider](https://learn.microsoft.com/en-us/dotnet/api/system.iserviceprovider) and resolves the `ExampleClient` from it.

```
IHost host = builder.Build();

ExampleClient client = host.Services.GetRequiredService<ExampleClient>();

await foreach (Comment? comment in client.GetCommentsAsync())
{
    Console.WriteLine(comment);
}
```

The preceding code:

- Builds the [IServiceProvider](https://learn.microsoft.com/en-us/dotnet/api/system.iserviceprovider) from the [ServiceCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.servicecollection).
- Resolves the `ExampleClient` from the [IServiceProvider](https://learn.microsoft.com/en-us/dotnet/api/system.iserviceprovider).
- Calls the `GetCommentsAsync` method on the `ExampleClient` to get the comments.
- Writes each comment to the console.

Imagine a situation where the network goes down or the server becomes unresponsive. The following diagram shows how the resilience strategies would handle the situation, given the `ExampleClient` and the `GetCommentsAsync` method:

[![Example HTTP GET work flow with resilience pipeline.](https://learn.microsoft.com/en-us/dotnet/core/resilience/media/http-get-comments-flow.png)](https://learn.microsoft.com/en-us/dotnet/core/resilience/media/http-get-comments-flow.png#lightbox)

The preceding diagram depicts:

- The `ExampleClient` sends an HTTP GET request to the `/comments` endpoint.
- The [HttpResponseMessage](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpresponsemessage) is evaluated:
  - If the response is successful (HTTP 200), the response is returned.
  - If the response is unsuccessful (HTTP non-200), the resilience pipeline employs the configured resilience strategies.

While this is a simple example, it demonstrates how the resilience strategies can be used to handle transient errors. For more information, see [Polly docs: Strategies](https://www.pollydocs.org/strategies).

## Known issues

The following sections detail various known issues.

### Compatibility with the `Grpc.Net.ClientFactory` package

If you're using `Grpc.Net.ClientFactory` version `2.63.0` or earlier, then enabling the standard resilience or hedging handlers for a gRPC client could cause a runtime exception. Specifically, consider the following code sample:

```
services
    .AddGrpcClient<Greeter.GreeterClient>()
    .AddStandardResilienceHandler();
```

The preceding code results in the following exception:

```
System.InvalidOperationException: The ConfigureHttpClient method isn't supported when creating gRPC clients. Unable to create client with name 'GreeterClient'.
```

To resolve this issue, we recommend upgrading to `Grpc.Net.ClientFactory` version `2.64.0` or later.

There's a build time check that verifies if you're using `Grpc.Net.ClientFactory` version `2.63.0` or earlier, and if you are the check produces a compilation warning. You can suppress the warning by setting the following property in your project file:

```
<PropertyGroup>
  <SuppressCheckGrpcNetClientFactoryVersion>true</SuppressCheckGrpcNetClientFactoryVersion>
</PropertyGroup>
```

### Compatibility with .NET Application Insights

If you're using .NET Application Insights version **2.22.0** or lower, then enabling resilience functionality in your application could cause all Application Insights telemetry to be missing. The issue occurs when resilience functionality is registered before Application Insights services. Consider the following sample causing the issue:

```
// At first, we register resilience functionality.
services.AddHttpClient().AddStandardResilienceHandler();

// And then we register Application Insights. As a result, Application Insights doesn't work.
services.AddApplicationInsightsTelemetry();
```

The issue can be fixed by updating .NET Application Insights to version **2.23.0** or higher. If you can't update it, then registering Application Insights services before resilience functionality, as shown below, will fix the issue:

```
// We register Application Insights first, and now it is working correctly.
services.AddApplicationInsightsTelemetry();
services.AddHttpClient().AddStandardResilienceHandler();
```
