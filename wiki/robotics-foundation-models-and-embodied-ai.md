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
