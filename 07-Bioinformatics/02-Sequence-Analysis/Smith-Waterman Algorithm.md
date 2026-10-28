---
aliases:
  - Smith-Waterman
  - SW Algorithm
  - Local Alignment Algorithm
  - Algorithme de Smith-Waterman
tags:
  - type/algorithm
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Needleman-Wunsch Algorithm]]"
  - "[[Sequence Alignment]]"
  - "[[Substitution Matrix]]"
  - "[[Gap Penalty]]"
  - "[[Dynamic Programming]]"
related:
  - "[[BLAST]]"
  - "[[E-Value]]"
  - "[[Seed and Extend]]"
  - "[[Semi-Global Alignment]]"
  - "[[Gotoh Algorithm]]"
  - "[[Protein Domain]]"
  - "[[Low-Complexity Region]]"
  - "[[Sequence Homology]]"
  - "[[Hirschberg Algorithm]]"
projects:
  - "[[04-alignment-engine]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Smith 1981 - Identification of Common Molecular Subsequences]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Altschul 1990 - Basic Local Alignment Search Tool]]"
  - "[[Farrar 2007 - Striped Smith-Waterman Speeds Database Searches Six Times over Other SIMD Implementations]]"
---

# Smith-Waterman Algorithm

> [!abstract]
> Smith-Waterman finds the best-scoring pair of segments, one from each sequence, by running the global alignment recurrence with one change: no cell may fall below zero, so an alignment can start afresh anywhere and end at the best cell of the table.

## Problem

- **Input**: sequences $s = s_1 \dots s_n$ and $t = t_1 \dots t_m$, a substitution score $\sigma(a, b)$ ([[Substitution Matrix]]) and a linear gap penalty $d > 0$ ([[Gap Penalty]]).
- **Output**: the maximal score, over all pairs of substrings $s_{i'+1} \dots s_i$ and $t_{j'+1} \dots t_j$, of their global alignment (the empty pair scores 0), with one optimal local alignment and its coordinates.
- **Biological use**: homology is often local. Two proteins can share one domain inside unrelated contexts ([[Protein Domain]]), and a query can match only part of a database sequence ([[Sequence Homology]]). Smith and Waterman (1981) gave a rigorous and simply programmed algorithm for the best-matching pair of segments, allowing insertions and deletions of any length.[^sw] It is the exact local alignment that [[BLAST]] gives up for speed.[^blast] [[04-alignment-engine]] implements it next to [[Needleman-Wunsch Algorithm]], with the shared tested version in [[bio-algorithms]].

## Intuition

In a global alignment, an unrelated prefix drags the score down and the debt is carried to the end. Locally you may drop it: when the best alignment ending at a cell has a negative score, starting a new, empty alignment there (score 0) is better. That is the zero in the recurrence. Symmetrically, you may stop wherever the score peaks, so the answer is the largest cell anywhere in the table, not the bottom-right corner. Between its start and its end, a local alignment is simply a global alignment of two substrings.

## Mathematical formulation

Let $H(i, j)$ be the best score of an alignment of a suffix of $s_1 \dots s_i$ with a suffix of $t_1 \dots t_j$, the empty alignment included.[^durbin]

**Base cases**: $H(i, 0) = H(0, j) = 0$.

**Recurrence**, for $1 \le i \le n$ and $1 \le j \le m$:
$$H(i, j) = \max\begin{cases} 0 & \text{start a new alignment here}\\ H(i-1, j-1) + \sigma(s_i, t_j) & \text{pair } (s_i, t_j)\\ H(i-1, j) - d & s_i \text{ against a gap}\\ H(i, j-1) - d & t_j \text{ against a gap}\end{cases}$$

The optimal local score is $\max_{i, j} H(i, j)$. The traceback starts from a maximal cell and stops at the first cell with value 0; the visited cells give the coordinates of the two segments.[^sw][^durbin]

**Correctness.** As for [[Needleman-Wunsch Algorithm]], by induction on $i + j$, with one more case: the best alignment of suffixes ending at $(i, j)$ is either empty (score 0) or ends with one of the three column types after an optimal alignment of suffixes ending one step earlier. Every local alignment ends at some cell, so the maximum over all cells covers every possible end.

**Why zero, precisely.** (1) Every cell becomes a possible start, so flanking sequence costs nothing. (2) Scores never go negative, so a similar segment after a long unrelated stretch is not hidden by its debt. (3) With a negative expected score for random pairs, unrelated stretches keep falling back to 0, and only real similarity builds a peak. If the expected score were positive, alignments of unrelated sequences would score high just by being long, and the local alignment would stretch over almost everything.[^durbin] (Exercise 3.) Stopping the traceback at the first 0 returns the shortest of possibly several co-optimal segments: extending back through cells of value 0 would add a part scoring 0 in total.

