---
aliases:
  - Series
  - Geometric Series
  - Série numérique
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Limit]]"
  - "[[Summation Notation]]"
related:
  - "[[Taylor Series]]"
  - "[[Improper Integral]]"
  - "[[Geometric Distribution]]"
  - "[[Poisson Distribution]]"
  - "[[Hidden Markov Model]]"
  - "[[CpG Island]]"
  - "[[Expected Value]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
---

# Infinite Series

> [!abstract]
> An infinite series adds infinitely many terms; it has a sum when its partial sums settle on a limit, which is how probabilities over unbounded counts (run lengths, read counts) can add up to exactly 1.

## Definition

Given numbers $a_1, a_2, \dots$, the **partial sums** are $S_n = \sum_{k=1}^{n} a_k$. The series $\sum_{k=1}^{\infty} a_k$ **converges** to $S$ if $S_n \to S$ as $n \to \infty$; $S$ is its **sum**. Otherwise the series **diverges**.[^os2][^mit]

## Why it matters

- **Distributions on unbounded counts.** The geometric, Poisson and negative binomial distributions put probability on every integer $k \ge 0$; that they sum to 1, and their means, are series ([[Geometric Distribution]], [[Poisson Distribution]]).[^blitz4]
- **Run lengths and state durations.** How long a hidden Markov model stays in a state (inside a CpG island, inside an exon) is geometric, and its mean is a geometric series ([[Hidden Markov Model]], [[CpG Island]]).[^durbin3]
- **Approximations.** Power series ($e^x$, $\ln(1 + x)$) are the basis of the small-rate approximations used throughout sequence evolution and statistics ([[Taylor Series]]).
- **Existence of expectations.** A discrete mean $\sum_k k\,P(X = k)$ is a series: it exists only if the series converges ([[Expected Value]]).

## Core (L1)

**Geometric series.** For a ratio $r$, $S_n = 1 + r + \dots + r^{n-1}$ satisfies $S_n - rS_n = 1 - r^n$, so $S_n = \frac{1 - r^n}{1 - r}$ for $r \neq 1$. Hence[^os2]

$$\sum_{k=0}^{\infty} r^k = \frac{1}{1 - r} \quad\text{if } \lvert r \rvert < 1, \qquad\text{and the series diverges if } \lvert r \rvert \ge 1 .$$

More generally $\sum_{k=m}^{\infty} c\,r^k = \frac{c\,r^m}{1 - r}$: first term over $1 - r$.

**Divergence test.** If $a_k \not\to 0$, the series diverges. The converse is false.[^os2]

**The harmonic series diverges.** $\sum 1/k$ has terms tending to 0, yet grouping $\frac13 + \frac14 > \frac12$, $\frac15 + \dots + \frac18 > \frac12$, and so on, adds infinitely many halves. Its partial sums grow like $\ln n$ (see the table below).

**$p$-series.** $\sum_{k=1}^\infty \frac{1}{k^p}$ converges if and only if $p > 1$, exactly like $\int_1^\infty x^{-p}\,dx$ ([[Improper Integral]]); the integral test makes the comparison rigorous.[^os2]

| $n$ | $\sum_{k=1}^n 0.9^{k-1}$ | $H_n = \sum_{k=1}^n \frac1k$ | $H_n - \ln n$ |
|---:|---:|---:|---:|
| 10 | 6.513216 | 2.9290 | 0.6264 |
| 100 | 9.999734 | 5.1874 | 0.5822 |
| 1000 | 10.0 | 7.4855 | 0.5777 |
| 100,000 | 10.0 | 12.0901 | 0.5772 |

The geometric partial sums reach $1/(1 - 0.9) = 10$ quickly; the harmonic ones keep growing, by about $\ln 10 \approx 2.3$ per factor of 10 in $n$.

## Deeper (L2)

### Convergence tests

For series with positive terms:[^os2]

| Test | Statement | Typical use |
|---|---|---|
| Comparison | $0 \le a_k \le b_k$: $\sum b_k < \infty \Rightarrow \sum a_k < \infty$ | bound by a geometric or $p$-series |
| Ratio | $L = \lim a_{k+1}/a_k$: $L < 1$ converges, $L > 1$ diverges, $L = 1$ no conclusion | factorials, powers ($\lambda^k/k!$, $k^2/2^k$) |
| Integral | $a_k = f(k)$, $f$ positive decreasing: $\sum a_k$ and $\int_1^\infty f$ converge together | $p$-series, $\sum 1/(k \ln k)$ |

**Absolute and conditional convergence.** If $\sum \lvert a_k \rvert$ converges, so does $\sum a_k$ (absolute convergence). The alternating harmonic series $1 - \frac12 + \frac13 - \dots$ converges (to $\ln 2$, [[Taylor Series]]) although $\sum 1/k$ diverges: it converges only conditionally, and its sum depends on the order of the terms.[^os2]

