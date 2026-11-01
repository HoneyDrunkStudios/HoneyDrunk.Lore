---
source: "https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/how-to/test-dotnet-http-resilience"
title: "Test retries and timeouts in .NET apps that use Microsoft.Extensions.Http.Resilience"
author: "waldekmastykarz"
date_published: "unknown"
date_clipped: "2026-10-31"
category: ".NET Ecosystem"
source_type: "web"
last_updated: "2026-10-29"
---

# Test retries and timeouts in .NET apps that use Microsoft.Extensions.Http.Resilience

Tip

New to throttling? Learn [what throttling is](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/concepts/what-is-throttling) and [how to handle it](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/concepts/how-to-handle-api-throttling).

> **At a glance**  
> **Goal:** Confirm that your .NET HTTP resilience handler retries, backs off, and times out as expected  
> **Time:** 15 minutes  
> **Plugins:** [GenericRandomErrorPlugin](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/technical-reference/genericrandomerrorplugin), [RetryAfterPlugin](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/technical-reference/retryafterplugin), [LatencyPlugin](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/technical-reference/latencyplugin)  
> **Prerequisites:** [Set up Dev Proxy](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/get-started/set-up), a .NET app that uses [Microsoft.Extensions.Http.Resilience](https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience)

You added `AddStandardResilienceHandler()` to your `HttpClient`. How do you know it works? The APIs you call rarely fail on demand, and unit tests that mock `HttpMessageHandler` skip the resilience pipeline that you want to test.

Dev Proxy sits between your app and the API. It returns errors and slow responses to your app, so your app runs unchanged and the resilience handler reacts to real HTTP responses. You see every attempt in the Dev Proxy output.

## What the standard resilience handler does

Before you test, know what to expect. With default options, `AddStandardResilienceHandler()`:

| Behavior | Default |
| --- | --- |
| Retries on | HTTP 500 and above, 408, 429, `HttpRequestException`, and `TimeoutRejectedException` |
| Number of retries | 3, with exponential backoff and jitter, starting at 2 seconds |
| `Retry-After` header | Honored. The handler waits for the time the API asks for. |
| Attempt timeout | 10 seconds per attempt |
| Total timeout | 30 seconds for the request, including all retries |

