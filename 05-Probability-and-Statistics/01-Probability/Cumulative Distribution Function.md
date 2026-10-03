---
aliases:
  - CDF
  - Distribution Function
  - Survival Function
  - Tail Probability
  - Fonction de répartition
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Random Variable]]"
  - "[[Probability Distribution]]"
related:
  - "[[P-Value]]"
  - "[[Quantile]]"
  - "[[Empirical Cumulative Distribution Function]]"
  - "[[Hypothesis Testing]]"
  - "[[Uniform Distribution]]"
  - "[[Probability Density Function]]"
  - "[[Random Variate Generation]]"
  - "[[Binomial Distribution]]"
  - "[[Variant Calling]]"
projects:
  - "[[05-sequence-search]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Nielsen 2011 - Genotype and SNP Calling from Next-Generation Sequencing Data]]"
---

# Cumulative Distribution Function

> [!abstract]
> The cumulative distribution function $F(x) = P(X \le x)$ accumulates probability from the left; its complement $1 - F$ gives tail probabilities, and a p-value is exactly such a tail.

## Definition

The **cumulative distribution function** (CDF) of a [[Random Variable]] $X$ is the function $F_X : \mathbb{R} \to [0, 1]$,

$$F_X(x) = P(X \le x).$$

Every CDF is non-decreasing, right-continuous, tends to 0 as $x \to -\infty$ and to 1 as $x \to +\infty$; conversely, the CDF determines the distribution of $X$. Unlike the PMF it is defined for every random variable, discrete or continuous.[^blitz3][^mit4a] For a discrete $X$ with PMF $p$ ([[Probability Distribution]]), $F(x) = \sum_{k \le x} p(k)$.

## Why it matters

- **p-values are tail probabilities.** A [[P-Value]] is the probability, under the null hypothesis, of a test statistic at least as extreme as the one observed,[^openstax9][^mit] for a large-is-extreme statistic $P(T \ge t_{\text{obs}}) = 1 - F(t_{\text{obs}}^-)$. Every significance call, from a variant caller to a k-mer over-representation test, evaluates a CDF ([[Hypothesis Testing]]).
- **Quantiles invert the CDF**: median read depth, coverage percentiles and critical values of tests are values of $F^{-1}$ ([[Quantile]]).
- **Simulation**: feeding uniform random numbers through $F^{-1}$ produces draws from any distribution ([[Random Variate Generation]]).
- **Comparing distributions**: the empirical CDF of data (coverage, p-values, expression) is the basis of Q-Q plots and of the Kolmogorov-Smirnov test ([[Empirical Cumulative Distribution Function]]).

## Core (L1)

### A step function

For a discrete variable, $F$ is flat between support points and jumps at each point $k$ by exactly $p(k)$. The figure shows $X \sim \mathrm{Bin}(10, 1/2)$, the number of reads carrying the alternative allele at a heterozygous site sequenced 10 times ([[Binomial Distribution]]).

![[cdf-step-tail-quantile.svg]]

At a jump, $F$ takes the upper value (filled dot): $F(7) = P(X \le 7)$ includes $p(7)$. Between jumps it is constant: $F(7.5) = F(7)$.

### Probabilities of intervals and tails

From $F$ alone:

| Quantity | Formula | Bin(10, 1/2) |
|---|---|---|
| lower tail $P(X \le x)$ | $F(x)$ | $F(7) = 968/1024 = 0.9453$ |
| upper tail $P(X > x)$ | $1 - F(x)$ | $P(X > 7) = 0.0547$ |
| $P(a < X \le b)$ | $F(b) - F(a)$ | $P(1 < X \le 7) = 0.9346$ |
| $P(X = k)$, integer $X$ | $F(k) - F(k - 1)$ | $p(5) = 0.2461$ |
| $P(X \ge k)$, integer $X$ | $1 - F(k - 1)$ | $P(X \ge 8) = 0.0547$ |

For a discrete variable **$\le$ and $<$ differ**: $P(X \ge 8) = 1 - F(7)$, not $1 - F(8)$. The function $S(x) = 1 - F(x) = P(X > x)$ is called the **survival function**.

### p-values are tail probabilities

