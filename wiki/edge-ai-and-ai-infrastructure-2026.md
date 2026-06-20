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

## 2026-05-23 compile additions

### Claims
- CNBC/TechCrunch reporting says OpenAI launched or announced a Guaranteed Capacity offering for customers to reserve compute; the raw CNBC capture was mostly CSS/scaffolding, so no detailed terms were promoted. confidence: 1 noisy secondary capture, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-ai-openai-announces-new-guaranteed-capacity-offering-for-customer.md]
- TechCrunch reports OpenAI may be preparing a September IPO and may file confidential paperwork soon, with Goldman Sachs and Morgan Stanley involved; OpenAI did not comment in the captured article. confidence: 1 secondary source, last-confirmed 2026-05-23. [source: raw/2026-05-23-rss-tldr-ai-openai-reportedly-moves-toward-ipo-2-minute-read.md]
- OpenAI says an internal general-purpose reasoning model autonomously found a proof disproving a longstanding belief about the planar unit-distance problem, checked by external mathematicians; this is a frontier-research milestone claim, not a deployable product capability. confidence: 1 primary vendor/research source, last-confirmed 2026-05-23. [source: raw/2026-05-22-rss-tldr-ai-ai-solves-a-longstanding-geometry-conjecture-14-minute-read.md]

### Typed entities
- company: OpenAI
- offering: OpenAI Guaranteed Capacity
- event: OpenAI potential IPO
- bank: Goldman Sachs
- bank: Morgan Stanley
- problem: planar unit-distance problem
- person: Paul Erdős
- concept: AI-discovered mathematics proof
- concept: frontier compute reservation

### Explicit relationships
- OpenAI Guaranteed Capacity depends-on scarce frontier compute becoming a reserved enterprise resource.
- OpenAI IPO readiness depends-on corporate-structure/legal/finance constraints per secondary reporting.
- AI-discovered math proof strengthens evidence that frontier reasoning models can contribute to formal research when proofs are externally checkable.

### HoneyDrunk implications
- Watch guaranteed-capacity offerings as an enterprise pricing/availability pattern, not a near-term need unless HoneyDrunk has predictable high-volume model demand.
- Treat AI-math breakthroughs as model capability signal but keep application decisions grounded in local benchmark tasks.

## 2026-05-24 compile additions

### Claims
- Bloomberg reports that Anthropic agreed to pay SpaceX nearly $45B over three years for compute supporting Claude, with SpaceX disclosing an expected $1.25B/month through May 2029 and a 90-day termination option for either party; this strengthens the frontier-compute-scarcity claim with a primary business-reporting source. confidence: 1 source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-ai-anthropic-to-pay-spacex-nearly-45-billion-for-computing-deal-2.md]
- The raw Bloomberg URL contained an access-token query string; wiki citations intentionally cite only the immutable raw filename and not the tokenized URL. confidence: 1 source, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-ai-anthropic-to-pay-spacex-nearly-45-billion-for-computing-deal-2.md]

### Typed entities
- company: Anthropic
- company: SpaceX
- product/model family: Claude
- concept: frontier compute supply chain
- contract term: 90-day termination option
- privacy artifact: tokenized article URL

### Explicit relationships
- Anthropic depends-on external SpaceX compute capacity to support Claude scale under the reported agreement.
- Frontier-model availability depends-on long-horizon compute contracts, not just model/runtime engineering.
- Privacy filtering supersedes raw URL copying when source links contain access-token query strings.

### HoneyDrunk implications
- Keep model-provider abstraction and rate-limit/fallback planning: frontier compute can become a contractual supply-chain dependency.
- Do not copy tokenized article URLs from raw into wiki, issue trackers, or public notes; cite raw files or clean canonical URLs instead.

### Inference routing note
- DigitalOcean describes its Inference Router architecture as a model-serving routing layer; the captured raw was too scaffold-heavy for detailed architecture extraction, but the title-level/TLDR summary is enough to track inference routing as an infrastructure pattern needing cleaner sourcing before design reuse. confidence: 1 noisy capture, last-confirmed 2026-05-24. [source: raw/2026-05-24-rss-tldr-devops-how-we-built-digitalocean-inference-router-12-minute-read.md]

Typed entities added: company: DigitalOcean; concept: inference router; concept: model-serving routing layer.

Relationships added: inference-routing decisions depend-on clean article/body extraction before architecture details can be reused.

## 2026-05-26 compile additions

### Claims
- Contrary Research reports Anthropic revenue/profitability projections and improved compute-cost ratio; if accurate, this reinforces frontier compute economics as a board-level/platform constraint rather than a back-office infra detail. confidence: 1 business-newsletter source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-ai-anthropic-s-march-to-profitability-3-minute-read.md]
- Contrary's roundup also reports Blackstone committing $5B equity to a Google TPU compute-as-a-service joint venture targeting 500 MW capacity in 2027; this is a secondary market signal that AI compute is moving into specialized infrastructure finance. confidence: 1 business-newsletter source, last-confirmed 2026-05-26. [source: raw/2026-05-26-rss-tldr-ai-anthropic-s-march-to-profitability-3-minute-read.md]

### Typed entities
- company: Blackstone
- company: Google
- infrastructure: TPU compute-as-a-service joint venture
- capacity target: 500 MW
- concept: AI infrastructure finance
- concept: model-lab compute unit economics

### Explicit relationships
- Frontier-model profitability depends-on compute cost per revenue dollar and access to scarce capacity.
- AI compute capacity increasingly depends-on capital-intensive infrastructure partnerships outside ordinary cloud procurement.

### HoneyDrunk implications
- Keep cost telemetry, provider fallback, and workload portability in agent/model infrastructure; frontier compute availability and economics can shift quickly.

### Quality notes
- Business/market claims from Contrary were not treated as canonical financial facts; use them as watchlist signals until primary filings or stronger reporting exist.

## 2026-06-01 compile additions

