# Edge AI and AI Infrastructure 2026

## Decision-useful summary
Google's May 2026 infrastructure sources point in two complementary directions: push inference closer to users/devices with LiteRT/NPU support, and keep large-scale training/inference pipelines fed with faster cloud storage/TPU post-training tooling. A separate AI-industry signal from The Rundown suggests frontier-model compute scarcity is also reshaping partnerships: model labs may rent capacity from rivals' AI clusters when limits bite. For HoneyDrunk, the decision signal is architectural: on-device AI needs cross-silicon abstraction and benchmarking, while cloud model work needs I/O, checkpoint, post-training, and capacity bottlenecks treated as first-class system design. [sources: raw/2026-05-07-rss-google-developers-blog-building-real-world-on-device-ai-with-litert-an.md; raw/2026-05-08-rss-google-developers-blog-speeding-up-ai-bringing-google-colossus-to-pyto.md; raw/2026-05-08-rss-google-developers-blog-maxtext-expands-post-training-capabilities-intr.md; raw/2026-05-11-web-the-rundown-ai-anthropic-spacex-ai-become-unlikely-compute-partners.md]

## Claims
- LiteRT is described as a cross-platform production-ready framework for on-device AI with CPU, GPU, and NPU acceleration across mobile, desktop, and IoT, using a unified API to avoid vendor-specific NPU SDK integration. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-rss-google-developers-blog-building-real-world-on-device-ai-with-litert-an.md]
- Google reports production LiteRT/NPU use cases in Google Meet segmentation, Epic Games Live Link Face Android real-time MetaHuman animation, Argmax Pro SDK on-device speech recognition, and Google AI Edge Gallery benchmarking for select Gemma models. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-rss-google-developers-blog-building-real-world-on-device-ai-with-litert-an.md]
- Argmax's LiteRT/NPU speech-recognition case reports over 2x speedup moving from GPU to NPU across Google Tensor, MediaTek, and Qualcomm SoCs, plus battery/session benefits for live transcription; treat this as vendor/partner-reported. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-rss-google-developers-blog-building-real-world-on-device-ai-with-litert-an.md]
- Google AI Edge Portal offers benchmarking across 100+ popular mobile phones to help choose AOT vs JIT and accelerator configurations; latest NPU features were in private preview in the source. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-07-rss-google-developers-blog-building-real-world-on-device-ai-with-litert-an.md]
- Google Rapid Bucket integrates Rapid Storage/Colossus with PyTorch through gcsfs/fsspec, using bidirectional gRPC, direct paths, and zonal co-location for higher-throughput AI data loading and checkpointing. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-speeding-up-ai-bringing-google-colossus-to-pyto.md]
- The Rapid Bucket source reports 15+ TiB/s aggregate throughput, <1ms random read/append write latency, 20M+ QPS, 23% total training-time improvement on a benchmark, 4.8x read throughput, and 2.8x write throughput; validate independently before relying on these numbers. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-speeding-up-ai-bringing-google-colossus-to-pyto.md]
- MaxText now supports supervised fine-tuning and reinforcement learning on single-host TPUs such as v5p-8 and v6e-8, using JAX and Tunix with workflows intended to scale to multi-host setups later. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-maxtext-expands-post-training-capabilities-intr.md]
- MaxText single-host RL support includes GRPO and GSPO; GRPO reduces hardware footprint by removing a separate value model, while GSPO rewards sequence-level behavior and is positioned for reasoning benchmarks such as GSM8K. confidence: 1 source, last-confirmed 2026-05-08. [source: raw/2026-05-08-rss-google-developers-blog-maxtext-expands-post-training-capabilities-intr.md]
- The Rundown reports Anthropic renting SpaceX/xAI Colossus 1 compute, underscoring that compute supply can become a strategic bottleneck and cross-company dependency even among AI rivals. confidence: 1 newsletter source, last-confirmed 2026-05-11. [source: raw/2026-05-11-web-the-rundown-ai-anthropic-spacex-ai-become-unlikely-compute-partners.md]

## Typed entities
- framework: LiteRT
- framework/library: LiteRT-LM
- hardware: Neural Processing Unit (NPU)
- app/product: Google Meet
- app/product: Epic Games Live Link Face
- concept/entity: MetaHuman
- product: Argmax Pro SDK
- app/tool: Google AI Edge Gallery
- service: Google AI Edge Portal
- model family: Gemma
- storage/product: Google Rapid Bucket
- storage architecture: Google Colossus
- library/interface: fsspec
- library: gcsfs
- framework: PyTorch
- project/framework: MaxText
- library: JAX
- library: Tunix
- algorithm: GRPO
- algorithm: GSPO
- hardware: TPU v5p-8
- hardware: TPU v6e-8
- company/platform: xAI
- partner/company: SpaceX
- infrastructure/cluster: Colossus 1
- concept: frontier compute scarcity

