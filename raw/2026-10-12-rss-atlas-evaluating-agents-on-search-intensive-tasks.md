---
source: "https://exa.ai/blog/atlas-benchmark"
title: "ATLAS: Evaluating Agents on Search-Intensive Tasks"
author: "Alexander Goldberg; Joshua Ahn; Scott Langille"
date_published: "2026-10-08"
date_clipped: "2026-10-12"
category: "AI / LLM Research & Tooling"
source_type: "rss"
discovered_via: "https://tldr.tech/ai/2026-10-09"
---

# ATLAS: Evaluating Agents on Search-Intensive Tasks

Today we’re previewing **ATLAS**, a new benchmark designed to grade the accuracy and completeness of agent responses to challenging real-world workflows that heavily utilize web search. ATLAS pairs queries grounded in real search demand with verified golden answers, using an automated pipeline that lets us refresh both as the web and models evolve.

Some of our takeaways from our runs of ATLAS to date:

* Comprehensive search at a reasonable cost is far from solved. Max-effort search agents consistently outperformed their lower-compute counterparts, but no agent run costing less than $1 per task achieved a row F1 over 0.5.
* Even the most expensive search agents miss about 1/3 of the golden results, indicating substantial room for web search to improve performance in use cases where completeness is critical.
* When holding the model harness fixed, Exa defines the cost-performance Pareto frontier, with scores ranging 16% across different search backends.

**Figure 1:** Quality vs. cost for agentic searchers. No cost-efficient searcher comes close to solving exhaustive search tasks.

## [#](https://exa.ai/blog/atlas-benchmark#what-does-a-good-benchmark-look-like)What does a good benchmark look like?

When language models first started using web search, they would often get stuck managing long contexts or reasoning across multiple documents. Even the order of search results could throw them off. In short, agentic search was bottlenecked by intelligence. Now, frontier models handle these tasks much more reliably and at a fraction of the cost, so the bottleneck to completing deep and wide research tasks is whether your search backend can actually find relevant information in the world.

