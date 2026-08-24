---
source: "https://dev.to/gamedevtoollab/where-unity-burst-and-jobs-actually-help-a-practical-guide-for-gameobject-based-projects-4pjd"
title: "Where Unity Burst and Jobs Actually Help: A Practical Guide for GameObject-Based Projects"
author: "GameDevToolLab"
date_published: "2026-08-22"
date_clipped: "2026-08-24"
category: "Game Development / Unity"
source_type: "rss"
---

# Where Unity Burst and Jobs Actually Help: A Practical Guide for GameObject-Based Projects

Source: https://dev.to/gamedevtoollab/where-unity-burst-and-jobs-actually-help-a-practical-guide-for-gameobject-based-projects-4pjd

## Introduction

Burst Compiler and the C# Job System can solve CPU bottlenecks, but they are not performance switches. Scheduling, copying, immediate `Complete()`

calls, and unclear NativeContainer ownership can easily erase the gain.

In a GameObject-based project, performance depends on **which calculation you isolate, which data crosses the managed boundary, and when the main thread waits**. This article focuses on that boundary rather than a full ECS migration or Job syntax basics.

The baseline is Unity 6.3 LTS, Burst 1.8.30, Collections 2.6.8, and Mathematics 1.3.3 as of August 2026. Examples use `IJobFor`

and `ScheduleParallelByRef`

. ByRef avoids a large scheduling-time struct copy, although workers still use local copies. Older Unity versions may expose different overloads.

The code demonstrates design boundaries, not a compiled drop-in sample. Validate it with Safety Checks, a Development Build, and the Profiler on target hardware.

## When Burst and Jobs are a good fit

Burst and Jobs fit workloads with many independent elements, substantial CPU work, contiguous value-type data, little Unity API access inside the kernel, and useful work available before the result is needed.

Good candidates include movement, projectiles, FOV tests, LOD or culling, AI scoring, procedural geometry, noise, grids, and bulk processing. Deterministic server or replay workloads need cross-platform reproducibility tests.

Poor candidates include small collections, Unity-API-heavy or immediate-result logic, managed-object-heavy processing, and cases where marshaling costs more than calculation. A compute shader may suit very large data-parallel work better.

Ask: **can you isolate a large enough calculation kernel that is closed over value-type data?**

## Understand the four separate roles

-
**Burst Compiler**optimizes supported C# kernels into native code; it does not create multithreading. -
**C# Job System**schedules work and tracks dependencies, with its own overhead. -
**NativeContainer**exposes shared data under Unity's ownership and safety rules. -
**Unity.Mathematics**provides Burst-friendly numerical types and functions.

Prepare data, schedule execution, and optimize the kernel as separate concerns.

## Four questions before introducing Jobs

### Is CPU computation really the bottleneck?

Profile first. Jobs do not fix frames dominated by rendering, physics, GC, asset loading, or synchronous I/O.

### Is each element independent?

`IJobFor.Execute(int index)`

has no guaranteed order. Shared accumulation should become per-index output followed by a reduction.

### Can the managed boundary stay small?

Measure input collection and result application. A faster worker kernel can still make the frame slower.

### Can waiting be delayed?

Immediate `Complete()`

removes most overlap. Schedule early, consume next frame, or chain dependencies and wait only for the final handle.

##
Start with `IJobFor`

and fixed-index output

For a new parallel loop, begin with input and output that use the same index.

```
using Unity.Burst;
using Unity.Collections;
using Unity.Jobs;
using Unity.Mathematics;
[BurstCompile]
public struct IntegratePositionJob : IJobFor
{
[ReadOnly] public NativeArray<float3> Velocities;
public NativeArray<float3> Positions;
public float DeltaTime;
public void Execute(int index)
{
float3 position = Positions[index];
Positions[index] = position + Velocities[index] * DeltaTime;
}
}
var job = new IntegratePositionJob
{
Velocities = velocities,
Positions = positions,
DeltaTime = deltaTime
};
JobHandle handle = job.ScheduleParallelByRef(
positions.Length,
innerloopBatchCount: 64,
dependency: default);
```

A NativeContainer indexer is not a `ref return`

