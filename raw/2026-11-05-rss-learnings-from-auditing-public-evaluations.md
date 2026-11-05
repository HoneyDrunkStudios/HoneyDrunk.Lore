---
source: "https://www.primeintellect.ai/blog/auditing-public-evaluations"
title: "Learnings from Auditing Public Evaluations"
author: "Florian Brand"
date_published: "2026-11-03"
date_clipped: "2026-11-05"
category: "AI / LLM Research & Tooling"
source_type: "rss"
discovered_via: "https://tldr.tech/ai/2026-11-04"
---

# Learnings from Auditing Public Evaluations

Evaluations are the foundation of LLM training, allowing us to put concrete numbers on the capabilities we care about. Public evaluations allow us to build a shared understanding of these capabilities and how different models perform on them, thus providing important insights. They also allow everyone in the community to [scrutinize](https://epoch.ai/benchmarks/search?reviewed=verified&reviewed=flawed&reviewed=not-enough-info) these benchmarks and [propose changes](https://github.com/harbor-framework/terminal-bench/pulls?q=sort%3Aupdated-desc+is%3Apr+state%3Aopen+label%3A%22task+fix%22).

While running popular evaluations reported in model cards, we ran into several issues that affect how results should be interpreted. After applying fixes, some of the benchmarks can be considered saturated. Below, we showcase some of them and discuss the design patterns and reward hacks we observed while running frontier models. We also open-source our fixes for the community to make the evaluation landscape more robust.

## AutomationBench

[**AutomationBench**](https://arxiv.org/pdf/2604.18934) is Zapier’s benchmark for agents completing business workflows that span multiple applications through APIs. Agents have to find the right endpoints themselves and follow business rules.

The agent gets one natural-language task and then works on its own until it finishes, with no further interaction. The environment contains many apps based on real business workflows, such as Gmail, Zoom or Asana. These apps expose different actions that the model has to discover and then apply with a `search` and an `execute` tool.

However, the actions the models can discover with the `search` tool describe their request bodies in prose rather than in JSON Schema, for example:

```
"request": "Body: {text or body (required, string — message text), profile_id (string — recipient profile ID), email (string — recipient email address), profile_url (string — recipient profile URL), recipients (array of person URN strings e.g. ['urn:li:person:{id}']), subject (optional, string — conversation title)}. Provide at least one of profile_id, email, profile_url, or recipients to identify the recipient."
```

In practice, models often struggled with these descriptions and had to make educated guesses about parameters or the allowed combinations of those parameters.

Therefore, we replaced the prose request descriptions with JSON Schemas, which better reflects how these models are used in production:

```
{
  "type": "object",
  "properties": {
    "text": {"type": "string", "minLength": 1},
    "body": {"type": "string", "minLength": 1},
    "profile_id": {"type": "string", "minLength": 1},
    "email": {"type": "string", "minLength": 1},
    "profile_url": {"type": "string", "minLength": 1},
    "recipients": {
      "type": "array",
      "minItems": 1,
      "items": {"type": "string", "minLength": 1}
    },
    "subject": {"type": "string"}
  },
  "allOf": [
    {
      "anyOf": [
        {"type": "object", "required": ["text"]},
        {"type": "object", "required": ["body"]}
      ]
    },
    {
      "anyOf": [
        {"type": "object", "required": ["profile_id"]},
        {"type": "object", "required": ["email"]},
        {"type": "object", "required": ["profile_url"]},
        {"type": "object", "required": ["recipients"]}
      ]
    }
  ],
  "additionalProperties": true
}
```

Furthermore, we fixed the majority of tasks and graders by slightly rewording them and by making unstated requirements in graders more permissive when they could not be reasonably inferred.

After applying these fixes, scores change drastically, with Claude Opus 5.5 @ max scoring 92.15% (strict: 70.83%), while DeepSeek V4.1-Flash 1017 scores 91.61% (strict: 69.50%). These fixes are only applied to the public set, which yields higher scores than the private held-out set.

We also added a mode that registers the tools for each task’s connected services directly with the harness. This more closely reflects how models are used in their respective harnesses in the real world, where users add tens or hundreds of tools. With Prime Agent, this mode boosts scores further.

![AutomationBench scores with tools registered directly in the harness](https://www.primeintellect.ai/blog/auditing-public-evaluations/automationbench-results.png)

Our changes are available in [PI-AutomationBench](https://github.com/xeophon/AutomationBench-PI), with individual fixes documented in the [merged pull requests](https://github.com/xeophon/AutomationBench-PI/pulls?q=is%3Apr+is%3Amerged). However, note that the runs reported by [Zapier](https://zapier.com/benchmarks) use a slightly different mode (`api_fetch`), which preserves the discovery aspect but alters the needed tool calls. Thus, the scores are not directly comparable.

As this benchmark is close to saturation when using partial scoring, we recommend either reporting the strict scores or moving to AutomationBench v1.5, which will be released soon.

## OfficeQA Pro v2

[**OfficeQA Pro v2**](https://huggingface.co/datasets/databricks/officeqa-pro-v2) is Databricks’ grounded reasoning benchmark built on two centuries of U.S. federal financial documents, where most questions require evidence from several sources. It measures how well agents retrieve, parse, and reason across large, unfamiliar document collections.

OfficeQA is graded using a [custom regex- and Python-based extraction and grading script](https://github.com/databricks/officeqa/blob/main/reward.py). In practice, it rejects many valid answers:

- During [this run](https://app.primeintellect.ai/dashboard/evaluations/f7uoq72v3z3nr3750dcyl7sw/traces?episodeId=cc4eb1066d9a4147913b1b830dc13799&traceId=4de576f182ee4398ad030877978ce7bd&idx=0&rolloutIdx=0&sourceIndex=252), DeepSeek V4.1-Flash 1017 answered `FY2014 (fiscal year 2014)`, which is correct, but the answer was rejected because the script rejects answers whose count of extracted numbers differs from the reference, even when the extra numbers repeat or explain the correct answer.
  - The same happened in [this run](https://app.primeintellect.ai/dashboard/evaluations/i7nswpi6whxrl4plbpnwvlsw/traces?episodeId=26e01668b9454459b4896ce9c869d9d0&traceId=a3d888beb8c64eb481b3c333aed34767&idx=0&rolloutIdx=0&sourceIndex=110) for GLM-5.3 and [this one](https://app.primeintellect.ai/dashboard/evaluations/lubq3ve5zzsq3xkyuc2ln9ln/traces?episodeId=b20c1640e78f4d0998059a761daac115&traceId=1a2a2dcdbfcd48d2951a3119725ebf24&idx=0&rolloutIdx=0&sourceIndex=12) for GPT-6.1 Sol.
- On [task 9](https://app.primeintellect.ai/dashboard/evaluations/do32u0yvbucbbue2ekojxfx9/traces?episodeId=0441444a4be44cb5ac950b52299e0c05&traceId=ecb98ddb491b418db6f240f41bf264df&idx=0&rolloutIdx=0&sourceIndex=48), GLM-5.3 includes a short explanation with its answer, which was rejected because it exceeds 250 characters.

We replaced this brittle grading logic with a reference-answer judge, which considerably improves grading accuracy.

OfficeQA Pro v2 also includes general web access, which leads to models retrieving the solutions from Hugging Face, for example [here](https://app.primeintellect.ai/dashboard/evaluations/gxdigmsalsej49yejp44qb9x/traces?episodeId=5577134e43544fd9adb20475e222248d&traceId=850862de030a4957b7d7c0274fb206e9&idx=0&rolloutIdx=0&sourceIndex=198), [here](https://app.primeintellect.ai/dashboard/evaluations/y917wrboz7wr67v41w710bs9/traces?episodeId=f573e8bf9e6e411f92c64e1b42fad9da&traceId=6fa9aad84e4b4a73bfef9ab8a34b04a3&idx=0&rolloutIdx=0&sourceIndex=209) or [here](https://app.primeintellect.ai/dashboard/evaluations/q8ay17wh4jm9uuvfnalcex0v/traces?episodeId=4172f5728ae5435f9d702d93cdf749ad&traceId=b1787ede48c54e8bb0303c1ce79b73ff&idx=0&rolloutIdx=0&sourceIndex=404). The default prompt used by the evaluation encourages the model to spell out its reasoning for the solution, which runs into content filters for Anthropic models. Furthermore, some tasks are ambiguous and can be interpreted in different ways to arrive at different yet valid answers.

[PI OfficeQA Pro v2](https://app.primeintellect.ai/dashboard/environments/primeintellect/pi-officeqa-pro-v2) fixes all these issues. It changes the default prompt, expands the corpus and drops some tasks so it runs entirely without web access. It uses a decision model as the judge instead of the brittle grading script.

![OfficeQA Pro v2 results](https://www.primeintellect.ai/blog/auditing-public-evaluations/officeqa-results.png)

Running current state-of-the-art models reveals that the benchmark is on the verge of becoming saturated, with Opus 5.5 @ max scoring 85.6% (avg@4) using Prime Agent, while DeepSeek V4.1-Flash 1017 reaches 78.8%.

## HLE-Diamond

[HLE-Diamond](https://lastexam.ai/blog/hle-diamond) is a refined 1,000-question subset of Humanity’s Last Exam that measures frontier expert-level knowledge and reasoning. The set is split evenly into 500 reasoning and 500 knowledge questions.

Models can be scored without tools, to test their general knowledge and reasoning capabilities, or with tools (code execution and web fetching). The latter setting is commonly reported in model cards.

Web search is a hard problem for public evaluations, as the answers need to be accessible *somewhere* for the evaluation to exist in the first place. Naturally, people republish the solutions elsewhere, either on the same site (e.g., other Hugging Face datasets), on similar sites and mirrors (like ModelScope) or even on [bespoke sites just to leak the solutions](https://autobenchaudit.com).

A common fix for this problem is a domain blocklist, which blocks access to listed domains at the sandbox level. However, this solution does not scale, as the blocklist would need continuous maintenance against the ever-growing surface of the internet.

To illustrate this point: in [this trace](https://app.primeintellect.ai/dashboard/evaluations/ysx70pbi0gskoi9adg88858f/traces?episodeId=fdd4e1f5cad84058a3636e60fdc7b65c&traceId=f0aa9621acaa4236a05bec2c6929402e&idx=0&rolloutIdx=0&sourceIndex=468), DeepSeek V4.1-Flash 1017 had already worked out its own answer (0.070) when it decided to "try one more avenue: HLE answer in model evaluation logs on `openreward` public API". It went through OpenReward’s public rollout API, found another model’s trajectory on the same question, and read the grader’s verdict: `Correct Answer: 0.011`. It then dropped its own answer, wrote a derivation that works backward to 0.011, and submitted it with 98% confidence.

One approach is to inspect tool outputs with synchronous monitors, which [we support with verifiers, our open-source framework for evals](https://www.primeintellect.ai/blog/verifiers-v1). The monitor is added to every tool call and instructed to check whether the accessed resource leaked the solution. If it did, the output is blocked before it reaches the model and the sandbox, which the interception server added in verifiers v1 makes possible.

![Synchronous monitor intercepting tool outputs](https://www.primeintellect.ai/blog/auditing-public-evaluations/monitor.png)

While adding a monitor on top of the blocklist does catch things that slip past the extensive list of regular expressions implemented [upstream](https://github.com/centerforaisafety/hle/blob/22ed3074b1e7b134bcbc09028d0ba320839b0655/docs/blocklist.json), it is not a silver bullet. Aside from false positives, which hurt scores, we found that the intelligence of the monitor is an important factor in correctly classifying tool calls and, more importantly, in keeping the model under evaluation in check.

The monitor is set up to scrub tool outputs before they reach the model and sandbox by replacing the output with `Tool output omitted. Do not circumvent this filter`. However, we observed models getting increasingly creative in tricking the monitor in order to reach their goal:

- Weak monitors, such as Clef, can be tricked by base64-encoding outputs, for example in [this run](https://app.primeintellect.ai/dashboard/evaluations/etsd66mmhn5m775gr6ir5sep/traces?episodeId=954ef32324c94518adabb3b2b27b5046&traceId=4c62c4ab358a42c586197c7a462c7525&idx=0&rolloutIdx=0&sourceIndex=30).
- The monitor can also be (ab)used to rule out candidate answers: in [this run](https://app.primeintellect.ai/dashboard/evaluations/y4jimw4l8j90eh02l8dvmfwb/traces?episodeId=c9a3bfe225e04cd5b91e7c6f20c73a8f&traceId=a928e4cecc8a4b838e30947865a72a66&idx=0&rolloutIdx=0&sourceIndex=84), Opus 5.5 inferred that the monitor blocks valid solutions (“I think the filter is content-based, so any key that appeared unblocked earlier can't be the answer”).
- The configuration of the monitor matters as well. In our runs, the monitor saw one tool call at a time. V4.1-Flash 1017 then started splitting its actions across multiple tool calls, each of which looked benign to GPT-6.1 Sol, the monitor ([link to the trace](https://app.primeintellect.ai/dashboard/evaluations/qqwhrwnwulku804itjtfpj36/traces?episodeId=58a185d9eaf0420ca144eafa16621203&traceId=cf60ec2ecc844dcea9a1c503a1fb60d7&idx=0&rolloutIdx=0&sourceIndex=75)).

In all these runs, the model under evaluation tricked the monitoring model with increasingly sophisticated methods to get the final reward. To stop this behavior, the ([multi-layered](https://openai.com/index/how-we-detect-frontier-model-misalignment/)) monitoring system must be able to stop evaluation runs if it detects reward hacking. Stopping mid-rollout is not only needed for high-stakes domains such as cyber, but is also cheaper than running a long-horizon evaluation and potentially regrading after the fact.

These runs all used a single model during the evaluation. In multi-agent setups, similar evasion methods could happen across agents: several models could coordinate so that their combined actions change the shared state of the world, while each agent’s individual actions look harmless enough to pass the monitor.

## Conclusion

Designing evaluations for frontier models is hard, because capabilities are advancing quickly. Evaluations with ambiguous prompts, broken graders or setups that allow for reward hacking risk giving a false impression of current capabilities and shortcomings.

This (and other relevant work by the community) also puts those who train models and report evaluations in an awkward position: if a model is able to exploit an evaluation successfully, e.g., by finding the answers with web search, should its score be compared to those of models that exploit less and stay within the intended boundaries?

Answering questions like this, auditing evaluations, and sharing fixes with the community are important, and we intend to keep doing this for the evaluations we care about. If this excites you, [join us!](https://www.primeintellect.ai/careers/7ef14297-51c3-45b1-abe4-890489a0bddb)

```
@article{brand2026auditingpublicevals,
author = {Florian Brand},
title = {Learnings from Auditing Public Evaluations},
journal = {Prime Intellect Blog},
year = {2026},
month = {November},
note = {https://www.primeintellect.ai/blog/auditing-public-evaluations}
}
```
