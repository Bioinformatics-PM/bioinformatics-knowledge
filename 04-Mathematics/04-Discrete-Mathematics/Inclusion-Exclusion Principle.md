---
aliases:
  - Inclusion–Exclusion
  - Inclusion Exclusion
  - Sieve Principle
  - Sieve Formula
  - Principe d'inclusion-exclusion
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Set]]"
  - "[[Combinatorics]]"
  - "[[Binomial Coefficient]]"
related:
  - "[[Probability]]"
  - "[[Independence (Probability)]]"
  - "[[Multiple Testing Correction]]"
  - "[[Permutation]]"
  - "[[Genomic Interval Arithmetic]]"
  - "[[Mutation]]"
projects: []
sources:
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[An Introduction to Statistical Learning (James)]]"
---

# Inclusion-Exclusion Principle

> [!abstract]
> To count a union of overlapping sets, add the sizes of the sets, subtract the pairwise overlaps, add back the triple overlaps, and so on: the rule that turns "genes found by at least one screen" and "at least one site mutates" into exact numbers.

## Definition

For finite sets $A_1, \dots, A_n$, the **inclusion-exclusion principle** states[^lehman][^mcs]

$$\left|\bigcup_{i=1}^{n} A_i\right| = \sum_{\emptyset \ne S \subseteq \{1, \dots, n\}} (-1)^{|S|+1} \left|\bigcap_{i \in S} A_i\right|.$$

For two sets, $|A \cup B| = |A| + |B| - |A \cap B|$; for three,

$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|.$$

The same identity holds for probabilities of events, with $P$ in place of $|\cdot|$.[^blitzstein]

## Why it matters

- **Merging results.** Genes reported by several screens, variants called by several callers, k-mers shared by several samples: the size of the union needs the overlaps ([[Set]]).
- **"At least one" probabilities.** At least one mutated site, at least one false positive among many tests, at least one occurrence of a motif: all are probabilities of unions.
- **Multiple testing.** Truncating the formula after its first term gives the union bound $P(\bigcup E_i) \le \sum P(E_i)$, on which the Bonferroni correction rests ([[Multiple Testing Correction]]).[^james]
- **Counting with constraints.** Sequences that use every base, or avoid several forbidden patterns, are counted by including and excluding the violations.

## Core (L1)

### Why the signs alternate

Adding $|A| + |B| + |C|$ counts each element once per set containing it. Track an element by the number $t$ of sets it belongs to:

| element lies in | counted by $+\sum \lvert A_i \rvert$ | by $-\sum \lvert A_i \cap A_j \rvert$ | by $+\lvert A \cap B \cap C \rvert$ | total |
|---|---:|---:|---:|---:|
| exactly 1 set | 1 | 0 | 0 | 1 |
| exactly 2 sets | 2 | $-1$ | 0 | 1 |
| all 3 sets | 3 | $-3$ | $+1$ | 1 |

Every element of the union ends up counted exactly once (the general proof is in the Mathematical representation).

### Bio: genes hit by at least one of several screens

Three genetic screens report gene sets $A$, $B$, $C$. Summing the list lengths counts a gene found by two screens twice; the formula corrects this using the pairwise and triple overlaps (worked example). With the lists in hand, Python sets compute the union directly; the formula matters when only summary counts are published, and as a check.

### Bio: the probability that at least one site mutates

Let $E_i$ be the event "site $i$ mutates", $i = 1, \dots, n$, each with probability $p$. Inclusion-exclusion needs $P(\bigcap_{i \in S} E_i)$ for every set of sites $S$. If sites mutate **independently** ([[Independence (Probability)]]), this is $p^{|S|}$, and there are $\binom{n}{j}$ sets of size $j$, so

$$P\Big(\bigcup_i E_i\Big) = \sum_{j=1}^{n} (-1)^{j+1}\binom{n}{j} p^j = 1 - (1 - p)^n$$