## Explicit relationships
- LiteRT uses CPU/GPU/NPU backends to run on-device AI across mobile, desktop, and IoT.
- LiteRT abstracts vendor-specific NPU SDKs to improve portability.
- Google AI Edge Portal benchmarks help decide deployment configuration for LiteRT workloads.
- Rapid Bucket uses Colossus, gRPC bidirectional streaming, direct paths, and zonal co-location to reduce PyTorch storage bottlenecks.
- gcsfs/fsspec lets PyTorch ecosystem tools use Rapid Bucket without large code rewrites.
- MaxText uses JAX and Tunix for SFT/RL post-training on TPUs.
- Frontier model providers depend-on scarce external compute capacity when internal/hyperscaler supply is constrained.

## HoneyDrunk implications
- For mobile/interactive prototypes, on-device AI feasibility should be tested against thermals, battery, FPS, and target-device NPU support, not just model accuracy.
- If HoneyDrunk pursues local speech, vision, or facial-animation features, LiteRT/Gemma/AI Edge tooling is a relevant scouting path.
- For any serious training/fine-tuning workload, profile data-loading and checkpoint I/O early; storage architecture can dominate GPU/TPU utilization.
- MaxText single-host TPU post-training is relevant only if HoneyDrunk needs custom model refinement; otherwise keep it as infrastructure literacy, not an immediate project.
- Treat model-provider availability/limits as supply-chain risk; keep routing/provider abstractions where practical.

## Confidence and quality notes
- Quality posture: decision-usable for scouting; all quantitative performance claims are vendor/partner-authored and need workload-specific validation.
- Weak claims: production examples are persuasive but not transferable without target device and workload testing.
- Privacy filter: no private data or credentials copied.

## 2026-05-20 compile additions

### Claims
- Azure Blob Storage plus Run:AI Model Streamer can stream SafeTensors model weights through CPU memory into GPU memory for vLLM and SGLang, skipping the conventional object-storage-to-local-disk staging step. confidence: 1 vendor benchmark source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-azure-blog-eliminate-llm-cold-starts-load-models-up-to-6x-faster-with-.md]
- Azure's benchmark reports vLLM load-time improvements from about 4.3x for a 14.99 GiB Llama 3.1 8B model to about 6.1x for a 232.8 GiB Qwen model on an 8x H100 ND96isr_H100_v5 VM using same-region Premium Blob Storage; validate on HoneyDrunk workloads before relying on the numbers. confidence: 1 vendor benchmark source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-azure-blog-eliminate-llm-cold-starts-load-models-up-to-6x-faster-with-.md]
- Streaming large model weights can move cold starts from multi-minute windows into a single autoscaler polling cycle, reducing queue buildup, timeout/retry cascades, and over-provisioning during scale-out/rollouts. confidence: 1 vendor source, last-confirmed 2026-05-20. [source: raw/2026-05-20-rss-azure-blog-eliminate-llm-cold-starts-load-models-up-to-6x-faster-with-.md]

### Typed entities
- service: Azure Blob Storage
- product/library: Run:AI Model Streamer
- inference engine: vLLM
- inference engine: SGLang
- model-weight format: SafeTensors
- URI scheme: `az://`
- hardware: Standard_ND96isr_H100_v5
- hardware: NVIDIA H100 80 GB
- model: Meta-Llama-3.1-8B-Instruct
- model: GPT-OSS-120B
- model: Qwen3.5-122B-A10B
- concept: LLM cold start
- concept: autoscaler polling cycle

### Explicit relationships
- Run:AI Model Streamer uses Azure Blob Storage and `az://` URIs to stream model weights directly into GPU memory for vLLM/SGLang.
- LLM serving cold starts depend-on model-weight I/O path, not only GPU availability.
- Local-disk staging contradicts fast autoscaling for very large model replicas when the load window exceeds autoscaler cadence.

### HoneyDrunk implications
- If HoneyDrunk hosts large open-weight models on Azure, test model streaming early; cold-start I/O can dominate GPU utilization and perceived reliability.
- Require workload-specific validation: model size, region/storage tier, NIC saturation, concurrency settings, managed identity auth, and autoscaler cadence all affect the decision.
