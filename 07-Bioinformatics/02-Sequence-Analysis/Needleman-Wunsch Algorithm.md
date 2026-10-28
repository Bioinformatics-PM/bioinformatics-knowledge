---
aliases:
  - Needleman-Wunsch
  - NW Algorithm
  - Global Alignment Algorithm
  - Algorithme de Needleman-Wunsch
tags:
  - type/algorithm
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Sequence Alignment]]"
  - "[[Dynamic Programming]]"
  - "[[Substitution Matrix]]"
  - "[[Gap Penalty]]"
  - "[[Big O Notation]]"
related:
  - "[[Smith-Waterman Algorithm]]"
  - "[[Semi-Global Alignment]]"
  - "[[Gotoh Algorithm]]"
  - "[[Hirschberg Algorithm]]"
  - "[[Edit Distance]]"
  - "[[Longest Common Subsequence]]"
  - "[[Directed Acyclic Graph]]"
  - "[[Progressive Alignment]]"
  - "[[Pair Hidden Markov Model]]"
projects:
  - "[[04-alignment-engine]]"
  - "[[bio-algorithms]]"
sources:
  - "[[Needleman 1970 - Search for Similarities in Amino Acid Sequences]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[An Introduction to Bioinformatics Algorithms (Jones)]]"
  - "[[Smith 1981 - Identification of Common Molecular Subsequences]]"
  - "[[Altschul 1985 - Significance of Nucleotide Sequence Alignments]]"
  - "[[Marco-Sola 2021 - Fast Gap-Affine Pairwise Alignment Using the Wavefront Algorithm]]"
---

# Needleman-Wunsch Algorithm

> [!abstract]
> Needleman-Wunsch finds an optimal global alignment of two sequences by filling a table with the best score of every pair of prefixes, each cell from three neighbours, then tracing back the path that produced the final score.

## Problem

- **Input**: sequences $s = s_1 \dots s_n$ and $t = t_1 \dots t_m$ over an alphabet $\Sigma$, a substitution score $\sigma(a, b)$ ([[Substitution Matrix]]) and a linear gap penalty $d > 0$ per gap column ([[Gap Penalty]]).
- **Output**: the maximal score of an alignment of $s$ and $t$ from end to end, and one alignment that achieves it ([[Sequence Alignment]]).
- **Biological use**: comparing two sequences homologous over their whole length, such as orthologous proteins of similar length ([[Ortholog]]), a predicted protein and its reference, or two alleles of a gene. Needleman and Wunsch introduced the method in 1970 to search for similarities in the amino acid sequences of two proteins,[^nw] and exact dynamic programming remains the reference that faster heuristics are tested against. [[04-alignment-engine]] implements it with traceback and a visualized table; the tested version is shared in [[bio-algorithms]].

## Intuition

Look at the last column of an optimal alignment of $s$ and $t$. It can only be $s_n$ paired with $t_m$, $s_n$ facing a gap, or $t_m$ facing a gap. Remove that column: what remains is an alignment of shorter prefixes, and it must itself be optimal, otherwise replacing it by a better one would improve the whole. So the best score for the full sequences follows from the best scores of three pairs of prefixes, and those from smaller ones. Solve all $(n + 1)(m + 1)$ prefix pairs once, smallest first, and store them in a table ([[Dynamic Programming]]). In the grid picture of [[Sequence Alignment]], this computes the heaviest path from the top-left to the bottom-right corner, one cell at a time.[^compeau]

## Mathematical formulation

Let $F(i, j)$ be the best score of an alignment of the prefixes $s_1 \dots s_i$ and $t_1 \dots t_j$.[^durbin]

**Base cases.** A prefix aligned with the empty string can only face gaps:
$$F(0, 0) = 0, \qquad F(i, 0) = -i d, \qquad F(0, j) = -j d.$$

**Recurrence**, for $1 \le i \le n$ and $1 \le j \le m$:
$$F(i, j) = \max\begin{cases} F(i-1, j-1) + \sigma(s_i, t_j) & \text{pair } (s_i, t_j)\\ F(i-1, j) - d & s_i \text{ against a gap}\\ F(i, j-1) - d & t_j \text{ against a gap}\end{cases}$$

