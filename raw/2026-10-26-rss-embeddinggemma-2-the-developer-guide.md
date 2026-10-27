---
source: "https://developers.googleblog.com/embeddinggemma-2-the-developer-guide"
title: "EmbeddingGemma 2: The Developer Guide"
author: "Maarten Grootendorst; Ian Ballantyne"
date_published: "2026-10-06"
category: "AI / LLM Research & Tooling"
source_type: "rss"
date_clipped: "2026-10-26"
---

# EmbeddingGemma 2: The Developer Guide

![embeddinggemma2-banner](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/embeddinggemma2-banner.original.jpg)

Modern search and retrieval augmented generation (RAG) applications increasingly need to work across diverse content types, from technical documentation and source code to images, video clips, and audio recordings. The challenge is finding models that deliver strong retrieval accuracy while maintaining low latency across all these formats without requiring massive compute infrastructure to run and index.

[**EmbeddingGemma 2**](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2) is designed to provide a single, compact open model released under the Apache 2.0 license, delivering exceptional multimodal performance for its size. Based on Gemma 4, this sub-1B model maps **text, code, images, video, and audio** into a unified 768-dimensional space. Its modular architecture lets you load only what you need, scaling from 270M parameters for text and code up to 740M parameters for all modalities.

Key capabilities include:

- **Native multimodal retrieval:** Unlocks search across text, code, images, video, and audio directly in a shared 768-dimensional vector space.
- **Superior code understanding:** Significantly outperforms EmbeddingGemma 1 on code search and technical retrieval, making it ideal for local codebase indexing and agentic code search.
- **Modular memory footprint:** Selectively load only the encoders you need at runtime: 270M (text/code), 440M (text + vision), 570M (text + audio), or 740M (full multimodal), all projecting into the same compatible vector space.
- **Flexible vector storage:** Matryoshka Representation Learning (MRL) enables dynamic truncation from 768 dimensions down to 128 dimensions, cutting vector database storage requirements while retaining much of the original quality. For instance, at 256 dimensions, most of the full quality of the original embedding on text and code is retained and about 95% on image, video, and speech retrieval

---

## **How it works under the hood**

EmbeddingGemma 2 replaces chained models with modular encoders that project into a shared 768-dimensional space:

![embeddinggemma2](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/embeddinggemma2.original.png)

Even though each modality is processed by a specialized encoder, all inputs are processed through the shared backbone and their resulting embeddings occupy the same dimensional space:

1. **Text and code (270M base):** An adapted Gemma 4 decoder with an 8,192-token context window.
2. **Vision (+170M):** A vision encoder that processes images, visual documents (PDFs, slides, charts), and video frames.
3. **Audio (+300M):** A dedicated speech and sound encoder that directly ingests raw audio.
4. **Modular loading:** You only load what you need. Run text-only at 270M parameters, add vision for 440M parameters, or load the full multimodal model at 740M parameters.
5. **Shared tokenizer & audio encoder with Gemma 4:** When paired with Gemma 4 in an on-device RAG pipeline, both models share the same text tokenizer and audio encoder architecture, reducing the total memory footprint.

---

## **See it in action**

[![

Sorry, your browser doesn't support playback for this video

](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/wagtailvideo-pbiup54x_thumb.jpg)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/pi_agent_flyto_transformers_dark_1.mp4)

We embedded the Hugging Face transformers codebase with the 270M text-only setup. Then, the embeddings are used to efficiently search through this large codebase by matching the similarity of the query with the codebase using an Agent (Gemma 4 26B A4B with the Pi agent harness) .

## **Developer Guide: Using EmbeddingGemma 2**

