---
source: "https://devblogs.microsoft.com/dotnet/dotnet-maui-moves-to-coreclr-in-dotnet-11/"
title: ".NET MAUI Moves to CoreCLR in .NET 11"
author: ".NET Blog"
date_published: "Wed, 13 May 2026 17:05:04 +0000"
date_clipped: "2026-05-16"
category: ".NET Ecosystem"
source_type: "rss"
---

# .NET MAUI Moves to CoreCLR in .NET 11

Source: https://devblogs.microsoft.com/dotnet/dotnet-maui-moves-to-coreclr-in-dotnet-11/

Starting in .NET 11 Preview 4, CoreCLR is the default runtime for .NET MAUI applications on Android, iOS, and Mac Catalyst. Your mobile apps now run on the same runtime that powers ASP.NET Core, Azure services, desktop applications, and millions of production workloads around the world.
Mono Made This Possible 
For more than 15 years, Mono has been the runtime making .NET possible in places it was never designed to go. Miguel de Icaza started the Mono project in 2001 with the ambitious goal of bringing .NET to Linux. From there it grew into something nobody quite predicted.
MonoTouch brought C# to the iPhone in 2009. MonoDroid followed for Android. Xamarin turned those experiments into a platform used by millions of developers to ship production mobile apps. When Microsoft acquired Xamarin in 2016 and began the journey toward .NET MAUI, Mono was the runtime underneath it all.
Mono’s impact extends far beyond Microsoft’s own products. Unity built its entire scripting runtime on Mono, powering one of the world’s most popular game engines and the millions of games created with it. Unity has also begun their own transition to CoreCLR .  Avalonia and Uno Platform leverage Mono on WebAssembly to deliver cross-platform apps in the browser, and for mobile. MonoGame carries forward the XNA legacy for .NET game development across every platform. Godot has a C# scripting backend powered by Mono.
This is a vast ecosystem, and it all traces back to the same foundation.
Mono didn’t just enable .NET on mobile. It proved that .NET could go anywhere. CoreCLR becoming the default for .NET MAUI is the next chapter of that story, not its ending.
What Changed 
When you build a .NET MAUI app targeting .NET 11, CoreCLR is now the default runtime for Release and Debug builds on Android, iOS, and Mac Catalyst.
This isn’t entirely new ground. We have been adding platforms to CoreCLR since .NET Framework starting with Windows and then Linux, macOS (AppKit), and Android. What’s new in .NET 11 is we’re extending that same runtime to Android, iOS, and Mac Catalyst. These were the last .NET MAUI platforms that were still on Mono.
For a deeper look at how runtimes and compilation work across platforms, see the Runtimes and compilation documentation.
A few important clarifications:
This applies to Android, iOS, Mac Catalyst, and tvOS. All of these move to CoreCLR. 
Blazor WebAssembly is not affected. WASM continues to use Mono, and that is not changing in .NET 11. 
You can opt back to Mono if you hit issues during the transition period. 
Why CoreCLR 
Three reasons drove this change.
Runtime unification. Until now, .NET mobile apps ran on Mono while server, desktop, and cloud ran on CoreCLR. That split meant different JIT behavior, different GC characteristics, different diagnostics tooling, and different bug surfaces. With CoreCLR across all platforms, your mobile app runs on the same runtime as your backend. One runtime, one set of tools, one set of behaviors to understand.
Better performance foundations. CoreCLR brings tiered JIT compilation, ReadyToRun (R2R) precompilation, and Profile-Guided Optimization (PGO) to mobile. We have been landing this infrastructure throughout the .NET 11 preview cycle, including default partial R2R and packaged PGO profiles that improve startup without any changes to your code.
NativeAOT across platforms. CoreCLR is the foundation for NativeAOT compilation, which produces fully ahead-of-time compiled native binaries. With CoreCLR as the default, the path to NativeAOT on Android opens up as a natural next step. On iOS and Mac Catalyst, NativeAOT builds on the ahead-of-time compilation that has always been required for Apple platforms, now with a more unified toolchain. This work is actively underway in dotnet/android and dotnet/macios . For details on how these compilation modes work, see Runtimes and compilation in .NET MAUI .
What You Should Expect 
I’ll be direct about performance. CoreCLR with R2R and PGO shows strong improvements for many apps, particularly for startup time. For a baseline dotnet new maui app, startup is measurably faster.
However, we have seen community reports of regressions in larger, more complex applications on Android. Issues like dotnet/android#10588 and dotnet/android#10914 document real cases where startup time or app size increased. On iOS, the team has validated CoreCLR through successful App Store submissions, but you should still measure your own app’s behavior. We take these reports seriously and are actively working through them.
Our guidance: measure your app. Build against Preview 4 in Release mode, test on your target devices, and compare startup and package size against your .NET 10 baseline. Don’t assume universal improvement. Let us know what you find by filing issues on the repo.
In reviewing which architectures CoreCLR should support in .NET 11, we have decided to not include older, less used architectures: Android x86, Android API 23 and lower, and embedding APIs. We are still reviewing whether to support Android arm32.
How to Opt Back to Mono 
If you hit a blocking issue, you can temporarily switch back to Mono while we work on fixes. Add this to your project file:
<PropertyGroup>
<UseMonoRuntime>true</UseMonoRuntime>
</PropertyGroup> 
This works for Android, iOS, and Mac Catalyst. Use it when you encounter a compatibility issue or an unacceptable performance regression that blocks your release timeline. When you do, please file an issue in dotnet/android or dotnet/macios with your app type, package size, startup timings, and a reproducible sample if possible. That feedback directly shapes what we prioritize before GA.
The opt-out to Mono is available through .NET 11 servicing. We will communicate any future timeline changes well in advance.
What to Test 
Here is a validation checklist for your Preview 4 testing:
Build and publish your app in Release mode targeting .NET 11 
Measure startup on physical devices (cold start and warm start) 
Compare package size (APK/AAB on Android, IPA on iOS) against your .NET 10 build 
Test your full app flow including navigation, data loading, and any platform-specific integrations. 
Check Hot Reload in your development workflow 
Validate third-party libraries that use reflection, dynamic code generation, or Mono-specific APIs 
Please note, the debugger and hot reload implementations are quite young for these new platforms, and many known issues exist. Still, if anything behaves differently than expected, check the known issues for Android or iOS/Mac Catalyst , or file a new issue. The more reproducible your report, the faster we can act on it.
Diagnostics 
One practical benefit you get immediately is full .NET diagnostics on mobile. The same dotnet-trace and dotnet-counters tools you use on server and desktop now work on your Android device and in your iOS/Mac Catalyst workflow. If you have never profiled a mobile app with these tools, this is a good reason to start. Other tools like dotnet-dump are under consideration.
The Road Ahead 
Preview 4 is the beginning of broad validation, not the end of tuning. Over the coming previews we will continue to:
Close startup and app size gaps for complex applications 
Expand R2R and PGO coverage across platforms 
Address compatibility issues surfaced by community testing 
Advance NativeAOT support on Android and refine it on iOS/Mac Catalyst 
Your feedback during the preview window is what shapes the GA release in November. Every issue filed, every benchmark shared, and every “this works great” confirmation helps us get there.
Thank You 
Many of the engineers who built Mono’s mobile support contributed directly to making CoreCLR work on Android, iOS, and Mac Catalyst. Their expertise didn’t disappear. It was focused.
I want to acknowledge the broader community that built on Mono for over two decades. The game developers using Unity and MonoGame. The cross-platform teams using Avalonia and Uno Platform. The Xamarin developers who proved that C# belonged on mobile long before the rest of the industry agreed. Mono made all of that possible, and its DNA lives on in CoreCLR’s mobile support.
Mono got us here. CoreCLR carries us forward.
Get Started 
Install the .NET 11 Preview 4 SDK and the .NET MAUI workload:
dotnet workload install maui 
Build your existing app against net11.0-android , net11.0-ios , or net11.0-maccatalyst and run your validation. For the complete list of changes in Preview 4, see the .NET 11 Preview 4 release notes .
We are eager to hear from you. File issues, share your benchmarks, and tell us how your apps perform on CoreCLR. This is a transition we are making together.
