---
aliases:
  - Chi-Squared Distribution
  - χ² Distribution
  - χ²(k)
  - Loi du khi-deux
  - Loi du chi carré
tags:
  - type/concept
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Normal Distribution]]"
  - "[[Variance]]"
  - "[[Probability Density Function]]"
related:
  - "[[Chi-Square Test]]"
  - "[[Student's t-Distribution]]"
  - "[[F-Distribution]]"
  - "[[Likelihood Ratio Test]]"
  - "[[Gamma Distribution]]"
  - "[[Exponential Distribution]]"
projects: []
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[MIT 18.650 - Statistics for Applications]]"
  - "[[Student 1908 - The Probable Error of a Mean]]"
---

# Chi-Square Distribution

> [!abstract]
> Square a few independent standard normal numbers and add them up: the total follows a chi-square distribution, the yardstick for sums of squared standardized deviations such as goodness-of-fit and likelihood ratio statistics.

## Definition

If $Z_1, \dots, Z_k$ are independent standard normal variables, then $X = Z_1^2 + \dots + Z_k^2$ follows the **chi-square distribution with $k$ degrees of freedom**, written $X \sim \chi^2_k$. It takes values in $[0, \infty)$, has mean $k$ and variance $2k$, and is skewed to the right, less so as $k$ grows.[^os11][^blitz]

## Why it matters

