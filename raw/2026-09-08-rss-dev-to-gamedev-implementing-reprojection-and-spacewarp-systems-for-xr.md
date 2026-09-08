---
source: "https://dev.to/beefedai/implementing-reprojection-and-spacewarp-systems-for-xr-172k"
title: "Implementing Reprojection and Spacewarp Systems for XR"
author: "beefed.ai"
date_published: "2026-09-08"
date_clipped: "2026-09-08"
category: "Game Development / Unity"
source_type: "rss"
---

# Implementing Reprojection and Spacewarp Systems for XR

Source: https://dev.to/beefedai/implementing-reprojection-and-spacewarp-systems-for-xr-172k

beefed.ai
Posted on Sep 8
•
Originally published at beefed.ai
Implementing Reprojection and Spacewarp Systems for XR
# gamedev
The engine symptom you actually care about is not “lower FPS” — it’s visual discontinuities and drifting cues that break vestibular-visual coupling: doubled edges on nearby geometry, head-locked HUD swim, shimmering reflections, and inconsistent input-to-display timing that produces user discomfort and reduced task performance. Those are the failure modes ATW/Spacewarp are designed to mask; done poorly they become new, equally toxic artifacts.
Contents
Anchoring Perception: Reprojection Fundamentals and Goals
Implementing Asynchronous Timewarp (ATW) for Rotational Correction
Generating Synthetic Frames: Spacewarp and Motion-Vector Reprojection
Wiring into the XR Compositor: Timing, Prediction, and Latency Budgets
Measuring Success: Tests, Metrics, and Artifact Mitigation
Practical Implementation Checklist and Example Code
Anchoring Perception: Reprojection Fundamentals and Goals
Start from the perceptual target: keep the image that reaches the retina consistent with the user's latest head pose and the scene’s motion state so the vestibular system and eyes remain in agreement. The practical metrics that follow from that are:
Motion-to-photon (M2P) latency target: industry practitioners aim for a system M2P under ~20 ms to avoid a large portion of latency-driven discomfort.
Primary objective for reprojection: prevent rotational judder by warping the last completed frame to match the latest head orientation (that’s what Asynchronous Timewarp / ATW does).
Secondary objective: when the app cannot render at the native refresh ratio, synthesize plausible intermediate frames that advance animation and translation (that’s Spacewarp / motion-vector frame synthesis).
Frame generation strategies are insurance, not replacements. Treat ATW/Spacewarp as controlled approximations: they should reduce perceptual disruptions during occasional overruns, not let an application persistently run at wildly inadequate budgets. Meta’s precedent is explicit: these systems are designed to save occasional frames but can’t substitute for steady full-rate rendering.
Important: Reprojection trades correct instantaneous geometry for stable temporal continuity . That trade is acceptable for the human visual system up to a point — beyond that point the artifacts become distracting or nauseating.
Implementing Asynchronous Timewarp (ATW) for Rotational Correction
Why ATW first? Rotation-only warping is cheap, robust, and covers the dominant perceptual error when the user turns their head. The canonical ATW design is a small, high-priority, late-executing pipeline that takes the last fully-rendered eye buffers and reprojects them from the renderer’s pose to the most recent/ predicted display pose.
Core pieces and implementation specifics
Data you need:
Last completed eye-images (left/right color buffers).
The pose used when those images were rendered (call this pose_render ).
The latest predicted pose for scanout (call this pose_display ), normally derived from the runtime’s predictedDisplayTime . Use xrWaitFrame /frame timing to get this in OpenXR.
Compute the delta rotation:
R_delta = R_display * inverse(R_render)
For orientation-only ATW you can ignore translation; use a 3x3 rotation or quaternion math for direction vectors.
Warp shader approach (cheap, widely used):
Reconstruct an eye ray from the pixel's UV and the original projection; rotate that direction by R_delta and reproject to new UV; sample the original color buffer. This is a 2D remap implemented in a fragment or compute shader. Using a single bilinear sample plus a simple hole-filling pass keeps latency low.
Timing & scheduling constraints
Run the ATW pass as late as possible — ideally within a few milliseconds before scanout. On a 90Hz HMD one vsync is ~11.1 ms; successful ATW needs to complete with a comfortable margin (we typically engineer for <2–3 ms execution + submission latency on the target hardware). Missing that window causes ATW to fail to save the frame.
To get that late execution you either need:
very fine-grained GPU preemption and driver/OS support (the hard path), or
a dedicated, high-priority compute context or small dedicated compute queue (where supported by drivers and APIs), plus careful command recording to limit work. NVIDIA and AMD have provided VR extensions and driver assistance to support such workflows.
Example: simple ATW fragment shader (GLSL, conceptual)
#version 450
layout ( binding = 0 ) uniform sampler2D uPrevColor ;
layout ( push_constant ) uniform Push { mat3 R_delta ; mat4 projInv ; mat4 proj ; } pc ;
in vec2 vUV ;
out vec4 oColor ;
void main () {
// Reconstruct view-space direction
vec4 ndc = vec4 ( vUV * 2 . 0 - 1 . 0 , 1 . 0 , 1 . 0 );
vec4 viewDir = pc . projInv * ndc ; viewDir /= viewDir . w ;
vec3 dir = normalize ( viewDir . xyz );
// Rotate direction
vec3 dirWarp = pc . R_delta * dir ;
// Project back to NDC and UV
vec4 proj = pc . proj * vec4 ( dirWarp , 0 . 0 );
vec2 uvNew = proj . xy / proj . w * 0 . 5 + 0 . 5 ;
// Sample last frame
oColor = texture ( uPrevColor , uvNew );
}
Enter fullscreen mode
Exit fullscreen mode
Practical tips
Keep the ATW shader tiny (no heavy math, no texture fetch chains besides the color sample and maybe an optional depth-aware improvement). ATW is your safety net — the sooner and lighter the better.
Use layered/blit-friendly framebuffers to minimize costly transitions; single-pass stereo will reduce duplication if your API supports it ( single-pass instanced in Vulkan/GL, or SV_RenderTargetArrayIndex patterns in D3D).
Test ATW with an artificially delayed renderer to validate that ATW actually executes under stress. Meta provides blog guidance and tools for this.
Generating Synthetic Frames: Spacewarp and Motion-Vector Reprojection
Rotational warps freeze animated objects relative to the last rendered frame — that freezes object motion and produces multiple images of moving objects. Spacewarp extends ATW by estimating per-pixel motion and depth and synthesizing frames that advance animation and translation.
Two common approaches
Frame-extrapolation using two previous frames (classical ASW / blend-and-extrapolate)
Use frames N-2 and N-1 and compute an estimate of scene motion to generate N. This is what early ASW and SteamVR Motion Smoothing do: extrapolate motion and interpolate texture samples to synthesize the intermediate frame. Works well for linear or low-frequency motion.
Motion-vector reprojection (higher-fidelity)
Require the renderer to produce a motion vector buffer (per-pixel or per-tile velocities in screen or world space) and a depth buffer. The compositor or an interstitial shader uses those vectors to reproject pixels forward in time; disocclusion holes are filled using depth-informed dilation, neighbor blending, or a small spatial inpainting pass. This is the approach used in modern motion smoothing implementations and in compositor-driven frame generation.
What to produce from the render pipeline
Color (rendered eyes)
Depth (linear or non-linear min/max)
Motion vectors (commonly: clip-space or world-space velocity per pixel)
Optional: object IDs or velocity buffers for problematic elements (particles, HUDs, hands)
Basic shader flow for motion-vector reprojection (conceptual HLSL)
Texture2D prevColor : register ( t0 );
Texture2D motionVec : register ( t1 ); // (dx,dy) in UV units
Texture2D depth : register ( t2 );
SamplerState s : register ( s0 );
float4 PS_Reproject ( VS_TO_PS input ) : SV_Target {
float2 uv = input . uv ;
float2 mv = motionVec . Sample ( s , uv ). xy ; // velocity per frame interval
float2 uv_prev = uv - mv ; // where this pixel came from
float4 col = prevColor . Sample ( s , uv_prev );
// Optional: depth-aware hole fill and weighting
// .. detect disocclusion and apply neighbor fill ..
return col ;
}
Enter fullscreen mode
Exit fullscreen mode
Valve’s Motion Smoothing and Microsoft’s motion reprojection use GPU motion vectors (sometimes derived from the hardware video encoder or the game engine TAA motion vectors) to extrapolate the new image; that reduces repeated single-frame reuse artifacts and better advances animated content.
Tradeoffs and failure modes
ASW can create “disocclusion trails” where geometry moves and reveals previously occluded regions; good depth buffers reduce this but do not eliminate it.
Rapid brightness changes, complex translucency, or shader-based procedural motion (particles, screen-space reflections) can be mispredicted and produce tearing / ghosting.
Motion vectors must be correct and coherent (consistent with depth and world motion). Cheap or noisy motion vectors cause smear and ghosting; invest in accurate velocity generation in the renderer.
Wiring into the XR Compositor: Timing, Prediction, and Latency Budgets
Correct compositor integration is non-negotiable: the runtime and compositor are the authority for predictedDisplayTime , vsync intervals, and whether a frame should render or be skipped. Use the platform APIs exactly as intended.
Use xrWaitFrame / XrFrameState::predictedDisplayTime as the single source of truth for display timing. Compute your simulation advancement and camera pose using that time and feed it consistently to rendering threads and the compositor submission. xrWaitFrame communicates the runtime's prediction for when the next composited frame will be displayed; you must thread that timestamp through your game pipeline.
OpenXR advice and compositor cooperation
xrWaitFrame returns predictedDisplayTime and predictedDisplayPeriod ; use those values as the anchor for your physics and animation advance so layered updates remain consistent. XrFrameState::shouldRender can signal when the runtime would prefer you skip heavy work.
Use composition layers for head-locked UI (HUDs, menus) so the compositor can track them separately and keep them crisp under reprojection. Meta recommends head-locked layers for HUDs to avoid HUD-specific judder.
Compositor timing primitives you can read (OpenVR/OpenXR)
In OpenVR, IVRCompositor::GetFrameTiming / Compositor_FrameTiming exposes detailed timing metrics (running start, GPU vs CPU breakdown, number of dropped frames) that are invaluable during integration and profiling. Use that to locate whether the bottleneck is CPU submission or GPU work.
Latency budget example (approximate)
Sensor sampling + fusion: 1–3 ms
Pose prediction & engine simulation: 1–3 ms
Application CPU work + command submission: 2–6 ms
GPU render: 3–8 ms (highly scene-dependent)
Compositor/scanout + display persistence: 1–4 ms
Total goal: <20 ms M2P in aggregate (industry target). Jitter reduction is as important as mean latency.
GPU preemption & scheduling
ATW and late-spacewarp passes demand fine-grained preemption or prioritized compute scheduling to run reliably late in the frame; Meta and GPU vendors worked on driver/OS primitives to enable this behavior (e.g., VRWorks context priority). Without such support, ATW may miss the display deadline.
On platforms that lack preemption, design your renderer to expose predictable, short-latency points where the warp task can safely run (for example by breaking large draws into smaller chunks or using compute-based rendering for expensive passes).
Measuring Success: Tests, Metrics, and Artifact Mitigation
You cannot fix what you don't measure. Use both automated telemetry and perceptual tests.
Essential metrics and tools
Motion-to-photon (M2P) — measure end-to-end using photodiode + motion stimulus or hardware timing rigs in the lab; aim for <20 ms.
Frame delivery statistics — counts of dropped frames, reprojected frames, m_nNumDroppedFrames , m_nNumReprojectedFrames from compositor APIs (OpenVR/OpenXR runtimes expose these).
Jitter — standard deviation of frame times (ms). Low jitter is as important as low mean.
Perceptual difference — compute SSIM or per-pixel difference between a ground-truth synthesized render and the composited result during controlled motion tests.
Tools: RenderDoc for frame inspection and to validate motion vectors & depth exports; Microsoft PIX and NVIDIA Nsight to capture CPU/GPU timing and visualize pipeline stalls; runtime-specific frame timing overlays (SteamVR Advanced Frame Timing, Meta performance HUD).
Artifact mitigation checklist (concrete)
Generate and submit a real depth buffer and motion vector buffer every frame (use XrCompositionLayerDepthInfoKHR if available) so the runtime can perform depth-aware spacewarp. Using depth reduces disocclusion artifacts dramatically.
Make HUDs and text head-locked layers that the compositor can handle separately — this avoids HUD drift when spacewarp is active.
Keep the frame interval stable: avoid fluctuating GPU loads that cause frequent toggles between native and half-rate — those toggles produce visible popping and tracking artifacts. Prefer a controlled fall to a half-rate rather than a chaotic frame delivery pattern.
Ensure motion vectors are in a consistent space (prefer world-space velocities where possible) and exclude or specially handle non-geometric content (particles, screen-space effects).
Practical Implementation Checklist and Example Code
Actionable, ordered protocol you can implement in one sprint
Tracking & Prediction
Deliver IMU and camera fusion at high rate; expose a predictPose(displayTime) API that produces pose_display for the compositor’s predictedDisplayTime . Propagate this predicted time into your simulation step.
Frame outputs (per-eye)
Produce color , depth , and motion vector buffers each frame. Use single-pass stereo if the engine supports it. Motion vectors must be correct for moving objects and camera motion (store world-space velocity if possible).
Engine timing loop (OpenXR-flavored pseudocode)
// Main render loop (concept)
while ( xrSessionRunning ) {
XrFrameState frameState {};
xrWaitFrame ( session , NULL , & frameState ); // predictedDisplayTime returned here
XrTime targetTime = frameState . predictedDisplayTime ;
// Advance simulation to the display time so animation and physics correlate
Simulation . AdvanceTo ( targetTime );
xrBeginFrame ( session , nullptr );
// Acquire swapchain images, render color/depth/motionVectors
RenderLayer ( colorSwapchain , depthSwapchain , motionVectorSwapchain , targetTime );
// Submit layers (include depth/motion buffers if runtime supports them)
xrEndFrame ( session , & frameEndInfo ); // displayTime == targetTime
}
Enter fullscreen mode
Exit fullscreen mode
Cite: Use xrWaitFrame ’s predictedDisplayTime as the single timing anchor.
ATW thread
Spawn a short-lived high-priority worker that:
reads the last completed color buffers and pose_render .
samples the latest predicted pose ( pose_display ) right before scanout.
dispatches the small ATW compute/frag pass and submits results to the compositor.
Implement a fast-path where the compositor accepts a warped buffer; otherwise fallback to the original buffer.
Spacewarp / motion-vector reprojection
If the runtime supports a spacewarp composition extension (or XR_KHR_composition_layer_depth ) submit motionVectorSubImage and depthSubImage alongside the color layer so the runtime/compositor can produce higher-quality synthetic frames. If not, implement an in-engine fallback that synthesizes intermediate frames using the two previous color buffers + motion vectors with depth-aware hole fill.
Profiling & validation
Capture representative scenes with RenderDoc and verify:
motion vectors direction & magnitude,
depth precision and near/far range,
that ATW shader inputs are the last frame’s pose and color.
Use Nsight Systems / PIX to identify CPU/GPU stalls, thread preemption issues, and to confirm ATW completes within the allocated late window.
Example: shallow motion-vector reprojection fragment (conceptual)
// Inputs: prevColor, prevDepth, motionVec
vec2 uv = vUV ;
vec2 mv = texture ( motionVec , uv ). xy ;
vec2 uv_src = uv - mv ; // backwards reprojection
vec4 color = texture ( prevColor , uv_src );
// detect hole (depth discontinuity) and do small dilate or neighbor blend
if ( isHole ( uv_src , prevDepth )) {
color = neighborFill ( prevColor , uv_src );
}
Enter fullscreen mode
Exit fullscreen mode
Table: Quick comparison
Technique
Fixes
Requires
Typical artifacts
Cost (relative)
ATW
Rotational jitter
last color buffer, pose delta
Frozen moving objects, reflection mismatch
Low
ASW / Frame Extrapolation
Adds synthetic frames for translation/animation
last 2 color frames (optionally depth)
Disocclusion trails, ghosting
Medium
Motion-vector reprojection
Better animation/translation handling
motion vectors + depth
Fewer trails; depends on vector quality
Medium–High
Sources
Asynchronous Timewarp Examined — Meta Developer Blog - Explains ATW design, limitations, GPU preemption needs, and perceptual failure modes that guide ATW architecture.
Asynchronous Spacewarp — Meta Developer Blog - Describes ASW’s frame-extrapolation approach, when it engages, known artifacts, and developer recommendations (e.g., head-locked layers).
OpenXR Specification — xrWaitFrame / Frame Timing - Defines predictedDisplayTime , predictedDisplayPeriod , and best practices for passing display time through the engine pipeline.
Introducing SteamVR Motion Smoothing — Valve/Steam Announcement - Describes SteamVR’s Motion Smoothing (motion-vector-based reprojection) and the rationale for compositor-driven frame synthesis.
SteamVR — Frame Timing (Valve Developer Community) - Practical reference for compositor timing primitives (IVRCompositor timings) and how to read frame timing breakdowns.
Latency and Cybersickness: Impact, Causes, and Measures — Frontiers in Virtual Reality (review) - Evidence and synthesis on M2P thresholds, jitter effects, and perceptual guidance (industry target ≈20 ms).
VRWorks — Context Priority (NVIDIA Developer) - Discussion of GPU scheduling/prioritization primitives that make late-timewarps feasible on PC GPUs.
timewarp_gl — ILLIXR plugin README - Example of a real-world asynchronous rotational reprojection implementation used in a research runtime.
RenderDoc — Official site - Frame capture and shader-level inspection tool (useful to validate motion vectors, depth, and warp shader behavior).
NVIDIA Nsight Systems — Developer Documentation - System-level profiling for CPU/GPU interactions, frame-stall detection, and latency analysis.
A final operational truth: reprojection systems are powerful tools that buy you milliseconds — and freedom from sudden judder — but they are not substitutes for predictable, budgeted rendering. Treat ATW and spacewarp as engineered insurance: lightweight, late, and measured. Apply the checklists above; measure everything; and instrument your compositor hooks so the runtime — not the renderer — remains the final arbiter of display timing.
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
