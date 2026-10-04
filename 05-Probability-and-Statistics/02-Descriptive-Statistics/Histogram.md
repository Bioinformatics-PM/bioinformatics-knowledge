---
aliases:
  - Frequency Histogram
  - Density Histogram
  - Histogramme
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
  - "[[Frequency Distribution]]"
  - "[[Measure of Central Tendency]]"
related:
  - "[[Box Plot]]"
  - "[[Kernel Density Estimation]]"
  - "[[Empirical Cumulative Distribution Function]]"
  - "[[Exploratory Data Analysis]]"
  - "[[Data Transformation]]"
  - "[[Read Quality Control]]"
  - "[[GC Content]]"
  - "[[Paired-End Read]]"
projects:
  - "[[10-genomic-pipeline]]"
  - "[[bio-visualization]]"
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
---

# Histogram

> [!abstract]
> A histogram cuts the range of a quantitative variable into adjacent bins and draws, over each bin, a bar showing how many observations fall in it: the quickest way to see the shape of a distribution, provided the bins are chosen with care.

## Definition

A **histogram** is a graph of the [[Frequency Distribution]] of a quantitative variable: the horizontal axis is divided into adjacent intervals (bins, or classes) and a bar over each bin shows its frequency or relative frequency. The bars touch, unlike those of a bar chart of categories, and the vertical axis is labelled frequency or relative frequency.[^os2] On the **density scale**, the height of a bar is its relative frequency divided by the bin width, so that the areas of all bars sum to 1.

## Why it matters

- **First look at any variable.** Histograms are a basic tool of exploratory data analysis: they show center, spread, skewness and unexpected modes before any summary is trusted ([[Exploratory Data Analysis]]).[^ph525]
- **Read lengths.** After trimming, or in a long-read run, the length distribution shows whether reads are usable and where to set length filters ([[Read Quality Control]]).
- **GC content per read.** Reads from a single genome give one hump; a second hump means a mixture, for example a contaminating organism with another composition ([[GC Content]]).
- **Insert sizes.** For [[Paired-End Read|paired-end reads]], the distance between mates of mapped pairs shows the fragment lengths of the library, and pairs far outside the bulk of the distribution stand out.

## Core (L1)

**Building one.** Choose a bin width $h$ and a starting point, count the observations in each bin, and draw a bar per bin. Bins are half-open, $[a, a + h)$: a value on an edge goes into the bin on its right. Three vertical scales exist: counts, relative frequencies (count / $n$) and densities (count / $(n h)$). Use the density scale to overlay a curve, to compare samples of different sizes, or when bins have unequal widths.

**Reading the shape.**[^os2]

- **Center and spread**: where the bulk of the data lies, and how wide it is.
- **Modality**: one peak (unimodal), two (bimodal) or more. Several modes usually mean several populations.
- **Skewness**: a long right tail pulls the mean above the median; a long left tail pulls it below ([[Measure of Central Tendency]]).
- **Gaps, spikes and isolated bars**: possible outliers, artifacts or a special value (such as a maximum read length).

**Choosing the bin width.** The same data can look very different:

![[histogram-bin-width-gc-content.svg]]

With bins of 0.10 (A), the 15 % of reads from the contaminant at GC 0.62 merge into a single lopsided hump. With 0.02 (B), two modes appear. With 0.005 (C), the bins are finer than the data: the GC fraction of a 100-bp read can only be a multiple of 0.01, so every other bin is empty and the remaining bars are twice as high. The comb is an artifact of binning, not a property of the reads. Always try several widths before reading a shape.

## Deeper (L2)

### Discrete data need aligned bins

Read lengths, depths and GC counts are integers (or multiples of a fixed step). A bin width that is not a multiple of the step makes some bins contain one possible value and others two, producing an alternating pattern (Exercise 3). Use a width that is a whole number of steps and put the edges between possible values, for example at half-integers for integer data.

### Comparing distributions

Histograms of several samples are comparable only with the same bins, the density scale and shared axes. Beyond two or three overlaid histograms, the picture becomes unreadable: use side-by-side [[Box Plot|box plots]] or overlaid [[Empirical Cumulative Distribution Function|ECDFs]], which need no bins.

### Logarithmic axes

Long-read lengths span from hundreds of bases to hundreds of kilobases. On a linear axis, everything above a few kilobases is squeezed into a thin tail; with bins of equal width on a log scale (each bin a constant ratio wider than the previous), the whole range is visible. A log vertical axis shows rare values in a tail. Label log axes in original units ([[Data Transformation]], [[Logarithm]]).

