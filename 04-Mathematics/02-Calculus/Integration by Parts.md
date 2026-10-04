---
aliases:
  - Partial Integration
  - Intégration par parties
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
  - "[[Integration by Substitution]]"
  - "[[Improper Integral]]"
  - "[[Exponential Distribution]]"
  - "[[Gamma Distribution]]"
  - "[[Expected Value]]"
  - "[[Variance]]"
  - "[[Taylor Series]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Molecular Evolution (Yang)]]"
---

# Integration by Parts

> [!abstract]
> Integration by parts is the product rule read backwards: it trades the integral of a product for a simpler one, and it is how the mean of a waiting time and the gamma function (the factorial extended to all positive numbers) are computed.

## Definition

If $u$ and $v$ have continuous derivatives on $[a, b]$, then[^os2][^mit]

$$\int u\,dv = uv - \int v\,du, \qquad \int_a^b u(x)\,v'(x)\,dx = \big[u(x)\,v(x)\big]_a^b - \int_a^b u'(x)\,v(x)\,dx .$$

## Why it matters

- **Moments of waiting times.** Means and variances of exponential and gamma waiting times (time to the next substitution on a branch, mRNA lifetimes) are integrals of $t^k e^{-\lambda t}$, solved by parts ([[Exponential Distribution]], [[Expected Value]]).[^blitz5]
- **The gamma function.** $\Gamma(a)$ normalizes the gamma, beta, chi-square and Student-t densities; its recursion $\Gamma(a + 1) = a\,\Gamma(a)$ comes from one integration by parts.[^blitz8] The gamma distribution models rate variation among alignment sites in phylogenetic substitution models ([[Gamma Distribution]]).[^yang]
- **Survival form of the mean.** $E[T] = \int_0^\infty P(T > t)\,dt$ for a non-negative $T$, the continuous counterpart of the tail-sum formula in [[Expected Value]], and the bridge to survival curves ([[Survival Analysis]]).
- **Error terms.** The integral form of the Taylor remainder is obtained by repeated integration by parts ([[Taylor Series]]).

## Core (L1)

**Where it comes from.** The product rule $(uv)' = u'v + uv'$, integrated over $[a, b]$ with the [[Fundamental Theorem of Calculus]], gives $[uv]_a^b = \int_a^b u'v + \int_a^b uv'$. Rearranging gives the formula.[^os2]

**Choosing $u$ and $dv$.** Pick $u$ that becomes simpler when differentiated and $dv$ that is easy to integrate.

> [!tip] Rule of thumb
> Logarithms and polynomials make good $u$ (they simplify or disappear when differentiated); exponentials, sines and cosines make good $dv$ (they integrate to themselves, up to constants).

**Examples.**

| Integral | $u$, $dv$ | Result |
|---|---|---|
| $\int x e^{x}\,dx$ | $u = x$, $dv = e^x\,dx$ | $x e^x - \int e^x\,dx = (x - 1)e^x + C$ |
| $\int \ln x\,dx$ | $u = \ln x$, $dv = dx$ | $x\ln x - \int x \cdot \frac1x\,dx = x\ln x - x + C$ |
| $\int x^2 e^{-x}\,dx$ | $u = x^2$, $dv = e^{-x}dx$, twice | $-(x^2 + 2x + 2)\,e^{-x} + C$ |

The second line shows a trick: when nothing looks like a product, take $dv = dx$. The third needs two rounds, each lowering the power of $x$ by one.

**Bio: the mean of an exponential waiting time.** If each mRNA molecule is degraded at constant rate $\lambda$, its lifetime has density $\lambda e^{-\lambda t}$ on $t \ge 0$.[^blitz5] With $u = t$, $dv = \lambda e^{-\lambda t}\,dt$, $v = -e^{-\lambda t}$:

$$E[T] = \int_0^\infty t\,\lambda e^{-\lambda t}\,dt = \Big[-t\,e^{-\lambda t}\Big]_0^\infty + \int_0^\infty e^{-\lambda t}\,dt = 0 + \frac{1}{\lambda}.$$

The boundary term vanishes because $t e^{-\lambda t} \to 0$ as $t \to \infty$ ([[Improper Integral]]). Mean lifetime $= 1/\lambda$; since the half-life is $t_{1/2} = \ln 2/\lambda$, the mean is $t_{1/2}/\ln 2 \approx 1.44\,t_{1/2}$.

## Deeper (L2)

### The gamma function

For $a > 0$, $\Gamma(a) = \int_0^\infty x^{a-1} e^{-x}\,dx$.[^blitz8] Integration by parts with $u = x^{a}$, $dv = e^{-x}dx$:

$$\Gamma(a + 1) = \Big[-x^{a} e^{-x}\Big]_0^\infty + a \int_0^\infty x^{a-1} e^{-x}\,dx = a\,\Gamma(a).$$

