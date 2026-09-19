# .NET Runtime and Mobile 2026

## Decision-useful summary
.NET 11 is making runtime/process work more operationally useful: MAUI moves Android/iOS/Mac Catalyst/tvOS apps to CoreCLR by default, while `System.Diagnostics.Process` gains safer one-call execution/capture APIs, explicit handle inheritance, kill/detach lifetime controls, and trimmer-friendly `SafeProcessHandle` paths. For HoneyDrunk, this is relevant to mobile C# prototypes and local agent/tool runners that need deadlock-free process execution and orphan-process control. Preview status means measure before adopting. [sources: raw/2026-05-16-rss-net-blog-net-maui-moves-to-coreclr-in-net-11.md; raw/2026-05-16-rss-net-blog-process-api-improvements-in-net-11.md]

## Claims
- Starting in .NET 11 Preview 4, CoreCLR is the default runtime for .NET MAUI apps on Android, iOS, Mac Catalyst, and tvOS; Blazor WebAssembly remains on Mono. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-net-blog-net-maui-moves-to-coreclr-in-net-11.md]
- The MAUI/CoreCLR move is intended to unify mobile with server/desktop runtime behavior and unlock tiered JIT, ReadyToRun, PGO, and a clearer NativeAOT path, but Microsoft reports community regressions in larger Android app startup/package size and recommends app-specific measurement. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-net-blog-net-maui-moves-to-coreclr-in-net-11.md]
- .NET MAUI apps can temporarily opt back to Mono with `<UseMonoRuntime>true</UseMonoRuntime>` if CoreCLR causes blocking compatibility or performance issues during the .NET 11 transition. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-net-blog-net-maui-moves-to-coreclr-in-net-11.md]
- .NET 11 adds `Process.RunAndCaptureText[Async]`, `Process.Run[Async]`, `ReadAllText/Bytes/Lines[Async]`, and `ProcessExitStatus` to make starting a process and capturing output/error easier and less deadlock-prone. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-net-blog-process-api-improvements-in-net-11.md]
- .NET 11 adds process-control APIs including `Process.StartAndForget`, `ProcessStartInfo.KillOnParentExit`, `ProcessStartInfo.StartDetached`, `ProcessStartInfo.InheritedHandles`, `ProcessStartInfo.Standard*Handle`, and `SafeProcessHandle` start/wait/kill/signal helpers. confidence: 1 source, last-confirmed 2026-05-17. [source: raw/2026-05-16-rss-net-blog-process-api-improvements-in-net-11.md]

## Typed entities
- runtime: .NET 11
- runtime: CoreCLR
- runtime: Mono
- platform: .NET MAUI
- platform: Android
- platform: iOS
- platform: Mac Catalyst
- platform: tvOS
- API: `System.Diagnostics.Process`
- API: `Process.RunAndCaptureText[Async]`
- API: `Process.Run[Async]`
- API: `Process.ReadAllText/Bytes/Lines[Async]`
- API: `ProcessStartInfo.KillOnParentExit`
- API: `ProcessStartInfo.StartDetached`
- API: `ProcessStartInfo.InheritedHandles`
- API: `SafeProcessHandle`
- concept: NativeAOT
- concept: ReadyToRun
- concept: Profile-Guided Optimization
- file: raw/2026-05-16-rss-net-blog-net-maui-moves-to-coreclr-in-net-11.md
- file: raw/2026-05-16-rss-net-blog-process-api-improvements-in-net-11.md

## Explicit relationships
- .NET MAUI uses CoreCLR by default in .NET 11 for mobile/native app targets, superseding Mono default runtime assumptions for those targets.
- Blazor WebAssembly continues to use Mono and is not superseded by the MAUI CoreCLR transition.
- CoreCLR enables MAUI access to unified diagnostics such as `dotnet-trace` and `dotnet-counters`.
- `Process.RunAndCaptureText[Async]` supersedes hand-rolled sequential stdout/stderr reading for common process-capture cases.
- `InheritedHandles` and explicit standard handle redirection reduce accidental handle inheritance that can cause deadlocks or leaks.
- `KillOnParentExit` depends-on platform support and helps local harnesses avoid orphaned child processes.
- [[microsoft-dotnet-ai-stack]] uses .NET 11 runtime/platform changes as scouting evidence for AI-adjacent tooling and MCP server work.

## HoneyDrunk implications
- For MAUI/mobile experiments, benchmark startup, package size, Hot Reload/debugger behavior, and third-party libraries on target physical devices before trusting CoreCLR defaults.
- For OpenClaw/Grid local tool runners written in .NET, prefer `RunAndCaptureText[Async]` or line APIs over custom stdout/stderr drains.
- Use `KillOnParentExit` for agent-spawned subprocesses that must not survive the parent; use `StartDetached` only when survival is intentional and logged.
- Treat .NET 11 APIs as preview until GA/servicing posture is acceptable for the specific service.

## Confidence and quality notes
- Quality posture: decision-usable for scouting and codebase audits; implementation should wait on current docs/GA state for production.
- Weak spots: vendor-authored preview posts; performance claims require local measurement.
- Privacy filter: no private app metrics or process arguments copied.

## 2026-05-22 compile additions

### Claims
- The C# memory-safety redesign is planned as a C# 16 feature, previewing with .NET 11 and targeted for production in .NET 12; it changes unsafe from a pointer-context marker into a caller-facing safety contract. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md; page: [[csharp-memory-safety-and-unsafe-code]]]
- Under the new model, unsafe member calls and pointer dereferences must be wrapped in inner `unsafe { }` blocks, while unsafe signatures propagate caller obligations unless boundary methods discharge them. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md]
- .NET projects can combine the new safety model with `<AllowUnsafeBlocks>false</AllowUnsafeBlocks>` to prevent unsafe code and unsafe API calls at compile time. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md]

### Typed entities
- language: C# 16
- runtime: .NET 11 preview
- runtime: .NET 12 planned production
- project property: `<AllowUnsafeBlocks>`
- page: [[csharp-memory-safety-and-unsafe-code]]

### Explicit relationships
- .NET 11 preview includes runtime/mobile changes and is also the preview vehicle for stricter C# memory-safety semantics.
- C# caller-unsafe support depends-on compiler and library metadata adoption across producer and consumer assemblies.

### HoneyDrunk implications
- Track .NET 11 previews not only for MAUI/process APIs, but also for unsafe-code policy gates in tool/agent repos.

