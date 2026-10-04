---
aliases:
  - FTC
  - Newton-Leibniz Formula
  - Théorème fondamental de l'analyse
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Derivative]]"
  - "[[Antiderivative]]"
  - "[[Integral]]"
  - "[[Continuity]]"
related:
  - "[[Cumulative Distribution Function]]"
  - "[[Probability Density Function]]"
  - "[[Exponential Distribution]]"
  - "[[Integration by Substitution]]"
  - "[[Improper Integral]]"
  - "[[Quantile]]"
  - "[[Ordinary Differential Equation]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Introduction to Probability (Blitzstein)]]"
---

# Fundamental Theorem of Calculus

> [!abstract]
> Differentiation and integration undo each other: accumulating a rate and then taking the rate of the accumulated total gives back the original rate, so areas can be computed from antiderivatives instead of from infinitely many rectangles.

## Definition

Let $f$ be continuous on $[a, b]$.[^os1][^mit]

- **Part 1.** The accumulation function $G(x) = \int_a^x f(t)\,dt$ is differentiable on $(a, b)$ and $G'(x) = f(x)$.
- **Part 2 (evaluation).** If $F$ is any [[Antiderivative]] of $f$ on $[a, b]$, then $\int_a^b f(x)\,dx = F(b) - F(a)$, written $\big[F(x)\big]_a^b$.

## Why it matters

- **Closed-form areas.** A limit of [[Integral|Riemann sums]] becomes one subtraction whenever an antiderivative is known: the exact pharmacokinetic AUC, a normalizing constant, a moment of a distribution.
- **Density and CDF are two views of one object.** For a continuous random variable, the [[Cumulative Distribution Function]] is the accumulated density, $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$, and the density is its derivative, $f_X = F_X'$ wherever $f_X$ is continuous.[^blitz5] Software exploits both directions: `cdf` for probabilities of intervals, `pdf` for likelihoods.
- **Totals from rates.** The net change of any quantity is the integral of its rate (net change theorem), which is how cumulative production, growth or exposure is computed from a rate model.
- **Differential equations.** $y' = f(t)$ with $y(t_0) = y_0$ is solved by $y(t) = y_0 + \int_{t_0}^t f$: Part 1 guarantees a solution exists even when no formula does ([[Ordinary Differential Equation]]).

## Core (L1)

**Part 2: evaluate.** Find an antiderivative, subtract its values at the ends:

$$\int_0^2 x^2\,dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3}, \qquad \int_0^{12} e^{-0.25t}\,dt = \left[-4 e^{-0.25t}\right]_0^{12} = 4\,(1 - e^{-3}) \approx 3.80 .$$

The constant $C$ of the antiderivative cancels in the subtraction, which is why any antiderivative works.[^os1]

**Part 1: the accumulation function.** $G(x) = \int_a^x f$ is the area from $a$ up to a moving right edge. Moving the edge from $x$ to $x + h$ adds a thin strip of width $h$ and height close to $f(x)$, so

$$\frac{G(x + h) - G(x)}{h} \approx f(x) \quad\Longrightarrow\quad G'(x) = f(x).$$

The rate at which area accumulates equals the height of the curve at the edge.

```mermaid
flowchart LR
    f["rate or density f"] -- "integrate from a: G(x) = ∫ f" --> G["accumulated total or CDF G"]
    G -- "differentiate: G' = f" --> f
```

**Net change theorem.** Applying Part 2 to $F'$: $\int_a^b F'(t)\,dt = F(b) - F(a)$. The integral of a rate of change is the total change.[^os1]

**Bio: a CDF is the integral of its density.** If every mRNA molecule of a gene is degraded with the same constant probability per unit time $\lambda$, its lifetime $T$ has the exponential density $f(t) = \lambda e^{-\lambda t}$ for $t \ge 0$ ([[Exponential Distribution]]).[^blitz5] Part 2 gives its CDF in one line:

$$F(t) = \int_0^t \lambda e^{-\lambda s}\,ds = \left[-e^{-\lambda s}\right]_0^t = 1 - e^{-\lambda t},$$

and Part 1 confirms $F'(t) = \lambda e^{-\lambda t} = f(t)$ (Worked example).

## Deeper (L2)

**Variable limits.** Combining Part 1 with the chain rule, for differentiable $u$ and $v$:

$$\frac{d}{dx} \int_{v(x)}^{u(x)} f(t)\,dt = f\big(u(x)\big)\,u'(x) - f\big(v(x)\big)\,v'(x).$$

This is how the density of a transformed variable is obtained from its CDF: if $Y = e^X$, then $F_Y(y) = F_X(\ln y)$ and $f_Y(y) = f_X(\ln y) / y$ ([[Integration by Substitution]], [[Transformation of Random Variables]]).

