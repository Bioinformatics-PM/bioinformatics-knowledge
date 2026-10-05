---
aliases:
  - Hamming Metric
  - Mismatch Count
  - k-Mismatch Search
  - Distance de Hamming
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[String]]"
  - "[[Exact Pattern Matching]]"
  - "[[Point Mutation]]"
related:
  - "[[Edit Distance]]"
  - "[[Approximate Pattern Matching]]"
  - "[[Sequence Alignment]]"
  - "[[Sequence Motif]]"
  - "[[K-mer]]"
  - "[[Demultiplexing]]"
  - "[[Evolutionary Distance]]"
  - "[[Pigeonhole Principle]]"
  - "[[Base Pairing]]"
projects:
  - "[[04-alignment-engine]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Algorithms on Strings, Trees, and Sequences (Gusfield)]]"
---

# Hamming Distance

> [!abstract]
> The Hamming distance between two strings of the same length is the number of positions where they differ; it counts substitutions between aligned sequences and, slid along a genome, finds every occurrence of a pattern with at most $k$ mismatches.

## Definition

For two strings $s$ and $t$ of the same length $n$, the **Hamming distance** $d_H(s, t)$ is the number of positions $i$ at which $s_i \neq t_i$. An **approximate occurrence** of a pattern $P$ (length $m$) in a text $T$ with at most $k$ mismatches is a position $i$ with $d_H(T[i..i+m), P) \le k$.[^compeau-ori] Strings of different lengths have no Hamming distance.

## Why it matters

- **Point substitutions.** Between two aligned sequences of equal length with no insertion or deletion, $d_H$ is the number of single-base substitutions observed ([[Point Mutation]]); an ungapped alignment is scored this way ([[Sequence Alignment]]), and it is the first distance implemented in [[04-alignment-engine]].
- **Hidden signals need mismatches.** Regulatory words such as DnaA boxes recur with variations; in the replication-origin chapter of Compeau and Pevzner they stand out only when approximate occurrences (and reverse complements) are counted ([[K-mer]], [[Sequence Motif]], [[GC Skew]]).[^compeau-ori]
- **Barcodes and primers.** Assigning a read to a sample means comparing its index sequence with the expected barcodes, and a barcode set tolerates sequencing errors only if its members are far apart in Hamming distance ([[Demultiplexing]], Deeper). A probe or primer site with few mismatches to its target can still pair ([[Base Pairing]]).
- **Filters and indexes.** Approximate search tools first find exact pieces of the pattern, a guarantee that follows from counting mismatches (Advanced, [[Approximate Pattern Matching]]).

## Core (L1)

**Computing it.** Compare position by position:

```text
s   G A T T A C A G G C T T A C G A T
t   G A C T A C A T G C T A A C G T T
        ^         ^       ^       ^      d_H(s, t) = 4   (invented pair)
```

**Approximate occurrences by brute force.** Slide the pattern along the text as in [[Exact Pattern Matching]], but count mismatches instead of stopping at the first one; stop a window once it exceeds $k$. Allowing mismatches turns 1 occurrence into 3 in this invented text, for $P = $ `GATCAAG`:

```text
text      T T G A T C A T C G A T C A A G T T G A T C C A G
k = 0                       G A T C A A G                       position 9, 0 mismatches
k = 1                       G A T C A A G     G A T C C A G     + position 18 (1 mismatch)
k = 2         G A T C A T C                                     + position 2 (2 mismatches)
```

Every exact occurrence is an approximate one; each extra mismatch allowed enlarges the set of windows that qualify, quickly (Mathematical representation). The cost is that of the naive exact search, $O((n - m + 1)\, m)$ in the worst case; with early exit, a window of random DNA is abandoned after about $(k+1)/(3/4)$ comparisons on average, since each comparison is a mismatch with probability $3/4$.

## Deeper (L2)

