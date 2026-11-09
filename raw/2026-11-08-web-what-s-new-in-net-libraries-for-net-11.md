---
source: "https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries"
title: "What's new in .NET libraries for .NET 11"
author: "gewarren"
date_published: "unknown"
date_clipped: "2026-11-08"
category: ".NET Ecosystem"
source_type: "web"
capture_note: "Official documentation snapshot explicitly last updated for .NET 11 RC 2; this is not a final-release or latest-RC assertion."
---

# What's new in .NET libraries for .NET 11

This article describes new features in the .NET libraries for .NET 11. It was last updated for release candidate 2 (RC 2).

## Diagnostics and process execution

- [Process API expansion](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#process-api-expansion)
- [Console FORCE\_COLOR support](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#console-force_color-support)

### Process API expansion

[Process](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process) has a substantial set of new APIs that cover common scenarios where you previously had to wire up [OutputDataReceived](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.outputdatareceived#system-diagnostics-process-outputdatareceived)/[ErrorDataReceived](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.errordatareceived#system-diagnostics-process-errordatareceived) events manually or use P/Invoke.

#### Run-and-capture helpers

New one-shot APIs let you launch a process and get its result without manual setup:

```
// One-shot capture: stdout and stderr together, plus exit code.
ProcessTextOutput result = await Process.RunAndCaptureTextAsync(
    "git", ["status", "--porcelain"]);

Console.WriteLine(result.StandardOutput);
Console.WriteLine($"Exit code: {result.ExitStatus.ExitCode}");
```

The full set of helpers includes:

- [Process.Run](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.run) and [Process.RunAsync](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.runasync) — launch a process and return an exit-status result.
- [Process.RunAndCaptureText](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.runandcapturetext) and [Process.RunAndCaptureTextAsync](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.runandcapturetextasync) — launch and capture stdout/stderr together with exit code.
- [Process.ReadAllText(Nullable<TimeSpan>)](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.readalltext#system-diagnostics-process-readalltext(system-nullable((system-timespan)))), [Process.ReadAllBytes(Nullable<TimeSpan>)](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.readallbytes#system-diagnostics-process-readallbytes(system-nullable((system-timespan)))), and their async variants — read a child process's standard output in a single call.
- [Process.ReadAllLines(Nullable<TimeSpan>)](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.readalllines#system-diagnostics-process-readalllines(system-nullable((system-timespan)))) — synchronously reads all lines of output from a child process, returning a sequence of [ProcessOutputLine](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processoutputline) values that distinguish stdout from stderr.
- [Process.ReadAllLinesAsync(CancellationToken)](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.readalllinesasync#system-diagnostics-process-readalllinesasync(system-threading-cancellationtoken)) — returns a stream of [ProcessOutputLine](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processoutputline) values that distinguish stdout from stderr without string parsing.

#### Fire-and-forget launches

- [Process.StartAndForget](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.startandforget) — starts a child process when you don't intend to wait for it; the runtime detaches the handle automatically.
- [ProcessStartInfo.StartDetached](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.startdetached#system-diagnostics-processstartinfo-startdetached) — detaches from the parent's session/console so the child can outlive a terminal exit.
- [ProcessStartInfo.KillOnParentExit](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.killonparentexit#system-diagnostics-processstartinfo-killonparentexit) (Windows only) — the child is terminated when the parent process exits.

#### SafeProcessHandle lifecycle methods

[SafeProcessHandle](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle) gains lifecycle methods for advanced scenarios:

- [SafeProcessHandle.Start(ProcessStartInfo)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle.start#microsoft-win32-safehandles-safeprocesshandle-start(system-diagnostics-processstartinfo)) and a new [SafeProcessHandle.ProcessId](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle.processid#microsoft-win32-safehandles-safeprocesshandle-processid) property — launch and identify processes without going through [Process](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process) itself.
- [SafeProcessHandle.Kill()](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle.kill#microsoft-win32-safehandles-safeprocesshandle-kill) and [SafeProcessHandle.Signal(PosixSignal)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle.signal#microsoft-win32-safehandles-safeprocesshandle-signal(system-runtime-interopservices-posixsignal)) — terminate or signal a process by handle.
- [SafeProcessHandle.WaitForExit()](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle.waitforexit#microsoft-win32-safehandles-safeprocesshandle-waitforexit) and [SafeProcessHandle.WaitForExitAsync(CancellationToken)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle.waitforexitasync#microsoft-win32-safehandles-safeprocesshandle-waitforexitasync(system-threading-cancellationtoken)) — wait for a process to exit by handle.

#### Tighter handle control

- [ProcessStartInfo.InheritedHandles](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.inheritedhandles#system-diagnostics-processstartinfo-inheritedhandles) — specify exactly which OS handles a child process inherits, instead of using the all-or-nothing `UseShellExecute = false` default.
- [ProcessStartInfo.StandardInputHandle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.standardinputhandle#system-diagnostics-processstartinfo-standardinputhandle), [ProcessStartInfo.StandardOutputHandle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.standardoutputhandle#system-diagnostics-processstartinfo-standardoutputhandle), and [ProcessStartInfo.StandardErrorHandle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.standarderrorhandle#system-diagnostics-processstartinfo-standarderrorhandle) — supply already-open [Microsoft.Win32.SafeHandles.SafeFileHandle](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safefilehandle) values for redirection without the framework opening new ones.

#### Suspended starts and process lookup

`System.Diagnostics.Process` adds finer control over starting and finding processes:

- [ProcessStartInfo.StartSuspended](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.startsuspended#system-diagnostics-processstartinfo-startsuspended) starts a process in a suspended state on Windows and macOS. Pair it with [SafeProcessHandle.Resume()](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle.resume#microsoft-win32-safehandles-safeprocesshandle-resume) to let it run once you've finished any setup, such as attaching a debugger or configuring job objects.
- [Process.TryGetProcessById(Int32, Process)](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.trygetprocessbyid#system-diagnostics-process-trygetprocessbyid(system-int32-system-diagnostics-process@)) returns `false` instead of throwing when no process with the given ID exists.
- [Open(Int32)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle.open#microsoft-win32-safehandles-safeprocesshandle-open(system-int32)) and [TryOpen(Int32, SafeProcessHandle)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle.tryopen#microsoft-win32-safehandles-safeprocesshandle-tryopen(system-int32-microsoft-win32-safehandles-safeprocesshandle@)) open a handle to an existing process by ID.

```
var startInfo = new ProcessStartInfo("worker.exe") { StartSuspended = true };
using var process = Process.Start(startInfo)!;

// Attach diagnostics or configure job objects while the process is suspended,
// then call Resume to start execution once your setup is complete.
AttachProfiler(process);
process.SafeHandle.Resume();
```

#### Signal processes and inspect termination status

[Process](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process) exposes process signaling and exit-status APIs directly, without requiring you to work through [SafeProcessHandle](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safeprocesshandle):

- [Process.Signal(PosixSignal)](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.signal#system-diagnostics-process-signal(system-runtime-interopservices-posixsignal)) sends a POSIX signal to the process.
- [Process.WaitForExitStatus()](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.waitforexitstatus#system-diagnostics-process-waitforexitstatus), [Process.TryWaitForExitStatus(TimeSpan, ProcessExitStatus)](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.trywaitforexitstatus#system-diagnostics-process-trywaitforexitstatus(system-timespan-system-diagnostics-processexitstatus@)), and [Process.WaitForExitStatusAsync(CancellationToken)](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.waitforexitstatusasync#system-diagnostics-process-waitforexitstatusasync(system-threading-cancellationtoken)) return a [ProcessExitStatus](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processexitstatus), which distinguishes a normal exit from a signal-based termination.

```
if (OperatingSystem.IsLinux() || OperatingSystem.IsMacOS())
{
    using Process process = Process.Start("sleep", "30")!;
    process.Signal(PosixSignal.SIGTERM);
    ProcessExitStatus status = await process.WaitForExitStatusAsync();
    Console.WriteLine(status);
}
```

### Console FORCE\_COLOR support

.NET console output now honors the [`FORCE_COLOR`](https://force-color.org/) standard alongside the existing `NO_COLOR` support. When `FORCE_COLOR` is set, [Console.IsOutputRedirected](https://learn.microsoft.com/en-us/dotnet/api/system.console.isoutputredirected#system-console-isoutputredirected) no longer suppresses ANSI escape codes. This is useful when you pipe `dotnet run` output through `tee`, into a CI log viewer, or through `less -R`:

```
FORCE_COLOR=1 dotnet run | tee build.log
```

## In-memory stream adapters

Four new `Stream` types wrap common in-memory data so you can pass them to any API that expects a `Stream`, without copying into a `MemoryStream` first:

- `ReadOnlyMemoryStream` exposes a `ReadOnlyMemory<byte>` as a read-only stream.
- `WritableMemoryStream` exposes a writable `Memory<byte>` as a fixed-size stream.
- `ReadOnlySequenceStream` exposes a `ReadOnlySequence<byte>` (for example, buffers from `System.IO.Pipelines`) as a stream without flattening it.
- `StringStream` reads a `string` or `ReadOnlyMemory<char>` as a stream using a specified encoding.

```
using System.IO;
using System.Text;

// Pass a string to an API that takes a Stream, with no intermediate byte[] needed.
using Stream config = new StringStream(yamlText, Encoding.UTF8);
var settings = ParseConfiguration(config);

// Expose an existing buffer as a read-only stream, for example as an HTTP request body.
ReadOnlyMemory<byte> payload = GetPayload();
using Stream body = new ReadOnlyMemoryStream(payload);
await httpClient.PostAsync(uri, new StreamContent(body));
```

`ReadOnlySequenceStream` is especially useful with `System.IO.Pipelines`, because it streams directly over the segments of a `ReadOnlySequence<byte>` instead of allocating a contiguous copy.

## Text, serialization, and data handling

- [String and character enhancements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#string-and-character-enhancements)
- [Base64 encoding improvements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#base64-encoding-improvements)
- [UTF validation and invalid-subsequence search](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#utf-validation-and-invalid-subsequence-search)
- [System.Text.Json improvements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#systemtextjson-improvements)
- [Regular expression improvements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#regular-expression-improvements)
- [Read CBOR incrementally](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#read-cbor-incrementally)

### String and character enhancements

.NET 11 introduces significant enhancements to string and character manipulation APIs, making it easier to work with Unicode characters and runes.

#### Rune support in String methods

The [String](https://learn.microsoft.com/en-us/dotnet/api/system.string) class now includes methods that accept [Rune](https://learn.microsoft.com/en-us/dotnet/api/system.text.rune) parameters, enabling you to search, replace, and manipulate strings using Unicode scalar values directly. These new methods include:

- `Contains` - Check if a string contains a specific rune: [String.Contains(Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.string.contains#system-string-contains(system-text-rune)) and [String.Contains(Rune, StringComparison)](https://learn.microsoft.com/en-us/dotnet/api/system.string.contains#system-string-contains(system-text-rune-system-stringcomparison)).
- `StartsWith` and `EndsWith` - Check if a string starts or ends with a specific rune: [String.StartsWith(Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.string.startswith#system-string-startswith(system-text-rune)), [String.StartsWith(Rune, StringComparison)](https://learn.microsoft.com/en-us/dotnet/api/system.string.startswith#system-string-startswith(system-text-rune-system-stringcomparison)), [String.EndsWith(Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.string.endswith#system-string-endswith(system-text-rune)), and [String.EndsWith(Rune, StringComparison)](https://learn.microsoft.com/en-us/dotnet/api/system.string.endswith#system-string-endswith(system-text-rune-system-stringcomparison)).
- `IndexOf` and `LastIndexOf` - Find the position of a rune in a string: [String.IndexOf(Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.string.indexof#system-string-indexof(system-text-rune)), [String.IndexOf(Rune, StringComparison)](https://learn.microsoft.com/en-us/dotnet/api/system.string.indexof#system-string-indexof(system-text-rune-system-stringcomparison)), [String.LastIndexOf(Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.string.lastindexof#system-string-lastindexof(system-text-rune)), and [String.LastIndexOf(Rune, StringComparison)](https://learn.microsoft.com/en-us/dotnet/api/system.string.lastindexof#system-string-lastindexof(system-text-rune-system-stringcomparison)).
- `Replace` - Replace occurrences of one rune with another: [String.Replace(Rune, Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.string.replace#system-string-replace(system-text-rune-system-text-rune)).
- `Split` - Split a string using a rune as the separator: [String.Split(Rune, StringSplitOptions)](https://learn.microsoft.com/en-us/dotnet/api/system.string.split#system-string-split(system-text-rune-system-stringsplitoptions)) and [String.Split(Rune, Int32, StringSplitOptions)](https://learn.microsoft.com/en-us/dotnet/api/system.string.split#system-string-split(system-text-rune-system-int32-system-stringsplitoptions)).
- `Trim`, `TrimStart`, and `TrimEnd` - Trim runes from strings: [String.Trim(Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.string.trim#system-string-trim(system-text-rune)), [String.TrimStart(Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.string.trimstart#system-string-trimstart(system-text-rune)), and [String.TrimEnd(Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.string.trimend#system-string-trimend(system-text-rune)).

Many of these methods include overloads that accept a [StringComparison](https://learn.microsoft.com/en-us/dotnet/api/system.stringcomparison) parameter for culture-aware comparisons.

#### Char.Equals with StringComparison

The [Char](https://learn.microsoft.com/en-us/dotnet/api/system.char) struct now includes an [Char.Equals(Char, StringComparison)](https://learn.microsoft.com/en-us/dotnet/api/system.char.equals#system-char-equals(system-char-system-stringcomparison)) method that accepts a [StringComparison](https://learn.microsoft.com/en-us/dotnet/api/system.stringcomparison) parameter, allowing you to compare characters using culture-aware or ordinal comparisons.

#### Rune support in TextInfo

The [TextInfo](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.textinfo) class now provides [TextInfo.ToLower(Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.textinfo.tolower#system-globalization-textinfo-tolower(system-text-rune)) and [TextInfo.ToUpper(Rune)](https://learn.microsoft.com/en-us/dotnet/api/system.globalization.textinfo.toupper#system-globalization-textinfo-toupper(system-text-rune)) methods that accept [Rune](https://learn.microsoft.com/en-us/dotnet/api/system.text.rune) parameters, enabling you to perform case conversions on individual Unicode scalar values.

#### StringBuilder.MoveChunks

To transfer content without copying characters, use the new static [StringBuilder.MoveChunks(StringBuilder)](https://learn.microsoft.com/en-us/dotnet/api/system.text.stringbuilder.movechunks#system-text-stringbuilder-movechunks(system-text-stringbuilder)) method, which moves all content from a source `StringBuilder` to a new `StringBuilder`. After the call, the source `StringBuilder` has a length of 0:

```
var source = new StringBuilder("Hello, ");
source.Append("World!");

// MoveChunks transfers all content from source to a new StringBuilder.
// After the call, source contains no characters.
StringBuilder dest = StringBuilder.MoveChunks(source);
Console.WriteLine(dest);          // Hello, World!
Console.WriteLine(source.Length); // 0
```

### Base64 encoding improvements

.NET 11 adds new APIs and overloads to the existing [Base64](https://learn.microsoft.com/en-us/dotnet/api/system.buffers.text.base64) type, providing comprehensive support for Base64 encoding and decoding. These additions offer improved performance and flexibility compared to existing methods.

#### New Base64 APIs

The new APIs support encoding and decoding operations with various input and output formats:

- **Encoding to chars**: [EncodeToChars](https://learn.microsoft.com/en-us/dotnet/api/system.buffers.text.base64.encodetochars) and [EncodeToString](https://learn.microsoft.com/en-us/dotnet/api/system.buffers.text.base64.encodetostring)
- **Encoding to UTF-8**: [EncodeToUtf8](https://learn.microsoft.com/en-us/dotnet/api/system.buffers.text.base64.encodetoutf8)
- **Decoding from chars**: [DecodeFromChars](https://learn.microsoft.com/en-us/dotnet/api/system.buffers.text.base64.decodefromchars)
- **Decoding from UTF-8**: [DecodeFromUtf8](https://learn.microsoft.com/en-us/dotnet/api/system.buffers.text.base64.decodefromutf8)

These methods provide both high-level convenience methods (that allocate and return arrays or strings) and low-level span-based methods (for zero-allocation scenarios).

### UTF validation and invalid-subsequence search

[System.Text.Unicode](https://learn.microsoft.com/en-us/dotnet/api/system.text.unicode) has two new complementary features. [Utf16.IsValid(ReadOnlySpan<Char>)](https://learn.microsoft.com/en-us/dotnet/api/system.text.unicode.utf16.isvalid#system-text-unicode-utf16-isvalid(system-readonlyspan((system-char)))) answers whether a sequence is well-formed UTF-16 without scanning twice, and [Utf8.IndexOfInvalidSubsequence(ReadOnlySpan<Byte>)](https://learn.microsoft.com/en-us/dotnet/api/system.text.unicode.utf8.indexofinvalidsubsequence#system-text-unicode-utf8-indexofinvalidsubsequence(system-readonlyspan((system-byte)))) / [Utf16.IndexOfInvalidSubsequence(ReadOnlySpan<Char>)](https://learn.microsoft.com/en-us/dotnet/api/system.text.unicode.utf16.indexofinvalidsubsequence#system-text-unicode-utf16-indexofinvalidsubsequence(system-readonlyspan((system-char)))) return the position of the first ill-formed code-unit sequence (or `-1` for valid input). Together, these methods let parsers, validators, and serializers report precise errors instead of generic encoding-error messages.

```
ReadOnlySpan<byte> bytes = [0xC3, 0x28]; // invalid UTF-8
int badIndex = Utf8.IndexOfInvalidSubsequence(bytes); // 0

ReadOnlySpan<char> chars = "valid \uD83D\uDC4D end"; // valid UTF-16 (👍 emoji)
bool ok = Utf16.IsValid(chars); // true
```

### System.Text.Json improvements

#### Union serialization

**C# union types.** Starting in .NET 11, C# offers union types. For example, `Reading` can hold an `int` or a `string`:

```
public union Reading(int, string);
```

A `Reading` that holds `"hello"` round-trips as a JSON string:

```
Reading reading = new("hello");
string json = JsonSerializer.Serialize(reading);
Reading copy = JsonSerializer.Deserialize<Reading>(json);
Console.WriteLine(json); // "hello"
Console.WriteLine(copy.Value); // hello
```

The serializer writes the active case directly, without a wrapper or `$type` discriminator. The JSON output depends on the active case:

| Union state | JSON output |
| --- | --- |
| `string` case with value `"hello"` | `"hello"` |
| `int` case with value `42` | `42` |
| Default struct union with no active case | `null` |

By default, deserialization selects the case from the JSON token kind: number, string, Boolean, array, or object. Two object cases share a token kind, so the default classifier can't distinguish them. To select an object case by its root-level property names, use [JsonUnionAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonunionattribute) with the built-in [JsonUnionTypeStructuralClassifier](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonuniontypestructuralclassifier):

```
[JsonUnion(TypeClassifier = typeof(JsonUnionTypeStructuralClassifier))]
public union PetUnion(Dog, Cat);

public sealed record Dog(string Name, string Breed);

public sealed record Cat(string Name, int Lives);
```

```
PetUnion? pet = JsonSerializer.Deserialize<PetUnion>(
    """{"Name":"Misty","Lives":9}""",
    PetJsonContext.Default.PetUnion);

Console.WriteLine(pet?.Value is Cat); // True
```

The payload's `Lives` property selects `Cat`. The structural classifier narrows the candidate cases by root-level property names and required properties; it doesn't inspect property values or nested content. If the payload matches zero or multiple cases, deserialization throws [JsonException](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonexception). The classifier doesn't support multiple non-object cases with the same JSON token kind, nested unions, polymorphic cases, or [ReferenceHandler.Preserve](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.referencehandler.preserve#system-text-json-serialization-referencehandler-preserve).

For other case-selection rules, derive from [JsonTypeClassifierFactory](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsontypeclassifierfactory). The factory receives a [JsonTypeClassifierContext](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsontypeclassifiercontext) describing the union cases and creates a [JsonTypeClassifier](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsontypeclassifier) delegate that reads JSON and selects a case type. Register the factory on one union through [JsonUnionAttribute.TypeClassifier](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonunionattribute.typeclassifier#system-text-json-serialization-jsonunionattribute-typeclassifier), on an options instance through [JsonSerializerOptions.TypeClassifiers](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.typeclassifiers#system-text-json-jsonserializeroptions-typeclassifiers), or on a source-generated context through [JsonSourceGenerationOptionsAttribute.TypeClassifiers](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonsourcegenerationoptionsattribute.typeclassifiers#system-text-json-serialization-jsonsourcegenerationoptionsattribute-typeclassifiers).

[JsonNumberHandlingAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonnumberhandlingattribute) is honored on C# unions, and the source generator no longer reports [SYSLIB1227](https://learn.microsoft.com/en-us/dotnet/fundamentals/syslib-diagnostics/syslib1220-1229) for unions that use custom converters.

If a union declares separate `T` and `T?` cases, the serializer selects the nullable case for a `null` payload. A non-null payload is ambiguous without a custom classifier because both cases use the same JSON shape. If no case accepts `null`, JSON `null` deserializes to the default union value, which also serializes as `null`.

For language syntax, see [C# 15 union types](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15#union-types). For more about classifiers and advanced contract metadata such as [JsonTypeInfoKind.Union](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfokind#system-text-json-serialization-metadata-jsontypeinfokind-union) and [JsonUnionCaseInfo](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsonunioncaseinfo), see [Serialize union types](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/union-types).

**F# discriminated unions.** The serializer represents cases without fields as JSON strings and cases with fields as JSON objects that contain a `$type` discriminator:

```
type Shape =
    | Point
    | Circle of radius: float
    | Rectangle of height: float * length: float
```

| F# value | JSON output |
| --- | --- |
| `Point` | `"Point"` |
| `Circle 3.14` | `{"$type":"Circle","radius":3.14}` |
| `Rectangle(10.0, 20.0)` | `{"$type":"Rectangle","height":10,"length":20}` |

For cases without fields, deserialization accepts both `"Point"` and `{"$type":"Point"}`. Class, struct, and recursive unions are supported. [JsonSerializerOptions.PropertyNamingPolicy](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.propertynamingpolicy#system-text-json-jsonserializeroptions-propertynamingpolicy) applies to case and field names, while [JsonPropertyNameAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonpropertynameattribute) on a case takes precedence. You can also change the discriminator property through [JsonPolymorphicAttribute.TypeDiscriminatorPropertyName](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonpolymorphicattribute.typediscriminatorpropertyname#system-text-json-serialization-jsonpolymorphicattribute-typediscriminatorpropertyname).

Important

F# discriminated-union support uses reflection only. It doesn't support `System.Text.Json` source generation, trimming, or Native AOT.

#### JSON Lines output

Four [JsonSerializer.SerializeAsyncEnumerable](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializer.serializeasyncenumerable) overloads serialize an [IAsyncEnumerable<T>](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.iasyncenumerable-1) to either a [Stream](https://learn.microsoft.com/en-us/dotnet/api/system.io.stream) or [PipeWriter](https://learn.microsoft.com/en-us/dotnet/api/system.io.pipelines.pipewriter). For each output type, one overload accepts [JsonSerializerOptions](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions) and one accepts [JsonTypeInfo<T>](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfo-1).

With the default `topLevelValues: false`, the output remains one JSON array. Set `topLevelValues: true` to write canonical JSON Lines (JSONL). The serializer writes each value compactly and follows it with a line feed (LF), `\n`, including the final value. JSONL output uses LF regardless of [JsonSerializerOptions.NewLine](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.newline#system-text-json-jsonserializeroptions-newline) and ignores [JsonSerializerOptions.WriteIndented](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.writeindented#system-text-json-jsonserializeroptions-writeindented) so that each value occupies one line.

```
static async IAsyncEnumerable<int> GenerateNumbers()
{
    for (int i = 0; i < 5; i++)
    {
        yield return i;
        await Task.Yield();
    }
}

using var arrayStream = new MemoryStream();
PipeWriter arrayPipe = PipeWriter.Create(arrayStream);

// Write a JSON array: [0,1,2,3,4]
await JsonSerializer.SerializeAsyncEnumerable(
    arrayPipe,
    GenerateNumbers());
await arrayPipe.CompleteAsync();

using var jsonlStream = new MemoryStream();
PipeWriter jsonlPipe = PipeWriter.Create(jsonlStream);

// Write JSON Lines (one value per line): 0\n1\n2\n3\n4\n
await JsonSerializer.SerializeAsyncEnumerable(
    jsonlPipe,
    GenerateNumbers(),
    topLevelValues: true);
await jsonlPipe.CompleteAsync();
```

#### Polymorphic hierarchy support

For a C# `closed` hierarchy, the serializer can infer the derived types, including generic specializations, and assign deterministic discriminators. Configure inference at any of these scopes:

```
[JsonPolymorphic(InferClosedTypePolymorphism = true)]
closed record Shape;
record Circle(double Radius) : Shape;
record Square(double Length) : Shape;
```

- Set [JsonSerializerOptions.InferClosedTypePolymorphism](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.inferclosedtypepolymorphism#system-text-json-jsonserializeroptions-inferclosedtypepolymorphism) for reflection-based serialization or as a global runtime setting.
- Set [JsonSourceGenerationOptionsAttribute.InferClosedTypePolymorphism](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonsourcegenerationoptionsattribute.inferclosedtypepolymorphism#system-text-json-serialization-jsonsourcegenerationoptionsattribute-inferclosedtypepolymorphism) so the source generator creates the required metadata at compile time.
- Set [JsonPolymorphicAttribute.InferClosedTypePolymorphism](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonpolymorphicattribute.inferclosedtypepolymorphism#system-text-json-serialization-jsonpolymorphicattribute-inferclosedtypepolymorphism) to `true` on one hierarchy. Set it to `false` to opt that hierarchy out of a global setting.

Inference also works through nested closed hierarchies, so a `closed` type that derives from another `closed` type contributes its own derived types to the inferred list. Explicit [JsonDerivedTypeAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonderivedtypeattribute) registrations take precedence and replace the inferred list instead of extending it. If source-generated metadata doesn't contain inferred or explicitly registered derived types, enabling only the runtime option fails fast. A per-type opt-in on a type that isn't `closed` throws [InvalidOperationException](https://learn.microsoft.com/en-us/dotnet/api/system.invalidoperationexception) with reflection and produces a source-generation error. Combining a per-type opt-in with explicit derived-type registrations produces a source-generation warning because the explicit registrations replace inference.

Open generic derived-type registrations are also supported. For example, one attribute registers `Derived<T>` for every compatible closed `Base<T>`:

```
[JsonDerivedType(typeof(Derived<>), "derived")]
public class Base<T> { }
public class Derived<T> : Base<T> { }
```

The resolver supports these type-argument patterns:

| Pattern | Example resolution |
| --- | --- |
| Direct binding | `Base<int>` resolves `Derived<T> : Base<T>` to `Derived<int>`. |
| Reordered parameters | `Base<int, string>` resolves `Derived<U, V> : Base<V, U>` to `Derived<string, int>`. |
| Partially concrete parameters | `Base<string, int>` resolves `Derived<T> : Base<T, int>` to `Derived<string>`. |
| Nested or array parameters | `Base<List<int>>` resolves `Derived<T> : Base<List<T>>` to `Derived<int>`. |

The same rules apply to generic interfaces and types nested in generic outer types. The registration must resolve to exactly one closed derived type and satisfy its generic constraints. A ground-type mismatch, an unbound parameter, a constraint violation, an ambiguous match, or an incompatible shape throws [InvalidOperationException](https://learn.microsoft.com/en-us/dotnet/api/system.invalidoperationexception) with reflection. For source generation, an unresolved registration produces the [SYSLIB1229](https://learn.microsoft.com/en-us/dotnet/fundamentals/syslib-diagnostics/syslib1220-1229) warning, and the generated hierarchy still fails when the serializer configures it. Suppressing the warning doesn't make the registration valid.

For serializer configuration guidance, see [Infer polymorphism from a closed hierarchy](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/polymorphism#infer-polymorphism-from-a-closed-hierarchy) and [Configure open generic derived types](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/polymorphism#configure-open-generic-derived-types). For more information about the language feature, see [C# 15 closed hierarchies](https://learn.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-15#closed-hierarchies).

#### Source-generation and contract metadata

The `System.Text.Json` source generator supports more contract shapes, and the generated unsafe accessors are compatible with the updated C# unsafe semantics:

- Members marked with [JsonIncludeAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonincludeattribute) can have `private`, `internal`, or `protected` accessors. Private, internal, and protected fields are also supported when they're marked with `[JsonInclude]`.
- An inaccessible constructor marked with [JsonConstructorAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonconstructorattribute) can participate in deserialization.
- An omitted `init`-only property retains its property-initializer value. The generated contract sets the property after construction only when the JSON payload contains that property.

`JsonSerializer` also deserializes types with constructors whose parameters use `in`, `ref`, `out`, or `ref readonly`. The serializer binds `in`, `ref`, and `ref readonly` parameters by their element type. An `out` parameter doesn't bind a JSON constructor argument; the constructor receives an initialized output location, and a matching writable property can receive the JSON value after construction.

For more information, see [Source-generation modes in System.Text.Json](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/source-generation-modes) and [Use immutable types and properties](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/immutability).

Generic [JsonSerializerOptions.GetTypeInfo<T>()](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.gettypeinfo#system-text-json-jsonserializeroptions-gettypeinfo-1) and [JsonSerializerOptions.TryGetTypeInfo<T>(JsonTypeInfo<T>)](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.trygettypeinfo#system-text-json-jsonserializeroptions-trygettypeinfo-1(system-text-json-serialization-metadata-jsontypeinfo((-0))@)) methods return [JsonTypeInfo<T>](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsontypeinfo-1) without a manual cast. `GetTypeInfo<T>()` throws if the options can't resolve the type, while `TryGetTypeInfo<T>()` returns `false` in that case. Resolver and configuration exceptions can still propagate. These methods simplify metadata access in source-generation, Native AOT, and polymorphic serialization scenarios. For more information, see [Get strongly typed metadata](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/custom-contracts#get-strongly-typed-metadata).

```
JsonSerializerOptions options = new(JsonSerializerDefaults.Web);
options.MakeReadOnly(populateMissingResolver: true);

// Before: manual downcast required
JsonTypeInfo<MyRecord> info1 = (JsonTypeInfo<MyRecord>)options.GetTypeInfo(typeof(MyRecord));

// After: generic method returns the right type directly
JsonTypeInfo<MyRecord> info2 = options.GetTypeInfo<MyRecord>();

// TryGetTypeInfo variant for cases where the type may not be registered
if (options.TryGetTypeInfo<MyRecord>(out JsonTypeInfo<MyRecord>? typeInfo))
{
    // Use typeInfo
    _ = typeInfo;
}
```

#### Property names and ignore conditions

[JsonNamingPolicy.PascalCase](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonnamingpolicy.pascalcase#system-text-json-jsonnamingpolicy-pascalcase) and [JsonKnownNamingPolicy.PascalCase](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonknownnamingpolicy#system-text-json-serialization-jsonknownnamingpolicy-pascalcase) provide built-in PascalCase conversion. Apply [JsonNamingPolicyAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonnamingpolicyattribute) to a class, struct, interface, property, or field to select a naming policy at the type or member level.

Naming precedence, from highest to lowest, is [JsonPropertyNameAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonpropertynameattribute), a member-level `[JsonNamingPolicy]`, a type-level `[JsonNamingPolicy]`, [JsonSerializerOptions.PropertyNamingPolicy](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.propertynamingpolicy#system-text-json-jsonserializeroptions-propertynamingpolicy), and the original member name.

[JsonIgnoreAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonignoreattribute) can now set a default ignore condition on classes, structs, and interfaces. A member-level `[JsonIgnore]` takes precedence over the type-level condition, which takes precedence over [JsonSerializerOptions.DefaultIgnoreCondition](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions.defaultignorecondition#system-text-json-jsonserializeroptions-defaultignorecondition). [JsonIgnoreCondition.Always](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonignorecondition#system-text-json-serialization-jsonignorecondition-always) isn't valid at the type level; reflection throws [InvalidOperationException](https://learn.microsoft.com/en-us/dotnet/api/system.invalidoperationexception), while source generation reports `SYSLIB1226` and ignores the type-level attribute.

```
// Type-level JsonIgnore: all members use WhenWritingNull by default
// Type-level JsonNamingPolicy: ReleaseVersion uses snake_case
// Per-member JsonNamingPolicy: EventName uses camelCase even though the
// serializer options use PascalCase
var options = new JsonSerializerOptions
{
    PropertyNamingPolicy = JsonNamingPolicy.PascalCase
};

var data = new EventData { EventName = "Launch", ReleaseVersion = "11", Notes = null };
string json = JsonSerializer.Serialize(data, options);
Console.WriteLine(json);
// {"eventName":"Launch","release_version":"11"}  -- Notes omitted (null), EventName camel-cased
```

For more information, see [Apply a naming policy to a type or member](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/customize-properties#apply-a-naming-policy-to-a-type-or-member) and [Ignore properties based on a type-level condition](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/ignore-properties#ignore-properties-based-on-a-type-level-condition).

#### Converters and collection contracts

**Numeric converters.** The serializer includes built-in converters for [BFloat16](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.bfloat16), [Decimal32](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.decimal32), [Decimal64](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.decimal64), and [Decimal128](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.decimal128). The converters support number-handling options, dictionary keys, and JSON Schema export. For generated metadata, [JsonMetadataServices](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsonmetadataservices) exposes [JsonMetadataServices.BFloat16Converter](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsonmetadataservices.bfloat16converter#system-text-json-serialization-metadata-jsonmetadataservices-bfloat16converter), [JsonMetadataServices.Decimal32Converter](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsonmetadataservices.decimal32converter#system-text-json-serialization-metadata-jsonmetadataservices-decimal32converter), [JsonMetadataServices.Decimal64Converter](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsonmetadataservices.decimal64converter#system-text-json-serialization-metadata-jsonmetadataservices-decimal64converter), and [JsonMetadataServices.Decimal128Converter](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsonmetadataservices.decimal128converter#system-text-json-serialization-metadata-jsonmetadataservices-decimal128converter).

**Open generic converters.** [JsonConverterAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonconverterattribute) can reference an open generic converter on a generic type or member:

```
[JsonConverter(typeof(OptionConverter<>))]
public readonly struct Option<T> { }
```

The converter's total generic arity must match the target type's arity. The serializer closes the converter with the target type arguments without requiring [JsonConverterFactory](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonconverterfactory). For supported nesting patterns, constraints, and error behavior, see [Use open generic converters with `JsonConverter`](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/converters-how-to#use-open-generic-converters-with-jsonconverter).

**Extension data.** A member marked with [JsonExtensionDataAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonextensiondataattribute) can use [IReadOnlyDictionary<TKey,TValue>](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlydictionary-2) with `string` keys and either `object` or [JsonElement](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonelement) values. During deserialization, the serializer assigns a mutable [Dictionary<TKey,TValue>](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.dictionary-2) implementation. If the property already contains entries, the serializer copies them first and then adds JSON properties, so an incoming value replaces an existing value with the same key. A [JsonObject](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.nodes.jsonobject) extension-data member writes its child properties directly into the containing object. For example, an `Id` property and a `JsonObject` entry named `nested` produce `{"Id":1,"nested":true}`. For more information, see [Handle overflow JSON](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/handle-overflow#handle-overflow-json).

**Read-only sets.** [JsonSerializer](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializer) serializes [IReadOnlySet<T>](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.ireadonlyset-1) as a JSON array and deserializes it into a [HashSet<T>](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.hashset-1) instance. For source-generated metadata, [JsonMetadataServices.CreateIReadOnlySetInfo](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.metadata.jsonmetadataservices.createireadonlysetinfo) creates the collection contract.

For more information about built-in numeric and collection contracts, see [Supported types in System.Text.Json](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/supported-types).

#### Writer reuse

[Reset](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.utf8jsonwriter.reset) accepts a [JsonWriterOptions](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonwriteroptions) together with either a [Stream](https://learn.microsoft.com/en-us/dotnet/api/system.io.stream) or [IBufferWriter<T>](https://learn.microsoft.com/en-us/dotnet/api/system.buffers.ibufferwriter-1). After you flush one JSON document, you can reuse or pool the writer with a different output target and different options instead of constructing another writer instance:

```
using var stream = new MemoryStream();
using var writer = new Utf8JsonWriter(stream, new JsonWriterOptions { Indented = true });
writer.WriteStartObject();
writer.WriteString("name", "example");
writer.WriteEndObject();
writer.Flush();

// Reset with different options for next use — no new allocation needed
stream.SetLength(0);
writer.Reset(stream, new JsonWriterOptions { Indented = false });
```

For more information, see [Reuse a writer](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/use-utf8jsonwriter#reuse-a-writer).

You can also opt a single closed hierarchy in to this behavior with [JsonPolymorphicAttribute.InferClosedTypePolymorphism](https://learn.microsoft.com/en-us/dotnet/api/system.text.json.serialization.jsonpolymorphicattribute.inferclosedtypepolymorphism#system-text-json-serialization-jsonpolymorphicattribute-inferclosedtypepolymorphism), without changing the application-wide `JsonSerializerOptions` setting:

```
[JsonPolymorphic(InferClosedTypePolymorphism = true)]
public abstract record Shape;

public sealed record Circle(double Radius) : Shape;

public sealed record Square(double Side) : Shape;
```

### Regular expression improvements

#### AnyNewLine option

A new [RegexOptions.AnyNewLine](https://learn.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regexoptions#system-text-regularexpressions-regexoptions-anynewline) flag makes `^`, `$`, and `.` treat the full set of Unicode newline characters as line terminators—not just `\n`. This helps when parsing text that mixes Windows (`\r\n`), Unix (`\n`), and Unicode-specific (`\u0085`, `\u2028`, `\u2029`) line endings.

```
string text = "line1\r\nline2\u0085line3\u2028line4";

// RegexOptions.AnyNewLine makes ^, $, and . treat all Unicode newline
// sequences as line terminators, not just \n.
MatchCollection matches = Regex.Matches(
    text,
    @"^line\d$",
    RegexOptions.Multiline | RegexOptions.AnyNewLine);

Console.WriteLine(matches.Count); // 4
```

#### Regex engine and source generator fixes

.NET 11 includes several regex correctness and code-quality fixes:

- The non-backtracking engine no longer takes super-linear time on certain nested-loop patterns and produces correct results for cases that previously diverged.
- The regex compiler and source generator handle `resumeAt` correctly when a conditional appears inside a loop body.
- The [SYSLIB1045](https://learn.microsoft.com/en-us/dotnet/fundamentals/syslib-diagnostics/syslib1040-1049) code fixer no longer creates duplicate class names when applied across multiple partial declarations of the same class.

### Read CBOR incrementally

[CborReader](https://learn.microsoft.com/en-us/dotnet/api/system.formats.cbor.cborreader) can read a Concise Binary Object Representation (CBOR) payload that's delivered in chunks, without first copying the entire document into contiguous memory. To read incrementally:

1. Construct a reader with `isFinalBlock: false`.
2. Check for `CborReaderState.NeedsMoreData` to determine when the reader needs the next chunk.
3. Pass the next chunk to `CborReader.SlideData`, and set `isFinalBlock` to `true` for the last chunk.

Incremental reading requires [CborConformanceMode.Lax](https://learn.microsoft.com/en-us/dotnet/api/system.formats.cbor.cborconformancemode#system-formats-cbor-cborconformancemode-lax). Other conformance modes reject a non-final block.

```
ReadOnlyMemory<byte> firstChunk = new byte[] { 0x82, 0x0a };
ReadOnlyMemory<byte> nextChunk = new byte[] { 0x14 };

// Incremental reading requires CborConformanceMode.Lax.
var reader = new CborReader(
    firstChunk,
    new CborReaderOptions { ConformanceMode = CborConformanceMode.Lax },
    isFinalBlock: false);

reader.ReadStartArray();
int first = reader.ReadInt32(); // 10

if (reader.PeekState() == CborReaderState.NeedsMoreData)
{
    // Slide in the next chunk after the reader consumes all the buffered bytes.
    if (reader.BytesRemaining == 0)
    {
        reader.SlideData(nextChunk, isFinalBlock: true);
    }
    else
    {
        throw new InvalidOperationException("Buffer management omitted from the sample.");
    }
}

int second = reader.ReadInt32(); // 20
reader.ReadEndArray();
```

## Compression and archive formats

- [Compression enhancements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#compression-enhancements)
- [Zstandard compression](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#zstandard-compression)
- [Tar archive format selection](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#tar-archive-format-selection)

### Compression enhancements

.NET 11 includes several improvements to compression APIs.

#### ZIP archive entry access modes

The [ZipArchiveEntry](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.ziparchiveentry) class now supports opening entries with specific file access modes through new overloads: [ZipArchiveEntry.Open(FileAccess)](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.ziparchiveentry.open#system-io-compression-ziparchiveentry-open(system-io-fileaccess)) and [ZipArchiveEntry.OpenAsync(FileAccess, CancellationToken)](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.ziparchiveentry.openasync#system-io-compression-ziparchiveentry-openasync(system-io-fileaccess-system-threading-cancellationtoken)). These overloads accept a [FileAccess](https://learn.microsoft.com/en-us/dotnet/api/system.io.fileaccess) parameter and allow you to open ZIP entries for read, write, or read-write access.

Additionally, a new [CompressionMethod](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.ziparchiveentry.compressionmethod#system-io-compression-ziparchiveentry-compressionmethod) property exposes the compression method used for an entry through the [ZipCompressionMethod](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.zipcompressionmethod) enum, which includes values for [Stored](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.zipcompressionmethod#system-io-compression-zipcompressionmethod-stored), [Deflate](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.zipcompressionmethod#system-io-compression-zipcompressionmethod-deflate), and [Deflate64](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.zipcompressionmethod#system-io-compression-zipcompressionmethod-deflate64).

#### ZIP CRC32 validation

[ZipArchive](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.ziparchive) validates the CRC32 checksum when reading ZIP entries. Corrupted or truncated archives that previously passed without error now throw [InvalidDataException](https://learn.microsoft.com/en-us/dotnet/api/system.io.invaliddataexception), helping you detect data integrity issues early.

#### ZIP archive password support

[ZipArchiveEntry](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.ziparchiveentry) now supports password-protected entries for read and write operations. Use the new password-aware [ZipArchiveEntry.Open(ReadOnlySpan<Char>)](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.ziparchiveentry.open#system-io-compression-ziparchiveentry-open(system-readonlyspan((system-char)))) and [ZipArchiveEntry.OpenAsync(ReadOnlySpan<Char>, CancellationToken)](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.ziparchiveentry.openasync#system-io-compression-ziparchiveentry-openasync(system-readonlyspan((system-char))-system-threading-cancellationtoken)) overloads, and use password plus [ZipEncryptionMethod](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.zipencryptionmethod) when you create encrypted entries.

#### DeflateStream and GZipStream behavior change

Starting in .NET 11, [DeflateStream](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.deflatestream) and [GZipStream](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.gzipstream) always write format headers and footers to the output stream, even when no data is written. This ensures the output is a valid compressed stream according to the Deflate and GZip specifications.

Previously, these streams didn't produce any output if no data was written, resulting in an empty output stream. This change ensures compatibility with tools that expect properly formatted compressed streams.

For more information, see [DeflateStream and GZipStream write headers and footers for empty payload](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/deflatestream-gzipstream-empty-payload).

#### Span-based Deflate, ZLib, and GZip APIs

[System.IO.Compression](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression) now offers `Span<byte>`/`ReadOnlySpan<byte>` encode and decode entry points for the Deflate, ZLib, and GZip formats. The new APIs, on types such as [DeflateEncoder](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.deflateencoder), [ZLibEncoder](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.zlibencoder), and [GZipEncoder](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.gzipencoder), mirror the shape of [BrotliEncoder](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.brotliencoder)/[BrotliDecoder](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.brotlidecoder) and the Zstandard primitives. You can compress and decompress buffers without allocating a `Stream`. This is useful for high-throughput scenarios such as protocol parsers, log shippers, and middleware that already operate on spans.

```
ReadOnlySpan<byte> source = [0x48, 0x65, 0x6C, 0x6C, 0x6F]; // "Hello"
byte[] buffer = new byte[source.Length + 32];
Span<byte> destination = buffer;

using ZLibEncoder encoder = new();
OperationStatus status = encoder.Compress(
    source, destination, out int bytesConsumed, out int bytesWritten,
    isFinalBlock: true);

Console.WriteLine($"Compressed {bytesConsumed} bytes into {bytesWritten} bytes. Status: {status}");
```

The streamless `DeflateEncoder`, `DeflateDecoder`, `ZLibEncoder`, `ZLibDecoder`, `GZipEncoder`, and `GZipDecoder` types also gain a `Reset()` method. Resetting returns an instance to its initial state so you can process another independent payload without allocating a replacement encoder or decoder.

### Zstandard compression

The Zstandard compression APIs, for example, [ZstandardStream](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.zstandardstream) and [ZstandardEncoder](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression.zstandardencoder), are now part of the [System.IO.Compression](https://learn.microsoft.com/en-us/dotnet/api/system.io.compression) namespace, alongside `DeflateStream`, `GZipStream`, and `BrotliStream`. The API surface is otherwise unchanged.

### Tar archive format selection

New overloads on [CreateFromDirectory](https://learn.microsoft.com/en-us/dotnet/api/system.formats.tar.tarfile.createfromdirectory) and [CreateFromDirectoryAsync](https://learn.microsoft.com/en-us/dotnet/api/system.formats.tar.tarfile.createfromdirectoryasync) accept a [TarEntryFormat](https://learn.microsoft.com/en-us/dotnet/api/system.formats.tar.tarentryformat) parameter, giving you direct control over the archive format. Previously, `CreateFromDirectory` always produced Pax archives. The new overloads support all four tar formats—Pax, Ustar, GNU, and V7—for compatibility with specific tools and environments.

```
// Create a GNU format tar archive for Linux compatibility
TarFile.CreateFromDirectory("/source/dir", "/dest/archive.tar",
    includeBaseDirectory: true, format: TarEntryFormat.Gnu);

// Create a Ustar format archive for broader compatibility
using Stream outputStream = File.OpenWrite("/dest/ustar.tar");
TarFile.CreateFromDirectory("/source/dir", outputStream,
    includeBaseDirectory: false, format: TarEntryFormat.Ustar);

// Async version
CancellationToken cancellation[redacted-secret-like-value];
await TarFile.CreateFromDirectoryAsync("/source/dir", "/dest/archive.tar",
    includeBaseDirectory: true, format: TarEntryFormat.Pax,
    cancellation[redacted-secret-like-value]);
```

`TarReader` can now also read entries that use the GNU sparse format 1.0 (PAX) representation. The earlier 0.1 representation was already supported. With 1.0 support in place, `TarReader` matches what modern `tar` implementations write by default for sparse files.

## Collections, numerics, and low-level I/O

- [LINQ join improvements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#linq-join-improvements)
- [IEEE 754 decimal floating-point types](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#ieee-754-decimal-floating-point-types)
- [Correctly rounded decimal and BigInteger conversions](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#correctly-rounded-decimal-and-biginteger-conversions)
- [Partial numeric parsing](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#partial-numeric-parsing)
- [Generic Complex<T>](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#generic-complext)
- [BFloat16 support in BitConverter](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#bfloat16-support-in-bitconverter)
- [Floating-point hex formatting and parsing](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#floating-point-hex-formatting-and-parsing)
- [Numerics improvements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#numerics-improvements)
- [Random generic methods](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#random-generic-methods)
- [Cross-lane vector operations](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#cross-lane-vector-operations)
- [Low-level I/O improvements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#low-level-io-improvements)
- [Collections improvements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#collections-improvements)

### LINQ join improvements

LINQ adds join enhancements, including a new `FullJoin` operation and tuple-returning overloads for the existing `Join` and `GroupJoin` methods. These APIs are available on [Enumerable](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable), [Queryable](https://learn.microsoft.com/en-us/dotnet/api/system.linq.queryable), and [AsyncEnumerable](https://learn.microsoft.com/en-us/dotnet/api/system.linq.asyncenumerable).

#### LeftJoin, RightJoin, and FullJoin

Because the three outer-join operations return tuples directly, you can work with them easily using pattern matching and deconstruction:

- [Enumerable.LeftJoin](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.leftjoin) — Returns all elements from the left (outer) sequence. When there's no matching element in the right (inner) sequence, the inner element is `default` (typically `null` for reference types).
- [Enumerable.RightJoin](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.rightjoin) — Returns all elements from the right (inner) sequence. When there's no matching element in the left (outer) sequence, the outer element is `default` (typically `null` for reference types).
- [Enumerable.FullJoin](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.fulljoin) — Returns all elements from both sequences, using `default` on either side when there's no match.

```
var products = new List<(int Id, string Name, string? Category)>
{
    (1, "Laptop", "Electronics"),
    (2, "Mouse", "Electronics"),
    (3, "Orphan", null), // No matching category
};
var categories = new List<(string Name, string Description)>
{
    ("Electronics", "Electronic devices"),
    ("Furniture", "Office furniture"), // No matching product
};

// LeftJoin: all products, matched categories (null if none)
var leftJoined = products.LeftJoin(
    categories,
    p => p.Category,
    c => c.Name);

foreach (var (product, category) in leftJoined)
    Console.WriteLine($"{product.Name}: {category.Description ?? "(none)"}");
// Laptop: Electronic devices
// Mouse: Electronic devices
// Orphan: (none)

// FullJoin: all products and categories, paired where they match
var fullJoined = products.FullJoin(
    categories,
    p => p.Category,
    c => c.Name);

foreach (var (product, category) in fullJoined)
    Console.WriteLine(
        $"{product.Name ?? "(none)"}: {category.Description ?? "(none)"}");
// Laptop: Electronic devices
// Mouse: Electronic devices
// Orphan: (none)
// (none): Office furniture
```

### IEEE 754 decimal floating-point types

[System.Numerics](https://learn.microsoft.com/en-us/dotnet/api/system.numerics) adds [Decimal32](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.decimal32), [Decimal64](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.decimal64), and [Decimal128](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.decimal128), which implement IEEE 754-2019 decimal floating-point semantics. These types support generic math, infinities, and NaN values, and can help when you need IEEE decimal behavior instead of [Decimal](https://learn.microsoft.com/en-us/dotnet/api/system.decimal).

The transcendental functions on these types are more accurate. The most significant fix is for `Decimal128` values near a cancellation point, such as `Asin` and `Acos` near ±1 and logarithms near 1, where earlier builds could lose most or all significant digits. For example, `Decimal128.Acos(1 - 1e-30)` previously had an error of roughly 10²⁴ units in the last place (ULPs). It's now well under one ULP.

The change also improves the following behaviors:

- Inverse trigonometric and hyperbolic functions, logarithms, `Pow`, and `RootN` preserve decimal precision during argument reduction.
- `SinPi`, `CosPi`, `TanPi`, and `SinCosPi` return exact results, such as zero for integer inputs written with alternate decimal representations (for example, `SinPi(1000.000)`).
- `Log(x, base)` rounds only once for all three types.
- `Exp2`, `Exp2M1`, and subnormal-result rounding are more accurate.
- Alternate representations of `1`, such as `Acosh(1.0000000)`, no longer return NaN for `Decimal64` and `Decimal128`.

No public APIs were added. Because the rounded results intentionally change, code that compares these results against stored values might observe different last digits. The functions still aren't guaranteed to be correctly rounded.

### Correctly rounded decimal and BigInteger conversions

Conversions between [Decimal](https://learn.microsoft.com/en-us/dotnet/api/system.decimal) and binary floating-point types, and conversions from [BigInteger](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.biginteger) to binary floating-point types, now round the exact source value once to the nearest representable destination value. The previous conversions could lose significant digits or round through an intermediate value, so binaries rebuilt with a .NET 11 SDK can produce different results than they did on earlier versions. There's no compatibility switch to restore the previous conversion algorithms.

For example, converting the `double` literal `1.23` to `decimal` now preserves the exact binary floating-point value rather than producing `1.23`. If a value is meant to be decimal, use a decimal literal such as `1.23m` instead of converting a `double` literal. For complete guidance, including previous and new behavior for each conversion direction, see [Decimal and BigInteger floating-point conversions are correctly rounded](https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/11/decimal-biginteger-floating-point-conversions).

### Partial numeric parsing

[INumberBase<TSelf>.TryParsePartial](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.inumberbase-1.tryparsepartial) adds partial parsing overloads that report consumed input. Use this API to parse delimited formats, such as CSV, so you don't copy substrings.

### Generic Complex<T>

[Complex<T>](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.complex-1) is now available, so complex arithmetic can use several floating-point types, including `float`, `Half`, `BFloat16`, and the new decimal floating-point types.

#### Tuple-returning Join and GroupJoin overloads

New overloads of [Enumerable.Join](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.join) and [Enumerable.GroupJoin](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.groupjoin) return tuples directly without requiring a result selector, and accept an optional [IEqualityComparer<T>](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.iequalitycomparer-1) parameter. The optional comparer overload is also available on the `FullJoin`, `LeftJoin`, and `RightJoin` operations.

```
var products = new[] { (Id: 1, Name: "Laptop"), (Id: 2, Name: "Mouse") };
var orders = new[] { (ProductId: 1, Qty: 3), (ProductId: 1, Qty: 1) };

var result = products.Join(orders, p => p.Id, o => o.ProductId);
foreach (var (product, order) in result)
    Console.WriteLine($"{product.Name}: qty={order.Qty}");
// Laptop: qty=3
// Laptop: qty=1
```

### BFloat16 support in BitConverter

The [BitConverter](https://learn.microsoft.com/en-us/dotnet/api/system.bitconverter) class now includes methods for converting between [BFloat16](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.bfloat16) values and byte arrays or bit representations. These new methods include:

- [BitConverter.GetBytes(BFloat16)](https://learn.microsoft.com/en-us/dotnet/api/system.bitconverter.getbytes#system-bitconverter-getbytes(system-numerics-bfloat16)) - Convert a BFloat16 value to a byte array.
- [BitConverter.ToBFloat16(Byte[], Int32)](https://learn.microsoft.com/en-us/dotnet/api/system.bitconverter.tobfloat16#system-bitconverter-tobfloat16(system-byte()-system-int32)) and [BitConverter.ToBFloat16(ReadOnlySpan<Byte>)](https://learn.microsoft.com/en-us/dotnet/api/system.bitconverter.tobfloat16#system-bitconverter-tobfloat16(system-readonlyspan((system-byte)))) - Convert a byte array to a BFloat16 value.
- [BitConverter.BFloat16ToInt16Bits(BFloat16)](https://learn.microsoft.com/en-us/dotnet/api/system.bitconverter.bfloat16toint16bits#system-bitconverter-bfloat16toint16bits(system-numerics-bfloat16)), [BitConverter.BFloat16ToUInt16Bits(BFloat16)](https://learn.microsoft.com/en-us/dotnet/api/system.bitconverter.bfloat16touint16bits#system-bitconverter-bfloat16touint16bits(system-numerics-bfloat16)), [BitConverter.Int16BitsToBFloat16(Int16)](https://learn.microsoft.com/en-us/dotnet/api/system.bitconverter.int16bitstobfloat16#system-bitconverter-int16bitstobfloat16(system-int16)), and [BitConverter.UInt16BitsToBFloat16(UInt16)](https://learn.microsoft.com/en-us/dotnet/api/system.bitconverter.uint16bitstobfloat16#system-bitconverter-uint16bitstobfloat16(system-uint16)) - Methods for converting between BFloat16 and its bit representation as `short` or `ushort`.

BFloat16 (Brain Floating Point) is a 16-bit floating-point format that's commonly used in machine learning and scientific computing.

### Floating-point hex formatting and parsing

`double`, `float`, and `Half` can now be formatted and parsed in their hexadecimal IEEE-754 form. The hex form preserves every bit of the underlying value, making it the right choice for golden-file tests, cross-language interop with C/C++ `printf("%a", ...)`, and any scenario where round-tripping a `double` through decimal text is too lossy.

```
double value = Math.PI;

// Format as hexadecimal IEEE-754: preserves all bits exactly
string hex = value.ToString("X"); // e.g., "0X1.921FB54442D18P+1"
double roundTripped = double.Parse(hex, NumberStyles.HexFloat);

Console.WriteLine(roundTripped == value); // True — exact round-trip
```

### Numerics improvements

[Matrix4x4.GetDeterminant()](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.matrix4x4.getdeterminant#system-numerics-matrix4x4-getdeterminant) now uses an SSE-vectorized implementation, improving performance by approximately 15%.

### Random generic methods

[Random](https://learn.microsoft.com/en-us/dotnet/api/system.random) gains two new generic methods that work with any numeric type implementing the appropriate generic math interfaces:

- [Random.NextInteger](https://learn.microsoft.com/en-us/dotnet/api/system.random.nextinteger) — Generates a random integer of type `T` where `T` implements `IBinaryInteger<T>` and `IMinMaxValue<T>`. Overloads accept an upper bound or both lower and upper bounds.
- [Random.NextBinaryFloat](https://learn.microsoft.com/en-us/dotnet/api/system.random.nextbinaryfloat) — Generates a random floating-point value of type `T` where `T` implements `IBinaryFloatingPointIeee754<T>`.

```
// Generate a random integer of any binary integer type
int i = Random.Shared.NextInteger<int>();
long l = Random.Shared.NextInteger<long>(0L, 100L);
byte b = Random.Shared.NextInteger<byte>(maxValue: (byte)10);

// Generate a random floating-point value of any IEEE-754 type
float f = Random.Shared.NextBinaryFloat<float>();
double d = Random.Shared.NextBinaryFloat<double>();
Half h = Random.Shared.NextBinaryFloat<Half>();

Console.WriteLine($"int={i}, long={l}, byte={b}");
Console.WriteLine($"float={f}, double={d}, Half={h}");
```

### Cross-lane vector operations

`Vector64<T>`, `Vector128<T>`, `Vector256<T>`, `Vector512<T>`, and `Vector<T>` gain a set of lane construction and composition methods that previously required hand-written shuffles. The new methods fall into a few families:

- **Patterned construction:** `CreateGeometricSequence`, `CreateAlternatingSequence`, and `CreateHarmonicSequence` build a vector from a starting value and a rule.
- **Interleave and de-interleave:** `Zip`, `ZipLower`/`ZipUpper`, `Unzip`, `UnzipEven`/`UnzipOdd`.
- **Rearrange:** The `Concat` family (`ConcatLowerLower`, `ConcatLowerUpper`, `ConcatUpperLower`, `ConcatUpperUpper`) and `Reverse`.

```
using System.Runtime.Intrinsics;

// {1, 2, 4, 8} — each lane is the previous lane times two
Vector128<int> powers = Vector128.CreateGeometricSequence(1, 2);

// Interleave two vectors lane-by-lane
(Vector128<int> lower, Vector128<int> upper) =
    Vector128.Zip(Vector128.Create(1), Vector128.Create(2));
```

These building blocks are useful for image processing, audio digital signal processing (DSP), and other SIMD-intensive workloads that need fine-grained control over vector element layout, without falling back to platform-specific intrinsics.

### Low-level I/O improvements

- [SafeFileHandle pipe support](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#safefilehandle-pipe-support)
- [RandomAccess pipe support](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#randomaccess-pipe-support)
- [File locking on iOS and tvOS](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#file-locking-on-ios-and-tvos)

#### SafeFileHandle pipe support

[SafeFileHandle](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safefilehandle) gains two new members:

- **[SafeFileHandle.Type](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safefilehandle.type#microsoft-win32-safehandles-safefilehandle-type) property:** Reports whether a handle represents a file, pipe, socket, directory, or other OS object, without requiring platform-specific code.
- **[SafeFileHandle.CreateAnonymousPipe(SafeFileHandle, SafeFileHandle, Boolean, Boolean)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.safehandles.safefilehandle.createanonymouspipe#microsoft-win32-safehandles-safefilehandle-createanonymouspipe(microsoft-win32-safehandles-safefilehandle@-microsoft-win32-safehandles-safefilehandle@-system-boolean-system-boolean)) method:** Creates a pair of connected anonymous pipe handles with independent async behavior for each end.

```
SafeFileHandle.CreateAnonymousPipe(
    out SafeFileHandle readEnd,
    out SafeFileHandle writeEnd,
    asyncRead: true,
    asyncWrite: false);

using (readEnd)
using (writeEnd)
{
    // SafeFileHandle.Type reports the kind of OS object the handle refers to
    Console.WriteLine(readEnd.Type);   // Pipe
    Console.WriteLine(writeEnd.Type);  // Pipe
}
```

#### RandomAccess pipe support

[RandomAccess.Read](https://learn.microsoft.com/en-us/dotnet/api/system.io.randomaccess.read) and [RandomAccess.Write](https://learn.microsoft.com/en-us/dotnet/api/system.io.randomaccess.write) now work with non-seekable handles such as pipes, in addition to regular file handles.

On Windows, `Process` now uses overlapped I/O for redirected stdout/stderr, which reduces thread-pool blocking in process-heavy applications.

#### File locking on iOS and tvOS

On iOS and tvOS, [FileStream](https://learn.microsoft.com/en-us/dotnet/api/system.io.filestream) no longer acquires advisory file locks by default. This change avoids operating-system termination when an app is suspended while it holds a file lock. As a result, [FileShare](https://learn.microsoft.com/en-us/dotnet/api/system.io.fileshare) restrictions aren't enforced on those platforms, including between handles in the same process. Mac Catalyst and other platforms keep their existing defaults. To restore locking, set the `System.IO.DisableFileLocking` runtime configuration property to `false`, or set the `DOTNET_SYSTEM_IO_DISABLEFILELOCKING` environment variable to `0`. For more information, see [File locking on iOS and tvOS](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/runtime#file-locking-on-ios-and-tvos).

### Collections improvements

- [BitArray span constructors](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#bitarray-span-constructors)
- [BitArray.PopCount](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#bitarraypopcount)
- [EqualityComparer<T>.Create](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#equalitycomparertcreate)
- [ConcurrentQueue reliability fix](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#concurrentqueue-reliability-fix)

#### BitArray span constructors

[BitArray](https://learn.microsoft.com/en-us/dotnet/api/system.collections.bitarray) now has constructors that accept [ReadOnlySpan<T>](https://learn.microsoft.com/en-us/dotnet/api/system.readonlyspan-1): `ReadOnlySpan<bool>`, `ReadOnlySpan<byte>`, and `ReadOnlySpan<int>`. You can construct a bit array directly from a slice or stack-allocated data without first allocating an array:

```
Span<byte> bytes = stackalloc byte[] { 0b_0000_0011, 0b_1000_0000 };
var bits = new BitArray(bytes);

Console.WriteLine(bits[0]);  // True
Console.WriteLine(bits[1]);  // True
Console.WriteLine(bits[15]); // True
```

The span-based constructors avoid the intermediate array allocation that `new BitArray(span.ToArray())` requires.

#### BitArray.PopCount

The [BitArray](https://learn.microsoft.com/en-us/dotnet/api/system.collections.bitarray) class now includes a [BitArray.PopCount()](https://learn.microsoft.com/en-us/dotnet/api/system.collections.bitarray.popcount#system-collections-bitarray-popcount) method that returns the number of bits set to `true` in the array. This provides an efficient way to count set bits without manually iterating through the array.

#### EqualityComparer<T>.Create

To create an equality comparer from a key selector function, use the new [EqualityComparer<T>.Create](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.equalitycomparer-1.create) factory method. You can pass an optional [IEqualityComparer<T>](https://learn.microsoft.com/en-us/dotnet/api/system.collections.generic.iequalitycomparer-1) for the key type itself:

```
// Create an equality comparer based on a key selector
var byName = EqualityComparer<(string Name, int Age)>.Create(p => p.Name);

var people = new HashSet<(string Name, int Age)>(byName)
{
    ("Alice", 30),
    ("Bob", 25),
    ("Alice", 40), // Duplicate by name — not added
};
Console.WriteLine(people.Count); // 2
```

#### ConcurrentQueue reliability fix

[ConcurrentQueue<T>.TryDequeue](https://learn.microsoft.com/en-us/dotnet/api/system.collections.concurrent.concurrentqueue-1.trydequeue) and [ConcurrentQueue<T>.TryPeek](https://learn.microsoft.com/en-us/dotnet/api/system.collections.concurrent.concurrentqueue-1.trypeek) no longer spuriously report an empty queue while the queue freezes a segment during growth.

## Extensions and developer platform

- [Discriminated-union scaffolding](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#discriminated-union-scaffolding)
- [MetadataLoadContext additions](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#metadataloadcontext-additions)
- [Reflection improvements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#reflection-improvements)
- [Assembly.Location override for AssemblyLoadContext](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#assemblylocation-override-for-assemblyloadcontext)
- [Reduced contention in System.IO.Pipelines](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#reduced-contention-in-systemiopipelines)
- [URI data scheme constant](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#uri-data-scheme-constant)
- [StringSyntax attribute enhancements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#stringsyntax-attribute-enhancements)

### Discriminated-union scaffolding

Note

This is a preview feature in .NET 11.

.NET 11 introduces [System.Runtime.CompilerServices.UnionAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.unionattribute) and [System.Runtime.CompilerServices.IUnion](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.iunion) in [System.Runtime.CompilerServices](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices). These types are the runtime side of the C# discriminated-union design. They aren't directly user-facing yet—the C# compiler and source generators are the expected producers—but they ship in the framework so libraries can author against the surface now.

For the language-side design, see the [discriminated unions working group overview](https://github.com/dotnet/csharplang/blob/main/meetings/working-groups/discriminated-unions/union-proposals-overview.md).

### MetadataLoadContext additions

[MetadataLoadContext.GetLoadContext(Assembly)](https://learn.microsoft.com/en-us/dotnet/api/system.reflection.metadataloadcontext.getloadcontext#system-reflection-metadataloadcontext-getloadcontext(system-reflection-assembly)) returns the load context that produced a given `Assembly`, mirroring the long-existing API on [AssemblyLoadContext](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.loader.assemblyloadcontext). This closes a gap for tooling that reflects over assemblies in an isolated `MetadataLoadContext` and needs to walk back from an `Assembly` reference to the context that owns it:

```
using System.Reflection;
using System.Reflection.Metadata;

string[] paths = [typeof(object).Assembly.Location];
using var mlc = new MetadataLoadContext(new PathAssemblyResolver(paths));
Assembly asm = mlc.LoadFromAssemblyPath(typeof(object).Assembly.Location);

MetadataLoadContext owner = MetadataLoadContext.GetLoadContext(asm)!;
Console.WriteLine(ReferenceEquals(owner, mlc)); // true
```

### URI data scheme constant

A new [Uri.UriSchemeData](https://learn.microsoft.com/en-us/dotnet/api/system.uri.urischemedata#system-uri-urischemedata) constant has been added, representing the `data:` URI scheme. This constant provides a standardized way to reference data URIs.

### Reflection improvements

#### Type.GetNullableUnderlyingType

[System.Type](https://learn.microsoft.com/en-us/dotnet/api/system.type) gains a new virtual method, [Type.GetNullableUnderlyingType()](https://learn.microsoft.com/en-us/dotnet/api/system.type.getnullableunderlyingtype#system-type-getnullableunderlyingtype), that returns the underlying value type for a `Nullable<T>` type, or `null` for any non-nullable type. Implementations are provided on [Type](https://learn.microsoft.com/en-us/dotnet/api/system.type), [TypeBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.reflection.emit.typebuilder), [EnumBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.reflection.emit.enumbuilder), [GenericTypeParameterBuilder](https://learn.microsoft.com/en-us/dotnet/api/system.reflection.emit.generictypeparameterbuilder), and [TypeDelegator](https://learn.microsoft.com/en-us/dotnet/api/system.reflection.typedelegator):

```
Type nullableIntType = typeof(int?);
Type? underlying = nullableIntType.GetNullableUnderlyingType();
Console.WriteLine(underlying); // System.Int32

Type nonNullable = typeof(int);
Console.WriteLine(nonNullable.GetNullableUnderlyingType() is null); // True
```

#### ConstructorInfo.GetGenericArguments

[ConstructorInfo.GetGenericArguments()](https://learn.microsoft.com/en-us/dotnet/api/system.reflection.constructorinfo.getgenericarguments#system-reflection-constructorinfo-getgenericarguments) now has an override, providing a consistent way to retrieve generic type arguments for constructor definitions, matching the behavior already available on other `MethodBase` subclasses.

### Assembly.Location override for AssemblyLoadContext

[AssemblyLoadContext.SetAssemblyLocationOverride(Func<Assembly,String,String>)](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.loader.assemblyloadcontext.setassemblylocationoverride#system-runtime-loader-assemblyloadcontext-setassemblylocationoverride(system-func((system-reflection-assembly-system-string-system-string)))) is a set-once callback that can override the location reported by [Assembly.Location](https://learn.microsoft.com/en-us/dotnet/api/system.reflection.assembly.location#system-reflection-assembly-location). This API helps hosts that stage assemblies in temporary paths or virtualized locations report stable, meaningful locations to diagnostics and resource-loading code.

### Reduced contention in System.IO.Pipelines

[System.IO.Pipelines](https://learn.microsoft.com/en-us/dotnet/api/system.io.pipelines) reduces reader and writer lock contention under high fan-in workloads. Internal changes include lower lock scope, local queue continuation scheduling, and pool updates that improve cache locality.

### StringSyntax attribute enhancements

The [StringSyntaxAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.codeanalysis.stringsyntaxattribute) class now includes constants for common programming languages:

- [CSharp](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.codeanalysis.stringsyntaxattribute.csharp#system-diagnostics-codeanalysis-stringsyntaxattribute-csharp) - Indicates C# syntax.
- [FSharp](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.codeanalysis.stringsyntaxattribute.fsharp#system-diagnostics-codeanalysis-stringsyntaxattribute-fsharp) - Indicates F# syntax.
- [VisualBasic](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.codeanalysis.stringsyntaxattribute.visualbasic#system-diagnostics-codeanalysis-stringsyntaxattribute-visualbasic) - Indicates Visual Basic syntax.

These constants can be used with the `StringSyntax` attribute to provide better tooling support for string literals containing code in these languages.

## Caching, configuration, and logging

- [Configuration binding](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#configuration-binding)
- [MemoryCache OpenTelemetry metrics](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#memorycache-opentelemetry-metrics)
- [Options builder validation improvements](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#options-builder-validation-improvements)
- [Asynchronous ChangeToken.OnChange](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#asynchronous-changetokenonchange)
- [Options-aware HybridCache factories](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#options-aware-hybridcache-factories)
- [Asynchronous validation with DataAnnotations](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#asynchronous-validation-with-dataannotations)
- [Format DataAnnotations messages](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#format-dataannotations-messages)
- [Activity tracing configuration](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#activity-tracing-configuration)
- [Generic source-generated logging methods](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#generic-source-generated-logging-methods)
- [Improved reliability for configuration file change detection](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#improved-reliability-for-configuration-file-change-detection)

### Configuration binding

[Microsoft.Extensions.Configuration](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.configuration) adds [Microsoft.Extensions.Configuration.ConfigurationIgnoreAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.configuration.configurationignoreattribute), so models can opt individual properties out of binding declaratively without relying on `BindNonPublicProperties` toggles or custom converters:

```
public sealed class AppOptions
{
    public string Endpoint { get; set; } = "";

    [ConfigurationIgnore]
    public string ComputedKey => Endpoint + ":default";
}
```

`ConfigurationBinder` now also binds an empty array to a constructor parameter instead of throwing.

`PhysicalFilesWatcher` no longer throws when its root directory doesn't yet exist, and `InMemoryDirectoryInfo` resolves `..` and other relative segments consistently with the physical provider.

### MemoryCache OpenTelemetry metrics

[MemoryCache](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.caching.memory.memorycache) now emits a built-in set of OpenTelemetry (OTel)-compatible metrics without an extra adapter package. To opt in, set [MemoryCacheOptions.TrackStatistics](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.caching.memory.memorycacheoptions.trackstatistics#microsoft-extensions-caching-memory-memorycacheoptions-trackstatistics) to `true`:

```
var cache = new MemoryCache(new MemoryCacheOptions
{
    TrackStatistics = true
});
```

The new `Microsoft.Extensions.Caching.Memory.MemoryCache` meter publishes four observable instruments:

- `dotnet.cache.requests` (with a `dotnet.cache.request.result` tag that distinguishes `hit` from `miss`)
- `dotnet.cache.evictions`
- `dotnet.cache.entries`
- `dotnet.cache.estimated_size` (with unit `1`, because its values represent application-defined cache size units rather than bytes)

If you filter telemetry on the hit/miss tag, use `dotnet.cache.request.result`. Earlier builds named the tag `dotnet.cache.request.type`.

Pass an [System.Diagnostics.Metrics.IMeterFactory](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.metrics.imeterfactory) to the new [MemoryCache.MemoryCache(IOptions<MemoryCacheOptions>, ILoggerFactory, IMeterFactory)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.caching.memory.memorycache.-ctor#microsoft-extensions-caching-memory-memorycache-ctor(microsoft-extensions-options-ioptions((microsoft-extensions-caching-memory-memorycacheoptions))-microsoft-extensions-logging-iloggerfactory-system-diagnostics-metrics-imeterfactory)) constructor overload for per-instance metrics. Without one, the instruments are aggregated process-wide on a shared meter.

### Options builder validation improvements

[OptionsBuilder<TOptions>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.options.optionsbuilder-1) gains a new generic [OptionsBuilder<TOptions>.Validate](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.options.optionsbuilder-1.validate) overload that accepts a type parameter instead of a factory delegate. The type must implement [IValidateOptions<TOptions>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.options.ivalidateoptions-1) and be registered in the dependency-injection container. This aligns options validation with the standard DI pattern:

```
services.AddSingleton<IValidateOptions<MyOptions>, MyOptionsValidator>();
services.AddOptions<MyOptions>()
    .Bind(configuration.GetSection("MyOptions"))
    .Validate<MyOptionsValidator>();
```

### Asynchronous ChangeToken.OnChange

[OnChange](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.primitives.changetoken.onchange) now has `Func<Task>` overloads, so you can run asynchronous callbacks without using `async void`. Re-registration now happens after the returned task completes.

### Options-aware HybridCache factories

[GetOrCreateAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.caching.hybrid.hybridcache.getorcreateasync) now has overloads that provide a mutable factory context. You can set entry-level options, such as expiration and local cache size, from the value-producing callback.

### Asynchronous validation with DataAnnotations

`System.ComponentModel.DataAnnotations` now supports asynchronous validation. A validation rule that needs to do I/O—a database lookup or a remote API call—can now run without blocking a thread. There are three new ways to express an async rule:

- Derive from `AsyncValidationAttribute` and override its `IsValidAsync` method.
- Implement `IAsyncValidatableObject` on the model.
- Call the new `Validator.ValidateObjectAsync`, `TryValidateObjectAsync`, `ValidatePropertyAsync`, and `ValidateValueAsync` methods.

```
using System;
using System.ComponentModel.DataAnnotations;

public sealed class ValidVatNumberAttribute : AsyncValidationAttribute
{
    protected override ValidationResult? IsValid(object? value, ValidationContext context) =>
        throw new InvalidOperationException("Validate this attribute with IsValidAsync.");

    protected override async Task<ValidationResult?> IsValidAsync(
        object? value, ValidationContext context, CancellationToken cancellationToken)
    {
        var registry = context.GetRequiredService<IVatRegistry>();
        return await registry.IsRegisteredAsync((string?)value, cancellationToken)
            ? ValidationResult.Success
            : new ValidationResult("That VAT number isn't registered with the tax authority.");
    }
}

public class Invoice
{
    [Required]
    [StringLength(14, MinimumLength = 8)]
    [RegularExpression(@"^[A-Z]{2}[A-Z0-9]+$")]
    [ValidVatNumber] // asynchronous
    public string VatNumber { get; set; } = "";
}

var context = new ValidationContext(model, serviceProvider, items: null);
await Validator.ValidateObjectAsync(model, context, validateAllProperties: true);
```

`Microsoft.Extensions.Options` gains matching support: options can be validated asynchronously, including at startup through the new `IAsyncStartupValidator`. This lets an app fail fast when an option that requires a network check is misconfigured. `IStartupValidator` is now obsolete; implement `IAsyncStartupValidator` instead.

Source-generated options validators provide a synchronous `IValidateOptions<TOptions>.Validate` implementation in addition to asynchronous validation, so existing synchronous validation call sites keep working alongside validators that need to await I/O:

```
public sealed class BackendOptionsValidator : IAsyncValidateOptions<BackendOptions>
{
    public async Task<ValidateOptionsResult> ValidateAsync(
        string? name, BackendOptions options, CancellationToken cancellationToken = default) =>
        await IsReachableAsync(options.HostName, cancellationToken)
            ? ValidateOptionsResult.Success
            : ValidateOptionsResult.Fail($"'{options.HostName}' isn't reachable.");

    // Source-generated validators also implement this synchronous fallback.
    public ValidateOptionsResult Validate(string? name, BackendOptions options) =>
        ValidateOptionsResult.Fail("Backend validation must run asynchronously.");
}
```

### Format DataAnnotations messages

`ValidationAttribute.FormatMessage` lets a validation host supply a message template while the attribute fills in its own placeholders. This method supports localization without duplicating the formatting logic for built-in attributes such as [RangeAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.rangeattribute):

```
using System.ComponentModel.DataAnnotations;

var range = new RangeAttribute(1, 10);
string message = range.FormatMessage("{0} must be between {1} and {2}", "Value");
// Value must be between 1 and 10
```

### Activity tracing configuration

A new tracing configuration API in `Microsoft.Extensions.Diagnostics` lets you turn `Activity` tracing on and off with rules instead of wiring up `ActivityListener` instances manually. Call `AddTracing` and describe which activity sources, operations, and listeners to enable or disable. Rules can be driven from configuration, so tracing can be tuned without a redeploy.

```
builder.Services.AddTracing(tracing =>
{
    tracing.EnableTracing(sourceName: "MyCompany.Orders");
    tracing.DisableTracing(sourceName: "MyCompany.Orders", operationName: "HealthCheck");
});
```

The same release adds `ActivitySourceFactory` and unseals `ActivitySource`, which together support factory-driven creation and refreshable listeners.

### Generic source-generated logging methods

The logging source generator now supports generic methods decorated with [LoggerMessageAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.logging.loggermessageattribute), primarily to avoid boxing. Generic type parameters can use standard constraints, such as `class`, `struct`, `unmanaged`, interfaces, base types, and `new()`. The `allows ref struct` anti-constraint isn't supported and produces [SYSLIB1011](https://learn.microsoft.com/en-us/dotnet/fundamentals/syslib-diagnostics/syslib1011).

```
[LoggerMessage(0, LogLevel.Trace, "Received {Code} ({Length} bytes)")]
public static partial void PacketReceived<TCode>(ILogger logger, TCode code, int length)
    where TCode : struct, Enum;
```

### Improved reliability for configuration file change detection

The [PhysicalFilesWatcher](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.fileproviders.physical.physicalfileswatcher) type, which configuration providers use to detect configuration file changes, includes several reliability improvements.

It now handles relative paths, missing directories, and file systems that don't support file watching more reliably. It also avoids watching subdirectories when it doesn't need to.

## Cryptography

- [X25519 Diffie-Hellman key exchange](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#x25519-diffie-hellman-key-exchange)
- [CryptographicOperations.FixedTimeEquals overload](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#cryptographicoperationsfixedtimeequals-overload)
- [AES Key Wrap](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#aes-key-wrap)
- [Faster authenticated encryption on Apple platforms](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#faster-authenticated-encryption-on-apple-platforms)
- [Experimental composite ML-KEM and HPKE APIs](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#experimental-composite-ml-kem-and-hpke-apis)
- [Encrypt CMS messages with ML-KEM](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#encrypt-cms-messages-with-ml-kem)

### X25519 Diffie-Hellman key exchange

The new [System.Security.Cryptography.X25519DiffieHellman](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.x25519diffiehellman) abstract class provides a clean API for the X25519 elliptic-curve Diffie-Hellman algorithm, which is widely used in TLS 1.3, SSH, and Signal-protocol implementations. Platform-specific implementations are provided through [X25519DiffieHellmanCng](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.x25519diffiehellmancng) (Windows) and [X25519DiffieHellmanOpenSsl](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.x25519diffiehellmanopenssl) (Linux and macOS), but the portable `GenerateKey()` factory method picks the right one automatically:

```
// Generate key pairs for Alice and Bob
using X25519DiffieHellman alice = X25519DiffieHellman.GenerateKey();
using X25519DiffieHellman bob = X25519DiffieHellman.GenerateKey();

// Each party derives the shared secret using the other's public key
byte[] aliceShared = alice.DeriveRawSecretAgreement(bob);
byte[] bobShared = bob.DeriveRawSecretAgreement(alice);

// Both parties arrive at the same secret
Console.WriteLine(aliceShared.SequenceEqual(bobShared)); // True
```

The class supports the full key lifecycle: key generation, PKCS#8 and SubjectPublicKeyInfo import/export, PEM serialization, and raw private/public key access.

### CryptographicOperations.FixedTimeEquals overload

For secret-comparison scenarios where the expected value is a single known byte, use the new [CryptographicOperations.FixedTimeEquals](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.cryptographicoperations.fixedtimeequals) overload that compares a [ReadOnlySpan<T>](https://learn.microsoft.com/en-us/dotnet/api/system.readonlyspan-1) with a single `byte` value in constant time:

```
bool equal = CryptographicOperations.FixedTimeEquals(receivedSpan, 0x42);
```

### AES Key Wrap

[System.Security.Cryptography.Aes](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes) now supports the AES Key Wrap algorithms used by JOSE and other libraries to encrypt cryptographic keys:

- [Aes.EncryptKeyWrapPadded](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes.encryptkeywrappadded), [Aes.DecryptKeyWrapPadded](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes.decryptkeywrappadded), [Aes.TryDecryptKeyWrapPadded(ReadOnlySpan<Byte>, Span<Byte>, Int32)](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes.trydecryptkeywrappadded#system-security-cryptography-aes-trydecryptkeywrappadded(system-readonlyspan((system-byte))-system-span((system-byte))-system-int32@)), and [Aes.GetKeyWrapPaddedLength(Int32)](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes.getkeywrappaddedlength#system-security-cryptography-aes-getkeywrappaddedlength(system-int32)) implement the padded AES-KWP algorithm (RFC 5649).
- [Aes.EncryptKeyWrap](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes.encryptkeywrap), [Aes.DecryptKeyWrap](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes.decryptkeywrap), [Aes.TryDecryptKeyWrap(ReadOnlySpan<Byte>, Span<Byte>, Int32)](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes.trydecryptkeywrap#system-security-cryptography-aes-trydecryptkeywrap(system-readonlyspan((system-byte))-system-span((system-byte))-system-int32@)), and [Aes.GetKeyWrapLength(Int32)](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aes.getkeywraplength#system-security-cryptography-aes-getkeywraplength(system-int32)) implement the unpadded AES Key Wrap algorithm (RFC 3394), which requires plaintext that's a multiple of 8 bytes.

Both sets of APIs provide array-returning and span-based overloads:

```
using Aes aes = Aes.Create();
aes.Key = RandomNumberGenerator.GetBytes(32); // AES-256 key-encryption key

byte[] keyToWrap = RandomNumberGenerator.GetBytes(24); // Multiple of 8 bytes

// Unpadded AES Key Wrap (RFC 3394)
byte[] wrapped = aes.EncryptKeyWrap(keyToWrap);
byte[] unwrapped = aes.DecryptKeyWrap(wrapped);
Console.WriteLine(keyToWrap.SequenceEqual(unwrapped)); // True

// Padded AES-KWP (RFC 5649) accepts a plaintext of any length
byte[] arbitraryLengthKey = RandomNumberGenerator.GetBytes(19);
byte[] wrappedPadded = aes.EncryptKeyWrapPadded(arbitraryLengthKey);
byte[] unwrappedPadded = aes.DecryptKeyWrapPadded(wrappedPadded);
Console.WriteLine(arbitraryLengthKey.SequenceEqual(unwrappedPadded)); // True
```

### Faster authenticated encryption on Apple platforms

[AesGcm](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.aesgcm) and [ChaCha20Poly1305](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.chacha20poly1305) avoid passing empty associated data to CryptoKit on Apple platforms, letting the native implementation use its empty-AAD fast path. On Apple platforms version 26 and later, encryption also skips a copy that was previously required for older Foundation implementations.

### Experimental composite ML-KEM and HPKE APIs

Warning

`CompositeMLKem` and `Hpke` are experimental in .NET 11 and might change. Direct use requires you to opt in to the `SYSLIB5006` diagnostic for `CompositeMLKem` and the `SYSLIB5009` diagnostic for `Hpke`.

`CompositeMLKem` combines post-quantum and classical key encapsulation so that both contribute to the shared secret. It's available on platforms that already support Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM). Call `CompositeMLKem.IsAlgorithmSupported` to determine whether the platform supports a particular combination of algorithms.

`Hpke` provides Hybrid Public Key Encryption (HPKE). The current implementation supports classical Diffie-Hellman key encapsulation mechanism (DHKEM) suites. ML-KEM and hybrid ML-KEM suites aren't supported yet. Check `Hpke.IsSupported` for the suite you select.

### Encrypt CMS messages with ML-KEM

The Cryptographic Message Syntax (CMS) API, [EnvelopedCms](https://learn.microsoft.com/en-us/dotnet/api/system.security.cryptography.pkcs.envelopedcms), can encrypt and decrypt messages by using ML-KEM key encapsulation mechanism (KEM) recipients. Support is limited to the pure ML-KEM algorithm, and it's available only on non-Windows platforms.

## Networking and transport security

- [TLS handshake hardening](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#tls-handshake-hardening)
- [Experimental caller-driven TLS sessions](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#experimental-caller-driven-tls-sessions)
- [HTTP request compression](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#http-request-compression)
- [Configurable HTTP connection eviction](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#configurable-http-connection-eviction)
- [Initial HTTP/2 concurrency](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#initial-http2-concurrency)
- [DNS record resolution APIs](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#dns-record-resolution-apis)
- [HTTP/2 automatic downgrade for Windows authentication](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#http2-automatic-downgrade-for-windows-authentication)
- [QUIC stream priority](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#quic-stream-priority)
- [Video MIME type constants](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#video-mime-type-constants)
- [HTTP metrics use observable instruments](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/libraries#http-metrics-use-observable-instruments)

### TLS handshake hardening

Two [System.Net.Security](https://learn.microsoft.com/en-us/dotnet/api/system.net.security) items improve TLS (Transport Layer Security) reliability:

- [SslStream](https://learn.microsoft.com/en-us/dotnet/api/system.net.security.sslstream) server-side handshake bounds-checking fixes in `TlsFrameHelper` close several edge cases that could surface as `IOException` on malformed ClientHello records.
- On Linux, certificate-validation failures now surface as standard TLS alerts to the peer, matching Windows behavior. Connecting clients receive an actionable handshake error instead of a connection drop.

Negotiate authentication servers can also validate TLS channel binding tokens on Unix. The managed GSSAPI path passes the channel binding data to `gss_accept_sec_context`, which rejects a mismatch in the same way as the existing Unix client path. This enables Extended Protection scenarios, such as ASP.NET Core's Negotiate authentication, that bind authentication to the underlying TLS connection.

### Experimental caller-driven TLS sessions

Warning

The `TlsContext`, `TlsSession`, `TlsBufferSession`, `TlsSocketSession`, and `TlsOperationStatus` types are experimental in .NET 11 and report diagnostic `SYSLIB5007`.

[System.Net.Security](https://learn.microsoft.com/en-us/dotnet/api/system.net.security) adds a caller-driven, non-blocking TLS state machine for advanced transports where the application controls buffers and I/O scheduling. `TlsBufferSession` operates over caller-provided spans, while `TlsSocketSession` works with a `SafeSocketHandle`.

Operations such as `Handshake`, `Read`, `Write`, `Shutdown`, and `RequestClientCertificate` return `TlsOperationStatus`, which reports whether an operation completed, needs more input, needs a larger destination buffer, or requires certificate validation or a new `TlsContext`.

### HTTP request compression

[System.Net.Http](https://learn.microsoft.com/en-us/dotnet/api/system.net.http) adds [GZipCompressedContent](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.gzipcompressedcontent), [BrotliCompressedContent](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.brotlicompressedcontent), and [ZstandardCompressedContent](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.zstandardcompressedcontent) wrappers for request bodies. These wrappers set the `Content-Encoding` header and stream compressed content as the request serializes.

### Configurable HTTP connection eviction

[SocketsHttpHandler](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.socketshttphandler) now provides [SocketsHttpHandler.ShouldEvictConnection](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.socketshttphandler.shouldevictconnection#system-net-http-socketshttphandler-shouldevictconnection) for per-connection eviction decisions. This callback lets you retire connections based on age, endpoint details, and DNS changes instead of fixed lifetime-only policies.

### Initial HTTP/2 concurrency

`SocketsHttpHandler.InitialHttp2MaxConcurrentStreams` limits the number of concurrent streams on each new HTTP/2 connection before the server's `SETTINGS` frame arrives. If you know that a server's stream limit is lower than the default of 100, set a lower value to limit the initial burst of requests on that connection. After the connection receives the `SETTINGS` frame, it uses the server's advertised limit.

The property requires a value of at least 1. If an earlier connection to the same host advertised a lower limit, that limit can further reduce the initial concurrency for the host.

```
var handler = new SocketsHttpHandler
{
    InitialHttp2MaxConcurrentStreams = 20
};
using var client = new HttpClient(handler);
```

### DNS record resolution APIs

[System.Net.Dns](https://learn.microsoft.com/en-us/dotnet/api/system.net.dns) adds typed record-resolution APIs, including [Dns.ResolveSrv(String)](https://learn.microsoft.com/en-us/dotnet/api/system.net.dns.resolvesrv#system-net-dns-resolvesrv(system-string)), [Dns.ResolveMx(String)](https://learn.microsoft.com/en-us/dotnet/api/system.net.dns.resolvemx#system-net-dns-resolvemx(system-string)), [Dns.ResolveTxt(String)](https://learn.microsoft.com/en-us/dotnet/api/system.net.dns.resolvetxt#system-net-dns-resolvetxt(system-string)), [Dns.ResolveCName(String)](https://learn.microsoft.com/en-us/dotnet/api/system.net.dns.resolvecname#system-net-dns-resolvecname(system-string)), [Dns.ResolvePtr(String)](https://learn.microsoft.com/en-us/dotnet/api/system.net.dns.resolveptr#system-net-dns-resolveptr(system-string)), and [Dns.ResolveNs(String)](https://learn.microsoft.com/en-us/dotnet/api/system.net.dns.resolvens#system-net-dns-resolvens(system-string)), together with `Async` variants. The results include records, response code, and negative-cache time-to-live (TTL) metadata through [DnsResult<T>](https://learn.microsoft.com/en-us/dotnet/api/system.net.dnsresult-1).

The new [DnsResolver](https://learn.microsoft.com/en-us/dotnet/api/system.net.dnsresolver) class provides the same record types through an instance API that accepts a [DnsResolverOptions](https://learn.microsoft.com/en-us/dotnet/api/system.net.dnsresolveroptions) object, which lets you supply a custom list of DNS servers instead of using the platform resolver configuration. `DnsResolver` and the static `Dns.Resolve*` methods now work on Linux in addition to Windows and macOS.

### HTTP/2 automatic downgrade for Windows authentication

[HttpClient](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient) automatically downgrades to HTTP/1.1 when a request requires Windows authentication (NTLM/Negotiate) over HTTP/2. The HTTP/2 specification disallows the connection-bound authentication schemes that NTLM and Kerberos rely on, so these requests previously failed. With the downgrade in place, applications targeting mixed-authentication environments—common in enterprise intranets—work without explicit `HttpRequestMessage.Version` overrides.

### QUIC stream priority

[QuicStream](https://learn.microsoft.com/en-us/dotnet/api/system.net.quic.quicstream) gains a [QuicStream.Priority](https://learn.microsoft.com/en-us/dotnet/api/system.net.quic.quicstream.priority#system-net-quic-quicstream-priority) property and a [QuicStream.DefaultPriority](https://learn.microsoft.com/en-us/dotnet/api/system.net.quic.quicstream.defaultpriority#system-net-quic-quicstream-defaultpriority) constant that exposes HTTP/3 stream prioritization (RFC 9218). Priority values range from 0 (highest) to 255 (lowest), with a default of 127:

```
// Increase priority for interactive streams
stream.Priority = 64; // Higher priority than the default 127
```

### Video MIME type constants

A new [System.Net.Mime.MediaTypeNames.Video](https://learn.microsoft.com/en-us/dotnet/api/system.net.mime.mediatypenames.video) class provides string constants for common video media types:

- `MediaTypeNames.Video.Mp4` — `"video/mp4"`
- `MediaTypeNames.Video.Mpeg` — `"video/mpeg"`
- `MediaTypeNames.Video.Ogg` — `"video/ogg"`
- `MediaTypeNames.Video.QuickTime` — `"video/quicktime"`
- `MediaTypeNames.Video.WebM` — `"video/webm"`

These join the existing `MediaTypeNames.Application`, `MediaTypeNames.Image`, `MediaTypeNames.Text`, and `MediaTypeNames.Multipart` classes.

### HTTP metrics use observable instruments

The high-cardinality HTTP `open_connections` and `active_requests` metrics are now observable instruments instead of regular counters. If you use [MeterListener](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.metrics.meterlistener) directly to read these metrics, call [MeterListener.RecordObservableInstruments()](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.metrics.meterlistener.recordobservableinstruments#system-diagnostics-metrics-meterlistener-recordobservableinstruments) to receive measurements from them.

## Unsafe API accessibility

.NET 11 removes the `[RequiresUnsafe]` attribute from a large set of APIs that take pointer parameters. Previously, calling these methods from code that used `unsafe` blocks still required a project-level `<AllowUnsafeBlocks>true</AllowUnsafeBlocks>` setting because the attribute enforced that requirement independently. Now, only the standard `unsafe` block or method modifier is required.

Affected APIs include:

- [Buffer.MemoryCopy](https://learn.microsoft.com/en-us/dotnet/api/system.buffer.memorycopy)
- [ReadOnlySpan<T>.ReadOnlySpan<T>(Void\*, Int32)](https://learn.microsoft.com/en-us/dotnet/api/system.readonlyspan-1.-ctor#system-readonlyspan-1-ctor(system-void*-system-int32)) and [Span<T>.Span<T>(Void\*, Int32)](https://learn.microsoft.com/en-us/dotnet/api/system.span-1.-ctor#system-span-1-ctor(system-void*-system-int32))
- [System.Runtime.CompilerServices.Unsafe](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.compilerservices.unsafe) pointer methods such as `AsRef`, `Read`, `Write`, and `Copy`
- [System.Runtime.InteropServices.NativeMemory](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.nativememory) methods
- [System.Text.Encoding](https://learn.microsoft.com/en-us/dotnet/api/system.text.encoding) pointer overloads (all encoding classes)
- [System.Numerics.Vector](https://learn.microsoft.com/en-us/dotnet/api/system.numerics.vector) pointer-based `Load` and `Store` methods
- Interop marshalling types in [System.Runtime.InteropServices.Marshalling](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.marshalling)

This change reduces friction for advanced scenarios such as interop authoring, memory-mapped files, and low-level buffer manipulation, where unsafe context is already required by the calling code.

## See also

- [What's new in the .NET 11 runtime](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/runtime)
- [What's new in the SDK for .NET 11](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/sdk)
- [Breaking changes in .NET 11](https://learn.microsoft.com/en-us/dotnet/core/compatibility/11)
