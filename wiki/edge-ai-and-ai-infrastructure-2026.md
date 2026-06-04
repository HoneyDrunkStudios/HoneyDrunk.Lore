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
