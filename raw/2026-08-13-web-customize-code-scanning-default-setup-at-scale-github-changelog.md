---
source: "https://github.blog/changelog/2026-08-04-customize-code-scanning-default-setup-at-scale/"
title: "Customize code scanning default setup at scale - GitHub Changelog"
author: "Allison"
date_published: "2026-08-04"
date_clipped: "2026-08-13"
category: "DevOps & CI/CD"
source_type: "web"
---

# Customize code scanning default setup at scale - GitHub Changelog

Source: https://github.blog/changelog/2026-08-04-customize-code-scanning-default-setup-at-scale/

# Customize code scanning default setup at scale

You can now apply your own configuration file to code scanning default setup, using the new `github-codeql-config-file`

repository property. This gives you control over how CodeQL scans your code for security vulnerabilities, whether that’s on one repository or across your whole organization. We recommend using this way to customize your security analysis at scale. You get the granular control of advanced setup without writing or maintaining a GitHub Actions workflow file in every repository.

## Apply a custom configuration file to default setup

Set the `github-codeql-config-file`

repository property to the path of a CodeQL configuration file, and code scanning now merges your settings with its built-in defaults. You can add queries, exclude paths, or set threat models, and still keep default setup’s low-maintenance benefits. Any threat models and CodeQL model packs you picked in the default setup user interface are kept in the merged configuration.

Repository properties support organization-wide default values, and organization owners decide whether individual repositories are allowed to override it. So you can keep one configuration file in a central repository and have every repository automatically pick it up, enforce it everywhere, or let teams tailor it where they need to. You can also try a value out on one repository before rolling it out. For more information, see customizing default setup with a configuration file.

## How to use configuration files from other repositories

There’s a new, more flexible syntax for pointing at a configuration file that lives in another repository. Only the repository name is required. If you leave out the ref and the file path, the reference falls back to a default configuration file path on the `main`

branch of a repository in the same organization as the one being analyzed. For more information, see how to reference a configuration file in another repository.

If that repository is private, you can now grant default setup access to it by configuring a `Git Source`

private registry for your organization, instead of managing a token in a workflow. For more information, see giving your organization access to private registries.

This is now generally available on github.com and will ship with GitHub Enterprise Server 3.23. To get started, see repository properties for code scanning.
