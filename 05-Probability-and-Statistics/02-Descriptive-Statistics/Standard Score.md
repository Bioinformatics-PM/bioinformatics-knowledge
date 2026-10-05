---
aliases:
  - z-score
  - Z-Score
  - Standardized Score
  - Standardization
  - Score z
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
  - "[[Measure of Dispersion]]"
related:
  - "[[Normal Distribution]]"
  - "[[Quantile]]"
  - "[[Outlier]]"
  - "[[Heatmap]]"
  - "[[Data Transformation]]"
  - "[[Correlation]]"
  - "[[Principal Component Analysis]]"
  - "[[Hierarchical Clustering]]"
projects: []
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Python Documentation]]"
---

# Standard Score

> [!abstract]
> A standard score (z-score) says how many standard deviations a value lies above or below the mean, which puts measurements made on different scales onto one common, unit-free scale.

## Definition

The **standard score** of a value $x$ in a population with mean $\mu$ and standard deviation $\sigma$ is $z = (x - \mu)/\sigma$: the number of standard deviations between $x$ and the mean, positive above it and negative below.[^os61] For a sample, $\mu$ and $\sigma$ are replaced by the sample mean $\bar x$ and the sample standard deviation $s$ ([[Measure of Central Tendency]], [[Measure of Dispersion]]).

## Why it matters

- **Heatmaps.** Scaling each gene (row) of an expression matrix to z-scores lets one color scale show the pattern of every gene, whatever its level ([[Heatmap]]).
- **Distances.** Before [[Principal Component Analysis]] or [[Hierarchical Clustering]], standardizing variables measured in different units stops the variable with the largest numbers from dominating the distances.[^holmes]
- **Comparisons across scales.** A sample's duplication rate and mapping rate, or a patient's two laboratory values, can be compared once each is expressed relative to its own reference distribution.
- **Unusual values and tests.** Flagging values far from the mean, in a robust form ([[Outlier]]), and test statistics, which are z-scores of an estimate ([[Hypothesis Testing]]).

## Core (L1)

**Compute.** Subtract the mean, divide by the standard deviation. An invented mouse weighs 31 g in a strain with mean 25 g and SD 3 g: $z = (31 - 25)/3 = +2.0$. Its tail measures 98 mm where the strain has mean 90 mm and SD 5 mm: $z = +1.6$. Grams and millimetres cannot be compared, but the z-scores can: the mass is the more unusual measurement.

**Properties.** The z-scores of a data set have mean 0 and standard deviation 1, and no unit. Standardizing only shifts and rescales: the shape of the distribution is unchanged, so skewed data remain skewed.

**From z to percentile, only with a model.** If the data are close to normal, $z$ converts to a percentile through the standard normal CDF: $z = 2$ is near the 97.7th percentile ([[Normal Distribution]], [[Quantile]]).[^os61] Without that model, $z$ is a distance, not a probability.

## Deeper (L2)

### Row scaling of an expression matrix

![[row-scaled-expression-heatmap.svg]]

In panel A, one color scale must span log2 expression from 2 to 12: the highly expressed genes G1 and G2 are dark, the others pale, and the effect of the treatment is barely visible. Panel B replaces each value by its z-score within its gene (row): every row now uses the whole color scale, and G2, G3 and G4 show a clear control versus treated pattern. The price:

1. **Level is lost.** A z-score is relative to the gene's own mean and SD; a red cell can belong to a barely expressed gene.
2. **Noise is amplified.** G1 and G5 have an SD of only 0.15 log2 units, yet their colors are as strong as those of G3, which changes more than fivefold between conditions (about 2.5 log2 units). Filter out low-variance genes before scaling, or show them unscaled.
3. **Scale after transforming.** Use log-transformed values, not raw counts, so that a few huge values do not set the mean and SD ([[Data Transformation]]).

Scaling columns (samples) instead answers another question: it removes differences between samples and keeps differences between genes.

### Sample or population standard deviation

