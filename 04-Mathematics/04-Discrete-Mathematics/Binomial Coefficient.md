---
aliases:
  - n choose k
  - Combination
  - Combinations
  - Pascal's Triangle
  - Pascal's Rule
  - Binomial Theorem
  - Multinomial Coefficient
  - Coefficient binomial
tags:
  - type/concept
  - domain/mathematics
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Combinatorics]]"
  - "[[Permutation]]"
  - "[[Set]]"
related:
  - "[[Binomial Distribution]]"
  - "[[Multinomial Distribution]]"
  - "[[Sequence Alignment]]"
  - "[[Dynamic Programming]]"
  - "[[Hamming Distance]]"
  - "[[Mutation]]"
  - "[[Inclusion-Exclusion Principle]]"
projects:
  - "[[04-alignment-engine]]"
sources:
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Introduction to Probability (Blitzstein)]]"
---

# Binomial Coefficient

> [!abstract]
> The binomial coefficient $\binom{n}{k}$ counts the ways to choose $k$ items out of $n$ when order does not matter: where $k$ mutations can fall in a gene, how many gap patterns an alignment can have, and the coefficients of $(x + y)^n$.

## Definition

For integers $0 \le k \le n$, the **binomial coefficient** $\binom{n}{k}$ ("$n$ choose $k$") is the number of $k$-element subsets of an $n$-element set, and[^lehman]

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}, \qquad \binom{n}{k} = 0 \text{ if } k < 0 \text{ or } k > n.$$

The **multinomial coefficient** $\binom{n}{k_1, \dots, k_r} = \dfrac{n!}{k_1! \cdots k_r!}$, with $k_1 + \dots + k_r = n$, counts the ways to split $n$ positions into labelled groups of sizes $k_1, \dots, k_r$; for $r = 2$ it is $\binom{n}{k_1}$.[^lehman][^mcs]

## Why it matters

- **Mutations.** $\binom{n}{k}$ is the number of ways to choose which $k$ of $n$ sites are mutated, the combinatorial factor of the [[Binomial Distribution]] and the size of mismatch neighbourhoods of k-mers.[^compeau-ori]
- **Alignment.** Pairwise alignments are paths through a grid;[^compeau-align] counting them shows that enumeration is hopeless and [[Dynamic Programming]] is necessary ([[Sequence Alignment]], [[04-alignment-engine]]).
- **Pairs.** $\binom{n}{2}$ pairs: all-versus-all comparisons of $n$ sequences, possible edges of a network on $n$ proteins ([[Graph]]).
- **Composition.** Multinomial coefficients count sequences with a given base composition, hence the number of distinct shuffles of a sequence ([[Permutation]]).

## Core (L1)

### From arrangements to subsets

There are $n!/(n-k)!$ ordered selections of $k$ distinct items ([[Permutation]]). Each $k$-subset appears in exactly $k!$ of them (its $k!$ orders), so by the division rule ([[Combinatorics]]) $\binom{n}{k} = \frac{n!}{(n-k)!\,k!}$. Choosing the $k$ items kept is the same as choosing the $n - k$ left out, so $\binom{n}{k} = \binom{n}{n-k}$.

### Pascal's rule

$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}, \qquad n \ge 1.$$

**Proof.** Fix one element $x$ of the $n$-set. A $k$-subset either contains $x$ (choose its other $k - 1$ elements among the remaining $n - 1$) or does not (choose all $k$ among the $n - 1$). The two cases are disjoint, so the sum rule gives the identity. $\square$

Each row of **Pascal's triangle** is computed from the previous one by this rule:

```text
n=0                1
n=1              1   1
n=2            1   2   1
n=3          1   3   3   1
n=4        1   4   6   4   1
n=5      1   5  10  10   5   1
n=6    1   6  15  20  15   6   1
```

### Binomial theorem

$$(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}.$$

**Proof.** Expanding $(x + y)(x + y)\cdots(x + y)$ picks $x$ or $y$ in each of the $n$ factors. The product equals $x^k y^{n-k}$ exactly when $x$ was picked in $k$ factors, and there are $\binom{n}{k}$ ways to choose those factors. $\square$ With $x = y = 1$: $\sum_k \binom{n}{k} = 2^n$, the number of subsets ([[Set]]).[^lehman]

