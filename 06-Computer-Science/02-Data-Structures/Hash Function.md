---
aliases:
  - Hashing
  - Hash Code
  - Universal Hashing
  - Fonction de hachage
tags:
  - type/concept
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Modular Arithmetic]]"
  - "[[Integer Representation]]"
  - "[[Expected Value]]"
  - "[[String]]"
related:
  - "[[Hash Table]]"
  - "[[Rolling Hash]]"
  - "[[MinHash]]"
  - "[[Bloom Filter]]"
  - "[[Data Integrity]]"
  - "[[K-mer]]"
projects:
  - "[[05-sequence-search]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Information Theory, Inference, and Learning Algorithms (MacKay)]]"
  - "[[Bioinformatics Data Skills (Buffalo)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Python for Data Analysis (McKinney)]]"
---

# Hash Function

> [!abstract]
> A hash function turns a key (a k-mer, a read name, a whole file) into a small number. Hash tables need it deterministic, fast and evenly spread; checksums need it to change when data are damaged; cryptographic hashes need it impossible to fool on purpose. Universal hashing draws the function at random, so that no input is bad on average.

## Definition

A **hash function** maps keys from a universe $U$, usually far larger than the table, to a range $\{0, 1, \dots, m - 1\}$; two keys with the same value **collide**. A good hash function for a table is **deterministic** (a key always gets the same value), approximately **uniform** (each key is equally likely to land in any of the $m$ slots, independently of where other keys land, the assumption under which hashing is analyzed) and **fast** to compute.[^clrs11] Longer hash values, or **hash codes**, also serve to retrieve, compare and authenticate data.[^mackay]

## Why it matters

- **Every `dict`, `set` and `Counter`** of k-mers, codons or read names relies on one ([[Hash Table]]); only hashable, in practice immutable, objects can be keys.[^mck3]
- **Sketches of genomes** select or compare k-mers by hash value ([[MinHash]], [[Minimizer]], [[Bloom Filter]]): the function and its seed must be fixed and shared, or the sketches of two genomes are not comparable. Python's built-in `hash` of a string is not (Core).
- **Data integrity.** Downloaded sequencing files are checked against published MD5 or SHA checksums with `md5sum` or `shasum` ([[Data Integrity]]).[^buffalo]
- **Collisions are certain beyond a size**, so the width of a hash used as an identifier must be planned (Advanced).[^mackay]

## Core (L1)

| Requirement | Why | Failure |
|---|---|---|
| Deterministic | a key must find the slot it was stored in | mutating an object after using it as a key |
| Uniform | expected $O(1)$ operations need keys spread evenly | `k % 1024` on keys that are multiples of 1024 (below) |
| Fast | computed on every operation | hashing a whole read when its 21-mer is the key |

**Constructions.**[^clrs11]
- **Integers.** Division, $h(k) = k \bmod m$: avoid $m = 2^p$, which keeps only the $p$ low-order bits of $k$. Multiply-shift, for $m = 2^\ell$ and $w$-bit words: $h(k) = \lfloor (a k \bmod 2^w) / 2^{w - \ell} \rfloor$ with a fixed odd $a$, which keeps the high bits of the product, and these depend on all bits of $k$.
- **Strings.** Polynomial hashing, $h(s) = \left(\sum_{i=0}^{n-1} s_i B^{\,n-1-i}\right) \bmod p$, computed by Horner's rule; updating it as a window slides is a [[Rolling Hash]].
- **k-mers.** Read as a base-4 number (A = 0, C = 1, G = 2, T = 3), a k-mer maps injectively to $\{0, \dots, 4^k - 1\}$: a collision-free index into an array of $4^k$ counters for small $k$.[^compeau] Since $2k$ bits suffice, any $k \le 32$ fits in a 64-bit word.

