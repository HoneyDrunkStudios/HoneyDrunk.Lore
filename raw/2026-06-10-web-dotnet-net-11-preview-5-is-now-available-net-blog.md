---
source: "https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/"
title: ".NET 11 Preview 5 is now available! - .NET Blog"
author: ".NET Team"
date_published: "2026-06-09"
date_clipped: "2026-06-10"
category: ".NET Ecosystem"
source_type: "web"
---

# .NET 11 Preview 5 is now available! - .NET Blog

Source: https://devblogs.microsoft.com/dotnet/dotnet-11-preview-5/

.NET Modernization

Join us June 16th for .NET Day on Agentic Modernization — explore agentic modernization with demos and AI strategies for .NET.

[RSVP now](https://aka.ms/dotnet/agentic-mod/rsvp)

![](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2023/01/dotnet-logo-96x96.png)

[.NET Team](https://devblogs.microsoft.com/dotnet/author/dotnet)

Today, we are excited to announce the fifth preview release of .NET 11! This release includes improvements across the .NET Runtime, SDK, libraries, ASP.NET Core, .NET MAUI, C#, Entity Framework Core, and more. Check out the linked release notes below and get started today.

[Download .NET 11 Preview 5](https://dotnet.microsoft.com/download/dotnet/11.0)

This release contains the following improvements.

## **📚Libraries**

- [System.Text.Json supports JSON Lines serialization](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/libraries.md#systemtextjson-supports-json-lines-serialization)
- [LINQ adds full outer joins](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/libraries.md#linq-adds-full-outer-joins)
- [Cryptography adds X25519 key agreement](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/libraries.md#cryptography-adds-x25519-key-agreement)
- [Random adds generic numeric APIs](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/libraries.md#random-adds-generic-numeric-apis)
- [See all library updates](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/libraries.md)

## **⏱️Runtime**

- [Runtime-async suspension is faster](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/runtime.md#runtime-async-suspension-is-faster)
- [JIT optimizations](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/runtime.md#jit-optimizations)
- [GC trimming and compaction improvements](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/runtime.md#gc-trimming-and-compaction-improvements)
- [See all runtime updates](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/runtime.md)

## **🛠️ SDK**

- [File-based apps can reference other C# files](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/sdk.md#file-based-apps-can-reference-other-c-files)
- [SDK vulnerability and EOL checks are available during build](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/sdk.md#sdk-vulnerability-and-eol-checks-are-available-during-build)
- [`dotnet new` includes the MCP Server template](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/sdk.md#dotnet-new-includes-the-mcp-server-template)
- [Console apps include `System.Net.Http.Json` by default](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/sdk.md#console-apps-include-systemnethttpjson-by-default)
- [See all SDK updates](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/sdk.md)

## **C#**

- [Closed class hierarchies](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/csharp.md#closed-class-hierarchies)
- [Union declarations and union patterns](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/csharp.md#union-declarations-and-union-patterns)
- [Unsafe Evolution](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/csharp.md#unsafe-evolution)
- [See all C# updates](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/csharp.md)

## **🌐 ASP.NET Core**

- [Blazor SSR supports client-side validation](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/aspnetcore.md#blazor-ssr-supports-client-side-validation)
- [QuickGrid works without interactivity](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/aspnetcore.md#quickgrid-works-without-interactivity)
- [Blazor WebAssembly Gateway](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/aspnetcore.md#blazor-webassembly-gateway)
- [`SupplyParameterFromSession` for Blazor](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/aspnetcore.md#supplyparameterfromsession-for-blazor)
- [See all ASP.NET Core updates](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/aspnetcore.md)

## **📱 .NET MAUI**

- [Reliability and platform-fix wave lands in .NET 11](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/dotnetmaui.md#reliability-and-platform-fix-wave-lands-in-net-11)
- [Animations get CancellationToken-aware overloads](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/dotnetmaui.md#animations-get-cancellationtoken-aware-overloads)
- [Windows Maps gains a real implementation backed by Azure Maps](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/dotnetmaui.md#windows-maps-gains-a-real-implementation-backed-by-azure-maps)
- [.NET for Android stabilizes API 37](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/dotnetmaui.md#net-for-android-stabilizes-api-37)
- [See all .NET MAUI updates](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/dotnetmaui.md)

## **🎁 Entity Framework Core**

- [`dotnet ef` supports file-based apps](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/efcore.md#dotnet-ef-supports-file-based-apps)
- [SQL Server 2022 compatibility is now the default](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/efcore.md#sql-server-2022-compatibility-is-now-the-default)
- [EF1004 warns when async EF queries run synchronously](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/efcore.md#ef1004-warns-when-async-ef-queries-run-synchronously)
- [Query translation produces cleaner SQL](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/efcore.md#query-translation-produces-cleaner-sql)
- [See all EF Core updates](https://github.com/dotnet/core/blob/main/release-notes/11.0/preview/preview5/efcore.md)

## 🚀 Get started

To get started with .NET 11, [install the .NET 11 SDK](https://dotnet.microsoft.com/download/dotnet/11.0).

If you’re on Windows using Visual Studio, we recommend installing the latest [Visual Studio 2026 Insiders](https://visualstudio.microsoft.com/insiders). You can also use Visual Studio Code and the [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit) extension with .NET 11.

### Category

- [.NET](https://devblogs.microsoft.com/dotnet/category/dotnet/)
- [.NET MAUI](https://devblogs.microsoft.com/dotnet/category/maui/)
- [ASP.NET Core](https://devblogs.microsoft.com/dotnet/category/aspnetcore/)
- [C#](https://devblogs.microsoft.com/dotnet/category/csharp/)
- [Entity Framework](https://devblogs.microsoft.com/dotnet/category/entity-framework/)

### Topics

- [.NET 11](https://devblogs.microsoft.com/dotnet/tag/dotnet-11/)
- [Featured](https://devblogs.microsoft.com/dotnet/tag/featured-preview/)

### Share

## Author

![.NET Team](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2023/01/dotnet-logo-96x96.png)

[.NET Team](https://devblogs.microsoft.com/dotnet/author/dotnet)

.NET is the free, open-source, cross-platform framework for building modern apps and powerful cloud services.

## 0 comments

Be the first to start the discussion.

### [Leave a comment](javascript:void(0) "Leave a comment")[Cancel reply](/dotnet/dotnet-11-preview-5/#respond)

[Sign in](https://devblogs.microsoft.com/dotnet/wp-login.php?redirect_to=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fdotnet-11-preview-5%2F%23comments)

## Read next

June 8, 2026

### [.NET at Microsoft Build 2026: Must watch sessions](https://devblogs.microsoft.com/dotnet/dotnet-at-microsoft-build-2026/)

![](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2022/05/Dan-headshot-dark-96x96.webp)

Daniel Roth

May 26, 2026

### [Doing More with GitHub Copilot as a .NET Developer](https://devblogs.microsoft.com/dotnet/doing-more-with-github-copilot/)

![](https://devblogs.microsoft.com/dotnet/wp-content/uploads/sites/10/2023/09/wendy-96x96.jpeg)

Wendy Breiding (SHE/HER)

## Stay informed

Get notified when new posts are published.

Follow this blog

-
-
-
-
-

Are you sure you wish to delete this
comment?

OK
Cancel
