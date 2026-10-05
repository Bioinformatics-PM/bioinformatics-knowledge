---
aliases:
  - Generalized Integral
  - Intégrale impropre
  - Intégrale généralisée
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Integral]]"
  - "[[Limit]]"
  - "[[Fundamental Theorem of Calculus]]"
related:
  - "[[Infinite Series]]"
  - "[[Integration by Parts]]"
  - "[[Probability Density Function]]"
  - "[[Expected Value]]"
  - "[[Normal Distribution]]"
  - "[[Exponential Distribution]]"
  - "[[Law of Large Numbers]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Introduction to Probability (Blitzstein)]]"
---

# Improper Integral

> [!abstract]
> An improper integral is an integral over an infinite range, or of a function that blows up, defined as a limit of ordinary integrals; it converges when that limit is a finite number, which is exactly what a probability density, a mean or a variance needs to exist.

## Definition

**Type 1 (infinite range).** If $f$ is integrable on $[a, t]$ for every $t > a$,[^os2]

$$\int_a^\infty f(x)\,dx = \lim_{t \to \infty} \int_a^t f(x)\,dx .$$

The integral **converges** if the limit exists and is finite, and **diverges** otherwise. $\int_{-\infty}^b$ is defined the same way, and $\int_{-\infty}^{\infty} f = \int_{-\infty}^{c} f + \int_{c}^{\infty} f$ converges only if **both** pieces converge (for any $c$).

**Type 2 (unbounded integrand).** If $f$ is continuous on $(a, b]$ and unbounded near $a$, $\int_a^b f = \lim_{t \to a^+} \int_t^b f$; similarly at $b$, or at an interior point by splitting there.[^os2][^mit]

## Why it matters