, so “read, modify, write back” is the clearest default for structures. The outer owner allocates and disposes the arrays and must call `Complete()`

before reading or disposing data still owned by a job. `[ReadOnly]`

and fixed-index output also make the access pattern explicit to the Safety System.

## Practical example: target evaluation with one-frame latency

Consider a lock-on system that scores targets by distance, field of view, and threat. The main thread snapshots Transform data into persistent NativeArrays and consumes the job next frame. A version prevents stale results from reaching changed or removed targets.

### Input, output, and the job

```
using Unity.Burst;
using Unity.Collections;
using Unity.Jobs;
using Unity.Mathematics;
public struct TargetInput
{
public float3 Position;
public float Threat;
public byte IsActive;
}
public struct TargetEvaluation
{
public float DistanceSq;
public float Score;
public byte IsCandidate;
}
[BurstCompile]
public struct EvaluateTargetsJob : IJobFor
{
[ReadOnly] public NativeArray<TargetInput> Inputs;
[WriteOnly] public NativeArray<TargetEvaluation> Outputs;
public float3 ObserverPosition;
public float3 ObserverForward;
public float MaxDistanceSq;
public float CosHalfFieldOfView;
public void Execute(int index)
{
TargetInput input = Inputs[index];
float3 toTarget = input.Position - ObserverPosition;
float distanceSq = math.lengthsq(toTarget);
bool isNearlySamePosition = distanceSq <= 0.0001f;
float3 direction = math.normalizesafe(toTarget);
float facing = isNearlySamePosition
? 1.0f
: math.dot(ObserverForward, direction);
bool candidate =
input.IsActive != 0 &&
distanceSq <= MaxDistanceSq &&
facing >= CosHalfFieldOfView;
float distanceSq01 = math.saturate(
distanceSq / math.max(MaxDistanceSq, 0.0001f));
Outputs[index] = new TargetEvaluation
{
DistanceSq = distanceSq,
Score = candidate
? input.Threat * 2.0f + facing - distanceSq01
: float.NegativeInfinity,
IsCandidate = (byte)(candidate ? 1 : 0)
};
}
}
```

The job receives no managed references and writes only to matching output indices. Near-zero-distance targets pass the FOV test; tune the threshold for your scale. `float.NegativeInfinity`

is an internal sentinel, so use `Score`

only when `IsCandidate != 0`

.

### Define the target contract

```
public abstract class TargetAgent : MonoBehaviour
{
public abstract float Threat { get; }
public abstract int EvaluationVersion { get; }
public abstract void ApplyEvaluation(float score, bool isCandidate);
}
```

Read `Threat`

before scheduling, increment `EvaluationVersion`

when relevant state changes, and call `ApplyEvaluation`

only on the main thread.

This example allows one frame of stale `_maxDistance`

or `_fieldOfView`

. That may suit lock-on assistance, LOD, or visual filtering, but not damage, server validation, deterministic replays, or ranking logic. Those paths need a request ID or deterministic synchronization.

This is a design excerpt, not a drop-in sample. Registration APIs, capacity growth, the complete

`TargetAgent`

, and tests are omitted.