With $\Gamma(1) = \int_0^\infty e^{-x}\,dx = 1$, induction gives $\Gamma(n) = (n - 1)!$ for integers $n \ge 1$: $\Gamma$ extends the factorial to all positive reals. The substitution $x = z^2/2$ turns $\Gamma(1/2)$ into the normal integral, giving $\Gamma(1/2) = \sqrt{\pi}$ ([[Integration by Substitution]]).

**Gamma distribution.** The density $\frac{\lambda^a}{\Gamma(a)} x^{a-1} e^{-\lambda x}$ ($x > 0$, shape $a$, rate $\lambda$) integrates to 1 by the substitution $u = \lambda x$, and its mean is

$$\int_0^\infty x \cdot \frac{\lambda^a x^{a-1} e^{-\lambda x}}{\Gamma(a)}\,dx = \frac{\Gamma(a + 1)}{\lambda\,\Gamma(a)} = \frac{a}{\lambda}.$$

For integer $a$ it is the waiting time for $a$ successive exponential events ([[Gamma Distribution]]).[^blitz8]

### The survival form of the mean

Let $T \ge 0$ have density $f$, CDF $F$ and survival function $S(t) = 1 - F(t) = P(T > t)$. With $u = t$, $dv = f(t)\,dt$, $v = -S(t)$:

$$E[T] = \Big[-t\,S(t)\Big]_0^\infty + \int_0^\infty S(t)\,dt = \int_0^\infty P(T > t)\,dt,$$

where the boundary term vanishes when $E[T]$ is finite. For the exponential, $\int_0^\infty e^{-\lambda t}\,dt = 1/\lambda$ again, with no product to integrate.

## Mathematical representation

- **Formula.** $\int_a^b u v' = [uv]_a^b - \int_a^b u' v$ for $u, v \in C^1([a, b])$; on infinite ranges, take limits and check the boundary term ([[Improper Integral]]).
- **Exponential moments.** $I_k = \int_0^\infty t^k \lambda e^{-\lambda t}\,dt$ satisfies $I_k = \frac{k}{\lambda} I_{k-1}$, $I_0 = 1$, hence $I_k = k!/\lambda^k$.
- **Gamma function.** $\Gamma(a + 1) = a\Gamma(a)$, $\Gamma(n) = (n - 1)!$, $\Gamma(\tfrac12) = \sqrt\pi$.[^blitz8]

## Computational representation

Python's `math.gamma` evaluates $\Gamma$; numerical integration checks every closed form above.

```python
import math

def midpoint(f, a: float, b: float, n: int = 200_000) -> float:
    """Midpoint Riemann sum of f on [a, b]."""
    dx = (b - a) / n
    return dx * sum(f(a + (i + 0.5) * dx) for i in range(n))

lam = math.log(2) / 30                       # invented: mRNA half-life 30 min
T_MAX = 2000                                 # e^{-lam * 2000} ~ 1e-20: the tail is negligible
mean = midpoint(lambda t: t * lam * math.exp(-lam * t), 0, T_MAX)
second = midpoint(lambda t: t * t * lam * math.exp(-lam * t), 0, T_MAX)
tail = midpoint(lambda t: math.exp(-lam * t), 0, T_MAX)          # integral of P(T > t)
print(round(mean, 3), round(1 / lam, 3), round(tail, 3))
print(round(second - mean ** 2, 1), round(1 / lam ** 2, 1))

def gamma_numeric(a: float, upper: float = 60.0) -> float:
    """Gamma(a) = integral of x^(a-1) e^(-x) on (0, upper), for a >= 1."""
    return midpoint(lambda x: x ** (a - 1) * math.exp(-x), 0, upper)

for a in (1, 2, 3.5, 5):
    print(a, round(gamma_numeric(a), 6), round(math.gamma(a), 6))
print(round(math.gamma(0.5) ** 2, 10), round(math.pi, 10))
```

Output:

```text
43.281 43.281 43.281
1873.2 1873.2
1 1.0 1.0
2 1.0 1.0
3.5 3.323351 3.323351
5 24.0 24.0
3.1415926536 3.1415926536
```

## Worked example

> [!example] Mean and spread of an mRNA lifetime (invented half-life)
> Half-life 30 min, so $\lambda = \ln 2/30 \approx 0.0231$ per min.
>
> 1. **Mean by parts.** $E[T] = 1/\lambda = 30/\ln 2 \approx 43.3$ min, longer than the half-life because a few molecules survive for a long time.
> 2. **Same result by the survival form.** $\int_0^\infty e^{-\lambda t}\,dt = 1/\lambda$.
> 3. **Second moment by parts twice.** $E[T^2] = 2/\lambda^2 \approx 3746$ min².
> 4. **Variance.** $2/\lambda^2 - 1/\lambda^2 = 1/\lambda^2 \approx 1873$ min², SD $\approx 43.3$ min: the SD of an exponential lifetime equals its mean ([[Variance]]), as the numerical integrals above confirm.