### Claims
- Callstack's Apex source describes a React Native-specialized coding model based on Gemma 4 and trained with SFT plus GRPO on curated React Native ecosystem data; it is positioned as a focused specialist, not a replacement for frontier coding models. confidence: 1 vendor/source-author source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-introducing-apex-a-fast-specialized-model-for-react-native.md; page: [[mobile-ai-and-react-native-2026]]]
- Apex reinforces a domain-specialist model pattern: a smaller or specialized model can improve cost/performance for narrow framework work when general coding benchmarks fail to capture framework conventions, native-module constraints, and cross-platform details. confidence: 1 source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-introducing-apex-a-fast-specialized-model-for-react-native.md; page: [[mobile-ai-and-react-native-2026]]]
- DigitalOcean's OpenCode integration makes inference routing usable from a coding harness through OpenAI-compatible API calls that target `router:<name>`, avoiding manual per-model configuration churn in `opencode.json`. confidence: 1 vendor source, last-confirmed 2026-06-01. [source: raw/2026-06-01-web-opencode-now-supports-digitalocean-inference-router-for-intelligent-mo.md]

### Typed entities
- model: Apex
- base model: Gemma 4
- framework: React Native
- training method: SFT
- training method: GRPO
- product: DigitalOcean Inference Router
- tool: OpenCode
- config file: `opencode.json`

### Explicit relationships
- Domain-specialized models complement frontier generalist models when framework-specific conventions dominate answer quality.
- Inference routing uses latency, cost, and quality tradeoffs to choose models per request.
- OpenCode depends-on provider/model configuration; router integration reduces static config churn.

### HoneyDrunk implications
- For any React Native/mobile agent work, benchmark specialized models on HoneyDrunk tasks before assuming frontier models are always the best cost/quality choice.
- Treat inference routers as operational infrastructure: log routing decisions, model costs, fallback behavior, and quality regressions.

## 2026-06-02 compile additions

### Claims
- Slack AI moved from SageMaker-hosted model endpoints to Amazon Bedrock provisioned throughput, then hybrid Bedrock on-demand routing, and finally a multi-cloud architecture including GCP Vertex AI by early 2026. confidence: 1 Slack Engineering source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-slack-engineering-slack-ai-the-path-to-multi-cloud.md]
- Slack's Bedrock migration used legal/security/FedRAMP signoff, load tests mapping SageMaker capacity to Model Units, A/B/evaluation parity checks, feature-flag rollout, and instant rollback; Slack reports zero customer-facing incidents during the migration. confidence: 1 Slack Engineering source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-slack-engineering-slack-ai-the-path-to-multi-cloud.md]
- Slack's hybrid strategy kept high-volume latency-sensitive workloads on provisioned throughput, moved bursty/asynchronous workloads to on-demand, and added spillover plus model hierarchy fallback when primary endpoints degraded. confidence: 1 Slack Engineering source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-slack-engineering-slack-ai-the-path-to-multi-cloud.md]
- Slack's multi-cloud routing layer normalizes provider APIs/error codes, uses quality/latency/health telemetry for model selection, supports A/B experiments, and trips circuit breakers on signals such as elevated time-to-first-token, 5xx spikes, throttling, p90 latency, or negative feedback trends. confidence: 1 Slack Engineering source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-slack-engineering-slack-ai-the-path-to-multi-cloud.md]
- Slack reports multi-cloud model-to-feature optimization produced approximately 10% quality improvement for complex reasoning tasks and 67% latency reduction for high-velocity low-token workloads; treat as Slack-specific production telemetry. confidence: 1 Slack Engineering source, last-confirmed 2026-06-02. [source: raw/2026-06-02-rss-slack-engineering-slack-ai-the-path-to-multi-cloud.md]

### Typed entities
- company/product: Slack AI
- cloud service: AWS SageMaker
- cloud service: Amazon Bedrock
- cloud service: GCP Vertex AI
- capacity unit: Bedrock Model Unit / MU
- capacity type: Provisioned Throughput
- capacity type: On Demand
- pattern: spillover routing
- pattern: model hierarchy fallback
- pattern: intelligent routing layer
- control: circuit breaker
- metric: time to first token / TTFT

### Explicit relationships
- Enterprise AI reliability depends-on provider abstraction, model fallback, load testing, and cross-functional compliance approval.
- Provisioned throughput complements on-demand capacity: PT handles predictable latency-sensitive traffic, while OD handles burst and model agility.
- Multi-cloud routing uses normalized provider signals to decouple product features from one provider's outage, capacity, or model catalog.
- Circuit breakers treat slow LLM endpoints as failures even when the endpoint is technically up.

### HoneyDrunk implications
- For OpenClaw/model routing, design provider abstraction, health metrics, fallback models, and cost attribution before multi-provider complexity grows.
- Treat TTFT, p90 latency, throttling, 5xxs, cost per feature, and quality feedback as routing inputs, not only uptime.
- Do not copy Slack's multi-cloud architecture prematurely; use it as a maturity map for when one provider becomes a reliability or model-quality bottleneck.

## 2026-06-03 compile additions

### Claims
- DigitalOcean Serverless Inference is a managed, API-first inference platform with 30+ foundation models across text, code, vision, image, video, speech, and embeddings, using a single key/base URL and pay-per-token pricing. confidence: 1 vendor source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-digitalocean-digitalocean-serverless-inference-a-deep-dive.md]
- DigitalOcean describes a production path of Cloudflare edge proxying, load balancer policy enforcement, Traefik on DOKS, Intelligent Inference API, Model Executor Service provider translation, Ray/vLLM backends for open models, provider APIs for OpenAI/Anthropic, and Kafka usage telemetry. confidence: 1 vendor source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-digitalocean-digitalocean-serverless-inference-a-deep-dive.md]
- The DigitalOcean Inference Router selects models by task using cost-efficiency, speed, manual ranking, or provider-defined optimal policies, and reports selected model/route metadata; this strengthens inference routing as an operational architecture pattern. confidence: 1 vendor source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-digitalocean-digitalocean-serverless-inference-a-deep-dive.md]
- Holo3.1 releases computer-use agent models from 0.8B to 35B-A3B, with FP8, NVFP4, and Q4 GGUF quantized checkpoints aimed at local, private, and cross-environment GUI automation across desktop, browser, and mobile. confidence: 1 Hugging Face/H Company source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-hugging-face-blog-holo3-1-fast-local-computer-use-agents.md]
- Holo3.1 reports AndroidWorld gains, cross-harness improvements, and local speedups from quantization/harness optimization; treat all benchmark and throughput numbers as vendor-reported until reproduced on HoneyDrunk tasks/hardware. confidence: 1 vendor/model-release source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-hugging-face-blog-holo3-1-fast-local-computer-use-agents.md]
- Google AI Edge Gallery added persistent chat history using LiteRT-LM fast prefill, custom system prompt editing, local notifications, and MCP support, showing mobile on-device agents moving from demos toward persistent/local routines. confidence: 1 Google source, last-confirmed 2026-06-03. [source: raw/2026-06-03-rss-google-developers-blog-a-smarter-google-ai-edge-gallery-mcp-integratio.md]

