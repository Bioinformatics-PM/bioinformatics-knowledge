---
aliases:
  - Pairwise Alignment
  - Pairwise Sequence Alignment
  - Alignment
  - Global Alignment
  - Local Alignment
  - Alignement de séquences
tags:
  - type/concept
  - domain/bioinformatics
  - domain/computer-science
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Sequence Homology]]"
  - "[[Dot Plot]]"
  - "[[Hamming Distance]]"
  - "[[Indel]]"
  - "[[Point Mutation]]"
related:
  - "[[Dynamic Programming]]"
  - "[[Edit Distance]]"
  - "[[Needleman-Wunsch Algorithm]]"
  - "[[Smith-Waterman Algorithm]]"
  - "[[Semi-Global Alignment]]"
  - "[[Substitution Matrix]]"
  - "[[Gap Penalty]]"
  - "[[BLAST]]"
  - "[[E-Value]]"
  - "[[Multiple Sequence Alignment]]"
  - "[[Read Mapping]]"
  - "[[Directed Acyclic Graph]]"
projects:
  - "[[04-alignment-engine]]"
  - "[[05-sequence-search]]"
  - "[[bio-algorithms]]"
  - "[[bio-visualization]]"
sources:
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Algorithms on Strings, Trees, and Sequences (Gusfield)]]"
  - "[[Needleman 1970 - Search for Similarities in Amino Acid Sequences]]"
  - "[[Smith 1981 - Identification of Common Molecular Subsequences]]"
  - "[[Altschul 1990 - Basic Local Alignment Search Tool]]"
  - "[[Pearson 2013 - An Introduction to Sequence Similarity Searching]]"
  - "[[Coursera UCSD - Bioinformatics Specialization]]"
  - "[[MIT 6.047 - Computational Biology]]"
---

# Sequence Alignment

> [!abstract]
> Aligning two sequences means writing them one above the other, inserting gaps so that corresponding residues fall in the same column; a score adds up matches, mismatches and gaps, and the best-scoring alignment is our hypothesis of which residues descend from a common ancestor.

## Definition

A **pairwise alignment** of sequences $s$ and $t$ places them in two rows of equal length by inserting gap symbols (`-`), without reordering residues and without any column made of two gaps. Each column is a **match** (identical residues), a **mismatch** (substitution) or a **gap** (a residue facing a gap, an insertion or deletion). An alignment is **scored** by adding one term per column, rewarding matches and similar residues and penalizing mismatches and gaps; the goal of alignment algorithms is the alignment of maximal score.[^durbin][^compeau] For homologous sequences, the aligned columns are a hypothesis of positional homology: residues in the same column are proposed to descend from the same ancestral residue ([[Sequence Homology]]).[^durbin]

## Why it matters

- **The central operation of the field.** Database search ([[BLAST]]), read mapping ([[Read Mapping]], alignments stored in [[SAM Format]]), variant calling, [[Multiple Sequence Alignment]], phylogenetics and genome annotation all start from alignments, and every reference course treats it as a core unit.[^coursera][^mit]
- **An algorithmic milestone.** Needleman and Wunsch (1970) gave the first efficient method for a globally optimal alignment,[^nw] Smith and Waterman (1981) the local version,[^sw] and BLAST (1990) the heuristic that made searching whole databases practical, with a statistical measure of significance.[^blast] Together they are the textbook example of [[Dynamic Programming]] and of the trade-off between exactness and speed.
- **Lab.** [[04-alignment-engine]] implements scoring, global and local alignment with traceback; [[05-sequence-search]] builds a BLAST-like search on top; [[bio-visualization]] draws alignments and their matrices.

## Core (L1)

### Writing an alignment

```text
s  GA-TTACA
   || || ||
t  GACTT-CA
```

Reading column by column: G/G match, A/A match, `-`/C gap in $s$, T/T, T/T, A/`-` gap in $t$, C/C, A/A; the middle line marks identities. Removing the gaps from a row gives back its sequence exactly (every residue used once, in order), no column contains two gaps, and the common length $L$ satisfies $\max(|s|, |t|) \le L \le |s| + |t|$.

### Column types and what they mean

| Column | Example | Evolutionary reading |
|---|---|---|
| match | `A` over `A` | residue conserved since the common ancestor |
| mismatch | `A` over `G` | a substitution on one of the two lineages ([[Point Mutation]]) |
| gap | `A` over `-` | an insertion in one lineage **or** a deletion in the other: without a third sequence we cannot tell, hence the neutral word **indel** ([[Indel]]) |

### Scoring an alignment