## Algorithm

```text
SMITH-WATERMAN(s, t, σ, d)
  H[i][0] ← 0 for all i;  H[0][j] ← 0 for all j
  best ← 0; (bi, bj) ← (0, 0)
  for i in 1..n:
    for j in 1..m:
      H[i][j] ← max(0, H[i-1][j-1] + σ(s[i], t[j]), H[i-1][j] - d, H[i][j-1] - d)
      if H[i][j] > best: best ← H[i][j]; (bi, bj) ← (i, j)
  (i, j) ← (bi, bj);  columns ← []
  while H[i][j] > 0:
    if H[i][j] = H[i-1][j-1] + σ(s[i], t[j]):  emit (s[i], t[j]); i ← i-1; j ← j-1
    else if H[i][j] = H[i-1][j] - d:           emit (s[i], -);    i ← i-1
    else:                                       emit (-, t[j]);    j ← j-1
  return best, reversed(columns), segments s[i+1..bi] and t[j+1..bj]
```

## Complexity

| | Time | Space |
|---|---|---|
| Smith-Waterman, score and alignment | $O(nm)$ | $O(nm)$ |
| Score and end cell only | $O(nm)$ | $O(\min(n, m))$ |
| Database search, query of length $m$ against $N$ residues | $O(mN)$ | $O(m)$ per sequence |
| Striped SIMD implementation[^farrar] | $O(nm)$, 2 to 8 times faster than other SIMD versions | $O(m)$ |
| [[BLAST]], seeds extended into segment pairs[^blast] | far fewer cells, no optimality guarantee | |

The per-cell work is constant, as in global alignment, with one extra comparison to 0 and one with the running maximum.

## Implementation

Standard library only. The oracle is the definition itself: the best global score over all pairs of substrings, computed with a two-row global aligner.

```python
import random

GAP = "-"

def smith_waterman(s: str, t: str, sub, gap: int):
    """Optimal local alignment with a linear gap score `gap` (< 0).

    Returns (score, row_s, row_t, (start_s, end_s, start_t, end_t), H), 0-based half-open.
    """
    n, m = len(s), len(t)
    H = [[0] * (m + 1) for _ in range(n + 1)]           # row 0 and column 0 stay 0
    best, bi, bj = 0, 0, 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            H[i][j] = max(0,                                        # start afresh here
                          H[i - 1][j - 1] + sub(s[i - 1], t[j - 1]),
                          H[i - 1][j] + gap,
                          H[i][j - 1] + gap)
            if H[i][j] > best:                                      # first maximum wins
                best, bi, bj = H[i][j], i, j
    a, b, i, j = [], [], bi, bj
    while H[i][j] > 0:                                              # stop at the first zero
        if H[i][j] == H[i - 1][j - 1] + sub(s[i - 1], t[j - 1]):
            a.append(s[i - 1]); b.append(t[j - 1]); i, j = i - 1, j - 1
        elif H[i][j] == H[i - 1][j] + gap:
            a.append(s[i - 1]); b.append(GAP); i -= 1
        else:
            a.append(GAP); b.append(t[j - 1]); j -= 1
    return best, "".join(reversed(a)), "".join(reversed(b)), (i, bi, j, bj), H

def simple(match: int = 2, mismatch: int = -1):
    return lambda x, y: match if x == y else mismatch

def global_score(s: str, t: str, sub, gap: int) -> int:
    """Needleman-Wunsch score only, two rows of memory (used as the oracle)."""
    prev = [j * gap for j in range(len(t) + 1)]
    for i in range(1, len(s) + 1):
        cur = [i * gap] + [0] * len(t)
        for j in range(1, len(t) + 1):
            cur[j] = max(prev[j - 1] + sub(s[i - 1], t[j - 1]), prev[j] + gap, cur[j - 1] + gap)
        prev = cur
    return prev[-1]

def local_by_definition(s: str, t: str, sub, gap: int) -> int:
    """Best global score over all pairs of substrings (the empty pair scores 0)."""
    subs = lambda x: {x[i:k] for i in range(len(x)) for k in range(i + 1, len(x) + 1)}
    return max([0] + [global_score(u, v, sub, gap) for u in subs(s) for v in subs(t)])

def rescore(a: str, b: str, sub, gap: int) -> int:
    return sum(gap if GAP in (x, y) else sub(x, y) for x, y in zip(a, b))

def show(H, s: str, t: str) -> None:
    print("     " + "".join(f"{c:>3}" for c in GAP + t))
    for i, row in enumerate(H):
        print(f"{(GAP + s)[i]:>4} " + "".join(f"{v:>3}" for v in row))

# Worked example (invented): a shared segment with one deletion, unrelated flanks
s, t, sub = "CAGACGGTACG", "TACGGACCTC", simple(2, -1)
score, a, b, (i0, i1, j0, j1), H = smith_waterman(s, t, sub, -2)
show(H, s, t)
print(score, a, b, f"s[{i0}:{i1}] t[{j0}:{j1}]", "global:", global_score(s, t, sub, -2))

# Tests against the definition, on random pairs and random scoring schemes
rng = random.Random(7)
for _ in range(200):
    s = "".join(rng.choices("ACGT", k=rng.randint(0, 7)))
    t = "".join(rng.choices("ACGT", k=rng.randint(0, 7)))
    sub, gap = simple(rng.randint(1, 3), -rng.randint(1, 3)), -rng.randint(1, 4)
    best, a, b, (i0, i1, j0, j1), _ = smith_waterman(s, t, sub, gap)
    assert best == local_by_definition(s, t, sub, gap) >= 0
    assert rescore(a, b, sub, gap) == best
    assert a.replace(GAP, "") == s[i0:i1] and b.replace(GAP, "") == t[j0:j1]
print("200 random pairs: SW score = best global score over all substring pairs")
```