Dividing by $s$ (denominator $n - 1$) or by $\hat\sigma$ (denominator $n$) changes every z-score by the same factor $\sqrt{n/(n-1)}$, 1.095 for six samples. Python offers `statistics.stdev` and `statistics.pstdev`;[^pydocs] libraries differ in their default, so check before comparing z-scores computed by two tools.

### z-scores and distances

For two z-scored profiles $a$ and $b$ over $n$ samples, the squared Euclidean distance is $d^2 = 2(n - 1)(1 - r)$, where $r$ is their Pearson [[Correlation]] (derivation below). Clustering row-scaled genes with Euclidean distance is therefore clustering by correlation: genes group by the shape of their profile, not by their level.

## Advanced (L3)

### Masking: why "|z| > 3" can fail

A single extreme value inflates the standard deviation that is used to judge it. With the sample SD, no value can have $|z| > (n - 1)/\sqrt{n}$ (derivation below): 2.85 for $n = 10$, so a "$|z| > 3$" rule can never flag anything among ten values. In the invented qPCR replicates of the code below, a failed well at 25.0 among values near 10 gets $z = 2.84$. A **robust z-score** replaces the mean by the median and the SD by the median absolute deviation (MAD), summaries that one value cannot drag:[^ph525]

$$\tilde z = \frac{x - \operatorname{med}(x)}{1.4826\,\operatorname{MAD}}.$$

The factor $1.4826 = 1/\Phi^{-1}(0.75)$ makes $1.4826\,\mathrm{MAD}$ estimate $\sigma$ for normal data. The failed well gets $\tilde z = 67$. This is the basis of robust outlier rules ([[Outlier]]).

### The reference group defines the score

A z-score is relative to the distribution it was computed in. Scaling a gene across all samples, across controls only, or across a public reference cohort gives three different numbers for the same measurement, and scores from different data sets are comparable only if their reference distributions are. A test statistic is a z-score whose reference is the sampling distribution of an estimate, $z = (\bar x - \mu_0)/(\sigma/\sqrt n)$; with $\sigma$ estimated from few replicates, it follows a t distribution instead ([[Hypothesis Testing]], [[Normal Distribution]]).

## Mathematical representation

- Sample z-scores: $z_i = (x_i - \bar x)/s$ with $s^2 = \frac{1}{n-1}\sum_i (x_i - \bar x)^2$. Then $\sum_i z_i = 0$ and $\frac{1}{n-1}\sum_i z_i^2 = 1$.
- **Affine invariance.** If $y_i = a x_i + b$ with $a > 0$, then $\bar y = a\bar x + b$, $s_y = a s_x$ and $z(y_i) = z(x_i)$; $a < 0$ flips the signs. Since $\log_{10} x = \log_2 x \cdot \log_{10} 2$, z-scores of log2 and log10 expression are identical.
- **Row scaling** of a matrix $X$ (genes $g$ × samples $j$): $Z_{gj} = (X_{gj} - \bar x_g)/s_g$, undefined when $s_g = 0$.
- **Distance and correlation.** For z-scored $a, b$: $\sum_j a_j^2 = \sum_j b_j^2 = n - 1$ and $\sum_j a_j b_j = (n - 1)\,r$, so $\sum_j (a_j - b_j)^2 = 2(n - 1)(1 - r)$.
- **Bound.** Let $d_i = x_i - \bar x$, $S = \sum_i d_i^2$. Since $\sum_i d_i = 0$, $d_k = -\sum_{i \ne k} d_i$, and by Cauchy-Schwarz $d_k^2 \le (n - 1)(S - d_k^2)$, so $d_k^2/S \le (n - 1)/n$ and $z_k^2 = (n - 1)\,d_k^2/S \le (n - 1)^2/n$.

## Computational representation

