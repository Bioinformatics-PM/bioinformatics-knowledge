---
aliases:
  - Memory Complexity
  - Auxiliary Space
  - Memory Footprint
  - Complexité en espace
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Big O Notation]]"
  - "[[Model of Computation]]"
  - "[[Integer Representation]]"
  - "[[Genome]]"
related:
  - "[[Memory Hierarchy]]"
  - "[[Virtual Memory]]"
  - "[[Python Object Model]]"
  - "[[External Memory Algorithm]]"
  - "[[K-mer]]"
  - "[[Suffix Array]]"
  - "[[FM-Index]]"
  - "[[Succinct Data Structure]]"
projects:
  - "[[01-dna-engine]]"
  - "[[04-alignment-engine]]"
  - "[[05-sequence-search]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[An Introduction to Bioinformatics Algorithms (Jones)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Langmead 2009 - Ultrafast and Memory-Efficient Alignment of Short DNA Sequences to the Human Genome]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
  - "[[Fernández 2024 - A 160 Gbp Fork Fern Genome Shatters Size Record for Eukaryotes]]"
---

# Space Complexity

> [!abstract]
> Space complexity measures how much memory an algorithm needs as a function of the input size; at genome scale it decides, before any timing, whether an analysis can run at all, because a structure that does not fit in RAM turns cheap random accesses into slow transfers from disk.

## Definition

The **space** an algorithm uses on an input is the largest number of memory words it occupies at any moment of the run; its **space complexity** $S(n)$ is the maximum over inputs of size $n$, stated with [[Big O Notation]] like running time. **Auxiliary space** leaves out the input (and usually the output). An algorithm works **in place** when it rearranges its input with at most a constant number of elements stored outside it, as insertion sort does.[^clrs2] In practice memory is counted in bytes: a 64-bit word of the [[Model of Computation]] is 8 bytes.

## Why it matters

- **Scale in bytes.** The 3.055 Gb human genome[^nurk] takes about 3.1 GB as text and 0.76 GB packed at 2 bits per base ([[Genome]]); the 160.45 Gb genome of the fork fern *Tmesipteris oblanceolata*[^fernandez] still needs 40 GB packed.
- **Indexes must stay in RAM.** A read mapper places each read with a few random accesses into an index of the reference ([[Read Mapping]]). Bowtie stores the human genome as a Burrows-Wheeler index with a memory footprint of about 1.3 GB,[^langmead] against 12 GB or more for a plain [[Suffix Array]] (Worked example).
- **Streams of reads.** A 30x human sequencing run yields about $6 \times 10^8$ reads of 150 bp (Deeper); a generator processes them in memory proportional to one record, not to the file ([[Iterator]], [[FASTA Format]]).
- **Alignment matrices.** Dynamic programming over sequences of lengths $n$ and $m$ fills $\Theta(nm)$ cells; two rows suffice for the score, and a divide-and-conquer variant recovers the alignment itself in linear space[^jones] ([[Hirschberg Algorithm]], [[04-alignment-engine]]).

## Core (L1)

### Space is bounded by time

In the word-RAM each step writes $O(1)$ words, so an algorithm cannot occupy more memory than its input plus a constant times its running time: $S(n) \le n + c\,T(n)$. The converse fails: GC content takes $\Theta(n)$ time and $O(1)$ auxiliary space (one counter).

### Bytes per value

![[python-list-vs-packed-memory.svg]]

| Value | Bytes (CPython 3.11, 64-bit) |
|---|---|
| one base as an ASCII character in a file or a `str` | 1 |
| one base packed at 2 bits | 1/4 |
| one position as an unsigned 32-bit integer (`array('I')`, NumPy `uint32`), at most 4,294,967,295 | 4 |
| one position as a 64-bit integer | 8 |
| a Python `int` object (below $2^{30}$) | 28, plus an 8-byte pointer in a list |
| a Python `str` of $k$ ASCII characters | $49 + k$ |

Python's convenience costs a factor: a list of positions holds a pointer per element and a separate `int` object per value, about 36 bytes per position against 4 in an `array('I')` (measured below; [[Python Object Model]]).

### Auxiliary space of common operations

| Operation on a sequence of length $n$ | Auxiliary space |
|---|---|
| GC content with one counter | $O(1)$ |
| [[Reverse Complement]] as a new string | $\Theta(n)$, the output |
| reverse complement in place on a `bytearray` | $O(1)$ ([[Loop Invariant]], Exercise 5) |
| [[K-mer]] counts in a dictionary | $\Theta(\min(n, 4^k))$ entries of $\Theta(k)$ bytes |
| frequency array over all k-mers | $\Theta(4^k)$ counters |
| full alignment matrix, lengths $n$ and $m$ | $\Theta(nm)$ cells: 4 TB of 4-byte scores for two 1 Mb sequences, 8 MB with two rows |

