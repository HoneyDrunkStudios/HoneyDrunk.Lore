---
source: "https://github.blog/changelog/2026-06-25-actions-steps-can-now-be-run-in-parallel"
title: "Actions steps can now be run in parallel"
author: "GitHub Changelog Actions"
date_published: "2026-06-25"
date_clipped: "2026-06-28"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Actions steps can now be run in parallel

Source: https://github.blog/changelog/2026-06-25-actions-steps-can-now-be-run-in-parallel

Back to changelog 
Improvement 
June 25, 2026 •
1 minute read 
Actions steps can now be run in parallel 
GitHub Actions now supports running steps concurrently using background .
Previously, all steps in a workflow ran in sequence, with each step starting only after the previous step completed. Previously, you could run steps in a non-blocking way using shell backgrounding ( & ), but that often interleaved logs from multiple steps. This new capability enables steps to run in parallel while retaining separate logs and execution.
Four new keywords are being introduced:
background: true runs a step asynchronously and immediately continues to the next step. 
wait / wait-all pauses execution until one or more named background steps complete. wait can target one or more specific background steps, while wait-all pauses until all prior background steps have completed. 
cancel gracefully terminates a background step when you no longer need it, enabling you to start long-running services with a background step. 
parallel takes a group of steps and converts them to background steps with a wait after, enabling you to easily run multiple steps in parallel. This is syntactic sugar for the “run these steps concurrently, then continue” pattern. 
This update helps you handle common patterns in a single job:
Running independent work in true parallel, such as multiple builds at once 
Starting a background service, running dependent work, then stopping that service cleanly 
Kicking off non-blocking work that can continue while later steps run, like uploading telemetry while packaging continues 
Read the GitHub Actions workflow syntax documentation for current syntax and usage details.
actions 
Share 
Copied 
Shared 
Back to changelog
