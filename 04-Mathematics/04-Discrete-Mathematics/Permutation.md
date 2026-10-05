---
aliases:
  - Arrangement
  - k-Permutation
  - Partial Permutation
  - Factorial
  - Signed Permutation
  - Shuffle
  - Permutation (mathématiques)
tags:
  - type/concept
  - domain/mathematics
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Function]]"
  - "[[Combinatorics]]"
related:
  - "[[Binomial Coefficient]]"
  - "[[Permutation Test]]"
  - "[[Hypothesis Testing]]"
  - "[[Genome Rearrangement]]"
  - "[[Random Number Generation]]"
  - "[[Sorting]]"
  - "[[Suffix Array]]"
projects: []
sources:
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 6.042J - Mathematics for Computer Science]]"
  - "[[Introduction to Algorithms (Cormen)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Altschul 1985 - Significance of Nucleotide Sequence Alignments]]"
  - "[[Freeland 1998 - The Genetic Code Is One in a Million]]"
  - "[[An Introduction to Statistical Learning (James)]]"
---

# Permutation

> [!abstract]
> A permutation is a reordering: there are $n!$ ways to order $n$ distinct objects, and shuffling, relabelling or rearranging a genome are all permutations, which is why they serve as null models and as models of genome evolution.

## Definition

A **permutation** of a finite set $A$ is a bijection $\sigma : A \to A$ ([[Function]]). Listing $\sigma(1), \sigma(2), \dots, \sigma(n)$ for $A = \{1, \dots, n\}$ gives an arrangement of the $n$ elements in a row, and every arrangement arises this way, so there are $n! = n(n-1)\cdots 1$ permutations.[^lehman] More generally, an ordered selection of $k$ distinct elements among $n$ (a **$k$-permutation**) can be made in $n!/(n-k)!$ ways, and a multiset with $n_1, \dots, n_r$ copies of $r$ kinds of objects ($n = n_1 + \dots + n_r$) has $n!/(n_1! \cdots n_r!)$ distinct arrangements.[^lehman][^mcs]

## Why it matters

- **Null models.** A shuffled sequence keeps the composition of the original and destroys its order; comparing a real alignment score with scores of shuffled sequences tests whether the similarity exceeds what composition alone explains.[^altschul85]
- **Permutation tests.** Relabelling samples at random gives a null distribution for a test statistic without assuming a parametric distribution ([[Permutation Test]]).[^james]
- **Genome evolution.** Large-scale rearrangements reorder and flip blocks of genes; genomes are compared as signed permutations of shared blocks ([[Genome Rearrangement]]).[^compeau-rearr]
- **Algorithms.** Sorting is finding the permutation that orders the data ([[Sorting]]); a [[Suffix Array]] is a permutation of the positions of a text.[^compeau-bwt]

## Core (L1)

### Counting arrangements

| Situation | Count | Example |
|---|---|---|
| all $n$ distinct objects in order | $n!$ | 5 genes in a row: 120 orders |
| $k$ of $n$ distinct objects, order matters, no repetition | $\dfrac{n!}{(n-k)!}$ | ordered choice of 3 primers out of 10: 720 |
| $k$ positions, $n$ options each, repetition allowed | $n^k$ | $4^k$ DNA k-mers ([[Combinatorics]]) |
| multiset with counts $n_1, \dots, n_r$ | $\dfrac{n!}{n_1! \cdots n_r!}$ | distinct shuffles of `GATTACA`: 420 |

The last line is a **multinomial coefficient** ([[Binomial Coefficient]]). Proofs are in the Mathematical representation.

### Composition and inverse

