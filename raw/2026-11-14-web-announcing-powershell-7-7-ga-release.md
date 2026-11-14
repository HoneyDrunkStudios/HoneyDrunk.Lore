---
source: "https://devblogs.microsoft.com/powershell/announcing-powershell-7-7"
title: "Announcing PowerShell 7.7 GA Release"
author: "Jason Helmick"
date_published: "2026-11-10"
date_clipped: "2026-11-14"
category: ".NET Ecosystem"
source_type: "web"
---

# Announcing PowerShell 7.7 GA Release

We’re excited to announce the General Availability of PowerShell 7.7, the next Standard Term Support
(STS) release of PowerShell. PowerShell 7.7 is built on .NET 11, continuing the alignment between
PowerShell and the modern .NET platform.

PowerShell 7.7 focuses on security hardening, new and improved commands, and reliability across the
engine, remoting, and interactive shell experience.

Notable areas of improvement include:

- Security hardening across Constrained Language Mode, remoting, and help
- New commands and parameters
- More predictable handling of switch parameters
- Startup, tab completion, and file system fixes
- Module updates

For support dates, see the [PowerShell support lifecycle](https://learn.microsoft.com/powershell/scripting/install/powershell-support-lifecycle) article.

## Highlights

- PowerShell 7.7 is built on .NET 11
- PowerShell 7.7 includes updates to the following modules:
  - Microsoft.PowerShell.PSResourceGet
  - Microsoft.PowerShell.Archive
- New and improved commands
  - Added the `New-TemporaryDirectory` cmdlet
  - Added the `-Extension` parameter to `Join-Path`
  - Added the `-ExcludeProperty` parameter to `Format-Table`, `Format-List`, and `Format-Custom`
  - `Get-AuthenticodeSignature` now returns a `SubjectAlternativeName` property
  - Added a `ToRegex()` method to `WildcardPattern`
  - `New-Guid` now generates version 7 (time-sortable) UUIDs by default
- Security hardening
  - Additional protections for Constrained Language Mode, including property assignment on
    non-core objects
  - Stronger argument and frame validation in PowerShell remoting, and restored schema validation
    in the CIM cmdlets
  - Implicit remoting protections now apply to resolved aliases
  - Stricter validation when extracting updatable help
  - Tighter file permissions for the fallback temporary home directory on Unix platforms
  - `Test-Json` no longer resolves external schema references unless you ask it to
- More predictable switch parameters
  - Explicit `-Switch:$false` values are now respected by `Split-Path`, `New-PSSession`,
    `Test-Connection`, `Get-TimeZone`, `Get-Random`, `Get-SecureRandom`, `Get-Uptime`, and
    `New-Guid`, and by the operator parameters of `Where-Object`
- Reliability and quality improvements
  - A damaged or unreadable per-user `powershell.config.json` no longer stops PowerShell from
    starting
  - Fixed `Resolve-Path -Relative` for names that begin with a dot
  - Fixed duplicate results from `Get-Command` fuzzy matching
  - Fixed `Clear-Host` for remote Windows sessions from non-Windows platforms
  - Fixed tab completion of positional parameters and completion for `$PSBoundParameters.Keys`
  - Improved handling of custom argument completers that return empty or null results
  - Fixed `pwsh -file` dot-sourcing of advanced-function scripts
  - Fixed progress bar rendering for double-width Unicode characters
- Telemetry now respects the Windows diagnostics and feedback setting

## A quick example

`New-TemporaryDirectory` creates a uniquely named directory in the system temp folder and returns a
`DirectoryInfo` object. Use `-Prefix` to make the directory easier to recognize:

```
# Create a uniquely named directory in the system temp folder

$workDir = New-TemporaryDirectory -Prefix build

$workDir.FullName



# Remove it when you're done

Remove-Item -LiteralPath $workDir.FullName -Recurse
```

## Breaking changes

PowerShell 7.7 includes a small number of breaking changes. Review them before you upgrade
production scripts.

- `New-Guid` generates version 7 (time-sortable) UUIDs by default instead of version 4. Use
  `[guid]::NewGuid()` when you need a fully random GUID.
- `Format-Table`, `Format-List`, and `Format-Custom` now validate that `-Property` is not null or
  empty.
- Null-or-empty argument validation now throws `System.ArgumentException`.
- Explicit false values for `Where-Object` operator switches, such as `-EQ:$false`, are now handled correctly.

## Other behavior changes

These changes might also affect existing scripts:

- The update notification feature was removed from PowerShell.
- `Test-Json` requires `-FetchExternalReference` to resolve external schema references.
- `Export-Csv` no longer accepts `-Append` together with `-NoHeader`. Using `-NoTypeInformation`
  on the CSV cmdlets now writes a deprecation warning and has no effect.
- `Get-ChildItem -Name` with `-Recurse` now returns matching files in subdirectories when the path
  contains a wildcard or names a file.
- Constrained Language Mode restricts property assignment on non-core objects, including through
  `ForEach()`.

## Community contributions

PowerShell is built by a global community of users and contributors. Thank you to everyone who
filed issues, tested previews, improved docs, and submitted fixes during the PowerShell 7.7
release cycle.

We want to give a special thanks to the community members who spent the most time helping
others in the repository this release:

- **Top pull request commenters:** @iSazonov, @muffy86, and @KirtiRamchandani
- **Top issue commenters:** @mklement0, @237dmitry, and @rhubarb-geek-nz

The following individuals contributed code to the PowerShell 7.7 release:

- @adamdriscoll, @amritanand-py, @behradbhrmi, @cuiweixie, @jborean93
- @jorgeasaurus, @kasperk81, @KirtiRamchandani, @logiclrd, @MartinGC94
- @MathiasMagnus, @mikkas456, @powercode, @reabr, @rwp0
- @scuzqy, @SufficientDaikon, @ThioJoe, @trackd, @xtqqczze
- @yotsuda, @yuunnn

## Call to action

Install PowerShell 7.7 now.

For more information, see the following articles:

- [Install PowerShell on Windows, Linux, and macOS](https://learn.microsoft.com/powershell/scripting/install/install-powershell)
- [What’s New in PowerShell 7.7](https://learn.microsoft.com/powershell/scripting/whats-new/what-s-new-in-powershell-77)

## Looking ahead

We continue to work on future releases of PowerShell. Preview releases will continue to provide
early access to new capabilities and improvements, and your feedback on them helps us ship with
confidence.

PowerShell Team
