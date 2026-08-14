---
source: "https://devblogs.microsoft.com/dotnet/dotnet-11-preview-7/"
title: ".NET 11 Preview 7 is now available!"
author: ".NET Blog"
date_published: "2026-08-11"
date_clipped: "2026-08-12"
category: ".NET Ecosystem"
source_type: "rss"
---

# .NET 11 Preview 7 is now available!

Source: https://devblogs.microsoft.com/dotnet/dotnet-11-preview-7/

Today, we are excited to announce the seventh preview release of .NET 11! This release includes improvements across libraries, the .NET Runtime, SDK, C#, ASP.NET Core, .NET MAUI, Entity Framework Core, F#, and Windows Forms. Check out the linked release notes below and get started today.
Download .NET 11 Preview 7
This release contains the following improvements.
📚Libraries
IEEE 754 decimal floating-point types
Generic Complex\<T>
HTTP request compression
Configurable HTTP connection eviction
DNS record resolution APIs
ZIP archive password support
More ZIP creation, extraction, and metadata APIs
Ordinal casing APIs
Polymorphism inference for closed type hierarchies in System.Text.Json
Asynchronous ChangeToken.OnChange
See all library updates
⏱️Runtime
Runtime-async tiering and tail-await optimizations
CoreCLR on WebAssembly runs the libraries test suite
JIT and code generation
NativeAOT
Runtime diagnostics
See all runtime updates
🛠️ SDK
NativeAOT dotnet CLI is now enabled by default
MSBuild server is enabled by default
dotnet test adds run-level --timeout and --maximum-failed-tests
dotnet test supports Microsoft.Build.Traversal projects
dotnet test reporter improvements on Microsoft.Testing.Platform
dotnet test gains .NET MAUI device and environment support
File-based apps get dotnet reference and up-to-date-check fixes
Container publishing prefers platform-native local runtimes
.NET tool packaging supports custom RID matrices
See all SDK updates
C#
Labeled break and continue
Union patterns match the union or its value
Exhaustiveness for type parameters constrained to a closed type
Unsafe Evolution: compat mode and nameof
See all C# updates
🌐 ASP.NET Core
Auto pause Blazor circuits on inactivity
Cache Blazor SSR output with CacheView
New Blazor analyzers
QuickGrid supports InitialItemIndex and ScrollToItemAsync
wasm-tools uses Emscripten 6
Razor accepts literal attributes for union-typed component parameters
Validation localization is built in
SignalR .NET client supports auth refresh after redirects
OpenAPI Server-Sent Events in OpenAPI 3.2
TLS channel-binding token access from ITlsConnectionFeature
See all ASP.NET Core updates
📱 .NET MAUI
Cross-platform passkey authentication
XAML Incremental Hot Reload
Shell route templates
AOT-safe RelativeSource bindings
Third-party platform backends
TabbedPage adopts handlers on Apple platforms
Platform-specific capabilities
.NET for Android
Apple platforms (.NET for iOS, Mac Catalyst, macOS, tvOS)
See all .NET MAUI updates
🎁 Entity Framework Core
LINQ query translation improvements
Azure Cosmos DB provider improvements
Migrations improvements
Half type support on SQLite
See all EF Core updates
F#
Computation expression bindings inside a plain let RHS
Attributes resolve inside recursive modules and namespaces
Clearer diagnostic for generic attribute type abbreviations
Correct StructLayout size emission for data-less struct unions
See all F# updates
🖥️ Windows Forms
Opt in to .NET 11 visual styles
React to system visual settings
Avoid white dark-mode flashes — deferred form revealing
Suspend painting during bulk control mutations (location, size changes)
Toggle-switch appearance for CheckBox, RadioButton
See all Windows Forms updates
🚀 Get started
To get started with .NET 11, install the .NET 11 SDK .
If you’re on Windows using Visual Studio, we recommend installing the latest Visual Studio 2026 Insiders . You can also use Visual Studio Code and the C# Dev Kit extension with .NET 11.
