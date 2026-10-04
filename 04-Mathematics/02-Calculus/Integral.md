---
aliases:
  - Definite Integral
  - Riemann Integral
  - Riemann Sum
  - Intégrale
tags:
  - type/concept
  - domain/mathematics
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Limit]]"
  - "[[Continuity]]"
  - "[[Summation Notation]]"
  - "[[Antiderivative]]"
related:
  - "[[Fundamental Theorem of Calculus]]"
  - "[[Improper Integral]]"
  - "[[Numerical Integration]]"
  - "[[Probability Density Function]]"
  - "[[Expected Value]]"
  - "[[Receiver Operating Characteristic Curve]]"
  - "[[Compartmental Model]]"
  - "[[Monte Carlo Method]]"
  - "[[Multiple Integral]]"
projects: []
sources:
  - "[[Calculus (OpenStax)]]"
  - "[[MIT 18.01SC - Single Variable Calculus]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[An Introduction to Statistical Learning (James)]]"
  - "[[Basic Principles of Drug Discovery and Development (Blass)]]"
  - "[[Molecular Evolution (Yang)]]"
---

# Integral

> [!abstract]
> The definite integral adds up infinitely many thin slices: it is the limit of sums of rectangles under a curve, which measures an area, the total accumulated from a rate, or a probability under a density.

## Definition

Let $f$ be defined on $[a, b]$. Choose a **partition** $a = x_0 < x_1 < \dots < x_n = b$ with widths $\Delta x_i = x_i - x_{i-1}$ and a **sample point** $x_i^* \in [x_{i-1}, x_i]$ in each piece. The **Riemann sum** is $\sum_{i=1}^{n} f(x_i^*)\,\Delta x_i$. If these sums approach the same number $I$ whenever the largest width tends to 0, whatever the sample points, $f$ is **integrable** on $[a, b]$ and

$$\int_a^b f(x)\,dx = I .$$

Every continuous function on $[a, b]$ is integrable.[^os1][^mit]

## Why it matters

- **Probability is an integral.** For a continuous measurement with density $f$, $P(a \le X \le b) = \int_a^b f(x)\,dx$; every normal-table lookup and every continuous p-value is one ([[Probability Density Function]]).[^blitz5]
- **Summaries of distributions.** Means, variances and moments of continuous variables are integrals weighted by the density ([[Expected Value]], [[Variance]]).
- **Classifier performance.** The area under the ROC curve, used to compare variant-pathogenicity predictors or diagnostic signatures, is an integral computed from a finite set of points ([[Receiver Operating Characteristic Curve]]).[^james]
- **Drug exposure.** The area under the plasma concentration-time curve (AUC) summarizes how much drug the body saw; it is computed from a handful of blood samples by the trapezoid rule.[^blass]
- **Totals from profiles.** Summing per-base read depth over a region gives the number of aligned bases there: the discrete version of integrating a coverage curve.

## Core (L1)

### Area by rectangles

Cut $[a, b]$ into $n$ equal pieces of width $\Delta x = (b - a)/n$, put on each piece a rectangle whose height is $f$ at a chosen point (left end, right end or midpoint), and add the areas. As $n$ grows the rectangles hug the curve and the sum approaches the integral.[^os1]

![[riemann-sum-concentration-curve.svg]]

In the figure, left sums under an invented concentration curve give 28.43 with 4 rectangles and 36.69 with 16, approaching the exact area 37.61 mg·h/L. Left endpoints underestimate where the curve rises and overestimate where it falls.

### Signed area and accumulation

The integral counts area **below** the axis negatively: $\int_0^{2\pi} \sin x\,dx = 0$ because the two humps cancel. The total (unsigned) area is $\int_a^b \lvert f(x) \rvert\,dx$.[^os1]

If $f$ is a **rate**, $\int_a^b f$ is the **net amount** accumulated between $a$ and $b$: integrating a growth rate in cells/h over hours gives a net change in cells, and integrating a concentration in mg/L over hours gives mg·h/L. The units of an integral are always (units of $f$) × (units of $x$). Computing integrals from antiderivatives, instead of from sums, is the [[Fundamental Theorem of Calculus]].

### Properties

For integrable $f, g$ and constants $\alpha, \beta$:[^os1]