### Typed entities
- product: DigitalOcean Serverless Inference
- component: Intelligent Inference API
- component: Model Executor Service
- framework/runtime: Ray
- inference engine: vLLM
- telemetry backbone: Kafka
- feature: prompt caching
- feature: model reasoning traces
- feature: Inference Router
- model family: Holo3.1
- base family: Qwen
- quantization: FP8
- quantization: NVFP4
- format: Q4 GGUF
- benchmark: AndroidWorld
- benchmark: OSWorld
- app: Google AI Edge Gallery
- library/runtime: LiteRT-LM

### Explicit relationships
- Serverless inference separates model consumption from GPU lifecycle management, but stateless requests depend-on callers providing full context or using supported prompt-caching features.
- Provider translation layers normalize API contracts and error/stream formats across self-hosted and commercial models.
- Inference routers depend-on live latency/cost/quality telemetry to avoid hardcoded model/provider choices.
- Local computer-use agents depend-on model size, quantization, harness optimization, and target GUI environment; benchmark transfer between web, desktop, and mobile is not guaranteed.
- On-device agents use fast prefill and persistent history to restore context locally, but local persistence also creates device-side privacy and retention responsibilities.

### HoneyDrunk implications
- Treat DigitalOcean Serverless Inference as a candidate provider abstraction layer only after testing routing decisions, provider failure behavior, VPC-bound keys, prompt cache economics, and MCP/web-search policy.
- Benchmark Holo3.1 or similar local computer-use models on actual HoneyDrunk UI automation tasks before assuming OSWorld/AndroidWorld gains transfer.
- For mobile/on-device agents, evaluate not only model speed but session retention, notification permissions, system prompt editability, local data storage, and MCP server trust.

### Quality notes
- All quantitative performance and pricing claims in the June 3 provider/model sources are vendor-authored snapshots; use them for scouting and local eval design, not as procurement-grade evidence.

## 2026-06-04 compile additions

### Claims
- DigitalOcean's prefix-aware routing source describes redundant prefill as a major inference cost: shared prompts, tool definitions, RAG documents, and conversation context are repeatedly prefetched unless KV cache reuse and routing are coordinated. confidence: 1 vendor infrastructure source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-digitalocean-the-inference-tax-how-prefix-aware-routing-eliminates-the.md]
- vLLM prefix caching stores KV blocks in a GPU memory pool and uses block hashes to find the longest cached prefix for later requests; only uncached suffix tokens need prefill on cache hits. confidence: 1 vendor infrastructure source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-digitalocean-the-inference-tax-how-prefix-aware-routing-eliminates-the.md]
- DigitalOcean's Inference Gateway consumes KV cache events from vLLM instances, builds per-pod prefix state, and routes requests using cache affinity plus KV utilization instead of round-robin alone. confidence: 1 vendor infrastructure source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-digitalocean-the-inference-tax-how-prefix-aware-routing-eliminates-the.md]
- DigitalOcean reports cache-hit improvement from roughly 25% under round-robin to 75%+ on shared-prefix workloads, with possible up to 4x effective compute-cost reduction for suitable multi-turn/RAG/agent traffic; treat as vendor-reported and workload-specific. confidence: 1 vendor infrastructure source, last-confirmed 2026-06-04. [source: raw/2026-06-04-web-digitalocean-the-inference-tax-how-prefix-aware-routing-eliminates-the.md]

### Typed entities
- technique: prefix-aware routing
- technique: prefix caching
- concept: redundant prefill
- artifact: KV cache
- inference engine: vLLM
- component: DigitalOcean Inference Gateway
- component: Endpoint Picker / EPP
- component: Envoy external processing / ext_proc
- hardware: AMD Instinct MI325X
- hardware: NVIDIA H200
- hardware: NVIDIA Blackwell / B200

### Explicit relationships
- Prefix-aware routing uses KV cache locality to choose the worker most likely to reuse shared prompt state.
- KV cache event streams complement load metrics because cache locality and utilization both affect routing quality.
- Prompt caching depends-on tenant isolation, cache salt/adapters, eviction policy, hardware memory, and engine compatibility.
- Agent traffic amplifies prefill waste because tool schemas, system prompts, and documents repeat across turns.

### HoneyDrunk implications
- If HoneyDrunk runs high-volume agent/RAG inference, log prefix length, cache hit rate, TTFT, selected worker/model, tenant isolation controls, and cached-token pricing before making provider decisions.
- Benchmark prefix-aware routing only on workloads with meaningful shared prefixes; it may not help short independent prompts.
- Treat vendor 4x cost-reduction claims as an eval hypothesis, not a procurement conclusion.

## 2026-06-05 compile additions

