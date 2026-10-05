---
aliases:
  - PDF
  - Density
  - Probability Density
  - Densité de probabilité
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
  - "[[Cumulative Distribution Function]]"
  - "[[Integral]]"
  - "[[Improper Integral]]"
  - "[[Fundamental Theorem of Calculus]]"
related:
  - "[[Expected Value]]"
  - "[[Variance]]"
  - "[[Uniform Distribution]]"
  - "[[Normal Distribution]]"
  - "[[Histogram]]"
  - "[[Kernel Density Estimation]]"
  - "[[Transformation of Random Variables]]"
  - "[[Likelihood Function]]"
  - "[[Data Transformation]]"
projects: []
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Harvard Stat 110 - Probability]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
---

# Probability Density Function

> [!abstract]
> A continuous measurement, such as a log-intensity, takes any single value with probability zero; its distribution is described by a density curve, and the probability of an interval is the area under that curve.

## Definition

A random variable $X$ is **continuous** with **probability density function** (PDF) $f$ if, for all $a \le b$,

$$P(a \le X \le b) = \int_a^b f(x)\,dx,$$

where $f(x) \ge 0$ for all $x$ and $\int_{-\infty}^{\infty} f(x)\,dx = 1$. Its [[Cumulative Distribution Function]] is then $F(x) = \int_{-\infty}^{x} f(t)\,dt$, and $f = F'$ wherever $f$ is continuous.[^blitz][^openstax][^stat110][^1805]

## Why it matters

- **Continuous measurements.** Fluorescence and mass-spectrometry intensities, qPCR cycle thresholds, fragment lengths and expression values on a log scale are modeled as continuous random variables with a density. High-throughput intensities and counts are usually analyzed after a log or variance-stabilizing transformation, and the transformation changes the density ([[Data Transformation]], [[Microarray]]).[^holmes]
- **Likelihood.** For continuous data, the [[Likelihood Function]] is a product of density values; every maximum likelihood fit of a normal, exponential or gamma model evaluates densities.
- **Plots.** Density plots and violin plots display estimated densities ([[Histogram]], [[Kernel Density Estimation]]).
- **Tails and p-values.** A p-value from a continuous test statistic is an area under its null density ([[P-Value]]).

## Core (L1)

**Points have probability zero.** For a continuous $X$, $P(X = x) = \int_x^x f = 0$ for every single $x$. Only intervals have positive probability, so $P(a < X < b) = P(a \le X \le b)$: including endpoints changes nothing.[^blitz]

**Probability is area.** $P(a \le X \le b)$ is the area under the curve $f$ between $a$ and $b$, and the whole area is 1.[^openstax] In the figure, a toy density for log2 intensities (invented) puts probability $70/256 \approx 0.273$ between 9 and 11; the histogram of simulated values, scaled to density, hugs the curve.

![[density-area-probability.svg]]

**A density is a rate, not a probability.** For a small width $\Delta x$, $P(x \le X \le x + \Delta x) \approx f(x)\,\Delta x$. So $f(x)$ is "probability per unit of $x$": it has units (per log2 unit, per base pair, per second), and it can exceed 1 when the distribution is concentrated. A difference between two technical replicates that is uniform on $[-0.1, 0.1]$ log2 units has density $5$ on that interval ([[Uniform Distribution]]).

**Summaries as integrals.** Sums over values become integrals weighted by the density ([[Expected Value]], [[Variance]]):[^blitz]

$$E[X] = \int_{-\infty}^{\infty} x f(x)\,dx, \qquad \operatorname{Var}(X) = \int_{-\infty}^{\infty} (x - E[X])^2 f(x)\,dx.$$

**Discrete versus continuous.**

| | Discrete ([[Probability Distribution]]) | Continuous |
|---|---|---|
| Described by | pmf $p(x) = P(X = x)$ | density $f(x)$ |
| Values | $0 \le p(x) \le 1$ | $f(x) \ge 0$, possibly $> 1$ |
| Total | $\sum_x p(x) = 1$ | $\int f(x)\,dx = 1$ |
| $P(a \le X \le b)$ | $\sum_{a \le x \le b} p(x)$ | $\int_a^b f(x)\,dx$ |
| Example | read count at a base | log2 intensity of a spot |

## Deeper (L2)

### From CDF to density and back

By the [[Fundamental Theorem of Calculus]], $F(x) = \int_{-\infty}^x f$ gives $F' = f$ at every point where $f$ is continuous, and $P(a \le X \le b) = F(b) - F(a)$. Changing $f$ at finitely many points changes no probability, so a density is defined only "up to" such changes. The median $m$ solves $F(m) = 1/2$; more generally quantiles invert $F$ ([[Quantile]]).

### Histograms estimate densities