### Geometric run lengths: CpG islands and HMM state durations

In a hidden Markov model, a state that loops back to itself with probability $a$ and leaves with probability $1 - a$ at each position produces a run of length $L$ with[^durbin3]

$$P(L = \ell) = (1 - a)\,a^{\ell - 1}, \qquad \ell = 1, 2, \dots$$

- **Probabilities sum to 1:** $\sum_{\ell \ge 1} (1 - a)a^{\ell - 1} = (1 - a) \cdot \frac{1}{1 - a} = 1$.
- **Mean length:** by the tail-sum formula ([[Expected Value]]), $E[L] = \sum_{\ell \ge 1} P(L \ge \ell) = \sum_{\ell \ge 1} a^{\ell - 1} = \frac{1}{1 - a}$.
- **Tail:** $P(L \ge \ell) = a^{\ell - 1}$, a geometric decay.

For a CpG-island state with $a = 0.999$ (invented), islands last $1/(1 - 0.999) = 1000$ bp on average. The self-transition probability is therefore set from the typical length of the feature being modeled, and the same logic gives the mean distance between stop codons in random sequence ([[Open Reading Frame]]).

### Poisson probabilities sum to 1

The exponential series $\sum_{k=0}^\infty \frac{\lambda^k}{k!} = e^{\lambda}$ converges for every $\lambda$: the ratio of consecutive terms is $\frac{\lambda}{k+1} \to 0 < 1$. Its value comes from the [[Taylor Series]] of $e^x$. Multiplying by $e^{-\lambda}$ gives $\sum_k e^{-\lambda}\frac{\lambda^k}{k!} = 1$, and the same series shifted by one gives the mean $\lambda$ ([[Poisson Distribution]]).[^blitz4]

## Mathematical representation

- $\sum_{k=1}^\infty a_k = S \iff \lim_{n \to \infty} S_n = S$, $S_n = \sum_{k=1}^n a_k$.
- **Geometric:** $\sum_{k=0}^{\infty} r^k = \frac{1}{1 - r}$, $\lvert r \rvert < 1$. Differentiating term by term (allowed inside the radius of convergence, [[Taylor Series]]): $\sum_{k=1}^\infty k\,r^{k-1} = \frac{1}{(1 - r)^2}$.
- **Necessary condition:** convergence implies $a_k \to 0$.
- **Tail of a convergent series:** $\sum_{k > n} a_k = S - S_n \to 0$; for a geometric series it equals $\frac{r^{n}}{1 - r}$ (index from 0), which bounds the truncation error.

## Computational representation

Sums are computed by accumulating terms until the remaining tail is provably small. Two numerical habits matter: build each term from the previous one (for $\lambda^k/k!$, multiply by $\lambda/k$) instead of computing huge powers and factorials, and stop on a bound of the tail rather than on a small last term.

```python
import math
import random

def partial_sums(term, checkpoints):
    """Partial sums S_n = term(1) + ... + term(n) at the requested n."""
    s, out = 0.0, []
    for k in range(1, max(checkpoints) + 1):
        s += term(k)
        if k in checkpoints:
            out.append((k, s))
    return out

checks = {10, 100, 1000, 100_000}
for (n, g), (_, h) in zip(partial_sums(lambda k: 0.9 ** (k - 1), checks),
                          partial_sums(lambda k: 1 / k, checks)):
    print(n, round(g, 6), round(h, 4), round(h - math.log(n), 4))

# Poisson probabilities: e^{-lam} lam^k / k!, built term by term (ratio lam / k)
lam, term, total, k = 30.0, math.exp(-30.0), math.exp(-30.0), 0
while 1 - total > 1e-12:
    k += 1
    term *= lam / k
    total += term
print("Poisson(30): terms up to k =", k, "sum =", total)

# HMM state with self-transition a: simulated durations versus 1 / (1 - a)
random.seed(3)
a = 0.95
def duration() -> int:
    length = 1
    while random.random() < a:
        length += 1
    return length
runs = [duration() for _ in range(100_000)]
print(round(sum(runs) / len(runs), 2), round(1 / (1 - a), 2),
      round(sum(r >= 50 for r in runs) / len(runs), 4), round(a ** 49, 4))
```

It prints the partial-sum table of the Core section, then:

```text
Poisson(30): terms up to k = 76 sum = 0.9999999999994293
19.97 20.0 0.0799 0.081
```

For $\lambda = 30$, the Poisson probabilities beyond $k = 76$ add up to less than $10^{-12}$; simulated state durations match the series values ($E[L] = 20$, $P(L \ge 50) = 0.95^{49}$).

## Worked example

