---
source: "https://devblogs.microsoft.com/dotnet/dotnet-11-rc-2"
title: "Announcing .NET 11 Release Candidate 2"
author: ".NET Team"
date_published: "2026-10-13"
date_clipped: "2026-10-13"
category: ".NET Ecosystem"
source_type: "rss"
---

# Announcing .NET 11 Release Candidate 2

.NET 11 Release Candidate 2 is now available. This is our second release
candidate, which comes with a
[go-live support license](https://dotnet.microsoft.com/platform/support/policy/dotnet-core#previews)
so you can confidently use this release for your production applications. This
release of .NET 11 is supported in the new
[Visual Studio 2026 Insiders](https://aka.ms/VS2026Insiders) release alongside
Visual Studio Code with the C# Dev Kit. Check out the full release notes below
and get started today.

[Download .NET 11 RC2](https://get.dot.net/11)

This release contains the following highlights and improvements.

## **📚 Libraries**

* [Read CBOR incrementally](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/libraries.md#read-cbor-incrementally)
* [Experimental composite ML-KEM and HPKE APIs](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/libraries.md#experimental-composite-ml-kem-and-hpke-apis)
* [Format DataAnnotations messages with attribute-specific arguments](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/libraries.md#format-dataannotations-messages-with-attribute-specific-arguments)
* [Configure initial HTTP/2 concurrency](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/libraries.md#configure-initial-http2-concurrency)
* [Full Release Notes](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/libraries.md)

## **⏱️ Runtime**

* [File locking on iOS and tvOS is disabled by default](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/runtime.md#changes-since-the-previous-preview)
* [Full Release Notes](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/runtime.md)

## **🛠️ SDK**

* [Quoted file-level directive values](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/sdk.md#quoted-file-level-directive-values)
* [MSBuild properties in launch-profile arguments](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/sdk.md#msbuild-properties-in-launch-profile-arguments)
* [Full Release Notes](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/sdk.md)

## **🧱 MSBuild**

* [Faster wildcard matching during project evaluation](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/msbuild.md#faster-wildcard-matching-during-project-evaluation)
* [Full Release Notes](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/msbuild.md)

## **📦 NuGet**

* [Configure minimum package publication age from the CLI](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/nuget.md#configure-minimum-package-publication-age-from-the-cli)
* [Full Release Notes](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/nuget.md)

## **F#**

* [Runtime async support](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/fsharp.md#runtime-async-support)
* [reraise in computation expressions](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/fsharp.md#reraise-in-computation-expressions)
* [Require named arguments for selected APIs](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/fsharp.md#require-named-arguments-for-selected-apis)
* [Lower allocations in FSharp.Core collections](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/fsharp.md#lower-allocations-in-fsharpcore-collections)
* [Compiler memory usage improvements](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/fsharp.md#compiler-memory-usage-improvements)
* [Bound concurrent asynchronous work](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/fsharp.md#bound-concurrent-asynchronous-work)
* [Trimming and Native AOT improvements](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/fsharp.md#trimming-and-native-aot-improvements)
* [Full Release Notes](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/fsharp.md)

## **🌐 ASP.NET Core**

* [`QuickGrid` virtualization APIs are no longer experimental](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/aspnetcore.md#quickgrid-virtualization-apis-are-no-longer-experimental)
* [Full Release Notes](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/aspnetcore.md)

## **📱 .NET MAUI**

* [Create an app with C# UI](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/dotnetmaui.md#create-an-app-with-c-ui)
* [Use Apple Icon Composer assets](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/dotnetmaui.md#use-apple-icon-composer-assets)
* [Evaluate the Apple Shell handler](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/dotnetmaui.md#evaluate-the-apple-shell-handler)
* [XAML authoring and Hot Reload](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/dotnetmaui.md#xaml-authoring-and-hot-reload)
* [.NET for Android](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/dotnetmaui.md#net-for-android)
* [Apple platforms (.NET for iOS, Mac Catalyst, macOS, tvOS)](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/dotnetmaui.md#apple-platforms-net-for-ios-mac-catalyst-macos-tvos)
* [Full Release Notes](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/dotnetmaui.md)

## **🖥️ Windows Forms**

* [Visual styles and appearance](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/winforms.md#visual-styles-and-appearance)
* [React to Windows visual and accessibility settings](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/winforms.md#react-to-windows-visual-and-accessibility-settings)
* [Deferred form reveal](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/winforms.md#deferred-form-reveal)
* [Visual Basic Application Framework](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/winforms.md#visual-basic-application-framework)
* [Suspend painting and layout during bulk updates](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/winforms.md#suspend-painting-and-layout-during-bulk-updates)
* [New KioskModeManager component](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/winforms.md#new-kioskmodemanager-component)
* [New Designer-guiding analyzers](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/winforms.md#new-designer-guiding-analyzers)
* [Full Release Notes](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/rc2/winforms.md)

## 🚀 Get started

To get started with .NET 11,
[install the .NET 11 SDK](https://get.dot.net/11).

If you’re on Windows, we recommend installing the latest version of
[Visual Studio 2026 Insiders](https://aka.ms/vs/insiders).

You can also use Visual Studio Code and the
[C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)
extension with .NET 11.

## 📦 Join a .NET community standup

Join us each week and engage with the developers and product managers behind
.NET for
[community standups](https://dotnet.microsoft.com/live/community-standup).

## 📢 .NET 11 Discussions

The team has been making release announcements alongside full
[release notes](https://github.com/dotnet/core/tree/main/release-notes/11.0)
on the
[dotnet/core GitHub Discussions](https://github.com/dotnet/core/discussions/categories/news).

## 🔔 Stay up-to-date with .NET 11

You can stay up-to-date with all the features of .NET 11 with:

* [What’s new in .NET 11](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-11/overview)
* [What’s new in C# 15](https://learn.microsoft.com/dotnet/csharp/whats-new/csharp-15)
* [What’s new in ASP.NET Core](https://learn.microsoft.com/aspnet/core/release-notes/aspnetcore-11)
* [What’s new in Entity Framework Core](https://learn.microsoft.com/ef/core/what-is-new/ef-core-11.0/whatsnew)
* [Breaking Changes in .NET 11](https://learn.microsoft.com/dotnet/core/compatibility/11)
* [.NET 11 Releases](https://github.com/dotnet/core/blob/main/release-notes/11.0/README.md)
