---
source: "https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/"
title: "Process API Improvements in .NET 11"
author: ".NET Blog"
date_published: "Wed, 13 May 2026 21:00:00 +0000"
date_clipped: "2026-05-16"
category: ".NET Ecosystem"
source_type: "rss"
---

# Process API Improvements in .NET 11

Source: https://devblogs.microsoft.com/dotnet/process-api-improvements-in-dotnet-11/

The System.Diagnostics.Process class is the primary way to create and interact with processes with .NET. We made the biggest update to it in years, with .NET 11. The changes add high-level APIs that make it easy to start a process and capture its output without deadlocks, give you full control over handle inheritance and standard handle redirection, introduce lifetime management features like KillOnParentExit , and include a lightweight SafeProcessHandle -based API surface that is more trimmer-friendly.
Summary 
Here’s a recap of new Process APIs in .NET 11:
Feature 
API 
Description 
One-liner process execution 
Process.RunAndCaptureText[Async] 
Starts a process, captures output/error, waits for exit – all in one call. 
One-liner process execution without capturing output 
Process.Run[Async] 
Starts a process and waits for exit without capturing output. 
Fire and forget 
Process.StartAndForget 
Starts a process, returns its PID, and releases all resources immediately. 
Deadlock-free output capture 
Process.ReadAllText/Bytes/Lines[Async] 
Reads both stdout and stderr simultaneously using multiplexing, avoiding pipe buffer deadlocks. 
Redirect to anything 
ProcessStartInfo.Standard[Input/Output/Error]Handle 
Redirect standard handles to files, pipes, null, or any SafeFileHandle . 
Controlled inheritance 
ProcessStartInfo.InheritedHandles 
Specify exactly which handles child process inheritance, preventing accidental leaks. 
Kill on parent exit 
ProcessStartInfo.KillOnParentExit 
Ensures child processes are terminated when the parent exits (Windows and Linux). 
Detached processes 
ProcessStartInfo.StartDetached 
Start a process that survives parent exit, signal, or terminal close. 
Lightweight process handle 
SafeProcessHandle.Start/WaitForExit/Kill/Signal 
Trimmer-friendly, lower-level API for starting and managing processes without Process . 
Process exit details 
ProcessExitStatus 
Reports exit code, terminating signal (Unix), and whether the process was killed due to timeout/cancellation. 
Null handle 
File.OpenNullHandle() 
Opens a handle that discards writes and returns EOF on reads. 
Anonymous pipes 
SafeFileHandle.CreateAnonymousPipe 
Creates a connected pipe pair with optional async support. 
Console handles 
Console.OpenStandard[Input/Output/Error]Handle() 
Gets the underlying OS handle for standard streams. 
Handle type detection 
SafeFileHandle.Type 
Identifies whether a handle is a file, pipe, socket, etc. 
Other improvements include:
Better scalability on Windows : BeginOutputReadLine / BeginErrorReadLine no longer block thread pool threads: throughput improvement when starting multiple processes in parallel with redirected output and error. 
Better trimmability : Up to 20% smaller NativeAOT binaries compared to .NET 10 when using Process and up to 32% smaller when using SafeProcessHandle . 
Improved process creation on Apple platforms : Up to 100x faster process creation on Apple Silicon due to switch to posix_spawn . 
Reduced memory allocations on Unix : 30–50% fewer allocations when starting processes on Unix. 
The rest of the blog post is a deep dive into each of these features.
Capturing process output without deadlocks 
Why capturing process output can hang your app 
When redirecting standard output and error of the process, it’s possible to run into deadlocks. Knowing why it’s possible is crucial to understanding the changes we have made. Let’s build a C# app that tries to read all output and error from a process.
First of all, we need to redirect standard output and error of the process to be able to read it. This is done by setting RedirectStandardOutput and RedirectStandardError properties of ProcessStartInfo to true . Then before the process is started, two dedicated pipes are created (one for standard output and one for standard error), and the process is created with the write ends of these pipes (each pipe comes with a read and write end) as standard output and error. The child process just writes to its standard output and error as usual, but instead of going to the console, the data is written to the pipes.
ProcessStartInfo startInfo = new("dotnet", "--help")
{
RedirectStandardOutput = true,
RedirectStandardError = true
};
using Process process = new() { StartInfo = startInfo }; 
Pipes have limited buffer size (usually 4KB on Windows and 64KB on Unix). When the producer (in our case, the child process) writes to the pipe, the data is stored in a buffer until it’s read by the consumer (the parent process). If the producer writes more data than the size of the buffer and the consumer is not reading from the pipe at the same time, the producer will be blocked on write operation, waiting for the consumer to read from the pipe and free some space in the buffer.
If the consumer is waiting for the producer to exit (e.g. by calling WaitForExit ) without reading from the pipe, it will be blocked as soon as the producer fills the buffer:
process.Start();
process.WaitForExit();
string output = process.StandardOutput.ReadToEnd();
string error = process.StandardError.ReadToEnd(); 
But does re-ordering the code help?
process.Start();
string output = process.StandardOutput.ReadToEnd();
string error = process.StandardError.ReadToEnd();
process.WaitForExit(); 
Not really. ReadToEnd is a blocking call – it reads until the stream reaches EOF, which only happens when the child process closes its end of the pipe (typically on exit). So in the code above, we first block on standard output until the child exits, and only then start reading standard error. While we’re waiting on standard output, nobody is draining standard error. If the child writes more to stderr than the pipe buffer can hold, the child blocks on its write – and we’re stuck waiting for each other.
The root cause is that we are reading the two streams sequentially , not simultaneously. To avoid this deadlock, we need to drain both standard output and error at the same time . So far, we had two options:
The existing APIs are not optimal in terms of simplicity and performance. I’ll show you a couple patterns.
Use asynchronous read operations on StandardOutput and StandardError 
The Process class exposes stream readers that you can read from, for example, with ReadToEndAsync .
process.Start();
// Start both operations to ensure both streams are drained at the same time
Task<string> outputTask = process.StandardOutput.ReadToEndAsync();
Task<string> errorTask = process.StandardError.ReadToEndAsync();
// Wait for both read operations to complete and process to exit
await Task.WhenAll(outputTask, errorTask, process.WaitForExitAsync());
string output = await outputTask;
string error = await errorTask; 
Use OutputDataReceived and ErrorDataReceived events 
These Process class events are raised when a line is written to standard output and error respectively.
StringBuilder stdOut = new(), stdErr = new();
process.OutputDataReceived += (sender, e) => stdOut.AppendLine(e.Data);
process.ErrorDataReceived += (sender, e) => stdErr.AppendLine(e.Data);
process.Start();
process.BeginOutputReadLine();
process.BeginErrorReadLine();
process.WaitForExit(); 
Process.ReadAllText and Process.ReadAllTextAsync 
We have added ReadAllText and ReadAllTextAsync ( PR ) methods to Process class. They drain standard output and error at the same time, helping us to avoid deadlocks. They decode the output using the encoding specified by the ProcessStartInfo.Standard[Output/Error]Encoding (or the default when not specified), and return the result as strings (per-line needs are handled by an API we’ll see shortly).
public class Process
{
public (string StandardOutput, string StandardError) ReadAllText(TimeSpan? timeout = default);
public Task<(string StandardOutput, string StandardError)> ReadAllTextAsync(CancellationToken cancellationToken = default);
} 
So the code to read all output and error from the process becomes much simpler:
ProcessStartInfo startInfo = new("dotnet", "--help")
{
RedirectStandardOutput = true,
RedirectStandardError = true
};
using Process process = new() { StartInfo = startInfo };
process.Start();
(string output, string error) = process.ReadAllText();
process.WaitForExit(); 
Process.RunAndCaptureText and Process.RunAndCaptureTextAsync 
We expect that capturing output and error and just waiting for the process to exit (process can close standard handles and keep running) is very common. That is why we have introduced RunAndCaptureText and RunAndCaptureTextAsync methods that combine starting the process, reading all output and error, and waiting for the process to exit in one method call.
namespace System.Diagnostics;
public sealed class ProcessExitStatus
{
public ProcessExitStatus(int exitCode, bool canceled, PosixSignal? signal = null);
public int ExitCode { get; }
public PosixSignal? Signal { get; }
public bool Canceled { get; }
}
public sealed class ProcessTextOutput
{
public ProcessTextOutput(ProcessExitStatus exitStatus, string standardOutput, string standardError, int processId);
public ProcessExitStatus ExitStatus { get; }
public string StandardOutput { get; }
public string StandardError { get; }
public int ProcessId { get; }
}
public class Process
{
public static ProcessTextOutput RunAndCaptureText(ProcessStartInfo startInfo, TimeSpan? timeout = default);
public static ProcessTextOutput RunAndCaptureText(string fileName, IList<string>? arguments = null, System.TimeSpan? timeout = default);
public static Task<ProcessTextOutput> RunAndCaptureTextAsync(ProcessStartInfo startInfo, CancellationToken cancellationToken = default);
public static Task<ProcessTextOutput> RunAndCaptureTextAsync(string fileName, IList<string>? arguments = null, CancellationToken cancellationToken = default);
} 
Which makes the code to start a process and capture its output and error literally a one liner:
ProcessTextOutput output = Process.RunAndCaptureText("dotnet", ["--help"]); 
We also provided Process.Run and Process.RunAsync methods that don’t capture output and error, but just wait for the process to exit, for cases when you don’t care about the output.
ProcessExitStatus status = Process.Run("dotnet", ["build", "-c", "Release"]); 
Process.ReadAllLines and Process.ReadAllLinesAsync 
If you need to capture output and error as lines, you can use ReadAllLines ( PR ) and ReadAllLinesAsync ( PR ) methods, which are implemented in the same way as their ReadAllText counterparts, but return an enumerable of ProcessOutputLine instead of a single string.
namespace System.Diagnostics;
public readonly struct ProcessOutputLine
{
public ProcessOutputLine(string content, bool standardError);
public string Content { get; }
public bool StandardError { get; }
}
public class Process
{
public IEnumerable<ProcessOutputLine> ReadAllLines(TimeSpan? timeout = default);
public IAsyncEnumerable<ProcessOutputLine> ReadAllLinesAsync(CancellationToken cancellationToken = default);
} 
Let’s see how we can use it to read output and error from the process line by line as they are produced:
using Process process = Process.Start(new ProcessStartInfo("dotnet", "--help")
{
RedirectStandardOutput = true,
RedirectStandardError = true
})!;
await foreach (ProcessOutputLine line in process.ReadAllLinesAsync())
{
if (line.StandardError)
Console.ForegroundColor = ConsoleColor.Red;
Console.WriteLine(line.Content);
Console.ResetColor();
} 
Process.ReadAllBytes and Process.ReadAllBytesAsync 
If you need to capture output and error as bytes, you can use ReadAllBytes method, which is internally used by ReadAllText ( PR ). It returns byte arrays instead of strings.
public class Process
{
public (byte[] StandardOutput, byte[] StandardError) ReadAllBytes(TimeSpan? timeout = default);
public Task<(byte[] StandardOutput, byte[] StandardError)> ReadAllBytesAsync(CancellationToken cancellationToken = default);
} 
Timeouts and cancellation 
All the aforementioned methods that read from standard output and error support timeouts and cancellation. If the timeout is reached or the cancellation token is cancelled before the end of the stream is reached, the methods will throw TimeoutException or OperationCanceledException respectively. The high-level RunAndCaptureText[Async] and Run[Async] methods will also try to kill the process to avoid leaving it running.
Multiplexing and other optimizations under the hood 
The new methods are not just simpler to use, but also faster. Behind the scenes, the synchronous Process.RunAndCaptureText and Process.ReadAll[Bytes/Text] methods use multiplexing ( poll on Unix and WaitForMultipleObjects on Windows) to read from both standard output and error using a single thread. They also implement a bunch of other optimizations such as using ArrayPool to reduce memory allocations. The asynchronous Process.RunAndCaptureTextAsync and Process.ReadAllTextAsync methods use asynchronous I/O operations without blocking any threads.
using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;
using System.Diagnostics;
using System.Text;
BenchmarkSwitcher.FromAssembly(typeof(CaptureOutputBenchmarks).Assembly).Run(args);
[MemoryDiagnoser, ThreadingDiagnoser]
public class CaptureOutputBenchmarks
{
private readonly ProcessStartInfo _processStartInfo = CreateStartInfo();
private static ProcessStartInfo CreateStartInfo()
{
ProcessStartInfo startInfo = OperatingSystem.IsWindows()
? new("cmd.exe", "/c for /L %i in (1,1,1000) do @echo Line %i")
: new("sh", ["-c", "for i in $(seq 1 1000); do echo \"Line $i\"; done"]);
startInfo.RedirectStandardOutput = true;
startInfo.RedirectStandardError = true;
return startInfo;
}
[Benchmark]
public int Events()
{
using Process process = new();
process.StartInfo = _processStartInfo;
StringBuilder stdOut = new(), stdErr = new();
process.OutputDataReceived += (sender, e) => stdOut.AppendLine(e.Data);
process.ErrorDataReceived += (sender, e) => stdErr.AppendLine(e.Data);
process.Start();
process.BeginOutputReadLine();
process.BeginErrorReadLine();
process.WaitForExit();
// Other benchmarks materialize the output, so we do it here
// to ensure it's apples to apples comparison.
_ = stdOut.ToString();
_ = stdErr.ToString();
return process.ExitCode;
}
[Benchmark]
public async Task<int> ReadToEndAsync()
{
using Process process = Process.Start(_processStartInfo)!;
Task<string> readOutput = process.StandardOutput.ReadToEndAsync();
Task<string> readError = process.StandardError.ReadToEndAsync();
_ = await readOutput;
_ = await readError;
await process.WaitForExitAsync();
return process.ExitCode;
}
[Benchmark]
public int RunAndCaptureText()
{
ProcessTextOutput processTextOutput = Process.RunAndCaptureText(_processStartInfo);
_ = processTextOutput.StandardOutput;
_ = processTextOutput.StandardError;
return processTextOutput.ExitStatus.ExitCode;
}
[Benchmark]
public async Task<int> RunAndCaptureTextAsync()
{
ProcessTextOutput processTextOutput = await Process.RunAndCaptureTextAsync(_processStartInfo);
_ = processTextOutput.StandardOutput;
_ = processTextOutput.StandardError;
return processTextOutput.ExitStatus.ExitCode;
}
} 
BenchmarkDotNet v0.16.0-nightly.20260505.517, Windows 11 (10.0.26200.8246/25H2/2025Update/HudsonValley2)
AMD Ryzen Threadripper PRO 3945WX 12-Cores 3.99GHz, 1 CPU, 24 logical and 12 physical cores
Memory: 63.86 GB Total, 44.02 GB Available
.NET SDK 11.0.100-preview.5.26255.101
[Host] : .NET 11.0.0 (11.0.0-preview.5.26255.101, 11.0.26.25601), X64 RyuJIT x86-64-v3
DefaultJob : .NET 11.0.0 (11.0.0-preview.5.26255.101, 11.0.26.25601), X64 RyuJIT x86-64-v3 
Method 
Mean 
Completed Work Items 
Allocated 
Events (old) 
71.21 ms 
2006.0000 
612.58 KB 
ReadToEndAsync (old) 
70.33 ms 
2004.0000 
636.67 KB 
RunAndCaptureText (new) 
68.11 ms 
– 
132.58 KB 
RunAndCaptureTextAsync (new) 
70.66 ms 
2004.0000 
534.09 KB 
// * Legends *
Completed Work Items : The number of work items that have been processed in ThreadPool (per single operation)
Allocated : Allocated memory per single operation (managed only, inclusive, 1KB = 1024B) 
As you can see, on Windows the synchronous RunAndCaptureText method is about 2-3 ms faster than the old approaches and allocates about 4.5x less memory. It also doesn’t use thread pool at all.
BenchmarkDotNet v0.16.0-nightly.20260505.517, Linux Ubuntu 24.04.4 LTS (Noble Numbat)
AMD Ryzen Threadripper PRO 3945WX 12-Cores 3.99GHz, 1 CPU, 24 logical and 12 physical cores
Memory: 31.27 GB Total, 29.69 GB Available
.NET SDK 11.0.100-preview.5.26255.101
[Host] : .NET 11.0.0 (11.0.0-preview.5.26255.101, 11.0.26.25601), X64 RyuJIT x86-64-v3
DefaultJob : .NET 11.0.0 (11.0.0-preview.5.26255.101, 11.0.26.25601), X64 RyuJIT x86-64-v3 
Method 
Mean 
Completed Work Items 
Allocated 
Events (old) 
4.494 ms 
90.8359 
178.79 KB 
ReadToEndAsync (old) 
4.831 ms 
78.0313 
108.43 KB 
RunAndCaptureText (new) 
4.488 ms 
– 
48.9 KB 
RunAndCaptureTextAsync (new) 
4.738 ms 
84.1641 
81.6 KB 
On Linux, the new methods allocate about 2-4x less memory and the synchronous method also does not use thread pool at all.
Handle inheritance 
In case of pipes, the end of the file (EOF) is reached when all handles to its write end have been closed. Process closes its own copy of the write end of the pipe after starting the process, but in order for the pipe to be used by the child process, it must be inherited, which requires the pipe to be inheritable. When a process is started, it by default inherits all inheritable handles from the parent process, which opens the door for another two issues that can lead to deadlocks:
when a sibling process started concurrently inherits the pipe handle and keeps it open, 
when a grandchild process inherits the pipe handle and keeps it open after the child process exits. 
From .NET perspective, there is no way to prevent this kind of accidental handle inheritance by the grandchild process, as the child process can do whatever it wants with the handles it inherits from the parent. The best we can do is to provide an API that allows the child process to inherit only selected handles. And this is exactly what we have done by introducing ProcessStartInfo.InheritedHandles property ( PR ) that allows you to specify which handles should be inherited by the child process.
public class ProcessStartInfo
{
public IList<SafeHandle>? InheritedHandles { get; set; } = null;
} 
Due to backwards compatibility reasons, the new property is set to null by default, which means that the behavior is the same as before – all inheritable handles are inherited. If you set it to an empty list, only standard handles will be inherited. If you set it to a list of specific handles, those handles will be inherited along with the standard handles.
Request for feedback: we are considering extending all the new APIs that capture process output with an ability to stop when the process exits but the pipes remain open. Please let us know if you are interested in this feature.
Important: handles in this list should not have inheritance enabled beforehand. If they do, they could be unintentionally inherited by other processes started concurrently with different APIs, which may lead to security or resource management issues.
Note: as of today only SafeFileHandle and SafePipeHandle are supported, if you need more, please let us know.
Performance implications: if InheritedHandles is not null :
In short: as long as you don’t run on old Linux kernels (prior to 5.9), there should be no performance regression compared to the old behavior when inheriting all handles.
On Windows we acquire only a reader lock when starting new process. It means that if you are starting multiple processes in parallel and they are all setting InheritedHandles , they won’t be blocked on process creation as they would be if we used a global lock. 
On Unix, we use the best available sys-call to ensure that only the specified handles are inherited by the child process:
On Apple platforms, we always use posix_spawn with POSIX_SPAWN_CLOEXEC_DEFAULT flag, which is supported by all versions supported by current .NET. 
On Linux, we use close_range or __NR_close_range if they are available and enabled. 
On FreeBSD we use close_range (available since FreeBSD 12.2). 
On Illumos/Solaris, we use fdwalk . 
If none of the above is available (or enabled), we fallback to iterating over all file descriptors and setting FD_CLOEXEC manually. This is expensive and can cause major performance regression. Mostly for Linux kernels prior to 5.9 (except RHEL 8.0 which backported it). 
Let’s benchmark the performance implications!
public class GlobalLock
{
private ProcessStartInfo info;
[Params(true, false)]
public bool SetInheritedHandles { get; set; }
[GlobalSetup]
public void Setup()
{
info = OperatingSystem.IsWindows()
? new("cmd.exe", ["/c", "exit 42"])
: new("sh", ["-c", "exit 42"]);
info.InheritedHandles = SetInheritedHandles ? [] : null;
}
[Benchmark]
public ParallelLoopResult Run() => Parallel.For(0, 1_000, (_, _) => _ = Process.Run(info));
} 
We can see that on this Windows machine, the throughput has doubled:
BenchmarkDotNet v0.16.0-nightly.20260505.517, Windows 11 (10.0.26200.8246/25H2/2025Update/HudsonValley2)
AMD Ryzen Threadripper PRO 3945WX 12-Cores 3.99GHz, 1 CPU, 24 logical and 12 physical cores
Memory: 63.86 GB Total, 32.5 GB Available
.NET SDK 11.0.100-preview.5.26255.101
[Host] : .NET 11.0.0 (11.0.0-preview.5.26255.101, 11.0.26.25601), X64 RyuJIT x86-64-v3
Dry : .NET 11.0.0 (11.0.0-preview.5.26255.101, 11.0.26.25601), X64 RyuJIT x86-64-v3
InvocationCount=1 IterationCount=10 LaunchCount=1
UnrollFactor=1 WarmupCount=1 
Method 
SetInheritedHandles 
Mean 
Run 
False 
4.014 s 
Run 
True 
1.958 s 
Redirecting standard handles 
Another way to limit handle inheritance issues is to let the users redirect standard handles to any file handle they want, without the need to make it inheritable. It’s now possible to redirect standard handles to any file handle ( PR ), which opens up new scenarios such as:
process piping , 
redirecting to a file, 
redirecting to a null handle (it reports 0 bytes read/written for every operation):
starting process with no input, 
discarding output, 
starting process with async handles (advanced, niche scenario), 
breaking inheritance chain by redirecting standard handles to other handles than parent process handles. 
The new API comes with a few new enablers ( File.OpenHandle already existed) that make it easier to use:
namespace System.Diagnostics
{
public class ProcessStartInfo
{
public SafeFileHandle? StandardInputHandle { get; set; }
public SafeFileHandle? StandardOutputHandle { get; set; }
public SafeFileHandle? StandardErrorHandle { get; set; }
}
}
namespace Microsoft.Win32.SafeHandles
{
public class SafeFileHandle
{
public static SafeFileHandle CreateAnonymousPipe(out SafeFileHandle readPipe, out SafeFileHandle writePipe, 
bool asyncRead = false, bool asyncWrite = false);
}
}
namespace System.IO
{
public static class File
{
public static SafeFileHandle OpenHandle(string path, FileMode mode = FileMode.Open, FileAccess access = FileAccess.Read, FileShare share = FileShare.Read, FileOptions options = FileOptions.None, long preallocationSize = 0);
public static SafeFileHandle OpenNullHandle();
}
}
namespace System
{
public static class Console
{
public static SafeFileHandle OpenStandardInputHandle();
public static SafeFileHandle OpenStandardOutputHandle();
public static SafeFileHandle OpenStandardErrorHandle();
}
} 
Let’s pipe ls /usr/bin into grep zip and redirect the output to a file to find zip-related commands:
ls /usr/bin | grep zip > output.txt 
And now we’re going to implement the same thing in C# with the new APIs.
SafeFileHandle.CreateAnonymousPipe(out SafeFileHandle readPipe, out SafeFileHandle writePipe);
using (readPipe)
using (writePipe)
using (SafeFileHandle outputFile = File.OpenHandle("output.txt", FileMode.Create, FileAccess.Write))
{
ProcessStartInfo producer = new("ls", ["/usr/bin"])
{
StandardOutputHandle = writePipe
};
// Start consumer with input from the read end of the pipe, writing output to file
ProcessStartInfo consumer = new("grep", ["zip"])
{
StandardInputHandle = readPipe,
StandardOutputHandle = outputFile,
};
using Process producerProcess = Process.Start(producer)!;
// The producer process has its own copy of the write end of the pipe, we need to dispose the parent copy.
writePipe.Dispose();
using Process consumerProcess = Process.Start(consumer)!;
// The consumer process has its own copy of the read end of the pipe, we need to dispose the parent copy.
readPipe.Dispose();
await producerProcess.WaitForExitAsync();
await consumerProcess.WaitForExitAsync();
} 
Note: all of the new enablers create non-inheritable handles but Process knows how to make them inheritable when starting the process, so you don’t have to worry about handle inheritance at all.
Other SafeFileHandle improvements 
It’s worth noting that SafeFileHandle class has also received some new features that make it easier to work with:
Type property to check if the handle type is a file, pipe, console, etc ( PR ). 
IsAsync returns true on Unix only if the handle has O_NONBLOCK flag enabled. 
All read and write RandomAccess methods now support non-seekable handles ( PR ) such as pipes, which makes it possible to use them without the need to use FileStream . 
namespace System.IO
{
public enum FileHandleType
{
Unknown = 0,
RegularFile,
Pipe,
Socket,
CharacterDevice,
Directory,
SymbolicLink,
BlockDevice,
}
}
namespace Microsoft.Win32.SafeHandles
{
public class SafeFileHandle
{
public FileHandleType Type { get; }
}
} 
Lifetime management 
Process.StartAndForget 
There is a common misconception that when a process is disposed, it’s also being killed. This is not the case, as Process.Dispose only releases the resources associated with the process, but does not kill it.
To make it easier to start a process without the need to worry about disposing it, we have introduced Process.StartAndForget method that starts a process, returns its ID and releases all resources associated with it ( PR ).
public class Process
{
public static int StartAndForget(ProcessStartInfo startInfo);
public static int StartAndForget(string fileName, IList<string>? arguments = null);
} 
The usage is straightforward:
int processId = Process.StartAndForget("notepad.exe"); 
ProcessStartInfo.KillOnParentExit 
Processes started by the parent process are not automatically terminated when the parent process exits. This can lead to orphaned processes that keep running in the background, which is not desirable in many scenarios. To address this issue, we have introduced ProcessStartInfo.KillOnParentExit property that ensures that the child process is killed when the parent process exits (including forced terminations and crashes).
public class ProcessStartInfo
{
[SupportedOSPlatform("windows")] // introduced in .NET 11 Preview 4
[SupportedOSPlatform("linux")] // introduced in .NET 11 Preview 5
[SupportedOSPlatform("android")] // introduced in .NET 11 Preview 5
public bool KillOnParentExit { get; set; }
} 
This is achieved by using platform-specific features such as JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE on Windows ( PR ) and PR_SET_PDEATHSIG on Linux and Android ( PR ). In contrast to other APIs, the behavior is slightly different on different platforms:
On Windows, we need to use Job object to ensure that the child process is killed when the parent process exits. Job objects are by default inherited by all child processes, so if the child process spawns another process (a grandchild), that grandchild will also be terminated when the parent process exits. 
On Linux and Android, we use PR_SET_PDEATHSIG to specify a SIGKILL that the kernel will send to the child process when the thread that created the process exits. Since both Thread Pool and user threads can be terminated at any time, we maintain a dedicated thread used only for spawning processes with KillOnParentExit enabled, to ensure that the child processes are killed when the parent process exits. So when there are multiple processes started with KillOnParentExit , a synchronization mechanism is used to ensure that the dedicated thread spawns one process at a time. 
Request for feedback: we are considering extending the API to support killing child processes when the parent process exits on other Unix platforms as well. Since none of them provides a similar mechanism, we could handle only normal ( atexit ) and graceful terminations ( SIGTERM etc). If you are interested in this feature, please let us know.
ProcessStartInfo.StartDetached 
ProcessStartInfo.StartDetached property allows you to start a process that is detached from the parent process, which means that it will keep running even if the parent process exits, gets signaled or terminal is closed. This is achieved by using platform-specific features such as DETACHED_PROCESS flag on Windows and setsid on Unix ( PR ).
public class ProcessStartInfo
{
public bool StartDetached { get; set; }
} 
Moreover, if StartDetached is set to true and no redirection for standard handles is specified, standard handles will be redirected to null handle to avoid keeping parent standard handles open unnecessarily.
SafeProcessHandle 
Sometimes Process doesn’t cover your scenario – for example, you may need to P/Invoke CreateProcessAsUser on Windows or use a custom posix_spawn configuration on Unix. In those cases, you already have an OS process handle, but so far SafeProcessHandle has not provided any public APIs other than constructor. We’ve extended it with a set of focused APIs for the most common operations:
namespace Microsoft.Win32.SafeHandles
{
public class SafeProcessHandle : SafeHandle
{
public int ProcessId { get; }
public void Kill();
public bool Signal(PosixSignal signal);
public static SafeProcessHandle Start(ProcessStartInfo startInfo);
public bool TryWaitForExit(System.TimeSpan timeout, [NotNullWhen(true)] out ProcessExitStatus? exitStatus);
public ProcessExitStatus WaitForExit();
public Task<ProcessExitStatus> WaitForExitAsync(CancellationToken cancellationToken = default);
public Task<ProcessExitStatus> WaitForExitOrKillOnCancellationAsync(CancellationToken cancellationToken);
public ProcessExitStatus WaitForExitOrKillOnTimeout(TimeSpan timeout);
}
} 
The Process class itself already exposes SafeProcessHandle via Process.SafeHandle property, so you can use the new APIs even if you are using Process class:
[UnsupportedOSPlatform("windows")] // SIGTERM is not supported on Windows
ProcessExitStatus TerminateProcess(Process process)
{
// First try to terminate the process gracefully with SIGTERM
process.SafeHandle.Signal(PosixSignal.SIGTERM);
if (process.SafeHandle.TryWaitForExit(TimeSpan.FromSeconds(3), out ProcessExitStatus? exitStatus))
{
return exitStatus;
}
// If the process is still running after the timeout, kill it forcefully with SIGKILL
process.SafeHandle.Signal(PosixSignal.SIGKILL);
return process.SafeHandle.WaitForExit();
} 
Or if you want to kill the process if it doesn’t exit within a certain timeout:
using SafeProcessHandle processHandle = SafeProcessHandle.Start(new ProcessStartInfo("myapp.exe"));
ProcessExitStatus exitStatus = processHandle.WaitForExitOrKillOnTimeout(TimeSpan.FromMinutes(1));
if (exitStatus.Canceled)
{
Console.WriteLine("The process was killed after timeout.");
} 
Trimmability 
SafeProcessHandle also offers better trimmability. Let’s publish a NativeAOT app that starts a process and waits for it to exit.
Using SafeProcessHandle :
using SafeProcessHandle handle = SafeProcessHandle.Start(new ProcessStartInfo("whoami"));
handle.WaitForExit(); 
And Process :
using Process process = Process.Start(new ProcessStartInfo("whoami"))!;
process.WaitForExit(); 
dotnet publish -c Release -r win-x64 -p:PublishAot=true
dotnet publish -c Release -r linux-x64 -p:PublishAot=true 
Type 
.NET Version 
OS 
Size (bytes) 
vs .NET 10 Process 
Process 
.NET 10 
Windows x64 
1 730 048 
baseline 
Process 
.NET 11 
Windows x64 
1 389 056 
-19.7% 
SafeProcessHandle 
.NET 11 
Windows x64 
1 178 624 
-31.9% 
Process 
.NET 10 
Linux x64 
2 113 808 
baseline 
Process 
.NET 11 
Linux x64 
2 043 768 
-3.3% 
SafeProcessHandle 
.NET 11 
Linux x64 
1 816 504 
-14.1% 
The size on disk improvements for Process ( PR ) include a community contribution from Red Hat. It’s worth noting that Tom Deseyn from Red Hat has contributed a LOT to this release by reviewing the Linux implementations of the new APIs, so a big thank you to him!
Notable performance improvements 
Improved scalability on Windows 
So far, both Process.BeginOutputReadLine and Process.BeginErrorReadLine were creating a background task that was performing blocking read on the output/error pipe. So for every process that was started with redirected output and error that used the Begin[Output/Error]ReadLine methods, two thread pool threads were being blocked ( #81896 ). For years, we have believed that it’s impossible to solve this issue on Windows, as there is no support for truly asynchronous I/O operations on anonymous pipes.
But when reading the documentation , we have found out that:
“Anonymous pipes are implemented using a named pipe with a unique name. Therefore, you can often pass a handle to an anonymous pipe to a function that requires a handle to a named pipe.”
We knew that named pipes support truly asynchronous I/O operations on Windows and combined with our previous experience from File IO improvements in .NET 6 we knew that it’s possible to open one end of named pipe for asynchronous IO and the other end for synchronous IO (99.99% of applications expect standard handles to be opened for synchronous IO).
We studied the CreatePipe implementation and ensured ( PR ) that the new approach does not introduce any breaking changes. Starting from .NET 11 Preview 4, on Windows, when you start a process with redirected output and error, the pipes are created as named pipes with the read end opened for asynchronous IO and the write end opened for synchronous IO. This allows us to use truly asynchronous IO operations on the output and error pipes without blocking any threads.
Last but not least, we have exposed the ability to create anonymous pipes using SafeFileHandle.CreateAnonymousPipe method, which creates a pair of connected pipes and returns their handles. This method is available on both Windows and Unix, and it abstracts away the platform-specific details of creating pipes.
All of that translates into much better scalability when starting multiple processes in parallel with redirected output and error on Windows, as we are no longer blocking thread pool threads for every process.
public class BeginReadLineBenchmarks
{
private static readonly ProcessStartInfo _processStartInfo = CreateStartInfo();
private static ProcessStartInfo CreateStartInfo()
{
ProcessStartInfo startInfo = OperatingSystem.IsWindows()
? new("cmd.exe", "/c for /L %i in (1,1,1000) do @echo Line %i")
: new("sh", ["-c", "for i in $(seq 1 1000); do echo \"Line $i\"; done"]);
startInfo.RedirectStandardOutput = true;
startInfo.RedirectStandardError = true;
return startInfo;
}
[Benchmark]
public ParallelLoopResult Run() => Parallel.For(0, 300, static (_, _) => _ = Events());
private static int Events()
{
using Process process = new();
process.StartInfo = _processStartInfo;
StringBuilder stdOut = new(), stdErr = new();
process.OutputDataReceived += (sender, e) => stdOut.AppendLine(e.Data);
process.ErrorDataReceived += (sender, e) => stdErr.AppendLine(e.Data);
process.Start();
process.BeginOutputReadLine();
process.BeginErrorReadLine();
process.WaitForExit();
return process.ExitCode;
}
} 
BenchmarkDotNet v0.16.0-nightly.20260505.517, Windows 11 (10.0.26200.8246/25H2/2025Update/HudsonValley2)
AMD Ryzen Threadripper PRO 3945WX 12-Cores 3.99GHz, 1 CPU, 24 logical and 12 physical cores
Memory: 63.86 GB Total, 39.4 GB Available
.NET SDK 11.0.100-preview.5.26255.101
[Host] : .NET 10.0.7 (10.0.7, 10.0.726.21808), X64 RyuJIT x86-64-v3
.NET 10.0 : .NET 10.0.7 (10.0.7, 10.0.726.21808), X64 RyuJIT x86-64-v3
.NET 11.0 : .NET 11.0.0 (11.0.0-preview.5.26255.101, 11.0.26.25601), X64 RyuJIT x86-64-v3 
Method 
Job 
Runtime 
Mean 
Ratio 
Run 
.NET 10.0 
.NET 10.0 
5.307 s 
1.00 
Run 
.NET 11.0 
.NET 11.0 
2.936 s 
0.57 
As you can see, for this particular micro-benchmark and machine, the throughput has improved by about 1.8x. The improvement will be even more significant when starting more processes in parallel, as we are no longer blocking thread pool threads for every process.
Improved process creation on apple platforms 
In order to implement ProcessStartInfo.InheritedHandles on apple platforms (macOS, MacCatalyst), we had to switch from fork + exec to posix_spawn ( PR ). To tell the long story short, it offers much better performance on apple platforms, especially on the arm64 architecture.
When running following benchmarks:
[MemoryDiagnoser]
public class ProcessStartBenchmarks
{
private static ProcessStartInfo s_startProcessStartInfo = new ProcessStartInfo()
{
FileName = "whoami", // exists on both Windows and Unix, and has very short output
RedirectStandardOutput = true // avoid visible output
};
private Process? _startedProcess;
[Benchmark]
public void Start()
{
_startedProcess = Process.Start(s_startProcessStartInfo)!;
}
[IterationCleanup(Target = nameof(Start))]
public void CleanupStart()
{
if (_startedProcess != null)
{
_startedProcess.WaitForExit();
_startedProcess.Dispose();
_startedProcess = null;
}
}
[Benchmark]
public void StartAndWaitForExit()
{
using (Process p = Process.Start(s_startProcessStartInfo)!)
{
p.WaitForExit();
}
}
} 
We have observed an impressive improvement of about 98x on Apple Silicon and about 4.5x on x64 machines:
BenchmarkDotNet v0.15.8, macOS Sequoia 15.4.1 (24E263) [Darwin 24.4.0]
Apple M4, 1 CPU, 10 logical and 10 physical cores
.NET SDK 11.0.100-preview.3.26174.112
[Host] : .NET 10.0.5 (10.0.5, 10.0.526.15411), Arm64 RyuJIT armv8.0-a 
Method 
Toolchain 
Mean 
Error 
Ratio 
StartAndWaitForExit 
/PR_126063/corerun 
1,246.5 us 
5.26 us 
1.00 
StartAndWaitForExit 
/main/corerun 
8,945.9 us 
80.30 us 
7.18 
Start 
/PR_126063/corerun 
122.0 us 
2.40 us 
1.00 
Start 
/main/corerun 
12,043.2 us 
116.96 us 
98.86 
BenchmarkDotNet v0.15.8, macOS Sequoia 15.2 (24C101) [Darwin 24.2.0]
Intel Core i5-8500B CPU 3.00GHz (Coffee Lake), 1 CPU, 6 logical and 6 physical cores
.NET SDK 11.0.100-preview.3.26174.112
[Host] : .NET 10.0.5 (10.0.5, 10.0.526.15411), X64 RyuJIT x86-64-v3 
Method 
Toolchain 
Mean 
Ratio 
StartAndWaitForExit 
PR #126063 
3,163.3 μs 
1.00 
StartAndWaitForExit 
main 
4,981.3 μs 
1.58 
Start 
PR #126063 
417.4 μs 
1.00 
Start 
main 
1,998.9 μs 
4.80 
Reduced memory allocations on Unix 
We have also reduced memory allocation by 30-50% when starting process on Unix ( PR ).
BenchmarkDotNet v0.15.8, macOS Sequoia 15.4.1 (24E263) [Darwin 24.4.0]
Apple M2, 1 CPU, 8 logical and 8 physical cores
.NET SDK 11.0.100-preview.3.26178.103
[Host] : .NET 10.0.5 (10.0.5, 10.0.526.15411), Arm64 RyuJIT armv8.0-a 
Method 
Toolchain 
Mean 
Allocated 
Alloc Ratio 
StartAndWaitForExit 
/bfe7a08/corerun 
1,570.2 us 
15.83 KB 
1.00 
StartAndWaitForExit 
/bfe7a08~1/corerun 
1,569.0 us 
23.92 KB 
1.51 
Start 
/bfe7a08/corerun 
173.0 us 
15.83 KB 
1.00 
Start 
/bfe7a08~1/corerun 
176.5 us 
23.98 KB 
1.51 
Call to Action 
All of these improvements are available today in .NET 11 Preview 4 . Give it a try, and let us know what you think – leave a comment here or file issues or feature requests at dotnet/runtime . We’d love your feedback!
