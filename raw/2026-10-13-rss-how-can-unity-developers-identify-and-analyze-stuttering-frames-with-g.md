---
source: "https://dev.to/gameoptim/how-can-unity-developers-identify-and-analyze-stuttering-frames-with-got-online-5eon"
title: "How Can Unity Developers Identify and Analyze Stuttering Frames with GOT Online?"
author: "GameOptim"
date_published: "2026-10-13"
date_clipped: "2026-10-13"
category: "Game Development / Unity"
source_type: "rss"
---

# How Can Unity Developers Identify and Analyze Stuttering Frames with GOT Online?

# Summary

Identifying the root cause of frame stuttering in Unity games can be time-consuming, especially when developers need to inspect performance data and function call stacks manually. GOT Online's Overview mode now includes a Stutter Analysis feature that automatically identifies stuttering frames and provides detailed function stack statistics for each identified point.

This article explains how stuttering frames are identified in GOT Online, what function stack data is available, and how Unity developers can use this information to investigate performance issues more efficiently.

# Introduction

Frame stuttering can negatively affect the gameplay experience, but identifying its root cause requires more than simply observing a drop in frame rate. Developers need to determine which frames experienced significant delays and investigate the function calls responsible for the additional execution time.

To make this process more efficient, GameOptim has introduced Stutter Analysis in GOT Online's Overview mode, incorporating feedback from development teams. The feature identifies stuttering frames during gameplay and provides detailed function stack statistics to help developers investigate the underlying causes.

## What Qualifies as a Stuttering Frame in GOT Online?

GOT Online's Stutter Analysis feature identifies frames that meet both of the following conditions:

* The current frame time exceeds 83.33 ms.
* The current frame time exceeds twice the average frame time of the previous three frames.

A frame must satisfy both conditions to be classified as a stuttering frame.

By applying these criteria, GOT Online lists the identified stuttering frames in a dedicated Stutter Analysis section on the Overview report page. Developers can use this list to quickly locate frames that experienced significant delays during execution.

[Image: Stutter Analysis section in the GOT Online Overview report](https://uploader.shimo.im/f/wYylBgfFa0ARVQzn.png)

## What Function Stack Data Is Available for Each Stuttering Point?

Identifying a stuttering frame is only the first step. Developers also need to investigate which function calls contributed to the delay.

GOT Online provides detailed function stack statistics for the relevant nodes associated with each stuttering point. The available information includes:

* Execution time percentage: The proportion of time attributed to a function or node.
* Execution time: The specific time consumed.
* Call count: The number of times the function was called.

These metrics help developers examine the execution costs associated with abnormal nodes and investigate the function stacks behind a stuttering frame.

[Image: Function stack statistics for a stuttering point in GOT Online](https://uploader.shimo.im/f/ZwrdQMQIX3y9kgyQ.png)

## How Can Developers Use Stutter Analysis to Investigate Performance Issues?

GOT Online allows developers to switch quickly between different stuttering points and inspect the corresponding function stacks.

This workflow helps development teams move from identifying a frame-time anomaly to examining the detailed execution data associated with that specific point.

Rather than investigating every frame manually, developers can focus on the identified stuttering frames, compare the relevant function stack information, and use execution time, time percentage, and call count to investigate potential causes.

The function stack data provides a more detailed basis for determining which parts of execution warrant further investigation, helping developers locate the specific causes of stuttering more efficiently.

## How Does Stutter Analysis Fit into the GOT Online Overview Workflow?

Stutter Analysis is integrated directly into the Overview report in GOT Online. Developers can review the list of stuttering frames and inspect the corresponding function stack statistics within the same reporting workflow.

This integration connects two important stages of performance investigation:

1. Identify abnormal frames: Locate frames that meet the stuttering criteria.
2. Inspect execution details: Examine function stack statistics at each stuttering point to investigate the cause.

By bringing these capabilities together, GOT Online helps streamline the process of moving from frame-time anomalies to detailed performance analysis.

# What Should Unity Developers Take Away?

* Check both stuttering criteria: A frame must exceed 83.33 ms and twice the average frame time of the previous three frames.
* Start with the identified frames: Use the Stutter Analysis section in the GOT Online Overview report to locate stuttering points.
* Inspect function stack statistics: Examine execution time percentage, execution time, and call count for relevant nodes.
* Compare different stuttering points: Switch between identified frames to investigate their corresponding function stacks.
* Use detailed execution data to guide investigation: Move beyond identifying frame-time anomalies and investigate the specific causes through function stack analysis.

# FAQ

### Q1. What is considered a stuttering frame in GOT Online?

A frame is classified as a stuttering frame when its frame time exceeds 83.33 ms and is more than twice the average frame time of the previous three frames. Both conditions must be met.

### Q2. Where can I find stuttering frames in GOT Online?

Stuttering frames are listed in the Stutter Analysis section of the Overview report in the latest version that includes this feature.

### Q3. What information does GOT Online provide for each stuttering point?

GOT Online provides detailed function stack statistics, including execution time percentage, specific execution time, and call count, helping developers investigate the execution costs associated with abnormal nodes.

### Q4. How can developers investigate the causes of stuttering?

Developers can switch between different stuttering points and inspect their corresponding function stacks. By examining execution time, time percentage, and call count, they can investigate which function calls may be contributing to the observed delays.

### Q5. Is Stutter Analysis available in GOT Online's Overview mode?

Yes. GameOptim has introduced Stutter Analysis in GOT Online's Overview mode, adding a dedicated section for identified stuttering frames and their associated function stack statistics.