**Quantiles.** If $F$ is a continuous, strictly increasing CDF with density $f$, its inverse $Q = F^{-1}$ (the [[Quantile]] function) has derivative $Q'(p) = 1 / f(Q(p))$, by differentiating $F(Q(p)) = p$. Where the density is low (the tails), quantiles move fast as $p$ changes, which is why extreme quantiles are hard to estimate.

**The hypotheses matter.**

- *Continuity of $f$ for Part 1.* For the uniform density on $[0, 1]$ (1 inside, 0 outside), $F$ has corners at 0 and 1: $F'$ exists and equals $f$ everywhere except at the two jumps of $f$. A density is only defined up to such points ([[Probability Density Function]]).
- *Continuity on the whole interval for Part 2.* Blindly, $\int_{-1}^{1} \frac{dx}{x^2} = \left[-\frac{1}{x}\right]_{-1}^{1} = -2$, a negative area for a positive function. The error: $1/x^2$ is not continuous (not even bounded) at 0, so the theorem does not apply; the integral is improper and diverges ([[Improper Integral]]).

## Mathematical representation

*Proof sketch of Part 1.* For $h > 0$, $G(x + h) - G(x) = \int_x^{x+h} f$. By the mean value theorem for integrals, this equals $h\, f(c_h)$ for some $c_h \in [x, x + h]$.[^os1] As $h \to 0$, $c_h \to x$ and continuity gives $f(c_h) \to f(x)$, so $G'(x) = f(x)$ ([[Limit]], [[Continuity]]).

*Part 2 from Part 1.* $G$ and $F$ are both antiderivatives of $f$, so $F = G + C$ on the interval. Then $F(b) - F(a) = G(b) - G(a) = \int_a^b f - 0$.

*For distributions.* $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$, $P(a < X \le b) = F_X(b) - F_X(a) = \int_a^b f_X$, and $F_X' = f_X$ at continuity points of $f_X$ ([[Cumulative Distribution Function]]).

## Computational representation

Numerically, Part 1 is a running sum: accumulate trapezoids along a grid to tabulate $G$; Part 2 is then a difference of two table entries, and a centred difference of $G$ gives back $f$. Libraries do the same (`numpy.cumsum`, `scipy.integrate.cumulative_trapezoid`; `numpy.gradient` for the reverse).

```python
import math

def cumulative_trapezoid(f, a: float, b: float, n: int):
    """Grid xs and G(x) = integral of f from a to x on that grid (trapezoid rule)."""
    dx = (b - a) / n
    xs = [a + i * dx for i in range(n + 1)]
    G = [0.0]
    for x0, x1 in zip(xs, xs[1:]):
        G.append(G[-1] + dx * (f(x0) + f(x1)) / 2)
    return xs, G

lam = math.log(2) / 30                        # invented mRNA half-life of 30 min
density = lambda t: lam * math.exp(-lam * t)  # exponential lifetime density
xs, G = cumulative_trapezoid(density, 0, 120, 1200)   # step 0.1 min
for t in (30, 60, 120):
    i = round(t / 0.1)
    print(t, f"{G[i]:.7f}", f"{1 - math.exp(-lam * t):.7f}")
i = 600                                       # t = 60: differentiate back
print(round((G[i + 1] - G[i - 1]) / (2 * 0.1), 6), round(density(60), 6))
```

Output:

```text
30 0.5000002 0.5000000
60 0.7500003 0.7500000
120 0.9375004 0.9375000
0.005776 0.005776
```

## Worked example

> [!example] Lifetime of an mRNA (invented half-life)
> Half-life 30 min, so $\lambda = \ln 2 / 30 \approx 0.0231$ per min.
>
> 1. **CDF from the density (Part 2).** $F(t) = 1 - e^{-\lambda t}$.
> 2. **Probabilities.** $P(T \le 30) = 1 - e^{-\ln 2} = 0.5$, as a half-life should give; $P(T \le 60) = 1 - \tfrac14 = 0.75$; $P(30 < T \le 60) = F(60) - F(30) = 0.25$.
> 3. **Back to the density (Part 1).** $F'(t) = \lambda e^{-\lambda t}$; at $t = 60$, $0.0231 \times 0.25 \approx 0.00578$ per min, the value the numerical derivative recovers above.
> 4. **Median.** $F(m) = 1/2$ gives $m = \ln 2 / \lambda = 30$ min: for an exponential lifetime, the median is the half-life ([[Quantile]]).

## Common misconceptions

> [!warning] "$\int_a^x f(t)\,dt$ is a number"
> With a variable upper limit it is a **function** of $x$. The integration variable $t$ is a dummy: $\int_a^x f(t)\,dt$ and $\int_a^x f(s)\,ds$ are the same function, while $\int_a^x f(x)\,dx$ mixes the two roles and should be avoided.

