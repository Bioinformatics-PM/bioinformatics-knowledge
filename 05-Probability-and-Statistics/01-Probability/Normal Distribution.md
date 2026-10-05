---
aliases:
  - Gaussian Distribution
  - Gaussian
  - Bell Curve
  - Standard Normal Distribution
  - N(μ, σ²)
  - Loi normale
  - Loi de Gauss
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Probability Density Function]]"
  - "[[Cumulative Distribution Function]]"
  - "[[Expected Value]]"
  - "[[Variance]]"
  - "[[Exponential Function]]"
related:
  - "[[Standard Score]]"
  - "[[Central Limit Theorem]]"
  - "[[Measurement Error]]"
  - "[[Q-Q Plot]]"
  - "[[Data Transformation]]"
  - "[[Transformation of Random Variables]]"
  - "[[Student's t-Distribution]]"
  - "[[Confidence Interval]]"
  - "[[P-Value]]"
  - "[[Binomial Distribution]]"
  - "[[Poisson Distribution]]"
  - "[[Uniform Distribution]]"
  - "[[Multivariate Normal Distribution]]"
  - "[[Log Fold Change]]"
projects: []
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Harvard Stat 110 - Probability]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
---

# Normal Distribution

> [!abstract]
> The normal (Gaussian) distribution is the symmetric bell curve fixed by a mean $\mu$ and a standard deviation $\sigma$. Standardizing, $z = (x - \mu)/\sigma$, turns every normal probability into a lookup in one table; the model describes measurement error and, approximately, many biological measurements on a log scale.

## Definition

A random variable $X$ has the **normal distribution** with mean $\mu \in \mathbb{R}$ and variance $\sigma^2 > 0$, written $X \sim \mathcal{N}(\mu, \sigma^2)$, if its density is

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, \exp\!\left(-\frac{(x - \mu)^2}{2\sigma^2}\right), \qquad x \in \mathbb{R}.$$

Then $E[X] = \mu$ and $\operatorname{Var}(X) = \sigma^2$. The **standard normal** $Z \sim \mathcal{N}(0, 1)$ has density $\varphi(z) = e^{-z^2/2}/\sqrt{2\pi}$ and CDF $\Phi(z) = \int_{-\infty}^{z} \varphi(t)\,dt$, which has no closed form and is read from tables or computed numerically.[^blitz5][^openstax6]

## Why it matters

- **Measurement error.** Repeated measurements of one quantity scatter around its value. When the error is a sum of many small independent contributions, the [[Central Limit Theorem]] makes it approximately normal, the main reason the distribution is so widely used.[^blitz5] See [[Measurement Error]].
- **Log-scale measurements.** High-throughput intensities and counts are usually analysed after a log or variance-stabilizing transformation.[^holmes] On that scale the normal model is a natural first approximation for one gene's values across replicates, to be checked with a [[Q-Q Plot]] rather than assumed ([[Data Transformation]], [[Log Fold Change]]).
- **z-scores and tests.** Standardization puts measurements on a common scale ([[Standard Score]]), and tests about means and proportions in large samples take their p-values as normal tail areas ([[P-Value]], [[Hypothesis Testing]]).[^openstax9]
- **Approximations and building blocks.** Binomial and Poisson counts with large means are approximately normal, and the chi-square and Student's t distributions are built from normal variables.[^blitz] See [[Binomial Distribution]], [[Poisson Distribution]], [[Student's t-Distribution]], [[Chi-Square Distribution]].

## Core (L1)

### Shape: center and spread

