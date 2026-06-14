---
source: "https://huggingface.co/blog/RikkaBotan/stable-static-embedding-in-practice"
title: "SSE in Practice: Fast Static Embeddings You Can Train, Serve, and Plug Into Your Agents"
author: "Hugging Face Blog"
date_published: "2026-06-13"
date_clipped: "2026-06-14"
category: "AI / LLM Research & Tooling"
source_type: "web"
---

# SSE in Practice: Fast Static Embeddings You Can Train, Serve, and Plug Into Your Agents

Source: https://huggingface.co/blog/RikkaBotan/stable-static-embedding-in-practice

Sentence Similarity • Updated • 57

#
[
](https://huggingface.co#sse-in-practice-fast-static-embeddings-you-can-train-serve-and-plug-into-your-agents)
SSE in Practice: Fast Static Embeddings You Can Train, Serve, and Plug Into Your Agents

[Community Article](https://huggingface.co/blog/community)Published June 13, 2026

**Rikka Botan**

Independent Researcher, Japan

*https://rikka-botan.github.io*

**Abstract**

**SSE (Stable Static Embedding)**through two companion open-source repositories. SSE is a family of ~16M-parameter static embedding models that reach a NanoBEIR English mean nDCG@10 of

**0.5158 (v2)**while running at tens of thousands of queries per second on CPU. The first repository,

**Stable-Static-Embedding-Models**, lets you generate embeddings, run semantic search, benchmark accuracy versus speed, build a quantized variant, and even retrain the model on your own data. The second,

**Fast-Embedding-MCP-SSE**, lets you serve the model behind an

**OpenAI-compatible API**so existing code works unchanged, run a self-contained semantic search server with no external database, and expose embeddings as

**MCP tools**to agents such as Claude Code and Claude Desktop.

[
](https://huggingface.co#1-technical-background)
1 Technical background

SSE is a *static* embedding model: it looks up token vectors and mean-pools them, with no attention at inference time. That is why it is fast on CPU and small enough to run almost anywhere. The one idea worth knowing is **Separable Dynamic Tanh (Separable DyT)**, a per-dimension transformation applied after pooling that stabilizes training and regularizes the representation space — which is what lets the model stay accurate even when its vectors are shortened.

That shortening is **Matryoshka (MRL)** truncation: the native 512-dimension vector can be cut to 256, 128, 64, or 32 dimensions and renormalized, trading a little accuracy for more speed and less storage. Every usage pattern below exposes this as a single dial. Full benchmark details are in the v1 and v2 technical reports.

**Technical report v1:** [https://huggingface.co/blog/RikkaBotan/stable-static-embedding-technical-report](https://huggingface.co/blog/RikkaBotan/stable-static-embedding-technical-report)

**Technical report v2:** [https://huggingface.co/blog/RikkaBotan/stable-static-embedding-v2-technical-report](https://huggingface.co/blog/RikkaBotan/stable-static-embedding-v2-technical-report)

##
[
](https://huggingface.co#2-what-you-can-do-with-stable-static-embedding-models)
2 What you can do with Stable-Static-Embedding-Models

Repository: [https://github.com/Rikka-Botan/Stable-Static-Embedding-Models](https://github.com/Rikka-Botan/Stable-Static-Embedding-Models) (MIT License)

This is the model-and-toolkit side. Setup is one command with [uv](https://docs.astral.sh/uv/) (`uv sync`

), and the published models cover English (v1/v2), Japanese, and bilingual Japanese–English.

###
[
](https://huggingface.co#21-generate-embeddings-and-measure-similarity)
2.1 Generate embeddings and measure similarity

The models load directly through `sentence-transformers`

, so encoding text is two lines. You get normalized vectors you can compare with a dot product, and you choose the dimension at encode time.

```
from sentence_transformers import SentenceTransformer
model = SentenceTransformer(
"RikkaBotan/stable-static-embedding-fast-retrieval-mrl-en-v2",
trust_remote_code=True,
)
emb = model.encode(
["What is Stable Static Embedding?", "A fast static text encoder."],
normalize_embeddings=True,
)
similarity = emb[0] @ emb[1] # cosine similarity
```


This is the building block for semantic search, deduplication, clustering, classification, or feeding a downstream retriever.

###
[
](https://huggingface.co#22-run-a-live-semantic-web-search-demo)
2.2 Run a live semantic web-search demo

A bundled Gradio app turns the model into an interactive semantic search over live web results. It launches with one command and lets you swap in any of the published models through an environment variable — useful for trying the model on real queries before wiring it into anything.

```
uv run --extra app python app/gradio_app.py
```


###
[
](https://huggingface.co#23-benchmark-accuracy-versus-speed-and-pick-a-dimension)
2.3 Benchmark accuracy versus speed and pick a dimension

Because the model is meant for resource-constrained settings, the repository includes scripts to evaluate it on the NanoBEIR benchmark across every Matryoshka dimension and to measure throughput. In practice this answers the question you actually care about: *how small can I make the vectors before quality drops too far for my use case?* The reported numbers below illustrate the curve.

**Table 1 | SSE v2 accuracy across Matryoshka dimensions (NanoBEIR English mean nDCG@10)**

| Dimensions | 32 | 64 | 128 | 256 | 512 |
|---|---|---|---|---|---|
| SSE v2 | 0.349 | 0.424 | 0.473 | 0.503 | 0.516 |

Notably, the 256-dimension setting already matches the score a prior 1024-dimension model reported — so you can often halve or quarter your vector size with little loss.

```
uv run --extra eval python scripts/analyze_matryoshka.py --config configs/matryoshka_model_config.json
```


###
[
](https://huggingface.co#24-shrink-the-model-further-with-4-bit-quantization)
2.4 Shrink the model further with 4-bit quantization

If you need an even smaller footprint, a single script builds a 4-bit (SSEQ) quantized variant of any of the models, on top of the already-small ~16M-parameter base.

```
uv run python scripts/make_quantized.py \
--model-name RikkaBotan/stable-static-embedding-fast-retrieval-mrl-en \
--output-dir ./sse-q4
```


###
[
](https://huggingface.co#25-train-it-on-your-own-data)
2.5 Train it on your own data

The full training recipe from the technical reports is reproducible here. You can fine-tune or retrain on your own dataset mixture and then push the result to the Hugging Face Hub with the included upload script. A `--smoke`

mode validates the whole pipeline offline on a tiny dataset first, so you can confirm everything works before committing GPU time. This is the path to a domain-specific or additional-language SSE model.

```
uv run --extra train python scripts/train.py \
--language en --output-dir outputs/sse-en
```


##
[
](https://huggingface.co#3-what-you-can-do-with-fast-embedding-mcp-sse)
3 What you can do with Fast-Embedding-MCP-SSE

Repository: [https://github.com/Rikka-Botan/Fast-Embedding-MCP-SSE](https://github.com/Rikka-Botan/Fast-Embedding-MCP-SSE) (Apache-2.0 License)

This is the serving side. It wraps the v2 English model in interfaces that existing tools already speak. Setup is again `uv sync`

; the first run downloads the model (~60 MB) and caches it. Everything runs locally.

###
[
](https://huggingface.co#31-drop-in-replacement-for-the-openai-embeddings-api)
3.1 Drop-in replacement for the OpenAI embeddings API

Start the server (`uv run sse-api`

, listening on port 8000) and it exposes an **OpenAI-compatible** `/v1/embeddings`

endpoint. Any code already written against the OpenAI SDK works by changing only the `base_url`

— no key, no cloud calls, and you can request a truncated dimension per call.

```
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="not-needed")
resp = client.embeddings.create(
model="RikkaBotan/stable-static-embedding-fast-retrieval-mrl-en-v2",
input=["hello world", "good morning"],
dimensions=256, # 512 / 256 / 128 / 64 / 32
)
print(len(resp.data[0].embedding)) # 256
```


###
[
](https://huggingface.co#32-run-a-self-contained-semantic-search-server)
3.2 Run a self-contained semantic search server

Beyond raw embeddings, the server offers ready-made similarity and retrieval endpoints — including an **in-memory index** you can add documents to and query — so you get working semantic search without standing up a separate vector database.

**Table 2 | Server endpoints and what each one is for**

| Endpoint | What you use it for |
|---|---|
`/v1/embeddings` |
OpenAI-compatible embeddings (with `dimensions` ) |
`/similarity` |
Cosine similarity matrix between two sets of texts |
`/search` |
Rank a set of documents against a query (stateless) |
`/index/add` |
Add documents to the in-memory index |
`/index/query` |
Search the in-memory index |
`/index/stats` |
Check how many documents are indexed |
`/index/clear` |
Empty the index |
`/health` |
Health check |

A typical flow is one `curl`

to add documents and another to query them by meaning:

```
curl -X POST http://localhost:8000/index/add \
-H "Content-Type: application/json" \
-d '{"documents": ["The cat sat on the mat", "Paris is in France"]}'
curl -X POST http://localhost:8000/index/query \
-H "Content-Type: application/json" \
-d '{"query": "Where is Paris?", "top_k": 1}'
```


###
[
](https://huggingface.co#33-give-your-agent-embedding-and-search-tools-via-mcp)
3.3 Give your agent embedding and search tools via MCP

The same capabilities are exposed as an **MCP server**, so agentic clients can call them as native tools: `embed_text`

, `similarity`

, `search`

, and the `index_*`

family. Registration is one command for **Claude Code**:

```
claude mcp add sse-embedding -- uv run python -m sse_embedding.mcp_server
```


and a short JSON block for **Claude Desktop**. Once registered, the agent can embed text, compare meanings, and build and query a local document index entirely on your machine — useful for giving an assistant fast, private retrieval over your own notes or files.

##
[
](https://huggingface.co#4-choosing-your-dimension)
4 Choosing your dimension

Both sides expose the same Matryoshka dial — as an evaluation sweep when training, and as a per-request `dimensions`

value when serving. The rule of thumb: start at 512 for best quality, drop to 256 for roughly half the storage and cost at near-identical accuracy, and go to 128/64/32 when speed and footprint matter more than the last few points of recall. Truncation is always applied to the full vector and renormalized, so cosine similarity stays valid at every level.

##
[
](https://huggingface.co#5-conclusion)
5 Conclusion

Between the two repositories you can encode text, run semantic search, benchmark and tune the accuracy-versus-speed trade-off, quantize, and retrain on your own data — then serve the result through an OpenAI-compatible API or hand it to an agent as MCP tools, all locally and on modest hardware. SSE's small size and CPU speed make each of these practical to actually run, not just to demo.

##
[
](https://huggingface.co#acknowledgements)
Acknowledgements

Our interest in static embeddings originated from Tom Aarsen's article, [ Train 400x faster Static Embedding Models with Sentence Transformers](https://huggingface.co/blog/static-embeddings).

I thank the developers of sentence-transformers, python, pytorch, uv, and the Model Context Protocol, and all the researchers whose work this builds upon.

And most of all, thank you for your interest in this article.

##
[
](https://huggingface.co#about-us)
About us

Japanese independent researcher having shy and pampered personality. Twin-tail hair is a charm point. Interested in nlp. Usually using python and C.

Please contact us if you have any requests for joint research, writing, speaking engagements, or employment.
