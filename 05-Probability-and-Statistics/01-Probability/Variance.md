---
aliases:
  - Var(X)
  - Standard Deviation of a Random Variable
  - Mean-Variance Relationship
  - Variance of a Sum
  - Écart-type
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Expected Value]]"
  - "[[Probability Distribution]]"
  - "[[Independence (Probability)]]"
related:
  - "[[Covariance]]"
  - "[[Bernoulli Distribution]]"
  - "[[Binomial Distribution]]"
  - "[[Poisson Distribution]]"
  - "[[Negative Binomial Distribution]]"
  - "[[Overdispersion]]"
  - "[[Conditional Expectation]]"
  - "[[Variance-Stabilizing Transformation]]"
  - "[[Biological Replicate]]"
projects:
  - "[[05-sequence-search]]"
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Harvard Stat 110 - Probability]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
---

# Variance

> [!abstract]
> Variance measures how far a random variable typically lands from its mean: it is the expected squared deviation. Variances of independent variables add, which is why averaging replicates reduces noise; for count data the variance is tied to the mean, and that relationship shapes every test on sequencing reads.

## Definition

For a random variable $X$ with mean $\mu = E[X]$ ([[Expected Value]]), the **variance** is

$$\operatorname{Var}(X) = E\big[(X - \mu)^2\big] = E[X^2] - \mu^2,$$

and the **standard deviation** is $\sigma = \sqrt{\operatorname{Var}(X)}$, expressed in the units of $X$. For a discrete variable, $\operatorname{Var}(X) = \sum_x (x - \mu)^2\, p_X(x)$.[^blitz4][^1805-5a][^stat110]

## Why it matters

- **Noise models are variance models.** Count-based differential expression models a gene's reads with a negative binomial, whose variance grows faster than its mean; assuming Poisson variance for biological replicates underestimates the noise and produces false positives ([[Differential Expression Analysis]], [[Overdispersion]]).[^holmes8]
- **Precision and sample size.** The standard deviation of a mean of $r$ replicates is $\sigma/\sqrt{r}$, and that of an allele fraction at depth $n$ is $\sqrt{p(1-p)/n}$ ([[Binomial Distribution]]): variance says how much data a question needs ([[Experimental Design]]).
- **Significance of counts.** A z-score (observed minus expected, divided by the standard deviation) is only as good as its variance: counts of self-overlapping words vary more than a Poisson count with the same mean (Deeper (L2)), which matters for the k-mer statistics of [[05-sequence-search]].

## Core (L1)

### Computing a variance

For $X$ = number of A in a random 3-mer (PMF $27/64, 27/64, 9/64, 1/64$, mean $3/4$):

$$E[X^2] = \frac{0 \cdot 27 + 1 \cdot 27 + 4 \cdot 9 + 9 \cdot 1}{64} = \frac{9}{8}, \qquad \operatorname{Var}(X) = \frac{9}{8} - \left(\frac{3}{4}\right)^2 = \frac{9}{16}, \qquad \sigma = \frac{3}{4}.$$

### Rules

