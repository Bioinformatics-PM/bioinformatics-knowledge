---
aliases:
  - Linearization
  - Tangent Line Approximation
  - Differential
  - Error Propagation
  - Propagation of Uncertainty
  - Approximation affine
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Derivative]]"
  - "[[Differentiation Rules]]"
related:
  - "[[Taylor Series]]"
  - "[[Newton's Method]]"
  - "[[Measurement Error]]"
  - "[[Rounding Error]]"
  - "[[Condition Number]]"
  - "[[Variance]]"
  - "[[Linear Stability Analysis]]"
  - "[[Quantitative Polymerase Chain Reaction]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]]"
  - "[[Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR]]"
  - "[[Cock 2010 - The Sanger FASTQ File Format]]"
---

# Linear Approximation

> [!abstract]
> Near a point, a differentiable function is almost a straight line: replacing $f$ by its tangent line gives simple approximations such as $\ln(1 + x) \approx x$, and tells how a measurement error propagates through a calculation.

## Definition

The **linear approximation** (linearization) of $f$ at $a$ is its tangent line

$$L(x) = f(a) + f'(a)(x - a),$$

and $f(x) \approx L(x)$ for $x$ near $a$. In differential form, a small change $dx$ of the input produces approximately the change $dy = f'(x)\,dx$ of the output; the **differential** $dy$ approximates the true change $\Delta y = f(x + dx) - f(x)$.[^calc1][^1801]

## Why it matters

