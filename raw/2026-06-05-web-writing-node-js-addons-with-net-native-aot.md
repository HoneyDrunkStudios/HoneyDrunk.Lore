---
source: "https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/"
title: "Writing Node.js addons with .NET Native AOT"
author: "Drew Noakes"
date_published: "2026-04-20"
date_clipped: "2026-06-05"
category: ".NET Ecosystem"
source_type: "web"
---

# Writing Node.js addons with .NET Native AOT

Source: https://devblogs.microsoft.com/dotnet/writing-nodejs-addons-with-dotnet-native-aot/

[C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit) is a VS Code extension. Like all VS Code extensions, its front end is TypeScript running in Node.js. For certain platform-specific tasks, such as reading the Windows Registry, we’ve historically used native Node.js addons written in C++, which are compiled via [node-gyp](https://github.com/nodejs/node-gyp) during installation to the developer’s workspace.

This works, but it comes with overhead. Using node-gyp to build these particular packages requires an old version of Python to be installed on every developer’s machine. For a team that works on .NET tooling, this requirement added complexity and friction. New contributors had to set up tools they’d never touch directly, and CI pipelines needed to provision and maintain them, which slowed down builds and added yet another set of dependencies to keep up to date over time.

The C# Dev Kit team already has the .NET SDK installed, so why not use C# and Native AOT to streamline our engineering systems?

## How Node.js addons work

A Node.js native addon is a shared library (`.dll`

on Windows, `.so`

on Linux, `.dylib`

on macOS) that exports a specific entry point. When Node.js loads such a library, it calls the function `napi_register_module_v1`

. The addon registers any functions it provides, and from that point on, JavaScript treats it like any other module.

The interface that makes this possible is [N-API](https://nodejs.org/api/n-api.html) (also called Node-API) – a stable, ABI-compatible C API for building addons. N-API doesn’t care what language produced the shared library, only that it exports the right symbols and calls the right functions. This makes Native AOT a viable option because it can produce shared libraries with arbitrary native entry points, which is all N-API needs.

Throughout the rest of this post, let’s look at the key parts of a small Native AOT Node.js addon that can read a string value from the registry. To keep things simple, we’ll put all the code in one class, though you could easily factor things out to be reusable.

## The project file

The project file is minimal:

```
<Project Sdk="Microsoft.NET.Sdk">
<PropertyGroup>
<TargetFramework>net10.0</TargetFramework>
<PublishAot>true</PublishAot>
<AllowUnsafeBlocks>true</AllowUnsafeBlocks>
</PropertyGroup>
</Project>
```

[ PublishAot](https://learn.microsoft.com/dotnet/core/deploying/native-aot/) tells the SDK to produce a shared library when the project is published.

`AllowUnsafeBlocks`

is needed because the N-API interop involves function pointers and fixed buffers.## The module entry point

Node.js expects the shared library to export `napi_register_module_v1`

. In C#, we can do this with [ [UnmanagedCallersOnly]](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.unmanagedcallersonlyattribute):

```
public static unsafe partial class RegistryAddon
{
[UnmanagedCallersOnly(
EntryPoint = "napi_register_module_v1",
CallConvs = [typeof(CallConvCdecl)])]
public static nint Init(nint env, nint exports)
{
Initialize();
RegisterFunction(
env,
exports,
"readStringValue"u8,
&ReadStringValue);
// Register additional functions...
return exports;
}
}
```

A few C# features are doing work here. [ nint](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/nint-nuint) is a native-sized integer — the managed equivalent of

`intptr_t`

– used to pass around N-API handles. The [produces a](https://learn.microsoft.com/dotnet/csharp/language-reference/builtin-types/reference-types#utf-8-string-literals)

`u8`

suffix`ReadOnlySpan<byte>`

containing a UTF-8 string literal, which we pass directly to N-API without any encoding or allocation. And `[UnmanagedCallersOnly]`

tells the AOT compiler to export the method with the specified entry point name and calling convention, making it callable from native code.Each call to `RegisterFunction`

attaches a C# function pointer to a named property on the JavaScript `exports`

object, so that calling `addon.readStringValue(...)`

in JavaScript invokes the corresponding C# method directly, in-process.

## Calling N-API from .NET

N-API functions are exported by `node.exe`

itself, so rather than linking against a separate library, we need to resolve them against the host process. We declare our P/Invoke methods using [ [LibraryImport]](https://learn.microsoft.com/dotnet/standard/native-interop/pinvoke-source-generation) with

`"node"`

as the library name, and then register a custom resolver via [that redirects to the host process at runtime:](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.nativelibrary.setdllimportresolver)

`NativeLibrary.SetDllImportResolver`

```
private static void Initialize()
{
NativeLibrary.SetDllImportResolver(
System.Reflection.Assembly.GetExecutingAssembly(),
ResolveDllImport);
static nint ResolveDllImport(
string libraryName,
Assembly assembly,
DllImportSearchPath? searchPath)
{
if (libraryName is not "node")
return 0;
return NativeLibrary.GetMainProgramHandle();
}
}
```

With this resolver in place, the runtime knows to look up all `"node"`

imports from the host process, and the N-API P/Invoke declarations work without any additional configuration:

```
private static partial class NativeMethods
{
[LibraryImport("node", EntryPoint = "napi_create_string_utf8")]
internal static partial Status CreateStringUtf8(
nint env, ReadOnlySpan<byte> str, nuint length, out nint result);
[LibraryImport("node", EntryPoint = "napi_create_function")]
internal static unsafe partial Status CreateFunction(
nint env, ReadOnlySpan<byte> utf8name, nuint length,
delegate* unmanaged[Cdecl]<nint, nint, nint> cb,
nint data, out nint result);
[LibraryImport("node", EntryPoint = "napi_get_cb_info")]
internal static unsafe partial Status GetCallbackInfo(
nint env, nint cbinfo, ref nuint argc,
Span<nint> argv, nint* thisArg, nint* data);
// ... other N-API functions as needed
}
```

For each registered function we must register a native function as a named property on the exports object:

```
private static unsafe void RegisterFunction(
nint env, nint exports, ReadOnlySpan<byte> name,
delegate* unmanaged[Cdecl]<nint, nint, nint> callback)
{
NativeMethods.CreateFunction(env, name, (nuint)name.Length, callback, 0, out nint fn);
NativeMethods.SetNamedProperty(env, exports, name, fn);
}
```

The source-generated `[LibraryImport]`

handles the marshalling. `ReadOnlySpan<byte>`

maps cleanly to `const char*`

, function pointers are passed through directly, and the generated code is trimming-compatible out of the box.

## Marshalling strings

Most of the interop work comes down to moving strings between JavaScript and .NET. N-API uses UTF-8, so the conversion is straightforward, though it does require a buffer. Here’s a helper that reads a string argument passed from JavaScript:

```
private static unsafe string? GetStringArg(nint env, nint cbinfo, int index)
{
nuint argc = (nuint)(index + 1);
Span<nint> argv = stackalloc nint[index + 1];
NativeMethods.GetCallbackInfo(env, cbinfo, ref argc, argv, null, null);
if ((int)argc <= index)
return null;
// Ask N-API for the UTF-8 byte length
NativeMethods.GetValueStringUtf8(env, argv[index], null, 0, out nuint len);
// Allocate a buffer
int bufLen = (int)len + 1;
byte[]? rented = null;
Span<byte> buf = bufLen <= 512
? stackalloc byte[bufLen]
: (rented = ArrayPool<byte>.Shared.Rent(bufLen));
try
{
fixed (byte* pBuf = buf)
NativeMethods.GetValueStringUtf8(env, argv[index], pBuf, len + 1, out _);
return Encoding.UTF8.GetString(buf[..(int)len]);
}
finally
{
if (rented is not null)
ArrayPool<byte>.Shared.Return(rented);
}
}
```

This code asks N-API for the byte length, allocates a buffer (on the stack for small strings, from the pool for larger ones), reads the bytes, then decodes to a .NET `string`

.

Returning a string to JavaScript is the same process in reverse. We encode a .NET string into a UTF-8 buffer and pass it to `napi_create_string_utf8`

:

```
private static nint CreateString(nint env, string value)
{
int byteCount = Encoding.UTF8.GetByteCount(value);
byte[]? rented = null;
Span<byte> buf = byteCount <= 512
? stackalloc byte[byteCount]
: (rented = ArrayPool<byte>.Shared.Rent(byteCount));
try
{
Encoding.UTF8.GetBytes(value, buf);
NativeMethods.CreateStringUtf8(
env, buf[..byteCount], (nuint)byteCount, out nint result);
return result;
}
finally
{
if (rented is not null)
ArrayPool<byte>.Shared.Return(rented);
}
}
```

Both directions use `Span<T>`

, `stackalloc`

, and `ArrayPool`

to avoid heap allocations for typical string sizes. Once you have these helpers in place, you can write exported functions without thinking much about marshalling values.

## Implementing an exported function

With the N-API plumbing in place, implementing an actual exported function is straightforward. Here’s one that reads a value from the Windows Registry and returns it to JavaScript as a string:

```
[UnmanagedCallersOnly(CallConvs = [typeof(CallConvCdecl)])]
private static nint ReadStringValue(nint env, nint info)
{
try
{
var keyPath = GetStringArg(env, info, 0);
var valueName = GetStringArg(env, info, 1);
if (keyPath is null || valueName is null)
{
ThrowError(env, "Expected two string arguments: keyPath, valueName");
return 0;
}
using var key = Registry.CurrentUser.OpenSubKey(
keyPath,
writable: false);
return key?.GetValue(valueName) is string value
? CreateString(env, value)
: GetUndefined(env);
}
catch (Exception ex)
{
ThrowError(env, $"Registry read failed: {ex.Message}");
return 0;
}
}
```

The structure is the same for every exported function. Read any arguments to the function first. Here we read string arguments with `GetStringArg`

. Then, do the work using normal .NET APIs, and finally return a result via `CreateString`

or similar. One thing to be careful about is exception handling – an unhandled exception in an `[UnmanagedCallersOnly]`

method will crash the host process. We catch exceptions and forward them to JavaScript via `ThrowError`

, which causes a standard JavaScript `Error`

to be thrown on the calling side.

This example also shows why native addons are useful in the first place. Node.js doesn’t have built-in access to the Windows Registry, so a native addon lets us use `Microsoft.Win32.Registry`

from .NET and expose the result to JavaScript with minimal ceremony.

## Calling our function from TypeScript

First, we must produce a platform-specific shared library. Running `dotnet publish`

produces a native library appropriate for your operating system (for example, `RegistryAddon.dll`

on Windows, `libRegistryAddon.so`

on Linux, or `libRegistryAddon.dylib`

on macOS). By convention, Node.js treats paths ending with `.node`

as native addons, so we rename this output file to `MyNativeAddon.node`

.

We declare a TypeScript interface for our module, through which we expose type-safe access to our module’s functions:

```
interface RegistryAddon {
readStringValue(keyPath: string, valueName: string): string | undefined;
// Declare additional functions...
}
```

From there, loading it in TypeScript is a standard `require()`

call:

```
// Load our native module
const registry = require('./native/win32-x64/RegistryAddon.node') as RegistryAddon
// Call our native function
const sdkPath = registry.readStringValue(
'SOFTWARE\\dotnet\\Setup\\InstalledVersions\\x64\\sdk', 'InstallLocation')
```

And with that, we’re done! We can call from TypeScript into native code that was written in C#. While this particular registry addon is Windows-only, the same Native AOT and N-API approach works equally well on Windows, Linux, and macOS.

## What about existing libraries?

There is an existing project, [node-api-dotnet](https://github.com/microsoft/node-api-dotnet), that provides a higher-level framework for .NET/JavaScript interop. It handles a lot of the boilerplate and supports richer scenarios. For our use case, we only needed a handful of functions, and the thin N-API wrapper gave us full control over the interop layer without bringing in additional dependencies. If you need to expose entire .NET classes or handle callbacks from JavaScript into .NET, a library like that is worth considering.

## What we gained

The immediate, practical benefit was simplifying our contributor experience. Anyone who wants to develop in our repo no longer needs a specific Python version. `yarn install`

works with just Node.js, C++ tooling and the .NET SDK, which are tools we already require for development. Our CI pipelines are simpler as well.

Performance has been comparable to the C++ implementation. Native AOT produces optimized native code, and for the kind of work these functions do – string marshalling, registry access – there’s no meaningful difference in practice. The .NET runtime does bring a garbage collector and a slightly larger memory footprint, but in a long-running VS Code extension process this is negligible.

Looking ahead, this opens up some interesting possibilities. We currently run substantial .NET workloads in a separate process, communicating over a pipe. With Native AOT producing shared libraries that load directly into the Node.js process, we could potentially host some of that logic in-process, avoiding the serialization and process-management overhead. That’s a longer-term exploration, but the foundation is now in place.

## A footnote

When the idea of using Native AOT first arose, no one on the team had direct experience of integrating native code with Node.js. Even though we have experience with Native AOT, the prospect of learning N-API’s C calling conventions and wiring up the interop might have seemed daunting enough to put the whole idea on the back burner. GitHub Copilot allowed us to get a working proof-of-concept running very quickly, at which point the idea seemed promising enough to pursue. It’s been a fantastic tool for exploring ideas that we wouldn’t previously have had the time for. It’s improving our products, and the team’s quality of life.

## Summary

Native AOT increases the number of places you can run your .NET code. In this case, it allowed us to consolidate our tooling around fewer technologies and streamline our developer experience, particularly for onboarding new developers to the codebase.

If you’re running in Node.js, or in any other environment that can load native code, consider using Native AOT to produce that code. It allows you to write your native code in a language with memory safety, a rich standard library, and modern tooling. And if you’re not very familiar with native coding, you might be surprised to learn just how simple it can be to wire this all up (especially if you have a Copilot to help).

Nice post! Could you maybe link a small repo on github showing the full code?

It would easy to try it out.

Sure, I whipped this up by pointing Copilot at the blog post:

https://github.com/drewnoakes/native-aot-node-addon-demo

This is the reason I sponsored bootsharp, it's about to get so easy with the 0.8.0 release even with complex code full of static partial ref struct, marshalled pointers, SIMD, etc.

I compile to AOTNative-LLVM and it's for some reason, *much faster* this way on even a single thread than Blazor/MONO with multi thread.. hmm. I initially went for dotnet-on-node-js and it's very nice, but I'm left high and dry for the front end!

With bootsharp it just does both. I can do a single file -compat build and use base64 inline if I want. It makes the NPM package setup...

What is the story for debugging the c# / nativeaot code from the node process? What is the best way doing that? This seems to be a challenge with node-api-dotnet library as well.

Cool to see… I’ve used edge-js a few times for similar things. Like event logging in Windows.

https://github.com/agracio/edge-js

This is great! Thanks for sharing the experience with us.

I think Native AOT needs a bit of love, it should be as easy to use .NET in AOT scenarios, like other compiled languages that predate .NET, .e.g, Delphi.

So it is nice to see these kind of approaches gaining adoption.

In what ways do you think Native AOT could be improved? I’d say it’s pretty easy to use, so long as you aren’t using unsupported features. This article discusses native interop, so the examples are a bit more involved, but for regular .NET applications you just add `true` to your project, then invoke `dotnet publish -r ` to produce a self-contained standalone native executable.

Exactly, that is more attrition than using something like Delphi. We should not be forced into the command line to build native executables.

When using Visual Studio, producing a binary should be easy, like a drop box selecting if I want traditional MSIL or native executable.

Having to create a publishing profile, configuring if it is R2R, AOT, with what options, is added complexity that could be much simplified.

C# DevKit could also provide similar amenities.

Another thing, that isn't directly dependent on the .NET team itself, is having more NativeAOT deployments, where Microsoft usually only pushes for C++.

For example, building COM components in...

Amazing! 👏👏👏

Can this approach be extended to MacOS and Linux?

Absolutely. The Node.js APIs are cross platform, and so is Native AOT. Note however that you cannot build across OS’s with Native AOT, so you would also need MacOS and Linux build environments.

That’s my boy !!

Thanks Dad 🙂
