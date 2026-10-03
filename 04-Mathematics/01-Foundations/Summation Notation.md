---
aliases:
  - Sigma Notation
  - Product Notation
  - Pi Notation
  - Double Sum
  - Notation sigma
tags:
  - type/concept
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Set]]"
  - "[[Function]]"
related:
  - "[[Logarithm]]"
  - "[[Mathematical Induction]]"
  - "[[GC Content]]"
  - "[[Independence (Probability)]]"
  - "[[Likelihood Function]]"
  - "[[Maximum Likelihood Estimation]]"
  - "[[Numerical Stability]]"
projects:
  - "[[01-dna-engine]]"
  - "[[08-phylogenetic-engine]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
---

# Summation Notation

> [!abstract]
> $\sum$ and $\prod$ write long sums and products in one symbol. Bioinformatics runs on them: GC content is a sum over positions, the likelihood of an alignment is a product over its columns, and the logarithm turns that product into a sum that a computer can actually evaluate.

## Definition

For integers $m \le n$ and numbers $a_m, \dots, a_n$,
$$\sum_{i=m}^{n} a_i = a_m + a_{m+1} + \dots + a_n, \qquad \prod_{i=m}^{n} a_i = a_m \times a_{m+1} \times \dots \times a_n.$$
$i$ is the **index**, a bound variable (any letter works); $m$ and $n$ are the **limits**; $a_i$ is the general **term**. Over a finite set $S$ one writes $\sum_{x \in S} f(x)$. The **empty sum** (no terms, for instance $n < m$) is 0 and the **empty product** is 1, the neutral elements of $+$ and $\times$.[^lehman]

## Why it matters

- **Composition and counts.** GC content is a normalized sum of indicators over positions ([[GC Content]], [[01-dna-engine]]); k-mer counts and expected counts are sums over positions ([[K-mer]], [[Expected Value]]).
- **Likelihoods.** Felsenstein's likelihood method assumes that sites evolve independently, so the likelihood of a tree is a product over alignment columns and its logarithm a sum ([[Independence (Probability)]], [[Maximum Likelihood Phylogenetics]], [[08-phylogenetic-engine]]).[^f81][^durbin8]
- **Scores.** An alignment score adds log-odds terms over aligned pairs: a sum that is the logarithm of a likelihood ratio between a related and a random model ([[Substitution Matrix]]).[^durbin2]
- **Numerics.** A product of thousands of probabilities underflows to 0 in floating point, the sum of their logarithms does not ([[Numerical Stability]], [[10-genomic-pipeline]]).

## Core (L1)

### Reading and expanding

$\sum_{i=1}^{4} i^2 = 1 + 4 + 9 + 16 = 30$ and $\prod_{i=1}^{4} i = 24 = 4!$. With the **indicator** $\mathbb{1}[\text{condition}]$, equal to 1 when the condition holds and 0 otherwise, counting becomes summing. For $s = s_1 \dots s_n$:
$$\mathrm{GC}(s) = \frac{1}{n} \sum_{i=1}^{n} \mathbb{1}[s_i \in \{G, C\}].$$

### Rules

| Rule | Sum | Product |
|---|---|---|
| constant term | $\sum_{i=1}^{n} c = nc$ | $\prod_{i=1}^{n} c = c^n$ |
| constant factor | $\sum_{i} c\,a_i = c \sum_{i} a_i$ | $\prod_{i=1}^{n} c\,a_i = c^n \prod_{i=1}^{n} a_i$ |
| split the term | $\sum_{i} (a_i + b_i) = \sum_{i} a_i + \sum_{i} b_i$ | $\prod_{i} a_i b_i = \prod_{i} a_i \prod_{i} b_i$ |
| split the range | $\sum_{i=1}^{n} a_i = \sum_{i=1}^{k} a_i + \sum_{i=k+1}^{n} a_i$ | $\prod_{i=1}^{n} a_i = \prod_{i=1}^{k} a_i \cdot \prod_{i=k+1}^{n} a_i$ |