```python
import os, subprocess, sys
from collections import Counter

def run_hash(seed=None):                        # hash('ACGTACGT') in a fresh interpreter
    env = {key: v for key, v in os.environ.items() if key != "PYTHONHASHSEED"}
    if seed is not None:
        env["PYTHONHASHSEED"] = seed
    cmd = [sys.executable, "-c", "print(hash('ACGTACGT'))"]
    return subprocess.run(cmd, capture_output=True, text=True, env=env).stdout
print(run_hash("1") == run_hash("1"), run_hash("1") == run_hash("2"), run_hash() == run_hash())
print(hash(42), hash(1) == hash(1.0) == hash(True), sys.hash_info.algorithm)

DIGITS = str.maketrans("ACGT", "0123")
def kmer_code(kmer: str) -> int:                # base-4 reading: injective on the 4**k k-mers
    return int(kmer.translate(DIGITS), 4)
def poly_hash(s: bytes, base: int = 257, p: int = (1 << 61) - 1) -> int:
    h = 0
    for c in s:                                 # Horner: ((c0 * B + c1) * B + c2) * B + c3
        h = (h * base + c) % p
    return h
print(kmer_code("AAAA"), kmer_code("ACGT"), kmer_code("TTTT"), poly_hash(b"ACGT"))

m, bits = 1024, 10
starts = range(0, 10_000_000, 1024)             # starts of 1-kb bins on a toy chromosome (keys)
A = 0x9E3779B97F4A7C15                          # a fixed odd 64-bit multiplier
def division(k):
    return k % m
def multiply_shift(k):
    return ((A * k) & (2**64 - 1)) >> (64 - bits)
for h in (division, multiply_shift):
    load = Counter(h(k) for k in starts)
    print(h.__name__, len(starts), "keys,", len(load), "slots used, fullest:", max(load.values()))
```

```text
True False False
42 True siphash13
0 27 255 1107792159
division 9766 keys, 1 slots used, fullest: 9766
multiply_shift 9766 keys, 1024 slots used, fullest: 12
```

What the output shows: within a fixed seed, `hash` is deterministic, but string hashes change between interpreter runs unless `PYTHONHASHSEED` is set, so they must never be stored or shared. Equal numbers hash equally across types, and an integer such as 42 hashes to itself, so `hash(k) % 1024` on integer keys would inherit the weakness of the division method. Bin starts, all multiples of 1024, land in a single slot with the division method; multiply-shift spreads them almost perfectly.

**Three kinds of hash, three contracts.**

| Kind | Examples | Designed for | Not designed for |
|---|---|---|---|
| Table hash | `hash`, multiply-shift, polynomial | spreading keys over slots, fast | resisting deliberately chosen keys, unless randomized |
| Checksum | CRC-32 (`zlib.crc32`) | detecting accidental differences between copies[^mackay] | deliberate tampering |
| Cryptographic hash | SHA-256, MD5 (`hashlib`) | making it hard to find another input with the same digest: tamper detection[^mackay] | speed in a hash table |

```python
import gzip, hashlib, struct, zlib
data = b"ACGT" * 1000
flip = bytes([data[0] ^ 1]) + data[1:]          # one bit changed: 'A' (0x41) becomes '@' (0x40)
print(hex(zlib.crc32(data)), hex(zlib.crc32(flip)))
print(hashlib.md5(data).hexdigest()[:16], hashlib.md5(flip).hexdigest()[:16], hashlib.sha256(data).hexdigest()[:16])
crc, size = struct.unpack("<II", gzip.compress(data)[-8:])   # gzip trailer: CRC-32 and length
print(crc == zlib.crc32(data), size == len(data))
```

```text
0x61b25a7c 0xa11159b9
2f1978cf2f926307 df7f01fdf70594c0 e746b654ea68be51
True True
```

A single flipped bit changes every digest. The last line shows that a gzip file (such as a `.fastq.gz`) ends with the CRC-32 and the length of its uncompressed content: decompression checks itself against accidental damage, while the archive's published MD5 or SHA digest checks the whole download.[^buffalo]

