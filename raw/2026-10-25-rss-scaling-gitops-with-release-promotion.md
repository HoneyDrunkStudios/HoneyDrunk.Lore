---
source: "https://cloudnativenow.com/contributed-content/scaling-gitops-with-release-promotion"
title: "Scaling GitOps With Release Promotion"
author: "Jesse Suen"
date_published: "2026-10-20"
date_clipped: "2026-10-25"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-10-23"
---

# Scaling GitOps With Release Promotion

## TL;DR — Key Takeaways

* Fleet scale changes the risk: GitOps workflows that reliably serve a few clusters can become difficult to manage across hundreds when a single merge triggers fleet-wide deployment.
* Synchronization isn’t promotion: Tools that distribute configurations and sequence rollouts don’t necessarily provide complete release tracking, verification history and promotion decisions.
* Controlled rollouts build confidence: Staged promotion lets teams validate changes against smaller cluster groups, halt failed releases and prevent problems from spreading across the fleet.

A GitOps pipeline that works reliably at five clusters, or even twenty, starts to make engineers hesitate once the number of clusters hits about fifty. Here’s how it shows up: An engineer who trusts the change still won’t hit merge.

Most teams respond by chasing a faster, more reliable way to roll the change out to every cluster in the fleet. As fleets grow, ordering rollouts is only part of the challenge. Teams also need to know which version is running where, what checks it has passed, and where it can go next.

[![Techstrong Gang Youtube](https://securityboulevard.com/wp-content/uploads/2024/12/Techstrong-Gang-Youtube-PodcastV2-770.png)](https://youtu.be/Fojn5NFwaw8)

### What it Looks Like From Inside a Large Fleet

A platform engineer I spoke with recently led a fleet built around dedicated, single-tenant environments, spread across multiple clouds — over 200 production clusters in total. Their GitOps setup was conventional: A merge to the main branch synced everywhere. That’s a reasonable design at five clusters.

At hundreds of clusters, a merge became what the engineer described as a fleet-wide event with no gate in between. The entire release process rested on a single replica environment catching failures before the change reached every cluster, and validating a release in that environment took weeks. Once triggered, propagation took about an hour.

No gate exists between merge and full fleet.

### Speed Doesn’t Fix the Ordering Problem

The change took about an hour to reach the fleet, but the team spent weeks validating it beforehand. Most teams try to remedy this by spreading changes faster and more reliably, but that doesn’t help the validation problem. CI built and tested the release. A GitOps controller synced it. In this setup, neither layer controlled when a release could advance to the next group of clusters.

Broadcast reaches every cluster at once; staged promotion gates each wave on the last.

Whatever fills that gap has to do more than decide what happens next. What mattered most to the engineer I spoke with wasn’t an easy-to-use interface: it was a fleet legible enough to show, at any moment, which version was running where, how it got there, and what was allowed to happen next.

That’s the bar a real promotion layer has to clear.

### What Promotion Adds to Staged Rollouts

ApplicationSets, Rancher Fleet, OCM, and Karmada solve a real problem: Getting the same configuration onto many clusters without hand-writing a manifest per cluster. Several of them go further, rolling a change out in waves and pausing when clusters become unhealthy: ApplicationSet Progressive Syncs, Rancher Fleet’s rollout partitions, and OCM’s progressive ManifestWorkReplicaSet strategies all work this way.

These tools already provide rollout sequencing and checks. A complete promotion workflow also needs to track a specific release, retain its verification results, and determine where it can go next. Teams need to understand how much of that workflow their existing tools provide and what they still have to build.

### Promotion is Becoming its Own Layer

The team managing 200 clusters needed a way to deploy to a few, check the results, and decide whether to continue. With no gates between merge and the full fleet, every release depended on catching problems beforehand.

I’ve spent the past decade building GitOps tooling, and I expect promotion to become a standard part of the delivery stack. Sync tools will keep getting faster and more reliable. Alongside them, teams will need a system that tracks each release, records the checks it has passed, and controls where it can go next. Git will still hold the desired state, with each group of clusters advancing to a new version when the release meets its requirements.

At a thousand clusters, those decisions need to be visible. Engineers should be able to see which version is running where and why a rollout has stopped. If verification fails in one group, the remaining clusters should stay on the previous version while the team investigates. That gives teams room to learn from a release before committing the whole fleet to it.

Before your next fleet-wide rollout, choose a small group of clusters to go first. Define what needs to pass before the next group updates, and test that a failed check actually stops the release from spreading further.