## Common misconceptions

> [!warning] Any choice of $u$ will do
> With $u = e^x$ and $dv = x\,dx$, $\int x e^x\,dx$ becomes $\frac{x^2}{2}e^x - \int \frac{x^2}{2}e^x\,dx$: the new integral is harder. If the power goes up, swap the roles.

> [!warning] Forgetting the boundary term
> In a definite or improper integral, $[uv]_a^b$ must be evaluated, and on $[0, \infty)$ its limit must exist. It vanishes for $t\,e^{-\lambda t}$ but not for every integrand: it is part of the proof, not a formality.

> [!warning] "The mean lifetime is the half-life"
> The half-life is the **median** of an exponential lifetime; the mean is $1/\lambda = t_{1/2}/\ln 2$, about 44 % longer. Mixing them distorts turnover rates computed from decay experiments.

## Exercises

> [!question] Exercise 1 (L1)
> Compute $\int x\cos x\,dx$.

> [!success]- Solution
> $u = x$, $dv = \cos x\,dx$, $v = \sin x$: $x\sin x - \int \sin x\,dx = x\sin x + \cos x + C$. Differentiating gives back $x\cos x$.

> [!question] Exercise 2 (L1)
> Compute $\int_1^e \ln x\,dx$.

> [!success]- Solution
> $\big[x\ln x - x\big]_1^e = (e - e) - (0 - 1) = 1$.

> [!question] Exercise 3 (L2)
> For $T$ with density $\lambda e^{-\lambda t}$, compute $E[T^2]$ by parts (using $E[T] = 1/\lambda$) and deduce $\operatorname{Var}(T)$.

> [!success]- Solution
> $u = t^2$, $dv = \lambda e^{-\lambda t}dt$: $E[T^2] = [-t^2 e^{-\lambda t}]_0^\infty + \int_0^\infty 2t\,e^{-\lambda t}\,dt = \frac{2}{\lambda}\int_0^\infty t\,\lambda e^{-\lambda t}\,dt = \frac{2}{\lambda} E[T] = \frac{2}{\lambda^2}$. Hence $\operatorname{Var}(T) = 2/\lambda^2 - 1/\lambda^2 = 1/\lambda^2$.

> [!question] Exercise 4 (L2)
> Using $\Gamma(a + 1) = a\Gamma(a)$, $\Gamma(1) = 1$ and $\Gamma(\tfrac12) = \sqrt\pi$, compute $\Gamma(5)$ and $\Gamma(\tfrac32)$.

> [!success]- Solution
> $\Gamma(5) = 4 \cdot 3 \cdot 2 \cdot 1 \cdot \Gamma(1) = 24 = 4!$. $\Gamma(\tfrac32) = \tfrac12 \Gamma(\tfrac12) = \sqrt\pi/2 \approx 0.886227$, the value `math.gamma(1.5)` returns.

> [!question] Exercise 5 (L2, Python)
> For the gamma density with shape $a = 3$ and rate $\lambda = 2$, check numerically that it integrates to 1 and that its mean is $a/\lambda$.

> [!success]- Solution
> ```python
> a, r = 3, 2.0
> dens = lambda x: r ** a * x ** (a - 1) * math.exp(-r * x) / math.gamma(a)
> print(round(midpoint(dens, 0, 40), 6), round(midpoint(lambda x: x * dens(x), 0, 40), 6), a / r)
> # 1.0 1.5 1.5
> ```
>
> The mean $\Gamma(a + 1)/(\lambda\Gamma(a)) = a/\lambda = 1.5$: the time for three successive events of rate 2 is three times the mean wait of one.

## Mastery checklist

- [ ] 1 Recognized: I can write the integration by parts formula and say it comes from the product rule.
- [ ] 2 Understood: I can explain how to choose $u$ and $dv$, and why the boundary term must be checked on infinite ranges.
- [ ] 3 Practiced: I can integrate $x e^x$, $\ln x$, $x^2 e^{-x}$, and compute exponential moments and gamma-function values by hand and in Python.
- [ ] 4 Applied: I can compute mean and variance of lifetimes or waiting times from decay data, and distinguish mean lifetime from half-life.
- [ ] 5 Explained: I can teach the gamma function and its recursion, the survival form of the mean, and how repeated integration by parts produces reduction formulas and the Taylor remainder.

## References

[^os2]: [[Calculus (OpenStax)]], Volume 2, techniques of integration (integration by parts).
[^mit]: [[MIT 18.01SC - Single Variable Calculus]], integration part (techniques of integration).
[^blitz5]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 5 "Continuous Random Variables" (the exponential distribution, its mean and variance).
[^blitz8]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 8 "Transformations" (the gamma function, its recursion and $\Gamma(1/2) = \sqrt\pi$; the gamma distribution as a sum of exponentials).
[^yang]: [[Molecular Evolution (Yang)]], treatment of rate variation among sites (the gamma model in nucleotide substitution models).
