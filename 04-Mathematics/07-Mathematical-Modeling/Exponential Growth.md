---
aliases:
  - Malthusian Growth
  - Geometric Growth
  - Doubling Time
  - Exponential Model
  - Croissance exponentielle
tags:
  - type/concept
  - domain/mathematics
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Mathematical Model]]"
  - "[[Exponential Function]]"
  - "[[Logarithm]]"
  - "[[Derivative]]"
related:
  - "[[Logistic Growth]]"
  - "[[Bacterial Growth]]"
  - "[[Polymerase Chain Reaction]]"
  - "[[Quantitative Polymerase Chain Reaction]]"
  - "[[DNA Replication]]"
  - "[[Linear Regression]]"
  - "[[Least Squares]]"
  - "[[Model Calibration]]"
  - "[[Branching Process]]"
  - "[[Poisson Distribution]]"
  - "[[Log Fold Change]]"
  - "[[Gene Expression]]"
projects: []
sources:
  - "[[Mathematical Biology (Murray)]]"
  - "[[Calculus (OpenStax)]]"
  - "[[Microbiology (OpenStax)]]"
  - "[[Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR]]"
  - "[[On the Origin of Species (Darwin)]]"
---

# Exponential Growth

> [!abstract]
> A population grows exponentially when every member reproduces at the same rate whatever the population size: its doubling time is constant, it is a straight line on a log scale, and a qPCR cycle threshold is a logarithm of the starting amount for exactly this reason.

## Definition

A quantity $N(t)$ grows **exponentially** when its rate of increase is proportional to its current size:

$$\frac{dN}{dt} = rN \quad\Longrightarrow\quad N(t) = N_0\, e^{rt},$$

where $r > 0$ is the **per-capita (intrinsic) growth rate**, equal to the per-capita birth rate minus the per-capita death rate; for a population this is the Malthusian model.[^murray][^calc] With separate generations or cycles, the discrete form is $N_{n+1} = R\,N_n$, so $N_n = N_0 R^n$ for a constant factor $R$ per step. The **doubling time** is $T_d = \ln 2 / r$.[^calc]

## Why it matters

- **Rates from data.** The doubling time of a culture or a cell line is a fitted parameter of this model; the plate-reader workflow is in [[Bacterial Growth]].
- **qPCR measures logarithms.** Amplification is exponential, so the cycle at which a signal crosses a threshold is a logarithm of the starting amount; relative expression from qPCR rests on this model and on its efficiency assumption ([[Quantitative Polymerase Chain Reaction]], [[Gene Expression]]).[^livak]
- **Log-scale thinking.** Multiplicative processes become additive after a logarithm: fits become [[Linear Regression]], and changes become [[Log Fold Change|log fold changes]].
- **The null model of growth.** Lag phases, plateaus and saturation are recognized as departures from exponential growth, which [[Logistic Growth]] and other models then explain.

## Core (L1)

### From assumption to equation

Assume each individual divides at per-capita rate $b$ and dies at per-capita rate $d$, independently of the others and of how many there are (no shortage of food or space). In a short time $\Delta t$ the population changes by about $(b - d) N \Delta t$, which gives $dN/dt = rN$ with $r = b - d$.[^murray] Differentiating $N_0 e^{rt}$ gives $r N_0 e^{rt} = rN$: the solution checks ([[Derivative]]). Everything else in this note follows from that one assumption, and every failure of exponential growth is a failure of it.

### Doubling time and the rule of 70

From $e^{r T_d} = 2$: $T_d = \ln 2 / r$. The number of doublings between $N_0$ and $N$ is $\log_2(N / N_0)$ ([[Logarithm]]). For growth of $p$ % per unit time, $r = \ln(1 + p/100) \approx p/100$, so $T_d \approx 69.3 / p \approx 70 / p$: 7 % per hour doubles in about 10 hours.

| Doubling time | $r$ (per hour) | Factor per hour | Factor per day |
|---|---|---|---|
| 20 min | 2.08 | 8 | $4.7 \times 10^{21}$ |
| 1 h | 0.693 | 2 | $1.7 \times 10^{7}$ |
| 24 h | 0.0289 | 1.029 | 2 |

