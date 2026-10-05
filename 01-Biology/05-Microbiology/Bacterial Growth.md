---
aliases:
  - Growth Curve
  - Bacterial Growth Curve
  - Microbial Growth
  - Generation Time
  - Binary Fission
  - Croissance bactérienne
tags:
  - type/concept
  - domain/biology
  - domain/mathematics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Prokaryote]]"
  - "[[Bacteria]]"
  - "[[Exponential Function]]"
  - "[[Logarithm]]"
related:
  - "[[Exponential Growth]]"
  - "[[Logistic Growth]]"
  - "[[Linear Regression]]"
  - "[[Least Squares]]"
  - "[[Michaelis-Menten Kinetics]]"
  - "[[Model Calibration]]"
  - "[[Beer-Lambert Law]]"
  - "[[DNA Replication]]"
  - "[[Sequencing Coverage]]"
  - "[[Metagenomics]]"
projects: []
sources:
  - "[[Microbiology (OpenStax)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Monod 1949 - The Growth of Bacterial Cultures]]"
  - "[[Korem 2015 - Growth Dynamics of Gut Microbiota Inferred from Single Metagenomic Samples]]"
---

# Bacterial Growth

> [!abstract]
> A bacterium divides into two, so a well-fed population doubles at regular intervals; in a closed flask this growth runs through lag, exponential, stationary and death phases, and the doubling time is read from the slope of the exponential phase on a logarithmic scale.

## Definition

In microbiology, **growth** is an increase in the number of cells. Bacteria divide by **binary fission**, one cell giving two;[^os10][^m91] the **generation time** (doubling time) $g$ is the time a population takes to double. In a closed (batch) culture, cell numbers follow a **growth curve** with four phases: **lag**, **exponential** (log), **stationary** and **death** (decline).[^m91]

## Why it matters

- **A growth curve is a first data-analysis problem.** Optical density read every few minutes is a time series; estimating $g$ means choosing the exponential window and fitting a line on a log scale ([[Linear Regression]], [[Model Calibration]]). The common mistakes (whole-curve fits, no blank subtraction) bias the result, by a factor of 2.5 on the invented data of the Computational representation.
- **Growth rates can be read from sequencing data.** In a growing bacterial population, read coverage peaks at the replication origin and dips at the terminus; the peak-to-trough ratio measures growth rate from a single metagenomic sample ([[Sequencing Coverage]], [[Metagenomics]]).[^korem]
- **The models recur.** Exponential and [[Logistic Growth]] models, and Monod's growth law, which has the form of [[Michaelis-Menten Kinetics]],[^monod] reappear in systems biology and ecology ([[Exponential Growth]]).

## Core (L1)

### Doubling

With binary fission, $n$ generations multiply the population by $2^n$:[^m91]

$$N = N_0 \cdot 2^{n}, \qquad n = \frac{t}{g}.$$

Under optimal laboratory conditions, *Escherichia coli* can divide about every 20 minutes.[^m91] The exponential itself (rules, base $e$, half-life) is in [[Exponential Function]]; this note is about reading it in real cultures.

### The four phases

![[bacterial-growth-curve-phases.svg]]

| Phase | What the cells do | What the curve does |
|---|---|---|
| Lag | adapt to the new medium, grow in size and make enzymes, divide little | flat |
| Exponential (log) | divide at a constant generation time | straight rising line on a log axis |
| Stationary | nutrients run out and wastes accumulate; new cells balance dying cells | flat |
| Death (decline) | cells die faster than new ones form | falls |

Phases after the microbiology text.[^m91] The phases belong to a **closed** culture: nothing is added or removed after inoculation.

### Measuring growth

Cells can be counted directly under the microscope, counted as colonies after plating dilutions (viable count, in colony-forming units), or estimated from the **turbidity** of the culture, measured as optical density (OD) in a spectrophotometer.[^m91] Turbidity is indirect: it must be calibrated against counts to give cell numbers ([[Beer-Lambert Law]] describes the absorbance side).

## Deeper (L2)

