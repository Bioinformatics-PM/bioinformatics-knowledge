---
aliases:
  - t-Distribution
  - Student Distribution
  - t(ν)
  - Loi de Student
tags:
  - type/concept
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Normal Distribution]]"
  - "[[Sampling Distribution]]"
  - "[[Chi-Square Distribution]]"
related:
  - "[[Student's t-Test]]"
  - "[[Confidence Interval]]"
  - "[[Variance]]"
  - "[[F-Distribution]]"
  - "[[Empirical Bayes]]"
projects: []
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Student 1908 - The Probable Error of a Mean]]"
---

# Student's t-Distribution

> [!abstract]
> When the standard deviation is estimated from the same few measurements as the mean, the standardized mean is more variable than a normal score; the t distribution describes it, and its heavier tails make intervals and tests honest about small samples.

## Definition

If $Z \sim \mathcal N(0, 1)$ and $V \sim \chi^2_\nu$ are independent, then $T = \dfrac{Z}{\sqrt{V/\nu}}$ follows **Student's t distribution with $\nu$ degrees of freedom**, written $T \sim t_\nu$. For a sample of $n$ independent normal observations with mean $\mu$, the studentized mean $\dfrac{\bar X - \mu}{S/\sqrt n}$ follows $t_{n-1}$, whatever the unknown $\sigma$.[^os8][^blitz] It was derived in 1908 by W. S. Gosset, publishing as "Student".[^student]

## Why it matters