You can run EmbeddingGemma 2 across text, code, images, video, and audio with the [sentence-transformers](https://github.com/huggingface/sentence-transformers) library (v6.1.0 or later):

```
pip install -U sentence-transformers[image,audio,video] transformers
```

Shell

Copied

### **Step 1: Load the Model**

The full model embeds text, code, images, video, and audio:

```
from sentence_transformers import SentenceTransformer

# Full model: all modalities (740M parameters)

MODEL_ID = "google/embeddinggemma-2"

model = SentenceTransformer(MODEL_ID)
```

Python

Copied

To minimize memory usage, you can omit unused modality encoders at load time by setting `vision\_config` or `audio\_config` to `None` in `config_kwargs`. Disabled encoders are never loaded into memory, so the savings apply to both the weights and peak allocation:

```
# Text only (270M parameters)

text_only_model = SentenceTransformer(

    MODEL_ID,

    config_kwargs={"vision_config": None, "audio_config": None},

)

# Text, images, and video (440M parameters)

text_image_model = SentenceTransformer(

    MODEL_ID,

    config_kwargs={"audio_config": None},

)

# Text and audio (570M parameters)

text_audio_model = SentenceTransformer(

    MODEL_ID,

    config_kwargs={"vision_config": None},

)
```

Python

Copied

## **Step 2: Embed Text and Code with Task Prompts**

EmbeddingGemma 2 is trained with short task instructions to steer representations for specific tasks. Set prompt\_name in encode() to add it for you:

![table1 (1)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/table1_1.original.png)

For retrieval, encode queries and documents with different prompts:

```
query = "What causes the northern lights?"

document = "The northern lights are caused by charged particles from the sun.." # truncated

# Embed using `prompt_name`

query_emb = model.encode(query, prompt_name="SearchQuery")

doc_emb = model.encode(document, prompt_name="Document")

print(model.similarity(query_emb, doc_emb))
```

Python

Copied

## **Step 3: Embed Images, Video, Audio, and Interleaved Inputs**

Pass media as a dictionary keyed by modality without a prompt. To embed text and media together, mark where each item goes with `<|image|>`, `<|video|>`, or `<|audio|>`:

```
# Cross-modal search: one text query against a photo and a sound recording

image_emb = model.encode({"image": "sunset_beach.jpg"})

audio_emb = model.encode({"audio": "ocean_waves.wav"})

query_emb = model.encode("ocean waves at sunset", prompt_name="SearchQuery")

print(model.similarity(query_emb, image_emb))

print(model.similarity(query_emb, audio_emb))

# Interleaved: one embedding for a product listing with text, photo, and video

listing_emb = model.encode({

    "text": "Waterproof trail shoe. <|image|> Grip test on wet rock: <|video|>",

    "image": "trail_shoe.jpg",

    "video": "grip_test.mp4",

})

query_emb = model.encode("waterproof trail shoes", prompt_name="SearchQuery")

print(model.similarity(query_emb, listing_emb))
```

Python

Copied

Despite coming from different modalities, the embeddings generated by EmbeddingGemma 2 occupy the same dimensional space and can be compared on their semantic similarity.

[![

Sorry, your browser doesn't support playback for this video

](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/wagtailvideo-rjg4vpri_thumb.jpg)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/original_videos/EG2-DRAWING-CHALLENGE.mp4)
[Draw the target object and EmbeddingGemma 2 guesses what you’re drawing. Try it yourself at the Embedding Draw Challenge.](https://huggingface.co/spaces/google/embedding-draw-challenge)

## **Step 4: Truncate Dimensions with Matryoshka (MRL)**

Pass `truncate_dim` (`512`, `256`, or `128`) with `normalize_embeddings=True` to get shorter, unit-length vectors. Queries and documents must use the same dimension:

```
# Truncate the query

query_emb = model.encode(

    query,

    prompt_name="SearchQuery",

    truncate_dim=256,

    normalize_embeddings=True,

)
```

Python

Copied

To use one dimension for every call, set it at load time instead: SentenceTransformer(MODEL\_ID, truncate\_dim=256). For instance, in bfloat16 precision, storing a million 768-dimensional vectors takes roughly 1.5 GB of memory, while truncating them to 128 dimensions requires just 250 MB. That 6x reduction allows you to store six times as many embeddings in the same memory budget, making it much easier to fit large indexes in memory or on-device.

---

## **Choosing Your Configuration**

In sentence-transformers, all four encoder setups load from the same checkpoint, so they share one vector space: a query embedded with the 270M text-only setup can be matched directly against documents embedded with the full model.

As a general guideline, load only the encoders your data needs, and truncate dimensions only when storage or search speed require it.

### **Which Encoders to Load**

![table2 (1)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/table2_1.original.png)

If you start with a text-only index and later add image or audio embeddings, simply reload the model with the additional encoder enabled. Embeddings you have already computed do not need to be re-computed.

## **Which Dimension to Use**

- **768d or 512d:** Multimodal and visual document retrieval, or whenever recall matters more than storage.
- **256d (3x storage reduction):** Storage-constrained indexes. Keeps most of the full quality of the original embedding on text and code and about 95% on image, video, and speech retrieval, at a third of the storage.
- **128d (6x storage reduction):** Large text-only indexes and first-stage shortlisting (shortlisting before re-ranking). Text and code retains around 90% quality, but image, video, and speech retrieval quality drop to around 75%. Validate on your target data before deploying 128d for multimodal queries..

## **How Much Fits in One Input**

All modalities share the 8,192-token context window, at fixed rates:

![table3](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/table3.original.png)

The maximums assume a single modality with no text. Pass media as file paths (MP4 for video), URLs (images and audio), or in-memory PIL images, arrays, and tensors. Video is sampled at 1 frame per second by default, and audio should be 16 kHz mono.

---

## **Benchmarks & Evaluation**

EmbeddingGemma 2 scores 14% higher than EmbeddingGemma 1 on MTEB (Code), adds image, video, and audio retrieval while retaining the accuracy on multilingual text of EmbeddingGemma 1

![Massive Text Embedding Benchmark (Code) (1)](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Massive_Text_Embedding_Benchmark_Code_1.original.png)

## **Getting Started Today**

Ready to explore multimodal embeddings? Take a look at the following resources to find out more:

- **Download the Weights:** Access the weights of the [model](https://huggingface.co/google/embeddinggemma-2) (released under the Apache 2.0 license) directly on Hugging Face.
- **Integrate & Learn:** Read more about EmbeddingGemma 2 in the [Gemma documentation](https://ai.google.dev/gemma/docs/embeddinggemma).
- **Use Your Favorite Development Tools:** Run the model efficiently using [vLLM](https://vllm.ai/), Hugging Face [Transformers](https://huggingface.co/google/embeddinggemma-2), [sentence-transformers](https://github.com/huggingface/sentence-transformers), [SGLang](https://www.sglang.io/), [MLX](https://github.com/ml-explore/mlx-lm), [Ollama](http://ollama.com/library/embeddinggemma-2), [LMStudio](https://lmstudio.ai/), and [LiteRT](https://developers.google.com/edge/litert-lm).
- **Adapt & Fine-Tune:** For rapid experimentation, you can explore efficient fine-tuning with [Unsloth](https://unsloth.ai/docs/models/embeddinggemma-2).
- **Explore Search**: Try the *Instant Media Search* and *Video Moments Finder* on-device demos in the [Google AI Edge Gallery](https://developers.google.com/edge/gallery).
