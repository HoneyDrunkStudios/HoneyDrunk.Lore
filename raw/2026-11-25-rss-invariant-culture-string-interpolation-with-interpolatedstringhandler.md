---
source: "https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/"
title: "Invariant culture string interpolation with [InterpolatedStringHandler]"
author: "Andrew Lock"
date_published: "2026-11-24"
date_clipped: "2026-11-25"
category: ".NET Ecosystem"
source_type: "rss"
---

# Invariant culture string interpolation with [InterpolatedStringHandler]

In this post, I describe how you can use a custom `[InterpolatedStringHandler]` to ensure string interpolation (e.g. `$"My value is {value}"`) formats values using the invariant culture. This can be important in many situations, such as in logging and other telemetry, as well as if you need to round trip values between different formats.

## [Interpolated strings and culture formatting](https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/#interpolated-strings-and-culture-formatting)

String interpolation was introduced way back in C# 6, back when .NET Core 1.0 was just being released! In it's simplest form, string interpolation provides some syntactic sugar around the venerable `string.Format()` method. So instead of code that looks like this:

```
var someInt = 123;
var someDouble = -1.23d;

string formatted = string.Format("the int is: {0}, the double is: {1}, someInt, someDouble");
```

The string formatting code instead looks like this:

```
string formatted = $"the int is: {someInt}, the double is: {someDouble}";
```

As well as being neater and easier to follow, it also removes a class of bugs related to mismatching "holes" and "values". As .NET has progressed (unsurprisingly for .NET Core) the performance of string interpolation has improved dramatically, as well as receiving additional features.

One thing to note is that by default, string interpolation always uses the *current* culture, which means that the final text contained in `formatted` is culture-specific, and depends where the app runs.

For example, if you compare the formatting in `en-US` (English-US) with `de-DE` (German-Germany), you can see that the double format is quite different:

```
CultureInfo.CurrentCulture = CultureInfo.GetCultureInfo("en-US");
Console.WriteLine($"the double is: {someDouble}"); // the double is: -1.23

CultureInfo.CurrentCulture = CultureInfo.GetCultureInfo("de-DE");
Console.WriteLine($"the double is: {someDouble}"); // the double is: -1,23
```

Different culture; different `double` formatting…

But what if you don't *want* that behaviour, and instead you want *consistent* formatting, using `CultureInfo.InvariantCulture`? There's no way to "pass" a culture into the string interpolation `$"..."` syntax, so does that mean you have to go back to the old `string.Format` option? What if you *always* want to use the invariant culture? What are your options?

## [Globalization Invariant Mode](https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/#globalization-invariant-mode)

Let's start with the last point—what if you *always* want to use the invariant culture? Well, if you're writing an *application*, and you're using .NET Core, you can opt into [Globalization Invariant Mode](https://learn.microsoft.com/en-us/dotnet/core/runtime-config/globalization#invariant-mode). There are many ways to set this; you can set the environment variable `DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1`; you can use *runtimeconfig.json*; or you can set the MSBuild property:

```
<PropertyGroup>
  <InvariantGlobalization>true</InvariantGlobalization>
</PropertyGroup>
```

This is a pretty heavy switch, in that it switches *everything* to use invariant culture rules, which may or may not be what you want. Additionally, this applies at the *app* level, so if you're writing a library, you can't rely on that switch. And finally, this doesn't apply to .NET Framework, so it may not be applicable depending on the environments you need to run in.

With that out the way, let's look at more targeted approaches.

## [`string.Create()` in modern .NET](https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/#string-create-in-modern-net)

