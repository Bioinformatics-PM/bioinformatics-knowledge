---
aliases:
  - Pearson Correlation
  - Pearson's r
  - Pearson Correlation Coefficient
  - Correlation Coefficient
  - Corrélation
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Scatter Plot]]"
  - "[[Measure of Dispersion]]"
  - "[[Standard Score]]"
related:
  - "[[Covariance]]"
  - "[[Rank Correlation]]"
  - "[[Linear Regression]]"
  - "[[Coefficient of Determination]]"
  - "[[Covariance Matrix]]"
  - "[[Distance Metric]]"
  - "[[Data Transformation]]"
  - "[[Outlier]]"
  - "[[Confounding]]"
  - "[[Causality]]"
  - "[[Gene Co-Expression Network]]"
projects: []
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Anscombe 1973 - Graphs in Statistical Analysis]]"
  - "[[Bland 1986 - Statistical Methods for Assessing Agreement Between Two Methods of Clinical Measurement]]"
  - "[[Stuart 2003 - A Gene-Coexpression Network]]"
  - "[[Leek 2010 - Tackling the Widespread and Critical Impact of Batch Effects]]"
  - "[[Python Documentation]]"
  - "[[Python for Data Analysis (McKinney)]]"
---

# Correlation

> [!abstract]
> Pearson's correlation coefficient $r$ is a single number between −1 and +1 that says how closely two measured variables follow a straight line together: useful for checking replicates and finding co-expressed genes, but blind to curves, sensitive to outliers, and silent about causes.

## Definition

**Pearson's correlation coefficient** $r$ measures the strength and direction of the **linear** association between two quantitative variables measured on the same units. It lies between −1 and +1: $r$ near +1 means the points lie close to an increasing line, near −1 close to a decreasing line, near 0 no linear trend. Its square $r^2$, the [[Coefficient of Determination]], is the fraction of the variation in $y$ explained by the least-squares line of $y$ on $x$.[^os12] For random variables, the population counterpart is $\rho = \operatorname{Cov}(X, Y) / (\sigma_X \sigma_Y)$ ([[Covariance]]).[^mit]

## Why it matters

- **Replicate concordance.** A routine quality check of an expression experiment is a [[Scatter Plot]] of one replicate against another, usually summarized by $r$ on log-transformed values; sample-by-sample correlation matrices, drawn as a [[Heatmap]], show which libraries group together.[^msmb]
- **Co-expression.** Genes whose expression profiles are correlated across many samples are linked in co-expression networks; Stuart and colleagues built one from 3,182 microarrays of humans, flies, worms and yeast and kept 22,163 relationships conserved across evolution.[^stuart] See [[Gene Co-Expression Network]].
- **Distances.** $1 - r$ turns correlation into a dissimilarity that groups genes or samples by the shape of their profiles rather than their level ([[Distance Metric]], [[Hierarchical Clustering]]).

## Core (L1)

**Plot first.** Always look at the [[Scatter Plot]] before computing $r$. Anscombe built four datasets of 11 points with the same means, nearly the same variances, the same correlation and the same regression line; only the plots show that one is linear with noise, one is a smooth curve, one is a perfect line spoiled by a single point, and in one $x$ takes a single value except for one extreme point that creates the whole correlation.[^anscombe]

![[anscombe-quartet.svg]]

**Computing $r$.** Convert each variable to [[Standard Score|z-scores]], multiply the paired z-scores, and average the products with denominator $n - 1$:

$$r = \frac{1}{n - 1} \sum_{i=1}^{n} z_{x,i}\, z_{y,i}.$$

A point above both means, or below both, contributes a positive product; a point above one mean and below the other contributes a negative product. $r$ is the balance.

**Reading $r$.**[^os12]

- The sign gives the direction; $|r|$ gives how tightly the points hug a line, not how steep the line is: every exact increasing line has $r = 1$.
- $r$ has no units and does not change when either variable is shifted or rescaled (counts per million instead of counts, °F instead of °C).
- $r = 0$ means no **linear** trend. A perfect parabola, symmetric around the mean of $x$, has $r = 0$ (Exercise 1).

