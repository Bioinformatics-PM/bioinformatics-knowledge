---
aliases:
  - Box-and-Whisker Plot
  - Boxplot
  - Box and Whisker Diagram
  - Boîte à moustaches
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Quantile]]"
  - "[[Measure of Dispersion]]"
related:
  - "[[Histogram]]"
  - "[[Outlier]]"
  - "[[Kernel Density Estimation]]"
  - "[[Read Quality Control]]"
  - "[[Phred Quality Score]]"
  - "[[FASTQ Format]]"
  - "[[Count Normalization]]"
projects:
  - "[[10-genomic-pipeline]]"
  - "[[bio-visualization]]"
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Galaxy Training Network - Training Material]]"
---

# Box Plot

> [!abstract]
> A box plot draws a distribution as a box from the first to the third quartile, a line at the median and whiskers toward the extremes, so that dozens of distributions can be compared side by side.

## Definition

A **box plot** (box-and-whisker plot) is a graph of the five-number summary of a quantitative variable: minimum, first quartile $Q_1$, median, third quartile $Q_3$ and maximum. A box spans $Q_1$ to $Q_3$ with a line at the median, and whiskers extend from the box toward the smallest and largest values.[^os2] In a common variant, the whiskers stop at the most extreme values within $1.5 \times \mathrm{IQR}$ of the box and values beyond these **fences**, potential outliers, are drawn as individual points.[^os23]

## Why it matters

- **Many distributions at once.** A histogram per sample does not fit on a page; a box per sample, position or condition does ([[Histogram]]). Box plots are a standard exploratory tool for life-science data.[^ph525]
- **Base quality along reads.** The per-position quality plot of read quality control draws one box per position of the reads ([[Read Quality Control]], [[Phred Quality Score]]).[^gtn]
- **Normalization checks.** Boxes of log expression per sample should line up after normalization; after quantile normalization they are identical ([[Quantile]], [[Count Normalization]]).
- **Group comparisons.** Expression of a gene per genotype, tissue or treatment, before any test.

## Core (L1)

**Anatomy.**

```text
 outlier        whisker              box              whisker
    o       |-----------[ Q1      |median     Q3 ]-----------|
           low end                                        high end
```

The box holds the middle half of the data; its length is the interquartile range ([[Measure of Dispersion]]).

**Reading one box.**

- **Center**: the median line.
- **Spread**: the length of the box (IQR) and of the whiskers.
- **Skewness**: a median close to one end of the box and a longer whisker on the other side indicate a skewed distribution.
- **Extremes**: points beyond the whiskers (with fence whiskers).

**Comparing boxes.** Put the groups on a common axis and compare medians first, then spreads. Boxes that barely overlap suggest a difference worth testing; a box plot is a description, not a test ([[Hypothesis Testing]]).

## Deeper (L2)

### Three whisker conventions