At a site sequenced 30 times, 4 reads show a non-reference base. Null hypothesis: no variant, and each read shows that base only by a sequencing error, with probability 0.01 per read, independently. Then the number of such reads is $X \sim \mathrm{Bin}(30, 0.01)$ and "at least as extreme as 4" means $X \ge 4$:

$$p = P(X \ge 4) = 1 - F(3) \approx 2.2 \times 10^{-4}.$$

Four error reads out of 30 are rare under the null, so the site deserves attention. Real callers model errors per read from base qualities and weigh genotypes rather than testing one null ([[Genotype Likelihood]], [[Variant Calling]]).[^nielsen]

## Deeper (L2)

### The quantile function

A discrete $F$ has no ordinary inverse (it is flat, then jumps), so one uses the **generalized inverse**

$$Q(u) = F^{-1}(u) = \min\{x : F(x) \ge u\}, \qquad 0 < u < 1.$$

$Q(0.5)$ is a median. For $\mathrm{Bin}(10, 1/2)$, $Q(0.025) = 2$, $Q(0.5) = 5$, $Q(0.975) = 8$: at a heterozygous site with depth 10, from 2 to 8 alternative reads is the typical range, and $P(2 \le X \le 8) = 1 - 2 \cdot 11/1024 = 0.9785$ ([[Quantile]]).

### Inverse transform sampling

The key property of $Q$ is $Q(u) \le x \iff u \le F(x)$. If $U$ is uniform on $(0, 1)$ ([[Uniform Distribution]]), then

$$P(Q(U) \le x) = P(U \le F(x)) = F(x),$$

so $Q(U)$ has CDF $F$. This turns any CDF into a sampler (code below: 100,000 draws give mean 4.99 and $P(X \ge 8) \approx 0.0551$, against 5 and 0.0547 exactly).

### Discrete p-values are conservative

A discrete statistic can only produce a few p-values. For $X \sim \mathrm{Bin}(10, 1/2)$ with the upper-tail p-value $P(X \ge x)$, the attainable values near the top are 0.1719 ($x = 7$), 0.0547 ($x = 8$), 0.0107 ($x = 9$) and 0.001 ($x = 10$). A test "reject if $p \le 0.05$" rejects only for $x \ge 9$, so under the null it rejects with probability 0.0107, well below 0.05. With very few reads, no outcome at all is significant: at depth 4, the smallest possible p-value is $1/16 = 0.0625$ (Exercise 4). Low counts limit what any test can detect.

## Advanced (L3)

### The probability integral transform

If $F$ is continuous, $U = F(X)$ is uniform on $(0, 1)$.[^blitz5] Consequently, a p-value computed from a continuous test statistic is uniform under the null hypothesis, which is why a histogram of p-values from a genome-wide screen is flat where nulls dominate ([[P-Value]], [[Uniform Distribution]]). For a discrete statistic $F(X)$ takes finitely many values and p-values satisfy only $P(p \le \alpha) \le \alpha$: their histogram under the null piles up near 1 and has gaps, a pattern to recognize when many genes or sites have low counts.

### Computing tails without losing them

$1 - F(x)$ subtracts two numbers close to 1, and double precision keeps about 16 significant digits ([[Floating-Point Arithmetic]]). For $X \sim \mathrm{Bin}(100, 0.01)$ and 40 error reads, $1 - F(39)$ returns $8.9 \times 10^{-16}$, pure rounding error, while summing the tail directly gives $7.6 \times 10^{-53}$. Even the direct sum fails when single terms underflow: for 400 of 1,000 reads, $0.01^{400}$ is below the smallest double, and only a log-space computation (log-gamma for the coefficients, log-sum-exp for the sum) gives $\log_{10} p \approx -511.9$ (Exercise 5). Compute the upper tail directly, or its logarithm, never as `1 - cdf` ([[Numerical Stability]]).

## Mathematical representation

