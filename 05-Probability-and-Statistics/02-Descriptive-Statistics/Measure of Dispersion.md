---
aliases:
  - Dispersion
  - Spread
  - Variability
  - Sample Variance
  - Sample Standard Deviation
  - Interquartile Range
  - IQR
  - Median Absolute Deviation
  - MAD
  - Coefficient of Variation
  - Dispersion (statistique)
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Measure of Central Tendency]]"
  - "[[Level of Measurement]]"
  - "[[Summation Notation]]"
related:
  - "[[Variance]]"
  - "[[Quantile]]"
  - "[[Standard Score]]"
  - "[[Box Plot]]"
  - "[[Outlier]]"
  - "[[Poisson Distribution]]"
  - "[[Overdispersion]]"
  - "[[Highly Variable Gene]]"
  - "[[Single-Cell RNA Sequencing]]"
  - "[[Sampling Distribution]]"
projects: []
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Brennecke 2013 - Accounting for Technical Noise in Single-Cell RNA-Seq Experiments]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Python Documentation]]"
---

# Measure of Dispersion

> [!abstract]
> A measure of dispersion says how spread out the data are around their center: the range, variance and standard deviation use every value, while the interquartile range and the median absolute deviation resist outliers, and the coefficient of variation compares spreads relative to the mean.

## Definition

For observations $x_1, \dots, x_n$ with mean $\bar x$:

- **range**: largest minus smallest value;
- **sample variance** $s^2$: sum of squared deviations from $\bar x$, divided by $n - 1$; **sample standard deviation** $s = \sqrt{s^2}$;[^os2]
- **interquartile range** (IQR): third quartile minus first quartile, the spread of the middle half of the data ([[Quantile]]);[^os2]
- **median absolute deviation** (MAD): the median of the distances $|x_i - \operatorname{med}(x)|$;[^ph525]
- **coefficient of variation** (CV): $s / \bar x$, the standard deviation relative to the mean.[^brennecke]

$s^2$ and $s$ are statistics of a sample; they estimate the population parameters $\sigma^2 = \operatorname{Var}(X)$ and $\sigma$ defined in [[Variance]].

## Why it matters

- **Highly variable genes.** Single-cell analyses look for the genes whose variability across cells exceeds what technical noise predicts at their mean expression: the candidates for true biological variability between cells ([[Highly Variable Gene]]).[^brennecke]
- **Outlier rules.** Values more than 1.5 IQR below the first quartile or above the third are flagged as potential outliers, as in box plots ([[Box Plot]], [[Outlier]]);[^os2] robust z-scores built on the MAD serve the same purpose (Exercise 4).
- **Standardization.** A z-score divides a deviation by a standard deviation ([[Standard Score]]); a heatmap row scaled this way compares genes on one scale.
- **Precision.** The spread of replicates is the noise against which every effect is judged ([[Sampling Distribution]], [[Statistical Inference]]).

## Core (L1)

![[dispersion-robustness-outlier.svg]]

**Toy data A** (invented $\log_2$ expression of one gene in 9 samples): 4.1, 4.4, 4.6, 4.8, 5.0, 5.1, 5.3, 5.6, 5.9; mean 4.98, median 5.0.

| Measure | Value for A | Uses | Units |
|---|---:|---|---|
| Range | 1.8 | two extreme values only | data units |
| Variance $s^2$ | 0.329 | every value, squared | squared units |
| Standard deviation $s$ | 0.574 | every value | data units |
| IQR (inclusive quartiles 4.6 and 5.3) | 0.7 | middle half | data units |
| MAD | 0.4 | every value, by rank | data units |
| CV | 0.115 | $s$ relative to $\bar x$ | none |

**Robustness.** Data B replace 5.9 by 9.8. The range grows from 1.8 to 5.7 and the standard deviation triples (0.574 to 1.708), while the IQR (0.7) and the MAD (0.4) do not move.[^ph525] Pair each center with its spread: mean with standard deviation, median with IQR or MAD ([[Measure of Central Tendency]]).

**CV needs a true zero.** The CV divides by the mean, so it only makes sense for positive, ratio-scale data (counts, concentrations, lengths), not for interval data such as $\log_2$ expression or °C ([[Level of Measurement]]). It is computed above for A only to show the formula.

## Deeper (L2)

