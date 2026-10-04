---
aliases:
  - Taylor Expansion
  - Taylor Polynomial
  - Maclaurin Series
  - Série de Taylor
  - Développement limité
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Derivative]]"
  - "[[Differentiation Rules]]"
  - "[[Linear Approximation]]"
  - "[[Infinite Series]]"
related:
  - "[[Jukes-Cantor Model]]"
  - "[[Evolutionary Distance]]"
  - "[[Variance]]"
  - "[[Poisson Distribution]]"
  - "[[Exponential Function]]"
  - "[[Logarithm]]"
  - "[[Hessian Matrix]]"
  - "[[Maximum Likelihood Estimation]]"
  - "[[Integration by Parts]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Inferring Phylogenies (Felsenstein)]]"
  - "[[Molecular Evolution (Yang)]]"
---

# Taylor Series

> [!abstract]
> A Taylor polynomial replaces a curve near a point by the polynomial that matches its value, slope, curvature and higher derivatives there; with a bound on the remainder, it says exactly how good approximations such as $\ln(1 + x) \approx x$ are, which is why corrected evolutionary distances are close to raw mismatch proportions when divergence is small.

## Definition

Let $f$ have $n$ derivatives at $a$. The **Taylor polynomial** of degree $n$ of $f$ at $a$ is[^os2][^mit]

$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}\,(x - a)^k = f(a) + f'(a)(x - a) + \frac{f''(a)}{2}(x - a)^2 + \dots$$

If $f$ has derivatives of all orders, the **Taylor series** is the power series $\sum_{k=0}^{\infty} \frac{f^{(k)}(a)}{k!}(x - a)^k$; at $a = 0$ it is called a **Maclaurin series**. The **remainder** is $R_n(x) = f(x) - P_n(x)$. **Taylor's theorem**: if $f^{(n+1)}$ exists between $a$ and $x$, then $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$ for some $c$ between $a$ and $x$ (Lagrange form). The series equals $f(x)$ exactly when $R_n(x) \to 0$.[^os2]

## Why it matters

- **Small-rate approximations, with a guarantee.** $e^{-x} \approx 1 - x$, $\ln(1 + x) \approx x$, $(1 + x)^\alpha \approx 1 + \alpha x$ are first-order Taylor polynomials ([[Linear Approximation]]); the remainder says when they fail.
- **Evolutionary distances.** The [[Jukes-Cantor Model|Jukes-Cantor]] correction $d = -\frac34 \ln(1 - \frac43 p)$ expands to $p + \frac23 p^2 + \dots$: for close sequences the raw proportion of differences is nearly the distance, for divergent ones it is not ([[Evolutionary Distance]]).[^felsenstein][^yang]
- **Variances of transformed estimates.** The delta method, $\operatorname{Var}(g(\hat\theta)) \approx g'(\theta)^2 \operatorname{Var}(\hat\theta)$, is a first-order Taylor expansion; it gives error bars for distances, log fold changes and other derived quantities ([[Variance]]).
- **Series behind distributions.** $\sum \lambda^k/k! = e^\lambda$, the Maclaurin series of $e^x$, is why Poisson probabilities sum to 1 ([[Poisson Distribution]], [[Infinite Series]]).
- **Optimization and numerics.** Second-order expansions underlie Newton's method and the curvature of log-likelihoods ([[Hessian Matrix]]); error orders of numerical integrators come from Taylor expansions ([[Euler Method]], [[Integral]]).

## Core (L1)

### Matching derivatives

$P_n$ is the unique polynomial of degree $\le n$ with $P_n^{(k)}(a) = f^{(k)}(a)$ for $k = 0, \dots, n$: differentiating $\frac{f^{(k)}(a)}{k!}(x - a)^k$ $k$ times at $a$ gives exactly $f^{(k)}(a)$. Degree 1 is the tangent line; degree 2 adds the curvature, and so on.

### Standard Maclaurin series