- $F_X(x) = P(X \le x)$ for $x \in \mathbb{R}$. Properties: $x \le y \Rightarrow F(x) \le F(y)$; $\lim_{h \downarrow 0} F(x + h) = F(x)$; $F(-\infty) = 0$, $F(+\infty) = 1$. Left limit: $F(x^-) = P(X < x)$, so $P(X = x) = F(x) - F(x^-)$.
- Discrete: $F(x) = \sum_{k \le x} p(k)$. Continuous with density $f$: $F(x) = \int_{-\infty}^{x} f(t)\, dt$ ([[Probability Density Function]]).
- Survival function $S(x) = 1 - F(x) = P(X > x)$; for integer $X$, $P(X \ge k) = S(k - 1)$.
- Quantile function $Q(u) = \inf\{x : F(x) \ge u\}$, with $Q(u) \le x \iff u \le F(x)$; if $U \sim \mathrm{Unif}(0, 1)$ then $Q(U)$ has CDF $F$.
- Upper-tail p-value for an observed $t$: $p(t) = P_{H_0}(T \ge t) = 1 - F_T(t^-)$.

## Computational representation

A discrete CDF is a running sum of the PMF; store the PMF and compute tails by summing the tail directly.

```python
from math import comb


def binom_pmf(n: int, p: float) -> dict[int, float]:
    return {k: comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)}


def cdf(pmf: dict, x: float) -> float:
    """F(x) = P(X <= x)."""
    return sum((p for v, p in pmf.items() if v <= x), 0.0)


def upper_tail(pmf: dict, x: float) -> float:
    """P(X >= x), summed directly (no 1 - F cancellation)."""
    return sum((p for v, p in pmf.items() if v >= x), 0.0)


def quantile(pmf: dict, u: float) -> float:
    """Generalized inverse: smallest x with F(x) >= u."""
    total = 0.0
    for v in sorted(pmf):
        total += pmf[v]
        if total >= u:
            return v
    return max(pmf)


het = binom_pmf(10, 0.5)                      # alt reads at a heterozygous site, depth 10
print(round(cdf(het, 7), 4), round(1 - cdf(het, 7), 4), round(upper_tail(het, 8), 4))
print(round(cdf(het, 7.5), 4), cdf(het, -1), round(cdf(het, 10), 4))
print([quantile(het, u) for u in (0.025, 0.5, 0.975)])

err = binom_pmf(30, 0.01)                     # error reads showing the alt base, depth 30
print("p-value of 4 alt reads:", f"{upper_tail(err, 4):.2e}")
deep = binom_pmf(100, 0.01)
print(1 - cdf(deep, 39), f"{upper_tail(deep, 40):.2e}")
```

```text
0.9453 0.0547 0.0547
0.9453 0.0 1.0
[2, 5, 8]
p-value of 4 alt reads: 2.23e-04
8.881784197001252e-16 7.63e-53
```

Inverse transform sampling and the discreteness of p-values, checked by simulation (seeded):

```python
import random
from math import comb

def binom_pmf(n, p):
    return {k: comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)}

def upper_tail(pmf, x):
    return sum((p for v, p in pmf.items() if v >= x), 0.0)

def quantile(pmf, u):
    total = 0.0
    for v in sorted(pmf):
        total += pmf[v]
        if total >= u:
            return v
    return max(pmf)

# 1. inverse-transform sampling from a PMF
rng = random.Random(8)
het = binom_pmf(10, 0.5)
draws = [quantile(het, rng.random()) for _ in range(100_000)]
print(round(sum(draws) / len(draws), 3), round(sum(d >= 8 for d in draws) / len(draws), 4))

# 2. discrete p-values are conservative
pvals = {x: upper_tail(het, x) for x in het}
size = sum(het[x] for x in het if pvals[x] <= 0.05)
print({x: round(p, 4) for x, p in pvals.items() if x >= 7}, round(size, 4))
sim = [pvals[quantile(het, rng.random())] for _ in range(100_000)]
print(round(sum(p <= 0.05 for p in sim) / len(sim), 4))
```

```text
4.99 0.0551
{7: 0.1719, 8: 0.0547, 9: 0.0107, 10: 0.001} 0.0107
0.0106
```

## Worked example