> [!warning] "Part 2 works whenever I can write an antiderivative"
> It needs $f$ continuous (more generally integrable with $F' = f$) on the **whole** closed interval. A singularity inside the interval, as in $\int_{-1}^{1} x^{-2}\,dx$, makes the formula produce nonsense.

> [!warning] "Every CDF has a density"
> Only CDFs of continuous variables with a density can be differentiated this way. The CDF of a count (a [[Poisson Distribution|Poisson]] read count) is a step function: its derivative is 0 between jumps and undefined at them.

## Exercises

> [!question] Exercise 1 (L1)
> Compute $\int_1^{e} \frac{1}{x}\,dx$ and $\int_0^{\pi} \sin x\,dx$.

> [!success]- Solution
> $\big[\ln x\big]_1^e = 1 - 0 = 1$. $\big[-\cos x\big]_0^\pi = -(-1) - (-1) = 2$.

> [!question] Exercise 2 (L1)
> Without computing any integral, find $\frac{d}{dx} \int_0^x e^{-t^2}\,dt$.

> [!success]- Solution
> By Part 1 it is $e^{-x^2}$. The integral itself has no elementary formula, but its derivative is immediate ([[Antiderivative]]).

> [!question] Exercise 3 (L2)
> A variable $X$ on $[0, 1]$ has density $f(x) = 2x$. Find its CDF, $P(X \le 0.5)$ and its median.

> [!success]- Solution
> $F(x) = \int_0^x 2t\,dt = x^2$ on $[0, 1]$ (0 before, 1 after). $P(X \le 0.5) = 0.25$. The median solves $m^2 = 1/2$: $m = \sqrt{0.5} \approx 0.707$.

> [!question] Exercise 4 (L2)
> Compute $\frac{d}{dx} \int_0^{x^2} \cos t\,dt$ in two ways: with the variable-limit rule, and by evaluating the integral first.

> [!success]- Solution
> Rule: $\cos(x^2) \cdot 2x$. Directly: $\int_0^{x^2} \cos t\,dt = \sin(x^2)$, whose derivative is $2x\cos(x^2)$. Both agree.

> [!question] Exercise 5 (L2, Python)
> With `cumulative_trapezoid`, tabulate $\int_{-8}^{x} \varphi$ for the standard normal density $\varphi$ on $[-8, 3]$ (step 0.001). Compare with $\Phi(x) = \tfrac12\big(1 + \operatorname{erf}(x/\sqrt2)\big)$ over the whole grid, then recover $\varphi(1)$ by a centred difference. Why can the lower limit be $-8$ instead of $-\infty$?

> [!success]- Solution
> ```python
> phi = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
> Phi = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))
> xs, G = cumulative_trapezoid(phi, -8, 3, 11000)
> print(f"{max(abs(g - Phi(x)) for x, g in zip(xs, G)):.1e}")      # 2.0e-08
> i = 9000                                                          # xs[i] = 1.0
> print(round(G[i], 6), round(Phi(1.0), 6))                         # 0.841345 0.841345
> print(round((G[i + 1] - G[i - 1]) / 0.002, 6), round(phi(1.0), 6))  # 0.241971 0.241971
> ```
>
> Accumulating the density reproduces $\Phi$ (Part 1) and differencing it returns $\varphi$. The area below $-8$ is $\Phi(-8) \approx 6 \times 10^{-16}$, negligible at this precision; in general the neglected tail must be bounded ([[Improper Integral]]).

## Mastery checklist

- [ ] 1 Recognized: I can state both parts of the theorem.
- [ ] 2 Understood: I can explain with the thin-strip argument why the accumulated area has derivative $f$, and why the constant of an antiderivative cancels.
- [ ] 3 Practiced: I can evaluate integrals with antiderivatives, differentiate integrals with variable limits, and tabulate a CDF numerically in Python.
- [ ] 4 Applied: I can move between density and CDF for a real model (mRNA lifetimes, waiting times) and compute probabilities of intervals.
- [ ] 5 Explained: I can teach which hypotheses the theorem needs, with counterexamples (the $1/x^2$ paradox, densities with jumps, discrete CDFs).

## References

[^os1]: [[Calculus (OpenStax)]], Volume 1, integration (the fundamental theorem of calculus, the mean value theorem for integrals, the net change theorem).
[^mit]: [[MIT 18.01SC - Single Variable Calculus]], integration part (first and second fundamental theorems).
[^blitz5]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 5 "Continuous Random Variables" (CDF as the integral of the PDF and PDF as the derivative of the CDF; the exponential distribution).
