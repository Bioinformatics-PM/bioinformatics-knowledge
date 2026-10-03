---
aliases:
  - Character String
  - Word (Formal Language)
  - Chaîne de caractères
  - str
  - bytes
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Array]]"
  - "[[Set]]"
  - "[[Python Object Model]]"
related:
  - "[[Exact Pattern Matching]]"
  - "[[K-mer]]"
  - "[[Reverse Complement]]"
  - "[[FASTA Format]]"
  - "[[FASTQ Format]]"
  - "[[Rolling Hash]]"
  - "[[Hash Function]]"
projects:
  - "[[01-dna-engine]]"
  - "[[bio-core]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Algorithms on Strings, Trees, and Sequences (Gusfield)]]"
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[Cock 2010 - The Sanger FASTQ File Format]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
---

# String

> [!abstract]
> A string is a finite sequence of symbols from an alphabet: a DNA read is a string over {A, C, G, T}. In Python it is either `str` (text) or `bytes` (raw data), both immutable, which makes them safe dictionary keys but means every slice and every concatenation builds a new object.

## Definition

Given a finite **alphabet** $\Sigma$, a **string** over $\Sigma$ is a finite sequence of symbols of $\Sigma$; $\Sigma^*$ is the set of all strings, $\varepsilon$ the empty string, $|s|$ the length of $s$, and $st$ the concatenation of $s$ and $t$. A string $w$ is a **prefix** of $s$ if $s = wy$ and a **suffix** if $s = yw$ for some string $y$.[^clrs32] A **substring** is a contiguous part of $s$; a **subsequence** keeps the order of the symbols but not necessarily their contiguity.[^gusfield]

In Python, `str` is an immutable sequence of Unicode characters and `bytes` an immutable sequence of bytes; `encode` and `decode` convert between them with an encoding such as UTF-8.[^mck2] `bytearray` is the mutable counterpart of `bytes` (shown below).

## Why it matters

- **Sequence files are strings over small alphabets**: DNA over {A, C, G, T} plus `N` and the ambiguity codes ([[IUPAC Nucleotide Code]], [[FASTA Format]]). In FASTQ, each quality character encodes a Phred score as its ASCII code minus 33,[^cock] so `bytes` hands you the integers directly ([[FASTQ Format]]).
- **Immutable strings are hashable**, hence usable as dictionary keys:[^mck3] k-mers as keys of a counter ([[K-mer]], [[Hash Table]]).
- **Slices copy.** Extracting all k-mers of a sequence by slicing writes $k$ characters per window, $O(nk)$ in total; a [[Rolling Hash]] or an integer encoding avoids it.
- **Memory.** One byte per base in `str` or `bytes` for ASCII letters; two bits per base when packed. For the 3.055 Gbp T2T-CHM13 genome,[^nurk] that is 3.06 GB against 0.76 GB.

## Core (L1)

**Counting.** A string of length $n$ has $n(n+1)/2$ non-empty substrings by position (choose a start $i$ and an end $j \ge i$) and $n - k + 1$ windows of length $k$; there are $\sigma^k$ possible strings of length $k$ over an alphabet of size $\sigma$, so $4^k$ k-mers.

| Type | `x[0]` | Mutable | Hashable | Typical use |
|---|---|---|---|---|
| `str` | a 1-character `str` | no | yes | text, sequences as keys, `str.translate` |
| `bytes` | an `int` 0-255 | no | yes | raw file content, quality strings |
| `bytearray` | an `int` 0-255 | yes | no | building or editing a sequence in place |
| `memoryview` | an `int` (over bytes) | as its object | n/a | slices without copying |

```python
s = "ACGT"
b = s.encode("ascii")                           # bytes: what a file holds
ba = bytearray(b)                               # mutable copy
print(s[0], b[0], ba[0], b[1:3], ba[1:3])
try:
    s[0] = "T"
except TypeError as e:
    print(e)
ba[0] = ord("T")
print(ba, hash(s) == hash("AC" + "GT"), len("é".encode("utf-8")), len(s.encode("utf-8")))
for bad in (lambda: "AC" + b"GT", lambda: hash(ba)):
    try:
        bad()
    except TypeError as e:
        print(e)
```