```
using System.Collections.Generic;
using Unity.Collections;
using Unity.Jobs;
using Unity.Mathematics;
using UnityEngine;
public sealed class TargetEvaluationSystem : MonoBehaviour
{
[SerializeField] private Transform _observer;
[SerializeField] private List<TargetAgent> _targets =
new List<TargetAgent>();
[SerializeField, Min(1)] private int _capacity = 1024;
[SerializeField, Min(0f)] private float _maxDistance = 30f;
[SerializeField, Range(1, 179)] private float _fieldOfView = 100f;
private NativeArray<TargetInput> _inputs;
private NativeArray<TargetEvaluation> _outputs;
private TargetAgent[] _scheduledTargets;
private int[] _scheduledVersions;
private JobHandle _pending;
private int _pendingCount;
private bool _isDisposed;
private void Awake()
{
int capacity = math.max(1, _capacity);
_inputs = new NativeArray<TargetInput>(
capacity, Allocator.Persistent,
NativeArrayOptions.UninitializedMemory);
_outputs = new NativeArray<TargetEvaluation>(
capacity, Allocator.Persistent,
NativeArrayOptions.UninitializedMemory);
_scheduledTargets = new TargetAgent[capacity];
_scheduledVersions = new int[capacity];
}
private void Update()
{
CompleteAndApply();
if (_isDisposed || !isActiveAndEnabled || _observer == null)
return;
int targetCount = _targets.Count;
Debug.Assert(
targetCount <= _inputs.Length,
"Target count exceeds NativeArray capacity.");
int count = math.min(targetCount, _inputs.Length);
for (int i = 0; i < count; i++)
{
TargetAgent target = _targets[i];
_scheduledTargets[i] = target;
_scheduledVersions[i] =
target != null ? target.EvaluationVersion : 0;
if (target == null || !target.isActiveAndEnabled)
{
_inputs[i] = default;
continue;
}
Vector3 p = target.transform.position;
_inputs[i] = new TargetInput
{
Position = new float3(p.x, p.y, p.z),
Threat = target.Threat,
IsActive = 1
};
}
if (count == 0)
return;
Vector3 op = _observer.position;
Vector3 forward = _observer.forward;
float maxDistanceSq = _maxDistance * _maxDistance;
var job = new EvaluateTargetsJob
{
Inputs = _inputs,
Outputs = _outputs,
ObserverPosition = new float3(op.x, op.y, op.z),
ObserverForward = math.normalizesafe(
new float3(forward.x, forward.y, forward.z)),
MaxDistanceSq = maxDistanceSq,
CosHalfFieldOfView = math.cos(
math.radians(_fieldOfView * 0.5f))
};
_pending = job.ScheduleParallelByRef(count, 64, default);
_pendingCount = count;
}
private void CompleteAndApply()
{
int count = _pendingCount;
if (count == 0)
return;
_pending.Complete();
_pendingCount = 0;
try
{
for (int i = 0; i < count; i++)
{
TargetAgent target = _scheduledTargets[i];
int version = _scheduledVersions[i];
if (target == null ||
!target.isActiveAndEnabled ||
target.EvaluationVersion != version)
{
continue;
}
TargetEvaluation value = _outputs[i];
target.ApplyEvaluation(
value.Score, value.IsCandidate != 0);
if (_isDisposed || !isActiveAndEnabled)
break;
}
}
finally
{
ClearScheduledReferences(count);
}
}
private void OnDisable() => CompleteWithoutApply();
private void OnDestroy()
{
_isDisposed = true;
CompleteWithoutApply();
if (_inputs.IsCreated)
_inputs.Dispose();
if (_outputs.IsCreated)
_outputs.Dispose();
}
private void CompleteWithoutApply()
{
int count = _pendingCount;
if (count == 0)
return;
_pending.Complete();
_pendingCount = 0;
ClearScheduledReferences(count);
}
private void ClearScheduledReferences(int count)
{
System.Array.Clear(_scheduledTargets, 0, count);
System.Array.Clear(_scheduledVersions, 0, count);
}
}
```

The next `Update`

completes the previous job before reusing the arrays. Removal code must also advance the target version.

`finally`

clears managed references but does not swallow exceptions. This sample is fail-fast; a system that must continue should catch individual callbacks and define recovery.

Capacity overflow triggers `Debug.Assert`

; production code should define a hard limit or resize only after the pending job completes.

## Build pipelines instead of isolated jobs

Pass one job's handle into the next instead of completing between stages. Use `JobHandle.CombineDependencies`

when several independent jobs feed one later stage. Keep data in NativeContainers through evaluation and reduction, then copy only the smallest required result back to GameObjects.

Do not let parallel iterations update one shared maximum. Write one score per index, then run a dependent single `IJob`

reduction. A linear final pass is often cheap and gives deterministic tie-breaking.

##
Variable-length output and `ParallelWriter`

Use a container-specific writer when parallel iterations append results.

```
[ReadOnly] public NativeArray<TargetEvaluation> Evaluations;
public NativeList<int>.ParallelWriter CandidateIndices;
public void Execute(int index)
{
if (Evaluations[index].IsCandidate != 0)
CandidateIndices.AddNoResize(index);
}
```

`AddNoResize`

requires enough Capacity before scheduling. When reusing the list, complete the previous writer, call `Clear()`

