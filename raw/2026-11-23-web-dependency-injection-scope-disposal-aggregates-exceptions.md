---
source: "https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/dependency-injection-disposal-exceptions"
title: "Dependency injection scope disposal aggregates exceptions"
author: "Microsoft"
date_published: "unknown"
date_clipped: "2026-11-23"
category: ".NET Ecosystem"
source_type: "web"
---

Source: https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/dependency-injection-disposal-exceptions

# Dependency injection scope disposal aggregates exceptions

In .NET 11, the built-in dependency injection container attempts to dispose every captured disposable service, even if a service throws an exception. This behavior applies to synchronous and asynchronous disposal of scopes and root service providers. Multiple disposal failures produce an [AggregateException](https://learn.microsoft.com/en-us/dotnet/api/system.aggregateexception).

## Version introduced

.NET 11

## Previous behavior

Previously, scope and root provider disposal processed captured disposable services in reverse capture order but stopped at the first exception. That exception propagated unchanged, and the remaining services weren't disposed.

For example, suppose you resolved `FirstDisposable` and then `SecondDisposable`, and both services threw during disposal. The container disposed `SecondDisposable` first. Its exception prevented disposal of `FirstDisposable`.

## New behavior

Starting in .NET 11, synchronous and asynchronous disposal of built-in scopes and root service providers attempts every captured disposable service in reverse capture order, even after a failure.

After all disposal attempts finish, a single exception is rethrown unchanged. If multiple disposal operations fail, disposal throws an [AggregateException](https://learn.microsoft.com/en-us/dotnet/api/system.aggregateexception) that contains all the exceptions.

In the preceding example, the container attempts to dispose `SecondDisposable` and then `FirstDisposable`. Because both throw, disposal throws an `AggregateException` that contains both exceptions.

## Type of breaking change

This change is a [behavioral change](https://learn.microsoft.com/en-us/dotnet/core/compatibility/categories#behavioral-change).

## Reason for change

To give every captured service an opportunity to release resources such as timers, event handlers, and unmanaged handles, the container continues disposal after exceptions. Previously, one service's failure prevented other services from releasing their resources.

For more information, see [dotnet/runtime PR #123342](https://github.com/dotnet/runtime/pull/123342).

## Recommended action

No action is required if your disposal implementations don't throw and your code doesn't rely on disposal to stop after the first failure.

To avoid cleanup failures, prefer `Dispose()` and `DisposeAsync()` implementations that don't throw. If your code handles disposal failures, handle both the original exception for a single failure and `AggregateException` for multiple failures. Catch `AggregateException` before a general exception handler, and inspect [InnerExceptions](https://learn.microsoft.com/en-us/dotnet/api/system.aggregateexception.innerexceptions#system-aggregateexception-innerexceptions) to handle each failure.

Don't rely on a disposal exception to prevent other services from being disposed. No compatibility switch restores the previous behavior.

## Affected APIs

- [Microsoft.Extensions.DependencyInjection.ServiceProvider.Dispose()](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.serviceprovider.dispose#microsoft-extensions-dependencyinjection-serviceprovider-dispose)
- [Microsoft.Extensions.DependencyInjection.ServiceProvider.DisposeAsync()](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.serviceprovider.disposeasync#microsoft-extensions-dependencyinjection-serviceprovider-disposeasync)
- [Microsoft.Extensions.DependencyInjection.AsyncServiceScope.Dispose()](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.asyncservicescope.dispose#microsoft-extensions-dependencyinjection-asyncservicescope-dispose)
- [Microsoft.Extensions.DependencyInjection.AsyncServiceScope.DisposeAsync()](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.asyncservicescope.disposeasync#microsoft-extensions-dependencyinjection-asyncservicescope-disposeasync)
- [System.IDisposable.Dispose()](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable.dispose#system-idisposable-dispose) on [Microsoft.Extensions.DependencyInjection.IServiceScope](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.iservicescope) instances created by the built-in container.