## Advanced (L3)

### A histogram is a density estimator

The count in a bin is binomial: $n_k \sim \mathrm{Bin}(n, p_k)$ with $p_k$ the probability of the bin, approximately $f(x)\,h$ for a density $f$. The bar height $\hat f(x) = n_k/(n h)$ then has

$$\mathbb E[\hat f(x)] = \frac{p_k}{h}, \qquad \operatorname{Var}[\hat f(x)] = \frac{p_k(1 - p_k)}{n h^2} \approx \frac{f(x)}{n h}.$$

Narrow bins reduce the bias (the average of $f$ over the bin approaches $f(x)$) but increase the variance; wide bins do the reverse. The relative standard deviation of a bar is about $1/\sqrt{n h f(x)}$, one over the square root of the expected count: the bin width should shrink as $n$ grows, more slowly than $1/n$. [[Kernel Density Estimation]] replaces the hard bins by smooth kernels and makes the same trade-off through a bandwidth.

### Modes as populations

A bimodal histogram is a hypothesis generator: contamination, two cell populations, two fragment populations of a library. A [[Mixture Model]] fitted to the data estimates the proportion and parameters of each component, which a histogram only suggests.

### Histograms of very large data

Counts per bin are additive: histograms computed on chunks of a file, on separate chromosomes or on different machines are merged by summing counts. A histogram therefore needs one pass and memory proportional to the number of bins, not to the number of reads, which is how per-read quality statistics scale to billions of reads ([[Quantile]] uses the same idea).

## Mathematical representation

- Bins $B_k = [t_0 + k h,\ t_0 + (k + 1) h)$ with origin $t_0$ and width $h$.
- Count $n_k = \sum_{i=1}^n \mathbf 1[x_i \in B_k]$, relative frequency $n_k / n$, density $\hat f(x) = \dfrac{n_k}{n h}$ for $x \in B_k$.
- Total area: $\sum_k \hat f_k\, h = \sum_k n_k / n = 1$. With unequal widths $h_k$, use $\hat f_k = n_k / (n h_k)$.
- Bin index of a value: $k = \lfloor (x - t_0)/h \rfloor$.

## Computational representation

```python
import math
import random
import statistics
from collections import Counter

def histogram(xs, width, origin=0.0):
    """Counts per half-open bin [origin + k*width, origin + (k+1)*width), empty bins included."""
    counts = Counter(math.floor((x - origin) / width) for x in xs)
    return {origin + k * width: counts[k] for k in range(min(counts), max(counts) + 1)}

def densities(hist, n, width):
    """Bar heights on the density scale: their areas sum to 1."""
    return {left: c / (n * width) for left, c in hist.items()}

def show(hist, n, width, scale=60):
    for left, c in hist.items():
        print(f"[{left:g}, {left + width:g})".ljust(12), f"{c:4d}", "#" * round(c / n * scale))

rng = random.Random(1)
# 1,000 invented read lengths after trimming: 70 % untouched (150 bp), 30 % trimmed to 50-149 bp
lengths = [150 if rng.random() < 0.7 else rng.randint(50, 149) for _ in range(1000)]
h = histogram(lengths, 10, origin=50)
show(h, len(lengths), 10)
print("mean", statistics.mean(lengths), " median", statistics.median(lengths))
print("area of density histogram:", sum(d * 10 for d in densities(h, len(lengths), 10).values()))
```

Output:

```text
[50, 60)       29 ##
[60, 70)       30 ##
[70, 80)       28 ##
[80, 90)       28 ##
[90, 100)      21 #
[100, 110)     25 ##
[110, 120)     38 ##
[120, 130)     36 ##
[130, 140)     38 ##
[140, 150)     34 ##
[150, 160)    693 ##########################################
mean 135.381  median 150.0
area of density histogram: 1.0
```

## Worked example

> [!example] Read lengths after trimming (invented, output above)
>
> 1. **Spike**: 693 of 1,000 reads sit in $[150, 160)$; since no read is longer than 150 bp, this bin holds exactly the untrimmed reads. The origin at 50 with width 10 isolates them; edges at 145 and 155 would have mixed them with reads trimmed to 145-149 bp.
> 2. **Tail**: about 30 reads per 10-bp bin from 50 to 149 bp, a flat left tail of trimmed reads.
> 3. **Summaries**: the median is 150 bp, the mean 135.4 bp. The mean describes almost no read: the distribution is a spike plus a tail, and should be reported as "69 % untrimmed, the rest spread between 50 and 149 bp".
> 4. **Decision**: a minimum-length filter at 50 bp keeps everything here; the histogram shows how many reads a filter at 100 bp would remove ($29 + 30 + 28 + 28 + 21 = 136$).

