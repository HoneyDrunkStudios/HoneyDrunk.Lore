---
"source": "https://dev.to/gameoptim/can-you-compare-gpu-counter-data-across-mali-adreno-and-powervr-devices-3fkg"
"title": "Can You Compare GPU Counter Data Across Mali, Adreno, and PowerVR Devices?"
"author": "GameOptim"
"date_published": "2026-11-16"
"date_clipped": "2026-11-17"
"category": "Game Development / Unity"
"source_type": "rss"
---

# Can You Compare GPU Counter Data Across Mali, Adreno, and PowerVR Devices?

**No. Each vendor exposes a different counter set and defines GPU load differently, so the same reading carries a different recommended value depending on the chip — compare one device against its own earlier runs, not against a different phone.**

Two phones, one build, one scene, two unrelated GPU readings. That is not a measurement bug. Mali, Adreno, and PowerVR route work through different hardware schedulers, expose different counters, and accept different values for what looks like the same metric. Treating those numbers as directly comparable produces optimization decisions that do not survive contact with the other device.

GameOptim GOT Online now collects GPU Counter data on **Adreno and PowerVR** chips in addition to Mali, and adds **GPU load for Mali** plus **GPU load, cache behavior, and texture filtering for Adreno**. The sections below explain what each vendor's counters actually measure, which values indicate a problem, and where the thresholds come from — including the one configuration in which power data is not trustworthy at all.

## Summary

- GPU Counter support now covers **Mali, Adreno, and PowerVR**, but the available counters and the meaning of "GPU load" differ between them.
- On **Mali**, load is a pair of ratios: **Non Fragment Utilization** and **Fragment Utilization**. At full load, at least one should sit near **100%** while the other works in parallel.
- If **both** Mali utilizations are clearly below 100%, the likely cause is **serialization or a compute dependency** between the two work queues, not spare capacity.
- On **Adreno**, load is read through **GPU frequency**, because the question there is whether the GPU is throttling under heat.
- **Texture L1 Cache Miss** on Adreno should stay **below 15%** per GameOptim's recommendation; filtering mode, Mipmap enablement, and texture compression are the levers when it runs higher.
- **Recommended values differ by chip architecture.** Vertical comparison on the same device is meaningful; horizontal comparison between devices is not, and only some chips support collection at all.
- **Power readings are only valid with USB disconnected** — charging or USB connection can skew them or produce negative values.

## What Is the Core Problem?

GPU profiling assumes a counter means the same thing on every device. It does not. A Mali GPU distributes work through a Job Manager with two FIFO queues; an Adreno GPU is better characterized by clock frequency under thermal load; a PowerVR GPU exposes load, shading, bandwidth, and primitives as four separate modules.

The consequence is practical rather than academic. A "GPU load is high" finding from one device type does not translate into a specific optimization action on another, and a value inside the acceptable range on one chip can be a warning on a different chip. Coverage is partial as well: GPU Counter collection currently works on **only some chips**, because architectures vary even within a single vendor's product line.

## Why Do the Same Metrics Behave Differently on Different Chips?

The difference originates in the scheduling layer.

**Mali.** The **Job Manager** coordinates the workload and exposes two FIFO work queues to the graphics driver:

| Queue | Work it carries |
| --- | --- |
| Queue 1 | **Non Fragment** work — Compute shading and Vertex-related shading |
| Queue 2 | **Fragment** work |

In the ideal state the two queues run in parallel. The cycles each queue spends working, divided by the total cycles the GPU spends working, give **Non Fragment Utilization** and **Fragment Utilization**. Both are fractions of the same total, so they describe how work is split between the queues rather than two independent loads.

**Adreno.** Load is expressed primarily as **GPU frequency**. Under sustained pressure and heat, a GPU throttles much as a CPU does, and the frequency trace records when that happens.

**PowerVR.** Load, shading, bandwidth, and primitives are exposed as separate modules. Shading, bandwidth, and primitive metrics carry the same meaning and optimization direction as their Mali equivalents.

## How Do You Judge Mali GPU Load?

Read the two utilization figures together.

