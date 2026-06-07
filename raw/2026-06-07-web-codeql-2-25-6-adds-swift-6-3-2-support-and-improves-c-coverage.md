---
source: "https://github.blog/changelog/2026-06-05-codeql-2-25-6-adds-swift-6-3-2-support-and-improves-c-coverage/"
title: "CodeQL 2.25.6 adds Swift 6.3.2 support and improves C# coverage"
author: "GitHub Changelog"
date_published: "2026-06-05"
date_clipped: "2026-06-07"
category: "Security & Ethical Hacking"
source_type: "web"
---

# CodeQL 2.25.6 adds Swift 6.3.2 support and improves C# coverage

Source: https://github.blog/changelog/2026-06-05-codeql-2-25-6-adds-swift-6-3-2-support-and-improves-c-coverage/

Back to changelog 
Improvement 
June 5, 2026 •
2 minute read 
CodeQL 2.25.6 adds Swift 6.3.2 support and improves C# coverage 
Table of Contents 
Language and framework support 
Query changes 
Menu. Currently selected: Language and framework support 
Language and framework support 
Query changes 
CodeQL is the static analysis engine behind GitHub code scanning , which finds and remediates security issues in your code. We’ve recently released CodeQL 2.25.6 , which adds Swift 6.3.2 support, completes full coverage for C# 14 and .NET 10, and improves sensitive data detection across multiple languages.
Language and framework support 
Swift 
CodeQL now supports analysis of apps built with Swift 6.3.2. 
C# 
We’ve completed full support for C# 14 and .NET 10. The extractor now supports all new language features, and the data flow library now includes generated models for the .NET 10 runtime. 
Java/Kotlin 
We’ve added source and sink models for org.apache.avro . 
C/C++ 
We’ve added flow source models for scanf_s and related functions. 
Query changes 
GitHub Actions 
We’ve adjusted actions/untrusted-checkout/critical so alerts now appear at the checkout point, aligning it with related untrusted resource queries. Note that this change will cause alerts that were previously closed from this query to reopen. 
The actions/unpinned-tag query now recognizes 64-character SHA-256 commit hashes as properly pinned references in addition to 40-character SHA-1 hashes, which may reduce false positives. 
The analysis now recognizes more Bash regex checks that restrict values to alphanumeric characters, including patterns that check for SHA-1 or SHA-256 hashes, which may reduce false positives where command output is validated before use. 
JavaScript/TypeScript, Python, Swift, and Rust 
We’ve improved the sensitive data heuristics used to identify code handling passwords and private data, allowing CodeQL to detect more variations of established patterns. Queries such as js/clear-text-logging , py/clear-text-logging-sensitive-data , swift/cleartext-logging , and rust/cleartext-logging may now find more correct results and fewer false positives. 
For a full list of changes, please refer to the complete changelog for version 2.25.6 . Every new version of CodeQL is automatically deployed to users of GitHub code scanning on github.com. The new functionality in CodeQL 2.25.6 will also be included in a future GitHub Enterprise Server (GHES) release. If you use an older version of GHES, you can manually upgrade your CodeQL version .
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
