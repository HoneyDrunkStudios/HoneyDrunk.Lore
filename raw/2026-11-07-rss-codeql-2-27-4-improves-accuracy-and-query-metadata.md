---
"source": "https://github.blog/changelog/2026-11-04-codeql-2-27-4-improves-accuracy-and-query-metadata/"
"title": "CodeQL 2.27.4 improves accuracy and query metadata"
"author": "Allison"
"date_published": "2026-11-04"
"date_clipped": "2026-11-07"
"category": "Security & Ethical Hacking"
"source_type": "rss"
---

# CodeQL 2.27.4 improves accuracy and query metadata

Source: https://github.blog/changelog/2026-11-04-codeql-2-27-4-improves-accuracy-and-query-metadata/

CodeQL is the static analysis engine behind GitHub code scanning, which finds and remediates security issues in your code. We’ve recently released [CodeQL 2.27.4](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.27.4/) with query accuracy improvements across several languages, stronger security checks when you bundle or publish a pack, and corrections to query metadata.

## [Query changes](https://github.blog/changelog/2026-11-04-codeql-2-27-4-improves-accuracy-and-query-metadata/#query-changes)

**Java/Kotlin**

- The `java/log-injection` query now recognizes additional sanitizers and sanitizer guards from the JDK, Apache Commons Lang and Text, Guava, OWASP Java Encoder, and Spring Framework.
- Path-injection queries now recognize additional substring guards and string replacement and removal operations from Apache Commons Lang and Guava.

**Rust**

- We have reduced false positives in the `rust/uncontrolled-allocation-size`, `rust/log-injection`, and `rust/cleartext-logging` queries.

**C/C++**

- The `cpp/suspicious-pointer-scaling` query no longer reports intentional pointer arithmetic on `std::byte*` buffers.
- The `cpp/unused-local-variable` and `cpp/unused-static-variable` queries no longer report variables marked with `[[maybe_unused]]`.

**CWE metadata changes**

CodeQL no longer applies the CWE-730 tag to the following queries:

- **C#**: `cs/redos` and `cs/regex-injection`.
- **Java/Kotlin**: `java/redos`, `java/polynomial-redos`, and `java/regex-injection`.
- **JavaScript/TypeScript**: `js/redos`, `js/polynomial-redos`, `js/regex-injection`, `js/regex-injection-more-sources`, `js/server-crash`, and `js/loop-bound-injection`.
- **Python**: `py/redos`, `py/polynomial-redos`, and `py/regex-injection`.
- **Ruby**: `rb/redos`, `rb/polynomial-redos`, and `rb/regexp-injection`.
- **Swift**: `swift/redos` and `swift/regex-injection`.

This was initially reported in [CodeQL issue #22318](https://github.com/github/codeql/issues/22318); thank you to `@wiggin15` for the feedback.

## [CodeQL CLI](https://github.blog/changelog/2026-11-04-codeql-2-27-4-improves-accuracy-and-query-metadata/#codeql-cli)

- The CLI now writes Java virtual machine warnings and initialization errors to standard error, so they won’t interfere with JSON or other machine-readable output.
- When you bundle or publish a pack, the CLI checks whether each file remains inside the pack root after resolving symbolic links. It omits files that resolve outside the root and displays a warning.

For full details, see the [CodeQL 2.27.4 changelog](https://codeql.github.com/docs/codeql-overview/codeql-changelog/codeql-cli-2.27.4/). GitHub automatically deploys every new CodeQL version to users of GitHub code scanning on github.com. The new functionality in CodeQL 2.27.4 will also be included in the GitHub Enterprise Server (GHES) `3.24` release. If you use an older version of GHES, you can [manually upgrade your CodeQL version](https://docs.github.com/enterprise-server@3.20/admin/managing-code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-codeql-analysis-on-a-server-without-internet-access).
