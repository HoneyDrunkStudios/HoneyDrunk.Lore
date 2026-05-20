---
source: "https://devblogs.microsoft.com/azure-sdk/eliminate-llm-cold-starts-load-models-up-to-6x-faster-with-azure-blob-storage-and-runai-model-streamer/"
title: "Eliminate LLM Cold starts: Load models up to 6x Faster with Azure Blob Storage and Run:AI Model Streamer"
author: "Azure Blog"
date_published: "Tue, 19 May 2026 15:00:07 +0000"
date_clipped: "2026-05-20"
category: "Azure & Cloud"
source_type: "rss"
---

# Eliminate LLM Cold starts: Load models up to 6x Faster with Azure Blob Storage and Run:AI Model Streamer

Source: https://devblogs.microsoft.com/azure-sdk/eliminate-llm-cold-starts-load-models-up-to-6x-faster-with-azure-blob-storage-and-runai-model-streamer/

Stop paying for idle GPUs while model weights copy to disk. Stream them straight into GPU memory instead with Run:AI Streamer from Azure Blob Storage. 
The Problem: Every Cold Start Costs You More Than Money 
GPU compute is among the most expensive cloud infrastructure, and every second a GPU is allocated but unavailable for serving is real money lost. The cost also goes beyond your Azure bill: slow cold starts can delay responses, stress SLAs, and degrade user experience during traffic spikes, when users need capacity most.
In many conventional inference deployments, a cold start triggered by auto-scaling, spot eviction, rolling deploy, restart, or model swap follows the same basic pattern: fetch model weights from object storage to local disk, then load them into GPU memory. In our tests, a 232.8 GiB model took roughly 3 to 5 minutes of allocated GPU capacity with the default vLLM loader, before the replica could serve requests.
Cold starts are not rare in production. Auto-scalers add replicas during spikes, spot VMs can be reclaimed, rolling deploys eventually touch every replica, and multi-tenant serving systems may swap models on demand. Each event can pay the same download-then-load tax unless the serving path is designed to avoid it.
While a large model is moving from object storage to local disk, then into GPU memory, several problems can stack up at once:
The replicas already running absorb all traffic. Queues grow, responses slow down, and the slowest users wait even longer. 
The autoscaler can continue adding replicas based on lagging capacity signals. Each new replica also needs time to load, so usable capacity arrives after the spike has already hurt latency. 
Some requests can start timing out. If queues grow past common 30-to-60-second gateway or client timeouts, users see errors and may retry, adding more pressure. 
Each restart adds another unavailable window. A rolling deployment across many replicas can stretch into a long operational event, and a spot reclaim leaves that replica unavailable until loading completes. 
Run:AI Model Streamer reduces that load window from minutes to seconds in our benchmark, which gives autoscaling, rollout, and recovery systems a much better chance of absorbing the event before the queue cascade starts.
The default loader runs two sequential steps: download the full model from Azure Blob Storage to local disk, then read it from disk into GPU memory. The GPU sits idle through both, and local disk becomes an extra copy stop and a bandwidth bottleneck.
Run:AI Model Streamer skips the local disk hop for model weights. It reads model data from Azure Blob Storage through CPU memory into GPU memory. Removing the extra copy step and local disk bottleneck lets the replica start serving in seconds rather than minutes in our benchmark, reducing the most expensive idle window in a cold start.
The Run:AI Model Streamer is now natively wired into two widely used open-source inference engines: vLLM (a fast and easy-to-use library for LLM inference and serving) and SGLang (a high-performance serving framework for large language models and multimodal models). Both engines stream weights directly from Azure Blob Storage via az:// URIs, so users on Azure can start serving requests in seconds rather than minutes.
Performance: Why Streaming Beats Downloading 
Production autoscalers typically run on tens-of-seconds polling cadences, often once every 30 to 60 seconds (e.g., KEDA , Hugging Face Inference Endpoints ). A cold start that runs several minutes longer than those cycles leaves the autoscaler reacting to traffic that has already moved on, and the cascade from the previous section kicks in. Below are the numbers on a Standard_ND96isr_H100_v5 VM (8x NVIDIA H100 80 GB, 80 Gbps network) streaming from a Premium block blob storage account in the same region.
vLLM Model Load Times: Run:ai Streamer vs. Default Loader 
Model 
Run:ai Streamer (s) 
Default vLLM Loader (s) 
Speedup 
Loads within one autoscaler cycle? 
Meta-Llama-3.1-8B-Instruct (14.99 GiB) 
3.61 +/- 0.17 
15.48 +/- 8.69 
~4.3x 
Default: Yes; Streamer: Yes 
GPT-OSS-120B (60.8 GiB) 
12.76 +/- 1.11 
42.29 +/- 25.96 
~3.3x 
Default: Almost; Streamer: Yes 
Qwen3.5-122B-A10B (232.8 GiB) 
37.14 +/- 0.79 
225.57 +/- 81.00 
~6.1x 
Default: No; Streamer: Yes 
Each configuration was run 5 times under cold-start conditions; results are averages +/- standard deviation.
Key takeaways: 
Cold starts fit one autoscaler cycle, not just run faster. On the 233 GiB Qwen model, the default loader averages ~3.7 minutes with 80-second swings. That triggers the cascade above (queue buildup, over-provisioning, 5xx on tight gateways). The streamer averages ~37 seconds with sub-second variance, so the autoscaler’s next decision sees the new replica online and traffic redistributes cleanly. 
Consistent, saturated throughput. The streamer holds a steady 80 Gbps across the full load. The default loader peaks at ~40 Gbps and drops as low as ~10 Gbps on the largest model, leaving half to seven-eighths of the network pipe idle. 
Speedups grow with model size. The streamer’s lead widens from ~4.3x at 15 GiB to ~6.1x at 233 GiB. The bigger the model, the more disk-hop overhead the streamer skips, which is exactly the regime where cold starts matter most for autoscaling. 
For full benchmark methodology and detailed results, see the complete benchmark report .
Quick Start: Serve Models from Azure Blob Storage 
Both vLLM and SGLang support streaming directly from Azure Blob Storage via az:// URIs. Here is how to get started.
Prerequisites: Get Model Weights into Azure Blob Storage 
Before streaming, you need SafeTensors model weights in an Azure Blob Storage container. Here’s the quickest path:
1. Download the model from Hugging Face: 
huggingface-cli download meta-llama/Llama-3.1-8B-Instruct --local-dir llama-3.1-8b 
2. Upload to your Azure Blob Storage container with azcopy: 
cd llama-3.1-8b
azcopy copy . "https://<your_account>.blob.core.windows.net/<your-container>/models/" --recursive 
The model weights are now accessible at az://<your-container>/models/llama-3.1-70b and ready to stream. Repeat for any model you want to serve.
Note: Paths use the form az://<container>/<path> ; the storage account is passed separately via the AZURE_STORAGE_ACCOUNT_NAME environment variable. The streamer requires SafeTensors weights (the default on Hugging Face), so make sure your model includes .safetensors files, not just .bin .
Using with vLLM 
Install vLLM with Run:AI support: 
uv pip install vllm[runai] 
Set your storage account once for all subsequent commands: 
export AZURE_STORAGE_ACCOUNT_NAME="<your_account_name>" 
Serve a model directly from Azure Blob Storage: 
vllm serve az://<your-container>/models/llama-3.1-8b \
--load-format runai_streamer 
No local copies, no staging scripts.
For multi-GPU serving, enable distributed streaming and optionally tune concurrency and memory limits via --model-loader-extra-config :
vllm serve az://<your-container>/models/llama-3.1-405b \
--load-format runai_streamer \
--tensor-parallel-size 8 \
--model-loader-extra-config '{"distributed": true, "concurrency": 32}' 
Tip: concurrency controls parallel download streams. Higher values (32, sometimes 64) better saturate high-throughput NICs.
Authentication uses DefaultAzureCredential , which supports az login , managed identity, environment variables ( AZURE_CLIENT_ID , AZURE_TENANT_ID , AZURE_CLIENT_SECRET ), and other methods, so it works out of the box on AKS, Azure ML, and VMs with managed identity.
For full details, see the vLLM Run:AI Model Streamer documentation .
Using with SGLang 
SGLang also supports loading models directly from object storage via the Run:AI Model Streamer, including Azure Blob Storage with az:// URIs.
Install SGLang with Run:AI support: 
uv pip install "sglang[runai]" --prerelease=allow 
Start the server pointing at your Azure Blob model path: 
export AZURE_STORAGE_ACCOUNT_NAME="<your_account_name>"
python -m sglang.launch_server \
--model-path az://<your-container>/models/llama-3.1-8b \
--load-format runai_streamer \
--served-model-name llama-3.1-8b 
For multi-GPU setups, SGLang supports distributed streaming to parallelize weight loading across devices. Enable it with tensor parallelism and the distributed flag:
python -m sglang.launch_server \
--model-path az://<your-container>/models/llama-3.1-405b \
--load-format runai_streamer \
--tp 8 \
--model-loader-extra-config '{"distributed": true, "concurrency": 32}' 
SGLang uses a two-phase approach: metadata files (config, tokenizer) are downloaded once to a local cache, while model weights are streamed directly from Azure Blob Storage into GPU memory on demand.
Tuning Performance 
The streamer exposes environment variables for tuning performance across all storage backends, including Azure Blob Storage:
Variable 
Default 
Description 
RUNAI_STREAMER_CONCURRENCY 
8 (object storage) / 16 (filesystem) 
Number of concurrent I/O threads 
RUNAI_STREAMER_MEMORY_LIMIT 
-1 (distributed) / 40 GiB (non-distributed) 
CPU buffer memory cap; set to a byte value to limit 
Increasing concurrency (for example, from the default 8 to 32 or 64) can improve throughput, especially when streaming from Azure Blob Storage where the backend can handle high parallelism. Retries and timeouts use Azure SDK defaults automatically. See the streamer usage docs for the full list of configuration options.
Getting Involved 
The Run:AI Model Streamer is fully open source under the Apache 2.0 license. The Azure Blob Storage plugin was developed in collaboration between Run:AI and Microsoft to bring first-class streaming support to Azure customers.
GitHub: run-ai/runai-model-streamer 
PyPI: pip install runai-model-streamer[azure] 
Azure Blob PR: #116 , the full implementation story and review discussion 
For deeper technical details on the streaming architecture, see the Run:AI Model Streamer documentation .
Have questions or want to share your benchmarks? Open an issue on GitHub .
