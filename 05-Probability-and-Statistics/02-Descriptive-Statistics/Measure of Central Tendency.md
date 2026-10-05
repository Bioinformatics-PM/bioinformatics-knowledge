---
aliases:
  - Central Tendency
  - Measures of Center
  - Sample Mean
  - Median
  - Mode (Statistics)
  - Geometric Mean
  - Tendance centrale
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Frequency Distribution]]"
  - "[[Level of Measurement]]"
  - "[[Summation Notation]]"
related:
  - "[[Expected Value]]"
  - "[[Measure of Dispersion]]"
  - "[[Quantile]]"
  - "[[Outlier]]"
  - "[[Histogram]]"
  - "[[Log Fold Change]]"
  - "[[Size Factor Estimation]]"
  - "[[Count Normalization]]"
  - "[[Law of Large Numbers]]"
projects: []
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Anders 2010 - Differential Expression Analysis for Sequence Count Data]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Python Documentation]]"
---

# Measure of Central Tendency

> [!abstract]
> The mean, the median and the mode each summarize a dataset by one "typical" value; they agree on symmetric data and disagree, instructively, on skewed data, outliers and ratios.

## Definition

For observations $x_1, \dots, x_n$, the **mean** is their sum divided by $n$, the **median** is the middle value once the data are sorted (the average of the two middle values when $n$ is even), and the **mode** is the most frequent value.[^os2] Computed from a sample, the mean $\bar x$ is a statistic that estimates the population mean $\mu$, the [[Expected Value]] of the variable ([[Sampling]]).

## Why it matters

- **Read lengths.** A long-read run is better summarized by its median read length than by its mean, because a few very long reads pull the mean up (Core (L1)); the length-weighted [[Quantile|N50]] complements it.
- **Normalization.** RNA-seq libraries are scaled by **median-of-ratios** size factors, a median chosen because it ignores the few genes that change strongly between samples.[^anders]
- **Ratios.** Fold changes are averaged on a log scale, which is a geometric mean on the original scale ([[Log Fold Change]]).
- **Choosing the center is choosing a model.** The mean belongs with the normal distribution and least squares; the median with robust and rank-based methods ([[Nonparametric Statistics]]).

## Core (L1)

**Toy long-read lengths** (invented, bp): 850, 1200, 1500, 2100, 2300, 2900, 3400, 4800, 7600, 25000.

- Mean $= 51{,}650/10 = 5165$ bp. Median: $n = 10$ is even, so it averages the 5th and 6th sorted values, $(2300 + 2900)/2 = 2600$ bp.
- Seven of the ten reads are shorter than the mean: the single 25 kb read pulls it to the right.

**Skewness.** In a right-skewed distribution (long tail to the right) the mean is typically larger than the median, which is larger than the mode; in a left-skewed one the order reverses; in a symmetric one they coincide.[^os2]

![[skewed-distribution-mean-median-mode.svg]]

**Outliers.** Replace the 25 kb read by a mis-parsed record of 250,000 bp: the mean jumps to 27,665 bp, the median stays at 2600 bp. The median is a **robust** summary: one aberrant value cannot move it far.[^ph525]

**Mode.** The mode is the only center for nominal data (the most common genotype) and is natural for discrete data with repeated values (trimmed Illumina reads: most are still at full length). Continuous measurements rarely repeat exactly, so their mode is read from a grouped table as the most frequent class ([[Frequency Distribution]]). A dataset can have several modes.

| Data | Use | Why |
|---|---|---|
| Nominal | mode | no order, no arithmetic ([[Level of Measurement]]) |
| Ordinal | median | order but no distances |
| Quantitative, roughly symmetric | mean (and median) | the mean uses every value |
| Quantitative, skewed or with outliers | median | robust |
| Ratios, fold changes | geometric mean | symmetric on the log scale |

## Deeper (L2)

