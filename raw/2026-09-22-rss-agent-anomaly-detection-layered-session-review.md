---
source: "https://developers.googleblog.com/agent-anomaly-detection-now-in-private-preview-on-the-gemini-enterprise-agent-platform"
title: "Agent Anomaly Detection, now in Private Preview on the Gemini Enterprise Agent Platform"
author: "Achuth Narayan Rajagopal"
date_published: "2026-09-16"
date_clipped: "2026-09-22"
category: "Security & Ethical Hacking"
source_type: "rss"
capture_format: "attributed-summary"
---

# Agent Anomaly Detection, now in Private Preview on the Gemini Enterprise Agent Platform

Source: [Agent Anomaly Detection, now in Private Preview on the Gemini Enterprise Agent Platform](https://developers.googleblog.com/agent-anomaly-detection-now-in-private-preview-on-the-gemini-enterprise-agent-platform)

Attributed summary of the fetched written article; not a full reproduction. Source claims have not been independently reproduced.

Google introduces a private-preview oversight service for agents on the Gemini Enterprise Agent Platform using ADK 1.2 or later. It examines existing logs and OpenTelemetry traces to detect suspicious behavior that may still produce a successful-looking response.

A lightweight pass identifies statistical outliers; a reasoning layer examines selected sessions in context. The example follows repeated inventory queries whose aggregate pagination behavior suggests bulk extraction. Findings include an explanation, severity, and probability, and can appear in Security Command Center.

An API allows an ADK callback or plugin to inspect findings and stop subsequent tools or turns according to configured thresholds. Detection therefore needs an explicit connection to enforcement; the article does not demonstrate that every harmful action is blocked before execution.

HoneyDrunk relevance: retain tool arguments and session-level traces, and distinguish behavioral review from task-success metrics. Apply the layered screening pattern with independently measured false positives, detection delay, and enforcement coverage before relying on it for autonomous workflows.