| Observation | What it means | What to do next |
| --- | --- | --- |
| At least one queue near **100%**, the other active in parallel for part of the time | Healthy full load — the GPU is genuinely busy | Work inside the busy queue's workload type |
| Both clearly below 100% | Possible **serialization** or **compute dependency** between the queues | Look for work that forces one queue to wait on the other |
| **Non Fragment Utilization** high | Vertex or compute work dominates | Optimize vertex count, Compute Shader, Geometry Shader, Tessellation Shader |
| **Fragment Utilization** high | Pixel work dominates | Check for excessive **Overdraw** and an overly complex **Fragment Shader** |

### Why Can Both Utilizations Be Low While the Frame Still Drops?

Low utilization on both queues reads like headroom, and teams routinely treat it as good news. If neither queue approaches saturation while frames are still being missed, the GPU is waiting on a dependency rather than running out of throughput. Adding parallelism to that situation does not help; finding the ordering constraint that serializes the two queues does.

## What Does Adreno GPU Load Tell You That Mali's Does Not?

Frequency answers a question that utilization percentages cannot: **is the GPU throttling?**

When a project carries high load and heats up noticeably, the GPU can drop its clocks the way a CPU does. A frequency curve that falls across a test session is direct evidence of thermal throttling, and it marks the scenes where the device was working hardest. That makes GPU frequency both a locator for high-pressure scenes and a thermal record of the run.

This matters because throttling changes the numbers you measure. The same scene profiled at the start and at the end of a long session can report different costs on identical content, purely from clock behavior.

## How Should You Read Cache Behavior on Adreno?

Data the GPU requests and finds in cache is a **hit**; data that is absent is a **miss**. The Adreno counter surfaces this as **Texture L1 Cache Miss** — the percentage of L1 texture cache misses.

Cache misses primarily drive **bandwidth and power consumption**. A higher miss rate means the GPU did more work for no result: extra memory traffic to fetch data it could not reuse.

**GameOptim recommends keeping Texture L1 Cache Miss below 15%.** Above that, the suggested areas to investigate are:

- **Texture filtering** — the filter mode changes the access pattern
- **Mipmap settings** — whether mipmaps are enabled at all
- **Texture compression** — how much data each fetch must move

## What Does Texture Filtering Data Tell You?

The primary texture filtering parameter is **Non-Base Level Textures** — textures using a Mipmap level other than 0. It is accompanied by three filter-mode metrics:

| Metric | Filter mode |
| --- | --- |
| **Nearest Filtered** | Nearest-neighbor filtering |
| **Linear Filtered** | Linear filtering |
| **Anisotropic Filtered** | Anisotropic filtering |

The guidance is to prefer low-cost filtering in general and to use **anisotropic filtering cautiously**, since it is the most expensive of the three. For 3D projects, confirm that **Mipmap is enabled**; a project running without mipmaps will show no non-base-level texture usage at all, which makes the parameter a direct check rather than an inference.

## What Do PowerVR Counters Add?

PowerVR provides four modules: **GPU load, GPU shading, GPU bandwidth, and GPU primitives**. Shading, bandwidth, and primitive metrics have the same meaning and optimization direction as on Mali, so the reading method transfers directly. The practical difference is that all four are available together, which lets you check load, shading cost, memory traffic, and geometry submission in one pass instead of inferring one from another.

## When Are Power Readings Meaningful?

The hardware info page now reports a **peak power** parameter, alongside the device's power and current during the test.

Power data earns its place for one specific reason: **power and bandwidth are closely related**. High device power implies high bandwidth, so the power trace can stand in as a proxy for bandwidth behavior. That also makes it an early thermal warning, since sustained high power is what leads to heat and throttling.

Two conditions limit when the number can be used:

1. **Power is a hardware characteristic of the device** and varies substantially between models. Do not compare power figures across devices.
2. **USB connection or charging heavily distorts the value**, producing anomalous or even negative readings. Only power and current data captured with USB disconnected is valid.

## What Should You Check First?

1. **Confirm the chip is supported.** Collection covers only some chips. Absent data is a coverage limit, not a zero reading.
2. **Identify the vendor's counter model before interpreting anything.** Mali reports a utilization pair, Adreno reports frequency and cache behavior, PowerVR reports four modules.
3. **On Mali, read both utilizations as a pair.** One near 100% is healthy; both low with dropped frames points at serialization or a compute dependency.
4. **On Adreno, inspect the frequency curve across the whole session.** A downward trend indicates throttling and identifies the responsible scenes.
5. **On Adreno, compare Texture L1 Cache Miss against the 15% recommendation.** If it exceeds that, check filter mode, Mipmap enablement, and compression.
6. **For power, disconnect USB before running the test.** Discard any run where the values are anomalous or negative.
7. **Compare vertically.** Use the same device before and after a change; disregard comparisons against other devices or other chip generations.

