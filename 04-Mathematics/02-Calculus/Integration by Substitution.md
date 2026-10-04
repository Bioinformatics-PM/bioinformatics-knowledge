---
aliases:
  - u-Substitution
  - Substitution Rule
  - Change of Variable in an Integral
  - Changement de variable
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Differentiation Rules]]"
  - "[[Antiderivative]]"
  - "[[Fundamental Theorem of Calculus]]"
related:
  - "[[Integration by Parts]]"
  - "[[Normal Distribution]]"
  - "[[Transformation of Random Variables]]"
  - "[[Probability Density Function]]"
  - "[[Uniform Distribution]]"
  - "[[Logarithm]]"
  - "[[Jacobian Matrix]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Introduction to Probability (Blitzstein)]]"
---

# Integration by Substitution

> [!abstract]
> Substitution is the chain rule read backwards: renaming an inner expression $u = g(x)$ turns a tangled integral into a simple one, and in probability it is what lets one table of the standard normal serve every normal distribution.

## Definition

If $g$ is differentiable with continuous derivative on $[a, b]$ and $f$ is continuous on the range of $g$, then[^os1][^mit]

$$\int f\big(g(x)\big)\,g'(x)\,dx = \int f(u)\,du \Big|_{u = g(x)}, \qquad \int_a^b f\big(g(x)\big)\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du .$$

In differential notation: set $u = g(x)$, $du = g'(x)\,dx$.

## Why it matters

