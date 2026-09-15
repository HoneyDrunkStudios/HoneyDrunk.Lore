---
source: "https://www.harness.io/blog/catch-ai-regressions-before-they-ship-with-ai-evals-in-ci-cd"
title: "Catch AI Regressions Before They Ship with AI Evals in CI/CD"
author: "Shibam Dhar"
date_published: "2026-09-02"
date_clipped: "2026-09-14"
category: "DevOps & CI/CD"
source_type: "rss"
capture_mode: "attributed-summary"
content_note: "Substantive summary of the fetched readable article; not a verbatim full-text archive."
discovered_via: "https://tldr.tech/devops/2026-09-14"
---

# Catch AI Regressions Before They Ship with AI Evals in CI/CD

Source: [Catch AI Regressions Before They Ship with AI Evals in CI/CD](https://www.harness.io/blog/catch-ai-regressions-before-they-ship-with-ai-evals-in-ci-cd)

## Attributed article summary

Harness demonstrates a blocking AI evaluation step alongside build and deployment stages. A support-agent example uses 32 golden scenarios with answer relevance, task completion, and toxicity measures, plus a fixed 70% passing threshold.

An initial run passed roughly 65% even though the application built and its endpoint worked. Case-level review exposed incorrect knowledge and incomplete answers. Later runs reached 75% and 78% after knowledge and prompt fixes without lowering the threshold.

Repeated runs sometimes produced different outcomes on the same inputs. The article therefore distinguishes real behavioral inconsistency from judge or target infrastructure failures and recommends confirming improvements across multiple evaluations.

HoneyDrunk relevance: make behavioral regression evidence part of release decisions for agents. Keep datasets and thresholds stable while diagnosing failures, inspect individual cases, and select acceptance criteria for the actual workflow. The small vendor demonstration is an implementation example, not evidence that its numerical threshold suits every application.