Store a permutation of $\{0, \dots, n-1\}$ as the tuple of images: $\sigma = (1, 2, 0, 3)$ sends $0 \mapsto 1$, $1 \mapsto 2$, $2 \mapsto 0$, $3 \mapsto 3$. **Composition** $(\sigma \circ \tau)(i) = \sigma(\tau(i))$ applies $\tau$ first; the result is again a permutation, the identity leaves everything in place, and $\sigma^{-1}$ undoes $\sigma$. Composition is **not commutative**: with $\tau = (0, 1, 3, 2)$, $\sigma \circ \tau = (1, 2, 3, 0)$ but $\tau \circ \sigma = (1, 3, 0, 2)$ (computed below).

### Bio: shuffled sequences as null models

A **shuffle** applies a random permutation to the positions of a sequence. Shuffling keeps the base counts exactly and erases everything that depends on order: motifs, codon structure, dinucleotide biases. Altschul and Erickson judged the significance of nucleotide alignments by comparison with randomly permuted sequences, and designed permutations that also conserve dinucleotide and codon usage, because what the shuffle preserves defines the null hypothesis.[^altschul85] The same idea at the level of the genetic code: Freeland and Hurst compared the standard code with a million random alternative codes, obtained by reassigning amino acids among the codon blocks of the standard table, a space of $20! \approx 2.4 \times 10^{18}$ codes.[^freeland]

### Bio: permutation tests

To test whether expression differs between treated and control samples, assume the null hypothesis that labels do not matter. Then every relabelling of the samples is equally likely; recomputing the statistic for each relabelling gives its null distribution, and the p-value is the fraction of relabellings at least as extreme as the observed one ([[Permutation Test]], [[Hypothesis Testing]]).[^james] See the worked example.

## Deeper (L2)

- **Uniform random shuffles.** The Fisher-Yates procedure swaps position $i$ with a uniformly chosen $j \in \{0, \dots, i\}$, for $i = n-1$ down to 1.[^clrs] It makes $n \cdot (n-1) \cdots 2 = n!$ equally likely choice sequences, and distinct choice sequences give distinct permutations (the element placed at position $i$ is determined by the choice at step $i$), so by the bijection rule each permutation has probability exactly $1/n!$. The tempting variant "swap every position with any of the $n$ positions" makes $n^n$ equally likely choice sequences; since $n^n$ is not a multiple of $n!$ for $n \ge 3$ (27 is not a multiple of 6), it cannot be uniform.
- **Cycles and fixed points.** Following $i \mapsto \sigma(i) \mapsto \sigma(\sigma(i)) \dots$ returns to $i$, so every permutation splits into disjoint cycles; $(1, 2, 0, 3)$ is the 3-cycle $0 \to 1 \to 2 \to 0$ with the fixed point 3. A permutation with no fixed point is a **derangement**, counted with the [[Inclusion-Exclusion Principle]].

## Advanced (L3)

- **Signed permutations and rearrangements.** Two genomes sharing $n$ conserved blocks (synteny blocks) are compared by writing the order of the blocks in one genome, labelled by their order in the other, with a sign for orientation: a **signed permutation** such as $(+1, -3, -2, +4)$.[^compeau-rearr] There are $2^n\, n!$ of them. A **reversal** (inversion) of blocks $i..j$ reverses their order and flips their signs: reversing $-3, -2$ in the example gives $(+1, +2, +3, +4)$.
- **Breakpoints.** Frame $\pi$ with $\pi_0 = 0$ and $\pi_{n+1} = n + 1$. A consecutive pair $(\pi_i, \pi_{i+1})$ is an **adjacency** if $\pi_{i+1} - \pi_i = 1$ (this covers $+2, +3$ and its reversed form $-3, -2$) and a **breakpoint** otherwise.[^compeau-rearr] A reversal changes only the two pairs at its ends, so it removes at most 2 breakpoints, and the identity has none: the reversal distance satisfies $d(\pi) \ge \lceil b(\pi)/2 \rceil$ (Exercise 3). Compeau and Pevzner use breakpoints to argue that some genome regions are rearrangement hotspots.[^compeau-rearr]
- **Size of $n!$.** Stirling's formula, $n! \sim \sqrt{2\pi n}\,(n/e)^n$,[^lehman] gives $\log_2 n! \approx n \log_2 n$: identifying one order among $n!$ needs about $n \log_2 n$ bits, the root of the $\Omega(n \log n)$ lower bound for comparison sorting.[^clrs]