With $n$ observations and bins of width $h$, the height $\hat f = \dfrac{\text{count in bin}}{n h}$ has expectation $\frac{1}{h}\int_{\text{bin}} f \approx f(\text{bin centre})$. A histogram drawn this way is on the density scale and its bars have total area 1; raw counts or proportions are not ([[Histogram]]). Smoothing the bars gives [[Kernel Density Estimation]].

### Changing variables

If $Y = g(X)$ with $g$ strictly increasing and differentiable, then $F_Y(y) = P(g(X) \le y) = F_X(g^{-1}(y))$, and differentiating,

$$f_Y(y) = f_X\big(g^{-1}(y)\big)\,\frac{d}{dy} g^{-1}(y).$$

For a decreasing $g$ the derivative gets an absolute value.[^blitz] Two consequences:

- **Units.** If $Y = aX$ with $a > 0$ (a change of units), $f_Y(y) = f_X(y/a)/a$: the density rescales so that areas stay the same.
- **Log and raw scales.** If $X$ is a log2 intensity and $I = 2^X$ the raw intensity, then $f_I(i) = f_X(\log_2 i) / (i \ln 2)$. Quantiles transform directly (the median of $I$ is $2^{\text{median}(X)}$), but means and modes do not (Exercises 3 and 4). The general theory is [[Transformation of Random Variables]].

### Variables without a density

Not every real-valued measurement has a density. If an instrument reports every value below its detection limit $d$ as $d$, the recorded variable has a point mass $P(X = d) > 0$ plus a density above $d$: a **mixed** distribution. Treating it as a pure density (for example fitting a normal to it) misrepresents the pile-up at $d$, and it must be modeled explicitly ([[Missing Data]]).

## Advanced (L3)

- **Likelihoods can exceed 1.** Because densities can be larger than 1, a likelihood $\prod_i f(x_i; \theta)$ can be larger than 1 and a log-likelihood can be positive (Exercise 5). Only differences of log-likelihoods between parameter values or models are meaningful ([[Maximum Likelihood Estimation]]).
- **Density values depend on the parametrization.** Probabilities of events are invariant under a change of variables, but the density picks up the factor $|d g^{-1}/dy|$. The most likely value on the log scale is therefore not the most likely value on the raw scale (Exercise 4), and a statement such as "the density is highest at $x$" is always relative to a chosen scale.
- **Several variables.** A pair $(X, Y)$ has a joint density $f(x, y)$ with $P((X, Y) \in A) = \iint_A f(x, y)\,dx\,dy$; integrating out $y$ gives the marginal density of $X$ ([[Joint Distribution]], [[Multiple Integral]]). The expression values of two genes, or the two coordinates of a cell in a PCA plot, are described this way.

## Mathematical representation

- **Definition.** $f : \mathbb{R} \to [0, \infty)$ integrable, $\int_{\mathbb{R}} f = 1$, $P(X \in [a, b]) = \int_a^b f$ for all $a \le b$.
- **CDF.** $F(x) = \int_{-\infty}^{x} f(t)\,dt$ is continuous and non-decreasing, $F(-\infty) = 0$, $F(\infty) = 1$ ([[Improper Integral]]).
- **Expectation of a function (LOTUS).** $E[g(X)] = \int_{-\infty}^{\infty} g(x) f(x)\,dx$, when the integral converges absolutely.[^blitz]
- **Support.** The set where $f > 0$. For the toy log-intensity model used here, $f(x) = \tfrac{3}{256}(x - 4)(12 - x)$ on $[4, 12]$ and $0$ elsewhere.

## Computational representation

In code, a density is a function evaluated pointwise, and its CDF is a function too; probabilities come from the CDF or from numerical integration ([[Numerical Integration]]). Sampling from an arbitrary density can use **rejection**: propose uniformly over the support and accept $x$ with probability $f(x)/\max f$ ([[Random Variate Generation]]). Libraries follow the same split: `scipy.stats` distributions expose `pdf`, `cdf` and `ppf` methods.

```python
import math
import random

def f(x: float) -> float:
    """Toy density of a log2 intensity: (3/256)(x - 4)(12 - x) on [4, 12], 0 elsewhere."""
    return 3 / 256 * (x - 4) * (12 - x) if 4 <= x <= 12 else 0.0

def F(x: float) -> float:
    """Its CDF, from integrating f: (12u^2 - u^3)/256 with u = x - 4, clipped to [0, 1]."""
    u = min(max(x - 4, 0.0), 8.0)
    return (12 * u**2 - u**3) / 256

def sample(rng: random.Random) -> float:
    """Rejection sampling: propose uniformly on [4, 12], accept with probability f(x)/max f."""
    f_max = f(8.0)
    while True:
        x = rng.uniform(4, 12)
        if rng.random() < f(x) / f_max:
            return x

print("P(X > 10) =", 1 - F(10), " P(9 <= X <= 11) =", F(11) - F(9))
rng = random.Random(42)
xs = [sample(rng) for _ in range(100_000)]
n = len(xs)
mean = sum(xs) / n
var = sum((x - mean) ** 2 for x in xs) / (n - 1)
print(f"simulated: P(X > 10) = {sum(x > 10 for x in xs) / n:.4f}, "
      f"P(9 <= X <= 11) = {sum(9 <= x <= 11 for x in xs) / n:.4f}, mean {mean:.3f}, variance {var:.3f}")
h = 0.5                                             # histogram bin width
for left in (5.0, 7.5, 10.0):
    density_hat = sum(left <= x < left + h for x in xs) / (n * h)
    print(f"bin [{left}, {left + h}): histogram {density_hat:.4f}, f(midpoint) {f(left + h / 2):.4f}")
```

