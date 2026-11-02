---
source: "https://cloudnativenow.com/contributed-content/one-hub-34-clusters-lessons-from-a-gitops-control-plane-at-scale/"
title: "One Hub, 34 Clusters: Lessons From a GitOps Control Plane at Scale"
author: "Nitish Mane"
date_published: "2026-10-27"
date_clipped: "2026-11-02"
category: "Software Architecture"
source_type: "rss"
discovered_url: "https://cloudnativenow.com/contributed-content/one-hub-34-clusters-lessons-from-a-gitops-control-plane-at-scale"
discovered_via: "https://tldr.tech/devops/2026-10-30"
---

# One Hub, 34 Clusters: Lessons From a GitOps Control Plane at Scale

# One Hub, 34 Clusters: Lessons From a GitOps Control Plane at Scale

On Oct. 6, [Red Hat published a walkthrough](https://developers.redhat.com/articles/2026/10/06/declarative-clusters-gitops-deployment-hosted-control-planes-red-hat-openshift) of Argo CD ApplicationSets provisioning hosted control planes straight from Git. A day later, [GitHub had an outage](https://www.githubstatus.com/incidents/djlmxz2zd0j7) that hit Actions, Git operations and pull requests, after smaller incidents on Oct. 5 and 6. Put those together and you have the state of GitOps in 2026. It now manages whole clusters, not just applications, and it depends on a Git layer that is not always there.

Most GitOps advice is written for a handful of clusters. At Lucid Motors I worked on a control plane where one Argo CD instance managed 34 clusters across 22 AWS accounts and one Oracle Cloud tenancy, in five regions on three continents. A single repository of 174 Helm charts rendered 1,214 Argo CD Application objects.

**What the Hub Owns, and What Stays in the Spokes**

The hub ran the only Argo CD instance for platform components. It held the cluster registrations, the Cluster API controller identity and three ApplicationSets: one deploying a per-cluster baseline through an app-of-apps chart, one deploying shared platform services to the clusters that host them, and one holding the Cluster API definitions for the clusters themselves.

The spokes kept what lets them say no. Each spoke’s own authentication config decided whether to admit the hub’s role. Each spoke owned the role that Cluster API used inside it, and its workloads got their cloud roles from the spoke’s own identity provider. On AWS, the hub stored no long-lived cross-account secrets. It received short-lived credentials, and every grant was declared on the spoke side and reviewed in Git. On Oracle Cloud we could not get the same property, and registration there still read a stored credential from a vault. Write down where your model breaks. Ours broke at the second provider.

**The Contract Is the Product**

The change that made the rest manageable was treating each cluster as a small configuration file of about twenty keys. Those keys covered identity, the account boundary, region and environment, how to reach the cluster’s API, delegated DNS and certificates, and opt-outs. Everything else was derived from that file: which Applications it got, its IAM role names, its Cluster API identity, its DNS delegation and its cost tags. Nothing downstream was configured separately.

That made fleet changes cheap. Adding a cluster to a fleet was a label change on its registration. Adding a component to a fleet was one line in a list. Matrix generators did the fan-out.

One of those account boundaries, the Oracle Cloud tenancy, came from a Middle East expansion I owned. It joined the fleet through the same contract rather than as a one-off, which is the real test of whether a contract works.

**Chart Sprawl Is the Real Problem**

At 174 charts, the risk is not Argo CD. It is a values change that renders fine for one cluster and breaks thirty others. Two habits kept it in check.

First, CI rendered everything on every merge request. Each chart had to render on its own. Each app-of-apps chart had to render against every cluster contract. Each cluster definition had to render. Each chart that an Application referenced had to render with the exact values it would receive.

Second, CI rendered the target branch and posted the manifest diff to the merge request. Reviewers looked at what would actually change on clusters, not at template edits.

**Measure Drift, Carefully**

Out-of-band configuration drift went from 24.3 incidents a month before cutover to 0.9 after, over two 90-day windows. The before number came from incident tickets tagged as drift, and tagging was incomplete. The after number came from controller diff events with a confirmed out-of-band cause. The methods differ, so it is not a clean 96% reduction. What it does show is that once drift was instrumented, it was rare, and the controller corrected every case within its reconciliation interval without anyone touching it.

If you can, count drift the same way before and after.

**Design for the Bad Day**

At this scale, a single bad commit is the failure mode to fear most. We restricted Argo CD’s defaults in two places. Every ApplicationSet was configured to preserve deployed resources on deletion, so removing an entry could not trigger their cascading deletion. Cluster objects carried a no-prune setting, so reverting a commit could not delete a running cluster. The principle: reconciliation should be proportional to blast radius and reversibility.

The same thinking applies to outages like GitHub’s. In a hub-and-spoke design, workloads run in the spokes. If Git or the hub is unavailable, existing workloads in the spokes can continue running, even though GitOps-driven deployments and configuration changes are interrupted. The goal is to ensure that a control-plane outage does not become a workload outage. Make the safe failure the one you get for free.

Also treat the hub as the most privileged system you run. A repository or CI compromise has the hub’s reach once a change merges.

**Onboarding Cluster 35**

Bringing a new cluster under management took four steps. Create the IAM roles that match the naming pattern, once, in Terraform. Write the cluster’s values file. Open a merge request so CI renders the whole graph and posts the diff. Merge and label the registration. Older clusters built by hand were adopted in place through an explicit import path.

Mean onboarding went from 4.0 days across eight earlier clusters, reconstructed from change tickets, to 1.7 hours across eleven after cutover, measured from merge to first successful sync. The cutover also removed manual approval steps, so not all of that gain belongs to GitOps. The measurement windows also differed, so these figures should not be treated as a direct comparison. The samples are small. The direction is not in doubt.

**Scale Punishes Shortcuts**

None of this changes GitOps principles. Declare state, review it, let a controller converge on it. What scale changes is how much each shortcut costs you. A credential stored in the hub, a values file nobody renders, a prune setting left on default: at five clusters those are habits. At thirty-four they are incidents waiting for a date.

**About the author:** Nitish Mane is a Software Engineer at Philo, where he builds infrastructure for AI-assisted production operations. He previously worked on platform infrastructure at Lucid Motors, including a large-scale GitOps control plane.
