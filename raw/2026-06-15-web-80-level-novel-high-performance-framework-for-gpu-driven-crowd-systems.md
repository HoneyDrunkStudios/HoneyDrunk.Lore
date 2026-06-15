---
source: "https://80.lv/articles/6-000-agents-on-one-game-thread-novel-high-performance-framework-for-gpu-driven-crowd-systems"
title: "Novel High-Performance Framework for GPU-Driven Crowd Systems"
author: "80 Level"
date_published: "2026-06-10"
date_clipped: "2026-06-15"
category: "Technical Art & Creator Tools"
source_type: "web"
---

# Novel High-Performance Framework for GPU-Driven Crowd Systems

Source: https://80.lv/articles/6-000-agents-on-one-game-thread-novel-high-performance-framework-for-gpu-driven-crowd-systems

Yeonju "Kaley" Cho shows us how to create a whole stadium of people with a framework for GPU-driven crowd systems using Houdini and Unreal Engine and explained the logic, texturing, and animation behind the project.

### Introduction

Hi, I'm Kaley Cho, a Technical Artist dedicated to exploring the technical boundaries of real-time environments. I’ve always been fascinated by the challenge of balancing extreme visual density with high performance, and this project was born out of a desire to see if I could create a truly massive, reactive crowd that feels alive without taxing the CPU. It was an incredibly rewarding puzzle to solve, bridging the gap between procedural Houdini setups and optimized Unreal Engine shaders.

Populating a massive boxing stadium with over 6,000 reactive spectators typically pushes CPU-bound skeletal mesh systems to their limit. By offloading character deformation to the GPU using **Vertex Animation Textures (VAT)**, I can maintain high frame rates while retaining high-fidelity motion. This breakdown explores a complete pipeline from procedural Houdini setups to shader-based animation triggering, focused on core technical art principles for modern game development.

This article walks through the full pipeline from raw stadium geometry to a living, breathing crowd.

*The finished system: 6,072 spectators animating in real time, controlled by a live UI. GPU Time: 17.51 ms. Draw Calls: 276.*

### Part 1: Building the Foundation in Houdini

#### Step 1: Extracting Seat Positions

The first problem is simple to state and annoying to solve manually: where does every spectator sit, and which direction do they face? Placing 6,000 transforms by hand is not an option, so the stadium's own seat geometry does the work instead.

The stadium FBX is imported into Houdini, the chair geometry is isolated, and a For Each loop iterates over every connected piece. Inside the loop, a VEX wrangle uses getbbox() to find the bounding box of each seat and drops a single point at its center using addpoint(). The result is a clean point cloud with no extra geometry.

### VEX wrangle placing a point at the bounding box center of each seat piece.

Unreal Engine utilizes a **Z-up** coordinate system, while Houdini defaults to **Y-up**. To ensure your VAT positions align with the static mesh instances in-engine, swap the Y and Z attributes and negate the new Y.

// Houdini Z -> Unreal Front/Back

// Houdini X -> Unreal Left/Right

// Houdini Y -> Unreal Up/Down

@P = set(@P.z, -@P.x, @P.y);

// Apply the same remap to normals

@N = set(@N.z, -@N.x, @N.y);

The final node in the chain is the **Labs CSV Exporter**. Only the four attributes that Unreal needs are exported: RowName, Index, P (position, split into Px/Py/Pz), and N (normal, split into Nx/Ny/Nz). The result is a lightweight spreadsheet that becomes the single source of truth for all 6,000+ seat transforms.

Inside Unreal, this CSV is imported as a **Data Table** using a custom struct S_CrowdTable. The result is a perfectly organized table of every seat in the arena.

### The S_CrowdTable Data Table in Unreal Engine. Each row contains a unique index and world-space position and normal for one seat.

### Part 2: Baking the VAT in Houdini

#### Character Pipeline

Each spectator character goes through a preparation pass first. The mesh is cleaned, poly-reduced to an appropriate LOD for the stands, and material groups are assigned (Body, Shirt, Hair) so the Unreal material can apply randomized colors per group.

### The deform mesh preparation network: polyreduce, fuse, clean, and OUT_DeformMesh null output.

### Character with material groups assigned and visible in the viewport – body (blue), shirt (green), hair (red). This grouping later drives per-instance color randomization in the shader.

#### Baking Multiple Animation States

The crowd needs more than one animation. It needs: **Idle** (seated, subtle movement), **Clap**, **Yell**, and **Stand**. Each animation is a separate VAT bake.

The network uses a shared OUT_DeformMesh that feeds into four parallel ProcessCharacter nodes, one per animation state. Each branch deforms the mesh through the animation frames and outputs to its own OUT_ null, which the Labs VAT ROP then reads.

