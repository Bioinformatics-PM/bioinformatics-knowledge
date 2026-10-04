---
aliases:
  - String Matching
  - Exact String Matching
  - Naive String Matching
  - Brute-Force String Search
  - Pattern Matching Problem
  - Recherche exacte de motif
tags:
  - type/algorithm
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[String]]"
  - "[[Big O Notation]]"
  - "[[Loop Invariant]]"
  - "[[Reverse Complement]]"
related:
  - "[[K-mer]]"
  - "[[Sequence Motif]]"
  - "[[Hamming Distance]]"
  - "[[Z-Algorithm]]"
  - "[[Knuth-Morris-Pratt Algorithm]]"
  - "[[Boyer-Moore Algorithm]]"
  - "[[Rabin-Karp Algorithm]]"
  - "[[Suffix Array]]"
  - "[[Regular Expression]]"
  - "[[Property-Based Testing]]"
projects:
  - "[[01-dna-engine]]"
  - "[[05-sequence-search]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Algorithms on Strings, Trees, and Sequences (Gusfield)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
---

# Exact Pattern Matching

> [!abstract]
> Exact pattern matching finds every position where a pattern occurs in a text, overlapping occurrences included and, for DNA, on both strands; the naive algorithm tries every alignment in $O(nm)$ worst-case time, runs in expected linear time on random DNA, and is the reference that every faster method must reproduce exactly.

## Problem

- **Input**: a text $T$ of length $n$ and a pattern $P$ of length $m$, $1 \le m \le n$, over an alphabet $\Sigma$ (for DNA, $\{A, C, G, T\}$).
- **Output**: the set of all **shifts** $i$, $0 \le i \le n - m$, such that $T[i..i+m) = P$ (0-based, half-open), in increasing order. Every occurrence is reported, including occurrences that overlap.[^clrs32][^compeau-ori] For double-stranded DNA, the output is the set of pairs (start, strand) in plus-strand coordinates, a reverse palindrome being reported once ([[Reverse Complement]]).
- **Biological use**: finding restriction sites, primer binding sites, adapters in reads and known regulatory words ([[Sequence Motif]], [[01-dna-engine]]); counting the occurrences of a [[K-mer]], such as the repeated DnaA boxes that mark a bacterial replication origin;[^compeau-ori] verifying the candidate hits proposed by an index or a seed ([[05-sequence-search]], [[Seed and Extend]]); and serving as the **test oracle** for the faster algorithms of [[String Algorithms]].

## Intuition

Place the pattern under the text at every possible offset and compare letter by letter, stopping at the first mismatch. Nothing is skipped and nothing is remembered between offsets: the method is obviously correct, and its only weakness is that a long partial match at one offset is re-read at the next. Every faster algorithm ([[Z-Algorithm]], [[Knuth-Morris-Pratt Algorithm]], [[Boyer-Moore Algorithm]]) is a way to reuse that information without losing a single occurrence.

## Mathematical formulation

**Occurrences.** $\mathrm{Occ}(P, T) = \{ i \in \{0, \dots, n - m\} : T[i + j] = P[j] \text{ for all } 0 \le j < m \}$. Its size is at most $n - m + 1$, reached for $T = A^n$, $P = A^m$.

**Both strands.** With $\mathrm{rc}$ the reverse complement, $P$ occurs on the minus strand at the plus-strand interval $[i, i + m)$ exactly when $\mathrm{rc}(P)$ occurs on the plus strand at $i$. So

$$\mathrm{Occ}_{\pm}(P, T) = \{(i, +) : i \in \mathrm{Occ}(P, T)\} \cup \{(i, -) : i \in \mathrm{Occ}(\mathrm{rc}(P), T)\},$$

