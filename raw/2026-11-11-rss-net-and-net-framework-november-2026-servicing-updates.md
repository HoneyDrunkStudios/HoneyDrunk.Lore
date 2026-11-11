---
source: "https://devblogs.microsoft.com/dotnet/dotnet-and-dotnet-framework-november-2026-servicing-updates"
title: ".NET and .NET Framework November 2026 servicing updates"
author: "Rahul Bhandari (MSFT)"
date_published: "2026-11-10"
date_clipped: "2026-11-11"
category: ".NET Ecosystem"
source_type: "rss"
---

# .NET and .NET Framework November 2026 servicing updates

The November 10, 2026 servicing updates for .NET 10, .NET 9, and .NET 8 include security and non-security fixes. This post brings together the security advisories, release notes, and download links for this month’s updates, along with resources for .NET Framework servicing.

## Security improvements

The following table covers vulnerabilities affecting .NET 8, 9, 10, and 11, including associated tooling. Follow each advisory for the full list of affected products and remediation guidance.

| CVE | Vulnerability or component | Affected versions covered in this post |
| --- | --- | --- |
| [CVE-2026-114146](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114146) | ASP.NET Core Elevation of Privilege Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-109475](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-109475) | .NET Denial of Service Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-114147](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114147) | ASP.NET Core Denial of Service Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-105544](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-105544) | .NET Elevation of Privilege Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-114149](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114149) | ASP.NET Core Denial of Service Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-109478](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-109478) | ASP.NET Core Denial of Service Vulnerability | 8 |
| [CVE-2026-114150](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114150) | ASP.NET Core Information Disclosure Vulnerability | 11 |
| [CVE-2026-114151](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114151) | Visual Studio Remote Code Execution Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-114152](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114152) | Visual Studio Remote Code Execution Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-114154](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114154) | ASP.NET Core Denial of Service Vulnerability | 8, 9, 10 |
| [CVE-2026-109476](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-109476) | ASP.NET Core Information Disclosure Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-109481](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-109481) | ASP.NET Core Elevation of Privilege Vulnerability | 11 |
| [CVE-2026-118745](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118745) | Visual Studio Remote Code Execution Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-114155](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114155) | .NET Elevation of Privilege Vulnerability | 10, 11 |
| [CVE-2026-114156](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114156) | ASP.NET Core Security Feature Bypass Vulnerability | 11 |
| [CVE-2026-70175](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-70175) | ASP.NET Core Elevation of Privilege Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-118746](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118746) | .NET Security Feature Bypass Vulnerability | 11 |
| [CVE-2026-118747](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118747) | .NET Denial of Service Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-114157](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114157) | ASP.NET Core Security Feature Bypass Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-114158](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114158) | Visual Studio Remote Code Execution Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-114159](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114159) | Visual Studio Remote Code Execution Vulnerability | 8, 9, 10, 11 |
| [CVE-2026-118748](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118748) | ASP.NET Core Denial of Service Vulnerability | 11 |
| [CVE-2026-118749](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118749) | ASP.NET Core Denial of Service Vulnerability | 11 |
| [CVE-2026-120796](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-120796) | .NET Denial of Service Vulnerability | 11 |
| [CVE-2026-118741](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118741) | ASP.NET Core Elevation of Privilege Vulnerability | 8, 9, 10 |

CVE-2026-118747 requires a separate `System.Formats.Cbor` NuGet package update. For the .NET 9 package line, the fix is in version 9.0.24, not 9.0.23. Installing runtime 9.0.23 alone does not fix this vulnerability; update the package, then rebuild and redeploy affected applications.

CVE-2026-118741 affects ASP.NET Core Identity scaffolding and templates. Update the affected scaffolding/template packages or the SDK that supplies the templates, and correct, rebuild, and redeploy previously generated applications. Updating the runtime alone does not repair generated code.