```text
       -  T  A  C  G  G  A  C  C  T  C
   -   0  0  0  0  0  0  0  0  0  0  0
   C   0  0  0  2  0  0  0  2  2  0  2
   A   0  0  2  0  1  0  2  0  1  1  0
   G   0  0  0  1  2  3  1  1  0  0  0
   A   0  0  2  0  0  1  5  3  1  0  0
   C   0  0  0  4  2  0  3  7  5  3  2
   G   0  0  0  2  6  4  2  5  6  4  2
   G   0  0  0  0  4  8  6  4  4  5  3
   T   0  2  0  0  2  6  7  5  3  6  4
   A   0  0  4  2  0  4  8  6  4  4  5
   C   0  0  2  6  4  2  6 10  8  6  6
   G   0  0  0  4  8  6  4  8  9  7  5
10 ACGGTAC ACGG-AC s[3:10] t[1:7] global: 0
200 random pairs: SW score = best global score over all substring pairs
```

The tests check, on 200 random pairs and scoring schemes, that the score equals the definition, that it is never negative, and that the returned rows rescore to it and spell the reported segments.

## Worked example

> [!example] A shared segment in unrelated flanks: `CAGACGGTACG` against `TACGGACCTC` (invented), match +2, mismatch −1, gap −2
> ![[smith-waterman-dp-table.svg]]
> 1. **Borders and floor**: row 0 and column 0 are 0, and scattered single matches score 2 then fall back to 0. 36 of the 110 inner cells are floored at 0.
> 2. **A ridge forms** along the shared segment: $H(4, 2) = 2$ (A/A), $H(5, 3) = 4$ (C/C), $H(6, 4) = 6$ (G/G), $H(7, 5) = 8$ (G/G).
> 3. **A gap**: at $(8, 5)$ the T of $s$ has no partner. The diagonal gives $H(7, 4) - 1 = 3$, the left move $H(8, 4) - 2 = 0$, the vertical move $H(7, 5) - 2 = 6$: T faces a gap.
> 4. **The ridge resumes**: $H(9, 6) = 8$ (A/A) and $H(10, 7) = 10$ (C/C), the maximum of the table.
> 5. **Traceback** from $(10, 7)$ to the first zero, $H(3, 1) = 0$: segments `s[3:10]` = ACGGTAC and `t[1:7]` = ACGGAC, aligned as `ACGGTAC` over `ACGG-AC`, score $6 \times 2 - 2 = 10$.
> 6. **Contrast**: the global alignment of the full sequences scores 0, because the flanks cost about what the shared segment earns.

## Limitations

> [!warning] Quadratic cost in database search
> Comparing a query of length $m$ with a database of $N$ residues fills $mN$ cells. Heuristics such as BLAST look for short word matches and extend them, trading the guarantee of the optimal local alignment for speed, and attach a statistical significance to the segment pairs they report.[^blast]

> [!warning] A local score is not a significance
> The best local score of two unrelated sequences grows with their lengths, and biased composition inflates it. Judge hits by their [[E-Value]] and mask [[Low-Complexity Region|low-complexity regions]]; the thresholds for inferring homology are in [[Sequence Homology]].

