---
aliases:
  - Rate Equation
  - Reaction Order
  - Integrated Rate Law
  - Half-Life
  - Loi de vitesse
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Reaction Kinetics]]"
  - "[[Exponential Function]]"
  - "[[Logarithm]]"
  - "[[Integral]]"
related:
  - "[[Ordinary Differential Equation]]"
  - "[[Separable Differential Equation]]"
  - "[[Activation Energy]]"
  - "[[Michaelis-Menten Kinetics]]"
  - "[[Gene Expression]]"
  - "[[Messenger RNA]]"
  - "[[Exponential Distribution]]"
  - "[[Linear Regression]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Schwanhäusser 2011 - Global Quantification of Mammalian Gene Expression Control]]"
---

# Rate Law

> [!abstract]
> A rate law says how a reaction's speed depends on concentrations; integrating it tells you how much is left at any time, and for first-order processes such as mRNA and protein decay it gives a half-life that does not depend on how much you started with.

## Definition

A **rate law** (rate equation) expresses the rate of a reaction as a function of reactant concentrations, usually as $v = k[\mathrm{A}]^m[\mathrm{B}]^n$, where $k$ is the rate constant and the exponents $m$ and $n$ are the **orders** with respect to A and B; their sum is the overall order. Orders are determined experimentally and need not match the stoichiometric coefficients.[^chem12] The **integrated rate law** gives concentration as a function of time, and the **half-life** $t_{1/2}$ is the time for a reactant's concentration to fall to half its initial value.[^chem12]

## Why it matters

- **Turnover data.** mRNA and protein stabilities are reported as first-order half-lives or decay constants, estimated genome-wide from labelling time courses ([[Gene Expression]]).[^schwan]
- **Models.** Every term of a kinetic model is a rate law; its order decides whether the ODE is linear (first order) or not ([[Ordinary Differential Equation]], [[Systems Biology]]).
- **Enzymes switch order.** A saturated enzyme runs at constant speed (zero order in substrate), an unsaturated one in proportion to substrate (first order) ([[Michaelis-Menten Kinetics]]).[^berg]
- **Model choice from data.** Deciding which integrated law fits a time course is a small model-selection problem, with the usual traps of short time windows and noise.

## Core (L1)

### Determining orders: the method of initial rates

Measure the initial rate ([[Reaction Kinetics]]) in experiments where only one concentration changes.[^chem12] If doubling $[\mathrm{A}]$ multiplies the rate by 4, then $2^m = 4$ and $m = 2$. In general, $m = \log(v_2/v_1)/\log([\mathrm{A}]_2/[\mathrm{A}]_1)$.

### Integrated rate laws

For $\mathrm{A} \to$ products with $-d[\mathrm{A}]/dt = k[\mathrm{A}]^n$, integration from $[\mathrm{A}]_0$ at $t = 0$ gives:[^chem12]

| Order | Rate law | Integrated form | Straight-line plot | Half-life |
|---:|---|---|---|---|
| 0 | $v = k$ | $[\mathrm{A}] = [\mathrm{A}]_0 - kt$ | $[\mathrm{A}]$ vs $t$, slope $-k$ | $[\mathrm{A}]_0/(2k)$ |
| 1 | $v = k[\mathrm{A}]$ | $\ln[\mathrm{A}] = \ln[\mathrm{A}]_0 - kt$ | $\ln[\mathrm{A}]$ vs $t$, slope $-k$ | $\ln 2/k$ |
| 2 | $v = k[\mathrm{A}]^2$ | $1/[\mathrm{A}] = 1/[\mathrm{A}]_0 + kt$ | $1/[\mathrm{A}]$ vs $t$, slope $+k$ | $1/(k[\mathrm{A}]_0)$ |

**First order, derived.** Separate variables ([[Separable Differential Equation]]): $d[\mathrm{A}]/[\mathrm{A}] = -k\,dt$, integrate ([[Integral]]): $\ln[\mathrm{A}] - \ln[\mathrm{A}]_0 = -kt$, so $[\mathrm{A}] = [\mathrm{A}]_0 e^{-kt}$, an exponential decay ([[Exponential Function]]). Setting $[\mathrm{A}] = [\mathrm{A}]_0/2$ gives $t_{1/2} = \ln 2/k$.

**Which plot is straight tells the order.**[^chem12] The figure shows one first-order data set in the three plots: only $\ln[\mathrm{A}]$ against $t$ is a line.

![[integrated-rate-law-linear-plots.svg]]

**Half-lives behave differently.** A first-order half-life is the same at every stage of the reaction; a zero-order half-life shrinks as $[\mathrm{A}]$ falls, and a second-order one grows.[^chem12]

### Bio: mRNA and protein decay are first order