There is **no** such rule for $\sum_i a_i b_i$: in general $\sum_i a_i b_i \ne \big(\sum_i a_i\big)\big(\sum_i b_i\big)$.

### Index shifts

Substituting $j = i - 1$ changes the term *and* both limits: $\sum_{i=1}^{n} a_i = \sum_{j=0}^{n-1} a_{j+1}$. This is the conversion between 1-based positions (biology, many file formats) and 0-based indices (Python) ([[Genomic Coordinate System]]). A sequence of length $n$ has $\sum_{i=0}^{n-k} 1 = n - k + 1$ windows of length $k$, whether starts are counted from 0 or from 1.

### Bio: from a product of probabilities to a sum of logarithms

If the bases of $s$ are independent with probabilities $\pi_A, \pi_C, \pi_G, \pi_T$ ([[Independence (Probability)]]), grouping equal factors and taking logarithms gives
$$P(s) = \prod_{i=1}^{n} \pi_{s_i} = \prod_{x \in \{A, C, G, T\}} \pi_x^{\,n_x}, \qquad \log P(s) = \sum_{x} n_x \log \pi_x,$$
where $n_x$ is the number of positions holding $x$: the likelihood depends on the sequence only through its counts. The same step, $\log \prod = \sum \log$ for positive terms, turns the likelihood of the $m$ columns $x^{(1)}, \dots, x^{(m)}$ of an alignment under independent sites and parameters $\theta$ into a log-likelihood:[^f81][^durbin8]
$$L = \prod_{j=1}^{m} P\big(x^{(j)} \mid \theta\big), \qquad \log L = \sum_{j=1}^{m} \log P\big(x^{(j)} \mid \theta\big).$$

## Deeper (L2)

### Double sums

A double sum adds over a grid of index pairs. For finite sums the order does not matter, and a product of separate factors factorizes:
$$\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} = \sum_{j=1}^{n} \sum_{i=1}^{m} a_{ij}, \qquad \sum_{i} \sum_{j} a_i b_j = \Big(\sum_{i} a_i\Big)\Big(\sum_{j} b_j\Big).$$
Over the unordered pairs of $n$ sequences, the **triangular** sum can be cut by rows or by columns:
$$\sum_{1 \le i < j \le n} a_{ij} = \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} a_{ij} = \sum_{j=2}^{n} \sum_{i=1}^{j-1} a_{ij}.$$

![[double-sum-index-grid.svg]]

With $a_{ij} = 1$, row $i$ holds $n - i$ cells, so the number of pairs is $\sum_{i=1}^{n-1} (n - i) = \sum_{k=1}^{n-1} k = \frac{n(n-1)}{2}$: a [[Distance Matrix]] of 1,000 sequences needs 499,500 comparisons.

### Closed forms

$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$: write the sum forwards and backwards and add, giving $n$ pairs each summing to $n + 1$ (or use [[Mathematical Induction]]). For $r \ne 1$, the geometric sum is $\sum_{k=0}^{n} r^k = \frac{1 - r^{n+1}}{1 - r}$, proved by **telescoping**: $(1 - r)\sum_{k=0}^{n} r^k = \sum_{k=0}^{n} (r^k - r^{k+1}) = 1 - r^{n+1}$, since every intermediate power cancels.[^lehman]

### Sums inside products

When each site has an unobserved state $z$ (a genotype, a rate class, a hidden state), the probability of a site sums over states and the likelihood multiplies over sites:
$$L = \prod_{j=1}^{m} \sum_{z} P(z)\, P\big(x^{(j)} \mid z\big), \qquad \log L = \sum_{j=1}^{m} \log \sum_{z} P(z)\, P\big(x^{(j)} \mid z\big).$$
The logarithm passes through the product, not through the inner sum: $\log \sum \ne \sum \log$ ([[Law of Total Probability]], [[Genotype Likelihood]]).

