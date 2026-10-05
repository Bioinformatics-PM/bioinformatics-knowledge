---
aliases:
  - Continuous Function
  - Intermediate Value Theorem
  - IVT
  - Continuité
  - Théorème des valeurs intermédiaires
tags:
  - type/concept
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Limit]]"
  - "[[Function]]"
related:
  - "[[Derivative]]"
  - "[[Extremum]]"
  - "[[Root Finding]]"
  - "[[Fixed Point]]"
  - "[[Phase Line]]"
  - "[[Bistability]]"
  - "[[Cumulative Distribution Function]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Nonlinear Dynamics and Chaos (Strogatz)]]"
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[Lander 1988 - Genomic Mapping by Fingerprinting Random Clones]]"
---

# Continuity

> [!abstract]
> A function is continuous when small changes of the input give small changes of the output, with no jumps or holes; then, by the intermediate value theorem, a function that goes from positive to negative must cross zero somewhere in between.

## Definition

A function $f$ is **continuous at $a$** if three conditions hold: $f(a)$ is defined, $\lim_{x \to a} f(x)$ exists, and the two are equal, $\lim_{x\to a} f(x) = f(a)$. It is continuous on an interval if it is continuous at every point of it (with one-sided limits at closed endpoints).[^calc1][^1801]

**Intermediate value theorem (IVT).** If $f$ is continuous on the closed interval $[a, b]$ and $N$ is any number between $f(a)$ and $f(b)$, then there is at least one $c \in (a, b)$ with $f(c) = N$. In particular, if $f(a)$ and $f(b)$ have opposite signs, $f$ has a root in $(a, b)$.[^calc1]

## Why it matters

- **Steady states exist.** In a model $dx/dt = g(x)$, a steady state ([[Fixed Point]]) is a concentration $x^*$ with $g(x^*) = 0$.[^strogatz] If the net rate is positive at a low concentration and negative at a high one, the IVT guarantees a steady state between them, without solving anything.
- **Guaranteed root finding.** Bisection, the most robust method of [[Root Finding]], is the IVT turned into an algorithm: it is how one solves "which coverage leaves 0.1 % of the genome uncovered?" or a likelihood equation when no formula exists.
- **Discontinuous data.** Thresholds (a p-value cutoff, a quality filter) and the [[Cumulative Distribution Function]] of a count are step functions; there the IVT fails, and "the value at which exactly 5 % ..." may not exist.
- **Prerequisite of the big theorems.** Continuity on a closed interval guarantees a maximum and a minimum ([[Extremum]]); the mean value theorem behind [[Derivative]] and [[Integral]] needs it too.

## Core (L1)

**Three ways to fail.** At a point $a$, continuity can break in three ways:[^calc1]

| Discontinuity | What fails | Example at $a$ |
|---|---|---|
| removable | the limit exists but differs from $f(a)$, or $f(a)$ is undefined | $\frac{x^2 - 1}{x - 1}$ at 1 (limit 2, value undefined) |
| jump | the one-sided limits exist but differ | a threshold rule: 0 below a cutoff, 1 at and above it |
| infinite | a one-sided limit is infinite | $1/x$ at 0 |

A removable discontinuity is repaired by (re)defining $f(a)$ as the limit.

**Which functions are continuous.** Polynomials are continuous everywhere; rational functions wherever the denominator is not zero; $e^x$ everywhere; $\ln x$ on $(0, \infty)$. Sums, products, quotients (where defined) and compositions of continuous functions are continuous.[^calc1] So most formulas met in models are continuous on their domain, and their limits are computed by substitution ([[Limit]]).

**The IVT in a picture.** A continuous curve that starts above the axis and ends below it must cross it; a function with a jump can skip zero.

![[intermediate-value-theorem-root.svg]]

**Bio: a steady state between two concentrations.** Consider a protein that represses its own production (an invented toy model in arbitrary units): production $\frac{2}{1 + x^2}$ falls as the concentration $x$ rises, degradation is $x$, and

$$\frac{dx}{dt} = g(x) = \frac{2}{1 + x^2} - x .$$

$g$ is continuous on $[0, 3]$, $g(0) = 2 > 0$ (net production at low concentration) and $g(3) = 0.2 - 3 = -2.8 < 0$ (net degradation at high concentration). By the IVT there is a steady state $x^* \in (0, 3)$. Here one can check $x^* = 1$ exactly ($g(1) = 1 - 1 = 0$), but the argument works for any continuous production and degradation curves with these signs, including measured ones.

## Deeper (L2)