### Bio: placing $k$ mutations among $n$ sites

- **Positions.** $k$ substitutions in a gene of $n$ sites can occupy $\binom{n}{k}$ sets of positions: $\binom{1000}{2} = 499{,}500$ position pairs in a 1 kb gene.
- **Sequences.** Each mutated site takes one of 3 other bases, so $\binom{n}{k}\,3^k$ sequences lie at [[Hamming Distance]] exactly $k$, and $\sum_{i=0}^{d} \binom{n}{i} 3^i$ within distance $d$: the $d$-neighbourhood used to find approximate k-mer occurrences.[^compeau-ori] For an 8-mer and $d = 2$: $1 + 24 + 252 = 277$.
- **Probability.** If each site mutates independently with probability $p$, each set of $k$ sites has probability $p^k (1-p)^{n-k}$ of being exactly the mutated set, so $P(K = k) = \binom{n}{k} p^k (1-p)^{n-k}$ ([[Binomial Distribution]]).[^blitzstein]

### Bio: monotone lattice paths through an alignment grid

Align $v$ of length $n$ with $w$ of length $m$. Each alignment is a path from $(0, 0)$ to $(n, m)$ in a grid: a down step aligns the next letter of $v$ to a gap, a right step the next letter of $w$ to a gap, a diagonal step aligns two letters.[^compeau-align] Paths with only down and right steps are words with $n$ D's and $m$ R's: choose the positions of the D's among $n + m$ steps, $\binom{n+m}{n}$ paths. With diagonals there are more (Mathematical representation).

## Deeper (L2)

- **Multinomial theorem.** $(x_1 + \dots + x_r)^n = \sum \binom{n}{k_1, \dots, k_r} x_1^{k_1} \cdots x_r^{k_r}$ over all $k_1 + \dots + k_r = n$, by the same expansion argument. Setting all $x_i = 1$ gives $r^n$: summing over compositions recovers all $4^n$ DNA sequences.
- **Composition classes.** 20-mers with exactly 5 of each base number $\binom{20}{5, 5, 5, 5} = 11{,}732{,}745{,}024$, about 1.07 % of the $4^{20}$ 20-mers: even the most likely composition class is a small fraction of sequence space.
- **Counting the alignment recurrence.** Let $D(i, j)$ be the number of alignment paths to cell $(i, j)$. The last step came from the top, the left or the diagonal, so $D(i, j) = D(i-1, j) + D(i, j-1) + D(i-1, j-1)$ with $D(0, 0) = 1$: the counting twin of the alignment score recurrence, where "add" becomes "maximize". $D(n, n)$ are the Delannoy numbers.
- **Computing safely.** `math.comb` returns exact integers of any size; floating-point factorials overflow ($\binom{2000}{1000} \approx 10^{600}$ exceeds the largest double, `sys.float_info.max` $\approx 1.8 \times 10^{308}$). For probabilities, work with logarithms (`math.lgamma`) ([[Floating-Point Arithmetic]]).

## Advanced (L3)

- **Growth.** Stirling's formula $n! \sim \sqrt{2\pi n}\,(n/e)^n$[^lehman] gives $\binom{2n}{n} = \frac{(2n)!}{(n!)^2} \sim \frac{\sqrt{4\pi n}\,(2n/e)^{2n}}{2\pi n\,(n/e)^{2n}} = \frac{4^n}{\sqrt{\pi n}}$. Gap-only paths for two 100-mers: about $10^{59}$; all alignment paths: about $10^{75}$, more than the $4^{100} \approx 10^{60}$ possible 100-mers (Exercise 3).
- **Pairs dominate.** All-versus-all comparison of $N$ reads costs $\binom{N}{2} \approx N^2/2$ comparisons, the reason overlap-based assembly and clustering index k-mers to avoid comparing every pair ([[Genome Assembly]], [[K-mer]]).
- **Identities by double counting.** $\sum_k \binom{n}{k}^2 = \binom{2n}{n}$: a monotone path in an $n \times n$ grid crosses the anti-diagonal $i + j = n$ at some cell $(k, n-k)$, reached in $\binom{n}{k}$ ways and left in $\binom{n}{n-k} = \binom{n}{k}$ ways.

## Mathematical representation