## Mathematical representation

- $S_n$ is the set of bijections of $[n] = \{1, \dots, n\}$. **$|S_n| = n!$** by the generalized product rule ([[Combinatorics]]): $n$ choices for $\sigma(1)$, then $n - 1$ for $\sigma(2)$ (any value but $\sigma(1)$), and so on.
- **$k$-permutations.** The same argument stopped after $k$ steps: $n(n-1)\cdots(n-k+1) = \dfrac{n!}{(n-k)!}$.
- **Multiset arrangements.** Label the $n_j$ copies of kind $j$ to make all $n$ objects distinct: $n!$ arrangements. Erasing labels is a $(n_1! \cdots n_r!)$-to-1 map (the copies of each kind can be relabelled among themselves in $n_j!$ ways), so the division rule gives $\dfrac{n!}{n_1! \cdots n_r!}$.
- **Group structure.** Composition is associative, $\mathrm{id}$ is neutral, every $\sigma$ has an inverse with $\sigma \circ \sigma^{-1} = \mathrm{id}$, and $(\sigma \circ \tau)^{-1} = \tau^{-1} \circ \sigma^{-1}$ ([[Function]]). For $n \ge 3$, $S_n$ is not commutative.
- **Signed permutations.** A choice of order ($n!$) and of $n$ signs ($2^n$), independent: $2^n\, n!$.

## Computational representation

```python
from itertools import permutations
from math import factorial, perm, prod
from collections import Counter
import random

n, k = 5, 3
print(sum(1 for _ in permutations(range(n), k)), perm(n, k), factorial(n) // factorial(n - k))

def compose(s, t):
    """(s o t)(i) = s(t(i)); a permutation of {0..n-1} is stored as the tuple of images."""
    return tuple(s[t[i]] for i in range(len(t)))

def inverse(s):
    inv = [0] * len(s)
    for i, si in enumerate(s):
        inv[si] = i
    return tuple(inv)

s, t = (1, 2, 0, 3), (0, 1, 3, 2)
print(compose(s, t), compose(t, s), compose(s, inverse(s)))

def n_shuffles(seq):
    """Distinct rearrangements of seq: n! / (n_A! n_C! n_G! n_T!)."""
    return factorial(len(seq)) // prod(factorial(c) for c in Counter(seq).values())

for seq in ("AACGT", "GATTACA"):
    print(seq, n_shuffles(seq), len(set(permutations(seq))))

def fisher_yates(seq, rng):
    a = list(seq)
    for i in range(len(a) - 1, 0, -1):
        j = rng.randint(0, i)              # uniform in {0, ..., i}
        a[i], a[j] = a[j], a[i]
    return "".join(a)

rng = random.Random(1)
print(sorted(Counter(fisher_yates("ACG", rng) for _ in range(60_000)).items()))
x = "ATGCGCGTATCG"
y = fisher_yates(x, rng)
print(y, Counter(y) == Counter(x))

def breakpoints(p):
    """Breakpoints of a signed permutation of 1..n, framed by 0 and n+1."""
    q = [0, *p, len(p) + 1]
    return sum(1 for a, b in zip(q, q[1:]) if b - a != 1)

def reversal(p, i, j):
    """Reverse p[i..j] (0-based, inclusive) and flip the signs of that block."""
    return p[:i] + [-v for v in reversed(p[i:j + 1])] + p[j + 1:]

p = [+1, -3, -2, +4]
print(breakpoints(p), reversal(p, 1, 2), breakpoints(reversal(p, 1, 2)))
```

