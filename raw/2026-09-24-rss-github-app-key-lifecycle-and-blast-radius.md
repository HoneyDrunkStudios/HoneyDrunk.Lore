---
source: "https://blog.gitguardian.com/github-app-private-keys-leaked/"
title: "GitHub App Private Keys: 474 Leaked Keys Still Work"
author: "Gaetan Ferry"
date_published: "2026-09-22"
date_clipped: "2026-09-24"
category: "Security & Ethical Hacking"
source_type: "rss"
capture_method: "attributed-summary"
discovered_via: "https://tldr.tech/infosec/2026-09-24"
---

# GitHub App Private Keys: 474 Leaked Keys Still Work

Attributed summary of the fetched article.

GitGuardian reports that 474 of 4,802 tested exposed keys still authenticated as 440 GitHub Apps. Its tested sample was selected from GitHub-related contexts with nearby App identifiers, not a random sample of all Apps. Permissions and installation scope determined the possible impact.

The central distinction is between a long-lived App private key and the short-lived tokens it can mint. Removing a leaked file or waiting for an individual token to expire does not remove the signing authority. Forgotten internal automation and abandoned integrations can retain access long after their original purpose ends.

HoneyDrunk application: inventory App owners, installations, repository scopes, and key rotation procedures; revoke compromised keys and remove unused integrations. Include public leak monitoring in credential hygiene. Source confidence: first-party security research with disclosed sampling limits; its findings do not establish compromise of HoneyDrunk.

Source: [Original article](https://blog.gitguardian.com/github-app-private-keys-leaked/).