### The shared deform mesh feeds four ProcessCharacter branches, producing OUT_Idle, OUT_Clap, OUT_Yell, and OUT_Stand.

#### VAT ROP Settings

The **Labs Vertex Animation Textures** ROP handles the actual export. A few settings here are critical:

**Method: Soft (Constant Topology)**— The mesh topology never changes between frames, which is required for VAT to work correctly.**Raster Depth: 16-Bit Floating Point**— This is non-negotiable. 8-bit textures don't have enough precision to store world-space position offsets without visible vertex jitter, especially when the camera is close to the stands.**Pack Normals into Position Alpha**— Packs the normal data into the alpha channel of the position texture, saving a texture slot.**Engine: Unreal Engine**— Sets the correct output coordinate conventions for UE.

### The Labs VAT ROP configured for the Idle animation. Note the 16-bit floating point raster depth and Soft (Constant Topology) method. Each of the five animations (Idle, Clap, Yell, Stand, Wave) has its own ROP node.

### Part 3: The Unreal Engine Shader

The material (M_VAT_HISM) is where the GPU does all its thinking. It reads the VAT textures, scrolls them in time, blends between animation states, randomizes colors, and handles the wave effect, all without a single CPU instruction per instance during runtime.

#### UV: Scrolling Through the Animation Texture

The core mechanic of VAT is that each animation frame is a horizontal row in the texture. To play the animation, the shader scrolls the V coordinate downward over time. The UV section handles this, building a time loop based on FPS and frame count parameters, then using PerInstanceRandom to offset each instance's start time so they don't all animate in sync. Without this, 6,000 characters would read as a single tiling texture rather than independent agents.

#### WPO: Dynamic Animation Blending

The World Position Offset section reads five animation textures simultaneously (Anim1–Anim4 for the four base states, plus AnimWave). Each texture's RGB stores compressed position offsets, and the bounding box min/max parameters are used to decompress them back to world-space values. A chain of Lerp nodes then blends between the active states based on alpha values driven by the UI sliders.

#### Normal: Unpacking Compressed Normals

Normals are decompressed using a custom material function MF_VAT_UnpackNormal, which reconstructs the Z component from the packed X and Y values, then Lerped in sync with the WPO blending. The same Lerp chain from the WPO section is mirrored here to keep normals consistent with the animated positions.

#### Wave: A GPU-Driven Stadium Wave

The wave behavior is the showpiece of the system. When triggered, spectators across the entire stadium stand up in sequence, creating the classic rippling "stadium wave" effect. Critically, this is computed **entirely in the shader** by calculating a unique start time for each agent relative to their position in the stadium or their GlobalID.

The MPC_VAT (Material Parameter Collection) holds the global variables: WaveStartTime (when the wave was triggered) and WaveSweepDuration (how long the full sweep should take across the stadium). Each instance stores its unique GlobalID in PerInstanceCustomData[6]. The Wave section of the shader uses this ID to calculate a personalized trigger time:

WaveTriggerTime = (GlobalID × WaveSweepDuration) + WaveStartTime

When the material's Time node surpasses WaveTriggerTime, the WaveAnimAlpha interpolates from 0 to 1, smoothly blending the instance from its current animation into the Wave VAT row.

### The Wave section and the Material Parameter Collection. The ten scalar parameters and one vector parameter are the only "levers" the CPU pulls to control the entire crowd's behavior.

#### Base Color

Base color randomization ensures that no two adjacent spectators are wearing the same outfit color. PerInstanceRandom drives a Hue Shift on the diffuse texture, and a separate PerInstanceCustomData[3,4,5] slot stores the shirt color set by the Blueprint at spawn time, allowing the CPU to set colors once on spawn rather than recalculating them every frame.

### Part 4: Blueprint Spawning and UI Logic

#### CrowdManager Blueprint

A single BP_CrowdManager actor reads the Data Table and populates the HISM. The spawning function (AddAgentInstances) takes a target agent count, computes how many instances to add or remove based on the current state, and iterates through the (shuffled) spawn list.

The "shuffled spawn list" is the key to organic fill. Rather than filling seats row by row, the Data Table rows are sorted into a shuffled order at initialization. As the Fill % slider increases, the crowd grows in a random, scattered pattern across the entire stadium.

### The first part of AddAgentInstances: clearing existing instances, computing the target agent count from the fill percentage, and preparing the ordered spawn list.

### Removing agents when the count decreases: a For Loop picks random indices from the spawn list and calls Remove Index, keeping the crowd density pattern visually random.

### Spawning agents: iterating through the data table, reading each row's position and normal, and calling Add Instance on the HISM with the correct world-space transform.

### The radial sweep calculation for wave timing. Atan2 converts each instance's world position to a polar angle, which is stored as Custom Data and later used by the shader to calculate the wave's sweep pattern.