## Deeper (L2)

**Why randomize.** For any fixed $h$ and $|U| > (n - 1)m$, the pigeonhole principle gives $n$ keys that share one slot, and an adversary, or merely structured data such as the bin starts above, can produce them. Choosing $h$ at random from a suitable family, independently of the keys, makes the expected cost good for every input.[^clrs11]

**Universal family.** A family $\mathcal{H}$ of functions $U \to \{0, \dots, m-1\}$ is **universal** if, for every pair of distinct keys $x \neq y$, at most $|\mathcal{H}|/m$ functions make them collide: $\Pr_{h \in \mathcal{H}}[h(x) = h(y)] \le 1/m$.[^clrs11][^6006-l4] With a prime $p$ larger than every key, the family

$$h_{ab}(k) = \big((a k + b) \bmod p\big) \bmod m, \qquad a \in \{1, \dots, p - 1\},\ b \in \{0, \dots, p - 1\}$$

is universal.[^clrs11][^6006-l4] Proof sketch: for $x \neq y$, the map $(a, b) \mapsto (r, s) = (ax + b \bmod p,\ ay + b \bmod p)$ is a bijection onto the pairs with $r \neq s$ (because $p$ is prime and $a \neq 0$); a collision needs $r \equiv s \pmod m$, and for each $r$ at most $(p - 1)/m$ values $s \neq r$ qualify, so at most $p(p - 1)/m = |\mathcal{H}|/m$ functions collide.

**Consequence.** With chaining, the expected number of other keys in the slot of $x$ is $\sum_{y \neq x} \Pr[h(x) = h(y)] \le (n - 1)/m$ by linearity of expectation, so each operation costs $O(1 + n/m)$ in expectation, whatever the keys ([[Hash Table]]).

```python
from itertools import combinations
p, m = 31, 4
family = [(a, b) for a in range(1, p) for b in range(p)]
def hab(a, b, k):
    return ((a * k + b) % p) % m
worst = max(sum(hab(a, b, x) == hab(a, b, y) for a, b in family) for x, y in combinations(range(p), 2))
print(len(family), worst, round(worst / len(family), 4), 1 / m)
```

```text
930 210 0.2258 0.25
```

Over all 465 pairs of keys and all 930 functions, the worst collision probability is $0.2258 \le 1/m$.

## Advanced (L3)

- **Birthday bound.** With $n$ keys hashed uniformly into $M$ values, the expected number of colliding pairs is $\binom{n}{2}/M$, and $P(\text{some collision}) \approx 1 - e^{-n(n-1)/(2M)}$, which reaches 50% near $n \approx 1.18\sqrt{M}$. MacKay uses this birthday problem to choose the length of hash codes.[^mackay] A 32-bit hash already gives about a thousand colliding pairs among 3 million distinct k-mers; a 64-bit hash stays below 0.03 expected pairs up to $10^9$ (Worked example).
- **Reproducible sketches.** Tools that compare sketches built on different machines must fix the hash function and its seed; a salted, per-process hash such as Python's `hash` of a `str` makes results irreproducible ([[MinHash]], [[Reproducibility]]).
- **Perfect hashing for static sets.** When the key set is fixed and small, a collision-free mapping can be built once: the 64 codons map to $\{0, \dots, 63\}$ by base-4 reading, which turns a codon table into a 64-entry array ([[Genetic Code]]).

## Mathematical representation

- $h : U \to [m] = \{0, \dots, m - 1\}$; **uniform hashing**: $\Pr[h(x) = i] = 1/m$ for each slot $i$, independently for distinct keys.
- **Universality**: $\forall x \neq y,\ \Pr_{h \in \mathcal{H}}[h(x) = h(y)] \le 1/m$. Then for $C_x$, the number of keys colliding with $x$ among $n$ stored keys, $E[C_x] \le (n - 1)/m$.
- **Birthday**: $P(\text{no collision}) = \prod_{i=0}^{n-1} \left(1 - \frac{i}{M}\right) \le \exp\!\left(-\frac{n(n-1)}{2M}\right)$, using $1 - x \le e^{-x}$; expected colliding pairs $\binom{n}{2}/M$.