> [!example] How long does an HMM stay in a state? (invented parameter)
> A gene-finding HMM has an intergenic state with self-transition $a = 0.95$.
>
> 1. **Distribution.** $P(L = \ell) = 0.05 \times 0.95^{\ell - 1}$.
> 2. **Check it is a distribution.** Geometric series with first term $0.05$ and ratio $0.95$: $\frac{0.05}{1 - 0.95} = 1$.
> 3. **Mean.** $\frac{1}{1 - 0.95} = 20$ positions.
> 4. **Long runs.** $P(L \ge 50) = 0.95^{49} \approx 0.081$.
> 5. **Most likely length.** $P(L = \ell)$ decreases with $\ell$, so the mode is 1: a single self-loop always makes length-1 runs the most frequent. Real intergenic regions are much longer than 1 bp, which is why gene finders chain several states or model durations explicitly ([[Hidden Markov Model]]).[^durbin3]

## Common misconceptions

> [!warning] "The terms tend to 0, so the series converges"
> $a_k \to 0$ is necessary, not sufficient: the harmonic series diverges. In data, $\sum 1/k$-type tails (as in some heavy-tailed count distributions) can make a mean infinite.

> [!warning] "Infinitely many positive terms must add up to infinity"
> The geometric series with $r = 1/2$ adds infinitely many positive terms and equals 2. This is what lets a run-length distribution give positive probability to every length and still total 1.

## Exercises

> [!question] Exercise 1 (L1)
> Compute $\sum_{k=0}^\infty (1/3)^k$ and $\sum_{k=1}^\infty 2(0.9)^k$.

> [!success]- Solution
> $\frac{1}{1 - 1/3} = 1.5$. First term $2 \times 0.9 = 1.8$, ratio $0.9$: $\frac{1.8}{0.1} = 18$.

> [!question] Exercise 2 (L2)
> Use the ratio test to show that $\sum_{k=1}^\infty \frac{k^2}{2^k}$ converges, and evaluate it numerically.

> [!success]- Solution
> $\frac{a_{k+1}}{a_k} = \frac{(k+1)^2}{2k^2} \to \frac12 < 1$: converges. `sum(k * k / 2 ** k for k in range(1, 200))` gives 6.0 (to rounding).

> [!question] Exercise 3 (L2)
> An HMM's "island" state has self-transition probability $0.99$. Give the mean island length and the probability that an island is longer than 300 positions.

> [!success]- Solution
> Mean $1/(1 - 0.99) = 100$ positions. $P(L > 300) = P(L \ge 301) = 0.99^{300} \approx 0.049$: about 1 island in 20 is more than three times the mean length.

> [!question] Exercise 4 (L2, Python)
> Adapt the Poisson loop above to $\lambda = 2$ and $\lambda = 100$. How many terms are needed to reach $1 - 10^{-12}$? Why would computing `lam ** k / math.factorial(k)` directly be a bad idea for $\lambda = 1000$?

> [!success]- Solution
> The loop stops at $k = 18$ for $\lambda = 2$ and $k = 178$ for $\lambda = 100$ (76 for $\lambda = 30$). For large $\lambda$ the cutoff sits about 8 standard deviations $\sqrt\lambda$ above the mean (7.8 for $\lambda = 100$); for small $\lambda$ the distribution is skewed and the cutoff is relatively further out (11.3 standard deviations for $\lambda = 2$). For $\lambda = 1000$, $1000^k$ overflows floating point (`OverflowError` for $k \ge 103$) and $e^{-1000}$ underflows to 0, so the product of the two is meaningless; the term-by-term ratio, or working with logarithms (`math.lgamma`), avoids both problems.

## Mastery checklist

- [ ] 1 Recognized: I can define partial sums and convergence, and give the sum of a geometric series.
- [ ] 2 Understood: I can explain why $a_k \to 0$ is not enough (harmonic series) and how the $p$-series mirrors the $p$-integral.
- [ ] 3 Practiced: I can apply comparison, ratio and integral tests and compute partial sums with a bounded tail in Python.
- [ ] 4 Applied: I can derive mean and tail probabilities of HMM state durations and check that discrete count distributions sum to 1.
- [ ] 5 Explained: I can teach why geometric durations have mode 1, why absolute convergence matters, and how to sum series stably on a computer.

## References

[^os2]: [[Calculus (OpenStax)]], Volume 2, sequences and series (infinite series, geometric and harmonic series, divergence, integral, comparison and ratio tests, alternating series).
[^mit]: [[MIT 18.01SC - Single Variable Calculus]], infinite series part.
[^blitz4]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 4 "Expectation" (geometric and Poisson distributions, their means via series).
[^durbin3]: [[Biological Sequence Analysis (Durbin)]], ch. 3 "Markov chains and hidden Markov models" (CpG islands; the geometric length distribution of a self-looping state and models with several states for other lengths).