**ε-δ form.** $f$ is continuous at $a$ when for every $\varepsilon > 0$ there is $\delta > 0$ with $|x - a| < \delta \Rightarrow |f(x) - f(a)| < \varepsilon$: the limit definition with $L = f(a)$ and $x = a$ allowed.[^calc1] Read it as a tolerance contract: any output tolerance can be met by a small enough input tolerance.

**Why the IVT needs the real numbers.** Over the rationals, $x^2 - 2$ is negative at 1 and positive at 2 but never zero, because $\sqrt 2$ is irrational.[^lehman] The IVT rests on the completeness of $\mathbb{R}$, the same property behind the monotone convergence theorem in [[Limit]].

**Bisection: the IVT as an algorithm.** Keep an interval $[a, b]$ with a sign change; evaluate at the midpoint $m$; keep the half that still has a sign change. Each step halves the interval, so after $k$ steps a root is known within $(b - a)/2^k$, and reaching a tolerance $\tau$ needs

$$k = \left\lceil \log_2 \frac{b - a}{\tau} \right\rceil \text{ steps,}$$

whatever $f$ looks like. Bisection never fails on a valid bracket, but gains only one binary digit per step; Newton's method ([[Newton's Method]], [[Linear Approximation]]) is much faster near a root and can diverge far from it.

**Existence, not uniqueness.** The IVT says *at least one* root. In the toy model, uniqueness comes from monotonicity: production $\frac{2}{1 + x^2}$ decreases and $-x$ decreases for $x > 0$, so $g$ is strictly decreasing and crosses zero once (a statement the sign of the [[Derivative]] makes routine).

**Extreme value theorem.** A function continuous on a closed bounded interval $[a, b]$ attains a largest and a smallest value there.[^calc1] On an open interval or with a jump, it may not: $1/x$ on $(0, 1]$ has no maximum. This is the existence result behind the search for maxima in [[Extremum]].

## Advanced (L3)

**Counting and classifying steady states.** A gene that activates its own production can have several steady states. Toy model (invented parameters): $h(x) = 0.02 + \frac{x^2}{1 + x^2} - 0.45\,x$. A grid scan of $[0, 3]$ finds three sign changes, and bisection refines them to $x^* \approx 0.0500,\ 0.5259,\ 1.6908$ (code below). For $dx/dt = h(x)$, a root where $h$ goes from $+$ to $-$ as $x$ increases attracts nearby trajectories (stable), and a root where it goes from $-$ to $+$ repels them (unstable): this is the [[Phase Line]] analysis of one-dimensional flows.[^strogatz] Here the low and high states are stable and the middle one unstable: two stable expression levels, the signature of [[Bistability]].

**What a grid scan cannot see.** A sign change between grid points certifies a root; the absence of a sign change certifies nothing, since two close roots (or a root where $h$ touches zero without crossing) leave no trace. Turning a scan into a proof needs extra information, for example a bound $|h'(x)| \le M$: then $h$ cannot vanish within $|h(x_i)|/M$ of a grid point $x_i$ (by the mean value theorem, see [[Derivative]]).

**Continuity of models versus data.** Continuity is a modeling choice. A cell count, a read depth or a CDF of a discrete variable is a step function; treating it as continuous (for differentiation, root finding or interpolation of quantiles) is an approximation whose validity depends on the scale of the jumps relative to the quantities of interest.

## Mathematical representation

- Continuity at $a$: $\ \forall \varepsilon > 0\ \exists \delta > 0\ \forall x:\ |x - a| < \delta \Rightarrow |f(x) - f(a)| < \varepsilon$; equivalently $\lim_{x\to a} f(x) = f(a)$.
- IVT: $f \in C([a, b])$ and $\min(f(a), f(b)) \le N \le \max(f(a), f(b))$ $\Rightarrow \exists c \in [a, b]: f(c) = N$. Here $C([a, b])$ denotes the set of functions continuous on $[a, b]$.
- Root corollary: $f \in C([a, b])$ and $f(a)\,f(b) < 0 \Rightarrow \exists c \in (a, b): f(c) = 0$.
- Bisection: intervals $[a_k, b_k]$ with $b_k - a_k = (b - a)/2^k$, nested, each with a sign change; the midpoints converge to a root $c$ with $|m_k - c| \le (b - a)/2^{k+1}$.
- Steady state of $\dot x = g(x)$: $x^*$ with $g(x^*) = 0$; for continuous $g$, $g(x_{\text{low}}) > 0 > g(x_{\text{high}})$ implies a steady state in $(x_{\text{low}}, x_{\text{high}})$.

## Computational representation

Bisection only needs to evaluate $g$ and compare signs. Comparing signs (rather than testing $g(a)\,g(m) < 0$) avoids underflow of the product when both values are tiny.

