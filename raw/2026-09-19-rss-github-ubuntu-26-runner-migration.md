---
source: "https://github.blog/changelog/2026-09-17-ubuntu-26-generally-available-and-latest-migration"
title: "Ubuntu 26 generally available and latest migration"
author: "Allison"
date_published: "2026-09-17"
date_clipped: "2026-09-19"
category: "DevOps & CI/CD"
source_type: "rss"
capture_format: "attributed-summary"
---

# Ubuntu 26 generally available and latest migration

Source: [Ubuntu 26 generally available and latest migration](https://github.blog/changelog/2026-09-17-ubuntu-26-generally-available-and-latest-migration)

*Attributed summary of the fetched written article; not a verbatim reproduction.*

GitHub announces production support for Ubuntu 26.04 hosted runners on x64 and arm64. Workflows can select ubuntu-26.04 or ubuntu-26.04-arm explicitly.

The announcement schedules migration of ubuntu-latest from Ubuntu 24.04 to 26.04 between October 19 and November 19, 2026. Changes to installed packages and tool versions may break workflows that depend on the previous image.

GitHub recommends testing against the explicit new image before migration. Workflows that need more preparation can pin ubuntu-24.04 temporarily. The runner image inventory is the reference for installed software and removed components.

HoneyDrunk implication: inventory uses of ubuntu-latest, test representative .NET and container jobs against the new label, and make image transitions deliberate. The durable lesson is to separate operating-system migration from application changes so failures can be attributed and rollback remains straightforward. The rollout dates are the announcement's schedule as captured.
