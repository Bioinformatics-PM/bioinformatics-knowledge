---
aliases:
  - Two's Complement
  - Fixed-Width Integer
  - Integer Overflow
  - Integer dtype
  - Représentation des entiers
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Python Object Model]]"
  - "[[N-Dimensional Array]]"
  - "[[Modular Arithmetic]]"
related:
  - "[[Floating-Point Arithmetic]]"
  - "[[Vectorization]]"
  - "[[Array]]"
  - "[[Genomic Coordinate System]]"
  - "[[SAM Format]]"
  - "[[K-mer]]"
  - "[[Hash Function]]"
  - "[[Bit-Parallel String Matching]]"
  - "[[Phred Quality Score]]"
  - "[[Delimited Text Format]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[09-genome-browser]]"
sources:
  - "[[Python Documentation]]"
  - "[[Python for Data Analysis (McKinney)]]"
  - "[[GA4GH hts-specs]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
---

# Integer Representation

> [!abstract]
> A machine integer is a fixed number of bits read either as unsigned or as two's complement: arithmetic on it is arithmetic modulo $2^w$, so NumPy integers wrap around silently when a result leaves their range, whereas Python's `int` grows as needed and never overflows.

## Definition

A **fixed-width integer** of $w$ bits stores one of $2^w$ bit patterns. Read as **unsigned**, the pattern is the binary number $0$ to $2^w - 1$; read as **two's complement**, the top bit carries weight $-2^{w-1}$, giving $-2^{w-1}$ to $2^{w-1} - 1$. NumPy's integer dtypes (`int8`, `uint8`, ..., `int64`, `uint64`) are fixed-width in this sense, with sizes of 1, 2, 4 or 8 bytes.[^mck4] Python's `int` is different: integers have unlimited precision, and Python defines bitwise operations and `int.to_bytes(..., signed=True)` on negative numbers through their two's complement.[^types]

## Why it matters

- **Memory is width × count.** Bases and Phred qualities fit in `uint8`, so a matrix of $10^8$ quality values takes 100 MB instead of 800 MB in `int64` ([[N-Dimensional Array]], [[Phred Quality Score]]).
- **Coordinates outgrow 32 bits.** A human genome holds about $3.055 \times 10^9$ bp,[^nurk] more than $2^{31} - 1 = 2\,147\,483\,647$: positions on a concatenated genome need 64 bits, while BAM stores positions as 32-bit integers and so limits each reference sequence to $2^{31} - 1$ bp.[^sam]
- **Overflow is silent.** An `int32` or `uint16` array that overflows returns wrong numbers with no error; a negative length computed in `uint32` becomes four billion. These bugs survive tests on small toy data and appear on real genomes ([[09-genome-browser]]).
- **Bits are a data structure.** Two bits per base pack a $k$-mer into one integer, the basis of fast [[K-mer]] counting, hashing and [[Bit-Parallel String Matching|bit-parallel matching]].

## Core (L1)

![[twos-complement-4bit-wheel.svg]]

The figure shows the whole idea on 4 bits: 16 patterns on a wheel, each with an unsigned and a signed reading. Adding 1 moves one step clockwise; the hardware keeps only the low $w$ bits, so crossing $1111 \to 0000$ wraps the unsigned value from 15 to 0 and crossing $0111 \to 1000$ turns the signed value 7 into $-8$. NumPy types are the same wheel with $2^8$, $2^{16}$, $2^{32}$ or $2^{64}$ positions. Outputs below come from NumPy 2.4.6 on Python 3.11.

```python
import numpy as np

for t in (np.uint8, np.int8, np.uint16, np.int32, np.uint32, np.int64):
    info = np.iinfo(t)
    print(f"{t.__name__:6} {info.bits:2} bits [{info.min}, {info.max}]")

print(2**63, (2**63).bit_length())                       # Python int: grows as needed
pos = np.array([2**31 - 1, 5], dtype=np.int32)
print(pos + 1)                                           # wraps, no warning
print(np.array([3_000_000_000, 120]).astype(np.int32))   # silent narrowing cast
try:
    np.array([3_000_000_000], dtype=np.int32)
except OverflowError as err:
    print("OverflowError:", err)
```

