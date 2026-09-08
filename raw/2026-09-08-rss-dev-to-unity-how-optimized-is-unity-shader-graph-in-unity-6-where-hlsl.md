---
source: "https://dev.to/gamedevtoollab/how-optimized-is-unity-shader-graph-in-unity-6-where-hlsl-still-wins-4222"
title: "How Optimized Is Unity Shader Graph in Unity 6? Where HLSL Still Wins"
author: "GameDevToolLab"
date_published: "2026-09-08"
date_clipped: "2026-09-08"
category: "Technical Art & Creator Tools"
source_type: "rss"
---

# How Optimized Is Unity Shader Graph in Unity 6? Where HLSL Still Wins

Source: https://dev.to/gamedevtoollab/how-optimized-is-unity-shader-graph-in-unity-6-where-hlsl-still-wins-4222

GameDevToolLab
Posted on Sep 8
How Optimized Is Unity Shader Graph in Unity 6? Where HLSL Still Wins
# unity3d
# gamedev
# shadergraph
# graphics
A few years ago, I treated Shader Graph as a prototyping tool. When a shader became performance-sensitive, I often rewrote the bottleneck in HLSL because stage placement, precision, branching, reuse, and pass structure were easier to control by hand.
So how much of that old rule still applies?
This article uses Unity 6.3 LTS (6000.3) and Shader Graph 17.3 as the baseline: Shader Graph package information .
For ordinary URP and HDRP materials, starting with Shader Graph is a reasonable default. Do not rewrite a finished graph in HLSL just because it is a graph. Inspect the generated shader and measure the target GPU first.
If Shader Graph and handwritten HLSL express the same work in the same stage, with the same precision, samples, branches, passes, and pipeline features, both eventually enter the platform shader compiler. Their final code may be similar, though identical output is not guaranteed.
The useful question is therefore: what work is executed, in which stage, how many times, and across how many passes and variants?
This is not a fixed-hardware benchmark. It is a guide to what Shader Graph generates, what it does not optimize for you, and when profiling should push you toward Custom Function or handwritten ShaderLab/HLSL.
Three layers you should not confuse
Separate the graph , Unity-generated ShaderLab/HLSL , and the platform-compiled GPU code . Nodes are not runtime objects executed one by one; Shader Graph generates source, then normal shader compilation takes over.
That is why a 100-node graph does not mean 100 runtime function calls, and why a long generated file is not automatically slow. Pipeline templates, varyings, keywords, lighting integration, and helper code can inflate source length. Conversely, a tiny handwritten shader can still be expensive if it performs many texture reads, screen-space operations, or loops.
Compare generated passes/stages, texture samples, branch structure, varyings/register pressure, variant count, warm-up, and finally GPU time on the target device.
What Shader Graph optimizes today
Modern Shader Graph is best treated as a shader code generator and authoring system , not a runtime abstraction layer.
Stage
What it can do
What it will not do for you
Shader Graph generation
Trace dependencies, generate per-pass/per-stage code, emit fields/varyings
Redesign your algorithm, always choose the optimal stage, merge every redundant sample
HLSL compilation
Constant folding, dead-code elimination, inlining
Produce identical machine code on every GPU
Driver/backend
Generate target-specific instructions
Guarantee the same register/instruction count as handwritten HLSL
Unconnected nodes normally do not become runtime work
Shader Graph 17.3 collects nodes upstream from active Master Stack blocks/output nodes. Unity's implementation is visible in Generator.cs and GenerationUtils.cs . A disconnected experiment therefore does not automatically run every frame.
A connected Detail Map whose strength is 0 at runtime is different: unless the compiler can prove the path unnecessary, the sample may remain.
Code is generated per pass and stage
Targets/SubTargets define pass requirements. A simple-looking material may still participate in Forward, Depth, ShadowCaster, DepthNormals, MotionVectors, and other passes. Vertex deformation can therefore be repeated in shadow/depth passes.
Custom Interpolators move suitable work to the vertex stage
Custom Interpolators can pass vertex-calculated values to the fragment stage. A candidate must be vertex-valid, interpolation-safe, within the varying budget, and supported on every target. Shader Graph exposes up to 32 channels, each float4-equivalent , while real hardware/API limits can be lower. Check whether the value replaces an existing varying or merely adds another one.
Precision is controllable
Shader Graph supports Single and Half precision: Precision Modes . Start with Single for large ranges, accumulated time, and precision-sensitive UV math; test Half for normals, colors, directions, and limited-range masks. FP16 behavior varies by GPU/backend, so verify final code and image quality.
Branch node, static variants, and Dynamic Branch are different
Branch node: both inputs are evaluated
Unity's Branch node is effectively generated as:
void Unity_Branch_float4 ( float Predicate , float4 True , float4 False , out float4 Out )
{
Out = Predicate ? True : False ;
}
Enter fullscreen mode
Exit fullscreen mode
The True and False inputs are computed before the helper selects one. If both sides contain expensive samples or math, both sides remain work. See Branch node . It is useful for selecting values, not reliably disabling an expensive feature.
Shader Feature / Multi Compile: separate variants
Static keywords generate separate variants. Inside a compiled variant, an inactive path can be constant-folded or removed. Keep this separate from build stripping , which decides which variants survive into the Player.
Shader Feature generally makes unused combinations easier to strip; Multi Compile retains combinations more aggressively. See Unity's branching guidance and the Shader Graph keyword reference .
Dynamic Branch: one runtime program
A Shader Graph keyword defined as Dynamic Branch produces one runtime program with a uniform branch; Unity sends its state as a uniform integer for the draw: Keyword concepts .
So the keyword itself is not normally a per-pixel predicate. Classic wave/warp divergence is more relevant to a varying branch in custom HLSL , for example one driven by texture data. For Dynamic Branch keywords, measure branch overhead, both paths living in one program, register pressure, instruction-cache pressure, and path asymmetry.
Do not choose Dynamic Branch only because a value changes often. Static variants can also be selected at runtime if the required variants survived stripping. Compare variant count, switching granularity, path cost, warm-up, memory, and GPU time.
What Shader Graph still does not optimize for you
Duplicate work: repeated Sample Texture nodes are not guaranteed to collapse into one fetch. Reuse sampled results where possible; Sub Graphs are not memoization caches.
Expensive algorithms: triplanar mapping, POM, procedural noise, Scene Color/Depth, transcendental math, extra lights, and shadows remain expensive when their underlying work is expensive.
Overdraw: transparency, full-screen effects, particles, foliage, and decals can remain fill-rate problems. Alpha Clip has different behavior from blending but still interacts with discard, early depth, MSAA, and dense overlap.
Pipeline features: shadows, fog, decals, SSAO, motion vectors, and pipeline textures are not automatically "Shader Graph overhead." A handwritten comparison is unfair if it simply removes those features.
Variant explosion: ten independent two-way keywords already imply 1024 theoretical combinations before passes and pipeline keywords. This can hurt compile time, build size, loading, memory, and warm-up.
Think in three budgets: GPU execution , CPU/render submission , and build/load/variant cost .
When Custom Function or handwritten HLSL is worth it
Situation
Start with
Same passes/stages/samples/precision and already within budget
Keep Shader Graph
A local formula, loop, or special sample is awkward in nodes
Custom Function
Custom passes, unusual buffers, stencil/render-state control dominate
Handwritten ShaderLab/HLSL
The real issue is overdraw, pass count, lighting, or coverage
Fix rendering design first
Custom Function is useful when most of the graph is productive but one algorithm needs explicit HLSL. Check the official Custom Function Node rules for $precision , _half / _float suffixes, include guards, texture wrapper types, and Shader Model/API/Target restrictions.
Moving the same expression into a Custom Function does not automatically make it faster. The gain comes when handwritten code enables a real algorithm or execution-structure improvement.
A practical optimization workflow
Count texture samples before nodes. A graph with many arithmetic nodes can be cheap; dependent texture reads can dominate. Sample once and reuse where possible.
Separate affine from nonlinear vertex work. uv * tiling + offset , including uniform scrolling, is affine and can often move across interpolation without changing the result except for finite precision. sin , noise, normalization, and distance-based distortion are nonlinear; compare sparse meshes and the lowest LOD.
Choose precision from numeric range. Use Single for large ranges/accumulation; test Half for normals, colors, directions, and masks. Verify long runtimes and low-end targets.
Choose branching for its trade-off. Branch node = both inputs; Dynamic Branch = one uniform runtime program; Shader Feature/Multi Compile = variants; varying custom-HLSL branch = potential lane divergence.
Inspect every pass. Disable unnecessary transparency, Alpha Clip, Two Sided, Receive Shadows, and related features. Remember that vertex work can repeat in ShadowCaster/depth passes.
Avoid giant keyword-driven uber shaders when features barely overlap. Separate graphs or quality-specific graphs may be simpler.
Keep CPU and GPU shader optimization separate. The SRP Batcher improves CPU setup/state changes; it does not merge draw calls like GPU Instancing, nor does it directly remove fragment instructions.
How to compare Shader Graph and HLSL fairly
Keep the rendering specification identical: pipeline, renderer, surface mode, passes, lights, textures/samplers, precision, keywords, mesh, camera, resolution, Render Scale, MSAA, and quality settings. If the handwritten shader drops a feature or pass, you are measuring a specification change.
Use a Development Build for Unity Profiler and diagnostic logs. For final A/B decisions, use a product-like measurement build matching the shipping Graphics API, Render Pipeline Asset, quality, resolution, IL2CPP configuration, and shader stripping, with only the hooks needed by your GPU tool.
Unity 6.3's GPU Usage Profiler is unavailable or restricted on several configurations. Check the GPU Usage Profiler documentation and use RenderDoc, PIX, Xcode GPU tools, Android GPU Inspector, or platform-specific timing when appropriate. Frame Debugger is for draw/pass inspection, not GPU timing.
Warm caches. Control VSync, Dynamic Resolution, frame caps, power state, background work, and device temperature. Measure A→B and B→A; record sample count, median, p95, and thermal state. If the difference is below the noise floor, treat it as no meaningful difference. Amplified tests are useful for diagnosis, but make the final decision in the real scene. Measure GPU milliseconds , not only FPS.
Inspect generated code and variant logs
View Generated Shader / See Generated Code lets you check passes, stages, samples, keywords, precision, and varyings.
For per-shader build information, search Editor.log for Compiling shader ; Unity reports variant counts before and after stripping: shader variant counts .
For URP aggregate stripping information in Unity 6.3 :
Open Edit > Project Settings > Graphics and select the URP tab.
Under Additional Shader Stripping Settings , set Shader Variant Log Level to anything except Disabled .
Enable Development Build in File > Build Profiles and build.
Inspect the Shader Stripping section in Console or Editor.log .
With Export Shader Variants enabled, Unity documents Temp/graphics-settings-stripping.json and Temp/shader-stripping.json : URP shader stripping .
Two tiny generated-code tests
Use a fixed baseline such as Unity 6.3 LTS, Shader Graph 17.3, URP Unlit, Opaque, Alpha Clip off, Single precision .
Disconnected sample
Graph A samples one texture into Base Color. Graph B adds a second disconnected Sample Texture node. Search generated code for the second texture/sample reference. If it is absent, you have directly verified dependency-driven generation for that case. This does not prove that connected equivalent expressions are always merged.
Branch versus keyword
Create a heavy Detail path with an extra texture sample. Compare a Branch node, a Boolean Dynamic Branch keyword, and the same keyword as Shader Feature. Inspect branch/ #pragma structure and build variant counts; verify whether the static OFF variant removes the Detail sample.
Practical examples
Scrolling water UVs: pure uv * scale + offset is affine and can be a good vertex-stage candidate. If you also move noise, sin , normalization, or distance-dependent distortion, compare the lowest LOD because those operations are nonlinear.
Detail Map on/off: Branch can still evaluate Detail upstream; Dynamic Branch keeps one runtime program; Shader Feature can remove the OFF path but needs variant management; Multi Compile retains combinations more aggressively.
Full-screen procedural noise: multiple noise octaves plus Scene Color distortion are expensive in both Shader Graph and HLSL. Try lower resolution, fewer octaves, smaller coverage, precomputed textures, LUTs, or approximations before rewriting. Handwritten HLSL matters when it enables real algorithmic changes such as early exits or specialized loops.
Decision flow
Build the same rendering specification in Shader Graph.
Inspect passes, stages, texture samples, branches, varyings, and variants.
Measure GPU time, image quality, loading, and stutter on the target device.
Fix sample reuse, stage placement, coverage, passes, and keyword design first.
Move only the remaining bottleneck to Custom Function or handwritten HLSL when the measured gain exceeds maintenance and portability cost.
For Unity 6.3 / Shader Graph 17.3, the useful shift from the old mindset is: Shader Graph can be the starting implementation; generated code and target-device profiling define the boundary where handwritten shader code becomes justified.
Release checklist
[ ] Product-like build: GPU time and image quality checked.
[ ] A/B tests use identical rendering specifications and conditions.
[ ] Caches warmed; median, p95, sample count, and thermal state recorded.
[ ] Generated code checked for samples, stages, branches, varyings, and passes.
[ ] Dynamic Branch keywords are not confused with varying per-pixel branches.
[ ] Static variant counts, stripping, and required runtime combinations verified.
[ ] Custom Interpolators checked for replacing versus adding varyings.
[ ] Half/Single verified on the target backend/GPU and against image quality.
[ ] Overdraw, Alpha Clip, lighting, and pipeline costs separated from authoring-format cost.
[ ] Any HLSL rewrite produces a repeatable gain larger than noise and maintenance cost.
References
Unity 6.3: Shader Graph package
Shader Graph 17.3: Branch node
Shader Graph 17.3: Keyword concepts
Unity 6.3: Shader branching
Shader Graph 17.3: Custom Interpolators
Shader Graph 17.3: Custom Function Node
Unity 6.3: GPU Usage Profiler
Unity 6.3: URP shader stripping
Unity 6.3: SRP Batcher
Top comments (0)
Subscribe
Personal
Trusted User
Create template
Templates let you quickly answer FAQs or store snippets for re-use.
Submit
Preview
Dismiss
Code of Conduct
•
Report abuse
Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink .
Hide child comments as well
Confirm
For further actions, you may consider blocking this person and/or reporting abuse