- **Small-rate shortcuts.** $\ln(1 + r) \approx r$, $e^{-x} \approx 1 - x$ and $1 - (1 - \mu)^L \approx L\mu$ are used constantly with growth rates, error rates and mutation rates.
- **Error propagation.** How an uncertainty on a threshold cycle, a concentration or an error probability carries over to a fold change, a log ratio or a Phred score ([[Measurement Error]]).
- **Engine of other methods.** [[Newton's Method]] solves a linearized equation at each step; the delta method linearizes a transformation to get a variance; the stability of a steady state is read from the linearized dynamics ([[Linear Stability Analysis]]).
- **Numerics.** The regime where $\ln(1 + x) \approx x$ is exactly where naive floating-point formulas lose digits, which is why `log1p` and `expm1` exist ([[Rounding Error]]).

## Core (L1)

![[secant-tangent-slope.svg]]

*The tangent line (green) is the linear approximation at $a$; the red gap at $a + h$ is its error, which shrinks like $h^2$ (Deeper).*

**Standard linearizations at 0.** With $a = 0$, $L(x) = f(0) + f'(0)\,x$:

| $f(x)$ | $f(0)$ | $f'(0)$ | $L(x)$ |
|---|---:|---:|---|
| $e^x$ | 1 | 1 | $1 + x$ |
| $\ln(1 + x)$ | 0 | 1 | $x$ |
| $(1 + x)^k$ | 1 | $k$ | $1 + kx$ |
| $\sqrt{1 + x}$ | 1 | $1/2$ | $1 + x/2$ |
| $1/(1 + x)$ | 1 | $-1$ | $1 - x$ |

The code below shows their quality: errors near $5 \times 10^{-5}$ at $x = 0.01$, near $5 \times 10^{-3}$ at $x = 0.1$, and useless at $x = 0.5$ ($\ln 1.5 = 0.405$, not 0.5).

**Bio: small rates.** A population growing by a fraction $x$ per generation has the continuous rate $\ln(1 + x) \approx x$: 2 % per generation is $\ln 1.02 = 0.0198$ ([[Exponential Growth]]). In the same way, a log ratio is a relative change for small changes: $\ln\frac{x + \Delta}{x} = \ln\left(1 + \frac{\Delta}{x}\right) \approx \frac{\Delta}{x}$; for a doubling ($\Delta/x = 1$) it is $\ln 2 = 0.69$, not 1.

**Bio: at least one mutation.** If each of $L$ sites mutates independently with probability $\mu$, the probability of at least one mutation is $1 - (1 - \mu)^L$. Linearizing twice ($\ln(1 - \mu) \approx -\mu$, then $1 - e^{-L\mu} \approx L\mu$) gives $\approx L\mu$ when $L\mu$ is small. With the human rate $\mu = 1.2 \times 10^{-8}$ per site per generation[^kong] and a 1 Mb region, $L\mu = 0.0120$ against the exact $0.011928$.

**Propagating a measurement error.** If $x$ is measured with error $\Delta x$, then $\Delta y \approx f'(x)\,\Delta x$, and in relative terms[^calc1]

$$\frac{\Delta y}{y} \approx \frac{x f'(x)}{f(x)}\cdot\frac{\Delta x}{x}.$$

For $y = \log_2 x$, $\Delta y \approx \frac{\Delta x}{x\ln 2}$: a 10 % relative error on an intensity or a count becomes $\pm 0.144$ on the $\log_2$ scale, whatever the value of $x$ (simulation below: 0.146).

**qPCR fold changes.** The $2^{-\Delta\Delta C_T}$ method estimates relative expression as $F = 2^{-\Delta\Delta C_T}$, assuming efficiencies near 100 %.[^livak] Since $\frac{dF}{d(\Delta\Delta C_T)} = -F\ln 2$, an uncertainty $\delta$ on $\Delta\Delta C_T$ gives a relative uncertainty $\frac{\Delta F}{F} \approx 0.69\,\delta$: a quarter of a cycle is about 17 % on the fold change (Worked example; [[Quantitative Polymerase Chain Reaction]]).

## Deeper (L2)

**How large is the error?** If $|f''(t)| \le M$ for every $t$ between $a$ and $x$, then

$$|f(x) - L(x)| \le \frac{M}{2}(x - a)^2,$$

a consequence of Taylor's theorem with remainder ([[Taylor Series]]).[^calc2] The error is quadratic: halving the distance to $a$ divides the error bound by four. For $\ln(1 + x)$ on $[0, 0.1]$, $f''(t) = -\frac{1}{(1 + t)^2}$ so $M = 1$ and the bound is $0.005$; the actual error at $0.1$ is $0.00469$.

**Which side?** If $f'' < 0$ (concave) the tangent lies above the graph, if $f'' > 0$ (convex) below. Hence the exact inequalities $\ln(1 + x) \le x$ for $x > -1$ and $e^x \ge 1 + x$ for all $x$: the linear approximation of a log ratio always overstates it, and $L\mu$ always overstates the probability of at least one mutation. Knowing the direction of the bias is often as useful as its size.

**Relative error amplification.** The factor $\kappa(x) = \left|\frac{x f'(x)}{f(x)}\right|$ multiplies relative errors ([[Condition Number]]). For a power $y = x^k$, $\kappa = |k|$: a 5 % error on a radius is about 15 % on a volume. For $y = \ln x$, $\kappa = 1/|\ln x|$, large near $x = 1$, where a log is close to zero.

**When linearization fails.** (1) Far from $a$, compared with the scale on which $f'$ changes ($M$ large). (2) When $f'(a) = 0$: the linear term vanishes, the error is governed by the second-order term, and "linear error propagation" wrongly predicts no error at all. (3) When the interval matters: a nonlinear $f$ maps a symmetric input interval to an asymmetric one, so $\pm$ notation hides the shape (Worked example).

## Advanced (L3)

**The delta method.** For a random quantity $X$ with mean $\mu$ and small standard deviation $\sigma$, $g(X) \approx g(\mu) + g'(\mu)(X - \mu)$; since $\operatorname{Var}(a + bX) = b^2\operatorname{Var}(X)$,[^blitz4]

$$\operatorname{Var}\big(g(X)\big) \approx g'(\mu)^2\,\sigma^2 .$$

With $g = \ln$, $\operatorname{Var}(\ln X) \approx \sigma^2/\mu^2$: on the log scale, the variance is the squared coefficient of variation, which is why log-transformed intensities with constant relative error have constant variance. With $g = \sqrt{\ }$ on a Poisson count, the variance is about $1/4$ whatever the mean ([[Poisson Distribution#Advanced (L3)]]). One order further, $E[g(X)] \approx g(\mu) + \frac{1}{2}g''(\mu)\sigma^2$: since $\ln$ is concave, the mean of logs is below the log of the mean ([[Expected Value]]). The general version is in [[Taylor Series]].

**Newton's method: solving the linearization.** To solve $g(x) = 0$, replace $g$ by its tangent at the current guess $x_k$ and solve $L(x) = 0$:

$$x_{k+1} = x_k - \frac{g(x_k)}{g'(x_k)}.$$

On the self-repression model $g(x) = \frac{2}{1 + x^2} - x$ of [[Continuity]], starting at $x_0 = 2$, the errors are $2.1 \times 10^{-1}$, $9.3 \times 10^{-3}$, $2.2 \times 10^{-5}$, $1.2 \times 10^{-10}$ (Exercise 5): near the root the error is roughly squared at each step, against one binary digit per step for bisection. Far from a root, or where $g'$ is near zero, the tangent can send the iterate anywhere ([[Newton's Method]], [[Root Finding]]).

**Linearizing dynamics.** Near a steady state $x^*$ of $\dot x = g(x)$, the deviation $u = x - x^*$ obeys $\dot u \approx g'(x^*)\,u$, whose solutions $u(t) = u(0)\,e^{g'(x^*)t}$ decay if $g'(x^*) < 0$ and grow if $g'(x^*) > 0$. For the self-repression model, $g'(1) = -2$: perturbations decay with rate 2, so the steady state is stable ([[Linear Stability Analysis]]; with several variables, the [[Jacobian Matrix]]).

## Mathematical representation

- Linearization at $a$: $L_a(x) = f(a) + f'(a)(x - a)$; remainder $R_a(x) = f(x) - L_a(x)$ with $|R_a(x)| \le \frac{M}{2}(x - a)^2$, $M = \max |f''|$ between $a$ and $x$.
- Differential: $dy = f'(x)\,dx$, and $\Delta y = dy + R$ with $R/dx \to 0$ as $dx \to 0$.
- Error propagation: $\ \sigma_y \approx |f'(x)|\,\sigma_x$; $\ \frac{\sigma_y}{|y|} \approx \kappa(x)\frac{\sigma_x}{|x|}$, $\ \kappa(x) = \left|\frac{x f'(x)}{f(x)}\right|$.
- Products and powers, to first order: for $y = x_1x_2$, $\frac{\Delta y}{y} \approx \frac{\Delta x_1}{x_1} + \frac{\Delta x_2}{x_2}$; for $y = x^k$, $\frac{\Delta y}{y} \approx k\frac{\Delta x}{x}$.
- Delta method: $E[g(X)] \approx g(\mu)$, $\operatorname{Var}(g(X)) \approx g'(\mu)^2\sigma^2$.
- Newton step: $x_{k+1} = x_k - g(x_k)/g'(x_k)$.

## Computational representation

```python
import math
import random
import statistics

# Tangent-line approximations at 0 and their errors
print(" x      e^x vs 1+x        ln(1+x) vs x      sqrt(1+x) vs 1+x/2")
for x in (0.01, 0.1, 0.5):
    print(f"{x:<5} {math.exp(x):.5f} {1 + x:.5f}   {math.log1p(x):.5f} {x:.5f}   {math.sqrt(1 + x):.5f} {1 + x / 2:.5f}")

# Error bound for ln(1 + x) ~ x on [0, 0.1]: |f''| <= 1, so error <= x^2 / 2
x = 0.1
print(f"actual error {x - math.log1p(x):.5f}  bound {x * x / 2:.5f}")

# Where the approximation lives, naive formulas lose digits
u = 1e-10
print(math.log(1 + u), math.log1p(u))

# Probability of at least one new mutation in L sites, rate mu per site (Kong 2012 rate; L invented)
mu, L = 1.2e-8, 1_000_000
exact = -math.expm1(L * math.log1p(-mu))   # 1 - (1 - mu)^L, computed stably
print(f"exact {exact:.6f}  linear L*mu = {L * mu:.6f}")

# Error propagation through log2: 10 % relative error on x (simulated, invented values)
random.seed(1)
xs = [random.gauss(100, 10) for _ in range(100_000)]
ys = [math.log2(v) for v in xs]
print(f"simulated SD of log2 x = {statistics.stdev(ys):.4f}  linear prediction = {0.10 / math.log(2):.4f}")
```

```text
 x      e^x vs 1+x        ln(1+x) vs x      sqrt(1+x) vs 1+x/2
0.01  1.01005 1.01000   0.00995 0.01000   1.00499 1.00500
0.1   1.10517 1.10000   0.09531 0.10000   1.04881 1.05000
0.5   1.64872 1.50000   0.40547 0.50000   1.22474 1.25000
actual error 0.00469  bound 0.00500
1.000000082690371e-10 9.999999999500001e-11
exact 0.011928  linear L*mu = 0.012000
simulated SD of log2 x = 0.1462  linear prediction = 0.1443
```

`math.log(1 + u)` is wrong from the 8th significant digit because $1 + 10^{-10}$ is rounded before the logarithm is taken; `log1p` and `expm1` evaluate $\ln(1 + u)$ and $e^u - 1$ accurately for tiny $u$ ([[Floating-Point Arithmetic]]). The simulated standard deviation (0.146) is slightly above the linear prediction (0.144): the neglected second-order terms.

## Worked example

> [!example] Uncertainty of a qPCR fold change (invented values)
> A target gene gives $\Delta\Delta C_T = -2.00$ with an uncertainty of $\pm 0.25$ cycle; relative expression is $F = 2^{-\Delta\Delta C_T}$.[^livak]
>
> 1. **Estimate.** $F = 2^{2} = 4$: a fourfold increase.
> 2. **Derivative.** $\frac{dF}{d(\Delta\Delta C_T)} = -F\ln 2 = -2.77$ per cycle.
> 3. **Linear propagation.** $\Delta F \approx 2.77 \times 0.25 = 0.69$, so $F \approx 4 \pm 0.69$ (17 %).
> 4. **Exact interval.** $2^{1.75} = 3.364$ and $2^{2.25} = 4.757$: the interval is $-0.64$ / $+0.76$, asymmetric.
> ```python
> ddct, d = -2.0, 0.25
> F = 2 ** -ddct
> print(F, round(F * math.log(2) * d, 3), round(2 ** -(ddct + d), 3), round(2 ** -(ddct - d), 3))
> # 4.0 0.693 3.364 4.757
> ```
> 5. **Interpretation.** On the cycle (log) scale the uncertainty is symmetric; the exponential stretches the upper side. Report the interval computed on the $C_T$ scale and transformed back ($3.4$ to $4.8$), and use the linear $\pm 0.69$ only as a quick summary.

## Common misconceptions

> [!warning] "Small $x$ is enough"
> Small compared with the curvature scale: the error is about $\frac{M}{2}x^2$. $\ln(1 + x) \approx x$ is 1 % off at $x = 0.02$ but 23 % off at $x = 0.5$.

> [!warning] "A log ratio is a percentage change"
> Only for small changes. $\log_2$ fold change 1 is +100 %, $-1$ is $-50$ %; $\ln(1.02) \approx 0.02$ works, $\ln 2 \approx 1$ does not.

> [!warning] "Errors propagate symmetrically"
> A nonlinear function turns a symmetric input interval into an asymmetric one (qPCR example). $\pm$ from linear propagation is a first-order summary.

> [!warning] "$f'(a) = 0$ means the input error does not matter"
> It means the first-order term vanishes. The error is then second order, $\frac12 f''(a)(\Delta x)^2$, which can be large for large $\Delta x$.

## Exercises

> [!question] Exercise 1 (L1)
> Linearize $\sqrt x$ at $a = 100$ and estimate $\sqrt{102}$.

> [!success]- Solution
> $f'(x) = \frac{1}{2\sqrt x}$, $f'(100) = \frac{1}{20}$, so $L(x) = 10 + \frac{x - 100}{20}$ and $\sqrt{102} \approx 10.1$. The true value is $10.0995$: error $4.9 \times 10^{-4}$, within the bound $\frac{M}{2}(2)^2 = 5 \times 10^{-4}$, where $M = |f''(100)| = \frac{1}{4 \cdot 100^{3/2}}$ is the largest $|f''|$ on $[100, 102]$.

> [!question] Exercise 2 (L1)
> Use linear approximations to estimate (a) the continuous growth rate equivalent to 5 % per generation, (b) $1/1.02$, (c) the probability of at least one new mutation in 3 Mb in one generation at $\mu = 1.2 \times 10^{-8}$.

> [!success]- Solution
> (a) $\ln 1.05 \approx 0.05$ (exact 0.0488). (b) $1/(1 + 0.02) \approx 0.98$ (exact 0.98039). (c) $L\mu = 3 \times 10^6 \times 1.2 \times 10^{-8} = 0.036$; exact $1 - e^{-0.036} \approx 0.0354$, slightly smaller, as the concavity of $1 - e^{-x}$ predicts.

> [!question] Exercise 3 (L2)
> Bound the error of $e^x \approx 1 + x$ on $[0, 0.1]$, and compare with the actual error at $x = 0.1$.

> [!success]- Solution
> $f'' = e^x \le e^{0.1}$ on the interval, so $|R| \le \frac{e^{0.1}}{2}(0.1)^2 = 0.00553$. Actual: $e^{0.1} - 1.1 = 0.00517$. Since $f'' > 0$, the tangent lies below: $1 + x$ underestimates $e^x$.

> [!question] Exercise 4 (L2)
> A Phred quality is $Q = -10\log_{10} p$, with $p$ the base-call error probability.[^cock] Show that a relative uncertainty $r = \Delta p/p$ gives $\Delta Q \approx 4.34\,r$. Evaluate for $p = 0.01 \pm 0.001$ and $p = 0.001 \pm 0.0002$, and compare with the exact change when $p$ decreases by $\Delta p$.

> [!success]- Solution
> $\frac{dQ}{dp} = -\frac{10}{p\ln 10}$, so $|\Delta Q| \approx \frac{10}{\ln 10}\frac{\Delta p}{p} = 4.343\,r$.
>
> ```python
> for p, dp in ((0.01, 0.001), (0.001, 0.0002)):
>     Q = -10 * math.log10(p)
>     print(round(Q, 2), round(10 / math.log(10) * dp / p, 3), round(-10 * math.log10(p - dp) - Q, 3))
> # 20.0 0.434 0.458
> # 30.0 0.869 0.969
> ```
>
> The Phred scale turns relative errors into absolute ones: the same 10 % uncertainty shifts $Q$ by about 0.43 whether $Q$ is 20 or 40. At 20 % the linear estimate is already 10 % too low.

> [!question] Exercise 5 (L3, Python)
> Implement Newton's method for $g(x) = \frac{2}{1 + x^2} - x$ from $x_0 = 2$, print the error $|x_k - 1|$ for 5 steps, and compute $g'(1)$. What do the errors and $g'(1)$ tell you?

> [!success]- Solution
> ```python
> g = lambda x: 2 / (1 + x * x) - x                 # self-repression toy model
> dg = lambda x: -4 * x / (1 + x * x) ** 2 - 1
> x = 2.0
> for step in range(5):
>     x = x - g(x) / dg(x)                          # root of the tangent line at the current x
>     print(step + 1, f"{x:.12f}", f"{abs(x - 1):.1e}")
> print(dg(1.0))
> ```
>
> ```text
> 1 0.787878787879 2.1e-01
> 2 0.990682905780 9.3e-03
> 3 0.999978401409 2.2e-05
> 4 0.999999999883 1.2e-10
> 5 1.000000000000 0.0e+00
> -2.0
> ```
>
> From step 2 on, each error is roughly the square of the previous one (times a constant): the number of correct digits doubles, because the linearization error is quadratic. Bisection needed 35 steps for $10^{-10}$ ([[Continuity]]). $g'(1) = -2 < 0$: the steady state is stable and perturbations decay like $e^{-2t}$.

## Mastery checklist

- [ ] 1 Recognized: I can write $L(x) = f(a) + f'(a)(x - a)$ and the linearizations of $e^x$, $\ln(1 + x)$ and $(1 + x)^k$ at 0.
- [ ] 2 Understood: I can explain why the error is quadratic, which side of the curve the tangent lies on, and when $\ln(1 + x) \approx x$ stops being acceptable.
- [ ] 3 Practiced: I propagate errors through $\log_2$, $2^{-\Delta\Delta C_T}$ and Phred conversions, bound linearization errors, and use `log1p` and `expm1` in code.
- [ ] 4 Applied: I report a fold change or a transformed estimate from real data with an uncertainty propagated correctly, including its asymmetry.
- [ ] 5 Explained: I can teach the delta method, Newton's method and linear stability as three uses of the same tangent line.

## References

[^calc1]: [[Calculus (OpenStax)]], Volume 1 (linear approximations and differentials, with propagated and relative error).
[^calc2]: [[Calculus (OpenStax)]], Volume 2 (Taylor polynomials and Taylor's theorem with remainder).
[^1801]: [[MIT 18.01SC - Single Variable Calculus]], differentiation part (applications: linear approximation).
[^blitz4]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 4 "Expectation" (variance and its properties).
[^kong]: [[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]], Kong A et al., *Nature* 488:471-475: $1.20 \times 10^{-8}$ de novo mutations per nucleotide per generation.
[^livak]: [[Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR]], Livak KJ, Schmittgen TD, *Methods* 25(4):402-408: the $2^{-\Delta\Delta C_T}$ formula and its assumption of efficiencies close to 100 %.
[^cock]: [[Cock 2010 - The Sanger FASTQ File Format]], *Nucleic Acids Research* 38(6):1767-1771: Phred quality $Q = -10 \log_{10} p$.