**Linear on a log scale.** Taking $\log_2$ of $N = N_0 2^{t/g}$ gives $\log_2 N = \log_2 N_0 + t/g$: a line of slope $1/g$ in doublings per unit time. Monod defined the growth rate this way, from base-2 logarithms of cell density, in doublings per unit time.[^monod] The **specific growth rate** used in models is $\mu = \ln 2 / g$ per unit time ([[Exponential Function#Deeper (L2)]]).

**Six phases, then four.** Monod divided the batch curve into lag, acceleration, exponential, retardation, stationary and decline phases;[^monod] textbooks merge the two transitions into their neighbours.[^m91] The transitions matter for fitting: points in acceleration or retardation lie below the exponential line.

**Estimating $g$ from data.** Three rules follow from the model.
1. **Subtract the blank** (the OD of medium without cells): a constant offset added to $N$ is not removed by the logarithm and flattens the curve.
2. **Fit only the exponential window**: the slope over the whole curve averages flat and rising parts.
3. **Check linearity**: a high $R^2$ on $\log_2 \mathrm{OD}$ over the chosen points.

**Nutrients set the rate.** Monod showed that the exponential growth rate depends hyperbolically on the concentration of a limiting substrate $S$:[^monod]

$$\mu(S) = \mu_{\max} \frac{S}{K_s + S},$$

where $\mu_{\max}$ is the maximal rate and $K_s$ the concentration giving half of it, the same form as the Michaelis-Menten equation for enzymes. A density-dependent slowdown toward a plateau is modelled by [[Logistic Growth]].

## Advanced (L3)

**Growth from read coverage.** Korem and colleagues showed that the sequencing coverage of a bacterial genome has a single peak at the replication origin and a single trough, and that the peak-to-trough ratio (PTR) quantifies growth rate. They validated it in vitro, in vivo and in complex communities, and for several gut species found that PTRs, but not relative abundances, were associated with inflammatory bowel disease and type II diabetes.[^korem]

**Why the peak exists (a model).** Assume steady exponential growth with doubling time $\tau$, and a chromosome copied from one origin in a fixed time $C$, as in the replication model of [[Prokaryote#Mathematical representation]]. A copy of the terminus completed now was started at the origin $C$ earlier, when the population was $2^{C/\tau}$ times smaller. Hence

$$\mathrm{PTR} = \frac{\text{origin copies}}{\text{terminus copies}} = 2^{C/\tau}, \qquad \tau = \frac{C}{\log_2 \mathrm{PTR}}.$$

With $C \approx 42$ min for *E. coli*,[^os14] $\tau = 20$ min gives PTR $\approx 4.3$, and $\tau = 60$ min gives 1.6. A PTR above 2 means $C > \tau$: new rounds of replication start before earlier ones finish. The model assumes a constant $C$ and steady growth; a real analysis treats PTR as a relative index ([[DNA Replication]]).

## Mathematical representation

| Quantity | Formula | Unit |
|---|---|---|
| Generations elapsed | $n = \log_2(N/N_0) = \log_{10}(N/N_0) / \log_{10} 2 \approx 3.32 \log_{10}(N/N_0)$ | doublings |
| Generation time | $g = t/n$ | time |
| Specific growth rate | $\mu = \ln 2 / g$, so $N = N_0 e^{\mu t}$ | time⁻¹ |
| Fitted slope | $\hat b = \dfrac{\sum_i (t_i - \bar t)(y_i - \bar y)}{\sum_i (t_i - \bar t)^2}$ with $y_i = \log_2(\mathrm{OD}_i - \mathrm{OD}_{\text{blank}})$ | doublings / time |
| Doubling time from the fit | $\hat g = 1/\hat b$ | time |

The slope is the [[Least Squares]] estimate over the exponential window only; $\bar t$ and $\bar y$ are the means over that window.

## Computational representation

```python
import math
from statistics import linear_regression, correlation

# Invented plate-reader data: one culture, OD read every 30 min, blank (medium only) = 0.040
T = list(range(0, 601, 30))                                   # minutes
OD = [0.050, 0.050, 0.051, 0.053, 0.062, 0.082, 0.124, 0.207, 0.369,
      0.640, 0.920, 1.060, 1.110, 1.120, 1.118, 1.110, 1.098, 1.083,
      1.065, 1.047, 1.030]
BLANK = 0.040


def best_exponential_window(t, od, blank, width=4, min_r2=0.99):
    """Fit log2(OD - blank) = a + b t on every run of `width` points; keep the steepest
    run with R^2 >= min_r2. Returns (start, end, slope b, doubling time 1/b, R^2)."""
    y = [math.log2(v - blank) for v in od]
    best = None
    for i in range(len(t) - width + 1):
        ts, ys = t[i:i + width], y[i:i + width]
        slope, _ = linear_regression(ts, ys)
        r2 = correlation(ts, ys) ** 2
        if r2 >= min_r2 and (best is None or slope > best[2]):
            best = (ts[0], ts[-1], slope, 1 / slope, r2)
    return best


start, end, b, g, r2 = best_exponential_window(T, OD, BLANK)
print(f"window {start}-{end} min, slope {b:.4f} doublings/min, g = {g:.1f} min, R2 = {r2:.5f}")
print(f"mu = {math.log(2) / g:.4f} per min = {60 * math.log(2) / g:.2f} per h")

# Two common mistakes: forgetting the blank, and fitting the whole curve
_, _, b_raw, g_raw, _ = best_exponential_window(T, OD, 0.0)
slope_all, _ = linear_regression(T, [math.log2(v - BLANK) for v in OD])
print(f"no blank: g = {g_raw:.1f} min; whole curve: g = {1 / slope_all:.1f} min")
```

```text
window 150-240 min, slope 0.0330 doublings/min, g = 30.3 min, R2 = 0.99998
mu = 0.0229 per min = 1.37 per h
no blank: g = 37.8 min; whole curve: g = 75.3 min
```

`statistics.linear_regression` and `statistics.correlation` need Python 3.10 or later. The sliding window is a simple, transparent rule; its width and $R^2$ threshold are choices to report with the result.

## Worked example

> [!example] Doubling time from two plate counts (invented data)
> A culture in exponential phase goes from $10^3$ to $10^6$ cells per mL in 4 hours.
> 1. **Generations**: $n = \log_2(10^6/10^3) = \log_2 1000 \approx 9.97$ (or $3.32 \times 3 \approx 9.97$).
> 2. **Generation time**: $g = 240 / 9.97 \approx 24.1$ min.
> 3. **Growth rate**: $\mu = \ln 2 / 24.1 \approx 0.0288$ min⁻¹ $\approx 1.73$ h⁻¹.
> 4. **Check**: $10^3 \cdot 2^{240/24.1} \approx 10^3 \cdot 2^{9.96} \approx 10^6$. The calculation is valid only if both counts lie in the exponential phase.

## Common misconceptions

> [!warning] "A species has one doubling time"
> The 20 minutes of *E. coli* hold under optimal conditions;[^m91] the growth rate depends on the medium, for instance on the concentration of the limiting nutrient.[^monod]

> [!warning] "In stationary phase, cells stop dividing"
> The count is flat because new cells balance dying cells.[^m91]

> [!warning] "Fit a line through all the points"
> The lag, stationary and death phases are not exponential. On the invented data above, a whole-curve fit gives 75 min instead of 30.

> [!warning] "OD is the number of cells"
> OD measures turbidity, an indirect estimate that must be calibrated against counts.[^m91]

## Exercises

> [!question] Exercise 1 (L1)
> Name the phase: (a) the count is flat just after inoculation into fresh medium; (b) $\log N$ rises linearly; (c) the count is flat after a long incubation; (d) the viable count falls.

> [!success]- Solution
> (a) Lag; (b) exponential; (c) stationary; (d) death. (a) and (c) are both flat for different reasons: adaptation without much division versus divisions balanced by deaths.

> [!question] Exercise 2 (L1)
> A culture starts at 500 cells per mL with a 30-minute generation time. How many cells per mL after 4 hours of exponential growth?

> [!success]- Solution
> $n = 240/30 = 8$ generations, $N = 500 \cdot 2^8 = 128{,}000 \approx 1.3 \times 10^5$ cells per mL.

> [!question] Exercise 3 (L2)
> With invented Monod parameters $\mu_{\max} = 1.2$ h⁻¹ and $K_s = 0.1$ mM, compute $\mu$ and $g$ at $S = 0.01$, $0.1$ and $1$ mM.

> [!success]- Solution
> $\mu(0.01) = 1.2 \times 0.01/0.11 \approx 0.109$ h⁻¹, $g = \ln 2/\mu \approx 6.4$ h. $\mu(0.1) = 0.6$ h⁻¹, $g \approx 1.16$ h. $\mu(1) = 1.2 \times 1/1.1 \approx 1.09$ h⁻¹, $g \approx 0.64$ h. Above $K_s$ the rate saturates: a tenfold increase from 0.1 to 1 mM less than doubles $\mu$.

> [!question] Exercise 4 (L3, Python)
> Using `best_exponential_window`, estimate $g$ for this second invented culture (OD every 20 min, blank 0.040) with window widths 3 to 6. Is the estimate robust?

> [!success]- Solution
> ```python
> T2 = list(range(0, 481, 20))
> OD2 = [0.045, 0.046, 0.046, 0.047, 0.049, 0.053, 0.060, 0.072, 0.095,
>        0.124, 0.192, 0.281, 0.455, 0.690, 0.905, 1.010, 1.050, 1.062,
>        1.065, 1.066, 1.066, 1.064, 1.061, 1.058, 1.055]
> for width in (3, 4, 5, 6):
>     s, e, b2, g2, r2b = best_exponential_window(T2, OD2, 0.040, width=width)
>     print(width, s, e, round(g2, 1), round(r2b, 4))
> ```
> ```text
> 3 180 220 26.3 0.9948
> 4 180 240 26.4 0.9979
> 5 180 260 27.2 0.9979
> 6 140 240 27.2 0.9988
> ```
> The estimates stay between 26 and 27 min across widths: robust to that choice. Report the window, the width and the threshold with the value.

> [!question] Exercise 5 (L3)
> Using the PTR model with $C = 42$ min, what doubling time corresponds to a PTR of 1.5? Which assumptions would make this estimate wrong for a gut bacterium?

> [!success]- Solution
> $\tau = 42 / \log_2 1.5 \approx 71.8$ min. The model assumes the *E. coli* value of $C$, a constant $C$ across conditions, steady exponential growth, and coverage free of biases from mapping and GC content. For an unknown species these assumptions are rarely checked, so PTR is safer as a relative index, compared between samples of the same species, than converted to minutes.

## Mastery checklist

- [ ] 1 Recognized: I can name the four phases and define generation time.
- [ ] 2 Understood: I can explain each phase biologically and why the exponential phase is a line on a log axis.
- [ ] 3 Practiced: I can compute $g$ and $\mu$ from two counts and fit a doubling time from OD data in Python.
- [ ] 4 Applied: I estimated doubling times from a real plate-reader file and reported the fitting choices.
- [ ] 5 Explained: I can explain Monod's growth law and how coverage ratios reveal growth rates in metagenomes, with their assumptions.

## References

[^m91]: [[Microbiology (OpenStax)]], section 9.1 "How Microbes Grow" (binary fission, generation time, *E. coli* doubling in about 20 minutes under optimal conditions, $N = N_0 2^n$, the growth curve and its phases, methods for counting cells: direct counts, plate counts, turbidity).
[^os10]: [[Biology 2e (OpenStax)]], chapter "Cell Reproduction", section on prokaryotic cell division (binary fission).
[^os14]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function" (replication of the *E. coli* chromosome from one origin in about 42 minutes).
[^monod]: [[Monod 1949 - The Growth of Bacterial Cultures]], *Annual Review of Microbiology* 3:371-394.
[^korem]: [[Korem 2015 - Growth Dynamics of Gut Microbiota Inferred from Single Metagenomic Samples]], *Science* 349(6252):1101-1106.
