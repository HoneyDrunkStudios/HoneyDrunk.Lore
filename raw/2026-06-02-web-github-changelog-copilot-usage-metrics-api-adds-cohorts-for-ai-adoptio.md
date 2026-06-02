---
source: "https://github.blog/changelog/2026-05-29-copilot-usage-metrics-api-adds-cohorts-for-ai-adoption"
title: "Copilot usage metrics API adds cohorts for AI adoption"
author: "GitHub Changelog"
date_published: "2026-05-29"
date_clipped: "2026-06-02"
category: "Developer Tooling & AI Coding"
source_type: "web"
---

# Copilot usage metrics API adds cohorts for AI adoption

Source: https://github.blog/changelog/2026-05-29-copilot-usage-metrics-api-adds-cohorts-for-ai-adoption

Back to changelog 
Improvement 
May 29, 2026 •
2 minute read 
Copilot usage metrics API adds cohorts for AI adoption 
Table of Contents 
What's new 
Why this matters 
Important notes 
Menu. Currently selected: What's new 
What's new 
Why this matters 
Important notes 
To help you tell a deeper Copilot adoption story—not just who is active, but how they’re using Copilot—the Copilot usage metrics API now classifies each engaged user into an AI adoption phase based on their Copilot product usage over a rolling 28-day window. A new ai_adoption_phase field is available on user-level reports, and a new totals_by_ai_adoption_phase array surfaces per-phase metrics on enterprise- and organization-level reports.
What’s new 
Each engaged user is assigned to one of four phases based on the Copilot surfaces they’ve used on at least two days in the last 28-day window:
Phase 0 — No cohort : User did not meet the engagement criteria for any phase. 
Phase 1 — Code first : User engaged with code completion and/or IDE agent mode. 
Phase 2 — Agent first : User engaged with a single GitHub-based agent surface (i.e., Copilot cloud agent, Copilot code review, or Copilot CLI). 
Phase 3 — Multi-agent : User engaged with two or more GitHub-based agent surfaces, or with the new GitHub Copilot app. 
Each ai_adoption_phase value includes a version field (starting at v1 ) so the classification logic can evolve as Copilot’s product surface grows, without breaking historical context.
On the enterprise- and organization-level reports, the new totals_by_ai_adoption_phase array groups engagement and activity metrics by phase, including:
Total engaged users (2-day-in-28 engagement window) 
User-initiated interaction average 
Code generation and acceptance activity averages 
Lines of code added and deleted averages 
Pull requests created, merged, and reviewed averages 
Median time-to-merge average 
Aggregated metrics report the average per user within each phase rather than the sum.
Why this matters 
Tell the maturity story: Move beyond simple active-user counts and show which Copilot capabilities your developers are actually adopting. 
Track cohort progression: Watch users graduate from code-first usage into agent-first and multi-agent workflows over time. 
Target enablement: Focus training, documentation, and rollout programs on the phases where you see the biggest opportunity. 
Important notes 
These metrics are available to enterprise administrators and organization owners who have access to Copilot usage metrics through the REST API. 
You can use this release in combination with the teams filter ship for greater granularity. 
Join the discussion within GitHub Community .
Table of Contents 
What's new 
Why this matters 
Important notes 
Menu. Currently selected: What's new 
What's new 
Why this matters 
Important notes 
account management 
copilot 
enterprise management tools 
Share 
Copied 
Shared 
Back to changelog