## 2026-05-30 compile additions

### Claims
- .NET MAUI 10 adds Android Material 3 opt-in styling through a single MSBuild property, `<UseMaterial3>true</UseMaterial3>`, while iOS, Mac Catalyst, and Windows continue using native design systems. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-give-your-net-maui-android-apps-a-material-3-makeover.md]
- Material 3 support requires .NET MAUI 10 / `net10.0-android`; Microsoft says the largest control wave landed in SR6 / Microsoft.Maui.Controls 10.0.60, covering Button, Entry, SearchBar, DatePicker, Slider, ProgressBar, ImageButton, Switch, Shell theming, and more. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-give-your-net-maui-android-apps-a-material-3-makeover.md]
- Material 3 currently affects supported default control appearance on Android; explicit app colors/styles and custom handlers still take precedence, and the app can opt back out by removing the property or setting it false. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-give-your-net-maui-android-apps-a-material-3-makeover.md]
- Microsoft states the active plan is for Material 3 to become the default Android styling after tracked gaps are resolved, but per-control opt-in, direct .NET MAUI APIs for Material color roles, and some navigation/collection surfaces remain tracked work. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-05-30. [source: raw/2026-05-30-rss-net-blog-give-your-net-maui-android-apps-a-material-3-makeover.md]

### Typed entities
- framework: .NET MAUI 10
- platform: Android
- design system: Material 3 / Material You
- property: `<UseMaterial3>`
- package: `Microsoft.Maui.Controls`
- release: 10.0.60 / SR6
- control: Entry
- control: SearchBar
- control: DatePicker
- control: Shell

### Explicit relationships
- .NET MAUI Android uses Material 3 opt-in to supersede Material 2 default styling for covered controls.
- Explicit app styles/custom handlers override Material 3 defaults.
- Material 3 default adoption depends-on closing tracked control/navigation/color-token gaps.

### HoneyDrunk implications
- For any MAUI Android app, run a visual regression pass across high-use screens before enabling Material 3.
- Keep `UseMaterial3` branch-scoped until unsupported controls, navigation chrome, brand colors, and Android API-level behavior are checked.

## 2026-06-05 compile additions

### Claims
- Microsoft's C# Dev Kit team replaced some C++/node-gyp native Node.js addons with .NET Native AOT shared libraries that export the Node-API entry point `napi_register_module_v1`. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-writing-node-js-addons-with-net-native-aot.md]
- The Native AOT Node addon pattern uses `[UnmanagedCallersOnly]` for exported entry points, `[LibraryImport]` P/Invokes against `node`, a `NativeLibrary.SetDllImportResolver` that resolves Node-API symbols from the host process, and Span/ArrayPool-based UTF-8 marshalling. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-writing-node-js-addons-with-net-native-aot.md]
- Microsoft reports the practical benefit was removing an old Python/node-gyp setup requirement for contributors and CI while keeping comparable performance for registry/string-marshalling work; Native AOT's larger memory footprint was described as negligible for the long-running VS Code extension process. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-writing-node-js-addons-with-net-native-aot.md]
- The source notes Native AOT and Node-API are cross-platform, but Native AOT cannot cross-compile across operating systems, so Windows, macOS, and Linux addons require matching build environments. confidence: 1 Microsoft/.NET Blog source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-writing-node-js-addons-with-net-native-aot.md]

### Typed entities
- product: C# Dev Kit
- runtime: .NET Native AOT
- platform/runtime: Node.js
- API: Node-API / N-API
- build tool: node-gyp
- attribute: `[UnmanagedCallersOnly]`
- attribute/API: `[LibraryImport]`
- API: `NativeLibrary.SetDllImportResolver`
- API: `NativeLibrary.GetMainProgramHandle`
- file extension: `.node`
- concept: native addon

### Explicit relationships
- .NET Native AOT can produce Node.js native addons when the shared library exports the Node-API registration entry point.
- Native AOT Node addons can supersede small C++/node-gyp addons when a team already depends on the .NET SDK and needs a narrow native API bridge.
- Node-API ABI stability complements Native AOT because Node only requires exported symbols and C ABI calls, not C++ implementation.
- Cross-platform addon distribution depends-on per-OS Native AOT builds.

### HoneyDrunk implications
- For HoneyDrunk VS Code/Node tooling that needs native Windows/macOS/Linux operations, consider .NET Native AOT addons before adding C++/node-gyp dependency chains.
- Keep the pattern narrow: interop code must catch exceptions before returning to Node, handle UTF-8 marshalling carefully, and ship platform-specific `.node` artifacts.

### Quality notes
- Source is an implementation case study from Microsoft. Validate debugging, packaging, signing, and CI matrix complexity before adopting.

## 2026-06-10 compile additions: .NET 11 Preview 5 and June servicing

### Source-backed claims
- .NET 11 Preview 5 includes runtime, SDK, libraries, ASP.NET Core, MAUI, C#, and EF Core updates, with runtime work including faster async suspension and SDK work including file-based app references, vulnerability checks, EOL checks, and an MCP Server template. Source: `raw/2026-06-10-web-dotnet-net-11-preview-5-is-now-available-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-10.
- .NET MAUI Preview 5 focuses on reliability and platform fixes, adds CancellationToken-aware animation overloads, adds a Windows Maps implementation backed by Azure Maps, and stabilizes .NET for Android API 37. Source: `raw/2026-06-10-web-dotnet-net-11-preview-5-is-now-available-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-10.
- The June 2026 .NET servicing release fixes CVE-2026-45591, CVE-2026-45491, and CVE-2026-45490 across supported .NET release trains, with runtime/ASP.NET Core updates for .NET 10, 9, and 8. Source: `raw/2026-06-10-web-dotnet-net-and-net-framework-june-2026-servicing-releases-updates-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft reports no new .NET Framework security or non-security updates in the June 2026 servicing post. Source: `raw/2026-06-10-web-dotnet-net-and-net-framework-june-2026-servicing-releases-updates-net-blog.md`. confidence: 1 source, last-confirmed 2026-06-10.

### Typed entities
- project: .NET 11 Preview 5
- project: .NET MAUI
- project: .NET 10
- project: .NET 9
- project: .NET 8
- vulnerability: CVE-2026-45591
- vulnerability: CVE-2026-45491
- vulnerability: CVE-2026-45490
- decision: June 2026 .NET servicing priority