With the simple scheme match $+1$, mismatch $-1$, gap $-2$ per gap column, the alignment above scores $6 \times (+1) + 2 \times (-2) = 2$. Changing the scheme changes the score, and can change which alignment is best (Worked example).

### Two special cases you already know

With no gaps allowed and $|s| = |t|$, there is a single alignment, and counting its mismatches is the [[Hamming Distance]]. Minimizing the number of substitutions, insertions and deletions is the [[Edit Distance]]: an alignment with cost 0 per match and 1 per mismatch or gap column is exactly an edit transcript.[^gusfield]

![[alignment-grid-path.svg]]

**Alignments are paths.** Put $s$ down the side and $t$ across the top of a grid, as in a [[Dot Plot]]. Every alignment is a path from the top-left to the bottom-right corner: a diagonal step aligns two residues, a vertical step aligns a residue of $s$ with a gap, a horizontal step a residue of $t$ with a gap. Finding the best alignment is finding the best path in this grid, a longest-path problem in a [[Directed Acyclic Graph]].[^compeau]

## Deeper (L2)

### Scoring schemes

A scheme has two parts.[^durbin]

- **Substitution scores** $\sigma(a, b)$ for aligning residue $a$ with $b$. For DNA, a match/mismatch pair such as $+1/-1$ is common. For proteins, scores come from a [[Substitution Matrix]] such as PAM or BLOSUM.
- **Gap penalties** $\gamma(g)$ for a gap of length $g$: **linear** $\gamma(g) = -g d$, or **affine** $\gamma(g) = -d - (g - 1)e$ with an opening cost $d$ larger than the extension cost $e$, so that one long gap is cheaper than several short ones ([[Gap Penalty]]).

Durbin and colleagues justify substitution scores as **log-odds**: $\sigma(a, b) = \log \dfrac{p_{ab}}{q_a q_b}$, where $p_{ab}$ is the probability of seeing $a$ and $b$ aligned in related sequences and $q_a, q_b$ are background frequencies. A positive score means "more likely under common ancestry than by chance", and adding scores over columns adds log-likelihood ratios, under the assumption that columns are independent.[^durbin]

### Three alignment modes (preview)

| Mode | Aligns | Typical use | Exact algorithm |
|---|---|---|---|
| **Global** | both sequences end to end | two homologous genes of similar length | [[Needleman-Wunsch Algorithm]][^nw] |
| **Local** | the best-scoring pair of segments, one from each | a shared domain inside unrelated contexts; database search | [[Smith-Waterman Algorithm]][^sw] |
| **Semi-global** | end to end, but gaps at the ends are free | a read fitted inside a genome; overlap of two reads | [[Semi-Global Alignment]] (fitting and overlap alignment)[^compeau] |

The same pair `TACGGT` / `ACGGTA` (invented) under the three modes, match $+1$, mismatch $-1$, gap $-2$:

```text
global          TACGGT-      5 matches, 2 end gaps: 5 - 4 = 1
                 |||||
                -ACGGTA

semi-global     TACGGT-      end gaps free: 5
                 |||||
                -ACGGTA

local            ACGGT       best segment pair only: 5
                 |||||
                 ACGGT
```

### Why an algorithm is needed

The number of alignments of two sequences explodes: it is the Delannoy number $D(n, m)$ (Mathematical representation), already 8,989 for two 6-mers, $8.1 \times 10^6$ for two 10-mers and about $2 \times 10^{75}$ for two sequences of 100 residues. Enumeration is hopeless beyond toy sizes. Dynamic programming finds an optimal path in $O(nm)$ time by reusing the best scores of prefixes, filling a matrix and tracing back from its end, which is what Needleman and Wunsch introduced ([[Dynamic Programming]]).[^nw] The algorithms have their own notes; this note only defines what they optimize.

## Advanced (L3)

