---
aliases:
  - Counting Sort
  - LSD Radix Sort
  - MSD Radix Sort
  - Linear-Time Sorting
  - Integer Sorting
  - Tri par base
  - Tri par dénombrement
tags:
  - type/algorithm
  - domain/computer-science
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Sorting]]"
  - "[[Big O Notation]]"
  - "[[Array]]"
  - "[[Loop Invariant]]"
  - "[[K-mer]]"
related:
  - "[[Divide and Conquer]]"
  - "[[Master Theorem]]"
  - "[[Hash Table]]"
  - "[[Suffix Array]]"
  - "[[Suffix Array Construction]]"
  - "[[Burrows-Wheeler Transform]]"
  - "[[K-mer Spectrum]]"
  - "[[Integer Representation]]"
  - "[[Model of Computation]]"
projects:
  - "[[05-sequence-search]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[MIT 6.006 - Introduction to Algorithms]]"
  - "[[Kärkkäinen 2003 - Simple Linear Work Suffix Array Construction]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
---

# Radix Sort

> [!abstract]
> Radix sort orders keys of $d$ digits in base $\sigma$ with $d$ stable counting-sort passes, least significant digit first, in $\Theta(d(n + \sigma))$ time: linear for short keys over a small alphabet such as 2-bit-encoded k-mers, because it uses digits as array indices instead of comparing keys, which puts it outside the $\Omega(n \log n)$ comparison bound.

## Problem