by the binomial theorem ([[Binomial Coefficient]]): the same answer as the complement route, $1 - P(\text{no site mutates})$. For $n = 20$ sites and $p = 0.05$: $1 - 0.95^{20} \approx 0.64$, not $20 \times 0.05 = 1$.

## Deeper (L2)

- **Bounds from truncation.** Write $S_1 = \sum P(E_i)$ and $S_2 = \sum_{i<j} P(E_i \cap E_j)$. Then $S_1 - S_2 \le P(\bigcup E_i) \le S_1$ (proof in the Mathematical representation). The upper bound needs no independence: testing $m$ hypotheses each at level $\alpha/m$ makes the probability of at least one false positive at most $\alpha$, which is the Bonferroni correction.[^james] In the 20-site example, $S_1 = 1$, $S_1 - S_2 = 0.525$, and the exact value 0.6415 lies between them; the three-term truncation, 0.6675, is again above it.
- **Complement (sieve) form.** The elements of a universe $U$ lying in *none* of the $A_i$ number $\sum_{S \subseteq \{1..n\}} (-1)^{|S|} |\bigcap_{i \in S} A_i|$, with the empty intersection equal to $U$.
- **k-mers using all four bases.** Let $A_x$ be the k-mers missing base $x$. A k-mer missing every base of a set $S$ uses only $4 - |S|$ letters: $(4 - |S|)^k$ of them. Hence the number of k-mers containing all four bases is $\sum_{j=0}^{4} (-1)^j \binom{4}{j} (4 - j)^k = 4^k - 4 \cdot 3^k + 6 \cdot 2^k - 4$: 1560 for $k = 6$.
- **Derangements.** Let $A_i$ be the permutations of $n$ items fixing item $i$; permutations fixing every item of $S$ number $(n - |S|)!$. The sieve form gives $D_n = n! \sum_{j=0}^{n} (-1)^j / j!$ permutations with no fixed point, so a random shuffle of $n$ distinct items leaves none in place with probability $\sum_{j \le n} (-1)^j/j! \to e^{-1} \approx 0.368$ (Exercise 5, [[Permutation]]).

## Advanced (L3)

- **Exponential cost.** The general formula has $2^n - 1$ terms. It is practical only for a few sets, or when intersections depend only on $|S|$ (then $n$ terms suffice, as in the mutation and k-mer examples). For many explicit sets, build the union with a hash set; for genomic intervals, merge sorted endpoints in one sweep ([[Genomic Interval Arithmetic]]).
- **Dependence is where the formula earns its keep.** Occurrences of a motif at overlapping positions are not independent: knowing `AAAA` starts at position $i$ makes a start at $i + 1$ more likely. $1 - (1-p)^n$ is then wrong, while inclusion-exclusion, with the correct joint probabilities, stays exact.
- **Rare events.** For independent events of equal probability $p$, $S_2 = \binom{n}{2}p^2 \approx S_1^2/2$, so when $S_1$ is small the union bound $S_1$ is nearly exact. When events overlap heavily (strongly dependent tests), the union is much smaller than $S_1$, which is why the Bonferroni bound becomes conservative.

## Mathematical representation

- **Proof of the formula.** Take $x \in \bigcup A_i$ lying in exactly $t \ge 1$ of the sets. It belongs to $\bigcap_{i \in S} A_i$ exactly when $S$ is a non-empty subset of those $t$ sets, so the right-hand side counts it
$$\sum_{j=1}^{t} (-1)^{j+1} \binom{t}{j} = 1 - \sum_{j=0}^{t} (-1)^{j} \binom{t}{j} = 1 - (1 - 1)^t = 1$$
time. Elements outside the union lie in no intersection and are counted 0 times. $\square$
- **Probability version.** On a finite sample space, weight each outcome by its probability instead of 1; the same per-element argument applies.
- **Two-sided bound.** For $x$ in exactly $t \ge 1$ sets, $S_1$ counts it $t \ge 1$ times and $S_1 - S_2$ counts it $t - \binom{t}{2}$ times. Now $t - \frac{t(t-1)}{2} \le 1 \iff (t-1)(t-2) \ge 0$, true for every integer $t \ge 1$. Summing over elements: $S_1 - S_2 \le |\bigcup A_i| \le S_1$.
- **Exactly one set.** By the same bookkeeping, the elements lying in exactly one of the sets number $S_1 - 2S_2 + 3S_3 - \dots$, since $t - 2\binom{t}{2} + 3\binom{t}{3} - \dots$ equals 1 for $t = 1$ and 0 for $t \ge 2$ (checked for three sets in the worked example).

