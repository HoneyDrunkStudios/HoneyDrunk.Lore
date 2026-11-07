---
"source": "https://andrewlock.net/understanding-lazy-thread-safety-modes/"
"title": "Understanding Lazy<T> thread safety modes"
"author": "Andrew Lock"
"date_published": "2026-11-03"
"date_clipped": "2026-11-07"
"category": ".NET Ecosystem"
"source_type": "rss"
---

# Understanding Lazy<T> thread safety modes

Source: https://andrewlock.net/understanding-lazy-thread-safety-modes/

In this post I look at the various thread-safety modes available for the venerable `Lazy<T>` type. This type has been around for a long time, but I recently saw some people (understandably) confused about the interactions between `LazyThreadSafetyMode` and exceptions, so this post aims to demonstrate how they work.

## [What is `Lazy<T>` For?](https://andrewlock.net/understanding-lazy-thread-safety-modes/#what-is-lazyt-for-)

[The `Lazy<T>` type](https://learn.microsoft.com/en-us/dotnet/api/system.lazy-1) has been around since .NET Framework 4.0 (and .NET Core 1.0). It provides is a way to describe *how* an object should be created, while deferring the actual creation to later. In other words, the object is *lazily* initialized. In one of it's simplest form, it might look like this:

```
// You provide a function that should be invoked when the object is required.
Lazy<object> lazy = new(Create);

// The `Create` factory method is not invoked (and the object is not created) until 
// you access the `Value` property on the Lazy<T>
var obj = lazy.Value;

// A factory method
object Create()
{
    // This would normally do something expensive or with side effects
    return new object();
}
```

> There are various other forms, not all of which use a factory method, but I have found the factory mode to be the most commonly used, so it's the only version I look at in this post.

`Lazy<T>` is useful wherever you want to delay or control the creation of the target object, `T`. This is often because `T` is expensive to create, and so you don't want to create it until you need it. `Lazy<T>` also provides a way to tune the behaviour when *multiple* threads try to access the `Value` property. This behaviour is controlled by the `LazyThreadSafetyMode` in the constructor.

> In addition to overloads that take `LazyThreadSafetyMode`, there are also overloads that take an `isThreadSafe` boolean value. I won't be looking at those overloads.

## [Choosing a `LazyThreadSafetyMode`](https://andrewlock.net/understanding-lazy-thread-safety-modes/#choosing-a-lazythreadsafetymode)

There are three different thread-safety modes you can use with `Lazy<T>`. In brief, these are:

- `None`. The `Lazy<T>` object provides no thread-safety, and is *not* safe to be called from more than one thread.
- `PublicationOnly`. Multiple threads can run the factory method at once, but "publishing" the final `Value` is thread-safe, so only one of the threads can "win".
- `ExecutionAndPublication`. Only one thread will run the factory, and publish it's value for all the other threads to see.

We'll look at each of these cases in more detail below.

### [Use `None` when you have a single thread](https://andrewlock.net/understanding-lazy-thread-safety-modes/#use-none-when-you-have-a-single-thread)

The `None` case is a simple one because it just avoids the whole threading/concurrency issue entirely. It is *not* safe to call a `Lazy<T>` that was created with `LazyThreadSafetyMode.None` from multiple threads, so if there's any chance of that in your application `None` is not for you! Attempting to do so will likely lead to `InvalidOperationException`s being thrown.

Thanks to this limitation, `LazyThreadSafetyMode.None` only really makes sense as a way to delay running a function until later and caching the result. And in that scenario, a simple use of `??=` *might* be conceptually simpler, depending on your code (or use `LazyInitializer`, [as I describe later](https://andrewlock.net/understanding-lazy-thread-safety-modes/#alternative-approaches-with-lazyinitializer)).

For example, the following are somewhat equivalent:

```
// The Lazy is provided the Create factory method
private readonly Lazy<object> _lazy = new(Create, LazyThreadSafetyMode.None);

// To do something with the lazy you always need to call .Value
// and the value is created the first time it's accessed
public void SomeMethod()
{
    var myValue = _lazy.Value;
    // .. do something with value
}
```

and

```
// The field is nullable, not readonly, and not initialized
private object? _value;

// Make sure that you initialize the value the first time it's accessed
// Using a property ensures the value is always initialized the first time it's used.
private object Value => _value ??= Create();

public void SomeMethod()
{
    var myValue = Value;
    // .. do something with value
}
```

Given we've already said this code is single-threaded, the `Lazy<T>` with `None` doesn't add a lot of extra value over a simple nullable field, though arguably it does better capture intent.

### [Racing for completion with `PublicationOnly`](https://andrewlock.net/understanding-lazy-thread-safety-modes/#racing-for-completion-with-publicationonly)

We'll now move on to looking at modes which *are* intended to be thread-safe and accessed concurrently. When you create a `Lazy<T>` with `LazyThreadSafetyMode.PublicationOnly`, and then multiple threads try to access the `Value` property:

- Multiple threads start running the factory method independently.
- Whichever thread finishes first "wins", and its return value is "published" to the `Value` property.
- When the other threads finish running the factory methods, their values are discarded, and all of the threads instead receive the previously published value.
- Any threads that try to access `Value` *after* the value is published receive the published value immediately, without running the factory function.

The following diagrams show an example of this process. *All* the threads that call `Value` before a value is published run the factory method concurrently:

![Three threads run the value factory concurrently](https://andrewlock.net/content/images/2026/lazy-publication-only-01-concurrent.svg)

Whichever thread finishes first sets the `Lazy<T>.Value`:

![The first completed result is published](https://andrewlock.net/content/images/2026/lazy-publication-only-02-first-published.svg)

When the other threads finish, their values are ignored, and they all get the same published value.

![Other results are discarded](https://andrewlock.net/content/images/2026/lazy-publication-only-03-discarded.svg)

So all the threads see the same value, even though the factory method may run more than once, and generate more than one value.

### [Once-only initialization with `ExecutionAndPublication`](https://andrewlock.net/understanding-lazy-thread-safety-modes/#once-only-initialization-with-executionandpublication)

The other thread-safe mode is `ExecutionAndPublication`. When you create a `Lazy<T>` with `LazyThreadSafetyMode.ExecutionAndPublication`, and then multiple threads try to access the `Value` property:

- Only the first thread to try to access `Value` runs the factory method.
- All the other threads are blocked waiting for the first thread to finish.
- Once the first thread finishes, it publishes the value, and returns it to the other threads.

The following diagrams show an example of this process. Only the *first* thread that calls `Value` before a value is published runs the factory method, all others block waiting:

![Thread A runs the factory once and publishes the value. Threads B and C wait.](https://andrewlock.net/content/images/2026/lazy-execution-publication-01-single-run.svg)

Once the thread finishes, it's passed to all the other blocked threads

![Thread A completes the value factory once, publishes the value, and Threads B and C receive it.](https://andrewlock.net/content/images/2026/lazy-execution-publication-02-published.svg)

The factory only runs once, and a single value is published.

In *most* cases, in my experience, the run-once behaviour of `ExecutionAndPublication` is often what you want from `Lazy<T>` but that's not *always* the case.

### [Choosing between `PublicationOnly` and `ExecutionAndPublication`](https://andrewlock.net/understanding-lazy-thread-safety-modes/#choosing-between-publicationonly-and-executionandpublication)

The big advantage of `ExecutionAndPublication` is that it only runs the factory *once*. If you are using `Lazy<T>` as a way to avoid duplicating expensive initialization, or to gate access to some resources, then `ExecutionAndPublication` achieves this where `PublicationOnly` does not. `ExecutionAndPublication` also avoids you creating multiple return objects and then discarding some of them, so if the created object is large, `ExecutionAndPublication` can avoid the extra allocations.

There are *some* cases, however, where `PublicationOnly` *might* be faster due to avoiding the extra synchronisation mechanisms that are required by `ExecutionAndPublication`. If running the factory method (and creating the return object) is cheap, then using `PublicationOnly` and running multiple instances of the factory can sometimes be cheaper than serializing with a lock. For example, if

- There is heavy concurrent access during initialisation.
- The factory executes quickly.
- Running the factory more than once is safe.
- Duplicate allocations are cheap.
- Lock contention is significant.

Then `PublicationOnly` might be a better choice than `ExecutionAndPublication`.

There's one other critical difference between how `PublicationOnly` and `ExecutionAndPublication` work, and that's how they handle exceptions.

## [Understanding exceptions with `LazyThreadSafetyMode`](https://andrewlock.net/understanding-lazy-thread-safety-modes/#understanding-exceptions-with-lazythreadsafetymode)

`Lazy<T>` has two different possible behaviours when it comes to a factory method that throws exceptions

- **Cached**: in this case a factory throwing an exception is "cached" the same way a "success" result is; subsequent calls to `Value` throw the exception again each time.
- **Uncached**: in this case, exceptions are thrown to the caller, but a subsequent/concurrent call will *not* automatically get the same exception thrown.

Whether exceptions are cached or not depends entirely on the `LazyThreadSafetyMode`:

| Mode | Exceptions cached? |
| --- | --- |
| None | Yes |
| PublicationOnly | No |
| ExecutionAndPublication | Yes |

As you can see, `PublicationOnly` is the *only* scenario where exceptions are *not* cached. The following exceptions demonstrate that more clearly.

### [`ExecutionAndPublication` caches exceptions](https://andrewlock.net/understanding-lazy-thread-safety-modes/#executionandpublication-caches-exceptions)

As you've already seen, `ExecutionAndPublication` only runs the factory method on a single thread. If that factory throws an exception, the exception is cached:

![Thread A runs the value factory, which throws an exception that is cached while Threads B and C wait](https://andrewlock.net/content/images/2026/lazy-exceptions-execution-publication-01-cached.svg)

All concurrent threads, *and* any subsequent callers of `Value` all have the cached exception thrown:

![Threads A, B, and C each receive the exception from cache](https://andrewlock.net/content/images/2026/lazy-exceptions-execution-publication-02-from-cache.svg)

Every caller sees the same `Exception` instance in each case. At this point, the `Lazy<T>` is effectively "broken"; it will never return a "real" value. The `None` case works the same way (it just doesn't support concurrent access).

### [`PublicationOnly` does not cache exceptions](https://andrewlock.net/understanding-lazy-thread-safety-modes/#publicationonly-does-not-cache-exceptions)

For `PublicationOnly`, when a value is not yet published to `Value`, the factory method runs on multiple threads. If the factory method for a given thread, say thread `A`, throws an exception, then *that* thread will see the exception, but it does not propagate to other threads, and it is *not* cached:

![Thread A encounters an exception while Threads B and C create result values](https://andrewlock.net/content/images/2026/lazy-exceptions-publication-only-01-concurrent.svg)

Any of the threads that throw an exception from their factory methods will bubble up that exception, The first thread that *successfully* executes the factory publishes its value

![Thread B creates the published value while exceptions from Threads A and C are ignored](https://andrewlock.net/content/images/2026/lazy-exceptions-publication-only-02-first-success.svg)

Any threads that are *currently* running, and which subsequently complete after a value has been published will have their result discarded and replaced with the published value. Any of the currently running threads that throw an exception will *still* see that exception, even after the successful results is published; exceptions are not swallowed

![An exception that is still thrown and an ignored result is discarded while the published value is used](https://andrewlock.net/content/images/2026/lazy-exceptions-publication-only-03-discarded.svg)

Once a value has been successfully published, then any subsequent threads that call `Value` will always see this value; they won't run the factory method, and so won't throw.

## [Changes (maybe) coming in .NET 12](https://andrewlock.net/understanding-lazy-thread-safety-modes/#changes-maybe-coming-in-net-12)

The fact that exception caching is tied to the thread-safety behaviour, despite being orthogonal behaviour, is something of a wart on the API.

There has been [a proposal raised](https://github.com/dotnet/runtime/issues/27421) on the .NET runtime for 8 years to add a *new* mode that allows an `ExecutionAndPublication` mode that does *not* cache exceptions. This was subsequently updated to simply be a `bool cacheExceptions` flag, so that you can have the full range of behaviours.

The good news is that this proposal [was recently approved](https://github.com/dotnet/runtime/issues/27421#issuecomment-6021921640).🎉 It's not implemented yet, but hopefully in .NET 12 you'll be able to disconnect these two aspects so that you can, for example, use `ExecutionAndPublication` *without* having exceptions cached.

## [Alternative approaches with `LazyInitializer`](https://andrewlock.net/understanding-lazy-thread-safety-modes/#alternative-approaches-with-lazyinitializer)

This post is primarily about `Lazy<T>`, but there's another approach you can use that gives you behaviour *similar* to the `ExecutionAndPublication` mode, which doesn't require allocating a `Lazy<T>` object at all, `LazyInitializer.EnsureInitialized<T>()`.

There are [several ways to use `LazyInitializer`](https://learn.microsoft.com/en-us/dotnet/api/system.threading.lazyinitializer?view=net-10.0&utm_source=chatgpt.com), but the example below shows how you can get either `PublicationOnly` or `ExecutionAndPublication`-like behaviour, depending on what you want, *without* a dedicated `Lazy<T>` object.

The `PublicationOnly` version looks like this:

```
// The field that will be lazy-initiatized
private object? _value;

// LazyInitializer ensures the ref field is initialized if it 
// hasn't been already, and is then returned. This overload 
// works similarly to PublicationOnly, in that threads race to
// create and publish the value.
var value = LazyInitializer.EnsureInitialized(ref _value, Create);
```

while the `ExecutionAndPublication` version takes an additional field as a lock:

```
// The field that will be lazy-initiatized
private object? _value;
// The value to use as a lock
private object? _lock;

// LazyInitializer ensures the ref field is initialized if it hasn't 
// been already using the _lock (initializing it first) to ensure the
// factory only runs once, and then returns the value. This overload 
// works similarly to ExecutionAndPublication, in that the Create 
// factory only ever runs once.
var value = LazyInitializer.EnsureInitialized(ref _value, ref _synclock, Create);
```

One big difference compared to the `Lazy<T>` equivalent is that neither of these approaches catch or cache exceptions.

Whether you should reach for `Lazy<T>` or `LazyInitializer` depends on what you're trying to achieve. If you want to pass lazily-initialized values around, then `Lazy<T>` is the obvious choice. On the other hand, using `LazyInitializer` can potentially avoid an additional object allocation, and in the case where you just need a simple field initialization, may be simpler.

## [Summary](https://andrewlock.net/understanding-lazy-thread-safety-modes/#summary)

In this post, I described the different thread-safety modes of the `Lazy<T>` type. `None` is not thread-safe, so must not be used where there are multiple threads. With `PublicationOnly`, multiple threads "race" to create the value, but they all see the result from whichever thread wins. With `ExecutionAndPublication`, only one thread runs the factory method, and then all threads see the value. For `None` and `ExecutionAndPublication`, any exceptions are cached, and will be thrown on subsequent accesses. For `PublicationOnly`, exceptions are not cached.