### Explicit relationships
- .NET 11 Preview 5 previews SDK and MAUI capabilities but should not supersede supported production trains.
- June 2026 servicing supersedes prior vulnerable .NET 10/9/8 patch levels for security posture.
- .NET Framework has no new June 2026 servicing action from this source.

### HoneyDrunk implications
- Audit HoneyDrunk .NET 8/9/10 services for June 2026 servicing uptake.
- Keep .NET 11 Preview 5 experiments isolated from production branches until API and tooling stability improve.
- Watch MAUI Windows Maps and Android API 37 if any mobile/desktop client work resumes.

### Quality notes
- Microsoft servicing posts are authoritative for release existence, but project-specific urgency depends on package/runtime inventory and exposure.

## 2026-07-03 compile additions: SkiaSharp 4.0 stable

### Source-backed claims
- SkiaSharp 4.148.0 is the first stable SkiaSharp v4 release, updating the native Skia engine through milestone m148 and adding variable font axes, color font palettes, animated WebP encoding, cleaner retired legacy APIs, and native object lifecycle fixes. Source: `raw/2026-07-03-web-dotnet-skiasharp-4-0-is-here-announcing-the-first-stable-release-net-blog.md`. confidence: 1 .NET Blog source, last-confirmed 2026-07-03.
- Microsoft reports initial hardware-accelerated OpenGL testing with up to 24% faster rendering for shadow-heavy UI scenes and about 6x faster CPU procedural Perlin-noise shaders, while warning absolute frame rates vary by GPU and driver. Source: `raw/2026-07-03-web-dotnet-skiasharp-4-0-is-here-announcing-the-first-stable-release-net-blog.md`. confidence: 1 vendor benchmark source, last-confirmed 2026-07-03.
- SkiaSharp now has a more predictable milestone cadence through stable and preview channels, with Uno Platform co-maintenance and Graphite backend work in preview. Source: `raw/2026-07-03-web-dotnet-skiasharp-4-0-is-here-announcing-the-first-stable-release-net-blog.md`. confidence: 1 source, last-confirmed 2026-07-03.

### Typed entities
- library: SkiaSharp
- version: 4.148.0
- engine: Skia m148
- library: HarfBuzzSharp
- feature: animated WebP encoding
- backend: Graphite
- partner: Uno Platform

### Explicit relationships
- SkiaSharp 4 supersedes v3 for teams that need the newer Skia engine, cleaned APIs, lifecycle fixes, and predictable milestone cadence.
- Graphics performance claims depend-on workload, GPU backend, driver, and UI composition.
- Uno Platform co-maintenance complements Microsoft ownership by adding active downstream renderer pressure.

### HoneyDrunk implications
- For .NET graphics, MAUI, Blazor, or creative-tool experiments, evaluate SkiaSharp 4 in a branch with visual regression and performance checks before upgrading shared code.
- Treat Graphite as preview-scouting until package maturity and target-platform behavior are verified.

### Quality notes
- Microsoft/.NET Blog source is authoritative for release existence. Performance and compatibility need local validation.

## 2026-07-04 compile additions: .NET 8/9 support deadline and WinApp CLI package identity

### Source-backed claims
- .NET 8 and .NET 9 both reach end of support on 2026-11-10; after that date Microsoft will stop servicing updates, security fixes, and technical support for those versions. Source: `raw/2026-07-04-web-net-8-and-net-9-will-reach-end-of-support-on-november-10-2026-net-blog.md`. confidence: 1 .NET Blog source, last-confirmed 2026-07-04.
- .NET 10 is an LTS release supported through November 2028 and is the recommended upgrade target from .NET 8 or .NET 9 in the captured source. Source: `raw/2026-07-04-web-net-8-and-net-9-will-reach-end-of-support-on-november-10-2026-net-blog.md`. confidence: 1 source, last-confirmed 2026-07-04.
- WinApp CLI lets .NET desktop applications test package identity through `dotnet run` after `winapp init`, and package applications as signed MSIX with `winapp pack`. Source: `raw/2026-07-04-web-packaging-and-package-identity-for-net-apps-with-winapp-cli-on-windows-net-blo.md`. confidence: 1 .NET Blog source, last-confirmed 2026-07-04.
- WinApp CLI initialization can add Windows App SDK and WinApp build tooling package references, generate `Package.appxmanifest` and assets, and allow apps to access Windows features gated behind package identity such as notifications, background tasks, file handlers, share target, and Windows AI APIs. Source: `raw/2026-07-04-web-packaging-and-package-identity-for-net-apps-with-winapp-cli-on-windows-net-blo.md`. confidence: 1 source, last-confirmed 2026-07-04.

### Typed entities
- runtime: .NET 8
- runtime: .NET 9
- runtime: .NET 10
- date: 2026-11-10 .NET 8/9 end of support
- tool: WinApp CLI
- command: `winapp init`
- command: `winapp pack`
- package: `Microsoft.WindowsAppSDK`
- package: `Microsoft.Windows.SDK.BuildTools.WinApp`
- artifact: MSIX
- file: `Package.appxmanifest`
- concept: package identity

### Explicit relationships
- .NET 10 supersedes .NET 8/9 as the supported LTS target after the 2026-11-10 support deadline.
- Unsupported .NET versions continue to run but no longer receive security servicing, which affects runtime inventory and patch policy.
- WinApp CLI complements ordinary .NET desktop tooling by registering package identity for local run/debug and generating MSIX distribution artifacts.
- Package identity enables Windows APIs that are unavailable to unpackaged desktop apps.

### HoneyDrunk implications
- Inventory HoneyDrunk .NET 8 and .NET 9 targets before 2026-11-10 and plan upgrades to .NET 10 or later.
- If HoneyDrunk desktop tools need Windows notifications, background tasks, file handlers, or Windows AI APIs, test WinApp CLI on a branch and review generated manifests/assets before adopting.

### Quality notes
- Microsoft/.NET Blog sources are authoritative for support timing and tooling direction. The Visual Studio installer behavior comment in the raw source was not promoted because it appears as user discussion rather than official guidance.

## 2026-08-12 compile additions: .NET 11 Preview 7 and August 2026 servicing