## Advanced (L3)

- **log-sum-exp.** To compute $\log \sum_z e^{\ell_z}$ from log-probabilities $\ell_z$ without underflow, factor out $M = \max_z \ell_z$:
$$\log \sum_z e^{\ell_z} = M + \log \sum_z e^{\ell_z - M}.$$
The identity is exact, and the largest term becomes $e^0 = 1$, so the inner sum lies between 1 and the number of terms. It lets mixture and hidden-state likelihoods be computed entirely on the log scale ([[Numerical Stability]], [[Hidden Markov Model]]).
- **Distributivity is an algorithm.** A sum over all joint values of hidden variables of a product of factors can be reorganized by pulling factors out of inner sums:
$$\sum_{z_1} \sum_{z_2} f(z_1)\, g(z_1, z_2) = \sum_{z_1} f(z_1) \sum_{z_2} g(z_1, z_2).$$
Applied along a chain or a tree, this replaces a sum over exponentially many joint assignments by a recursion with polynomially many terms. It is the principle of the forward algorithm of hidden Markov models and of Felsenstein's computation of a tree likelihood from the tips to the root ([[Felsenstein Pruning Algorithm]], [[Dynamic Programming]]).[^f81][^durbin3]

## Mathematical representation

- **Recursive definition.** $\sum_{i=m}^{n} a_i = 0$ if $n < m$, and $\big(\sum_{i=m}^{n-1} a_i\big) + a_n$ otherwise; the same with $\times$ and 1 for $\prod$. Every rule above follows by [[Mathematical Induction]] on $n$ from this definition.
- **Change of variable.** For a bijection $\sigma$ of a finite index set $S$, $\sum_{x \in S} a_{\sigma(x)} = \sum_{x \in S} a_x$: reordering terms changes nothing ([[Function]]). The shift $j = i - 1$ and the reversal $j = n + 1 - i$ are such bijections between index ranges.
- **Logarithms.** For $a_i > 0$: $\log \prod_{i} a_i = \sum_{i} \log a_i$ and $\prod_{i} a_i = \exp\big(\sum_{i} \log a_i\big)$ ([[Logarithm]], [[Exponential Function]]).
- **Grouping by value.** $\sum_{i=1}^{n} f(s_i) = \sum_{x} n_x f(x)$ with $n_x = \sum_{i} \mathbb{1}[s_i = x]$: a sum over positions becomes a sum over the alphabet, the step behind count-based likelihoods.

## Computational representation

Python's `sum` and `math.prod` implement $\sum$ and $\prod$ over any iterable, with the empty conventions built in; below, GC content, log-likelihoods and underflow, a triangular double sum cut by rows and by columns, and log-sum-exp:

```python
import math
from collections import Counter

seq = "ATGCGCGTTAGC"                                  # invented
gc = sum(1 for x in seq if x in "GC") / len(seq)      # (1/n) * sum of indicators
print(len(seq), round(gc, 3))
print(sum(i * i for i in range(1, 5)), math.prod(range(1, 5)))   # 1+4+9+16 and 1*2*3*4
print(sum([]), math.prod([]))                         # empty sum, empty product

def log_likelihood(seq: str, pi: dict) -> float:
    """log P(seq) = sum_i log pi[s_i] = sum_x n_x log pi[x], bases independent."""
    return sum(n_x * math.log(pi[x]) for x, n_x in Counter(seq).items())

uniform = dict.fromkeys("ACGT", 0.25)
gc_rich = {"A": 0.15, "C": 0.35, "G": 0.35, "T": 0.15}
lu, lg = log_likelihood(seq, uniform), log_likelihood(seq, gc_rich)
print(round(lu, 3), round(lg, 3), round(lg - lu, 3))

long_seq = seq * 300                                  # 3,600 bases
print(math.prod(uniform[x] for x in long_seq))        # the product underflows to 0.0
print(round(log_likelihood(long_seq, uniform), 1))    # the sum of logs does not

seqs = ["ACGT", "ACGA", "TCGA", "TCCA"]               # invented, aligned

def d(u: str, v: str) -> int:
    return sum(a != b for a, b in zip(u, v))           # Hamming distance

n = len(seqs)
by_rows = sum(d(seqs[i], seqs[j]) for i in range(n) for j in range(i + 1, n))
by_cols = sum(d(seqs[i], seqs[j]) for j in range(n) for i in range(j))
print(n * (n - 1) // 2, by_rows, by_cols)

def logsumexp(values: list[float]) -> float:
    m = max(values)
    return m + math.log(sum(math.exp(v - m) for v in values))

logs = [-1000.0, -1001.0, -1002.0]                    # log-probabilities of three alternatives
print(sum(math.exp(v) for v in logs))                 # naive: every term underflows
print(round(logsumexp(logs), 4))
```