- **What each center optimizes.** The mean minimizes the sum of squared deviations $\sum_i (x_i - c)^2$ (set the derivative $-2\sum_i (x_i - c)$ to zero: $c = \bar x$). The median minimizes the sum of absolute deviations $\sum_i |x_i - c|$: moving $c$ to the right adds 1 to the slope for every point left of $c$ and subtracts 1 for every point right of it, so the slope is zero where half the points lie on each side. For even $n$, every $c$ between the two middle values is a minimizer (Exercise 4).
- **Weighted mean.** $\bar x_w = \sum_i w_i x_i / \sum_i w_i$. Pooling group means requires weighting by group sizes: the mean of two group means equals the overall mean only when the groups have equal $n$.
- **Geometric mean.** For positive values, $G = \left(\prod_i x_i\right)^{1/n} = \exp\left(\frac{1}{n}\sum_i \ln x_i\right)$, the back-transformed mean of the logs. Fold changes 2, 0.5, 4 and 0.25 (two genes up, two down by the same factors) have arithmetic mean 1.6875 but geometric mean 1: the arithmetic mean treats a 2-fold rise and a 2-fold fall asymmetrically. Always $G \le \bar x$, with equality only when all values are equal (inequality of arithmetic and geometric means).
- **Sample mean and expected value.** $\bar x$ varies from sample to sample around $\mu$ and approaches it as $n$ grows ([[Law of Large Numbers]], [[Sampling Distribution]]); the median of a sample likewise estimates the population median.

## Advanced (L3)

**Median-of-ratios size factors.** RNA-seq libraries differ in depth, and a few strongly expressed genes that change between conditions can dominate total read counts, so the total count is not a reliable measure of depth.[^anders] Anders and Huber build a pseudo-reference sample from the per-gene geometric means across samples and take, for each sample, the **median** over genes of the ratio of its counts to that reference.[^anders] Each ingredient has a role:

- the **geometric mean** makes the reference symmetric in the samples and insensitive to the overall scale of any one sample;
- the **median** ignores genes that really change, as long as no more than half of the genes are differentially expressed.[^anders]

Genes with a zero count in any sample have a zero geometric mean and are left out. In the toy matrix of the code below, one gene induced 300-fold makes sample 3 look 4.79 times deeper by total counts, while the size factors correctly say it has the same depth as sample 1 ([[Size Factor Estimation]], [[Count Normalization]]).[^holmes8]

**Breakdown.** One corrupted value can move the mean anywhere; the median stays within the range of the good values until half of the data are corrupted. This is why robust pipelines summarize with medians, and why the median-of-ratios fails when most genes change (Exercise 5).

## Mathematical representation

Let $x_{(1)} \le x_{(2)} \le \dots \le x_{(n)}$ be the sorted observations and $f(v)$ the frequency of value $v$.

$$\bar x = \frac{1}{n}\sum_{i=1}^{n} x_i, \qquad
\operatorname{med}(x) = \begin{cases} x_{((n+1)/2)} & n \text{ odd} \\ \tfrac{1}{2}\left(x_{(n/2)} + x_{(n/2+1)}\right) & n \text{ even} \end{cases}, \qquad
\operatorname{mode}(x) = \arg\max_v f(v).$$

Equivalently, $\bar x = \arg\min_c \sum_i (x_i - c)^2$ and $\operatorname{med}(x) \in \arg\min_c \sum_i |x_i - c|$.