```text
uint8   8 bits [0, 255]
int8    8 bits [-128, 127]
uint16 16 bits [0, 65535]
int32  32 bits [-2147483648, 2147483647]
uint32 32 bits [0, 4294967295]
int64  64 bits [-9223372036854775808, 9223372036854775807]
9223372036854775808 64
[-2147483648           6]
[-1294967296         120]
OverflowError: Python integer 3000000000 out of bounds for int32
```

**Choosing a dtype** is choosing the smallest wheel that can never be crossed, including by intermediate results:

| Data | Range needed | dtype |
|---|---|---|
| Base codes, one-hot values, Phred qualities | 0 to a few dozen | `uint8` |
| Read depth at one position | can exceed 65 535 in amplicon data | `uint32` (not `uint16`) |
| Position within one chromosome | below $2^{31} - 1$ (the BAM limit)[^sam] | `int32` for storage, `int64` for arithmetic |
| Position on a concatenated genome, cumulative offsets | above $3 \times 10^9$[^nurk] | `int64` |
| Counts per gene and sample; totals over a matrix | totals can exceed $2^{31}$ | `int32` cells, `int64` sums |

**Unsigned subtraction is a trap.** A length `end - start` on a malformed interval, or a distance between two positions taken in the wrong order, wraps instead of going negative. Signed types have their own edge: $-(-2^{w-1})$ does not fit, so `abs` of the minimum is the minimum.

```python
start = np.array([500, 1200], dtype=np.uint32)          # invented intervals, the second malformed
end = np.array([800, 1000], dtype=np.uint32)
print(end - start, end.astype(np.int64) - start)
print(np.abs(np.array([-128, -5], dtype=np.int8)))
```

```text
[       300 4294967096] [ 300 -200]
[-128    5]
```

## Deeper (L2)

**Where NumPy wraps, warns or raises.** The behaviour depends on the operation, not only on the values (observed with NumPy 2.4.6):

| Operation | Out-of-range result |
|---|---|
| Arithmetic between arrays, or array and NumPy scalar | wraps silently |
| Arithmetic between two NumPy scalars | wraps, with a `RuntimeWarning` |
| Python `int` that does not fit the array's dtype (`np.array(..., dtype=)`, `uint8_array + 300`) | `OverflowError` |
| `astype` to a narrower type | wraps silently |
| `sum`, `cumsum` of small integer types | accumulate in a 64-bit type |

```python
import warnings

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    print(np.int32(2**31 - 1) + np.int32(1), [str(w.message) for w in caught])
depth = np.full(70_000, 60_000, dtype=np.uint16)         # invented per-base depths
print(depth.sum(), depth.sum().dtype, (depth + depth)[:2], np.add(depth, depth, dtype=np.uint32)[:2])
mixed = np.array([2**63 + 1], dtype=np.uint64) + np.array([1], dtype=np.int64)
print(mixed.dtype, int(mixed[0]), 2**63 + 2)
```

```text
-2147483648 ['overflow encountered in scalar add']
4200000000 uint64 [54464 54464] [120000 120000]
float64 9223372036854775808 9223372036854775810
```

The reduction is safe, the element-wise sum of two `uint16` depth tracks is not, unless the output dtype is widened (`dtype=np.uint32`, or `astype` before computing). Mixing `uint64` with `int64` has no common integer type, so NumPy computes in `float64`, which represents integers exactly only up to $2^{53}$ ([[Floating-Point Arithmetic]]): the last digits are lost without any warning.

**Integers that become floats.** An integer column with one missing value cannot stay `int64` in a NumPy-backed table: it is read as `float64`, exact only below $2^{53}$ ([[Delimited Text Format]]). Nullable integer types (`Int64` in pandas) keep integers and missing values together.[^mck7]

**Defensive rules.** Store compactly, compute wide: cast to `int64` before subtracting coordinates or summing counts; check ranges with `np.iinfo` before narrowing (Exercise 4); keep coordinates signed so that a bug shows up as a negative number instead of four billion.

## Advanced (L3)