#### UI Binding

The UI widget uses two types of sliders: a Spawn # slider that directly controls total agent count, and a Fill % slider that controls what percentage of the spawned agents are visible. Animation state sliders (Clap, Yell, Stand) drive PerInstanceCustomData channels for blending alphas.

*The UI binding section. Top: agent spawn events bound to the fill percentage and agent count sliders, each calling AddAgentInstances. Bottom: the animation slider event iterates through all agent instances and sets the appropriate Custom Data channel.*

### Part 5: Performance Results

#### Demo in Action

Before the numbers: here's what the system actually looks like at runtime.

*The crowd system in action with real-time spawning and animation blending. As the Spawn # and Fill % sliders are adjusted, spectators appear organically across the stadium rather than filling row by row.* *The animation sliders drive PerInstanceCustomData channels per-instance, transitioning 6,072 spectators between Idle, Clap, Yell, Stand, and Wave states with no CPU animation cost.*

#### VAT vs. Skeletal Mesh: The Real Cost

To prove the VAT approach is actually worth it, the same stadium was populated with a comparable number of **standard Skeletal Mesh actors** decimated to a nearly identical polygon budget as the VAT static mesh, so the comparison is fair. All profiling was captured on an RTX 3070 at 1080p with 90% screen percentage.

The mesh budget for both approaches is nearly identical. The VAT static mesh has **14,130 triangles/10,063 vertices**, and the skeletal mesh is **14,073 triangles/12,292 vertices**

|
|
|
|
|---|---|---|---|
FPS | 28.37 | 57.31 |
|
Game Time | 34.15 ms | 0.66 ms |
|
Draw Time | 16.22 ms | 0.74 ms |
|
GPU Time | 32.00 ms | 17.51 ms |
|
Draw Calls | 21,369 | 276 |
|

**Eliminating the Game Thread Bottleneck:** The move from 34.15 ms to 0.66 ms on the Game Thread essentially "unlocked" the engine. The CPU was working so hard to calculate bone transforms for skeletal meshes that it had no headroom left for gameplay logic, physics, or any other game systems.

**Draw Call Efficiency:** Reducing draw calls from 21,369 to just 276 is a **98.7% reduction in RHI overhead**. By batching 6,072 agents into Hierarchical Instanced Static Meshes (HISMs), the engine sends only a few massive instructions to the GPU instead of thousands of small ones.

**GPU Gains through Instancing:** Even though Vertex Animation Textures add math to the vertex shader, the GPU time dropped by nearly half (32 ms to 17.5 ms). This proves that the overhead of managing 6,000 individual skeletal mesh draw calls was actually slowing down the GPU itself, and the HISM instancing pipeline is significantly more efficient for the hardware to process.

### Skeletal mesh version: 28.37 FPS, 34.15ms game thread, and 21,369 draw calls for 6,072 agents. The game thread is completely saturated.

### VAT + HISM version: 57.31 FPS, 0.66ms game thread, 276 draw calls for the same 6,072 agents. The CPU is essentially idle.

#### Shader Complexity

Unreal's Shader Complexity view color-codes per-pixel instruction cost from green (cheap) to pink (expensive). With 6,072 VAT agents filling the frame, the entire crowd renders solidly in the green band.

*Shader Complexity Buffer Visualization with 6,072 active agents. Despite five simultaneous animation texture samples, bounding box decompressions, lerp blends, wave timing, and per-instance color variation, the crowd stays firmly in the "Good" green range throughout the arena.*

#### 8-bit vs 16-bit Texture Precision Trap

One decision that's easy to overlook in the Houdini VAT ROP settings has a very visible consequence: **Raster Depth**. Setting this to 8-bit instead of 16-bit floating point introduces quantization error in the stored position offsets, which manifests as vertex jitter. Always use 16-bit. The texture memory overhead is modest and the visual difference is stark.

### Conclusion

The shift from CPU-driven skeletal meshes to GPU-driven VAT instances changes the fundamental question of crowd systems. It stops being about how many characters are affordable and becomes about how to make them feel real. The most satisfying moment in this project was watching the wave propagate across a full stadium for the first time as 6,072 figures rose in sequence, driven by two numbers sent from the CPU and nothing else. That is the promise of technical art: turning cold math into collective emotion.

Looking ahead, the potential for this system extends far beyond manual sliders. By integrating dynamic lighting reactions into the shader where stadium lights pulse in response to crowd energy and expanding character variety through shared-material VAT meshes, it can move toward environments that are not just dense but deeply reactive. This framework paves the way for crowds driven by live, unpredictable gameplay events, turning the background audience into an active participant in the digital experience.

In an era of increasing visual complexity, the most powerful optimization is not just about saving frames. It is about making room for life.