- **Scores need statistics.** A score says how good an alignment is under a model, not whether it is surprising. For local alignments, the expected number of chance alignments with at least a given score in a search is the [[E-Value]]; BLAST attached such a measure to its hits from the start.[^blast] Inferring homology from an alignment uses thresholds on that value, stricter for DNA than for proteins.[^pearson]
- **Heuristics trade optimality for speed.** BLAST looks for short word matches above a threshold score and extends them into high-scoring segment pairs, instead of filling the full matrix.[^blast] Read mappers and whole-genome aligners use related seed-and-extend and anchor-chaining strategies ([[Seed and Extend]], [[Whole-Genome Alignment]]). The exact algorithms remain the reference against which heuristics are tested.
- **"The" alignment does not exist.** Different scoring schemes and modes give different optimal alignments, and one scheme often has several co-optimal alignments. In repeats, a gap can slide without changing the score (deleting one A from `AAAA` can be placed at four positions), so tools must choose a convention, such as the leftmost placement, for variants to be comparable ([[Indel]]).
- **Memory, not time, is often the limit.** The full matrix needs $O(nm)$ memory: $10^{10}$ cells for two 100 kb sequences. Divide and conquer recovers an optimal alignment in linear space ([[Hirschberg Algorithm]]); banded alignment restricts the matrix to a diagonal band when sequences are known to be similar.
- **Beyond two sequences and beyond scores.** Aligning many sequences at once is the harder [[Multiple Sequence Alignment]] problem; recasting alignment as a probabilistic model gives [[Pair Hidden Markov Model|pair HMMs]], which compute the probability that two residues are aligned instead of a single best path.[^durbin4]

## Mathematical representation

Let $\Sigma$ be an alphabet, $- \notin \Sigma$ the gap symbol, $s \in \Sigma^n$, $t \in \Sigma^m$.

- **Alignment.** A pair $(\hat{s}, \hat{t}) \in (\Sigma \cup \{-\})^L \times (\Sigma \cup \{-\})^L$ such that deleting all $-$ from $\hat{s}$ gives $s$, from $\hat{t}$ gives $t$, and no column $l$ has $\hat{s}_l = \hat{t}_l = -$.
- **Score with a linear gap penalty** $d > 0$ and substitution scores $\sigma$:
$$S(\hat{s}, \hat{t}) = \sum_{l=1}^{L} w(\hat{s}_l, \hat{t}_l), \qquad w(a, b) = \sigma(a, b),\quad w(a, -) = w(-, b) = -d.$$
With affine gaps, each maximal run of $g$ gap columns in the same row costs $-d - (g-1)e$ instead of $-gd$.
- **Log-odds scores** $\sigma(a, b) = \log \big(p_{ab} / (q_a q_b)\big)$, so $S$ is a log-likelihood ratio of a "related" model against a "random" model when columns are independent.[^durbin]
- **Optimal global alignment** $\max_{(\hat{s}, \hat{t})} S(\hat{s}, \hat{t})$. The **edit distance** is $\min$ of the cost with $\sigma(a, a) = 0$, $\sigma(a, b) = -1$ for $a \neq b$ and $d = 1$, negated.[^gusfield]
- **Grid graph.** Vertices $(i, j)$, $0 \le i \le n$, $0 \le j \le m$; edges $(i-1, j-1) \to (i, j)$ of weight $\sigma(s_i, t_j)$, $(i-1, j) \to (i, j)$ and $(i, j-1) \to (i, j)$ of weight $-d$. Alignments are in bijection with paths from $(0, 0)$ to $(n, m)$, and the score is the path weight.[^compeau]
- **Counting.** A path with $k$ diagonal steps also has $n - k$ vertical and $m - k$ horizontal steps, in any order, so the number of alignments is the Delannoy number
$$D(n, m) = \sum_{k=0}^{\min(n, m)} \frac{(n + m - k)!}{k!\,(n-k)!\,(m-k)!} = \sum_{k=0}^{\min(n, m)} \binom{n}{k} \binom{m}{k} 2^k,$$
the second form being a classical identity that is cheaper to compute. For the figure, $D(4, 3) = 129$.

## Computational representation

An alignment is stored as two gapped strings of equal length; everything else (score, identity, the operation string used by alignment file formats) is derived from its columns. No dynamic programming here: that is the job of the algorithm notes.

```python
from itertools import groupby

GAP = "-"


def check_alignment(a: str, b: str, s: str, t: str) -> None:
    """a, b: gapped rows. Removing gaps must give s and t; no column may be two gaps."""
    assert len(a) == len(b), "rows must have equal length"
    assert a.replace(GAP, "") == s and b.replace(GAP, "") == t, "rows must spell s and t"
    assert all(x != GAP or y != GAP for x, y in zip(a, b)), "gap-gap column"


def column_ops(a: str, b: str) -> str:
    """One letter per column: M match, X mismatch, D gap in b (s has a letter), I gap in a."""
    return "".join("D" if y == GAP else "I" if x == GAP else "M" if x == y else "X"
                   for x, y in zip(a, b))


def score(a: str, b: str, match: int = 1, mismatch: int = -1, gap: int = -2) -> int:
    """Additive score with a linear gap penalty (each gap column costs `gap`)."""
    points = {"M": match, "X": mismatch, "D": gap, "I": gap}
    return sum(points[op] for op in column_ops(a, b))


def run_length(ops: str) -> str:
    """Compress the column operations: MMXMDDM -> 2M1X1M2D1M (the idea behind CIGAR strings)."""
    return "".join(f"{len(list(g))}{op}" for op, g in groupby(ops))


s, t = "TACGGT", "ACGGTA"                        # invented toy pair
alignments = {"A (no gaps)": ("TACGGT", "ACGGTA"), "B (end gaps)": ("TACGGT-", "-ACGGTA")}
for name, (a, b) in alignments.items():
    check_alignment(a, b, s, t)
    print(f"{name:13s} {column_ops(a, b):8s} {run_length(column_ops(a, b)):7s}",
          "score gap=-2:", score(a, b), " gap=-5:", score(a, b, gap=-5))
```