- **Reference distribution of count tests.** Pearson's statistic $\sum (O - E)^2/E$, used for Mendelian ratios, [[Hardy-Weinberg Equilibrium]] and case-control allele counts, is approximately $\chi^2$ for large counts ([[Chi-Square Test]]).[^os11]
- **Reference distribution of likelihood ratio tests.** Twice the log-likelihood ratio of nested models is approximately $\chi^2$ for large samples, the basis of tests between substitution models, molecular clock tests and many differential expression tests ([[Likelihood Ratio Test]]).[^18650]
- **Variance estimates.** For normal data, $(n - 1)S^2/\sigma^2 \sim \chi^2_{n-1}$: the chi-square describes how noisy a variance from three replicates is ([[Variance#Estimating a variance from a few replicates]]), and it is the denominator ingredient of the t and F distributions ([[Student's t-Distribution]], [[F-Distribution]]).[^blitz]

## Core (L1)

### Construction and degrees of freedom

Each $Z_i^2$ is a squared standardized deviation: about 1 on average, rarely above 4 (since $|Z| > 2$ has probability 0.046). Adding $k$ of them gives a total around $k$. The **degrees of freedom** $k$ count the independent squared standard normals in the sum.[^os11]

![[chi-square-densities-df.svg]]

### Shape and key values

- Never negative; right-skewed; for $k \ge 2$ the density peaks at $k - 2$; as $k$ grows it approaches $\mathcal N(k, 2k)$.[^os11]
- $k = 1$: $X = Z^2$, so $P(X > 3.841) = P(|Z| > 1.96) = 0.05$. A 1-df chi-square test is a two-sided z-test in disguise.
- $k = 2$: $X$ is exponential with mean 2, $P(X > x) = e^{-x/2}$ ([[Exponential Distribution]]).

| $k$ | 1 | 2 | 3 | 4 | 5 | 10 |
|---|---|---|---|---|---|---|
| 95 % quantile | 3.841 | 5.991 | 7.815 | 9.488 | 11.070 | 18.307 |
| 99 % quantile | 6.635 | 9.210 | 11.345 | 13.277 | 15.086 | 23.209 |

These are the critical values of chi-square tests at the 5 % and 1 % levels (computed by the code below).

### Bio: the yardstick of goodness of fit

A goodness-of-fit statistic adds one squared standardized deviation $(O - E)/\sqrt E$ per category. If the model is right, each term is roughly a squared standard normal, and the total is compared with $\chi^2$: a value far above the degrees of freedom, such as 15 with 2 df, signals a misfit. Genotype counts tested against Hardy-Weinberg proportions use 1 df, a 3:1 Mendelian ratio 1 df, a 9:3:3:1 ratio 3 df ([[Chi-Square Test]], [[Mendelian Inheritance]]).

## Deeper (L2)

- **Additivity.** If $X_1 \sim \chi^2_{k_1}$ and $X_2 \sim \chi^2_{k_2}$ are independent, $X_1 + X_2 \sim \chi^2_{k_1 + k_2}$: concatenate the two lists of squared normals.[^blitz] Independent tests can therefore be combined by adding their statistics and degrees of freedom.
- **Constraints remove degrees of freedom.** In a sum of squared deviations from an *estimated* mean, $\sum_{i=1}^n (Z_i - \bar Z)^2 \sim \chi^2_{n-1}$: the deviations must sum to 0, so only $n - 1$ are free. The same logic gives $k - 1$ df for $k$ categories whose counts must add to $n$, and one fewer for each parameter estimated from the data ([[Chi-Square Test]]).[^blitz]
- **Gamma family.** $\chi^2_k$ is the [[Gamma Distribution]] with shape $k/2$ and rate $1/2$, which gives its density and the tail recurrence used in the code.[^blitz]
- **Sample variance.** For normal data, $(n - 1)S^2/\sigma^2 \sim \chi^2_{n-1}$, independent of $\bar X$, the result that makes the t statistic exact; Student derived the sampling distribution of $s^2$ in 1908.[^student][^blitz] The result needs normality: for exponential data with $n = 3$, the 5 % tail of $2S^2/\sigma^2$ beyond 5.991 holds 7.8 % of the values (Exercise 3).

## Advanced (L3)

- **Why Pearson's statistic is chi-square.** Standardized counts $(O_j - E_j)/\sqrt{E_j}$ are approximately normal for large $E_j$ ([[Binomial Distribution]], central limit theorem), but they are linked by $\sum O_j = n$. The sum of their squares is a quadratic form in approximately normal variables with one linear constraint, and its limit is $\chi^2_{k-1}$, not $\chi^2_k$.[^18650] Small expected counts break the normal approximation, which is why exact tests exist ([[Fisher's Exact Test]]).
- **Wilks' theorem.** For nested models, under $H_0$ and regularity conditions, $2\log \Lambda = 2(\ell_1 - \ell_0)$ is approximately $\chi^2$ with as many degrees of freedom as extra free parameters in the larger model ($\ell_0$, $\ell_1$: maximized log-likelihoods).[^18650] Testing a molecular clock, or one codon model against a richer one, reads $2\log\Lambda$ on this scale ([[Likelihood Ratio Test]]).
- **Normal approximation in the tail.** By the central limit theorem, $(X - k)/\sqrt{2k}$ is approximately standard normal for large $k$, but the right skew persists in the tail: for $k = 50$, $P(X > 100)$ is $3.5 \times 10^{-5}$ exactly, against $2.9 \times 10^{-7}$ from the normal approximation ($z = 50/10 = 5$), 120 times too small. Use the exact tail for p-values ([[Normal Distribution#Advanced (L3)]]).

## Mathematical representation

- **Density**: for $x > 0$, $f_k(x) = \dfrac{x^{k/2 - 1}\,e^{-x/2}}{2^{k/2}\,\Gamma(k/2)}$, with $\Gamma$ the gamma function.[^blitz]
- **Moments**: $E[Z^2] = 1$ and $E[Z^4] = 3$ for $Z \sim \mathcal N(0, 1)$, so $\mathrm{Var}(Z^2) = 3 - 1 = 2$; by linearity and independence, $E[X] = k$ and $\mathrm{Var}(X) = 2k$.
- **Upper tail** $Q(x; k) = P(X \ge x) = \Gamma(k/2, x/2)/\Gamma(k/2)$, where $\Gamma(s, y) = \int_y^\infty u^{s-1}e^{-u}\,du$. Integrating by parts, $\Gamma(s + 1, y) = s\,\Gamma(s, y) + y^s e^{-y}$, hence the recurrence
$$Q(x; k + 2) = Q(x; k) + \frac{(x/2)^{k/2}\,e^{-x/2}}{\Gamma(k/2 + 1)},$$
started from $Q(x; 1) = \operatorname{erfc}\!\big(\sqrt{x/2}\big) = 2[1 - \Phi(\sqrt x)]$ and $Q(x; 2) = e^{-x/2}$. The quantile $\chi^2_{k,\,q}$ solves $P(X \le \chi^2_{k,\,q}) = q$.

## Computational representation

The recurrence gives exact tail probabilities for integer $k$ with `math.erfc`, `math.exp` and `math.lgamma` only; quantiles follow by bisection. SciPy's `scipy.stats.chi2` gives the same critical values.

```python
import math


def chi2_sf(x, k):
    """P(X >= x) for X ~ chi-square with integer k degrees of freedom (exact recurrence in k)."""
    if x <= 0:
        return 1.0
    q, j = (math.erfc(math.sqrt(x / 2)), 1) if k % 2 else (math.exp(-x / 2), 2)
    while j < k:                       # Q(x; j + 2) = Q(x; j) + (x/2)^(j/2) e^(-x/2) / Gamma(j/2 + 1)
        q += math.exp((j / 2) * math.log(x / 2) - x / 2 - math.lgamma(j / 2 + 1))
        j += 2
    return q


def chi2_quantile(prob, k):
    """x such that P(X <= x) = prob, by bisection."""
    lo, hi = 0.0, 10.0 * k + 100.0
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if 1 - chi2_sf(mid, k) < prob else (lo, mid)
    return (lo + hi) / 2


print("k   95 %    99 %")
for k in (1, 2, 3, 4, 5, 10):
    print(f"{k:2d} {chi2_quantile(0.95, k):6.3f}  {chi2_quantile(0.99, k):6.3f}")
```

```text
k   95 %    99 %
 1  3.841   6.635
 2  5.991   9.210
 3  7.815  11.345
 4  9.488  13.277
 5 11.070  15.086
10 18.307  23.209
```

A seeded simulation (seed 6) of 50,000 sums of $k$ squared standard normals for $k = 1, 3, 8$ gives means 1.00, 3.01, 8.03, variances 2.01, 6.06, 16.13, and 5.1 %, 5.1 %, 5.2 % of values beyond the 95 % quantiles: the definition and the formulas agree.

## Worked example

> [!example] From a statistic to a p-value
> A Hardy-Weinberg goodness-of-fit test gives $X^2 = 4.2$ with 1 degree of freedom; a test of a 3-genotype model with no estimated parameter would give the same value with 2 df.
> 1. **1 df**: $4.2 > 3.841$, reject at 5 %. Exactly: $P(\chi^2_1 \ge 4.2) = 2[1 - \Phi(\sqrt{4.2})] = 2[1 - \Phi(2.049)] = 0.040$.
> 2. **2 df**: $4.2 < 5.991$, do not reject. Exactly: $P(\chi^2_2 \ge 4.2) = e^{-2.1} = 0.122$.
> 3. **Reading**: the same statistic is surprising for 1 df but not for 2 df, because a sum of two squared normals is naturally larger. Getting the degrees of freedom right is part of the test ([[Chi-Square Test]]).

## Common misconceptions

> [!warning] "The degrees of freedom are the number of categories"
> They are the number of independent squared deviations: categories minus constraints minus estimated parameters. Hardy-Weinberg with 3 genotype classes and one estimated allele frequency has $3 - 1 - 1 = 1$ df.

> [!warning] "A large chi-square value is always significant"
> Values are judged against $k$: 15 is extreme for 2 df ($p = 5.5 \times 10^{-4}$) and ordinary for 15 df (the mean).

## Exercises

> [!question] Exercise 1 (L1)
> Using the table, decide at 5 % and give the approximate p-value range for: (a) $X^2 = 6.1$ with 2 df; (b) $X^2 = 6.1$ with 4 df; (c) $X^2 = 12$ with 3 df.

> [!success]- Solution
> (a) $5.991 < 6.1 < 9.210$: reject at 5 %, $0.01 < p < 0.05$ (exactly $e^{-3.05} = 0.047$). (b) $6.1 < 9.488$: do not reject, $p > 0.05$. (c) $12 > 11.345$: reject even at 1 %, $p < 0.01$.

> [!question] Exercise 2 (L2)
> Derive $E[X] = k$ and $\mathrm{Var}(X) = 2k$ from $E[Z^2] = 1$ and $E[Z^4] = 3$. Then use the normal approximation $\mathcal N(k, 2k)$ to guess the 95 % quantile for $k = 10$ and compare with 18.307.

> [!success]- Solution
> $E[X] = \sum E[Z_i^2] = k$; $\mathrm{Var}(Z_i^2) = E[Z_i^4] - (E[Z_i^2])^2 = 2$, and independence adds variances: $2k$. Approximation: $10 + 1.645\sqrt{20} = 17.36$, below the exact 18.307: the right skew puts more mass in the upper tail than a symmetric normal.

> [!question] Exercise 3 (L3, Python)
> With seed 10, simulate 50,000 values of $(n - 1)S^2/\sigma^2$ for $n = 3$ from standard normal data and from exponential data with variance 1, and estimate the probability of exceeding 5.991, the 95 % quantile of $\chi^2_2$.

> [!success]- Solution
> ```python
> import random
> import statistics as st
>
> rng = random.Random(10)
> for name, draw, var in (("normal", lambda: rng.gauss(0, 1), 1.0), ("exponential", lambda: rng.expovariate(1.0), 1.0)):
>     stats = [2 * st.variance([draw() for _ in range(3)]) / var for _ in range(50_000)]   # (n - 1) S^2 / sigma^2
>     print(f"{name:11s} mean {st.fmean(stats):.2f}  P(> 5.991) = {sum(s > 5.991 for s in stats) / len(stats):.3f}")
> ```
> Output: `normal      mean 2.01  P(> 5.991) = 0.050`, then `exponential mean 2.02  P(> 5.991) = 0.078`. Both means are 2 (the sample variance is unbiased for any distribution), but only normal data give the $\chi^2_2$ tail; skewed data produce large variances too often. Variance tests and intervals based on the chi-square are therefore sensitive to non-normality.

## Mastery checklist

- [ ] 1 Recognized: I can define $\chi^2_k$ as a sum of squared standard normals and read its critical values.
- [ ] 2 Understood: I can explain degrees of freedom as independent squared deviations, and why constraints and estimated parameters remove them.
- [ ] 3 Practiced: I can compute chi-square tail probabilities and quantiles in Python and derive the mean and variance.
- [ ] 4 Applied: I converted real goodness-of-fit or likelihood ratio statistics into p-values with the correct degrees of freedom.
- [ ] 5 Explained: I can explain why Pearson and likelihood ratio statistics are asymptotically chi-square, the role of normality for variance statistics, and the limits of the normal approximation in the tail.

## References

[^os11]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 11 "The Chi-Square Distribution", section 11.1 "Facts About the Chi-Square Distribution" (sum of squared standard normals, degrees of freedom, mean, skewness, approach to the normal).
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the chi-square and Student-t distributions (chi-square as a sum of squared normals and as a gamma distribution, the distribution of the sample variance of normal data).
[^18650]: [[MIT 18.650 - Statistics for Applications]], testing part (goodness of fit and likelihood ratio tests).
[^student]: [[Student 1908 - The Probable Error of a Mean]], *Biometrika* 6(1):1-25.