**On a log axis.** Taking logarithms, $\ln N = \ln N_0 + rt$: exponential growth is a straight line on a semi-log plot, with slope $r$ (or $1/T_d$ in $\log_2$ units) ([[Logarithm#Linearizing exponentials]]). Curvature on that plot is the signal that the model no longer holds.

### Bio: bacteria in log phase

Under optimal conditions *E. coli* can divide about every 20 minutes, but a batch culture grows exponentially only during its exponential (log) phase, between lag and stationary phases.[^micro] The first row of the table shows why: no culture can keep multiplying by $4.7 \times 10^{21}$ per day.

### Bio: PCR, where one cycle is a factor of two

Each PCR cycle can copy every target molecule, so the product grows by a factor $1 + E$ per cycle, where the efficiency $E$ is at most 1.[^livak] The detector crosses a fixed threshold $N_\theta$ at the **threshold cycle** $C_t$ where $N_0 (1 + E)^{C_t} = N_\theta$. With $E = 1$, $C_t = \log_2(N_\theta / N_0)$: **halving the starting template delays $C_t$ by exactly one cycle**, and a tenfold dilution by $\log_2 10 \approx 3.32$ cycles.

![[qpcr-amplification-curves-ct.svg]]

On a linear axis (A) the curves are sigmoids that look flat until late; on a log axis (B) their exponential parts are parallel lines, shifted by the same number of cycles for each tenfold dilution. The plateau is where the exponential assumption fails.

## Deeper (L2)

### Fitting on a log scale

To estimate $r$ from measurements $(t_i, N_i)$ in the exponential window, fit the straight line $\ln N_i = \ln N_0 + r t_i + \varepsilon_i$ by least squares ([[Least Squares]], [[Linear Regression]]); $\hat T_d = \ln 2 / \hat r$. This assumes **multiplicative** noise: each measurement is off by a similar percentage, which a log turns into constant additive noise. Two consequences follow from $d(\ln N) = dN / N$:

- **Small values are noisy on a log scale.** An absolute error $\delta$ near the detection limit becomes a log error $\delta / N$, large when $N$ is small: drop or down-weight points near the baseline, and subtract the blank first ([[Bacterial Growth#Deeper (L2)]]).
- **Fitting on the original scale weights the largest values.** Least squares on $N$ itself lets the last points dominate, so one late point that is starting to bend can drag the whole fit (Exercise 5).

Because $T_d = \ln 2 / r$, a relative error in $\hat r$ gives the same relative error in $\hat T_d$: $|d T_d / T_d| = |dr / r|$. Report the window, the number of points and the fit quality with the value ([[Model Calibration]]).

### qPCR: from cycles to copies

Solving $N_0 (1 + E)^{C_t} = N_\theta$ for $C_t$:

$$C_t = \frac{\log_{10} N_\theta - \log_{10} N_0}{\log_{10}(1 + E)}.$$

- **Standard curve.** $C_t$ is linear in $\log_{10} N_0$ with slope $s = -1/\log_{10}(1 + E)$, so a dilution series of known amounts gives the efficiency, $E = 10^{-1/s} - 1$. Perfect doubling gives $s = -3.32$ cycles per tenfold dilution. An unknown is then read off the line (Worked example).
- **Efficiency from one curve.** In the exponential window the fluorescence, proportional to product, follows $F_c = F_0 (1 + E)^c$, so the slope of $\ln F_c$ against $c$ is $\ln(1 + E)$ (Computational representation).
- **Comparing samples.** Two samples measured with the same assay differ in starting amount by $(1 + E)^{\Delta C_t}$. The $2^{-\Delta\Delta C_t}$ method normalizes the target to a reference gene and to a calibrator sample and converts cycles with base 2, which assumes efficiencies close to 100 % and similar for target and reference.[^livak] If the true efficiency is 0.9, assuming 2 overestimates a ratio by $(2/1.9)^{\Delta C_t}$: 1.05-fold for one cycle, 1.67-fold for ten (computed below).

## Advanced (L3)

### Exponential phases end

Real growth slows: nutrients run out and cultures enter stationary phase;[^micro] PCR runs out of primers and nucleotides, a ceiling that [[Stoichiometry#Worked example]] computes for a typical mix. On a semi-log plot the decline appears as downward curvature; its simplest model adds a carrying capacity ([[Logistic Growth]]). Extrapolating an exponential beyond its window is the classic modeling error.

> [!info] Geometric increase in the history of biology
> Darwin argued that every species tends to increase in a geometrical ratio, so that more individuals are produced than can survive, and a struggle for existence follows;[^darwin] the continuous model carries the name of Malthus.[^murray]

### Small numbers: the stochastic start

With few template molecules, amplification is random: in each cycle each molecule is copied with probability $E$. This is a **Galton-Watson branching process** ([[Branching Process]]). Its mean follows the deterministic model exactly, $E[N_n] = N_0 (1 + E)^n$, but the early cycles leave a relative spread that later cycles do not remove: the coefficient of variation of the final amount tends to $\sqrt{(1 - E)/((1 + E) N_0)}$ (derived below). On top of that, the number of molecules pipetted into a well is Poisson-distributed with mean $\lambda$ ([[Poisson Distribution]]): a well is empty with probability $e^{-\lambda}$, 37 % at $\lambda = 1$. Combining both sources, the standard deviation of $C_t$ between replicate wells is about

$$\mathrm{SD}(C_t) \approx \frac{1}{\ln(1 + E)} \sqrt{\frac{2}{(1 + E)\,\lambda}},$$

0.16 cycles at 100 copies and 0.5 at 10 copies for $E = 0.9$ (Exercise 6). Low-copy replicates scatter for reasons of counting, not of technique, and a $\Delta C_t$ of half a cycle between single wells at about 10 copies means little.

## Mathematical representation

- **Continuous**: $\dot N = rN$, $N(t) = N_0 e^{rt}$. **Discrete**: $N_{n+1} = R N_n$, $N_n = N_0 R^n$. Same curve when $r = \ln R / \Delta t$ for steps of length $\Delta t$ ([[Exponential Function#Deeper (L2)]]).
- **Doubling**: $T_d = \ln 2 / r = \Delta t \ln 2 / \ln R$; doublings between $N_0$ and $N$: $\log_2(N / N_0)$.
- **Log-linear fit** on the window $i = 1, \dots, m$, with $y_i = \ln N_i$: $\hat r = \dfrac{\sum_i (t_i - \bar t)(y_i - \bar y)}{\sum_i (t_i - \bar t)^2}$, $\hat N_0 = e^{\bar y - \hat r \bar t}$. Error propagation: $\mathrm{Var}(\ln N) \approx \mathrm{Var}(N) / N^2$.
- **qPCR**: $N_c = N_0 (1 + E)^c$; $C_t = \log_{1+E}(N_\theta / N_0)$; standard curve $C_t = a + s \log_{10} N_0$ with $s = -1/\log_{10}(1 + E)$; ratio of two samples $N_0^{A} / N_0^{B} = (1 + E)^{C_t^{B} - C_t^{A}}$.
- **Branching process.** One molecule leaves 1 copy (probability $1 - E$) or 2 (probability $E$): offspring mean $m = 1 + E$, variance $\sigma^2 = E(1 - E)$. By the law of total variance, $V_{n+1} = m^2 V_n + \sigma^2 E[N_n]$. Starting from one molecule, write $V_n = m^{2n} w_n$: $w_{n+1} = w_n + \sigma^2 m^{-n-2}$, so $w_\infty = \sigma^2 / (m(m - 1)) = (1 - E)/(1 + E)$, the limiting squared coefficient of variation. For $N_0$ independent molecules divide by $N_0$; for $N_0 \sim \mathrm{Poisson}(\lambda)$, $\mathrm{CV}^2 = \big(1 + \tfrac{1 - E}{1 + E}\big)/\lambda = 2/((1 + E)\lambda)$. Since $C_t$ is $-\ln N / \ln(1 + E)$ up to a constant, $\mathrm{SD}(C_t) \approx \mathrm{CV} / \ln(1 + E)$.

## Computational representation

```python
import math
from statistics import linear_regression


def fit_exponential(t: list[float], n: list[float]) -> tuple[float, float, float]:
    """Least-squares line through (t, ln n). Returns rate r, N0 and doubling time ln2 / r."""
    slope, intercept = linear_regression(t, [math.log(v) for v in n])
    return slope, math.exp(intercept), math.log(2) / slope


# 1. qPCR standard curve: invented Ct values of a tenfold dilution series
COPIES = [1e6, 1e5, 1e4, 1e3, 1e2, 1e1]
CT = [15.99, 19.30, 22.86, 26.25, 29.77, 33.12]
slope, intercept = linear_regression([math.log10(c) for c in COPIES], CT)
efficiency = 10 ** (-1 / slope) - 1
print(f"slope {slope:.3f} cycles per tenfold, intercept {intercept:.2f}, E = {efficiency:.3f}")
print(f"unknown sample at Ct 27.30: {10 ** ((27.30 - intercept) / slope):.0f} copies")

# 2. Efficiency from the exponential window of one amplification curve (invented, baseline subtracted)
cycles = [14, 15, 16, 17, 18]
fluorescence = [0.0021, 0.0040, 0.0078, 0.0149, 0.0285]
r, _, _ = fit_exponential(cycles, fluorescence)
print(f"factor per cycle {math.exp(r):.3f}, E = {math.exp(r) - 1:.3f}")

# 3. Converting a Ct difference with E = 1 when the true efficiency is 0.9
for d_ct in (1, 3.32, 5, 10):
    print(f"dCt = {d_ct:<5} 2^dCt = {2 ** d_ct:7.1f}   1.9^dCt = {1.9 ** d_ct:6.1f}   "
          f"overestimate x{(2 / 1.9) ** d_ct:.2f}")
```

```text
slope -3.441 cycles per tenfold, intercept 36.59, E = 0.952
unknown sample at Ct 27.30: 502 copies
factor per cycle 1.921, E = 0.921
dCt = 1     2^dCt =     2.0   1.9^dCt =    1.9   overestimate x1.05
dCt = 3.32  2^dCt =    10.0   1.9^dCt =    8.4   overestimate x1.19
dCt = 5     2^dCt =    32.0   1.9^dCt =   24.8   overestimate x1.29
dCt = 10    2^dCt =  1024.0   1.9^dCt =  613.1   overestimate x1.67
```

`statistics.linear_regression` needs Python 3.10 or later. The standard curve and the single-curve slope are two independent estimates of $E$; when they disagree, inspect the window and the dilution series before trusting either.

## Worked example

> [!example] Absolute quantification with a standard curve (invented data)
> A tenfold dilution series from $10^6$ to $10^1$ copies gives $C_t$ = 15.99, 19.30, 22.86, 26.25, 29.77, 33.12.
> 1. **Fit** $C_t$ against $\log_{10}$ copies: slope $s = -3.441$, intercept $a = 36.59$ (output above).
> 2. **Efficiency**: $E = 10^{1/3.441} - 1 = 0.952$, close to but below perfect doubling ($s = -3.32$).
> 3. **Unknown** at $C_t = 27.30$: $\log_{10} N_0 = (27.30 - 36.59)/(-3.441) = 2.70$, so $N_0 \approx 500$ copies. It lies inside the calibrated range, so no extrapolation is needed.
> 4. **One cycle later** ($C_t = 28.30$) would mean $502 / 1.952 \approx 257$ copies: about half, as the "one cycle, one doubling" rule says, corrected for $E$.

## Common misconceptions

> [!warning] "Exponential means fast"
> It means a constant relative rate. A cell line doubling every 24 hours grows exponentially; on a linear axis, the early part of any exponential looks flat.

> [!warning] "Fitting on the linear scale or on the log scale gives the same answer"
> They assume different noise and weight the points differently. On the invented data of Exercise 5, the two doubling times differ by 10 %.

> [!warning] "One qPCR cycle is a factor of two"
> Only at $E = 1$. At $E = 0.9$ it is 1.9, and assuming 2 inflates a ten-cycle difference 1.67-fold.[^livak]

## Exercises

> [!question] Exercise 1 (L1)
> A strain doubles every 30 minutes. Give $r$ per hour, and the time to go from $10^3$ to $10^9$ cells in exponential growth.

> [!success]- Solution
> $r = \ln 2 / 0.5\ \text{h} = 1.386$ h⁻¹. Doublings: $\log_2(10^6) = 6 \log_2 10 \approx 19.9$, so about 10 hours.

> [!question] Exercise 2 (L1)
> A population grows by 7 % per hour. Estimate its doubling time with the rule of 70, then exactly.

> [!success]- Solution
> Rule of 70: $70 / 7 = 10$ h. Exactly: $\ln 2 / \ln 1.07 = 0.693 / 0.0677 = 10.24$ h. The approximation $\ln(1 + x) \approx x$ is good for small rates.

> [!question] Exercise 3 (L1)
> In the same qPCR assay, sample B crosses the threshold 2 cycles after sample A. How much starting template did B have relative to A, with $E = 1$ and with $E = 0.9$?

> [!success]- Solution
> $E = 1$: $2^{-2} = 1/4$. $E = 0.9$: $1.9^{-2} = 1/3.61 \approx 0.28$. Later crossing means less template.

> [!question] Exercise 4 (L2)
> Two standard curves have slopes $-3.6$ and $-3.0$ cycles per tenfold dilution. Compute both efficiencies and comment.

> [!success]- Solution
> $10^{1/3.6} - 1 = 0.896$: a plausible, somewhat low efficiency. $10^{1/3.0} - 1 = 1.154$: more than doubling per cycle, impossible for this model, so the curve contains an artifact: typically the concentrated points crossing too late (inhibition) or dilution errors. Inspect the series rather than use $E > 1$.

> [!question] Exercise 5 (L2, Python)
> Fit invented hourly counts $N$ = 1050, 1320, 2160, 2770, 4160, 5490, 8820, 11500, 14100 ($t$ = 0 to 8 h) on the log scale with `fit_exponential`, and on the original scale by least squares (for each $r$ the best $N_0$ has a closed form). Compare doubling times and relative residuals.

> [!success]- Solution
> ```python
> T = [0, 1, 2, 3, 4, 5, 6, 7, 8]                                  # hours
> N = [1050, 1320, 2160, 2770, 4160, 5490, 8820, 11500, 14100]     # invented counts
>
> def fit_linear_scale(t, n):
>     """Least squares on the original scale: for each r, the best N0 is closed-form."""
>     best = None
>     for i in range(1, 10001):
>         r = i * 1e-4
>         e = [math.exp(r * ti) for ti in t]
>         n0 = sum(ni * ei for ni, ei in zip(n, e)) / sum(ei * ei for ei in e)
>         sse = sum((ni - n0 * ei) ** 2 for ni, ei in zip(n, e))
>         if best is None or sse < best[0]:
>             best = (sse, r, n0)
>     return best[1], best[2]
>
> r_log, n0_log, td_log = fit_exponential(T, N)
> r_lin, n0_lin = fit_linear_scale(T, N)
> print(f"log scale:    r = {r_log:.4f}/h, N0 = {n0_log:.0f}, Td = {td_log:.2f} h")
> print(f"linear scale: r = {r_lin:.4f}/h, N0 = {n0_lin:.0f}, Td = {math.log(2) / r_lin:.2f} h")
> for name, r, n0 in (("log", r_log, n0_log), ("linear", r_lin, n0_lin)):
>     print(name, [f"{100 * (ni / (n0 * math.exp(r * ti)) - 1):+.0f}%" for ti, ni in zip(T, N)])
> # log scale:    r = 0.3397/h, N0 = 1032, Td = 2.04 h
> # linear scale: r = 0.3100/h, N0 = 1236, Td = 2.24 h
> # log ['+2%', '-9%', '+6%', '-3%', '+4%', '-3%', '+11%', '+3%', '-10%']
> # linear ['-15%', '-22%', '-6%', '-12%', '-3%', '-6%', '+11%', '+6%', '-4%']
> ```
> The linear-scale fit sacrifices the first points ($-15$ %, $-22$ %) to follow the large late values and gives a 10 % longer doubling time. The log fit spreads relative errors evenly, and its last residual ($-10$ %) flags the possible start of a slowdown: refit without the last point before reporting.

> [!question] Exercise 6 (L3, Python)
> Simulate qPCR wells with Poisson-distributed templates (mean $\lambda$ = 1, 10, 100, 1000), each molecule copied with probability $E = 0.9$ per cycle until 1000 copies, then deterministic growth to a threshold of $10^{10}$. Compare the standard deviation of $C_t$ with the approximation above.

> [!success]- Solution
> ```python
> import random
> from statistics import mean, pstdev
>
> def poisson(lam: float, rng: random.Random) -> int:
>     """Number of arrivals of a unit-rate Poisson process in [0, lam]."""
>     k, t = 0, rng.expovariate(1.0)
>     while t < lam:
>         k, t = k + 1, t + rng.expovariate(1.0)
>     return k
>
> def ct_of_well(lam: float, eff: float, threshold: float, rng: random.Random, switch: int = 1000):
>     """Ct of one well: Poisson templates, stochastic copying until `switch` copies, then deterministic."""
>     n = poisson(lam, rng)
>     if n == 0:
>         return None                                    # empty well: no amplification
>     cycle = 0
>     while n < switch:
>         n += sum(rng.random() < eff for _ in range(n))
>         cycle += 1
>     return cycle + math.log(threshold / n) / math.log(1 + eff)
>
> rng, EFF = random.Random(3), 0.9
> for lam in (1, 10, 100, 1000):
>     cts = [ct_of_well(lam, EFF, 1e10, rng) for _ in range(2000)]
>     ok = [c for c in cts if c is not None]
>     approx = math.sqrt(2 / ((1 + EFF) * lam)) / math.log(1 + EFF)
>     print(f"lambda {lam:5}: empty {1 - len(ok) / len(cts):.3f}, mean Ct {mean(ok):5.2f}, "
>           f"SD {pstdev(ok):.3f} (approx {approx:.3f})")
> # lambda     1: empty 0.379, mean Ct 35.36, SD 0.811 (approx 1.598)
> # lambda    10: empty 0.000, mean Ct 32.38, SD 0.581 (approx 0.505)
> # lambda   100: empty 0.000, mean Ct 28.71, SD 0.159 (approx 0.160)
> # lambda  1000: empty 0.000, mean Ct 25.11, SD 0.050 (approx 0.051)
> ```
> The approximation holds from about 100 copies; at $\lambda = 1$, 38 % of wells are empty ($e^{-1} = 0.37$) and the surviving wells, all started from at least one molecule, are less variable than the large-$\lambda$ formula predicts. Mean $C_t$ shifts by about $\ln 10 / \ln 1.9 = 3.59$ cycles per tenfold, as the deterministic model says.

## Mastery checklist

- [ ] 1 Recognized: I can write $dN/dt = rN$ and $N_0 R^n$, and define per-capita rate and doubling time.
- [ ] 2 Understood: I can explain why exponential growth is a line on a log axis, why one qPCR cycle means a factor $1 + E$, and when the model stops holding.
- [ ] 3 Practiced: I can fit growth rates on a log scale, build a qPCR standard curve and compute efficiencies and copy numbers in Python.
- [ ] 4 Applied: I estimated a doubling time or a qPCR efficiency from real data and reported the window and the assumptions.
- [ ] 5 Explained: I can teach the noise model behind log-scale fitting, the efficiency assumption of $2^{-\Delta\Delta C_t}$, and why low-copy qPCR replicates scatter (branching and Poisson sampling).

## References

[^murray]: [[Mathematical Biology (Murray)]], 3rd ed. (2002), Volume I, continuous population models for a single species (the Malthusian model, birth minus death rate).
[^calc]: [[Calculus (OpenStax)]], Volume 1, exponential growth and decay models (growth rate, doubling time); section not verified.
[^micro]: [[Microbiology (OpenStax)]], section 9.1 "How Microbes Grow" (*E. coli* doubling in about 20 minutes under optimal conditions; lag, exponential, stationary and death phases).
[^livak]: [[Livak 2001 - Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR]], *Methods* 25:402-408 (exponential amplification with an efficiency, threshold cycle, the $2^{-\Delta\Delta C_T}$ method and its assumptions).
[^darwin]: [[On the Origin of Species (Darwin)]], 1st ed. (1859), chapter on the struggle for existence (geometrical ratio of increase).
