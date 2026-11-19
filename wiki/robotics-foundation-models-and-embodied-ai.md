# Robotics Foundation Models and Embodied AI

This page tracks foundation-model patterns for robots and embodied manipulation, especially evidence that pretraining, evaluation protocol, and real-robot task design transfer into practical automation.

## 2026-09-12 web-video pretraining for robot policies

### Sources
- [Rhoda AI: Does Scaling Web-Video Pre-training Help Real Robots Do Real Work?](../raw/2026-09-12-rss-tldr-ai-does-scaling-web-video-pre-training-help-real-robots-do-real-w.md)

### Typed entities
- `company/lab`: Rhoda AI
- `model family`: Direct Video-Action model / DVA
- `task`: industrial bearing unpacking and packaging-waste sorting
- `metric`: at-speed completion rate
- `metric`: DINO FD / Frechet distance over DINOv2 embeddings
- `artifact`: real-robot evaluation SOP
- `method`: web-video pretraining
- `method`: task-specific robot post-training
- `component`: inverse dynamics model

### Claims
- Rhoda AI reports that scaling general web-video pretraining by model size and training compute improved a real industrial robot bearing-unpacking task after task-specific post-training, with larger gains when robot demonstration data was scarce. confidence: 1 primary lab/source report, last-confirmed 2026-09-12. [source: raw/2026-09-12-rss-tldr-ai-does-scaling-web-video-pre-training-help-real-robots-do-real-w.md]
- The study uses a Direct Video-Action setup where a causal video model predicts future frames and a fixed inverse dynamics model turns those predictions into robot actions, holding the robot task, inverse dynamics model, inference frequency, and evaluation procedure fixed while varying the pre-trained video model. confidence: 1 source, last-confirmed 2026-09-12. [source: raw/2026-09-12-rss-tldr-ai-does-scaling-web-video-pre-training-help-real-robots-do-real-w.md]
- Rhoda reports that pretraining quality measured before robot post-training, using DINO FD on held-out web video, correlated with real-robot at-speed task completion across seven checkpoints in one architecture family. confidence: 1 source, last-confirmed 2026-09-12. [source: raw/2026-09-12-rss-tldr-ai-does-scaling-web-video-pre-training-help-real-robots-do-real-w.md]
- The report is careful about limitations: one task, one embodiment/setup, one post-training run per condition, correlational checkpoint selection, non-compute-matched size sweep, and over 200 hours of real-robot evaluation cost. confidence: 1 source, last-confirmed 2026-09-12. [source: raw/2026-09-12-rss-tldr-ai-does-scaling-web-video-pre-training-help-real-robots-do-real-w.md]

### Explicit relationships
- Robot-policy performance depends-on pretraining scale, task demonstration quality, checkpoint selection, embodiment, and a real-world scoring protocol rather than proxy loss alone.
- Held-out video-prediction quality can complement real-robot trials by ranking candidate checkpoints before expensive robot evaluation, but it does not supersede robot trials.
- Demonstration scarcity increases the value of better pretraining in the reported setup.

### HoneyDrunk implications
- If HoneyDrunk explores robotics or embodied simulation, require task-level metrics that include speed, completion, correctness, intervention rules, and trial-audit policy.
- Treat video-pretraining quality as a candidate triage metric, not as proof of deployment performance without target embodiment trials.
- Any simulation-to-real or robot-agent benchmark should record setup errors, exclusions, evaluator certification, and trial recordings; otherwise success rates are not decision-grade.

### Confidence and quality notes
- Quality posture: unusually decision-useful because the source reports task protocol, limitations, and real-robot trial counts. Still single-lab and single-task evidence; do not generalize to all robotics tasks without replication.
- Privacy filter: no private customer identity, operator personal details beyond public author/acknowledgment names, or unsafe robot-control procedures were promoted.


## 2026-09-22: Simulation tooling needs sensor and replay validation

### Typed entities

project: Unity Simulation Pro; project: Unity Industry; project: ROS 2; project: TIER IV; project: KITECH; concept: simulation clock; concept: hardware-in-the-loop.

### Claims and evidence

- Unity announces Simulation Pro early access for Unity Industry customers on Unity 6.3 or newer, including URDF import, LiDAR/image/IMU simulation, ROS 2 integration, and headless Linux builds. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-22-rss-unity-simulation-pro-sensor-validation.md)
- Vendor case studies describe staggered camera rendering, simulation-time and asset tuning, sensor packet reproduction, synchronized observations on one clock, recorded trajectories, and replayed procedures. They do not prove the new package supplied every capability of those earlier projects. confidence: 1 source, last-confirmed 2026-09-22 (archived attributed summary reviewed; no live refresh). [captured source](../raw/2026-09-22-rss-unity-simulation-pro-sensor-validation.md)

### Explicit relationships

Simulation-to-real work depends-on sensor timing, packet behavior, and measured fidelity. Repeatable inspection uses shared clocks and replay separately from visual presentation. See [[unity-3d-and-realtime-vfx-patterns]].

### Decision and quality notes

Vendor early-access release and case studies, not independent sensor-validation results. Verify licensing, runtime support, replay consistency, and actual sensor fidelity before adoption. Source-specific claims remain provisional single-source evidence; related articles and derived queries add no independent support. Open question: Which sensor packet, timing, shared-clock, deterministic-replay, headless-runtime, and license checks would qualify Simulation Pro for a specific HoneyDrunk simulation workload? See [[indexes/gaps]].


## 2026-11-19: SimReady validates asset properties separately from task behavior

### Typed entities

project: SimReady Central; project: Isaac Sim 6.2; library: OpenUSD; concept: profile validation; concept: contact-based grasp; file: raw/2026-11-16-rss-build-a-robot-pick-and-place-simulation-with-simready-assets.md.

### Claims and evidence

- The NVIDIA/Hugging Face walkthrough separates profile, feature and requirement checks from assembled-scene testing. Joints/drives plus collision/mass properties are a baseline; movement, contact, grasp, lift and placement need task tests. confidence: 1 source, last-confirmed 2026-11-19 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-16-rss-build-a-robot-pick-and-place-simulation-with-simready-assets.md)
- The example uses fixed positions, scripted waypoints, no vision, limited collision checks and an uncalibrated simulation drive-effort cap. It does not establish uncertain-pose robustness, deformable-object handling or hardware safety. confidence: 1 source, last-confirmed 2026-11-19 (archived capture reviewed; no live refresh). [captured source](../raw/2026-11-16-rss-build-a-robot-pick-and-place-simulation-with-simready-assets.md)

### Explicit relationships

Task validation depends-on both asset properties and controller behavior; Isaac Sim uses OpenUSD assets. See [[technical-art-community-and-talent-signals]].

### Decision and quality notes

Primary vendor walkthrough, not an independently reproduced task. Links labelled Robotiq 2F-140 point to 2F-85 asset paths while validation/example paths name 2F-140. Actual package identity is unresolved; neither gripper is assumed interchangeable. Source-specific claims remain provisional; related reports and derived outputs are not independent confirmation. Open question: Which pinned arm/gripper/can packages reconcile the 2F-140 versus 2F-85 links and verify profile checks, contact grasp, placement error and repeatability? See [[indexes/gaps]].