### Source-backed claims
- .NET 11 Preview 7 includes library/runtime/SDK/C#/ASP.NET Core/MAUI/EF Core/F#/Windows Forms updates, including IEEE 754 decimal floating-point types, generic complex support, HTTP request compression, HTTP connection eviction, DNS record resolution APIs, ZIP password-related APIs, and JSON polymorphism inference. Source: `raw/2026-08-12-rss-net-blog-net-11-preview-7-is-now-available.md`. confidence: 1 .NET Blog source, last-confirmed 2026-08-12.
- The same preview source says NativeAOT CLI support is enabled by default, MSBuild server is default, `dotnet test` gains run-level timeout and max-failed-tests controls, traversal-project support improves, and container publishing prefers platform-native local runtimes. Source: `raw/2026-08-12-rss-net-blog-net-11-preview-7-is-now-available.md`. confidence: 1 source, last-confirmed 2026-08-12.
- .NET 11 Preview 7 adds C# features such as labeled `break`/`continue`, union patterns, exhaustiveness checks for closed type parameters, Unsafe Evolution compatibility mode, and `nameof` improvements. Source: `raw/2026-08-12-rss-net-blog-net-11-preview-7-is-now-available.md`. confidence: 1 source, last-confirmed 2026-08-12.
- ASP.NET Core preview items include automatic pausing of Blazor circuits, `CacheView` SSR output caching, QuickGrid scrolling updates, OpenAPI 3.2 server-sent-events description support, and SignalR client auth refresh after redirects. Source: `raw/2026-08-12-rss-net-blog-net-11-preview-7-is-now-available.md`. confidence: 1 source, last-confirmed 2026-08-12.
- MAUI preview items include cross-platform passkey authentication, XAML incremental Hot Reload, route templates, AOT-safe RelativeSource improvements, and third-party backend support. Source: `raw/2026-08-12-rss-net-blog-net-11-preview-7-is-now-available.md`. confidence: 1 source, last-confirmed 2026-08-12.
- Microsoft August 2026 servicing posts provide security and non-security fixes for .NET 10.0.11, 9.0.19, and 8.0.30, with multiple CVEs affecting supported .NET trains and separate .NET Framework security updates. Source: `raw/2026-08-12-web-dotnet-framework-august-2026-servicing-updates.md`; page: [[dotnet-dependency-security-and-nuget]]. confidence: 1 Microsoft servicing source, last-confirmed 2026-08-12.

### Typed entities
- runtime: .NET 11 Preview 7
- runtime: .NET 10.0.11
- runtime: .NET 9.0.19
- runtime: .NET 8.0.30
- feature: IEEE 754 decimal floating-point types
- feature: NativeAOT CLI default
- tool behavior: MSBuild server default
- command: `dotnet test`
- framework: ASP.NET Core
- framework: .NET MAUI
- component: Windows Forms
- vulnerability class: information disclosure
- vulnerability class: security feature bypass
- vulnerability class: denial of service
- vulnerability class: elevation of privilege
- vulnerability class: remote code execution

### Explicit relationships
- .NET 11 Preview 7 previews future runtime and SDK direction but does not supersede supported production release trains.
- August 2026 servicing supersedes earlier .NET 10/9/8 patch levels for security posture.
- NativeAOT, MSBuild server, and test-run controls affect CI/runtime behavior and should be treated as toolchain changes, not only language/runtime changes.

### HoneyDrunk implications
- Inventory HoneyDrunk .NET 8/9/10 runtimes for August 2026 servicing uptake, especially internet-facing services and build images.
- Keep .NET 11 Preview 7 experimentation isolated from production branches until APIs, SDK defaults, and hosting behavior are validated.
- Before adopting NativeAOT or MSBuild server defaults broadly, verify build determinism, diagnostics, and CI worker behavior.

### Quality notes
- Microsoft release and servicing sources are authoritative for release existence. CVE-specific urgency depends on HoneyDrunk runtime inventory and exposure.

## 2026-08-14 compile additions: Microsoft.Testing.Platform report surface

### Source-backed claims
- Microsoft.Testing.Platform 2.3+ reporting can produce inline failure annotations, provider job summaries, live Azure DevOps result publishing, crash-resilient TRX files, HTML/JUnit/CTRF reports, and schema-versioned JSON test discovery. Source: `raw/2026-08-14-rss-net-blog-test-reporting-in-microsoft-testing-platform-from-red-build-t.md`; page: [[microsoft-dotnet-ai-stack]]. confidence: 1 .NET Blog source, last-confirmed 2026-08-14.
- Azure DevOps-only history options can annotate failures as known-flaky or regression-like, demote known flakes to warnings, and detect slow tests against historical runtime; these options require REST API access through the pipeline token. Source: `raw/2026-08-14-rss-net-blog-test-reporting-in-microsoft-testing-platform-from-red-build-t.md`. confidence: 1 source, last-confirmed 2026-08-14.
- MTP suppresses banners, ANSI escapes, and progress animation in agent/LLM environments and defaults stdout/stderr display to failed tests, making command output easier for automated tooling to consume. Source: `raw/2026-08-14-rss-net-blog-test-reporting-in-microsoft-testing-platform-from-red-build-t.md`. confidence: 1 source, last-confirmed 2026-08-14.

### Typed entities
- platform: Microsoft.Testing.Platform
- version: 2.3+
- reporter: GitHub Actions
- reporter: Azure DevOps
- report: TRX
- report: JUnit XML
- report: CTRF JSON
- file: `testconfig.json`
- file: `Directory.Build.props`

### Explicit relationships
- Structured test reports complement coding agents by replacing terminal scraping with versioned test metadata and source-linked failure annotations.
- Crash-resilient TRX reporting preserves partial evidence when a test host fails before normal serialization.
- Repo-level testconfig and MSBuild properties supersede per-developer shell-history settings for consistent local/CI reporting.

### HoneyDrunk implications
- For .NET repositories, consider centralizing MTP report settings once one-project validation confirms useful annotations and artifact shape.
- Keep GitHub and Azure DevOps reporter feature differences explicit; do not assume flaky-history triage exists on GitHub Actions yet.

### Quality notes
- Microsoft source is authoritative for MTP direction. Preview reporters and framework adapter requirements should be verified per repository.

## 2026-08-26 compile additions: .NET 11 launch schedule and C# 15 preview