- **Experiments have few replicates.** Three biological replicates per condition are common in expression studies; with $\nu = 2$, the 97.5 % quantile is 4.30, not 1.96, so honest 95 % intervals are 2.2 times wider than the normal recipe suggests ([[Confidence Interval]]).[^1805]
- **It is the reference distribution of the t-test**, the default test for comparing means of continuous measurements: qPCR values, log-expression, growth rates ([[Student's t-Test]]).[^os8]
- **Small-sample variances are unreliable**, which is exactly what the heavy tails encode; methods that estimate gene-wise variances by sharing information across thousands of genes exist for this reason ([[Empirical Bayes]], [[Variance#Estimating a variance from a few replicates]]).[^holmes8]

## Core (L1)

### Why not the normal?

With $\sigma$ known, $Z = (\bar X - \mu)/(\sigma/\sqrt n)$ is standard normal ([[Sampling Distribution]]). In practice $\sigma$ is replaced by the sample SD $S$, which is itself random: when $S$ happens to be small, the ratio is large. The extra variability makes the distribution of $T = (\bar X - \mu)/(S/\sqrt n)$ wider in the tails than $\mathcal N(0, 1)$.[^os8]

![[t-distribution-heavy-tails.svg]]

### Shape and degrees of freedom

- Symmetric around 0, bell-shaped, with heavier tails than the normal.[^os8]
- One parameter, the **degrees of freedom** $\nu$: the number of independent pieces of information in the variance estimate. One sample of size $n$ gives $\nu = n - 1$, because one is used up by estimating the mean.[^os8]
- As $\nu$ grows, $S$ becomes precise and $t_\nu$ approaches $\mathcal N(0, 1)$.[^os8][^blitz]

| $\nu$ | 1 | 2 | 3 | 4 | 5 | 9 | 29 | $\infty$ (normal) |
|---|---|---|---|---|---|---|---|---|
| $t_{\nu,\,0.975}$ | 12.706 | 4.303 | 3.182 | 2.776 | 2.571 | 2.262 | 2.045 | 1.960 |
| $P(\lvert T\rvert > 1.96)$ | 0.300 | 0.189 | 0.145 | 0.122 | 0.107 | 0.082 | 0.060 | 0.050 |

The second row is the error rate of a "95 %" rule that wrongly uses 1.96 with an estimated SD: 19 % with three replicates (values computed by the code below).

### Bio: three replicates per condition

Log2 expression of a gene in three replicates: 7.9, 8.6, 8.2 (invented). $\bar x = 8.233$, $s = 0.351$, $\mathrm{SE} = 0.203$. The 95 % interval for the mean is $8.233 \pm 4.303 \times 0.203 = [7.36, 9.11]$. The normal recipe would give $\pm 0.40$ instead of $\pm 0.87$, an interval that misses the truth about one time in five.

## Deeper (L2)

- **Moments.** $E[T] = 0$ for $\nu > 1$ and $\mathrm{Var}(T) = \frac{\nu}{\nu - 2}$ for $\nu > 2$ (derived below): 3 for $\nu = 3$, 1.25 for $\nu = 10$. For $\nu \le 2$ the variance is infinite, and for $\nu = 1$, the Cauchy distribution, even the mean does not exist.
- **Polynomial tails.** The density decreases like $|t|^{-(\nu+1)}$, not like $e^{-t^2/2}$: extreme values are rare but not astronomically rare, so a few large $|t|$ among thousands of genes are expected even with no effect.
- **The normality assumption.** The exact $t_{n-1}$ result needs normal observations. For larger $n$ the central limit theorem rescues the mean, but skewed data distort the two tails unequally, and slowly: for exponential data the lower 2.5 % tail of the studentized mean is still 6.6 % at $n = 30$ (Exercise 3). Work on a scale where data are roughly symmetric, such as log-expression ([[Normal Distribution#Log scale and the log-normal]]).
- **Other degrees of freedom.** Two groups sharing a pooled variance give $\nu = n_1 + n_2 - 2$; Welch's test uses an estimated, non-integer $\nu$ ([[Student's t-Test]]).[^os10]

## Advanced (L3)

- **A normal with a random variance.** Conditional on $V$, $T = Z\sqrt{\nu/V}$ is normal with variance $\nu/V$. Averaging normals over a random variance produces heavier tails: the t distribution is a scale mixture of normals. The same construction makes it a robust error model, where occasional outliers are expected instead of treated as impossible.
- **Relation to F.** $T^2 = \frac{Z^2/1}{V/\nu}$ is a ratio of independent chi-square variables divided by their degrees of freedom, the definition of $F(1, \nu)$ ([[F-Distribution]], [[Chi-Square Distribution]]). Hence $t_{\nu,\,0.975}^2 = F_{1,\nu,\,0.95}$: $4.303^2 = 18.51$. A two-sided t-test and a one-way ANOVA F-test on two groups are the same test ([[Analysis of Variance]]).
- **Borrowing strength.** With 20,000 genes and three replicates each, the gene-wise $s$ values are so noisy that the genes with the largest $|t|$ are often those with accidentally tiny variance. Shrinking each gene's variance toward a value estimated from all genes stabilizes the denominator ([[Empirical Bayes]], [[Differential Expression Analysis]]).[^holmes8]

## Mathematical representation

- **Density**: for $t \in \mathbb R$,
$$f_\nu(t) = \frac{\Gamma\!\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\,\Gamma\!\left(\frac{\nu}{2}\right)}\left(1 + \frac{t^2}{\nu}\right)^{-\frac{\nu+1}{2}},$$
where $\Gamma$ is the gamma function. For $\nu = 1$: $f_1(t) = \frac{1}{\pi(1 + t^2)}$, the Cauchy density.[^blitz]
- **Studentized mean**: for i.i.d. $\mathcal N(\mu, \sigma^2)$ data, $Z = \frac{\bar X - \mu}{\sigma/\sqrt n} \sim \mathcal N(0, 1)$, $V = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$, independent of $Z$, so $\frac{Z}{\sqrt{V/(n-1)}} = \frac{\bar X - \mu}{S/\sqrt n} \sim t_{n-1}$: $\sigma$ cancels.[^blitz]
- **Variance**: $\mathrm{Var}(T) = E[Z^2]\,E[\nu/V] = \nu\,E[1/V]$, and $E[1/V] = \frac{1}{\nu - 2}$ for $V \sim \chi^2_\nu$, $\nu > 2$, so $\mathrm{Var}(T) = \frac{\nu}{\nu-2}$.
- **Normal limit**: $\left(1 + \frac{t^2}{\nu}\right)^{-\frac{\nu+1}{2}} \to e^{-t^2/2}$ as $\nu \to \infty$, since $\nu \ln(1 + t^2/\nu) \to t^2$. Notation: $t_{\nu,\,q}$ is the quantile with $P(T \le t_{\nu,\,q}) = q$.

## Computational representation

The standard library has no t distribution, but the density uses only `math.lgamma`, the CDF is one integral (Simpson's rule), and quantiles follow by bisection. SciPy's `scipy.stats.t` gives the same table to three decimals.

```python
import math


def t_pdf(x, df):
    c = math.exp(math.lgamma((df + 1) / 2) - math.lgamma(df / 2)) / math.sqrt(df * math.pi)
    return c * (1 + x * x / df) ** (-(df + 1) / 2)


def t_cdf(x, df, steps=2000):
    """P(T <= x) = 1/2 + integral of the density from 0 to x (Simpson's rule, even steps)."""
    h = x / steps
    inner = sum((4 if i % 2 else 2) * t_pdf(i * h, df) for i in range(1, steps))
    return 0.5 + (t_pdf(0, df) + inner + t_pdf(x, df)) * h / 3


def t_quantile(q, df):
    """Solve t_cdf(x) = q for q > 0.5 by bisection."""
    lo, hi = 0.0, 100.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if t_cdf(mid, df) < q else (lo, mid)
    return (lo + hi) / 2


print("df  t_0.975  P(|T| > 1.96)")
for df in (1, 2, 3, 4, 5, 9, 29):
    print(f"{df:2d}  {t_quantile(0.975, df):7.3f}  {2 * (1 - t_cdf(1.96, df)):.3f}")
```

```text
df  t_0.975  P(|T| > 1.96)
 1   12.706  0.300
 2    4.303  0.189
 3    3.182  0.145
 4    2.776  0.122
 5    2.571  0.107
 9    2.262  0.082
29    2.045  0.060
```

A seeded simulation (seed 8) of 50,000 studentized means of 3 normal replicates with $\mu = 5$ and $\sigma = 2$ gives $P(|T| > 1.96) = 0.191$ and $P(|T| > 4.303) = 0.052$, matching the $t_2$ values: $\sigma$ cancels. `t_cdf` also accepts non-integer `df`, as needed for Welch's test.

## Worked example

> [!example] How much does a fourth replicate buy?
> A pilot with 3 replicates gives $s = 0.35$ on the log2 scale (invented). Compare the half-width $t_{n-1,\,0.975}\,s/\sqrt n$ of the 95 % interval for $n = 3, 4, 6$, keeping $s$ fixed.
> 1. $n = 3$: $4.303 \times 0.35/\sqrt3 = 0.870$.
> 2. $n = 4$: $3.182 \times 0.35/2 = 0.557$.
> 3. $n = 6$: $2.571 \times 0.35/\sqrt6 = 0.367$.
> 4. **Reading**: going from 3 to 4 replicates shrinks the interval by 36 %, much more than the $\sqrt{3/4}$ factor (13 %) of the standard error alone, because the critical value drops from 4.30 to 3.18. At very small $n$, each replicate buys precision twice: through $\sqrt n$ and through the degrees of freedom.

## Common misconceptions

> [!warning] "Use t for small samples and z for $n > 30$"
> With an estimated SD and normal data, $t_{n-1}$ is exact at every $n$; for large $n$ it is simply close to the normal (2.045 against 1.96 at $\nu = 29$). There is no switch point, and software always uses t.

> [!warning] "The t distribution fixes non-normal data"
> Its heavier tails account for estimating $\sigma$, not for skewness or outliers. The exact result assumes normal observations; skewed data give unequal tail errors even at $n = 30$ (Exercise 3).

## Exercises

> [!question] Exercise 1 (L1)
> Four replicates give a mean log2 fold change of 2.1 with $s = 0.4$. Give the 95 % confidence interval, and the interval a careless analyst would get with 1.96.

> [!success]- Solution
> $\mathrm{SE} = 0.4/2 = 0.2$, $\nu = 3$, $t_{3,\,0.975} = 3.182$: $2.1 \pm 0.636 = [1.46, 2.74]$. With 1.96: $2.1 \pm 0.392 = [1.71, 2.49]$, about 40 % narrower than it should be.

> [!question] Exercise 2 (L2)
> Using the definitions, show that $T^2 \sim F(1, \nu)$ when $T \sim t_\nu$. Check numerically that $t_{2,\,0.975}^2$ equals the 95 % quantile of $F(1, 2)$, which is 18.51.

> [!success]- Solution
> $T^2 = Z^2/(V/\nu)$, with $Z^2 \sim \chi^2_1$ independent of $V \sim \chi^2_\nu$: a ratio of independent chi-squares each divided by its degrees of freedom, which defines $F(1, \nu)$. Since $P(T^2 \le c^2) = P(|T| \le c)$, the 95 % quantile of $T^2$ is the square of the 97.5 % quantile of $T$: $4.303^2 = 18.52 \approx 18.51$ (the difference is rounding of 4.303).

> [!question] Exercise 3 (L3, Python)
> Simulate (seed 9, 50,000 runs) the studentized mean of exponential data with mean 1 for $n = 3, 10, 30$, and estimate each tail probability beyond $\pm t_{n-1,\,0.975}$. Compare with the nominal 0.025 per tail.

> [!success]- Solution
> ```python
> import math
> import random
> import statistics as st
>
> rng = random.Random(9)
> for n, crit in ((3, 4.303), (10, 2.262), (30, 2.045)):
>     lower = upper = 0
>     for _ in range(50_000):
>         xs = [rng.expovariate(1.0) for _ in range(n)]        # skewed data, true mean 1
>         t = (st.fmean(xs) - 1.0) / (st.stdev(xs) / math.sqrt(n))
>         lower += t < -crit
>         upper += t > crit
>     print(f"n = {n:2d}: P(T < -t) = {lower / 50_000:.3f}, P(T > t) = {upper / 50_000:.3f} (nominal 0.025 each)")
> ```
> Output: `n =  3: P(T < -t) = 0.109, P(T > t) = 0.007`, `n = 10: P(T < -t) = 0.098, P(T > t) = 0.004`, `n = 30: P(T < -t) = 0.066, P(T > t) = 0.008`. With right-skewed data, a sample whose mean is low also tends to have a small SD, so large negative $t$ values are too frequent and large positive ones too rare. A log transformation, a rank test or the bootstrap is safer than trusting $t$ ([[Nonparametric Statistics]], [[Bootstrap]]).

## Mastery checklist

- [ ] 1 Recognized: I know when the t distribution replaces the normal and what its degrees of freedom are.
- [ ] 2 Understood: I can explain why estimating $\sigma$ thickens the tails and why $t_\nu \to \mathcal N(0, 1)$.
- [ ] 3 Practiced: I can compute t densities, CDFs and quantiles in Python and build t-intervals from replicates.
- [ ] 4 Applied: I reported intervals from real experiments with three or four replicates using the correct quantiles.
- [ ] 5 Explained: I can derive the studentized mean's distribution, its variance, its link to F, and explain its failure for skewed data and the idea of borrowing variance information across genes.

## References

[^os8]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 8 "Confidence Intervals" (a single population mean using the Student t distribution; properties of the t distribution and degrees of freedom).
[^1805]: [[MIT 18.05 - Introduction to Probability and Statistics]], Spring 2022, Reading 22 "Confidence Intervals Based on Normal Data".
[^os10]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 10 "Hypothesis Testing with Two Samples".
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the chi-square and Student-t distributions (construction from normals, the studentized mean of normal data, convergence to the normal).
[^holmes8]: [[Modern Statistics for Modern Biology (Holmes)]], ch. 8 "High-Throughput Count Data" (dispersion estimation by sharing information across genes).
[^student]: [[Student 1908 - The Probable Error of a Mean]], *Biometrika* 6(1):1-25.