The optimal global score is $F(n, m)$.[^durbin]

**Correctness**, by induction on $i + j$. Base cases: the only alignment of $s_1 \dots s_i$ with the empty string has $i$ gap columns. Step: every alignment of the two prefixes ends with one of the three column types; its score is the score of that column plus the score of an alignment of the corresponding shorter prefixes, at most their $F$ by the induction hypothesis. Each of the three bounds is reached by appending the column to an optimal shorter alignment, so the maximum of the three is $F(i, j)$.

**Traceback.** From $(n, m)$, move to a predecessor whose value plus the step score equals the current value, emitting the column: diagonal, $(s_i, t_j)$; up, $(s_i, -)$; left, $(-, t_j)$. Stop at $(0, 0)$ and reverse the columns.[^durbin] When several predecessors qualify, each choice leads to a co-optimal alignment; the order of preference (here diagonal, then up, then left) is a convention.

## Algorithm

```text
NEEDLEMAN-WUNSCH(s, t, σ, d)
  for i in 0..n: F[i][0] ← -i·d
  for j in 0..m: F[0][j] ← -j·d
  for i in 1..n:                       # any order in which the three predecessors are ready
    for j in 1..m:
      F[i][j] ← max(F[i-1][j-1] + σ(s[i], t[j]),  F[i-1][j] - d,  F[i][j-1] - d)
  (i, j) ← (n, m);  columns ← []
  while i > 0 or j > 0:
    if i > 0 and j > 0 and F[i][j] = F[i-1][j-1] + σ(s[i], t[j]):  emit (s[i], t[j]); i ← i-1; j ← j-1
    else if i > 0 and F[i][j] = F[i-1][j] - d:                    emit (s[i], -);    i ← i-1
    else:                                                          emit (-, t[j]);    j ← j-1
  return F[n][m], reversed(columns)
```

## Complexity

| | Time | Space |
|---|---|---|
| Needleman-Wunsch, score and alignment | $O(nm)$ | $O(nm)$ |
| Score only, two rows kept | $O(nm)$ | $O(\min(n, m))$ |
| [[Hirschberg Algorithm]], alignment by divide and conquer[^jones] | $O(nm)$ | $O(n + m)$ |
| Banded, cells with $\lvert i - j \rvert \le k$ | $O(k \max(n, m))$ | $O(k \max(n, m))$ |
| Wavefront alignment (WFA), gap-affine, $s$ = alignment score[^wfa] | $O(ns)$ | $O(s^2)$ |

Each of the $(n + 1)(m + 1)$ cells costs a constant number of operations, and the traceback adds $O(n + m)$. The banded version is exact only when an optimal path stays inside the band (Exercise 5).

## Implementation

Standard library only. The substitution score is a function, so a DNA match/mismatch scheme and a protein matrix plug in the same way. Tests compare the result with a brute-force enumeration of every alignment on random small inputs.