```text
A 65 65 b'CG' bytearray(b'CG')
'str' object does not support item assignment
bytearray(b'TCGT') True 2 4
can only concatenate str (not "bytes") to str
unhashable type: 'bytearray'
```

ASCII letters take one byte in UTF-8, `é` two. Equal strings hash equally whatever object holds them, which is what dictionary lookups rely on.

## Deeper (L2)

**Building a sequence piece by piece.** Immutability means `s + t` creates a new string of $|s| + |t|$ characters. Appending one character $n$ times therefore copies $1 + 2 + \dots + n = n(n+1)/2$ characters in the worst case. Measured on CPython 3.11 (ms, best of 3; indicative):

```python
import timeit
def plus_str(n):
    out = ""
    for _ in range(n):
        out += "A"
    return out
def plus_bytes(n):
    out = b""
    for _ in range(n):
        out += b"A"
    return out
def extend_bytearray(n):
    out = bytearray()
    for _ in range(n):
        out += b"A"
    return out
def join_list(n):
    parts = []
    for _ in range(n):
        parts.append("A")
    return "".join(parts)
for n in (50_000, 100_000, 200_000):
    times = [min(timeit.repeat(lambda: f(n), number=1, repeat=3)) for f in (plus_str, plus_bytes, extend_bytearray, join_list)]
    print(n, " ".join(f"{t * 1e3:.1f}" for t in times))
```

```text
50000 4.5 29.1 1.8 1.3
100000 4.1 121.5 3.4 3.0
200000 8.4 482.4 6.7 5.8
```

`bytes +=` quadruples when $n$ doubles: quadratic, as derived. `bytearray` (a dynamic array, [[Array]]) and `"".join` are linear by design. `str +=` happened to stay linear here because CPython resized the string in place; nothing in the language promises it, so build with `join` or a `bytearray`.

**Slices copy; views do not.** A `bytes` slice copies its bytes; a `memoryview` slice only records an offset and a length over the same buffer.

```python
genome = b"ACGT" * 2_500_000                    # 10 Mb toy sequence (invented)
view = memoryview(genome)
for L in (1_000, 1_000_000):
    t_copy = min(timeit.repeat(lambda: genome[100:100 + L], number=200, repeat=5)) / 200
    t_view = min(timeit.repeat(lambda: view[100:100 + L], number=200, repeat=5)) / 200
    print(L, f"bytes slice {t_copy * 1e6:.2f} us", f"memoryview slice {t_view * 1e6:.2f} us")
print(view[4:8].tobytes(), view[4:8].obj is genome)
```

```text
1000 bytes slice 0.14 us memoryview slice 0.11 us
1000000 bytes slice 69.83 us memoryview slice 0.11 us
b'ACGT' True
```

The copy grows with the slice, the view does not. NumPy array slices are views as well.[^mck4]

**Text or bytes for sequence data.** Files open in text mode by default, which decodes their bytes into `str`; appending `b` to the mode gives binary mode and `bytes`.[^mck3] For large FASTA or FASTQ files, working on `bytes` skips decoding, and `bytes.translate` complements a sequence without it ([[Reverse Complement]], Exercise 4). Decode only what must become text, such as identifiers.

## Advanced (L3)

- **CPython's `str` memory depends on the widest character** (observed with `sys.getsizeof` on 1,000-character strings): 1,049 bytes when all characters are ASCII, 1,073 with one `é`, 2,074 with one `α`, 4,076 with one character beyond U+FFFF; `bytes` takes 1,033. A single non-Latin character pasted into a header and concatenated with a sequence can double or quadruple the memory of the result.
- **Packing.** With four letters, 2 bits per base suffice: 4 bases per byte, and a k-mer with $k \le 32$ fits in one 64-bit integer, so it can be hashed or compared as a single machine word ([[Hash Function]], [[Rolling Hash]]). Packing loses `N` and case, which must be stored separately, for instance as intervals.
- **Strings as index input.** Suffix arrays, the Burrows-Wheeler transform and the FM-index preprocess one long string so that substring queries no longer scan it ([[Suffix Array]], [[Burrows-Wheeler Transform]], [[FM-Index]]); exact matching on raw strings is the baseline they replace ([[Exact Pattern Matching]]).

## Mathematical representation

