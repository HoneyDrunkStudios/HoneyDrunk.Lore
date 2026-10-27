---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/evaluating-decision-models-for-document-categorization"
title: "Evaluating decision models for document categorization"
author: "Pallavi Sinha"
date_published: "2026-10-15"
category: "Software Architecture"
source_type: "rss"
date_clipped: "2026-10-26"
---

# Evaluating decision models for document categorization

Consider a scenario in which thousands of documents require tagging by domain, type or sensitivity. The labels are already known, but a reliable mechanism is necessary to assign the appropriate classification and explicitly indicate instances of uncertainty.

An LLM can do this, but it generates an answer as text. You then need to extract and validate the label, handle malformed responses and deal with answers outside your allowed set. It also spends more tokens generating the response rather than simply making the decision.

Instead, an AI decision model approaches the problem differently. You give it the document and a defined set of choices, and it returns a probability for each one. The output is constrained, uncertainty is explicit and there are less generated tokens.

In this blog post I'll explore how decision models work, my experience using Laya for document categorization, the practical considerations encountered and how its results compare with an LLM (Claude Sonnet).

## Understanding decision models

A decision model supports three main question types:

**Choice:**Select one label from a predefined list, such as billing, support or sales.**Score:**Assign a level on an ordered scale, such as customer frustration from one to five.**Yes/No:**Make a binary judgment, such as whether an action needs a signature.

Each answer includes probabilities, which makes uncertainty explicit instead of forcing a guess.

## Exploring Laya

The exploration started by researching Laya and Jev:

[Laya](https://github.com/NandhaKishorM/laya)(Convai Innovations) — open weights, locally runnable, with a 512-token context window for English language model.[Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)(TypeSafe AI) — paid model, managed API with support for up to 64,000 tokens.

For this first experiment I used Laya because it could be [run locally](https://huggingface.co/blog/sora-2/laya-ai-model-how-it-works-run-it-locally-and-eval) and is free. After installing the [laya package(v0.3.22)](https://pypi.org/project/laya/0.3.22/) via pip and loading its [Hugging Face checkpoint](https://huggingface.co/convaiinnovations/laya), I generated roughly 5,000-word documents across four domains: legal, medical, finance and technology.

I then gave Laya a choice question with those domains as the options as described below:

```
{
"domain": {
"type": "choice",
"instructions": "What subject-matter domain does the document belong to?",
"criteria": {
"legal": "contracts, litigation, statutes, court rulings, legal obligations",
"medical": "diagnoses, symptoms, treatments, clinical or health guidance",
"finance": "investments, markets, accounting, loans, currency, budgets",
"technology": "software, hardware, programming, IT infrastructure, computing"
}
}
}
```

For a legal document, the model returned:

```
{
"answers": {
"domain": {
"type": "choice",
"choice": "legal",
"probabilities": {
"legal": 0.826,
"finance": 0.122,
"technology": 0.032,
"medical": 0.021
},
"answer_confidence": 0.826
}
}
}
```

The model selected criteria: legal with 82.6% probability.

To be sure of the categorization, I included documents outside the four domains, like cooking recipes and a poem. These fell below a predefined confidence threshold and were classified as uncategorized rather than being forced into one of the available domains.

This is one of the most useful properties of the approach: the probability provides a basis for deciding when to accept a classification and when to escalate it.

## Multiple decisions in one call

Document categorization use cases often need several labels, for example, which domain, document type, sensitivity and complexity. Multiple typed questions can be sent together, with each producing its own probability distribution.

The quality of these decisions depends heavily on how the instructions and criteria are written. The model evaluates each option against the descriptions provided, so ambiguous criteria can lead to ambiguous classifications.

There is also a latency trade-off when adding more questions. Classification of documents over four dimensions, domain, type, sensitivity and complexity took roughly 3–4x longer than domain categorizing alone.

Document | Domain only | Four dimensions | Increase |
|---|---|---|---|
Legal | 856 ms | 3,461 ms | ~4.0× |
Medical | 897 ms | 3,854 ms | ~4.3× |
Finance | 1,219 ms | 4,126 ms | ~3.4× |

## Handling long documents

Decision models can process long documents by splitting the input into sections, scoring each section and then aggregating the results into a final answer. The aggregation depends on the question type:

Choice and score: The most confident section determines the answer.

Yes/No: One sufficiently confident section can produce a "yes."

This means the way a question is framed matters for document-wide checks. For example, asking "Is this compliant with policy X?" can produce a misleading result if one section looks compliant. Reframing it as "Does this contain anything that violates policy X?" works better because a single violation is sufficient to answer yes.

While experimenting with Laya, I also tried replacing its token-based chunking with custom sentence-based chunking, so that sections contained complete sentences rather than ending at arbitrary token boundaries. The classifications stayed the same, while the number of sections and latency both dropped by about 40%.

Approach | Sections | Latency |
|---|---|---|
Laya's own chunking | 235 | ~5 seconds |
Sentence-based chunking | 138 | ~3 seconds |

Effective chunking can also improve categorization by preserving complete context within each section.

## Benchmarking: How it compared with Claude Sonnet

To evaluate document categorization accuracy and latency, I benchmarked Laya against Claude Sonnet using six technical documents across various industries. A confidence threshold of 0.55 was used for Laya.

Document | Label | Laya | Claude Sonnet |
|---|---|---|---|
Doc 1 | transportation_and_logistics | ✓ (0.553) | ✓ |
Doc 2 | pharma_and_healthcare | ✓ (0.664) | ✓ |
Doc 3 | financial_services | ✓ (0.586) | ✓ |
Doc 4 | retail | ✓ (0.600) | ✓ |
Doc 5 | insurance | ✗ (0.106) | ✓ |
Doc 6 | retail | ✓ (0.615) | ✗ |

Both models got 5 of 6 right. Mean latency was 1.72 s for Laya and 1.45 s for Claude Sonnet.

The important difference is not just the accuracy. Laya also returned a probability distribution over the allowed choices, giving an explicit uncertainty signal that can be used for thresholding or human review.

This is an early signal, but it suggests that a decision model can be competitive with a generative LLM for this type of constrained classification task.

## Final insights on Laya and decision models

Document categorization is fundamentally a decision problem, making decision models a natural fit. They provide constrained outputs and explicit probabilities without requiring output parsing.

The initial Laya exploration showed promising results, including comparable accuracy to Claude Sonnet on a small test and useful uncertainty signals. The main considerations are clear criteria for reliable decisions, latency as the number of questions and document length increase and effective chunking for long documents.

Within the Research team, we regularly investigate emerging models and technologies across various practical scenarios. The current research was part of a two-day time-boxed exploration with a concrete use case.