### Claims
- Foundry IQ Serverless Developer tier is a managed retrieval infrastructure preview with scale-to-zero economics and per-minute Compute Unit metering; Microsoft says billing will not start before late 2026 and details will be provided at least 30 days ahead. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-foundry-iq-build-smarter-agents-faster-with-unified-knowledge-and-server.md]
- Foundry IQ retrieval updates claim up to 20% answer-quality benchmark improvements and up to 54% recall improvement over single-shot RAG through batched iterative retrieval, semantic ranking, and server-side token caching; treat as vendor-reported retrieval benchmark evidence. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-foundry-iq-build-smarter-agents-faster-with-unified-knowledge-and-server.md]
- Microsoft Fabric Data Warehouse announced GPU acceleration in early access preview, with Microsoft reporting up to 7x faster performance versus three comparable external vendors for reporting/application workloads at 64-user concurrency in internal May 2026 benchmarking. confidence: 1 Microsoft Fabric source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-mic.md]
- Azure HorizonDB's public preview signals a PostgreSQL-compatible AI-application data plane that combines transactional PostgreSQL compatibility with vector search, AI model management, and Foundry/Fabric connectivity. confidence: 1 Microsoft source, last-confirmed 2026-06-05. [source: raw/2026-06-05-web-microsoft-build-2026-building-agentic-apps-with-microsoft-fabric-and-mic.md]

### Typed entities
- product: Foundry IQ Serverless
- metric: Compute Unit / CU
- technique: agentic retrieval
- technique: semantic ranking
- technique: server-side token caching
- service: Fabric Data Warehouse
- hardware/technique: GPU acceleration
- database: Azure HorizonDB
- concept: AI application data plane

### Explicit relationships
- Serverless retrieval infrastructure complements agent/RAG workloads when usage is bursty and idle capacity cost matters.
- Agentic retrieval uses multiple query/retrieval steps and semantic ranking to improve answer coverage over single-shot RAG.
- GPU-accelerated analytics complements agentic business applications by reducing latency for many simultaneous data questions.
- HorizonDB complements vector/RAG stores when applications need PostgreSQL-compatible transactions plus AI search.

### HoneyDrunk implications
- Treat Foundry IQ Serverless as a retrieval-cost experiment, not a default; benchmark Lore-like and app-like queries against flat-file/local retrieval before adopting.
- If HoneyDrunk uses Fabric or HorizonDB, capture query latency, concurrency, cost, vector quality, data egress, and backup/failover behavior under representative agent workloads.

### Quality notes
- All June 5 infrastructure performance claims here are vendor-reported. Use them to design local evals, not as procurement-grade conclusions.

## 2026-06-07 compile additions

### Claims
- Foundry Managed Compute is a Microsoft Foundry preview for serving open-source and custom models on Foundry-managed dedicated GPU capacity, with templates that pin runtime, accelerator family/count, context length, quantization, and model-specific tuning. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-announcing-foundry-managed-compute-run-open-models-in-microsoft-foundr.md]
- Foundry Managed Compute supports a unified Foundry endpoint/SDK surface, Azure Monitor metrics for request/latency/token usage, private networking, Entra/RBAC, Azure Policy, billing tags, and curated runtime/container patching for supported runtimes. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-announcing-foundry-managed-compute-run-open-models-in-microsoft-foundr.md]
- Managed Compute uses hourly accelerator-family billing for model instances, starting with A100 and H100 Global Managed Compute preview, with Data Zone scope, MI300X, BYO weights, LoRA adapters, and IP-protected marketplace models on the roadmap. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-07. [source: raw/2026-06-07-web-announcing-foundry-managed-compute-run-open-models-in-microsoft-foundr.md]

### Typed entities
- service: Foundry Managed Compute
- deployment template: Foundry managed compute deployment template
- accelerator family: A100 80GB
- accelerator family: H100 80GB
- accelerator family: MI300X 192GB
- inference runtime: vLLM
- model catalog: Hugging Face Collection in Foundry Model Catalog
- scope: Global Managed Compute
- scope: Data Zone Managed Compute

### Explicit relationships
- Foundry Managed Compute complements pay-per-token and provisioned throughput by adding managed open/custom model hosting under the same Foundry resource.
- Deployment templates supersede manual GPU VM/runtime sizing for supported catalog models.
- Cache-aware routing and session affinity complement open-model serving when agent/RAG traffic has repeated prefixes or multi-turn context.
- Managed runtime patching reduces DIY container/CVE burden but depends-on supported runtimes and provider-controlled update behavior.

### HoneyDrunk implications
- Benchmark Managed Compute only if HoneyDrunk has open-weight/custom-model serving needs; otherwise it remains infrastructure literacy.
- Compare against direct GPU VMs, local inference, and other managed providers using the same model, context length, expected concurrency, private-networking, identity, and observability requirements.

### Quality notes
- Microsoft source is a preview announcement with vendor-reported economics and roadmap. Treat as scouting evidence until pricing, quotas, and region availability are verified.

## 2026-06-09 compile additions

### Claims
- Microsoft Foundry's model-operations guidance frames model selection as a continuous operating discipline across capability, safety, latency, and cost rather than a one-time leaderboard choice. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-a-developer-s-guide-to-managing-models-cost-and-quality-in-microsoft-f.md]
- Foundry Model Router is described as routing each request to an appropriate model based on workload characteristics, cost targets, and latency requirements; this reinforces model routing as production infrastructure. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-a-developer-s-guide-to-managing-models-cost-and-quality-in-microsoft-f.md]
- Fireworks AI on Microsoft Foundry is now generally available, providing open-model inference through a single Azure endpoint with enterprise SLAs, provisioned throughput Data Zone support, SOC 2 readiness, access controls, and audit logging under Foundry. confidence: 2 Microsoft Foundry sources, last-confirmed 2026-06-09. [sources: raw/2026-06-09-web-a-developer-s-guide-to-managing-models-cost-and-quality-in-microsoft-f.md; raw/2026-06-09-web-what-s-new-in-microsoft-foundry-build-edition-microsoft-foundry-blog.md]
- Microsoft Foundry Build recap expands model/compute choices with MAI-Thinking-1, MAI-Image-2.5, MAI-Transcribe-2, MAI-Voice-2, Managed Compute, fine-tuning, and Frontier Tuning; all are platform signals requiring local cost/quality validation. confidence: 1 Microsoft Foundry source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-what-s-new-in-microsoft-foundry-build-edition-microsoft-foundry-blog.md]
- Datadog argues that warehouse-native experimentation and OpenFeature protect portability while still allowing unified feature-flag/product-observability decisions, making data-model ownership part of AI/release infrastructure. confidence: 1 Datadog source, last-confirmed 2026-06-09. [source: raw/2026-06-09-web-how-a-unified-data-model-improves-feature-flag-rollout-decisions-datad.md]