| Whiskers reach | Points drawn beyond | Where you meet it |
|---|---|---|
| minimum and maximum | none | introductory textbooks[^os2] |
| last values within $1.5 \times \mathrm{IQR}$ of the box | values beyond the fences | general-purpose plotting (check your library's default) |
| chosen percentiles, e.g. 10th and 90th | none | per-position quality plots of FastQC[^gtn] |

The same data give different whiskers under each convention (Worked example). A caption must say which one is used.

### What a box plot hides

Five numbers cannot show modality, gaps or sample size. A bimodal sample with no values near its median can have the same box as a bell-shaped one (Exercise 2), and a box drawn from 5 values looks as solid as one drawn from 5,000. Remedies: overlay the individual points (jittered) when $n$ is small, draw violin plots (a box plot combined with a smoothed density, [[Kernel Density Estimation]]) when $n$ is large, and report $n$ per group.[^holmes]

### Points beyond the fences are expected

For normal data, $Q_3 = \mu + 0.674\sigma$ and the IQR is $1.349\sigma$, so the upper fence sits at $\mu + 2.698\sigma$ and 0.70 % of the values fall beyond one fence or the other. Among 20,000 genes, about 140 points beyond the whiskers are expected with no anomaly at all (Exercise 3). Points beyond the fences are candidates to inspect, not errors to delete ([[Outlier]]).

## Advanced (L3)

### Per-position base quality

![[per-position-base-quality-boxplot.svg]]

In this plot, each position of the reads gets a box of the Phred scores observed at that position across all reads ([[FASTQ Format]]); FastQC draws the box from the 25th to the 75th percentile, whiskers at the 10th and 90th percentiles, a red line at the median and a blue line through the means.[^gtn] In the invented data above, the medians stay near Q36 after three slightly lower first positions, then fall and the boxes widen toward the 3' end; from position 34, the lower whiskers (10th percentiles) drop below Q20, an error probability of 1 %. Trimming tools act on such ends ([[Read Quality Control]]).

Two consequences of integer scores: quantiles are integers, so a median can coincide with $Q_1$ or $Q_3$ and the box looks one-sided (Exercise 4); and the plot can be computed exactly in one pass over billions of reads by keeping, for each position, a count of each possible score, then reading quantiles from cumulative counts ([[Quantile]]). Memory is (read length) × (number of possible scores), whatever the number of reads.

## Mathematical representation

- Five-number summary $(x_{(1)}, Q_1, Q_2, Q_3, x_{(n)})$, quartiles as in [[Quantile]]; $\mathrm{IQR} = Q_3 - Q_1$.
- Fences $L = Q_1 - 1.5\,\mathrm{IQR}$ and $U = Q_3 + 1.5\,\mathrm{IQR}$; whisker ends $w_- = \min\{x_i : x_i \ge L\}$ and $w_+ = \max\{x_i : x_i \le U\}$; points drawn: $\{x_i : x_i < L \text{ or } x_i > U\}$.
- Normal reference: $Q_{1,3} = \mu \mp z_{0.75}\sigma$ with $z_{0.75} = 0.6745$, so $U = \mu + 4 z_{0.75}\sigma = \mu + 2.698\sigma$ and $P(X \notin [L, U]) = 2\,(1 - \Phi(2.698)) = 0.0070$.

## Computational representation

```python
import statistics
from statistics import NormalDist

def five_number(xs):
    """Minimum, Q1, median, Q3, maximum; quartiles with the (n + 1) rule of statistics.quantiles."""
    q1, med, q3 = statistics.quantiles(xs, n=4)
    return min(xs), q1, med, q3, max(xs)

def fences(xs, k=1.5):
    """Fences Q1 - k*IQR and Q3 + k*IQR, whisker ends, and the points drawn individually."""
    _, q1, _, q3, _ = five_number(xs)
    lo, hi = q1 - k * (q3 - q1), q3 + k * (q3 - q1)
    inside = [x for x in xs if lo <= x <= hi]
    return (lo, hi), (min(inside), max(inside)), sorted(x for x in xs if x < lo or x > hi)

# invented Phred scores of 20 reads at one position
quals = [38, 37, 37, 36, 36, 36, 35, 35, 35, 34, 34, 33, 33, 32, 30, 28, 26, 20, 12, 2]
print("five-number summary:", five_number(quals))
print("1.5 IQR fences, whiskers, outliers:", fences(quals))
deciles = statistics.quantiles(quals, n=10)
print("percentile whiskers (10th, 90th):", deciles[0], deciles[-1])

Z = NormalDist()
upper = Z.inv_cdf(0.75) + 1.5 * (Z.inv_cdf(0.75) - Z.inv_cdf(0.25))
print("normal data: upper fence at", round(upper, 3), "sd; fraction outside =", round(2 * (1 - Z.cdf(upper)), 5))
```

Output:

```text
five-number summary: (2, 28.5, 34.0, 36.0, 38)
1.5 IQR fences, whiskers, outliers: ((17.25, 47.25), (20, 38), [2, 12])
percentile whiskers (10th, 90th): 12.8 37.0
normal data: upper fence at 2.698 sd; fraction outside = 0.00698
```

## Worked example

> [!example] One position, two conventions (invented scores, output above)
>
> 1. **Box**: $Q_1 = 28.5$, median 34, $Q_3 = 36$; IQR 7.5. The median sits near the top of the box and the lower whisker is long: the scores are skewed toward low values.
> 2. **Fence whiskers**: $L = 28.5 - 11.25 = 17.25$ and $U = 36 + 11.25 = 47.25$. The lower whisker stops at 20, the last score above $L$; scores 12 and 2 are drawn as points. The upper whisker reaches the maximum, 38.
> 3. **Percentile whiskers** (FastQC style): 12.8 and 37. The lower whisker now extends into the low scores, and no point is drawn: the score of 2 has disappeared from the picture.
> 4. **Lesson**: identical data, different pictures. Read the caption before reading the whiskers.

## Common misconceptions

> [!warning] "The whiskers show the minimum and the maximum"
> Only in one convention. With fence whiskers, extremes are separate points; with percentile whiskers, they are not drawn at all.

> [!warning] "Points beyond the whiskers are errors"
> About 0.7 % of perfectly normal data fall beyond the fences. Inspect them; delete only with a documented reason ([[Outlier]]).

> [!warning] "Non-overlapping boxes mean a significant difference, overlapping ones mean none"
> Boxes show the spread of the data, which does not shrink with $n$; the uncertainty of a median does. With thousands of values, overlapping boxes can differ significantly, and with three values, separated boxes can be chance.

## Exercises

> [!question] Exercise 1 (L1)
> Depths of eight samples at a locus (invented): 12, 15, 18, 20, 22, 25, 30, 41. Give the five-number summary (quartiles with the $(n + 1)$ rule) and decide whether 41 is beyond the upper fence.

> [!success]- Solution
> Positions $0.25 \times 9 = 2.25$, 4.5 and 6.75: $Q_1 = 15 + 0.25 \times 3 = 15.75$, median $= 21$, $Q_3 = 25 + 0.75 \times 5 = 28.75$. Summary (12, 15.75, 21, 28.75, 41); IQR 13. Upper fence $28.75 + 19.5 = 48.25 > 41$: 41 is inside, and the upper whisker reaches it.

> [!question] Exercise 2 (L2, Python)
> With `random.Random(8)`, draw 2,000 values from $\mathcal N(0, 1)$, and 2,000 from a mixture of $\mathcal N(\pm 0.674, 0.2^2)$ (alternating signs). Compare their quartiles and the fraction of values within 0.2 of the median.

> [!success]- Solution
> ```python
> import random, statistics
> rng = random.Random(8)
> uni = [rng.gauss(0, 1) for _ in range(2000)]
> bi = [rng.gauss(-0.674 if i % 2 else 0.674, 0.2) for i in range(2000)]
> for xs in (uni, bi):
>     q1, med, q3 = statistics.quantiles(xs, n=4)
>     print(round(q1, 2), round(med, 2), round(q3, 2), round(sum(abs(x - med) < 0.2 for x in xs) / len(xs), 2))
> # -0.65 0.01 0.67 0.16
> # -0.68 0.03 0.69 0.01
> ```
> The boxes are nearly identical, but only 1 % of the bimodal values lie near its median, against 16 % for the normal sample: the median line sits in an empty gap. Overlay the points or a density to see it.

> [!question] Exercise 3 (L3)
> A box plot of the log expression of 20,000 genes, roughly normal, shows about 140 points beyond the whiskers. A colleague wants to remove them as outliers. What do you answer?

> [!success]- Solution
> For normal data, $2\,(1 - \Phi(2.698)) = 0.70\,\%$ of values lie beyond the fences: $20{,}000 \times 0.0070 = 140$ are expected without any anomaly. These points are the tails of the distribution, not errors. The fence rule flags values to inspect; removing them would shrink the variance and bias every downstream test.

> [!question] Exercise 4 (L3)
> At one read position, the Phred scores of 1,000 reads are 20 (50 reads), 25 (100), 30 (300), 35 (400) and 38 (150), invented. Using the lower quantile from cumulative counts, give the 10th, 25th, 50th, 75th and 90th percentiles. What does the box look like, and why?

> [!success]- Solution
> Cumulative counts: 50, 150, 450, 850, 1000. The first score whose cumulative count reaches $p \times 1000$: 10th → 25 (150 ≥ 100); 25th → 30 (450 ≥ 250); median → 35 (850 ≥ 500); 75th → 35 (850 ≥ 750); 90th → 38. The box runs from 30 to 35 with the median on its upper edge, and the whiskers at 25 and 38. With few possible values, quantiles coincide and boxes look one-sided; this is a property of discrete data, not a plotting error.

## Mastery checklist

- [ ] 1 Recognized: I can name the parts of a box plot and the five-number summary.
- [ ] 2 Understood: I can read center, spread and skewness from a box, and explain the three whisker conventions and what a box hides.
- [ ] 3 Practiced: I can compute summaries, fences and whiskers in Python, and per-position quantiles from count arrays.
- [ ] 4 Applied: I read the per-base quality plot of a real FASTQ file and decide on trimming ([[10-genomic-pipeline]]).
- [ ] 5 Explained: I can teach why points beyond fences are expected in large data and why box overlap is not a test.

## References

[^os2]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 2 "Descriptive Statistics" (box plots: the five values, box and whiskers).
[^os23]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 2, section 2.3 "Measures of the Location of the Data" (interquartile range and potential outliers beyond $1.5 \times \mathrm{IQR}$).
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x, exploratory data analysis.
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], graphics of one-dimensional data (box plots, dot plots, violin plots and densities).
[^gtn]: [[Galaxy Training Network - Training Material]], topic "Sequence analysis", tutorial "Quality Control": FastQC per base sequence quality plot (box 25th-75th percentile, whiskers 10th-90th percentile, median and mean lines).
