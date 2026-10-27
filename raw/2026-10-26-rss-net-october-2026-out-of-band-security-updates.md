---
source: "https://devblogs.microsoft.com/dotnet/dotnet-october-2026-oob-security-updates"
title: ".NET October 2026 Out-of-Band Security Updates"
author: "Rahul Bhandari"
date_published: "2026-10-25"
category: ".NET Ecosystem"
source_type: "rss"
date_clipped: "2026-10-26"
---

# .NET October 2026 Out-of-Band Security Updates

Today, we are releasing out-of-band (OOB) security updates for .NET 8, .NET 9, and .NET 10, along with .NET 11 Release Candidate 3. We recommend updating as soon as possible.

## Security updates

This out-of-band release addresses [CVE-2026-111497](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-111497), a vulnerability in the [Brotli decompression algorithm](https://www.rfc-editor.org/rfc/rfc7932). It also includes a fix for [CVE-2026-114148 (Linux .NET tarball ownership)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114148) in .NET 8, 9, 10, and 11.

| CVE | Description | Affected platforms |
| --- | --- | --- |
| [CVE-2026-111497](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-111497) | A buffer overflow vulnerability exists in .NET’s use of the Brotli decompression algorithm. This vulnerability may allow an unauthenticated attacker to read or corrupt process memory. This could lead to information disclosure, denial of service, or elevation of privilege. | All Platforms |
| [CVE-2026-114148](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-114148) | Unsafe ownership metadata in affected .NET tarballs could allow a local attacker to modify files and gain elevated privileges. | Linux |

Applications may be affected if they process Brotli-compressed data through [ASP.NET Core request decompression](https://learn.microsoft.com/aspnet/core/fundamentals/middleware/request-decompression), [HttpClient automatic response decompression](https://learn.microsoft.com/dotnet/api/system.net.http.httpclienthandler.automaticdecompression), or the `System.IO.Compression` Brotli APIs. Request decompression and automatic response decompression are not enabled by default. .NET Framework is not affected.

For .NET 10 and .NET 11, CVE-2026-114148 affects source-build tarballs only. For .NET 8 and .NET 9, it also affects ASP.NET Core distributions obtained through ASP.NET Core tarballs, including users who do not build .NET from source.

For vulnerability details and affected products, see the linked security advisories.

Additionally, we are re-releasing the advisories for [CVE-2026-70197 (SocketAsyncEventArgs memory corruption)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-70197) in .NET 8, 9, 10, and 11, and [CVE-2026-102870 (Blazor WebAssembly debugger)](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-102870) in .NET 10 and 11 because the October 13, 2026 release did not fully address these issues. Today’s updates provide those fixes.

## Download the updates

| .NET version | Update | Download |
| --- | --- | --- |
| .NET 8 | **8.0.33** | [.NET 8 SDK and Runtime](https://dotnet.microsoft.com/download/dotnet/8.0) |
| .NET 9 | **9.0.22** | [.NET 9 SDK and Runtime](https://dotnet.microsoft.com/download/dotnet/9.0) |
| .NET 10 | **10.0.14** | [.NET 10 SDK and Runtime](https://dotnet.microsoft.com/download/dotnet/10.0) |
| .NET 11 | **Release Candidate 3** | [.NET 11 SDK and Runtime](https://dotnet.microsoft.com/download/dotnet/11.0) |

.NET 11 RC2 users should update to RC3 to receive these fixes.

## Update your applications and build environments

- **Framework-dependent applications:** Install the updated runtime for the .NET version your application targets, then restart the application.
- **Self-contained applications:** Rebuild and republish with the updated runtime. Installing a newer runtime on the host does not update the runtime bundled with your application.
- **Containers:** Rebuild and redeploy using updated [.NET container images](https://mcr.microsoft.com/catalog?search=dotnet/).
- **Source-build consumers:** Obtain the updated source-build artifacts for your .NET version and rebuild your packages to incorporate the tarball ownership fix.
- **ASP.NET Core tarball users on .NET 8 and .NET 9:** Update your installation using the refreshed ASP.NET Core Runtime tarball for your .NET version. This applies even if you do not build .NET from source.

You can check the runtimes installed on a machine with:

```
dotnet --list-runtimes
```

For framework-dependent deployments, confirm that the appropriate updated runtime listed above is installed. Self-contained applications and container deployments must be checked separately because they carry their own runtime.

See the [.NET deployment documentation](https://learn.microsoft.com/dotnet/core/deploying/) for more information about framework-dependent and self-contained applications.

## Feedback

If you encounter a problem after updating, report it in the [.NET release feedback issues](https://github.com/dotnet/core/issues).