## Common misconceptions

> [!warning] "A histogram is a bar chart"
> A bar chart shows categories, in any order, with gaps. A histogram has a quantitative axis, touching bars, and on the density scale it is the area of a bar, not its height, that measures a proportion.

> [!warning] "The default bins are good enough"
> Automatic bin widths can merge two modes (panel A) or create a comb on discrete data (panel C). Try several widths and align bins with the resolution of the data.

> [!warning] "A bar height is a probability"
> On the density scale, heights can exceed 1 (about 14 in panel C): the probability of a bin is height × width.

## Exercises

> [!question] Exercise 1 (L1)
> Insert sizes of 100 mapped pairs (invented): 200-250 bp: 12; 250-300: 45; 300-350: 30; 350-400: 10; 400-450: 3. Give the modal class, the class containing the median, an estimate of the mean from the class midpoints, and describe the shape.

> [!success]- Solution
> Modal class 250-300 bp (45 pairs). Cumulative counts 12, 57: the 50th value is in 250-300. Mean ≈ $(225 \cdot 12 + 275 \cdot 45 + 325 \cdot 30 + 375 \cdot 10 + 425 \cdot 3)/100 = 298.5$ bp. Unimodal and right-skewed: the tail extends to 450 bp, which pulls the mean above the middle of the median class.

> [!question] Exercise 2 (L1)
> Fragment lengths are tabulated with unequal bins: 100-200 bp: 40; 200-300: 120; 300-400: 30; 400-800: 10. Compute the densities. Why would a plot of the raw counts mislead?

> [!success]- Solution
> $n = 200$. Densities $n_k/(n h_k)$: 0.002, 0.006, 0.0015 and $10/(200 \cdot 400) = 0.000125$ per bp. With counts, the 400-800 bar (10) would look a third as tall as the 300-400 bar (30) and four times as wide, suggesting a substantial tail; per base pair, it is 12 times less dense.

> [!question] Exercise 3 (L2, Python)
> Simulate 5,000 reads of 100 bp with GC probability 0.45 using `random.Random(1)` (count G or C bases as `sum(rng.random() < 0.45 for _ in range(100))`), and bin the GC counts with `histogram` at widths 1.5 and 2 (GC fractions 0.015 and 0.02). Explain the result.

> [!success]- Solution
> For bins between 40 and 50 GC bases, width 1.5 gives 301, 699, 397, 778, 343, 624, 251 (alternating low and high), while width 2 gives a smooth 528, 699, 797, 721, 624. With width 1.5, bins alternately contain one possible integer (for example $[40.5, 42)$ holds only 41) and two ($[42, 43.5)$ holds 42 and 43): the alternation is aliasing, not biology. Use widths that are whole numbers of the data step.

> [!question] Exercise 4 (L3)
> With $n = 10{,}000$ reads and a true density $f = 8$ at GC 0.42, compare the relative standard deviation of the bar height for bin widths 0.005 and 0.02. What else changes when $h$ grows?

> [!success]- Solution
> Relative SD $\approx 1/\sqrt{n h f}$: for $h = 0.005$, $n h f = 400$, giving 0.05 (5 %); for $h = 0.02$, $1600$, giving 0.025 (2.5 %). Quadrupling the width halves the noise. In exchange the bar averages $f$ over a wider interval, so a narrow peak is flattened and two close modes can merge (the bias of panel A). The width balances these two errors.

## Mastery checklist

- [ ] 1 Recognized: I can tell a histogram from a bar chart and name the three vertical scales.
- [ ] 2 Understood: I can read center, spread, modality and skewness, and explain how bin width and edges change the picture.
- [ ] 3 Practiced: I can compute a histogram and densities in Python, and choose bins for discrete data.
- [ ] 4 Applied: I plot read-length, GC-content and insert-size histograms of a real run and interpret them in a QC report ([[10-genomic-pipeline]]).
- [ ] 5 Explained: I can teach the histogram as a density estimator, its bias-variance trade-off, and why it scales to billions of reads.

## References

[^os2]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 2 "Descriptive Statistics" (histograms; skewness and the mean, median and mode).
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x, exploratory data analysis.
