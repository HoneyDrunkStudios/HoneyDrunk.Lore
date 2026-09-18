---
source: "https://huggingface.co/blog/asyncgrpo-lora-hfjobs"
title: "Async GRPO with LoRA across HF Jobs: a bucket, a proxy, and no NCCL"
author: "Amine Dirhoussi; Quentin Gallouédec; Kashif Rasul; Sergio Paniego"
date_published: "2026-09-10"
date_clipped: "2026-09-16"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
---

# Async GRPO with LoRA across HF Jobs: a bucket, a proxy, and no NCCL

Source: [Async GRPO with LoRA across HF Jobs: a bucket, a proxy, and no NCCL](https://huggingface.co/blog/asyncgrpo-lora-hfjobs)

## Attributed content summary

Hugging Face describes asynchronous reinforcement-learning training with a LoRA trainer and separate vLLM inference jobs. Small adapter updates travel through a shared storage bucket instead of transferring complete model weights between machines. A proxy handles authentication, routes rollouts toward cached prefixes, and broadcasts adapter loads.

Adapters are published as versioned directories. Ongoing rollouts retain their original policy while later requests use newer versions. The example reserves enough adapter slots for the permitted staleness window plus the temporary overlap during replacement; insufficient slots can evict a policy still serving work.

The transferable pattern is to separate training from generation, persist checkpoints outside ephemeral jobs, and measure which stage limits throughput before adding hardware. This is a specific TRL/vLLM implementation and vendor experiment, not a guarantee that bucket synchronization or the reported performance transfers to other workloads. Pin compatible versions and validate storage visibility, authentication, and recovery before adoption.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