- **Input**: $n$ records whose keys are integers in $\{0, \dots, \sigma^d - 1\}$, read as $d$ digits in base $\sigma$ (equivalently, strings of length $d$ over an alphabet of $\sigma$ letters).
- **Output**: the records in non-decreasing key order, **stably**: records with equal keys keep their input order.
- **Biological use**: DNA is the small-alphabet case. A k-mer encoded with 2 bits per base is an integer whose numeric order is the lexicographic order ([[K-mer#Mathematical representation]]), so the k-mers of a genome can be sorted in linear time, then counted as runs of equal codes ([[K-mer Spectrum]]) or stored as a sorted index searched by [[Binary Search]] ([[05-sequence-search]]). A [[Suffix Array]] is the list of a genome's suffixes in sorted order;[^compeau] its construction algorithms sort pairs or triples of integer ranks, by prefix doubling (Exercise 4) or by the skew algorithm, whose only nontrivial subroutine is integer sorting[^karkkainen] ([[Suffix Array Construction]], [[Burrows-Wheeler Transform]]).

## Intuition

- **Counting sort.** With keys in $\{0, \dots, \sigma - 1\}$: count how many records carry each key; prefix sums of the counts give the block where each key starts in the output; scan the input and drop each record into the next free slot of its block. No two keys are ever compared.[^clrs8]
- **Radix sort.** Sort by the last digit, then stably by the one before, and so on up to the first. When two keys tie on the current digit, stability keeps them in the order the less significant digits already gave them.[^clrs8][^6006-l5] It is the "secondary key first, then primary key" trick of [[Sorting#Exercises]] (Exercise 3), applied digit by digit.
- **Why the lower bound does not apply.** $\Omega(n \log n)$ holds for algorithms that learn about keys only by comparing pairs ([[Sorting#Mathematical formulation]]). Counting sort uses a key as an array index, a different operation of the word-RAM ([[Model of Computation]]).[^clrs8]

## Mathematical formulation

**Counting sort.** For keys $k_1, \dots, k_n \in \{0, \dots, \sigma - 1\}$, let $C(v) = |\{i : k_i < v\}|$ (exclusive prefix sums of the counts). Record $i$ goes to the 0-based position

$$\pi(i) = C(k_i) + |\{j < i : k_j = k_i\}|.$$

The map $\pi$ is a bijection onto $\{0, \dots, n - 1\}$ that sends smaller keys to smaller positions and keeps the input order among equal keys: a stable sort, in time $\Theta(n + \sigma)$ (a pass to count, a pass over the $\sigma$ counters, a pass to place) and extra space $\Theta(n + \sigma)$.

**LSD radix sort is correct.** Write a key as digits $x_d \dots x_2 x_1$ (most significant first) and run stable passes on digits $1, 2, \dots, d$. **Invariant** ([[Loop Invariant]]): after pass $t$, the records are sorted by the number $x_t \dots x_1$ formed by their last $t$ digits.

- *Initialization*: after pass 1 they are sorted by $x_1$.
- *Maintenance*: take records $x$ and $y$ after pass $t$. If $x_t \neq y_t$, pass $t$ ordered them by $x_t$, which decides the order of their last $t$ digits. If $x_t = y_t$, stability kept the order they had after pass $t - 1$, which by the invariant is the order of their last $t - 1$ digits, hence of their last $t$.
- *Termination*: after pass $d$, the records are sorted by the whole key.

Stability is used in the maintenance step and nowhere else; Exercise 1 breaks it.

**Cost and digit width.** $d$ passes of counting sort cost $\Theta(d(n + \sigma))$. For $b$-bit integers cut into $r$-bit digits, $d = \lceil b/r \rceil$ and $\sigma = 2^r$:[^clrs8]

$$T(n) = \Theta\!\left(\frac{b}{r}\,\left(n + 2^r\right)\right).$$

Wider digits mean fewer passes until the $2^r$ counters outweigh the $n$ records, so the best width is near $r \approx \lg n$, giving $\Theta(bn / \lg n)$. Keys bounded by a polynomial in $n$, $u = n^{c}$, have $b = c \lg n$ bits and sort in $\Theta(cn)$: linear. MIT 6.006 states the same result as $O(n + n \log_n u)$ for keys below $u$.[^6006-l5]

**DNA keys.** With $e(A) = 0$, $e(C) = 1$, $e(G) = 2$, $e(T) = 3$, the code $\mathrm{idx}(w) = \sum_{j=1}^{k} e(w_j)\,4^{k-j}$ is an order-preserving bijection $\{A, C, G, T\}^k \to \{0, \dots, 4^k - 1\}$ ([[K-mer#Mathematical representation]]): $b = 2k$ bits, $k$ passes with one base per pass, $\lceil k/4 \rceil$ passes with 8-bit digits.

## Algorithm

```text
COUNTING-SORT(A, key, σ)                       RADIX-SORT(A, b, r)        // keys < 2^b
  count[0..σ-1] = 0                              for shift = 0, r, 2r, ... while shift < b
  for each record x in A                             A = COUNTING-SORT(A, x -> (x >> shift) mod 2^r, 2^r)
      count[key(x)] += 1                         return A
  start = exclusive prefix sums of count
  for each record x in A, left to right         // left to right: stable
      out[start[key(x)]] = x
      start[key(x)] += 1
  return out
```

## Complexity

| Algorithm | Time | Extra space | Stable | Keys |
|---|---|---|---|---|
| Counting sort | $\Theta(n + \sigma)$ | $\Theta(n + \sigma)$ | yes | integers in $[0, \sigma)$ |
| LSD radix sort | $\Theta(d(n + \sigma))$ | $\Theta(n + \sigma)$ | yes | $d$ digits in base $\sigma$ |
| k-mers, 8-bit digits | $\Theta(\lceil k/4 \rceil (n + 256))$ | $\Theta(n)$ | yes | $2k$-bit codes |
| Comparison sorts ([[Sorting]]) | $\Omega(n \log n)$ comparisons | $O(1)$ to $\Theta(n)$ | depends | any total order |

## Implementation

Counting sort, LSD radix sort on integers, and k-mer counting by sorting 2-bit codes, tested against `sorted()` and `collections.Counter`:

```python
import random
import time
from collections import Counter

def counting_sort(records: list, key, sigma: int) -> list:
    """Stable sort of records by key(record) in range(sigma), in Theta(n + sigma)."""
    count = [0] * sigma
    for r in records:                          # 1. histogram of key values
        count[key(r)] += 1
    start, total = [0] * sigma, 0
    for v in range(sigma):                     # 2. exclusive prefix sums: first slot of value v
        start[v], total = total, total + count[v]
    out = [None] * len(records)
    for r in records:                          # 3. place in input order: stability
        v = key(r)
        out[start[v]] = r
        start[v] += 1
    return out

def radix_sort(keys: list, bits: int, r: int = 8) -> list:
    """LSD radix sort of integers in [0, 2**bits): ceil(bits / r) stable passes of r bits."""
    mask = (1 << r) - 1
    for shift in range(0, bits, r):            # least significant digit first
        keys = counting_sort(keys, lambda x: (x >> shift) & mask, 1 << r)
    return keys

CODE = {"A": 0, "C": 1, "G": 2, "T": 3}        # order-preserving 2-bit code

def kmer_codes(seq: str, k: int) -> list:
    """2-bit codes of the n - k + 1 k-mers of an ACGT string, updated in O(1) per step."""
    mask, x, codes = (1 << 2 * k) - 1, 0, []
    for i, base in enumerate(seq):
        x = ((x << 2) | CODE[base]) & mask     # shift in the new base, drop the oldest
        if i >= k - 1:
            codes.append(x)
    return codes

def decode(x: int, k: int) -> str:
    return "".join("ACGT"[(x >> 2 * (k - 1 - i)) & 3] for i in range(k))

def kmer_counts_by_sorting(seq: str, k: int) -> list:
    """(k-mer, count) in lexicographic order: radix sort the codes, then count runs."""
    runs = []
    for x in radix_sort(kmer_codes(seq, k), 2 * k):
        if runs and runs[-1][0] == x:
            runs[-1][1] += 1
        else:
            runs.append([x, 1])
    return [(decode(x, k), c) for x, c in runs]

rng = random.Random(3)
for _ in range(200):                           # oracles: sorted() and Counter
    keys = [rng.randrange(2 ** 20) for _ in range(rng.randint(0, 300))]
    assert radix_sort(keys, 20, r=rng.choice([1, 2, 4, 8, 11])) == sorted(keys)
    seq = "".join(rng.choices("ACGT", k=rng.randint(5, 200)))
    k = rng.randint(1, min(12, len(seq)))
    assert kmer_counts_by_sorting(seq, k) == sorted(Counter(seq[i:i + k] for i in range(len(seq) - k + 1)).items())

print(kmer_counts_by_sorting("GATTACAGATTACA", 3)[:5])   # invented toy read

n, k = 200_000, 31
codes = kmer_codes("".join(rng.choices("ACGT", k=n + k - 1)), k)
for label, sort in [("radix, r = 8 bits", lambda: radix_sort(codes, 2 * k, 8)),
                    ("radix, r = 16 bits", lambda: radix_sort(codes, 2 * k, 16)),
                    ("sorted() built-in", lambda: sorted(codes))]:
    t0 = time.perf_counter()
    assert sort() == sorted(codes)
    print(f"{label:19} {time.perf_counter() - t0:.2f} s")
```

```text
[('ACA', 2), ('AGA', 1), ('ATT', 2), ('CAG', 1), ('GAT', 2)]
radix, r = 8 bits   0.51 s
radix, r = 16 bits  0.36 s
sorted() built-in   0.10 s
```

Reading the results (the 200 randomized tests passed silently; timings are indicative, CPython 3.11, one run):

- **Correctness**: radix sort agrees with `sorted()` for digit widths from 1 to 11 bits, and sort-then-count agrees with `Counter`, returning k-mers in lexicographic order because the 2-bit code preserves it.
- **Asymptotics are not timings.** On 200,000 codes of 31-mers (62 bits), 16-bit digits need 4 passes, about $4 \times 200{,}000$ digit steps, against roughly $n \lg n \approx 3.5 \times 10^6$ comparisons for a comparison sort; yet the built-in sort is several times faster (3.6 times in this run) than radix sort written as interpreted Python loops, because each Python-level step costs far more than one comparison inside the built-in. Linear-time sorting pays off in compiled or vectorized code, as in the inner loops of suffix-array construction, not as pure Python.
- **Digit width.** Halving the number of passes (8-bit to 16-bit digits) cut the time by about 30 %: the passes dominate while $2^r \ll n$.

## Worked example

> [!example] LSD radix sort of six 3-mers (invented): `GAT ACA TTG ACG GAA CAT`
> **Pass 1, third base.** Counts: A = 2 (ACA, GAA), C = 0, G = 2 (TTG, ACG), T = 2 (GAT, CAT). Exclusive prefix sums: blocks start at A = 0, C = 2, G = 2, T = 4. Placing in input order gives `ACA GAA TTG ACG GAT CAT`; passes 2 and 3 work the same way (output below).
>
> **Stability at work.** GAA and GAT tie on their first two bases; GAA comes first only because pass 1 put it first (third base A < T) and passes 2 and 3 kept that order.
> ```python
> kmers = ["GAT", "ACA", "TTG", "ACG", "GAA", "CAT"]       # invented 3-mers
> for position in (2, 1, 0):                                # last base first
>     kmers = counting_sort(kmers, lambda s: CODE[s[position]], 4)
>     print(f"after base {position + 1}:", " ".join(kmers))
> ```
> ```text
> after base 3: ACA GAA TTG ACG GAT CAT
> after base 2: GAA GAT CAT ACA ACG TTG
> after base 1: ACA ACG CAT GAA GAT TTG
> ```

## Limitations

> [!warning] Linear in $n$, but also linear in the key length
> The cost $\Theta(d(n + \sigma))$ is linear only for a fixed number of digits $d$. Sorting $n$ reads of length $L$ costs $\Theta(L(n + \sigma))$, linear in the input size; but sorting the $n$ suffixes of a genome digit by digit would cost $\Theta(n^2)$, since suffixes are up to $n$ letters long. Suffix sorting therefore sorts **ranks** of prefixes instead of letters (Exercise 4).

> [!warning] Memory and the word-RAM assumption
> Radix sort is not in place: each pass writes an output array of $n$ records and uses $2^r$ counters. Its linear bound assumes that extracting a digit costs $O(1)$, i.e. keys fit in machine words: a 31-mer needs 62 bits, a 33-mer no longer fits in 64 ([[Integer Representation]]).

> [!warning] LSD needs keys of equal length
> Strings of different lengths must be padded with a symbol smaller than every letter, as the "past the end" rank 0 does in Exercise 4. MSD radix sort handles variable-length keys naturally.

## Variants and successors

- **MSD radix sort**: split the records into $\sigma$ buckets by their first digit, then recurse into each bucket on the next digit, stopping when a bucket holds one record: a [[Divide and Conquer]] with $\sigma$ subproblems whose work depends on the prefixes needed to tell keys apart, natural for reads of different lengths.
- **Bucket sort**: for keys spread uniformly over an interval, distribute into $n$ buckets and sort each: expected linear time.[^clrs8]
- **Prefix doubling** for suffix arrays: ranks of the $2^h$-letter prefixes are refined by radix sorting the pairs (rank of $i$, rank of $i + 2^h$): $O(n)$ per round, at most $\lceil \lg n \rceil$ rounds, $O(n \log n)$ in all (Exercise 4).
- **The skew algorithm** sorts rank triples with radix sort and recurses on two thirds of the suffixes: linear overall[^karkkainen] ([[Master Theorem]], case 3).
- **Hashing instead of sorting**: a [[Hash Table]] counts k-mers in expected $O(1)$ each but returns them unordered; a sorted array of codes can be merged with another sorted array in linear time and searched by [[Binary Search]]. The choice depends on what is done with the counts.

## Exercises

> [!question] Exercise 1 (L2, Python)
> Replace the inner counting sort by a version that fills each block from its end while scanning the input forward (equal keys come out reversed), and run LSD radix sort on `AC AA CA CC`. Which step of the correctness proof fails? How can a block-from-the-end version be made stable?

> [!success]- Solution
> ```python
> def unstable_counting_sort(records, key, sigma):
>     """Same counts, but fills each block from its end: equal keys come out reversed."""
>     count = [0] * sigma
>     for r in records:
>         count[key(r)] += 1
>     end = [sum(count[:v + 1]) for v in range(sigma)]   # one past the last slot of value v
>     out = [None] * len(records)
>     for r in records:                           # forward scan, filling blocks backwards
>         end[key(r)] -= 1
>         out[end[key(r)]] = r
>     return out
>
> words = ["AC", "AA", "CA", "CC"]
> for inner in (counting_sort, unstable_counting_sort):
>     w = words
>     for position in (1, 0):
>         w = inner(w, lambda s: CODE[s[position]], 4)
>     print(inner.__name__, w)
> ```
> Output: `counting_sort ['AA', 'AC', 'CA', 'CC']`, then `unstable_counting_sort ['AC', 'AA', 'CC', 'CA']`. The maintenance step fails: AA and AC tie on the first letter, and the second pass reverses the order the first pass had established. Scanning the input **backwards** while filling blocks from their ends restores stability (the last record with a key takes the last slot of its block), which is the textbook formulation.[^clrs8]

> [!question] Exercise 2 (L2, Python)
> You must sort $n = 10^8$ codes of 31-mers (62 bits). Compare digit widths $r = 2, 8, 16, 22, 31$ by the cost model $\lceil 62/r \rceil (n + 2^r)$. Which is best, and what rule does it illustrate?

> [!success]- Solution
> ```python
> n = 10 ** 8
> for r in (2, 8, 16, 22, 31):
>     passes = -(-62 // r)
>     print(r, passes, f"{passes * (n + 2 ** r):.3e}")
> ```
> Output: `2 31 3.100e+09`, `8 8 8.000e+08`, `16 4 4.003e+08`, `22 3 3.126e+08`, `31 2 4.495e+09`. One base per pass costs 31 passes; widening the digit helps until $2^r$ approaches $n$: at $r = 31$, two billion counters make the two passes 14 times more expensive than three passes of 22 bits. The optimum sits near $r \approx \lg n \approx 26.6$; the counter array must also fit in memory, and in cache for speed.

> [!question] Exercise 3 (L2)
> A student runs the stable passes from the **most** significant digit to the least. Give a two-key counterexample, and say which key the final order actually sorts by.

> [!success]- Solution
> Keys 12 and 21 (two decimal digits). Pass on the first digit: 12, 21. Pass on the second digit: 21 (digit 1), 12 (digit 2). Output 21, 12: wrong. The last pass decides the primary order, so passes must end with the most significant digit; going MSD-first requires recursion into buckets (MSD radix sort), not a sequence of global passes.

> [!question] Exercise 4 (L3, Python)
> Build a suffix array by prefix doubling: give each position the rank of its first letter, then repeatedly radix sort the pairs (rank of $i$, rank of $i + h$) with two counting-sort passes, re-rank, and double $h$ until all ranks differ. Test against naive suffix sorting, count the rounds on `GATTACA`, on $A^{1000}$ and on a random sequence of length 1,000, and bound the total cost.

> [!success]- Solution
> ```python
> def suffix_array(s: str) -> tuple:
>     """Suffix array by prefix doubling: each round radix-sorts the pairs (rank[i], rank[i + h])."""
>     n = len(s)
>     letters = sorted(set(s))
>     rank = [letters.index(ch) + 1 for ch in s]        # rank of the 1-letter prefix; 0 = past the end
>     sa, h, rounds = list(range(n)), 1, 0
>     while True:
>         rounds += 1
>         second = lambda i: rank[i + h] if i + h < n else 0
>         sigma = max(rank) + 1
>         sa = counting_sort(sa, second, sigma)          # secondary key first ...
>         sa = counting_sort(sa, lambda i: rank[i], sigma)   # ... then primary: an LSD radix sort of pairs
>         new, r = [0] * n, 0
>         for j, i in enumerate(sa):                     # equal pairs share a rank
>             if j == 0 or (rank[i], second(i)) != (rank[sa[j - 1]], second(sa[j - 1])):
>                 r += 1
>             new[i] = r
>         rank = new
>         if r == n or h >= n:                           # all prefixes distinct: done
>             return sa, rounds
>         h *= 2
>
> for _ in range(300):
>     s = "".join(rng.choices("ACGT" if rng.random() < 0.8 else "A", k=rng.randint(1, 80)))
>     assert suffix_array(s)[0] == sorted(range(len(s)), key=lambda i: s[i:])
> for s in ("GATTACA", "A" * 1000, "".join(rng.choices("ACGT", k=1000))):
>     sa, rounds = suffix_array(s)
>     print(s[:10], len(s), rounds, sa[:8])
> ```
> Output: `GATTACA 7 1 [6, 4, 1, 5, 0, 3, 2]`, `AAAAAAAAAA 1000 10 [999, 998, 997, 996, 995, 994, 993, 992]`, `TAGGAGAATT 1000 4 [449, 775, 348, 480, 56, 576, 87, 450]`. After the round with step $h$, ranks order the prefixes of length $2h$ (by induction: a $2h$-prefix is the pair of two $h$-prefixes), so the loop stops once prefixes of length $2^{\text{rounds}}$ are all distinct. Ranks stay below $n + 1$, so each round is two counting sorts in $O(n)$; rounds are at most $\lceil \lg n \rceil$, reached by the repetitive $A^{1000}$ (10 rounds), while the random sequence needs 4: its prefixes already differ after about $2 \log_4 n \approx 10$ letters, and $2^4 = 16$. Total $O(n \log n)$, against up to $\Theta(n^2 \log n)$ letter comparisons for comparison-sorting the suffixes of $A^n$.

## Mastery checklist

- [ ] 1 Recognized: I can say when counting sort and radix sort apply and state their $\Theta(d(n + \sigma))$ cost.
- [ ] 2 Understood: I can prove counting sort stable and LSD radix sort correct with the invariant, and explain why the comparison lower bound does not apply.
- [ ] 3 Practiced: I can implement both, choose the digit width, and sort and count 2-bit k-mer codes against a `Counter` oracle.
- [ ] 4 Applied: in [[05-sequence-search]], I build a k-mer index by sorting 2-bit codes and compare its memory and speed with a hash table on real sequences.
- [ ] 5 Explained: I can teach the roles of stability, key length and machine words, and how integer sorting powers suffix array construction.

## References

[^clrs8]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 8 "Sorting in Linear Time" (lower bounds for comparison sorting, counting sort, radix sort, bucket sort).
[^6006-l5]: [[MIT 6.006 - Introduction to Algorithms]], Spring 2020, lecture 5 "Linear Sorting" (direct-access array sort, tuple sort, counting sort, radix sort in $O(n + n \log_n u)$) and recitation 5 (stable subroutines, comparison lower bound).
[^karkkainen]: [[Kärkkäinen 2003 - Simple Linear Work Suffix Array Construction]], ICALP 2003, LNCS 2719:943-955 (recursive sorting of the suffixes at positions $i \bmod 3 \neq 0$, integer sorting as the only nontrivial subroutine).
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Locate Disease-Causing Mutations?" (suffix arrays).
