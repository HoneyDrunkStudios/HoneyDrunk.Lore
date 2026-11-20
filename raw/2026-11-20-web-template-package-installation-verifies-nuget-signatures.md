---
source: "https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/template-package-signature-verification"
title: "Template package installation verifies NuGet signatures"
author: "gewarren"
date_published: "unknown"
date_clipped: "2026-11-20"
category: ".NET Ecosystem"
source_type: "web"
source_last_updated: "2026-11-12"
---

# Template package installation verifies NuGet signatures

Template package installation now verifies signed packages downloaded from NuGet sources when signature verification is enabled. Packages that fail verification aren't installed.

## Version introduced

- .NET 8 SDK 8.0.134 and 8.0.428
- .NET 9 SDK 9.0.124 and 9.0.321
- .NET 10 SDK 10.0.115 and 10.0.404
- .NET 11 SDK 11.0.100

## Previous behavior

Previously, `dotnet new install` didn't verify NuGet package signatures when downloading template packages. Packages could be installed even if their signatures were invalid or they were unsigned despite a client or repository policy requiring signatures.

## New behavior

When signature verification is enabled, signed template packages downloaded from NuGet sources are verified using `dotnet nuget verify --all` before installation. If verification fails, installation fails. The `--force` option doesn't bypass verification.

Unsigned packages are accepted only if the applicable NuGet configuration's `signatureValidationMode` is `accept` (the default) and the source doesn't declare `allRepositorySigned=true`. A client policy of `require` or a repository signing requirement causes unsigned packages to be rejected.

Verification is always enabled on Windows. On Linux, it's enabled by default and can be disabled by setting `DOTNET_NUGET_SIGNATURE_VERIFICATION=false`. On macOS, it's disabled by default and can be enabled by setting `DOTNET_NUGET_SIGNATURE_VERIFICATION=true`. See [NuGet signed-package verification](https://learn.microsoft.com/en-us/dotnet/core/tools/nuget-signed-package-verification) for certificate-store requirements and platform limitations.

This verification applies to packages downloaded from configured or additional NuGet sources. It doesn't apply when you install a template package directly from a local `.nupkg` file or folder.

## Type of breaking change

This change is a [behavioral change](https://learn.microsoft.com/en-us/dotnet/core/compatibility/categories#behavioral-change).

## Reason for change

Signature verification helps validate the authenticity and integrity of downloaded template packages and rejects unsigned packages when client or repository policy requires signing. A valid signature doesn't guarantee that template code is safe to run.

## Recommended action

If your template packages pass verification, no action is required.

If installation fails, run `dotnet new install` with `--diagnostics` to see verification details. You can also use [`dotnet nuget verify`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-nuget-verify) to verify a downloaded package explicitly.

For signature or integrity failures, obtain a valid package from a trusted source or contact the package publisher. For certificate-trust failures, review the certificate-store requirements in [NuGet signed-package verification](https://learn.microsoft.com/en-us/dotnet/core/tools/nuget-signed-package-verification).

If an unsigned package is rejected, check the applicable [signatureValidationMode](https://learn.microsoft.com/en-us/nuget/reference/nuget-config-file#signaturevalidationmode) and the source's repository-signing requirements. Use a signed package that meets those requirements rather than bypassing verification.

For command behavior and configuration, see [`dotnet new install`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new-install#package-signature-verification).

## Affected APIs

None.