```python
import math
from typing import Callable

def bisect(g: Callable[[float], float], a: float, b: float, tol: float = 1e-10) -> tuple[float, int]:
    """Root of a continuous g on [a, b] with g(a), g(b) of opposite signs (IVT guarantee)."""
    ga, gb = g(a), g(b)
    if ga == 0 or gb == 0:
        return (a if ga == 0 else b), 0
    if (ga < 0) == (gb < 0):
        raise ValueError("g(a) and g(b) have the same sign: no guarantee")
    steps = 0
    while b - a > tol:
        m = (a + b) / 2
        gm = g(m)
        if gm == 0:
            return m, steps
        if (gm < 0) == (ga < 0):
            a, ga = m, gm        # the sign change is in [m, b]
        else:
            b = m                # the sign change is in [a, m]
        steps += 1
    return (a + b) / 2, steps

# Toy negative autoregulation (invented units): production 2/(1 + x^2), degradation x
g = lambda x: 2 / (1 + x * x) - x
print(g(0.0), round(g(3.0), 3))
root, steps = bisect(g, 0.0, 3.0)
print(f"steady state x* = {root:.10f} after {steps} halvings; bound {math.ceil(math.log2(3 / 1e-10))}")

# Toy positive autoregulation (invented units): basal 0.02, activation x^2/(1 + x^2), degradation 0.45 x
h = lambda x: 0.02 + x * x / (1 + x * x) - 0.45 * x
grid = [i / 100 for i in range(0, 301)]
brackets = [(u, v) for u, v in zip(grid, grid[1:]) if (h(u) < 0) != (h(v) < 0)]
print(brackets)
print([f"{bisect(h, u, v)[0]:.4f}" for u, v in brackets])
```

```text
2.0 -2.8
steady state x* = 1.0000000000 after 35 halvings; bound 35
[(0.04, 0.05), (0.52, 0.53), (1.69, 1.7)]
['0.0500', '0.5259', '1.6908']
```

The step count matches the formula: $\lceil \log_2(3 / 10^{-10}) \rceil = 35$. `scipy.optimize.brentq` combines this bracketing guarantee with faster interpolation steps ([[Root Finding]]).

## Worked example

> [!example] Proving a steady state exists, then locating it
> Toy model (invented): $\frac{dx}{dt} = g(x) = \frac{2}{1 + x^2} - x$, with $x$ a protein concentration in arbitrary units.
>
> 1. **Continuity.** $1 + x^2 \ge 1$ never vanishes, so $\frac{2}{1 + x^2}$ is a continuous rational function; subtracting the polynomial $x$ keeps continuity on $[0, 3]$.
> 2. **Signs at the ends.** $g(0) = 2 > 0$ and $g(3) = -2.8 < 0$.
> 3. **IVT.** There is $x^* \in (0, 3)$ with $g(x^*) = 0$: a steady state exists.
> 4. **Uniqueness.** For $x \ge 0$, both $\frac{2}{1 + x^2}$ and $-x$ decrease, so $g$ is strictly decreasing and has exactly one root.
> 5. **Location.** Bisection on $[0, 3]$ returns $x^* = 1.0000000000$ after 35 halvings, and indeed $g(1) = 0$.
> 6. **Stability.** $g > 0$ below $x^*$ (concentration rises) and $g < 0$ above (it falls): trajectories converge to $x^* = 1$, a stable steady state ([[Phase Line]]).

## Common misconceptions

> [!warning] "A sign change always means a root"
> Only for a continuous function. $1/x$ is negative at $-1$ and positive at $1$ and never zero; the jump of the figure skips zero too. Check continuity on the whole closed interval first.

> [!warning] "No sign change means no root"
> The IVT is one-directional. $x^2 - 0.01$ is positive at $-1$ and at $1$ but has two roots in between. Grid scans and bisection miss roots that do not produce a sign change.

> [!warning] "The IVT finds the root"
> It proves existence and says nothing about uniqueness or location. Uniqueness needs another argument (monotonicity), and location needs an algorithm (bisection).

> [!warning] "Continuous means smooth"
> $|x|$ is continuous but has a corner at 0, where it has no derivative ([[Derivative]]). Continuity forbids jumps, not corners.

## Exercises

> [!question] Exercise 1 (L1)
> Where is $f(x) = \frac{x^2 - 4}{x - 2}$ continuous? Classify its discontinuity and repair it.

> [!success]- Solution
> $f$ is a rational function, continuous wherever $x \neq 2$. At 2 it is undefined, but $f(x) = x + 2$ for $x \neq 2$, so $\lim_{x\to2} f(x) = 4$: a removable discontinuity. Defining $f(2) = 4$ makes $f$ continuous everywhere (it becomes $x + 2$).

