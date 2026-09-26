---
source: "https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/"
title: "Node 20 is no longer available in GitHub Actions"
author: "Allison"
date_published: "2026-09-23"
date_clipped: "2026-09-24"
category: "DevOps & CI/CD"
source_type: "rss"
capture_method: "attributed-summary"
---

# Node 20 is no longer available in GitHub Actions

Attributed summary of the fetched article.

GitHub reports that Actions runners now use Node 24 for JavaScript actions and no longer provide the temporary Node 20 opt-out. Action maintainers should update their runtime declaration and publish a compatible release; workflow owners should adopt compatible action versions.

The announcement identifies macOS 13.4 and earlier and ARM32 as unsupported for the new action runtime. Its stated service scope is github.com and GitHub with Data Residency.

HoneyDrunk application: inventory JavaScript action versions, custom action runtime declarations, and self-hosted runner platforms. Validate a representative workflow after upgrades. Keep the action execution runtime distinct from any Node version installed for building the application itself. Source confidence: official platform migration notice; this capture records the announced September cutover rather than predicting future runner behavior.

Source: [Original article](https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/).
