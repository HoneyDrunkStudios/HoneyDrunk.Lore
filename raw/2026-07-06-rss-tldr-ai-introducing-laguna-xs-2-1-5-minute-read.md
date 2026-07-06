---
source: "https://poolside.ai/blog/introducing-laguna-xs-2-1"
title: "Introducing Laguna XS 2.1 (5 minute read)"
author: "TLDR AI"
date_published: "Fri, 03 Jul 2026 00:00:00 GMT"
date_clipped: "2026-07-06"
category: "AI / LLM Research & Tooling"
source_type: "rss"
discovered_via: "https://tldr.tech/ai/2026-07-03"
source_role: "primary-via-tldr"
---

# Introducing Laguna XS 2.1 (5 minute read)

Source: https://poolside.ai/blog/introducing-laguna-xs-2-1

2026-07-02 Introducing Laguna XS 2.1 Poolside team Table of contents XS 2.1 vs XS.2 A better local experience A more open license Get started strong]:text-secondary prose-a:text-pri-800 prose-a:font-normal prose-a:hover:text-pri-700 prose-pre:p-8 prose-li:[&>p]:my-4 prose-a:underline-offset-4 prose-ul:text-list col-span-1 col-start-1 row-start-1 min-w-0 max-w-[unset] svelte-18z5kmr"> Today we're releasing Laguna XS 2.1, an upgraded version of our Laguna XS.2 model. 
Laguna XS 2.1 is a 33B total parameter Mixture-of-Experts model with 3B activated parameters per token, designed for agentic coding and long-horizon work on a local machine. It's the same architecture as XS.2, with a notable improvement on SWE-bench Multilingual and stronger performance on terminal-style tasks. 
XS 2.1 vs XS.2 XS 2.1 improves upon XS.2 across a key field of agentic coding benchmarks. The largest move is on SWE-bench Multilingual, up 5.4 points to 63.1%. 
Laguna XS 2.1 33B-A3B Laguna XS.2 33B-A3B Qwen3.6 35B-A3B North Mini Code (Cohere) 30B MAI-Code-1-Flash 137B gpt-oss-120b 120B Claude Haiku 4.5 - GPT-5.4 Nano - SWE-bench Verified SWE-bench Verified Resolved tasks on SWE-bench Verified. 0.0 0.0 0.0 0.0 0.0 0.0 SWE-bench Multilingual SWE-bench Multilingual Resolved tasks on SWE-bench Multilingual. 0.0 0.0 0.0 0.0 SWE-Bench Pro SWE-Bench Pro Resolved tasks on SWE-Bench Pro. 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 Terminal-Bench 2.0 Terminal-Bench 2.0 Resolved tasks on Terminal-Bench 2.0. 0.0 0.0 0.0 0 0.0 0.0 0.0 0.0 Benchmarks as of 2 July 2026 † We have chosen to include dense models with larger activated parameter counts to highlight the relative efficiency of MoE models. A better local experience XS 2.1 is supported in vLLM, SGLang, NVIDIA TensorRT-LLM, HF transformers and Ollama, with llama.cpp support coming soon. We’re also making three quantized checkpoints available—FP8, INT4 & NVFP4—allowing XS 2.1 to be deployed in setups with tighter VRAM & compute budgets. We also intend to make quantized GGUF checkpoints available in the near future as part of our native llama.cpp support. 
We’re also open-weighting DFlash speculator models for each XS 2.1 checkpoint. We trained these speculators to balance overhead and acceptance rate. In our tests, these speculator models double the achieved tok/s, making local inference of XS 2.1 even faster than it was before. 
We are serving the model at 256K context length on our API and through OpenRouter . 
A more open license We are licensing Laguna XS 2.1 under OpenMDW-1.1. 
We are making this change to support open model distribution for the community. OpenMDW-1.1 is fully permissive and designed for models and related artifacts, giving developers and organizations a more consistent framework for using, modifying and deploying open models. 
We are glad to support the direction NVIDIA and the Linux Foundation are taking with OpenMDW, and we think this is a useful step toward reducing licensing friction for open model releases. 
Get started Download the weights from the Laguna XS 2.1 collection on Hugging Face — BF16, FP8, NVFP4, and INT4. Use the model on OpenRouter (poolside/laguna-xs-2.1) or via our API . Free and paid endpoints are both available with paid pricing matched to XS.2 at $0.10 / $0.20 / $0.05 per 1M input / output / cache-read tokens. Run it locally with Ollama, llama.cpp, TRT-LLM, vLLM, or SGLang, and add the DFlash draft model for faster inference. Install pool , our terminal-based coding agent, for the best agent experience with the model. We want to see what people build with XS 2.1, and we want your feedback. Try both models side by side and tell us where 2.1 is better and where it isn't. Join our Discord to share what you find and talk to the team directly, or reach us at models@poolside.ai or on X . 
Laguna XS.2 will sunset on our API after 1 week. XS.2 will remain available as part of Baseten’s Model Library for dedicated deployments. 
Footnotes 
All benchmarking for Laguna XS 2.1 was completed using Laude Institute’s Harbor Framework with our agent harness , with a maximum of 500 steps and sandboxed execution. The same sampling parameters were used for all Laguna XS 2.1 benchmarking: temperature=1.0, top_k=20 and top_p=1, with thinking mode enabled and a context length of 256K tokens. All tasks were run in their own sandbox using 8 GB RAM/2 CPUs, with the exception of Terminal-Bench 2.0, which used 48 GB RAM/32 CPUs. 
Some base task images and verifiers were patched to fix infrastructure reliability issues inherent in task setup, such as rate limits on third-party dependencies in external registries used by the verifier. All four agentic benchmarks were run with patched images. We also ran a reward-hack judge post-hoc on Laguna XS 2.1 evaluation runs and did not find significant reward hacking after joint judge review and manual review. 
SWE-bench Verified: mean pass@1 averaged over 4 attempts per task SWE-bench Multilingual: mean pass@1 averaged over 4 attempts per task SWE-Bench Pro: mean pass@1 averaged over 2 attempts per task Terminal-Bench 2.0: mean pass@1 averaged over 5 attempts per task; 48 GB RAM/32 CPUs * We used the highest publicly-referenced scores for all comparison models across each benchmark. In all cases these were official scores published in release blog posts or equivalent, with the exception of gpt-oss-120b and Claude Haiku 4.5 where the highest published (verified) scores for SWE-Bench Pro and Terminal-Bench 2.0 are from their respective official leaderboards. 
Copy link to clipboard