If we start by thinking about modern .NET, then [there's an easy way](https://github.com/dotnet/runtime/issues/73639) to achieve our goal by using the `string.Create()` method that was introduced in .NET 6:

```
// Pass the desired culture as the first argument
string formatted = string.Create(CultureInfo.InvariantCulture, $"the double is: {someDouble}");
```

Now, if you're not familiar with how this works, it looks a *bit* like there's two `string`s: the interpolated string and the return value of `string.Create()`, but that's not how this works. [The method signature](https://learn.microsoft.com/en-us/dotnet/api/system.string.create?view=net-10.0#system-string-create(system-iformatprovider-system-runtime-compilerservices-defaultinterpolatedstringhandler@)) gives a hint to what's going on:

```
public static string Create(
    IFormatProvider? provider,
    ref DefaultInterpolatedStringHandler handler);
```

That `DefaultInterpolatedStringHandler` is the interesting part, and we'll come back to that before the end of the post.

`string.Create()` works great if you're working only with modern .NET, but if, like me, you work on a library that's used in older frameworks too (`netstandard2.0`, .NET Framework), then we need another approach.

## [`FormattableString.Invariant()` for legacy .NET](https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/#formattablestring-invariant-for-legacy-net)

`FormattableString` was introduced at the same time as string interpolation was introduced in C#, with .NET Framework 4.6 and .NET Core 1.0, and it provides a way to format an interpolated string with the invariant culture by using the `static` method `FormattableString.Invariant()`:

```
string formatted = FormattableString.Invariant($"the double is: {someDouble}"); // the double is: -1.23
```

The interpolated string is implicitly converted to a `FormattableString` instance, which is an abstract class, e.g.

```
// implicity convert to FormattableString
FormattableString formattable = $"the double is: {someDouble}";

// format the FormattableString as a string using the invariant culture
string formatted = FormattableString.Invariant(formattable);
```

Behind the scenes, in .NET Framework, the compiler calls `FormattableStringFactory.Create()`, which returns a private implementation, `ConcreteFormattableString`:

```
public static class FormattableStringFactory
{
    public static FormattableString Create(string format,params object[] arguments)
      =>  new ConcreteFormattableString(format, arguments);

    // private implementation of FormattableString
    private sealed class ConcreteFormattableString : FormattableString
    {
        private readonly string _format;
        private readonly object[] _arguments;

        public ConcreteFormattableString(string format, object[] arguments)
        {
            _format = format;
            _arguments = arguments;
        }

        public override string Format => _format;
        public override object[] GetArguments() => _arguments;
        public override int ArgumentCount => _arguments.Length;
        public override object GetArgument(int index) => _arguments[index];
        public override string ToString(IFormatProvider formatProvider)
            => string.Format(formatProvider, _format, _arguments);
    }
}
```

The important takeaway from the code above is that the interpolated string is decomposed into a `string format` and an `object[] arguments`, and is ultimately turned into a "normal" `string.Format` call when it's converted into a string. This obviously *works* fine, but the `object[]` allocation clearly stands out as a source of extra allocation; not only will that array need to be allocated, you'll have to box any value types (e.g. the `int` or `double` above) further increasing the allocation.

Additionally, the fact that you need to use completely different APIs for invariant interpolated string handling between .NET 6 and older frameworks is a little annoying. Ideally, it would be nice to have a simple helper method that dispatches to the best option for libraries that multi-target multiple frameworks, so you don't have to think about it at the target.

In the next section, I provide a possible implementation, which not only unifies the API across frameworks, but also reduces allocation.

## [A solution for older TFMs with `[InterpolatedStringHandler]`](https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/#a-solution-for-older-tfms-with-interpolatedstringhandler-)

The key to the following solution is the `[InterpolatedStringHandler]` attribute. This attribute was added in C#10 (alongside .NET 6) and [lets you control *how* interpolated strings `$"..."` are handled](https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/performance/interpolated-string-handler). The `string.Create()` method shown above for .NET 6 uses [one implementation, `DefaultInterpolatedStringHandler`](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.defaultinterpolatedstringhandler?view=net-10.0), which formats a string handler directly into the internal `Span<T>` of a `string` being created, making it very efficient. However, you can write your own handlers too.

An interpolated string handler is a type that processes a placeholder interpolated string expression in some way. It doesn't *have* to directly create or format the values into a `string`, though that is obviously the most common use.

### [Creating a helper for invariant interpolated string formatting](https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/#creating-a-helper-for-invariant-interpolated-string-formatting)

We'll look at how to implement a handler shortly, but first we'll look at how it's used. For our use case of Invariant formatting, we'll create a simple helper class that we can call on all frameworks, like this:

```
var formatted = StringUtil.Invariant($"the double is {someDouble}");
```

This same method can be called on all supported frameworks (.NET Framework, .NET standard, .NET 6+ etc in this case), and it works similarly to `FormattableString.Invariant()`, but *without* the extra allocation this requires.

The implementation of this helper is very simple, but that's because the bulk of the implementation happens in our custom interpolated string handler. All the helper does is receive an instance of our custom `InvariantInterpolatedStringHandler`, and calls `ToStringAndClear()` on it:

```
public static class StringUtil
{
    public static string Invariant(ref InvariantInterpolatedStringHandler handler)
        => handler.ToStringAndClear();
}
```

The compiler is responsible for creating an instance of `InvariantInterpolatedStringHandler`, making all the appropriate calls on it, and passing it (by reference) as an argument to `StringUtil.Invariant`.

Clearly `InvariantInterpolatedStringHandler` is the important piece, so lets start by looking at a custom interpolated string handler implementation.

### [Implementing a custom interpolated string handler](https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/#implementing-a-custom-interpolated-string-handler)

A custom interpolated string handler has to have at *least* all of the following:

- The `[InterpolatedStringHandler]` attribute applied to the type.
- A constructor that takes two `int` parameters: `literalLength` and `formattedCount`
- A public method for string literals: `public void AppendLiteral(string s)`
- A public method for arbitrary values: `public void AppendFormatted<T>(T t)`

It's valid (and common) to have *more* methods than this minimum set, and the runtime will use them when available, but you must have *at least* this set. In addition, it's common for the implementation to be a `ref struct`, to avoid any extra allocations.

A very simple minimal handler that meets these requirements might look something like this:

```
[InterpolatedStringHandler]
public ref struct StringBuilderInterpolatedStringHandler
{
    StringBuilder builder;

    public LogInterpolatedStringHandler(int literalLength, int formattedCount)
    {
        builder = new StringBuilder(literalLength);
    }

    public void AppendLiteral(string s) => builder.Append(s);

    public void AppendFormatted<T>(T t) => builder.Append(t?.ToString());

    public override string ToString() => builder.ToString();
}
```

This ticks all the boxes, and uses a `StringBuilder` to build up the final string. I'm not suggesting you should use this implementation for anything, this is just an example of the minimum amount you need!

In the next section we finally get to on of our "real" handlers, starting with the .NET 6+ implementation.

### [Delegating to `DefaultInterpolatedStringHandler` for .NET 6+](https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/#delegating-to-defaultinterpolatedstringhandler-for-net-6)

*Part* of the reason for creating `StringUtil.Invariant()` was to provide a consistent API across multiple frameworks and the *other* part of the reason was to provide a more efficient way of performing invariant formatting. .NET 6+ already *has* a very efficient way of doing the formatting, so the `InvariantInterpolatedStringHandler` implementation below for .NET 6+ entirely leverages that, and we just need to make sure we can use it in our API.

The following implementation essentially delegates everything to the `DefaultInterpolatedStringHandler` implementation that's already provided as part of .NET 6 (and is heavily optimized). `DefaultInterpolatedStringHandler` is used by the existing `string.Create()` method, so all we're doing is setting the inner handler's culture to be `CultureInfo.InvariantCulture`, and then delegating all the method calls the runtime makes on *our* handler to the inner handler.

```
// This is the implementation for .NET 6+
#if NET6_0_OR_GREATER

using System.Globalization;
using System.Runtime.CompilerServices;

namespace System;

[InterpolatedStringHandler]
internal ref struct InvariantInterpolatedStringHandler
{
    // We delegate all calls this handler
    private DefaultInterpolatedStringHandler _handler;

    // Mirror the constructors available on DefaultInterpolatedStringHandler 
    public InvariantInterpolatedStringHandler(int literalLength, int formattedCount)
    {
        // We explicitly pass CultureInfo.InvariantCulture to force invariant formatting
        _handler = new DefaultInterpolatedStringHandler(literalLength, formattedCount, CultureInfo.InvariantCulture);
    }

    public InvariantInterpolatedStringHandler(int literalLength, int formattedCount, Span<char> initialBuffer)
    {
        // We explicitly pass CultureInfo.InvariantCulture to force invariant formatting
        _handler = new DefaultInterpolatedStringHandler(literalLength, formattedCount, CultureInfo.InvariantCulture, initialBuffer);
    }

    // Mirror and delegate the methods on DefaultInterpolatedStringHandler

    public void AppendLiteral(string value) => AppendLiteral(value);

    public void AppendFormatted(scoped ReadOnlySpan<char> value) => _handler.AppendFormatted(value);
    public void AppendFormatted(string? value) => _handler.AppendFormatted(value);
    public void AppendFormatted(object? value, int alignment = 0, string? format = default)
      => _handler.AppendFormatted(value, alignment, format);
    public void AppendFormatted(scoped ReadOnlySpan<char> value, int alignment = 0, string? format = default)
      => _handler.AppendFormatted(value, alignment, format);
    public void AppendFormatted(string? value, int alignment = 0, string? format = default)
      => _handler.AppendFormatted(value, alignment, format);
    public void AppendFormatted<T>(T value, int alignment, string? format)
      => _handler.AppendFormatted(value, alignment, format);
    public void AppendFormatted<T>(T value, string? format) => _handler.AppendFormatted(value, format);
    public void AppendFormatted<T>(T value) => _handler.AppendFormatted(value);
    public void AppendFormatted<T>(T value, int alignment) => _handler.AppendFormatted(value, alignment);

    public void Clear() => _handler.Clear();

    public override string ToString() => _handler.ToString();
    public string ToStringAndClear() => _handler.ToStringAndClear();
}
#endif
```

Having to mirror all of this feels a little bit messy, and it is, but it's unfortunately the only way I could find. *Ideally* it would be nicer to be able to just use the `DefaultInterpolatedStringHandler` directly, and to specify the culture you want, but unfortunately I couldn't find a way to do that, hence the code above.

The good news is that the performance of our `StringUtil.Invariant()` method with the custom handler is essentially identical to `string.Create()` and `DefaultInterpolatedStringHandler` (and is significantly better than the alternatives) allocation-wise:

| Method | Mean | Error | StdDev | Allocated |
| --- | --- | --- | --- | --- |
| StringCreate\_InvariantCulture | 191.9 ns | 3.80 ns | 9.88 ns | 176 B |
| StringUtil\_Invariant | 177.4 ns | 3.07 ns | 2.72 ns | 176 B |
| FormattableString\_InvariantCulture | 196.3 ns | 3.44 ns | 3.53 ns | 264 B |
| StringFormat\_InvariantCulture | 190.2 ns | 3.59 ns | 3.36 ns | 224 B |

The important thing for me is that this messiness is hidden from the *users* of the API, and the net result is that the following calls give identical outputs for .NET 6+:

```
// The "raw" string.Create version available in .NET 6+
string formatted = string.Create(CultureInfo.InvariantCulture, $"the double is: {someDouble}");

// Our uniform API that goes through our InvariantInterpolatedStringHandler 
var formatted = StringUtil.Invariant($"the double is {someDouble}")
```

With .NET 6+ covered, we now need to provide the implementation for the other frameworks, such as .NET Framework.

### [Implementing `InvariantInterpolatedStringHandler` on .NET Framework](https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/#implementing-invariantinterpolatedstringhandler-on-net-framework)

For the .NET Framework custom handler we use a `StringBuilder` as the core builder type, [and a simple thread-local cache](https://github.com/DataDog/dd-trace-dotnet/blob/master/tracer/src/Datadog.Trace/Util/StringBuilderCache.cs) of `StringBuilder` instances means that the `StringBuilder` allocations are amortized to zero.

The following is a relatively simple implementation that adds only a couple of possible `AppendFormatted` overloads. This definitely isn't perfect, and there's a lot of places where we need to call `ToString()`, which feels dirty when you're used to writing modern .NET 😅 But the end result is still a win, as you'll see shortly:

```
#if !NET6_0_OR_GREATER
[InterpolatedStringHandler]
public ref struct InvariantInterpolatedStringHandler
{
    private readonly StringBuilder _builder;

    public InvariantInterpolatedStringHandler(int literalLength, int formattedCount)
    {
        // Assume each hole is roughly the length of a formatted int to roughly
        // pre-size the StringBuilder 
        _builder = StringBuilderCache.Acquire(literalLength + (formattedCount * 11));
    }

    public void AppendLiteral(string value) => _builder.Append(value);

    // Non-generic overloads for the most common holes, so they don't box on .NET Framework
    public void AppendFormatted(int value) => _builder.Append(value.ToString(CultureInfo.InvariantCulture));

    public void AppendFormatted(long value) => _builder.Append(value.ToString(CultureInfo.InvariantCulture));

    public void AppendFormatted(double value) => _builder.Append(value.ToString(CultureInfo.InvariantCulture));

    public void AppendFormatted<T>(T value) => AppendFormatted(value, format: null);

    public void AppendFormatted<T>(T value, string? format)
    {
        if (value is IFormattable formattable)
        {
            _builder.Append(formattable.ToString(format, CultureInfo.InvariantCulture));
        }
        else if (value is not null)
        {
            _builder.Append(value.ToString());
        }
    }

    public void AppendFormatted(string? value) => _builder.Append(value);

    public string ToStringAndClear() => StringBuilderCache.GetStringAndRelease(_builder);
}
#endif
```

There's a lot that's suboptimal in here, and we could potentially add a bunch more overloads etc. But if we write a simple benchmark, we can see that it still works out better than the alternatives:

```
[MemoryDiagnoser]
public class StringInterpolationBenchmark
{
    [Benchmark]
    public string StringUtil_Invariant()
        => StringUtil.Invariant($"MinValue is {double.MinValue}. MaxValue is {double.MaxValue}.");

    // Uses current culture, not invariant culture, but here for comparison
    [Benchmark]
    public string StringInterpolation_CurrentCulture()
        => $"MinValue is {double.MinValue}. MaxValue is {double.MaxValue}.";

    [Benchmark]
    public string StringFormat_InvariantCulture()
        => string.Format(CultureInfo.InvariantCulture,
            "MinValue is {0}. MaxValue is {1}.",
            double.MinValue,
            double.MaxValue);

    [Benchmark]
    public string FormattableString_Invariant()
    {
        FormattableString formattable = $"MinValue is {double.MinValue}. MaxValue is {double.MaxValue}.";
        return FormattableString.Invariant(formattable);
    }
}
```

Looking at the results, you can see that out custom handler is both faster *and* lower allocation than the available alternatives on .NET Framework:

| Method | Mean | Error | StdDev | Allocated |
| --- | --- | --- | --- | --- |
| StringUtil\_Invariant | 4.464 us | 0.0813 us | 0.0721 us | 313 B |
| StringInterpolation\_CurrentCulture | 4.601 us | 0.0745 us | 0.0697 us | 361 B |
| StringFormat\_InvariantCulture | 4.590 us | 0.0491 us | 0.0435 us | 361 B |
| FormattableString\_InvariantCulture | 4.665 us | 0.0903 us | 0.1174 us | 433 B |

So, as a reminder, the *main* reason we started looking at interpolated string handlers in the first place was because we wanted to improve on the allocations compared to `FormattableString.Invariant`, and the benchmarks above show that at least for this simple example, we've achieved our goal with a simple helper method.

That wasn't the *only* reason though; by combining the two different `InvariantInterpolatedStringHandler` methods, we can provide a consistent API across all the target frameworks that we need to support, while preserving the high performance of the .NET 6+ `string.Create()` method. Win-win.

## [Summary](https://andrewlock.net/invariant-culture-string-interpolation-with-interpolatedstringhandler/#summary)

In this post I discussed the fact that interpolated strings like `$"double: {someDouble}"` always format using the current culture by default. However, sometimes you might want to format consistently using `CultureInfo.InvariantCulture`. I described the built in solutions like globalization invariant mode for apps, `string.Create()` in .NET 6+, and `FormattableString.Invariant` for older frameworks.

Finally, I describe an approach that allows the best of all worlds: the performance of `string.Create()` on .NET 6+, and fewer allocations than `FormattableString`. This involves creating a small helper method, and implementing a custom interpolated string handler using `[InterpolatedStringHandler]`. On .NET 6+, this just defers to the standard `DefaultInterpolatedStringHandler`, while on .NET Framework we use a `StringBuilder` and a simple object cache to improve both allocations and execution time.
