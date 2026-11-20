---
source: "https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/ihost-runasync-stopasync-throw-backgroundservice-failure"
title: "IHost.RunAsync and IHost.StopAsync throw when a BackgroundService fails"
author: "gewarren"
date_published: "unknown"
date_clipped: "2026-11-20"
category: ".NET Ecosystem"
source_type: "web"
source_last_updated: "2026-11-11"
---

# IHost.RunAsync and IHost.StopAsync throw when a BackgroundService fails

When a [BackgroundService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.backgroundservice) fails with an exception from its `ExecuteAsync` method and [HostOptions.BackgroundServiceExceptionBehavior](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.hostoptions.backgroundserviceexceptionbehavior#microsoft-extensions-hosting-hostoptions-backgroundserviceexceptionbehavior) is set to [StopHost](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.backgroundserviceexceptionbehavior#microsoft-extensions-hosting-backgroundserviceexceptionbehavior-stophost) (the default), the host stops. In .NET 11, the tasks returned from `RunAsync`, `StopAsync`, `WaitForShutdownAsync`, and their synchronous equivalents now fail with an exception instead of completing successfully.

## Version introduced

.NET 11

## Previous behavior

Previously, when a `BackgroundService` threw an exception from its [ExecuteAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.backgroundservice.executeasync) method and `HostOptions.BackgroundServiceExceptionBehavior` was set to `BackgroundServiceExceptionBehavior.StopHost`, the task returned from calling `RunAsync`, `StopAsync`, or `WaitForShutdownAsync` completed successfully. This usually meant the application exited with a success exit code (zero).

## New behavior

Starting in .NET 11, when a `BackgroundService` throws an exception from its `ExecuteAsync` method and `HostOptions.BackgroundServiceExceptionBehavior` is set to `BackgroundServiceExceptionBehavior.StopHost`, the task returned from calling `RunAsync`, `StopAsync`, or `WaitForShutdownAsync` fails with an exception. The application typically exits with a failure exit code (non-zero).

- If a single service fails, the exception thrown by the service is rethrown.
- If multiple services fail, their exceptions are combined into an [AggregateException](https://learn.microsoft.com/en-us/dotnet/api/system.aggregateexception).

## Type of breaking change

This change is a [behavioral change](https://learn.microsoft.com/en-us/dotnet/core/compatibility/categories#behavioral-change).

## Reason for change

If an application stops because of a failure, it shouldn't exit with a success exit code. The previous behavior hid the failure, making it harder to detect and diagnose the exception that caused it.

## Recommended action

The recommended action is to do nothing—a failing application should exit with a failure exit code, which is the new behavior.

If you need to maintain the previous behavior and exit with a success exit code, wrap the `await` of `RunAsync` or `StopAsync` in a `try`-`catch` block:

```
try
{
    await host.RunAsync();
}
catch (Exception ex)
{
    // Log or inspect the exception if needed.
}
```

## Affected APIs

- [Microsoft.Extensions.Hosting.HostingAbstractionsHostExtensions.RunAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.hostingabstractionshostextensions.runasync)
- [Microsoft.Extensions.Hosting.HostingAbstractionsHostExtensions.Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.hostingabstractionshostextensions.run)
- [Microsoft.Extensions.Hosting.HostingAbstractionsHostExtensions.StopAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.hostingabstractionshostextensions.stopasync)
- [Microsoft.Extensions.Hosting.HostingAbstractionsHostExtensions.WaitForShutdownAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.hostingabstractionshostextensions.waitforshutdownasync)
- [Microsoft.Extensions.Hosting.HostingAbstractionsHostExtensions.WaitForShutdown](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.hostingabstractionshostextensions.waitforshutdown)
- [Microsoft.Extensions.Hosting.IHost.StopAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.hosting.ihost.stopasync) (default implementation)
