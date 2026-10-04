---
aliases:
  - Scatterplot
  - Scatter Diagram
  - Scattergram
  - Nuage de points
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Level of Measurement]]"
  - "[[Logarithm]]"
  - "[[Exploratory Data Analysis]]"
related:
  - "[[Correlation]]"
  - "[[Rank Correlation]]"
  - "[[Data Transformation]]"
  - "[[Outlier]]"
  - "[[Principal Component Analysis]]"
  - "[[Batch Effect]]"
  - "[[RNA Sequencing]]"
  - "[[Differential Expression Analysis]]"
projects:
  - "[[bio-visualization]]"
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Python Documentation]]"
---

# Scatter Plot

> [!abstract]
> A scatter plot draws one point per observation at the coordinates given by two quantitative variables, and shows at a glance whether they move together, how tightly, and which observations break the pattern.

## Definition

A **scatter plot** displays paired measurements $(x_i, y_i)$ of two quantitative variables, taken on the same individuals, as points in a plane. It shows whether the variables are related and, if so, the **direction** of the relationship (positive or negative), its **form** (linear or curved) and its **strength** (how closely the points follow it).[^os12]

## Why it matters

- **Replicate agreement.** Plotting the expression of every gene in one replicate against another is the first check that an experiment is reproducible; a swapped or failed sample shows up as a broad or bent cloud ([[RNA Sequencing]], [[Sampling]]).[^ph525]
- **Fold changes.** The MA plot, a rotated scatter plot of two samples or conditions, displays log fold change against mean level ([[Differential Expression Analysis]]).[^holmes]
- **Samples in reduced dimensions.** A PCA score plot is a scatter plot of samples; clusters reveal biological groups or batches ([[Principal Component Analysis]], [[Batch Effect]]).

## Core (L1)

**Building one.** One point per observation. If one variable may influence the other, put it on the horizontal axis. Label both axes with units. When both axes measure the same quantity (two replicates), give them the same range and an equal aspect ratio, and draw the identity line $y = x$: agreement then means "on the diagonal".

**Reading one.**[^os12]

- **Direction**: points rising to the right (positive), falling (negative), or no trend.
- **Form**: a straight band, a curve, or a fan that widens.
- **Strength**: a thin band (strong) or a diffuse cloud (weak).
- **Clusters and outliers**: separate groups of points, isolated points.

![[replicate-scatter-ma-plot.svg]]

Panel A shows two technical replicates of the same invented library. Highly expressed genes lie tightly on $y = x$; below about $2^4$ counts the cloud fans out; genes with no read in one replicate sit on an axis, because $\log_2(0 + 1) = 0$.

## Deeper (L2)

### Log scales and pseudocounts

Counts in these data range from 0 to more than 35,000. On linear axes, a few highly expressed genes would set the scale and all others would collapse into a blob at the origin. The $\log_2(\text{count} + 1)$ transform spreads the range evenly by ratios; the pseudocount 1 avoids $\log 0$ at the price of compressing low counts ([[Data Transformation]], [[Logarithm]]).

### The MA plot

Differences from a diagonal are hard to judge by eye. The MA plot (panel B) uses

$$M = \log_2 \frac{y}{x}, \qquad A = \frac{\log_2 x + \log_2 y}{2},$$

the log ratio against the mean log level: a 45° rotation of panel A (up to axis scaling) that turns the identity line into the horizontal line $M = 0$ and makes fold changes readable on the vertical axis.[^holmes] Both panels show the same 600 genes.

### Overplotting

With 20,000 genes, points pile up and the densest regions look no darker than sparse ones. Use small points with transparency (as in the figure), two-dimensional binning (counting points per hexagon or square and coloring by count) or density contours.

## Advanced (L3)

### The funnel is counting noise

Panel B narrows from left to right even though both replicates come from the same library. If a gene has expected count $\mu$ in each replicate and the counts vary like Poisson variables (reads sampled at random, as `random.choices` does below), the delta method gives $\operatorname{Var}(\log_2 X) \approx 1/(\mu (\ln 2)^2)$, and for the difference of two independent replicates

$$\operatorname{sd}(M) \approx \frac{\sqrt{2/\mu}}{\ln 2}.$$