For version-specific CVE lists, see [.NET 11](https://github.com/dotnet/core/blob/main/release-notes/11.0/cve.md), [.NET 10](https://github.com/dotnet/core/blob/main/release-notes/10.0/cve.md), [.NET 9](https://github.com/dotnet/core/blob/main/release-notes/9.0/cve.md), and [.NET 8](https://github.com/dotnet/core/blob/main/release-notes/8.0/cve.md).

## Downloads and release notes

|  | .NET 11.0 | .NET 10.0 | .NET 9.0 | .NET 8.0 |
| --- | --- | --- | --- | --- |
| Release notes | [11.0.0](https://github.com/dotnet/core/blob/main/release-notes/11.0/11.0.0/11.0.0.md) | [10.0.15](https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.15/10.0.15.md) | [9.0.23](https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.23/9.0.23.md) | [8.0.34](https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.34/8.0.34.md) |
| Installers and binaries | [11.0.0](https://dotnet.microsoft.com/download/dotnet/11.0) | [10.0.15](https://dotnet.microsoft.com/download/dotnet/10.0) | [9.0.23](https://dotnet.microsoft.com/download/dotnet/9.0) | [8.0.34](https://dotnet.microsoft.com/download/dotnet/8.0) |
| Container images | [Images](https://mcr.microsoft.com/catalog?search=dotnet/) | [Images](https://mcr.microsoft.com/catalog?search=dotnet/) | [Images](https://mcr.microsoft.com/catalog?search=dotnet/) | [Images](https://mcr.microsoft.com/catalog?search=dotnet/) |
| Linux packages | [11.0](https://github.com/dotnet/core/blob/main/release-notes/11.0/install-linux.md) | [10.0](https://github.com/dotnet/core/blob/main/release-notes/10.0/install-linux.md) | [9.0](https://github.com/dotnet/core/blob/main/release-notes/9.0/install-linux.md) | [8.0](https://github.com/dotnet/core/blob/main/release-notes/8.0/install-linux.md) |
| Known issues | [11.0](https://github.com/dotnet/core/blob/main/release-notes/11.0/known-issues.md) | [10.0](https://github.com/dotnet/core/blob/main/release-notes/10.0/known-issues.md) | [9.0](https://github.com/dotnet/core/blob/main/release-notes/9.0/known-issues.md) | [8.0](https://github.com/dotnet/core/blob/main/release-notes/8.0/known-issues.md) |

### Release changelogs

- ASP.NET Core: [11.0.0](https://github.com/dotnet/aspnetcore/issues?q=milestone%3A11.0.0%20is%3Aclosed%20label%3Aservicing-approved)
- Entity Framework Core: [11.0.0](https://github.com/dotnet/efcore/issues?q=milestone%3A11.0.0%20is%3Aclosed%20label%3Aservicing-approved) | [10.0.15](https://github.com/dotnet/efcore/issues?q=milestone%3A10.0.15%20is%3Aclosed%20label%3Aservicing-approved)
- Roslyn: [.NET 11](https://github.com/dotnet/roslyn/issues?q=milestone%3A%22.NET%2011%22%20is%3Aclosed%20label%3Aservicing-approved)
- Runtime: [11.0.0](https://github.com/dotnet/runtime/issues?q=milestone%3A11.0.0%20is%3Aclosed%20label%3Aservicing-approved) | [10.0.15](https://github.com/dotnet/runtime/issues?q=milestone%3A10.0.15%20is%3Aclosed%20label%3Aservicing-approved)
- SDK: [11.0.100](https://github.com/dotnet/sdk/issues?q=milestone%3A11.0.0%20is%3Aclosed%20label%3Aservicing-approved)
- Windows Forms: [11.0.0](https://github.com/dotnet/winforms/issues?q=milestone%3A%22.NET%2011%22%20is%3Aclosed%20label%3Aservicing-approved)

## .NET Framework November 2026 updates

For .NET Framework servicing information and update details, see the [.NET Framework release notes](https://learn.microsoft.com/dotnet/framework/release-notes/release-notes).

## Update to the latest servicing release

Use the download links above to update your .NET SDK and runtimes. Review the release notes and security advisories for guidance relevant to your applications.