### Source-backed claims
- .NET Conf 2026 is scheduled as a free online event from 2026-11-10 through 2026-11-12 and is positioned as the .NET 11 launch event. Source: `raw/2026-08-26-rss-net-blog-net-conf-2026.md`; page: [[microsoft-dotnet-ai-stack]]. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-08-26.
- Microsoft says .NET 11 previews include runtime, libraries, SDK, ASP.NET Core, C#, .NET MAUI, Entity Framework Core, and other updates, with highlighted items including C# 15 union types, MAUI CoreCLR for Android/iOS/Mac Catalyst, richer Blazor SSR/form validation, smaller Blazor WebAssembly apps, Minimal API async validation and union type support, and OpenAPI 3.2 by default. Source: `raw/2026-08-26-rss-net-blog-net-conf-2026.md`. confidence: 1 source, last-confirmed 2026-08-26.
- The C# 15 preview source says C# 15 ships with .NET 11 in November and is available in .NET 11 Preview 7. Source: `raw/2026-08-26-rss-net-blog-explore-new-features-available-in-c-15-preview.md`; page: [[csharp-memory-safety-and-unsafe-code]]. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-08-26.

### Typed entities
- event: .NET Conf 2026
- runtime: .NET 11
- language version: C# 15
- framework: ASP.NET Core
- framework: Blazor
- framework: .NET MAUI
- framework: Entity Framework Core
- standard: OpenAPI 3.2

### Explicit relationships
- .NET Conf 2026 complements .NET 11 migration planning by giving a concrete launch window and expected session surface.
- .NET 11 preview features do not supersede supported production baselines until GA and repository-specific validation.
- MAUI CoreCLR and Blazor/Minimal API changes depend-on target app shape, platform support, and build/deployment tooling.

### HoneyDrunk implications
- Keep .NET 11 preview checks separate from .NET 8/9/10 servicing work until .NET 11 is GA.
- Before adopting C# 15 language features in public APIs, verify tooling, analyzers, OpenAPI/serialization output, and downstream consumer support.

### Quality notes
- Microsoft source is authoritative for event and preview direction. Sessions, final SDK behavior, and migration costs remain live facts.

## 2026-09-04 compile additions: MSTest Native AOT test lanes

### Source-backed claims
- MSTest 4.4 can publish test projects as Native AOT executables using source generation, so teams can run tests against the runtime shape they intend to ship instead of only a managed test host. Source: `raw/2026-09-04-rss-net-blog-test-what-you-ship-mstest-and-native-aot.md`; page: [[microsoft-dotnet-ai-stack]]. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-09-04.
- Microsoft warns that a managed test pass can hide Native AOT or trimming problems, especially around serialization, reflection, dependency injection, configuration, plugins, and third-party dependencies; native lanes should start with representative smoke/regression tests and compare test counts against managed discovery. Source: `raw/2026-09-04-rss-net-blog-test-what-you-ship-mstest-and-native-aot.md`. confidence: 1 source, last-confirmed 2026-09-04.
- The source lists current MSTest Native AOT limitations including direct `[TestClass]` requirements, accessibility/static/generic constraints, unsupported generic/ref/out/in test methods, AssemblyFixtureProvider replacement needs, and unavailable integrations/extensions/reporters beyond supported outputs such as TRX and Code Coverage. Source: `raw/2026-09-04-rss-net-blog-test-what-you-ship-mstest-and-native-aot.md`. confidence: 1 source, last-confirmed 2026-09-04.

### Typed entities
- test framework: MSTest 4.4
- runtime mode: Native AOT
- property: `PublishAot`
- package: `MSTest.Sdk/4.4.0`
- test platform: Microsoft.Testing.Platform
- report: TRX
- report: Code Coverage

### Explicit relationships
- Native AOT testing complements .NET runtime adoption by checking publish-time/trimming behavior in the shipped artifact.
- Managed test success does not supersede native test evidence for AOT-published applications.
- Native test-lane scope depends-on RID, AOT-compatible test shape, reporter support, and dependency behavior.

### HoneyDrunk implications
- For HoneyDrunk .NET applications that target Native AOT, add a native lane gradually and gate it on representative scenarios plus managed/native discovery parity.
- Do not migrate all tests to Native AOT by default; keep a faster managed lane and reserve native execution for release, scheduled, or AOT-sensitive checks until cost is measured.

### Quality notes
- Microsoft source is authoritative for MSTest feature posture as captured. Validate SDK version, RID publishing, and reporter compatibility in each repo before standardization.
## 2026-09-08 compile additions: September servicing and .NET Conf Community Days

### Source-backed claims
- The September 2026 .NET servicing release updates .NET 10 to 10.0.12, .NET 9 to 9.0.20, and .NET 8 to 8.0.31, with security/non-security fixes and matching ASP.NET Core, EF Core, runtime, container-image, and Linux-package release artifacts. Source: `raw/2026-09-08-rss-net-blog-net-and-net-framework-september-2026-servicing-releases-updat.md`; page: [[microsoft-dotnet-ai-stack]]. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-09-08.
- The same servicing source lists CVE-2026-69805, CVE-2026-69439, CVE-2026-71328, CVE-2026-69522, CVE-2026-69304, CVE-2026-58649, CVE-2026-66822, and CVE-2026-69806 as addressed for applicable .NET versions; CVE-2026-69522 also applies to .NET Framework 4.6.2 through 4.8.1. Source: `raw/2026-09-08-rss-net-blog-net-and-net-framework-september-2026-servicing-releases-updat.md`. confidence: 1 source, last-confirmed 2026-09-08.
- .NET Conf 2026 Community Days CFP is open from 2026-09-08 to 2026-10-06, accepts 30-minute remote talks plus Q&A, prefers .NET 11 demonstrations, and covers web, native, mobile, desktop, AI, IoT, game development, containers, microservices, ML, data, DevOps, and open-source .NET projects. Source: `raw/2026-09-08-rss-net-blog-net-conf-2026-community-days-call-for-presenters-is-open.md`. confidence: 1 Microsoft .NET Blog source, last-confirmed 2026-09-08.

### Typed entities
- runtime: .NET 10.0.12
- runtime: .NET 9.0.20
- runtime: .NET 8.0.31
- runtime: .NET Framework 4.6.2-4.8.1
- event: .NET Conf 2026 Community Days
- date: 2026-10-06 CFP deadline

### Explicit relationships
- September servicing supersedes prior supported-runtime patch levels for security posture.
- .NET Framework servicing overlaps with modern .NET servicing where CVE-2026-69522 applies across both runtime families.
- Community Days depends-on practical implementation submissions and complements the Microsoft-led first two .NET Conf days.