The density is symmetric about $\mu$, highest at $\mu$, with inflection points at $\mu \pm \sigma$ (derived in [[#Mathematical representation]]): $\mu$ moves the curve, $\sigma$ stretches it. Its tails fall off like $e^{-z^2/2}$, so values beyond a few standard deviations are rare.

![[normal-density-shaded-tail.svg]]

### Standardize: z-scores

If $X \sim \mathcal{N}(\mu, \sigma^2)$, then $Z = (X - \mu)/\sigma \sim \mathcal{N}(0, 1)$, so

$$P(X \le x) = \Phi\!\left(\frac{x - \mu}{\sigma}\right).$$

The **z-score** $z = (x - \mu)/\sigma$ is the number of standard deviations between $x$ and the mean, positive above it and negative below.[^openstax6][^blitz5] It is why a single table of $\Phi$ serves every normal distribution ([[Standard Score]]).

### Reading the table

| $z$ | 0 | 1 | 1.645 | 1.96 | 2 | 2.576 | 3 |
|---|---|---|---|---|---|---|---|
| $\Phi(z)$ | 0.5000 | 0.8413 | 0.9500 | 0.9750 | 0.9772 | 0.9950 | 0.9987 |
| $1 - \Phi(z)$ | 0.5000 | 0.1587 | 0.0500 | 0.0250 | 0.0228 | 0.0050 | 0.0013 |

Tables list $z \ge 0$; symmetry gives the rest (values computed in [[#Computational representation]]):

- $P(Z > z) = 1 - \Phi(z)$ and $\Phi(-z) = 1 - \Phi(z)$;
- $P(a < X < b) = \Phi\big(\frac{b - \mu}{\sigma}\big) - \Phi\big(\frac{a - \mu}{\sigma}\big)$;
- quantiles $x_p = \mu + \sigma z_p$, where $\Phi(z_p) = p$: $z_{0.975} = 1.96$, so $\mu \pm 1.96\,\sigma$ holds 95 % of the distribution ([[Quantile]]).

**The 68-95-99.7 rule.** About 68 % of the values lie within one standard deviation of the mean, 95 % within two and 99.7 % within three.[^openstax6]

### Bio: measurement error and log-expression

Invented model: the log2 expression of a gene across replicate samples is $X \sim \mathcal{N}(8, 0.5^2)$. A replicate exceeds 9 with probability $P\big(Z > (9 - 8)/0.5\big) = 1 - \Phi(2) = 0.0228$, the shaded tail of the figure; 68 % of the replicates fall in $[7.5, 8.5]$ and 95 % in $[7.02, 8.98]$. The same steps apply to any measurement whose error is modelled as normal, such as a concentration read on an instrument (Exercise 1).

## Deeper (L2)

### Linear transformations and sums

If $X \sim \mathcal{N}(\mu, \sigma^2)$ and $a \ne 0$, then $aX + b \sim \mathcal{N}(a\mu + b, a^2\sigma^2)$; standardization is the case $a = 1/\sigma$, $b = -\mu/\sigma$. A sum of independent normal variables is normal, with means and variances adding:[^blitz] $X_1 + X_2 \sim \mathcal{N}(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)$. Two consequences for replicated measurements ([[Variance]]):

- the mean of $n$ independent measurements with errors $\mathcal{N}(0, \sigma^2)$ is normal with standard deviation $\sigma/\sqrt{n}$ (Exercise 2);
- a value combining biological variation $\mathcal{N}(0, \sigma_b^2)$ and independent technical error $\mathcal{N}(0, \sigma_t^2)$ has variance $\sigma_b^2 + \sigma_t^2$: variances add, standard deviations do not (Exercise 3).

### Why measurement errors look normal, and when they do not

An error made of many small, independent contributions (pipetting, temperature, optics, counting) is approximately normal by the [[Central Limit Theorem]], whatever the distribution of each contribution.[^blitz5] The argument fails when one source dominates, when errors multiply instead of adding (their logarithm is then closer to normal, see below), or when outliers occur. Closeness to normality is checked on the data with a [[Q-Q Plot]], not assumed.

### Normal approximation of counts

For counts with a large mean, $\mathrm{Bin}(n, p) \approx \mathcal{N}\big(np, np(1 - p)\big)$ and $\mathrm{Pois}(\lambda) \approx \mathcal{N}(\lambda, \lambda)$ ([[Binomial Distribution]], [[Poisson Distribution]]). Because the count is an integer, $P(X \le k)$ is better approximated by $\Phi\big((k + 0.5 - \mu)/\sigma\big)$, the **continuity correction**.[^blitz] For a depth $X \sim \mathrm{Pois}(30)$, $P(X \le 25) = 0.208$, against 0.181 for the plain normal approximation and 0.206 with the correction (Exercise 4).

### Log scale and the log-normal

If $\log X$ is normal, $X$ is **log-normal**: positive and right-skewed, with median $2^{\mu}$ when $\log_2 X \sim \mathcal{N}(\mu, \sigma^2)$, but a larger mean, $E[X] = 2^{\mu} e^{(\sigma \ln 2)^2/2}$ (derived below). An average computed on the log scale and back-transformed estimates the median of the raw values, not their mean (Exercise 5; [[Probability Density Function#Deeper (L2)]], [[Transformation of Random Variables]]).

## Advanced (L3)

- **Thin tails.** $P(Z > z)$ falls from $1.3 \times 10^{-3}$ at $z = 3$ to $2.9 \times 10^{-7}$ at $z = 5$ and $9.9 \times 10^{-10}$ at $z = 6$; for large $z$, $P(Z > z) \approx \varphi(z)/z$. Small departures from normality in the tails therefore change tail probabilities by orders of magnitude. For $X \sim \mathrm{Pois}(30)$, $P(X \ge 60) = 9.3 \times 10^{-7}$, while the normal approximation gives $3.6 \times 10^{-8}$, 26 times smaller: a z-score p-value for an extreme count, such as a k-mer or a depth far above expectation, overstates the evidence (Exercise 4).
- **Computing tiny tails.** $1 - \Phi(z)$ subtracts two numbers close to 1: in double precision it returns $6.7 \times 10^{-16}$ instead of $6.2 \times 10^{-16}$ at $z = 8$, and 0 at $z = 10$ ([[Floating-Point Arithmetic]]). The complementary error function computes the tail directly, $1 - \Phi(z) = \frac12 \operatorname{erfc}(z/\sqrt2)$; smaller tails are handled in log space ([[Cumulative Distribution Function#Advanced (L3)]], [[Numerical Stability]]).
- **Estimated standard deviations.** A z-score assumes $\sigma$ known. With $\sigma$ estimated from $n$ replicates, $(\bar X - \mu)/(s/\sqrt{n})$ follows Student's t distribution with $n - 1$ degrees of freedom, whose heavier tails widen intervals for small samples ([[Student's t-Distribution]], [[Confidence Interval]]).[^openstax8] With three replicates ($n - 1 = 2$), the 97.5 % quantile is 4.30 instead of 1.96.
- **Several variables.** Jointly normal vectors, such as the expression of several genes or correlated traits, are described by a mean vector and a covariance matrix ([[Multivariate Normal Distribution]]).

## Mathematical representation

- **Density and CDF.** $f(x) = \frac{1}{\sigma}\varphi\big(\frac{x - \mu}{\sigma}\big)$ and $F(x) = \Phi\big(\frac{x - \mu}{\sigma}\big)$, with $\Phi(z) = \frac12\big[1 + \operatorname{erf}(z/\sqrt{2})\big]$ and $\operatorname{erf}(u) = \frac{2}{\sqrt{\pi}}\int_0^u e^{-t^2}\,dt$.
- **Normalization.** $I = \int_{-\infty}^{\infty} e^{-z^2/2}\,dz$ satisfies $I^2 = \iint e^{-(x^2 + y^2)/2}\,dx\,dy = \int_0^{2\pi}\!\!\int_0^{\infty} e^{-r^2/2}\, r\,dr\,d\theta = 2\pi$ in polar coordinates ([[Multiple Integral]]), so $I = \sqrt{2\pi}$.
- **Symmetry.** $\varphi(-z) = \varphi(z)$ gives $\Phi(-z) = 1 - \Phi(z)$ and $E[Z] = 0$.
- **Inflection points.** $\varphi'(z) = -z\varphi(z)$ and $\varphi''(z) = (z^2 - 1)\varphi(z)$, which changes sign at $z = \pm 1$, that is at $x = \mu \pm \sigma$.
- **Variance.** Integrating by parts with $u = z$ and $dv = z\varphi(z)\,dz$ ($v = -\varphi(z)$): $E[Z^2] = \big[-z\varphi(z)\big]_{-\infty}^{\infty} + \int \varphi(z)\,dz = 1$, so $\operatorname{Var}(\mu + \sigma Z) = \sigma^2$.
- **Linear maps.** For $a > 0$: $P(aX + b \le y) = \Phi\big(\frac{(y - b)/a - \mu}{\sigma}\big) = \Phi\big(\frac{y - (a\mu + b)}{a\sigma}\big)$, the CDF of $\mathcal{N}(a\mu + b, a^2\sigma^2)$.
- **Moment generating function.** Completing the square in the exponent gives $E[e^{tX}] = e^{\mu t + \sigma^2 t^2/2}$; with $t = \ln 2$, $E[2^X] = 2^{\mu} e^{(\sigma \ln 2)^2/2}$.
- **Tail bound.** For $z > 0$: $P(Z > z) = \int_z^{\infty} \varphi(t)\,dt \le \int_z^{\infty} \frac{t}{z}\varphi(t)\,dt = \frac{\varphi(z)}{z}$.

## Computational representation

The standard library covers the essentials: `statistics.NormalDist` has `pdf`, `cdf` and `inv_cdf`, `math.erfc` gives tails without cancellation, and `random.gauss` draws normal variates.

```python
import math
import random
from statistics import NormalDist

Z = NormalDist()                                    # standard normal N(0, 1)
for z in (0.0, 1.0, 1.645, 1.96, 2.0, 2.576, 3.0):
    print(f"z = {z:5.3f}: Phi(z) = {Z.cdf(z):.5f}, upper tail = {1 - Z.cdf(z):.5f}")
print("quantiles: z_0.95 =", round(Z.inv_cdf(0.95), 3), " z_0.975 =", round(Z.inv_cdf(0.975), 3))

# log2 expression of a gene across replicate samples, modelled as N(8, 0.5^2) (invented)
X = NormalDist(mu=8, sigma=0.5)
print(f"P(X > 9) = {1 - X.cdf(9):.4f}  (z = {(9 - X.mean) / X.stdev})")
print(f"P(7.5 < X < 8.5) = {X.cdf(8.5) - X.cdf(7.5):.4f}; central 95 %: "
      f"[{X.inv_cdf(0.025):.3f}, {X.inv_cdf(0.975):.3f}]")

# Seeded simulation: standardize, then check the 68-95-99.7 rule and the tail
rng = random.Random(42)
xs = [rng.gauss(8, 0.5) for _ in range(200_000)]
zs = [(x - 8) / 0.5 for x in xs]
for k in (1, 2, 3):
    print(f"within {k} sd: simulated {sum(abs(z) <= k for z in zs) / len(zs):.4f}, "
          f"exact {Z.cdf(k) - Z.cdf(-k):.4f}")
print(f"simulated P(X > 9) = {sum(x > 9 for x in xs) / len(xs):.4f}")

# Far tails: 1 - cdf is lost to rounding; erfc computes the tail directly
for z in (5, 8, 10):
    print(f"z = {z:2d}: 1 - Phi(z) = {1 - Z.cdf(z):.3e}, erfc form = {0.5 * math.erfc(z / math.sqrt(2)):.3e}")
```

```text
z = 0.000: Phi(z) = 0.50000, upper tail = 0.50000
z = 1.000: Phi(z) = 0.84134, upper tail = 0.15866
z = 1.645: Phi(z) = 0.95002, upper tail = 0.04998
z = 1.960: Phi(z) = 0.97500, upper tail = 0.02500
z = 2.000: Phi(z) = 0.97725, upper tail = 0.02275
z = 2.576: Phi(z) = 0.99500, upper tail = 0.00500
z = 3.000: Phi(z) = 0.99865, upper tail = 0.00135
quantiles: z_0.95 = 1.645  z_0.975 = 1.96
P(X > 9) = 0.0228  (z = 2.0)
P(7.5 < X < 8.5) = 0.6827; central 95 %: [7.020, 8.980]
within 1 sd: simulated 0.6814, exact 0.6827
within 2 sd: simulated 0.9543, exact 0.9545
within 3 sd: simulated 0.9972, exact 0.9973
simulated P(X > 9) = 0.0231
z =  5: 1 - Phi(z) = 2.867e-07, erfc form = 2.867e-07
z =  8: 1 - Phi(z) = 6.661e-16, erfc form = 6.221e-16
z = 10: 1 - Phi(z) = 0.000e+00, erfc form = 7.620e-24
```

The 200,000 simulated values reproduce the 68-95-99.7 rule and the shaded tail within sampling error. The last lines show the tail lost by `1 - cdf` beyond $z \approx 8$.

## Worked example

> [!example] Is this run of the reference sample unusual?
> A laboratory sequences a reference RNA sample in every run. For a control gene, its log2 expression across past runs is modelled as $\mathcal{N}(8, 0.5^2)$ (invented). Run 12 gives 9.2.
>
> 1. **Standardize.** $z = (9.2 - 8)/0.5 = 2.4$.
> 2. **Tail probability.** $P(X \ge 9.2) = 1 - \Phi(2.4) = 0.0082$; a deviation at least this large in either direction has probability $2 \times 0.0082 = 0.016$.
> 3. **Control limits.** Limits at $\mu \pm 3\sigma = [6.5, 9.5]$ flag a run with probability $1 - 0.9973 = 0.0027$ when nothing is wrong, about one false alarm in 370 runs. Run 12 lies inside them, but $|z| \ge 2.4$ happens in only 1.6 % of normal runs: worth watching.
> 4. **Check the model.** These numbers are only as good as the normal model of past runs: a [[Q-Q Plot]] of their values should be close to a straight line, especially in the tails, before a probability like 0.0027 is trusted.

## Common misconceptions

> [!warning] "Biological measurements are normally distributed"
> The normal distribution is a model. Counts, intensities and concentrations are often skewed on the raw scale, and even after a log transformation their tails must be checked. The [[Central Limit Theorem]] concerns sums and averages, not each measurement.

> [!warning] "Standard deviations add"
> Variances of independent errors add: a biological SD of 0.4 and a technical SD of 0.3 give a total SD of 0.5, not 0.7 (Exercise 3).

> [!warning] "A z-score always gives the right p-value"
> Only if the statistic is close to normal in the relevant tail. For a count of 60 where 30 are expected under a Poisson model, the z-score 5.5 suggests $p \approx 2 \times 10^{-8}$; the exact tail is $9 \times 10^{-7}$ (Exercise 4).

> [!warning] "Back-transforming the mean of log values gives the mean"
> $2^{\text{mean of } \log_2 x}$, the geometric mean, estimates the median of the raw values, which is smaller than their mean whenever the values vary (Exercise 5).

## Exercises

> [!question] Exercise 1 (L1)
> Readings of a DNA concentration have errors modelled as $\mathcal{N}(0, 2^2)$ ng/µL around the true value 50 ng/µL (invented). Compute $P(X < 47)$, $P(46 < X < 54)$ and the reading exceeded only 2.5 % of the time. ($\Phi(1.5) = 0.9332$.)

> [!success]- Solution
> $P(X < 47) = \Phi(-1.5) = 1 - 0.9332 = 0.067$. $P(46 < X < 54) = \Phi(2) - \Phi(-2) = 2 \times 0.9772 - 1 = 0.954$. The 97.5 % quantile is $50 + 1.96 \times 2 = 53.9$ ng/µL.

> [!question] Exercise 2 (L2)
> With measurement errors $\mathcal{N}(0, 2^2)$, how many independent readings must be averaged for the mean to lie within ±0.5 ng/µL of the true value with probability 0.95?

> [!success]- Solution
> The mean of $n$ readings is $\mathcal{N}(50, 4/n)$. Require $1.96 \times 2/\sqrt{n} \le 0.5$: $\sqrt{n} \ge 7.84$, $n \ge 61.5$, so 62 readings. Precision grows like $\sqrt{n}$: halving the error band costs four times as many replicates.

> [!question] Exercise 3 (L2)
> In an invented model, the log2 expression of a gene in a sample is $\mu + B + T$, with biological variation $B \sim \mathcal{N}(0, 0.4^2)$ and technical error $T \sim \mathcal{N}(0, 0.3^2)$, independent. Give the standard deviation of a measurement, the probability that it differs from $\mu$ by more than 1 log2 unit, and the probability that two independent biological replicates differ by more than 1.

> [!success]- Solution
> Variances add: $0.16 + 0.09 = 0.25$, SD 0.5. $P(|X - \mu| > 1) = P(|Z| > 2) = 0.046$. The difference of two independent replicates has variance $2 \times 0.25 = 0.5$, SD 0.707, so $P(|D| > 1) = P(|Z| > 1.414) = 0.157$. A twofold difference between replicates occurs in about one comparison in six without any biological effect: a fold change means little without its variance ([[Log Fold Change]]).

> [!question] Exercise 4 (L3, Python)
> A depth (or a k-mer count) is modelled as $\mathrm{Pois}(30)$. Compare the exact CDF with the normal approximation, with and without continuity correction, for $k = 20$ to 40; then compare the upper tails $P(X \ge 45)$ and $P(X \ge 60)$. Where does the approximation work, and where does it fail?

> [!success]- Solution
> ```python
> import math
> from statistics import NormalDist
>
> def pois_pmf(i: int, lam: float) -> float:
>     return math.exp(-lam + i * math.log(lam) - math.lgamma(i + 1))
>
> def pois_cdf(k: int, lam: float) -> float:
>     return sum(pois_pmf(i, lam) for i in range(k + 1))
>
> def pois_upper(k: int, lam: float) -> float:
>     """P(X >= k), summed directly over the tail (no 1 - cdf cancellation)."""
>     return sum(pois_pmf(i, lam) for i in range(k, k + 400))
>
> lam = 30                                     # e.g. expected read depth, or expected k-mer count
> approx = NormalDist(lam, math.sqrt(lam))
> print(" k   P(X <= k)  normal   normal, k + 0.5")
> for k in (20, 25, 30, 35, 40):
>     print(f"{k:2d}   {pois_cdf(k, lam):.4f}     {approx.cdf(k):.4f}   {approx.cdf(k + 0.5):.4f}")
> for k in (45, 60):
>     print(f"P(X >= {k}): exact {pois_upper(k, lam):.2e}, normal {1 - approx.cdf(k - 0.5):.2e}")
> ```
>
> ```text
>  k   P(X <= k)  normal   normal, k + 0.5
> 20   0.0353     0.0339   0.0414
> 25   0.2084     0.1807   0.2057
> 30   0.5484     0.5000   0.5364
> 35   0.8426     0.8193   0.8423
> 40   0.9677     0.9661   0.9724
> P(X >= 45): exact 6.27e-03, normal 4.06e-03
> P(X >= 60): exact 9.25e-07, normal 3.60e-08
> ```
>
> Near the mean, the continuity-corrected approximation is within about 0.01 of the exact CDF. In the upper tail it ignores the right skew of the Poisson: 35 % too small at 45 and 26 times too small at 60. Significance of extreme counts must come from exact or log-space tails ([[Cumulative Distribution Function]]), not from z-scores.

> [!question] Exercise 5 (L3, Python)
> Simulate log2 expression values $Y \sim \mathcal{N}(8, \sigma^2)$ for $\sigma = 0.5$ and $1.5$ (seed 8), transform them to the raw scale $X = 2^Y$, and compare means and medians on both scales with $2^8$ and $E[X] = 2^{8} e^{(\sigma \ln 2)^2/2}$.

> [!success]- Solution
> ```python
> import math
> import random
> from statistics import median
>
> rng = random.Random(8)
> for sigma in (0.5, 1.5):                  # log2 expression ~ N(8, sigma^2), invented
>     logx = [rng.gauss(8, sigma) for _ in range(100_000)]
>     raw = [2 ** x for x in logx]
>     exact_mean = 2 ** 8 * math.exp((sigma * math.log(2)) ** 2 / 2)
>     print(f"sigma = {sigma}: log scale mean {sum(logx) / len(logx):.3f}, median {median(logx):.3f}; "
>           f"raw scale mean {sum(raw) / len(raw):.1f} (exact {exact_mean:.1f}), median {median(raw):.1f}")
> ```
>
> ```text
> sigma = 0.5: log scale mean 8.003, median 8.004; raw scale mean 272.4 (exact 271.8), median 256.7
> sigma = 1.5: log scale mean 8.003, median 8.006; raw scale mean 438.1 (exact 439.5), median 257.1
> ```
>
> On the log scale mean and median coincide. On the raw scale the median stays at $2^8 = 256$, because quantiles survive increasing transformations, while the mean exceeds it by 6 % for $\sigma = 0.5$ and by 72 % for $\sigma = 1.5$. State which one a "mean expression" refers to.

## Mastery checklist

- [ ] 1 Recognized: I can write the normal density, name $\mu$ and $\sigma$, and quote the 68-95-99.7 rule.
- [ ] 2 Understood: I can standardize, read $\Phi$ from a table using symmetry, and explain why variances, not standard deviations, add.
- [ ] 3 Practiced: I can compute normal probabilities and quantiles by hand and with `statistics.NormalDist`, simulate normal data with a seed and compute far tails with `erfc`.
- [ ] 4 Applied: I check real log-expression or replicate measurements with a Q-Q plot before using z-scores, and I compute exact tails for counts instead of z-score p-values.
- [ ] 5 Explained: I can teach why measurement errors are approximately normal and when they are not, the continuity correction, the log-normal gap between mean and median, and how estimating $\sigma$ leads to the t distribution.

## References

[^blitz5]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 5 "Continuous Random Variables" (the normal distribution: density, $\Phi$, standardization and symmetry; its importance through the central limit theorem).
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of sums of independent normals, of the normal approximation with continuity correction, and of the chi-square and Student-t distributions; see also [[Harvard Stat 110 - Probability]], named distributions and limit theorems.
[^openstax6]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 6 "The Normal Distribution", section 6.1 "The Standard Normal Distribution" (z-scores, the empirical rule).
[^openstax8]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 8 "Confidence Intervals" (Student's t distribution).
[^openstax9]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 9 (hypothesis testing with one sample).
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], treatment of data transformations (log and variance-stabilizing) for high-throughput data.