- $\Sigma^k$ is the set of strings of length $k$, $|\Sigma^k| = \sigma^k$ with $\sigma = |\Sigma|$, and $\Sigma^* = \bigcup_{k \ge 0} \Sigma^k$.
- Concatenation is associative with identity $\varepsilon$: $(\Sigma^*, \cdot, \varepsilon)$ is a monoid, and $|st| = |s| + |t|$.
- Substring $s[i..j] = s_i \dots s_j$ for $1 \le i \le j \le n$: $\binom{n}{2} + n = n(n+1)/2$ choices of $(i, j)$; windows of length $k$: $n - k + 1$.
- Repeated concatenation with copying: $\sum_{i=1}^{n} i = n(n+1)/2 = \Theta(n^2)$ character writes. Packing $n$ bases at 2 bits: $\lceil 2n/8 \rceil$ bytes.

## Computational representation

The code above covers the types, building, slicing and views. For sequence work, a `str` is convenient (translate, find, dictionary keys); `bytes` is the raw form of a file and gives integers when indexed; `bytearray` builds or edits in place; `memoryview` exposes windows of a large `bytes` without copying. The Lab's [[01-dna-engine]] wraps a validated sequence string in an immutable type ([[Value Object]]).

## Worked example

> [!example] Decoding and trimming a FASTQ record as bytes (toy record, invented)
> ```python
> record = b"@read1\nGATTACAGATTACA\n+\nIIIIIIHHH#####\n"
> header, seq, plus, qual = record.split(b"\n")[:4]
> q = [c - 33 for c in qual]                      # Phred+33: iterating bytes yields ints
> print(q)
> cut = next((i for i, x in enumerate(q) if x < 20), len(q))
> print(round(sum(q) / len(q), 2), cut, seq[:cut].decode())
> # [40, 40, 40, 40, 40, 40, 39, 39, 39, 2, 2, 2, 2, 2]
> # 26.21 9 GATTACAGA
> ```
> 1. `I` is ASCII 73, so $Q = 73 - 33 = 40$; `H` gives 39 and `#` (35) gives 2.[^cock]
> 2. The mean quality, 26.21, hides a bad tail: five bases at $Q = 2$, that is an error probability $p = 10^{-Q/10} = 10^{-0.2} \approx 0.63$ each ([[Phred Quality Score]]).[^cock]
> 3. An invented rule, "cut at the first base below $Q = 20$", keeps 9 bases. Only the kept sequence is decoded to `str`, the header and qualities never are.

## Common misconceptions

> [!warning] "`str` and `bytes` are interchangeable"
> `b"ACGT"[0]` is the integer 65, `"ACGT"[0]` is `"A"`, and mixing the two in `+` raises `TypeError`. Pick one per layer: bytes for I/O and heavy scanning, `str` where text semantics are needed.

> [!warning] "A slice is a view"
> Slices of `str`, `bytes` and `list` are new objects; slicing a 1 Mb window cost about 70 µs above, against 0.1 µs for a `memoryview`. NumPy slices, by contrast, are views, and modifying them modifies the original.[^mck4]

> [!warning] "`s += t` in a loop is fine"
> It is quadratic for `bytes` (measured) and for any immutable string type without special help. CPython's in-place trick for `str` is an implementation detail; `join` and `bytearray` are linear by design.

## Exercises

> [!question] Exercise 1 (L1)
> For a string of length 10, count the non-empty substrings by position, the windows of length 3, and the possible DNA 3-mers. Are `TAC` and `ATA` substrings, subsequences, or both, of `GATTACA`?

> [!success]- Solution
> $10 \times 11 / 2 = 55$ substrings by position; $10 - 3 + 1 = 8$ windows; $4^3 = 64$ possible 3-mers. `TAC` is a substring (positions 4 to 6), hence also a subsequence. `ATA` is only a subsequence (positions 2, 3, 5): the windows of length 3 are GAT, ATT, TTA, TAC, ACA.

> [!question] Exercise 2 (L1)
> Predict: `"ACGT"[1]`, `b"ACGT"[1]`, `bytearray(b"ACGT")[1:3]`, `"AC" + b"GT"`, `hash(b"ACGT") == hash(b"AC" + b"GT")`.

> [!success]- Solution
> `'C'`; `67`; `bytearray(b'CG')`; `TypeError` (cannot concatenate `str` and `bytes`); `True` (equal immutable values hash equally).