Each molecule of a given mRNA or protein has, at every moment, the same chance of being degraded, so the population decays at a rate proportional to its size: first order. Schwanhäusser and colleagues measured mRNA and protein turnover for more than 5,000 genes in mouse fibroblasts by metabolic pulse labelling and fitted first-order synthesis-degradation models; typical half-lives were about 9 h for mRNAs and 46 h for proteins.[^schwan]

| Molecule | $t_{1/2}$ | $k = \ln 2/t_{1/2}$ | left after 24 h | time to lose 90 % |
|---|---:|---:|---:|---:|
| typical mRNA | 9 h | 0.077 h⁻¹ | 15.7 % | 29.9 h |
| typical protein | 46 h | 0.0151 h⁻¹ | 69.7 % | 152.8 h |

Losing 90 % takes $\ln 10/k \approx 3.3$ half-lives, whatever the molecule.

## Deeper (L2)

**Where zero order comes from.** A reaction is zero order in a substrate when something else limits it. An enzyme saturated with substrate works at its maximal velocity, independent of substrate concentration, until the substrate runs low and the kinetics become first order.[^berg]

**Pseudo-first-order.** For $v = k[\mathrm{A}][\mathrm{B}]$ with B in large excess, $[\mathrm{B}] \approx [\mathrm{B}]_0$ throughout, so $v \approx k'[\mathrm{A}]$ with $k' = k[\mathrm{B}]_0$. Flooding with one reactant is how the order in the other is isolated, and why many biological processes look first order.

**First order means memoryless lifetimes.** A constant per-molecule probability of decay per unit time makes the lifetime of each molecule exponentially distributed with mean $1/k$ ([[Exponential Distribution]]): the surviving fraction $e^{-kt}$ is both a concentration curve and a survival function.

**Short time courses do not discriminate.** Over about one half-life, all three plots of a first-order decay look nearly straight (Exercise 4). To distinguish orders, follow the reaction over two or more half-lives, or vary the initial concentration and check whether $t_{1/2}$ changes.

## Advanced (L3)

**Decay rates at genome scale.** Turnover studies label newly made molecules (or pre-existing ones) and follow labelled and unlabelled fractions over time; a first-order model per gene converts the curves into decay constants and half-lives.[^schwan] Two modelling choices matter:

- **Dilution by growth.** In dividing cells, concentration also falls because volume doubles every $T_d$: the observed decay constant is $k_{\mathrm{obs}} = k_{\mathrm{deg}} + \ln 2/T_d$. A stable protein in fast-dividing cells is "lost" mostly by dilution (Exercise 6). The fitted rates feed the mRNA-protein model of [[Gene Expression]].
- **Fitting on the log scale or not.** A straight-line fit of $\ln[\mathrm{A}]$ against $t$ ([[Linear Regression]]) is simple, but it weights relative errors equally and amplifies the noise of late, low points; nonlinear least squares on $[\mathrm{A}]_0 e^{-kt}$ weights absolute errors. With noisy proteomics or sequencing data, the choice changes the estimated half-lives of unstable and very stable molecules most.

## Mathematical representation

The rate law is the ODE $\dfrac{d[\mathrm{A}]}{dt} = -k[\mathrm{A}]^n$, with $[\mathrm{A}](0) = [\mathrm{A}]_0$. For $n \ne 1$, separation of variables gives

$$[\mathrm{A}]^{1-n} = [\mathrm{A}]_0^{1-n} + (n-1)\,k\,t, \qquad t_{1/2} = \frac{2^{\,n-1} - 1}{(n-1)\,k\,[\mathrm{A}]_0^{\,n-1}},$$

and $n = 1$ is the limit $[\mathrm{A}] = [\mathrm{A}]_0 e^{-kt}$, $t_{1/2} = \ln 2/k$. Hence $t_{1/2} \propto [\mathrm{A}]_0^{\,1-n}$: independent of $[\mathrm{A}]_0$ only for first order, which is the experimental test. Symbols: $[\mathrm{A}]$ concentration, $t$ time, $k$ rate constant (units M$^{1-n}$ time⁻¹), $n$ order.

## Computational representation

