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