> [!question] Exercise 3 (L2)
> Prove that building a string of $n$ characters by $n$ one-character concatenations that copy costs $\Theta(n^2)$, and evaluate the copies for $n = 10^6$. Why is `bytearray` linear?

> [!success]- Solution
> The $i$-th concatenation writes the $i - 1$ old characters and the new one: $\sum_{i=1}^{n} i = n(n+1)/2 = \Theta(n^2)$, that is $500{,}000{,}500{,}000$ character writes for $n = 10^6$. A `bytearray` is a dynamic array: appends write into spare capacity and resizes are geometric, so the total is $O(n)$ amortized ([[Array]]).

> [!question] Exercise 4 (L2, Python)
> Write the reverse complement of a DNA sequence held as `bytes` (keep `N`, handle lowercase), and check it against a `str` version.

> [!success]- Solution
> ```python
> COMP = bytes.maketrans(b"ACGTacgtN", b"TGCAtgcaN")
> def revcomp(seq: bytes) -> bytes:
>     return seq.translate(COMP)[::-1]
> print(revcomp(b"GATTACAN"), revcomp(b"GATTACAN") == "GATTACAN".translate(str.maketrans("ACGTN", "TGCAN"))[::-1].encode())
> # b'NTGTAATC' True
> ```
> Both `translate` and `[::-1]` run in $O(n)$ inside the interpreter's C code; no per-base Python loop.

> [!question] Exercise 5 (L3, Python)
> Pack a DNA string at 2 bits per base (A=0, C=1, G=2, T=3, first base in the high bits), unpack it, and compute the packed size of the T2T-CHM13 genome.

> [!success]- Solution
> ```python
> CODE = {"A": 0, "C": 1, "G": 2, "T": 3}
> def pack(seq: str) -> bytes:
>     out = bytearray((len(seq) + 3) // 4)
>     for i, base in enumerate(seq):
>         out[i // 4] |= CODE[base] << (6 - 2 * (i % 4))
>     return bytes(out)
> def unpack(data: bytes, n: int) -> str:
>     return "".join("ACGT"[(data[i // 4] >> (6 - 2 * (i % 4))) & 3] for i in range(n))
> p = pack("GATTACACGT")
> print(p.hex(), len(p), unpack(p, 10) == "GATTACACGT")
> # 8f11b0 3 True
> ```
> `GATT` → `10 00 11 11` = `0x8f`; the length must be stored with the data, since the last byte is padded. For $3.055 \times 10^9$ bases: $3.055 \times 10^9 / 4 \approx 0.76$ GB instead of 3.06 GB, before storing `N` runs and soft-masking separately.

## Mastery checklist

- [ ] 1 Recognized: I can define alphabet, string, substring, subsequence, prefix and suffix, and name Python's four string-like types.
- [ ] 2 Understood: I can explain immutability, why slices and concatenations copy, and when `bytes` beats `str`.
- [ ] 3 Practiced: I can decode Phred qualities from bytes, build sequences linearly, slice without copying and pack DNA at 2 bits per base.
- [ ] 4 Applied: in [[01-dna-engine]], my sequence type validates its alphabet and I measured its memory and speed on a real genome file.
- [ ] 5 Explained: I can teach the cost model of strings in Python and the representation choices of genome-scale tools.

## References

[^clrs32]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 32 "String Matching": notation for strings, prefixes and suffixes.
[^gusfield]: [[Algorithms on Strings, Trees, and Sequences (Gusfield)]], 1997: substrings versus subsequences.
[^mck2]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 2 "Python Language Basics, IPython, and Jupyter Notebooks": immutable strings, bytes and Unicode, `encode` and `decode`.
[^mck3]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 3 "Built-In Data Structures, Functions, and Files": dictionary keys must be hashable (immutable); text versus binary file modes.
[^mck4]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 4 "NumPy Basics: Arrays and Vectorized Computation": array slices are views.
[^cock]: [[Cock 2010 - The Sanger FASTQ File Format]], *Nucleic Acids Research*: Phred quality $Q = -10 \log_{10} p$, encoded as ASCII characters with an offset of 33.
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science*: 3.055 Gbp T2T-CHM13 assembly.