> [!question] Exercise 2 (L1)
> Show that $x^3 + x - 3 = 0$ has a solution between 1 and 2.

> [!success]- Solution
> $p(x) = x^3 + x - 3$ is a polynomial, hence continuous on $[1, 2]$. $p(1) = -1 < 0$ and $p(2) = 7 > 0$, so by the IVT there is $c \in (1, 2)$ with $p(c) = 0$. (It is unique: $p$ is strictly increasing.)

> [!question] Exercise 3 (L2)
> For a self-repressing protein with production $\frac{\beta}{1 + x^2}$ and degradation $\gamma x$ ($\beta, \gamma > 0$), prove that $\frac{dx}{dt} = \frac{\beta}{1 + x^2} - \gamma x$ has exactly one steady state, and that it lies in $(0, \beta/\gamma)$.

> [!success]- Solution
> $g(x) = \frac{\beta}{1 + x^2} - \gamma x$ is continuous. $g(0) = \beta > 0$ and $g(\beta/\gamma) = \frac{\beta}{1 + (\beta/\gamma)^2} - \beta < 0$ because the fraction is smaller than $\beta$. By the IVT a root lies in $(0, \beta/\gamma)$. For $x \ge 0$ both terms decrease, one strictly, so $g$ is strictly decreasing and the root is unique. Biological reading: the steady state can never exceed the level $\beta/\gamma$ reached with full, unrepressed production.

> [!question] Exercise 4 (L2, Python)
> Under the Poisson coverage model, a fraction $e^{-c}$ of the genome receives no read at mean coverage $c$.[^lw] Use `bisect` to find the coverage that leaves 0.1 % uncovered, and compare with the closed form.

> [!success]- Solution
> Solve $e^{-c} - 0.001 = 0$ on $[0, 20]$: the function is continuous, positive at 0 ($0.999$) and negative at 20.
>
> ```python
> cov = lambda c: math.exp(-c) - 0.001     # uncovered fraction minus target
> c, _ = bisect(cov, 0.0, 20.0, tol=1e-9)
> print(round(c, 4), round(math.log(1000), 4))
> # 6.9078 6.9078
> ```
>
> Both give $c = \ln 1000 \approx 6.91$. The closed form exists here; bisection is what you use when the model (for instance with uneven coverage) has none.

> [!question] Exercise 5 (L3)
> For the positive-autoregulation toy model $h(x) = 0.02 + \frac{x^2}{1 + x^2} - 0.45\,x$, use the signs of $h$ between the three roots found above to classify each steady state. Why can the grid scan alone not prove that there are exactly three?

> [!success]- Solution
> $h(0) = 0.02 > 0$; $h < 0$ on $(0.0500, 0.5259)$; $h > 0$ on $(0.5259, 1.6908)$; $h < 0$ beyond $1.6908$ (for large $x$, $-0.45x$ dominates). Roots where the sign goes $+ \to -$ are stable: $0.0500$ and $1.6908$; the root at $0.5259$ ($- \to +$) is unstable and separates the two basins: the system is bistable. The scan only proves *at least* three roots: two roots between neighbouring grid points would cancel their sign changes. Exactly three follows algebraically: $h(x) = 0$ multiplied by $1 + x^2$ is a cubic, which has at most three real roots.

## Mastery checklist

- [ ] 1 Recognized: I can state the three conditions for continuity and the intermediate value theorem.
- [ ] 2 Understood: I can classify removable, jump and infinite discontinuities, and explain why a sign change forces a root only for continuous functions.
- [ ] 3 Practiced: I prove the existence of roots and steady states with the IVT and implement bisection with the correct step count.
- [ ] 4 Applied: I locate the steady states of a production-degradation model (toy or fitted) and classify them by the sign of the net rate.
- [ ] 5 Explained: I can teach why the IVT needs the real numbers, why it gives existence but not uniqueness, and what a grid scan can and cannot certify.

## References

[^calc1]: [[Calculus (OpenStax)]], Volume 1 (continuity: definition, types of discontinuities, continuity of elementary functions and their combinations, the intermediate value theorem; the extreme value theorem).
[^1801]: [[MIT 18.01SC - Single Variable Calculus]], differentiation part (limits and continuity).
[^strogatz]: [[Nonlinear Dynamics and Chaos (Strogatz)]], one-dimensional flows (fixed points of $\dot x = f(x)$ and their stability from the sign of $f$).
[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, proofs part (proof by contradiction that $\sqrt 2$ is irrational).
[^lw]: [[Lander 1988 - Genomic Mapping by Fingerprinting Random Clones]], Lander ES, Waterman MS, *Genomics* 2(3):231-239: clones placed at random along the genome; coverage (redundancy) and gaps as functions of it.