**Size factors.** For a count matrix $K = (k_{ij})$ with genes $i = 1, \dots, m$ and samples $j = 1, \dots, n$ ([[Exploratory Data Analysis#Mathematical representation]]):

$$\hat s_j = \operatorname*{median}_{i \,:\, k_{il} > 0 \ \forall l} \; \frac{k_{ij}}{\left(\prod_{l=1}^{n} k_{il}\right)^{1/n}}.$$

The denominator is the geometric mean of gene $i$ across samples; normalized counts are $k_{ij}/\hat s_j$. Only ratios of size factors matter: multiplying all $\hat s_j$ by a constant rescales every normalized count equally.

## Computational representation

The `statistics` module provides `mean` and `fmean` (fast float mean), `median` (averaging the two middle values for even $n$; `median_low` and `median_high` return an observed value), `mode` (the first mode met if several), `multimode` and `geometric_mean`.[^python]

```python
import math
import statistics

# Invented long-read lengths (bp) from a toy sequencing run.
lengths = [850, 1200, 1500, 2100, 2300, 2900, 3400, 4800, 7600, 25000]
print(statistics.fmean(lengths), statistics.median(lengths))
lengths_bad = lengths[:-1] + [250000]          # one chimeric or mis-parsed record
print(statistics.fmean(lengths_bad), statistics.median(lengths_bad))

# Mode: discrete or categorical data (invented trimmed Illumina read lengths, genotypes).
trimmed = [150, 150, 148, 150, 132, 150, 150, 101, 149, 150]
print(statistics.mode(trimmed), statistics.multimode(["AA", "Aa", "Aa", "AA", "aa"]))

# Ratios: arithmetic versus geometric mean of fold changes.
fold = [2.0, 0.5, 4.0, 0.25]
print(statistics.fmean(fold), statistics.geometric_mean(fold),
      statistics.fmean(math.log2(x) for x in fold))


def size_factors(counts: dict[str, list[int]]) -> list[float]:
    """Median-of-ratios size factors (Anders and Huber 2010).

    counts: gene -> counts in each sample. Genes with a zero count in any
    sample are skipped, because their geometric mean is zero.
    """
    n = len(next(iter(counts.values())))
    ratios = [[] for _ in range(n)]
    for row in counts.values():
        if min(row) == 0:
            continue
        log_ref = statistics.fmean(math.log(k) for k in row)   # log geometric mean
        for j, k in enumerate(row):
            ratios[j].append(math.exp(math.log(k) - log_ref))
    return [statistics.median(r) for r in ratios]


# Invented toy matrix: s2 is s1 sequenced twice as deep; in s3 one gene (g6) is hugely induced.
counts = {
    "g1": [100, 200, 100],
    "g2": [200, 400, 200],
    "g3": [50, 100, 50],
    "g4": [400, 800, 400],
    "g5": [30, 60, 30],
    "g6": [10, 20, 3000],
    "g7": [0, 5, 2],
}
totals = [sum(col) for col in zip(*counts.values())]
sf = size_factors(counts)
print(totals, [round(t / totals[0], 2) for t in totals])
print([round(s, 3) for s in sf], [round(s / sf[0], 2) for s in sf])
```

```text
5165.0 2600.0
27665.0 2600.0
150 ['AA', 'Aa']
1.6875 1.0 0.0
[790, 1585, 3782] [1.0, 2.01, 4.79]
[0.794, 1.587, 0.794] [1.0, 2.0, 1.0]
```

The geometric mean is computed through logs, which avoids overflow of the product for thousands of genes.

## Worked example

> [!example] Median-of-ratios by hand on the toy matrix
> 1. **Reference.** For g1, the geometric mean of 100, 200, 100 is $(2 \times 10^6)^{1/3} \approx 126.0$; g2 to g5 are proportional to g1 across samples, so they behave the same way. For g6: $(10 \times 20 \times 3000)^{1/3} = (6 \times 10^5)^{1/3} \approx 84.3$. g7 has a zero and is skipped.
> 2. **Ratios.** g1 to g5: $0.794$ (s1), $1.587$ (s2), $0.794$ (s3). g6: $10/84.3 \approx 0.119$, $0.237$, $3000/84.3 \approx 35.6$.
> 3. **Medians.** s1: median of five 0.794 and one 0.119 is 0.794. s2: 1.587. s3: median of five 0.794 and one 35.6 is 0.794.
> 4. **Read.** Relative to s1, the depths are 1, 2, 1. Totals (790, 1585, 3782) would claim 1, 2.01, 4.79: dividing s3 by its total would make the five unchanged genes look almost 5-fold down-regulated, a false result created by one induced gene.

## Common misconceptions

> [!warning] "The mean is the typical value"
> On skewed data most observations lie on one side of the mean: 7 of the 10 toy reads are shorter than it. Report the median, or both, for read lengths, coverage and expression.

> [!warning] "The median throws information away"
> It ignores the magnitudes of extreme values on purpose. That costs a little precision on clean, symmetric data and protects the summary from outliers, failed records and the minority of genes that really change.

> [!warning] "Average fold changes with the arithmetic mean"
> Ratios are symmetric on the log scale: 2 and 0.5 average to 1 geometrically but to 1.25 arithmetically. Average $\log_2$ fold changes, then back-transform if needed.

> [!warning] "The mean of group means is the overall mean"
> Group A (2 samples, mean 10) and group B (8 samples, mean 20) have overall mean $(2 \times 10 + 8 \times 20)/10 = 18$, not 15. Weight by group size.

## Exercises

> [!question] Exercise 1 (L1)
> Compute the mean, median and mode of the trimmed read lengths `150, 150, 148, 150, 132, 150, 150, 101, 149, 150`. Which one describes the run best?

> [!success]- Solution
> Mean $= 1430/10 = 143.0$; sorted, the 5th and 6th values are both 150, so the median is 150; the mode is 150 (6 times). Checked with `statistics`: `143.0 150.0 150`. Median and mode say "most reads kept full length"; the mean is pulled down by the few heavily trimmed reads.

> [!question] Exercise 2 (L1)
> Choose a measure of center for: (a) genotypes at a SNP; (b) tumor grades; (c) long-read lengths; (d) $\log_2$ expression of a gene in 6 replicates with a symmetric spread.

> [!success]- Solution
> (a) mode (nominal); (b) median (ordinal); (c) median (right-skewed); (d) mean, which uses every value; the median would be close.

> [!question] Exercise 3 (L2)
> Three labs estimate a variant's frequency as 0.10 (500 people), 0.20 (100 people) and 0.40 (25 people). Give the unweighted and the sample-size-weighted mean frequency, and say which estimates the frequency in the pooled 625 people.

> [!success]- Solution
> Unweighted: $(0.10 + 0.20 + 0.40)/3 \approx 0.233$. Weighted: $(500 \times 0.10 + 100 \times 0.20 + 25 \times 0.40)/625 = (50 + 20 + 10)/625 = 0.128$. The weighted mean is the frequency in the pooled sample; the unweighted one gives the smallest lab the same influence as the largest.

> [!question] Exercise 4 (L2, Python)
> With `lengths` from the code above, scan $c$ from 0 to 30,000 in steps of 50 and find which $c$ minimizes $\sum_i (x_i - c)^2$ and which values minimize $\sum_i |x_i - c|$.

> [!success]- Solution
> ```python
> grid = range(0, 30_001, 50)
> sq = min(grid, key=lambda c: sum((x - c) ** 2 for x in lengths))
> best = min(sum(abs(x - d) for x in lengths) for d in grid)
> ab = [c for c in grid if sum(abs(x - c) for x in lengths) == best]
> print(sq, ab[0], ab[-1])
> ```
> Output: `5150 2300 2900`. The squared loss is minimized at the grid point nearest the mean (5165). The absolute loss is flat between the two middle values 2300 and 2900: for even $n$ any value there is "a" median, and the convention takes the midpoint, 2600.

> [!question] Exercise 5 (L3, Python)
> In the toy matrix, set sample s3 to `500, 1000, 250, 2000, 30, 10` for g1 to g6 (g1 to g4 up 5-fold, g5 and g6 unchanged relative to s1). Recompute the size factors relative to s1 and explain the result.

> [!success]- Solution
> ```python
> counts2 = {g: row[:] for g, row in counts.items()}
> for g, k in zip(("g1", "g2", "g3", "g4", "g6"), (500, 1000, 250, 2000, 10)):
>     counts2[g][2] = k
> sf2 = size_factors(counts2)
> print([round(s / sf2[0], 2) for s in sf2])
> ```
> Output: `[1.0, 2.0, 5.0]`. With 4 of 6 usable genes up 5-fold, the median ratio is a changed gene: the method reads the induction as 5-fold deeper sequencing. After normalization g1 to g4 look unchanged and g5, g6 look 5-fold down. The median-of-ratios assumes that most genes do not change;[^anders] experiments with global shifts in expression need a reference known not to change.

## Mastery checklist

- [ ] 1 Recognized: I can compute a mean, a median and a mode, and say which applies to which level of measurement.
- [ ] 2 Understood: I can explain why skewness and outliers separate the mean from the median, and why ratios need a geometric mean.
- [ ] 3 Practiced: I can implement weighted and geometric means and median-of-ratios size factors in Python and verify them by hand.
- [ ] 4 Applied: I summarized real read lengths with median and N50 and computed size factors for a real count matrix, comparing them with library totals.
- [ ] 5 Explained: I can teach what each center minimizes, its robustness, and the assumption behind median-of-ratios normalization and when it fails.

## References

[^os2]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 2 "Descriptive Statistics" (mean, median, mode; skewness).
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x (robust summaries).
[^anders]: [[Anders 2010 - Differential Expression Analysis for Sequence Count Data]], *Genome Biology* 11(10):R106, estimation of size factors.
[^holmes8]: [[Modern Statistics for Modern Biology (Holmes)]], ch. 8 "High-Throughput Count Data".
[^python]: [[Python Documentation]], Library Reference, `statistics` module.