```text
12 0.583
30 24
0 1
-16.636 -16.834 -0.199
0.0
-4990.7
6 10 10
0.0
-999.5924
```

## Worked example

> [!example] Which composition model explains a sequence better? (invented data)
> $s$ = `ATGCGCGTTAGC`, $n = 12$, with $n_A = 2$, $n_C = 3$, $n_G = 4$, $n_T = 3$, so GC = 7/12 = 0.583.
> 1. **Uniform model**, $\pi_x = 0.25$: $\log L_U = 12 \log 0.25 = -16.636$.
> 2. **GC-rich model**, $\pi_G = \pi_C = 0.35$ and $\pi_A = \pi_T = 0.15$: $\log L_G = 7 \log 0.35 + 5 \log 0.15 = -16.834$.
> 3. **Compare** with the log-likelihood ratio, itself a sum: $\log(L_G / L_U) = 7 \log(0.35/0.25) + 5 \log(0.15/0.25) = -0.199$. The uniform model fits slightly better: 58 % GC is closer to 50 % than to 70 %.
> 4. **Scale up.** For the same composition over 3,600 bases, the product of probabilities is `0.0` in floating point while the log-likelihood is $-4990.7$: comparisons must be made on the log scale.

## Common misconceptions

> [!warning] "The log of a sum is the sum of the logs"
> Only $\log \prod = \sum \log$. A likelihood with hidden states keeps a sum inside each logarithm; replacing $\log \sum_z P(z) P(x \mid z)$ by $\sum_z P(z) \log P(x \mid z)$ gives a smaller number, because the logarithm is concave (Exercise 5).

> [!warning] "$\sum_i a_i b_i = (\sum_i a_i)(\sum_i b_i)$"
> Only a double sum of $a_i b_j$ over a full grid of independent indices factorizes. $\sum_{i=1}^{2} i \cdot i = 5$, but $(1 + 2)(1 + 2) = 9$.

> [!warning] "Shifting the index only renames it"
> A shift changes the term and both limits. Converting $\sum_{i=1}^{n} a_i$ to `range(0, n)` without rewriting $a_i$ as $a_{j+1}$ is the classic off-by-one error.

## Exercises

> [!question] Exercise 1 (L1)
> Compute $\sum_{i=1}^{5} (2i - 1)$ and $\prod_{i=1}^{3} (i + 1)$. Which closed form does the first suggest, and why is it true?

> [!success]- Solution
> $1 + 3 + 5 + 7 + 9 = 25$ and $2 \times 3 \times 4 = 24$. The sum of the first $n$ odd numbers is $n^2$: since $2i - 1 = i^2 - (i - 1)^2$, the sum telescopes to $n^2 - 0^2$.

> [!question] Exercise 2 (L1)
> A quality track $q_1, \dots, q_N$ is stored 0-based in a Python list `q`, with `q[j]` $= q_{j+1}$. Rewrite $\sum_{i=p}^{p+w-1} q_i$ (1-based positions $p$ to $p + w - 1$) with $j = i - 1$, and give the matching slice.