| Property | Statement |
|---|---|
| Linearity | $\int_a^b (\alpha f + \beta g) = \alpha \int_a^b f + \beta \int_a^b g$ |
| Additivity | $\int_a^b f + \int_b^c f = \int_a^c f$ |
| Orientation | $\int_a^a f = 0$, $\int_b^a f = -\int_a^b f$ |
| Comparison | $f \le g$ on $[a, b]$ implies $\int_a^b f \le \int_a^b g$ |
| Bounds | $m \le f \le M$ implies $m(b - a) \le \int_a^b f \le M(b - a)$ |
| Average value | $\bar f = \frac{1}{b - a} \int_a^b f$ |

### Three integrals in biology

1. **Probability as area under a density.** The whole area under a density is 1 and the area over an interval is a probability; the details and pitfalls (densities above 1, units) are in [[Probability Density Function]].
2. **Area under the ROC curve.** A classifier scores each case; for every threshold, the true positive rate (TPR, sensitivity) is plotted against the false positive rate (FPR, 1 − specificity). The AUC is $\int_0^1 \mathrm{TPR}\,d(\mathrm{FPR})$: 1 for a perfect ranking, about 0.5 for a random one.[^james]
3. **Pharmacokinetic AUC.** The area under the concentration-time curve, $\int_0^T C(t)\,dt$, measures the total exposure of the body to a drug over $[0, T]$.[^blass] Two drugs with the same peak concentration can have very different AUCs if one is cleared faster ([[Compartmental Model]]).

## Deeper (L2)

### How fast Riemann sums converge

On each piece, $\lvert f(x) - f(x_{i-1}) \rvert \le M_1 (x - x_{i-1})$ where $M_1 = \max \lvert f' \rvert$; integrating over the piece and summing gives the left-sum error bound $M_1 (b - a)^2 / (2n)$: **first order**, halving the step halves the error. The midpoint and trapezoid rules cancel the first-order term and have errors at most $M_2 (b - a)^3 / (24 n^2)$ and $M_2 (b - a)^3 / (12 n^2)$, with $M_2 = \max \lvert f'' \rvert$: **second order**, halving the step divides the error by 4 (Exercise 5).[^os2] Higher-order and adaptive rules are the subject of [[Numerical Integration]].

### Integrating sampled data

