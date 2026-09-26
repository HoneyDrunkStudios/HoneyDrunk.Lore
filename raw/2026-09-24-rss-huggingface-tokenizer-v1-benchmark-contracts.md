---
source: "https://huggingface.co/blog/tokenizers-v1"
title: "tokenizers v1: encode, decode and scaling, measured"
author: "Arthur Zucker; Simon Brandeis; Luc Georges; Lysandre"
date_published: "2026-09-21"
date_clipped: "2026-09-24"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_method: "attributed-summary"
---

# tokenizers v1: encode, decode and scaling, measured

Attributed summary of the fetched article.

Hugging Face describes the Rust release candidate for tokenizers v1, designed to preserve token IDs and existing APIs while reducing encoding and decoding work. Its changes include reusable scratch memory, batched model calls, thread-local word caches, and specialized SIMD splitting for recognized tokenizer patterns. Unrecognized patterns retain the regex path.

The benchmark separates vocabulary loading from encoding, verifies output-ID hashes, compares common supported cases, and distinguishes repeated-document caching from streams of distinct inputs. Reported speedups depend on model family and hardware; Python binding overhead is excluded. Some improvements remain planned for 1.0 rather than implemented in the candidate.

HoneyDrunk application: benchmark retrieval and inference preprocessing with representative documents, correctness checks, and realistic cache behavior before adopting the prerelease. Source confidence: maintainer measurements, not independently reproduced here.

Source: [Original article](https://huggingface.co/blog/tokenizers-v1).
