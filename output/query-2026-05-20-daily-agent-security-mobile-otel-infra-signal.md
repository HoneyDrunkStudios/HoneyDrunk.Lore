# Daily agent security, mobile engine, OTel, and infrastructure signal — 2026-05-20

## Decision signal
- Coding-agent safety should move from prompt-level instructions to execution-layer controls: workspace isolation, scoped identity, blocked credential paths, network egress policy, audit logs, and hard approval gates. [wiki: [[ai-coding-agent-security]], [[ai-agent-harnesses]]]
- Azure Blob Storage + Run:AI Model Streamer is worth tracking for large open-weight serving on Azure because cold-start model-weight I/O can dominate autoscaling reliability. [wiki: [[edge-ai-and-ai-infrastructure-2026]]]
- Mobile engine selection got a stronger Unity-vs-Godot-vs-Unreal criteria source, but it is explicitly Unity-biased; HoneyDrunk still needs target-device prototype evidence. [wiki: [[unity-3d-and-realtime-vfx-patterns]], [[godot-2026-mobile-and-4-7-cycle]]]
- OTel legacy-environment guidance extends the privacy model: operational telemetry can be sensitive even when it is not ordinary PII. [wiki: [[opentelemetry-genai-observability-and-ecosystem]]]
- TLDR/Rundown extraction remains unfit for title-level claims where raw bodies contain sponsor blocks or site scaffolding. [wiki: [[browser-snapshot-source-quality]]]

## Durable facts crystallized
- Docker's source names six coding-agent risk classes: unrestricted filesystem access, excessive privilege inheritance, secrets leakage, prompt injection via ingested content, malicious skills/plugins, and autonomous action without human-in-the-loop. [source: raw/2026-05-20-rss-docker-blog-coding-agent-horror-stories-the-security-crisis-threatenin.md]
- Azure's source says Run:AI Model Streamer is integrated with vLLM and SGLang for `az://` model-weight streaming from Azure Blob Storage and requires SafeTensors weights. [source: raw/2026-05-20-rss-azure-blog-eliminate-llm-cold-starts-load-models-up-to-6x-faster-with-.md]
- OTel's legacy guidance prefers an external Collector bridge when source systems are hard to patch or modify. [source: raw/2026-05-20-rss-opentelemetry-blog-applying-opentelemetry-security-practices-in-legacy.md]
- Ocean View Games' mobile comparison recommends Unity for most commercial mobile projects, Godot for indie/solo 2D projects with lighter monetization needs, and Unreal for high-fidelity/PC-console-first projects with C++ depth. [source: raw/2026-05-20-rss-dev-to-unity-unity-vs-godot-vs-unreal-for-mobile-games-a-practical-com.md]

## Gaps
- Evaluate sandbox/microVM agent execution options for OpenClaw/Grid under Windows and HoneyDrunk workflow constraints.
- Benchmark Azure model streaming only if HoneyDrunk has a real Azure open-weight serving workload.
- Run a representative mobile-engine spike before turning engine-selection criteria into a default.
- Fix TLDR/Rundown extraction before using those sources for title-level claims.

## Confidence
Decision-usable for architecture direction and sourcing priorities. Vendor/biased performance and security claims need local/primary validation before procurement or platform commitments.