> [!success]- Solution
> $\sum_{j=p-1}^{p+w-2} q_{j+1}$, that is `sum(q[p - 1 : p + w - 1])`: the slice starts at $p - 1$ and its end is exclusive, so it covers exactly $w$ values.

> [!question] Exercise 3 (L2)
> Count the unordered pairs among $n$ sequences by summing the columns of the triangle instead of its rows, and evaluate for $n = 1000$.

> [!success]- Solution
> Column $j$ holds the $j - 1$ cells with $i < j$: $\sum_{j=2}^{n} (j - 1) = \sum_{k=1}^{n-1} k = \frac{n(n-1)}{2}$, the same total as by rows. For $n = 1000$: $1000 \times 999 / 2 = 499{,}500$.

> [!question] Exercise 4 (L2, Python)
> Find the smallest $n$ for which Python computes `0.25 ** n` as `0.0`, and the log-likelihood of a 1,000,000 bp sequence under the uniform model.

> [!success]- Solution
> ```python
> from itertools import count
>
> print(next(n for n in count(1) if 0.25 ** n == 0.0))
> print(round(1_000_000 * math.log(0.25), 1))
> ```
> Output: `538`, then `-1386294.4`. A product of a few hundred base probabilities already underflows; the log-likelihood of a whole bacterial genome is an ordinary number.

> [!question] Exercise 5 (L3, Python)
> Three sites, two hidden rate classes with probabilities 0.7 and 0.3, and invented per-class site likelihoods. Compute $\log L = \sum_j \log \sum_z P(z) P(x_j \mid z)$ with `logsumexp`, and compare it with the wrong $\sum_j \sum_z P(z) \log P(x_j \mid z)$.

> [!success]- Solution
> ```python
> p_class = [0.7, 0.3]                                   # invented class probabilities
> site_lik = [[1e-5, 4e-3], [2e-4, 1e-3], [3e-6, 5e-4]]  # invented P(x_j | class)
> right = sum(logsumexp([math.log(p) + math.log(l) for p, l in zip(p_class, row)])
>             for row in site_lik)
> wrong = sum(sum(p * math.log(l) for p, l in zip(p_class, row)) for row in site_lik)
> print(round(right, 3), round(wrong, 3))
> ```
> Output: `-23.239 -28.932`. The wrong version moves the logarithm inside the mixture and underestimates the log-likelihood by almost 6 units, a factor of about $e^{5.7} \approx 300$ in likelihood.

## Mastery checklist

- [ ] 1 Recognized: I can read $\sum$ and $\prod$ with their index, limits and term, and know the empty conventions.
- [ ] 2 Understood: I can explain why log-likelihoods are sums, why $\log \sum \ne \sum \log$, and how an index shift changes the limits.
- [ ] 3 Practiced: I manipulate sums with the rules, shift indices, swap the order of double sums and derive closed forms.
- [ ] 4 Applied: I computed GC content and log-likelihoods on real sequences in [[01-dna-engine]] or [[08-phylogenetic-engine]] without underflow.
- [ ] 5 Explained: I can teach log-sum-exp and how distributing products over sums turns an exponential sum into dynamic programming.

## References

[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision (sum and product notation, arithmetic and geometric sums).
[^f81]: [[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]], Felsenstein J, *Journal of Molecular Evolution* 17(6):368-376: likelihood of a tree as a product over independently evolving sites, computed recursively from the tips to the root.
[^durbin8]: [[Biological Sequence Analysis (Durbin)]], ch. 8 "Probabilistic approaches to phylogeny".
[^durbin2]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment" (random model and log-odds scores).
[^durbin3]: [[Biological Sequence Analysis (Durbin)]], ch. 3 "Markov chains and hidden Markov models" (forward algorithm).