## What Should You Avoid?

- **Do not compare GPU Counter values across device brands.** Recommended values differ by architecture, so a healthy Mali figure can be a warning on PowerVR.
- **Do not compare across chip generations within one brand either.** Same-vendor architectures differ, which is also why only some chips are supported.
- **Do not read two low Mali utilizations as spare capacity.** Both well below 100% suggests the queues are waiting on each other.
- **Do not chase utilization when the cause is thermal.** On Adreno, a falling frequency explains a drop that utilization percentages will not.
- **Do not reduce cache misses by changing one lever only.** Filter mode, Mipmap enablement, and compression all contribute to the miss rate.
- **Do not trust power data captured over USB or while charging.** The values can invert.
- **Do not assume Mipmap is enabled in a 3D project.** No non-base-level texture usage is the signal that it is off.

## Practical Recommendations

| Problem | What to inspect | How to judge | What to optimize | What to expect |
| --- | --- | --- | --- | --- |
| Frames drop while the GPU looks idle | Mali Non Fragment / Fragment Utilization | Both clearly below 100% | Serialization and compute dependencies between the queues | At least one utilization rising |
| Vertex-heavy scenes | Non Fragment Utilization | High relative to Fragment | Vertex count, Compute / Geometry / Tessellation shader cost | Lower Non Fragment load |
| Pixel-heavy scenes | Fragment Utilization | High relative to Non Fragment | Overdraw, Fragment Shader complexity | Lower Fragment load |
| Frame time degrades during a session | Adreno GPU frequency | Frequency falling across the run | The scenes running when frequency dropped | A stable frequency curve |
| Bandwidth or battery concerns | Adreno Texture L1 Cache Miss | Above the 15% recommendation | Filter mode, Mipmap enablement, texture compression | Miss rate below 15% |
| 3D project with unexplained texture cost | Non-Base Level Textures | No non-base-level usage at all | Enable Mipmap | Non-base-level usage appears in the data |
| Throttling suspected | Peak power, USB disconnected | Power sustained high; values anomalous over USB | The bandwidth-heavy scenes driving power | Lower sustained power |

## Key Takeaways

- **Mali, Adreno, and PowerVR expose different counters.** "GPU load" means a utilization ratio on Mali, a frequency on Adreno, and one of four modules on PowerVR.
- **Mali's two utilization figures are read as a pair.** One near 100% is healthy; both low suggests serialization or a compute dependency rather than headroom.
- **Adreno GPU frequency reveals throttling**, which utilization percentages cannot express.
- **Texture L1 Cache Miss should stay below 15%** by GameOptim's recommendation, with filtering, Mipmap, and compression as the levers.
- **Compare the same device over time.** Cross-brand and cross-generation horizontal comparison carries little meaning, and only some chips are supported.

## FAQ

**Is it valid to compare a Mali result against an Adreno result for the same scene?**  
Not meaningfully. The counters differ in what they measure, and the recommended values for a given parameter differ by chip architecture. The comparison that holds up is the same device measured before and after a change.

**What does it mean when neither Mali utilization is close to 100% but frames are still late?**  
It suggests the two work queues are serialized or one depends on the other's output, so the GPU idles while waiting. Look for ordering constraints between Non Fragment and Fragment work rather than adding more parallel work.

**What is an acceptable Texture L1 Cache Miss rate on Adreno?**  
GameOptim recommends staying below 15%. Higher rates indicate extra memory traffic and power draw from cache misses, and the areas to review are texture filtering, Mipmap settings, and texture compression.

**Why are my power values negative or clearly wrong?**  
The device was on USB or charging during the measurement. Those states strongly affect the power figure, so only runs with USB disconnected should be used.

**My device shows no GPU Counter data at all. Is the collection broken?**  
Collection is currently supported on only some chips, since architectures differ even within one brand. Verify your chip is covered before treating the absence as a measurement of zero.
