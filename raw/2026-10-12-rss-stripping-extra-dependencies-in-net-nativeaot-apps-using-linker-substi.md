---
source: "https://andrewlock.net/stripping-extra-dependencies-in-.net-nativeaot-apps-using-linker-substitutions"
title: "Stripping extra dependencies in .NET NativeAOT apps using linker substitutions"
author: "Andrew Lock"
date_published: "2026-10-06"
date_clipped: "2026-10-12"
category: ".NET Ecosystem"
source_type: "rss"
---

# Stripping extra dependencies in .NET NativeAOT apps using linker substitutions

In this post, I describe how I customized the linker for a NativeAOT application to remove a whole web of dependencies that I know will never be needed, but which the linker was unable to determine directly that it could remove. By using method substitutions, you can significantly reduce the size of the final NativeAOT binary, by enabling additional dead-code elimination.

## [Background: The `dd-dotnet` command line tool](https://andrewlock.net/stripping-extra-dependencies-in-.net-nativeaot-apps-using-linker-substitutions#background-the-dd-dotnet-command-line-tool)

The [Datadog .NET SDK](https://github.com/DataDog/dd-trace-dotnet) includes a small .NET command line application, `dd-dotnet` that is installed with the auto-instrumentation libraries and is used for various purposes. It's intentionally lightweight, and we compile it using NativeAOT to create a small binary that can run without any specific .NET version needing to be installed on a target machine.

The app takes a dependency on the [Microsoft.Diagnostics.Runtime](https://github.com/microsoft/clrmd) library, also known as "ClrMD". This is a process and crash dump introspection tool that we use in `dd-dotnet` to analyse failures. With our recent work on supporting [the upcoming .NET 11 release](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/overview), we needed to update the version of ClrMD that we were using. That's where things got interesting.

## [Updating the ClrMD NuGet package](https://andrewlock.net/stripping-extra-dependencies-in-.net-nativeaot-apps-using-linker-substitutions#updating-the-clrmd-nuget-package)

Updating the NuGet package was easy enough, we simply bumped to the latest version of the package in our *csproj* file:

```
-    <PackageReference Include="Microsoft.Diagnostics.Runtime" Version="3.2.527301" />
+    <PackageReference Include="Microsoft.Diagnostics.Runtime" Version="4.1.745802" />
```

There's [a migration guide](https://github.com/microsoft/clrmd/blob/main/doc/Migrating4.md) for bumping from 3.x to 4.x, but we weren't impacted by anything that's called out there, so the only other thing we had to do was update from targeting .NET 8 to .NET 10. There was no specific reason we had delayed that update, it was just a case of "if it's not broke, don't fix it"!

Everything built fine, and all the tests passed, so just ship it, right? Unfortunately, there was one adverse consequence of making the update: the binary was now significantly larger.

## [Updating the package increased the binary size significantly](https://andrewlock.net/stripping-extra-dependencies-in-.net-nativeaot-apps-using-linker-substitutions#updating-the-package-increased-the-binary-size-significantly)

After updating the ClrMD version, we checked the size of the final compiled binary, and unfortunately, it had increased in size compared to the pre-update size:

| Platform | Before | After | Diff | % change |
| --- | --- | --- | --- | --- |
| win-x64 | 3.519 MB | 3.956 MB | +437 kB | +12.42% |
| linux-x64 | 4.028 MB | 4.459 MB | +431 kB | +10.71% |
| linux-musl-x64 | 4.025 MB | 4.458 MB | +433 kB | +10.77% |
| linux-arm64 | 3.502 MB | 3.813 MB | +311 kB | +8.88% |
| linux-musl-arm64 | 3.499MB | 3.810 MB | +310 kB | +8.88% |

We need to keep this binary as small as possible, and so any increases are a problem, with an increase of ~0.5MB and ~10% definitely not being something we can just accept blindly. Luckily, there are tools to help with debugging this kind of issue.

## [Analyzing the size increase using Sizoscope](https://andrewlock.net/stripping-extra-dependencies-in-.net-nativeaot-apps-using-linker-substitutions#analyzing-the-size-increase-using-sizoscope)

My go-to tool for investigating the size of NativeAOT apps is [the Sizoscope tool](https://github.com/MichalStrehovsky/sizoscope) by [Michal Strehovsky](https://bsky.app/profile/migeel.sk). It has the option of both a GUI and a dotnet CLI tool, each of which shows everything that goes into a binary; which namespaces are taking up the most space, which types etc. It doesn't tell you *why* the various namespaces are included in the binary, but it gives a great starting point, and importantly, something an LLM can easily use!

![Image of the Sizoscope GUI showing where things are in a NativeAOT application](https://andrewlock.net/content/images/2026/sizoscope.png)

Rather than install the GUI, I chose to install the CLI tool instead, using

```
dotnet tool install sizoscope-cli --global
```

I then told Claude Code to use it to work out where all the extra space usage was coming from compared to the previous version. To do the analysis, you have to enable additional compile-time diagnostics by setting the following in your project file, but Claude handled all that itself, without me needing to do anything else:

```
<PropertyGroup>
  <IlcGenerateMstatFile>true</IlcGenerateMstatFile>
  <IlcGenerateDgmlFile>true</IlcGenerateDgmlFile>
</PropertyGroup>
```

After a little while, Claude popped up the analysis as to why the binary had increased in size.

## [Unreachable code brings dependencies along for the ride](https://andrewlock.net/stripping-extra-dependencies-in-.net-nativeaot-apps-using-linker-substitutions#unreachable-code-brings-dependencies-along-for-the-ride)

The problem lay with the `Microsoft.Diagnostics.Runtime.Implementation.SymbolServer`'s constructor, which looks a little like this:

```
internal SymbolServer(FileSymbolCache cache, Uri server, bool trace, TokenCredential? credential)
{
    // ...
    if (IsSymweb)
        _tokenCredential ??= new InteractiveBrowserCredential();
}
```

The `IsSymweb` property and the `InteractiveBrowserCredential` type are the core problem. `InteractiveBrowserCredential` is a type in the `Azure.Identity` assembly, which ultimately brings in:

* `Azure.Identity`
* `Microsoft.Identity.Client`
* `Microsoft.Identity.Client.Extensions.Msal`
* `System.Text.Json`

And all of that is needed *only* if `IsSymweb` is true. So what is `IsSymweb`?

`IsSymweb` is a property on `SymbolServer` that does a `string` comparison between the `Host` property of the `Uri server` parameter passed in the constructor, and a well-known `SymwebHost` URI value:

```
public static readonly Uri SymwebHost = new("https://symweb.azurefd.net/"); // Well-known host

public Uri Server { get; private set; } // Set in the constructor

// 👇 The comparison
private bool IsSymweb => Server.Host.Equals(SymwebHost.Host, StringComparison.OrdinalIgnoreCase);
```

The problem is that even though *we* know that this comparison will never evaluate to `true` (because the required `SymwebHost` value is never passed to the `SymbolServer` in any code paths we hit in our app, and we never configure `SymbolTokenCredential`), the *compiler*/*linker* doesn't know that. The comparison is performed at *runtime*, so the linker has to assume that the `new InteractiveBrowserCredential()` call is reachable, and so it has to preserve that type, and any dependencies that type depends on.

Unfortunately, due to this design, there didn't seem to be any way around this. No matter what you do, the linker is going to see the type as reachable, and anchor the whole dependency chain, increasing the size of our binary 🙁

What I didn't know (until the 🤖 pointed it out) is that there *is* a workaround; we can easily substitute the implementation of a method at compile-time and fix the problem!

## [Using linker substitutions to improve trimming and eliminate dead code](https://andrewlock.net/stripping-extra-dependencies-in-.net-nativeaot-apps-using-linker-substitutions#using-linker-substitutions-to-improve-trimming-and-eliminate-dead-code)

[*ILLink.Substitutions.xml*](https://github.com/dotnet/runtime/blob/main/docs/tools/illink/data-formats.md#substitution-format) is an XML configuration file used by the .NET IL trimmer (`illink`) and NativeAOT compiler (`ilc`) to replace the body of specific methods or fields with constant return values or throw statements. This provides a way to do the exact kind of dead-code elimination that we need, where the compiler isn't able to perform that analysis at linker time.

In theory, [according to the documentation](https://github.com/dotnet/runtime/blob/main/docs/tools/illink/data-formats.md#substitution-format), you should be able to simply embed the xml file in your project for it to take effect:

```
<ItemGroup>
  <EmbeddedResource Include="ILLink.Substitutions.xml">
    <LogicalName>ILLink.Substitutions.xml</LogicalName>
  </EmbeddedResource>
</ItemGroup>
```

But I found that for the NativeAOT case, this didn't work, and instead I had to use `<IlcArg>` to wire up the file directly with [the `--substitution` parameter](https://github.com/dotnet/runtime/blob/main/docs/tools/illink/illink-options.md#using-custom-substitutions)

```
<ItemGroup>
  <IlcArg Include="--substitution:$(MSBuildThisFileDirectory)ILLink.Substitutions.xml" />
</ItemGroup>
```

> Apparently the `Microsoft.DotNet.ILCompiler` SDK targets don't wire up `ILLinkSubstitutionsXmls` for `PublishAot`, which is why we need to pass the file directly using `--substitution` instead.

The content of the *ILLink.Substitutions.xml* file itself is below. The file provides one or more references to methods that you want to remove, or for which you want to replace the method body with a constant. You can also [remove embedded resources](https://github.com/dotnet/runtime/blob/main/docs/tools/illink/data-formats.md#remove-embedded-resources) and [*conditionally* enable replacements](https://github.com/dotnet/runtime/blob/main/docs/tools/illink/data-formats.md#conditional-substitutions-and-descriptors) if you wish.

For our case, we just need to replace the body of the `IsSymweb` property with the constant value `false`. With that change, the linker is able to see that we will never call the `new InteractiveBrowserCredential()` constructor, and consequently we don't need any of the dependencies for Azure and MSAL authentication. The following *ILLink.Substitutions.xml* file is all we need:

```
<linker>
  <assembly fullname="Microsoft.Diagnostics.Runtime">
    <type fullname="Microsoft.Diagnostics.Runtime.Implementation.SymbolServer">
      <method signature="System.Boolean get_IsSymweb()" body="stub" value="false" />
    </type>
  </assembly>
</linker>
```

With this extra file, and the small change in the project file to hook it up, we can compile our app again, and see the impact of this one small change:

## [Testing out our substitution](https://andrewlock.net/stripping-extra-dependencies-in-.net-nativeaot-apps-using-linker-substitutions#testing-out-our-substitution)

Simply re-publishing the app using NativeAOT shows that our change had a *big* effect:

| Platform | Before substitution | After substitution | % Change |
| --- | --- | --- | --- |
| win-x64 | 3.956 MB | 2.949 MB | −25.43% |
| linux-x64 | 4.459 MB | 3.466 MB | −22.27% |
| linux-musl-x64 | 4.458 MB | 3.465 MB | −22.28% |
| linux-arm64 | 3.813 MB | 2.965 MB | −22.24% |
| linux-musl-arm64 | 3.810 MB | 2.963 MB | −22.23% |

Adding the substitution reduced the size of the binary by 22-25%, i.e. it was even *smaller* than our original, *before* we updated the version of ClrMD from 3.x to 4.x! 😮

| Platform | Original  (.NET 8, ClrMD 3.x) | Final  (.NET 10, ClrMD 4.x) | % Change |
| --- | --- | --- | --- |
| win-x64 | 3.518 MB | 2.949 MB | −16.2% |
| linux-x64 | 4.027 MB | 3.466 MB | −13.9% |
| linux-musl-x64 | 4.028 MB | 3.465 MB | −14.0% |
| linux-arm64 | 3.499 MB | 2.965 MB | −15.3% |
| linux-musl-arm64 | 3.501 MB | 2.963 MB | −15.4% |

This seemed a little surprising on the surface, but it turns out the reduction in binary size is almost entirely due to the upgrade from .NET 8 to .NET 10. If we *only* updated to .NET 10, and didn't update ClrMD, then our binary size would be even smaller. However, our additional `ilc` substitution means that the the ClrMD 3.x to 4.x update has little overall effect on the final binary size *and* we will be able to support .NET 11 once it's released, so it's win-win!

There are two main take-aways for me. The obvious one is *ILLink.Substitutions.xml*, and how easy it makes it to force runtime-only properties to be compile-time constants, making trimming much easier. However, I was also impressed by how quick and easy it was for Claude to use the sizoscope CLI to accurately investigate where the binary size increase came from, and how we could resolve it.

Obviously you'll want to verify the claims any LLM makes, but if you're creating NativeAOT applications, then throwing an LLM at a binary to look for trimming opportunities seems like a simple way to reduce the size of your apps.

## [Summary](https://andrewlock.net/stripping-extra-dependencies-in-.net-nativeaot-apps-using-linker-substitutions#summary)

In this post, I describe how we reduced the size of a NativeAOT binary by using *ILLink.Substitutions.xml* to replace a property's body with a constant at linking time. By returning a constant (instead of performing a comparison at runtime, even one that will always return the same value) the linker is able to perform much more dead code elimination than it would otherwise be able to, which in some cases can mean many dependencies can also be removed. In our case, we were able to reduce the size of a binary by 22-25%, by replacing a single property in ClrMD with the constant `false` instead of relying on a run-time comparison.