**Bases as bits.** With the code A=0, C=1, G=2, T=3, a $k$-mer is a base-4 number of $2k$ bits: `code = ((code << 2) | base) & mask` slides the window by one base in $O(1)$, and in this code the complement of $b$ is $3 - b$, so the reverse complement and the canonical $k$-mer (the smaller of the two codes) are integer operations ([[K-mer]], [[Reverse Complement]]). Since $4^{32} = 2^{64}$, a `uint64` holds any $k$-mer with $k \le 32$; in NumPy the left shift then discards the high bits by the same wrap-around that is a bug elsewhere, and in Python the `& mask` is mandatory because `int` never drops bits.

```python
CODE = {"A": 0, "C": 1, "G": 2, "T": 3}


def kmer_codes(seq: str, k: int) -> list[int]:
    """Rolling 2-bit codes of all k-mers: shift in 2 bits, mask to 2k bits."""
    mask = (1 << 2 * k) - 1
    codes, code = [], 0
    for i, base in enumerate(seq):
        code = ((code << 2) | CODE[base]) & mask
        if i >= k - 1:
            codes.append(code)
    return codes


def decode(code: int, k: int) -> str:
    return "".join("ACGT"[(code >> 2 * (k - 1 - j)) & 3] for j in range(k))


def revcomp_code(code: int, k: int) -> int:
    """Complement is 3 - b in this code (A<->T, C<->G); read the 2-bit digits backwards."""
    rc = 0
    for _ in range(k):
        rc = (rc << 2) | (3 - (code & 3))
        code >>= 2
    return rc


seq = "GATTACAGATTACA"                                       # invented
codes = kmer_codes(seq, 4)
print(codes[:5], [decode(c, 4) for c in codes[:5]])
print(decode(revcomp_code(codes[0], 4), 4), min(codes[0], revcomp_code(codes[0], 4)))
print(all(decode(c, 4) == seq[i:i + 4] for i, c in enumerate(codes)))
```

```text
[143, 60, 241, 196, 18] ['GATT', 'ATTA', 'TTAC', 'TACA', 'ACAG']
AATC 13
True
```

**Binary genomic formats are integer layouts.** BAM writes all multi-byte integers little-endian, stores the read sequence as 4-bit codes indexed into `=ACMGRSVTWYHKDBN` (two bases per byte, high nibble first) and positions as signed 32-bit integers.[^sam] Its BAI index bins positions only up to $2^{29}$ (about 537 Mb), which is why longer reference sequences need the CSI index, whose bin depth is configurable.[^csi] A parser that reads these bytes with the wrong width or byte order produces plausible-looking garbage (Exercise 6).

## Mathematical representation

- A $w$-bit pattern is $b = (b_{w-1}, \dots, b_0) \in \{0,1\}^w$. Its **unsigned** value is $U(b) = \sum_{i=0}^{w-1} b_i 2^i \in [0, 2^w - 1]$; its **two's complement** value is
$$T(b) = -b_{w-1} 2^{w-1} + \sum_{i=0}^{w-2} b_i 2^i = U(b) - b_{w-1} 2^w \in [-2^{w-1}, 2^{w-1} - 1].$$
- Both readings agree modulo $2^w$: $T(b) \equiv U(b) \pmod{2^w}$. Addition, subtraction and multiplication are therefore the same circuit for both, and the stored result of an exact result $x$ is $x \bmod 2^w$ (unsigned) or $\big((x + 2^{w-1}) \bmod 2^w\big) - 2^{w-1}$ (signed): the wheel of the figure ([[Modular Arithmetic]]).
- **Negation.** Let $\bar b$ flip every bit. Then $U(\bar b) = 2^w - 1 - U(b)$, so $U(\bar b) + 1 \equiv -U(b) \pmod{2^w}$: "flip the bits and add 1" negates. For $T(b) = -2^{w-1}$ the result is $-2^{w-1}$ again, the only value (besides 0) equal to its own negation.
- **Overflow test.** A signed sum $x + y$ overflows exactly when $x$ and $y$ have the same sign and the stored result has the other sign.
- **Size.** $n$ values of width $w$ occupy $nw/8$ bytes; a $k$-mer needs $2k$ bits, so the number of distinct $k$-mers, $4^k$, fits a $w$-bit code iff $k \le w/2$.

