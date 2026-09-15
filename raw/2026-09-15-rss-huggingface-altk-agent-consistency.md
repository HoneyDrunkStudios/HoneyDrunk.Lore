---
source: "https://huggingface.co/blog/ibm-research/altk-evolve-consistency"
title: "Your Agent Aced the Task. Will It Do It Again?"
author: "Evelyn Duesterwald; Lilian Ngweta; Vatche Isahagian; Jayaram Radhakrishnan; Vinod Muthusamy; Gaodan Fang; Ashwath Vaithinathan Aravindan; Punleuk Oum; G Thomas; Merve Unuvar; Ayhan Sebin; Michał Ulewicz"
date_published: "2026-09-15"
date_clipped: "2026-09-15"
category: "AI / LLM Research & Tooling"
source_type: "rss"
capture_format: "attributed-summary"
extraction_status: "full written page fetched; readable body reviewed"
---

# Your Agent Aced the Task. Will It Do It Again?

Source: [Your Agent Aced the Task. Will It Do It Again?](https://huggingface.co/blog/ibm-research/altk-evolve-consistency)

## Attributed content summary

IBM Research distinguishes average agent accuracy from repeatability. Mean@k averages success across repeated runs; Pass^k requires every run of a task to succeed, while Pass@k requires only one success.

On 168 AppWorld tasks, its GPT-4.1 ReAct baseline reportedly achieved 77.4% Mean@5 but only 53.0% Pass^5. ALTK-Evolve's Consistency Analyzer resamples decisions from a recorded trajectory, identifies unstable choices, and generates reusable guidance without rerunning tool interactions. With those guidelines, the reported figures rose to 81.0% and 69.0%, respectively.

The portable evaluation practice is to report repeated-run reliability alongside average success, inspect difficult task segments, and test whether guidance transfers to related tasks. The authors report variability even at temperature zero.

Evidence limit: these are the authors' benchmark results, not independent validation or a production reliability guarantee. Offline decision resampling adds model-call cost and does not establish that every downstream action is safe.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