```python
import random

GAP = "-"

def needleman_wunsch(s: str, t: str, sub, gap: int):
    """Optimal global alignment of s and t with a linear gap score `gap` (< 0).

    sub(a, b) returns the substitution score. Returns (score, row_s, row_t, F).
    """
    n, m = len(s), len(t)
    F = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):                      # first column: s[:i] against gaps
        F[i][0] = i * gap
    for j in range(1, m + 1):                      # first row: t[:j] against gaps
        F[0][j] = j * gap
    for i in range(1, n + 1):                      # fill row by row
        for j in range(1, m + 1):
            F[i][j] = max(F[i - 1][j - 1] + sub(s[i - 1], t[j - 1]),   # diagonal
                          F[i - 1][j] + gap,                            # up: gap in t
                          F[i][j - 1] + gap)                            # left: gap in s
    a, b, i, j = [], [], n, m                      # traceback from the corner
    while i > 0 or j > 0:
        if i > 0 and j > 0 and F[i][j] == F[i - 1][j - 1] + sub(s[i - 1], t[j - 1]):
            a.append(s[i - 1]); b.append(t[j - 1]); i, j = i - 1, j - 1
        elif i > 0 and F[i][j] == F[i - 1][j] + gap:
            a.append(s[i - 1]); b.append(GAP); i -= 1
        else:
            a.append(GAP); b.append(t[j - 1]); j -= 1
    return F[n][m], "".join(reversed(a)), "".join(reversed(b)), F

def simple(match: int = 1, mismatch: int = -1):
    return lambda x, y: match if x == y else mismatch

def rescore(a: str, b: str, sub, gap: int) -> int:
    return sum(gap if GAP in (x, y) else sub(x, y) for x, y in zip(a, b))

def all_alignments(s: str, t: str):
    """Brute-force oracle: every alignment of s and t (tiny inputs only)."""
    if not s and not t:
        yield "", ""
        return
    if s and t:
        for a, b in all_alignments(s[1:], t[1:]):
            yield s[0] + a, t[0] + b
    if s:
        for a, b in all_alignments(s[1:], t):
            yield s[0] + a, GAP + b
    if t:
        for a, b in all_alignments(s, t[1:]):
            yield GAP + a, t[0] + b

def show(F, s: str, t: str) -> None:
    print("     " + "".join(f"{c:>4}" for c in GAP + t))
    for i, row in enumerate(F):
        print(f"{(GAP + s)[i]:>4} " + "".join(f"{v:>4}" for v in row))

# Worked example (invented pair, also used in Sequence Alignment)
score, a, b, F = needleman_wunsch("TACGGT", "ACGGTA", simple(1, -1), -2)
show(F, "TACGGT", "ACGGTA")
print(score, a, b, sep="\n")

# Tests: brute-force oracle, consistent traceback, symmetry, edit distance
rng = random.Random(42)
for _ in range(300):
    s = "".join(rng.choices("ACGT", k=rng.randint(0, 6)))
    t = "".join(rng.choices("ACGT", k=rng.randint(0, 6)))
    sub, gap = simple(rng.randint(1, 3), -rng.randint(0, 3)), -rng.randint(1, 4)
    best, a, b, _ = needleman_wunsch(s, t, sub, gap)
    assert best == max(rescore(x, y, sub, gap) for x, y in all_alignments(s, t))
    assert rescore(a, b, sub, gap) == best and a.replace(GAP, "") == s and b.replace(GAP, "") == t
    assert best == needleman_wunsch(t, s, sub, gap)[0]
print("300 random pairs: DP score = brute-force optimum")
print("edit distance kitten/sitting:", -needleman_wunsch("kitten", "sitting", simple(0, -1), -1)[0])
```

```text
        -   A   C   G   G   T   A
   -    0  -2  -4  -6  -8 -10 -12
   T   -2  -1  -3  -5  -7  -7  -9
   A   -4  -1  -2  -4  -6  -8  -6
   C   -6  -3   0  -2  -4  -6  -8
   G   -8  -5  -2   1  -1  -3  -5
   G  -10  -7  -4  -1   2   0  -2
   T  -12  -9  -6  -3   0   3   1
1
TACGGT-
-ACGGTA
300 random pairs: DP score = brute-force optimum
edit distance kitten/sitting: 3
```

The tests check four properties on 300 random pairs and random scoring schemes: the score equals the brute-force optimum, the returned alignment spells both sequences and rescores to the same value, and swapping the sequences leaves the score unchanged. The last line uses match 0, mismatch −1 and gap −1, for which $-F(n, m)$ is the [[Edit Distance]].

## Worked example