## Computational representation

Python exposes the bit patterns directly; NumPy reinterprets bytes with `view` and `frombuffer`, with the byte order written in the dtype (`<` little-endian, `>` big-endian):

```python
for v in (5, -5, -128):
    print(v, v.to_bytes(1, "big", signed=True).hex(), format(v & 0xFF, "08b"),
          np.array([v], dtype=np.int8).view(np.uint8)[0])
raw = b"\xe8\x03\x00\x00"
print((1000).to_bytes(4, "little").hex(), np.frombuffer(raw, dtype="<i4")[0], np.frombuffer(raw, dtype=">i4")[0])


def wrap(x: int, bits: int, signed: bool) -> int:
    """What a fixed-width register keeps of the exact integer x."""
    x %= 1 << bits
    return x - (1 << bits) if signed and x >= 1 << (bits - 1) else x


print(wrap(250 + 10, 8, False), wrap(2**31, 32, True), wrap(-1, 32, False), wrap(3_000_000_000, 32, True))
```

```text
5 05 00000101 5
-5 fb 11111011 251
-128 80 10000000 128
e8030000 1000 -402456576
4 -2147483648 4294967295 -1294967296
```

`-5` is stored as `11111011`, the same byte as unsigned 251 ($251 - 256 = -5$). The four bytes `e8 03 00 00` are 1000 read little-endian and $-402\,456\,576$ read big-endian. `wrap` reproduces every NumPy result above from Python's exact integers, which makes it a test oracle for fixed-width code.

## Worked example

> [!example] Genome-wide coordinates in 32 bits
> A [[09-genome-browser]] track concatenates chromosomes so that one integer locates any base. Toy genome (invented): 13 chromosomes of 248 Mb each.
> 1. **Offsets**: chromosome $j$ starts at $o_j = \sum_{i<j} L_i$; the last one starts at $12 \times 248 \times 10^6 = 2.976 \times 10^9$.
> 2. **Global position** of base 1,000,000 on chromosome 13: $2.977 \times 10^9$, larger than $2^{31} - 1 = 2\,147\,483\,647$.
> 3. **Narrowing to save memory**:
> ```python
> lengths = np.full(13, 248_000_000, dtype=np.int64)          # invented chromosome lengths
> offsets = np.concatenate(([0], np.cumsum(lengths)[:-1]))     # start of each chromosome
> glob = offsets + 1_000_000                                   # position 1,000,000 of each chromosome
> print(offsets[-1], glob[-1], glob.astype(np.int32)[-3:])
> print(2**31 - 1, (glob > 2**31 - 1).sum())
> ```
> ```text
> 2976000000 2977000000 [-1813967296 -1565967296 -1317967296]
> 2147483647 4
> ```
> 4. **Diagnosis**: $2\,977\,000\,000 - 2^{32} = -1\,317\,967\,296$, exactly the wrap formula. Four chromosomes are corrupted, the first nine are fine, so a test on a small genome passes. A real human assembly, about $3.055 \times 10^9$ bp,[^nurk] crosses the same line. Fix: keep global coordinates in `int64`, or store `(chromosome, int32 position)` pairs as BAM does.[^sam]

## Common misconceptions

> [!warning] "NumPy raises an error on overflow"
> Array arithmetic wraps silently; only scalar operations warn and only out-of-range Python literals raise. A pipeline can run to completion on wrapped numbers.

> [!warning] "Unsigned types are safer for things that cannot be negative"
> Lengths and positions cannot be negative, but their differences can. In `uint32`, `800 - 1000` is 4 294 967 096, a valid-looking position. Signed types make the bug visible.

> [!warning] "`int64` is always enough, so dtype choice does not matter"
> It is enough for coordinates, but an `int64` quality or one-hot matrix costs 8 times the memory of `uint8`, and mixing `uint64` with `int64` silently produces `float64`.

> [!warning] "Python integers are slow because they overflow into big numbers"
> Python integers never overflow; they are slow in loops because each is a separate boxed object ([[Python Object Model]]). Exactness is their advantage, which is why `wrap` above can check NumPy results.

## Exercises

