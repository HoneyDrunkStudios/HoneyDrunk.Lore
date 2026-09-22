---
source: "https://huggingface.co/blog/train-multi-vector-encoder"
title: "Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers"
author: "Tom Aarsen"
date_published: "2026-08-26"
date_clipped: "2026-09-20"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
---

# Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers

Source: [Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-multi-vector-encoder)

Attributed summary of the fetched full written article; not a verbatim reproduction. Claims remain source-specific and have not been independently reproduced.

Tom Aarsen describes training late-interaction retrieval models with Sentence Transformers. Token-level representations preserve detailed query matches but enlarge the index. Document-length limits can discard relevant material before scoring, so training and serving lengths deserve explicit checks.

The recipe uses domain question/passage pairs, in-batch negatives with gradient caching, explicit query/document prompts, and held-out retrieval evaluation. Easy evaluation corpora can hide differences; the article adds deduplicated distractor passages to make retrieval meaningful. Training loss alone is insufficient.

On the author's MIRIAD setup, the fine-tuned model scores 0.9139 NDCG@10 against 0.8520 for its zero-shot counterpart. These results concern one constructed domain benchmark, whose generated questions favor lexical overlap. They do not establish universal superiority.

Raw token embeddings require about 45 GB for the evaluated corpus. Pooling, pruning, and quantization trade storage against quality; the article reports a 3.37 GB quantized configuration at 0.8984 NDCG@10.

HoneyDrunk relevance: evaluate retrieval quality, truncation, and index cost together before selecting a future Lore retrieval implementation.
