---
source: "https://grafana.com/blog/bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview"
title: "Bridging Alloy and OpenTelemetry: the OTel engine is now in Public Preview"
author: "Bejal Lewis; Kyle Eckhart"
date_published: "2026-11-03"
date_clipped: "2026-11-08"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-11-04"
---

# Bridging Alloy and OpenTelemetry: the OTel engine is now in Public Preview

[Bejal Lewis](https://grafana.com/author/bejal-lewis?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview),

[Kyle Eckhart](https://grafana.com/author/kyle-eckhart?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview)

•

2026-11-03•9 min

Many Grafana Cloud customers love what Alloy offers them, but we're also seeing a growing base of users who feel the same way about the OpenTelemetry Collector. We want to make it easy for customers to make the decision that makes the most sense, regardless of their preference.

When we [introduced the OpenTelemetry engine for Grafana Alloy](https://grafana.com/blog/native-opentelemetry-inside-alloy-now-you-can-get-the-best-of-both-worlds/?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview&plcmt=in-text), we set out to give teams a way to run native OTLP pipelines without giving up the power and flexibility Alloy is known for. Since then we've kept building: ironing out service installation support, enabling [Fleet Management](https://grafana.com/docs/grafana-cloud/send-data/fleet-management/?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview&plcmt=in-text), and folding in feedback from early users. Today, as of Alloy v1.21.0, we're happy to share that **the OTel engine has moved into Public Preview**, running right alongside the default engine you already know.

[Download the latest version of Alloy](https://github.com/grafana/alloy/releases)

In this post, we'll dig into when you'd reach for each engine, walk through some of the most interesting use cases we've seen so far, and give a preview of where both engines are headed next.

## The motivation behind each engine

Before diving into specific new features, let’s recap *why* we have two engines in Alloy.

### Default engine

The default engine is a cross-ecosystem engine at its core; it's not tied to any single wire format or vendor. It can just as easily run a Prometheus pipeline, an OTLP pipeline, or a Loki pipeline, all defined using Alloy's own configuration syntax. That flexibility is what makes it a Swiss army knife: the same engine that scrapes Prometheus metrics can pull in logs over syslog for logs, ingest OTLP, scrape Prometheus metrics from embedded exporters, and route all of it to wherever it needs to go.

### OpenTelemetry engine

There's a lot to like about being able to speak every ecosystem's language. But the telemetry landscape itself is moving in the opposite direction. Rather than translating between formats, the industry is increasingly converging on a single, shared model defined by the OpenTelemetry specification. That's what an OpenTelemetry Collector actually is: a pipeline that treats OTLP as the native format end-to-end, prioritizing portability and open standards over ecosystem-bridging translation. At its core, Alloy's OTel engine is Grafana Labs' own distribution of the OpenTelemetry Collector.

## Running the OTel engine

### It's just a collector

The OTel engine is an OpenTelemetry Collector distribution that ships inside Alloy. It runs standard collector YAML with no translation and no Alloy syntax. If you already have a collector config, you already have an OTel engine config.

```
- otelcol --config=config.yaml
+ alloy otel --config=config.yaml
```

The rest of the CLI matches, too. `validate`, `components`, `print-config`, and `--set` all work the way they do upstream, so scripts and CI that call `otelcol validate` keep working.

The same goes for the tools you deploy collectors with. On the upstream [Helm chart](https://grafana.com/docs/alloy/latest/set-up/otel_engine/helm/?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview&plcmt=in-text), it's two values:

```
image:
  repository: grafana/alloy
command:
  name: "bin/otelcol"
```

The OpenTelemetry Operator used to fail on the Alloy image because it had no way to set the container command. We added `spec.command` upstream (Operator v0.153.0 and later), so now it's one line:

```
spec:
  image: grafana/alloy:<ALLOY_VERSION>
  command: ["/bin/alloy", "otel"]
```

For a non-containerized installation, the Alloy packages can run either engine as a service. Set `ALLOY_OTEL_MODE=1` and the service runs the OTel engine against `config.yaml`. Read our docs for more information on [how to set it up by platform](https://grafana.com/docs/alloy/latest/set-up/otel_engine/service-installations/?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview&plcmt=in-text).

### Fleet management

Managing collector configuration by hand doesn't scale past a handful of hosts, so remote configuration was one of the first gaps we closed after the initial release. As of Alloy v1.19.0, you can manage OTel engine configuration centrally with [Fleet Management](https://grafana.com/docs/grafana-cloud/send-data/fleet-management/introduction/?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview&plcmt=in-text). The OpAMP supervisor is embedded in the Alloy binary and runs through the new experimental `otel-supervisor` subcommand: point it at your Fleet Management endpoint and credentials with a supervisor configuration file, and Alloy handles the connection, pulls down your pipeline configuration, and applies changes as you publish them. See the Alloy [otel-supervisor reference](https://grafana.com/docs/alloy/latest/reference/cli/otel-supervisor/?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview&plcmt=in-text) to get started.

### An escape hatch: the alloyengine extension

Sometimes the component you need only exists in the default engine today. The [alloyengine extension](https://grafana.com/docs/alloy/latest/set-up/otel_engine/engine-extension/?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview&plcmt=in-text) runs Alloy configuration inside the same collector process, so you can pick up that one piece without running a second agent.

It's Experimental, and we expect it to stay that way. The two engines run side by side but can't pass data to each other directly, so anything that crosses over goes out over the network, usually OTLP.

If you reach for it, *tell us why*. Open an issue on the [Alloy repo](https://github.com/grafana/alloy/issues) with the component you needed. That list is how we decide which default engine pieces become native OpenTelemetry collector components next.

## Experiments with Grafana Cloud products

> Heads up first: nothing in this section is supported, and you *shouldn't* run it in production. Part of what we're working out with the OTel engine is how Grafana Cloud's products behave when the pipeline is OTel end to end. Here's where two of them stand.

**Database Observability.** Today the path that works is adding your existing Alloy config to the collector you already run. Your OTLP pipelines keep doing their thing, and the extension runs database observability next to them. The [Database Observability](https://grafana.com/docs/grafana-cloud/observe-and-act/monitor-infrastructure/database-observability/introduction/?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview&plcmt=in-text) app can't tell the difference:

```
extensions:
  alloyengine:
    config:
      inline:
        content: |
          database_observability.postgres "default" {
            data_source_name = env("POSTGRES_DSN")
            forward_to       = [loki.write.grafana_cloud.receiver]
          }
          // ...the rest of your existing Alloy config

receivers:
  otlp:
    protocols:
      grpc: {}
      http: {}

service:
  extensions: [alloyengine]
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [otlp_http/grafana_cloud]
```

A native collector path is in the works but still further off as we decide how to break the Alloy components out into OpenTelemetry native ones.

**Cloud Provider Observability.** Alloy's cloud provider exporters, like `prometheus.exporter.gcp`, work through the extension the same way. The data will be identical when run in the alloyengine extension as when run in Alloy’s default engine. The more interesting result is what happens without Alloy’s native Prometheus exporters at all. 

We've been working with the Prometheus community to [make exporters embeddable](https://youtu.be/BDryNblRXUE?t=12680) as libraries, so they run as real collector receivers instead of something a collector scrapes. With a collector built to include it, the GCP exporter is just another receiver:

```
receivers:
  stackdriver_exporter:
    exporter_config:
      project_ids: ["<PROJECT_ID>"]
      metrics_prefixes: [compute.googleapis.com/instance]
      aggregate_deltas: true  # off by default; Alloy turns it on
```

Looking beyond Cloud Provider Observability, the [OpenTelemetry Collector Prometheus Distro](https://github.com/open-telemetry/opentelemetry-collector-releases/tree/main/distributions/otelcol-prometheus) is an official, experimental collector distribution that ships embeddable Prometheus exporters as OpenTelemetry receivers including blackbox, Postgres, Google Cloud Monitoring with stackdriver exporter and CloudWatch through yet-another-cloudwatch exporter. The receivers live in [prometheus-opentelemetry-collector](https://github.com/prometheus/prometheus-opentelemetry-collector) if you'd rather build your own with Open Telemetry Collector Builder (OCB). As they progress through the OpenTelemetry stability model we will look to add them to the OTel engine.

## Looking ahead

### OTel engine

So what comes next for the OTel engine now that it's in Public Preview? Making sure you can properly debug your collector is high on the list. Support bundles are a key feature for this in the default engine —a single request to `/-/support` packages your configuration, logs, internal metrics, runtime flags, and pprof profiles into one file you can inspect before sharing. The OTel engine has no equivalent today, so we're building an OTel-native extension to match it. Stay tuned for more updates on that front!

We also want to hear what's pulling you back to the default engine via the Alloy engine extension. The extension is there as an escape hatch, but we plan to break those pieces out into native collector components, the way we've started with Prometheus exporters. If you've reached for the extension, or held off on the OTel engine because something was missing, [tell us what it was](https://github.com/grafana/alloy/issues/new?template=feature_request.yam).

### Default engine

The default engine isn't standing still. Most of the work ahead is about one thing: making sure your data always arrives, even when something downstream is having a bad day.

**Prometheus: a better Remote Write** 

Today  `prometheus.remote_write` is what keeps your metrics from disappearing when your backend goes down, and there’s a lot going on to improve it:

- **Smaller footprint.** Keeping what’s in memory and what’s on disk as small as possible to help in high scale environments and keep restart delays minimal.
- **Pickup where you left off.** Data that was in flight when Alloy restarted should still get sent.
- **Remote Write 2.0.** When we moved our own internal Prometheus workloads to it, egress costs for that telemetry dropped by [more than half](https://grafana.com/blog/how-prometheus-remote-write-v2-can-help-cut-network-egress-costs-by-as-much-as-50-/?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview&plcmt=in-text). You can try it in `prometheus.remote_write` today as an experimental feature, and we're helping push it toward stable upstream.

Because `prometheus.remote_write` builds on upstream Prometheus, much of this work happens upstream, so it helps the whole Prometheus ecosystem, not just Alloy.

**Loki: pipelines that know when something failed**

Alloy's log pipelines still use a design inherited from Promtail, where components pass logs with no way to report back whether delivery worked. That's behind most of the rough edges you might have experienced: logs lost when Alloy shuts down, a slow stage holding up everything behind it, and file positions that advance before a line is actually sent. We're rebuilding the pipeline so success and failure flow back to the source:

- **No silent gaps.** A file's position only moves once its lines are delivered, and Alloy drains in-flight logs on shutdown instead of dropping them.
- **Throughput that scales.** A slow stage stops blocking the whole pipeline, so giving Alloy more CPU actually buys you more throughput.
- **A WAL you can rely on.** We're working through the known issues to take the `loki.write` WAL to general availability, so logs survive an outage or a restart on disk.

Both engines are shaped by what we hear from the people running them, so tell us what you want us to focus on next. Open an issue on the Alloy [repo](https://github.com/grafana/alloy/issues) or come find us in [#alloy](https://grafana.slack.com/archives/C01050C3D8F) on the Grafana Community Slack.

*Miss out on ObservabilityCON 2026? Check out* *[our blog post recapping all the big announcements](https://grafana.com/blog/observabilitycon-2026-announcements/?pg=bridging-alloy-and-opentelemetry-the-otel-engine-is-now-in-public-preview&plcmt=in-text)**!*