Real curves are known only at measured points $(t_0, y_0), \dots, (t_m, y_m)$, often unevenly spaced (dense around a drug's peak, sparse later). The **trapezoid rule** joins them by straight lines:

$$\int_{t_0}^{t_m} y\,dt \approx \sum_{j=1}^{m} (t_j - t_{j-1})\,\frac{y_{j-1} + y_j}{2}.$$

Its bias follows the curvature: where the curve is concave (around a peak) the chords lie below it and the rule underestimates; where it is convex (an exponential decline) the chords lie above and it overestimates. The same rule integrates an empirical ROC curve, whose points are $(\mathrm{FPR}, \mathrm{TPR})$ pairs (Exercise 4).

## Advanced (L3)

- **Not every function is integrable.** Let $D(x) = 1$ for rational $x$ and $0$ otherwise. Every piece of every partition of $[0, 1]$ contains both kinds of numbers, so choosing rational sample points gives sums equal to 1 and irrational ones gives 0: the limit does not exist, although $D$ is bounded. Integrability is a real condition, not a formality.
- **Mixed distributions.** An instrument that reports every value below its detection limit $d$ as $d$ produces a variable with a point mass at $d$ plus a density above it. Its mean is a sum plus an integral, $d\,P(X = d) + \int_d^\infty x f(x)\,dx$, where $f$ integrates to $1 - P(X = d)$ (see [[Probability Density Function#Variables without a density]]).
- **High dimensions.** A grid with $m$ points per axis needs $m^d$ evaluations in $d$ dimensions, impossible beyond a few dimensions. Monte Carlo integration estimates $\int_a^b f$ by $(b - a)$ times the average of $f$ at uniform random points; its standard error is proportional to $1/\sqrt{n}$ because the variance of a mean of $n$ independent terms is $\sigma^2/n$, and this does not depend on $d$ ([[Monte Carlo Method]], [[Variance]]). Posterior summaries in Bayesian phylogenetics are integrals over many parameters and are computed by Markov chain Monte Carlo ([[Markov Chain Monte Carlo]]).[^yang]

## Mathematical representation

- **Partition** $P = \{x_0, \dots, x_n\}$ of $[a, b]$, **mesh** $\lVert P \rVert = \max_i \Delta x_i$.
- **Riemann sum** $S(f, P, x^*) = \sum_{i=1}^n f(x_i^*)\,\Delta x_i$; **definite integral** $\int_a^b f = \lim_{\lVert P \rVert \to 0} S(f, P, x^*)$ when the limit exists for all choices of $x^*$.
- **Upper and lower sums** use $M_i = \sup_{[x_{i-1}, x_i]} f$ and $m_i = \inf_{[x_{i-1}, x_i]} f$; $f$ is integrable iff they can be made arbitrarily close.[^os1]
- **Equal widths**, $\Delta x = (b - a)/n$, $x_i = a + i\Delta x$: left sum $L_n = \Delta x \sum_{i=0}^{n-1} f(x_i)$, right sum $R_n = \Delta x \sum_{i=1}^{n} f(x_i)$, trapezoid $T_n = (L_n + R_n)/2$, midpoint $M_n = \Delta x \sum_{i=1}^{n} f\!\left(\tfrac{x_{i-1} + x_i}{2}\right)$.
- **ROC AUC** with $n_+$ positives and $n_-$ negatives: points $(\mathrm{FPR}_j, \mathrm{TPR}_j)$ from $(0, 0)$ to $(1, 1)$, area by the trapezoid rule.

## Computational representation

A function `riemann(f, a, b, n, rule)` covers the four equal-width rules; `trapezoid(xs, ys)` integrates sampled data. Libraries provide the same (`numpy.trapezoid`, `scipy.integrate.quad` for adaptive quadrature).

```python
import math

def C(t: float) -> float:
    """Invented plasma concentration (mg/L) after an oral dose at t = 0 (h)."""
    return 12 * (math.exp(-0.25 * t) - math.exp(-1.5 * t))

def riemann(f, a: float, b: float, n: int, rule: str = "mid") -> float:
    """Riemann sum of f on [a, b] with n equal subintervals; rule = left, right, mid or trap."""
    dx = (b - a) / n
    if rule == "trap":
        return dx * (f(a) / 2 + sum(f(a + i * dx) for i in range(1, n)) + f(b) / 2)
    shift = {"left": 0.0, "right": 1.0, "mid": 0.5}[rule]
    return dx * sum(f(a + (i + shift) * dx) for i in range(n))

def trapezoid(xs, ys) -> float:
    """Trapezoid rule on samples at possibly uneven positions xs."""
    return sum((x1 - x0) * (y0 + y1) / 2 for x0, x1, y0, y1 in zip(xs, xs[1:], ys, ys[1:]))

exact = 12 * ((1 - math.exp(-3)) / 0.25 - (1 - math.exp(-18)) / 1.5)   # from an antiderivative
print("exact", round(exact, 4))
for n in (4, 16, 64, 256):
    print(n, *(f"{riemann(C, 0, 12, n, r):.4f}" for r in ("left", "right", "mid", "trap")))
```

Output (columns: left, right, midpoint, trapezoid):

```text
exact 37.6102
4 28.4278 30.2202 40.7215 29.3240
16 36.6933 37.1413 37.9503 36.9173
64 37.5099 37.6219 37.6324 37.5659
256 37.5934 37.6214 37.6116 37.6074
```

## Worked example

> [!example] Drug exposure from eight blood samples (invented data)
> Concentrations (mg/L) were read from the invented curve of the figure at a typical sampling schedule and rounded:
>
> | Interval (h) | $C$ at ends | Trapezoid area |
> |---|---|---:|
> | 0 to 0.5 | 0.00, 4.92 | 1.230 |
> | 0.5 to 1 | 4.92, 6.67 | 2.898 |
> | 1 to 2 | 6.67, 6.68 | 6.675 |
> | 2 to 4 | 6.68, 4.38 | 11.060 |
> | 4 to 6 | 4.38, 2.68 | 7.060 |
> | 6 to 8 | 2.68, 1.62 | 4.300 |
> | 8 to 12 | 1.62, 0.60 | 4.440 |
>
> 1. **Sum.** `trapezoid([0, 0.5, 1, 2, 4, 6, 8, 12], [0, 4.92, 6.67, 6.68, 4.38, 2.68, 1.62, 0.6])` gives $\mathrm{AUC}_{0-12} \approx 37.66$ mg·h/L.
> 2. **Compare.** The exact area is 37.61. The near-agreement is partly luck: the chords underestimate around the concave peak (1 to 2 h) and overestimate on the convex decline (8 to 12 h), and the two errors cancel.
> 3. **Beyond the last sample.** The curve keeps decaying roughly like $0.60\,e^{-0.25(t - 12)}$, whose area from 12 h to infinity is $0.60/0.25 = 2.4$ ([[Improper Integral]]). Adding it gives $\approx 40.06$, against the exact $\int_0^\infty C = 12\,(1/0.25 - 1/1.5) = 40$.

## Common misconceptions

> [!warning] "An integral is an area"
> It is a **signed** area. Integrating a rate that changes sign (net growth then net death of a culture) gives the net change, not the total activity; for the latter integrate $\lvert f \rvert$.

> [!warning] "The integral is a number without units"
> Its units are those of $f$ times those of $x$: mg·h/L for a pharmacokinetic AUC, a probability (no units) for a density in 1/mm integrated over mm. A ROC AUC has no units because both axes are proportions.

> [!warning] "The trapezoid rule is exact enough on any sampling schedule"
> Its error depends on curvature and spacing. Sparse sampling around a sharp peak underestimates the area, sparse sampling on a decaying tail overestimates it, and no sample after the last time point means the tail is missing altogether.

## Exercises

> [!question] Exercise 1 (L1)
> Compute the left and right Riemann sums of $f(x) = x^2$ on $[0, 2]$ with $n = 4$, and compare with the exact value $8/3$.

> [!success]- Solution
> $\Delta x = 0.5$. Left: $0.5\,(0 + 0.25 + 1 + 2.25) = 1.75$. Right: $0.5\,(0.25 + 1 + 2.25 + 4) = 3.75$. Since $f$ increases, left sums underestimate and right sums overestimate: $1.75 < 8/3 \approx 2.667 < 3.75$. Their average (the trapezoid rule) is 2.75.

> [!question] Exercise 2 (L1)
> A sequencer produces data at a rate $r(t)$ in gigabases per hour. What does $\int_0^{24} r(t)\,dt$ mean, and in which units? What is $\int_{-1}^{1} x^3\,dx$, and why?

> [!success]- Solution
> The total output during the first 24 h, in gigabases ((Gb/h) × h). The second integral is 0: $x^3$ is odd, so the signed areas on $[-1, 0]$ and $[0, 1]$ cancel.

> [!question] Exercise 3 (L2)
> Using $\sum_{i=1}^n i = n(n+1)/2$, show that the right Riemann sum of $f(x) = x$ on $[0, 1]$ is $\frac{n+1}{2n}$ and find its limit.

> [!success]- Solution
> $\Delta x = 1/n$ and $x_i = i/n$, so $R_n = \sum_{i=1}^n \frac{i}{n}\cdot\frac{1}{n} = \frac{1}{n^2}\cdot\frac{n(n+1)}{2} = \frac{n+1}{2n} \to \frac12$, the area of the triangle under $y = x$ ([[Summation Notation]], [[Limit]]).

> [!question] Exercise 4 (L2, Python)
> A predictor gives scores to 6 pathogenic variants `[0.92, 0.81, 0.77, 0.64, 0.58, 0.40]` and 8 benign ones `[0.70, 0.52, 0.35, 0.33, 0.21, 0.15, 0.10, 0.05]` (invented). Build the ROC points by lowering the threshold through every score, compute the AUC with `trapezoid`, and compare it with the fraction of (pathogenic, benign) pairs in which the pathogenic variant scores higher.

> [!success]- Solution
> ```python
> pos = [0.92, 0.81, 0.77, 0.64, 0.58, 0.40]
> neg = [0.70, 0.52, 0.35, 0.33, 0.21, 0.15, 0.10, 0.05]
>
> def roc_points(pos, neg):
>     """(FPR, TPR) points as the threshold decreases through every score (no ties assumed)."""
>     pts, tp, fp = [(0.0, 0.0)], 0, 0
>     for s, label in sorted([(s, 1) for s in pos] + [(s, 0) for s in neg], reverse=True):
>         tp, fp = tp + label, fp + (1 - label)
>         pts.append((fp / len(neg), tp / len(pos)))
>     return pts
>
> fpr, tpr = zip(*roc_points(pos, neg))
> pairs = sum(p > q for p in pos for q in neg) / (len(pos) * len(neg))
> print(round(trapezoid(fpr, tpr), 4), round(pairs, 4))   # 0.9167 0.9167
> ```
>
> Both give 0.9167 (44 of the 48 pairs are correctly ordered). The equality is no accident: each benign variant moves the curve one step right at the height reached by the pathogenic variants scoring above it, so the area adds up correctly ordered pairs. This is why an AUC reads as "the probability that a random positive outranks a random negative" ([[Receiver Operating Characteristic Curve]]).

> [!question] Exercise 5 (L3, Python)
> With `riemann`, integrate $e^{-x}$ on $[0, 1]$ with $n = 10, 20, 40$ using the left, midpoint and trapezoid rules. Compute the error ratios when $n$ doubles and relate them to the error bounds.

> [!success]- Solution
> ```python
> f, ex = (lambda x: math.exp(-x)), 1 - math.exp(-1)
> for rule in ("left", "mid", "trap"):
>     errs = [abs(riemann(f, 0, 1, n, rule) - ex) for n in (10, 20, 40)]
>     print(rule, [f"{e:.2e}" for e in errs], [round(errs[i] / errs[i + 1], 2) for i in range(2)])
> # left ['3.21e-02', '1.59e-02', '7.93e-03'] [2.02, 2.01]
> # mid ['2.63e-04', '6.58e-05', '1.65e-05'] [4.0, 4.0]
> # trap ['5.27e-04', '1.32e-04', '3.29e-05'] [4.0, 4.0]
> ```
>
> The left rule is first order (ratio 2, error $\propto 1/n$); midpoint and trapezoid are second order (ratio 4, error $\propto 1/n^2$), and the midpoint error is about half the trapezoid error, as the bounds $1/24$ versus $1/12$ suggest.

> [!question] Exercise 6 (L3)
> Explain why a grid-based rule is hopeless for an integral over 20 parameters, and what the error of Monte Carlo integration depends on.

> [!success]- Solution
> With only 10 points per axis a grid needs $10^{20}$ evaluations. Monte Carlo averages $f$ at $n$ random points; the average has standard deviation $\sigma_f/\sqrt{n}$ whatever the dimension, so its accuracy depends on $n$ and on the variability $\sigma_f$ of $f$, not on the number of parameters. Reducing $\sigma_f$ (sampling where $f$ is large) is the idea behind importance sampling and MCMC.

## Mastery checklist

- [ ] 1 Recognized: I can say that an integral is a limit of Riemann sums and that it measures signed area or accumulation.
- [ ] 2 Understood: I can explain sample points, signed area, units of an integral and the properties table.
- [ ] 3 Practiced: I can compute left, right, midpoint and trapezoid sums by hand and in Python, and predict their error order.
- [ ] 4 Applied: I can compute a pharmacokinetic AUC from sampled concentrations and a ROC AUC from classifier scores, and explain their biases.
- [ ] 5 Explained: I can teach why some functions are not Riemann integrable, how mixed distributions are integrated, and why Monte Carlo replaces grids in high dimension.

## References

[^os1]: [[Calculus (OpenStax)]], Volume 1, integration (approximating areas, Riemann sums, the definite integral and its properties, average value).
[^os2]: [[Calculus (OpenStax)]], Volume 2, techniques of integration (numerical integration: midpoint and trapezoidal rules and their error bounds).
[^mit]: [[MIT 18.01SC - Single Variable Calculus]], integration part (definite integrals as limits of Riemann sums).
[^blitz5]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 5 "Continuous Random Variables" (probabilities as integrals of a PDF).
[^james]: [[An Introduction to Statistical Learning (James)]], treatment of classification (ROC curve as true positive rate against false positive rate over all thresholds, AUC as overall performance).
[^blass]: [[Basic Principles of Drug Discovery and Development (Blass)]], 2nd ed., treatment of pharmacokinetics (plasma concentration-time curve and AUC as a measure of exposure).
[^yang]: [[Molecular Evolution (Yang)]], Bayesian methods (Markov chain Monte Carlo for posterior inference in phylogenetics).