- $\binom{n}{k} = |\{S \subseteq [n] : |S| = k\}|$ with $[n] = \{1, \dots, n\}$.
- **Symmetry.** $S \mapsto [n] \setminus S$ is a bijection from $k$-subsets to $(n-k)$-subsets.
- **Multinomial.** $\binom{n}{k_1, \dots, k_r} = \binom{n}{k_1}\binom{n - k_1}{k_2} \cdots \binom{k_r}{k_r}$ (choose the positions of group 1, then of group 2 among the rest, ...), which telescopes to $\frac{n!}{k_1! \cdots k_r!}$.
- **Alignment paths.** A path with $d$ diagonal steps has $n - d$ down and $m - d$ right steps, $n + m - d$ steps in all, so
$$D(n, m) = \sum_{d=0}^{\min(n, m)} \binom{n + m - d}{d,\ n - d,\ m - d}.$$
For $n = 3$, $m = 2$: $10 + 12 + 3 = 25$.

## Computational representation

```python
from math import comb, factorial
from itertools import combinations, product

def pascal(n_max):
    """Rows 0..n_max of Pascal's triangle, built with C(n,k) = C(n-1,k-1) + C(n-1,k)."""
    rows = [[1]]
    for n in range(1, n_max + 1):
        prev = rows[-1]
        rows.append([1] + [prev[k - 1] + prev[k] for k in range(1, n)] + [1])
    return rows

rows = pascal(6)
print(rows[6], sum(rows[6]), all(rows[n][k] == comb(n, k) for n in range(7) for k in range(n + 1)))

def monotone_paths(n, m):
    """Enumerate grid paths with n down and m right steps: choose the down steps."""
    return sum(1 for _ in combinations(range(n + m), n))

def alignment_paths(n, m):
    """Paths from (0,0) to (n,m) with down, right and diagonal steps (dynamic programming)."""
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == j == 0:
                D[i][j] = 1
            else:
                D[i][j] = (D[i - 1][j] if i else 0) + (D[i][j - 1] if j else 0) \
                          + (D[i - 1][j - 1] if i and j else 0)
    return D[n][m]

print(monotone_paths(3, 2), comb(5, 2), alignment_paths(3, 2))

def hamming_ball(k, d):
    """Number of k-mers within Hamming distance d of a fixed k-mer."""
    return sum(comb(k, i) * 3**i for i in range(d + 1))

ref = "ACGTACGT"
brute = sum(1 for w in product("ACGT", repeat=8) if sum(a != b for a, b in zip(w, ref)) <= 2)
print(hamming_ball(8, 2), brute)

def multinomial(*ks):
    out = factorial(sum(ks))
    for k in ks:
        out //= factorial(k)
    return out

print(multinomial(5, 5, 5, 5), round(multinomial(5, 5, 5, 5) / 4**20, 4))
```

```text
[1, 6, 15, 20, 15, 6, 1] 64 True
10 10 25
277 277
11732745024 0.0107
```

Every formula is checked against brute-force enumeration on a small case before being trusted on a large one.

## Worked example

> [!example] Paths through the grid of `ACG` versus `AT` (invented sequences)
> $n = 3$, $m = 2$.
> 1. **Gap-only paths**: 5 steps, 3 of them down: $\binom{5}{3} = 10$. One of them, DDDRR, is the alignment
> ```text
> ACG--
> ---AT
> ```
> 2. **All alignment paths**: add diagonal steps. With $d$ diagonals: $d = 0$: 10; $d = 1$: $\frac{4!}{1!\,2!\,1!} = 12$; $d = 2$: $\frac{3!}{2!\,1!\,0!} = 3$. Total 25, as `alignment_paths(3, 2)` prints. Path M D M (diagonal, down, diagonal):
> ```text
> ACG
> A-T
> ```
> 3. **Scaling**: the same count for two sequences of length 100 is about $10^{75}$ (Exercise 3). An aligner never lists paths: the recurrence of Deeper (L2), with "add" replaced by "take the best score", finds the optimum in $O(nm)$ cells ([[Sequence Alignment]]).

## Common misconceptions

> [!warning] "$\binom{n}{k}$ counts ordered choices"
> $\binom{n}{k}$ ignores order. Ordered choices of $k$ distinct items are $n!/(n-k)! = k!\binom{n}{k}$.