Output:

```text
P(X > 10) = 0.15625  P(9 <= X <= 11) = 0.2734375
simulated: P(X > 10) = 0.1561, P(9 <= X <= 11) = 0.2744, mean 8.003, variance 3.191
bin [5.0, 5.5): histogram 0.0986, f(midpoint) 0.0989
bin [7.5, 8.0): histogram 0.1851, f(midpoint) 0.1868
bin [10.0, 10.5): histogram 0.1282, f(midpoint) 0.1282
```

The simulated probabilities, mean and variance match the exact values derived below, and the density-scaled histogram matches $f$.

## Worked example

> [!example] A toy density for log2 intensities (invented model)
> Suppose the log2 intensity $X$ of probes on an array follows $f(x) = c\,(x - 4)(12 - x)$ on $[4, 12]$, zero elsewhere.
>
> 1. **Normalize.** With $u = x - 4 \in [0, 8]$: $\int_0^8 u(8 - u)\,du = \left[4u^2 - u^3/3\right]_0^8 = 256 - 512/3 = 256/3$, so $c = 3/256$.
> 2. **CDF.** $F(x) = \tfrac{3}{256}\int_0^{u} t(8 - t)\,dt = \dfrac{12u^2 - u^3}{256}$ for $0 \le u \le 8$; check $F(12) = (768 - 512)/256 = 1$.
> 3. **A tail.** $P(X > 10) = 1 - F(10) = 1 - (432 - 216)/256 = 40/256 = 5/32 \approx 0.156$: about one probe in six is brighter than $2^{10}$.
> 4. **An interval.** $P(9 \le X \le 11) = F(11) - F(9) = (245 - 175)/256 = 70/256 \approx 0.273$, the shaded area of the figure.
> 5. **Mean and variance.** $f$ is symmetric about 8, so $E[X] = 8$. $\operatorname{Var}(X) = \tfrac{3}{256}\int_0^8 (u - 4)^2 u(8 - u)\,du = 3.2$ (expand and integrate term by term), standard deviation $\approx 1.79$.
> 6. **Height at the peak.** $f(8) = \tfrac{3}{256} \times 16 = 0.1875$ per log2 unit: the probability of a window of width 0.1 around 8 is about $0.019$.
>
> The simulation in Computational representation confirms steps 3 to 5 (0.1561, 0.2744, 8.003 and 3.191).

## Common misconceptions

> [!warning] "$f(x)$ is the probability that $X = x$"
> That probability is 0 for a continuous variable. $f(x)$ is a probability per unit length; multiply by a small width to get a probability.

> [!warning] "A density cannot be larger than 1"
> Only its total area is 1. A variable concentrated on an interval of width 0.2 has density at least 5 somewhere. Values above 1 are no sign of an error, in a plot or in a likelihood.

> [!warning] "Averaging on the log scale and back-transforming gives the mean intensity"
> $2^{E[X]}$ is the median of $I = 2^X$ when $X$ is symmetric, not its mean: in the toy model $2^{E[X]} = 256$ while $E[2^X] \approx 515$ (Exercise 3). Say which one you report.

> [!warning] "The heights of a histogram are densities"
> Only if the counts are divided by $n$ times the bin width. With raw counts or proportions, changing the bin width changes the heights, and comparing them with a density curve is meaningless.

## Exercises

> [!question] Exercise 1 (L1)
> $f(x) = c\,x$ on $[0, 2]$ and $0$ elsewhere. Find $c$, $P(X \le 1)$, $P(X = 1)$ and $E[X]$.

> [!success]- Solution
> $\int_0^2 c\,x\,dx = 2c = 1$, so $c = 1/2$. $P(X \le 1) = \int_0^1 x/2\,dx = 1/4$: half the range carries only a quarter of the probability, because the density grows with $x$. $P(X = 1) = 0$ (a single point). $E[X] = \int_0^2 x \cdot x/2\,dx = [x^3/6]_0^2 = 4/3$.