For the full list of strategies and their defaults, see [Standard resilience handler defaults](https://learn.microsoft.com/en-us/dotnet/core/resilience/http-resilience#standard-resilience-handler-defaults).

## Route your app through Dev Proxy

.NET uses the system proxy, so when you start Dev Proxy, it intercepts your app's requests without code changes. For more information, see [Use Dev Proxy with .NET applications](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/how-to/use-dev-proxy-with-dotnet).

## Simulate transient errors

Create a Dev Proxy configuration that fails requests to your API with the errors that the handler retries. This example uses `https://api.contoso.com`. Replace it with the URL of the API that your app calls.

**File:** devproxyrc.json

```
{
  "$schema": "https://raw.githubusercontent.com/dotnet/dev-proxy/main/schemas/v4.0.0/rc.schema.json",
  "plugins": [
    {
      "name": "RetryAfterPlugin",
      "enabled": true,
      "pluginPath": "~appFolder/plugins/DevProxy.Plugins.dll"
    },
    {
      "name": "GenericRandomErrorPlugin",
      "enabled": true,
      "pluginPath": "~appFolder/plugins/DevProxy.Plugins.dll",
      "configSection": "transientErrors"
    }
  ],
  "urlsToWatch": [
    "https://api.contoso.com/*"
  ],
  "transientErrors": {
    "$schema": "https://raw.githubusercontent.com/dotnet/dev-proxy/main/schemas/v4.0.0/genericrandomerrorplugin.schema.json",
    "errorsFile": "transient-errors.json",
    "rate": 50
  }
}
```

Caution

Add the `RetryAfterPlugin` before the `GenericRandomErrorPlugin` in your configuration file. If you add it after, the `GenericRandomErrorPlugin` fails the request before the `RetryAfterPlugin` can check it.

In the errors file, define a throttling response and two server errors. The `@dynamic` value sets the `Retry-After` header and tells the `RetryAfterPlugin` to check that your app waits that long before it calls the API again.

**File:** transient-errors.json

```
{
  "$schema": "https://raw.githubusercontent.com/dotnet/dev-proxy/main/schemas/v4.0.0/genericrandomerrorplugin.errorsfile.schema.json",
  "errors": [
    {
      "request": {
        "url": "https://api.contoso.com/*"
      },
      "responses": [
        {
          "statusCode": 429,
          "headers": [
            {
              "name": "Retry-After",
              "value": "@dynamic"
            }
          ]
        },
        {
          "statusCode": 500
        },
        {
          "statusCode": 503
        }
      ]
    }
  ]
}
```

Start Dev Proxy and run your app.

```
devproxy --config-file devproxyrc.json
```

With a 50% failure rate, most requests recover after one or two retries. In the Dev Proxy output, check that:

- After a 429 response, the next attempt to the same URL comes after the `Retry-After` time. Dev Proxy uses 5 seconds by default. If your app calls the API too early, the `RetryAfterPlugin` reports it and throttles the request.
- Your app doesn't send more attempts than you configured.
- Requests that you don't want to retry, like a `POST` that creates a record, are sent only once. To exclude them, call `options.Retry.DisableForUnsafeHttpMethods()` or `options.Retry.DisableFor(...)`.

## Test what happens when retries run out

Retries hide short failures. You also need to know what your app does when the API keeps failing. Start Dev Proxy with a 100% failure rate:

```
devproxy --config-file devproxyrc.json --failure-rate 100
```

Dev Proxy shows 4 attempts for each request: the original request and 3 retries. After the last retry, the standard handler doesn't throw. It returns the last error response to your code. Check what your app does with it. For example, `EnsureSuccessStatusCode()` throws an `HttpRequestException`, and `GetStringAsync()` throws as well. Make sure that your app shows a useful message or falls back, instead of crashing or showing a generic error.

## Test timeouts

Slow APIs trigger a different path in the handler. To test it, use the [LatencyPlugin](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/technical-reference/latencyplugin) to delay responses beyond the 10-second attempt timeout.

**File:** devproxyrc.json

```
{
  "$schema": "https://raw.githubusercontent.com/dotnet/dev-proxy/main/schemas/v4.0.0/rc.schema.json",
  "plugins": [
    {
      "name": "LatencyPlugin",
      "enabled": true,
      "pluginPath": "~appFolder/plugins/DevProxy.Plugins.dll",
      "configSection": "slowApi"
    }
  ],
  "urlsToWatch": [
    "https://api.contoso.com/*"
  ],
  "slowApi": {
    "$schema": "https://raw.githubusercontent.com/dotnet/dev-proxy/main/schemas/v4.0.0/latencyplugin.schema.json",
    "minMs": 11000,
    "maxMs": 15000
  }
}
```

Start Dev Proxy and run your app. Each attempt takes longer than 10 seconds, so the attempt timeout cancels it and the handler retries. After 30 seconds, the total timeout cancels the request and your code gets a `TimeoutRejectedException`. Check that your app catches it and tells the user what happened.

Tip

To test the same scenarios with your own resilience settings, change the values in your `AddStandardResilienceHandler(options => ...)` call and run the same Dev Proxy configurations again.

## Next step

Learn more about simulating throttling on any API.

[Test that my application handles throttling properly](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/how-to/test-that-my-application-handles-throttling-properly)

## See also

- [Use Dev Proxy with .NET applications](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/how-to/use-dev-proxy-with-dotnet) - .NET setup
- [GenericRandomErrorPlugin](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/technical-reference/genericrandomerrorplugin) - Full reference
- [RetryAfterPlugin](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/technical-reference/retryafterplugin) - Verify retry behavior
- [LatencyPlugin](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/technical-reference/latencyplugin) - Simulate slow responses
- [Change request failure rate](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/how-to/change-request-failure-rate) - Adjust how often requests fail
- [Use Dev Proxy in CI/CD](https://learn.microsoft.com/en-us/microsoft-cloud/dev/dev-proxy/how-to/use-dev-proxy-in-ci-cd-overview) - Automate resilience testing in your pipeline
