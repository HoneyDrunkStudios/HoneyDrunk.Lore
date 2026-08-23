---
source: "https://thegustafson.com/blog/paged-attention"
title: "PagedAttention: Virtual Memory for the KV Cache (15 minute read)"
author: "unknown"
date_published: "2026-08-21"
date_clipped: "2026-08-23"
category: "AI / LLM Research & Tooling"
source_type: "rss"
discovered_via: "https://tldr.tech/ai/2026-08-21"
source_role: "primary-via-tldr"
---

# PagedAttention: Virtual Memory for the KV Cache (15 minute read)

Source: https://thegustafson.com/blog/paged-attention

Arc 6 : Inference Engines & Serving Systems PagedAttention: Virtual Memory for the KV Cache 15 min read builds on The KV Cache from First Principles A note on this series
I built this series as a learning project and used Claude extensively for research, drafting, critique, coding, and revision. I chose the curriculum and dependency order, drove the questions, edited the explanations, developed the interactive examples, and take responsibility for the published result.
This is an educational first edition rather than a formal reference. I am reviewing the articles against primary sources, testing the executable examples, and tracking corrections as the series matures. Every single line of example code has been run and tested for correctness on my machine.
CONTIGUOUS reserve max_context per request PAGED fixed-size blocks, scattered, allocated on demand R 1 25 / 64 R 2 47 / 64 R 3 12 / 64 pool WASTED MEMORY 56 % 192 slots reserved same three requests, two memory layouts
Here's a thing I think about a lot: very occasionally, an idea from one subfield of computer science walks across the room, taps another subfield on the shoulder, and changes everything. PagedAttention is one of those moments. The idea is just virtual memory, the thing operating systems have been doing since the 1960s, transplanted onto the KV cache of a language model. That's it. That single observation is why a modern inference engine can serve two to four times more users per GPU than the naive approach.
This post is about that crossover. I want to build the intuition for why the KV cache wastes so much memory by default, why virtual memory is exactly the right analogy, and how PagedAttention implements the idea in a way that attention kernels can still work with.
A quick refresher before we go further, in case you didn't just come from the KV cache post : the KV cache is the per-request store of attention keys and values. It lets the model avoid recomputing them at every decoding step. It grows linearly with sequence length and at long contexts it eats more GPU memory than the model weights themselves. So it's the scarce resource. Every serving-system innovation in this arc is, in one way or another, about managing this one resource better.
Fragmented memory, wasted GPU
When you serve an LLM, you don't know in advance how long each request will be. User A might generate 25 tokens. User B might keep going for 2,000. Your service promises to support, say, 2,048 tokens per request, and you have no idea which user will use all of it. So a naive serving system does the obvious thing: reserve max_context slots of KV cache for each active request. If the model is 70B and the context is 32k tokens, that's gigabytes of GPU memory per request, reserved up front, most of it unused.
Two things go wrong here, and they compound.
The first is internal fragmentation . A request that only generates 47 tokens still holds onto 2,048 slots of cache. 2,001 slots sit empty the entire time. Multiply by 30 concurrent requests and you've reserved 60k token slots for what, in aggregate, is maybe 1–2k filled. That's unused memory you can't hand to another request, because it's already spoken for.
The second is external fragmentation . Requests show up and leave at different times. When request A finishes, its contiguous 2,048-slot chunk becomes available. But if you have a new request that also wants 2,048 slots, and the only free regions are a 1,500-slot hole from A and an 800-slot hole from someone else, you can't use them together. The free memory is the right size in total but the wrong shape. Either you defragment (copy stuff around, which is expensive and disruptive) or you sit on unusable memory.
Memory Use: Contiguous vs Paged max_context = 2048 , block = 16 tokens CONTIGUOUS reserve max_context per request PAGED allocate blocks on demand R A 25 used R A wasted: 2023 slots 2048 R B 47 used R B wasted: 2001 slots 2048 R C 12 used R C wasted: 2036 slots 2048 TOTAL SLOTS RESERVED 6,144 ( 84 actually in use, 6060 wasted) PAGED / CONTIGUOUS 96 / 6,144 64.0 × less Three requests, lengths 25, 47, and 12 tokens, at a 2,048-token context budget. Contiguous allocation reserves 6,144 slots for 84 real tokens. Paged allocation rounds up to block boundaries and uses 96. That's a 64× difference for this toy, and it's not atypical.
Kwon et al.'s original vLLM paper puts real numbers on the waste. On production workloads they measured KV-cache utilization around 20–40%, which means 60–80% of the most expensive memory on the most expensive GPU in the cluster was sitting there doing nothing. That's the problem PagedAttention set out to fix.
This is just virtual memory
The moment the vLLM paper clicked for me was when I realized the problem it's solving is exactly the same problem operating systems solved decades ago.
In the early days of multiprogramming, every process asked for a contiguous chunk of RAM. The OS had to decide where to put it. Processes of different sizes came and went. Over time the free memory turned into a jigsaw of unusable fragments. Programs couldn't fit even when there was plenty of free RAM in total. The solution, pioneered on the Atlas at Manchester and refined by the 1970s, was virtual memory .
Here's how virtual memory works, boiled down: each process sees a contiguous virtual address space, but the operating system chops it into fixed-size pages (typically 4 KB) and stores them wherever it likes in physical memory. A per-process page table maps virtual page numbers to physical frame numbers. When the process reads virtual address 0x1000 , the CPU (with help from the MMU) looks up the translation in the page table and fetches the data from whatever scattered physical frame is actually holding it. The process never knows the pages aren't contiguous. The OS gets to pack physical memory however it likes.
Now read that paragraph again and replace "process" with "request", "page" with "KV block", "physical frame" with "physical block in the GPU KV-cache pool", and "page table" with "block table". That's PagedAttention. The whole thing is a one-to-one correspondence.
OS virtual memory → PagedAttention
------------------------------ -----------------------------
process → request (one prompt + generation)
page (4 KB) → KV block (e.g. 16 tokens)
page table → block table (logical → physical block idx)
physical frame → physical KV block in the shared pool
page fault / alloc → allocate a new block on demand
copy-on-write → copy-on-write for shared prefixes
I think this is the most useful mental model for the entire post. If you remember "it's virtual memory for the KV cache", you can reconstruct most of the mechanics on a napkin.
PagedAttention in one picture
Here's the machinery. The KV cache is no longer one big contiguous array per request. Instead:
GPU memory holds a shared pool of fixed-size physical blocks . A typical block is 16 tokens. Each block can hold the K and V vectors for 16 consecutive positions of one request. Blocks are allocated from the pool as requests need them and freed back to the pool when they're done.
Each request has a logical sequence of blocks: L0, L1, L2, ... arranged in order. The first 16 tokens go in L0, the next 16 in L1, and so on.
Each request has a small block table that maps logical block index → physical block index. table[0] = 7 means "logical block 0 of this request lives at physical block 7 in the pool".
Block Table Indirection block = 16 tokens REQUEST + BLOCK TABLE PHYSICAL BLOCK POOL Request A 25 tokens L 0 → P 3 L 1 → P 7 Request B 47 tokens L 0 → P 0 L 1 → P 5 L 2 → P 9 Request C 12 tokens L 0 → P 4 P 0 req B P 1 free P 2 free P 3 req A P 4 req C P 5 req B P 6 free P 7 req A P 8 free P 9 req B P 10 free P 11 free Request A : 25 tokens → 2 blocks, mapped to P3, P7 Three requests mapped into a shared physical block pool. Each request's block table is tiny (a handful of integers), and the physical blocks it points at are scattered through the pool. Unrelated requests share scattered physical memory, just like unrelated processes share scattered RAM.
When attention runs, the kernel doesn't assume keys and values are contiguous. It walks the block table: "logical block 0 is physical block 7, logical block 1 is physical block 3, ..." and gathers the K and V vectors from wherever they actually live. There's a little indirection cost per block, but because blocks are substantial (16 tokens × hidden dimension), the fixed cost of the lookup is amortized across many arithmetic operations. The overhead ends up in the single-digit percent range.
The payoff is that you only ever allocate what you use , rounded up to block size. A request of 47 tokens takes three blocks (48 slots). Waste per request is bounded by BLOCK_SIZE - 1 tokens, so total waste across the system is small and constant instead of growing with max_context . Kwon et al. measured the resulting cache utilization at ~96% on production-like workloads, up from 20–40%.
A small worked example
Let me make this concrete with the three requests from the comparison above.
Say we have a pool of 64 physical blocks, each holding 16 tokens of KV cache. Three requests arrive:
Request A : 25 tokens. Needs ceil(25 / 16) = 2 blocks. The scheduler hands it blocks P3 and P7. Block table for A: [3, 7] . First 16 tokens live in P3, next 9 in P7 (with 7 token slots of padding in P7).
Request B : 47 tokens. Needs 3 blocks. Gets P0, P5, P9. Block table: [0, 5, 9] . 47 = 16 + 16 + 15, so 1 slot of padding in P9.
Request C : 12 tokens. Needs 1 block. Gets P4. Block table: [4] . 4 slots of padding.
Total physical slots used: 2×16 + 3×16 + 1×16 = 96 slots, to hold 84 generated tokens. Waste: 12 slots, about 12%. Compare to the contiguous case at max_context = 2,048 : 3 × 2,048 = 6,144 slots reserved, only 84 in use, 98.6% waste.
With the paged approach, the pool has 64 − 6 = 58 blocks still free. We can admit another 30+ requests of average length without thinking twice. In the contiguous approach we couldn't admit a single additional request at max_context = 2,048 unless we had another 2,048 slots free. Paged allocation doesn't make memory bigger. It just stops pretending every request needs the worst case.
Now say request B generates another 20 tokens and crosses into a 4th block. The scheduler allocates one more block from the pool (say P11), appends it to B's block table, and attention on the next step uses [0, 5, 9, 11] . That's a single table write, no copying and no defragmentation.
KV Cache Growth model 7B 70B K cache V cache The cat sat prefill memory 10.0 GB at 32k context per request d_head= 128 d_head= 128 Tokens 3 / 8 KV heads / layer 8 Layers 80 Grouped-Query 8 KV heads for 64 Q heads 2 (K+V) × 80 layers × 8 kv_heads × 128 d_head × seq_len × 2 bytes Reset Step heads MHA ( 64 ) GQA ( 8 ) MQA ( 1 ) As a quick refresher: this is the KV cache growing one row per decode step. PagedAttention doesn't change what goes in the cache, only how it's laid out in memory. Each 16-token chunk becomes one physical block in the pool.
Copy-on-write: when two requests share a prefix
Here is where the analogy pays off twice. Operating systems have a lovely trick called copy-on-write (COW): when a process forks, instead of duplicating its entire memory, the kernel shares the parent's pages with the child and marks them read-only. The child only gets its own copy of a page the instant it writes to one. Memory stays shared as long as nobody actually modifies it, which is most of the time.
This trick transfers directly. In LLM serving, many requests share a prefix. A chat app might prepend the same 800-token system prompt to every user message. Parallel sampling (the same prompt, multiple sampled continuations) shares every token up to the first sample token. Beam search is the same, at a finer grain: beams share everything except their most recent divergent token. If every one of those shared prefixes gets its own copy of the KV cache, you're paying for the same work many times over.
With PagedAttention, the scheduler can point multiple block tables at the same physical block . Each physical block maintains a reference count. As long as the count is greater than 1, nobody is allowed to write into the block in place. The moment one request needs to write (say, because it's about to generate a new token in a block still shared with another request), the engine clones that one block, decrements the refcount on the original, and updates the writing request's table to point at the clone. Everybody else keeps pointing at the original.
Copy-On-Write for Shared Prefix A and B share a system-prompt prefix REQUEST A (user 1, no new write) REQUEST B (user 2, writes a new token) block table A block table B L 0 → P 0 L 1 → P 1 L 0 → P0 L 1 → P1 PHYSICAL BLOCK POOL P0 "You are a helpful..." refcount = 2 SHARED P1 "...assistant. User:" refcount = 2 SHARED P2 "...cloned, then new" refcount = 0 B only (clone) The intuition: shared prefixes stay shared until someone writes. A and B both point at P0 and P1 for the system prompt; when B generates a new token, only the one block being written gets cloned (P1 → P2). A's view never moves. Copy a page, not the whole cache.
The practical implication is that as long as your shared prefix is actually shared (nobody writes into it), you pay for it exactly once across all the requests that use it. This is the mechanism behind prefix caching as well. Kwon et al. demonstrate COW unlocking beam search and parallel sampling, but the much bigger win in production turns out to be system prompts. If your chatbot has a 2k-token system prompt and you're serving a hundred concurrent users, PagedAttention + COW saves you roughly 200k tokens of cache versus the naive approach. On a 70B model in fp16, that's tens of gigabytes.
Note that COW is a refinement of the basic paging idea. You can get most of PagedAttention's win without it. COW is what turns the "already good" into "extremely good" for workloads with heavy prompt reuse. SGLang's RadixAttention generalizes this further by organizing all cached blocks into a radix tree indexed by token prefix, so arbitrary shared prefixes get found and reused even when they aren't explicitly declared.
Why the attention kernel works at all
One thing that bothered me when I first read the paper was: attention is a dense matrix operation. How can it possibly work on non-contiguous memory without falling apart?
The answer is that attention, at the kernel level, is already a loop that walks over keys and values one chunk at a time. FlashAttention, for example, tiles the K and V matrices into blocks that fit in SRAM and processes them iteratively. PagedAttention aligns its block size with the tile size the kernel uses anyway. Inside each block, memory is contiguous. Across blocks, you just look up the next physical block address from the block table and continue. The kernel does a little more pointer arithmetic. It doesn't rewrite attention from scratch.
The indirection does have a cost. For small block sizes, the overhead of block-table lookups gets proportionally larger, and memory accesses get more random. For huge block sizes, internal fragmentation creeps back in. The sweet spot in practice is around 16 tokens per block for most modern GPUs and models, which is what vLLM, TGI, and TensorRT-LLM all converged on.
Block Size Tradeoff 47 tokens, three block sizes BLOCKS ALLOCATED STATS block = 4 12 blocks 12 lookups 1 wasted ( 2 %) 48 slots total block = 16 3 blocks 3 lookups 1 wasted ( 2 %) 48 slots total block = 64 1 blocks 1 lookups 17 wasted ( 27 %) 64 slots total Smaller blocks → more lookups, less waste   |   Larger blocks → fewer lookups, more waste The same 47-token request at three block sizes. Block = 4 needs 12 lookups but wastes only 1 slot. Block = 64 needs 1 lookup but wastes 17 slots (26%). Block = 16 sits in the middle: 3 lookups, 1 wasted slot. That's the sweet spot the ecosystem converged on.
A sketch of the scheduler
To get a feel for how this plays out in code, here's a stripped-down sketch of what a paged-KV scheduler looks like. Not runnable as a real engine, but structurally honest.
Paged KV scheduler (sketch) − collapse # --- Paged KV cache scheduler, simplified ---
BLOCK_SIZE = 16 # tokens per physical block (vLLM's default)
class BlockPool :
def __init__ (self, num_blocks: int ):
self .free = list ( range (num_blocks)) # physical block ids
self .refcount = [ 0 ] * num_blocks # for copy-on-write
def alloc (self) -> int :
if not self .free:
raise MemoryError ( "out of KV blocks" )
pid = self .free.pop()
self .refcount[pid] = 1
return pid
def incref (self, pid: int ):
self .refcount[pid] += 1 # COW: share instead of copy
def free_block (self, pid: int ):
self .refcount[pid] -= 1
if self .refcount[pid] == 0 :
self .free.append(pid)
class Request :
def __init__ (self, req_id, prompt_tokens):
self .id = req_id
self .tokens = list (prompt_tokens)
self .block_table = [] # logical idx -> physical block id
def need_new_block (self) -> bool :
# allocate a new block when crossing a block boundary
return len ( self .tokens) % BLOCK_SIZE == 0
def append_token (self, tok, pool: BlockPool):
if self .need_new_block() or not self .block_table:
self .block_table.append(pool.alloc())
self .tokens.append(tok)
# (attention kernel reads K/V via self.block_table when it runs)
# --- Example: three requests, shared pool ---
pool = BlockPool( num_blocks = 64 )
A = Request( "A" , prompt_tokens = [ 0 ] * 25 )
B = Request( "B" , prompt_tokens = [ 0 ] * 47 )
# Prefill: allocate blocks for the prompts
for r in (A, B):
for _ in range ( 0 , len (r.tokens), BLOCK_SIZE ):
r.block_table.append(pool.alloc())
print ( "A table:" , A.block_table) # e.g. [63, 62]
print ( "B table:" , B.block_table) # e.g. [61, 60, 59]
print ( "free pool:" , len (pool.free), "/" , 64 )
The real vLLM scheduler is more involved (paging policies, eviction, preemption, GPU kernel integration), but this captures the bones. A block table is just a list of integers. Allocation is just popping from a free list. COW is a refcount. The only fancy part lives inside the attention kernel, and even there the change is local.
Misconceptions
"PagedAttention changes the model output." No. It doesn't touch the math at all. Attention produces the exact same logits regardless of whether the K and V tensors are laid out contiguously or scattered through a pool. The only change is in how the kernel fetches memory. Output tokens, sampling probabilities, everything is bit-for-bit identical (modulo the usual floating-point non-determinism that affects any reduction on a GPU).
"Smaller blocks are always better because they reduce waste." It's more of a tradeoff. Smaller blocks reduce internal fragmentation (less padding in the last block per request) but inflate the block-table size and add per-block overhead inside the attention kernel. They also spread memory accesses more randomly, which can hurt cache performance. Kwon et al. found 16 tokens to be a strong default for a wide range of models, and that's where the major engines settled. Some workloads with mostly short sequences can benefit from smaller blocks; some with uniformly long sequences prefer 32 or 64. The number isn't magic, just well-tuned.
"Copy-on-write is mostly a beam-search optimization." The paper emphasizes beam search, but in production the dominant source of shared prefixes is system prompts . One prompt, many users, many concurrent requests all starting with the same 500–2000 tokens. COW there means the cached prefix lives exactly once in GPU memory across all of them. That's where most of the savings come from in a serving workload.
What's next
The next post zooms out from one allocation strategy to the full GPU memory budget (weights, KV cache, activations, CUDA overhead) and the formula for how many concurrent requests you can actually serve. Start with Memory Management for LLMs .
Additional reading (and watching)
Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu, C. H., Gonzalez, J. E., Zhang, H., & Stoica, I. (2023). Efficient Memory Management for Large Language Model Serving with PagedAttention . SOSP 2023 . The paper that introduced PagedAttention. The numbers I cite for 20–40% vs 96% cache utilization, 16-token blocks, and 2–4× throughput come from here.
Kilburn, T., Edwards, D. B. G., Lanigan, M. J., & Sumner, F. H. (1962). One-Level Storage System . IRE Transactions on Electronic Computers . The Atlas paper. First description of paged virtual memory, cited as the ancestor PagedAttention is borrowing from.
Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts , 10th ed. , Chapter 10: Virtual Memory. The standard textbook treatment of paging, page tables, TLBs, and copy-on-write. If you want the OS-side intuition in full, this is where it lives.
Zheng, L., et al. (2023). SGLang: Efficient Execution of Structured Language Model Programs . arXiv:2312.07104. Introduces RadixAttention, which generalizes PagedAttention's copy-on-write prefix sharing into a radix tree of cached blocks.
Dao, T., Fu, D. Y., Ermon, S., Rudra, A., & Ré, C. (2022). FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness . NeurIPS 2022 . Background on the block-tiled attention kernel that PagedAttention extends with indirect addressing.
vLLM Project. (2023–2026). vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention (blog announcement) and vLLM documentation . Reference for block size defaults, automatic prefix caching, and production deployment guidance.
Hugging Face. (2024). Text Generation Inference (TGI) — PagedAttention adoption . TGI's documentation covering its paged KV-cache implementation and the performance improvements over its earlier contiguous cache.
Yu, G.-I., Jeong, J. S., Kim, G.-W., Kim, S., & Chun, B.-G. (2022). Orca: A Distributed Serving System for Transformer-Based Generative Models . OSDI 2022 . The precursor work on iteration-level scheduling that set the stage for vLLM's scheduler design.
Pope, R., Douglas, S., Chowdhery, A., Devlin, J., Bradbury, J., Levskaya, A., Heek, J., Xiao, K., Agrawal, S., & Dean, J. (2022). Efficiently Scaling Transformer Inference . arXiv:2211.05102. Background on KV-cache memory dominating long-context inference — the reason managing it well matters so much.
Denning, P. J. (1970). Virtual Memory . ACM Computing Surveys . The classic survey article that established the vocabulary PagedAttention borrows (pages, page tables, working sets, thrashing). Useful when you want to pull on the OS thread a bit further.
Back to Arc 06 : Inference Engines & Serving Systems ← Previous Kernel Fusion and the Memory Wall Next → Memory Management: Fitting a Model and Deciding Concurrency
