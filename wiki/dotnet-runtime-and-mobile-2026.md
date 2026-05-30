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
