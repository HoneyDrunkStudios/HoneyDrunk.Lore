---
source: "https://developers.googleblog.com/optimizing-a-200000-line-python-codebase-overnight-with-gemini-4-argon"
title: "Optimizing a 200,000-line Python codebase overnight with Gemini 4 Argon"
author: "George Weale; Bo Yang; Andrew Biernat"
date_published: "2026-10-13"
date_clipped: "2026-10-18"
category: "AI / LLM Research & Tooling"
source_type: "rss"
---

# Optimizing a 200,000-line Python codebase overnight with Gemini 4 Argon

![banner_option_1_no_four](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/banner_option_1_no_four.original.png)

When a new model launches, most demos show greenfield apps built from an empty folder. They're fun to watch. They also tell a working software engineer very little about how the model handles an existing codebase.

For the launch of Gemini 4 Argon, we wanted to test whether it could run unattended overnight on a much harder problem: finding and fixing cross-file performance bottlenecks in [google/adk-python](https://github.com/google/adk-python). Agent Development Kit (ADK) is Google's open-source framework for building and deploying enterprise agents.

The Python repository spans roughly 205,000 lines of code across nearly 800 source files, backed by nearly 17,000 unit tests.

Performance work is a hard test for a model because you can't just open one file and spot the slowdown. You have to look orthogonally to where the symptom appears and hold a map of how the entire codebase fits together over a long run.

This post walks through the prompts, [.agents/skills](https://github.com/google/adk-python/tree/main/.agents/skills) rulefiles, and human code-review decisions from the 11-hour overnight run that cut ADK's in-memory session prep time by about 40% in long sessions and sped up cold package imports by 21%. You'll see the two optimizations that shipped, the four we rejected in review, and how to set up the same overnight workflow on your own codebase.

![image1](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/image1_RanesVB.original.png)

Figure 1: ADK's overhead before the first model request, measured after 50 and 150 turns. Argon's change cuts it by about 40% at both points, so the time saved grows as the session gets longer.

## **Steering the run with .agents/skills and /goal mode**

Most performance work with a coding agent still runs in a tight human loop: an engineer runs a profiler, points the model at a single hot function, and specifies the fix. We wanted to see what Argon would do when given only the outcome the team cared about.

In round one, we tested Argon with zero custom repository instructions. We gave it this single-paragraph prompt:

> Make ADK add no noticeable overhead to any agent:  
> at startup, in long sessions, in multi-agent and  
> workflow setups. Keep what the model receives and  
> the public API unchanged, and back each change  
> with a test that would catch a regression.

Round one ran for about two hours. Argon wrote a benchmark script 7 minutes in, spent 70 minutes measuring and reading code before editing a single line of ADK source, and found real bottlenecks in session copying and package imports. Parts of round one's code made it into the [final commit](https://github.com/google/adk-python/commit/1754b3eeb6cdb2c16e3b30619a12066623df132e) we shipped.

Where round one fell short was maintainer conventions. Because Argon didn't know how the ADK team reviews code, it attached a custom hook to ADK's authentication model that subtly altered its public JSON schema, missed mock event edge cases in its custom copier, ran only 216 nearby unit tests, and left benchmark numbers out of its pull request description.

Round one proved there were real speedups to be had, so we set up a second round with two adjustments. First, we put the team's maintainer guidelines into the repository's [.agents/skills](https://github.com/google/adk-python/tree/main/.agents/skills) directory, like an onboarding guide for a new engineer. Each skill starts with a short `SKILL.md` index that points to focused `references/` files on demand, so we don't flood the agent's context window on every turn. When Argon started its run at 9:11 PM (Figure 2), it read `visibility.md` for our private `_-prefixed` module rule and `imports.md` for our lazy-loading checks before touching a line of code.

![image2](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/image2_KO83oXE.original.png)

Figure 2: Argon's two-hour first run compared with its 11-hour overnight run on the same goal. Round 1 found real speedups on its own, while Round 2 followed repo conventions, ran all 16,892 unit tests, and opened a review-ready pull request.

Second, we turned on /goal mode in [Google Antigravity](https://antigravity.google/docs/enterprise/), which preserves the goal across context compactions so the agent keeps running until the task is finished. We also added two sentences asking for an unmerged pull request with before-and-after numbers:

> /goal Make ADK add no noticeable overhead to any agent:  
> at startup, in long sessions, in multi-agent and workflow setups.  
>  Keep what the model receives and the public API unchanged, and back each change with a test that would catch a regression.  
>  Open one pull request against main that the ADK maintainers would approve, with before and after numbers in its description. Don't merge it.

With .agents/skills in the repo and /goal mode active, Argon ran unattended for 11 hours overnight (Figure 3).

![image3](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/image3_LbilGNt.original.png)

Figure 3: Argon's overnight ADK run in Google Antigravity. The /goal prompt stays pinned at the top and bottom of the window while finished work collapses into summary blocks, so the original rules stay in view across hours of edits, benchmarks, and test runs. (Screenshot replayed in the public Antigravity interface to remove internal workspace details.)

## **6 proposals led to 2 shipped changes after code review**

Looking at the overnight session log the next morning, a few behaviors stood out right away. Before touching source code, Argon read 12 guideline files and ran a baseline benchmark across four test workloads: package startup, a 200-step conversation, a test app where 20 sub-agents hand tasks to one another, and a 12-node workflow, run 30 times. Even three minutes before finishing its 11-hour run, Argon was still auditing its own diff, catching a bug in its own multi-agent cache and rerunning all 16,892 unit tests before stopping on its own.

More importantly, Argon did the cross-module legwork a profiler can't do for you. A profiler will tell you that copying sessions and importing packages take time. What it won't do is trace every caller, mock target, and shared reference across 40 files so that speeding up those paths doesn't break existing apps.

In total, Argon's pull request proposed six optimizations across 32 files. Two of those optimizations solved ADK's core bottlenecks cleanly and shipped to production:

### **1. Filtering in-memory session history before copying**

Every step in an ADK run starts by loading the conversation history. Previously, ADK's in-memory session service deep-copied the entire stored conversation on every read before filtering down to the events a caller asked for. Even listing sessions without their events copied every event first. Argon updated the service to filter events before copying, and replaced Pydantic's generic deep-copy path on sessions and events with a fast, cycle-safe copier that preserves shared state dictionaries and test mocks.

### **2. Loading heavy packages only when needed**

Running `import google.adk` previously pulled in modules for live audio and video streaming, OpenTelemetry tracing, and web servers (FastAPI and Starlette) even for a basic text agent. Simply deleting top-level imports in a framework breaks downstream tests that mock attributes directly on modules. When Argon's round-two pull request removed three internal flow imports from `llm_agent.py`, all 16,892 open-source tests passed, yet 25 internal Google test targets failed because they patched those exact attributes. The shipped fix uses lazy module accessors so heavy packages load only on first use while every public attribute stays patchable where tests expect it.

What about the other four optimizations Argon proposed?

We found that the model comes up with creative solutions we wouldn’t have considered otherwise. Some of those creative ideas run into framework rules where breaking changes are not acceptable.

![image3](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/image3_kMOO2hx.original.png)

Figure 4: The six optimizations in Argon's morning pull request, split between the two we shipped and the four we cut in code review. We kept the session-copy and lazy-import changes that cut real overhead cleanly, and dropped the four that relied on fragile state, private library internals, or synthetic-only gains.

During code review, we rejected the other four changes:

* A multi-agent event cache sped up a synthetic benchmark by 17%, yet relied on a weak memory reference that could return stale data across sessions if Python reused a memory address after garbage collection.
* A telemetry check read a private attribute on OpenTelemetry's tracer implementation, which could break silently on a minor library upgrade.
* A rewrite of how ADK formats conversation history before each model call made a core code path harder to read without moving end-to-end latency on our independent holdout benchmark.
* A lookup index for workflow event replays added state-tracking complexity that only helped synthetic replay tests rather than everyday agent runs.

That division of labor is why the workflow worked: **the agent explores, the maintainer subtracts**. We combined the best parts of rounds one and two into a 22-file change backed by 17 new test functions. After review across the ADK team, it landed in main with the commit note "Argon generated these changes."

## **Benchmark results: what a "turn" is in ADK, and why 158 turns matters**

To make sense of the numbers in the commit message, it helps to know what ADK calls a turn.

When an engineer types a prompt and gets a final answer back, ADK calls that an invocation. A turn is an internal step under the hood every time the agent acts: calling a tool, running a batch of parallel tool calls, or querying an MCP server.

The reason you use an agent framework is multi-turn tool calling, where dozens or hundreds of internal turns happen underneath a run.

Before either round ran we wrote an independent holdout benchmark (bench\_turn.py) that Argon never saw. In bench\_turn.py, a single session grows turn by turn against an instant model and instant tools, so every millisecond on the clock is ADK's own framework overhead. Each turn runs three rounds of four parallel tool calls before returning its answer, timing 5 turns after 0, 50, and 150 earlier turns. Each number below is the median of 6 to 12 runs, and on every turn the model receives byte-identical requests before and after the change.

We tested the merged commit against the previous release across five benchmarks (Figure 5):

![05_figure5_benchmark_results](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/05_figure5_benchmark_results.original.png)

Figure 5: Median ADK framework overhead before and after Argon's changes across all five holdout benchmarks. Session preparation drops by about 40% in long sessions and package import time drops by 21%, while new-process time to first request stays flat because deferred modules load on the first turn.

How to read these numbers for your own agents:

* The 21% faster import google.adk helps every ADK user right away, speeding up CLI commands, local development, and test discovery. Because deferred modules still load when an agent runs its first turn, time from a brand-new process to its first model request stays flat (3.07 s to 3.09 s). On a production server, send a warm-up request before taking live traffic so the first user call doesn't pay that one-time import cost.
* The 40% reduction in pre-model overhead applies to `InMemorySessionService`, which powers `InMemoryRunner`, local evaluation loops, CI test suites, and default Cloud Run or GKE deployments when no external database URI is configured. On a single LLM call that takes seconds, a human won't feel 28 ms or 78 ms. Across 158 internal turns of tool calling interactions, however, those copies compound: removing them **cuts the full 158-turn run from 65.6 seconds to 56.1 seconds** (nearly 10 seconds of pure framework overhead). External database, SQLite, Gemini platform, Firestore, and Redis session stores deserialize from storage rather than deep-copying in memory, so their read times don't change here.

## **Try Gemini 4 Argon**

Enterprise developers and builders can access Argon via API in [Gemini platform](https://console.cloud.google.com/agent-platform/studio/multimodal;mode=prompt?model=gemini-4-argon&region=global) under model ID `gemini-4-argon`, in [Google AI Studio](https://aistudio.google.com/), and in [Google Antigravity](https://antigravity.google/docs/enterprise/).

Review the [model card](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-argon) and [developer guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-argon) for complete technical specifications, token limits, and migration instructions.

## **Try the optimized ADK**

* [Python Quickstart for ADK](https://google.github.io/adk-docs/get-started/quickstart/)
* Review the [merged pull request and benchmark commit](https://github.com/google/adk-python/commit/1754b3eeb6cdb2c16e3b30619a12066623df132e) directly in [google/adk-python](https://github.com/google/adk-python).
* Copy the [.agents/skills layout](https://github.com/google/adk-python/tree/main/.agents/skills) in google/adk-python if you want to give agents your repo's architectural rules and CI checks before an unattended run.