> [!example] A p-value and a critical value for error reads
> Site with depth $n = 30$; null model: each read shows a given non-reference base by error with probability $\varepsilon = 0.01$, independently, so $X \sim \mathrm{Bin}(30, 0.01)$.
> 1. **Lower CDF values.** $F(0) = 0.99^{30} = 0.7397$; $F(1) = F(0) + 30 (0.01)(0.99)^{29} = 0.9639$; $F(2) = F(1) + 435 (0.01)^2 (0.99)^{28} = 0.9967$; $F(3) = 0.99978$.
> 2. **p-value of 4 alternative reads.** $P(X \ge 4) = 1 - F(3) \approx 2.2 \times 10^{-4}$.
> 3. **Critical value at level $10^{-3}$.** Find the smallest $c$ with $P(X \ge c) \le 10^{-3}$: $P(X \ge 3) = 1 - F(2) = 0.0033$ is too large, $P(X \ge 4) = 0.00022$ is small enough, so $c = 4$. It is a quantile: $c - 1 = Q(0.999)$.
> 4. **Interpretation.** The model assumes independent errors. If they are not independent (for example, the same DNA fragment read twice, or an error that recurs at this position), extreme counts become more likely and this p-value is too small: it is a first screen, not a call.

## Common misconceptions

> [!warning] "$P(X \ge k) = 1 - F(k)$"
> For an integer variable $1 - F(k) = P(X > k)$, which leaves out $P(X = k)$. For $\mathrm{Bin}(10, 1/2)$ the error changes $P(X \ge 8)$ from 0.0547 to 0.0107. With continuous variables the distinction disappears, which is why the habit forms.

