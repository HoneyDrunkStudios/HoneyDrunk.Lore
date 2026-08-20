---
source: "https://github.blog/changelog/2026-08-19-codeql-2-26-3-improves-github-actions-queries-and-javascript-modeling/"
title: "CodeQL 2.26.3 improves GitHub Actions queries and JavaScript modeling"
author: "GitHub Changelog"
date_published: "2026-08-19"
date_clipped: "2026-08-20"
category: "DevOps & CI/CD"
source_type: "web"
---

# CodeQL 2.26.3 improves GitHub Actions queries and JavaScript modeling

Source: https://github.blog/changelog/2026-08-19-codeql-2-26-3-improves-github-actions-queries-and-javascript-modeling/

Back to changelog
Improvement
August 19, 2026 •
2 minute read
CodeQL 2.26.3 improves GitHub Actions queries and JavaScript modeling
Table of Contents
Language and framework support
Query changes
Menu. Currently selected: Language and framework support
Language and framework support
Query changes
CodeQL 2.26.3 adds JavaScript, TypeScript, and Vue source modeling and improves the accuracy of several GitHub Actions queries. CodeQL is the static analysis engine behind GitHub code scanning , which helps you find and remediate security issues in your code.
Language and framework support
GitHub Actions
Analysis now recognizes untrusted data in github.event.merge_group for workflows triggered by the merge_group event.
Breaking change: We’ve removed the codeql.actions.security.SelfHostedQuery module because runner labels don’t reliably distinguish self-hosted runners from managed runners. You’ll need to update any custom queries that rely on this module.
JavaScript/TypeScript
Custom models can now reference specific files using a package name in the form file:<path> . This lets you define sources and sinks based on a file’s public exports.
We’ve added flow models for Vue’s ref , shallowRef , toRef , reactive , and computed Composition API helpers.
CodeQL now recognizes Vue Router’s useRoute() Composition API as a client-side remote flow source, including its query , params , path , fullPath , and hash members.
CodeQL now treats declared inputs properties in Sails Action2 controller files as remote flow sources. This may improve results for queries such as js/path-injection .
Queries using the response threat model now track promise-wrapped client response data into promise fulfillment values. This may improve results for queries such as js/xss .
C/C++
We’ve added flow source models for RegQueryValue and related functions from the winreg.h Windows header.
Ruby
We’ve removed library input to vendored gems from the set of taint sources, reducing false positives for several queries when you use vendoring.
Query changes
GitHub Actions
We’ve improved the accuracy of the actions/output-clobbering/high query so it no longer reports simple jq path filters when their output remains JSON-encoded. We also implemented a fix for a performance issue in this query caused by unescaped regular expression input.
The actions/cache-poisoning/poisonable-step and actions/untrusted-checkout/critical queries now start paths at the expressions that control untrusted checkouts, making alerts easier to follow.
GitHub Actions queries now correctly classify the schedule event when determining whether a workflow can be externally triggered.
The actions/envvar-injection/critical query now requires the untrusted source and privileged context to originate from the same trigger event. It also no longer treats pull request head labels as injection-capable because they can’t contain newlines.
The actions/cache-poisoning/code-injection , actions/cache-poisoning/direct-cache , and actions/cache-poisoning/poisonable-step queries now account for read-only cache access on low-trust triggers running in the default branch scope. They retain results only for triggers that GitHub allows to write to that cache scope.
We’ve clarified the name and alert message of the actions/cache-poisoning/code-injection query.
JavaScript/TypeScript
The js/missing-rate-limiting query now recognizes the @fastify/rate-limit package as a rate limiter.
For all changes, see the complete CodeQL 2.26.3 changelog .
GitHub automatically deploys each new CodeQL version to users of GitHub code scanning on GitHub.com. A future GitHub Enterprise Server (GHES) release will include this functionality. If you use an older GHES version, you can manually upgrade CodeQL .
Table of Contents
Language and framework support
Query changes
Menu. Currently selected: Language and framework support
Language and framework support
Query changes
application security
Share
Copied
Shared
Back to changelog
