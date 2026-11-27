---
source: "https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao"
title: "CFAST Unity Dev Report #4: Building a Stateful Fortran Fire Simulation Worker for Unity"
author: "Hidenori Ishii"
date_published: "2026-11-26"
date_clipped: "2026-11-27"
category: "Game Development / Unity"
source_type: "rss"
---

# CFAST Unity Dev Report #4: Building a Stateful Fortran Fire Simulation Worker for Unity

## Table of Contents

- [Introduction](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#introduction)
- [1. Development Environment](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#1-development-environment)
- [2. Why a Stateful Fire Simulator Is Necessary](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#2-why-a-stateful-fire-simulator-is-necessary)
- [3. System Architecture](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#3-system-architecture)
- [4. Extending the Fortran Calculation Loop](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#4-extending-the-fortran-calculation-loop)
- [5. Preserving DASSL Solver State](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#5-preserving-dassl-solver-state)
- [6. Handling Changes in Simulation Inputs](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#6-handling-changes-in-simulation-inputs)
- [7. Designing the Communication Protocol](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#7-designing-the-communication-protocol)
- [8. Validating Native Inputs](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#8-validating-native-inputs)
- [9. Interprocess Communication](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#9-interprocess-communication)
- [10. Atomic Publication of Simulation Results](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#10-atomic-publication-of-simulation-results)
- [11. Asynchronous Process Management in CSharp](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#11-asynchronous-process-management-in-csharp)
- [12. Preventing Concurrent STEP Requests](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#12-preventing-concurrent-step-requests)
- [13. Separating the Different Time Domains](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#13-separating-the-different-time-domains)
- [14. Accepting Simulation Results Safely](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#14-accepting-simulation-results-safely)
- [15. Validating Simulation Continuity](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#15-validating-simulation-continuity)
- [16. Connecting Loading and Gameplay](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#16-connecting-loading-and-gameplay)
- [17. Model Identity and Build Provenance](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#17-model-identity-and-build-provenance)
- [18. Worker Lifecycle Management](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#18-worker-lifecycle-management)
- [19. Validation Results](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#19-validation-results)
- [20. Similarities to Embedded Software Engineering](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#20-similarities-to-embedded-software-engineering)
- [21. AI-Assisted Native Software Development](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#21-aiassisted-native-software-development)
- [22. Current Limitations](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#22-current-limitations)
- [23. Interactive Technical Documentation](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#23-interactive-technical-documentation)
- [24. Conclusion](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#24-conclusion)
- [References](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#references)
- [About the Project](https://dev.to/47_robin_ebe9e47eb349d767/cfast-x-unity-dev-report-4-building-a-stateful-fortran-fire-simulation-worker-for-unity-9ao#about-the-project)

---

## Introduction

I am an independent developer working on a firefighting and disaster response game called **SOKYU: OPERATION RESCUE BLAZE SERIES**.

The project combines Unity game development, embedded systems, robotics, artificial intelligence, and scientific fire simulation.

In the previous development reports, I introduced how I integrated CFAST, a fire simulator developed by the National Institute of Standards and Technology (NIST), into an interactive game environment.

| Report | Technical Focus |
| --- | --- |
| #1 | Fire simulation integration and numerical stability |
| #2 | Multiple fire sources, fuel consumption, and asynchronous state management |
| #3 | Real-time smoke rendering and performance optimization |
| #4 | Stateful native simulation and interprocess communication |

In this fourth report, I will focus on the software architecture behind these features.

CFAST is written primarily in Fortran, while Unity gameplay logic is implemented in C#.

The challenge is to connect these two systems without losing the internal state of the fire simulation or blocking the game's main thread.

Rather than repeatedly starting a conventional CFAST simulation, I developed a **stateful CFAST derivative that operates as an independent native worker**.

This article introduces the actual implementation architecture, including selected Fortran and C# code excerpts.

---

## 1. Development Environment

The integration uses the following technologies.

| Component | Technology |
| --- | --- |
| Game engine | Unity |
| Gameplay programming | C# |
| Fire simulator | CFAST 7.7.7 |
| Native programming | Fortran |
| Numerical solver | DASSL |
| Communication | Standard input and result files |
| Asynchronous execution | Task, async, await |
| Data integrity | SHA-256 |
| Development assistance | OpenAI Codex |

The CFAST derivative is based on a specific upstream revision.

```
CFAST Version: 7.7.7

Upstream Commit:
b43e74e0f43c704582c5782f5446597ce729a07f
```

Official repository:

<https://github.com/firemodels/cfast>

Pinning the upstream revision makes it possible to identify exactly which scientific simulation implementation the derivative is based on.

---

## 2. Why a Stateful Fire Simulator Is Necessary

A conventional fire simulation workflow generally starts with predefined input conditions.

```
Building Model
      |
Fire and Ventilation Conditions
      |
CFAST Execution
      |
Simulation Results
```

This workflow is suitable when the simulation scenario is known before execution.

An interactive game is different.

During gameplay, a player may:

- Open or close a door.
- Open a window.
- Apply water to a fire.
- Extinguish a fire.
- Change the combustion conditions inside a compartment.

These events cannot all be defined in advance.

More importantly, the state of the fire depends on its previous history.

Opening a door ten seconds after ignition is not necessarily equivalent to opening the same door sixty seconds after ignition.

The temperature, smoke accumulation, oxygen concentration, and wall thermal conditions may already be different.

Restarting CFAST from its initial state whenever an input changes would lose that history.

I therefore extended CFAST so that it can receive new input conditions at accepted simulation boundaries while preserving its internal physical state.

---

## 3. System Architecture

The CFAST worker runs as a separate native process rather than executing directly inside Unity's managed runtime.

The actual SOKYU integration contains the following principal components.

| Component | Responsibility |
| --- | --- |
| StageTwoCfastBackground | Stage02 gameplay integration |
| CfastLiveSession | Request ownership and result acceptance |
| CfastLiveProcessTransport | Native process communication |
| live\_inputs.f90 | Native input validation and application |
| solve.f90 | CFAST numerical calculation loop |
| DASSL | Numerical integration |
| BlazeZeroCfastSmokeVolume | Compartment smoke rendering |

The overall architecture is:

```
SOKYU / UNITY / C#
+---------------------------------------+
| Gameplay Logic                        |
| Fire Sources / Doors / Windows        |
|                 |                     |
| StageTwoCfastBackground               |
|                 |                     |
| CfastLiveSession                      |
|                 |                     |
| CfastLiveProcessTransport             |
+-----------------+---------------------+
                  |
                  | STEP / FIRE / VENTG
                  | Standard Input
                  v
CFAST NATIVE WORKER / FORTRAN
+---------------------------------------+
| live_inputs.f90                       |
|                 |                     |
| solve.f90                             |
|                 |                     |
| DASSL Numerical Integration           |
|                 |                     |
| Persistent Physical State             |
|                 |                     |
| Simulation Snapshot                   |
+-----------------+---------------------+
                  |
                  | Atomic Result File
                  v
UNITY RESULT VALIDATION
+---------------------------------------+
| Current / AcceptedStep                |
|                 |                     |
| Fire / Fuel State                     |
| Indoor Volumetric Smoke               |
| Opening Smoke Rendering               |
+---------------------------------------+
```

The native worker preserves the simulation state while Unity continues processing the game.

This architecture separates gameplay execution, scientific computing, communication, and graphics rendering.

---

## 4. Extending the Fortran Calculation Loop

The main modification is applied to the CFAST numerical calculation loop.

The relevant upstream file is:

```
Source/CFAST/solve.f90
```

The conventional calculation loop contains a termination condition based on the specified simulation end time.

```
do while (idid>=0 .and. t+0.000001_eb<=tstop)
```

In the stateful derivative, the loop condition also considers whether live simulation mode is active.

```
do while (idid>=0 .and. &
    (t+0.000001_eb<=tstop.or.live_active))
```

This allows the calculation loop to remain active across multiple externally supplied simulation requests.

However, simply keeping the loop alive is not sufficient.

The worker must stop at the requested simulation boundary, publish the accepted result, and wait for the next command.

The following code is adapted from the actual patch, with performance instrumentation omitted.

```
if(live_active.and.idid>0.and.t==live_target)then

    call update_data(p,odevara)
    call update_data(p,odevarc)

    call update_species(0._eb)

    call snapshot(t,total_steps, &
        rwork,iwork,info,pprime,rpar(1))

    call next_request(t,tstop,live_changed)

    if(live_done)exit

    if(live_changed)call live_rebase( &
        t,n_odes,info,rwork, &
        pdzero,pdnew,rpar,ipar)

end if
```

The important operations are:

1. Reach the requested simulation boundary.
2. Synchronize the accepted numerical state.
3. Generate a simulation snapshot.
4. Publish the result.
5. Receive the next request.
6. Apply changes to the simulation inputs.
7. Continue from the accepted state.

The same invocation of the native simulation loop remains active.

The calculation is not reconstructed from the previously exported snapshot.

---

## 5. Preserving DASSL Solver State

CFAST uses DASSL to solve differential-algebraic equations.

A general DAE system can be expressed as:

$$  
F(t,y,\dot{y})=0  
$$

DASSL maintains internal information required for numerical integration.

The stateful derivative retains the relevant solver arrays and physical state within the running worker.

| Variable | General Purpose |
| --- | --- |
| p | Current numerical state |
| pprime | Time derivative of the state |
| rwork | Real-valued solver workspace |
| iwork | Integer solver workspace |
| info | Solver control information |

In addition to these arrays, the worker retains physical simulation history.

This includes compartment conditions, species quantities, wall conduction, target states, ignition events, and accumulated quantities such as fuel pyrolysis.

The distinction between internal state and exported results is important.

```
Internal CFAST State
----------------------------
Solver Workspace
Physical State
Gas Species History
Wall Conduction
Ignition and Event State
Accumulated Quantities
             |
             | Selected Observation
             v
Exported Snapshot
----------------------------
Room Conditions
Fire Conditions
Opening Flow Conditions
Simulation Time
```

The snapshot is an observation intended for Unity.

It is not a complete restart checkpoint containing every piece of internal information required to reconstruct the native solver.

When no simulation input changes, the derivative does not deliberately reset DASSL at every STEP boundary.

---

## 6. Handling Changes in Simulation Inputs

A player opening a door changes the gas transport conditions.

A player extinguishing a fire changes the requested heat release rate.

These changes can modify the equations being evaluated by the solver.

Preserving the physical state does not mean that numerical reinitialization must never occur.

When the input changes, the derivative uses the existing CFAST solver reinitialization mechanism while retaining the accepted physical state.

The actual implementation includes the following rebasing operation.

```
told=t

pold(1:nequals)=p(1:nequals)

ipar(2)=1
ires=0

call calculate_residuals( &
    t,p,pdzero,pdnew,ires,rpar,ipar)

call require(ires==0,'input residual')

pdold(n_odes+1:nequals)= &
    pdnew(n_odes+1:nequals)

call set_info_flags(info,rwork)
```

This code evaluates the residual using the updated conditions and rebases the relevant non-ODE flow history before invoking the existing solver initialization mechanism.

The compartment, gas species, and wall thermal states are not reset to their original values.

The intended behavior is:

```
Accepted Physical State
          |
     Input Changes?
       /       \
     No         Yes
      |          |
Continue      Re-evaluate
Solver        Residual
History          |
              Rebase Flow
              Information
                 |
          Solver Reinitialization
                 |
      Continue Physical Simulation
```

This is the meaning of stateful simulation in this project.

The physical simulation continues across requests, while numerical solver preparation is performed when required.

---

## 7. Designing the Communication Protocol

Unity and the Fortran worker exchange information using a custom text-based protocol.

The protocol is designed to preserve the relationship between:

- The execution session
- The simulation model
- The STEP number
- The previous accepted simulation time
- The next requested simulation time
- The fire and opening conditions

### 7.1 STEP Request

The basic request format is:

```
STEP runBase64url epoch modelSHA256 step fromSeconds targetSeconds fireUpdateCount wallVentUpdateCount
```

| Field | Meaning |
| --- | --- |
| runBase64url | Encoded execution session identifier |
| epoch | Session generation |
| modelSHA256 | Simulation model identity |
| step | Sequential request number |
| fromSeconds | Previously accepted simulation time |
| targetSeconds | Requested simulation time |
| fireUpdateCount | Number of fire update records |
| wallVentUpdateCount | Number of wall vent update records |

The run identifier uses canonical, unpadded Base64url encoding.

This avoids problematic characters that could otherwise interfere with Fortran list-directed input.

### 7.2 Fire Source Input

The fire source update format is:

```
FIRE id hrrWatts heatOfCombustionJoulesPerKg
```

The fire ID refers to the native model's one-based fire ordinal, not a Unity GameObject name.

The requested heat release rate and heat of combustion are used to define the prescribed fuel pyrolysis rate.

```
fireinfo(id)%qdot(1)=q(i)

fireinfo(id)%mdot(1)=q(i)/hoc(i)

fireinfo(id)%hoc(1)=hoc(i)
```

The relationship is:

$$

# \dot{m}\_{fuel}

\frac{\dot{Q}\_{requested}}{\Delta H\_c}  
$$

The actual HRR calculated by CFAST can differ from the requested HRR because of oxygen limitations and other modeled combustion conditions.

### 7.3 Opening Input

Wall opening conditions are updated using:

```
VENT id openingFraction
```

A geometry-enabled update can also be submitted.

```
VENTG id openingFraction width sill soffit
```

This extended record includes the opening width, lower edge, and upper edge.

It is used to represent dynamic opening conditions derived from the Unity building.

For example, a door operation can change the effective opening condition submitted to the worker.

The current dynamic input protocol supports wall vents. Dynamic control of horizontal and mechanical vents is outside the implemented protocol described here.

---

## 8. Validating Native Inputs

The communication protocol must reject invalid data before changing the native simulation state.

The Fortran input implementation contains explicit validation.

```
call require(from==t.and.target>from, &
    'request time range')

call require(step==live_step+1.and.epoch>=0, &
    'step sequence')

call require(hash==model_hash, &
    'model identity')
```

Fire input values are also validated.

```
call require(q(i)>=0.and.hoc(i)>0, &
    'fire units/range')
```

Opening fractions must remain within the permitted range.

```
call require(f(i)>=0.and.f(i)<=1, &
    'vent fraction')
```

Additional checks cover duplicate IDs, invalid record counts, model identity, and non-finite numerical values.

Importantly, the implementation validates the entire input batch before applying changes to the model.

```
Receive Request
      |
Validate Request Header
      |
Validate All FIRE Records
      |
Validate All VENT Records
      |
All Records Valid?
    /      \
  No        Yes
   |         |
Reject     Apply Input
Request    Changes
```

This avoids accepting the valid portion of a request while leaving the simulation in a partially updated state because another record was invalid.

For a stateful simulator, input validation is part of maintaining numerical and application-level consistency.

---

## 9. Interprocess Communication

The native communication architecture combines standard input and file-based result exchange.

| Communication | Mechanism |
| --- | --- |
| Unity to CFAST | Standard input |
| CFAST startup acknowledgement | ready file |
| CFAST to Unity | Result files |
| Standard output | Diagnostic log |
| Standard error | Diagnostic log |

The diagnostic streams are separated from the machine-readable simulation results.

This prevents ordinary diagnostic messages from being interpreted as protocol records.

The worker operates in a dedicated execution directory.

```
Session Directory/
|
+-- model.in
+-- stdout.log
+-- stderr.log
|
+-- wire/
    |
    +-- ready
    +-- step-1.result
    +-- step-2.result
    +-- step-3.result
```

Each request advances the same native simulation process.

A new process is not started for each STEP.

---

## 10. Atomic Publication of Simulation Results

File-based communication introduces a potential race condition.

A file may already exist while its contents are still being written.

If Unity reads it at that moment, the result may be incomplete.

The native publication protocol therefore uses the following sequence.

```
Write Temporary Result
          |
Close Temporary File
          |
Rename Within the Same Filesystem
          |
Publish Final Result Filename
          |
Unity Reads Final Result
          |
Validate and Accept
```

For example:

```
step-42.result.tmp
          |
          | Close + Rename
          v
step-42.result
```

Unity consumes the final filename rather than the temporary file.

This provides an atomic publication boundary under the expected same-filesystem rename semantics.

It does not provide a persistent recovery checkpoint or guarantee durability after every possible operating system failure.

The purpose is to prevent a partially written simulation result from being accepted as a complete observation.

---

## 11. Asynchronous Process Management in CSharp

On the Unity side, native process communication is managed by `CfastLiveProcessTransport`.

The worker is started using the .NET process API.

```
var start = new ProcessStartInfo(executable, "model.in")
{
    WorkingDirectory = directory,
    UseShellExecute = false,
    CreateNoWindow = true,
    RedirectStandardInput = true,
    RedirectStandardOutput = true,
    RedirectStandardError = true
};
```

The native process runs independently of the Unity main thread.

STEP requests are executed asynchronously.

The following simplified excerpt illustrates the structure.

```
return Task.Run(async () =>
{
    using var deadline =
        CancellationTokenSource.CreateLinkedTokenSource(
            cancellation);

    deadline.CancelAfter(timeout);

    // Start the worker when necessary.
    // Submit the request.
    // Wait for the result.
    // Parse and validate the response.
});
```

The main objective is to avoid blocking Unity's gameplay thread while scientific computation is in progress.

However, asynchronous execution does not eliminate numerical calculation delays.

If CFAST becomes unresponsive, Unity can continue processing the game, but new simulation data will not be available.

That distinction was particularly important in the numerical stability investigation introduced in Development Report #1.

---

## 12. Preventing Concurrent STEP Requests

The worker represents a sequential simulation.

A STEP request must begin from the previously accepted native simulation state.

Submitting multiple requests concurrently would complicate the relationship between the current native state and the requested simulation times.

The transport therefore permits only one request in flight.

```
if (Interlocked.CompareExchange(
        ref inFlight, 1, 0) != 0)
{
    throw new InvalidOperationException(
        "One native request may be in flight.");
}
```

The intended execution sequence is:

```
Accepted State S0
        |
      STEP 1
        |
Accepted State S1
        |
      STEP 2
        |
Accepted State S2
        |
      STEP 3
        |
Accepted State S3
```

Each request has an explicit starting state and target time.

This is not a parallel simulation of several independent future states.

The single-request constraint makes the ownership and continuity of the native simulation easier to validate.

---

## 13. Separating the Different Time Domains

A real-time game and a numerical simulator use different concepts of time.

The current implementation distinguishes between several time domains.

| Time Domain | Meaning |
| --- | --- |
| Unity frame time | Time associated with game and rendering frames |
| Gameplay time | Elapsed time within the game |
| Committed simulation time | Last accepted CFAST time |
| Requested target time | Next simulation boundary |
| DASSL internal time step | Numerical integration interval |
| File polling interval | Result-file observation interval |

The result file polling implementation contains the following code.

```
while (!File.Exists(path))
{
    cancellation.ThrowIfCancellationRequested();

    if (!IsAvailable)
        throw new IOException(
            "Native worker terminated without a complete observation.");

    await Task.Delay(10, cancellation)
        .ConfigureAwait(false);
}
```

The 10 ms delay is an I/O polling interval.

**It is not the CFAST simulation time step.**

DASSL determines its internal integration steps according to the numerical calculation.

Similarly, Unity may render several frames between accepted CFAST updates.

```
CFAST SIMULATION

State A ---------- State B -------- State C

UNITY RENDERING

Frame 1  Frame 2  Frame 3  Frame 4  Frame 5
   |        |        |        |        |
State A  State A  State B  State B  State C
```

This diagram is conceptual and does not represent measured frame or solver timing.

Separating these time domains is essential when connecting a scientific simulator to a real-time graphics application.

---

## 14. Accepting Simulation Results Safely

A completed asynchronous task does not automatically become the current gameplay state.

The project uses `CfastLiveSession` to manage requests and accepted observations.

The request creation process includes a stamp containing the session identity, model identity, request number, and simulation boundaries.

```
var stamp = new CfastStepStamp(
    runId,
    epoch,
    modelHash,
    checked(step + 1),
    CommittedSeconds,
    targetSeconds);
```

The session starts the asynchronous operation.

```
pending = transport.StepAsync(
    request,
    cancellation.Token);
```

When the owner calls `Pump`, the session checks whether the result can be accepted.

```
if (retired || paused ||
    pending == null || !pending.IsCompleted)
    return false;

var result = pending.GetAwaiter().GetResult();

Validate(result);

var accepted = new CfastLiveAcceptedStep(
    request.Stamp,
    request.Input,
    result);

Current = result;
AcceptedStep = accepted;
```

Although `GetResult()` appears in this code, the task completion state is checked first.

The owner does not deliberately block while waiting for an unfinished numerical calculation.

The result acceptance process is therefore:

```
Native Calculation Completed
            |
         Task Ready
            |
       Unity Session Pump
            |
       Validate Response
            |
       Validation Passed?
          /      \
        No        Yes
         |         |
     Reject      Update
     Result      Current State
                    |
              Fire and Smoke
              Visualization
```

An asynchronous operation completing and a simulation state being accepted are two separate events.

This is an important architectural decision in the SOKYU implementation.

---

## 15. Validating Simulation Continuity

Each native result is validated before it becomes the current simulation state.

The validation includes:

| Validation Item | Purpose |
| --- | --- |
| Session identity | Prevent mixing different runs |
| Epoch | Identify the correct execution generation |
| Model SHA-256 | Verify the input model |
| STEP number | Match request and response |
| Actual simulation time | Verify the requested boundary |
| Compartment count | Verify result layout |
| Fire count | Verify native fire mapping |
| Opening count | Verify native opening mapping |
| Process ID | Check worker continuity |
| Accepted internal steps | Check numerical progression |
| DASSL initialization count | Check counter continuity |

One of the actual continuity checks is:

```
if (Current != null &&
    (result.ProcessId != Current.ProcessId ||
     result.AcceptedSteps <= Current.AcceptedSteps ||
     result.DasslInitializations <
         Current.DasslInitializations))
{
    throw new InvalidDataException(
        "Native continuity mismatch.");
}
```

These checks are designed to prevent unexpected discontinuities in the accepted observation sequence.

A matching process ID does not prove that the physical simulation is correct.

Similarly, a monotonically increasing solver counter does not establish numerical accuracy.

However, these observations help verify that the same native calculation process is continuing as intended.

---

## 16. Connecting Loading and Gameplay

Stage02 uses an introductory heat release history during its initial loading sequence.

The objective is to allow gameplay to begin with an existing fire environment rather than starting every simulation from an entirely clear compartment.

The loading sequence prepares the native model and worker, then advances the introductory simulation.

```
Stage02 Loading
      |
Load Archived HRR Input
      |
Generate Native Model
      |
Extract and Validate Worker
      |
Start CFAST
      |
Advance Introductory Simulation
      |
Accept Final Introductory State
      |
Begin Gameplay
      |
Continue Using the Same Worker
```

The same worker continues operating after the introductory phase.

Its compartment conditions and numerical history are not discarded when gameplay begins.

The Unity-side implementation determines the next target time using the introductory simulation boundary and elapsed gameplay time.

```
double target =
    intro.EndSeconds +
    (elapsed - adoptedAt.Value);

if (session.HasPending ||
    target <= session.CommittedSeconds)
{
    return;
}
```

A new request is issued only when the previous request is no longer pending and the target time advances beyond the accepted simulation time.

The introductory fire history and the subsequent player-driven conditions are connected through the same stateful simulation process.

---

## 17. Model Identity and Build Provenance

CFAST fire IDs and opening IDs are specific to a particular input model.

Changing a model without updating the associated mappings could cause a Unity command to affect the wrong native fire or opening.

To reduce this risk, the project verifies model identity using SHA-256.

```
using (var hash = SHA256.Create())
using (var file = File.OpenRead(copied))
{
    modelHash = BitConverter
        .ToString(hash.ComputeHash(file))
        .Replace("-", "")
        .ToLowerInvariant();
}

if (modelHash != request.Stamp.ModelId)
{
    throw new InvalidDataException(
        "Input file SHA256 mismatch.");
}
```

The bundled worker is also associated with a pinned manifest and executable hash.

The build process retains information about:

- Upstream CFAST revision
- Source file hashes
- Applied patches
- Compiler information
- Build inputs
- Generated worker identity

The original upstream source and executable are not directly overwritten.

Instead, the derivative is built from a preserved source snapshot in a separate build environment.

```
Official CFAST Source
          |
Pinned Source Revision
          |
Separate Build Directory
          |
Apply Live Integration Patch
          |
Add Native Integration Modules
          |
Compile Native Worker
          |
Record Build Provenance
          |
Package Worker for Unity
```

SHA-256 verification confirms artifact identity.

It does not independently establish the physical validity of the simulation model.

---

## 18. Worker Lifecycle Management

The native worker has an explicit lifecycle associated with the game session.

```
Create Session
      |
Prepare Workspace
      |
Start Native Worker
      |
Submit and Accept STEP Requests
      |
Stage Ends or Session Fails
      |
Retire Session
      |
Release Native Process
      |
Wait for Log Streams to Finish
      |
Release Workspace
```

When a session is retired, subsequent responses are not permitted to update its accepted state.

This is important because asynchronous operations can complete after the game has already transitioned to another state.

The implementation also waits for relevant native process and log operations before completing workspace release.

The current implementation does not automatically reconstruct the full CFAST simulation state in a replacement worker after an abnormal termination.

That would require a separate recovery design.

A previously accepted observation is not sufficient to restore every internal DASSL and CFAST state variable.

---

## 19. Validation Results

The stateful worker is the foundation of the Stage02 Hall integration and smoke rendering system.

Following the building model correction described in Development Report #1, the following results were obtained using the existing production worker and the revised Stage02 model.

| Validation Item | Result |
| --- | --- |
| Previously unresponsive conditions resolved | 3 / 3 |
| Native STEP responses | 1,078 / 1,078 |
| Unity tests | 37 / 37 |
| Failed Unity tests | 0 |
| Skipped Unity tests | 0 |
| Independent review | PASS |
| Outstanding review findings | 0 |

The Unity tests covered three gameplay modes:

- AIM3D
- AIM3D2
- ZERO

In the tested scenes, the accepted CFAST simulation time advanced beyond 20 seconds while indoor smoke and opening smoke updates continued.

Additional checks included water damage retention, entrance door operation in ZERO, and native worker release when returning to the title screen.

These results apply to the specific Stage02 integration and tested configurations.

They are not a general performance benchmark of every possible CFAST model or execution environment.

---

## 20. Similarities to Embedded Software Engineering

One of the interesting aspects of this project is how closely its architecture resembles embedded software engineering.

Although Unity is a game engine, many of the underlying technical challenges are system-level problems.

| Embedded Software Concept | Application in SOKYU |
| --- | --- |
| Task communication | Unity and native worker communication |
| State machine | Simulation session lifecycle |
| Exclusive access | Single in-flight STEP request |
| Asynchronous events | Native calculation completion |
| Input validation | FIRE and VENT record validation |
| Data consistency | Request and response identity |
| Timeout management | Unresponsive worker detection |
| Resource management | Native process and workspace release |
| Version management | Model and worker identity |
| Diagnostic logging | Separate native output streams |

As someone with experience in embedded software development, I find these similarities particularly interesting.

The game engine provides the interactive environment.

The scientific simulator provides numerical calculations.

The software architecture connects these systems through clearly defined interfaces and state ownership.

---

## 21. AI-Assisted Native Software Development

This project is being developed with the assistance of OpenAI Codex.

The development work extends beyond generating Unity C# scripts.

It includes:

- Investigating the upstream Fortran source code
- Understanding the CFAST calculation loop
- Implementing native input control modules
- Designing communication protocols
- Investigating numerical solver behavior
- Developing C# asynchronous communication
- Performing regression tests
- Conducting independent code reviews

The upstream numerical implementation is preserved, and modifications are managed as a separate derivative.

Implementation and review responsibilities are separated.

I also distinguish approved requirements from proposed functionality so that automated testing does not unnecessarily expand the development scope.

AI-assisted development makes it possible to investigate unfamiliar technical domains.

However, defining the engineering objective, understanding the meaning of the calculation results, and deciding which changes should be adopted remain essential developer responsibilities.

---

## 22. Current Limitations

The stateful CFAST integration provides a foundation for simulation-driven gameplay, but it has several limitations.

| Feature | Current Scope |
| --- | --- |
| Persistent native calculation | Implemented |
| Dynamic fire inputs | Implemented |
| Dynamic wall vent inputs | Implemented |
| Geometry-enabled opening inputs | Implemented |
| Asynchronous communication | Implemented |
| Result validation | Implemented |
| Automatic full-state restoration | Not implemented |
| Dynamic horizontal vent protocol | Not implemented |
| Stage02 LAN integration | Outside the current native integration path |

The ordinary Stage02 CFAST integration in the inspected implementation targets supported macOS ARM64 modes.

Full Windows, LAN, and production deployment validation should be considered separately.

The architecture allows incremental simulation during gameplay, but this does not guarantee that every simulation request will complete within real-time constraints.

The physical limitations of CFAST as a zone model also remain.

This project is being developed as a game rather than a validated engineering tool for real-world fire prediction.

---

## 23. Interactive Technical Documentation

I have also prepared technical documentation on the SOKYU project website.

The website presents the fire simulation architecture through visual diagrams, animations, and interactive explanations.

### CFAST × Unity Technical Guide

[Explore the CFAST and Unity Fire Simulation Guide](https://ronsard.sakura.ne.jp/sokyu/cfast-guide.html)

### Stage02 Technical Validation

[Stage02 — Numerical Stability, Smoke Rendering, and Opening Control](https://ronsard.sakura.ne.jp/sokyu/cfast-guide.html#stage02-validation)

Topics include:

- CFAST's two-zone model
- Stateful simulation architecture
- Compartment and opening geometry
- Indoor volumetric smoke
- Opening smoke transport
- Numerical solver instability
- Building model corrections
- Rendering performance optimization
- Interactive interior doors

The documentation is primarily presented in Japanese, with visual diagrams and animations explaining the technical concepts.

---

## 24. Conclusion

In this development report, I introduced the stateful Fortran-based CFAST worker that supports the fire simulation system in SOKYU: OPERATION RESCUE BLAZE SERIES.

The main engineering challenges included:

- Extending the CFAST numerical calculation loop
- Preserving physical and numerical state across requests
- Handling dynamic changes to fire and opening conditions
- Designing a language-independent communication protocol
- Publishing simulation observations atomically
- Managing asynchronous native execution in C#
- Preventing concurrent simulation requests
- Validating the identity and continuity of simulation results
- Connecting introductory simulation and normal gameplay
- Managing native worker lifecycles

Integrating scientific computing into a game engine requires more than connecting an external executable.

It requires a software architecture that respects the numerical model, preserves state ownership, and maintains reliable communication between independent execution environments.

The stateful CFAST worker is the computational foundation behind the fire behavior, smoke transport, and interactive environmental changes introduced in the previous reports.

In the next development report, I will investigate a particularly challenging issue encountered during development:

**Debugging Numerical Stalls in Fortran-Based CFAST and DASSL Through Residual Analysis.**

That report will focus on Newton iteration, discontinuous gas-layer assignment, convergence rejection, and numerical time-step reduction.

---

## References

- [NIST CFAST Official Website](https://pages.nist.gov/cfast/)
- [CFAST Official GitHub Repository](https://github.com/firemodels/cfast)
- [CFAST Version 7.7.7 — Development Baseline Source Code](https://github.com/firemodels/cfast/tree/b43e74e0f43c704582c5782f5446597ce729a07f)
- [CFAST Version 7 Technical Reference Guide](https://doi.org/10.6028/NIST.TN.1889v1)
- [NIST Fire Dynamics Simulator and Smokeview](https://pages.nist.gov/fds/)

---

## About the Project

**SOKYU: OPERATION RESCUE BLAZE SERIES**

An independently developed firefighting and disaster response game combining:

- Scientific fire simulation
- Unity game development
- Fortran and C# integration
- Real-time computer graphics
- Embedded systems
- Robotics
- Artificial intelligence

Developed by **Motomachi Digital Making Lab**, Yokohama, Japan.

Project Technical Website:

<https://ronsard.sakura.ne.jp/sokyu/cfast-guide.html>

Stage02 Technical Validation:

<https://ronsard.sakura.ne.jp/sokyu/cfast-guide.html#stage02-validation>

---

**CFAST × Unity Development Report #4**

November 26, 2026