```python
import math
import statistics
from statistics import NormalDist

def zscores(xs, sample=True):
    """Standard scores; sample=True divides by the n - 1 standard deviation."""
    m = statistics.mean(xs)
    s = statistics.stdev(xs) if sample else statistics.pstdev(xs)
    return [(x - m) / s for x in xs]

def robust_z(xs):
    """(x - median) / (1.4826 * MAD): a z-score that one extreme value cannot hide."""
    med = statistics.median(xs)
    mad = statistics.median([abs(x - med) for x in xs])
    return [(x - med) / (1.4826 * mad) for x in xs]

expr = {  # invented log2 expression, samples C1 C2 C3 T1 T2 T3 (as in the figure)
    "G1": [12.1, 12.3, 12.0, 12.2, 12.4, 12.1],
    "G3": [2.1, 2.4, 2.0, 4.6, 4.9, 4.4],
    "G5": [3.0, 3.3, 2.9, 3.1, 3.2, 3.0],
}
for gene, values in expr.items():
    print(gene, "sd", round(statistics.stdev(values), 2), [f"{z:+.2f}" for z in zscores(values)])

print("MAD consistency factor 1 / Phi^-1(0.75) =", round(1 / NormalDist().inv_cdf(0.75), 4))

qpcr = [9.8, 10.1, 10.0, 9.9, 10.2, 10.0, 9.7, 10.3, 10.1, 25.0]   # invented, one failed well
print("z of the outlier:", round(zscores(qpcr)[-1], 2), " bound (n-1)/sqrt(n):", round(9 / math.sqrt(10), 2))
print("robust z of the outlier:", round(robust_z(qpcr)[-1], 1))
```

Output:

```text
G1 sd 0.15 ['-0.57', '+0.79', '-1.25', '+0.11', '+1.47', '-0.57']
G3 sd 1.37 ['-0.95', '-0.73', '-1.02', '+0.88', '+1.10', '+0.73']
G5 sd 0.15 ['-0.57', '+1.47', '-1.25', '+0.11', '+0.79', '-0.57']
MAD consistency factor 1 / Phi^-1(0.75) = 1.4826
z of the outlier: 2.84  bound (n-1)/sqrt(n): 2.85
robust z of the outlier: 67.2
```

## Worked example

> [!example] Row-scaling gene G3 (invented)
> log2 expression in C1 to T3: 2.1, 2.4, 2.0, 4.6, 4.9, 4.4.
>
> 1. Mean $20.4/6 = 3.4$; deviations −1.3, −1.0, −1.4, +1.2, +1.5, +1.0; squares sum to 9.34; $s^2 = 9.34/5 = 1.868$, $s = 1.367$.
> 2. z-scores: −0.95, −0.73, −1.02, +0.88, +1.10, +0.73: negative in all controls, positive in all treated samples.
> 3. G5 (2.9 to 3.3) gives z-scores from −1.25 to +1.47, as intense as G3's. On the heatmap the two rows look equally "regulated"; only the unscaled values (or the SD) show that G5 is flat.

## Common misconceptions

> [!warning] "Standardizing makes the data normal"
> It is a shift and a rescaling: skewness, modes and outliers are all preserved. Converting $z$ to a percentile with the normal table is valid only if the data are close to normal.

> [!warning] "A row-scaled heatmap shows expression levels"
> It shows each gene relative to its own mean, in units of its own SD. A strongly colored row may be a flat, noisy gene.

> [!warning] "|z| > 3 always catches outliers"
> The outlier inflates the SD: with ten values, $|z|$ cannot exceed 2.85. Use robust z-scores or other robust rules.

## Exercises

> [!question] Exercise 1 (L1)
> Over 50 previous runs, a sequencing facility recorded a mean duplication rate of 12 % (SD 4 %) and a mean mapping rate of 95 % (SD 1.5 %). A new sample has 18 % duplicates and 91 % mapped reads (invented values). Which metric is more unusual?

> [!success]- Solution
> Duplication: $z = (18 - 12)/4 = +1.5$. Mapping: $z = (91 - 95)/1.5 = -2.67$. The mapping rate is further from its usual value, although its raw difference (4 points) is smaller than that of duplication (6 points).

> [!question] Exercise 2 (L2)
> Two genes have log2 expression (4, 6, 8, 10) and (1, 5, 3, 7) in four samples. Row-scale both. Do their heatmap rows look alike?