- **Densities live on infinite ranges.** Normal, exponential and gamma densities are defined on $\mathbb{R}$ or $(0, \infty)$. "The density integrates to 1", tail probabilities and p-values are improper integrals ([[Probability Density Function]]).[^blitz5]
- **Whether a mean or variance exists.** $E[X] = \int x f(x)\,dx$ exists only if $\int \lvert x \rvert f(x)\,dx$ converges. Heavy-tailed variables (some ratios of noisy measurements) have no mean, and averaging them does not stabilize ([[Expected Value]]).[^blitz]
- **Tails beyond the data.** Extrapolating a pharmacokinetic curve beyond the last sample, or a survival curve beyond follow-up, is an improper integral of a fitted tail ([[Integral#Worked example]]).
- **Convergence tests for series.** The integral test decides the convergence of sums such as $\sum 1/k^p$ by comparing them with $\int 1/x^p$ ([[Infinite Series]]).

## Core (L1)

**Type 1 examples.** Compute the integral up to $t$, then let $t \to \infty$:

| Integral | Up to $t$ | Limit |
|---|---|---|
| $\int_1^\infty \frac{dx}{x^2}$ | $1 - \frac1t$ | $1$: converges |
| $\int_1^\infty \frac{dx}{x}$ | $\ln t$ | $\infty$: diverges |
| $\int_0^\infty \lambda e^{-\lambda x}\,dx$ | $1 - e^{-\lambda t}$ | $1$: converges (the exponential density) |

$1/x$ and $1/x^2$ both tend to 0, but $1/x$ does so too slowly: tending to 0 is not enough.

**$p$-integrals.** $\int_1^\infty x^{-p}\,dx$ converges if and only if $p > 1$ (value $\frac{1}{p - 1}$), and $\int_0^1 x^{-p}\,dx$ converges if and only if $p < 1$ (value $\frac{1}{1 - p}$).[^os2] So $\int_0^1 \frac{dx}{\sqrt x} = 2$ converges although the integrand is unbounded, while $\int_0^1 \frac{dx}{x}$ diverges.

**Both ends infinite.** $\int_{-\infty}^\infty \frac{dx}{1 + x^2} = \lim \big[\arctan x\big] = \frac\pi2 - \left(-\frac\pi2\right) = \pi$, so $\frac{1}{\pi(1 + x^2)}$ is a density (the Cauchy density).

**Hidden singularities.** $\int_{-1}^{1} \frac{dx}{x^2}$ is improper at 0; splitting there, $\int_0^1 x^{-2}\,dx$ diverges ($p = 2 \ge 1$), so the whole integral diverges. Applying the [[Fundamental Theorem of Calculus]] across the singularity gives the absurd value $-2$.

## Deeper (L2)

### Comparison test

If $0 \le f(x) \le g(x)$ for $x \ge a$: if $\int_a^\infty g$ converges, so does $\int_a^\infty f$; if $\int_a^\infty f$ diverges, so does $\int_a^\infty g$.[^os2] Convergence can thus be decided without computing anything, by bounding the tail.

### Normalizing the normal density

$e^{-x^2/2}$ has no elementary antiderivative ([[Antiderivative]]), so convergence comes from comparison. Since $(\lvert x \rvert - 1)^2 \ge 0$, $\frac{x^2}{2} \ge \lvert x \rvert - \frac12$, hence $0 < e^{-x^2/2} \le e^{1/2 - \lvert x \rvert}$, and

$$\int_{-\infty}^{\infty} e^{1/2 - \lvert x \rvert}\,dx = 2\sqrt{e} \approx 3.30 \quad\Longrightarrow\quad \int_{-\infty}^{\infty} e^{-x^2/2}\,dx \text{ converges (and is below 3.30).}$$

Its exact value is $\sqrt{2\pi} \approx 2.5066$, which is why the standard normal density carries the factor $1/\sqrt{2\pi}$.[^blitz5] The value is obtained by squaring the integral and switching to polar coordinates ([[Multiple Integral]]); the numerical check below reaches it with $[-8, 8]$.

### Expected values must converge absolutely

For a density $f$, $E[X] = \int_{-\infty}^{\infty} x f(x)\,dx$ is defined only when $\int \lvert x \rvert f(x)\,dx < \infty$; likewise $\operatorname{Var}(X)$ needs $\int x^2 f(x)\,dx < \infty$.[^blitz5] The Cauchy density $\frac{1}{\pi(1 + x^2)}$ is symmetric about 0 but has no mean: $\lvert x \rvert f(x) \approx \frac{1}{\pi \lvert x \rvert}$ for large $\lvert x \rvert$, a divergent $p = 1$ tail. The ratio of two independent standard normals has exactly this distribution.[^blitz] Sample means of Cauchy data never settle, because the [[Law of Large Numbers]] assumes a finite mean (Exercise 5).

### Symmetric limits are not enough

$\int_{-t}^{t} \frac{x}{1 + x^2}\,dx = 0$ for every $t$, yet $\int_0^\infty \frac{x}{1 + x^2}\,dx = \lim \frac12\ln(1 + t^2) = \infty$, so $\int_{-\infty}^{\infty} \frac{x}{1+x^2}\,dx$ diverges. Both tails must converge separately.

## Mathematical representation

- $\int_a^\infty f = \lim_{t \to \infty} \int_a^t f$; $\int_a^b f = \lim_{t \to a^+} \int_t^b f$ for a singularity at $a$.
- $\int_1^\infty x^{-p}\,dx < \infty \iff p > 1$; $\int_0^1 x^{-p}\,dx < \infty \iff p < 1$; $\int_0^\infty e^{-\lambda x}\,dx = 1/\lambda$ for $\lambda > 0$.
- **Absolute convergence.** If $\int \lvert f \rvert$ converges, so does $\int f$ (comparison applied to $\lvert f \rvert - f \le 2\lvert f \rvert$).[^os2]
- **Densities.** $f \ge 0$ with $\int_{\mathbb{R}} f = 1$; the $k$-th moment exists iff $\int_{\mathbb{R}} \lvert x \rvert^k f(x)\,dx < \infty$.

## Computational representation

A computer can only integrate over finite ranges: an improper integral is approximated by truncating the range and **bounding the neglected tail**, or by a substitution that maps $[0, \infty)$ onto a finite interval (what adaptive routines such as `scipy.integrate.quad` do with infinite limits).

```python
import math

def midpoint(f, a: float, b: float, n: int = 100_000) -> float:
    """Midpoint Riemann sum of f on [a, b]."""
    dx = (b - a) / n
    return dx * sum(f(a + (i + 0.5) * dx) for i in range(n))

# 1. partial integrals on [1, t]: 1/x^2 settles at 1, 1/x keeps growing like ln t
for t in (10, 100, 1000, 10_000):
    print(t, round(1 - 1 / t, 4), round(math.log(t), 4))

# 2. normalizing the normal density: integral of e^{-x^2/2} on [-L, L]
for L in (1, 2, 4, 8):
    print(L, round(midpoint(lambda x: math.exp(-x * x / 2), -L, L), 6))
print("sqrt(2 pi) =", round(math.sqrt(2 * math.pi), 6))
```

Output:

```text
10 0.9 2.3026
100 0.99 4.6052
1000 0.999 6.9078
10000 0.9999 9.2103
1 1.711249
2 2.392576
4 2.506469
8 2.506628
sqrt(2 pi) = 2.506628
```

The partial integrals of $1/x$ never stop growing, only slowly: no finite truncation reveals divergence by itself, which is why the limit has to be computed or bounded analytically.

## Worked example

> [!example] A density with a mean but no variance (invented model)
> Suppose the sizes of clusters in some assay are modeled by $f(x) = \frac{c}{(1 + x)^3}$ for $x \ge 0$.
>
> 1. **Normalize.** $\int_0^\infty (1 + x)^{-3}\,dx = \lim \left[-\tfrac12 (1 + x)^{-2}\right]_0^t = \tfrac12$, so $c = 2$.
> 2. **Mean.** With $u = 1 + x$: $\int_0^\infty \frac{2x}{(1+x)^3}\,dx = 2\int_1^\infty (u^{-2} - u^{-3})\,du = 2\left(1 - \tfrac12\right) = 1$. Finite.
> 3. **Second moment.** $\int_0^\infty \frac{2x^2}{(1 + x)^3}\,dx = 2\int_1^\infty \left(\frac1u - \frac{2}{u^2} + \frac{1}{u^3}\right) du$, and the $\frac1u$ term diverges. The variance is infinite.
> 4. **Numerically.** Integrating up to $t = 10, 100, 1000$ with `midpoint` gives total mass $0.9917, 0.9999, 1.0000$, mean part $0.8264, 0.9803, 0.9980$, but second-moment part $2.151, 6.270, 10.822$: it grows like $2\ln t$, without limit.
> 5. **Consequence.** A sample mean of such data converges, but slowly and erratically, and a sample standard deviation estimates nothing stable: report medians and quantiles instead.

## Common misconceptions

> [!warning] "If $f(x) \to 0$, the integral to infinity converges"
> $1/x \to 0$ but $\int_1^\infty dx/x = \infty$. What matters is how fast $f$ decays: faster than $1/x^{p}$ with some $p > 1$.

> [!warning] "A symmetric density has mean equal to its centre"
> Only if the mean exists. The Cauchy density is symmetric about 0 and has no mean; symmetry gives the median, not the mean.

> [!warning] "Integrate numerically far enough and you have the answer"
> Truncation hides divergence ($\int_1^{10^4} dx/x \approx 9.2$ looks harmless) and mishandles slowly decaying tails. Always check convergence analytically (comparison, $p$-test) and bound the neglected tail.

## Exercises

> [!question] Exercise 1 (L1)
> Compute $\int_0^\infty e^{-3x}\,dx$ and $\int_1^\infty x^{-3/2}\,dx$.

> [!success]- Solution
> $\lim \frac{1 - e^{-3t}}{3} = \frac13$. $\lim \left[-2x^{-1/2}\right]_1^t = \lim (2 - 2t^{-1/2}) = 2$ ($p = 3/2 > 1$).

> [!question] Exercise 2 (L1)
> Decide whether these converge: $\int_0^1 x^{-2/3}\,dx$, $\int_1^\infty x^{-1/2}\,dx$, $\int_0^\infty \frac{dx}{1 + x^2}$.

> [!success]- Solution
> Converges to 3 ($p = 2/3 < 1$ near 0). Diverges ($p = 1/2 \le 1$ at infinity). Converges to $\pi/2$ ($\arctan t \to \pi/2$).

> [!question] Exercise 3 (L2)
> Find $c$ such that $f(x) = c\,e^{-\lvert x \rvert}$ is a density on $\mathbb{R}$, then compute its mean and variance.

> [!success]- Solution
> $\int_{-\infty}^\infty e^{-\lvert x \rvert} = 2\int_0^\infty e^{-x} = 2$, so $c = \frac12$ (the Laplace density). The mean is 0: $\int \lvert x \rvert f$ converges and $x f(x)$ is odd. $E[X^2] = \int_0^\infty x^2 e^{-x}\,dx = \Gamma(3) = 2$ ([[Integration by Parts]]), so the variance is 2.

> [!question] Exercise 4 (L2)
> Show that $\int_2^\infty \frac{dx}{x\ln x}$ diverges, and explain why a computer would hardly notice.

> [!success]- Solution
> With $u = \ln x$, $du = dx/x$: $\int_{\ln 2}^{\ln t} \frac{du}{u} = \ln\ln t - \ln\ln 2 \to \infty$ ([[Integration by Substitution]]). But the growth is extremely slow: about 1.2 at $t = 10$, 3.0 at $t = 10^6$ and 3.7 at $t = 10^{12}$. Any truncated numerical integral looks stable.

> [!question] Exercise 5 (L2, Python)
> Draw $10^5$ standard Cauchy values as $\tan(\pi(U - \tfrac12))$ with $U$ uniform, and $10^5$ standard normal values (seed 2, Cauchy draws first). Print both running means after 100, 1000, 10,000 and 100,000 draws. Explain the difference.

> [!success]- Solution
> ```python
> import math, random
> random.seed(2)
> cauchy = [math.tan(math.pi * (random.random() - 0.5)) for _ in range(100_000)]
> normal = [random.gauss(0, 1) for _ in range(100_000)]
> for n in (100, 1000, 10_000, 100_000):
>     print(n, round(sum(cauchy[:n]) / n, 3), round(sum(normal[:n]) / n, 3))
> # 100 3.406 -0.189
> # 1000 0.669 0.035
> # 10000 -0.387 0.001
> # 100000 0.126 -0.002
> ```
>
> The normal running mean shrinks towards 0 like $1/\sqrt n$. The Cauchy running mean wanders, pushed around by occasional huge values: $\int \lvert x \rvert f(x)\,dx$ diverges, the mean does not exist, and the law of large numbers does not apply. In data, a ratio whose denominator can approach 0 behaves this way.

## Mastery checklist

- [ ] 1 Recognized: I can say what makes an integral improper (infinite range, unbounded integrand) and that it is a limit.
- [ ] 2 Understood: I can explain the $p$-test, why both tails must converge separately, and why $f \to 0$ is not enough.
- [ ] 3 Practiced: I can evaluate convergent improper integrals, decide convergence by comparison, and check values numerically with a bounded tail.
- [ ] 4 Applied: I can check that a model density normalizes and that its mean and variance exist before reporting them.
- [ ] 5 Explained: I can teach why $\int e^{-x^2/2}$ converges, why the Cauchy distribution has no mean, and what that implies for averaging heavy-tailed data.

## References

[^os2]: [[Calculus (OpenStax)]], Volume 2, techniques of integration (improper integrals over infinite intervals and of discontinuous integrands, the comparison theorem).
[^mit]: [[MIT 18.01SC - Single Variable Calculus]], integration part (improper integrals).
[^blitz5]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 5 "Continuous Random Variables" (PDFs integrate to 1, expectation of a continuous random variable, the normalizing constant $1/\sqrt{2\pi}$ of the normal density).
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the Cauchy distribution (ratio of independent standard normals, no mean) and of the law of large numbers.
