---
source: "https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods"
title: "Making foreach on an IEnumerable allocation-free using reflection and dynamic methods"
author: "Andrew Lock"
date_published: "2026-01-20"
date_clipped: "2026-10-12"
category: ".NET Ecosystem"
source_type: "rss"
---

# Making foreach on an IEnumerable allocation-free using reflection and dynamic methods

January 20, 2026  ~16 min read

* [Performance](https://andrewlock.net/tag/performance/)
* [.NET Core](https://andrewlock.net/tag/net-core/)
* [Datadog](https://andrewlock.net/tag/datadog/)

# Making foreach on an IEnumerable allocation-free using reflection and dynamic methods

In this post I describe a technique for reducing the allocation associated with calling `foreach` on an `IEnumerable<T>`. This has been [described](https://www.macrosssoftware.com/2020/07/13/enumerator-performance-surprises/) and [used](https://github.com/open-telemetry/opentelemetry-dotnet/blob/73bff75ef653f81fe6877299435b21131be36dc0/src/OpenTelemetry/Internal/EnumerationHelper.cs#L58) previously by others, but I was recently optimizing some code in my day job working on the .NET SDK at Datadog and used the technique, so decided to explain it in more detail.

## [Background: when `foreach` allocates](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#background-when-foreach-allocates)

`foreach` is one of the most commonly used patterns in C#; it's literally used all over the place. A quick, crude, [search of the dotnet/runtime](https://github.com/search?q=repo%3Adotnet%2Fruntime+%2F%28%3F-i%29foreach%2F+language%3AC%23&type=code&l=C%23) repository reveals 3.9 *thousand* instances! The vast majority of those cases are enumerating built-in types from the .NET base class library, such as `List<T>` and arrays, but you can easily `foreach` over your own custom types too.

Interestingly, the way that *most* people likely think or are taught about `foreach` is that you need to implement `IEnumerable` (or `IEnumerable<T>`), and then you can enumerate the collection. This is correct, but there's actually an interesting subtlety. *Technically* [the compiler uses pattern matching](https://ericlippert.com/2011/06/30/following-the-pattern/), and looks for a `GetEnumerator()` method that returns an `Enumerator`-like type with a `Current` property and `MoveNext` method. That pattern requirement is [the *same* as what `IEnumerable` defines](https://learn.microsoft.com/en-us/dotnet/api/system.collections.ienumerable.getenumerator?view=net-10.0), so what's the difference?

Before we dig into that, it's worth taking a look at a quick benchmark which demonstrates the difference.

### [Creating a benchmark to compare `foreach`](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#creating-a-benchmark-to-compare-foreach)

I started by creating a new BenchmarkDotNet project [using their templates](https://benchmarkdotnet.org/articles/guides/dotnet-new-templates.html) by running

```
dotnet new benchmark
```

I then updated the `Benchmarks` file as shown below. This simple benchmark just calls `foreach` on a `List<int>` instance, and then runs the same `foreach` loop on the *same* `List<int>`, but this time stored as an `IEnumerable<int>` variable:

```
using System.Collections.Generic;
using System.Linq;
using BenchmarkDotNet.Attributes;

[MemoryDiagnoser]
public class Benchmarks
{
    private List<int> _list;
    private IEnumerable<int> _enumerable;

    [GlobalSetup]
    public void GlobalSetup()
    {
        _list = Enumerable.Range(0, 10_000).ToList();
        _enumerable = _list;
    }

    [Benchmark]
    public long List()
    {
        var value = 0;
        foreach (int i in _list)
        {
            value += i;
        }

        return value;
    }

    [Benchmark]
    public long IEnumerable()
    {
        var value = 0;
        foreach (int i in _enumerable)
        {
            value += i;
        }

        return value;
    }
}
```

You might think that both these benchmarks would give the same results. Afterall, they're running the *same* `foreach` loop on the *same* `List<T>` instance. The only difference is whether the variable is stored as a `List<int>` or an `IEumerable<int>`, that can't make much difference, right?

If we run the benchmarks (I ran them against both .NET Framework and .NET 9), then we can see there actually *is* a difference; the `IEnumerable` version is both slower *and* it allocates:

| Method | Runtime | Mean | Error | StdDev | Allocated |
| --- | --- | --- | --- | --- | --- |
| List | .NET Framework 4.8 | 8.245 us | 0.1582 us | 0.1480 us | - |
| IEnumerable | .NET Framework 4.8 | 25.433 us | 0.4977 us | 0.6644 us | 40 B |
|  |  |  |  |  |  |
| List | .NET 9.0 | 2.951 us | 0.0587 us | 0.0861 us | - |
| IEnumerable | .NET 9.0 | 8.032 us | 0.1520 us | 0.1422 us | 40 B |

So the question is, *why*?

### [`foreach` as lowered C#](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#foreach-as-lowered-c-)

It helps initially to understand exactly what the `foreach` construct looks like in "lowered" C#. This is effectively what the compiler converts the `foreach` loop into before converting it to IL. If we take the `EnumerateList()` method above and [run it through sharplab.io](https://sharplab.io/#v2:CYLg1APgAgDABFAjAFgNwFgBQsGIHQAyAlgHYCOGmWUAzAgExwBCApiQMYAWAtgIYBOAawDOWAN5Y4UuAAd+RAG68ALizjFhygDyllAPjgB9ADZFNlSdNpxjAexIBzOAFESAV24t+KlhuUAKAEpLKQlMaQi4JX4o3mM3NQBeOBhKSOkAM1t+Fl4uOH9dOCJikiNTTWDw9LgwmsileLUwZKI0moBfLBDIqAB2WKb2qS7MDqA=), you get the following:

```
private List<int> _list;

public long EnumerateList()
{
    int num = 0;
    List<int>.Enumerator enumerator = _list.GetEnumerator();
    try
    {
        while (enumerator.MoveNext())
        {
            int current = enumerator.Current;
            num += current;
        }
    }
    finally
    {
        ((IDisposable)enumerator).Dispose();
    }
    return num;
}
```

As you can see, in this example, the `GetEnumerator()` method returns a `List<int>.Enumerator` instance, which exposes a `MoveNext()` method, a `Current` property, and implements `IDisposable`. If we compare that to `EnumerateIEnumerable()` we [get *almost* the same code](https://sharplab.io/#v2:CYLg1APgAgDABFAjAFgNwFgBQsGIHQAyAlgHYCOGmWUAzAgExwBCApiQMYAWAtgIYBOAawDOWAN5Y4UuAAd+RAG68ALi1w0APKWUA+OAH02AV24t+vAEYAbFpUnTacKwHsSAczgBREibMqWSDQAFACU9lISmNLRcEr8sbxWRmoAvHAwlDHSAGbO/Cy8XHBB2nBEZSQGxqbm1ixhUVlwkU0xSklqYGlEmU0AvljhMVAA7AkdvVIDmH1AA):

```
private IEnumerable<int> _enumerable;

public long EnumerateIEnumerable()
{
    int num = 0;
    IEnumerator<int> enumerator = _enumerable.GetEnumerator();
    try
    {
        while (enumerator.MoveNext())
        {
            int current = enumerator.Current;
            num += current;
        }
    }
    finally
    {
        if (enumerator != null)
        {
            enumerator.Dispose();
        }
    }
    return num;
}
```

The main difference in the code above is that the `GetEnumerator()` method returns an `IEnumerator<int>` instance instead of a concrete `List<int>.Enumerator` instance. If we look at the implementation details [of `List<T>`'s enumeration](https://github.com/dotnet/dotnet/blob/b0f34d51fccc69fd334253924abd8d6853fad7aa/src/runtime/src/libraries/System.Private.CoreLib/src/System/Collections/Generic/List.cs#L665) methods, we can see there actually 3 different implementations, but they all ultimately delegate to the `GetEnumerator()` method that returns an `List<T>.Enumerator` instance.

```
public class List<T>
{
    public Enumerator GetEnumerator() => new Enumerator(this);
    IEnumerator<T> IEnumerable<T>.GetEnumerator() => GetEnumerator();
    IEnumerator IEnumerable.GetEnumerator() => ((IEnumerable<T>)this).GetEnumerator();

    public struct Enumerator : IEnumerator<T>, IEnumerator
    {
        // details hidden for brevity
    }
}
```

And importantly, the `List<T>.Enumerator` is defined as a `struct` type.

### [Struct enumerators](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#struct-enumerators)

The `struct` enumerator is the key to the difference in allocation. By returning a mutable `struct` implementation of the `Enumerator` instead of a `class`, the `List<T>.Enumerator` type can be allocated on the stack, avoid any allocation on the heap, and so avoid adding pressure on the garbage collector. That's *as long* as the compiler can call the `GetEnumerator()` method directly…

However, when calling `foreach` on the `IEnumerable` variable, we need to return an `IEnumerator` (or `IEnumerator<T>`) to satisfy the interface. The only way to do that is for the `List<T>.Enumerator` object to [be boxed onto the heap](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/types/boxing-and-unboxing). This is the source of the allocation we saw in the benchmark for the `IEnumerable` variable.

In general, this limitation is all a little unfortunate and kind of annoying. Returning basic interface types like `IEnumerable<T>` or `ICollection<T>` rather than their concrete types is a standard method of encapsulation, which allows for later evolution without disrupting the public API, and is generally, *rightly*, encouraged. It's just a shame that results in allocation. Unless, that is, you're using .NET 10…

### [A .NET 10 caveat: deabstraction](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#a-net-10-caveat-deabstraction)

If I run the same benchmark above on .NET 10, I get some interesting results:

| Method | Runtime | Mean | Error | StdDev | Allocated |
| --- | --- | --- | --- | --- | --- |
| List | .NET 10.0 | 2.895 us | 0.0527 us | 0.0493 us | - |
| IEnumerable | .NET 10.0 | 3.016 us | 0.0590 us | 0.0725 us | - |

*Both* benchmarks are essentially the same. There's no allocation, and the execution time is essentially the same! So what's going on here? the short answer is that .NET 10 [introduced a bunch of techniques](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-10/#deabstraction) to make this sort of pattern faster. There's devertualization, so the runtime can see that it's always a `List<T>` and call the `struct` enumerator, and there's also Object Stack Allocation, where objects which would otherwise be allocated to the heap are actually allocated to the stack if the compiler can prove the object won't "escape". Add to that [*additional* work to fix the `List<T>.Enumerator`](https://devblogs.microsoft.com/dotnet/performance-improvements-in-net-10/#collections), and you get the glorious results above!

Which is all great if you're using .NET 10. Unfortunately, in my work on the Datadog .NET SDK, we have customers that run on all sorts of older versions of .NET (including .NET Framework), and as we are often in the hot path for apps, we need to be as efficient as possible. And all those 40 byte allocations add up!

## [Avoiding `foreach` allocation for known return types](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#avoiding-foreach-allocation-for-known-return-types)

These days, most collection types that are exposed by the BCL or by popular libraries will use the same pattern of a `stack`-based enumerator. But you lose these performance benefits when the collection is exposed as an `IEnumerable` collection.

One way to avoid this regression (if you know what the return type of an API will be) is to simply cast to that type, so the compiler can "find" the better `GetEnumerator()` method:

```
IEnumerable<int> someCollection = SomeApiThatReturnsAList();

// If we know that someCollection always returns List<T>, we can "help" the compiler
if(someCollection is List<int> list)
{
    // The compiler can call `List<T>.GetEnumerator()`, allocate
    // on the stack, and avoid the boxing allocation
    foreach(var value in list)
    {
    }
}
else
{
    // Optionally Keep a fallback case for safety, in case our assumptions are wrong
    // or it changes in the future
    foreach(var value in someCollection)
    {
    }
}
```

It feels a bit clumsy but it works to avoid the allocations, and when you're trying to be efficient, every byte counts!

## [Avoiding `foreach` allocation when you can't reference the return type](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#avoiding-foreach-allocation-when-you-can-t-reference-the-return-type)

The above approach is easy and works well if

1. You know what type is going to be returned by an API. Obviously this may change (that's the whole point of using `IEnumerable` after all!) so you must make sure to handle this scenario.
2. That type is public, so you can reference it.

That second point is often a problem for us in the Datadog SDK, because we instrument many different libraries, and can't reference them at compile time. So if we want to avoid allocation from enumerators, we need to do something else.

Take for example [the `Activity.TagObjects` property](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.activity.tagobjects?view=net-10.0). This API returns an `IEnumerable<KeyValuePair<string, object>>`, but [the concrete type is `TagsLinkedList`](https://github.com/dotnet/dotnet/blob/b0f34d51fccc69fd334253924abd8d6853fad7aa/src/runtime/src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Activity.cs#L109), which is [an internal type](https://github.com/dotnet/dotnet/blob/b0f34d51fccc69fd334253924abd8d6853fad7aa/src/runtime/src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Activity.cs#L1632), with a `struct` enumerator. We can't use the `is` trick above because `TagsLinkedList` isn't public (and [we can't use the `EnumerateTagObjects()` method](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.activity.enumeratetagobjects?view=net-10.0), because that's not available in all runtimes we support). So how can we avoid the allocation?

The answer was to use an approach that we use in various other places: use *Reflection.Emit* capabilities to create a `DynamicMethod` that explicitly uses the struct enumerator.

> As I mentioned at the start of this post, this approach isn't novel, and has been [described](https://www.macrosssoftware.com/2020/07/13/enumerator-performance-surprises/) and [used](https://github.com/open-telemetry/opentelemetry-dotnet/blob/73bff75ef653f81fe6877299435b21131be36dc0/src/OpenTelemetry/Internal/EnumerationHelper.cs#L58) previously by others. I mostly took that prior art and tweaked it for my purposes, so kudos to them for doing the hard work!

### [Designing our *Reflection.Emit* `DynamicMethod`](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#designing-our-reflection-emit-dynamicmethod)

Reflection.Emit refers to the *System.Reflection.Emit* namespace, which contains various methods for creating *new* intermediate language (IL) in your application. IL instructions are the "assembly code" that the compiler outputs when you compile your application. The JIT in the .NET runtime converts these IL instructions into real assembly code when your application runs.

*Reflection.Emit* is primarily used by libraries and frameworks that are either trying to wild things or are trying to eek out performance wherever they can, so it's definitely an "advanced" API. If you haven't used it before, or you find it confusing, don't worry about it!

In the implementation coming below, we're basically going to "manually" construct a method that contains a "lowered" `foreach` loop, but making sure we call the `struct`-based `GetEnumerator()` on the object. Something like this:

```
// This is effectively the method we're going to create
public static void AllocationFreeForEach(
    TagsLinkedList list, // The object to enumerate
     ref SomeState state, // A state object the callback object can use 
      Func<SomeState, KeyValuePair<string, object>, bool> callback) // The callback to execute
{
    // We create a lowered version of this code:
    // foreach(var item in list)
    // {
    //     if (!callback(ref state, item))
    //         break;
    // }
    using (TagsLinkedList.Enumerator enumerator = list.GetEnumerator())
    {
        while (enumerator.MoveNext())
        {
            if (!callback(ref state, enumerator.Current))
                break;
        }
    }
}
```

We have to create the "lowered" version of the code when constructing our Dynamic Method, which means we *also* need to lower the `using` block, so we're actually looking at something more like this instead:

```
public static void AllocationFreeForEach(
    TagsLinkedList list,
     ref SomeState state,
      Func<SomeState, KeyValuePair<string, object>, bool> callback)
{
    TagsLinkedList.Enumerator enumerator = list.GetEnumerator();

    try
    {
        while (enumerator.MoveNext())
        {
            if (!callback(ref state, enumerator.Current))
                break;
        }

    }
    finally
    {
        enumerator.Dispose();
    }
}
```

That covers pretty much what we want to emit, all we need to do now is to generate our `DynamicMethod`.

### [Generating the `DynamicMethod`](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#generating-the-dynamicmethod)

We'll emit a method similar to the code above, but as a generalized version that can be called with many different enumeration types, and with many different item types.

```
internal static class AllocationFreeEnumerator<TEnumerable, TItem, TState>
    where TEnumerable : IEnumerable<TItem>
    where TState : struct
{
    // Use reflection to references to the methods we need to call
    private static readonly MethodInfo GenericGetEnumeratorMethod = typeof(IEnumerable<TItem>).GetMethod("GetEnumerator")!;
    private static readonly MethodInfo GenericCurrentGetMethod = typeof(IEnumerator<TItem>).GetProperty("Current")!.GetMethod!;
    private static readonly MethodInfo MoveNextMethod = typeof(IEnumerator).GetMethod("MoveNext")!;
    private static readonly MethodInfo DisposeMethod = typeof(IDisposable).GetMethod("Dispose")!;

    // This is the method we're going to invoke
    public delegate void AllocationFreeForEachDelegate(TEnumerable instance, ref TState state, CallbackDelegate itemCallback);

    // This is the callback which is invoked for each item
    public delegate bool CallbackDelegate(ref TState state, TItem item);

    // Build an allocation-free enumerator
    public static AllocationFreeForEachDelegate BuildAllocationFreeForEachDelegate(Type enumerableType)
    {
        var itemCallbackType = typeof(CallbackDelegate);

        // Try to find a non-interface returning GetEnumerator() method
        var getEnumeratorMethod = ResolveGetEnumeratorMethodForType(enumerableType);
        if (getEnumeratorMethod == null)
        {
            // We couldn't find a non-interface GetEnumerator() method, so
            // fallback to allocation mode and use IEnumerable<TItem>.GetEnumerator
            getEnumeratorMethod = GenericGetEnumeratorMethod;
        }

        var enumeratorType = getEnumeratorMethod.ReturnType;

        // build the Dynamic method (our AllocationFreeForEachDelegate)
        var dynamicMethod = new DynamicMethod(
            "AllocationFreeForEach",
            null,
            [typeof(TEnumerable), typeof(TState).MakeByRefType(), itemCallbackType],
            typeof(AllocationFreeForEachDelegate).Module,
            skipVisibility: true);

        var generator = dynamicMethod.GetILGenerator();

        // TagsLinkedList.Enumerator enumerator
        generator.DeclareLocal(enumeratorType);

        var beginLoopLabel = generator.DefineLabel();
        var processCurrentLabel = generator.DefineLabel();
        var returnLabel = generator.DefineLabel();
        var breakLoopLabel = generator.DefineLabel();

        // enumerator = arg0.GetEnumerator();
        generator.Emit(OpCodes.Ldarg_0);
        generator.Emit(OpCodes.Callvirt, getEnumeratorMethod);
        generator.Emit(OpCodes.Stloc_0);

        // try
        generator.BeginExceptionBlock();
        {
            // while()
            generator.Emit(OpCodes.Br_S, beginLoopLabel);

            generator.MarkLabel(processCurrentLabel);

            // bool shouldContinue = callback(arg1, enumerator.Current);
            generator.Emit(OpCodes.Ldarg_2);
            generator.Emit(OpCodes.Ldarg_1);
            generator.Emit(OpCodes.Ldloca_S, 0);
            generator.Emit(OpCodes.Constrained, enumeratorType);
            generator.Emit(OpCodes.Callvirt, GenericCurrentGetMethod);

            generator.Emit(OpCodes.Callvirt, itemCallbackType.GetMethod("Invoke")!);

            // if (!continue)
            //     break;
            generator.Emit(OpCodes.Brtrue_S, beginLoopLabel);
            generator.Emit(OpCodes.Leave_S, returnLabel);

            // if (enumerator.MoveNext())
            //    goto: start of while loop
            generator.MarkLabel(beginLoopLabel);
            generator.Emit(OpCodes.Ldloca_S, 0);
            generator.Emit(OpCodes.Constrained, enumeratorType);
            generator.Emit(OpCodes.Callvirt, MoveNextMethod);
            generator.Emit(OpCodes.Brtrue_S, processCurrentLabel);

            // close while loop
            generator.MarkLabel(breakLoopLabel);
            generator.Emit(OpCodes.Leave_S, returnLabel);
        }

        // finally
        generator.BeginFinallyBlock();
        {
            // enumerator.Dispose();
            if (typeof(IDisposable).IsAssignableFrom(enumeratorType))
            {
                generator.Emit(OpCodes.Ldloca_S, 0);
                generator.Emit(OpCodes.Constrained, enumeratorType);
                generator.Emit(OpCodes.Callvirt, DisposeMethod);
            }
        }

        generator.EndExceptionBlock();

        generator.MarkLabel(returnLabel);

        // return
        generator.Emit(OpCodes.Ret);

        return (AllocationFreeForEachDelegate)dynamicMethod.CreateDelegate(typeof(AllocationFreeForEachDelegate));
    }

    private static MethodInfo? ResolveGetEnumeratorMethodForType(Type type)
    {
        // Look for a `GetEnumerator()` method that _doesn't_ return an
        // interface. This doesn't _guarantee_ a struct-based enumerator,
        // but it's the standard pattern so catches most cases
        var methods = type.GetMethods(BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic);

        foreach (var method in methods)
        {
            if (method.Name == "GetEnumerator" && !method.ReturnType.IsInterface)
            {
                return method;
            }
        }

        return null;
    }
}
```

There's a lot of code there, and if you struggle to follow IL then it will no doubt be confusing 😅 The only small piece of advice I have if you're trying to *write* this code, is to use an IL generator to show the IL that you *should* be trying to generate. I tend to use the one built into Rider when I'm working on this stuff:

![The output of Rider's IL window](https://andrewlock.net/content/images/2026/enumeration_il.png)

Now that we have this dynamic method generator, we can put it to the test and check the results.

### [Benchmarking the `DynamicMethod` on `List<T>`](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#benchmarking-the-dynamicmethod-on-listt)

To test it out, I initially updated the benchmark to test 3 different scenarios

* A `List<int>` saved in a `List<int>` variable
* A `List<int>` saved in an `IEnumerable<int>` variable
* A `List<int>` saved in an `IEnumerable<int>` variable, using the `DynamicMethod` above

```
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using BenchmarkDotNet.Attributes;

[MemoryDiagnoser]
public class Benchmarks
{
    private List<int>? _list;
    private IEnumerable<int>? _listEnumerable;
    private AllocationFreeEnumerator<IEnumerable<int>, int, long>.AllocationFreeForEachDelegate _listEnumerator;

    [GlobalSetup]
    public void GlobalSetup()
    {
        _list = Enumerable.Range(0, 10_000).ToList();
        _listEnumerable = _list;
        _listEnumerator = AllocationFreeEnumerator<IEnumerable<int>, int, long>.BuildAllocationFreeForEachDelegate(_list.GetType());
    }

    [Benchmark]
    public long List()
    {
        long value = 0;
        foreach (int i in _list!)
        {
            value += i;
        }

        return value;
    }

    [Benchmark]
    public long IEnumerable()
    {
        long value = 0;
        foreach (int i in _listEnumerable!)
        {
            value += i;
        }

        return value;
    }

    [Benchmark]
    public long IEnumerableDynamicMethod()
    {
        long value = 0;
        _listEnumerator(_list!, ref value, static (ref state, i) =>
        {
            state += i;
            return true;
        });

        return value;
    }
}
```

The results from running this against .NET Framework 4.8 and .NET 9 are a bit of a mixed bag:

| Method | Runtime | Mean | Error | StdDev | Allocated |
| --- | --- | --- | --- | --- | --- |
| List | .NET 9.0 | 3.120 us | 0.0573 us | 0.0536 us | - |
| IEnumerable | .NET 9.0 | 7.554 us | 0.0935 us | 0.0828 us | 40 B |
| IEnumerableDynamicMethod | .NET 9.0 | 15.436 us | 0.1631 us | 0.1446 us | - |
|  |  |  |  |  |  |
| List | .NET Framework 4.8 | 7.789 us | 0.0560 us | 0.0496 us | - |
| IEnumerable | .NET Framework 4.8 | 23.181 us | 0.1515 us | 0.1417 us | 40 B |
| IEnumerableDynamicMethod | .NET Framework 4.8 | 14.894 us | 0.1978 us | 0.1754 us | - |

For .NET Framework, we're clearly onto a winner. We see reduced execution time *and* we're now allocation-free, so that's great.

For .NET 9, we're now allocation free, but execution time has doubled, which is unfortunate, but likely comes from the fact that `List<T>` has seen a huge number of performance attention over the years, and we're likely stomping over that somewhat with our DynamicMethod. Whether the performance hit is worth it will likely come down to what the limiting factor is for you here. Bear in mind that the allocation cost is fixed regardless of the size of the list, whereas execution time for this case obviously scales approximately linearly with list size.

For .NET 10, somewhat unsurprisingly, our `DynamicMethod` approach comes out worse than just using `IEnumerable<int>`:

| Method | Runtime | Mean | Error | StdDev | Allocated |
| --- | --- | --- | --- | --- | --- |
| List | .NET 10.0 | 3.105 us | 0.0442 us | 0.0413 us | - |
| IEnumerable | .NET 10.0 | 3.162 us | 0.0365 us | 0.0341 us | - |
| IEnumerableDynamicMethod | .NET 10.0 | 15.448 us | 0.2034 us | 0.1903 us | - |

This is what we'd expect, given all the performance improvements over the years, and the attention that's been given to `List<T>`. Given that enumerating `IEnumerable<T>` is *already* allocation free in .NET 10, there's no good reason to use it in this case.

### [Benchmarking the `DynamicMethod` with a custom `IEnumerable<T>`](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#benchmarking-the-dynamicmethod-with-a-custom-ienumerablet)

My initial reason for looking into the `DynamicMethod` approach was for handling types that *aren't* built into the BCL, so I took a look at benchmarking a custom `IEnumerable<T>` implementation. The following linked list implementation is *super* basic, and is a heavily stripped-down version of an implementation [used internally by `Activity`](https://github.com/dotnet/dotnet/blob/b0f34d51fccc69fd334253924abd8d6853fad7aa/src/runtime/src/libraries/System.Diagnostics.DiagnosticSource/src/System/Diagnostics/Activity.cs#L1632). These details aren't really important, I just include it below for completeness:

```
internal sealed class CustomLinkedList<T> : IEnumerable<T>
{
    private Node<T>? _first;
    private Node<T>? _last;

    public CustomLinkedList()
    {
    }

    public CustomLinkedList(T firstValue) => _last = _first = new Node<T>(firstValue);

    public CustomLinkedList(IEnumerator<T> e)
    {
        _last = _first = new Node<T>(e.Current);

        while (e.MoveNext())
        {
            _last.Next = new Node<T>(e.Current);
            _last = _last.Next;
        }
    }

    public Node<T>? First => _first;

    public void Add(T value)
    {
        Node<T> newNode = new Node<T>(value);
        if (_first is null)
        {
            _first = _last = newNode;
            return;
        }

        _last!.Next = newNode;
        _last = newNode;
    }

    public Enumerator<T> GetEnumerator() => new Enumerator<T>(_first);
    IEnumerator<T> IEnumerable<T>.GetEnumerator() => GetEnumerator();
    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();


    internal struct Enumerator<T> : IEnumerator<T>
    {
        private static readonly Node<T> s_Empty = new Node<T>(default!);

        private Node<T>? _nextNode;
        private Node<T> _currentNode;

        public Enumerator(Node<T>? head)
        {
            _nextNode = head;
            _currentNode = s_Empty;
        }

        public T Current => _currentNode.Value;

        object? IEnumerator.Current => Current;

        public bool MoveNext()
        {
            if (_nextNode == null)
            {
                _currentNode = s_Empty;
                return false;
            }

            _currentNode = _nextNode;
            _nextNode = _nextNode.Next;
            return true;
        }

        public void Reset() => throw new Exception();

        public void Dispose()
        {
        }
    }
    
    internal sealed partial class Node<T>
    {
        public Node(T value) => Value = value;
        public T Value;
        public Node<T>? Next;
    }
}
```

I then updated the benchmark to run the same set of tests with the `CustomLinkedList` implementation instead:

```
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using BenchmarkDotNet.Attributes;

[MemoryDiagnoser]
public class Benchmarks
{
    private CustomLinkedList<int>? _linkedList;
    private IEnumerable<int>? _linkedListEnumerable;
    private AllocationFreeEnumerator<IEnumerable<int>, int, long>.AllocationFreeForEachDelegate _linkedListEnumerator;

    [GlobalSetup]
    public void GlobalSetup()
    {
        _linkedList = new();
        foreach (var i in Enumerable.Range(0, 10_000))
        {
            _linkedList.Add(i);
        }

        _linkedListEnumerable = _linkedList;
        _linkedListEnumerator =
            AllocationFreeEnumerator<IEnumerable<int>, int, long>.BuildAllocationFreeForEachDelegate(
                _linkedList.GetType());
    }

    [Benchmark]
    public long LinkedList()
    {
        long value = 0;
        foreach (int i in _linkedList!)
        {
            value += i;
        }

        return value;
    }

    [Benchmark]
    public long IEnumerableLinkedList()
    {
        long value = 0;
        foreach (int i in _linkedListEnumerable!)
        {
            value += i;
        }

        return value;
    }

    [Benchmark]
    public long IEnumerableLinkedListDynamicMethod()
    {
        long value = 0;
        _linkedListEnumerator(_linkedList!, ref value, static (ref state, i) =>
        {
            state += i;
            return true;
        });

        return value;
    }
}
```

The results from these `CustomLinkedList<T>` benchmarks are *pretty* similar to the ones for `List<T>`, but with one main caveat: the `DynamicMethod` approach is now faster on .NET 9 *as well* as not allocating, so it becomes a clear winner in this case. The speed up for .NET Framework is also quite substantial:

| Method | Runtime | Mean | Error | StdDev | Allocated |
| --- | --- | --- | --- | --- | --- |
| LinkedList | .NET 9.0 | 7.844 us | 0.1340 us | 0.1254 us | - |
| IEnumerableLinkedList | .NET 9.0 | 18.892 us | 0.3430 us | 0.3209 us | 32 B |
| IEnumerableLinkedListDynamicMethod | .NET 9.0 | 15.148 us | 0.2613 us | 0.2445 us | - |
|  |  |  |  |  |  |
| LinkedList | .NET Framework 4.8 | 7.914 us | 0.1295 us | 0.1212 us | - |
| IEnumerableLinkedList | .NET Framework 4.8 | 42.272 us | 0.8344 us | 0.9933 us | 32 B |
| IEnumerableLinkedListDynamicMethod | .NET Framework 4.8 | 13.480 us | 0.2430 us | 0.2273 us | - |

As before, with .NET 10, the results for the `DynamicMethod` are worse than the plain `IEnumerable<<T>`. This is actually really quite impressive—.NET 10 manages to treat the `LinkedList` and `IEnumerableLinkedList` benchmarks as essentially indistinguishable. Very cool 😎

| Method | Runtime | Mean | Error | StdDev | Allocated |
| --- | --- | --- | --- | --- | --- |
| LinkedList | .NET 10.0 | 7.944 us | 0.1570 us | 0.1542 us | - |
| IEnumerableLinkedList | .NET 10.0 | 7.798 us | 0.0745 us | 0.0622 us | - |
| IEnumerableLinkedListDynamicMethod | .NET 10.0 | 14.990 us | 0.2606 us | 0.2559 us | - |

So there you have it—a way to do allocation free enumeration of collection types. Obviously the question of whether you *should* do this is entirely context-dependent. If the enumeration is in a hot path, you're *not* on .NET 10, and these allocations are showing up in your profiling, then, well, *maybe* you should consider it 😅

## [Summary](https://andrewlock.net/making-foreach-on-an-ienumerable-allocation-free-using-reflection-and-dynamic-methods#summary)

In the first part of this post I provide some background on how and when a `foreach` loop might cause allocations. I create a simple benchmark to demonstrate the problem, show the "lowered" C#, and describe that the allocation comes from boxing a `struct` enumerator.

In the second part of the post, I describe how you can avoid this allocation, for scenarios where you *can't* simply cast to a known type, by creating a `DynamicMethod` using *Reflection.Emit*. This is a pretty advanced technique, but it shows how you can completely remove the allocations from enumeration.

Finally, I showed how this approach performs in benchmarks. If you're using .NET 10, then you have no need for the `DynamicMethod` and don't need to worry at all 😀 On earlier runtimes, including .NET Framework, the `DynamicMethod` approach eliminates allocations, and in many cases improves execution time, particularly for "custom" collection types.

Whether you should use this approach is very context dependent. In most scenarios, allocating 40 bytes is not a big deal. But if it *is* a problem for you, now you have a tool in your toolbelt!
