---
source: "https://github.blog/changelog/2026-10-01-actions-runner-controller-release-0-15-0"
title: "Actions Runner Controller release 0.15.0"
author: "Allison"
date_published: "2026-10-01"
date_clipped: "2026-10-02"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Actions Runner Controller release 0.15.0

# Actions Runner Controller release 0.15.0

GitHub Actions Runner Controller 0.15.0 includes reliability, scalability, and observability improvements for runner scale sets.

These updates help you operate larger runner fleets with fewer disruptions during upgrades and Kubernetes API updates. Here’s what’s now available:

- Patch version upgrades now update resources in place, reducing disruption between autoscaling runner sets and ephemeral runner sets.
- Controller shutdown behavior is more reliable because
`terminationGracePeriodSeconds`

is configurable and now aligns with the controller manager graceful shutdown timeout. - Runner scale sets can be reregistered when the recorded scale set no longer exists in the Actions service.
- Controller updates now use patch requests instead of full update requests, reducing Kubernetes API payload size.
- Runner status aggregation has moved to metrics for
`EphemeralRunnerSet`

and`AutoscalingRunnerSet`

, reducing status patch requests. - Listener Kubernetes client rate limits are configurable through QPS and burst settings.
- Controller concurrency can now be configured globally and per controller with
`max-concurrent-reconciles`

flags. - Controllers now filter incoming events so they perform fewer reconciliations than before.
- Ephemeral runners are deleted faster because the server-side check for runner removal is skipped when the runner pod successfully exits.

These changes are especially useful for clusters with many runner scale sets where controller throughput, graceful shutdown, and accurate metrics are important for day-to-day operations.

Learn more in the [Actions Runner Controller documentation](https://docs.github.com/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller).