merging $(i, +)$ and $(i, -)$ when $P = \mathrm{rc}(P)$. One scan for two patterns; the reverse complement of the genome is never built ([[Reverse Complement#Deeper (L2)]]).

**Overlaps and periods.** Two occurrences at shifts $i < i'$ with $d = i' - i < m$ overlap, which forces $P[j] = P[j + d]$ for all $0 \le j < m - d$: $d$ is a **period** of $P$. `ATA` has period 2, so its occurrences can sit 2 apart; `ACGT` has no period below 4, so its occurrences never overlap. Periods are what [[Knuth-Morris-Pratt Algorithm|KMP's failure function]] encodes.

**Correctness of the naive algorithm.** Invariant of the inner loop at shift $i$: $T[i..i+j) = P[0..j)$. It holds for $j = 0$, each increment preserves it, and the loop stops at $j = m$ (occurrence) or at the first mismatch (no occurrence at $i$). Since the outer loop tries every $i \in [0, n - m]$, every occurrence is reported and nothing else ([[Loop Invariant]]).

**Worst case.** Shift $i$ costs $\ell_i + 1$ comparisons, where $\ell_i$ is the length of the match found before stopping (at most $m$ comparisons in all). Hence $C \le m(n - m + 1)$, with equality for $T = A^n$ and $P = A^{m-1}C$ (every shift fails at its last letter) or $P = A^m$.[^clrs32] For fixed $m \ll n$, that is $\Theta(nm)$.

**Expected case on random text.** If text letters are i.i.d. uniform over $\sigma$ letters, comparison $j$ at a shift happens only if the first $j$ letters matched, with probability $\sigma^{-j}$. The expected cost per shift is

$$E = \sum_{j=0}^{m-1} \sigma^{-j} = \frac{1 - \sigma^{-m}}{1 - 1/\sigma} < \frac{\sigma}{\sigma - 1},$$

that is, less than $4/3$ comparisons per shift for DNA, whatever $m$. The naive algorithm is linear in expectation on random DNA; its quadratic behaviour needs repetitive text and a self-similar pattern, which genomes (microsatellites, poly-A tracts) do provide.

## Algorithm

```text
NAIVE-MATCH(T, P)                      // n = |T|, m = |P|, 1 <= m <= n
1  hits = []
2  for i = 0 to n - m                  // every shift
3      j = 0
4      while j < m and T[i + j] = P[j] // invariant: T[i .. i+j) = P[0 .. j)
5          j = j + 1
6      if j = m
7          append i to hits
8  return hits

BOTH-STRANDS(T, P) = NAIVE-MATCH(T, P) labelled "+"  ∪  NAIVE-MATCH(T, rc(P)) labelled "-"
                     (one hit per position if P = rc(P))
```

One run of the naive algorithm for `P = ATA` on the invented text `GATATATGCATATAC` (`x` marks the mismatch that ends a shift, `=` a matched letter):

```text
position   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
text       G A T A T A T G C A T  A  T  A  C
shift 0    x                                     1 comparison
shift 1      = = =                               occurrence at 1
shift 2        x                                 1
shift 3          = = =                           occurrence at 3 (overlaps the one at 1)
shift 5              = = x                       3 comparisons, fails on G
shift 9                      = =  =              occurrence at 9
shift 11                          =  =  =        occurrence at 11
```

Shifts 4, 6, 7, 8, 10 and 12 fail on their first letter. Total: 23 comparisons over 13 shifts.

## Complexity

| | Time | Space |
|---|---|---|
| Naive, worst case | $\Theta((n - m + 1)\, m)$ comparisons[^clrs32] | $O(1)$ beyond the output |
| Naive, i.i.d. uniform text | $< \frac{\sigma}{\sigma - 1}(n - m + 1)$ expected comparisons | $O(1)$ |
| [[Knuth-Morris-Pratt Algorithm]], [[Z-Algorithm]] | $O(n + m)$ worst case[^clrs32][^gusfield] | $O(m)$ |
| [[Boyer-Moore Algorithm]] | sublinear in practice on large alphabets[^gusfield] | $O(m + \sigma)$ |
| Index of $T$ ([[Suffix Array]], [[FM-Index]]), many queries | $O(m \log n)$ or $O(m)$ per query, after preprocessing $T$[^compeau-mut] | $\Theta(n)$ index |

Any algorithm that reports all occurrences needs time proportional to the output, up to $n - m + 1$ positions, plus enough reading of $T$ to rule out every other shift.

## Implementation

```python
import random
import re

def naive_matches(text: str, pattern: str) -> list[int]:
    """0-based start of every occurrence of pattern in text, overlapping ones included."""
    n, m = len(text), len(pattern)
    hits = []
    for i in range(n - m + 1):                    # every alignment (shift) of the pattern
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1                                # extend while characters agree
        if j == m:
            hits.append(i)
    return hits

def naive_comparisons(text: str, pattern: str) -> int:
    """Character comparisons made by naive_matches (a mismatch counts as one)."""
    n, m, total = len(text), len(pattern), 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            total += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
    return total

text = "GATATATGCATATAC"                          # invented
print(naive_matches(text, "ATA"))
print(text.count("ATA"), [m.start() for m in re.finditer("ATA", text)])
print([m.start() for m in re.finditer("(?=ATA)", text)])
print(naive_matches("ACGT", "ACGT"), naive_matches("ACG", "ACGT"), naive_matches("ACGT", ""))

random.seed(0)
n, m = 100_000, 8
dna = "".join(random.choices("ACGT", k=n))         # simulated, uniform i.i.d. bases
pat = "GATTACAG"
c = naive_comparisons(dna, pat)
print(len(naive_matches(dna, pat)), c, round(c / (n - m + 1), 4), round((1 - 4**-m) / (1 - 1/4), 4))
worst = naive_comparisons("A" * n, "A" * (m - 1) + "C")
print(worst, m * (n - m + 1))
print(naive_comparisons("A" * n, "A" * m), len(naive_matches("A" * n, "A" * m)))
```

```text
[1, 3, 9, 11]
2 [1, 9]
[1, 3, 9, 11]
[0] [] [0, 1, 2, 3, 4]
1 133257 1.3327 1.3333
799944 799944
799944 99993
```

What the output shows:

- **Library calls answer a different question.** `str.count` and `re.finditer` return 2 occurrences at 1 and 9: after a match they resume searching after its end, so overlapping occurrences (3 and 11) are lost. A zero-width lookahead `(?=ATA)` restores them. Always test the overlapping case.
- **Edge cases.** A pattern longer than the text has no occurrence; the empty pattern "occurs" at all $n + 1$ positions, which is why the precondition $m \ge 1$ belongs in the specification.
- **Expected versus worst case.** On 100,000 simulated uniform bases, the naive search makes 1.3327 comparisons per shift, against $1.3333$ predicted; on $A^n$ with $P = A^7C$ it makes exactly $m(n - m + 1) = 799{,}944$, six times more. With $P = A^8$, the same cost buys 99,993 overlapping occurrences: here the output itself is as large as the text.

## Worked example

> [!example] Searching a short sequence on both strands (invented)
> Text `5'-ATGCATGATCAT-3'` ($n = 12$). Find `ATG` and `GATC` on both strands, reporting plus-strand coordinates.
>
> 1. `ATG`: $\mathrm{rc}(\texttt{ATG}) = \texttt{CAT}$. Plus strand: `ATG` at 0 and 4. `CAT` occurs at 3 and 9, so `ATG` occurs on the minus strand over the plus intervals $[3, 6)$ and $[9, 12)$. Result: $(0, +), (3, -), (4, +), (9, -)$.
> 2. `GATC`: $\mathrm{rc}(\texttt{GATC}) = \texttt{GATC}$, a reverse palindrome. The two scans both report position 6; it is **one** site, read on both strands: $(6, \pm)$.
> 3. Check by length: a 12-nt text has $12 - 3 + 1 = 10$ shifts for a 3-mer on each strand, so 20 strand-specific windows were examined for `ATG` without building the reverse-complement text.
> 4. The overlap between `CAT` at 3 and `ATG` at 4 is real biology in miniature: on a double helix, sites on the two strands can share bases.

## Limitations

> [!warning] "`str.count` and `re.finditer` find all occurrences"
> They find non-overlapping occurrences, scanning left to right and resuming after each match (output above). For tandem repeats, k-mer counting and self-similar patterns such as `ATAT`, that silently undercounts.

> [!warning] "Exact means the biology is exact"
> Real binding sites, primers and reads tolerate mismatches, and a single sequencing error hides an occurrence from an exact search. Exact matching is the right tool for verifying candidates and for exact words (restriction sites); otherwise move to mismatches ([[Hamming Distance]]) or edits ([[Approximate Pattern Matching]]).

- **Alphabet conventions decide matches.** `a` and `A` are different characters to a string comparison, and an `N` in the text never equals a base of the pattern. Normalize case and decide how ambiguity codes match ([[IUPAC Nucleotide Code]]) before searching.
- **Many patterns, or many queries.** Searching $k$ patterns naively costs $k$ scans of the text; [[Aho-Corasick Algorithm]] does one. Searching the same genome for millions of reads calls for an index of the text, built once ([[Suffix Array]], [[FM-Index]], [[Inverted Index]]).
- **Coordinates.** Report 0-based half-open intervals (or convert explicitly to 1-based closed ones) and plus-strand positions for minus-strand hits ([[Genomic Coordinate System]]).

## Variants and successors

- **Linear worst case** by reusing comparisons: [[Z-Algorithm]] (fundamental preprocessing), [[Knuth-Morris-Pratt Algorithm]] (failure function), both $O(n + m)$.[^clrs32][^gusfield]
- **Skipping alignments**: [[Boyer-Moore Algorithm]], which gains most on large alphabets (proteins, text) and less on DNA.
- **Hashing**: [[Rabin-Karp Algorithm]] compares rolling hashes of windows ([[Rolling Hash]]) and verifies candidates with the naive comparison.
- **Sets of patterns**: [[Aho-Corasick Algorithm]] for primers, adapters and barcodes in one pass.
- **Mismatches and edits**: [[Hamming Distance]] (equal length, substitutions only), then [[Approximate Pattern Matching]].
- **Text indexes**: [[Suffix Tree]], [[Suffix Array]], [[FM-Index]] when the text is fixed and queried many times.[^compeau-mut]

## Exercises

> [!question] Exercise 1 (L1)
> In the invented text `CATATATAG`, list by hand every occurrence of `ATA` and of `ATAT`, and say what `text.count` returns for each.

> [!success]- Solution
> `ATA` occurs at 1, 3 and 5 (overlapping, period 2); `text.count("ATA")` returns 2 (positions 1 and 5: after the match at 1 the search resumes at 4). `ATAT` occurs at 1 and 3; `count` returns 1. Overlaps are possible exactly because both patterns have period 2.

> [!question] Exercise 2 (L1)
> State precisely the output of a both-strand search for a pattern $P$ of length $m$ in a text of length $n$: coordinates, strand labels, palindromes, and the maximum possible number of hits.

> [!success]- Solution
> A list of (start, strand) with start in plus-strand 0-based coordinates, $0 \le \text{start} \le n - m$, each hit covering $[\text{start}, \text{start} + m)$; strand `+` when $T[\text{start}..\text{start}+m) = P$, `-` when it equals $\mathrm{rc}(P)$; if $P = \mathrm{rc}(P)$, one hit labelled `±`. At most $n - m + 1$ positions per strand, so at most $2(n - m + 1)$ hits (or $n - m + 1$ for a palindrome).

> [!question] Exercise 3 (L2)
> Show that no text of length $n$ can make the naive algorithm exceed $m(n - m + 1)$ comparisons, and give two different (text, pattern) pairs that reach it. Why is the naive algorithm nevertheless used as the oracle?

> [!success]- Solution
> Each of the $n - m + 1$ shifts makes at most $m$ comparisons (the inner loop stops at $j = m$). The bound is reached when every shift reads all $m$ letters: $T = A^n$ with $P = A^m$ (every shift matches) or $P = A^{m-1}C$ (every shift fails on its last letter); measured above, $799{,}944$ for $n = 10^5$, $m = 8$. The oracle's job is to be **obviously** correct, not fast: its correctness proof is three lines, and on test inputs of a few hundred letters its cost is irrelevant.

> [!question] Exercise 4 (L2, Python)
> Write `find_all_fast` with `str.find` (restarting one position after each hit) and test it against `naive_matches` on 1,000 random cases. Then check that the test catches the variant that restarts at `i + len(pattern)`.

> [!success]- Solution
> ```python
> def find_all_fast(text: str, pattern: str) -> list[int]:
>     """All occurrences with str.find (a C-level search), restarting one position later."""
>     hits, i = [], text.find(pattern)
>     while i != -1:
>         hits.append(i)
>         i = text.find(pattern, i + 1)
>     return hits
>
> def find_all_buggy(text, pattern):
>     hits, i = [], text.find(pattern)
>     while i != -1:
>         hits.append(i)
>         i = text.find(pattern, i + len(pattern))   # skips overlapping occurrences
>     return hits
>
> random.seed(1)
> failures = 0
> for _ in range(1000):
>     txt = "".join(random.choices("ACGT", k=random.randint(0, 60)))
>     pat = "".join(random.choices("AC", k=random.randint(1, 4)))   # small alphabet: many overlaps
>     assert find_all_fast(txt, pat) == naive_matches(txt, pat)
>     failures += find_all_buggy(txt, pat) != naive_matches(txt, pat)
> print("fast version agrees on 1000 cases; buggy version fails on", failures)
> ```
> Output: `fast version agrees on 1000 cases; buggy version fails on 42`. Patterns drawn from a two-letter alphabet are often periodic (`AA`, `ACA`), which is what exposes the bug; random patterns over four letters would trigger it far less often. Designing the test distribution is part of [[Property-Based Testing]].

> [!question] Exercise 5 (L3, Python)
> Generalize the expected cost per shift to an i.i.d. text with base probabilities $p_A, p_C, p_G, p_T$, compute it for `AAAAAAAA` and `GCGCGCGC` in a simulated genome with 70 % A+T, and compare with measurements.

> [!success]- Solution
> Comparison $j$ happens iff the first $j$ letters matched: $E(P) = \sum_{j=0}^{m-1} \prod_{l < j} p_{P[l]}$.
> ```python
> def expected_comparisons(pattern: str, p: dict) -> float:
>     """E[comparisons per alignment] for i.i.d. text with base probabilities p."""
>     total, prob_prefix = 0.0, 1.0
>     for c in pattern:
>         total += prob_prefix                      # comparison j happens iff the first j matched
>         prob_prefix *= p[c]
>     return total
>
> at_rich = {"A": 0.35, "T": 0.35, "C": 0.15, "G": 0.15}
> random.seed(2)
> genome = "".join(random.choices("ACGT", weights=[at_rich[b] for b in "ACGT"], k=200_000))
> for pat in ("AAAAAAAA", "GCGCGCGC"):
>     measured = naive_comparisons(genome, pat) / (len(genome) - len(pat) + 1)
>     print(pat, round(expected_comparisons(pat, at_rich), 4), round(measured, 4))
> ```
> ```text
> AAAAAAAA 1.5381 1.5393
> GCGCGCGC 1.1765 1.1769
> ```
> Composition matters only mildly: the cost stays below $1/(1 - \max_a p_a)$ per shift, here $1/0.65 \approx 1.54$. The naive algorithm becomes slow only when the text is locally repetitive in the pattern's own letters, which an i.i.d. model never produces; benchmarks of string algorithms on random text therefore flatter the naive method, and real genomes with low-complexity regions should be part of any benchmark ([[Benchmarking]]).

## Mastery checklist

- [ ] 1 Recognized: I can state the exact matching problem with its output convention: all shifts, overlapping, 0-based, both strands.
- [ ] 2 Understood: I can prove the naive algorithm correct with its invariant and derive both its worst case $m(n - m + 1)$ and its expected cost on random DNA.
- [ ] 3 Practiced: I can implement the naive search and a both-strand wrapper, and use them as an oracle in randomized tests that include overlapping and palindromic patterns.
- [ ] 4 Applied: in [[01-dna-engine]] and [[05-sequence-search]], my motif search reports the same hits as the oracle on real sequences, in plus-strand coordinates.
- [ ] 5 Explained: I can teach why library calls miss overlapping hits, when the naive method is quadratic in practice, and which faster method (linear-time matcher, multi-pattern automaton, index) fits which workload.

## References

[^clrs32]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), ch. 32 "String Matching": the string-matching problem stated with valid shifts, the naive algorithm and its $O((n - m + 1)m)$ worst case, and linear-time matching (Knuth-Morris-Pratt).
[^gusfield]: [[Algorithms on Strings, Trees, and Sequences (Gusfield)]], part on exact string matching (the naive method, fundamental preprocessing, Boyer-Moore and the classical linear-time methods).
[^compeau-ori]: [[Bioinformatics Algorithms (Compeau)]], chapter "Where in the Genome Does DNA Replication Begin?" (the pattern matching problem: all starting positions of a pattern in a genome, overlapping occurrences included; DnaA boxes and their reverse complements).
[^compeau-mut]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Locate Disease-Causing Mutations?" (pattern matching with suffix trees, suffix arrays and the Burrows-Wheeler transform).