## Deeper (L2)

### Why a genome index must fit in RAM

1. **Index queries are random accesses.** A hash lookup, a step of binary search in a suffix array or a rank query in an FM-index jumps to an address that depends on the data, with no locality from one access to the next.
2. **The model's unit cost holds only in RAM.** Secondary storage is much slower per access and transfers whole blocks, which is why algorithms on disk-resident data are analyzed by their number of disk accesses instead of their instructions.[^clrs-btree]
3. **Back of the envelope**, with round illustrative latencies (check real ones in [[Memory Hierarchy]]): 100 ns per random RAM access, 10 ms per random hard-disk access. Mapping $30 \times 3.055 \times 10^9 / 150 \approx 6.1 \times 10^8$ reads of 150 bp, at an assumed 100 random index accesses per read, makes $6.1 \times 10^{10}$ accesses: about 1.7 hours in RAM, about 19 years on disk. The latency ratio of $10^5$ passes straight into the running time.
4. **So index design is a space problem.** Shrinking the index from 12.2 GB (a 4-byte suffix array of one strand) to about 1.3 GB[^langmead] is a factor of 9.4; from 48.9 GB (8-byte positions, both strands), a factor of 38. That is what lets the whole index live in memory.

### Space-time trade-offs

- **Precompute or recompute.** Prefix sums of GC indicators ($n + 1$ integers) give the GC count of any window as one subtraction; recounting needs no extra memory but $\Theta(w)$ time per window of width $w$.
- **Three ways to count k-mers.** A frequency array of $4^k$ counters, the approach Compeau and Pevzner introduce after the naive algorithm,[^compeau] answers in $O(1)$ but costs $\Theta(4^k)$ memory even for a short text; a dictionary stores only the k-mers present; sorting the $n - k + 1$ k-mers needs $\Theta(n)$ memory and $\Theta(n \log n)$ comparisons.
- **Streaming versus loading.** Reading a whole file costs memory proportional to the file; streaming costs memory proportional to the largest record ([[FASTA Format]]).
- **Recursion is not free.** Each pending call keeps a stack frame, so a recursion of depth $d$ uses $\Theta(d)$ space even without any data structure ([[Recursion]]).

## Advanced (L3)

- **An information-theoretic floor.** A representation that distinguishes all $4^n$ DNA strings of length $n$ needs at least $\log_2 4^n = 2n$ bits, since $b$ bits have only $2^b$ states (pigeonhole). For the human genome that is $6.11 \times 10^9$ bits, 0.76 GB. Bowtie's index at about 1.3 GB[^langmead] is within a factor of 1.7 of storing the bare sequence while still supporting search: the goal of compressed and [[Succinct Data Structure|succinct data structures]] ([[Burrows-Wheeler Transform]], [[FM-Index]]). The bound holds for arbitrary strings; only structured sequences (repeats, biased composition) can be stored in fewer bits per base.
- **Beyond RAM by design.** Sorting alignments larger than memory switches to the external-memory model, where the cost is the number of block transfers ([[External Memory Algorithm]], [[Out-of-Core Computation]]).
- **Exactness for space.** [[Bloom Filter|Bloom filters]] and [[Count-Min Sketch|count-min sketches]] answer membership and count queries in a fixed budget of bits whatever the length of the keys, at the price of a controlled error rate.

## Mathematical representation

- With $M_t(x)$ the set of memory words in use after step $t$ on input $x$: $S_A(x) = \max_t |M_t(x)|$ and $S_A(n) = \max_{|x| = n} S_A(x)$; auxiliary space removes the words of the input and output.
- In the word-RAM, $S_A(n) \le n + c\,T_A(n)$ for a constant $c$.
- Bytes $=$ cells $\times$ bytes per cell. A position in a text of length $n$ needs $\lceil \log_2 n \rceil$ bits, rounded up to 32 or 64 in practice.
- DNA packed at 2 bits per base: $\lceil n/4 \rceil$ bytes; lower bound $2n$ bits for arbitrary DNA strings. Frequency array: $4^k \cdot b$ bytes for $b$-byte counters.

## Computational representation

`sys.getsizeof` gives the size of one object; `tracemalloc` measures what Python allocates while building a structure:

```python
import random
import sys
import tracemalloc
from array import array

print("int  ", sys.getsizeof(7), sys.getsizeof(10**9), sys.getsizeof(2**64))
print("str  ", sys.getsizeof(""), sys.getsizeof("ACGT"), sys.getsizeof("A" * 1000))
print("list ", sys.getsizeof([]), sys.getsizeof([0] * 1000))

def held_mb(build) -> float:
    """Memory (MB) still allocated by build() once it returns, while its result is alive."""
    tracemalloc.start()
    obj = build()
    held = tracemalloc.get_traced_memory()[0]
    tracemalloc.stop()
    return held / 1e6

def kmer_index(seq: str, k: int) -> dict[str, list[int]]:
    index: dict[str, list[int]] = {}
    for i in range(len(seq) - k + 1):
        index.setdefault(seq[i:i + k], []).append(i)
    return index

n = 10**6
random.seed(0)
print(f"list of n positions      {held_mb(lambda: [random.randrange(10**9) for _ in range(n)]):5.1f} MB")
print(f"array('I') of positions  {held_mb(lambda: array('I', (random.randrange(10**9) for _ in range(n)))):5.1f} MB")
print(f"list of n base codes 0-3 {held_mb(lambda: [random.randrange(4) for _ in range(n)]):5.1f} MB")
print(f"str of n bases           {held_mb(lambda: ''.join(random.choices('ACGT', k=n))):5.1f} MB")

random.seed(1)
seq = "".join(random.choices("ACGT", k=200_000))      # toy sequence
per_position = held_mb(lambda: kmer_index(seq, 16)) * 1e6 / (len(seq) - 15)
print(f"dict of 16-mer positions {per_position:5.0f} bytes per position"
      f" -> human genome (3.055e9 bases): {per_position * 3.055e9 / 1e9:.0f} GB")
```

```text
int   28 28 36
str   49 53 1049
list  56 8056
list of n positions       36.4 MB
array('I') of positions    4.1 MB
list of n base codes 0-3   8.4 MB
str of n bases             1.0 MB
dict of 16-mer positions   223 bytes per position -> human genome (3.055e9 bases): 682 GB
```

One million positions cost 36.4 MB as a list and 4.1 MB as an array. The list of base codes costs only its pointers, 8.4 MB, because CPython shares one object for each small integer; the same bases as a string take 1 MB. The most natural Python index, a dictionary from each 16-mer to the list of its positions, costs 223 bytes per position.

## Worked example

> [!example] A memory budget for indexing the human genome
> Machine: a workstation with 16 GB of RAM (an assumption for the exercise). Genome: $G = 3.055 \times 10^9$ bases.[^nurk] The Python dictionary cost comes from the measurement above; the rest is arithmetic (1 GB $= 10^9$ bytes).
>
> | Representation of the genome | Size | Fits in 16 GB? |
> |---|---:|---|
> | text, 1 byte per base | 3.1 GB | yes |
> | packed, 2 bits per base | 0.76 GB | yes |
> | suffix array, 4-byte positions, one strand | 12.2 GB | barely, with the text (15.3 GB) |
> | suffix array, 8-byte positions, both strands | 48.9 GB | no |
> | frequency array of all 16-mers, 4-byte counters | 17.2 GB | no |
> | Python dictionary of 16-mer positions (measured) | about 682 GB | no |
> | Bowtie Burrows-Wheeler index (published) | about 1.3 GB[^langmead] | yes |
>
> **Conclusion.** The algorithmically simplest index costs about 500 times more memory than the published compressed one. All of them except the frequency array are $\Theta(G)$; the constant in front of $G$ (223 bytes, 8 bytes, or under half a byte per base) decides whether the analysis runs on this machine.

## Common misconceptions

> [!warning] "Memory is cheap; only time matters"
> Memory is a hard limit, not a cost that grows smoothly: once a random-access structure spills out of RAM, each access pays disk latency, and a job of hours becomes a job of years (Deeper). Check the memory budget before optimizing speed.

> [!warning] "A list of a million small numbers takes about a megabyte"
> In CPython it takes 8.4 MB of pointers even when the numbers are shared small integers, and 36.4 MB for genomic positions (measured above). A `bytes`, `array` or NumPy array stores the raw values: 1 to 8 bytes each.

## Exercises

> [!question] Exercise 1 (L1)
> An index stores every position of both strands of the human genome. Can it use unsigned 32-bit positions? How many bytes do the positions take?

> [!success]- Solution
> Both strands give $2 \times 3.055 \times 10^9 = 6.11 \times 10^9$ positions, more than $2^{32} - 1 = 4{,}294{,}967{,}295$: 32 bits cannot number them ([[Model of Computation]]). With 8-byte positions: $6.11 \times 10^9 \times 8 = 48.9$ GB. One workaround: number the positions of one strand and store the strand as a separate bit, which keeps 4-byte positions (24.4 GB for the entries of both strands).

> [!question] Exercise 2 (L2)
> What is the largest $k$ for which a frequency array of 4-byte counters over all k-mers fits in 16 GB? For the human genome, would a dictionary holding only the k-mers present do better at $k = 20$?