> [!warning] The scoring scheme must keep alignments local
> A negative expected score per random pair is required,[^durbin] but with gaps it is not sufficient: cheap gaps let an aligner dodge mismatches, and local alignments of unrelated sequences become long again (Exercise 3).

> [!warning] One answer per run
> The algorithm reports a single best segment pair. A repeated domain or a second region of similarity needs further runs, for example after masking the first hit (Exercise 4).

## Variants and successors

- [[Gotoh Algorithm]]: affine gaps with three tables; the local version floors every table at zero in the same way.
- [[Semi-Global Alignment]]: free end gaps without a zero floor, for reads against genomes and overlapping reads (Exercise 2 shows the difference).
- [[Seed and Extend]] and [[BLAST]]: exact dynamic programming only around short exact or high-scoring word matches.[^blast]
- [[PSI-BLAST]] and [[Profile Hidden Markov Model|profile HMMs]]: local alignment of a sequence to a model of a whole family.

## Advanced (L3)

- **Local is global on the best substrings**, as the test oracle encodes: every property of global alignment (traceback, co-optimal paths, linear space) carries over once the two segments are known.
- **Linear space.** A score-only pass with two rows finds the best score and its end cell. Because the local alignment is a global alignment of two segments, a second pass on the reversed prefixes finds the start, and the segments are then aligned globally in linear space ([[Hirschberg Algorithm]]).
- **Where the zero puts the boundary.** Removing the floor while keeping zero borders still lets an alignment start at the beginning of either sequence for free, but no longer anywhere inside: that is a semi-global flavour, and on the worked example it loses a point (Exercise 2).
- **From scores to statistics.** For ungapped local alignments of random sequences (maximal segment pairs) with a negative expected score, the best score has a known distribution, which BLAST used from the start to report the significance of its hits ([[E-Value]]).[^blast]

## Frontier (M1)

- **Exact search at hardware speed.** In the recurrence, a cell depends only on its left, upper and diagonal neighbours, so whole groups of cells can be updated together. Farrar's striped layout of the query across SIMD vector registers made Smith-Waterman 2 to 8 times faster than earlier SIMD implementations, above 3 billion cell updates per second on a 2.0 GHz Core 2 Duo processor.[^farrar]
- **Exact alignment inside heuristics.** Seed-and-extend search restricts alignment to the neighbourhood of its seeds ([[Seed and Extend]]); there, the problem is small enough for exact dynamic programming, so the quadratic algorithm survives as an inner step of fast search.

## Exercises

> [!question] Exercise 1 (L2)
> Fill the Smith-Waterman table of `GTTAC` (rows) against `TTGC` (columns) with match +2, mismatch −1, gap −2. Find the maximum, trace back, and give the local alignment with its coordinates.

> [!success]- Solution
> ```text
>        -  T  T  G  C
>    -   0  0  0  0  0
>    G   0  0  0  2  0
>    T   0  2  2  0  1
>    T   0  2  4  2  0
>    A   0  0  2  3  1
>    C   0  0  0  1  5
> ```
> The maximum is $H(5, 4) = 5$. Traceback: C/C from $H(4, 3) = 3$, A/G mismatch from $H(3, 2) = 4$, T/T from $H(2, 1) = 2$, T/T from $H(1, 0) = 0$: stop. Alignment `TTAC` over `TTGC`, segments `s[1:5]` and `t[0:4]`, score $3 \times 2 - 1 = 5$: a mismatch inside a local alignment is kept when the matches after it pay for it.

> [!question] Exercise 2 (L3, Python)
> Remove the 0 from the maximum but keep the zero borders, and compute the best cell on the worked example. Which problem does this variant solve, and why is its score lower?

> [!success]- Solution
> ```python
> def no_floor_best(s: str, t: str, sub, gap: int) -> int:
>     """Same recurrence and zero borders, but without the 0 inside the max."""
>     H = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
>     for i in range(1, len(s) + 1):
>         for j in range(1, len(t) + 1):
>             H[i][j] = max(H[i - 1][j - 1] + sub(s[i - 1], t[j - 1]), H[i - 1][j] + gap, H[i][j - 1] + gap)
>     return max(max(row) for row in H)
>
> print(no_floor_best("CAGACGGTACG", "TACGGACCTC", simple(2, -1), -2))
> ```
> Output: `9`, against 10 for Smith-Waterman. Zero borders let an alignment start after a free prefix of *one* sequence, but it must then begin at the first residue of the other. The shared segment starts inside both sequences, so the best this variant can do is to include the leading T of $t$ as a mismatch (−1). That is the free-leading-gap half of [[Semi-Global Alignment]], not local alignment.

