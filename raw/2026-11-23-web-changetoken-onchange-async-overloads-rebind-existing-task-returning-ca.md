---
source: "https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/changetoken-onchange-async-overloads-rebind-callbacks"
title: "ChangeToken.OnChange async overloads rebind existing Task-returning callbacks"
author: "Microsoft"
date_published: "unknown"
date_clipped: "2026-11-23"
category: ".NET Ecosystem"
source_type: "web"
---

Source: https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/changetoken-onchange-async-overloads-rebind-callbacks

# ChangeToken.OnChange async overloads rebind existing Task-returning callbacks

Starting in .NET 11, [OnChange](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.primitives.changetoken.onchange) adds async callback overloads. After you recompile against .NET 11, existing calls that pass an `async` lambda or a `Task`-returning callback can silently bind to a different overload and behave differently at runtime.

## Version introduced

.NET 11

## Previous behavior

Previously, `ChangeToken.OnChange` only exposed synchronous callback overloads:

```
public static IDisposable OnChange(Func<IChangeToken?> changeTokenProducer, Action changeTokenConsumer);
public static IDisposable OnChange<TState>(Func<IChangeToken?> changeTokenProducer, Action<TState> changeTokenConsumer, TState state);
```

If you passed an `async` lambda, the compiler bound the call to an `Action` overload and compiled the lambda as `async void`. The callback behaved as fire-and-forget. `ChangeToken.OnChange` re-registered for the next change as soon as the callback yielded at its first incomplete `await`, and exceptions thrown later surfaced on the synchronization context or thread pool.

```
// Bound to OnChange(Func<IChangeToken?>, Action) and compiled as 'async void'.
ChangeToken.OnChange(config.GetReloadToken, async () =>
{
    await Task.Delay(1000);
    Console.WriteLine("Reloaded");
});
```

## New behavior

Starting in .NET 11, `ChangeToken.OnChange` includes two asynchronous callback overloads:

```
public static IDisposable OnChange(Func<IChangeToken?> changeTokenProducer, Func<Task> changeTokenConsumer);
public static IDisposable OnChange<TState>(Func<IChangeToken?> changeTokenProducer, Func<TState, Task> changeTokenConsumer, TState state);
```

If you pass an `async` lambda or another `Task`-returning callback, the compiler now binds to `Func<Task>` or `Func<TState, Task>`. The callback compiles as `async Task` instead of `async void`, and `ChangeToken.OnChange` re-registers only after the returned task completes. If multiple changes occur while the callback task runs, `ChangeToken.OnChange` coalesces those changes into one later callback invocation.

```
// Binds to OnChange(Func<IChangeToken?>, Func<Task>) and compiles as 'async Task'.
// The token re-registers after the returned task completes.
ChangeToken.OnChange(config.GetReloadToken, async () =>
{
    await Task.Delay(1000);
    Console.WriteLine("Reloaded");
});
```

This overload rebinding is silent. The same source code still compiles, and the compiler reports no ambiguity.

## Type of breaking change

This change is a [behavioral change](https://learn.microsoft.com/en-us/dotnet/core/compatibility/categories#behavioral-change).

## Reason for change

To support correct asynchronous workflows, `ChangeToken.OnChange` now provides callback overloads that return `Task`. Before .NET 11, asynchronous callback logic required `async void` or synchronous blocking, which made error handling and callback timing harder to control. For API approval details, see [dotnet/runtime#69099](https://github.com/dotnet/runtime/issues/69099).

## Recommended action

For most code, no action is required. The new binding usually improves behavior because asynchronous work now completes before `ChangeToken.OnChange` re-registers for the next notification.

If you need the previous fire-and-forget `async void` behavior, cast the callback to `Action` (or `Action<TState>`) so your call continues to bind to the synchronous overload:

```
ChangeToken.OnChange(config.GetReloadToken, (Action)(async () =>
{
    await Task.Delay(1000);
    Console.WriteLine("Reloaded");
}));
```

You can't control this behavior with an AppContext switch or configuration setting. Overload selection happens at compile time.

## Affected APIs

- `OnChange(Func<IChangeToken?> changeTokenProducer, Func<Task> changeTokenConsumer)`
- `OnChange<TState>(Func<IChangeToken?> changeTokenProducer, Func<TState, Task> changeTokenConsumer, TState state)`
- [Microsoft.Extensions.Primitives.ChangeToken.OnChange(Func<IChangeToken>, Action)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.primitives.changetoken.onchange#microsoft-extensions-primitives-changetoken-onchange(system-func((microsoft-extensions-primitives-ichangetoken))-system-action))
- [Microsoft.Extensions.Primitives.ChangeToken.OnChange<TState>(Func<IChangeToken>, Action<TState>, TState)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.primitives.changetoken.onchange#microsoft-extensions-primitives-changetoken-onchange-1(system-func((microsoft-extensions-primitives-ichangetoken))-system-action((-0))-0))