> [!question] Exercise 2 (L1)
> The log2 ratio $D$ between two technical replicates of the same sample is modeled (invented model) as uniform on $[-0.2, 0.2]$. Write its density, check that it is valid, and compute $P(|D| > 0.1)$.

> [!success]- Solution
> $f(d) = 1/0.4 = 2.5$ on $[-0.2, 0.2]$, $0$ elsewhere. It is non-negative with area $0.4 \times 2.5 = 1$, so it is valid even though $f > 1$. $P(|D| > 0.1) = 2 \times 0.1 \times 2.5 = 0.5$.

> [!question] Exercise 3 (L2, Python)
> Using `f` from the code above, write a midpoint-rule integrator and check numerically that $\int f = 1$, $P(X > 10) = 5/32$ and $E[X] = 8$. Then compute $E[2^X]$, the mean raw intensity, and compare with $2^{E[X]}$.

> [!success]- Solution
> ```python
> def midpoint_integral(g, a: float, b: float, n: int = 10_000) -> float:
>     """Midpoint rule: sum of g at the centres of n equal sub-intervals, times their width."""
>     h = (b - a) / n
>     return h * sum(g(a + (i + 0.5) * h) for i in range(n))
>
> print(round(midpoint_integral(f, 4, 12), 6))                      # 1.0
> print(round(midpoint_integral(f, 10, 12), 6))                     # 0.15625
> print(round(midpoint_integral(lambda x: x * f(x), 4, 12), 6))     # 8.0
> print(round(midpoint_integral(lambda x: 2**x * f(x), 4, 12), 1))  # 515.2
> ```
>
> $E[2^X] \approx 515$ is twice $2^{E[X]} = 256$: $2^x$ is convex, so bright probes pull the raw-scale mean up (Jensen's inequality). $256$ is the median of the raw intensity, since $2^x$ is increasing and $X$ has median 8.

> [!question] Exercise 4 (L3)
> For the toy model, derive the density of the raw intensity $I = 2^X$ and find its mode. Compare mode, median and mean of $I$.

> [!success]- Solution
> $g^{-1}(i) = \log_2 i$, $\frac{d}{di}\log_2 i = \frac{1}{i \ln 2}$, so $f_I(i) = \dfrac{f(\log_2 i)}{i \ln 2}$ for $16 \le i \le 4096$. Writing $i = 2^x$, $f_I$ is maximal where $f(x)\,2^{-x}$ is: setting the derivative of $\ln f(x) - x \ln 2$ to zero gives $\dfrac{16 - 2x}{(x - 4)(12 - x)} = \ln 2$, i.e. $\ln 2\, x^2 - (16 \ln 2 + 2)x + 16 + 48 \ln 2 = 0$, whose root in $[4, 12]$ is $x \approx 5.19$. The mode of $I$ is $2^{5.19} \approx 36.5$, the median $256$, the mean $\approx 515$. The log scale has mode = median = mean = 8; the raw scale is so skewed that the three disagree by a factor of 14. The Jacobian $1/(i \ln 2)$ moved the peak.

> [!question] Exercise 5 (L3)
> Ten replicate log-ratios are observed and modeled as independent uniform on $[-0.1, 0.1]$ (all ten fall in this interval). Compute the log-likelihood. Is a positive log-likelihood a problem?

> [!success]- Solution
> Each observation has density $1/0.2 = 5$, so $\ell = 10 \ln 5 \approx 16.1 > 0$. No problem: a likelihood built from densities is not a probability and has units (here per $(\log_2 \text{unit})^{10}$). What matters is the comparison: under a uniform on $[-0.2, 0.2]$, $\ell = 10 \ln 2.5 \approx 9.2$, so the narrower model fits these data better, as long as it contains all of them.

## Mastery checklist

- [ ] 1 Recognized: I can state that probabilities of a continuous variable are areas under its density and that single points have probability 0.
- [ ] 2 Understood: I can explain why a density can exceed 1, what its units are, and how density, CDF and histogram relate.
- [ ] 3 Practiced: I can normalize a density, compute interval probabilities, means and variances by integration, and check them by simulation and numerical integration in Python.
- [ ] 4 Applied: I plot the density of real log-intensities or log-expression values, on the density scale, and say which summary (mean, median) I report on which scale.
- [ ] 5 Explained: I can teach the change-of-variables formula, why modes and means do not survive a log transformation while quantiles do, and why likelihoods of continuous data can be larger than 1.

## References

[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of continuous random variables (PDF, CDF, expectation and LOTUS, change of variables).
[^stat110]: [[Harvard Stat 110 - Probability]], continuous random variables and densities.
[^1805]: [[MIT 18.05 - Introduction to Probability and Statistics]], random variables and probability distributions.
[^openstax]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 5 "Continuous Random Variables".
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], treatment of data transformations (log and variance-stabilizing) for high-throughput data.
