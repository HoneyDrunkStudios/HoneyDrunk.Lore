---
source: "https://www.thoughtworks.com/insights/articles/rebuilding-self-hosted-github-actions-runners-on-aks"
title: "The 14 GB cold-start problem: Rebuilding self-hosted GitHub Actions runners on Azure Kubernetes Service"
author: "Renicius Pagotto Fostaini"
date_published: "2026-10-28"
date_clipped: "2026-10-28"
category: "Azure & Cloud"
source_type: "rss"
---

# The 14 GB cold-start problem: Rebuilding self-hosted GitHub Actions runners on Azure Kubernetes Service

Source: https://www.thoughtworks.com/insights/articles/rebuilding-self-hosted-github-actions-runners-on-aks

*How a platform team reduced Windows build times with ephemeral runners, image caching and prebuilt toolchains*

## The slowest part of delivery was not always the code

For a team of about 20 developers working on a large content platform, getting feedback from a CI/CD pipeline could take around 40 minutes. The problem wasn't necessarily the build itself. Jobs competed for resources on a small pool of shared Windows virtual machines (VMs), while provisioning new environments introduced additional delays.

The platform supported more than 100 external websites and relied on two or three static Windows VMs for its build workloads. When the team began migrating from Azure Pipelines to GitHub Actions, it had an opportunity to rethink how build capacity was provisioned rather than reproduce the same constraints on new infrastructure.

## Why the existing runner pool had reached its limits

The original setup used Azure Pipelines with self-hosted runners on two or three static Azure virtual machines shared by a team of about 20 developers. The applications depended on .NET Framework, which constrained the build environment to Windows and made the hosts heavier to provision and maintain than a simple Linux runner.

Builds competed for CPU, memory and disk I/O on the same machines. Adding permanent Windows VMs could increase capacity, but it also meant more machines to patch and manage and more always-on cost. Moving to larger VMs would add resources without isolating one job from another. When the team began moving workflows to GitHub Actions, it treated the transition as a chance to address the underlying bottleneck rather than reproduce the old runner model on new infrastructure.

## The first improvement exposed a different bottleneck

The team evaluated serverless container options, including Azure Container Instances and Azure Container Apps. In its implementation, the disposable execution environments enabled more parallel work and reduced the reported pipeline duration from about 40 minutes to about 30 minutes. But each new environment also lost the local image cache.

The Windows container image used by the build was approximately 14 GB. The team reported that pulling it on a cold start could take 5–10 minutes. That meant a design that scaled execution more flexibly could still spend a meaningful share of each run waiting for the same large image. The team needed isolated, on-demand runners that could reuse the large build image.

## Using AKS and ARC to make runners disposable

The team moved the runner workload to Azure Kubernetes Service (AKS) and used GitHub Actions Runner Controller (ARC) to manage runner capacity in Kubernetes. In this model, runner jobs execute in dedicated, short-lived pods rather than sharing a long-lived host environment. The platform can scale runner capacity with demand, up to its configured limits, and remove a runner after its job completes.

The architecture separates the components that coordinate runner demand from the worker capacity that executes jobs. Lightweight controller and listener components remain available to manage the runner fleet, while the more resource-intensive worker nodes can scale according to workload. This separation gives the platform team a way to tune always-on coordination separately from build compute.

AKS allowed subsequent jobs scheduled on the same worker node to reuse a locally cached image, avoiding another 14 GB download. The project team reported that a cached pull took roughly 10–20 seconds, compared with 5–10 minutes on a cold node. Node lifecycle and cache retention therefore became important performance considerations.

## Treat the cold start as a design choice, not an edge case

A local cache is valuable only while the node that holds it is available. Scaling a worker pool to zero can reduce idle worker compute, but a node that is later recreated may need to download the image again. Teams considering this pattern should measure both sides of the trade-off: the cost of keeping warm capacity and the time and network cost of cold starts.

In the implementation described here, the team used node-level caching and configured the worker pool to scale down during off-hours. It also used ephemeral operating-system disks for high-throughput local storage and image garbage-collection settings to reduce the risk of disk exhaustion. Those choices can help, but they do not make cold starts disappear. The right policy depends on the team’s build schedule, concurrency profile, image size and tolerance for first-run latency.

## Pre-build the toolchain to shorten the feedback loop

The team found another source of avoidable work: some build tools, including Yarn and MSBuild, were installed during pipeline execution. It moved those tools into a custom runner image built through a repeatable image pipeline. The image was refreshed on a scheduled cadence so the team could incorporate security updates without relying on manual rebuilds.

The revised image and workflow reportedly brought the total pipeline duration into a 10–15 minute range. Parallel execution reduced contention, caching avoided repeated downloads and pre-installing tools eliminated setup work. The improvement did not come from Kubernetes alone, but from treating the complete path from job request to usable feedback as a system to optimize.

## Make the platform easier to consume than the infrastructure

A runner platform is useful only if product teams can adopt it without becoming Kubernetes operators. The platform team packaged the configuration into reusable GitHub workflows so application teams could use a standard path instead of rebuilding runner logic for every repository.

The implementation also used a scoped GitHub App for runner-platform authentication and Azure Workload Identity for workloads that needed to access Azure resources. These mechanisms reduce reliance on long-lived credentials in the relevant paths. Teams would still need to document how application credentials, GitHub App credentials and runner secrets are provisioned, protected and rotated. “Secretless” should not be used as a blanket description unless every credential path has been verified.

Monitoring and logging across AKS, Azure Monitor, Log Analytics and Dynatrace gave the platform team visibility into node utilization, runner state and failures. These controls help the platform team diagnose capacity limits, failed image updates and stalled runners.

## What changed and what to measure

In this implementation, the project team reported the following outcomes. These figures are specific to this environment, not a guarantee for another one:

|  |  |  |
| --- | --- | --- |
| Measure | Before | Reported after redesign |
| Pipeline duration | About 40 minutes | About 10–15 minutes |
| Runner capacity | 2–3 shared VMs | Configured for up to 50 concurrent runner pods |
| Monthly compute cost | About $975 | About $327 |
| Image pull | 5–10 minutes on a cold start | About 10–20 seconds when the image is cached on the node |

Using the figures in the project draft, the monthly compute comparison is approximately a 66% reduction, or about $7,800 annualized. That comparison is meaningful only if both figures use the same scope and time basis. A configured maximum of 50 pods is a capacity ceiling, not evidence that 50 concurrent jobs were sustained in production. Likewise, a 10–15 minute range should be accompanied by a definition of the measured interval and the test conditions.

## When this pattern may and may not fit

AKS and ephemeral runners can be a good fit when teams have Windows-specific build requirements, variable or high concurrent demand and a platform capability able to own Kubernetes operations, image maintenance, security and observability. The approach is less compelling when job volume is low and predictable, a simpler autoscaling VM model meets the need or the organization cannot support the additional platform components.

Before choosing a design, measure queue time separately from job execution and end-to-end feedback time. Compare cold and warm starts, include the cost of coordination and observability components, and load-test what happens when concurrency reaches the configured maximum. Those measurements make it possible to choose deliberately between a warm cache, lower idle spend and a slower first run.

For teams considering ephemeral runners, the starting point should be their actual workload: how often jobs run, how much time they spend waiting, what needs to be cached and how quickly capacity must become available. Those measurements will help determine whether Kubernetes offers enough benefit to justify the additional operational complexity.
