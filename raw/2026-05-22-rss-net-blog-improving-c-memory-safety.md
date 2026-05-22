---
source: "https://devblogs.microsoft.com/dotnet/improving-csharp-memory-safety/"
title: "Improving C# Memory Safety"
author: ".NET Blog"
date_published: "Thu, 21 May 2026 16:08:00 +0000"
date_clipped: "2026-05-22"
category: ".NET Ecosystem"
source_type: "rss"
---

# Improving C# Memory Safety

Source: https://devblogs.microsoft.com/dotnet/improving-csharp-memory-safety/

We’re in the process of significantly improving memory safety in C# . The unsafe keyword is being redesigned to inform callers that they have obligations that must be discharged to maintain safety, documented via a new safety comment style. The keyword will expand from marking pointers to any code that interacts with memory in ways the compiler cannot validate as safe. The compiler will enforce that the unsafe keyword is used to encapsulate unsafe operations. The result is that safety contracts and assumptions become visible and reviewable instead of implied by convention.
We plan to release the new model and syntax (nominally a C# 16 feature) as a preview in .NET 11 and as a production release in .NET 12. It will initially be opt-in and may become the default in a later release. We will update templates to enable the new model just like we have done with nullable reference types. The early compiler implementation has landed in main and is taking shape.
C# 1.0 introduced the unsafe keyword as the way to establish an unsafe context on types, methods, and interior method blocks, letting developers choose the most convenient scope. An unsafe context grants access to pointer features. A method marked unsafe can use those features in its signature and implementation while unmarked methods cannot. We also exposed a set of unsafe types like System.Runtime.CompilerServices.Unsafe and System.Runtime.InteropServices.Marshal that required careful usage as a convention.
The unsafe keyword has since been reused and remixed in Rust and Swift, where those language teams gave it stricter, propagation-oriented semantics. C# 16 follows the same path, applies unsafe uniformly (including on Unsafe and Marshal members) in the .NET runtime libraries, and most closely resembles the Rust implementation. The result: unsafe stops marking a kind of syntax and starts marking a kind of contract; one the compiler can’t verify, that a skilled developer has to read and uphold.
C# already blocks unsafe code by default. Most developers won’t notice any change when they enable the new model because they don’t enable or use unsafe APIs. The default block will cover a much larger surface area when the C# 16 safety model is enabled. The new model establishes strong guard rails that are visible, reviewable, and enforced by the compiler. It is also an important tool to enforce engineering and supply chain standards. Memory safety has been a rising priority across industry and government for several years, and AI-assisted code generation adds a new dimension as software production scales faster than human review.
Safety 
An earlier post discusses the structural safety mechanisms in .NET:
safety is enforced by a combination of the language and the runtime … Variables either reference live objects, are null, or are out of scope. Memory is auto-initialized by default such that new objects do not use uninitialized memory. Bounds checking ensures that accessing an element with an invalid index will not allow reading undefined memory — often caused by off-by-one errors — but instead will result in a IndexOutOfRangeException .
Source: What is .NET, and why should you choose it? 
C# comes with strong safety enforcement for regular safe code. The new model enables developers and agents to accurately mark safety boundaries in unsafe code. There are two reasons to write unsafe code: interoperating with native code, and in some cases for performance. Go, Rust, and Swift also include an unsafe dialect for these cases. The language typically cannot help you write unsafe code; its role is to make clear where unsafe code is used and how it transitions back to safe code.
Programming safety may be easier to understand if we consider another domain. Road designers improve safety by painting solid yellow or white lines that prohibit crossing into oncoming traffic. Drivers understand and abide by this convention. High-speed highways use barriers to provide safety via structural separation that continues to function in the absence of sober compliance. The highway example shows us that higher speeds come with higher stakes.
Programming has its own kind of accidents, with memory. Every application has potential access to gigabytes of virtual memory. Writing to or reading from arbitrary memory results in arbitrary behavior ( Undefined Behavior , or UB , is the industry term) and is the cause of most security bugs . Accessing arbitrary memory isn’t possible in safe code, but is an ever-present possibility in unsafe code.
The model in a nutshell 
.NET programs are expected to uphold one core invariant: every memory access targets live memory : memory that is allocated, initialized, and available at the time of access. Safe code upholds this by construction: compiler rules and runtime checks combine to make a stray access impossible. Unsafe code is any operation that can violate the invariant, typically by reading or writing memory that isn’t live, or by leaving memory in a state where a later access will fail.
Unsafe code can read or write arbitrary memory accessed via interop, by NativeMemory , or hand-managed by the developer. The invariant must hold all the same. The compiler can’t detect UB there, so the burden of validation shifts to the developer.
The solution to this risk is a layered set of mechanics that intentionally and transparently push unsafety through the call graph, each layer enabling the next:
Inner unsafe { } block : every unsafe operation (calling an unsafe member, dereferencing a pointer, and other unsafe actions) must appear inside an inner unsafe { } block. This is the base mechanic. Unsafe operations are syntactically marked, scoped, and reviewable. 
Propagation : adding unsafe to the enclosing method’s signature republishes the inner block’s obligations to its own callers, unless discharged. This carves the call graph into safe methods, unsafe methods, and the boundary methods between them. Developers can chain propagation through any number of intermediates before someone decides to stop. 
Safety documentation : every unsafe member should carry a /// <safety> block: the formal contract between callee and caller. Authoring it is a strongly encouraged best practice, and analyzers can flag its absence. 
Suppression at the boundary : a method that contains an inner unsafe block but does not mark its own signature unsafe is the boundary between unsafe and safe code. It discharges the callee’s documented obligations, through runtime guards on inputs, static reasoning, or documented invariants from upstream APIs (e.g., malloc guaranteeing the returned pointer is valid for at least size bytes). Correct discharge is what makes safe callers actually safe. 
You have to step through each layer to get the value. Do half the work and you get much less than half the value. Step through each layer correctly and you have a connected line of reasoning through a call graph that others can review and potentially improve.
Writing unsafe code is a special skill that requires a strong understanding of this invariant and of many pitfalls. The new model makes unsafe code easier to reason about and review, not easier to write — it forces a formal, visible structure. The keywords and compiler enforcement aren’t the safety; they’re the scaffolding that gets developers to articulate and honor it.
C# 1.0 grouped a category of “pointer features” under unsafe : declaring and dereferencing pointer types, taking the address of variables, stackalloc to a pointer, sizeof on arbitrary types, and other capabilities added over the years, including the suppression of certain compiler errors. The new model is more selective.
Changes relative to C# 1.0 rules include:
The unsafe type modifier produces an error. Unsafe scope moves down to individual methods, properties, and fields, where its contract is in view and more minimally specified. Delegates also cannot be unsafe because they are type-shaped. 
unsafe is not allowed on static constructors or finalizers. Their invocations don’t have a call site pattern that can be wrapped in an unsafe { } block, so the signature marker has nothing to propagate. 
The new() generic constraint matches only a safe parameterless constructor; a type whose parameterless constructor is unsafe can’t satisfy new() . 
A new safe keyword lets a developer attest that a declaration is sound where the compiler requires the choice to be explicit. Today the only such place is extern declarations, which must be marked safe or unsafe , including LibraryImport partial method declarations. 
unsafe on a member no longer establishes an unsafe context. Interior unsafe blocks are now required at unsafe call sites. 
Pointer types in signatures no longer propagate unsafety. Only pointer dereferences are unsafe, so a byte* parameter doesn’t propagate unsafety to its callers on its own. For new code, avoid IntPtr for pointers; prefer typed pointers like byte* , or void* for truly opaque pointers. For existing IntPtr -based APIs, consider adding pointer-typed overloads and hiding or soft-obsoleting the IntPtr versions. For opaque handles, prefer SafeHandle . nint and IntPtr are indistinguishable in metadata, so when a parameter is genuinely a native-sized integer, document that explicitly. 
Adoption is via a new opt-in project-level property. See § Project-level opt-in for the details.
The model in practice 
Unsafe code significantly raises the stakes and is always unbounded in some dimension. The best unsafe APIs are designed to make the unboundedness as narrow as possible: pushing what they can into the signature, discharging what they can in the body, and leaving the caller with a small, well-defined residue to handle themselves.
Encoding.GetString(byte*, int) is a good example.
public unsafe string GetString(byte* bytes, int byteCount)
{
ArgumentNullException.ThrowIfNull(bytes);
ArgumentOutOfRangeException.ThrowIfNegative(byteCount);
return string.CreateStringFromEncoding(bytes, byteCount, this);
} 
The method clearly communicates what the API expects: the byte* parameter advertises a raw, unmanaged buffer, and the paired byteCount says exactly how many bytes the API will read. The body discharges what it can: a null pointer or negative length is rejected with an exception. The guards remove a subset of cases where string.CreateStringFromEncoding will silently read arbitrary memory. GetString returns a new string , removing any aliasing or lifetime concerns with the buffer.
The caller holds a single, narrow obligation: byteCount bytes starting at bytes must be readable memory. Passing a length larger than the buffer is undefined behavior: the decoder may run into unreadable memory and crash, or it may read whatever happens to live past the end and return a string built from arbitrary foreign bytes. In the existing model, the byte* in the signature is what prevents this API from being called from safe code. Under the new model, a pointer in a signature no longer implies unsafety on its own; GetString will be explicitly annotated unsafe so it stays uncallable from safe code.
“Better unsafe” isn’t defined by more or less dangerous, but by more or less descriptive of unsafety; sharp knives make the finest cuts, and dull ones tear.
Marshal.ReadByte is a more cautionary case.
public static unsafe byte ReadByte(IntPtr ptr, int ofs)
{
try
{
byte* addr = (byte*)ptr + ofs;
return *addr;
}
catch (NullReferenceException)
{
throw new AccessViolationException();
}
} 
Callers of Marshal.ReadByte pass an IntPtr and offset that together address a byte the program is allowed to read. The cautionary difference from GetString is that ReadByte doesn’t perform any input validation and is callable from safe code today. The try / catch clause doesn’t offer any safety, but is used to change the exception type, for only one scenario of misbehavior. The reason this is considered OK is that Marshal and Unsafe are conventionally understood to be unsafe to call.
We can dissect the method a bit further. Today’s unsafe signature on ReadByte establishes an unsafe context for the implementation but doesn’t create a caller contract or document a caller warning. The existing model propagates unsafety through pointer types in signatures, but IntPtr dodges that rule; the API is effectively pointer smuggling.
The new model closes this gap. It widens unsafety to cover any operation that can violate the live-memory invariant (not just operations involving pointer types), and makes the unsafe signature marker the member contract, with inner unsafe blocks encapsulating the unsafe operations. It also aligns the safety character of IntPtr and pointers like byte* : both can be held, assigned, and exposed in signatures outside an unsafe block; it is pointer dereference that is unsafe.
ReadByte changes with the new model, per the following mockup:
/// <summary>Reads a single byte from unmanaged memory.</summary>
/// <safety>
/// The sum of <paramref name="ptr"/> and <paramref name="ofs"/> must address a byte
/// the caller is permitted to read.
/// </safety>
public static unsafe byte ReadByte(IntPtr ptr, int ofs)
{
try
{
byte* addr = (byte*)ptr;
unsafe
{
// SAFETY: relies on caller obligation.
return addr[ofs];
}
}
catch (NullReferenceException)
{
throw new AccessViolationException();
}
} 
Let’s dig into the implementation. The cast (byte*)ptr is pointer manipulation, not a dereference; IntPtr and byte* are the same shape, different representation; both are just a number. The unsafety is on a single line: return addr[ofs] . That is the point where the developer needs to attest that addr + ofs addresses readable memory, since the indexing dereferences that address. byte* → byte requires copying memory from the pointer address into a value. That’s the dangerous operation.
The new model works because the pointer dereference, addr[ofs] , gets wrapped in an unsafe block, shining light on the unsafety. The unsafe signature becomes a caller contract, forcing callers to wrap their calls in an unsafe block as well, and a reminder to look at the callee safety doc.
A strict “smallest unsafe block” reading would put the + ofs arithmetic outside the block, since arithmetic on its own isn’t a dereference. We prefer to keep addr[ofs] together: indexing is the indirection ( addr[0] is by spec the same as *addr ), and grouping makes the exact address being read visible at the point of access. We expect these kinds of choices to be codified in unsafe coding guidelines over time.
Violations are compile errors, not warnings. The model isn’t an “honor system”. Take Marshal.ReadByte from above: it is marked unsafe because its implementation dereferences an opaque caller-supplied pointer. In the new model, it will continue to be marked unsafe because it passes a pointer validity obligation on to callers. The obligation was previously understood by convention. The compiler now requires Marshal.ReadByte to expose the obligation as a contract.
Propagation and suppression 
The safety marking system established by Rust is a good guide for propagation and suppression. C# 16 is adopting the same approach and syntax. The unsafe keyword is used in two ways. The first is an inner unsafe block that wraps an unsafe operation, typically due to calling another unsafe method and/or dereferencing a pointer. The second is an outer unsafe signature marker that defines a caller contract.
To propagate unsafety to the caller, the developer adds unsafe to the member signature; to suppress unsafety as an implementation detail, they leave unsafe absent. Presence or absence of unsafe on a member signature (for methods with inner unsafe ) is the compiler signal for propagation or suppression. Propagation pushes unsafety one caller higher while suppression caps unsafety by offering a safe-caller-compatible surface area.
C# 1.0 model 
C# 1.0 uses unsafe on a type or member to mean “unsafe context from this point”. It doesn’t inform or change the caller contract. Pointers are the sole propagation mechanism in C# 1.0. Inner unsafe can be used to tighten the scope of unsafety.
Let’s start with code that is legal today, in the C# 1.0 model.
void Caller()
{
M();
}
unsafe void M() { } 
Caller can call unsafe M without any ceremony.
The reason is twofold:
unsafe is being used to create an inner unsafe block for the entire method, not to define a caller contract. 
M doesn’t expose pointers, so doesn’t propagate unsafety. 
This example is analogous to ReadByte . Caller could call ReadByte just as freely as it is calling M . It could not call Encoding.GetString in the same way due to pointer usage.
We need to critique the existing model to understand why we are moving away from it. The roles and responsibilities of M and Caller are specified only by convention. There is no standard for the safety concerns or obligations that M should communicate to Caller or how Caller meets the expectations of its safe callers. In short, there is no overarching system that pushes developers towards actual safety or that enables straightforward auditing. Safety is currently deployed by skilled engineers who understand how to define obligations and risks, without help from the compiler.
C# 16 model 
The new model adopts unsafe on a method signature as a caller-facing propagation mechanism. The absence of unsafe is used to communicate suppression.
Caller from the previous example would have to be adjusted to either Caller1 or Caller2 below.
/// <safety>
/// Caller must satisfy obligation 1
/// </safety>
unsafe void Caller1()
{
unsafe
{
// SAFETY: Obligation is passed to caller.
M();
}
}
void Caller2()
{
if (/* obligation 1 not satisfied */) throw new Exception();
unsafe
{
// SAFETY: obligation 1 is discharged by the check above
M();
}
}
/// <safety>
/// Caller must satisfy obligation 1
/// </safety>
unsafe void M() { } 
Both M and Caller1 propagate unsafety to their callers. Caller2 suppresses the unsafety of its callees and is an unsafe boundary method. Either form is a valid replacement for Caller . The developer decides which is appropriate based on whether it is possible or desirable to validate obligation 1. If caller obligations remain, then Caller1 is the right choice. Choosing between propagation and suppression isn’t compiler-enforced (or compiler-suggested), but requires careful judgment.
Caller1 carries two unsafe markers by design: the outer one projects the caller contract, the inner one scopes the unsafe operations. Inside an unsafe member, omitting the inner unsafe block at an unsafe operation is a compile error; the signature marker no longer establishes an unsafe context on its own. This outer-propagates / inner-scopes shape matches Rust’s unsafe fn / unsafe { } and Swift’s @unsafe / unsafe expr .
Caller2 is safe-callable, placing no obligation on its callers and requiring no unsafe blocks at their call sites.
The model applies to any caller. The example above demonstrates callers on the same type. The model applies uniformly across types, projects, and packages. It also applies to source generators. There is no planned scoped opt-out mechanism.
The enforcement is compile-time only. The model introduces no new runtime checks and has no performance impact; existing runtime checks that result in exceptions like IndexOutOfRangeException and ArgumentNullException are unchanged.
The .NET runtime libraries will opt in. That’s necessary as the basis of the model for callers. Consuming a library that has opted in does not require your project to opt in, and vice versa. Cross-assembly behavior depends on which side has opted in:
Opted-in caller, opted-in callee. The new model. The callee’s unsafe markers travel via metadata, and the caller must wrap calls in an unsafe { } block; without one, the call is a compile error. 
Opted-in caller, non-opted-in (legacy) callee. Compat mode. The compiler treats any callee member with a pointer type in its signature as unsafe , requiring an enclosing unsafe { } block at the call site. Non-pointer unsafe surface ( IntPtr / nint parameters, P/Invoke signatures, and so on) isn’t flagged, because the legacy assembly carries no metadata to distinguish it. Compat mode prevents a “safety dip” where a legacy package’s unsafe APIs would silently lose their pointer-driven unsafe propagation when the new model is enabled. 
Non-opted-in caller, opted-in callee. No enforcement of the new model’s unsafe markers; the legacy caller can’t interpret them. Legacy C# 1.0 pointer rules still apply: a callee that exposes a pointer type in its signature still requires the legacy caller to be in an unsafe context. The gap is new-model unsafe methods that have no pointer types in their signature (e.g., unsafe byte ReadByte(IntPtr, int) ). Those become callable from legacy safe code. 
Migration of the runtime libraries is already underway: the reduce-unsafe label tracks the running list of PRs removing unsafe code from the libraries, including swaps like #127394 (replacing MemoryMarshal.Read / Write with BitConverter equivalents) and #127485 (removing unsafe code from IBinaryInteger.TryReadBigEndian ). This migration is also a sign that industrial code can be moved to safe patterns. Your unsafe code probably can, too.
To summarize the changes from C# 1.0:
unsafe on a member signature now defines a caller-facing contract that propagates unsafety up the call graph. C# 1.0 used it only to establish an unsafe context. 
An unsafe block is required at every call to an unsafe member. 
Cross-language comparison: propagation 
The differences between C#, Rust, and Swift are both subtle and instructive. C# 16 propagates unsafety only when the unsafe keyword appears on the member; pointer types and other unsafe-typed parameters do not propagate on their own. Rust behaves the same way: a *const u8 parameter on a plain fn propagates nothing. Swift is the outlier: any @unsafe type appearing in a signature implicitly makes the declaration @unsafe , in addition to the explicit @unsafe attribute.
The implicit Swift model leads to needing @safe as a broadly-applicable opt-out for APIs that encapsulate the unsafety (e.g., Array.withUnsafeBufferPointer ). Both C# and Rust include a narrow positive safe form for interop (FFI), but for different reasons. Rust’s safe fn inside an unsafe extern block is an override of the default. The block is unsafe by default and safe opts an individual declaration out, analogous in shape to Swift’s @safe . C# 16’s safe extern for LibraryImport declarations is not an override. It’s a statement about the whole declaration and it’s required because the language biases toward explicit markings and won’t let a developer leave a foreign declaration’s safety implicit.
Every LibraryImport partial method must be marked safe or unsafe :
[LibraryImport("libc")]
internal static safe partial int getpid();
[LibraryImport("libc", StringMarshalling = StringMarshalling.Utf8)]
internal static unsafe partial nint strlen(byte* str); 
getpid has no parameters and returns a primitive; the author attests that the call is sound and safe callers can use it without ceremony. strlen takes a raw pointer the native code will dereference; the author has no way to discharge that obligation at the boundary, so the declaration propagates unsafe and a <safety> block names the caller’s obligation. Omitting both modifiers is a compile error — the developer has to make the choice.
Let’s look at a propagation example. A short Rust program (edition 2024) triggers both an unsafe_op_in_unsafe_fn warning (an unsafe op inside an unsafe fn body without an inner unsafe block) and a hard E0133 error (a call to an unsafe fn from a safe context without an unsafe block):
$ cat main.rs
/// # Safety
///
/// `bytes` must be non-null and point to at least one readable byte.
pub unsafe fn first_byte(bytes: *const u8) -> u8 {
// No inner `unsafe { }`: warns under `unsafe_op_in_unsafe_fn` (edition 2024).
*bytes
}
fn main() {
let data = [42u8];
// No `unsafe { }` around the call: hard error E0133.
let value = first_byte(data.as_ptr());
println!("{value}");
}
$ cargo build
Compiling unsafe_demo v0.1.0 (/private/tmp/unsafe-demo)
warning[E0133]: dereference of raw pointer is unsafe and requires unsafe block
--> src/main.rs:6:5
|
6 | *bytes
| ^^^^^^ dereference of raw pointer
|
= note: raw pointers may be null, dangling or unaligned; they can violate aliasing rules and cause data races: all of these are undefined behavior
note: an unsafe function restricts its caller, but its body is safe by default
--> src/main.rs:4:1
|
4 | pub unsafe fn first_byte(bytes: *const u8) -> u8 {
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
= note: for more information, see <https://doc.rust-lang.org/edition-guide/rust-2024/unsafe-op-in-unsafe-fn.html>
= note: `#[warn(unsafe_op_in_unsafe_fn)]` (part of `#[warn(rust_2024_compatibility)]`) on by default
error[E0133]: call to unsafe function `first_byte` is unsafe and requires unsafe block
--> src/main.rs:12:17
|
12 | let value = first_byte(data.as_ptr());
| ^^^^^^^^^^^^^^^^^^^^^^^^^ call to unsafe function
|
= note: consult the function's documentation for information on how to avoid undefined behavior
For more information about this error, try `rustc --explain E0133`.
warning: `unsafe_demo` (bin "unsafe_demo") generated 1 warning
error: could not compile `unsafe_demo` (bin "unsafe_demo") due to 1 previous error; 1 warning emitted 
This experience is very similar to what we have planned. The key difference is that both of these cases will be errors in C# 16.
Boiling this all down, C# and Rust code bias toward simple explicit rules and arguably require less domain knowledge. A case-in-point is that it is reasonable to use grep as a safety audit tool with C# 16 and Rust since the explicit keywords act as a fixture that queries can easily grab onto.
Project-level opt-in 
The C# 16 safety model has two project-level switches. They are independent and serve different purposes.
The first switch is a new opt-in property (final name landing with the .NET 11 preview). With it off, the legacy C# 1.0 rules continue to govern; with it on, the new caller-unsafe rules apply. This switch decides what counts as unsafe and how it propagates .
The second switch is the existing <AllowUnsafeBlocks> property. It defaults to false (under all versions of C#) and gates every appearance of the unsafe keyword in the project’s source: member signatures, inner blocks, fields, and safe extern declarations under the new rules. Calling an unsafe API from another project counts, because the call site needs an inner unsafe { } block. So a project at the default cannot use any unsafe API.
The two properties combine as follows:
New property on, <AllowUnsafeBlocks> off (default). The safest configuration. The project participates in the new model and allows no unsafe code. You know your code isn’t calling Marshal.ReadByte or any other unsafe member. 
New property on, <AllowUnsafeBlocks> on. The project participates in the new model and allows unsafe code. 
New property off, <AllowUnsafeBlocks> off. The legacy model continues to apply. The project may not use pointer types. 
New property off, <AllowUnsafeBlocks> on. The legacy model continues to apply. The project may use pointer types. 
We want everyone to move to the new model. We also expect fewer projects to enable <AllowUnsafeBlocks> over time. That’s what we’re doing with our own code.
To help with the move, we plan to ship a dotnet format fixer that performs a best-effort migration on projects that haven’t yet flipped the new property on: wrapping unsafe call sites in unsafe { } blocks, moving the unsafe modifier off types onto their members, and similar mechanical rewrites. The fixer can’t infer safety obligations or write <safety> blocks; that work stays with the developer. It’s a starting point that gets the code compiling under the new rules, not a finished migration.
The core question with agents generating code is whose responsibility it is to determine whether unsafe code has been written. With the new model, that’s the compiler’s. Assuming you haven’t set AllowUnsafeBlocks=true , the compiler will refuse to compile any unsafe code at all. No code review can match the efficiency of a compile error. Memory-safety auditing collapses from inspecting every diff to checking one project property.
Cross-language comparison: defaults 
The differences are subtle and important here as well. We can frame the three languages along two safety axes: strict propagation (how aggressively unsafety propagates and what counts as unsafe) and disallowing unsafe code outright. For each axis, the safer posture is either the default or available as an opt-in.
Language 
Strict propagation 
Safe code only 
C# 
Opt-in (C# 16 model) 
Default ( AllowUnsafeBlocks=false ) 
Rust 
Default (the only model) 
Opt-in ( #![forbid(unsafe_code)] ) 
Swift 
Opt-in ( -strict-memory-safety ) 
Opt-in (no standard switch) 
C# 16 will enable the strict model with the new safety keyword. AllowUnsafeBlocks=false remains the default. Under the new model it performs even heavier lifting, because the set of unsafe actions it gates is much larger.
Rust has only one safety model, a strict one. The compiler allows unsafe in any crate by default and requires the #![forbid(unsafe_code)] lint to disable it.
Swift also offers a strict opt-in mode ( -strict-memory-safety , SE-0458 ), which can be set per file or per module to turn implicit unsafety into diagnostics.
These comparisons are not really apples to apples since they are multi-dimensional. Rust has the strongest default position. Our viewpoint aligns with the Memory Safety Continuum : stricter defaults are better. Our intention is to make the new C# safety model the new normal. We’ll start by enabling it with templates. It is simpler for us to introduce a stricter safety model given that unsafe code is already prohibited by default, and we expect good adoption because of that.
Safety documentation 
It’s easy to interpret the term “unsafe” literally, but it is misleading. It means “disable the safeties”. Safe code is known by the compiler to comply with a defined safety model, while unsafe code is not. With unsafe code, the burden of knowing falls to the developer. Knowing starts with reading dedicated safety documentation. Properly written unsafe code documents the caller’s obligations: the conditions the caller must satisfy for the code to behave correctly.
Unsafe code with missing or poorly written documentation isn’t safe to call since the caller is left guessing. Code auditors pay close attention to that. That’s already the case in the Rust community: Google and Mozilla .
An analyzer will flag missing /// <safety> blocks.
Rust safety comments 
We’ll rely on Rust for canonical examples since it is well-established. Rust uses Safety Comments to demonstrate that unsafe code is sound.
An unsafe Rust function, as_bytes_mut :
/// Converts a mutable string slice to a mutable byte slice.
///
/// # Safety
///
/// The caller must ensure that the content of the slice is valid UTF-8
/// before the borrow ends and the underlying `str` is used.
///
/// Use of a `str` whose contents are not valid UTF-8 is undefined behavior.
///
/// ...
pub unsafe fn as_bytes_mut(&mut self) -> &mut [u8] {
// SAFETY: the cast from `&str` to `&[u8]` is safe since `str`
// has the same layout as `&[u8]` (only libstd can make this guarantee).
// The pointer dereference is safe since it comes from a mutable reference which
// is guaranteed to be valid for writes.
unsafe { &mut *(self as *mut str as *mut [u8]) }
} 
Clippy enforces this convention. An unsafe function without a # Safety section trips the missing_safety_doc lint:
$ cat main.rs
#![deny(clippy::missing_safety_doc)]
pub unsafe fn first_byte(bytes: *const u8) -> u8 {
unsafe { *bytes }
}
fn main() {
let data = [42u8];
let value = unsafe { first_byte(data.as_ptr()) };
println!("{value}");
}
$ cargo clippy
Checking unsafe_demo v0.1.0 (/private/tmp/unsafe-demo)
error: unsafe function's docs are missing a `# Safety` section
--> src/main.rs:3:1
|
3 | pub unsafe fn first_byte(bytes: *const u8) -> u8 {
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
|
= help: for further information visit https://rust-lang.github.io/rust-clippy/rust-1.95.0/index.html#missing_safety_doc
note: the lint level is defined here
--> src/main.rs:1:9
|
1 | #![deny(clippy::missing_safety_doc)]
| ^^^^^^^^^^^^^^^^^^^^^^^^^^
error: could not compile `unsafe_demo` (bin "unsafe_demo") due to 1 previous error 
If you are new to Rust, yes, it has /// doc comments . It also has attributes , which are used for proposed safety tags .
The /// # Safety block above the function documents formal and contractual caller obligations. It is the caller’s responsibility to read safety comments. Neglecting to do that can result in writing incorrect unsafe code with undefined consequences. If bad things happen, blame falls to the caller. That’s why we refer to this feature as “ caller unsafe”.
The /// comments get copied directly into the public Rust docs for as_bytes_mut . The safety comments are lifted out of the code into a public portal where callers see them. That’s a strong indication of their importance and why they need to be distinct from regular comments.
The example also includes a second, more internal, kind of safety comment. The // SAFETY: notes inside the function body are for developers or auditors of the codebase; they outline safety assumptions, not caller obligations. The compiler doesn’t read, require, or honor these comments. They are a convention.
Both comment styles are important. Together they tell a two-sided story about safety, anchored to the call graph.
With the unsafe block, we’re asserting to Rust that we’ve read the function’s documentation, we understand how to use it properly, and we’ve verified that we’re fulfilling the contract of the function.
Source: Calling an Unsafe Function or Method 
This excerpt from the Rust Book makes clear that safety depends on a process that starts with compiler diagnostics but doesn’t end there. The corresponding Rust lint ( unsafe_op_in_unsafe_fn ) was allow by default in earlier editions, so missing inner unsafe blocks were silently accepted. The 2024 edition promoted it to warn-by-default, a compatibility compromise that keeps existing crates building across the edition boundary. C# 16 doesn’t carry the same legacy and makes it a compile error.
C# safety comments 
C# uses two safety comment styles, shown here in the ReadByte mockup:
/// <summary>Reads a single byte from unmanaged memory.</summary>
/// <safety>
/// The sum of <paramref name="ptr"/> and <paramref name="ofs"/> must address a byte
/// the caller is permitted to read.
/// </safety>
public static unsafe byte ReadByte(IntPtr ptr, int ofs)
{
try
{
byte* addr = (byte*)ptr;
unsafe
{
// SAFETY: relies on caller obligation.
return addr[ofs];
}
}
catch (NullReferenceException)
{
throw new AccessViolationException();
}
} 
The /// <safety> block above the signature is the formal caller contract. The // SAFETY: comment inside the body is an internal note naming what the unsafe operation relies on.
The signature alone, unsafe byte ReadByte(IntPtr, int) , tells you the shape, not the safety contract. The /// <safety> block is the contract, which is why an analyzer will flag its absence. The lesson is that knowing the shape of an unsafe API is necessary but not sufficient to write correct code. Writing unsafe code calls for safety glasses.
A single residual obligation is named: ptr + ofs must address a readable byte. The caller must discharge it. The unsafe keyword on the signature is what surfaces that obligation to callers. The // SAFETY: comment names what the dereference is relying on: that the caller has safety guards for the obligation.
Consider the states an IntPtr parameter can be in when a caller passes it:
IntPtr.Zero (null): The dereference traps on the runtime’s null-check guard pages and surfaces as a NullReferenceException , which the catch translates to AccessViolationException . Removing the catch wouldn’t change safety, only the type of exception. 
A pointer to unmapped memory (uninitialized, freed, or a garbage value): The dereference takes a hardware access violation. On most platforms this terminates the process; the catch may not even run. 
A pointer to mapped memory the caller doesn’t own (someone else’s buffer, the GC heap, a code segment): The dereference may succeed . Mapped pages can still be unreadable (guard pages, for example), in which case behavior matches the previous bullet. When it does succeed, ReadByte returns an arbitrary byte from memory with an arbitrary value. No exception, no warning. This is the textbook UB outcome; the program continues with corrupted assumptions. Worst case is that it reads memory that is interpreted as a valid value for the program. 
A pointer the caller correctly knows points to a readable byte: Works as intended. 
The try/catch handles the first state, fails ungracefully on the second, and is invisible to the third. None of that is validation. The contract travels up to the caller, where information about the buffer’s origin, length, and lifetime can be used to rule out the dangerous states. The /// <safety> block is what makes that contract visible. The caller needs to understand and protect against these cases.
Safety guards 
Documentation names the obligations. Guards discharge them. This pattern matters most at the unsafe boundary, where a developer attests that unsafe code has been brought into alignment with compiler-provided safety. The boundary is also where a review should start. With good documentation as a guide, the reviewer can tell whether the code is compliant.
One might wonder why unsafe methods don’t include enough if checks to remove the need for caller obligations. For ReadByte , no if check inside the method can validate that a caller-supplied IntPtr points to readable memory: the runtime simply doesn’t know what the caller has allocated, where, or for how long. Callers are uniquely able to determine the minimum set of checks that maintain safety while maximizing performance.
Note: there isn’t a standard name for these boundary methods/functions. Rust docs call them “safe elements”. This post calls them “unsafe boundary methods”: methods that sit at the boundary of safe and unsafe code, where unsafety is suppressed. The label unsafe is deliberate: these methods retain every dangerous capability of unsafe -decorated methods; they just don’t propagate that to their callers.
Rust safety guards 
Another Rust example, str.split_at :
pub fn split_at(&self, mid: usize) -> (&str, &str) {
// is_char_boundary checks that the index is in [0, .len()]
if self.is_char_boundary(mid) {
// SAFETY: just checked that `mid` is on a char boundary.
unsafe { (self.get_unchecked(0..mid), self.get_unchecked(mid..self.len())) }
} else {
slice_error_fail(self, 0, mid)
}
} 
Unsafe boundary functions typically have only // SAFETY: comments; they don’t impose obligations of their own. The formal /// style is reserved for unsafe methods, whose obligations the boundary then discharges. Functions that propagate must be marked unsafe .
The if self.is_char_boundary(mid) check in split_at is a guard that maintains safety for the unsafe code it calls. It ensures that the split is on a character boundary, since Unicode characters can be multi-byte. If that test fails, then the program panics via slice_error_fail . A panic will crash the program to prevent undefined behavior.
A program that panics to avoid undefined behavior is far more reliable than one that lets it happen.
C# safety guards 
The same boundary pattern from Rust applies in C#: same // SAFETY: convention, same absence of an unsafe marker on the signature.
String.CopyTo :
// Converts a substring of this string to an array of characters. Copies the
// characters of this string beginning at position sourceIndex and ending at
// sourceIndex + count - 1 to the character array buffer, beginning
// at destinationIndex.
//
public void CopyTo(int sourceIndex, char[] destination, int destinationIndex, int count)
{
ArgumentNullException.ThrowIfNull(destination);
ArgumentOutOfRangeException.ThrowIfNegative(count);
ArgumentOutOfRangeException.ThrowIfNegative(sourceIndex);
ArgumentOutOfRangeException.ThrowIfGreaterThan(count, Length - sourceIndex, nameof(sourceIndex));
ArgumentOutOfRangeException.ThrowIfGreaterThan(destinationIndex, destination.Length - count);
ArgumentOutOfRangeException.ThrowIfNegative(destinationIndex);
unsafe
{
// SAFETY: the bounds checks above ensure that `count` characters
// starting at `sourceIndex` are in range of this string, and that
// `count` characters starting at `destinationIndex` fit in `destination`.
Buffer.Memmove(
destination: ref Unsafe.Add(ref MemoryMarshal.GetArrayDataReference(destination), destinationIndex),
source: ref Unsafe.Add(ref _firstChar, sourceIndex),
elementCount: (uint)count);
}
} 
Every ThrowIf* call here is a memory-safety guard. Each one props up an invariant that the raw Buffer.Memmove call assumes:
ThrowIfNull(destination) : without it, MemoryMarshal.GetArrayDataReference(null) is UB. 
ThrowIfNegative(count) : without it, (uint)count silently wraps a negative value into a huge elementCount , and the resulting out-of-range copy is UB. 
ThrowIfNegative(sourceIndex) and ThrowIfNegative(destinationIndex) : without them, Unsafe.Add(ref …, negativeIndex) walks the ref off the front of the storage, and the resulting read or write is UB. 
The two ThrowIfGreaterThan checks layer on top of the negative checks above (and rely on the runtime invariant that Length is in [0, int.MaxValue] , so that Length - sourceIndex doesn’t overflow) to bound count against the remaining capacity of source and destination. Without them, the copy can run past the end of either buffer, and the resulting read or write is UB. 
The checks compose. Each one is only sufficient because the preceding ones have already ruled out classes of inputs. Change any link in that chain (switch to an unsigned index type, or change what the runtime guarantees about Length ), and the safety reasoning has to be re-derived.
The ThrowIf* methods are the C# analog of Rust panic helpers like slice_error_fail ; both crash the program at the boundary rather than let UB happen, and both are factored into separate functions to keep cold paths out of hot code.
Unsafe fields 
Fields deserve a discussion. A field needs to be unsafe when its declared type doesn’t express an invariant the enclosing type maintains and downstream code depends on. The unsafety lives in the gap between what the type system sees and what the enclosing type promises.
The simplest case is a field holding a native pointer. The example below is a mockup; it isn’t sourced from dotnet/runtime like the other examples.
public class NativeBuffer : IDisposable
{
/// <safety>
/// Must be null or point to a buffer of Length bytes.
/// </safety>
private unsafe byte* _ptr;
public int Length { get; }
public NativeBuffer(int length)
{
ArgumentOutOfRangeException.ThrowIfNegative(length);
unsafe
{
// SAFETY: NativeMemory.Alloc throws OutOfMemoryException on failure rather than
// returning null (unlike the malloc it wraps), so on return _ptr points to `length` bytes.
_ptr = (byte*)NativeMemory.Alloc((nuint)length);
}
Length = length;
}
public byte ReadAt(int index)
{
ArgumentOutOfRangeException.ThrowIfNegative(index);
ArgumentOutOfRangeException.ThrowIfGreaterThanOrEqual(index, Length);
unsafe
{
ObjectDisposedException.ThrowIf(_ptr is null, this);
// SAFETY: bounds checked above; null check just above; _ptr therefore points to Length bytes
return _ptr[index];
}
}
public void Dispose()
{
unsafe
{
// SAFETY: _ptr is null or was returned by NativeMemory.Alloc; Free accepts both
NativeMemory.Free(_ptr);
_ptr = null;
}
}
} 
The class is safe-callable, with the unsafe field carrying the validity invariant on behalf of the public surface. Length is a get-only auto-property fixed at construction; its immutability is the other half of the invariant, since _ptr ‘s size obligation is stated in terms of Length . If Length could change after construction, it would need its own unsafe marker and <safety> block to keep the pair coherent. Dispose deliberately weakens that invariant from “valid” to “null or valid” by writing null , which is why _ptr can’t be readonly and why ReadAt checks for null before dereferencing. The unsafe marker on the field keeps both writes (the allocation in the constructor and the invalidation in Dispose ) reviewable in one place.
A more idiomatic case in the runtime libraries is a field whose declared type is sound but less specific than what the class actually maintains. The design doc gives a simplified version of this pattern: a generic class holds an Array field that must always contain a T[] . Array is the object of array types; every T[] is an Array , so declaring the field as Array is type-correct, and doing so avoids generic specialization costs. The C# type system permits any array to be assigned to that field, while the class promises always exactly T[] . The unsafety lives in that gap: the type system can’t see the tighter invariant, and the class is responsible for upholding it.
public class ArrayWrapper<T>
{
/// <safety>
/// Must always hold a value whose runtime type is T[].
/// </safety>
private readonly unsafe Array _array;
public ArrayWrapper(T[] items)
{
ArgumentNullException.ThrowIfNull(items);
unsafe
{
// SAFETY: items is statically T[], so the field invariant holds.
_array = items;
}
}
public T GetItem(int index)
{
unsafe
{
// SAFETY: _array is always a T[] per the field's <safety> block
var typedArray = Unsafe.As<T[]>(_array);
return typedArray[index];
}
}
} 
The pattern is the same as NativeBuffer : an unsafe field with a documented invariant, unsafe blocks at the boundary discharging it, and a safe-callable public surface.
Rust is working through the same problem, and the unsafe-fields proposal uses Vec<T> as its motivating case. Vec<T> carries an invariant that the elements at data[i] for i < len are initialized. Today, that invariant lives only in comments and prose. There is nothing stopping a method (even a private one) from desynchronizing len and data in entirely safe code:
pub struct Vec<T> {
data: Box<[MaybeUninit<T>]>,
len: usize,
}
impl<T> Vec<T> {
// Safe code, but the next read is undefined behavior.
pub fn evil(&mut self) {
self.len += 2;
}
} 
The proposed future shape moves the invariant into the type system by marking both fields unsafe :
struct Vec<T> {
// SAFETY: The elements `data[i]` for
// `i < len` are in a valid state.
unsafe data: Box<[MaybeUninit<T>]>,
unsafe len: usize,
} 
With that change, any write to len or data has to happen inside an unsafe block; evil no longer compiles as written. The two fields are reviewed together, in the same place, against the same contract. That’s the same benefit NativeBuffer gets from pairing unsafe byte* _ptr with a fixed Length , and that ArrayWrapper<T> gets from pairing readonly unsafe Array _array with the always- T[] promise.
You might say that “you can still write evil with unsafe and it still results in UB”. Yes. The entire proposition is that unsafe code is marked and easy to audit. That’s the basis of safety in all of these languages.
A few rules of thumb for unsafe on fields:
Writes are the primary motivation. unsafe on the field forces every write into a reviewable context where the contract is in view, establishing (at least) the member-to-member discipline that keeps the invariant intact. For example, a write to _ptr in the NativeBuffer example would violate Length . 
Readonly fields satisfy much of the same need. It helps to think of unsafe readonly as the contract plus a built-in guard: unsafe names the invariant, and readonly is the safety guard that prevents post-construction writes from violating it. Drop the readonly and the contract remains; it just has to be discharged the harder way, by reviewing every write site. The ArrayWrapper<T> example above is readonly unsafe for exactly this reason. Rust is converging on the same shape via the unsafe-fields design axioms : the marker stays, but the operations it gates (writes, reinitialization) are exactly the ones immutability already prevents. 
Private isn’t a free pass. It’s tempting to assume that because a field is private, the type’s own methods can be trusted to maintain the invariant. That was the old unsafe type model. In the new model, member-to-member interaction is itself a contract surface; one method’s correct write can be undone by another method’s uncoordinated write. Unsafety is about protecting the contract from any code that might violate it, including code within the type itself. 
A migration walkthrough 
The best way to understand the model is to migrate some existing code to it. This is what the .NET team is doing across the runtime libraries. Pick an unsafe API, follow it to a caller, and decide whether the migration can discharge the callee’s obligations inline or has to propagate them upward. Each caller is a candidate place for the boundary; the migration answers whether that’s where the boundary belongs.
This section is speculative. The model isn’t finalized and the runtime libraries haven’t been migrated yet. The examples are informed guesses, intended to convey where we’re headed and what the new model implies for existing code.
We’re going to migrate some methods in this section that bottom out in NativeMemory.Alloc and NativeMemory.Free . Here’s how the two NativeMemory methods look under the new 
