---
aliases:
  - Gap Cost
  - Gap Score
  - Affine Gap Penalty
  - Linear Gap Penalty
  - Gap Opening and Extension
  - Pénalité de gap
tags:
  - type/concept
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Sequence Alignment]]"
  - "[[Indel]]"
  - "[[Substitution Matrix]]"
related:
  - "[[Gotoh Algorithm]]"
  - "[[Needleman-Wunsch Algorithm]]"
  - "[[Smith-Waterman Algorithm]]"
  - "[[Semi-Global Alignment]]"
  - "[[Edit Distance]]"
  - "[[BLAST]]"
  - "[[Pair Hidden Markov Model]]"
  - "[[Dynamic Programming]]"
projects:
  - "[[04-alignment-engine]]"
sources:
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[NCBI BLAST]]"
---

# Gap Penalty

> [!abstract]
> A gap penalty is the score subtracted for a run of gap columns; whether it grows with every column or charges mainly for opening the gap decides whether an aligner explains an indel as one event or scatters it into many.

## Definition

In a [[Sequence Alignment|pairwise alignment]], a **gap** is a maximal run of consecutive gap symbols in one row, the trace of an insertion or a deletion ([[Indel]]). A **gap penalty** $\gamma(g)$ is the score given to a gap of length $g$, added to the [[Substitution Matrix|substitution scores]] of the aligned pairs.[^durbin] The two standard forms are:[^durbin]

- **linear**: $\gamma(g) = -gd$, every gap column costs $d$;
- **affine**: $\gamma(g) = -d - (g - 1)e$, a **gap-open** penalty $d$ for the first column and a smaller **gap-extension** penalty $e < d$ for each further one.

## Why it matters

- **One event, several residues.** A single indel can insert or delete several residues at once ([[Indel]]). A linear penalty charges a 3-residue gap like three independent 1-residue gaps; an affine penalty charges mostly for the event.
- **Defaults to know.** NCBI BLAST charges a gap of $k$ residues $a + bk$ ("existence" $a$, "extension" $b$);[^ncbi] BLAST+ blastp uses $a = 11$, $b = 1$ with BLOSUM62, and its `blastp-short` task 9 and 1 with PAM30.[^ncbi]
- **It changes the answer.** On the same pair of sequences, linear and affine penalties can give different optimal alignments, hence different indel calls and different variant descriptions (Worked example).
- **Lab.** [[04-alignment-engine]] implements linear gaps first ([[Needleman-Wunsch Algorithm]]), then affine gaps with three matrices ([[Gotoh Algorithm]]).

## Core (L2)

![[gap-penalty-linear-vs-affine.svg]]

### Linear versus affine

With $d = 2$ for the linear penalty and $d = 5$, $e = 1$ for the affine one:

| Gap length $g$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| linear, $-2g$ | −2 | −4 | −6 | −8 | −10 | −12 |
| affine, $-5 - (g-1)$ | −5 | −6 | −7 | −8 | −9 | −10 |

- Short gaps are cheaper under this linear penalty, long ones under the affine penalty; the two cross at $g = 4$.
- More important: **a linear penalty ignores whether gap columns are contiguous.** Three gap columns cost 6 whether they form one gap or three. The affine penalty charges each opening: 7 for one gap of 3, 11 for 2 + 1, 15 for 1 + 1 + 1 (figure, right).
- Consequence: under linear costs, gap columns scatter wherever each one buys an extra match; under affine costs, they gather into few, longer gaps.

### Two conventions for the same idea

| Convention | Cost of a gap of length $g$ | Used by |
|---|---|---|
| open + extend | $d + (g - 1)e$: the opening includes the first residue | Durbin et al.[^durbin] |
| existence + extension | $a + bg$: every residue pays $b$, plus $a$ once | NCBI BLAST[^ncbi] |

Since $a + bg = (a + b) + (g - 1)b$, the conventions match with $d = a + b$ and $e = b$: BLAST's default (11, 1) is $d = 12$, $e = 1$, and a 1-residue gap costs 12, not 11 (Exercise 2). Reading parameters in the wrong convention shifts every gap cost by $b$.

### End gaps and alignment modes

In a [[Needleman-Wunsch Algorithm|global alignment]], end gaps cost as much as internal ones. [[Semi-Global Alignment|Semi-global]] alignment (fitting a read into a genome, overlapping two reads) makes end gaps free, and [[Smith-Waterman Algorithm|local alignment]] leaves unaligned ends out altogether. Choosing the mode is choosing which gaps count as evidence of indels and which merely reflect where the sequences start and end.