| Rule | Formula | Bioinformatics reading |
|---|---|---|
| Shift and scale | $\operatorname{Var}(aX + b) = a^2 \operatorname{Var}(X)$, $\ \sigma_{aX+b} = \lvert a \rvert \sigma_X$ | rescaling counts to counts per million rescales their SD by the same factor |
| Independent sum | $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$ | reads of a library split over two lanes |
| Independent difference | $\operatorname{Var}(X - Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$ | treated minus control: both noises add |
| Any sum | $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2\operatorname{Cov}(X, Y)$ | overlapping k-mer windows ([[Covariance]]) |
| Mean of $n$ i.i.d. values | $\operatorname{Var}(\bar X) = \sigma^2/n$, SD $\sigma/\sqrt n$ | four times more replicates halve the SD |

The first two rows and the last follow from the definition and linearity (Mathematical representation).[^blitz4][^1805-5a] The covariance row holds for any pair of variables.[^blitz]

### The mean-variance relationship of count data

![[count-mean-variance-relationship.svg]]

| Count model | Mean | Variance | Typical use |
|---|---|---|---|
| [[Binomial Distribution]] $\mathrm{Bin}(n, p)$ | $np$ | $np(1-p)$, below the mean | alternative-allele reads among $n$ reads |
| [[Poisson Distribution]] $\mathrm{Pois}(\lambda)$ | $\lambda$ | $\lambda$ | depth at a base; a gene's count when one library is resequenced |
| [[Negative Binomial Distribution]] | $\mu$ | $\mu + \alpha\mu^2$ | a gene's count across biological replicates |

Resequencing one library adds Poisson sampling noise; independent biological samples also differ in their true expression level, which adds a term growing like $\mu^2$: **overdispersion**, with dispersion $\alpha$.[^holmes8] Three consequences:

1. **A raw variance means nothing without its mean.** Variance 100 is quiet for a gene with mean 1000 and noisy for a gene with mean 10.
2. **The coefficient of variation** $\mathrm{CV} = \sigma/\mu$ separates the two noise sources: $\mathrm{CV}^2 = 1/\mu + \alpha$. Depth shrinks the Poisson part $1/\mu$, never the biological part; with $\alpha = 0.1$ (an illustrative value), CV levels off at $\sqrt{0.1} \approx 0.32$.
3. **On log-log axes** the Poisson line has slope 1; the negative binomial bends to slope 2 once $\mu$ is well above $1/\alpha$, as in the figure.

## Deeper (L2)

### Variance of a sum of dependent indicators: word counts

The count of a word $w$ of length $k$ is a sum of window indicators ([[Expected Value#Expected occurrences of a k-mer]]), each with variance $p(1-p)$, $p = 4^{-k}$ ([[Bernoulli Distribution]]). Windows less than $k$ apart share bases, so

$$\operatorname{Var}(N_w) = \sum_i \operatorname{Var}(I_i) + 2 \sum_{i < j} \operatorname{Cov}(I_i, I_j),$$

where only pairs at distance $d < k$ contribute: $\operatorname{Cov} = P(I_i = I_{i+d} = 1) - p^2$, and $P(I_i = I_{i+d} = 1)$ is $4^{-(k+d)}$ if $w$ overlaps itself at shift $d$, and 0 otherwise. Exact values for random 10 kb sequences (code below), all with mean 39.05:

| Word | Self-overlap shifts | Variance | SD |
|---|---|---:|---:|
| ACGT | none | 37.98 | 6.16 |
| ATAT | 2 | 42.86 | 6.55 |
| AAAA | 1, 2, 3 | 63.61 | 7.98 |
| Poisson with the same mean | | 39.05 | 6.25 |

ACGT cannot overlap itself: nearby windows exclude each other, the covariances are negative and the count is slightly *less* variable than Poisson. AAAA occurrences come in clumps (AAAAA holds two), so its variance is 1.6 times the Poisson value. These exact SDs match the simulation of [[Expected Value#Computational representation]] (6.08 and 7.97).

### Standardizing: z-scores and Chebyshev's inequality

$Z = (X - \mu)/\sigma$ has mean 0 and variance 1 ([[Standard Score]]). Seventy occurrences of a 4-mer in a random 10 kb sequence give $z = (70 - 39.05)/6.16 = 5.0$ for ACGT but $z = 3.9$ for AAAA; a Poisson variance would give 4.95 for both, overstating the evidence for AAAA. **Chebyshev's inequality**, $P(\lvert X - \mu \rvert \ge c\sigma) \le 1/c^2$, holds for any distribution with finite variance:[^blitz] for $c = 3.9$ it guarantees a probability of at most 6.6 %: always valid, often loose. Exact tail probabilities need the distribution itself ([[Cumulative Distribution Function]]); the inequality is the engine of the [[Law of Large Numbers]].

## Advanced (L3)

### Law of total variance: where overdispersion comes from

Conditioning on the true expression level $\Lambda$ of a sample ([[Conditional Expectation]]):

$$\operatorname{Var}(X) = \underbrace{E[\operatorname{Var}(X \mid \Lambda)]}_{\text{technical (sampling)}} + \underbrace{\operatorname{Var}(E[X \mid \Lambda])}_{\text{biological}}.$$

With $X \mid \Lambda \sim \mathrm{Pois}(\Lambda)$ and $\Lambda$ gamma-distributed with mean $\mu$ and variance $\alpha\mu^2$ (shape $1/\alpha$, scale $\alpha\mu$), $\operatorname{Var}(X) = \mu + \alpha\mu^2$: the gamma-Poisson, or [[Negative Binomial Distribution]].[^holmes8] The general inequality $\operatorname{Var}(X) \ge E[X]$ for Poisson mixtures is derived in [[Poisson Distribution#Advanced (L3)]].

### Delta method and variance stabilization

For a smooth $g$ and a variable concentrated near $\mu$, a first-order Taylor expansion gives $\operatorname{Var}(g(X)) \approx g'(\mu)^2 \operatorname{Var}(X)$. The square root stabilizes Poisson counts (see [[Poisson Distribution]]). For negative binomial counts and the natural log, $g'(\mu) = 1/\mu$ and $\operatorname{Var}(\ln X) \approx (\mu + \alpha\mu^2)/\mu^2 = 1/\mu + \alpha$: on the log scale, well-expressed genes share a variance close to $\alpha$, while low counts carry the extra $1/\mu$. This is why log-transformed low counts look noisy and why variance-stabilizing transformations are used before clustering or PCA ([[Variance-Stabilizing Transformation]], [[Data Transformation]]).[^holmes-t]

### Estimating a variance from a few replicates

The sample variance $S^2 = \frac{1}{n-1}\sum_{i=1}^{n} (X_i - \bar X)^2$ is unbiased, $E[S^2] = \sigma^2$, because $\sum_i (X_i - \bar X)^2 = \sum_i (X_i - \mu)^2 - n(\bar X - \mu)^2$ has expectation $n\sigma^2 - \sigma^2$ ([[Estimator]], [[Measure of Dispersion]]). Unbiased is not precise: for normal data $(n-1)S^2/\sigma^2$ follows a chi-square distribution with $n - 1$ degrees of freedom ([[Chi-Square Distribution]]),[^blitz] so the relative SD of $S^2$ is $\sqrt{2/(n-1)}$, that is 100 % with three replicates. Gene-by-gene variances from three samples are unreliable, which is why count-based methods estimate dispersions by sharing information across genes ([[Empirical Bayes]], Exercise 4).[^holmes8]

## Mathematical representation

- **Definition.** $\operatorname{Var}(X) = \sum_x (x - \mu)^2 p_X(x)$, or $\int (x - \mu)^2 f(x)\, dx$ for a density.
- **Shortcut.** $E[(X - \mu)^2] = E[X^2] - 2\mu E[X] + \mu^2 = E[X^2] - \mu^2$.
- **Shift and scale.** $\operatorname{Var}(aX + b) = E[(aX + b - a\mu - b)^2] = a^2 \operatorname{Var}(X)$.
- **Sums.** $\operatorname{Var}\left(\sum_i X_i\right) = \sum_i \operatorname{Var}(X_i) + 2 \sum_{i < j} \operatorname{Cov}(X_i, X_j)$ with $\operatorname{Cov}(X, Y) = E[XY] - E[X]E[Y]$, which is 0 for independent variables. For the mean of $n$ i.i.d. variables, $\operatorname{Var}(\bar X) = n\sigma^2/n^2 = \sigma^2/n$.
- **Indicator.** $\mathbf{1}_A^2 = \mathbf{1}_A$, so $\operatorname{Var}(\mathbf{1}_A) = P(A) - P(A)^2 = P(A)\big(1 - P(A)\big)$.
- **Word count.** With $m = n - k + 1$ windows, $p = 4^{-k}$, and $c_d = 1$ if $w_{d+1} \dots w_k = w_1 \dots w_{k-d}$ (self-overlap at shift $d$), else 0:
$$\operatorname{Var}(N_w) = m\,p(1-p) + 2\sum_{d=1}^{k-1} (m - d)\left(c_d\, 4^{-(k+d)} - p^2\right).$$
- **Delta method.** $\operatorname{Var}(g(X)) \approx g'(\mu)^2 \sigma^2$. **Chebyshev.** $P(\lvert X - \mu \rvert \ge c\sigma) \le 1/c^2$.

## Computational representation

Exact variances from a PMF and from the word-count formula, with fractions:

```python
from fractions import Fraction


def mean_var(pmf: dict):
    """Mean and variance of a PMF given as {value: probability}."""
    m = sum(x * p for x, p in pmf.items())
    return m, sum((x - m) ** 2 * p for x, p in pmf.items())


def word_count_moments(word: str, n: int):
    """Exact mean and variance of the overlapping count of word in n i.i.d. uniform bases."""
    k = len(word)
    m = n - k + 1                                  # number of windows
    p = Fraction(1, 4 ** k)                        # P(a window equals word)
    var = m * p * (1 - p)                          # sum of the indicator variances
    for d in range(1, k):                          # windows d < k apart share bases
        both = Fraction(1, 4 ** (k + d)) if word[d:] == word[:k - d] else 0
        var += 2 * (m - d) * (both - p * p)        # 2 x (number of pairs) x covariance
    return m * p, var


q = Fraction(1, 4)
X = {0: (1 - q) ** 3, 1: 3 * q * (1 - q) ** 2, 2: 3 * q ** 2 * (1 - q), 3: q ** 3}
m, v = mean_var(X)
print("A in a 3-mer: mean", m, "variance", v, "SD", float(v) ** 0.5)
for word in ("ACGT", "AAAA", "ATAT"):
    m, v = word_count_moments(word, 10_000)
    print(f"{word}: mean {float(m):.2f}, variance {float(v):.2f}, SD {float(v) ** 0.5:.2f}")
```

```text
A in a 3-mer: mean 3/4 variance 9/16 SD 0.75
ACGT: mean 39.05, variance 37.98, SD 6.16
AAAA: mean 39.05, variance 63.61, SD 7.98
ATAT: mean 39.05, variance 42.86, SD 6.55
```

The mean-variance relationship by simulation: technical replicates are Poisson draws, biological replicates are Poisson draws around a gamma-distributed true level. These are the dots of the figure above.

```python
import math
import random


def poisson_sample(lam: float, rng: random.Random) -> int:
    """Inversion sampling, as in Poisson Distribution (fine for lam up to a few hundred)."""
    u, k = rng.random(), 0
    p = cdf = math.exp(-lam)
    while u > cdf:
        k += 1
        p *= lam / k
        cdf += p
    return k


def mean_and_var(xs):
    m = sum(xs) / len(xs)
    return m, sum((x - m) ** 2 for x in xs) / (len(xs) - 1)


rng = random.Random(10)
alpha, reps = 0.1, 20_000            # dispersion (illustrative value), replicates per mean
for mu in (5, 20, 100):
    technical = [poisson_sample(mu, rng) for _ in range(reps)]
    # biological: each replicate has its own true level, gamma with mean mu and variance alpha * mu^2
    biological = [poisson_sample(rng.gammavariate(1 / alpha, alpha * mu), rng) for _ in range(reps)]
    (m1, v1), (m2, v2) = mean_and_var(technical), mean_and_var(biological)
    print(f"mu {mu:3d} | Poisson: mean {m1:5.1f}, var {v1:6.1f} | "
          f"gamma-Poisson: mean {m2:5.1f}, var {v2:6.1f} (model {mu + alpha * mu ** 2:.1f})")
```

```text
mu   5 | Poisson: mean   5.0, var    5.0 | gamma-Poisson: mean   5.0, var    7.6 (model 7.5)
mu  20 | Poisson: mean  20.0, var   20.1 | gamma-Poisson: mean  20.1, var   59.3 (model 60.0)
mu 100 | Poisson: mean 100.0, var  101.5 | gamma-Poisson: mean  99.7, var 1104.2 (model 1100.0)
```

The sample variance divides by $n - 1$ (Advanced (L3)); `statistics.variance` does the same, `statistics.pvariance` divides by $n$. Summing squared deviations around the mean, as here, is numerically safer than computing $E[X^2] - \mu^2$ in floating point, which subtracts two large, nearly equal numbers when $\sigma \ll \mu$.

## Worked example

> [!example] More sequencing depth or more replicates?
> A gene receives on average $\mu$ reads per sample. Biological samples differ with dispersion $\alpha = 0.1$ (illustrative), so one sample has variance $\mu + \alpha\mu^2$. The expression of a condition is estimated by the mean of $r$ independent replicates.
> 1. **Variance of the mean.** Variances of independent replicates add, then the factor $1/r$ is squared: $\operatorname{Var}(\bar X) = (\mu + \alpha\mu^2)/r$.
> 2. **Relative standard error.** $\mathrm{SE}/\mu = \sqrt{(1/\mu + \alpha)/r}$.
> 3. **Numbers.** $\mu = 100$, $r = 3$: $\sqrt{0.11/3} = 0.19$. Doubling the depth ($\mu = 200$, $r = 3$): $0.187$. Doubling the replicates ($\mu = 100$, $r = 6$): $0.135$.
> 4. **Fixed budget.** If the gene's total expected reads $T = \mu r$ is fixed, $(1/\mu + \alpha)/r = 1/T + \alpha/r$: the Poisson part depends only on the total number of reads, the biological part only on the number of replicates.
> 5. **Conclusion.** Once $\mu$ is well above $1/\alpha = 10$, the biological term dominates, and more [[Biological Replicate|biological replicates]], not more depth, reduce the uncertainty ([[Experimental Design]]).

## Common misconceptions

> [!warning] "Standard deviations add"
> Variances of independent variables add; standard deviations do not. Independent errors with SD 3 and 4 combine into SD $\sqrt{9 + 16} = 5$, not 7.

> [!warning] "Subtracting a control removes noise"
> $\operatorname{Var}(X - Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$ for independent measurements: a background-subtracted signal or a difference between two samples is noisier than either measurement.

> [!warning] "The gene with the larger variance is the more variable one"
> For counts the variance grows with the mean, so comparing raw variances between genes of different expression is meaningless. Compare CVs, or variances on a stabilized scale.

## Exercises

> [!question] Exercise 1 (L1)
> A count $X$ has $p(0) = 0.3$, $p(1) = 0.4$, $p(2) = 0.2$, $p(3) = 0.1$. Compute $E[X]$, $\operatorname{Var}(X)$ and the standard deviation.

> [!success]- Solution
> $E[X] = 0.4 + 0.4 + 0.3 = 1.1$. $E[X^2] = 0.4 + 0.8 + 0.9 = 2.1$. $\operatorname{Var}(X) = 2.1 - 1.1^2 = 0.89$, $\sigma = 0.943$. Check with deviations: $0.3(1.21) + 0.4(0.01) + 0.2(0.81) + 0.1(3.61) = 0.89$.

> [!question] Exercise 2 (L1)
> A library is sequenced on two lanes; a gene's counts on the lanes are independent Poisson counts of mean 50. Give the mean and SD of the gene's total count and of the difference between lanes. Then: replicates have SD 20; what is the SD of the mean of 4 replicates?

> [!success]- Solution
> Total: mean 100, variance $50 + 50 = 100$, SD 10. Difference: mean 0, variance also 100, SD 10: differences add noise. Mean of 4 replicates: $20/\sqrt 4 = 10$.

> [!question] Exercise 3 (L2, Python)
> Continuing the first code block, compare the exact mean and variance of the counts of ACGT and ATAT in random 1 kb sequences with a simulation of 20,000 sequences (seed 4).

> [!success]- Solution
> ```python
> import random
>
>
> def count_overlapping(seq: str, word: str) -> int:
>     count, i = 0, seq.find(word)
>     while i != -1:
>         count += 1
>         i = seq.find(word, i + 1)
>     return count
>
>
> rng = random.Random(4)
> n, reps = 1_000, 20_000
> seqs = ["".join(rng.choices("ACGT", k=n)) for _ in range(reps)]
> for word in ("ACGT", "ATAT"):
>     exact_mean, exact_var = word_count_moments(word, n)      # from the code above
>     counts = [count_overlapping(s, word) for s in seqs]
>     m = sum(counts) / reps
>     v = sum((c - m) ** 2 for c in counts) / (reps - 1)
>     print(word, round(float(exact_mean), 3), round(float(exact_var), 3), round(m, 3), round(v, 3))
> # ACGT 3.895 3.788 3.899 3.8
> # ATAT 3.895 4.274 3.9 4.248
> ```
>
> Same exact mean (3.895), different variances: 3.79 for ACGT (below the mean, occurrences repel) and 4.27 for ATAT (overlaps at shift 2 add positive covariance). The simulation agrees within sampling error.

> [!question] Exercise 4 (L3)
> (a) Derive $\operatorname{Var}(X) = \mu + \alpha\mu^2$ for the gamma-Poisson. (b) For $\alpha = 0.1$, above which mean does the biological term exceed the Poisson term? (c) An invented gene has counts 80, 130 and 95 in three biological replicates. Estimate its mean, variance and dispersion by the method of moments, $\hat\alpha = (s^2 - \bar x)/\bar x^2$, and comment.

> [!success]- Solution
> (a) Law of total variance: $E[\operatorname{Var}(X \mid \Lambda)] = E[\Lambda] = \mu$ and $\operatorname{Var}(E[X \mid \Lambda]) = \operatorname{Var}(\Lambda) = \alpha\mu^2$. (b) $\alpha\mu^2 > \mu \iff \mu > 1/\alpha = 10$. (c) $\bar x = 101.7$, $s^2 = 1316.7/2 = 658.3$, $\hat\alpha = (658.3 - 101.7)/101.7^2 = 0.054$. With $n = 3$ the relative SD of $s^2$ is around 100 % even for normal data, so $\hat\alpha$ could easily be 0 or 0.15: a single gene cannot pin down its dispersion, which is why methods pool genes with similar means ([[Empirical Bayes]], [[Method of Moments]]).

## Mastery checklist

- [ ] 1 Recognized: I can define variance and standard deviation and compute them from a PMF.
- [ ] 2 Understood: I can explain why variances (not SDs) add for independent variables, why differences add noise, and why count variance depends on the mean.
- [ ] 3 Practiced: I can derive the variance of a sum with covariances (word counts with self-overlap) and check it by simulation in Python.
- [ ] 4 Applied: on a real RNA-seq count table, I plot gene-wise variance against mean on log-log axes and read off the Poisson and overdispersed regimes; in [[05-sequence-search]], I score k-mer counts with the correct variance.
- [ ] 5 Explained: I can teach the law of total variance (technical versus biological), the delta method behind log and square-root transforms, and why replicates beat depth.

## References

[^blitz4]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 4 "Expectation" (variance, its properties, variance of a sum of independent random variables).
[^1805-5a]: [[MIT 18.05 - Introduction to Probability and Statistics]], Spring 2022, Reading 5a "Variance of Discrete Random Variables".
[^stat110]: [[Harvard Stat 110 - Probability]], expectation, variance and the named distributions.
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of covariance (variance of a sum), inequalities (Chebyshev) and the chi-square distribution of the sample variance of normal data.
[^holmes8]: [[Modern Statistics for Modern Biology (Holmes)]], ch. 8 "High-Throughput Count Data" (Poisson sampling noise, gamma-Poisson model of variation between biological replicates, dispersion estimation across genes).
[^holmes-t]: [[Modern Statistics for Modern Biology (Holmes)]], treatment of data transformations (log and variance-stabilizing) for high-throughput data.
