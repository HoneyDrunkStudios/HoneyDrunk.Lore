---
source: "https://huggingface.co/blog/transformers-llama-cpp-quants"
title: "Transformers now runs llama.cpp quants"
author: "Marc Sun; Arthur Zucker; Lysandre"
date_published: "2026-09-22"
date_clipped: "2026-09-22"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
---

# Transformers now runs llama.cpp quants

Source: [Transformers now runs llama.cpp quants](https://huggingface.co/blog/transformers-llama-cpp-quants)

Attributed summary of the fetched written article; not a full reproduction. Source claims have not been independently reproduced.

Hugging Face integrates packed GGUF inference into Transformers by reusing ggml kernels through the kernels library. Developers can load a specific GGUF file with the usual model-loading API, generate through PyTorch, and expose a compatible local serving endpoint.

The initial packed path targets Apple Silicon and supported Qwen3.5-family architectures, including compatible Qwen3.8 checkpoints. It requires compatible kernel builds and development-version Transformers at publication. Unsupported kernels can trigger dequantization and greater memory consumption; padded batches remain a limitation.

The implementation combines specialized Metal operations with fewer CPU/GPU synchronization points during generation. Published throughput comparisons use different timing conventions for Transformers and llama.cpp, so they do not establish identical-condition performance. The authors still recommend llama.cpp when efficient local inference is the primary goal.

HoneyDrunk relevance: evaluate quantized models through existing Python tooling while recording device, kernel, architecture, and fallback behavior. This release does not establish packed inference support on the studio's Windows hardware.