```text
60 60 60
(1, 2, 3, 0) (1, 3, 0, 2) (0, 1, 2, 3)
AACGT 60 60
GATTACA 420 420
[('ACG', 9879), ('AGC', 9998), ('CAG', 9952), ('CGA', 9984), ('GAC', 10029), ('GCA', 10158)]
TGTCCGCAAGTG True
2 [1, 2, 3, 4] 0
```

The six orders of `ACG` each appear close to $60{,}000/6 = 10{,}000$ times, and the shuffle keeps the composition. In practice `random.shuffle` does the shuffling; seed the generator (`random.Random(seed)`) so that a null distribution can be reproduced ([[Random Number Generation]]).

## Worked example

> [!example] An exact permutation test on 3 versus 3 samples (invented values)
> Expression of one gene: treated 8.1, 7.4, 9.0; control 6.2, 6.9, 5.8.
> 1. **Statistic**: difference of means, $8.167 - 6.300 = 1.867$.
> 2. **Null hypothesis**: the labels are arbitrary, so any 3 of the 6 values could have been "treated". There are $\binom{6}{3} = 20$ relabellings ([[Binomial Coefficient]]), all equally likely under the null.
> 3. **Null distribution**: compute the statistic for each relabelling.
> ```python
> from itertools import combinations
>
> treated, control = [8.1, 7.4, 9.0], [6.2, 6.9, 5.8]
> values = treated + control
> observed = sum(treated) / 3 - sum(control) / 3
> diffs = []
> for group in combinations(range(6), 3):
>     a = [values[i] for i in group]
>     b = [values[i] for i in range(6) if i not in group]
>     diffs.append(sum(a) / 3 - sum(b) / 3)
> p_value = sum(d >= observed - 1e-9 for d in diffs) / len(diffs)
> print(len(diffs), round(observed, 3), p_value)    # 20 1.867 0.05
> ```
> 4. **p-value**: only the observed labelling (the three largest values as treated) reaches 1.867, so the one-sided p-value is $1/20 = 0.05$. The tolerance `1e-9` avoids missing ties through floating-point rounding.
> 5. **Lesson**: with 3 samples per group, 0.05 is the *smallest possible* one-sided p-value (Exercise 4).

## Common misconceptions

> [!warning] "A shuffled sequence is a random sequence"
> It is a random sequence *with exactly the original composition*. If the original is depleted in some dinucleotide, a plain shuffle restores it to the level expected from composition, and the null model becomes too easy to beat. Choose what to preserve on purpose.[^altschul85]

> [!warning] "$n^k$ and $n!/(n-k)!$ count the same thing"
> $n^k$ allows repetition: there are $4^4 = 256$ DNA 4-mers but only $4! = 24$ orders of the four distinct bases.

> [!warning] "A permutation test makes no assumptions"
> It assumes that, under the null hypothesis, the labels are exchangeable. If samples were processed in two batches that coincide with the groups, relabelling mixes batch and treatment and the test is invalid.

## Exercises

> [!question] Exercise 1 (L1)
> In how many orders can 5 genes be arranged along a chromosome segment? In how many ways can you pick an ordered list of 3 primers among 10? How many DNA 4-mers have four distinct bases?

> [!success]- Solution
> $5! = 120$; $10 \cdot 9 \cdot 8 = 720$; $4! = 24$ (out of $4^4 = 256$ 4-mers).

> [!question] Exercise 2 (L2)
> How many distinct sequences can a shuffle of `GATTACA` produce? Check with `n_shuffles` and by enumeration.

> [!success]- Solution
> Counts: A 3, T 2, G 1, C 1. $7!/(3!\,2!\,1!\,1!) = 5040/12 = 420$. The code above prints `GATTACA 420 420`.

> [!question] Exercise 3 (L3, Python)
> For the signed permutation $(+2, -1, +3)$, count breakpoints, derive a lower bound on the number of reversals needed to sort it, and find the true reversal distance by breadth-first search. Check the bound on all 48 signed permutations of 3 blocks.

