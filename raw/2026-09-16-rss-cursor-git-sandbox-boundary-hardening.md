---
source: "https://accomplish.ai/blog/beltdown2-escaping-the-cursor-cli-sandbox/"
title: "Beltdown2: Escaping the Cursor CLI sandbox"
author: "Or Hiltch"
date_published: "2026-09-12"
date_clipped: "2026-09-16"
category: "Security & Ethical Hacking"
source_type: "rss"
capture_format: "attributed-summary"
discovered_via: "https://tldr.tech/infosec/2026-09-16"
---

# Beltdown2: Escaping the Cursor CLI sandbox

Source: [Beltdown2: Escaping the Cursor CLI sandbox](https://accomplish.ai/blog/beltdown2-escaping-the-cursor-cli-sandbox/)

## Attributed content summary

Accomplish reports a Cursor CLI macOS sandbox escape involving an attacker-prepared workspace containing executable Git configuration. Although the shell tool was confined, the harness's own background Git commands ran outside that boundary and honored a repository-supplied filesystem-monitor hook. A read-only agent request was sufficient in the reported test.

The researchers distinguish this prepared-archive path from an ordinary clone and state that they did not test a separate clone-delivery variant for Cursor. They report that build 2026.08.04-aaa8809 introduced centralized Git hardening and that repeated tests no longer triggered the hook.

The architectural lesson is to inventory every subprocess path, including indexing and status collection, rather than treating the visible shell tool as the whole attack surface. Centralized restrictions on executable Git configuration or confinement inherited by all child processes reduce missed-call-site risks.

This capture records the researchers' tested scope and reported fix, not a claim that current Cursor versions remain vulnerable or that one mitigation covers every sandbox-escape class.

Capture note: Paraphrased from the fetched written source; not a full-text reproduction.
