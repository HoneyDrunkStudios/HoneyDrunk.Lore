---
source: "https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3"
title: "CFAST Unity Dev Report #3: From Fire Simulation to Real-Time Smoke Rendering"
author: "Hidenori Ishii"
date_published: "2026-11-26"
date_clipped: "2026-11-28"
category: "Technical Art & Creator Tools"
source_type: "rss"
secondary_categories: ["Game Development / Unity"]
---

# CFAST Unity Dev Report #3: From Fire Simulation to Real-Time Smoke Rendering

## Table of Contents

- [Introduction](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#introduction)
- [1. Game Smoke Effects vs. Simulation-Driven Smoke](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#1-game-smoke-effects-vs-simulationdriven-smoke)
- [2. Understanding the CFAST Two-Zone Model](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#2-understanding-the-cfast-twozone-model)
- [3. Two Separate Smoke Rendering Systems](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#3-two-separate-smoke-rendering-systems)
- [4. Indoor Volumetric Smoke Rendering](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#4-indoor-volumetric-smoke-rendering)
- [5. Optical Density and Smoke Visibility](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#5-optical-density-and-smoke-visibility)
- [6. Visualizing Gas Transport Through Openings](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#6-visualizing-gas-transport-through-openings)
- [7. Bidirectional Flow Through a Single Opening](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#7-bidirectional-flow-through-a-single-opening)
- [8. Investigating Differences Between Game Modes](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#8-investigating-differences-between-game-modes)
- [9. Why Identical Renderers Can Produce Different Results](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#9-why-identical-renderers-can-produce-different-results)
- [10. Dynamic Interior Doors and Smoke Transport Paths](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#10-dynamic-interior-doors-and-smoke-transport-paths)
- [11. Investigating Rendering Performance](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#11-investigating-rendering-performance)
- [12. Optimizing Opening Smoke Rendering](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#12-optimizing-opening-smoke-rendering)
- [13. Reusing Meshes Without Reducing Rendering Accuracy](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#13-reusing-meshes-without-reducing-rendering-accuracy)
- [14. Performance Measurement Results](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#14-performance-measurement-results)
- [15. Component Performance vs. Overall Game FPS](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#15-component-performance-vs-overall-game-fps)
- [16. Separating Simulation Time from Rendering Time](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#16-separating-simulation-time-from-rendering-time)
- [17. CFAST and FDS for Future Smoke Visualization](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#17-cfast-and-fds-for-future-smoke-visualization)
- [18. Interactive Technical Documentation](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#18-interactive-technical-documentation)
- [19. Conclusion](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#19-conclusion)
- [References](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#references)
- [About the Project](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-3-from-fire-simulation-to-real-time-smoke-rendering-hf3#about-the-project)

---

## Introduction

I am an independent developer working on a firefighting and disaster response game called **SOKYU: OPERATION RESCUE BLAZE SERIES**.

In the previous development reports, I introduced how I integrated CFAST, a fire simulator developed by the National Institute of Standards and Technology (NIST), with the Unity game engine.

The series currently covers the following topics:

| Report | Topic |
| --- | --- |
| #1 | Integrating NIST's fire simulator into a game |
| #2 | Fire states, fuel consumption, and asynchronous extinguishing events |
| #3 | Real-time smoke rendering and performance optimization |

In this third report, I will focus on how numerical fire simulation results are transformed into visible smoke inside Unity.

CFAST does not generate ready-to-render three-dimensional smoke meshes or game particles.

Instead, it provides numerical information describing the fire environment:

- Gas-layer heights
- Optical density
- Temperature
- Gas composition
- Mass flow rates
- Gas transport directions
- Opening conditions

The challenge is to convert these numerical results into an interactive visual experience while maintaining acceptable rendering performance.

This requires combining scientific computing, computer graphics, geometry processing, and real-time software engineering.

---

## 1. Game Smoke Effects vs. Simulation-Driven Smoke

Unity provides several technologies for creating fire and smoke effects, including particle systems, shaders, and the Visual Effect Graph.

These tools allow developers to create visually convincing smoke effects.

For this project, however, I wanted smoke to respond to changes in the simulated fire environment rather than relying exclusively on predefined effects.

For example:

- Smoke accumulates near the ceiling.
- The gas-layer interface changes as the fire develops.
- Smoke may travel into adjacent rooms.
- Opening a door changes the available gas transport paths.
- Windows and exterior doors affect ventilation.
- Existing smoke does not immediately disappear when a fire stops producing heat.

The objective is to connect these visual changes to numerical simulation results.

| Feature | Effect-Driven Approach | CFAST-Driven Approach |
| --- | --- | --- |
| Smoke generation | Configured visual effects | Simulation-dependent smoke state |
| Smoke accumulation | Effect parameters | Compartment gas-layer state |
| Smoke density | Artist-defined parameters | Calculated optical density |
| Smoke-layer height | Predefined or animated | Calculated layer interface |
| Door operation | Effect activation | Simulation input changes |
| Smoke transport direction | Configured particle movement | Calculated gas flow direction |
| Residual smoke | Particle lifetime | Accepted simulation state |

This does not mean that traditional game effects are inferior.

The difference is that the visual effects in this project are driven by the evolving state of a fire simulation.

---

## 2. Understanding the CFAST Two-Zone Model

CFAST stands for **Consolidated Fire and Smoke Transport**.

It is an open-source fire simulation program developed by NIST.

Official website:

<https://pages.nist.gov/cfast/>

CFAST primarily represents each compartment using two gas layers.

- An upper gas layer, where hot combustion gases and smoke typically accumulate.
- A lower gas layer, which is generally cooler.

The temperature, composition, volume, and optical properties of these layers change as the simulation progresses.

```
                CEILING
    ┌──────────────────────────┐
    │                          │
    │     Upper Gas Layer      │
    │     Hot Gas and Smoke    │
    │                          │
    ├──────────────────────────┤ ← Layer Interface
    │                          │
    │     Lower Gas Layer      │
    │                          │
    │         Fire Source      │
    └──────────────────────────┘
                  FLOOR
```

This model is computationally different from CFD-based simulation.

CFAST does not directly calculate the detailed three-dimensional velocity field at every location inside a compartment.

Instead, it calculates representative compartment and gas-layer conditions together with modeled gas transport processes.

This distinction determines how the simulation results can be visualized in Unity.

---

## 3. Two Separate Smoke Rendering Systems

One of the most important architectural decisions was to separate indoor smoke rendering from opening smoke rendering.

These two types of smoke represent different information.

### Indoor Smoke

Indoor smoke represents the optical state of a compartment and its upper and lower gas layers.

It is rendered using compartment-based smoke volumes.

### Opening Smoke

Opening smoke represents visible gas transport through doors, windows, and other supported openings.

It is rendered using particles and dynamically generated meshes.

The overall architecture is:

```
              CFAST Native Worker
                       │
              Accepted Simulation Data
                       │
         ┌─────────────┴─────────────┐
         │                           │
  Compartment Data              Opening Data
         │                           │
  Layer Heights                 Mass Flow Rates
  Optical Density               Flow Directions
  Room Geometry                 Source Optical State
         │                           │
         ▼                           ▼
  Volumetric Smoke              Opening Smoke
      Renderer                  Particle Renderer
         │                           │
         └─────────────┬─────────────┘
                       ▼
                Unity Game View
```

This separation allows the two rendering systems to use the simulation information appropriate to their respective purposes.

Indoor smoke does not require every visible part of the smoke volume to be represented by an individual particle.

Opening smoke, on the other hand, benefits from a directional particle-based representation.

---

## 4. Indoor Volumetric Smoke Rendering

Indoor smoke is rendered using compartment geometry and the accepted gas-layer information from CFAST.

The primary rendering inputs are:

| Input | Purpose |
| --- | --- |
| Compartment geometry | Defines the smoke rendering region |
| Lower-layer depth | Determines the gas-layer interface |
| Upper-layer optical density | Controls upper-layer extinction |
| Lower-layer optical density | Controls lower-layer extinction |
| Accepted simulation time | Associates rendering with a confirmed simulation state |

### 4.1 Calculating the Layer Interface

If the compartment floor elevation is represented by $y\_{floor}$ and the lower-layer depth calculated by CFAST is represented by $h\_{lower}$, the interface position is:

$$  
y\_{interface}=y\_{floor}+h\_{lower}  
$$

As the simulation progresses, changes in this interface position are reflected in the Unity smoke volume.

For example, a descending gas-layer interface can increase the region occupied by upper-layer smoke.

```
Early Fire                    Developing Fire

┌───────────────────┐        ┌───────────────────┐
│ Upper Smoke Layer │        │                   │
├───────────────────┤        │                   │
│                   │        │ Upper Smoke Layer │
│                   │        │                   │
│ Lower Gas Layer   │        ├───────────────────┤
│                   │        │ Lower Gas Layer   │
└───────────────────┘        └───────────────────┘
```

The illustration is conceptual and does not represent measured smoke-layer heights.

### 4.2 Preparing GPU Layer Data

The Unity implementation converts the accepted CFAST room information into a compact data structure for rendering.

The following is a simplified excerpt based on the existing implementation:

```
double upperOD = room.UpperOpticalDensityPerMetre.Value;
double lowerOD = room.LowerOpticalDensityPerMetre.Value;

double interfaceHeight = floor + lowerDepth;

var layer = new Vector4(
    (float)interfaceHeight,
    (float)lowerOD,
    (float)upperOD,
    0f
);
```

The resulting vector contains the layer interface position and the optical density values required by the rendering system.

The implementation also uses GPU buffers for compartment geometry and layer information.

```
material.SetBuffer("_GasPlanes", planes);
material.SetBuffer("_GasCells", cells);
material.SetBuffer("_GasLayers", layers);
```

The three buffers serve different purposes.

| Buffer | Purpose |
| --- | --- |
| GasPlanes | Boundary planes of the gas regions |
| GasCells | Compartment-related rendering geometry |
| GasLayers | Current upper-layer and lower-layer optical information |

The geometry and the evolving simulation state are represented separately.

This allows the rendering system to update the gas-layer state without reconstructing the entire compartment geometry for every simulation result.

### 4.3 Why Not Use Persistent Particles for the Entire Room?

Representing an entire smoke-filled room using persistent particles can introduce substantial particle management and rendering costs.

A compartment-based volume avoids making the existence of indoor smoke dependent on the lifetime of individual particles.

The accepted CFAST layer state remains available to the renderer until a new simulation state is received.

This is particularly useful for representing accumulated indoor smoke.

---

## 5. Optical Density and Smoke Visibility

Optical density describes the attenuation of light as it travels through a medium.

In the context of fire simulation, it provides information related to the visibility reduction caused by smoke.

It is important to distinguish optical density from a simple opacity parameter.

Optical density depends on the optical properties of the medium and the distance through which light travels.

For an optical density per unit length $D$ and a path length $L$, an idealized decadic attenuation relationship can be expressed as:

$$  
\frac{I}{I\_0}=10^{-DL}  
$$

Where:

- $I\_0$ is the original light intensity.
- $I$ is the transmitted light intensity.
- $D$ is the optical density per unit length.
- $L$ is the optical path length.

An equivalent exponential extinction representation is:

$$  
\frac{I}{I\_0}=e^{-\kappa L}  
$$

Where:

$$  
\kappa=D\ln(10)  
$$

These equations describe the general relationship between optical density and light attenuation.

They are presented here to explain the underlying optical concept, not as a complete reproduction of the project's shader implementation.

In Unity, smoke visibility is also affected by rendering factors such as:

- Lighting
- Scattering
- Camera position
- Viewing distance
- Occlusion
- Other visual effects

Therefore, two scenes containing the same optical density values may still appear different if their rendering environments differ.

---

## 6. Visualizing Gas Transport Through Openings

Doors and windows create transport paths between compartments or between a compartment and the exterior environment.

CFAST calculates gas transport through these openings.

The opening smoke renderer uses several pieces of information from the accepted simulation results.

| Simulation Input | Rendering Purpose |
| --- | --- |
| Signed mass flow rate | Determines transport direction |
| Gas density | Converts mass flow into volumetric flow |
| Native opening area | Supports average velocity calculation |
| Source gas-layer optical density | Determines the visible smoke contribution |
| Opening geometry | Defines the visualization region |

### 6.1 Converting Mass Flow into Volumetric Flow

The volumetric flow rate is calculated using the relationship:

$$  
\dot{V}=\frac{|\dot{m}|}{\rho}  
$$

Where:

- $\dot{m}$ is the signed gas mass flow rate in kg/s.
- $\rho$ is the gas density in kg/m³.
- $\dot{V}$ is the volumetric flow rate in m³/s.

The sign of the mass flow rate is used to determine the transport direction.

### 6.2 Calculating Average Flow Velocity

Given an opening area $A$, the average flow velocity can be calculated as:

$$  
v=\frac{\dot{V}}{A}  
$$

The result is an average velocity associated with the modeled opening flow.

It is not a detailed three-dimensional velocity field.

The Unity renderer uses this information to represent directional smoke transport.

### 6.3 Smoke Transport Is Not the Same as Airflow

Gas flow through an opening does not necessarily mean that dense smoke should be rendered.

The optical state of the gas source layer must also be considered.

A flow originating from a relatively clear lower gas layer may contain significantly less visible smoke than a flow originating from a smoke-filled upper layer.

```
Signed Mass Flow
       │
       ├── Flow Direction
       │
       └── Mass Flow / Gas Density
                    │
              Volumetric Flow
                    │
              Opening Area
                    │
              Average Velocity
                    │
Source Optical Density
                    │
                    ▼
          Opening Smoke Rendering
```

This is how numerical transport information is connected to the visual smoke representation.

---

## 7. Bidirectional Flow Through a Single Opening

An opening does not necessarily have only one gas transport direction.

Depending on the fire conditions, pressure differences, and temperatures, a doorway may support simultaneous flows in different directions.

For example, hot smoke may leave a compartment through the upper part of an opening while cooler air enters through the lower part.

```
    Fire Compartment           Adjacent Compartment

┌──────────────────────┬──────────────────────┐
│                      │                      │
│ Hot Smoke  ──────────┼───────────────>      │
│                      │                      │
│                OPENING                      │
│                      │                      │
│            <─────────┼────────── Cooler Air │
│                      │                      │
└──────────────────────┴──────────────────────┘
```

The opening smoke renderer uses the direction-specific and region-specific flow information calculated by CFAST.

This avoids assigning one fixed direction to every particle associated with an opening.

However, the illustrated flow pattern is not guaranteed whenever a door is opened.

The actual gas transport depends on the accepted simulation conditions.

The objective is to visualize the calculated transport rather than impose a predefined animation.

---

## 8. Investigating Differences Between Game Modes

During development, I noticed that smoke appeared different between stages and between gameplay modes.

The three relevant gameplay modes were:

- AIM3D
- AIM3D2
- ZERO

The question was whether these differences originated from the simulation or the rendering implementation.

### 8.1 Investigating CFAST Optical Density

In an early Stage02 native test, I compared the optical density of the living area and entrance hall three seconds after the simulation started.

| Compartment | Upper-Layer Optical Density |
| --- | --- |
| R4 — Living, dining, and kitchen area | 0.291650 |
| R5 — Entrance hall | 0.009422 |

The entrance hall's upper-layer optical density was approximately 3.23% of the living area's value.

$$  
\frac{0.009422}{0.291650}\times100  
\approx3.23\%  
$$

The lower-layer optical density in the entrance hall was also close to zero.

Gas containing smoke was moving from the living area into the entrance hall, but the calculated optical density in the entrance hall was still relatively low.

This showed that the limited visible smoke in that compartment was not necessarily a rendering defect.

These results were obtained before the later addition of six interior doors and their fully closed initial conditions.

They should not be interpreted as measurements of the latest door configuration.

### 8.2 Comparing the Actual Unity Rendering

A separate investigation compared the indoor smoke rendering across the three gameplay modes.

The comparison controlled the following conditions:

- CFAST smoke-layer data
- Camera position
- Camera orientation
- Field of view: 60 degrees
- Stage geometry

A total of 150 images were collected from nine scene executions.

When the same smoke-layer data and camera conditions were used within the same stage, the indoor smoke images matched at the pixel level across the three modes.

| Validation Item | Result |
| --- | --- |
| AIM3D indoor smoke | Shared rendering implementation |
| AIM3D2 indoor smoke | Shared rendering implementation |
| ZERO indoor smoke | Shared rendering implementation |
| Matched-condition indoor smoke images | Pixel-level match |

This established that, within the tested conditions, separate smoke rendering implementations were not required for each mode.

---

## 9. Why Identical Renderers Can Produce Different Results

Even when multiple gameplay modes use the same rendering implementation, their simulation inputs may differ.

In the earlier Stage02 configuration, the entrance door was open in the AIM modes and closed in ZERO.

This produced different CFAST gas transport conditions.

The following values were measured at a simulation time of three seconds.

| Gameplay Mode | Smoke-Bearing Upper Gas Flow from LDK to Hall |
| --- | --- |
| AIM3D | 0.003881 kg/s |
| AIM3D2 | 0.003881 kg/s |
| ZERO | 0.003678 kg/s |

The difference in the opening configuration changed the simulation results.

```
Different Opening Conditions
              ↓
Different CFAST Inputs
              ↓
Different Gas Transport
              ↓
Different Compartment Conditions
              ↓
Different Smoke Visualization
```

This is an important debugging principle.

A visible difference is not automatically evidence of a rendering bug.

The numerical input to the renderer must also be compared.

Other visual factors, including lighting, fire effects, and occlusion, can contribute to differences in the final scene appearance.

The investigation did not independently quantify every one of these contributions.

---

## 10. Dynamic Interior Doors and Smoke Transport Paths

Six interactive interior doors were added to Stage02.

All six doors start in the fully closed state.

| Opening | Connected Compartments | Opening Direction |
| --- | --- | --- |
| V1 | Entrance hall and toilet | Toward the entrance hall |
| V3 | Bathroom and washroom | Toward the washroom |
| V4 | Living area and left bedroom | Toward the living area |
| V5 | Entrance hall and washroom | Toward the washroom |
| V6 | Entrance hall and living area | Toward the living area |
| V7 | Living area and right bedroom | Toward the living area |

The former opening V2 remains permanently closed.

V7 is the designated entrance to the right bedroom.

### Closing an Opening

When V6 is closed, direct gas transport through V6 between the living area and entrance hall is prevented by the model configuration.

### Opening an Opening

When V6 is opened, a potential gas transport path becomes available.

The actual flow direction and flow rate are determined by CFAST.

```
PLAYER OPERATES DOOR
          │
          ▼
UNITY DOOR STATE
          │
          ▼
CFAST OPENING INPUT
          │
          ▼
GAS TRANSPORT CALCULATION
          │
          ▼
ACCEPTED SIMULATION RESULT
          │
     ┌────┴────┐
     ▼         ▼
 Indoor      Opening
 Smoke       Smoke
 Update      Update
```

The player is changing a simulation input, rather than simply activating a smoke effect.

Closing a door also does not imply that all smoke already present inside the adjacent compartments should immediately disappear.

Existing indoor smoke remains associated with the accepted compartment simulation state.

---

## 11. Investigating Rendering Performance

Real-time smoke visualization introduces both CPU and GPU workloads.

During actual Stage02 gameplay, I observed differences in lag symptoms depending on whether the entrance door was open or closed.

Several possible contributors were identified.

| Processing Area | Potential Workload |
| --- | --- |
| CFAST | Gas transport calculations |
| CPU | Particle generation and simulation |
| CPU | Particle data retrieval |
| CPU | Vertex generation |
| CPU | Mesh updates |
| CPU/GPU | Mesh data transfer |
| GPU | Transparent particle overdraw |
| GPU | Volumetric smoke rendering |
| GPU | Additional visible geometry |

The number of open transport paths may influence the rendering workload.

However, the observation alone does not establish whether the primary bottleneck is the number of openings, the number of particles, GPU overdraw, or the CFAST calculation itself.

I therefore started with a smaller optimization: eliminating unnecessary CPU work in the opening smoke renderer.

The CFAST calculation method and simulation update frequency were preserved.

---

## 12. Optimizing Opening Smoke Rendering

The original opening smoke rendering path could perform particle retrieval and mesh writing even when there were no particles to render.

This created unnecessary CPU work.

The revised implementation distinguishes between three conditions:

1. No particles are available.
2. The rendering input is identical to the previous frame's input.
3. The rendering input has changed.

### 12.1 No Particles Available

When an opening contains no particles to render, unnecessary operations are skipped.

These include:

- Particle data retrieval
- Unnecessary vertex generation
- Unnecessary mesh transfer

However, appearance and boundary buffer updates are preserved.

The optimization must not prevent the renderer from updating the opening geometry or other required visual state.

```
BEFORE OPTIMIZATION

Particle Retrieval
        ↓
Vertex Generation
        ↓
Mesh Writing
        ↓
Appearance and Boundary Updates

AFTER OPTIMIZATION — EMPTY OPENING

Check Particle Count
        ↓
No Particles
        ↓
Skip Unnecessary Particle and Mesh Operations
        ↓
Preserve Appearance and Boundary Updates
```

### 12.2 Zero Gas Flow Does Not Mean Zero Existing Particles

A gas flow rate of zero does not automatically mean that every particle associated with an opening has disappeared.

Existing particles may still require visualization.

The optimization therefore checks the actual particle state rather than using zero gas flow as an unconditional reason to disable rendering.

This preserves the existing behavior when the opening condition changes.

---

## 13. Reusing Meshes Without Reducing Rendering Accuracy

When particles remain present, the renderer determines whether the rendering inputs have changed.

The comparison includes information such as:

- Particle position
- Particle size
- Particle rotation
- Particle opacity or optical appearance
- Relevant transformation matrices

If the rendering inputs are exactly identical, the previously generated mesh can be reused.

If the inputs change, the mesh is updated.

```
             Opening Smoke Rendering
                         │
                  Particles Present?
                    │          │
                   No         Yes
                    │          │
                    ▼          ▼
               Skip Work    Compare Input
                               │
                       ┌───────┴───────┐
                       │               │
                   Identical        Changed
                       │               │
                       ▼               ▼
                  Reuse Mesh       Update Mesh
                       │               │
                       └───────┬───────┘
                               ▼
                    Appearance and Boundary
                           Updates
```

### Example Frame Sequence

| Frame | Rendering Input | Mesh Operation |
| --- | --- | --- |
| Frame 1 | Initial input | Generate mesh |
| Frame 2 | Identical | Reuse mesh |
| Frame 3 | Identical | Reuse mesh |
| Frame 4 | Changed | Update mesh |
| Frame 5 | Identical to Frame 4 | Reuse mesh |

This is an explanatory example, not a recorded rendering trace.

No fixed mesh refresh interval was introduced.

No arbitrary tolerance threshold was added to classify different particle positions as identical.

The objective was to remove redundant processing without deliberately reducing rendering quality.

---

## 14. Performance Measurement Results

The opening smoke optimization was evaluated using the Stage02 ZERO scene in the Unity Editor.

The accepted CFAST state, camera conditions, and graphics settings were controlled during the comparison.

### 14.1 Initial Optimization Candidate

The initial candidate produced the following median CPU processing times.

| Condition | Before | Initial Candidate |
| --- | --- | --- |
| No particles | 0.0878 ms | 0.0063 ms |
| Identical rendering input | 0.2843 ms | 0.0927 ms |
| Moving particles | 0.2752 ms | 0.2528 ms |

However, independent review identified a problem with the empty-particle optimization.

The early-return path also skipped required appearance and boundary buffer updates.

As a result, the initial performance improvement could not be accepted as the final result.

The implementation was revised to preserve these required updates.

This is an example of why performance improvements must be evaluated together with behavioral correctness.

### 14.2 Final Measurement After Review Corrections

The revised empty-opening implementation was measured again.

The test covered 13 openings containing no smoke particles.

| Measurement | Before | After |
| --- | --- | --- |
| Median CPU processing time | 0.09370 ms | 0.04965 ms |
| Particle retrieval calls per frame | 13 | 0 |
| Mesh write calls per frame | 13 | 0 |

The CPU processing time reduction was:

$$  
\frac{0.09370-0.04965}{0.09370}  
\times100  
\approx47.01\%  
$$

**Approximately 47% less CPU processing time for the measured operation.**

```
Opening Smoke CPU Processing Time

Before  |████████████████████| 0.09370 ms

After   |███████████         | 0.04965 ms

CPU Time Reduction: Approximately 47%
```

The result applies specifically to the measured rendering operation involving 13 empty openings.

It is not a measurement of overall game FPS.

The initially measured values for identical inputs and moving particles should also be distinguished from the final empty-opening measurement.

---

## 15. Component Performance vs. Overall Game FPS

A percentage reduction in the processing time of one component does not necessarily translate into the same percentage improvement in overall game performance.

The absolute time saved in the final empty-opening test was:

$$  
0.09370-0.04965=0.04405\text{ ms}  
$$

For comparison, a game running at 60 FPS has a nominal frame time of:

$$  
\frac{1000}{60}\approx16.67\text{ ms}  
$$

The optimization eliminates unnecessary work, but the absolute time saved is relatively small compared with the total frame budget.

If GPU rendering is the primary bottleneck, reducing CPU processing time may have little effect on FPS.

Similarly, a CFAST simulation stall cannot be resolved simply by reducing mesh generation overhead.

These are separate performance problems.

| Optimization Area | Intended Improvement |
| --- | --- |
| Native simulation | Numerical calculation performance |
| Inter-process communication | Simulation response latency |
| CPU rendering preparation | Particle and mesh processing |
| GPU rendering | Smoke shading and transparency |
| Game frame processing | Overall responsiveness |

The current optimization demonstrates an improvement in CPU processing for the measured component.

An overall FPS improvement in the production standalone Player has not yet been established.

---

## 16. Separating Simulation Time from Rendering Time

The project uses a stateful CFAST worker that advances the fire simulation through incremental requests.

Unity renders the currently accepted simulation state.

The simulation update frequency and rendering frame rate do not need to be identical.

```
CFAST SIMULATION

STEP 1 ──────── STEP 2 ──────── STEP 3
   │               │               │
   ▼               ▼               ▼
State A         State B         State C

UNITY RENDERING

Frame 1  Frame 2  Frame 3  Frame 4  Frame 5
    │        │        │        │        │
 State A  State A  State B  State B  State C
```

This illustration shows the conceptual relationship between accepted simulation updates and rendering frames.

It does not represent the actual timing of a recorded gameplay session.

### Accepted Simulation State

Indoor smoke rendering uses the accepted compartment state.

The opening smoke renderer uses the corresponding accepted transport information.

The renderer does not need to reconstruct the fire simulation independently for every graphics frame.

This separation has several advantages:

- Numerical simulation can run outside the Unity main thread.
- Rendering can continue using accepted simulation information.
- Static compartment geometry can be maintained separately from dynamic smoke-layer data.
- Mesh updates can be avoided when the relevant rendering input has not changed.

However, if the native worker stops returning new results, Unity cannot continue updating the physical smoke state with new simulation information.

This is why the numerical stability issues discussed in Development Report #1 are also relevant to graphics rendering.

Simulation stability and rendering efficiency are different aspects of the same interactive system.

---

## 17. CFAST and FDS for Future Smoke Visualization

CFAST provides compartment-level gas-layer information and modeled gas transport.

This is useful for interactive simulation, but it has limitations when representing detailed local smoke motion.

For example, CFAST does not directly provide the spatial velocity fields required to reproduce:

- Small-scale smoke vortices
- Detailed flow around furniture
- Local turbulence near obstacles
- Fine spatial variations in smoke concentration

Another NIST fire simulation program, **FDS (Fire Dynamics Simulator)**, uses computational fluid dynamics to calculate spatially distributed fire-driven flows.

| Characteristic | CFAST | FDS |
| --- | --- | --- |
| Simulation model | Zone model | CFD |
| Spatial representation | Compartments and gas layers | Three-dimensional computational mesh |
| Smoke information | Representative layer conditions | Spatial distribution |
| Gas velocity | Modeled transport processes | Spatial velocity field |
| Computational workload | Generally lower | Generally higher |
| Current project role | Incremental gameplay simulation | Detailed fire analysis and visualization development |

I am exploring how these two simulation models can complement each other in game development.

A potential architecture is:

```
CFAST                         FDS
  │                            │
Compartment State         Detailed Fire Analysis
  │                            │
Smoke Layers              Spatial Smoke Distribution
Opening Flows             Local Flow Structures
  │                            │
  └─────────────┬──────────────┘
                ▼
           Unity Engine
                │
       Interactive Visualization
```

The CFAST-based smoke rendering described in this article is already implemented.

The broader use of FDS spatial data remains a separate development and investigation topic.

A complete real-time coupling of FDS velocity fields and CFAST compartment states is not claimed here.

Future reports will discuss FDS, Smokeview, and the different roles of zone models and CFD in more detail.

---

## 18. Interactive Technical Documentation

I have also prepared a technical guide on the project website.

The guide uses diagrams, animations, and interactive visual explanations to introduce the CFAST and Unity integration.

### CFAST × Unity Technical Guide

[Explore the CFAST and Unity Fire Simulation Guide](https://ronsard.sakura.ne.jp/sokyu/cfast-guide.html)

### Stage02 Technical Validation

[Stage02 — Numerical Stability, Smoke Rendering, and Opening Control](https://ronsard.sakura.ne.jp/sokyu/cfast-guide.html#stage02-validation)

The technical documentation covers:

- CFAST's two-zone model
- Compartment-based smoke visualization
- Smoke transport through openings
- Numerical solver instability
- Horizontal vent closure
- Building model corrections
- Opening smoke rendering optimization
- Interactive interior doors

The website is primarily presented in Japanese, with visual diagrams and animations explaining the technical concepts.

Readers interested in simulation-driven game development, scientific computing, and real-time graphics are welcome to explore the project.

---

## 19. Conclusion

In this development report, I introduced how numerical fire simulation results are transformed into real-time smoke visualization inside Unity.

The main architectural decisions include:

- Separating indoor volumetric smoke from opening smoke rendering.
- Using CFAST gas-layer heights and optical density for compartment visualization.
- Using signed mass flow rates and gas density for opening smoke visualization.
- Connecting door and window operations to simulation input conditions.
- Distinguishing numerical simulation differences from rendering differences.
- Reusing meshes when the rendering input is unchanged.
- Eliminating unnecessary work for openings containing no smoke particles.
- Separating component-level performance measurements from overall game FPS.

One of the most important lessons from this project is that scientific simulation and computer graphics solve different problems.

CFAST calculates the evolving fire environment using its physical and numerical models.

Unity transforms the accepted numerical information into an interactive visual experience.

Connecting the two requires careful consideration of data representation, numerical stability, rendering architecture, and computational performance.

The objective is not simply to make smoke look more realistic.

It is to create a game environment in which smoke changes in response to simulated fire conditions and player interactions.

In the next development report, I will examine the underlying software architecture in greater detail:

**Building a Stateful CFAST Worker in Fortran and Connecting It to Unity Through Inter-Process Communication.**

That report will focus on the native calculation loop, DASSL state retention, communication protocols, asynchronous C# processing, and simulation result validation.

This project is being developed as a game. It does not claim validated accuracy for real-world fire prediction or certified effectiveness as a professional firefighting training system.

---

## References

- [NIST CFAST Official Website](https://pages.nist.gov/cfast/)
- [CFAST Official GitHub Repository](https://github.com/firemodels/cfast)
- [CFAST Version 7 Technical Reference Guide](https://doi.org/10.6028/NIST.TN.1889v1)
- [CFAST 7.7.7 — Development Baseline Source Code](https://github.com/firemodels/cfast/tree/b43e74e0f43c704582c5782f5446597ce729a07f)
- [NIST Fire Dynamics Simulator and Smokeview](https://pages.nist.gov/fds/)

---

## About the Project

**SOKYU: OPERATION RESCUE BLAZE SERIES**

An independently developed firefighting and disaster response game combining:

- Fire simulation
- Scientific computing
- Unity game development
- Real-time computer graphics
- Embedded systems
- Robotics
- Artificial intelligence

Developed by **Motomachi Digital Making Lab**, Yokohama, Japan.

### Project Technical Website

<https://ronsard.sakura.ne.jp/sokyu/cfast-guide.html>

### Stage02 Technical Validation

<https://ronsard.sakura.ne.jp/sokyu/cfast-guide.html#stage02-validation>

---

**CFAST × Unity Development Report #3**

November 26, 2026