> [!example] `TACGGT` against `ACGGTA` (invented), match +1, mismatch −1, gap −2
> ![[needleman-wunsch-dp-table.svg]]
> 1. **Initialize**: row 0 and column 0 hold $-2j$ and $-2i$, the cost of aligning a prefix with gaps only.
> 2. **Fill**, row by row. $F(1, 1)$, T against A: $\max(0 - 1, -2 - 2, -2 - 2) = -1$. $F(3, 2)$, C against C: $\max(F(2, 1) + 1, F(2, 2) - 2, F(3, 1) - 2) = \max(0, -4, -5) = 0$. Along the matching letters ACGGT the diagonal climbs: $F(4, 3) = 1$, $F(5, 4) = 2$, $F(6, 5) = 3$.
> 3. **Last cell**: $F(6, 6) = \max(F(5, 5) - 1, F(5, 6) - 2, F(6, 5) - 2) = \max(-1, -4, 1) = 1$, reached from the left: the last column is $(-, \mathrm{A})$.
> 4. **Traceback**: $(6,6) \to (6,5) \to (5,4) \to (4,3) \to (3,2) \to (2,1) \to (1,0) \to (0,0)$: one left move, five diagonal moves, one up move.
> 5. **Result**: `TACGGT-` over `-ACGGTA`, score $5 \times 1 - 2 \times 2 = 1$: the unique optimum that the enumeration of all 8,989 alignments found in [[Sequence Alignment#Worked example]], obtained here from 49 cells.

## Limitations

> [!warning] End-to-end assumption
> Global alignment forces every residue into the alignment. When two proteins share only a domain, or a read covers part of a gene, the unrelated ends are paid for with gaps and mismatches and can distort the core alignment. Use [[Smith-Waterman Algorithm|local]] or [[Semi-Global Alignment|semi-global]] alignment instead.

> [!warning] Linear gaps
> With a linear penalty a multi-residue indel costs the same split or contiguous, so gaps tend to scatter ([[Gap Penalty]]). Affine gaps need three tables ([[Gotoh Algorithm]]).

> [!warning] Quadratic memory
> Two 100 kb sequences need $10^{10}$ cells: 10 GB with one byte of traceback per cell. Keep two rows for the score, recover the alignment in linear space ([[Hirschberg Algorithm]]), or restrict the computation to a band.

> [!warning] An optimum is not evidence of homology
> The algorithm returns an optimal alignment for any pair, related or not. Whether the score is surprising needs a null model, for example scores of shuffled sequences that keep the composition of the originals.[^altschul85]

## Variants and successors

- **Other modes, same table**: [[Smith-Waterman Algorithm]] (local alignment: scores floored at zero, traceback from the maximum cell)[^sw] and [[Semi-Global Alignment]] (free end gaps: zero first row and column, answer taken in the last row or column).
- **Other gap and memory models**: [[Gotoh Algorithm]] (affine gaps in $O(nm)$ with three tables) and [[Hirschberg Algorithm]] (the same alignment in linear space).[^jones]
- **Special cases and descendants**: [[Edit Distance]] (unit costs), [[Longest Common Subsequence]] (match 1, mismatches and gaps 0), [[Progressive Alignment]] (multiple alignment built from pairwise dynamic programming) and [[Pair Hidden Markov Model]] (the probabilistic version).

## Advanced (L3)

- **The table is a directed acyclic graph.** Cells are vertices, the three moves are weighted edges, and the algorithm computes a heaviest path in topological order ([[Directed Acyclic Graph]], [[Topological Sort]]).[^compeau] Any order that computes a cell after its three predecessors is valid: row by row, column by column, or anti-diagonal by anti-diagonal, the order that parallel hardware exploits since the cells of one anti-diagonal are independent.
- **Counting co-optimal alignments.** Ties are common, especially in repeats, and the traceback returns only one of the co-optimal alignments. To count them, replace max by "add the counts of every predecessor that achieves the max": $N(i, j) = \sum N(\text{tied predecessor})$, with $N = 1$ on the borders (Exercise 4).
- **Linear space.** The score needs only two rows. To recover the alignment, Hirschberg's divide and conquer computes forward scores to the middle row and backward scores from the end, finds where an optimal path crosses the middle row, and recurses on the two halves, in $O(nm)$ time (about twice one pass) and linear space.[^jones] For two 100 kb sequences this replaces a $10^{10}$-cell table by a few rows of $10^5$ cells.
- **The 1970 version.** Needleman and Wunsch's original scoring and gap treatment differ from today's formulation with linear or affine gap costs; textbooks present the modern recurrence.[^nw]

## Frontier (M1)

- **Exact but no longer quadratic.** The wavefront algorithm (WFA) computes the optimal gap-affine alignment in $O(ns)$ time and $O(s^2)$ memory, where $s$ is the alignment score: nearly linear when the sequences are similar. Its authors report speed-ups of 20 to 300 times over other methods on short Illumina-like reads and 10 to 100 times on long noisy reads.[^wfa] It shows that "exact" and "fast" are not opposed when the divergence is low.
- **From one path to probabilities.** Recasting alignment as a pair hidden Markov model replaces the maximum over alignments by a sum, and gives for each pair of residues the posterior probability that they are aligned, a measure of reliability that a single optimal path cannot provide ([[Pair Hidden Markov Model]]).[^durbin4]

## Exercises

> [!question] Exercise 1 (L2)
> Fill by hand the table for `GCA` (rows) against `GA` (columns) with match +1, mismatch −1, gap −2, then trace back an optimal alignment.

> [!success]- Solution
> ```text
>         -   G   A
>    -    0  -2  -4
>    G   -2   1  -1
>    C   -4  -1   0
>    A   -6  -3   0
> ```
> $F(3, 2) = 0$ comes from the diagonal (A/A, $-1 + 1$), $F(2, 1) = -1$ from above (C against a gap, $1 - 2$), $F(1, 1) = 1$ from the diagonal (G/G). Alignment `GCA` over `G-A`, score $1 - 2 + 1 = 0$; `needleman_wunsch("GCA", "GA", simple(1, -1), -2)` returns the same.

> [!question] Exercise 2 (L2)
> Why do row 0 and column 0 hold $-jd$ and $-id$ rather than 0? What problem would you solve by setting them to 0?

> [!success]- Solution
> $F(i, 0)$ is the score of aligning $s_1 \dots s_i$ with nothing, which is possible only with $i$ gap columns. With zeros, leading gaps would become free: the alignment could skip a prefix of either sequence at no cost, which is one half of [[Semi-Global Alignment]] (taking the maximum over the last row and column frees the trailing gaps too).

> [!question] Exercise 3 (L2, Python)
> With match 0, mismatch −1 and gap −1, compute the edit distance of `GATTACA` and `GCATGCT` and print an optimal transcript. Explain why $-F(n, m)$ is the edit distance. Is the transcript unique?

> [!success]- Solution
> ```python
> score, a, b, _ = needleman_wunsch("GATTACA", "GCATGCT", simple(0, -1), -1)
> print(-score, a, b, sep="\n")
> ```
> ```text
> 4
> GATTACA
> GCATGCT
> ```
> Every column that is not a match costs exactly 1, so the alignment score is minus the number of substitutions, insertions and deletions, and maximizing it minimizes the number of edits ([[Edit Distance]]). Not unique: `G-ATTACA` over `GCAT-GCT` also costs 4 (one insertion, one deletion, two substitutions); the traceback preference picked four substitutions.

> [!question] Exercise 4 (L3, Python)
> Count the co-optimal global alignments of `TACGGT`/`ACGGTA` (gap −2), `ACCT`/`ACT` (gap −2) and `AAAA`/`AA` (gap −1), match +1 and mismatch −1.

> [!success]- Solution
> ```python
> def count_optimal(s: str, t: str, sub, gap: int) -> int:
>     """Number of co-optimal global alignments: add up the counts of every tied predecessor."""
>     _, _, _, F = needleman_wunsch(s, t, sub, gap)
>     N = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
>     for i in range(len(s) + 1):
>         for j in range(len(t) + 1):
>             if i == 0 or j == 0:
>                 N[i][j] = 1                     # a single all-gap path along the border
>                 continue
>             N[i][j] = ((F[i][j] == F[i - 1][j - 1] + sub(s[i - 1], t[j - 1])) * N[i - 1][j - 1]
>                        + (F[i][j] == F[i - 1][j] + gap) * N[i - 1][j]
>                        + (F[i][j] == F[i][j - 1] + gap) * N[i][j - 1])
>     return N[-1][-1]
>
> print(count_optimal("TACGGT", "ACGGTA", simple(1, -1), -2), count_optimal("ACCT", "ACT", simple(1, -1), -2),
>       count_optimal("AAAA", "AA", simple(1, -1), -1))
> ```
> Output: `1 2 6`. The worked example has a unique optimum; in `ACCT`/`ACT` the gap can face either C; in `AAAA`/`AA` any 2 of the 4 A's can be paired, $\binom{4}{2} = 6$. Repeats multiply co-optimal alignments.

> [!question] Exercise 5 (M1, Python)
> Write a banded version that only computes cells with $\lvert i - j \rvert \le k$. Run it on the worked example for $k = 0, 1, 2$, then on `GGGGAAAACCCC`/`AAAACCCCGGGG` with $k = 2$, and compare with the full algorithm. When is banding exact?

> [!success]- Solution
> ```python
> def banded_nw_score(s: str, t: str, sub, gap: int, k: int) -> float:
>     """Needleman-Wunsch restricted to cells with |i - j| <= k (others are unreachable)."""
>     NEG = float("-inf")
>     F = [[NEG] * (len(t) + 1) for _ in range(len(s) + 1)]
>     for i in range(len(s) + 1):
>         for j in range(max(0, i - k), min(len(t), i + k) + 1):
>             if i == 0 or j == 0:
>                 F[i][j] = (i + j) * gap
>             else:
>                 F[i][j] = max(F[i - 1][j - 1] + sub(s[i - 1], t[j - 1]), F[i - 1][j] + gap, F[i][j - 1] + gap)
>     return F[-1][-1]
>
> print([banded_nw_score("TACGGT", "ACGGTA", simple(1, -1), -2, k) for k in (0, 1, 2)])
> print(banded_nw_score("GGGGAAAACCCC", "AAAACCCCGGGG", simple(1, -1), -2, 2),
>       needleman_wunsch("GGGGAAAACCCC", "AAAACCCCGGGG", simple(1, -1), -2)[0])
> ```
> ```text
> [-4, 1, 1]
> -10 -8
> ```
> With $k = 0$ no gap is possible (score −4); from $k = 1$ the band contains the optimal path, whose cells all satisfy $\lvert i - j \rvert \le 1$. In the second pair the optimal alignment shifts by 4 positions (−8), outside a band of 2 (−10). Banding is exact when an optimal path stays in the band, which holds for similar sequences with few net indels; the guarantee must come from a bound on the indels, otherwise banding is a heuristic.

## Mastery checklist

- [ ] 1 Recognized: I can state the global alignment problem and the three cases of the recurrence.
- [ ] 2 Understood: I can prove the recurrence correct, fill a small table by hand and trace back an alignment.
- [ ] 3 Practiced: I implemented it from scratch, with a brute-force oracle, symmetry and edit-distance tests.
- [ ] 4 Applied: in [[04-alignment-engine]], I aligned real orthologous proteins with BLOSUM62, visualized the table and measured time and memory as the length grows.
- [ ] 5 Explained: I can explain when global alignment is the wrong model, the memory problem and its solutions (linear space, banding), and what WFA and pair HMMs add.

## References

[^nw]: [[Needleman 1970 - Search for Similarities in Amino Acid Sequences]], *Journal of Molecular Biology* 48:443-453.
[^durbin]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment" (global alignment by dynamic programming, traceback).
[^durbin4]: [[Biological Sequence Analysis (Durbin)]], ch. 4 "Pairwise alignment using HMMs".
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Compare Biological Sequences?" (alignment graph, longest paths in a DAG).
[^jones]: [[An Introduction to Bioinformatics Algorithms (Jones)]], space-efficient alignment by divide and conquer.
[^sw]: [[Smith 1981 - Identification of Common Molecular Subsequences]], *Journal of Molecular Biology* 147:195-197.
[^altschul85]: [[Altschul 1985 - Significance of Nucleotide Sequence Alignments]], *Molecular Biology and Evolution* 2(6):526-538.
[^wfa]: [[Marco-Sola 2021 - Fast Gap-Affine Pairwise Alignment Using the Wavefront Algorithm]], *Bioinformatics* 37(4):456-463.