```python
import math
import statistics

def concentration(order: int, a0: float, k: float, t: float) -> float:
    """Integrated rate law for A -> products, rate = k[A]^order (order 0, 1 or 2)."""
    if order == 0:
        return max(a0 - k * t, 0.0)
    if order == 1:
        return a0 * math.exp(-k * t)
    return a0 / (1 + k * a0 * t)

def half_life(order: int, a0: float, k: float) -> float:
    return {0: a0 / (2 * k), 1: math.log(2) / k, 2: 1 / (k * a0)}[order]

def diagnose(t: list[float], a: list[float]) -> dict[int, float]:
    """R^2 of the straight-line fit in each linearizing plot: [A], ln[A], 1/[A] versus t."""
    transforms = {0: lambda x: x, 1: math.log, 2: lambda x: 1 / x}
    return {n: statistics.correlation(t, [f(x) for x in a]) ** 2 for n, f in transforms.items()}

def orders_from_initial_rates(c1: float, c2: float, r1: float, r2: float) -> float:
    """Order in one reactant from two experiments where only that reactant changes."""
    return math.log(r2 / r1) / math.log(c2 / c1)

# half-lives depend (or not) on the starting concentration
for order in (0, 1, 2):
    print(order, [round(half_life(order, a0, 0.1), 2) for a0 in (1.0, 0.5)])

# invented pulse-chase data (labelled protein, % remaining) -> which order?
t = [0, 4, 8, 12, 16, 24]
a = [100, 88, 77, 69, 61, 47]
print({n: round(r2, 4) for n, r2 in diagnose(t, a).items()})
slope, intercept = statistics.linear_regression(t, [math.log(x) for x in a])
print("k =", round(-slope, 4), "per h; t1/2 =", round(math.log(2) / -slope, 1), "h")

# invented initial-rate table for rate = k[A]^m [B]^n
print(orders_from_initial_rates(0.10, 0.20, 2.0e-3, 8.0e-3),
      orders_from_initial_rates(0.10, 0.20, 2.0e-3, 4.0e-3))
```

```text
0 [5.0, 2.5]
1 [6.93, 6.93]
2 [10.0, 20.0]
{0: 0.9858, 1: 0.9995, 2: 0.9839}
k = 0.0312 per h; t1/2 = 22.2 h
2.0 1.0
```

The first-order fit is best, but the zero-order $R^2$ is also 0.986: the invented time course covers about one half-life, too short to rule the other orders out by $R^2$ alone.

## Worked example

> [!example] Orders and rate constant from initial rates (invented data)
> | Experiment | $[\mathrm{A}]_0$ (M) | $[\mathrm{B}]_0$ (M) | $v_0$ (M s⁻¹) |
> |---:|---:|---:|---:|
> | 1 | 0.10 | 0.10 | $2.0 \times 10^{-3}$ |
> | 2 | 0.20 | 0.10 | $8.0 \times 10^{-3}$ |
> | 3 | 0.10 | 0.20 | $4.0 \times 10^{-3}$ |
>
> 1. Experiments 1 and 2: $[\mathrm{A}]$ doubles, rate ×4, so $m = \log 4/\log 2 = 2$.
> 2. Experiments 1 and 3: $[\mathrm{B}]$ doubles, rate ×2, so $n = 1$.
> 3. Rate law $v = k[\mathrm{A}]^2[\mathrm{B}]$, third order overall.
> 4. From experiment 1: $k = 2.0 \times 10^{-3}/(0.10^2 \times 0.10) = 2.0$ M⁻² s⁻¹.
> 5. Check with experiment 2: $2.0 \times 0.20^2 \times 0.10 = 8.0 \times 10^{-3}$ M s⁻¹. Consistent.

## Common misconceptions

> [!warning] "Every reaction has a constant half-life"
> Only first-order processes do. Quoting a half-life for a zero- or second-order process without the starting concentration is meaningless.[^chem12]

> [!warning] "The order equals the stoichiometric coefficient"
> Orders are measured. They match the coefficients only for elementary steps.[^chem12]

> [!warning] "A high R² in the ln plot proves first order"
> Over a short time window, every order gives a nearly straight line in every plot. Use a long window, residuals, or the dependence of $t_{1/2}$ on $[\mathrm{A}]_0$.

## Exercises

> [!question] Exercise 1 (L1)
> A first-order reaction has $k = 0.05$ min⁻¹. Find its half-life, and the fraction left after 1 h.

> [!success]- Solution
> $t_{1/2} = \ln 2/0.05 = 13.9$ min. After 60 min: $e^{-0.05 \times 60} = e^{-3} = 0.050$, about 5 %, consistent with $60/13.9 \approx 4.3$ half-lives ($2^{-4.3} \approx 0.05$).

> [!question] Exercise 2 (L1)
> A saturated enzyme converts 2 mM substrate at a constant 0.05 mM/min. How long until the substrate is gone, and what is the half-life starting from 2 mM? From 1 mM?

> [!success]- Solution
> Zero order: $t = [\mathrm{S}]_0/k = 40$ min to exhaustion (in reality the enzyme desaturates near the end and the last part is slower). $t_{1/2} = [\mathrm{S}]_0/(2k)$: 20 min from 2 mM, 10 min from 1 mM. The half-life depends on the start, the signature of zero order.