```text
A (no gaps)   XXXMXX   3X1M2X  score gap=-2: -4  gap=-5: -4
B (end gaps)  DMMMMMI  1D5M1I  score gap=-2: 1  gap=-5: -5
```

The run-length operation string is the compact form in which aligners report where a read has matches, insertions and deletions relative to the reference; see the CIGAR field of [[SAM Format]] for its exact letters.

## Worked example

> [!example] The best alignment depends on the scoring scheme
> Align $s$ = `TACGGT` with $t$ = `ACGGTA` (invented) globally, match $+1$, mismatch $-1$.
> 1. **Alignment A**, no gaps: one match (G/G at column 4), five mismatches: $1 - 5 = -4$.
> 2. **Alignment B**, shift by one with two end gaps: five matches, two gap columns.
> 3. **Gap cost 2**: B scores $5 - 4 = 1 > -4$, so B wins: the scheme "believes" in one indel at each end.
> 4. **Gap cost 5**: B scores $5 - 10 = -5 < -4$, so A wins: gaps are now so expensive that five mismatches are preferred.
> 5. **Check by brute force** (Exercise 3): among all 8,989 alignments of these two 6-mers, B is the unique optimum with gap cost 2 and A with gap cost 5. With free end gaps (a read against a genome region, semi-global), B wins at any gap cost: the biology of the comparison, not the arithmetic, decides the scheme.

## Common misconceptions

> [!warning] "Two sequences have one correct alignment"
> The optimal alignment is optimal **for a scoring scheme and a mode**. Change the gap penalty, the matrix or global versus local, and the answer can change; co-optimal alignments are also common.

> [!warning] "A gap means a deletion"
> A gap column records an indel: a deletion in one lineage or an insertion in the other. Only an outgroup or other evidence can polarize it.

> [!warning] "A high score means homology"
> Scores grow with length and depend on composition and scheme; a long alignment of unrelated sequences can outscore a short alignment of true homologs. Homology is inferred from the significance of the score ([[E-Value]], [[Sequence Homology]]).[^pearson]

## Exercises

> [!question] Exercise 1 (L1)
> Score this alignment with match $+2$, mismatch $-1$, gap $-2$, then with match $+1$, mismatch $-1$, gap $-2$:
> ```text
> ACGTTGA-C
> AC-TTGAGC
> ```

> [!success]- Solution
> Columns: A/A M, C/C M, G/- gap, T/T M, T/T M, G/G M, A/A M, -/G gap, C/C M: 7 matches, 0 mismatches, 2 gaps. Scores: $7 \times 2 - 4 = 10$ and $7 - 4 = 3$. In code, `score(a, b)` gives 3 and `run_length(column_ops(a, b))` gives `2M1D4M1I1M`.

> [!question] Exercise 2 (L2)
> Using the grid of the figure ($s$ = `ACGT`, $t$ = `AGT`), how many steps of each kind does any alignment path contain if it uses $k$ diagonal steps? Deduce the alignment length $L$ as a function of $k$.

> [!success]- Solution
> A path must go down $n = 4$ rows and right $m = 3$ columns. Each diagonal step covers one of each, so there are $4 - k$ vertical and $3 - k$ horizontal steps, and $L = k + (4 - k) + (3 - k) = 7 - k$, from $L = 4$ ($k = 3$, the highlighted path) to $L = 7$ ($k = 0$, no residue aligned).

> [!question] Exercise 3 (L3, Python)
> Enumerate every alignment of `TACGGT` and `ACGGTA` recursively, check that their number equals the Delannoy number, and find the optimal ones for gap costs 2 and 5. How long would the same enumeration take for two 100-residue proteins?

