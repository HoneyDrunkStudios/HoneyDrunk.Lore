---
source: "https://www.harness.io/blog/your-ci-pipeline-just-failed-with-system-failure"
title: "Your CI Pipeline Just Failed With \"System Failure\" (Again). Here's What That Actually Means | Harness Blog"
author: "Animesh Pathak"
date_published: "2026-11-25"
date_clipped: "2026-11-28"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-11-27"
---

# Your CI Pipeline Just Failed With "System Failure" (Again). Here's What That Actually Means | Harness Blog

I ran one Harness pipeline with five parallel stages against a small Python ledger service. Five stages failed and the console showed three distinct messages. Three of the stages showed the identical one, exit status 1, for three different causes: a failing assertion, a full disk and a package index that did not resolve.

That gap is what this post decodes. A step message tells you how the step ended. The cause is in the log, a few lines above the banner. Below you run the same lab, read each failure and see which part of the answer lives where.

## What you will run

The pipeline is Ledger Service CI. The app is a small Python service that posts ledger entries and calculates processing fees, with a pytest suite that passes in about 0.1s on a laptop. Five environment settings turn that green suite into five different failures, one per stage. The code is under the [ledger-ci-lab folder](https://github.com/harness-community/harness-sample-apps/tree/main/ledger-ci-lab) in [harness-community/harness-sample-apps](https://github.com/harness-community/harness-sample-apps/tree/main/ledger-ci-lab) repo.

1. Fork harness-community/harness-sample-apps, check out the ci-test/ledger-lab branch and open the ledger-ci-lab folder
2. Optional if you use the public image: build the image for the runner's architecture and push it: `docker buildx build --platform linux/amd64 -t YOUR_DOCKERHUB_USER/ledger-ci-lab:1.0 --push` .
3. In your project, create a pipeline and paste the contents of `.harness/ledger_ci.yaml`into the YAML editor (the file uses the [v1 pipeline YAML format](https://developer.harness.io/harness-platform/3.0/in-harness-new-experience/pipelines))
4. Create a [Docker connector](https://developer.harness.io/harness-platform/use-harness-platform/connectors/artifact-repositories/add-a-docker-registry-connector) that can pull your image, then set connector in each app stage to its ID and image to the image you pushed (the file points at the public image `sonichigo/ledger-ci-lab:1.0`)
5. Run the pipeline

**Two terms first.** A stage is a major segment of a pipeline and a step is a series of commands that performs a task, as the [key concepts page](https://developer.harness.io/docs/continuous-integration/get-started/key-concepts) defines them. Here every stage holds one step, so the console shows a failed stage and a failed step side by side.

The five stages sit in a parallel group, so the run ends when the slowest one does. Each stage gets its own [Harness Cloud](https://developer.harness.io/docs/continuous-integration/use-ci/set-up-build-infrastructure/use-harness-cloud-build-infrastructure) machine, which is why every stage starts with an Initialize step before your command runs.

## Failure zero: an image for the wrong architecture

My first run failed before a single test was executed. I had built the image on an arm64 laptop, and four of the five stages failed with the same message:

shell

```
no matching manifest for linux/amd64 in the manifest list entries
```

The log shows the pull retried three times. Nothing in that message mentions the laptop, so the fix is to read the platform in it: the runner asked for linux/amd64 and the image had none. Rebuilding with --platform linux/amd64 fixed it. If four stages fail with one identical message and no test output, suspect the environment before the code.

## One message, three causes

After the rebuild, the settings that make each stage fail were switched on. This table is from the latest run:

| Stage | Harness message | What the log shows |
| --- | --- | --- |
| Unit Tests | exit status 1 | assert 102 == 103, 1 failed and 3 passed |
| Export Tests | exit status 1 | OSError: [Errno 28] No space left on device |
| Install Dependencies | exit status 1 | Name or service not known, then No matching distribution found for pytest==8.3.5 |
| Load Tests | OOM killed | the log ends with Killed |
| Integration Tests | Expired | "Please Check the timeout configuration on the step to extend the duration of the step" |

The point,  a code bug, a disk problem and a network problem look the same on the step banner. Only the log separates them.

### Unit Tests: a code failure

yaml

```
- id: run_unit_tests
  name: Run unit tests
  run:
    shell: sh
    container:
      connector: devrel_harness_docker
      image: sonichigo/ledger-ci-lab:1.0
    script: |-
      cd /app
      FEE_MODE=legacy pytest -v tests/test_accounts.py tests/test_fees.py
```

With `FEE_MODE=legacy` the fee calculation truncates instead of rounding half up, so 2.9% of 2500 plus the 30 cent flat fee comes out as 102 instead of 103. The log carries the whole diagnosis:

shell

```
>       assert processing_fee(2500) == 103
E       assert 102 == 103
tests/test_fees.py:10: AssertionError
1 failed, 3 passed in 0.02s
```

This is the one failure where exit status 1 is the honest message: pytest exited with 1 because a test failed. The fix is in the code.

### Export Tests: a full disk

The step sets `EXPORT_ROWS=20000000000`. The export reserves its full size up front with `posix_fallocate`, which at 96 bytes per row is 1.92 TB. The log:

shell

```
OSError: [Errno 28] No space left on device
1 failed in 0.41s
```

The console shows exit status 1, the same as the unit test failure. It failed in under half a second because reserving space first makes a full disk fail before any rows are written. The fix is in the environment or the size of the request.

### Install Dependencies: a network failure

This stage runs pip install against an index URL that does not resolve:

shell

```
WARNING: Retrying (Retry(total=0, ...)) after connection broken by 'NewConnectionError(...: Failed to establish a new connection: [Errno -2] Name or service not known)': /simple/pytest/
ERROR: Could not find a version that satisfies the requirement pytest==8.3.5 (from versions: none)
ERROR: No matching distribution found for pytest==8.3.5
```

Harness shows exit status 1 again. Pip's last line says no distribution matches, which reads like a version problem. The warning two lines above it says the name did not resolve, and that is the cause.

### Load Tests: OOM killed

yaml

```
- id: run_load_tests
  name: Run load tests
  timeout: 15m
  run:
    shell: sh
    container:
      connector: devrel_harness_docker
      image: sonichigo/ledger-ci-lab:1.0
    script: |-
      cd /app
      FIXTURE_ROWS=150000000 pytest -s tests/test_load.py
```

The fixture builds every row in memory. On my laptop one million rows takes about 593 MB, so 150 million rows is on the order of 89 GB, more than either machine size I saw. The log shows pytest start collecting and then:

bash

```
collected 1 item
Killed
```

Harness shows OOM killed. There is no traceback, no memory figure and no test name beyond the file. The message names the cause and the log confirms nothing more, so the next question is how much memory the run had.

The actual reason might surprise you. Although the dashboard displays Linux (Small) for the Load Tests instance across both executions, Resource Insights reveals dissimilar specs underneath. During the second attempt, the stage registered 16 vCPUs and 62.79 GB, allowing the suite to succeed at **60 million records while consuming roughly 55% RAM.**

On the third attempt, that exact stage logged 8 vCPUs and 30.36 GB, hitting max capacity right before the process was terminated. Because a tier designation doesn't ensure fixed memory, verify Resource Insights when configuring memory-intensive suites, and baseline test datasets for the lowest potential hardware configuration.

### Integration Tests: Expired, not Failed

yaml

```
- id: run_integration_tests
  name: Run integration tests
  timeout: 60s
  run:
    shell: sh
    container:
      connector: devrel_harness_docker
      image: sonichigo/ledger-ci-lab:1.0
    script: |-
      cd /app
      DB_HOST=db.internal DB_WAIT_SECONDS=300 pytest -s tests/test_integration.py
```

The test waits up to 300 seconds for a database host that does not exist, and the step has a 60 second timeout. The step shows as Expired, not Failed, and shows the timeout message in the table. The console shows 1m 40s for a 60 second limit. The timeout covers the step's own execution. The stage's Initialize step took 36 seconds, and the remaining few seconds are startup and image pull time.

Raising the timeout would not fix this test. The host does not exist, so a longer wait only delays the same expiry.

## What the group and the summary said

The parallel group has its own failure message, and in this run it read OOM killed. The run summary named a single failing step, Install Dependencies, even though five stages failed. If you read only the group message or the summary, you see one failure out of five.

## Ask Harness AI, then check it

To get error analysis, enable Harness AI under Account Settings, Default Settings, Harness AI, then click Save. Per the [Harness AI troubleshooting docs](https://developer.harness.io/docs/platform/harness-ai/core-capabilities/in-harness-ui/ci-agent), analysis is available from the Harness AI dialog on a failed step's logs.

I tested the Harness AI chat on the run page against an earlier version of this lab, and checked its answer against the logs. Config values, timestamps and the relationship between the 30 second timeout and a 120 second sleep held up.

Three claims did not: it described a hard memory cap that the logs do not show, it said a process exited with signal 9 when neither the message nor the log says so, and it gave 1m 17s as a step duration when that was the whole stage. It also called the failures "self-inflicted by design", which is true of a lab and says nothing about a real incident. Treat its answer as a fast first read and verify numbers and causes against the log.

## A checklist for the next opaque failure

1. Read the step status first: Failed and Expired point to different places
2. Compare the messages across stages: four stages with one identical message and no test output points at the environment
3. Read the log lines above the banner, not only the last one
4. For OOM killed, find out how much memory the machine had before changing the code
5. Compare Initialize time with the step timeout before blaming the step
6. Ask Harness AI for a first read, and verify every number it cites

This post is part of the Test at the Speed of AI series. The earlier post, [Running a Green CI Pipeline Isn't the Hard Part Anymore](https://www.harness.io/blog/green-ci-pipeline-isnt-enough), covers how a green pipeline still wastes time on repeated compilation, dependency downloads and test runs.

To run the lab yourself, [sign up for Harness for free](https://app.harness.io/auth/#/signup?module=ci&utm_source=harness_io&utm_medium=cta&utm_campaign=ci), fork the ledger-ci-lab folder and compare your messages with the ones here.

## Related reading

- [Test Intelligence: Move Fast, Don't Break Things](https://www.harness.io/blog/test-intelligence)
- [Continuous Integration Testing: Types, Best Practices, and Tools](https://www.harness.io/blog/continuous-integration-testing)
- [AI Test Automation for faster and smarter DevOps delivery](https://www.harness.io/blog/announcing-harness-ai-test-automation)
