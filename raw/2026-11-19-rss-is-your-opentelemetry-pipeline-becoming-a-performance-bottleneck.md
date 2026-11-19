---
source: "https://www.cncf.io/blog/2026/11/17/is-your-opentelemetry-pipeline-becoming-a-performance-bottleneck"
title: "Is your OpenTelemetry pipeline becoming a performance bottleneck?"
author: "Diana Todea"
date_published: "2026-11-17"
date_clipped: "2026-11-19"
category: "DevOps & CI/CD"
source_type: "rss"
---

# Is your OpenTelemetry pipeline becoming a performance bottleneck?

Source: https://www.cncf.io/blog/2026/11/17/is-your-opentelemetry-pipeline-becoming-a-performance-bottleneck

Posted on November 17, 2026
by Diana Todea (CNCF Ambassador, OpenTelemetry Documentation approver, Romanian Localization maintainer)

CNCF projects highlighted in this post

[![OpenTelemetry logo](https://landscape.cncf.io/logos/52818595352a47637721976b546e0a2a1d0da186a0eb97ec203bd7e5248eb4fc.svg)](https://www.cncf.io/projects/opentelemetry "Go to OpenTelemetry")

At [Cloud Native Days Austria](https://cloudnativedays.at/) 2026, I presented a talk called [*How to Defeat OTel’s Silent Killer: The Performance Overhead*](https://www.youtube.com/watch?v=OolHw9MJ37Y&list=PLcMwH4f9MXB4&index=5), exploring a problem that is easy to overlook when building observability pipelines: the cost of collecting telemetry itself.

[OpenTelemetry](https://opentelemetry.io/) has become a cornerstone of cloud-native observability, providing standardized APIs, SDKs, and tooling for generating, collecting, processing, and exporting metrics, logs, and traces. However, instrumentation and telemetry processing are not free. Every span created, attribute attached, and batch exported consumes resources.

As applications scale, poorly configured telemetry pipelines can introduce significant CPU usage, memory pressure, network traffic, and storage costs. In some cases, the infrastructure responsible for observing a system can become a performance problem of its own.

The good news is that much of this overhead can be understood, measured, and reduced without sacrificing the visibility engineers depend on.

## **Where does OpenTelemetry overhead come from?**

When discussing OpenTelemetry performance, we often focus on the application SDK. However, the cost extends beyond instrumentation.

The entire telemetry pipeline contributes to resource consumption, from generating spans and collecting metrics to processing, exporting, and storing data.

Instrumentation overhead is also workload-dependent. Two applications using the same instrumentation libraries can experience very different results depending on request throughput, attribute volume, runtime behavior, and the number of spans generated per request.

This is why relying on a single overhead percentage can be misleading. Instead, we should examine CPU consumption, memory usage, application latency, telemetry volume, and the behavior of the Collector under load.

There is also an important trade-off between application safety and telemetry completeness. When a pipeline becomes overloaded, backpressure and memory safeguards can protect the application and OpenTelemetry Collector, but they may also lead to rejected or dropped telemetry.

The objective is not simply to minimize resource consumption. It is to maintain useful observability while keeping its operational cost predictable.

## **Investigating the Collector: five common configuration problems**

For my demonstration, I used [Telemetrygen](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/cmd/telemetrygen), an OpenTelemetry utility that generates synthetic telemetry, to investigate how Collector configuration affects resource consumption.

The investigation focused on five common sources of unnecessary overhead.

### **1. Inefficient batching**

Exporting small amounts of telemetry frequently can increase serialization work, export requests, and network overhead.

The OpenTelemetry Collector groups telemetry inside the exporter’s sending queue before transmitting it downstream, helping amortize this work across larger payloads. (Note: Historically, this was handled by a standalone batch processor, which is now [deprecated](https://opentelemetry.io/blog/2026/collector-batching-migration/) in favor of built-in exporter batching).

However, batching parameters should reflect the actual workload. Larger batches are not automatically better: they can increase buffering requirements and affect export latency.

```
exporters:
  otlp_grpc:
    endpoint: "otel-backend:4317"
    sending_queue:
      enabled: true
      sizer: items       
      queue_size: 100000 
      batch:
        enabled: true
        min_size: 8192
        flush_timeout: 200ms
```

Configuring batch inside an exporter’s sending\_queue groups spans, metrics, or logs before forwarding them downstream, improving compression efficiency and durability while reducing export overhead. Batches are sent when a configured size threshold is reached or a timeout expires.

In this example, min\_size: 8192 triggers an export when the batch reaches 8,192 items, while flush\_timeout: 200ms triggers an export regardless of batch size. Once batching is enabled, these values are the Collector’s documented defaults, not universal performance recommendations. (Note: Because unbatched requests enter the queue first in this architecture, this example switches sizer from the default requests to items with a queue\_size of 100000 to prevent smaller, unbatched bursts from overflowing the queue).

The important point is to measure how batching affects resource consumption and throughput rather than relying on example configurations.

### **2. Unnecessary resource attributes**

[Resource attributes](https://opentelemetry.io/docs/specs/semconv/resource/host/) provide valuable context about the systems producing telemetry. But collecting and forwarding attributes that nobody uses can increase payload sizes and downstream processing costs.

For example, an application might need `host.name, host.arch`, and `os.type` for troubleshooting, but not detailed hardware information such as `host.cpu.model.name` or `host.cpu.cache.l2.size`.

The OpenTelemetry Collector’s [resource detection processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/resourcedetectionprocessor/README.md) allows engineers to configure which system attributes are collected. Disabling unnecessary attributes can reduce telemetry volume and processing overhead, although the impact on storage and cardinality depends on the backend.

**A practical example:** Keep the hostname and operating system type, but disable CPU model and cache metadata when those details are not needed for troubleshooting.

### **3. Aggressive receiver polling**

Infrastructure receivers collect metrics at configured intervals, often independently of application traffic.

Polling [host metrics](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/hostmetricsreceiver/README.md), container statistics, databases, and network services every few seconds creates continuous work even when applications are relatively idle.

Increasing collection intervals from 10 to 30 seconds, where operational requirements permit, can reduce collection frequency and associated overhead.

This introduces a trade-off: lower polling frequency means less temporal resolution. The appropriate interval depends on how quickly a metric changes and how it is used for troubleshooting or alerting.

### **4. Exporting every trace**

Not every successful request needs to produce a trace that is retained.

Exporting all traces can consume significant bandwidth, Collector resources, and backend capacity, particularly in high-throughput applications.

Sampling provides a way to control this volume.

[Head-based sampling](https://opentelemetry.io/docs/concepts/sampling/#head-sampling) makes decisions early, reducing downstream work. [Tail-based sampling](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/tailsamplingprocessor) makes decisions after observing more of a trace, enabling policies that retain errors or other diagnostically interesting requests.

![Figure 1: OpenTelemetry Collector YAML configuration showing tail-based sampling with a 10-second decision window. The configuration retains traces with an ERROR status and probabilistically samples 5% of traces. The trace pipeline applies memory limiting, resource detection, span sanitization, GenAI normalization, tail sampling, and batching before exporting telemetry.](https://www.cncf.io/wp-content/uploads/2026/11/image-12.png)

These policies retain traces with an error status and probabilistically sample 5% of traces, including potentially some additional error traces. However, tail sampling is not free. It requires buffering trace data until a decision can be made, introducing additional memory and processing overhead.

Choosing a sampling strategy means balancing cost, diagnostic value, and the resources needed to make sampling decisions.

### **5. Memory safeguards applied too late**

The OpenTelemetry Collector includes a `memory_limiter` processor to help manage memory pressure.

Processor ordering matters. When enrichment and transformation processors run before memory limiting, the Collector may perform additional work on telemetry that is subsequently refused under memory pressure.

Memory limiting is a protective mechanism rather than a performance optimization in itself. Its purpose is to improve stability under pressure, not necessarily to reduce CPU consumption during normal operation. Placing the [memory limiter](https://github.com/open-telemetry/opentelemetry-collector/blob/main/processor/memorylimiterprocessor/README.md) early in the pipeline helps apply safeguards before more expensive processing.

It is important to understand that the memory limiter is not a substitute for appropriate resource limits or capacity planning. It can refuse incoming data when memory pressure becomes excessive, and receivers must handle this behavior correctly to avoid unnecessary telemetry loss.

## **From local experiments to production architecture**

Optimizing a single Collector is only part of the solution.

In Kubernetes, telemetry workloads can fluctuate significantly as applications scale, deployments change, and traffic increases. A Collector configuration that performs well under synthetic load may behave differently in production.

Here are some architectural practices that can help address these challenges.

1. **Separate collection from centralized processing.** A two-tier architecture can use lightweight edge Collectors for local collection and gateway Collectors for more expensive processing. This allows different parts of the pipeline to scale according to their workloads.
2. **Control telemetry volume early.** Filtering unnecessary attributes, removing unneeded data, and avoiding excessive cardinality can reduce the amount of information processed and transferred downstream. These decisions should preserve the context required for debugging and correlation.
3. **Plan for memory pressure and backend outages.** Kubernetes memory limits, Collector memory safeguards, bounded queues, and retry mechanisms serve different purposes. Persistent queues can improve resilience during temporary backend failures, but they still require capacity planning and cannot guarantee delivery under every failure scenario.
4. **Scale with signal-specific requirements in mind.** Horizontal scaling can increase throughput, but stateful processing requires additional consideration. Tail sampling, for example, generally requires spans belonging to the same trace to reach the same processing instance.

These architectural decisions are just as important as tuning individual processors.

## **Don’t forget the instrumentation**

One of the most effective optimizations happens before telemetry reaches the Collector.

Instrumentation should answer meaningful operational questions rather than collect everything simply because it is possible. Excessive spans, high-cardinality attributes, and unnecessary instrumentation can increase resource consumption throughout the entire pipeline.

For metrics, attributes containing unbounded values such as unique request IDs can create large numbers of distinct time series. For traces and logs, excessive attributes and events increase payload sizes and may affect backend processing or indexing costs.

### **Why I chose Telemetrygen for my demo**

When preparing my performance investigation, I initially considered using the official [OpenTelemetry Astronomy Shop](https://github.com/open-telemetry/opentelemetry-demo). While it is an excellent environment for exploring instrumentation across microservices, its multiple applications, databases, and supporting services introduce additional CPU and memory consumption.

For this experiment, I wanted to isolate the Collector’s performance overhead without the background noise of a complete application environment.

Instead, I chose [Telemetrygen](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/cmd/telemetrygen), a lightweight utility for generating synthetic traces, metrics, and logs at controlled rates.

In my [OpenTelemetry performance overhead demo](https://github.com/didiViking/otel-performance-overhead), I used synthetic telemetry to investigate how Collector configuration affects resource consumption. The demonstration walks through common inefficiencies, including missing batching, unnecessary resource attributes, aggressive receiver polling, excessive trace export, and memory limiter placement, showing how targeted configuration changes can improve pipeline efficiency.

This approach helped isolate Collector behavior, but it is only one part of the performance picture. For understanding instrumentation overhead inside real applications, a complete environment such as Astronomy Shop remains valuable.

### **Exploring instrumentation further**

Reducing overhead starts with understanding what telemetry an application generates and why. The official [OpenTelemetry instrumentation documentation](https://opentelemetry.io/docs/) introduces automatic and manual instrumentation, while the sampling documentation explains how to control trace volume. These are useful starting points for reviewing instrumentation decisions before optimizing the Collector itself.

For engineers interested in investigating performance further, the OpenTelemetry Collector documentation covers pipeline configuration and processing. The OpenTelemetry community is also a good place to discuss performance challenges. The Collector SIG focuses on Collector architecture, performance, and configuration, with discussions taking place in the **#otel-collector** channel on CNCF Slack.

For questions about instrumentation overhead in a specific programming language, the corresponding language SIG is a better starting point. The [OpenTelemetry community page](https://opentelemetry.io/community/) provides information about SIGs, public meetings, and how to get involved.

## **Making performance part of observability design**

OpenTelemetry overhead is not a single problem with a single configuration fix.

It is the combined effect of instrumentation decisions, data volume, processor configuration, export behavior, and infrastructure architecture.

The most useful lesson from this investigation is that **observability pipelines should be measured and optimized like any other production system**.

Start with controlled benchmarks. Understand where resources are consumed. Introduce configuration changes individually, and evaluate their impact on CPU, memory, latency, throughput, and telemetry loss.

Most importantly, treat example configurations as starting points rather than production-ready defaults.

OpenTelemetry gives us the tools to understand complex distributed systems. With thoughtful instrumentation, careful pipeline configuration, and appropriate scaling strategies, we can ensure that collecting this information does not become an unnecessary burden on the systems we are trying to observe.