Recent bake-offs between agentic search configurations[1](https://exa.ai/blog/atlas-benchmark#citation-1),[2](https://exa.ai/blog/atlas-benchmark#citation-2),[3](https://exa.ai/blog/atlas-benchmark#citation-3),[4](https://exa.ai/blog/atlas-benchmark#citation-4) reflect the increasingly urgent need to rigorously evaluate web search efficacy. These evaluations seek to elucidate which combinations of harness, model, and search provider work best on challenging and economically valuable research tasks.

To support rigorous comparisons, we think an agentic search benchmark should:

1. **Require search.** Answers must depend upon retrieving information from sources beyond what models already have memorized.
2. **Reward search quality and effort.** High-quality search results and additional search volume should meaningfully improve scores.
3. **Represent real-world search tasks.** Tasks must reflect what humans and agents actually search for.

| Benchmark | Released | Tasks | Memorized | Saturated | Grading cost |
| --- | --- | --- | --- | --- | --- |
| BrowseComp [[5]](https://exa.ai/blog/atlas-benchmark#citation-5) | Apr 2025 | 1,266 | 48% | ✓ | $26 |
| WideSearch [[6]](https://exa.ai/blog/atlas-benchmark#citation-6) | Aug 2025 | 200 | 59% | ✓ | $80 |
| DeepSearchQA [[7]](https://exa.ai/blog/atlas-benchmark#citation-7) | Jan 2026 | 900 | 61% | ✓ | $16 |
| WANDR [[4]](https://exa.ai/blog/atlas-benchmark#citation-4) | Jul 2026 | 500 | unmeasurable | ✗ | $18k–50k |
| ATLAS (ours) | Oct 2026 | 547 | 9% | ✗ | $2 |

**Table 1:** Memorization is calculated as the percent of tasks recalled by at least one of GPT-6 Astra, GPT-5.6 Sol, or Claude Opus 5. WANDR cannot directly measure memorization because it has no fixed answer key against which to score a model’s response without search. Grading cost refers to the cost to grade 10 full runs using the official grader.

These requirements may sound obvious, but today’s popular agentic-search benchmarks each fail one or more of them. BrowseComp[5](https://exa.ai/blog/atlas-benchmark#citation-5), WideSearch[6](https://exa.ai/blog/atlas-benchmark#citation-6) and DeepSearchQA[7](https://exa.ai/blog/atlas-benchmark#citation-7) are largely memorized and close to saturated. Many of their questions are contrived and written to be hard to find rather than to reflect what people search for. Newer benchmarks such as Perplexity’s WANDR[4](https://exa.ai/blog/atlas-benchmark#citation-4),[12](https://exa.ai/blog/atlas-benchmark#citation-12) stay fresh by grading with an LLM judge, which makes runs expensive to grade and highly sensitive to grader design (e.g., what provider is used for the grader’s web fetch tool).

These benchmarks tend to lose value over time as search providers optimize for them and the knowledge they require gets added to the latest frontier models. These issues are all downstream of the fundamental challenge that building new, high-quality search evals is slow and expensive. Therefore, agentic search benchmarks often go stale faster than they are replaced with fresh, up-to-date ones.

## [#](https://exa.ai/blog/atlas-benchmark#designing-atlas)Designing ATLAS

We address these shortcomings with a new benchmark, **ATLAS** (**A**gentic **T**asks for **L**arge **A**ggregation + **S**earch), consisting of 547 deep and wide research tasks. Tasks are generated from seed topics drawn from clustering of anonymized search demand. Each task asks a system to discover every entity (e.g. a person, place or company) that meets precise conditions, and then to enrich each entity with 2–10 multi-hop attributes.

**Figure 2:** How an ATLAS task grows from a seed topic into a golden answer table.

Following a growing trend of synthetically generated benchmark data[8](https://exa.ai/blog/atlas-benchmark#citation-8),[9](https://exa.ai/blog/atlas-benchmark#citation-9),[10](https://exa.ai/blog/atlas-benchmark#citation-10), we expend extensive inference-time compute within a structured pipeline to generate tasks and golden answers. Our pipeline includes a committee of frontier models and search providers which spend a median of 8 agent-hours and 1,200 searches per task to find answers, independently verify them against sources, and resolve disagreements or ambiguities until confident in their correctness. Because the pipeline is automated, we can regenerate the ATLAS dataset using topics based on recent search trends, keeping the benchmark aligned with what agents actually search for as the web updates.

Given the large amount of inference-time compute deployed at eval generation time, the challenge we pose for this benchmark is *efficient search*: solve each task in under a minute and for under $1, a budget at which no current system reaches even 0.5 row F1.

## [#](https://exa.ai/blog/atlas-benchmark#the-results)Results

Based on a suite of ablations and experiments, we believe that ATLAS rectifies the multitude of flaws present in current popular agentic search evals, providing a benchmark that truly measures search and distinguishes various systems by search quality and effort.

ATLAS strongly differentiates search providers:††Each metric is an F1: the harmonic mean of *precision* (share of returned units that are correct) and *recall* (share of gold units returned). They differ only in the unit counted:
**Discovery F1:** entities.  
**Row F1** (headline): whole rows, correct only if every cell is.  
**Item F1:** individual cells, covering discovery and enrichment.

Model

![Row F1 against median cost per task (agent + search, log scale) for a fixed GPT-6 Luna harness with Exa auto and fast, Perplexity, OpenAI, Brave, and Parallel advanced and fast search](https://exa.ai/images/blog/atlas-benchmark-search-apis-luna-row.png)

**Figure 3:** With the harness fixed, the search API alone strongly impacts performance. Every search API runs in the same neutral Scout harness, with GPT-6 Luna or Claude Haiku 5.5 as the model.

### [#](https://exa.ai/blog/atlas-benchmark#atlas-rewards-search-quality)ATLAS rewards search quality

ATLAS depends on search quality far more than existing benchmarks: when we severely degrade the quality of search by hiding the top 7 of every 10 search results, the same searcher loses roughly half of its ATLAS score. In contrast, on BrowseComp, WideSearch and DeepSearchQA, the searcher retains 81–89% of its original score, indicating that these benchmarks do not actually measure search quality.

**Figure 4:** Degraded search hurts ATLAS far more than other benchmarks. We synthetically degrade search quality: on every Exa search the top k of 10 results are censored and results k+1 to 10 returned. Results are shown for GPT-5.6 Luna with Exa search in the neutral [Scout harness](https://github.com/exa-labs/benchmarks/blob/master/harness/scout.py).

### [#](https://exa.ai/blog/atlas-benchmark#atlas-is-unmemorized)ATLAS is unmemorized

We measure memorization of evals by checking the percent of tasks whose full answer set is recalled by at least one of GPT-6 Astra, GPT-5.6 Sol, or Claude Opus 5. Nearly 50% or more of BrowseComp, WideSearch, and DeepSearchQA are memorized (Table 1).

In contrast, ATLAS’s older rows are less memorized than WideSearch’s, and it includes fresh information past current frontier model knowledge cutoffs, where frontier models almost never answer correctly without search. As a result, adding search to frontier models gives a much bigger lift in performance over a no-search baseline than current popular evals (Figure 5).

**Figure 5:** ATLAS is largely unmemorized. (a) WideSearch is far more memorized than ATLAS such that there is barely any lift from search. (b) Share of gold rows that at least one of three closed-book models (Claude Opus 5, GPT-5.6 Sol, GPT-6 Astra) finds, by when the row became publicly knowable. Older ATLAS rows are often niche, and therefore less memorized, and recent ones are almost never recalled. Unlike Table 1, which counts whole tasks, (b) counts individual rows.

### [#](https://exa.ai/blog/atlas-benchmark#atlas-requires-wide-and-deep-search)ATLAS requires wide and deep search

74% of ATLAS’s tasks ask for 10 or more entities, and each entity needs 2–10 attributes. Moreover, these wide and deep tables actually require multi-hop searches as opposed to retrieval from a single URL or domain. We estimate, based on our dataset construction logs, that discovery of entities requires a median of 4 different domains per task and full discovery + enrichment requires a median of 18 different domains per task. In contrast, many popular existing evals nominally require width or depth but can actually be solved with very few retrieval steps due to memorization, contamination, or flawed benchmark design. For example, in our experiments we find that on WideSearch, a strong agent cites a single website for 48% of its tasks, against 0.2% on ATLAS.

Both the width and depth of ATLAS make it difficult. We find that increasing both makes tasks harder for all searchers tested.

**Figure 6:** Wider and deeper tasks are harder. (a) Row F1 by the number of gold rows to discover in the task. (b) Share of found rows that are fully correct, by the number of columns to enrich.

## [#](https://exa.ai/blog/atlas-benchmark#construction-and-validation)Construction and validation

**Figure 7:** Frontier agents build each task in a custom harness over five stages, spending a median of 8 agent-hours and about 1,200 searches. Every stage checks its output item by item and adaptively repairs it, through additional research or by refining the task’s specification.

Two agents from different model families do the construction: Codex with GPT-6 Astra and Claude Code with Opus 5.5. Single-agent steps (screening, verification and repair) use GPT-6 Astra. To ensure the gold is not biased towards any one search index, every agent searches through a provider-neutral tool we built. The tool calls Exa, Brave and Perplexity search APIs on each query and returns one interleaved list with provider names hidden. We found that the golden table construction agents cited pages sourced from different providers at near-equal rates.

### [#](https://exa.ai/blog/atlas-benchmark#1-topic-seeding)1. Topic seeding

Each task starts from a topic in Exa’s aggregate, anonymized search demand. Seeding from real demand spreads ATLAS across more than 300 topics and increases the likelihood that proposed tasks are unmemorized. An agent proposes a task from the topic with a few searches. Before construction starts, a cheap screener agent probes the task and rejects tasks that either clearly do not have information available online or are memorized.

### [#](https://exa.ai/blog/atlas-benchmark#2-entity-discovery)2. Entity discovery

Finding a set that is exhaustively enumerable yet unmemorized proved to be challenging, so we built the set first in its own generation stage. The two construction agents search independently over several passes to construct a golden list of entities. A verifier agent then point-wise checks every row, including its cited pages, with additional searches on a separate index (OpenAI’s). Any unsettled rows go to targeted repair, where a repair agent makes additional searches or clarifies the task to remove ambiguity.

### [#](https://exa.ai/blog/atlas-benchmark#3-row-enrichment)3. Row enrichment

After the discovery entity list is established, an agent proposes enrichment columns. The two construction agents fill every cell independently, saving each value with a page citation and a verbatim quote. Verification, repair and a final checker (GPT-5.6 Sol) then settle any disagreements. Cells that cannot be settled are left ungraded in the final eval, which accounts for 7.1% of cells across all tables. Additionally, 3.8% of cells are *blanks*, where our agents can show that no data exists for the value in question, e.g. the event asked for did not happen or there is conclusively no public record. These blanks are graded, testing a searcher agent’s ability to infer that specific information does not exist or is not applicable to a given entity.

### [#](https://exa.ai/blog/atlas-benchmark#4-stress-test)4. Stress test

Twelve systems attempt every task: Exa Agent[11](https://exa.ai/blog/atlas-benchmark#citation-11) at four effort levels; Claude Opus 5.5 and GPT-6 Astra, each at two effort levels, with their providers’ native search; and GPT-5.6 Luna with Exa, Perplexity, Brave and Parallel search.

### [#](https://exa.ai/blog/atlas-benchmark#5-audit)5. Audit

Blind judges research every disagreement with the key. Based on a sampled audit with live browser use, we estimate that under 1% of gold values are incorrect (0.9%, 95% CI 0.6–1.4%). The audit judges are Codex (Astra) and Claude Code (Opus 5.5) with Gemini 3.1 Pro breaking ties, all using their native search. If there’s still disagreement after this step, Exa engineers manually adjudicate the differences.

### [#](https://exa.ai/blog/atlas-benchmark#6-answer-key)6. Answer key

Rows that survive the audit become part of the golden answer key. Ungraded and blank cells are permitted.

**Figure 8:** Diverse task topics. Each task is derived from a precise subcategory within one of the above 23 categories, sourced from search trends.

## [#](https://exa.ai/blog/atlas-benchmark#grading)Grading

We grade returned tables against golden answers using three F1 metrics, computed per task and averaged over tasks. Each F1 is the harmonic mean of precision and recall, but the three differ in what they count, similar to metrics used in WideSearch[6](https://exa.ai/blog/atlas-benchmark#citation-6):

* **Discovery F1** counts just row discovery: *precision* = % of returned rows that name a gold entity, and *recall* = % of all gold entities returned.
* **Item F1** counts cells, including both discovery and enrichment: *precision* = % of returned cells that are correct, and *recall* = % of all gold cells returned correctly.
* **Row F1** counts rows, where a row is correct only when every cell in the row is: *precision* = % of returned rows that are fully correct, and *recall* = % of gold rows returned fully correct. This is our headline metric.

The grader aligns returned rows to the key by entity name and a set of aliases, falling back to an LLM aligner (GPT-6 Luna) on misses. It then scores each cell deterministically where possible, with an LLM judge (GPT-6 Luna) adjudicating the remaining 4.5% of cells. Blank cells earn credit only when left empty, while ungraded cells are excluded. Grading is both cheap and consistent: grading one system on all 547 tasks costs ~$0.24, and regrading the same 7,658 answers (547 tasks from each of 14 agent runs) gave the same row F1 on about 7,550 of them (98.6%) and moved no system’s mean row F1 by more than 0.001.

|  | ATLAS | WANDR\*\*We quote the most cost-efficient WANDR judge we have built internally at Exa. |
| --- | --- | --- |
| Graded against | fixed, audited answer key | rubric and re-fetched pages |
| Cost per graded answer | $0.0004 | $0.88 |
| Grading time per answer | 15 s | 7.6 min |
| Cells decided by an LLM | 4.5% | every record |
| Completeness checked against a full set | ✓ | ✗ |

**Table 2:** Grading scalability overview. Due to the ease and scalability of our grading, ATLAS serves as a much more effective benchmark for developing cost-effective but powerful agentic searchers.

## [#](https://exa.ai/blog/atlas-benchmark#driving-future-innovation)Driving future innovation

We believe that ATLAS provides a much more faithful signal than existing benchmarks of which agentic search configurations actually work on hard, economically valuable research. As reflected in initial runs on ATLAS, efficient agentic search remains far from solved: the best system we tested reaches 0.66 row F1 only with a budget of $8.92 and 18 minutes per task, and no system under $1 gets even half the rows correct.

Exa will continue to push the frontier of efficient search toward solving wide and deep research at low latency and cost. We view ATLAS as a first step toward a new generation of continuously refreshed search evals, and we hope it helps measure progress on the workflows for which people actually rely on agentic web search. We will be releasing the tasks, golden tables and grader in the coming weeks along with full technical detail and plan to regenerate ATLAS from fresh demand every 3–6 months.

## [#](https://exa.ai/blog/atlas-benchmark#citation)Citation

```
@online{exa2026atlas,


author = {Alexander Goldberg and Joshua Ahn and Scott Langille},


title = {{ATLAS: Evaluating Agents on Search-Intensive Tasks}},


date = {2026-10-08},


url = {https://exa.ai/blog/atlas-benchmark}


}
```