- **Standardizing.** Every probability for $X \sim \mathcal{N}(\mu, \sigma^2)$ reduces to the standard normal by $z = (x - \mu)/\sigma$: this is why z-scores and a single $\Phi$ function suffice ([[Normal Distribution]]).[^blitz5]
- **Log scales.** Expression, intensity and concentration data are analyzed on log scales; how a density changes when the axis is transformed is a substitution with its factor $g'$ ([[Transformation of Random Variables]]).[^blitz8]
- **Simulation.** Inverse-transform sampling, which turns uniform random numbers into draws from another distribution, is justified by a substitution (Exercise 5, [[Uniform Distribution]]).
- **Kinetics and growth.** Integrals such as $\int e^{-kt}\,dt$, $\int \frac{N'}{N}\,dt = \ln N$ appear every time a rate equation is solved ([[Separable Differential Equation]]).

## Core (L1)

**Why it works.** By the chain rule, $\frac{d}{dx} F(g(x)) = F'(g(x))\,g'(x)$. So if $F' = f$, then $F(g(x))$ is an antiderivative of $f(g(x))\,g'(x)$.[^os1]

**Recipe.**

1. Spot an inner function $u = g(x)$ whose derivative $g'(x)$ also appears (up to a constant factor).
2. Write $du = g'(x)\,dx$ and rewrite the whole integrand in $u$; no $x$ may remain.
3. Integrate in $u$.
4. Indefinite integral: substitute back $u = g(x)$. Definite integral: change the limits to $g(a)$ and $g(b)$ instead.

**Examples.**

| Integral | Substitution | Result |
|---|---|---|
| $\int 2x\,e^{x^2}\,dx$ | $u = x^2$, $du = 2x\,dx$ | $e^{x^2} + C$ |
| $\int x\,e^{-x^2/2}\,dx$ | $u = -x^2/2$, $du = -x\,dx$ | $-e^{-x^2/2} + C$ |
| $\int \frac{\ln x}{x}\,dx$ | $u = \ln x$, $du = dx/x$ | $\frac{(\ln x)^2}{2} + C$ |
| $\int \frac{f'(x)}{f(x)}\,dx$ | $u = f(x)$ | $\ln\lvert f(x) \rvert + C$ |
| $\int_0^1 x(1 + x^2)^3\,dx$ | $u = 1 + x^2$, limits $1 \to 2$ | $\frac12 \int_1^2 u^3\,du = \frac{15}{8}$ |

The second line is why the standard normal has mean 0: the antiderivative $-e^{-x^2/2}$ takes the same value (0) at $-\infty$ and $+\infty$, so $\int_{-\infty}^{\infty} x\,e^{-x^2/2}\,dx = 0$ ([[Improper Integral]]). The fourth is the logarithmic derivative: integrating a per-capita growth rate $N'/N$ gives $\ln N$.

**Linear substitution.** $\int f(ax + b)\,dx = \frac{1}{a} F(ax + b) + C$ for $a \neq 0$: shifting does nothing to the area, stretching the axis by $a$ divides it by $a$.

## Deeper (L2)

### Standardizing a normal variable

Let $X \sim \mathcal{N}(\mu, \sigma^2)$ with density $\frac{1}{\sigma\sqrt{2\pi}} e^{-(x - \mu)^2/(2\sigma^2)}$. With $z = (x - \mu)/\sigma$, $dx = \sigma\,dz$, the factor $\sigma$ cancels and

$$P(a \le X \le b) = \int_a^b \frac{e^{-(x-\mu)^2/(2\sigma^2)}}{\sigma\sqrt{2\pi}}\,dx = \int_{(a-\mu)/\sigma}^{(b-\mu)/\sigma} \frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz = \Phi\!\left(\frac{b - \mu}{\sigma}\right) - \Phi\!\left(\frac{a - \mu}{\sigma}\right).$$

For a gene whose log2 expression is modeled as $\mathcal{N}(8, 0.5^2)$ (invented), $P(X > 9) = 1 - \Phi(2) \approx 0.0228$.[^blitz5]

### Log-transforming a density

Let $X > 0$ be an intensity whose natural log $Y = \ln X$ is $\mathcal{N}(\mu, \sigma^2)$. For $0 < c < d$, $P(c \le X \le d) = P(\ln c \le Y \le \ln d) = \int_{\ln c}^{\ln d} f_Y(y)\,dy$. Substituting $y = \ln x$, $dy = dx/x$:

$$P(c \le X \le d) = \int_c^d f_Y(\ln x)\,\frac{1}{x}\,dx, \qquad\text{so}\qquad f_X(x) = \frac{1}{x\sigma\sqrt{2\pi}}\, e^{-(\ln x - \mu)^2/(2\sigma^2)} .$$

This is the **log-normal** density.[^blitz8] The factor $1/x$ is the substitution's $g'$: probabilities are preserved, density values are not. The same reasoning on the log2 scale, and its consequences for means and modes, is in [[Probability Density Function#Changing variables]].

### Beyond one dimension

In two or more variables, $g'(x)$ becomes the absolute determinant of the [[Jacobian Matrix]]. Polar coordinates ($dx\,dy = r\,dr\,d\theta$) are the classic case: they compute $\int e^{-x^2/2}\,dx = \sqrt{2\pi}$ ([[Multiple Integral]], [[Improper Integral]]).

## Mathematical representation

- **Rule.** $\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$, valid for any $C^1$ function $g$, monotone or not.[^os1]
- **Densities.** If $X$ has density $f_X$ and $Y = g(X)$ with $g$ strictly monotone and differentiable, $h = g^{-1}$, then $f_Y(y) = f_X(h(y))\,\lvert h'(y) \rvert$ on the range of $g$.[^blitz8] The absolute value appears because a decreasing $g$ reverses the limits.

## Computational representation

Numerically, a substitution never changes the value of an integral; it changes how hard it is to compute (a smoother or bounded integrand, a finite range). The checks below compare midpoint sums with the closed forms obtained by substitution.

```python
import math

def midpoint(f, a: float, b: float, n: int = 100_000) -> float:
    """Midpoint Riemann sum of f on [a, b]."""
    dx = (b - a) / n
    return dx * sum(f(a + (i + 0.5) * dx) for i in range(n))

# 1. definite substitution u = 1 + x^2: integral of x (1 + x^2)^3 on [0, 1] equals 15/8
print(round(midpoint(lambda x: x * (1 + x * x) ** 3, 0, 1), 8), 15 / 8)

# 2. standardizing: log2 expression X ~ N(8, 0.5^2) (invented); P(X > 9) = 1 - Phi(2)
mu, sigma = 8.0, 0.5
f_X = lambda x: math.exp(-((x - mu) / sigma) ** 2 / 2) / (sigma * math.sqrt(2 * math.pi))
Phi = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))
print(round(midpoint(f_X, 9, 14), 6), round(1 - Phi((9 - mu) / sigma), 6))

# 3. log-normal density obtained by substitution from Y = ln X ~ N(6, 1)
m, s = 6.0, 1.0
f_LN = lambda x: math.exp(-((math.log(x) - m) / s) ** 2 / 2) / (x * s * math.sqrt(2 * math.pi))
print(round(midpoint(f_LN, 1e-9, math.exp(m + 8 * s), 10**6), 5))   # total area
print(round(midpoint(f_LN, 1e-9, math.exp(m), 10**5), 5))           # P(X <= e^m)
```

Output:

```text
1.875 1.875
0.02275 0.02275
1.0
0.5
```

The log-normal density integrates to 1 and puts half its mass below $e^{\mu}$, the image of the normal median: quantiles follow the substitution.

## Worked example

> [!example] Fragment lengths of a sequencing library (invented model)
> Insert sizes are modeled as $X \sim \mathcal{N}(350, 50^2)$ bp. What fraction falls between 300 and 450 bp?
>
> 1. **Substitute** $z = (x - 350)/50$, $dx = 50\,dz$. Limits: $x = 300 \mapsto z = -1$, $x = 450 \mapsto z = 2$.
> 2. **Rewrite.** $\int_{300}^{450} \frac{e^{-(x-350)^2/5000}}{50\sqrt{2\pi}}\,dx = \int_{-1}^{2} \frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz$.
> 3. **Evaluate.** $\Phi(2) - \Phi(-1) \approx 0.9772 - 0.1587 = 0.8186$.
> 4. **Read.** About 82 % of fragments are in range. The answer depends on $(a - \mu)/\sigma$ and $(b - \mu)/\sigma$ only, which is why one table of $\Phi$ serves every normal.

## Common misconceptions

> [!warning] Keeping the old limits
> After substituting in a definite integral, the limits must be in $u$: $\int_0^1 x(1 + x^2)^3\,dx \neq \frac12 \int_0^1 u^3\,du$. Either change the limits or substitute back before evaluating.

> [!warning] Transforming a density without the factor
> If $Y = \ln X$, the density of $X$ is **not** $f_Y(\ln x)$: it is $f_Y(\ln x)/x$. Omitting the factor gives a curve whose area is not 1 and whose peak is in the wrong place.

> [!warning] Applying the density formula to a non-monotone map
> The integral rule holds for any smooth $g$, but $f_Y = f_X(h)\,\lvert h' \rvert$ needs $g$ one-to-one. For $Y = X^2$ with $X$ normal, the two branches $x = \pm\sqrt{y}$ both contribute, and their densities must be added.

## Exercises

> [!question] Exercise 1 (L1)
> Compute $\int \frac{3x^2}{1 + x^3}\,dx$ and $\int_0^{\ln 2} e^{2x}\,dx$.

> [!success]- Solution
> $u = 1 + x^3$, $du = 3x^2\,dx$: $\ln\lvert 1 + x^3 \rvert + C$. Second: $u = 2x$, limits $0 \to 2\ln 2$: $\frac12 \int_0^{2\ln 2} e^u\,du = \frac12(4 - 1) = \frac32$.

> [!question] Exercise 2 (L1)
> Compute $\int_0^2 x\,e^{-x^2/2}\,dx$.

> [!success]- Solution
> $u = x^2/2$, $du = x\,dx$, limits $0 \to 2$: $\int_0^2 e^{-u}\,du = 1 - e^{-2} \approx 0.865$.

> [!question] Exercise 3 (L2)
> A gene's log2 expression is modeled as $\mathcal{N}(8, 0.5^2)$ (invented). Express $P(7.5 \le X \le 9)$ with $\Phi$ and evaluate it.

> [!success]- Solution
> $z$-limits $(7.5 - 8)/0.5 = -1$ and $(9 - 8)/0.5 = 2$: $\Phi(2) - \Phi(-1) \approx 0.8186$, the same number as the worked example, because only the standardized limits matter.

> [!question] Exercise 4 (L2)
> Starting from $T$ with density $\lambda e^{-\lambda t}$ ($t$ in minutes), find the density of the same time measured in hours, $H = T/60$. Check that it integrates to 1.

> [!success]- Solution
> $h(y) = 60y$, $h'(y) = 60$: $f_H(y) = 60\lambda e^{-60\lambda y}$, an exponential with rate $60\lambda$ per hour. $\int_0^\infty 60\lambda e^{-60\lambda y}\,dy = 1$ by the substitution $u = 60\lambda y$. A change of units rescales the density so that areas are preserved.

> [!question] Exercise 5 (L2, Python)
> Let $U$ be uniform on $(0, 1]$ and $Y = -\ln U$. Use the density formula to find $f_Y$, then check by simulation (seed 1, $10^5$ draws) the mean of $Y$ and $P(Y > 2)$.

> [!success]- Solution
> $g(u) = -\ln u$ is decreasing, $h(y) = e^{-y}$, $\lvert h'(y) \rvert = e^{-y}$, and $f_U = 1$ on $(0, 1]$, so $f_Y(y) = e^{-y}$ for $y \ge 0$: an exponential with rate 1, mean 1 and $P(Y > 2) = e^{-2} \approx 0.135$.
>
> ```python
> import math, random
> random.seed(1)
> ys = [-math.log(1.0 - random.random()) for _ in range(100_000)]   # 1 - random() is in (0, 1]
> print(round(sum(ys) / len(ys), 3), round(sum(y > 2 for y in ys) / len(ys), 4), round(math.exp(-2), 4))
> # 1.004 0.1372 0.1353
> ```
>
> The simulation agrees up to sampling noise. This is inverse-transform sampling: $-\ln(U)/\lambda$ draws exponential waiting times from uniform random numbers ([[Uniform Distribution]], [[Cumulative Distribution Function]]).

## Mastery checklist

- [ ] 1 Recognized: I can say that substitution reverses the chain rule and write $du = g'(x)\,dx$.
- [ ] 2 Understood: I can explain why the limits change in a definite integral and why a transformed density picks up the factor $\lvert h' \rvert$.
- [ ] 3 Practiced: I can choose $u$ for standard integrals, standardize any normal probability, and check results numerically.
- [ ] 4 Applied: I can derive the density of a log-transformed or rescaled measurement and use z-scores on real expression or insert-size data.
- [ ] 5 Explained: I can teach the link between substitution, the change-of-variables formula for densities, inverse-transform sampling and the Jacobian in several dimensions.

## References

[^os1]: [[Calculus (OpenStax)]], Volume 1, integration (substitution for indefinite and definite integrals).
[^mit]: [[MIT 18.01SC - Single Variable Calculus]], integration part (change of variables).
[^blitz5]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 5 "Continuous Random Variables" (the normal distribution and standardization).
[^blitz8]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 8 "Transformations" (change of variables for densities, the log-normal example).