### Balance with the matrix

Gap penalties are in the units of the substitution scores (half bits for BLOSUM62, see [[Substitution Matrix]]). Too low, and the aligner opens gaps to collect chance matches; too high, and it prefers a run of mismatches to a true indel, as in the worked example of [[Sequence Alignment]]. Search tools therefore document default gap costs per matrix: 11 and 1 with BLOSUM62, 9 and 1 with PAM30 in BLAST+.[^ncbi]

## Advanced (L3)

- **The price of generality.** With an arbitrary $\gamma$, each cell of the dynamic programming table must consider every gap length that can end there:
$$F(i, j) = \max\Big\{F(i-1, j-1) + s(x_i, y_j),\ \max_{1 \le k \le i} F(i-k, j) + \gamma(k),\ \max_{1 \le k \le j} F(i, j-k) + \gamma(k)\Big\},$$
which costs $O(n^2 m + n m^2)$ time, cubic for sequences of similar length.[^durbin] For affine penalties it suffices to remember whether the alignment currently ends inside a gap, with three matrices, and the cost returns to $O(nm)$ ([[Gotoh Algorithm]]).[^durbin]
- **Probabilistic reading.** If a gap opens with probability $\delta$ and each further column extends it with probability $\varepsilon$, a gap of length $g$ has probability $\delta \varepsilon^{g-1}$, whose logarithm $\log \delta + (g - 1)\log \varepsilon$ is an affine penalty: affine costs model **geometrically distributed** gap lengths (Exercise 5). Durbin and colleagues derive the exact correspondence between affine penalties and the transition probabilities of a pair hidden Markov model ([[Pair Hidden Markov Model]]).[^durbin4]
- **Other shapes.** Any other $\gamma$, for example one that grows ever more slowly with $g$, is allowed by the general recurrence above, at its higher cost.
- **Where the gap goes.** Inside a repeat, a gap can slide without changing the score: the penalty does not choose among these positions, the traceback convention does, and variant representations must then be normalized ([[Indel]], [[Sequence Alignment#Advanced (L3)]]).

## Mathematical representation

- An alignment has $c$ gap columns grouped into $k$ gaps of lengths $g_1, \dots, g_k$ (maximal runs in either row), with $\sum_r g_r = c$. Its score is $S = \sum_{\text{pair columns}} s(\hat x_l, \hat y_l) + \sum_{r=1}^{k} \gamma(g_r)$.
- **Linear**: $\sum_r \gamma(g_r) = -dc$, which depends only on the number of gap columns, not on how they are grouped.
- **Affine**: $\sum_r \gamma(g_r) = -\sum_r \big(d + (g_r - 1)e\big) = -\big(ce + k(d - e)\big)$. For a fixed $c$ the penalty grows with the number of gaps $k$ as soon as $d > e$: affine costs favour few, long gaps.
- **Conversion**: $a + bg = (a + b) + (g - 1)b$, so $(a, b) \mapsto (d, e) = (a + b, b)$.
- **Geometric lengths**: $\log_2\big(\delta \varepsilon^{g-1}\big) = \log_2 \delta + (g - 1)\log_2 \varepsilon$, an affine score with opening $-\log_2 \delta$ and extension $-\log_2 \varepsilon$ bits.

## Computational representation

Gap penalties as functions of the length, a score that finds the gap runs of each row, and a brute-force search over all alignments of a tiny pair (no dynamic programming needed to see the effect).

```python
from itertools import groupby

GAP = "-"


def linear(d: float):
    """gamma(g) = -g d."""
    return lambda g: -g * d


def affine(d: float, e: float):
    """gamma(g) = -d - (g - 1) e: d opens the gap (first column), e extends it."""
    return lambda g: -d - (g - 1) * e


def gap_runs(row: str) -> list[int]:
    """Lengths of the maximal runs of gap symbols in one row."""
    return [len(list(run)) for symbol, run in groupby(row) if symbol == GAP]


def score(a: str, b: str, gamma, match: int = 2, mismatch: int = -1) -> float:
    pairs = sum(match if x == y else mismatch for x, y in zip(a, b) if GAP not in (x, y))
    return pairs + sum(gamma(g) for row in (a, b) for g in gap_runs(row))


def all_alignments(s: str, t: str):
    """Every alignment of s and t (exponential: tiny inputs only)."""
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


print([(g, linear(2)(g), affine(5, 1)(g)) for g in range(1, 7)])

# Invented history: t = s with GAT deleted after the first base, then one A -> T substitution
s, t = "CGATATAT", "CATTT"
alignments = list(all_alignments(s, t))
print(len(alignments), "alignments")
for name, gamma in (("linear d=2", linear(2)), ("affine d=5 e=1", affine(5, 1))):
    best = max(score(a, b, gamma) for a, b in alignments)
    winners = [(a, b) for a, b in alignments if score(a, b, gamma) == best]
    print(f"{name}: best {best}, {len(winners)} optimum:", winners, "gap runs", gap_runs(winners[0][1]))
for a, b in (("CGATATAT", "C-AT-T-T"), ("CGATATAT", "C---ATTT")):
    print(b, "linear:", score(a, b, linear(2)), "affine:", score(a, b, affine(5, 1)))
```

```text
[(1, -2, -5), (2, -4, -6), (3, -6, -7), (4, -8, -8), (5, -10, -9), (6, -12, -10)]
13073 alignments
linear d=2: best 4, 1 optimum: [('CGATATAT', 'C-AT-T-T')] gap runs [1, 1, 1]
affine d=5 e=1: best 0, 1 optimum: [('CGATATAT', 'C---ATTT')] gap runs [3]
C-AT-T-T linear: 4 affine: -5
C---ATTT linear: 1 affine: 0
```

In an aligner, $\gamma$ enters the recurrence instead of being applied afterwards ([[Needleman-Wunsch Algorithm]] for linear gaps, [[Gotoh Algorithm]] for affine ones).

## Worked example

> [!example] One deletion or three? (invented history)
> 1. **History**: $t$ was made from $s$ = `CGATATAT` by deleting `GAT` after the first base, then changing one A to T: $t$ = `CATTT`.
> 2. **Search**: score all 13,073 alignments with match +2, mismatch −1.
> 3. **Linear gaps** ($d = 2$): best score 4, a unique optimum with three 1-residue gaps and no mismatch.
> 4. **Affine gaps** ($d = 5$, $e = 1$): best score 0, a unique optimum with one 3-residue gap and one mismatch, which is exactly the invented history.
> ```text
> linear optimum        affine optimum
> s  CGATATAT           s  CGATATAT
> t  C-AT-T-T           t  C---ATTT
> ```
> 5. **Cross-check**: each scheme prefers its own optimum, 4 against 1 under linear costs, 0 against −5 under affine costs.
> 6. **Lesson**: in the repeat `ATATAT`, the linear scheme fragments the deletion at no extra cost; the affine scheme pays for each opening and recovers one event. With real data the history is unknown, so the gap model should reflect how indels arise.

## Common misconceptions

> [!warning] "The gap-open penalty is the cost of a 1-residue gap"
> Only in the $d + (g - 1)e$ convention. In BLAST's $a + bk$ convention, a 1-residue gap costs $a + b$.[^ncbi] Check which convention a tool uses before copying parameters.

> [!warning] "Higher gap penalties give better alignments"
> They give fewer gaps. Too high, and a real indel is replaced by a run of mismatches, as in the worked example of [[Sequence Alignment]], where a gap cost of 5 makes five mismatches win over two end gaps.

> [!warning] "Affine penalties are right, linear ones are wrong"
> Both are models. Linear costs are simpler, and [[Edit Distance]] is exactly the linear case with unit costs; affine costs describe multi-residue indels better, for a constant factor more work ([[Gotoh Algorithm]]).

> [!warning] "End gaps are evidence of indels"
> In a global alignment they are charged as such, but when a read is placed inside a genome, or two reads overlap, unmatched ends are not indels ([[Semi-Global Alignment]]).

## Exercises

> [!question] Exercise 1 (L2)
> With the affine penalty $d = 10$, $e = 0.5$ and the linear penalty $d = 3$, compute the cost of gaps of length 1, 2 and 10. Which scheme prefers one 10-residue gap to ten 1-residue gaps?

> [!success]- Solution
> Affine: 10, 10.5 and $10 + 9 \times 0.5 = 14.5$; ten separate gaps cost $10 \times 10 = 100$. Linear: 3, 6 and 30, and ten separate gaps also cost 30. Only the affine scheme prefers the single gap (14.5 against 100); the linear one is indifferent.

> [!question] Exercise 2 (L2, Python)
> Score the gaps of the alignment `MKV--LLSAG---W` / `MKVQELL-AGKRPW` with BLAST's default convention ($a = 11$, $b = 1$) and with Durbin's convention ($d = 12$, $e = 1$), using `gap_runs` and `affine`.

> [!success]- Solution
> ```python
> a, b = "MKV--LLSAG---W", "MKVQELL-AGKRPW"
> print(gap_runs(a), gap_runs(b))
> blast = lambda g: -(11 + 1 * g)            # NCBI form: a + b k with a = 11, b = 1
> print(sum(blast(g) for row in (a, b) for g in gap_runs(row)),
>       sum(affine(12, 1)(g) for row in (a, b) for g in gap_runs(row)))
> ```
> ```text
> [2, 3] [1]
> -39 -39
> ```
> Three gaps of lengths 2, 3 and 1 cost $13 + 14 + 12 = 39$ either way: $(a, b) = (11, 1)$ is $(d, e) = (12, 1)$.

> [!question] Exercise 3 (L2)
> Six gap columns, $d = 5$, $e = 1$. Write the total affine penalty as a function of the number $k$ of gaps they form, and evaluate it for $k = 1$ and $k = 6$.

> [!success]- Solution
> $ce + k(d - e) = 6 + 4k$: 10 for one gap of 6 ($5 + 5 \times 1$), 30 for six 1-residue gaps ($6 \times 5$). Each extra opening costs $d - e = 4$.

> [!question] Exercise 4 (L3)
> For two sequences of length $n = m = 1000$, estimate the number of candidate terms examined by the general-gap recurrence and compare with the three affine matrices.

> [!success]- Solution
> Cell $(i, j)$ examines $1 + i + j$ candidates, so $\sum_{i, j} (1 + i + j) \approx nm + nm(n + m)/2 = 10^6 + 10^9$, about $10^9$. The affine version examines a constant number of terms per cell in each of three matrices, about $10^7$: roughly a hundred times less work, and the gap grows linearly with the sequence length.

> [!question] Exercise 5 (L3, Python)
> Gaps open with probability $\delta = 0.01$ and extend with probability $\varepsilon = 0.4$ (illustrative values). Compute $\log_2(\delta \varepsilon^{g-1})$ for $g = 1$ to 4, deduce the open and extension penalties in bits, then in half bits (BLOSUM62 units). Compare with BLAST's default.

> [!success]- Solution
> ```python
> import math
> delta, eps = 0.01, 0.4                        # P(open), P(extend), illustrative values
> print([round(math.log2(delta * eps ** (g - 1)), 2) for g in range(1, 5)])
> print(round(-math.log2(delta), 2), round(-math.log2(eps), 2))
> ```
> ```text
> [-6.64, -7.97, -9.29, -10.61]
> 6.64 1.32
> ```
> Each extra column subtracts the same 1.32 bits: an affine penalty with $d \approx 6.6$ and $e \approx 1.3$ bits, about 13 and 2.6 half bits. BLAST's (11, 1), that is $d = 12$, $e = 1$ in half bits, corresponds to a similar opening and longer expected gaps. This simplified argument ignores the comparison with the random model that a pair HMM includes.[^durbin4]

## Mastery checklist

- [ ] 1 Recognized: I can define a gap and write the linear and affine penalties.
- [ ] 2 Understood: I can explain why affine costs favour few long gaps, convert between the two affine conventions and choose how end gaps are treated.
- [ ] 3 Practiced: I can score alignments with any $\gamma$ in code and show, on a small example, that linear and affine penalties select different optima.
- [ ] 4 Applied: in [[04-alignment-engine]], I aligned real homologous proteins with linear and affine gaps and compared the indels each scheme reports.
- [ ] 5 Explained: I can explain the cubic cost of general gap functions, why affine gaps stay in $O(nm)$, and the geometric-length interpretation of affine costs.

## References

[^durbin]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment" (linear and affine gap penalties, general gap functions and dynamic programming with affine gaps).
[^durbin4]: [[Biological Sequence Analysis (Durbin)]], ch. 4 "Pairwise alignment using HMMs".
[^ncbi]: [[NCBI BLAST]], documentation of gap costs (a gap of $k$ residues scores $-(a + bk)$) and BLAST+ command-line manual (blastp and blastp-short defaults).
