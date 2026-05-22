# C# Memory Safety and Unsafe Code

## Decision-useful summary
C# is adding a stricter caller-unsafe model, nominally C# 16, previewing with .NET 11 and planned for production in .NET 12. The shift makes unsafe code a reviewable contract rather than just a pointer-syntax context: unsafe operations need inner `unsafe { }` blocks, APIs that pass safety obligations to callers use unsafe signatures plus `/// <safety>` docs, and boundary methods must discharge obligations with guards or documented invariants. For HoneyDrunk, this is a useful compiler-enforced guardrail against AI-generated or dependency-sourced memory unsafety, especially in tool runners, native interop, high-performance code, and C# game/engine integrations. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md]

## Claims
- Microsoft says the redesigned `unsafe` model will preview in .NET 11 and is planned as a production feature in .NET 12, initially opt-in with templates expected to enable it later similarly to nullable reference types. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md]
- The new model makes `unsafe` a caller-facing safety contract: calling an unsafe member requires an inner `unsafe { }` block, and unsafe signatures propagate obligations up the call graph unless a safe boundary method discharges them. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md]
- Unsafe operations are no longer limited to pointer syntax; the model covers APIs and operations the compiler cannot prove maintain the invariant that every memory access targets allocated, initialized, live memory. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md]
- The model requires unsafe operations to be scoped with inner `unsafe` blocks even inside unsafe members, and violations are intended to be compile errors rather than warnings. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md]
- C# safety documentation uses `/// <safety>` blocks for caller obligations and `// SAFETY:` implementation comments for local reasoning; analyzers are expected to flag missing safety docs. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md]
- Project adoption has two independent switches: the new safety-model opt-in property controls caller-unsafe propagation, while existing `<AllowUnsafeBlocks>` controls whether any unsafe keyword/use is allowed; with new model on and `AllowUnsafeBlocks=false`, unsafe API calls fail at compile time. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md]
- The .NET runtime libraries are migrating toward the new model and reducing unsafe code, including replacing some unsafe memory reads/writes with safe alternatives such as `BitConverter` where possible. confidence: 1 source, last-confirmed 2026-05-22. [source: raw/2026-05-22-rss-net-blog-improving-c-memory-safety.md]

## Typed entities
- language: C#
- version: C# 16
- runtime/platform: .NET 11 preview
- runtime/platform: .NET 12 planned production
- keyword: `unsafe`
- keyword: `safe`
- project property: `<AllowUnsafeBlocks>`
- documentation tag: `/// <safety>`
- implementation comment: `// SAFETY:`
- API family: `System.Runtime.CompilerServices.Unsafe`
- API family: `System.Runtime.InteropServices.Marshal`
- type/API: `NativeMemory`
- type/API: `MemoryMarshal`
- type/API: `SafeHandle`
- concept: caller unsafe
- concept: unsafe boundary method
- concept: live-memory invariant
- concept: undefined behavior
- related language: Rust
- related language: Swift

## Explicit relationships
- C# 16 unsafe propagation uses explicit unsafe member signatures to pass safety obligations to callers.
- Inner `unsafe { }` blocks depend-on safety comments and guards to make each unsafe operation reviewable.
- Boundary methods suppress unsafe propagation only when they discharge callee obligations through runtime guards, static reasoning, or upstream invariants.
- `<AllowUnsafeBlocks>false</AllowUnsafeBlocks>` blocks unsafe code and, under the new model, also blocks unsafe API calls that would require unsafe call-site blocks.
- Pointer and `IntPtr` signatures no longer by themselves define the safety contract; dereference/unsafe member use is the review point.
- C# 16's model resembles Rust's `unsafe fn`/`unsafe {}` separation more than legacy C# 1.0 unsafe contexts.
- [[dotnet-runtime-and-mobile-2026]] tracks the .NET 11 platform context in which the preview model appears.
- [[ai-coding-agent-security]] uses compiler-enforced unsafe blocking as a supply-chain/AI-generated-code guardrail.

## HoneyDrunk implications
- For .NET tools/agents, keep `AllowUnsafeBlocks=false` unless a project explicitly needs native interop or performance unsafe code.
- When the preview is available, test enabling the new safety model on internal .NET repos to turn unsafe API use into compile-time review points.
- If unsafe is required, demand `/// <safety>` docs and `// SAFETY:` comments in code review; missing docs should fail analyzer/lint gates.
- Prefer safe APIs (`SafeHandle`, typed wrappers, `BitConverter`, bounds-checked spans) before accepting `Unsafe`, `Marshal`, `IntPtr`, or raw pointer surfaces.

## Confidence and quality notes
- Quality posture: decision-usable for .NET coding standards and AI-code guardrails; syntax/property names may shift before .NET 11 preview/GA, so verify current docs before implementation.
- Weak spots: single official preview/planning source; do not assume exact final C# 16 syntax until shipped.
- Privacy filter: no private code, pointers, or memory addresses copied.