The prediction is 0.72 at $\mu = 8$ ($A \approx 3$), 0.18 at $\mu = 128$ ($A \approx 7$) and 0.045 at $\mu = 2048$ ($A \approx 11$); the simulation below gives 0.70, 0.20 and 0.047 in the corresponding bins. A twofold difference ($M = 1$) is therefore ordinary for a gene with a handful of reads and exceptional for a gene with thousands. Biological replicates add their own variation on top, which is why count models for differential expression include an extra dispersion term (Exercise 3).[^holmes]

### Correlation summarizes, the plot shows

The Pearson [[Correlation]] between the replicates is 0.99993 on raw counts and 0.986 on the log scale. The first is driven by the few largest genes (the five largest hold a third of the reads); neither reveals that low-count genes disagree by a factor of two. A correlation coefficient measures how well one line fits the whole cloud, which mostly reflects how different the genes' levels are, not how well replicates agree gene by gene. Look at the plot, and prefer [[Rank Correlation]] or the MA plot for agreement.

## Mathematical representation

- Data: pairs $(x_i, y_i)$, $i = 1, \dots, n$; plotted after an optional transform $u_i = \log_2(x_i + c)$, $v_i = \log_2(y_i + c)$ with pseudocount $c$.
- MA coordinates: $M_i = v_i - u_i$, $A_i = (u_i + v_i)/2$, and back: $u_i = A_i - M_i/2$, $v_i = A_i + M_i/2$. In matrix form $(A, M)^\top = \begin{pmatrix} 1/2 & 1/2 \\ -1 & 1 \end{pmatrix} (u, v)^\top$.
- Delta method: if $X$ has mean $\mu$ and variance $\sigma^2$, $\operatorname{Var}(\log_2 X) \approx \sigma^2 / (\mu \ln 2)^2$; for Poisson counts $\sigma^2 = \mu$.
- Pearson correlation $r$ as in [[Correlation]], computed by `statistics.correlation`.[^pydocs]

## Computational representation

```python
import math
import random
import statistics
from collections import Counter

def replicate_counts(seed=3, genes=600, reads=300_000):
    """Two technical replicates: reads drawn independently from the same invented gene abundances."""
    rng = random.Random(seed)
    weights = [rng.lognormvariate(0, 2) for _ in range(genes)]
    reps = []
    for _ in range(2):
        c = Counter(rng.choices(range(genes), weights=weights, k=reads))
        reps.append([c[g] for g in range(genes)])
    return reps

def ma(x, y, pseudo=1):
    """M = log2 ratio y/x and A = mean log2 level, with a pseudocount."""
    lx = [math.log2(v + pseudo) for v in x]
    ly = [math.log2(v + pseudo) for v in y]
    return [b - a for a, b in zip(lx, ly)], [(a + b) / 2 for a, b in zip(lx, ly)]

r1, r2 = replicate_counts()                       # the data of the figure
M, A = ma(r1, r2)
print("Pearson r, raw counts:", round(statistics.correlation(r1, r2), 5))
print("Pearson r, log2(count + 1):", round(statistics.correlation(*[[math.log2(v + 1) for v in r] for r in (r1, r2)]), 5))
print("A bin   genes   sd(M)")
for lo in range(0, 14, 2):
    sel = [m for a, m in zip(A, M) if lo <= a < lo + 2]
    if len(sel) > 2:
        print(f"[{lo:2d}, {lo + 2:2d})  {len(sel):5d}   {statistics.stdev(sel):.3f}")
```

Output:

```text
Pearson r, raw counts: 0.99993
Pearson r, log2(count + 1): 0.98633
A bin   genes   sd(M)
[ 0,  2)     26   1.329
[ 2,  4)     95   0.703
[ 4,  6)    161   0.345
[ 6,  8)    149   0.195
[ 8, 10)    117   0.097
[10, 12)     39   0.047
[12, 14)     10   0.017
```

## Worked example

> [!example] Is a twofold change noise? (technical replicates, invented counts)
>
> | Gene | Counts (rep 1, rep 2) | $M$ | $A$ | predicted sd($M$) | $M$ / sd |
> |---|---|---:|---:|---:|---:|
> | a | 3, 6 | 1.00 | 2.08 | 0.96 | 1.0 |
> | b | 100, 200 | 1.00 | 7.14 | 0.17 | 6.0 |
> | c | 1000, 1100 | 0.14 | 10.03 | 0.063 | 2.2 |
>
> $M$ and $A$ use $\log_2$ of the counts (no pseudocount); sd($M$) uses $\mu$ = the mean of the two counts.
>
> 1. Genes a and b both double. For a, that is one standard deviation of pure counting noise: unremarkable. For b, six: not explained by sampling of reads.
> 2. Gene c changes by only 10 %, yet at more than two standard deviations: with thousands of reads, small changes become detectable.
> 3. The same vertical distance on an MA plot means different things at different $A$, which is why differential expression methods model the noise as a function of the count level ([[Differential Expression Analysis]]).