> [!success]- Solution
> Framed: $0, 2, -1, 3, 4$. Pairs $(0, 2)$, $(2, -1)$, $(-1, 3)$ are breakpoints, $(3, 4)$ is an adjacency: $b = 3$, so at least $\lceil 3/2 \rceil = 2$ reversals.
> ```python
> from collections import deque
> from itertools import permutations, product
>
> def reversal_distance(p):
>     """Breadth-first search over signed permutations (fine for n <= 5)."""
>     target, start = tuple(range(1, len(p) + 1)), tuple(p)
>     seen, queue = {start: 0}, deque([start])
>     while queue:
>         q = queue.popleft()
>         if q == target:
>             return seen[q]
>         for i in range(len(q)):
>             for j in range(i, len(q)):
>                 r = tuple(reversal(list(q), i, j))
>                 if r not in seen:
>                     seen[r] = seen[q] + 1
>                     queue.append(r)
>
> print(breakpoints([+2, -1, +3]), reversal_distance([+2, -1, +3]))
> signed = [[s * v for s, v in zip(signs, order)]
>           for order in permutations((1, 2, 3)) for signs in product((1, -1), repeat=3)]
> print(len(signed), all(reversal_distance(q) >= (breakpoints(q) + 1) // 2 for q in signed),
>       max(reversal_distance(q) for q in signed))
> ```
> Output: `3 2`, then `48 True 3`. Two reversals suffice (reverse $+2, -1$ into $+1, -2$, then flip $-2$), matching the bound; the hardest signed permutation of 3 blocks needs 3.

> [!question] Exercise 4 (L3)
> In an exact two-group permutation test with $m$ samples per group, what is the smallest possible one-sided p-value? How many samples per group are needed before $p < 0.01$ is even possible?

> [!success]- Solution
> The observed labelling is one of $\binom{2m}{m}$ equally likely relabellings and is always counted, so $p \ge 1/\binom{2m}{m}$. $\binom{6}{3} = 20$ gives 0.05; $\binom{8}{4} = 70$ gives 0.014; $\binom{10}{5} = 252$ gives 0.004. At least 5 samples per group.

## Mastery checklist

- [ ] 1 Recognized: I can define a permutation and give $n!$, $n!/(n-k)!$, $n^k$ and the multinomial count with an example of each.
- [ ] 2 Understood: I can compose and invert permutations and explain what a shuffle preserves and destroys.
- [ ] 3 Practiced: I can implement Fisher-Yates, compute shuffle counts, breakpoints and an exact permutation test in Python.
- [ ] 4 Applied: I used shuffled sequences or label permutations as a null model on real data and justified what they preserve.
- [ ] 5 Explained: I can teach signed permutations, the breakpoint bound, and the exchangeability assumption of permutation tests.

## References

[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, treatment of counting (permutations, the division rule, arrangements of a multiset) and of asymptotics (Stirling's formula).
[^mcs]: [[MIT 6.042J - Mathematics for Computer Science]], counting part.
[^clrs]: [[Introduction to Algorithms (Cormen)]], 4th ed. (2022), treatment of randomly permuting arrays and of lower bounds for comparison sorting.
[^compeau-rearr]: [[Bioinformatics Algorithms (Compeau)]], chapter "Are There Fragile Regions in the Human Genome?" (synteny blocks, signed permutations, reversals, breakpoints).
[^compeau-bwt]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Locate Disease-Causing Mutations?" (suffix arrays).
[^altschul85]: [[Altschul 1985 - Significance of Nucleotide Sequence Alignments]], *Molecular Biology and Evolution* 2(6):526-538.
[^freeland]: [[Freeland 1998 - The Genetic Code Is One in a Million]], *Journal of Molecular Evolution* 47:238-248.
[^james]: [[An Introduction to Statistical Learning (James)]], treatment of multiple testing and resampling-based p-values.