### Typed entities
- platform: Microsoft Foundry Models
- feature: Model Router
- provider: Fireworks AI on Foundry
- model: MAI-Thinking-1
- model: MAI-Image-2.5
- model: MAI-Transcribe-2
- model: MAI-Voice-2
- service: Foundry Managed Compute
- tuning method: Frontier Tuning
- standard: OpenFeature SDK
- concept: warehouse-native experimentation

### Explicit relationships
- Model routing depends-on workload-specific quality, safety, latency, cost, and throughput criteria.
- Fireworks AI on Foundry complements managed open-model inference by bringing external/open models under Azure endpoint, audit, and SLA controls.
- Fine-tuning, compression, distillation, caching, batching, quota management, and provisioned throughput complement routing as cost/performance levers.
- OpenFeature and warehouse-native experimentation reduce release-platform lock-in while preserving correlated decision data.

### HoneyDrunk implications
- Treat every model/provider switch as a dependency upgrade: baseline evals, latency/cost comparison, staged rollout, monitoring, and rollback.
- For OpenClaw routing, profile by task type before optimizing globally; extraction/routing, coding, RAG, long-context review, and image/voice work have different cost-quality tradeoffs.
- If adopting feature-flag or experimentation tooling, require OpenFeature/provider portability and warehouse/source-data ownership where practical.

### Quality notes
- Foundry and Datadog claims are vendor-authored. Use them to design local routing/retrieval/release evals, not as default platform choices.

## 2026-06-10 compile additions: North Mini Code, HF Jobs, and Foundry routing

### Source-backed claims
- North Mini Code is a 30B sparse MoE coding model with 3B active parameters, Apache 2.0 weights on Hugging Face, and availability through OpenCode, Cohere API, and BF16/FP8 model files. Source: `raw/2026-06-10-web-hugging-face-introducing-north-mini-code-coheres-first-model-for-developers.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Hugging Face Jobs can run CI workloads on selectable CPU and GPU hardware while GitHub Actions remains the orchestrator through an ephemeral self-hosted runner bridge. Source: `raw/2026-06-10-web-hugging-face-migrating-your-github-ci-to-hugging-face-jobs.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft Foundry gateway guidance treats model access as infrastructure needing routing, failover, throttling, auth, telemetry, and policy controls; direct model clients must otherwise implement these controls individually. Source: `raw/2026-06-10-web-microsoft-learn-access-foundry-models-and-other-language-models-through-a-gateway-azure.md`. confidence: 1 source, last-confirmed 2026-06-10.
- Microsoft's Foundry baseline distinguishes provisioned deployments, which target predictable latency and reserved capacity, from consumption deployments, which are best-effort and subject to noisy-neighbor behavior. Source: `raw/2026-06-10-web-microsoft-learn-baseline-microsoft-foundry-chat-reference-architecture-azure-architectur.md`. confidence: 1 source, last-confirmed 2026-06-10.

### Typed entities
- project: North Mini Code
- project: Hugging Face Jobs
- project: Microsoft Foundry
- concept: sparse MoE
- concept: ephemeral self-hosted runner
- concept: provisioned model deployment
- decision: HoneyDrunk model/CI infrastructure routing

### Explicit relationships
- North Mini Code uses sparse MoE architecture to reduce active-parameter compute per token.
- Hugging Face Jobs depends-on external orchestration and tokens when used as GitHub Actions runner infrastructure.
- Foundry provisioned capacity mitigates latency variance at higher commitment cost.
- Foundry gateway routing mitigates direct-client duplication of resilience and policy controls.

### HoneyDrunk implications
- Compare North Mini Code against local and hosted coding models on actual repo tasks before adopting it as an open-model default.
- Evaluate HF Jobs only for suites where GPU access or runner speed materially changes developer throughput.
- Treat Foundry gateway/provisioned deployments as an enterprise-grade option, not a default for lightweight Lore/OpenClaw workflows.

### Quality notes
- Infrastructure claims are vendor-authored and cost-sensitive. Recheck current pricing, quota, and regional availability before architectural decisions.

## 2026-06-12 compile additions: Azure Container Apps Sandboxes and DiffusionGemma infrastructure