## Computational representation

```python
from itertools import combinations, product
from fractions import Fraction
from math import comb
import random

def union_size(sets):
    """|A1 u ... u An| by inclusion-exclusion (2^n - 1 intersection terms)."""
    total = 0
    for r in range(1, len(sets) + 1):
        for group in combinations(sets, r):
            total += (-1) ** (r + 1) * len(set.intersection(*group))
    return total

rng = random.Random(3)
genes = [f"g{i:03d}" for i in range(300)]                   # invented gene identifiers
A, B, C = (set(rng.sample(genes, size)) for size in (120, 90, 60))
print(union_size([A, B, C]), len(A | B | C))

n, p = 20, Fraction(1, 20)
exact = 1 - (1 - p) ** n
alternating = sum((-1) ** (j + 1) * comb(n, j) * p**j for j in range(1, n + 1))
print(exact == alternating, round(float(exact), 4))
truncations = [float(sum((-1) ** (j + 1) * comb(n, j) * p**j for j in range(1, t + 1))) for t in (1, 2, 3)]
print([round(x, 4) for x in truncations])

def all_four_bases(k):
    return 4**k - 4 * 3**k + 6 * 2**k - 4 * 1**k

print(all_four_bases(6), sum(1 for w in product("ACGT", repeat=6) if set(w) == set("ACGT")))
```

```text
204 204
True 0.6415
[1.0, 0.525, 0.6675]
1560 1560
```

`Fraction` keeps the alternating sum exact; in floating point, large alternating sums can lose all their digits to cancellation.

## Worked example

> [!example] Three screens (invented summary counts)
> Screen sizes $|A| = 120$, $|B| = 90$, $|C| = 60$; overlaps $|A \cap B| = 30$, $|A \cap C| = 20$, $|B \cap C| = 15$, $|A \cap B \cap C| = 8$.
> 1. **Union**: $S_1 - S_2 + S_3 = 270 - 65 + 8 = 213$ genes hit by at least one screen.
> 2. **Region check.** All three: 8. Exactly $A$ and $B$: $30 - 8 = 22$; exactly $A$ and $C$: 12; exactly $B$ and $C$: 7. Only $A$: $120 - 22 - 12 - 8 = 78$; only $B$: $90 - 22 - 7 - 8 = 53$; only $C$: $60 - 12 - 7 - 8 = 33$. Sum: $8 + 22 + 12 + 7 + 78 + 53 + 33 = 213$.
> 3. **Exactly one screen**: $S_1 - 2S_2 + 3S_3 = 270 - 130 + 24 = 164 = 78 + 53 + 33$.
> 4. **Common slip**: stopping after the pairwise term gives 205, missing the 8 genes that were added three times and subtracted three times.

## Common misconceptions

> [!warning] "The union is the sum of the list lengths"
> Only for disjoint lists (the sum rule of [[Combinatorics]]). Otherwise every shared element is over-counted.

> [!warning] "For three sets, subtract the pairwise overlaps and stop"
> Elements in all three sets are then added 3 times and subtracted 3 times, so they vanish. The triple intersection must be added back.

> [!warning] "$P(\text{at least one}) = np$"
> $np$ is the union bound, an upper bound that can exceed 1. With $n = 1000$ sites and $p = 0.001$, $np = 1$ while the true probability under independence is 0.632.

> [!warning] "$1 - (1 - p)^n$ is the inclusion-exclusion answer"
> It is the answer only when the events are independent with equal probability $p$. Inclusion-exclusion itself needs no independence, only the probabilities of the intersections.

## Exercises