- **Why $n - 1$.** Deviations are measured from $\bar x$, which is fitted to the same data, so they are slightly too small; dividing by $n - 1$ makes $s^2$ an unbiased estimator of $\sigma^2$ (proof in [[Variance#Advanced (L3)]], see [[Estimator]]). `statistics.variance` divides by $n - 1$, `statistics.pvariance` by $n$: 0.329 against 0.293 for A. With 3 replicates the two differ by a factor $3/2$.
- **Scaling the MAD.** For normal data the MAD is about $0.6745\,\sigma$, so $1.4826 \times \mathrm{MAD}$ estimates $\sigma$ (derivation below). For A it gives 0.593, close to $s = 0.574$; for B it stays 0.593 while $s$ jumps to 1.708.
- **Quartile conventions.** For small samples, quartile methods disagree: Python's default "exclusive" method gives quartiles 4.5 and 5.45 for A (IQR 0.95), the "inclusive" method 4.6 and 5.3 (IQR 0.7). State the method ([[Quantile]]).[^python]
- **Transformations.** Shifting data does not change $s$, scaling by $a$ multiplies it by $|a|$: $s(ax + b) = |a|\,s(x)$. The CV is unchanged by scaling but not by shifting (Exercise 3). For small CV, the standard deviation of $\ln x$ approximates the CV, because $\ln x \approx \ln \bar x + (x - \bar x)/\bar x$: on a log scale, absolute spread is relative spread.

## Advanced (L3)

**Spread depends on the mean in count data.** A Poisson count has variance equal to its mean, so its squared CV is $1/\mu$; counts from biological replicates vary even more ([[Poisson Distribution]], [[Overdispersion]]).[^holmes8] Two naive rankings of genes therefore fail:

- by **variance**: highly expressed genes win, because their variance is large in absolute terms;
- by **CV²**: lowly expressed genes win, because Poisson noise alone gives them a large CV².

Brennecke and colleagues normalize single-cell counts for library size, compute each gene's mean and $CV^2$, estimate the technical $CV^2$-mean relationship from spike-in controls, and keep the genes whose $CV^2$ is significantly above the technical expectation at their mean.[^brennecke] The toy code below uses the simplest reference, Poisson noise: the ratio of observed to Poisson-expected $CV^2$ is $\dfrac{s^2/\bar x^2}{1/\bar x} = s^2/\bar x$. Real technical noise exceeds Poisson, which is why methods fit the trend from spike-ins or from the data ([[Highly Variable Gene]], [[Single-Cell RNA Sequencing]]).

## Mathematical representation

With sorted values $x_{(1)} \le \dots \le x_{(n)}$ and sample quantiles $\hat Q(p)$ ([[Quantile]]):

$$R = x_{(n)} - x_{(1)}, \qquad s^2 = \frac{1}{n-1}\sum_{i=1}^{n} (x_i - \bar x)^2, \qquad s = \sqrt{s^2},$$

$$\mathrm{IQR} = \hat Q(0.75) - \hat Q(0.25), \qquad \mathrm{MAD} = \operatorname*{median}_i \,\lvert x_i - \operatorname{med}(x)\rvert, \qquad \mathrm{CV} = \frac{s}{\bar x}.$$

**MAD constant.** For $X \sim \mathcal{N}(\mu, \sigma^2)$ ([[Normal Distribution]]), the median $c$ of $|X - \mu|$ satisfies $P(|Z| \le c/\sigma) = \tfrac12$ with $Z$ standard normal, so $\Phi(c/\sigma) = \tfrac34$ and $c = \sigma\,\Phi^{-1}(3/4) \approx 0.6745\,\sigma$, where $\Phi$ is the standard normal cumulative distribution function. Hence $\hat\sigma_{\mathrm{MAD}} = \mathrm{MAD}/\Phi^{-1}(3/4) \approx 1.4826\,\mathrm{MAD}$.

**Poisson reference.** If $X$ is Poisson with mean $\mu$, $\operatorname{Var}(X) = \mu$ ([[Variance]]), so $\mathrm{CV}^2 = \mu/\mu^2 = 1/\mu$, and observed over expected $\mathrm{CV}^2$ equals $s^2/\bar x$.

## Computational representation

```python
import statistics
from statistics import NormalDist

# Invented toy measurements (e.g. log2 expression of one gene in 9 samples).
a = [4.1, 4.4, 4.6, 4.8, 5.0, 5.1, 5.3, 5.6, 5.9]
b = a[:-1] + [9.8]                     # same data, last value replaced by an outlier

MAD_SCALE = 1 / NormalDist().inv_cdf(0.75)   # makes the MAD estimate sigma for normal data


def dispersion(x: list[float]) -> dict[str, float]:
    q1, _, q3 = statistics.quantiles(x, n=4, method="inclusive")
    med = statistics.median(x)
    mad = statistics.median(abs(v - med) for v in x)
    return {
        "range": max(x) - min(x),
        "var": statistics.variance(x),          # sample variance, divides by n - 1
        "sd": statistics.stdev(x),
        "iqr": q3 - q1,
        "mad": mad,
        "mad_scaled": MAD_SCALE * mad,
        "cv": statistics.stdev(x) / statistics.fmean(x),
    }


print(round(MAD_SCALE, 4))
for name, x in (("a", a), ("b", b)):
    print(name, {k: round(v, 3) for k, v in dispersion(x).items()})
print(round(statistics.pvariance(a), 3), round(statistics.variance(a), 3))
print([round(q, 3) for q in statistics.quantiles(a, n=4)], statistics.quantiles(a, n=4, method="inclusive"))

# Highly variable genes: invented normalized counts of 4 genes in 8 cells.
cells = {
    "housekeeping": [100, 104, 96, 110, 92, 101, 99, 98],
    "lowly_expr":   [0, 2, 1, 0, 3, 1, 0, 1],
    "marker":       [0, 0, 0, 40, 38, 0, 45, 0],
    "high_noisy":   [300, 220, 410, 260, 350, 180, 390, 290],
}
print(f"{'gene':12} {'mean':>7} {'var':>8} {'CV2':>6} {'var/mean':>8}")
for gene, x in sorted(cells.items(), key=lambda kv: -statistics.variance(kv[1]) / statistics.fmean(kv[1])):
    m, v = statistics.fmean(x), statistics.variance(x)
    print(f"{gene:12} {m:7.2f} {v:8.1f} {v / m**2:6.2f} {v / m:8.1f}")
```

```text
1.4826
a {'range': 1.8, 'var': 0.329, 'sd': 0.574, 'iqr': 0.7, 'mad': 0.4, 'mad_scaled': 0.593, 'cv': 0.115}
b {'range': 5.7, 'var': 2.919, 'sd': 1.708, 'iqr': 0.7, 'mad': 0.4, 'mad_scaled': 0.593, 'cv': 0.316}
0.293 0.329
[4.5, 5.0, 5.45] [4.6, 5.0, 5.3]
gene            mean      var    CV2 var/mean
marker         15.38    454.0   1.92     29.5
high_noisy    300.00   6457.1   0.07     21.5
lowly_expr      1.00      1.1   1.14      1.1
housekeeping  100.00     28.9   0.00      0.3
```

`statistics.variance` and `stdev` divide by $n - 1$, `pvariance` and `pstdev` by $n$; `statistics.quantiles` uses the exclusive method unless told otherwise.[^python] Sums of squared deviations from the mean, as these functions compute, are numerically safer than $\overline{x^2} - \bar x^2$ ([[Variance#Computational representation]]).

## Worked example

> [!example] Choosing highly variable genes in the toy cells
> 1. **By variance**: high_noisy (6457) ranks first, the marker (454) second. Variance mostly reflects the mean (300 against 15).
> 2. **By CV²**: the marker (1.92) ranks first, then lowly_expr (1.14), whose counts 0 to 3 are just what Poisson noise gives at mean 1 (expected $CV^2 = 1$).
> 3. **By observed over Poisson-expected CV²** ($s^2/\bar x$): marker 29.5, high_noisy 21.5, lowly_expr 1.1, housekeeping 0.3. lowly_expr is now unremarkable, and the marker, expressed in only 3 of 8 cells, ranks first: it separates two groups of cells, which is what a highly variable gene should do.
> 4. **Caveat**: the toy values are invented to make the contrasts extreme (housekeeping even varies less than Poisson noise, 0.3). Real data are compared with a fitted technical trend, not with pure Poisson noise.[^brennecke]

## Common misconceptions

> [!warning] "Standard deviation and standard error are the same"
> $s$ describes the spread of individual observations; the standard error $s/\sqrt{n}$ describes how precisely the mean is known ([[Sampling Distribution]]). Error bars must say which one they show.

> [!warning] "Dividing by $n$ or $n - 1$ makes no difference"
> It does for small samples: with 3 replicates, the two variances differ by 50 %. Use $n - 1$ for a sample, and know which one a function computes.

> [!warning] "A gene with a large variance is a variable gene"
> In count data variance grows with the mean, so raw variance mostly ranks expression level. Compare spread with what is expected at the same mean (Advanced (L3)).

> [!warning] "The CV compares the variability of any two variables"
> Only for ratio-scale, positive data. Shifting the zero changes the CV: the same body temperatures have CV 0.0135 in °C and 0.0016 in kelvin (Exercise 3).

## Exercises

> [!question] Exercise 1 (L1)
> For `2, 4, 4, 4, 5, 5, 7, 9`, compute the range, the sample variance and standard deviation, and the variance and standard deviation dividing by $n$.

> [!success]- Solution
> Mean 5; squared deviations 9, 1, 1, 1, 0, 0, 4, 16, sum 32. Range $9 - 2 = 7$. $s^2 = 32/7 \approx 4.571$, $s \approx 2.138$; dividing by $n$: $32/8 = 4$ and 2. Checked: `statistics` prints `7 4.571 2.138 4 2.0`.

> [!question] Exercise 2 (L1)
> Choose a measure of spread: (a) long-read lengths; (b) symmetric replicate measurements without outliers; (c) the precision of two assays with very different mean signals; (d) data with a suspected outlier.

> [!success]- Solution
> (a) IQR or MAD (skewed); (b) standard deviation; (c) CV, if the signals are ratio-scale; (d) MAD or IQR, which the outlier cannot inflate.

> [!question] Exercise 3 (L2, Python)
> Compute $s$ and the CV of the temperatures `36.5, 37.0, 37.5` in °C and in kelvin ($+273.15$). Explain the result with the transformation rules.

> [!success]- Solution
> ```python
> celsius = [36.5, 37.0, 37.5]
> kelvin = [t + 273.15 for t in celsius]
> for t in (celsius, kelvin):
>     print(round(statistics.stdev(t), 3), round(statistics.stdev(t) / statistics.fmean(t), 5))
> ```
> Output: `0.5 0.01351`, then `0.5 0.00161`. A shift leaves $s$ unchanged ($s(x + b) = s(x)$) but changes the mean, hence the CV. Only the kelvin CV is meaningful, because 0 K is a true zero.

> [!question] Exercise 4 (L2, Python)
> For the value 9.8 in data B, compute the classical z-score $(x - \bar x)/s$, the robust z-score $(x - \operatorname{med})/(1.4826\,\mathrm{MAD})$, and the upper fence $Q_3 + 1.5\,\mathrm{IQR}$. Which rules flag it?

> [!success]- Solution
> ```python
> med = statistics.median(b)
> mad_scaled = MAD_SCALE * statistics.median(abs(v - med) for v in b)
> q1, _, q3 = statistics.quantiles(b, n=4, method="inclusive")
> print(round((9.8 - statistics.fmean(b)) / statistics.stdev(b), 2),
>       round((9.8 - med) / mad_scaled, 1), round(q3 + 1.5 * (q3 - q1), 2))
> ```
> Output: `2.57 8.1 6.35`. The robust z-score (8.1) and the fence (9.8 > 6.35) flag it clearly. The classical z-score is only 2.57, because the outlier inflated both the mean and $s$: an outlier partly hides itself from rules built on $\bar x$ and $s$ ([[Outlier]], [[Standard Score]]).

> [!question] Exercise 5 (L3)
> Show that a Poisson gene has $CV^2 = 1/\mu$. Compute it for $\mu = 1$ and $\mu = 300$, and compare with lowly_expr and high_noisy in the toy cells.

> [!success]- Solution
> $\operatorname{Var}(X) = \mu$ gives $CV^2 = \mu/\mu^2 = 1/\mu$: 1 at $\mu = 1$, about 0.0033 at $\mu = 300$. lowly_expr has $CV^2 = 1.14 \approx 1$: Poisson noise explains it. high_noisy has $CV^2 = 0.07$, about 21 times the Poisson value: small in absolute terms, large relative to its mean. Ranking by raw $CV^2$ would prefer the uninformative gene; the comparison must be made at equal mean.[^brennecke]

## Mastery checklist

- [ ] 1 Recognized: I can define range, variance, standard deviation, IQR, MAD and CV.
- [ ] 2 Understood: I can explain $n - 1$, robustness to outliers, which spread pairs with which center, and when the CV is meaningful.
- [ ] 3 Practiced: I can compute all six measures with `statistics`, scale the MAD, and build classical and robust outlier rules.
- [ ] 4 Applied: I ranked the genes of a real single-cell count matrix by variance, by $CV^2$ and by excess over a mean-dependent trend, and compared the selections.
- [ ] 5 Explained: I can teach why spread depends on the mean in count data and how highly variable gene selection corrects for it.

## References

[^os2]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 2 "Descriptive Statistics" (measures of spread, quartiles and the IQR, outliers).
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x (robust summaries: median and median absolute deviation).
[^brennecke]: [[Brennecke 2013 - Accounting for Technical Noise in Single-Cell RNA-Seq Experiments]], *Nature Methods* 10:1093-1095.
[^holmes8]: [[Modern Statistics for Modern Biology (Holmes)]], ch. 8 "High-Throughput Count Data".
[^python]: [[Python Documentation]], Library Reference, `statistics` module.
