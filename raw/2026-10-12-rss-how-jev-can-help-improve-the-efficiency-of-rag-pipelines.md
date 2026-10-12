---
source: "https://www.thoughtworks.com/insights/blog/generative-ai/how-jev-can-help-improve-the-efficiency-of-rag-pipelines"
title: "How Jev can help improve the efficiency of RAG pipelines"
author: "Jayanth Penumarthi"
date_published: "2026-10-06"
date_clipped: "2026-10-12"
category: "Software Architecture"
source_type: "rss"
---

# How Jev can help improve the efficiency of RAG pipelines

Retrieval augmented generation is a useful technique for improving LLM outputs, but a RAG pipeline can accumulate decisions and model calls in a way that impacts performance. Recently I traced a user question through a RAG platform we’re building for a client and found the model was called a huge number of times even before a user sees an answer. In fact, only one call wrote a sentence a person would actually read; the rest were decisions.

This realization got me thinking about a model that’s currently flavor of the month: Jev. What’s interesting about Jev is that it is a decision model, not an LLM. It doesn’t output text, it outputs structured probabilities that guide decision making. More specifically, Jev offers three kinds of answers: a choice from a list, a score and what TypeSafe calls a Noul, which is a yes-or-no probability. Because you fix the possible outputs before the call runs, the model can't return something your code doesn't expect.

Given the mechanics and design of Jev, I wanted to explore how it could help improve our RAG pipeline.

## Where decisions pile up in a RAG pipeline

## 

Before we get into how Jev can help, let’s first identify where small decisions pile up in a RAG pipeline.

* **Ingestion.** Before a document enters the system, you need to know what it is. Is it a policy document, a claim form or a contract? Does it contain sensitive data? For a knowledge graph, which entity type does each extracted item belong to? These are all choice questions, and they run on every document, so speed and cost add up fast.
* **Before retrieval.** This is where routing lives: the system needs to select the right store, decide if the query needs rewriting and then flag questions that need no retrieval. If we could skip retrieval for those queries, that could help us a lot in terms of efficiency.
* **After retrieval.** Reranking is a natural fit for the score type. Instead of asking an LLM to judge 20 chunks one by one, you score them all in parallel and keep the top ones. Then comes a question most pipelines skip: do we have enough context to answer? A yes-or-no probability here lets you retrieve again or tell the user "I don't know" instead of letting the LLM guess.
* **After generation.** Once the LLM writes an answer, you can split it into claims and ask, for each one, whether the retrieved chunks support it. Unsupported claims get flagged or removed before the user sees them.

Only one step in that list needs to generate language: writing the final answer. While that can stay with the LLM, everything else is a candidate for Jev.

## How Jev can help

The pattern for using Jev is the same at every step in the RAG pipeline. You describe the input, ask one question and then provide Jev with the answers it's allowed to choose from. Jev can also answer several questions about the same input in a single call.

Here's how that plays out across the pipeline:

* **For ingestion, use a choice.** Ask "What type of document is this?" with options such as policy document, claim form, contract or other. Alongside this, ask a yes-or-no question: does this document contain sensitive data? The answers will go straight into the document's metadata, which means your retrieval filters can use them later.
* **Why Jev?** This step runs on every document, often thousands a day. A fast call that can only return one of your labels beats an LLM writing labels you then have to clean up.

* **Before retrieval, use a choice and a yes-or-no question.** Ask Jev where the query should go: vector store, knowledge graph, both or no retrieval needed. Then ask whether the query needs rewriting before search. If Jev picks "no retrieval needed" with high confidence, you can send the query straight to the LLM.

* **Why Jev?** Routing sits in front of every user question, so any delay here is a delay for everyone. A decision that comes back in a fraction of a second keeps the whole pipeline responsive.

* **After retrieval, use a score, then a yes-or-no.** Send each retrieved chunk with the query and ask how relevant it is. Score all 20 chunks in parallel and keep the top five. Then ask one more question about the chunks you kept: is this enough to answer the query? If the probability is low, retrieve again with a rewritten query or tell the user you don't know.

* **Why Jev?** Reranking with an LLM means either 20 slow calls or one long prompt with an answer that's hard to parse. Scores are numbers your code can sort, compare and log.

* **After generation, use a yes-or-no for each claim.** Split the LLM's answer into individual claims. A simple sentence splitter is usually enough. For each claim, ask whether the retrieved chunks support it, then flag or remove anything below your threshold before the answer reaches the user.

* **Why Jev?** A grounding check only helps if you run it on every answer, and that's only realistic when each check is fast and cheap.

In every case, Jev will deliver a probability and an answer. That's what makes the next part possible.

## Use the probability, not just the answer

The real value of Jev here isn't just speed; It's that every answer comes with a number you can act on.

I implemented a simple framework:

* Above 0.9, act on the decision automatically.
* Between 0.6 and 0.9, fall back to the LLM for a second opinion.
* Below 0.6, send it for human review or return a safe default.

This keeps the cheaper and more lightweight model on the easy majority of cases and saves the expensive model for the hard ones. What’s more, you can tune the bands with real data rather than guesswork.

This is particularly important when you’re using RAG in highly regulated settings. "The model was 94% confident this document is sensitive, and our threshold is 90%" is an audit trail. "The LLM said so" is absolutely not. Using Jev allowed us to log every probability, chart it and then alert us when it drifts.

This is what it looks like to rewire your systems for agents in practice. Not bigger models everywhere, but the right model for each decision.

## Things to watch out for when implementing Jev

Jev is new. This means there are some things that are important to consider. A degree of caution is required. For instance, at the time of writing (early October 2026), Jev remains in early access; published benchmarks come from TypeSafe itself and independent results are only starting to appear. It's also a proprietary hosted model. This means that if you’re working in a regulated field, such as financial services, data residency and vendor risk will certainly be issues that need to be addressed before any pilot.

Aside from those issues, it’s worth noting that Jev only works as well as the answer options you give it. Jev isn’t generative and so won’t hallucinate, but a badly designed list of choices will still produce confident wrong answers. So, when Jev says 80%, check that it's right about 80% of the time on your own data. It also doesn't explain itself: when a decision needs a written reason an LLM is a more suitable option.

These points aren’t intended to warn you off Jev, it’s more to say that you shouldn’t go ahead and rip out a working pipeline. Instead, I’d recommend picking one high-volume, low-risk decision, such as query routing, and run Jev next to the current LLM call, comparing the results for a few weeks.

## Deciding, not thinking

For two years, we've asked one kind of model to do every job in our RAG systems. What I like about Jev is that it reminds us that most of that work isn't thinking, it's deciding.

If you’re able to design for that subtly but important distinction, and you’ll get something that’s far better than impressive AI. You’ll get AI that works.
