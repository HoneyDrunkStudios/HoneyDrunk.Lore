---
source: "https://www.thoughtworks.com/insights/blog/why-a-language-model-misses-fraud-in-your-transaction-data"
title: "Why a language model misses fraud in your transaction data"
author: "Nathan Hilt"
date_published: "2026-11-06"
date_clipped: "2026-11-08"
category: "Software Architecture"
source_type: "rss"
---

# Why a language model misses fraud in your transaction data

- [AI and ML](https://www.thoughtworks.com/machine-learning-artifical-intelligence)
- [Data strategy](https://www.thoughtworks.com/insights/topic/data-strategy)
- [Blog](https://www.thoughtworks.com/insights/blog)

By 

[Nathan Hilt](https://www.thoughtworks.com/profiles/n/nathan-hilt)

Published: November 06, 2026

Ask a general-purpose AI model to review a batch of credit card transactions for fraud, and it will give you an answer. It has read enormous amounts of English, so it can describe patterns and flag odd timing. However, it can't natively understand what a transaction is. A purchase at 2 AM, from a new device, in a city the customer has never visited carries a specific meaning in the grammar of money, and a model trained on language has no native way to read it.

That gap between fluency in language and fluency in transactions was the working problem at a Thoughtworks, AWS and NVIDIA breakfast at [Sibos 2026](https://www.thoughtworks.com/about-us/events/thoughtworks-at-sibos-2026) and it's  two model architectures, transaction foundation models (TFM) and graph neural networks (GNN), address it from different angles, and both are moving toward production in financial services.

## Two views of the same fraud

A transaction foundation model is trained specifically on transaction events.  It has the relevant context. It learns that a purchase, a transfer or a login is a step in a sequence with its own grammar: velocity, timing, merchant category and device history. Reading a sequence of events is a different skill from reading a sentence, and it explains why a general model pointed at raw transaction data returns surface-level flags. Because the TFM learns from the full sequence, it can tell when a purchase breaks an entity’s established pattern, such as a new device at 2 a.m. after months of daytime spending on a familiar one.

A graph neural network models customers, devices, merchants and cards as nodes connected by edges representing shared attributes or transactions. Each node "learns" from its neighbours through message passing, which we talk about in [GNNs: Modernizing fraud prevention in financial services](https://www.thoughtworks.com/en-us/insights/articles/graph-neural-networks-in-fraud-prevention). That structure is built to catch coordinated, network-based fraud (such as mule rings and synthetic identity clusters) that looks individually normal but becomes statistically improbable once you can see the group.

The distinction that matters for architects: a TFM captures behavioural and temporal patterns within one entity's history. A GNN captures relational patterns between entities. One reads a customer's story over time. The other reads the company that the customer keeps. Neither replaces the other, and the institutions moving fastest are combining both into one shared context layer.

## Early proof points from the market

Large players are already building transaction models. [Mastercard's Large Transaction Model](https://www.mastercard.com/us/en/news-and-trends/stories/2026/mastercard-new-generative-ai-model.html), built with NVIDIA and Databricks, is positioned as an insights engine spanning fraud, cybersecurity and personalization. [Revolut's PRAGMA model](https://resources.nvidia.com/en-us-financial-services-industry/revolut-builds-a-transaction-foundation-model-1185435), trained on 24 billion events and 207 billion tokens across 111 countries, improved external fraud recall by 64.7% and  lifted product recommendation by 40.5% from one pre-trained backbone. [Adyen Uplift](https://www.adyen.com/press-and-media/adyen-uplift-launch) reported an 86% reduction in manual risk rules across 60 enterprise pilots.

At the breakfast, Pahal Patangia, global payments industry leader at NVIDIA named the context problem most institutions face, it isn't a shortage of AI capability: "Your enterprise context is sitting in your proprietary warehouses, which is not available to the most popular large language models out there, and that's the key." Fine-tuning models on an institution's own proprietary transaction history lets it learn that institution's fraud, risk and routing patterns.

## Data readiness comes first

At the Sibos 2026 breakfast, Brian Blanchard of Thoughtworks ran the same batch of transactions through a general AI model and then through one grounded in transaction context, using Claude as the model in both cases. The first pass produced a vague, pattern-level read. The second came back with a structured risk breakdown across the batch and a specific, actionable count of transactions warranting immediate review.

Getting to that second result requires structuring data in stages. A raw layer brings sources together.  A second layer gives every field, including "risk score" and "merchant category," one consistent, semantic definition that every downstream model shares.

As Paul Chang, head of payment networks at AWS noted, the first real question every institution asks is how much historical data they need to start: "typically, we recommend twenty-five months of data; that's all you need to get started." That's a meaningfully lower bar than the multi-year data-readiness timelines that have historically stalled these programmes.

## Build governance into the pipeline

Regulators will ask how a fraud decision was reached, so the audit trail belongs in the pipeline from the start. That means a record of every question a model was asked and every answer it gave, clear limits on what data each model can access and the ability to reconstruct how a decision was made. A fraud model that can't explain itself is unlikely to clear production review, however accurate it looks in a demo.

## Next steps

Our article [The power of transaction foundation models](https://www.thoughtworks.com/en-us/insights/articles/power-of-transaction-foundation-models-building-the-unified-intelligence-layer-for-payments) covers the use cases, maturity map and build process for a shared transaction intelligence layer.

For a hands-on starting point, NVIDIA’s [Build Your Own Transaction Foundation Model](https://build.nvidia.com/nvidia/build-your-own-transaction-foundation-model) blueprint gives developers a way to start building.

The [AWS Payments on the Cloud eBook](https://pages.awscloud.com/GLOBAL-multi-DL-Payments-on-the-Cloud-eBook-2026-learn.html) covers how payments organizations are moving from siloed fraud models to layered, instant defenses that use embeddings, graph analytics and agentic workflows.

Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.