**Correlation is not causation.** A correlation between $x$ and $y$ can arise because $x$ affects $y$, because $y$ affects $x$, because a third variable drives both, or by chance.[^os12] In expression data, two genes can be correlated across tissue samples simply because both are expressed by one cell type whose proportion varies between samples, or because the samples were processed in batches.[^leek] Establishing a cause needs an intervention or a design that rules the alternatives out ([[Causality]], [[Confounding]], [[Experimental Design]]).

## Deeper (L2)

**Correlate log counts, not raw counts.** Gene expression spans several orders of magnitude, so on the raw scale a few highly expressed genes dominate every sum of squares: in the worked example below, one gene of six carries 81 % of the raw-scale sum of products. Expression is therefore compared after a log transformation, $\log_2(x + 1)$, or a variance-stabilizing transformation.[^msmb] See [[Data Transformation]] and [[Variance-Stabilizing Transformation]]. The pseudocount 1 is a choice, and genes with zero counts in both samples pile up at the origin and add agreement that carries no information.

**A first look at Spearman.** Spearman's correlation is Pearson's $r$ computed on the ranks of the values. It measures **monotone** association, is unchanged by any increasing transformation (log or not gives the same value), and resists outliers, which can create a high Pearson correlation from unrelated data.[^ph525] Anscombe's quartet shows the difference: same Pearson $r$, but Spearman 0.82, 0.69, 0.99 and 0.50 (code below). Ties, Kendall's tau and inference are developed in [[Rank Correlation]].

**Why a high correlation between replicates can hide problems.** Correlation measures linear relationship, not agreement: it ignores systematic differences of scale or offset, and it grows with the range of the true values in the sample.[^bland] Three consequences for replicate checks, shown on invented simulated data (5,000 genes with log2 expression spread uniformly from 0 to 14, replicate noise SD 0.3):

```python
import random
import statistics
# uses pearson() from the Computational representation section below

rng = random.Random(7)
G = 5000
truth = [rng.uniform(0, 14) for _ in range(G)]                  # invented log2 expression levels
rep_a = [t + rng.gauss(0, 0.3) for t in truth]
rep_b = [t + rng.gauss(0, 0.3) for t in truth]                  # good replicate
biased = [t + 1 + rng.gauss(0, 0.3) for t in truth]             # every gene 2-fold too high
changed = [t + (rng.choice((-3, 3)) if g < 500 else 0) + rng.gauss(0, 0.3)
           for g, t in enumerate(truth)]                         # 10% of genes changed 8-fold
for name, other in (("replicate", rep_b), ("2-fold biased", biased), ("10% genes changed", changed)):
    diffs = [o - a for a, o in zip(rep_a, other)]
    print(f"{name:<18} r = {pearson(rep_a, other):.3f}  mean diff = {statistics.mean(diffs):+.2f}"
          f"  sd diff = {statistics.stdev(diffs):.2f}")
low = [g for g in range(G) if truth[g] < 4]
print("low-expressed only, replicate r =", round(pearson([rep_a[g] for g in low], [rep_b[g] for g in low]), 3), len(low))
```

```text
replicate          r = 0.995  mean diff = -0.00  sd diff = 0.42
2-fold biased      r = 0.995  mean diff = +1.00  sd diff = 0.42
10% genes changed  r = 0.969  mean diff = -0.00  sd diff = 1.05
low-expressed only, replicate r = 0.934 1514
```

1. **Bias is invisible.** A library whose every gene reads two-fold too high correlates exactly as well as a good replicate ($r = 0.995$). The mean of the log differences ($+1.00$, i.e. two-fold) reveals it.
2. **Range inflates $r$.** The same noise gives $r = 0.995$ over all genes but $0.934$ among low-expressed genes: the huge spread of expression between genes, not the precision of the measurement, makes replicate correlations look excellent.
3. **Real differences hide.** A sample in which 10 % of genes changed eight-fold still has $r = 0.969$; a fixed threshold such as "$r > 0.95$" would pass a swapped sample from a different condition.