## Computational representation

The code above uses Python's built-in `hash` (salted for `str` and `bytes`, identity-like for small `int`), integer arithmetic for multiply-shift and polynomial hashes, `zlib.crc32` for checksums and `hashlib` for cryptographic digests. Custom tables and sketches should use an explicit, seeded function rather than `hash`.

## Worked example

> [!example] Is a 32-bit hash a safe identifier for k-mers?
> 1. **Model**: $n$ distinct k-mers hashed uniformly into $M = 2^{b}$ values; expected colliding pairs $\approx n^2 / (2M)$.
> 2. **Compute**:
> ```python
> import math
> for b in (32, 64):
>     M = 2.0 ** b
>     for n in (10**6, 10**9):
>         pairs = n * (n - 1) / (2 * M)
>         print(b, f"{n:.0e}", f"{pairs:.3g}", f"{-math.expm1(-pairs):.3g}")
>     print(b, "50% at n =", f"{math.sqrt(2 * M * math.log(2)):.4g}")
> # 32 1e+06 116 1
> # 32 1e+09 1.16e+08 1
> # 32 50% at n = 7.716e+04
> # 64 1e+06 2.71e-08 2.71e-08
> # 64 1e+09 0.0271 0.0267
> # 64 50% at n = 5.057e+09
> ```
> 3. **Read**: at 32 bits, a collision is likely from about 77,000 k-mers on, and a million k-mers give 116 colliding pairs. At 64 bits, $10^9$ k-mers give a 2.7% chance of any collision.
> 4. **Decide**: a 32-bit hash is fine to *bucket* k-mers (the table compares the actual keys), never to *identify* them. As an identifier, use 64 bits up to about $10^9$ k-mers, or the exact 2-bit encoding when $k \le 32$.

## Common misconceptions

> [!warning] "`hash()` gives the same value on every run"
> Not for `str` and `bytes`: they are salted per process (shown above). Persisted or shared hash values need an explicit function such as `hashlib` digests or a seeded hash.

> [!warning] "A good hash function has no collisions"
> When $|U| > m$, collisions are unavoidable (pigeonhole). The goal is an even spread, with collisions resolved by the table or made negligible by enough bits.

> [!warning] "A matching checksum proves a file is authentic"
> It shows that the file matches the reference digest. Checksums such as CRC-32 catch accidental damage only; against deliberate tampering you need a cryptographic hash, and the reference digest itself must come from a trusted source.[^mackay]

## Exercises

> [!question] Exercise 1 (L1)
> Compute the base-4 code of `GATTACA` (A = 0, C = 1, G = 2, T = 3). Why is this map injective, and up to which $k$ does it fit in a 64-bit integer?

> [!success]- Solution
> $2 \cdot 4^6 + 0 \cdot 4^5 + 3 \cdot 4^4 + 3 \cdot 4^3 + 0 \cdot 4^2 + 1 \cdot 4 + 0 = 8192 + 768 + 192 + 4 = 9156$, as `int("2033010", 4)` confirms. Base-4 representations of numbers below $4^k$ with exactly $k$ digits are unique, so distinct k-mers get distinct codes. Each base needs 2 bits: $2k \le 64$ gives $k \le 32$.

> [!question] Exercise 2 (L1)
> Which kind of hash fits each use: (a) a `dict` of read identifiers; (b) checking a downloaded `.fastq.gz` against the archive's published digest; (c) detecting a corrupted gzip block during decompression; (d) proving to a reviewer that a released dataset was not altered by a third party?