**A metric.** $d_H$ satisfies $d_H(s, t) \ge 0$ with equality iff $s = t$, symmetry, and the **triangle inequality** $d_H(s, u) \le d_H(s, t) + d_H(t, u)$: at any position where $s$ and $u$ differ, $t$ differs from at least one of them. So "within $k$ mismatches" behaves like a ball of radius $k$, whose size is $\sum_{i=0}^{k} \binom{m}{i} 3^i$ for DNA ([[Sequence Motif#Mathematical representation]]).

**Barcode design: detect and correct.** Let $d_{\min}$ be the smallest Hamming distance between two barcodes of a set. If a read's barcode carries $e \le d_{\min} - 1$ substitutions, it cannot equal another barcode: the error is **detected**. If $e \le t = \lfloor (d_{\min} - 1)/2 \rfloor$, the true barcode is the only one within distance $t$, since two barcodes within $t$ of the same read would be within $2t < d_{\min}$ of each other: the error is **corrected**. A set with $d_{\min} = 3$ corrects 1 substitution and detects 2 (Exercise 2).

**Only substitutions.** One insertion shifts every downstream position, so the Hamming distance explodes although a single event happened: $d_H(\texttt{ACGTACGTAC}, \texttt{CGTACGTACG}) = 10$, while one deletion at the start and one insertion at the end (an [[Edit Distance]] of 2) turn one into the other. Sequences with indels need alignment ([[Sequence Alignment]]), not Hamming distance.

**Distance and divergence.** The proportion of differing sites, $p = d_H / n$, is the simplest [[Evolutionary Distance]]. For two unrelated random DNA sequences with uniform bases, each site differs with probability $3/4$, so $p$ saturates near $0.75$, and multiple substitutions at one site are counted once at most: observed differences underestimate the substitutions that occurred, which substitution models correct ([[Jukes-Cantor Model]]).

## Advanced (L3)

- **Pigeonhole filter.** Split $P$ into $k + 1$ contiguous blocks. If a window has at most $k$ mismatches with $P$, the mismatches touch at most $k$ blocks, so at least one block occurs **exactly** at the corresponding offset. Searching the blocks exactly (with an index, [[Inverted Index]]) and verifying only those candidates with $d_H$ loses nothing and skips most of the text: the principle behind seed-based mappers ([[Pigeonhole Principle]], [[Approximate Pattern Matching]], Exercise 3).
- **Constant-time extension.** With a suffix tree, the length of the longest common extension of the pattern and the text from any pair of positions is answered in $O(1)$ after linear preprocessing; jumping from mismatch to mismatch then decides each window in $O(k)$, and the $k$-mismatch problem is solved in $O(kn)$.[^gusfield9]
- **Bit-parallel counting.** With 2 bits per base (A = 00, C = 01, G = 10, T = 11), two packed k-mers $x, y$ differ at a base exactly where $d = x \oplus y$ has a nonzero 2-bit group, so $d_H = \mathrm{popcount}\big((d \lor (d \gg 1)) \land 0101\ldots01_2\big)$: a constant number of word operations for $k \le 32$ in a 64-bit word ([[Model of Computation]]). In Python: `((d | (d >> 1)) & int("01" * k, 2)).bit_count()`.

## Mathematical representation

- $d_H(s, t) = \sum_{i=1}^{n} [s_i \neq t_i]$ for $s, t \in \Sigma^n$, with $[\cdot]$ the indicator (1 if true, 0 otherwise). $(\Sigma^n, d_H)$ is a metric space.
- **Random sequences.** If $s$ and $t$ are independent with i.i.d. letters of probabilities $(p_a)$, each indicator is 1 with probability $q = 1 - \sum_a p_a^2$, so $d_H \sim \mathrm{Binomial}(n, q)$, mean $nq$ ($3n/4$ for uniform DNA) ([[Binomial Distribution]]).
- **Chance approximate occurrences.** A fixed pattern matches a uniform random window within $k$ mismatches with probability $\pi_k = \sum_{i=0}^{k} \binom{m}{i} (3/4)^i (1/4)^{m-i}$, and the expected number of such windows in a text of length $n$ is $(n - m + 1)\, \pi_k$ per strand.
- **Barcode guarantees**: detection of up to $d_{\min} - 1$ substitutions, correction of up to $\lfloor (d_{\min} - 1)/2 \rfloor$ (Deeper).

## Computational representation

```python
import random

def hamming(s: str, t: str) -> int:
    """Number of positions where s and t differ; defined only for equal lengths."""
    if len(s) != len(t):
        raise ValueError(f"lengths differ: {len(s)} != {len(t)}")
    return sum(a != b for a, b in zip(s, t))

def approx_occurrences(text: str, pattern: str, k: int) -> list[int]:
    """Start of every window of text within k mismatches of pattern (brute force, early exit)."""
    m, hits = len(pattern), []
    for i in range(len(text) - m + 1):
        mismatches = 0
        for j in range(m):
            if text[i + j] != pattern[j]:
                mismatches += 1
                if mismatches > k:                # this window cannot qualify any more
                    break
        if mismatches <= k:
            hits.append(i)
    return hits

print(hamming("GATTACAGGCTTACGAT", "GACTACATGCTAACGTT"))
try:
    hamming("ACGT", "ACG")
except ValueError as e:
    print("ValueError:", e)
print(sum(a != b for a, b in zip("ACGT", "ACG")))      # zip truncates silently

text = "TTGATCATCGATCAAGTTGATCCAG"                     # invented
print(approx_occurrences(text, "GATCAAG", 0), approx_occurrences(text, "GATCAAG", 1),
      approx_occurrences(text, "GATCAAG", 2))

```

```text
4
ValueError: lengths differ: 4 != 3
0
[9] [9, 18] [2, 9, 18]
```

`zip` stops at the shorter string, so the one-line version returns 0 for `ACGT` against `ACG`: check lengths explicitly. In NumPy, the same computation on arrays of bytes is `(a != b).sum()`.

## Worked example

> [!example] A 1-mismatch search on both strands (invented text)
> Text `5'-TTGATCATCGATCAAGTTGATCCAG-3'` ($n = 25$), pattern $P$ = `GATCAAG` ($m = 7$), $k = 1$.
>
> 1. **Plus strand**: windows at positions 9 (`GATCAAG`, 0 mismatches) and 18 (`GATCCAG`, 1 mismatch: A→C at pattern position 4). Position 2 (`GATCATC`) has 2 mismatches and is rejected.
> 2. **Minus strand**: search $\mathrm{rc}(P)$ = `CTTGATC` the same way ([[Reverse Complement]]). Window 15, `GTTGATC`, differs from it only at its first base: a 1-mismatch occurrence of $P$ on the minus strand, covering the plus-strand interval $[15, 22)$, which overlaps the plus-strand hit at 18. Window 6, `ATCGATC`, has 2 mismatches and is rejected. Easy to miss by eye: `TTGATCA` at position 0 looks similar but, aligned position by position, differs from `CTTGATC` at 6 of 7 positions.
> 3. **Chance level**: $\pi_1 = (1/4)^7 + 7 \cdot (3/4)(1/4)^6 \approx 0.0013$, so about $19 \times 2 \times 0.0013 \approx 0.05$ chance hits are expected over the 19 windows of both strands. Three hits in 25 bases are far above chance: the text was built from repeated `GATC`-containing words.

## Common misconceptions

> [!warning] "Two sequences of different lengths have a large Hamming distance"
> They have none. Truncating with `zip`, or padding, silently produces a number that measures nothing; a length difference means an indel, and the right quantity is the [[Edit Distance]] or an alignment.

> [!warning] "The Hamming distance counts the mutations that happened"
> It counts observed differences. Two substitutions at the same site count once, or zero if the second restores the original base, and a single indel inflates the count. As divergence grows, $d_H/n$ underestimates the true number of substitutions and saturates near 0.75 for DNA.

> [!warning] "Allowing one more mismatch adds a few hits"
> For a pattern of length $m$, the Hamming ball grows by $\binom{m}{k} 3^k$ sequences at radius $k$: for $m = 9$, from 1 (exact) to 28 ($k = 1$) to 352 ($k = 2$). Chance hits grow in proportion, so a $k$ chosen without computing $\pi_k$ can turn a specific search into noise.

## Exercises

> [!question] Exercise 1 (L1)
> Compute $d_H$(`GATTACA`, `GACTATA`) and $d_H$(`ACGT`, `TGCA`). Is $d_H$(`ACGT`, `ACGTA`) equal to 1?

> [!success]- Solution
> `GATTACA` vs `GACTATA`: positions 2 (T/C) and 5 (C/T) differ, $d_H = 2$. `ACGT` vs `TGCA`: all 4 positions differ, $d_H = 4$ (the complement, read in the same direction, differs everywhere). `ACGTA` is one base longer: the Hamming distance is undefined; the edit distance is 1 (one insertion).

> [!question] Exercise 2 (L2, Python)
> The invented barcodes are S1 `ACGTAC`, S2 `ACTTGA`, S3 `TCGAAA`, S4 `GGGTCC`. Compute $d_{\min}$, the number of errors the set detects and corrects, and assign the observed indexes `ACGTAC`, `ACGTAA`, `ACTTAA`, `ACGTTT` with the rule "unique barcode within the correction radius, else unassigned".

> [!success]- Solution
> ```python
> from itertools import combinations
>
> barcodes = {"S1": "ACGTAC", "S2": "ACTTGA", "S3": "TCGAAA", "S4": "GGGTCC"}   # invented
> dmin = min(hamming(a, b) for a, b in combinations(barcodes.values(), 2))
> t = (dmin - 1) // 2
> print("minimum distance", dmin, "corrects", t, "detects", dmin - 1)
>
> def assign(read_index: str) -> str:
>     near = [s for s, b in barcodes.items() if hamming(read_index, b) <= t]
>     return near[0] if len(near) == 1 else "unassigned"
>
> for r in ("ACGTAC", "ACGTAA", "ACTTAA", "ACGTTT"):
>     print(r, assign(r), [hamming(r, b) for b in barcodes.values()])
> ```
> ```text
> minimum distance 3 corrects 1 detects 2
> ACGTAC S1 [0, 3, 3, 3]
> ACGTAA S1 [1, 2, 2, 4]
> ACTTAA S2 [2, 1, 3, 5]
> ACGTTT unassigned [2, 3, 4, 4]
> ```
> `ACGTAA` (1 error) is corrected to S1. `ACGTTT` has 2 errors from S1: detected (it matches no barcode) but not corrected. `ACTTAA` shows the danger: if it came from S1 with 2 errors, it lands within distance 1 of S2 and is **miscorrected**. Beyond $t$ errors, correction becomes misassignment, so the error rate of the index read must be low compared with $t / (\text{barcode length})$.

> [!question] Exercise 3 (L3, Python)
> Implement the pigeonhole filter for $k$ mismatches (exact search of $k + 1$ blocks, then verification), test it against `approx_occurrences`, and count how many candidates it verifies for a 14-mer with $k = 2$ in a simulated 200,000-base genome containing two planted variants.

> [!success]- Solution
> ```python
> def pigeonhole_occurrences(text: str, pattern: str, k: int) -> list[int]:
>     """Windows within k mismatches: exact hits of one of k + 1 blocks, then verification."""
>     m = len(pattern)
>     bounds = [round(b * m / (k + 1)) for b in range(k + 2)]          # k + 1 contiguous blocks
>     candidates = set()
>     for lo, hi in zip(bounds, bounds[1:]):
>         block, q = pattern[lo:hi], text.find(pattern[lo:hi])
>         while q != -1:                                                # exact, overlapping hits
>             start = q - lo
>             if 0 <= start <= len(text) - m:
>                 candidates.add(start)
>             q = text.find(block, q + 1)
>     return sorted(i for i in candidates if hamming(text[i:i + m], pattern) <= k)
>
> random.seed(3)
> for _ in range(500):
>     txt = "".join(random.choices("ACGT", k=random.randint(10, 300)))
>     m = random.randint(4, 12); k = random.randint(0, 3)
>     pat = "".join(random.choices("ACGT", k=m))
>     if k + 1 > m: continue
>     assert pigeonhole_occurrences(txt, pat, k) == approx_occurrences(txt, pat, k)
> genome = "".join(random.choices("ACGT", k=200_000))                   # simulated
> genome = genome[:50_000] + "GATTCCAGATTACA" + genome[50_014:120_000] + "GATTACAGATTAGT" + genome[120_014:]
> pat = "GATTACAGATTACA"
> print(len(approx_occurrences(genome, pat, 2)), pigeonhole_occurrences(genome, pat, 2) == approx_occurrences(genome, pat, 2))
> m, k = len(pat), 2
> bounds = [round(b * m / (k + 1)) for b in range(k + 2)]
> print(bounds, sum(genome.count(pat[lo:hi]) for lo, hi in zip(bounds, bounds[1:])))
> ```
> ```text
> 2 True
> [0, 5, 9, 14] 1224
> ```
> Both planted variants (1 and 2 mismatches) are found, as the brute force finds them. The filter verifies about 1,224 candidates (blocks of 5, 4 and 5 bases; `str.count` gives an approximation since it skips overlapping block hits) instead of 199,987 windows. Shorter blocks (larger $k$ for the same $m$) produce many more random block hits: about $n/4^{\ell}$ per block of length $\ell$, the trade-off that sets seed length in mappers ([[Seed and Extend]]).

## Mastery checklist

- [ ] 1 Recognized: I can define the Hamming distance and say when it is undefined.
- [ ] 2 Understood: I can prove it is a metric, explain why indels break it, and derive the detection and correction capacity of a barcode set.
- [ ] 3 Practiced: I can implement brute-force $k$-mismatch search with early exit and the pigeonhole filter, test them against each other, and write the packed bit-parallel distance.
- [ ] 4 Applied: in [[04-alignment-engine]], I compute Hamming distances between real aligned sequences and compare them with edit distances on sequences with indels.
- [ ] 5 Explained: I can teach the pigeonhole filter, the growth of chance hits with $k$, and why observed differences underestimate evolutionary change.

## References

[^compeau-ori]: [[Bioinformatics Algorithms (Compeau)]], chapter "Where in the Genome Does DNA Replication Begin?" (Hamming distance, approximate occurrences of a pattern with at most $d$ mismatches, frequent words with mismatches and reverse complements, DnaA boxes).
[^gusfield9]: [[Algorithms on Strings, Trees, and Sequences (Gusfield)]], ch. 9 "More Applications of Suffix Trees" (longest common extension in constant time after linear preprocessing; the $k$-mismatch problem).