> [!warning] "There are $\binom{n}{k}$ sequences with $k$ mutations"
> $\binom{n}{k}$ counts the sets of mutated *positions*. Each position can change to 3 other bases, so there are $\binom{n}{k} 3^k$ mutant sequences.

> [!warning] "The number of alignments is $\binom{n+m}{n}$"
> That counts paths made only of gaps. Alignments also use diagonal steps, giving the larger $D(n, m)$; and two paths that differ only in the order of adjacent gaps may be treated as the same alignment by some conventions, so always say what is being counted.

## Exercises

> [!question] Exercise 1 (L1)
> Compute $\binom{10}{3}$. In how many ways can 2 mutated sites be chosen among 100? How many distinct double mutants of a 100-nt sequence exist?

> [!success]- Solution
> $\binom{10}{3} = \frac{10 \cdot 9 \cdot 8}{6} = 120$. $\binom{100}{2} = 4950$ position pairs. Each of the 2 sites has 3 alternatives: $4950 \times 9 = 44{,}550$ double mutants.

> [!question] Exercise 2 (L2)
> Prove that $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$ for $n \ge 1$, and interpret it.

> [!success]- Solution
> Binomial theorem with $x = -1$, $y = 1$: $(-1 + 1)^n = 0$. A finite non-empty set has as many subsets of even size as of odd size. This identity is the engine of the [[Inclusion-Exclusion Principle]]. `[sum((-1)**k * comb(n, k) for k in range(n + 1)) for n in range(1, 6)]` gives `[0, 0, 0, 0, 0]`.

> [!question] Exercise 3 (L3, Python)
> Compare $\log_{10}$ of the number of gap-only paths, of all alignment paths, and of $4^n$ for two sequences of length $n = 10, 100, 1000$.

> [!success]- Solution
> ```python
> from math import comb, log10
>
> for n in (10, 100, 1000):
>     print(n, round(log10(comb(2 * n, n)), 1), round(log10(alignment_paths(n, n)), 1),
>           round(n * log10(4), 1))
> ```
> Output:
> ```text
> 10 5.3 6.9 6.0
> 100 59.0 75.3 60.2
> 1000 600.3 763.8 602.1
> ```
> Gap-only paths grow like $4^n/\sqrt{\pi n}$, slightly below $4^n$; all alignment paths grow faster, roughly $10^{0.76 n}$. Listing them is impossible beyond tiny $n$, while dynamic programming fills only $(n+1)^2$ cells.

> [!question] Exercise 4 (L3)
> What fraction of all 20-mers have composition exactly (5, 5, 5, 5)? Why is this the most frequent composition, yet rare?

> [!success]- Solution
> $\binom{20}{5,5,5,5}/4^{20} = 11{,}732{,}745{,}024 / 1{,}099{,}511{,}627{,}776 \approx 0.0107$. The multinomial coefficient is largest when the parts are as equal as possible, but there are $\binom{23}{3} = 1771$ possible compositions (place 3 separators among $20 + 3$ slots), so the mass is spread over many nearby classes.

## Mastery checklist

- [ ] 1 Recognized: I can define $\binom{n}{k}$, compute small values and write rows of Pascal's triangle.
- [ ] 2 Understood: I can prove the formula, Pascal's rule and the binomial theorem by counting arguments.
- [ ] 3 Practiced: I can count mutants, Hamming neighbourhoods, compositions and alignment paths, and check them by enumeration in Python.
- [ ] 4 Applied: I used these counts to justify dynamic programming in [[04-alignment-engine]] and to size mismatch neighbourhoods for k-mer search.
- [ ] 5 Explained: I can teach multinomial coefficients, Delannoy counts and the growth of $\binom{2n}{n}$, including numerical pitfalls.

## References

[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, treatment of counting (binomial and multinomial coefficients, the binomial theorem, combinatorial proofs) and of asymptotics (Stirling's formula).
[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]], counting part.
[^compeau-ori]: [[Bioinformatics Algorithms (Compeau)]], chapter "Where in the Genome Does DNA Replication Begin?" (approximate k-mer occurrences, mismatch neighbourhoods).
[^compeau-align]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Compare Biological Sequences?" (alignment as a path in a grid).
[^blitzstein]: [[Introduction to Probability (Blitzstein)]], treatment of the binomial distribution.
