---
source: "https://trustsig.eu/blog/wasm2c-tableflip-unchecked-calloc"
title: "Table flip: a wasm2c guest runs a shell command on the host, through one unchecked calloc"
author: "TrustSig; Robert Vähhi"
date_published: "2026-08-19"
date_clipped: "2026-08-24"
category: "Security & Ethical Hacking"
source_type: "rss"
---

# Table flip: a wasm2c guest runs a shell command on the host, through one unchecked calloc

Source: https://trustsig.eu/blog/wasm2c-tableflip-unchecked-calloc

# Table flip: a wasm2c guest runs a shell command on the host, through one unchecked calloc

wasm2c sets a table's size from the element count the guest declared, then ignores whether the allocation succeeded. Make it fail and every table index becomes an absolute address on the host.

wasm2c compiles a WebAssembly module to C. The point of it is that you can take a

`.wasm`

file you do not trust, turn it into source, build it into your own program, and rely on the generated bounds checks to keep the guest inside its own memory. Firefox ships libraries this way. So does a long tail of software that wanted a sandbox without shipping a JIT.We ran a sandboxed module through the toolchain under an address space limit, which is the kind of limit you set when you run other people's code, and the guest wrote a file on the host.

The whole thing is one allocation whose return value nobody reads.

## Three lines that trust the allocator

This is the table allocator, from

`wasm2c/wasm-rt-impl-tableops.inc`

. The file is a template included three times, so this code exists once for `funcref`

tables, once for `externref`

, once for `exnref`

.```
void WASM_RT_TABLE_APINAME(wasm_rt_allocate)(WASM_RT_TABLE_TYPE* table,
uint32_t elements,
uint32_t max_elements) {
table->size = elements;
table->max_size = max_elements;
table->data = calloc(table->size, sizeof(WASM_RT_TABLE_ELEMENT_TYPE));
}
```

`elements`

is the element count from the module's table declaration. The guest wrote it. It goes into `table->size`

on the first line, before anything has been allocated, and the `calloc`

on the third line is never asked whether it worked.When that

`calloc`

returns NULL, the runtime does not notice. Instantiation continues, `table->data`

is NULL, and `table->size`

is still the number the guest declared.Bytes of allocation-failure handling in the table allocator

0

The return value of calloc is stored and never compared. There is no failure path to take.

The same runtime does handle this elsewhere. The linear memory allocator on current

`main`

reads like this:```
memory->data = (MEMORY_CELL_TYPE)calloc(byte_length, 1);
if (byte_length != 0 && !memory->data) {
abort();
}
```

That check landed on 2026-07-03, in a commit titled "wasm2c: guard wasm_rt_allocate_memory size overflow and alloc failure". The table allocator sat two files away and was not part of it. The unchecked

`calloc`

there dates back to `ab9e0b55`

in March 2018, when `wasm-rt-impl.c`

was first split out, and it is unchanged in released 1.0.41 and in `main`

as of writing.## A NULL table is an addressing primitive

Every table access wasm2c emits is bounds checked against

`table->size`

, and that check is correct. It is also now checking the wrong thing, because `size`

describes a table that was never allocated.The arithmetic is the entire bug. With

`data`

at NULL, `table.data[x]`

is `x * sizeof(wasm_rt_funcref_t)`

, and that struct is four pointers, so 32 bytes. A table index is an absolute address divided by 32, and the guest names it directly as an `i32.const`

.A table is meant to be a fenced field with a gate that counts. The gate here is still counting correctly, against a fence that was never built. Slot 4 does not mean "the fifth thing in my table" any more. It means "byte 128 of the host process", and the gate waves it through because 4 really is less than the declared size.

Two properties make this better than a generic out of bounds write. Table entries are 32 bytes of four separate pointer fields, so one

`table.get`

reads four consecutive host words at once, and `table.set`

writes four. And the range is not small: two billion elements at 32 bytes each covers the first 64 GiB of the address space, which contains everything a non-relocatable binary maps.## The guest decides whether the allocation fails

An unchecked allocation is only a bug if the allocation can fail, and here the size of it is guest input.

The module declares

`(table $t 2147483648 funcref)`

. Two billion entries at 32 bytes is a 64 GiB `calloc`

. On a stock 64-bit Linux box with the default heuristic, that request succeeds, the pages are never faulted in because nothing touches them, and the bug stays invisible. That is why it survived eight years of testing.It fails, and returns NULL rather than aborting, in exactly the situations where you would be running untrusted code in the first place:

### An address space limit

`ulimit -v`

, `RLIMIT_AS`

, or the container equivalent. This is the standard way to stop a hostile guest from exhausting the host, and it converts an oversized request into a NULL return.### Strict overcommit

`vm.overcommit_memory=2`

, where the kernel refuses requests it cannot back rather than gambling on them.### A 32-bit host

The request cannot be satisfied at any setting, so the failure is unconditional.

### Memory pressure

No configuration required, just a host busy enough that a large request loses.

The uncomfortable shape of this: hardening the host is what arms the bug. A deployment that sets no limits at all is the one where the sandbox holds.

## From a broken table to system()