> [!question] Exercise 3 (L3, Python)
> Align 20 pairs of random 100-nt sequences under three schemes, $+1/-1/-2$, $+2/-1/-2$ (the worked example) and $+1/0/-2$ (match, mismatch, gap), and report the mean local alignment length with the expected score of a random pair. What do you conclude?

> [!success]- Solution
> ```python
> rng = random.Random(1)
> for match, mismatch, gap in ((1, -1, -2), (2, -1, -2), (1, 0, -2)):
>     lengths = []
>     for _ in range(20):
>         x = "".join(rng.choices("ACGT", k=100))
>         y = "".join(rng.choices("ACGT", k=100))
>         lengths.append(len(smith_waterman(x, y, simple(match, mismatch), gap)[1]))
>     expected = 0.25 * match + 0.75 * mismatch          # uniform random bases
>     print(f"{match:+d}/{mismatch:+d}/{gap:+d}: E = {expected:+.2f}, mean local length {sum(lengths) / 20:.1f} of 100")
> ```
> ```text
> +1/-1/-2: E = -0.50, mean local length 15.3 of 100
> +2/-1/-2: E = -0.25, mean local length 92.3 of 100
> +1/+0/-2: E = +0.25, mean local length 92.5 of 100
> ```
> With a clearly negative expected score, unrelated sequences give short local alignments, as intended. With a positive one, the "local" alignment covers almost everything. The worked example's scheme is in between: its ungapped expected score is negative, yet with gaps costing only 2 the aligner skips mismatches cheaply and random alignments are long. It is fine for a toy table, too permissive for a search: gap costs must be judged together with the substitution scores.

> [!question] Exercise 4 (L3, Python)
> Find a second, non-overlapping local alignment in the worked example by masking the first hit of $s$ with `N` and rerunning.

> [!success]- Solution
> ```python
> masked = "CAG" + "N" * 7 + "G"            # hide the first hit s[3:10]
> print(smith_waterman(masked, "TACGGACCTC", simple(2, -1), -2)[:4])
> ```
> Output: `(3, 'CAG', 'CGG', (0, 3, 2, 5))`: `CAG` over `CGG`, score 3, far below 10. Masking one sequence is the simplest way to list several local alignments; it misses hits that overlap the masked segment, which is why tools use more careful schemes.

> [!question] Exercise 5 (M1)
> Show that all cells on an anti-diagonal $i + j = k$ can be computed at the same time. How many sequential steps does a fully parallel computation need, and why do practical SIMD versions such as Farrar's use another layout?

> [!success]- Solution
> $H(i, j)$ depends on $(i-1, j-1)$, $(i-1, j)$ and $(i, j-1)$, whose index sums are $k - 2$ and $k - 1$: all inputs of anti-diagonal $k$ lie on the two previous ones, so its cells are independent. With unlimited processors, $n + m - 1$ steps suffice instead of $nm$. But anti-diagonals have varying lengths and their cells are not contiguous in a table stored row by row, which complicates vectorization; Farrar instead laid the query out in stripes across SIMD registers and obtained a 2 to 8 times speed-up over other SIMD implementations.[^farrar]

## Mastery checklist

- [ ] 1 Recognized: I can state the local alignment problem and say what the zero in the recurrence does.
- [ ] 2 Understood: I can fill a small table by hand, find the maximum, trace back to the first zero and explain why the expected score must be negative.
- [ ] 3 Practiced: I implemented it from scratch and tested it against the substring definition on random inputs.
- [ ] 4 Applied: in [[04-alignment-engine]], I found a shared domain between two real multidomain proteins with BLOSUM62 and compared the result with a BLAST hit for the same pair.
- [ ] 5 Explained: I can explain why BLAST approximates it, how the scoring scheme keeps alignments local, how to find several hits, and how SIMD implementations make exact search fast.

## References

[^sw]: [[Smith 1981 - Identification of Common Molecular Subsequences]], *Journal of Molecular Biology* 147:195-197.
[^durbin]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment" (local alignment, the condition of a negative expected score).
[^blast]: [[Altschul 1990 - Basic Local Alignment Search Tool]], *Journal of Molecular Biology* 215(3):403-410.
[^farrar]: [[Farrar 2007 - Striped Smith-Waterman Speeds Database Searches Six Times over Other SIMD Implementations]], *Bioinformatics* 23(2):156-161.