> [!success]- Solution
> Both have SD $\sqrt{20/3} = 2.58$. Gene 1: (−1.16, −0.39, +0.39, +1.16); gene 2: (−1.16, +0.39, −0.39, +1.16). Same set of values, different order: the rows share the extreme samples but differ in the middle two. Unscaled, gene 1 would look darker everywhere because its level is higher; scaled, only the pattern remains.

> [!question] Exercise 3 (L2, Python)
> Using `zscores`, check that the z-scores of G3 are the same whether its expression is expressed in log2 or in log10 units. Why?

> [!success]- Solution
> With `g3 = expr["G3"]`, `zscores(g3)` and `zscores([v * math.log10(2) for v in g3])` agree to $10^{-12}$. Changing the log base multiplies every value by the same positive constant; the mean and the SD are multiplied by it too, and it cancels in $(x - \bar x)/s$: z-scores are unit-free.

> [!question] Exercise 4 (L3)
> Nine values equal 0 and one equals $a > 0$. Compute the z-score of $a$ with the sample SD, and compare with the bound $(n - 1)/\sqrt n$. What does the robust z-score do here, and what does that teach?

> [!success]- Solution
> Mean $a/10$; deviations: nine of $-a/10$ and one of $9a/10$; sum of squares $90a^2/100$; $s^2 = (90a^2/100)/9 = a^2/10$. So $z = (9a/10)/(a/\sqrt{10}) = 9/\sqrt{10} = 2.85$, exactly the bound, whatever $a$. The MAD is 0 (more than half of the values equal the median), so the robust z-score is undefined: robust rules need a minimum of spread, and real pipelines guard against a zero MAD. The lesson: with small $n$, use rules that do not let the outlier set its own yardstick, and look at the data.

> [!question] Exercise 5 (L3, Python)
> For two invented profiles a = (5.0, 7.1, 6.2, 9.4, 8.8, 4.9) and b = (3.1, 2.0, 2.2, 0.5, 1.4, 3.3), verify $d^2 = 2(n-1)(1-r)$ between their z-scores, using `statistics.correlation`. What does it imply for clustering z-scored genes?

> [!success]- Solution
> ```python
> a, b = [5.0, 7.1, 6.2, 9.4, 8.8, 4.9], [3.1, 2.0, 2.2, 0.5, 1.4, 3.3]
> d2 = sum((x - y) ** 2 for x, y in zip(zscores(a), zscores(b)))
> r = statistics.correlation(a, b)
> print(round(d2, 6), round(2 * 5 * (1 - r), 6), round(r, 4))   # 19.761575 19.761575 -0.9762
> ```
> The two agree. Distance is a decreasing function of correlation: anti-correlated profiles ($r \approx -1$) are the farthest apart, at nearly the maximum $4(n - 1) = 20$. Euclidean clustering of row-scaled genes groups co-expressed genes regardless of their levels ([[Hierarchical Clustering]]).

## Mastery checklist

- [ ] 1 Recognized: I can write $z = (x - \mu)/\sigma$ and say what $z = -2$ means.
- [ ] 2 Understood: I can explain why z-scores are unit-free, why they do not change the shape of a distribution, and what row scaling hides in a heatmap.
- [ ] 3 Practiced: I can compute z-scores and robust z-scores in Python, row-scale a matrix and prove the distance-correlation identity.
- [ ] 4 Applied: I draw a heatmap of real expression data with and without row scaling, after filtering low-variance genes, and explain the difference.
- [ ] 5 Explained: I can teach masking, the choice of reference group, and when z converts to a probability.

## References

[^os61]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 6 "The Normal Distribution", section 6.1 "The Standard Normal Distribution" (z-scores; the standard normal distribution).
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x, robust statistics (median and median absolute deviation).
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], multivariate analysis: centering and scaling variables before computing distances and principal components.
[^pydocs]: [[Python Documentation]], Library Reference, `statistics` module: `mean`, `stdev`, `pstdev`, `median`, `NormalDist`, `correlation`.