The remedy is to look at differences: plot $y - x$ against $(x + y)/2$, the Bland-Altman plot, and summarize the differences by their mean and SD.[^bland] On log expression this difference-versus-average plot is the MA plot of expression analysis.[^msmb] Use $r$ to rank samples relative to each other (which library correlates least with its group, see [[Outlier]]), never as an absolute pass mark.

## Advanced (L3)

**Inference.** $r$ estimates $\rho$. Under $\rho = 0$ and approximately normal data, $t = r\sqrt{(n-2)/(1-r^2)}$ follows a [[Student's t-Distribution|$t$ distribution]] with $n - 2$ degrees of freedom.[^os12] Significance is not strength: with $n = 1000$ samples, $r = 0.1$ gives $t \approx 3.18$ and a two-sided p-value near 0.0015, yet $r^2 = 1\,\%$ (Exercise 5). With few samples, a [[Permutation Test]] avoids the normality assumption.

**Uncorrelated is not independent.** Independent variables have $\rho = 0$, but $\rho = 0$ only excludes a linear relation ([[Independence (Probability)]]).[^mit] The converse holds for jointly normal variables, where uncorrelated implies independent ([[Multivariate Normal Distribution]]).[^blitz]

**Co-expression at genome scale.** With $G$ genes there are $G(G-1)/2$ pairs, about $2 \times 10^8$ for $G = 20{,}000$: many large correlations arise by chance ([[Multiple Testing Correction]]), and hidden factors (batch, cell composition) correlate whole blocks of genes.[^leek] Stuart and colleagues kept only links conserved across species, using conservation as evidence of a functional relationship.[^stuart] Removing the linear effect of a third variable (regressing it out, then correlating residuals) gives a partial correlation ([[Linear Regression]]).

**Compositional data.** When values are proportions of a total (relative abundances in a [[Microbiome]] sample, reads per gene divided by library size), each row sums to 1, so the parts must covary negatively on average: $\sum_{j \ne i} \operatorname{Cov}(p_i, p_j) = -\operatorname{Var}(p_i)$ (Exercise 4). Independent taxa then look negatively correlated; see [[Compositional Data Analysis]].

## Mathematical representation

For paired data $(x_i, y_i)$, $i = 1, \dots, n$, with means $\bar x, \bar y$ and standard deviations $s_x, s_y$ (denominator $n - 1$, see [[Measure of Dispersion]]):

$$r = \frac{\sum_{i}(x_i - \bar x)(y_i - \bar y)}{\sqrt{\sum_i (x_i - \bar x)^2}\,\sqrt{\sum_i (y_i - \bar y)^2}} = \frac{s_{xy}}{s_x s_y}, \qquad s_{xy} = \frac{1}{n-1}\sum_i (x_i - \bar x)(y_i - \bar y).$$

- **Geometry.** With centered vectors $\mathbf{u} = (x_i - \bar x)_i$ and $\mathbf{v} = (y_i - \bar y)_i$, $r = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert} = \cos\theta$ ([[Dot Product]]). The Cauchy-Schwarz inequality gives $|r| \le 1$, with equality exactly when $\mathbf{v} = c\,\mathbf{u}$, i.e. the points lie on a line.
- **Invariance.** For $b, d \ne 0$: $r(a + bx,\ c + dy) = \operatorname{sign}(bd)\, r(x, y)$, because centering removes $a$ and $c$ and the scale factors cancel between numerator and denominator.
- **Regression.** The least-squares slope of $y$ on $x$ is $\hat\beta = r\, s_y / s_x$, so $r$ is the slope between z-scores.[^os12] Stacking all pairwise $r$ gives the correlation matrix ([[Covariance Matrix]]).
- **Population.** $\rho = \dfrac{E[(X - \mu_X)(Y - \mu_Y)]}{\sigma_X \sigma_Y}$, with $|\rho| \le 1$ ([[Expected Value]], [[Variance]], [[Covariance]]).[^mit]

## Computational representation

By hand, then with the standard library (`statistics.correlation` exists from Python 3.10; its `method="ranked"` option for Spearman from 3.12).[^pydoc] Data frames compute all pairwise correlations at once with pandas `DataFrame.corr`.[^mckinney]

```python
import math
import statistics


def pearson(x, y):
    """Pearson's r: sum of products of deviations over the root of the sums of squares."""
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    return sxy / math.sqrt(sxx * syy)


def ranks(v):
    """1-based ranks; tied values share the mean of their positions."""
    order = sorted(range(len(v)), key=v.__getitem__)
    r = [0.0] * len(v)
    i = 0
    while i < len(v):
        j = i
        while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]:
            j += 1
        for k in range(i, j + 1):
            r[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(x, y):
    """Spearman's rho: Pearson's r computed on the ranks."""
    return pearson(ranks(x), ranks(y))


# Anscombe's quartet (Anscombe 1973)
x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
quartet = {
    "I": (x, [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
    "II": (x, [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
    "III": (x, [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
    "IV": ([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
           [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]),
}
print("set  mean_y  var_y  pearson  spearman  slope")
for name, (xs, ys) in quartet.items():
    r = pearson(xs, ys)
    slope = r * statistics.stdev(ys) / statistics.stdev(xs)
    print(f"{name:<4} {statistics.mean(ys):6.2f} {statistics.variance(ys):6.2f} "
          f"{r:8.3f} {spearman(xs, ys):9.3f} {slope:6.3f}")
print(round(statistics.correlation(*quartet["I"]), 3))   # standard library, Python 3.10+
```

```text
set  mean_y  var_y  pearson  spearman  slope
I      7.50   4.13    0.816     0.818  0.500
II     7.50   4.13    0.816     0.691  0.500
III    7.50   4.12    0.816     0.991  0.500
IV     7.50   4.12    0.817     0.500  0.500
0.816
```

## Worked example

> [!example] Replicate concordance on the log scale (invented counts)
> Six genes measured in two replicate libraries. Counts were chosen so that $\log_2(\text{count} + 1)$ is a whole number.
>
> | Gene | Rep 1 | Rep 2 | $x = \log_2(c_1 + 1)$ | $y = \log_2(c_2 + 1)$ | $x - \bar x$ | $y - \bar y$ | product |
> |---|---:|---:|---:|---:|---:|---:|---:|
> | g1 | 1 | 3 | 1 | 2 | −5.167 | −4.167 | 21.528 |
> | g2 | 7 | 7 | 3 | 3 | −3.167 | −3.167 | 10.028 |
> | g3 | 31 | 15 | 5 | 4 | −1.167 | −2.167 | 2.528 |
> | g4 | 127 | 255 | 7 | 8 | 0.833 | 1.833 | 1.528 |
> | g5 | 511 | 511 | 9 | 9 | 2.833 | 2.833 | 8.028 |
> | g6 | 4095 | 2047 | 12 | 11 | 5.833 | 4.833 | 28.194 |
>
> 1. **Means.** $\bar x = \bar y = 37/6 \approx 6.167$.
> 2. **Sums.** Products sum to 71.833; $\sum (x - \bar x)^2 = 80.833$; $\sum (y - \bar y)^2 = 66.833$.
> 3. **Coefficient.** $r = 71.833 / \sqrt{80.833 \times 66.833} = 71.833 / 73.501 \approx 0.977$.
> 4. **Raw scale.** On the counts themselves, `pearson(rep1, rep2)` gives 0.990, and gene g6 alone contributes 81 % of the sum of products (39 % on the log scale). Drop g6 and the raw $r$ falls to 0.964: the raw-scale value mostly reports one gene.
> 5. **Ranks.** Both replicates order the six genes identically, so Spearman's $r_s = 1$.
> 6. **Agreement.** The log differences $y - x$ are $1, 0, -1, 1, 0, -1$: mean 0, so no systematic bias, with typical disagreements of one two-fold step.

## Common misconceptions

> [!warning] "r = 0 means the variables are unrelated"
> $r$ only detects linear trends. $y = x^2$ on $x = -3, \dots, 3$ is a perfect deterministic relation with $r = 0$; Anscombe's set II is a smooth curve with $r = 0.82$.[^anscombe] Plot the data.

> [!warning] "A replicate correlation of 0.99 means the replicates agree"
> Correlation ignores bias of scale and offset and grows with the range of values.[^bland] A library that reads every gene two-fold too high has the same $r$ as a perfect replicate; check the differences.

> [!warning] "A strong correlation shows that one variable causes the other"
> Shared hidden factors (batch, cell-type composition, tumor purity) correlate genes with no regulatory link, and the direction of any causal effect is not given by $r$.[^os12][^leek]

## Exercises

> [!question] Exercise 1 (L1)
> Let $x = (-3, -2, -1, 0, 1, 2, 3)$ and $y = x^2$. Compute $r$ without a calculator and explain what it shows.

> [!success]- Solution
> $\bar x = 0$, so the numerator is $\sum x_i (y_i - \bar y) = \sum x_i^3 - \bar y \sum x_i = 0 - 0 = 0$ by symmetry: $r = 0$ (`pearson(x, [v * v for v in x])` returns `0.0`). $y$ is a deterministic function of $x$, so $r = 0$ cannot mean "no relation"; it means "no linear trend".

> [!question] Exercise 2 (L2)
> Across 200 tumor samples, the expression of genes A and B has $r = 0.9$. Give three explanations other than "A activates B", and one check for each.

> [!success]- Solution
> (1) **B activates A** (reverse direction): perturb one gene (knockdown) and measure the other. (2) **A common driver**: both are expressed by a cell type whose share varies between tumors (tumor purity, immune infiltration); check by correlating each gene with a marker of that cell type, or by computing the correlation within samples of similar composition. (3) **Technical batch**: samples processed together share a shift in many genes; color the [[Scatter Plot]] by batch and see whether the correlation holds within batches.[^leek] A further possibility is chance among the very many gene pairs tested.

> [!question] Exercise 3 (L2, Python)
> Using `pearson` and `spearman` from the code above, compute both coefficients for the invented unrelated values `a = [2.1, 3.4, 1.8, 2.9, 3.1, 2.5, 1.9, 3.3, 2.2, 2.7]` and `b = [5.2, 4.1, 4.8, 5.5, 4.3, 5.0, 4.6, 4.4, 5.3, 4.9]`, then again after appending one extreme pair (12.0, 15.0).

> [!success]- Solution
> ```python
> a = [2.1, 3.4, 1.8, 2.9, 3.1, 2.5, 1.9, 3.3, 2.2, 2.7]      # invented, unrelated values
> b = [5.2, 4.1, 4.8, 5.5, 4.3, 5.0, 4.6, 4.4, 5.3, 4.9]
> print(round(pearson(a, b), 3), round(spearman(a, b), 3))    # -0.48 -0.43
> a2, b2 = a + [12.0], b + [15.0]                              # one extreme pair added
> print(round(pearson(a2, b2), 3), round(spearman(a2, b2), 3))  # 0.959 -0.073
> ```
> One point turns a weak negative Pearson correlation into $r = 0.959$, because its deviations dwarf all the others. Spearman only sees that the new point has the largest rank in both variables, and stays near 0. In expression data, one outlier sample or one contaminated library can do the same ([[Outlier]]).

> [!question] Exercise 4 (L3, Python)
> Three taxa have independent absolute abundances, uniform between 10 and 100, in 2,000 invented samples. Compute the correlations of the absolute abundances and of the proportions. Then prove that for proportions $p_1 + \dots + p_K = 1$, $\sum_{j \ne i} \operatorname{Cov}(p_i, p_j) = -\operatorname{Var}(p_i)$.

> [!success]- Solution
> ```python
> import random
> rng = random.Random(1)
> abs_ab = [[rng.uniform(10, 100) for _ in range(3)] for _ in range(2000)]   # 3 independent taxa
> props = [[v / sum(row) for v in row] for row in abs_ab]
> cols, raw = list(zip(*props)), list(zip(*abs_ab))
> print([round(pearson(cols[i], cols[j]), 3) for i, j in ((0, 1), (0, 2), (1, 2))])  # [-0.51, -0.504, -0.485]
> print([round(pearson(raw[i], raw[j]), 3) for i, j in ((0, 1), (0, 2), (1, 2))])    # [-0.007, 0.002, 0.028]
> cov = statistics.covariance
> print(round(cov(cols[0], cols[1]) + cov(cols[0], cols[2]), 6), round(-statistics.variance(cols[0]), 6))
> # -0.019541 -0.019541
> ```
> Proof: $\sum_j p_j = 1$ is constant, so $0 = \operatorname{Cov}(p_i, \sum_j p_j) = \operatorname{Var}(p_i) + \sum_{j \ne i} \operatorname{Cov}(p_i, p_j)$. With $K = 3$ exchangeable parts this gives correlations near $-1/(K-1) = -0.5$, created by closure alone, with no biological interaction ([[Compositional Data Analysis]]).

> [!question] Exercise 5 (L3, Python)
> (a) For the worked example ($n = 6$, $r \approx 0.977$), compute the exact permutation p-value: the fraction of the $6! = 720$ reorderings of $y$ whose correlation with $x$ is at least the observed one. (b) Compute $t = r\sqrt{(n-2)/(1-r^2)}$ for $n = 1000$ and $r = 0.1$, and a two-sided p-value with the normal approximation. Comment.

> [!success]- Solution
> ```python
> from itertools import permutations
> l1, l2 = [1, 3, 5, 7, 9, 12], [2, 3, 4, 8, 9, 11]          # log2 values of the worked example
> r_obs = pearson(l1, l2)
> perm = [pearson(l1, p) for p in permutations(l2)]
> k = sum(r >= r_obs - 1e-12 for r in perm)
> print(len(perm), k, round(k / len(perm), 4))                 # 720 1 0.0014
> r, n = 0.1, 1000
> t = r * math.sqrt((n - 2) / (1 - r ** 2))
> print(round(t, 2), round(math.erfc(t / math.sqrt(2)), 4))   # 3.18 0.0015
> ```
> (a) Only the observed order reaches $r \ge 0.977$: one-sided $p = 1/720 \approx 0.0014$ ([[Permutation Test]]). (b) With 1,000 samples, $r = 0.1$ is clearly "significant", yet it explains $r^2 = 1\,\%$ of the variance. A p-value answers "is $\rho \ne 0$?", not "is the association strong?" ([[Effect Size]]).

## Mastery checklist

- [ ] 1 Recognized: I can state what $r$ measures, its range, and that correlation is not causation.
- [ ] 2 Understood: I can explain why $r$ needs a plot (Anscombe), why expression is correlated on the log scale, and how Spearman differs from Pearson.
- [ ] 3 Practiced: I can compute $r$ by hand and in Python, rank with ties, and run a permutation test for $r$.
- [ ] 4 Applied: on a public RNA-seq dataset, I computed the sample correlation matrix of log counts, plotted replicate pairs with their differences, and flagged the least concordant library.
- [ ] 5 Explained: I can teach why replicate correlations look excellent even when samples are biased or swapped, the compositional bias of proportions, and the multiple-testing problem of genome-wide co-expression.

## References

[^os12]: [[Introductory Statistics (OpenStax)]], 2nd ed., chapter on linear regression and correlation.
[^mit]: [[MIT 18.05 - Introduction to Probability and Statistics]], covariance and correlation of random variables.
[^blitz]: [[Introduction to Probability (Blitzstein)]], joint distributions, covariance and the multivariate normal.
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x, exploratory data analysis and robust statistics.
[^msmb]: [[Modern Statistics for Modern Biology (Holmes)]], high-throughput count data (transformations and sample-level quality assessment).
[^anscombe]: [[Anscombe 1973 - Graphs in Statistical Analysis]], *The American Statistician* 27(1):17-21.
[^bland]: [[Bland 1986 - Statistical Methods for Assessing Agreement Between Two Methods of Clinical Measurement]], *The Lancet* 1(8476):307-310.
[^stuart]: [[Stuart 2003 - A Gene-Coexpression Network]], *Science* 302(5643):249.
[^leek]: [[Leek 2010 - Tackling the Widespread and Critical Impact of Batch Effects]], *Nature Reviews Genetics* 11(10):733-739.
[^pydoc]: [[Python Documentation]], Library Reference, `statistics` module.
[^mckinney]: [[Python for Data Analysis (McKinney)]], pandas part.