### Source-backed claims
- Azure Container Apps Sandboxes are in public preview as `Microsoft.App/SandboxGroups`, offering per-sandbox hardware-isolated microVMs, sub-second startup, OCI disk images, snapshot-based suspend/resume, lifecycle policies, egress controls, volumes, secrets, managed identity, and portal/CLI/SDK management. Source: `raw/2026-06-12-web-microsoft-techcommunity-introducing-azure-container-apps-sandboxes-secure-infr.md`. confidence: 1 Microsoft source, last-confirmed 2026-06-12.
- Microsoft says ACA Sandboxes are the infrastructure used by Cloud sandboxes in GitHub Copilot, Foundry Hosted Agents, and ACA Express, and are the successor direction for Azure Container Apps Dynamic Sessions for new isolated ephemeral compute work. Source: `raw/2026-06-12-web-microsoft-techcommunity-introducing-azure-container-apps-sandboxes-secure-infr.md`. confidence: 1 Microsoft source, last-confirmed 2026-06-12.
- ACA Sandboxes support deny-by-default network egress policy with host and CIDR rules, managed volumes backed by Blob or Azure Disk, scoped group secrets, system/user-assigned managed identity, and managed MCP connectors/triggers through Connector Namespace. Source: `raw/2026-06-12-web-microsoft-techcommunity-introducing-azure-container-apps-sandboxes-secure-infr.md`. confidence: 1 Microsoft source, last-confirmed 2026-06-12.
- DiffusionGemma shifts local text generation pressure from memory bandwidth toward compute by denoising a 256-token canvas in parallel, with Google reporting high token throughput on RTX 5090 and H100-class GPUs; treat this as vendor performance evidence. Source: `raw/2026-06-12-web-google-developers-blog-diffusiongemma-the-developer-guide-google-developers-bl.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-12.

### Typed entities
- platform: Azure Container Apps Sandboxes
- Azure resource: `Microsoft.App/SandboxGroups`
- isolation type: hardware-isolated microVM
- feature: snapshot suspend/resume
- feature: network egress policy
- storage: Managed Azure Blob volume
- storage: Managed Data Disk volume
- identity: managed identity
- platform: Connector Namespace
- model: DiffusionGemma
- hardware: NVIDIA RTX 5090
- hardware: NVIDIA H100

### Explicit relationships
- ACA Sandboxes supersede Dynamic Sessions as Microsoft's new-work target for isolated ephemeral compute, while Dynamic Sessions remain supported.
- Snapshot suspend/resume enables stateful scale-to-zero agent compute, but snapshot storage and lifecycle policies become operational controls.
- Egress policy and managed identity make sandbox networking/credential boundaries platform concerns rather than prompt instructions.
- DiffusionGemma uses compute-heavy parallel denoising to reduce autoregressive memory-bandwidth bottlenecks for suitable GPU workloads.

### HoneyDrunk implications
- Evaluate ACA Sandboxes as a candidate for cloud-side OpenClaw/Honeyclaw code execution only after testing Windows/dev ergonomics, egress logs, identity boundaries, cost, lifecycle cleanup, and local fallback.
- Treat managed MCP connectors attached to sandboxes as high-capability tools requiring profile governance and audit.
- If local open-model serving becomes relevant, benchmark DiffusionGemma against autoregressive coding/chat models on HoneyDrunk tasks instead of relying on generic token-throughput claims.

### Quality notes
- Microsoft and Google sources are vendor-authored preview/developer materials. Feature existence is useful; costs, limits, quotas, and performance require current tenant/hardware validation.

## 2026-06-14 compile additions: inference-aware routing, static embeddings, and agent compute surfaces

### Source-backed claims
- Datadog describes the Kubernetes Gateway API Inference Extension as a routing layer that chooses LLM-serving backends using model-serving state such as KV cache locality, LoRA adapter availability, queue length, health, and flow-control priority rather than generic round-robin HTTP routing. Source: `raw/2026-06-14-rss-datadog-monitor-llm-routing-with-the-kubernetes-inference-extension-da.md`. confidence: 1 vendor observability source, last-confirmed 2026-06-14.
- Inference Extension flow control can centrally queue, dispatch, or shed requests based on capacity, priority, and fairness; this enables priority tiers and scale-to-zero patterns for noninteractive workloads while keeping real-time workloads sensitive to cold-start latency. Source: `raw/2026-06-14-rss-datadog-monitor-llm-routing-with-the-kubernetes-inference-extension-da.md`. confidence: 1 source, last-confirmed 2026-06-14.
- Datadog recommends correlating gateway, EPP, vLLM, GPU, and Kubernetes signals to distinguish routing misconfiguration from real capacity limits; useful metrics include TTFT, KV cache hit/utilization, per-pod queue depth, swapped requests, shedding events, pod restarts, OOMKills, GPU memory, and GPU utilization. Source: `raw/2026-06-14-rss-datadog-monitor-llm-routing-with-the-kubernetes-inference-extension-da.md`. confidence: 1 source, last-confirmed 2026-06-14.
- Stable Static Embedding (SSE) models are described as small static embedding models using token lookup, mean pooling, Separable Dynamic Tanh, and Matryoshka truncation to trade retrieval quality for CPU speed and vector storage footprint. Source: `raw/2026-06-14-web-hugging-face-blog-sse-in-practice-fast-static-embeddings-you-can-train.md`. confidence: 1 community technical source, last-confirmed 2026-06-14.
- Fast-Embedding-MCP-SSE wraps SSE v2 behind an OpenAI-compatible embeddings API, stateless and in-memory semantic search endpoints, and MCP tools for local agent retrieval without a separate vector database. Source: `raw/2026-06-14-web-hugging-face-blog-sse-in-practice-fast-static-embeddings-you-can-train.md`. confidence: 1 source, last-confirmed 2026-06-14.
- Google Colab CLI makes Colab GPU runtimes accessible through terminal commands for provisioning, package install, remote execution, artifact download, notebook logs, and cleanup, making it an agent-consumable compute surface. Source: `raw/2026-06-14-web-google-developers-blog-introducing-the-google-colab-cli-google-develop.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-14.

### Typed entities
- project/spec: Kubernetes Gateway API Inference Extension
- resource: InferencePool
- resource: InferenceObjective
- component: Endpoint Picker / EPP
- component: Body-Based Router / BBR
- filter: Envoy ext_proc
- serving engine: vLLM
- serving engine: NVIDIA Triton Inference Server
- metric: Time to First Token / TTFT
- model family/toolkit: Stable Static Embedding / SSE
- technique: Separable Dynamic Tanh / Separable DyT
- technique: Matryoshka truncation / MRL
- API: OpenAI-compatible embeddings API
- project: Fast-Embedding-MCP-SSE
- CLI: Google Colab CLI

### Explicit relationships
- Inference-aware routing uses serving-state telemetry to select model backends that can respond with lower latency or less redundant computation.
- LoRA adapter-aware routing depends-on adapter residency in GPU memory; static routing causes cold-start penalties when adapters churn.
- Prefix-aware routing depends-on consistent session/context identifiers and fresh KV cache telemetry.
- Flow control complements backend-local queues by centralizing priority, fairness, shedding, and scale-to-zero behavior.
- Static embeddings complement transformer encoders when CPU throughput, local privacy, and small vector footprints matter more than maximum semantic quality.
- MCP retrieval tools can expose local embedding/search capability to agents, but they inherit MCP tool-governance requirements.
- Colab CLI complements local agent workflows by offloading heavy compute without requiring the agent to provision cloud infrastructure directly.