> [!question] Exercise 3 (L2)
> With the typical half-lives of 9 h (mRNA) and 46 h (protein),[^schwan] compute each decay constant and the time to lose 90 % of a pre-existing pool after synthesis stops. What does this mean for an experiment that inhibits transcription for 12 h?

> [!success]- Solution
> $k_{\mathrm{mRNA}} = \ln 2/9 = 0.077$ h⁻¹, 90 % lost after $\ln 10/k = 29.9$ h. $k_{\mathrm{prot}} = \ln 2/46 = 0.0151$ h⁻¹, 152.8 h. After 12 h of transcription block, a typical mRNA is down to $e^{-0.077 \times 12} = 40$ %, while the protein it encodes has barely changed: protein-level effects of transcriptional perturbations lag by days.

> [!question] Exercise 4 (L2, Python)
> Using `concentration` and `diagnose`, generate a noise-free first-order decay with $k = 0.1$ over 0 to 10 time units, and then over 0 to 50. Compare the three $R^2$ values in each case and conclude.

> [!success]- Solution
> ```python
> for t_end in (10, 50):
>     t = [t_end * i / 10 for i in range(11)]
>     a = [concentration(1, 1.0, 0.1, x) for x in t]
>     print(t_end, {n: round(r2, 4) for n, r2 in diagnose(t, a).items()})
> # 10 {0: 0.9811, 1: 1.0, 2: 0.9811}
> # 50 {0: 0.7153, 1: 1.0, 2: 0.7153}
> ```
>
> Over one half-life and a half ($t = 10$, $k t = 1$), the wrong orders still reach $R^2 = 0.98$; over seven half-lives they fall to 0.72 (the two wrong plots give equal values here, a symmetry of exponential data on an even time grid). With real noise, a short experiment cannot tell the orders apart.

> [!question] Exercise 5 (L3, Python)
> Integrate $d[\mathrm{A}]/dt = -k[\mathrm{A}]$ with $k = 0.1$ and $[\mathrm{A}]_0 = 1$ by Euler's method with step 0.5 up to $t = 10$, and compare with the exact value. Why is the error systematic?

> [!success]- Solution
> ```python
> k, a, dt = 0.1, 1.0, 0.5
> for step in range(int(10 / dt)):
>     a += -k * a * dt
> print(round(a, 4), round(math.exp(-1), 4))
> # 0.3585 0.3679
> ```
>
> Euler multiplies by $(1 - k\,\Delta t) = 0.95$ per step, and $0.95^{20} = 0.3585 < e^{-1}$: the slope is evaluated at the start of each step, where the concentration is highest, so every step overshoots the decay. Halving the step halves the error (first-order method); ODE solvers use higher-order schemes and adaptive steps ([[Ordinary Differential Equation]]).

> [!question] Exercise 6 (L3)
> A protein has a degradation half-life of 46 h in cells that divide every 24 h (invented doubling time). What half-life does a labelling experiment observe, and which process removes most of the labelled protein?

> [!success]- Solution
> $k_{\mathrm{deg}} = \ln 2/46 = 0.0151$ h⁻¹ and $k_{\mathrm{dil}} = \ln 2/24 = 0.0289$ h⁻¹. They add: $k_{\mathrm{obs}} = 0.0440$ h⁻¹, an observed half-life of 15.8 h. Dilution by growth removes about two thirds of the labelled protein; the degradation half-life is recovered only by subtracting $\ln 2/T_d$.

## Mastery checklist

- [ ] 1 Recognized: I can write a rate law, name orders and state the half-life of a first-order process.
- [ ] 2 Understood: I can derive the first-order integrated law and explain why only first-order half-lives are constant.
- [ ] 3 Practiced: I can find orders from initial rates and from linearized plots, and compute half-lives, by hand and in Python.
- [ ] 4 Applied: I can fit decay constants to a turnover time course and correct them for growth dilution.
- [ ] 5 Explained: I can teach where zero, first and pseudo-first order come from, and the pitfalls of short windows and log-scale fits.

## References

[^chem12]: [[Chemistry 2e (OpenStax)]], ch. 12 "Kinetics" (rate laws and reaction orders, the method of initial rates, integrated rate laws for zero-, first- and second-order reactions, graphical determination of order, half-lives).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of enzyme kinetics (maximal velocity at saturating substrate, the Michaelis-Menten model).
[^schwan]: [[Schwanhäusser 2011 - Global Quantification of Mammalian Gene Expression Control]], *Nature* 473:337-342 (mRNA and protein half-lives for more than 5,000 genes in NIH3T3 cells by parallel metabolic pulse labelling; typical half-lives of about 9 h for mRNAs and 46 h for proteins).