> [!question] Exercise 1 (L1)
> Two differential expression analyses report 250 and 180 genes, 70 in both. How many genes are reported by at least one? By exactly one?

> [!success]- Solution
> $250 + 180 - 70 = 360$. Exactly one: $360 - 70 = 290$ (or $S_1 - 2S_2 = 430 - 140$).

> [!question] Exercise 2 (L2)
> 1000 sites mutate independently, each with probability 0.001. Compute the probability that at least one mutates, the union bound, and the lower bound $S_1 - S_2$.

> [!success]- Solution
> Exact: $1 - 0.999^{1000} \approx 0.6323$. Upper bound $S_1 = 1000 \times 0.001 = 1$. $S_2 = \binom{1000}{2} 0.001^2 = 0.4995$, so $S_1 - S_2 = 0.5005$. The truth lies in $[0.5005, 1]$, as proved.

> [!question] Exercise 3 (L2, Python)
> Derive the number of 6-mers that contain all four bases and check it by enumeration.

> [!success]- Solution
> Sieve form with $A_x$ = 6-mers missing $x$: $4^6 - 4 \cdot 3^6 + 6 \cdot 2^6 - 4 \cdot 1^6 = 4096 - 2916 + 384 - 4 = 1560$. The code above prints `1560 1560`.

> [!question] Exercise 4 (L3, Python)
> Prove $S_1 - S_2 \le |\bigcup A_i| \le S_1$, then check `union_size` and both bounds on 200 random families of 4 sets.

> [!success]- Solution
> Proof in the Mathematical representation.
> ```python
> ok = True
> for _ in range(200):
>     sets = [set(rng.sample(range(40), rng.randint(0, 25))) for _ in range(4)]
>     s1 = sum(len(s) for s in sets)
>     s2 = sum(len(a & b) for a, b in combinations(sets, 2))
>     u = len(set().union(*sets))
>     ok &= union_size(sets) == u and s1 - s2 <= u <= s1
> print(ok)
> ```
> Output: `True`.

> [!question] Exercise 5 (L3, Python)
> A permutation null model shuffles the labels of 10 distinct genes. What is the probability that no gene keeps its label? Compare with $e^{-1}$.

> [!success]- Solution
> $D_{10}/10! = \sum_{j=0}^{10} (-1)^j / j!$.
> ```python
> from math import factorial, exp
> from itertools import permutations
>
> def derangements(n):
>     return sum((-1) ** j * factorial(n) // factorial(j) for j in range(n + 1))
>
> print(derangements(10), round(derangements(10) / factorial(10), 6), round(exp(-1), 6))
> print([derangements(n) for n in range(1, 7)],
>       [sum(all(p[i] != i for i in range(n)) for p in permutations(range(n))) for n in range(1, 7)])
> ```
> Output: `1334961 0.367879 0.367879`, then `[0, 1, 2, 9, 44, 265] [0, 1, 2, 9, 44, 265]`. Already for 10 items the probability agrees with $e^{-1}$ to six decimals, and the formula matches enumeration for small $n$.

## Mastery checklist

- [ ] 1 Recognized: I can write the inclusion-exclusion formula for two and three sets.
- [ ] 2 Understood: I can explain why the signs alternate and prove the general formula with the binomial theorem.
- [ ] 3 Practiced: I can count unions, "exactly one", and constrained k-mers, and compute "at least one" probabilities exactly and by bounds, in Python.
- [ ] 4 Applied: I combined real gene or variant lists from several sources and reported the union and overlaps correctly.
- [ ] 5 Explained: I can teach the union bound behind Bonferroni, when $1 - (1-p)^n$ is valid, and why the formula is exponential in the number of sets.

## References

[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, treatment of counting (inclusion-exclusion).
[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]], counting part.
[^blitzstein]: [[Introduction to Probability (Blitzstein)]], treatment of probability foundations (inclusion-exclusion for events).
[^james]: [[An Introduction to Statistical Learning (James)]], treatment of multiple testing (family-wise error rate and the Bonferroni correction).