> [!success]- Solution
> (a) A table hash. (b) A digest used as a checksum (MD5 or SHA), compared with the published value. (c) The CRC-32 checksum stored in the gzip file. (d) A cryptographic hash (SHA-256), with the reference digest published through a trusted channel.

> [!question] Exercise 3 (L2)
> Prove that with a universal family and chaining, the expected number of other stored keys in the slot of a key $x$ is at most $(n - 1)/m$.

> [!success]- Solution
> Let $I_y = [h(x) = h(y)]$ for each stored key $y \neq x$. The count is $C_x = \sum_{y \neq x} I_y$, and by linearity of expectation $E[C_x] = \sum_{y \neq x} \Pr[h(x) = h(y)] \le (n - 1) \cdot \frac{1}{m}$. No independence between the $I_y$ is needed.

> [!question] Exercise 4 (L2, Python)
> Allow $a = 0$ in the family $h_{ab}$ ($p = 31$, $m = 4$). Is it still universal? Explain the result.

> [!success]- Solution
> ```python
> with_zero = [(a, b) for a in range(p) for b in range(p)]
> worst = max(sum(hab(a, b, x) == hab(a, b, y) for a, b in with_zero) for x, y in combinations(range(p), 2))
> print(round(worst / len(with_zero), 4), 1 / m)
> # 0.2508 0.25
> ```
> No: the 31 functions with $a = 0$ are constant and make every pair collide, which pushes the worst pair to $(210 + 31)/961 = 0.2508 > 1/4$.

> [!question] Exercise 5 (L3)
> A pangenome index will hash $10^{10}$ distinct k-mers to fixed-width identifiers. How many colliding pairs do you expect with 64 bits and with 128 bits? How many bits keep the expectation below 0.01?

> [!success]- Solution
> Expected pairs $\approx n^2 / 2^{b+1}$: $10^{20} / 2^{65} \approx 2.71$ at 64 bits, $1.5 \times 10^{-19}$ at 128 bits. Requiring $n^2 / 2^{b+1} \le 0.01$ gives $2^b \ge 10^{20} / 0.02$, so $b \ge 72.1$: 73 bits, in practice 128. Below $k = 32$, the exact 2-bit encoding avoids the question entirely.

## Mastery checklist

- [ ] 1 Recognized: I can state the three requirements of a table hash and name a checksum and a cryptographic hash.
- [ ] 2 Understood: I can explain why `k mod 2^p` fails on structured keys and why Python's string hash is salted per process.
- [ ] 3 Practiced: I can implement multiply-shift, polynomial and base-4 k-mer hashes, and prove the universality bound.
- [ ] 4 Applied: in [[05-sequence-search]], I chose an explicit, seeded hash for k-mers and verified downloaded data against published digests.
- [ ] 5 Explained: I can teach universal hashing, the birthday bound for identifier width, and the difference between checksums and cryptographic hashes.

## References

[^clrs11]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 11 "Hash Tables": hash functions (division and multiplicative methods), uniform hashing, random and universal hashing, the $((ak + b) \bmod p) \bmod m$ family.
[^6006-l4]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, lecture 4 "Hashing": universal hash families and expected chain length.
[^mackay]: [[Information Theory, Inference, and Learning Algorithms (MacKay)]], ch. 12 "Hash Codes: Codes for Efficient Information Retrieval": hash codes, collisions and the birthday problem, error detection and tamper detection.
[^buffalo]: [[Bioinformatics Data Skills (Buffalo)]], chapter "Bioinformatics Data": checking data integrity with MD5 and SHA checksums.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], 3rd ed., chapter "Where in the Genome Does DNA Replication Begin?": k-mers numbered in base 4 to index a frequency array.
[^mck3]: [[Python for Data Analysis (McKinney)]], 3rd ed. (2022), ch. 3 "Built-In Data Structures, Functions, and Files": hashability of dictionary keys and the `hash` function.