### HoneyDrunk implications
- If HoneyDrunk serves open-weight LLMs, log routing distribution, TTFT, KV cache hit rate, queue depth, adapter churn, GPU memory, and shedding outcomes before tuning routers.
- For background inference, test central queue and scale-to-zero separately from interactive serving; cold model loads can be acceptable for batch jobs and unacceptable for chat.
- Evaluate SSE-style local embeddings for Lore indexes or agent scratch retrieval only against HoneyDrunk queries, with vector dimension, recall, latency, and memory footprint recorded.
- Treat Colab CLI as a convenient experiment runner, not durable production compute; require artifact capture, job cleanup, and budget guardrails.

### Quality notes
- Datadog and Google are vendor-authored. SSE is a community article with benchmark claims that should be reproduced locally before retrieval decisions.

## 2026-06-15 compile additions: local multimodal agents, persistent execution, and agent-native data runtimes

### Source-backed claims
- Google released Gemma 4 12B as a dense multimodal model with a unified encoder-free decoder-only architecture intended to reduce latency and fragmented memory footprints compared with separate vision/audio encoders. Source: `raw/2026-06-15-web-google-developers-blog-gemma-4-12b-the-developer-guide.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-15.
- Google positions Gemma 4 12B for local/offline multimodal agent workflows including ASR, diarization, video understanding, coding, and agentic reasoning, with examples using llama.cpp and OpenCode. Source: `raw/2026-06-15-web-google-developers-blog-gemma-4-12b-the-developer-guide.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-15.
- Google says LiteRT-LM can serve Gemma 4 12B through a local OpenAI-compatible API server using `litert-lm serve`, with stateless prefix caching intended to reduce repeated prefill latency. Source: `raw/2026-06-15-web-google-developers-blog-gemma-4-12b-the-developer-guide.md`. confidence: 1 Google Developers source, last-confirmed 2026-06-15.
- OpenAI's planned Ona acquisition reinforces persistent cloud execution as agent infrastructure: agents need secure environments with tools, systems, context, scoped credentials, and logs over hours or days. Source: `raw/2026-06-15-web-openai-openai-to-acquire-ona.md`; page: [[openai-frontier-models-and-codex-2026]]. confidence: 1 official OpenAI source, last-confirmed 2026-06-15.
- MotherDuck Flights runs agent-created Python ingest jobs against MotherDuck/DuckDB infrastructure and exposes MCP, SQL, and UI control paths. Source: `raw/2026-06-15-web-motherduck-introducing-flights-agent-native-ingest-in-motherduck.md`; page: [[mcp-tool-governance-and-app-surfaces]]. confidence: 1 vendor product source, last-confirmed 2026-06-15.

### Typed entities
- model: Gemma 4 12B
- framework/runtime: LiteRT-LM
- command: `litert-lm serve`
- project: llama.cpp
- tool: OpenCode
- product: Google AI Edge Gallery
- company: Ona
- product: MotherDuck Flights
- concept: encoder-free multimodal architecture
- concept: OpenAI-compatible local API server

### Explicit relationships
- Gemma 4 12B uses a unified decoder-only architecture to reduce dependency on separate modality encoders.
- LiteRT-LM local serving complements agent harnesses by presenting local multimodal models behind an OpenAI-compatible API.
- Persistent agent execution depends-on durable compute environments, credential scoping, and logs, whether hosted by OpenAI/Ona-style infrastructure or self-hosted.
- Agent-native ingest runtimes complement data platforms when agents need to create scheduled code workflows without handling raw secrets.

### HoneyDrunk implications
- Add Gemma 4 12B/LiteRT-LM to the local-model scouting queue for multimodal Lore/artifact inspection only after testing Windows install, hardware fit, latency, memory, and quality on HoneyDrunk tasks.
- Treat local OpenAI-compatible servers as useful harness adapters, but keep model identity, retention, and cost/latency telemetry explicit.
- For scheduled data ingest, compare MotherDuck Flights-style managed Python jobs against simpler repo scripts based on secret handling, logs, versioning, schedule control, and rollback.

### Quality notes
- Google, OpenAI, and MotherDuck sources are vendor-authored. Use as infrastructure scouting evidence; reproduce performance and operational claims locally before adoption.

## 2026-06-16 compile additions: inference economics, inference engineering, tokenizer optimization, and data debugging

### Source-backed claims
- Inference cost analysis from Injuly frames per-user serving cost as a function of GPU memory bandwidth, compute throughput, active parameters, KV-cache size, context length, batching, and user duty cycle; long advertised context windows are not the same as typical active KV-cache usage. Source: `raw/2026-06-16-web-injuly-inference-cost-at-scale-with-napkin-math.md`. confidence: 1 technical blog source, last-confirmed 2026-06-16.
- The same source argues that without KV cache, generation repeats expensive work over prior tokens, while KV caching shifts decode toward memory-bandwidth limits and makes batching/duty-cycle assumptions central to realistic cost estimates. Source: `raw/2026-06-16-web-injuly-inference-cost-at-scale-with-napkin-math.md`. confidence: 1 technical blog source, last-confirmed 2026-06-16.
- ByteByteGo describes production LLM inference as two phases with different bottlenecks: prefill is compute-bound and measured by time to first token, while decode is memory-bandwidth-bound and measured by tokens per second. Source: `raw/2026-06-16-web-bytebytego-a-guide-to-ai-inference-engineering.md`. confidence: 1 technical explainer source, last-confirmed 2026-06-16.
- ByteByteGo groups inference-engineering techniques by that split: batching, prefix caching, quantization, speculative decoding, tensor/expert parallelism, and prefill/decode disaggregation. Source: `raw/2026-06-16-web-bytebytego-a-guide-to-ai-inference-engineering.md`. confidence: 1 technical explainer source, last-confirmed 2026-06-16.
- A.Q. Nichol reports a cutting-plane approach to tokenizer optimization that found provably optimal tokenizers for small/pretokenized settings, but notes limited practical impact because common tokenizers can already be near optimal and held-out generalization may matter more than training-set optimality. Source: `raw/2026-06-16-web-aqnichol-finding-optimal-tokenizers.md`. confidence: 1 research-practice source, last-confirmed 2026-06-16.
- Goodfire introduces predictive data debugging: passing preference data through an interpreted model can predict which behaviors DPO will amplify or suppress before training, trace them to responsible data clusters, and guide filtering or targeted interventions. Source: `raw/2026-06-16-web-goodfire-predictive-data-debugging-reveal-and-shape-what-your-model-learns-before-you-train.md`; page: [[agent-evaluation-and-benchmarks]]. confidence: 1 research/vendor source, last-confirmed 2026-06-16.