### HoneyDrunk implications
- Patch or at least triage every supported HoneyDrunk .NET runtime and container image against the September 2026 release notes.
- If HoneyDrunk submits or tracks .NET Conf content, the relevant CFP deadline is 2026-10-06.

### Quality notes
- Official release notes are high-authority but operational applicability depends on local runtime inventory, package locks, and container base images.

## 2026-09-10 .NET 11 RC1 and C# union support

### Sources
- [.NET Blog: Announcing .NET 11 Release Candidate 1](../raw/2026-09-10-rss-net-blog-announcing-net-11-release-candidate-1.md)
- [.NET Blog: Use C# unions and closed hierarchies in ASP.NET Core](../raw/2026-09-10-rss-net-blog-use-c-unions-and-closed-hierarchies-in-asp-net-core.md)

### Typed entities
- `runtime`: .NET 11 RC1
- `language`: C# 15
- `framework`: ASP.NET Core
- `library`: System.Text.Json
- `feature`: union types
- `feature`: closed class hierarchies

### Claims
- .NET 11 RC1 was published on 2026-09-08 with a go-live license and tooling support in Visual Studio 2026 Insiders and VS Code C# Dev Kit. confidence: 1 source, last-confirmed 2026-09-10
- .NET 11 RC1 includes cross-stack updates spanning libraries, runtime, SDK, MSBuild, NuGet, C# 15, F#, ASP.NET Core, .NET MAUI, and Windows Forms. confidence: 1 source, last-confirmed 2026-09-10
- ASP.NET Core can serialize and bind C# 15 union types and closed hierarchies through System.Text.Json for JSON bodies, Minimal APIs, MVC, SignalR JsonHubProtocol, Blazor interop/persistence/prerendered parameters, and OpenAPI schemas. confidence: 1 source, last-confirmed 2026-09-10
- C# union support does not apply to query strings, route values, headers, or form fields, and SignalR MessagePack/Newtonsoft protocols do not support the union feature described in the source. confidence: 1 source, last-confirmed 2026-09-10

### Explicit relationships
- C# 15 union types use compiler exhaustiveness checks to model a fixed set of possible case types.
- Closed class hierarchies depend-on related controlled class families and can use inferred System.Text.Json polymorphism with a discriminator.
- ASP.NET Core OpenAPI generation represents union shapes as `anyOf`, which depends-on client support for polymorphic schemas.

### HoneyDrunk implications
- Treat .NET 11 RC1 as testable for production-shaped previews because of go-live support, but keep deployment behind package/runtime inventory and rollback checks.
- Prefer union types for established discriminator-free contracts or unrelated cases; prefer closed hierarchies with discriminators for new controlled related contracts.
- Add tests for unsupported binding paths before exposing unions through route/query/header/form surfaces.

### Quality notes
- Microsoft release and feature guidance is authoritative for framework behavior; validate preview tooling and generated OpenAPI output against local clients before adoption.

## 2026-09-14: Fetch Metadata protection in preview 6

### Typed entities

project: ASP.NET Core; concept: Fetch Metadata CSRF protection; concept: antiforgery tokens.

### Claims and evidence

- Lock's captured account describes Fetch Metadata-based CSRF protection in .NET 11 preview 6 and different adoption paths for Blazor SSR/Minimal APIs versus MVC/Razor Pages. Existing token validation can remain active; the author's removal experiment is explicitly unverified. confidence: 1 source, last-confirmed 2026-09-14 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-13-rss-andrew-lock-automatic-csrf-protection-based-on-fetch-metadata-headers-.md)

### Explicit relationships

ASP.NET Core uses browser request-context headers to classify request origins; CSRF configuration depends-on endpoint type and framework version.

### Decision and quality notes

Preview-era practitioner evidence only. Changing defenses requires primary release documentation and endpoint/browser tests; this capture does not justify removing token validation. Source count is provisional single-source support; repeated citations and derived summaries add no independent corroboration. Open question: Which endpoint types, cookie settings, browsers, and released ASP.NET Core versions must be tested before changing Fetch Metadata or token-based CSRF protection? See [[indexes/gaps]].

## 2026-09-14: Host capacity versus process allocation

### Typed entities

project: .NET; concept: host logical processor count; concept: process CPU allocation.

### Claims and evidence

- Lock distinguishes host logical processor totals from Environment.ProcessorCount, which the captured account says reflects process restrictions in modern .NET. His platform-specific host-count sample had not shipped in production. confidence: 1 source, last-confirmed 2026-09-14 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-13-rss-andrew-lock-finding-the-total-number-of-processors-on-a-machine-with-n.md)

### Explicit relationships

Capacity diagnostics depends-on an explicit host-versus-process definition; the sample uses OS-specific discovery.

### Decision and quality notes

Use this as a diagnostic-design distinction, with container and topology validation before implementation. A host total does not establish an appropriate worker concurrency limit. Source count is provisional single-source support; repeated citations and derived summaries add no independent corroboration. Open question: Which HoneyDrunk diagnostics need host CPU totals versus process allocation, and how will container limits, CPU topology changes, and caching be validated? See [[indexes/gaps]].

## 2026-09-14: Preview union serialization boundaries

### Typed entities

library: System.Text.Json; concept: union types; concept: closed class hierarchies.

### Claims and evidence

- In Lock's .NET 11 preview 7 walkthrough, primitive unions serialize directly while class members need suitable polymorphic configuration. Accessibility, nested inheritance, and deserialization complicate round trips. The capture mentions subsequent RC1 API changes without establishing their final behavior. confidence: 1 source, last-confirmed 2026-09-14 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-13-rss-andrew-lock-the-pain-of-serializing-unions-and-closed-class-hierarchie.md)

### Explicit relationships

Union JSON contracts depends-on System.Text.Json polymorphic configuration; this preview account qualifies the API-surface discussion in [[microsoft-dotnet-ai-stack]].

### Decision and quality notes

This does not contradict later ASP.NET integration claims: versions and layers differ. Validate concrete bidirectional contracts on the chosen release; do not carry preview limitations forward as confirmed current behavior. Source count is provisional single-source support; repeated citations and derived summaries add no independent corroboration. Open question: Which union and closed-hierarchy request/response shapes need serialization, deserialization, nested-type, and generated-client tests on the actual .NET release? See [[indexes/gaps]].

## 2026-09-15: Preview buffer ownership transfer

### Typed entities

project: .NET; library: System.Text.StringBuilder; concept: buffer ownership transfer; project: Roslyn.