> [!question] Exercise 1 (L1)
> Give the range of `uint8`, `int16`, `uint32` and `int64` from $w$ alone, and choose a dtype for: (a) a per-base depth track of amplicon data where depth reaches $2 \times 10^5$; (b) 0-based starts of BED intervals on one chromosome; (c) the sum of all counts of a $60\,000 \times 1000$ count matrix with cells up to $10^5$.

> [!success]- Solution
> $[0, 2^8 - 1] = [0, 255]$; $[-2^{15}, 2^{15} - 1] = [-32\,768, 32\,767]$; $[0, 2^{32} - 1]$; $[-2^{63}, 2^{63} - 1]$. (a) `uint32` (or `int32`): $2 \times 10^5 > 65\,535$ rules out 16 bits. (b) `int32` for storage, below the $2^{31} - 1$ BAM limit; cast to `int64` before arithmetic across chromosomes. (c) The total can reach $6 \times 10^7 \times 10^5 = 6 \times 10^{12} > 2^{31}$: accumulate in `int64` (NumPy's `sum` does for small types, but say so explicitly with `dtype=np.int64`).

> [!question] Exercise 2 (L1)
> Predict, then check: `np.array([200], dtype=np.uint8) + np.array([100], dtype=np.uint8)`, `200 + 100`, `np.array([-128], dtype=np.int8) * -1`, `np.array([10], dtype=np.uint8) - np.array([20], dtype=np.uint8)`.

> [!success]- Solution
> `[44]` ($300 - 256$), `300` (Python), `[-128]` ($128$ does not fit; $128 - 256 = -128$), `[246]` ($-10 + 256$). Output: `[44] 300 [-128] [246]`.

> [!question] Exercise 3 (L2)
> Write $-100$ as an 8-bit two's complement pattern by hand, using "flip the bits and add 1", and check that it equals unsigned $256 - 100$.

> [!success]- Solution
> $100 = 01100100_2$; flipped: $10011011_2$; plus 1: $10011100_2$ = `0x9c` = 156 unsigned, and $156 = 256 - 100$, as $T(b) = U(b) - 2^8$ predicts. Python: `(-100).to_bytes(1, "big", signed=True).hex()` gives `9c`, and `format(-100 & 0xFF, "08b")` gives `10011100`.

> [!question] Exercise 4 (L2, Python)
> Adding 1000 reads to a `uint16` depth track that already holds 65,000 at one position wraps. Write `checked_add(a, b)` that computes in `int64` and raises `OverflowError` if any result does not fit `a.dtype`.

> [!success]- Solution
> ```python
> def checked_add(a: np.ndarray, b) -> np.ndarray:
>     """Add in int64, refuse results that do not fit a's dtype."""
>     info = np.iinfo(a.dtype)
>     wide = a.astype(np.int64) + b
>     if (wide > info.max).any() or (wide < info.min).any():
>         raise OverflowError(f"result does not fit {a.dtype}")
>     return wide.astype(a.dtype)
>
>
> depth = np.array([65_000, 1_000], dtype=np.uint16)
> print(depth + np.uint16(1000))
> try:
>     checked_add(depth, 1000)
> except OverflowError as err:
>     print("OverflowError:", err)
> print(checked_add(np.array([10, 20], dtype=np.uint16), 5))
> ```
> ```text
> [ 464 2000]
> OverflowError: result does not fit uint16
> [15 25]
> ```
> The plain sum returns 464 ($66\,000 - 65\,536$) without complaint. `int64` is wide enough for any sum of two values of 32 bits or less, so the check is exact.

> [!question] Exercise 5 (L3, Python)
> Using `kmer_codes`, `revcomp_code` and `decode` from Advanced, count canonical 3-mers of the invented sequence `ACGGATTCGAATTCTG` as integers, check that its reverse complement gives the same counts, and state the largest $k$ a `uint64` code supports.

> [!success]- Solution
> ```python
> from collections import Counter
>
>
> def canonical_counts(seq: str, k: int) -> Counter:
>     return Counter(min(c, revcomp_code(c, k)) for c in kmer_codes(seq, k))
>
>
> s = "ACGGATTCGAATTCTG"                                         # invented
> rc = s.translate(str.maketrans("ACGT", "TGCA"))[::-1]
> cc = canonical_counts(s, 3)
> print(cc == canonical_counts(rc, 3), sorted((decode(c, 3), n) for c, n in cc.items())[:4])
> print(2 * 32, 4**32 == 2**64, 4**33 > np.iinfo(np.uint64).max)
> ```
> ```text
> True [('AAT', 3), ('ACG', 1), ('AGA', 1), ('ATC', 1)]
> 64 True True
> ```
> Same counts as the string version in [[DNA#Exercises]] (AAT appears 3 times), with integers instead of strings as keys. $k = 32$ uses all 64 bits; $4^{33}$ codes do not fit.

> [!question] Exercise 6 (L3, Python)
> Write `encode_bam_seq` and `decode_bam_seq` for BAM's 4-bit sequence encoding (codes 0 to 15 index `=ACMGRSVTWYHKDBN`, high nibble first).[^sam] Encode `ACGTN`, then decode the bytes `84 21` as a 4-base read.

> [!success]- Solution
> ```python
> NIBBLE = "=ACMGRSVTWYHKDBN"                                    # BAM 4-bit base codes, 0 to 15
>
>
> def decode_bam_seq(packed: bytes, length: int) -> str:
>     """High nibble first; an odd-length read leaves the last low nibble unused."""
>     out = []
>     for byte in packed:
>         out += [NIBBLE[byte >> 4], NIBBLE[byte & 0x0F]]
>     return "".join(out[:length])
>
>
> def encode_bam_seq(seq: str) -> bytes:
>     codes = [NIBBLE.index(b) for b in seq] + [0] * (len(seq) % 2)
>     return bytes((codes[i] << 4) | codes[i + 1] for i in range(0, len(codes), 2))
>
>
> packed = encode_bam_seq("ACGTN")
> print(packed.hex(), len(packed), decode_bam_seq(packed, 5), decode_bam_seq(bytes.fromhex("8421"), 4))
> ```
> ```text
> 1248f0 3 ACGTN TGCA
> ```
> A=1, C=2, G=4, T=8, N=15: five bases fit in 3 bytes instead of 5. The length must be stored separately (BAM keeps it in its own field), otherwise the padding nibble of an odd-length read would decode as `=`.

## Mastery checklist

- [ ] 1 Recognized: I can give the range of any `intN` and `uintN` dtype and say that Python integers never overflow.
- [ ] 2 Understood: I can explain two's complement, why arithmetic wraps modulo $2^w$, and where NumPy wraps, warns or raises.
- [ ] 3 Practiced: I can choose dtypes for bases, depths, coordinates and counts, write overflow checks, and encode $k$-mers as integers.
- [ ] 4 Applied: [[09-genome-browser]] stores coordinates in deliberate dtypes that survive a real human assembly, and [[07-evolution-simulator]] counts alleles without overflow.
- [ ] 5 Explained: I can teach the wheel, the unsigned-difference and `uint64`/`int64` traps, and how binary formats such as BAM lay out integers.

## References

[^types]: [[Python Documentation]], 3.13, Library Reference, "Built-in Types": integers have unlimited precision; bitwise operations on negative numbers use their two's complement; `int.to_bytes` and `int.from_bytes` (`signed=True` uses two's complement, `OverflowError` when the integer does not fit).
[^mck4]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 4 "NumPy Basics: Arrays and Vectorized Computation": NumPy data types (signed and unsigned 8-, 16-, 32- and 64-bit integers) and `astype`.
[^mck7]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 7 "Data Cleaning and Preparation": missing data and extension data types such as `Int64`.
[^sam]: [[GA4GH hts-specs]], `SAMv1`: BAM encoding (little-endian integers, 32-bit `pos`, 4-bit `seq` codes `=ACMGRSVTWYHKDBN`, high nibble first), `@SQ` `LN` range $[1, 2^{31} - 1]$.
[^csi]: [[GA4GH hts-specs]], `SAMv1` (BAI binning up to $2^{29}$) and `CSIv1` (configurable minimum shift and depth for longer references).
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science*: T2T-CHM13, about 3.055 Gbp.