| $f(x)$ | Series | Valid for |
|---|---|---|
| $e^x$ | $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = \sum_k \frac{x^k}{k!}$ | all $x$ |
| $\frac{1}{1 - x}$ | $1 + x + x^2 + \dots$ | $\lvert x \rvert < 1$ |
| $\ln(1 + x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$ | $-1 < x \le 1$ |
| $(1 + x)^\alpha$ | $1 + \alpha x + \frac{\alpha(\alpha - 1)}{2} x^2 + \dots$ | $\lvert x \rvert < 1$ |
| $\sin x$, $\cos x$ | $x - \frac{x^3}{3!} + \dots$, $1 - \frac{x^2}{2!} + \dots$ | all $x$ |

These are given with their intervals of validity in the references;[^os2] the second line is the geometric series, and the third follows from it by integrating term by term. At $x = 1$ the third gives $\ln 2 = 1 - \frac12 + \frac13 - \dots$, the alternating harmonic series.

### Controlling the remainder

If $\lvert f^{(n+1)} \rvert \le M$ between $a$ and $x$, Lagrange's form gives

$$\lvert R_n(x) \rvert \le \frac{M\,\lvert x - a \rvert^{n+1}}{(n + 1)!}.$$

For $e^{0.1}$ around $a = 0$, all derivatives are $e^c \le e^{0.1}$:

| $n$ | $P_n(0.1)$ | true error | bound $e^{0.1}\,0.1^{n+1}/(n+1)!$ |
|---:|---:|---:|---:|
| 0 | 1.00000000 | 1.05e-01 | 1.11e-01 |
| 1 | 1.10000000 | 5.17e-03 | 5.53e-03 |
| 2 | 1.10500000 | 1.71e-04 | 1.84e-04 |
| 3 | 1.10516667 | 4.25e-06 | 4.60e-06 |

Each extra degree gains roughly a factor $\lvert x - a \rvert / (n + 2)$: close to $a$, a few terms are enough.

### Small-rate approximations in biology

- **Rare events.** For a Poisson count with small mean $\lambda$, $P(X \ge 1) = 1 - e^{-\lambda} = \lambda - \frac{\lambda^2}{2} + \dots \approx \lambda$: with $\lambda = 0.01$, $0.00995$ versus $0.01$. The error is about $\lambda^2/2$.
- **Log fold changes.** $\ln(1 + x) \approx x - \frac{x^2}{2}$: a 10 % increase has natural log fold change $\ln 1.1 = 0.0953$, close to $0.1$; for a doubling ($x = 1$) the linear approximation gives 1 instead of $\ln 2 = 0.693$.

## Deeper (L2)

### Radius of convergence

A power series $\sum c_k (x - a)^k$ converges for $\lvert x - a \rvert < R$ and diverges for $\lvert x - a \rvert > R$, for some radius $R \in [0, \infty]$; inside, it can be differentiated and integrated term by term.[^os2] For $\frac{1}{1 - x}$ and $\ln(1 + x)$, $R = 1$: at $x = 2$, the series for $\ln(1 + x)$ diverges although $\ln 3$ exists. Adding terms helps only inside the radius.

### Jukes-Cantor distance at small divergence

Under the Jukes-Cantor (JC69) model, all substitutions between the four nucleotides occur at the same rate. If $d$ is the expected number of substitutions per site separating two sequences, the expected proportion of differing sites is $p = \frac34\left(1 - e^{-4d/3}\right)$, and inverting gives the distance estimated from an observed $p$:[^felsenstein][^yang]

$$d = -\frac34 \ln\left(1 - \frac43 p\right), \qquad p < \frac34 .$$

With $u = \frac43 p$ and $\ln(1 - u) = -\sum_{k \ge 1} u^k / k$:

$$d = \frac34 \sum_{k \ge 1} \frac{1}{k}\left(\frac{4p}{3}\right)^k = p + \frac23 p^2 + \frac{16}{27} p^3 + \dots$$

- **Small divergence:** $d \approx p$. Multiple substitutions at the same site are rare, so counting differences counts substitutions.
- **The correction:** $\frac23 p^2$ to second order, always positive: $p$ underestimates $d$, by about $\frac23 p$ in relative terms.
- **Saturation:** the radius of convergence is $\lvert u \rvert < 1$, that is $p < \frac34$, exactly where $d$ is defined. As $p \to \frac34$ (random sequences), $d \to \infty$.

| $p$ | 0.01 | 0.05 | 0.1 | 0.2 | 0.3 | 0.5 | 0.7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| $d_{JC}$ | 0.01007 | 0.05174 | 0.10733 | 0.23262 | 0.38312 | 0.82396 | 2.03104 |
| $p + \frac23 p^2$ | 0.01007 | 0.05167 | 0.10667 | 0.22667 | 0.36000 | 0.66667 | 1.02667 |
| $(d - p)/p$ | 0.7 % | 3.5 % | 7.3 % | 16.3 % | 27.7 % | 64.8 % | 190.1 % |

### The delta method

If an estimator $\hat\theta$ is concentrated near $\theta$, expand $g(\hat\theta) \approx g(\theta) + g'(\theta)(\hat\theta - \theta)$. A constant plus a constant times $\hat\theta$ has variance

$$\operatorname{Var}\big(g(\hat\theta)\big) \approx g'(\theta)^2 \operatorname{Var}(\hat\theta).$$

**JC distance.** With $n$ aligned sites and $\hat p = k/n$, $\operatorname{Var}(\hat p) = p(1 - p)/n$ ([[Binomial Distribution]]) and $d'(p) = \frac{1}{1 - 4p/3}$, so

$$\operatorname{Var}(\hat d) \approx \frac{p(1 - p)}{n\,(1 - 4p/3)^2},$$

the variance formula given for the JC69 distance in the references.[^yang] The factor $(1 - 4p/3)^{-2}$ explodes near saturation: distances between divergent sequences are not only larger but much noisier. The simulation below checks the approximation at $n = 500$, $p = 0.2$.

## Advanced (L3)

- **Several variables.** $f(\theta + h) \approx f(\theta) + \nabla f(\theta) \cdot h + \frac12 h^\top H(\theta)\,h$, with $\nabla f$ the [[Gradient]] and $H$ the [[Hessian Matrix]]. Maximizing this quadratic model gives Newton's step $h = -H^{-1}\nabla f$; near a maximum of a log-likelihood, the curvature $-H$ measures how sharply the data pin down the parameters, which is how standard errors of maximum likelihood estimates (branch lengths, rates) are obtained ([[Maximum Likelihood Estimation]]).[^yang] The multivariate delta method replaces $g'(\theta)^2$ by $\nabla g^\top \Sigma\,\nabla g$.
- **Smooth is not enough.** $f(x) = e^{-1/x^2}$ (with $f(0) = 0$) has every derivative equal to 0 at 0, so its Maclaurin series is identically 0 while $f(x) > 0$ for $x \neq 0$. Functions equal to their Taylor series near every point are called analytic; $e^x$, $\ln$, polynomials and their combinations are.
- **Error orders of numerical methods.** $y(t + h) = y(t) + h\,y'(t) + \frac{h^2}{2} y''(c)$ shows that one Euler step makes an error $O(h^2)$, hence $O(h)$ over a fixed interval ([[Euler Method]]); expanding $f$ around a midpoint shows why the midpoint rule is second order ([[Integral#How fast Riemann sums converge]]).

## Mathematical representation

- **Taylor's theorem (Lagrange).** $f(x) = P_n(x) + \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$, $c$ between $a$ and $x$.[^os2]
- **Integral form.** $R_n(x) = \int_a^x \frac{f^{(n+1)}(t)}{n!}(x - t)^n\,dt$, obtained from $f(x) = f(a) + \int_a^x f'(t)\,dt$ by repeated [[Integration by Parts]].
- **Big-O notation.** $f(x) = P_n(x) + O\big((x - a)^{n+1}\big)$ as $x \to a$ ([[Big O Notation]]).
- **Radius.** For $\sum c_k (x - a)^k$, $R = \lim \lvert c_k / c_{k+1} \rvert$ when this limit exists (ratio test, [[Infinite Series]]).

## Computational representation

Computing a truncated series and comparing it with the exact function and with the remainder bound is the standard check of an approximation.

```python
import math
import random

def taylor_exp(x: float, n: int) -> float:
    """Degree-n Maclaurin polynomial of e^x."""
    return sum(x ** k / math.factorial(k) for k in range(n + 1))

x = 0.1
for n in range(4):
    err = abs(math.exp(x) - taylor_exp(x, n))
    bound = math.exp(x) * x ** (n + 1) / math.factorial(n + 1)    # Lagrange, |f^(n+1)| <= e^x on [0, x]
    print(n, f"{taylor_exp(x, n):.8f}", f"{err:.2e}", f"{bound:.2e}")

def jc_distance(p: float) -> float:
    """Jukes-Cantor distance from the proportion p of differing sites (p < 3/4)."""
    return -0.75 * math.log(1 - 4 * p / 3)

print("p      d_JC    p+2p^2/3  rel.gap(d vs p)")
for p in (0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7):
    d = jc_distance(p)
    print(f"{p:<6} {d:.5f} {p + 2 * p * p / 3:.5f}   {(d - p) / p:.1%}")

# delta method: variance of the estimated JC distance, n sites, true p
random.seed(4)
n, p = 500, 0.2
d_hat = []
for _ in range(20_000):
    k = sum(random.random() < p for _ in range(n))
    d_hat.append(jc_distance(k / n))
m = sum(d_hat) / len(d_hat)
var_sim = sum((d - m) ** 2 for d in d_hat) / (len(d_hat) - 1)
var_delta = p * (1 - p) / (n * (1 - 4 * p / 3) ** 2)
print(f"simulated Var = {var_sim:.3e}, delta method = {var_delta:.3e}")
```

It prints the two tables above, then `simulated Var = 6.017e-04, delta method = 5.950e-04`: the delta method is within about 1 % of the simulated variance.

## Worked example

> [!example] Two sequences differing at 10 % of sites (invented alignment)
> 100 differences in 1000 aligned sites: $p = 0.1$.
>
> 1. **Exact JC distance.** $d = -0.75 \ln(1 - 0.1\overline{3}) = 0.75 \times 0.14310 = 0.10733$ substitutions per site.
> 2. **First order.** $d \approx p = 0.1$: error $0.0073$, 6.8 % of $d$.
> 3. **Second order.** $p + \frac23 p^2 = 0.10667$: error $0.00066$.
> 4. **Third order.** $+\frac{16}{27}p^3 = 0.10726$: error $0.00007$. Each term is smaller than the previous one by a factor below $\frac43 p \approx 0.13$, so the error is of the order of the first omitted term.
> 5. **Uncertainty.** $\operatorname{Var}(\hat d) \approx \frac{0.1 \times 0.9}{1000 \times (1 - 0.1\overline{3})^2} = 1.20 \times 10^{-4}$, SD $\approx 0.011$: the sampling error is larger than the difference between $d$ and $p$ here, but at $p = 0.3$ the gap (0.083) dwarfs it.

## Common misconceptions

> [!warning] "A Taylor series always converges to the function"
> It may converge only within a radius ($\ln(1 + x)$ for $-1 < x \le 1$), and even where it converges it may converge to something else ($e^{-1/x^2}$ at 0). Check the remainder.

> [!warning] "The p-distance is a fine evolutionary distance"
> Only at small divergence: $p$ underestimates the JC distance by 7 % at $p = 0.1$ and by 39 % at $p = 0.5$ (in units of $d$). Trees built from raw $p$ compress long branches ([[Evolutionary Distance]]).

> [!warning] "The delta method is exact"
> It is a first-order approximation. It degrades when the estimator is spread out relative to the curvature of $g$: with 20 sites and $p = 0.5$, $\hat p \ge 0.75$ happens with probability about 0.02, and then $\hat d$ is infinite, so its variance does not even exist.

## Exercises

> [!question] Exercise 1 (L1)
> Write the degree-3 Maclaurin polynomial of $e^{-x}$ and use it to approximate $e^{-0.2}$.

> [!success]- Solution
> $1 - x + \frac{x^2}{2} - \frac{x^3}{6}$. At $0.2$: $1 - 0.2 + 0.02 - 0.001333 = 0.818667$, versus $e^{-0.2} = 0.818731$.

> [!question] Exercise 2 (L1)
> Approximate $\ln 1.1$ to second order and interpret it as a log fold change.

> [!success]- Solution
> $\ln(1 + x) \approx x - \frac{x^2}{2} = 0.1 - 0.005 = 0.095$ (exact $0.09531$). For small changes, the natural log fold change is close to the relative change, slightly below it.

> [!question] Exercise 3 (L2)
> Bound the error of $1 + x + \frac{x^2}{2}$ as an approximation of $e^x$ on $[0, 0.5]$.

> [!success]- Solution
> $f''' = e^x \le e^{0.5}$ on the interval, so $\lvert R_2(x) \rvert \le e^{0.5} \frac{0.5^3}{6} \approx 0.034$. The bound is worst at $x = 0.5$, where the true error is $e^{0.5} - 1.625 = 0.0237$.

> [!question] Exercise 4 (L2)
> Derive $d = p + \frac23 p^2 + O(p^3)$ for the JC distance. By how much does $p$ underestimate $d$, as a fraction of $d$, at $p = 0.05$ and $p = 0.2$? How much does the second-order formula improve this?

> [!success]- Solution
> $\ln(1 - u) = -u - \frac{u^2}{2} - O(u^3)$ with $u = \frac43 p$ gives $d = \frac34\left(\frac43 p + \frac{8}{9}p^2\right) + O(p^3) = p + \frac23 p^2 + O(p^3)$. With $d = 0.05174$ and $0.23262$: $(d - p)/d = 3.4\,\%$ and $14.0\,\%$. The second-order formula leaves $0.15\,\%$ and $2.6\,\%$.

> [!question] Exercise 5 (L3, Python)
> Repeat the delta-method simulation with $n = 100$ sites and $p = 0.5$ (seed 4, 20,000 replicates), discarding replicates with $\hat p \ge 0.75$ if any. Compare the simulated variance with the delta-method value and explain the gap.

> [!success]- Solution
> ```python
> random.seed(4)
> n, p, d_hat = 100, 0.5, []
> for _ in range(20_000):
>     k = sum(random.random() < p for _ in range(n))
>     if k / n < 0.75:
>         d_hat.append(jc_distance(k / n))
> m = sum(d_hat) / len(d_hat)
> var_sim = sum((d - m) ** 2 for d in d_hat) / (len(d_hat) - 1)
> print(len(d_hat), f"{var_sim:.3e}", f"{p * (1 - p) / (n * (1 - 4 * p / 3) ** 2):.3e}")
> # 20000 2.540e-02 2.250e-02
> ```
>
> No replicate reached $\hat p \ge 0.75$ with this seed, and the simulated variance exceeds the delta-method value by about 13 %. Near saturation $d(p)$ curves sharply upward, so the linear approximation underestimates the spread: large $\hat p$ produce disproportionately large $\hat d$. The delta method is reliable only when $\hat p$ stays well inside the region where $d$ is nearly linear.

> [!question] Exercise 6 (L3)
> Use the delta method to find the approximate variance of $\sqrt X$ for $X \sim \mathrm{Pois}(\lambda)$ with large $\lambda$. Why is the square root used before analyzing counts?

> [!success]- Solution
> $g(x) = \sqrt x$, $g'(\lambda) = \frac{1}{2\sqrt\lambda}$, $\operatorname{Var}(X) = \lambda$: $\operatorname{Var}(\sqrt X) \approx \frac{\lambda}{4\lambda} = \frac14$, whatever $\lambda$. Raw counts have variance growing with the mean; after the square root, variance is roughly constant, which suits methods that assume equal variances ([[Variance#Delta method and variance stabilization]]).

## Mastery checklist

- [ ] 1 Recognized: I can write the Taylor polynomial formula and the Maclaurin series of $e^x$, $\frac{1}{1-x}$ and $\ln(1 + x)$.
- [ ] 2 Understood: I can explain the Lagrange remainder, the radius of convergence, and why first-order approximations work for small rates.
- [ ] 3 Practiced: I can expand a function to a given order, bound the error, and check both in Python.
- [ ] 4 Applied: I can decide when a p-distance is an acceptable proxy for the JC distance and give a delta-method error bar for a derived estimate.
- [ ] 5 Explained: I can teach the multivariate second-order expansion behind Newton's method and likelihood curvature, and the limits of Taylor approximations (non-analytic functions, saturation, the delta method near singularities).

## References

[^os2]: [[Calculus (OpenStax)]], Volume 2, power series (power series and their interval of convergence, term-by-term differentiation and integration, Taylor and Maclaurin series, Taylor's theorem with remainder).
[^mit]: [[MIT 18.01SC - Single Variable Calculus]], infinite series part (Taylor series).
[^felsenstein]: [[Inferring Phylogenies (Felsenstein)]], treatment of the Jukes-Cantor model and of distances corrected for multiple substitutions.
[^yang]: [[Molecular Evolution (Yang)]], treatment of the JC69 model (expected proportion of differences, the JC69 distance and its variance) and of maximum likelihood estimation (variance from the curvature of the log-likelihood).
