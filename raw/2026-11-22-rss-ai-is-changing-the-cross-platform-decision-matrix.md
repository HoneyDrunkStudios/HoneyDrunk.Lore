---
source: "https://devblogs.microsoft.com/dotnet/ai-cross-platform-decision-matrix"
title: "AI is Changing the Cross-Platform Decision Matrix"
author: "David Ortinau"
date_published: "2026-11-20"
date_clipped: "2026-11-22"
category: ".NET Ecosystem"
source_type: "rss"
---

# AI is Changing the Cross-Platform Decision Matrix

How you build a cross-platform app has always come down to a few hard constraints. Over the years I’ve talked with a lot of teams about how they chose their approach, and the factors are consistent: what the team already knows, how many codebases it has the capacity to support, what it costs to build and to maintain, solution characteristics like app size and performance, and the health of the ecosystem and support behind the stack.

Many of you reevaluate your technology investment choice on at least an annual basis. In 2026 there’s a major new factor to consider: AI coding agents.

Today the first two factors, team knowledge and team capacity, look different. A well-configured GitHub Copilot can write UIKit or Android Views whether or not anyone on your team has, and it doesn’t mind writing the same screen twice. Does that flatten the playing field between fully cross-platform and fully platform-specific, or is there still value in choosing a single stack to reach multiple platforms?

I ran an experiment to find out. The short version: agents made a second UI cheap to build, but owning it still took work. The first pass of a full rewrite took under four hours of my time. Adding the same feature to both versions used more worker model time with two UIs, and the coordinating agent used more model time than both implementation groups combined.

## The experiment