> [!success]- Solution
> Using `GAP` and `score` from the code above:
> ```python
> from math import comb
>
>
> def delannoy(n: int, m: int) -> int:
>     return sum(comb(n, k) * comb(m, k) * 2**k for k in range(min(n, m) + 1))
>
>
> def all_alignments(s: str, t: str):
>     """Yield every alignment (a, b) of s and t: exponential, for tiny inputs only."""
>     if not s and not t:
>         yield "", ""
>         return
>     if s and t:
>         for a, b in all_alignments(s[1:], t[1:]):
>             yield s[0] + a, t[0] + b
>     if s:
>         for a, b in all_alignments(s[1:], t):
>             yield s[0] + a, GAP + b
>     if t:
>         for a, b in all_alignments(s, t[1:]):
>             yield GAP + a, t[0] + b
>
>
> s, t = "TACGGT", "ACGGTA"
> alignments = list(all_alignments(s, t))
> print(len(alignments), delannoy(len(s), len(t)))
> for gap in (-2, -5):
>     best = max(score(a, b, gap=gap) for a, b in alignments)
>     winners = [(a, b) for a, b in alignments if score(a, b, gap=gap) == best]
>     print(f"gap={gap}: best score {best}, {len(winners)} optimal alignment(s), e.g. {winners[0]}")
> ```
> ```text
> 8989 8989
> gap=-2: best score 1, 1 optimal alignment(s), e.g. ('TACGGT-', '-ACGGTA')
> gap=-5: best score -4, 1 optimal alignment(s), e.g. ('TACGGT', 'ACGGTA')
> ```
> For $n = m = 100$ there are $D(100, 100) \approx 2 \times 10^{75}$ alignments: even at $10^{9}$ alignments per second this is about $10^{66}$ seconds, while dynamic programming fills $101 \times 101$ cells. The brute-force enumerator remains useful as a test oracle for [[04-alignment-engine]] on tiny inputs.

> [!question] Exercise 4 (L3)
> Choose the alignment mode for each task and justify: (a) placing a 150-nt sequencing read on a 5 Mb bacterial genome; (b) finding which proteins of a database share a kinase domain with your query; (c) comparing two full-length orthologous genes of similar length; (d) detecting that the end of read 1 overlaps the start of read 2 in assembly.

> [!success]- Solution
> (a) Semi-global, fitting the whole read into a part of the genome: end gaps in the genome must be free, but the read should be aligned entirely ([[Read Mapping]]). (b) Local: only the domain is shared, flanks are unrelated ([[Smith-Waterman Algorithm]], [[BLAST]]). (c) Global: the sequences are homologous end to end ([[Needleman-Wunsch Algorithm]]). (d) Overlap alignment, a semi-global variant where a suffix of one sequence is aligned with a prefix of the other ([[Semi-Global Alignment]], [[Genome Assembly]]).

## Mastery checklist

- [ ] 1 Recognized: I can write a valid alignment, name its column types and score it by hand.
- [ ] 2 Understood: I can explain scoring schemes (substitution scores as log-odds, linear and affine gaps), the three modes and alignments as grid paths.
- [ ] 3 Practiced: I can represent, validate and score alignments in code, derive operation strings, and count alignments with the Delannoy formula.
- [ ] 4 Applied: in [[04-alignment-engine]], my brute-force oracle and my dynamic programming implementations agree on random short sequences, and I aligned real homologous genes.
- [ ] 5 Explained: I can explain why an alignment is a hypothesis, how scores become significance, and when heuristics (BLAST, seeds) replace exact algorithms.

## References

[^durbin]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment" (scoring model, log-odds substitution scores, gap penalties, global and local alignment).
[^durbin4]: [[Biological Sequence Analysis (Durbin)]], ch. 4 "Pairwise alignment using HMMs".
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Compare Biological Sequences?" (alignment graph and longest paths, global, local, fitting and overlap alignment).
[^gusfield]: [[Algorithms on Strings, Trees, and Sequences (Gusfield)]], part on inexact matching, sequence alignment and dynamic programming (edit distance and alignment).
[^nw]: [[Needleman 1970 - Search for Similarities in Amino Acid Sequences]], *Journal of Molecular Biology*.
[^sw]: [[Smith 1981 - Identification of Common Molecular Subsequences]], *Journal of Molecular Biology*.
[^blast]: [[Altschul 1990 - Basic Local Alignment Search Tool]], *Journal of Molecular Biology*.
[^pearson]: [[Pearson 2013 - An Introduction to Sequence Similarity Searching]], *Current Protocols in Bioinformatics*.
[^coursera]: [[Coursera UCSD - Bioinformatics Specialization]], course III "Comparing Genes, Proteins, and Genomes".
[^mit]: [[MIT 6.047 - Computational Biology]], "Genomes" part (sequence alignment).
