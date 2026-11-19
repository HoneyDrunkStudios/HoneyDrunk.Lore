---
"source": "https://learn.microsoft.com/en-us/dotnet/core/compatibility/11"
"title": "Breaking changes in .NET 11"
"author": "gewarren"
"date_published": "unknown"
"date_clipped": "2026-11-17"
"category": ".NET Ecosystem"
"source_type": "web"
---

# Breaking changes in .NET 11

If you're migrating an app to .NET 11, the breaking changes listed here might affect you. Changes are grouped by technology area, such as ASP.NET Core or Windows Forms.

This article categorizes each breaking change as *binary incompatible* or *source incompatible*, or as a *behavioral change*:

- **Binary incompatible** - When run against the new runtime or component, existing binaries may encounter a breaking change in behavior, such as failure to load or execute, and if so, require recompilation.
- **Source incompatible** - When recompiled using the new SDK or component or to target the new runtime, existing source code may require source changes to compile successfully.
- **Behavioral change** - Existing code and binaries may behave differently at runtime. If the new behavior is undesirable, existing code would need to be updated and recompiled.

Note

This article is a work in progress. It's not a complete list of breaking changes in .NET 11.

## ASP.NET Core

See [Breaking changes in ASP.NET Core 11](https://learn.microsoft.com/en-us/aspnet/core/breaking-changes/11/overview).

## Containers

| Title | Type of change |
| --- | --- |
| [dotnet test needs a writable VSTest artifacts base directory in containers](https://learn.microsoft.com/en-us/dotnet/core/compatibility/containers/11/vstest-artifacts-base-directory) | Behavioral change |

## Core .NET libraries

| Title | Type of change |
| --- | --- |
| [Assembly.GetCallingAssembly behavior changes when stack trace support is disabled](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/assembly-getcallingassembly-stacktracesupport-disabled) | Behavioral change |
| [CborReader and CborWriter enforce a default maximum nesting depth](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/cbor-max-depth) | Behavioral change |
| [Complex special-value results now follow C23 Annex G](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/complex-annex-g-special-values) | Behavioral change |
| [CRC32 validation added when reading ZIP archive entries](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/ziparchive-entry-crc32-validation) | Behavioral change |
| [DateOnly and TimeOnly TryParse methods throw for invalid input](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/dateonly-timeonly-tryparse-argumentexception) | Behavioral change |
| [Decimal and BigInteger floating-point conversions are correctly rounded](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/decimal-biginteger-floating-point-conversions) | Behavioral change |
| [DeflateStream and GZipStream write headers and footers for empty payload](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/deflatestream-gzipstream-empty-payload) | Behavioral change |
| [Environment.GetCommandLineArgs()[0] preserves the apphost invocation name](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/environment-getcommandlineargs-apphost-invocation-name) | Behavioral change |
| [Environment.TickCount made consistent with Windows timeout behavior](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/environment-tickcount-windows-behavior) | Behavioral change |
| [Generated WMI collection and enumerator wrappers implement IDisposable](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/wmi-wrappers-implement-idisposable) | Source/behavioral change |
| [Math.Round and MathF.Round return correctly rounded results](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/math-round-digits) | Behavioral change |
| [Named mutexes default to user scope on Unix](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/named-mutexes-unix-default-scope) | Behavioral change |
| [NamedPipeServerStream with PipeOptions.CurrentUserOnly tightens Unix socket file permissions](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/namedpipeserverstream-unix-permissions) | Behavioral change |
| [Nullable.GetUnderlyingType throws for custom Type subclasses](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/nullable-getunderlyingtype-throws) | Behavioral change |
| [PackagePart.GetStream() returns a non-seekable stream for compressed parts in ReadWrite packages](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/packagepart-getstream-non-seekable) | Behavioral change |
| [API obsoletions with non-default diagnostic IDs (.NET 11)](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/obsolete-apis) | Source incompatible |
| [SafeFileHandle.IsAsync and FileStream.IsAsync accurately reflect non-blocking state on Unix](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/safefilehandle-isasync-unix) | Behavioral change |
| [TAR-reading APIs verify header checksums when reading](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/tar-checksum-validation) | Behavioral change |
| [TarWriter uses HardLink entries for hard-linked files](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/tarwriter-hardlink-entries) | Behavioral change |
| [Tensor operations align equivalent shapes and empty tensors](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/tensor-shape-alignment) | Behavioral change |
| [Tensor operations reject unsupported storage layouts](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/tensor-storage-layout-validation) | Behavioral change |
| [ZipArchive.CreateAsync eagerly loads ZIP archive entries](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/ziparchive-createasync-eager-load) | Behavioral change |

## Cryptography

| Title | Type of change |
| --- | --- |
| [API obsoletions](https://learn.microsoft.com/en-us/dotnet/core/compatibility/cryptography/11/obsolete-apis) | Source incompatible |
| [Composite ML-DSA on Windows uses native implementation](https://learn.microsoft.com/en-us/dotnet/core/compatibility/cryptography/11/compositemldsa-windows-native) | Behavioral change |
| [DSA removed from macOS](https://learn.microsoft.com/en-us/dotnet/core/compatibility/cryptography/11/dsa-removed-macos) | Behavioral change |
| [HKDF on Windows uses CNG implementation](https://learn.microsoft.com/en-us/dotnet/core/compatibility/cryptography/11/hkdf-windows-cng) | Behavioral change |
| [Linux AIA certificate fetching limited to two fetches per chain build](https://learn.microsoft.com/en-us/dotnet/core/compatibility/cryptography/11/aia-fetch-limit-linux) | Behavioral change |

## Deployment

| Title | Type of change |
| --- | --- |
| [configProperties in .runtimeconfig.dev.json override .runtimeconfig.json](https://learn.microsoft.com/en-us/dotnet/core/compatibility/deployment/11/runtimeconfigdev-configproperties-precedence) | Behavioral change |

## Extensions

| Title | Type of change |
| --- | --- |
| [ChangeToken.OnChange async overloads rebind existing Task-returning callbacks](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/changetoken-onchange-async-overloads-rebind-callbacks) | Behavioral change |
| [Dependency injection scope disposal aggregates exceptions](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/dependency-injection-disposal-exceptions) | Behavioral change |
| [Empty strings in chained configuration override earlier providers](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/chained-configuration-empty-string) | Behavioral change |
| [FileConfigurationProvider doesn't raise reload token after ignored load failure](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/fileconfigurationprovider-reload-token-load-failure) | Behavioral change |
| [FileConfigurationSource.OnLoadException callback is called for IO errors](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/fileconfigurationsource-onloadexception-io-errors) | Behavioral change |
| [IHost.RunAsync and IHost.StopAsync throw when a BackgroundService fails](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/ihost-runasync-stopasync-throw-backgroundservice-failure) | Behavioral change |
| [Options validation generator reports SYSLIB1205 for explicit Validate implementations](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/options-validator-explicit-validate) | Source incompatible |
| [PhysicalFilesWatcher validates root and FileSystemWatcher paths](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/physicalfileswatcher-validates-root-path) | Behavioral change |
| [Some Microsoft.Extensions packages included in shared framework](https://learn.microsoft.com/en-us/dotnet/core/compatibility/extensions/11/extensions-in-shared-framework) | Behavioral change |

## Globalization

| Title | Type of change |
| --- | --- |
| [Japanese Calendar minimum supported date corrected](https://learn.microsoft.com/en-us/dotnet/core/compatibility/globalization/11/japanese-calendar-min-date) | Behavioral change |

## Interop

| Title | Type of change |
| --- | --- |
| [Native AOT rejects non-blittable UnmanagedCallersOnly signatures](https://learn.microsoft.com/en-us/dotnet/core/compatibility/interop/11/unmanagedcallersonly-non-blittable) | Behavioral change |
| [NativeAOT uses lib prefix for native library outputs on Unix](https://learn.microsoft.com/en-us/dotnet/core/compatibility/interop/11/nativeaot-lib-prefix) | Behavioral change |

## JIT compiler

| Title | Type of change |
| --- | --- |
| [Floating-point conversions to small integral types are saturating](https://learn.microsoft.com/en-us/dotnet/core/compatibility/jit/11/fp-to-small-integer) | Behavioral change |
| [Minimum hardware requirements updated](https://learn.microsoft.com/en-us/dotnet/core/compatibility/jit/11/minimum-hardware-requirements) | Behavioral change |

## Networking

| Title | Type of change |
| --- | --- |
| [HttpClient high-cardinality metrics use observable counters](https://learn.microsoft.com/en-us/dotnet/core/compatibility/networking/11/http-metrics-observable-counters) | Behavioral change |
| [SslStream server-side AIA certificate downloads disabled by default](https://learn.microsoft.com/en-us/dotnet/core/compatibility/networking/11/sslstream-aia-downloads-disabled) | Behavioral change |

## .NET MAUI

| Title | Type of change |
| --- | --- |
| [Android x86 is not supported](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/android-x86-unsupported) | Binary incompatible/behavioral change |
| [Code generation on mobile changes from Mono to CoreCLR](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/mobile-code-generation) | Source incompatible/behavioral change |
| [CoreCLR replaces Mono runtime for .NET mobile apps](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/mobile-runtime-replacement) | Binary/source incompatible/behavioral change |
| [CoreCLR trace events replace Mono trace events](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/runtime-trace-events) | Binary/source incompatible/behavioral change |
| [Crash-reporting behavior changes on mobile platforms](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/mobile-crash-reporting) | Behavioral change |
| [Debugging interfaces on mobile platforms changing to `ICorDebug`](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/mobile-debugger-interfaces) | Binary/source incompatible/behavioral change |
| [Minimum Android API level raised to 24](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/android-minimum-api-level) | Behavioral change |
| [Mono embedding APIs no longer supported on mobile platforms](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/mono-embedding-apis) | Binary/source incompatible/behavioral change |
| [Mono project properties no longer configure mobile apps](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/mono-project-properties) | Source incompatible/behavioral change |
| [Mono runtime settings no longer configure mobile apps](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/mono-runtime-settings) | Behavioral/source incompatible |
| [UnwindNativeCode isn't supported on Apple targets](https://learn.microsoft.com/en-us/dotnet/core/compatibility/maui/11/unwind-native-code-apple) | Source incompatible/behavioral change |

## SDK and MSBuild

| Title | Type of change |
| --- | --- |
| [dnx scripts bypass global.json SDK selection](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/dnx-scripts-bypass-global-json) | Behavioral change |
| [Full build skipped for Native AOT publish](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/aot-publish-skips-full-build) | Behavioral change |
| [mono launch target not set for .NET Framework apps](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/mono-launch-target-removed) | Behavioral change |
| [NativeAOT CLI command handling enabled by default](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/native-cli-command-handling-enabled) | Behavioral change |
| [NU1703 warns for packages that use deprecated MonoAndroid framework assets](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/nu1703-deprecated-monoandroid-framework) | Source incompatible |
| [NuGet locks directory moved on Linux](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/nuget-locks-directory-linux) | Behavioral change |
| [NuGet pack warns for package IDs with restricted characters](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/nuget-pack-nu5052-packageid) | Behavioral change |
| [Restore doesn't search global packages folder for higher version](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/restore-global-packages-folder-version-search) | Source incompatible |
| [SDK local container runtime selection prefers platform-native tools](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/native-local-container-runtimes) | Behavioral change |
| [Template engine packages no longer support netstandard2.0](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/template-engine-netstandard) | Binary/source incompatible |
| [Template package installation verifies NuGet signatures](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/template-package-signature-verification) | Behavioral change |
| [VSTest removes dependency on Newtonsoft.Json](https://learn.microsoft.com/en-us/dotnet/core/compatibility/sdk/11/vstest-removes-newtonsoft-json) | Binary/source incompatible |
