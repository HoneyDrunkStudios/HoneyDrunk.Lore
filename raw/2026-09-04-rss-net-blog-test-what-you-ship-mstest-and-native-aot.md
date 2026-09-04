---
source: "https://devblogs.microsoft.com/dotnet/mstest-source-generation/"
title: "Test what you ship: MSTest and Native AOT"
author: "Amaury Levé"
date_published: "2026-09-03"
date_clipped: "2026-09-04"
category: ".NET Ecosystem"
source_type: "rss"
---

# Test what you ship: MSTest and Native AOT

Source: https://devblogs.microsoft.com/dotnet/mstest-source-generation/

If you ship an application with
Native AOT ,
a green managed test run leaves a gap. Native AOT compiles ahead of time,
removes unused code ,
and requires alternatives to runtime code generation and unrestricted
reflection. The published application can therefore behave differently from
the code exercised by the managed test process.
Starting with MSTest 4.4, MSTest supports publishing and running test projects
as Native AOT executables. Source generation records which tests exist and how
to invoke them before trimming happens, without requiring developers to rewrite
their test classes. The result is simple: test what you ship .
For teams with formal validation plans, including some in regulated
environments, that native run provides more representative evidence. It doesn’t
replace testing the final application artifact.
A managed pass can still hide a deployment failure
Consider an application that serializes a receipt with System.Text.Json and a
test that covers that path:
[TestClass]
public class ReceiptFormatterTests
{
[TestMethod]
public void ReceiptIsSerialized()
{
var json = JsonSerializer.Serialize(new Receipt(42));
StringAssert.Contains(json, "\"Total\":42");
}
}
public sealed record Receipt(decimal Total);
The test passes in a normal managed run because System.Text.Json can discover
the type through reflection. In a trimmed or Native AOT publish,
reflection-based serialization is disabled by default. The same path throws:
System.InvalidOperationException:
Reflection-based serialization has been disabled for this application.
That failure is useful. It identifies an application deployment problem, not a
testing-framework problem. The production code should provide generated JSON
metadata, for example:
[JsonSerializable(typeof(Receipt))]
internal partial class AppJsonContext : JsonSerializerContext
{
}
var json = JsonSerializer.Serialize(
new Receipt(42),
AppJsonContext.Default.Receipt);
The
System.Text.Json source-generation guidance
describes this behavior and the available generation modes. Serialization is
only one example; native testing can also expose unsupported runtime code
generation, missing reflection metadata, or an incompatible dependency.
There are two separate responsibilities here. MSTest source generation keeps
the test discoverable and runnable after trimming. The JSON source generator
fixes the application path that the test exercises. MSTest doesn’t hide the
application problem; it lets the native test process expose it before the
product reaches deployment.
How MSTest makes the native test executable possible
MSTest’s first
Native AOT preview
arrived in April 2024. It proved that an MSTest project could become a native
executable, but the experimental engine and source generator had limited
coverage.
The new path moves source generation into the open MSTest toolchain and aligns
it with MSTest 4.4. During compilation, the generator emits:
A registry of the test classes in the assembly.
Attribute data for supported test members.
Delegates that construct test classes and invoke test methods.
References that preserve discovered test classes and supported base classes
when trimming runs.
The important result isn’t the generated code itself. The build records which
tests exist and how to run them before trimming happens. Your tests remain
ordinary [TestClass] and [TestMethod] code; the generator changes the build
and execution path, not the programming model.
Configure one representative project
With the targeted release, the minimum project configuration is deliberately
small:
For engineering leaders
Keep the fast managed test lane, then pilot one additional native
publish-and-run lane. The cost is extra CI publish time and, for VSTest users,
migration to Microsoft Testing Platform. Success means identical test counts
and outcomes, acceptable CI time, and earlier detection of deployment-only
defects.
<Project Sdk="MSTest.Sdk/4.4.0">
<PropertyGroup>
<TargetFramework>net10.0</TargetFramework>
<PublishAot>true</PublishAot>
</PropertyGroup>
<!-- Keep your existing ItemGroup elements and project references. -->
</Project>
MSTest.Sdk uses Microsoft Testing Platform (MTP) by default. Setting
PublishAot enables MSTest source generation and the native executable path.
Projects that still use VSTest should review the
VSTest-to-MTP migration guidance
because command-line arguments, CI integration, and supported .runsettings
entries differ.
Publish for the same operating system and architecture as the application:
dotnet publish ./MyProject.Tests/MyProject.Tests.csproj \
-c Release -r linux-x64 -o ./artifacts/native-tests
./artifacts/native-tests/MyProject.Tests
The example uses the linux-x64 runtime identifier (RID). Replace it with the
RID you deploy, such as win-x64 or osx-arm64 ; on Windows, run
MyProject.Tests.exe . Replace the project path with your test project.
Then add a focused CI pilot:
Keep the existing managed test run.
Publish and run one representative test project as Native AOT.
Assert that both lanes discover the exact expected test count and outcomes.
Record native publish-and-run time separately from test execution time.
Expand only where the additional confidence justifies the CI cost.
This isn’t expected after a clean migration. It can happen when a test class
can’t enter the generated registry—for example, because it only inherits
[TestClass] or is inaccessible, file-local, static, or open generic—and the
related diagnostics are ignored or suppressed. The registered subset can still
pass and the process can exit successfully, so test-count parity is a release
gate.
Start with a scheduled or release-validation job. Move the lane to every pull
request only if its signal and publish time justify the added feedback cost.
Choose a project with meaningful deployment-sensitive paths: serialization,
dependency injection, configuration binding, reflection-based plugins, or a
dependency whose Native AOT support you need to prove. A project containing
only arithmetic-style unit tests can demonstrate that the runner works, but it
won’t tell you much about the application you ship.
Run both layers
Managed tests optimize the development feedback loop. The native lane checks
the deployment model. They answer different questions and are most useful
together.
Keep the boundaries clear
This isn’t equivalent to an end-to-end production validation. Configuration,
operating system, architecture, external services, and packaging can still
differ. It removes one important variable: the test and application can use the
same trimming and ahead-of-time compilation model.
Source generation also doesn’t mean zero reflection. The default
ReflectionFree mode uses generated attributes and delegates for supported
construction and invocation, but some operations retain reflective fallbacks.
For compatibility investigations, set:
<PropertyGroup>
<MSTestSourceGenMode>Rooting</MSTestSourceGenMode>
</PropertyGroup>
Rooting preserves discovered test members but uses reflective execution.
The most important migration limits are:
Limitation
Migration guidance
A class only inherits [TestClass]
Declare the attribute directly; MSTEST0069 identifies this shape.
A test class is inaccessible, file-local, static, abstract, or open generic
Use a concrete, accessible, non-static, closed type. Abstract base fixtures remain supported through a concrete derived test class.
A test method is generic or has ref , out , or in parameters
Use a supported method signature.
[AssemblyFixtureProvider] is used
Replace it with a supported fixture pattern before relying on the native run.
Some MSTest SDK integrations, MTP extensions, and CI reporters aren’t available
in the Native AOT path. TRX and Code Coverage remain supported. Treat analyzer
and build diagnostics as migration gates rather than warnings to suppress, and
check the
MSTest SDK documentation
for the current support matrix.
For a team, the change should stay deliberately narrow:
Keep
Add
Still required
Fast managed tests for everyday feedback
One published native test lane for selected projects
End-to-end validation of the final application artifact
That separation makes the rollout reversible. If the native lane costs more
than the confidence it adds, change its frequency, choose a more representative
project, or stop the pilot without disrupting the managed test suite.
Performance is evidence, not the premise
Source generation avoids the assembly-wide Assembly.GetTypes() scan and
reflective construction and invocation for supported tests. That can reduce
startup and discovery work, but it doesn’t guarantee a faster end-to-end run;
test execution, process startup, publishing, and remaining reflection can
dominate.
Production fidelity is useful even if the performance improvement is small.
Performance is secondary, not the reason to test under the deployment model
you ship.
Start with one project
Choose a project that exercises code you publish with Native AOT. Use the next
deployment-only failure, test-count mismatch, or clean native run to evaluate
whether the lane adds useful confidence. Then decide whether to expand, refine,
or stop the pilot.
With MSTest 4.4 and a verified native publish path, the tests still look like
MSTest while the executable behaves more like the application you actually
ship.
Prepare an MSTest project for Native AOT