### Claims and evidence

- Lock's June 23 preview account describes StringBuilder.MoveChunks as transferring internal character chunks to a new builder and emptying the original, avoiding an intermediate ToString allocation. Retaining the original reference therefore does not retain ownership of the transferred content. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-andrew-lock-avoiding-tostring-allocations-with-stringbuilder-movechunk.md)
- The proposed Roslyn SourceText integration was not shipped functionality in this account, and source-generator target-framework constraints remained unresolved. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-andrew-lock-avoiding-tostring-allocations-with-stringbuilder-movechunk.md)

### Explicit relationships

MoveChunks uses ownership transfer; allocation savings depend-on the consumer accepting builder content. This extends the runtime topic without establishing Roslyn availability.

### Decision and quality notes

Practitioner preview summary. Benchmark allocation, storage reuse, and downstream immutability on the target SDK before adopting the pattern. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which text-generation paths can accept transferred builder chunks, and what target-SDK, allocation, reuse, and immutability tests decide whether MoveChunks helps? See [[indexes/gaps]].


## 2026-09-15: Concurrent subprocess output draining

### Typed entities

project: .NET; library: System.Diagnostics.Process; concept: redirected output; concept: pipe deadlock.

### Claims and evidence

- Lock describes a deadlock when a parent reads redirected stdout and stderr sequentially while the child fills the other pipe. His existing-API pattern starts both asynchronous reads before awaiting completion. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-andrew-lock-improvements-to-reading-process-outputs-exploring-the-net-.md)
- The July 7 .NET 11 preview account describes coordinated text, byte, and line capture, including stream identity for line APIs and bounded waiting through timeouts or cancellation. It does not establish final released SDK behavior. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-14-rss-andrew-lock-improvements-to-reading-process-outputs-exploring-the-net-.md)

### Explicit relationships

Subprocess capture depends-on draining both pipes. Coordinated readers address the deadlock mechanism behind the earlier Process API entry; [[ai-agent-harnesses]] uses subprocess wrappers as tool boundaries.

### Decision and quality notes

This adds mechanism and version context to existing Process coverage, not a contradictory release claim. Cancellation of a read is not evidence that a child process was terminated. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which agent/build subprocess wrappers can fill either redirected pipe, and how will concurrent draining, cancellation, child lifetime, and target-SDK behavior be tested? See [[indexes/gaps]].

## 2026-09-15: Closed hierarchy exhaustiveness in preview 5

### Typed entities

project: .NET; concept: closed class hierarchy; concept: exhaustive switch; concept: union; concept: compiler metadata.

### Claims and evidence

- Lock's preview 5 account describes closed bases limiting direct derivation to their assembly, allowing missing-case checks in switch expressions. Derived classes are not automatically closed; sealing all cases enables further impossible-conversion checks. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-andrew-lock-closed-class-hierarchies.md)
- Closed hierarchies use inheritance while unions describe permitted alternatives without that requirement. The article's language settings and temporary ClosedAttribute workaround belong to preview 5, not an established current installation recipe. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-andrew-lock-closed-class-hierarchies.md)

### Explicit relationships

Exhaustive switches depend-on compiler knowledge of permitted alternatives. This modeling account complements the later serialization limitations already recorded on this page.

### Decision and quality notes

Historical practitioner preview evidence. Generic restrictions and consuming-assembly metadata require target-SDK checks; no temporary workaround is recommended for adoption. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which domain alternatives benefit from closed hierarchies versus unions, and how do target-SDK switch, generic, derivation, and serialization checks behave? See [[indexes/gaps]].


## 2026-09-15: Device-bound session renewal

### Typed entities

concept: Device Bound Session Credentials; concept: device-bound key; concept: challenge-response; concept: cookie replay.

### Claims and evidence

- Lock describes DBSC as registering a device-bound public key and renewing short-lived cookies through proof of private-key possession. His refresh account checks signature, active session identity, and challenge before issuing another cookie. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-andrew-lock-device-bound-session-credentials.md)
- Unsupported browsers retain ordinary cookie behavior in this progressive-adoption account. The post reports implementation and ad-blocker difficulties and points toward framework support; device binding does not establish protection from every compromised-device scenario. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-andrew-lock-device-bound-session-credentials.md)

### Explicit relationships

Cookie renewal depends-on key possession and session validation. Replay resistance uses device binding; unsupported clients retain the ordinary cookie threat model.

### Decision and quality notes

Practitioner synthesis, not specification conformance or current browser coverage proof. No custom authentication implementation or security guarantee follows from ingestion. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which browser and ASP.NET Core versions support the intended DBSC flow, and how will renewal, fallback, blockers, and compromised-device limits be tested? See [[indexes/gaps]].


## 2026-09-15: Runtime performance evidence at release candidate

### Typed entities

project: .NET; library: BenchmarkDotNet; concept: JIT optimization; concept: runtime configuration; concept: representative hot path.

### Claims and evidence

- Toub's release-candidate-era survey covers JIT, runtime async, GC, startup, threading, collections, I/O, networking, JSON, diagnostics, and other library performance work. Identical-code comparisons use .NET 10 and .NET 11 Release builds; other examples compare alternatives on one runtime. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-dotnet-11-performance-improvements.md)
- The survey cautions that microbenchmarks vary with hardware, OS, runtime settings, and surrounding activity. Improvements in an affected pattern do not establish equivalent whole-application speedup. confidence: 1 source, last-confirmed 2026-09-15 (archived capture reviewed; no live refresh). [captured source](../raw/2026-09-15-rss-dotnet-11-performance-improvements.md)

### Explicit relationships

Upgrade performance conclusions depend-on representative hot paths and deployment configuration. JIT changes can affect existing code; API-level optimization uses different evidence than runtime-only comparisons.

### Decision and quality notes

Official engineering summary with reproduction-oriented examples, not a benchmark run in this pass. Release-candidate context does not establish production readiness. New source-specific claims remain provisional single-source evidence; repeated citations and derived summaries add no independent corroboration. Open question: Which HoneyDrunk hot paths and runtime configurations should compare .NET 10 and 11, and what application-level measurements and compatibility checks qualify an upgrade? See [[indexes/gaps]].

## 2026-09-18: Browser compute and worker lifetime

### Typed entities

project: Blazor; project: .NET 11; concept: Web Worker; concept: runtime isolation; concept: serialization boundary.