on the main thread, verify Capacity, and schedule again.

Parallel append order is undefined. If order affects state, sort afterward, compact fixed flags in source order, or preserve source indices with an explicit tie rule.

## NativeContainer lifetime and batch size

Use `Temp`

for extremely short-lived data, `TempJob`

for short jobs disposed within four frames, and `Persistent`

for explicitly owned buffers. For every-frame work, allocate persistent capacity once and reuse it. One owner should control allocation, the outstanding handle, resizing, and disposal. Never resize or dispose while a job may access the memory; call `Complete()`

even when `IsCompleted`

is true. See the NativeContainer manual.

Batch size also needs measurement. Start around 64 for light work, 16 or 32 for medium work, and 1 for expensive iterations; compare average time, worst frames, and the wait at `Complete()`

.

## GameObjects, Transforms, and data boundaries

A Burst job cannot directly access a normal `GameObject`

or `MonoBehaviour`

.

**Snapshot values:** copy Transform data into NativeArrays. This suits multi-stage numerical pipelines, but collection and application costs must be measured.

**Use IJobParallelForTransform:** process a

`TransformAccessArray`

. Use read-write scheduling when modifying Transforms and read-only scheduling when reading; read-only jobs may receive invalid entries, so check `TransformAccess.isValid`

. Frequent additions and removals make maintenance and index mapping part of the cost. See `IJobParallelForTransformExtensions`

.## Write kernels Burst can optimize

Keep managed references outside the kernel and copy only required values before scheduling. Prefer Unity.Mathematics and squared-distance comparisons for numerical work.

Do not enable `FloatMode.Fast`

automatically. Approximate visuals may tolerate it; replay, server validation, and cross-device agreement require error and reproducibility tests.

Per-element `FunctionPointer<T>`

calls retain overhead and can block wider vectorization. Prefer direct job code or batched calls; see Burst's Function Pointer guidance.

Treat Safety System errors as design feedback. Prefer fixed-index output, dependency chains, staged reductions, or supported writers before disabling restrictions. Pass mutable settings through the job struct, not mutable static state.

## Invalidate results instead of canceling jobs

A scheduled job cannot be interrupted halfway through. When a result becomes obsolete, let the job finish and reject it with a generation or request ID. Split very long work into shorter jobs. This is usually safer than a cancellation flag because the main thread cannot freely mutate shared job memory after scheduling.

## Measure the complete system

Compare a normal C# loop, `RunByRef`

, `ScheduleByRef`

, and `ScheduleParallelByRef`

. Measure collection, scheduling, `Complete()`

wait, result application, and the whole frame. Reject the design if the kernel improves but the full boundary becomes slower.

Profile after Burst warm-up and decide in a Development Build on target hardware. For `WaitForJobGroup`

, inspect Timeline: completion timing, scheduling timing, dependency serialization, worker occupancy, and Burst compilation.

## A practical adoption sequence

- Extract numerical work from
`MonoBehaviour.Update`

- Express inputs and outputs as value-type arrays
- Validate results, disposal, invalidation, and scene transitions with
`RunByRef`

or`ScheduleByRef`

- Switch to
`ScheduleParallelByRef`

and measure batch size and independence - Schedule earlier and delay
`Complete()`

- Split work into dependent jobs only when profiling supports it

Common failures are per-frame allocation, immediate completion, many tiny jobs, excessive copying, suppressed safety errors, and assumed output order. Fix data and synchronization before adding more jobs.

## Conclusion

With Burst and the Job System, data boundaries and synchronization matter more than syntax.

- Keep Unity API access outside the kernel
- Reuse NativeContainers and complete jobs before reading, resizing, or disposal
- Chain work instead of waiting immediately
- Validate stale results and variable output order explicitly
- Measure the entire path on target hardware

Start with many similar elements and a result that can tolerate one frame of latency. Expand only where profiling proves a benefit.

## References

- Unity Manual: NativeContainer
- Unity Scripting API: IJobForExtensions
- Unity Scripting API: IJobParallelForTransformExtensions
- Unity Scripting API: JobHandle.Complete

This article was created with AI-assisted drafting. The author reviewed the technical content and makes the final publication decision.