Absolute addressing at 32-byte granularity is not yet code execution. Four steps close that, and none of them need a second bug.

### Leak libc through the embedder's GOT

The guest runs

`table.get`

at `got_slot / 32`

and `table.set`

at `globals_addr / 32`

. The read pulls 32 bytes of the embedder's out of host memory as if it were a table entry, and the write drops those same 32 bytes into the module's own globals, which the guest can then read as ordinary `i64`

values. One of those words is libc's `malloc`

, resolved by the loader at startup. `system`

follows from a fixed distance in the same libc, computed at build time. Address randomisation is on throughout and does not matter, because the address is read rather than guessed.### Forge a table entry in four globals

`wasm_rt_funcref_t`

is `{func_type, func, func_tailcallee, module_instance}`

. The guest writes those four fields as four consecutive `i64`

globals: `func`

gets the leaked `system`

address, `module_instance`

gets a pointer to a command string, also assembled in globals, and `func_type`

points at a copy of the call site's type hash.### Walk through the type check

The check

`call_indirect`

performs is this:```
static inline bool func_types_eq(const wasm_rt_func_type_t a,
const wasm_rt_func_type_t b) {
return (a == b) || LIKELY(a && b && !memcmp(a, b, 32));
}
#define CHECK_CALL_INDIRECT(table, ft, x) \
(LIKELY((x) < table.size && table.data[x].func && \
func_types_eq(ft, table.data[x].func_type)) || \
TRAP(CALL_INDIRECT))
```

A type is a pointer to 32 bytes, compared with

`memcmp`

. The guest holds 32 bytes of the right value in its own globals and points `func_type`

at them, so the comparison succeeds on bytes the guest wrote. The index check and the null check pass for the same reason they always do.### Call it

`DO_CALL_INDIRECT`

expands to `((t)table.data[x].func)(...)`

with the entry's `module_instance`

as the first argument, because that is how wasm2c closes a function over its instance. With `func`

set to `system`

and `module_instance`

set to a string, one `call_indirect`

at `globals_addr / 32`

is `system("echo goodbye sandbox > /tmp/pwned.txt")`

.The guest returns 0 and the embedder prints that the module ran fine. The file is on the host.

Additional bugs required

None

One unchecked allocation supplies the read, the write, the leak and the call.

## What the exploit assumes, and what it does not

Being precise about the boundary matters more here than the result does.

The defect is platform independent. Any host where a large

`calloc`

returns NULL instead of succeeding gets a table whose bounds check has stopped meaning anything, on any operating system and any architecture.This particular chain is Linux specific, and it assumes a non-relocatable embedder. Exactly one layout fact is baked into the module: the address of the module instance, which is a global and therefore fixed in a non-PIE build. Everything else is read at runtime. The proof of concept resolves the instance address, the GOT slot and the libc offset out of the binary it just built and out of that machine's libc with

`nm`

and `readelf`

, so it works unmodified on `linux/arm64`

and `linux/amd64`

.macOS is not a target for the exploit and is a useful illustration of the difference. Darwin does not enforce

`RLIMIT_AS`

, so the oversized `calloc`

succeeds and the failure path is never reached, arm64 builds are always position independent, and Mach-O has no ELF GOT to read. The bug is still there. This route to it is not.Embedder code required to be vulnerable

A plain instantiate

The proof of concept's host program is instantiate, call the exported function, free. No exploit support code.

## The fix is the check that already exists

Mirror the memory allocator. Compare the result of

`calloc`

, and if it is NULL with a non-zero element count, abort instead of continuing with a table that claims to exist.There is a second, cheaper mitigation available at the same place: a guest-declared element count is attacker input and can be bounded before it reaches the allocator, rather than being multiplied by 32 and handed to libc. Both together give you a runtime where the declared size and the allocated size cannot disagree.

We reported this upstream. No fix has landed at the time of writing, and the proof of concept is public because the failing code is one function long and any reader of the file can see it.

The repository is trustsig-eu/wasm2c-tableflip. It builds wabt at tag 1.0.41 from source in Docker, generates the guest module, compiles a plain embedder around it, and runs it:

```
git clone https://github.com/trustsig-eu/wasm2c-tableflip.git
cd wasm2c-tableflip
docker build -t wabt-w2c-poc .
docker run --rm wabt-w2c-poc
```

```
running guest
guest returned 0
--- file on host ---
goodbye sandbox
```

`--build-arg WABT_REF=main`

runs it against the current tree instead.## Why we were reading a wasm runtime

We compile parts of our detection client to WebAssembly and spend a lot of time on the other side of that, taking wasm payloads apart in TrustSig Lab. wabt is the toolchain on both ends of that work, so its runtime gets read the way you read anything you have made load bearing.

The pattern worth carrying out of this is not about wasm. A size field and the allocation that backs it are one fact stored twice, and a failure that updates only one of them leaves every check downstream reasoning about a shape that was never built. Bounds checks do not fail loudly when this happens. They keep passing, politely, on a fence that is not there.

*TrustSig is an invisible bot-detection and device-identity platform built in the EU. If you run wasm2c output in production, or you have found something adjacent to this and want to compare notes, get in touch.*