[Barista Notes](https://github.com/davidortinau/BaristaNotes) is a .NET MAUI app that runs on Android, iOS, macOS, and Windows. It has a dozen screens, more than 20 NuGet dependencies, and about 31,000 lines of hand-written C#. The UI is written in a fluent, reactive style with [MauiReactor](https://github.com/adospace/reactorui-maui) (C# UI, no XAML), which is worth keeping in mind when you read the size and startup numbers later.

![Nine Barista Notes screens built with .NET for iOS and .NET for Android](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/baristanotes-hero.webp)

In September, I had agents rebuild the iOS and Android apps with .NET for iOS and .NET for Android over a shared class library. In this post, “platform UI” means UIKit on iOS and Android Views on Android, written in C#. This provides the most direct comparison with today’s .NET MAUI, rather than using SwiftUI and Jetpack Compose.

The .NET MAUI app stayed as the reference, and it still ships the Mac Catalyst and Windows versions.

Then, to see what a change costs once both versions exist, I had each one add the same new feature. Across the two phases I compared:

- model time and token usage
- startup time
- screen transition time
- app size
- code sharing

### Where platform UI sits in .NET

This wasn’t a move off .NET, or even off the stack the app already used. Every .NET MAUI app runs on .NET for iOS and .NET for Android, and from the same C# you can use UIKit and Android Views directly, for one screen or the whole app.

Many developers know .NET MAUI as `Microsoft.Maui.Controls`: pages, layouts, and XAML. That’s the part you touch most, and it sits on top of the platform SDKs. When your app shows a button on iOS, a [.NET MAUI handler](https://learn.microsoft.com/dotnet/maui/user-interface/handlers/) creates a `UIButton` through .NET for iOS. On Android, the same handler pattern creates an `Android.Views.View` through .NET for Android.

![Diagram of the .NET MAUI stack, from UI options down through handlers, platform SDKs, and the .NET runtime](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/maui-stack.webp)

These layers are mature. Every one of them is .NET, and you can build features at any of them. .NET MAUI Controls is still the right starting point for most apps, and from that base you can also go to Blazor Hybrid, drawn UI, or a mix. I cover when I’d reach for each in [Choosing your mix](https://devblogs.microsoft.com/dotnet/ai-cross-platform-decision-matrix#choosing-your-mix). I measured only two: .NET MAUI Controls, and platform UI over a shared library.

> Teams have shipped platform UI with shared C# for a long time. In a [2017 account of the Azure mobile app](https://jj09.net/under-the-hood-of-the-azure-mobile-app/), engineer Jacob Jedryszek described an app built with Xamarin Native in C# and reported around 60-70% code sharing. I cite it as an example of the architecture, not as a statement about that app today.

## The results

### Cost to build: the rewrite

The rewrite ran from September 25 to 28, about three elapsed days in one GitHub Copilot session. A coordinator agent split the work between platform implementers and independent reviewers, 13 agent identities in all. The session record reports:

- 58 hours of aggregate model time
- about 3.293 billion gross input tokens, including 3.185 billion cache reads and 107.843 million cache writes
- 7.8 million output tokens
- 699 passing tests

Cache reads, cache writes, and the remaining 66,276 input tokens are parts of the gross input total, not additional usage. These counts include the context processed again on successive calls; they are not a count of newly supplied requirements. The rewrite used a mix of recorded models, primarily GPT-6 Astra at High and Extra High effort, with GPT-6 Sol and GPT-5.6 Sol also contributing. The [usage report](https://github.com/davidortinau/BaristaNotes/blob/main/docs/native-rebuild-model-token-cost.md) identifies the recorded models and accounting limits. It does not establish a reliable dollar cost for the run, and a subscription price would not establish one either. My own time went to prompting and validation, under 4 hours by my estimate.

**What these numbers cover**

These figures cover the recorded rewrite phase only. Later parity reviews found behavior gaps and an intermittent Android startup issue, and I made further fixes and device checks after the record ends. I count those separately because they are the cost of owning the platforms, which the next section looks at.

![Stacked bars comparing shared and platform-specific C# lines before and after the rewrite](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/code-share.webp)

Shared code went from 99.2% to 40.4% across both platforms because the two apps now have separate UI implementations. Look at each app on its own, though, and the shared Core is still 56.4% of the Android app and 58.7% of the iOS app. The Core project grew from 10,152 to 15,869 lines, because behavior that used to live in pages moved into code both apps use. Total product code grew 26.1%.

### Cost to maintain: adding a feature

![Barista Notes beans list with the new map of bean origins](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/barista-map.webp)

Next, I added the same feature to both versions: a map of where my beans come from, built with [Mapsui](https://mapsui.com) and cached place lookups. Each version got its own agent, using `gpt-6.1-sol` at High effort with the same scope. The platform UI version had to build for iOS and Android, with shared code counted once.

![Recorded worker measures for platform UI are 1.36 to 1.72 times the .NET MAUI measures for the map feature](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/map-feature-ratio.webp)

| Measure | .NET MAUI | .NET for iOS + .NET for Android |
| --- | --- | --- |
| Model minutes | 87.6 | 121.2 |
| Model calls | 254 | 368 |
| Gross input tokens, including cache activity | 10,041,328 | 17,283,666 |
| Cache-read input tokens | 8,976,914 | 15,815,339 |
| Cache-write input tokens | 1,063,652 | 1,467,223 |
| Remaining input tokens | 762 | 1,104 |
| Output tokens | 261,000 | 375,000 |
| Product lines added | 2,027 | 2,795 |
| Test lines added | 946 | 1,286 |
| Defect and technical feedback items | 13 | 19 |

The platform UI workers used about 1.4 times the model minutes of the .NET MAUI worker, added 1.36 times the test lines, and received 19 defect and technical feedback items against 13. Some of that feedback was about behavior on a single platform. One of my notes read: “On Android I have to tap a row in the list twice before it navigates to the bean detail page. iOS works correctly with one tap.”

For this feature, a second UI did not double worker model time, helped by the shared Core being written once. It did add implementation and verification work. The cache categories and remaining input add up to gross input; they should not be added to that total again.

A coordinating agent planned the work, ran builds, checked the running apps, and routed my feedback, and it used more model time than both versions combined: 616 minutes against 209. Part of that was the comparison harness itself, so I didn’t charge it to either side. It is still the clearest sign in this experiment that verification has its own cost, and that it can be larger than the cost of writing the code.

**What these numbers cover**

The table is a snapshot frozen on October 3, after both versions ran in the simulator and emulator and before I signed off on either. It measures worker model time up to that point. Later reviews found and fixed issues in both versions that aren’t counted here.

### What changed at runtime

I measured process-cold startup, package size, and two screen transitions on an iPhone 15 Pro and a Pixel 5. I chose these devices simply because they are what I have sitting on my desk. This process compares the two implementations on the same device within each platform, using the same accepted 1,000-drink dataset.

On November 18 I reran startup and screen navigation for all ten Android and iOS configurations on the original devices, with SDK `11.0.100`, GA runtime packs, and .NET MAUI Controls `11.0.0`. I used the original application baseline, with the scene-lifecycle wiring required by the GA iOS toolchain added to the isolated .NET MAUI benchmark copy. I also aligned the Entity Framework Core and Microsoft.Extensions packages used by the original app to `11.0.0`; the third-party packages stayed at the original versions.

The Android Release defaults differ: .NET MAUI uses partial composite ReadyToRun, while .NET for Android uses full composite ReadyToRun. I lead with full composite ReadyToRun on both to separate the UI choice from that runtime-setting difference. The partial rows are additional configured comparisons, not defaults for both apps, and the two apps do not use identical profile coverage.

Android startup used `am start -W` `TotalTime`, with a separate check that New Drink and the fixture were ready. It is not a time-to-fully-interactive measurement. The iOS timer ran from process start until New Drink was ready and two display frames completed. Compare the apps within each platform, not the absolute times between iOS and Android.

**Measurement scope**

Both platforms use .NET 11 GA. Each startup result has 30 measured launches after one pilot and five conditioning launches. Each screen-navigation result has ten fresh-process samples. Separate reverse-order runs reproduced the direction of the comparisons on both platforms, but some medians moved substantially. The charts retain each configuration’s first complete timing cohort, without pooling or substituting later observations. These compare the two app implementations within each platform, not Android versus iOS.

![Startup comparison: platform UI starts faster on iOS and Android in every runtime configuration](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/startup.webp)

With full ReadyToRun on both, the Android startup median was 1,233 ms for .NET MAUI and 615 ms for platform UI, a 50% reduction. On iOS it was 569 ms against 367 ms, a 35% reduction.

The matched full-ReadyToRun GA results were:

| Measure | .NET MAUI, iOS | .NET for iOS | .NET MAUI, Android | .NET for Android |
| --- | --- | --- | --- | --- |
| Startup median, 30 launches | 569 ms | 367 ms | 1,233 ms | 615 ms |
| Signed benchmark package | 58.87 MiB | 49.09 MiB | 45.64 MiB | 31.74 MiB |
| New Drink to history median, 10 samples | 660.5 ms | 115.0 ms | 826.8 ms | 381.0 ms |
| History to Settings median, 10 samples | 283.3 ms | 43.9 ms | 102.7 ms | 62.1 ms |

![Platform UI packages are smaller in each matched runtime configuration on iOS and Android](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/package-size.webp)

With full ReadyToRun on both, the platform UI package was 30% smaller on Android and 17% smaller on iOS. The Android figures are signed, arm64-only APK file sizes; the iOS figures are signed IPA file sizes. Both include the fixture and probes. These are not Google Play or App Store download estimates.

Using each Android app’s defaults changes that tradeoff. Platform UI’s full-R2R build started in 615 ms against 1,192 ms for the .NET MAUI partial-R2R build, but its APK was 31.74 MiB against 28.84 MiB. That is a 48% lower startup median with a 10% larger package, rather than a claim that the default platform UI package is always smaller.

Part of the package-size difference comes from the different dependency graphs: my .NET MAUI app includes MauiReactor, toolkits, and popups. This experiment does not isolate the size of .NET MAUI Controls alone.

![Screen-navigation medians on .NET 11 GA for iOS and Android, with matched full composite ReadyToRun highlighted](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2026/11/transitions.webp)

On Android, platform UI had the lower median in five of six configured screen-navigation comparisons. With NativeAOT, .NET MAUI had the lower median on the short Settings route, about 43 ms against 47 ms, with overlapping sample ranges. On iOS, platform UI had the lower median in every measured route, including 660 ms versus 115 ms from New Drink to history with full ReadyToRun.

Both Android implementations keep these routes within one Activity. The .NET MAUI version uses Shell navigation; the platform UI version swaps view trees inside its `MainActivity`, without Fragments or an Activity per screen. “Activity” in the route names means the app’s drink-history screen, not an Android Activity component. These are screen-navigation measurements, not Activity-launch measurements. They include each implementation’s data loading, view construction, navigation, and frame scheduling, rather than isolating framework overhead.

**About NativeAOT**

NativeAOT for .NET for Android is experimental in .NET 11. The GA builds retained trimming and AOT warnings, accepted only for this isolated benchmark, not a production release. One .NET MAUI iOS NativeAOT memory attempt did not reach probe readiness within 65 seconds. Its timing cohorts completed; its memory rerun remains incomplete and the cause is not isolated. The separate timing confirmation also moved its startup median from 349 to 505 ms. A successful measured route does not establish whole-app NativeAOT safety or a stable universal percentage.

The [Android GA report](https://github.com/davidortinau/BaristaNotes/blob/main/docs/native-runtime-comparison-net11-ga.md) and [iOS GA report](https://github.com/davidortinau/BaristaNotes/blob/main/docs/native-runtime-comparison-ios-net11-ga.md) retain the source, fixture, build configuration, raw samples, package hashes, confirmation runs, incomplete memory collection, and measurement limits.

## What AI changes, and what it doesn’t

Here is the decision matrix, with what this one experiment says about each factor.

| Factor | Before agents | What Barista Notes showed |
| --- | --- | --- |
| **What your team knows** | You chose a stack your team could write | Agents wrote the UIKit and Android Views code. I still had to recognize what was wrong on each platform |
| **Cost to build** | A second UI was a second project | A full rewrite took about three days and under 4 hours of my time for the first pass |
| **Cost to maintain** | Scaled with the number of UIs | This feature used about 1.4 times the worker model time and drew more feedback items |
| **Capacity to verify** | Counted as part of each feature | The largest cost I recorded: 616 coordinator minutes against 209 for implementation |
| **Ecosystem and support** | A reason to pick one well-supported stack | Not tested here. Both versions still leaned on the same libraries, such as Mapsui |
| **Runtime results** | Assumed to favor platform UI | Matched runtime builds favored platform UI for startup and size here. Android defaults traded startup against size; navigation results depended on the route |

For me, the cost to build changed enough to make this rewrite practical as an experiment.

What AI doesn’t erase is the work around the code:

- **Testing on every platform.** Shared unit tests run once, but user journeys need checks on each platform UI you own.
- **Validation on devices.** Every UI-heavy change now has an implementation to verify on each platform.
- **Issue triage.** A second UI brings platform-specific bugs that a shared UI wouldn’t have.
- **Pull requests and review.** Two UI implementations mean bigger diffs and reviewers who know each platform.

Agents help with all of these, though someone still owns the result. Plan for both your agent capacity and your people to grow with the number of UIs you maintain.

## Choosing your mix

Now that you’ve seen the numbers, here’s how I think about each option.

### .NET MAUI Controls

One UI in XAML or C# across Android, iOS, Mac Catalyst, and Windows is my starting point when one team owns all those platforms. Forms, lists, and navigation fit this approach well. Barista Notes still ships its Mac Catalyst and Windows versions this way.

### .NET MAUI with Blazor Hybrid

[Blazor Hybrid](https://learn.microsoft.com/aspnet/core/blazor/hybrid/) runs Razor components in a `BlazorWebView` inside a .NET MAUI app, with full access to the device. It is worth considering when you already have Blazor UI to share with a web app, or your team works in HTML and CSS.

### .NET MAUI with drawn UI

Draw the UI yourself with [`GraphicsView` and Microsoft.Maui.Graphics](https://learn.microsoft.com/dotnet/maui/user-interface/graphics/), [SkiaSharp](https://github.com/mono/SkiaSharp), or community libraries like [DrawnUi](https://github.com/taublast/DrawnUi.Maui). This gives you control over a consistent branded appearance and visuals the platform controls do not provide.

Drawn controls don’t get platform accessibility for free, so budget time for screen reader support. I didn’t measure drawn UI or Blazor Hybrid in Barista Notes.

### .NET for iOS and .NET for Android

Platform UI in C# over a shared .NET core is another option. .NET for Mac Catalyst and WinUI let you use the same approach on desktop. Consider it when:

- **Platform look and feel is the product.** You write UIKit and Android Views directly.
- **You’ve measured a startup, size, or screen performance problem** and the platform UI fixes it.
- **You want direct control** of navigation, lifecycle, and platform integration.
- **You can staff verification on each platform**, with people and agents.

### Mix them

You don’t have to pick one. Use platform UI for the screens that need it and .NET MAUI for the rest. Embed .NET MAUI views in a platform app with `ToPlatformEmbedded`. Or split by platform the way Barista Notes does today: platform UI on iOS and Android, .NET MAUI on Mac Catalyst and Windows, one shared Core underneath.

## Where to start

1. **Pick the screens where platform UI matters most.** Start with one, and either embed it or add a platform app project next to your .NET MAUI app.
2. **Measure one real journey, then change a requirement.** The first port tells you what construction costs. The second change tells you what maintenance costs.
3. **Budget for the work around the code.** Tests, device checks, triage, and review for every platform you own, for both people and agents.
4. **Compare against a current .NET MAUI build.** [.NET 11 moved .NET MAUI to CoreCLR](https://learn.microsoft.com/dotnet/maui/whats-new/dotnet-11), so measure against that instead of an app from three releases ago.
5. **Start with what’s already in your app.** .NET for iOS and .NET for Android are there today.

For more details, see the [native embedding documentation](https://learn.microsoft.com/dotnet/maui/platform-integration/native-embedding), the [.NET for Android documentation](https://learn.microsoft.com/dotnet/android/), and the [.NET for iOS documentation](https://learn.microsoft.com/dotnet/ios/). The full Barista Notes source and every measurement report are on [GitHub](https://github.com/davidortinau/BaristaNotes).

## How the agents saw the app

Agents write better UI code when they can see and drive the running app. Here’s what I used:

- **[GitHub Copilot app](https://github.com/github/app).** I ran the rewrite and the feature comparison as agent sessions here, with subagents per platform and separate reviewers, and stepped in when a session needed direction. If you haven’t tried it with .NET yet, see [Modernize .NET applications in the GitHub Copilot app](https://devblogs.microsoft.com/dotnet/modernize-dotnet-in-github-copilot-app/).
- **[DevFlow](https://github.com/dotnet/maui-labs/tree/main/src/DevFlow).** It lets agents read the visual tree, tap, type, take screenshots, and inspect logs and network traffic in a running app. I used it on the .NET MAUI version, and it also works with plain .NET for iOS and .NET for Android apps.
- **[Ailoha](https://ailoha.dev).** It does the same across frameworks, including native Android and Flutter. The Barista Notes iOS and Android apps include it in Debug builds only, so agents could inspect the UIKit and Android Views screens.
- **[Mobile Canvas](https://github.com/Redth/mobile-canvas-ghcp).** It streams the iOS Simulator and Android emulator into the GitHub Copilot app, so you and the agent see, and tap, the same device.

**Experimental tools**

DevFlow ships in .NET MAUI Labs, which is experimental and not covered by the .NET MAUI support policy. Ailoha and Mobile Canvas are early, experimental projects from Jonathan Dick. Try them, expect rough edges, and send feedback.

## So, is the playing field flat?

Not quite. Building a second UI used to be the expensive part, and for Barista Notes it no longer was. Owning it is what still costs: one feature took about 1.4 times the worker model time, drew more feedback, and needed checking on every platform. In exchange, the matched runtime builds gave me faster startup and smaller packages. The Android default builds showed why the settings matter: faster platform UI startup came with a larger package than the .NET MAUI default.

That changes how I’d weigh the decision without changing where I’d begin. A single shared UI is still my starting point because it gives my team less UI code to own. What’s new is that going platform-specific for a screen, a platform, or the whole app is now practical to try and measure before committing to it.

What factors are you weighing for your apps? Tell me in the comments what you’ve measured, what has turned out to be right for your app and business, and how AI is changing your plans.