> [!success]- Solution
> $4^k \times 4 \le 1.6 \times 10^{10}$ gives $4^k \le 4 \times 10^9$, so $k \le \log_4(4 \times 10^9) \approx 15.9$: $k = 15$ (4.3 GB), while $k = 16$ needs 17.2 GB. At $k = 20$ the array would need $4^{20} \times 4 \approx 4.4$ TB. A dictionary stores at most $G - 19 \approx 3 \times 10^9$ entries, but at about 200 bytes each in Python that is still hundreds of GB. Neither fits. Packing each k-mer into one 64-bit word ($k \le 32$) and storing the words in a sorted array brings the cost to 8 bytes per k-mer, still $3 \times 10^9 \times 8 \approx 24$ GB: the next steps are counting only distinct k-mers, compressing, or splitting the work by k-mer prefix.

> [!question] Exercise 3 (L2, Python)
> Pack a DNA string into a `bytearray` at 2 bits per base (A, C, G, T = 0, 1, 2, 3, first base in the high bits), write the inverse function, and compare the sizes for $10^6$ random bases.

> [!success]- Solution
> ```python
> import random
> import sys
>
> CODE = {"A": 0, "C": 1, "G": 2, "T": 3}
>
> def pack(seq: str) -> bytearray:
>     """4 bases per byte, first base in the two high bits."""
>     out = bytearray((len(seq) + 3) // 4)
>     for i, base in enumerate(seq):
>         out[i // 4] |= CODE[base] << (6 - 2 * (i % 4))
>     return out
>
> def unpack(packed: bytearray, n: int) -> str:
>     return "".join("ACGT"[(packed[i // 4] >> (6 - 2 * (i % 4))) & 3] for i in range(n))
>
> random.seed(4)
> seq = "".join(random.choices("ACGT", k=10**6))        # toy sequence
> packed = pack(seq)
> assert unpack(packed, len(seq)) == seq
> print(sys.getsizeof(seq), sys.getsizeof(packed), pack("ACGT").hex(), pack("GATTACA").hex())
> ```
> Output: `1000049 250057 1b 8f10`. The packed form is 4 times smaller; `ACGT` becomes the single byte `00 01 10 11` = `0x1b`. The length must be stored separately (the last byte of `GATTACA` is padded with zeros), and so must any `N`, which has no 2-bit code.

> [!question] Exercise 4 (L3)
> Prove that no lossless encoding can store every DNA string of length $n$ in fewer than $2n$ bits, and compare this floor with Bowtie's human index. Why can a compressor still go below 2 bits per base on some genomes?

> [!success]- Solution
> There are $4^n = 2^{2n}$ strings; an encoding into fewer than $2n$ bits has fewer than $2^{2n}$ possible codes, so two strings would share a code (pigeonhole) and could not both be decoded. For $n = 3.055 \times 10^9$ the floor is $6.11 \times 10^9$ bits, 0.76 GB; Bowtie's searchable index, about 1.3 GB,[^langmead] is 1.7 times this floor. The bound concerns all strings at once: an encoding can give short codes to likely strings (repetitive or compositionally biased sequence) only by giving longer codes to others, so it beats 2 bits per base exactly on sequences with structure.

## Mastery checklist

- [ ] 1 Recognized: I can define space complexity, auxiliary space and in-place algorithms.
- [ ] 2 Understood: I can explain why space is bounded by time, and why a genome index must fit in RAM.
- [ ] 3 Practiced: I can compute the bytes of a representation of a real genome and measure Python memory with `sys.getsizeof` and `tracemalloc`.
- [ ] 4 Applied: in [[05-sequence-search]], I measured the memory of my k-mer index for several $k$ and chose a representation that fits the machine; [[01-dna-engine]] streams genome files.
- [ ] 5 Explained: I can teach space-time trade-offs, the $2n$-bit floor, and how compressed indexes and external-memory algorithms push the limits.

## References

[^clrs2]: [[Introduction to Algorithms (Cormen)]], 4th ed., ch. 2 "Getting Started" (insertion sort sorts in place).
[^clrs-btree]: [[Introduction to Algorithms (Cormen)]], 4th ed., chapter "B-Trees" (data on secondary storage; algorithms analyzed by disk accesses).
[^jones]: [[An Introduction to Bioinformatics Algorithms (Jones)]], treatment of space-efficient sequence alignment by divide and conquer.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "Where in the Genome Does DNA Replication Begin?" (the frequency array).
[^langmead]: [[Langmead 2009 - Ultrafast and Memory-Efficient Alignment of Short DNA Sequences to the Human Genome]], *Genome Biology* 10(3):R25, abstract (memory footprint for the human genome).
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science* 376:44-53.
[^fernandez]: [[Fernández 2024 - A 160 Gbp Fork Fern Genome Shatters Size Record for Eukaryotes]], *iScience* 27(6):109889.