## Common misconceptions

> [!warning] "A correlation of 0.999 means the replicates agree"
> Here $r = 0.99993$ while low-count genes differ twofold. A high $r$ mostly reflects the wide range of gene levels.

> [!warning] "Genes far from the diagonal at low expression are regulated"
> At low counts, large ratios are expected from sampling alone (the funnel). Judge distance from the diagonal against the noise at that level.

> [!warning] "Each axis may get its own scale"
> For two measurements of the same quantity, unequal ranges or aspect tilt the identity line and fake a bias. Use equal ranges, equal aspect and the line $y = x$.

## Exercises

> [!question] Exercise 1 (L1)
> Six genomic windows (invented) have GC fraction 0.30, 0.38, 0.45, 0.52, 0.60, 0.68 and mean depth 22, 30, 34, 33, 27, 18. Sketch the scatter plot and describe direction, form and strength. Pearson's $r$ is −0.27: what does it miss?

> [!success]- Solution
> Depth rises from 22 to 34, then falls to 18: a strong, curved (inverted-U) relationship with no single direction. $r = -0.27$ suggests a weak negative association because $r$ only measures linear trend. The plot shows a strong dependence of depth on GC content at both extremes, which a correlation coefficient hides.

> [!question] Exercise 2 (L2, Python)
> With the simulated replicates, compute the fraction of reads held by the five genes with the most reads. Why is the raw-count correlation so close to 1?

> [!success]- Solution
> ```python
> top = sorted(range(len(r1)), key=lambda g: r1[g] + r2[g], reverse=True)[:5]
> print(round(sum(r1[g] for g in top) / sum(r1), 3))   # 0.332
> ```
> Five genes out of 600 hold a third of the reads. On raw counts, the cloud is a few points far out on the diagonal plus a dense clump near the origin: the line through the far points explains nearly all the variance, whatever happens in the clump. The log scale gives every order of magnitude its share of the plot.

> [!question] Exercise 3 (L3)
> In biological replicates, suppose a gene's count has variance $\mu + \phi\mu^2$ with $\phi = 0.04$ (a coefficient of variation of 0.2 between individuals on top of counting noise). Compute sd($M$) at $\mu = 8$, 128 and 2048 and compare with technical replicates.

> [!success]- Solution
> Delta method: $\operatorname{Var}(\log_2 X) \approx (\mu + \phi\mu^2)/(\mu \ln 2)^2 = (1/\mu + \phi)/(\ln 2)^2$, so $\operatorname{sd}(M) \approx \sqrt{2(1/\mu + \phi)}/\ln 2$: 0.83, 0.45 and 0.41 (technical: 0.72, 0.18, 0.045). The funnel no longer closes: it levels off at $\sqrt{2\phi}/\ln 2 = 0.41$. At high counts biological variation dominates, which is why count models used for RNA-seq add a dispersion parameter to the Poisson variance.[^holmes]

## Mastery checklist

- [ ] 1 Recognized: I can describe direction, form, strength, clusters and outliers on a scatter plot.
- [ ] 2 Understood: I can explain log axes, pseudocounts, the MA transform and why replicate plots need equal scales.
- [ ] 3 Practiced: I can simulate replicate counts, draw the scatter and MA plots in Python and quantify the funnel.
- [ ] 4 Applied: I check replicate agreement and sample clusters on a real RNA-seq count matrix.
- [ ] 5 Explained: I can teach why the funnel exists, why correlation misleads, and how counting and biological noise differ.

## References

[^os12]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 12 "Linear Regression and Correlation" (scatter plots: direction, form and strength of a relationship).
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x, exploratory data analysis (scatter plots of life-science data).
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], high-throughput count data (MA plots, the negative binomial model with a dispersion parameter).
[^pydocs]: [[Python Documentation]], Library Reference, `statistics` module: `correlation`, `stdev`.