> [!warning] "A p-value is the probability that the null hypothesis is true"
> It is a tail probability computed **assuming** the null: $P(\text{data this extreme} \mid H_0)$. The probability of $H_0$ given the data needs a prior and [[Bayes' Theorem]]; see [[P-Value]].

> [!warning] "Under the null, p-values are always uniform"
> Only for continuous statistics. Discrete statistics (small counts) give p-values that are conservative and lumpy; a p-value histogram with a spike at 1 often just means many low-count features.

## Exercises

> [!question] Exercise 1 (L1)
> $X$ has PMF $p(0) = 0.3$, $p(1) = 0.4$, $p(2) = 0.2$, $p(3) = 0.1$. Give $F(x)$ for all real $x$, then $F(1.7)$, $F(-2)$, $F(5)$, $P(1 < X \le 3)$, $P(X \ge 2)$ and $P(X > 2)$.

> [!success]- Solution
> $F(x) = 0$ for $x < 0$; $0.3$ on $[0, 1)$; $0.7$ on $[1, 2)$; $0.9$ on $[2, 3)$; $1$ for $x \ge 3$. So $F(1.7) = 0.7$, $F(-2) = 0$, $F(5) = 1$. $P(1 < X \le 3) = F(3) - F(1) = 0.3$. $P(X \ge 2) = 1 - F(1) = 0.3$. $P(X > 2) = 1 - F(2) = 0.1$.

> [!question] Exercise 2 (L1)
> At a heterozygous site with depth 10, the alternative read count is $\mathrm{Bin}(10, 1/2)$, with $F(1) = 11/1024$ and $F(7) = 968/1024$. Compute $P(X \le 1)$, $P(X \ge 8)$ and $P(2 \le X \le 7)$. What does a filter that discards heterozygous calls with fewer than 2 alternative reads lose?

> [!success]- Solution
> $P(X \le 1) = 11/1024 = 0.0107$. $P(X \ge 8) = 1 - F(7) = 56/1024 = 0.0547$. $P(2 \le X \le 7) = F(7) - F(1) = 957/1024 = 0.9346$. The filter discards about 1.1 % of true heterozygous sites at depth 10, purely by sampling chance.

> [!question] Exercise 3 (L2)
> With the PMF of Exercise 1, compute $Q(0.3)$, $Q(0.5)$ and $Q(0.95)$. Why is $Q(0.3) = 0$ and not 1?

> [!success]- Solution
> $F$ takes the values 0.3, 0.7, 0.9, 1 at 0, 1, 2, 3. $Q(u)$ is the smallest $x$ with $F(x) \ge u$: $Q(0.3) = 0$ (since $F(0) = 0.3 \ge 0.3$), $Q(0.5) = 1$, $Q(0.95) = 3$. The definition uses $\ge$, so a level hit exactly by a jump belongs to that support point.

> [!question] Exercise 4 (L2, Python)
> A one-sided test of allelic imbalance at a heterozygous site uses $p = P(X \ge x)$ with $X \sim \mathrm{Bin}(n, 1/2)$. The smallest attainable p-value is $0.5^n$. Find the smallest depth $n$ at which the test can reject at $\alpha = 0.05$ and at $\alpha = 0.001$.

> [!success]- Solution
> ```python
> for alpha in (0.05, 0.001):
>     n = 1
>     while 0.5 ** n > alpha:
>         n += 1
>     print(alpha, n)
> # 0.05 5
> # 0.001 10
> ```
>
> Below depth 5, no data can reach $p \le 0.05$ ($0.5^4 = 0.0625$), and below depth 10 none can reach $10^{-3}$. A screen that tests every site, including low-depth ones, contains tests with no power at all.

> [!question] Exercise 5 (L3, Python)
> Implement `log_upper_tail(x, n, p)` returning $\log P(X \ge x)$ for $X \sim \mathrm{Bin}(n, p)$ with `math.lgamma` and log-sum-exp. Compare with the direct sum for $(x, n) = (4, 30), (40, 100), (400, 1000)$ at $p = 0.01$.

> [!success]- Solution
> ```python
> import math
>
>
> def log_binom_pmf(k: int, n: int, p: float) -> float:
>     """Natural log of P(X = k) for X ~ Bin(n, p), via log-gamma (no overflow)."""
>     return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
>             + k * math.log(p) + (n - k) * math.log1p(-p))
>
>
> def log_upper_tail(x: int, n: int, p: float) -> float:
>     """log P(X >= x) by log-sum-exp over the tail terms."""
>     terms = [log_binom_pmf(k, n, p) for k in range(x, n + 1)]
>     m = max(terms)
>     return m + math.log(sum(math.exp(t - m) for t in terms))
>
>
> for x, n in ((4, 30), (40, 100), (400, 1000)):
>     lt = log_upper_tail(x, n, 0.01)
>     direct = sum(math.comb(n, k) * 0.01 ** k * 0.99 ** (n - k) for k in range(x, n + 1))
>     print(n, x, f"log10 p = {lt / math.log(10):.2f}", f"direct = {direct:.3g}")
> # 30 4 log10 p = -3.65 direct = 0.000223
> # 100 40 log10 p = -52.12 direct = 7.63e-53
> # 1000 400 log10 p = -511.92 direct = 0
> ```
>
> Subtracting the maximum before exponentiating keeps every term representable; the largest term is then $e^0 = 1$. The direct sum returns 0 for the last case because $0.01^{400} = 10^{-800}$ underflows. Working with, and reporting, $-\log_{10} p$ avoids the problem.

## Mastery checklist

- [ ] 1 Recognized: I can define $F(x) = P(X \le x)$ and sketch the step CDF of a discrete variable.
- [ ] 2 Understood: I can derive interval and tail probabilities from $F$ and explain why a p-value is a tail probability.
- [ ] 3 Practiced: I can compute CDFs, tails and quantiles in Python, sample by inverse transform, and compute tails in log space.
- [ ] 4 Applied: in [[10-genomic-pipeline]], I compute and check the p-values of an error model at real sites, knowing which are limited by depth.
- [ ] 5 Explained: I can teach the probability integral transform, why discrete p-values are conservative, and why `1 - cdf` is the wrong way to compute tiny tails.

## References

[^blitz3]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 3 "Random Variables and Their Distributions".
[^blitz5]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 5 "Continuous Random Variables".
[^mit4a]: [[MIT 18.05 - Introduction to Probability and Statistics]], Spring 2022, Reading 4a "Discrete Random Variables".
[^mit]: [[MIT 18.05 - Introduction to Probability and Statistics]], frequentist statistics part (hypothesis testing and p-values).
[^openstax9]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 9 (hypothesis testing with one sample).
[^nielsen]: [[Nielsen 2011 - Genotype and SNP Calling from Next-Generation Sequencing Data]], genotype likelihoods and probabilistic calling.