### Claims and evidence

- Lock describes a .NET 11 preview 3 worker project, JSExport methods, and asynchronous WebWorkerClient invocation to move CPU-intensive work off the browser UI thread. Merely awaiting a CPU-bound method does not relocate its computation. confidence: 1 source, last-confirmed 2026-09-18 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-16-rss-andrew-lock-blazor-web-workers.md)
- Each worker initializes an isolated .NET runtime; reuse can amortize startup while ownership, disposal, and complex-result serialization remain explicit concerns in the example. confidence: 1 source, last-confirmed 2026-09-18 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-16-rss-andrew-lock-blazor-web-workers.md)

### Explicit relationships

Responsive browser computation uses worker isolation; useful speedup depends-on startup, memory, serialization, and workload cost.

### Decision and quality notes

May preview evidence. The newly clipped article does not supersede the later RC1 coverage above or establish current template/package behavior. Source-specific claims remain provisional single-source evidence; related sources and derived summaries are not independent confirmation of these details. Open question: Which Blazor workloads justify a reused worker, and what target-SDK tests measure startup, memory, serialization, disposal, and UI responsiveness? See [[indexes/gaps]].

## 2026-09-18: Union modeling in historical preview evidence

### Typed entities

project: C#; project: .NET 11; concept: union type; concept: exhaustiveness; concept: nullable alternative.

### Claims and evidence

- Lock describes preview 4 unions as a fixed choice among potentially unrelated types, with switch-expression exhaustiveness warnings and explicit null handling for nullable cases. The article discusses generated wrappers and UnionAttribute/IUnion conventions. confidence: 1 source, last-confirmed 2026-09-18 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-16-rss-andrew-lock-csharp-union-types.md)
- The captured installation and helper-type guidance is specific to the May preview. Its modeling distinction between explicit alternatives and informally interpreted object results does not establish current SDK or IDE support. confidence: 1 source, last-confirmed 2026-09-18 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-16-rss-andrew-lock-csharp-union-types.md)

### Explicit relationships

Union modeling uses enumerated outcomes; API adoption depends-on representation and serialization checks. The existing closed-hierarchy comparison remains the canonical related guidance.

### Decision and quality notes

Practitioner preview summary. Preserve newer RC1 and serialization qualifications; no contradictory release claim or new independent implementation verification. Reuse the 2026-09-15 closed-hierarchy/union validation question in [[indexes/gaps]]. Source-specific claims remain provisional single-source evidence; related sources and derived summaries are not independent confirmation of these details.


## 2026-09-19: Contextual options and rename-sensitive configuration

### Typed entities

person: Andrew Lock; library: Microsoft.Extensions.Options.Contextual; concept: contextual options; concept: generated context receiver.

### Claims and evidence

- Lock’s April example supplies caller context to an asynchronous options provider, using an OptionsContext partial type, IOptionsContextReceiver, and IContextualOptions. It contrasts arbitrary context with a fixed collection of named configurations. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-rss-dotnet-contextual-options-tradeoffs.md)
- The example’s receiver depends on property-name strings, leaving rename-related coupling. The cited package is 10.4.0-preview.1.26160.2; its experimental API usage, including generated code, required explicit EXTEXP0018 suppression at publication. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-18-rss-dotnet-contextual-options-tradeoffs.md)

### Explicit relationships

Contextual configuration uses generated context and a receiver; adoption depends-on rename behavior and target-package maturity.

### Decision and quality notes

Historical April practitioner evidence, newly clipped in September. It does not establish present package maturity or replace newer runtime release evidence. Indirection is a design tradeoff rather than proof of reduced coupling. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which configuration cases need arbitrary caller context rather than named options, and what rename, asynchronous-loading, generated-code, and target-package tests would qualify contextual options? See [[indexes/gaps]].


## 2026-09-19: Constant byte spans require target-specific IL verification

### Typed entities

person: Andrew Lock; library: System.Memory; concept: `ReadOnlySpan<byte>`; concept: constant assembly data; concept: emitted IL.

### Claims and evidence

- Lock shows a compiler optimization where `ReadOnlySpan<byte>` points into constant assembly data without array allocation/copying, including a .NET Framework example using System.Memory. The walkthrough verifies address/length construction in emitted IL and relates UTF-8 literals to the mechanism. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-dotnet-readonlyspan-constant-data.md)
- The demonstrated portable case depends on immutable access, constant elements, and byte-sized primitives. Changing element types or using nonconstant values can introduce allocations; array-like source syntax alone does not establish allocation behavior. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-dotnet-readonlyspan-constant-data.md)

### Explicit relationships

Allocation avoidance depends-on compiler lowering and target build; constant spans use existing assembly data.

### Decision and quality notes

April technical reference, not a new runtime release. Inspect the actual compiled target and measure protocol-table or parsing workloads before claiming savings. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which fixed byte tables qualify for constant-span lowering, and what emitted-IL and allocation measurements verify every HoneyDrunk target/compiler configuration? See [[indexes/gaps]].


## 2026-09-19: Fetch Metadata distinguishes browser request context

### Typed entities

person: Andrew Lock; concept: Sec-Fetch-Site; concept: Sec-Fetch-Dest; concept: Sec-Fetch-Mode; concept: Sec-Fetch-User; concept: CSRF.

### Claims and evidence

- Lock explains site relationships, resource destinations, navigation/CORS modes, and user activation through Fetch Metadata headers. Same-site is broader than same-origin, so subdomain and port treatment matters when defining a policy. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-fetch-metadata-request-boundaries.md)
- The article distinguishes sending cross-origin requests from script access to responses: a no-CORS request can reach a server despite an opaque response. CORS alone is not complete CSRF protection. confidence: 1 source, last-confirmed 2026-09-19 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-19-rss-fetch-metadata-request-boundaries.md)

### Explicit relationships

Browser request policy uses context headers; safe rejection rules depend-on legitimate navigation, embedded resources, and integrations. This grounds the earlier ASP.NET Core preview discussion.

### Decision and quality notes

Practitioner background, not a complete production middleware configuration or a basis to remove antiforgery tokens. Related Lock articles are not independent verification of released framework behavior. Source-specific claims remain provisional single-source evidence; related articles and derived summaries add no independent support. Open question: Which same-site subdomains, ports, user navigations, embedded resources, and cross-site integrations must remain valid under HoneyDrunk browser-facing request policies? See [[indexes/gaps]].