### Typed entities
- concept: prefill
- concept: decode
- metric: time to first token / TTFT
- metric: tokens per second / TPS
- technique: KV cache
- technique: prefix caching
- technique: quantization
- technique: speculative decoding
- technique: tensor parallelism
- technique: expert parallelism
- technique: prefill/decode disaggregation
- method: cutting-plane optimization
- method: integer linear programming / ILP
- concept: predictive data debugging
- method: direct preference optimization / DPO
- page: [[agent-evaluation-and-benchmarks]]

### Explicit relationships
- Inference unit economics depends-on workload duty cycle, batch size, median context length, and KV-cache memory pressure, not only advertised GPU FLOPS.
- Prefill and decode have different bottlenecks, so optimization techniques can improve one phase without improving the other.
- Prefix caching depends-on stable shared prompt prefixes; variable content placed before shared content can defeat the cache.
- Tokenizer optimality on training data can contradict held-out robustness or operational simplicity.
- Predictive data debugging complements post-training evals by surfacing likely behavioral changes before the training run.

### HoneyDrunk implications
- For any self-hosted model spike, record TTFT, TPS, active batch size, median context, KV-cache usage, prompt-cache hit rate, duty cycle, and cost per successful task.
- Treat long-context marketing claims as capacity, not expected cost. Use observed HoneyDrunk task traces to size serving.
- Keep tokenizer work as research signal unless HoneyDrunk has a measured tokenization bottleneck.
- If HoneyDrunk trains or tunes models, evaluate data-debugging methods before productionizing preference data changes.

### Quality notes
- Sources are technical blog/research/vendor sources. Use them for modeling and spike design; confirm hardware specs, serving-engine behavior, and task traffic locally.

## 2026-06-20 compile additions: open-weight model and AI data-center infrastructure signals

### Source-backed claims
- Simon Willison reports Z.ai released GLM-5.2 open weights under an MIT license on 2026-06-16; the captured source describes it as a 753B-parameter text-only MoE model with about 40B active parameters and a 1M-token context window. Source: `raw/2026-06-20-web-simon-willison-glm-5-2-is-probably-the-most-powerful-text-only-open-we.md`. confidence: 1 practitioner/model-watch source, last-confirmed 2026-06-20.
- The same source cites Artificial Analysis ranking GLM-5.2 as the leading open-weight model on its Intelligence Index snapshot, while also noting higher output-token use per task than several peer open-weight models; it also reports a high Code Arena WebDev rank despite text-only input. Source: `raw/2026-06-20-web-simon-willison-glm-5-2-is-probably-the-most-powerful-text-only-open-we.md`. confidence: 1 source with third-party benchmark references, last-confirmed 2026-06-20.
- System Design Newsletter's AI data-center explainer frames AI scaling as constrained by power, cooling, space, memory/storage hierarchy, and networking rather than model code alone; GPU compute stalls when data movement, synchronization, or thermal/power limits dominate. Source: `raw/2026-06-20-web-system-design-newsletter-the-secret-architecture-behind-ai-data-center.md`. confidence: 1 explanatory newsletter source, last-confirmed 2026-06-20.
- The same infrastructure source highlights HBM/GPU memory, CPU RAM, NVMe, parallel filesystems, object storage, NVLink, InfiniBand/RoCE, RDMA, GPUDirect, and zero-copy pipelines as the architecture layers that keep large GPU clusters fed. Source: `raw/2026-06-20-web-system-design-newsletter-the-secret-architecture-behind-ai-data-center.md`. confidence: 1 source, last-confirmed 2026-06-20.
- DigitalOcean's Server-Side Tools public preview makes web access, knowledge bases, MCP servers, and coding-agent-like tools available inside DigitalOcean Inference Engine requests, reinforcing that inference infrastructure is expanding upward into tool hosting and agent runtime support. Source: `raw/2026-06-20-web-digitalocean-server-side-tools-are-now-available-for-digitalocean-infe.md`; page: [[ai-agent-harnesses]]. confidence: 1 DigitalOcean source, last-confirmed 2026-06-20.

### Typed entities
- model: GLM-5.2
- company/lab: Z.ai
- architecture: Mixture of Experts / MoE
- benchmark/provider: Artificial Analysis
- benchmark: Code Arena WebDev
- platform: OpenRouter
- hardware: GPU
- memory: HBM
- storage: NVMe
- filesystem: Lustre / GPFS
- network: NVLink
- network: InfiniBand / RoCE
- technique: RDMA
- technique: GPUDirect
- platform: DigitalOcean Inference Engine

### Explicit relationships
- Open-weight model usefulness depends-on context length, active-parameter cost, output-token behavior, hosting availability, license, and benchmark/task fit.
- AI infrastructure performance depends-on feeding GPUs through memory, storage, and networking layers; FLOPS alone do not predict throughput.
- Hosted inference platforms increasingly combine model serving with retrieval/tool execution, blurring the boundary between inference and agent harness.

### HoneyDrunk implications
- Treat GLM-5.2 as a candidate for model scouting only after checking hardware/hosting cost, output-token inflation, license fit, and HoneyDrunk task quality.
- For self-hosted or rented GPU work, record power/cooling constraints, memory bandwidth, storage tier, network topology, and synchronization overhead; model selection alone is insufficient.
- When comparing inference providers, include tool-hosting trust boundaries and per-tool billing, not just token price.

### Quality notes
- Simon Willison is a strong model-watching source but not a local benchmark. System Design Newsletter is explanatory and partly teaser/paywalled. DigitalOcean is vendor-authored.
