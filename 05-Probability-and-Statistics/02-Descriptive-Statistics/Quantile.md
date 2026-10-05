---
aliases:
  - Percentile
  - Quartile
  - Decile
  - Centile
  - Fractile
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
  - "[[Measure of Central Tendency]]"
  - "[[Measure of Dispersion]]"
related:
  - "[[Cumulative Distribution Function]]"
  - "[[Empirical Cumulative Distribution Function]]"
  - "[[Box Plot]]"
  - "[[Q-Q Plot]]"
  - "[[Outlier]]"
  - "[[Sequencing Coverage]]"
  - "[[Assembly Quality Assessment]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Python Documentation]]"
  - "[[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]]"
  - "[[Bolstad 2003 - A Comparison of Normalization Methods for High Density Oligonucleotide Array Data]]"
---

# Quantile

> [!abstract]
> A quantile is a cut point of sorted data: the 90th percentile is the value with 90 % of the observations at or below it, and the three quartiles cut the data into four equal parts.

## Definition

For a proportion $p$ between 0 and 1, a **$p$-quantile** is a value with a fraction $p$ of the data at or below it and a fraction $1 - p$ at or above it. **Percentiles** are the quantiles for $p = k/100$: the $k$-th percentile has $k$ % of the values at or below it and $(100 - k)$ % at or above. The **quartiles** are the 25th ($Q_1$), 50th ($Q_2$, the median) and 75th ($Q_3$) percentiles.[^os23]

## Why it matters

- **Coverage.** Sequencing depth along a genome or a target region is summarized by its median, its low percentiles ("10 % of the target is below 4×") and the fraction of positions above a threshold, which is a percentile read backwards ([[Sequencing Coverage]]). The mean hides the poorly covered regions where variants are missed.
- **Assembly statistics.** The N50 of an assembly is a length-weighted median of contig lengths ([[Genome Assembly]], [[Assembly Quality Assessment]]).[^lander]
- **Normalization.** Quantile normalization gives every microarray the same distribution of intensities ([[Microarray]]).[^bolstad]
- **Plots and robust rules.** Box plots, the interquartile range, Q-Q plots and robust outlier rules are built from quantiles ([[Box Plot]], [[Measure of Dispersion]], [[Q-Q Plot]], [[Outlier]]).

## Core (L1)

**Sort, then count.** A quantile only needs the data in order ([[Sorting]]). With $n$ sorted values $x_{(1)} \le \dots \le x_{(n)}$, the introductory rule places the $k$-th percentile at position[^os23]

$$i = \frac{k}{100}\,(n + 1).$$

If $i$ is a whole number, the percentile is $x_{(i)}$; otherwise interpolate between the two neighbouring values. The **interquartile range** $\mathrm{IQR} = Q_3 - Q_1$ is the spread of the middle half of the data ([[Measure of Dispersion]]).

**Bio: depth at 20 positions of a target (invented).**

```text
0  3  8  12  14  15  17  18  18  19  20  21  22  22  24  25  27  30  41  96
```

$Q_1$: $i = 0.25 \times 21 = 5.25$, so $Q_1 = 14 + 0.25\,(15 - 14) = 14.25$. Median: $i = 10.5$, $(19 + 20)/2 = 19.5$. $Q_3$: $i = 15.75$, $24 + 0.75\,(25 - 24) = 24.75$. The 10th percentile is 3.5: one position in ten is almost uncovered. The mean, 22.6, sits above the median because of the single position at 96×; if 96 became 960 the quartiles would not move. This robustness is why medians and quantiles are preferred summaries for skewed data.[^ph525] Half of the positions reach 20×.

## Deeper (L2)

### Several conventions, one idea

For small samples, software disagrees. Python's `statistics.quantiles` uses by default the "exclusive" method, for data sampled from a population that can have more extreme values than the sample (the $(n + 1)$ rule above); its "inclusive" method treats the minimum and maximum as the 0th and 100th percentiles.[^pydocs] On the 20 depths, the quartiles are 14.25 and 24.75 (exclusive) versus 14.75 and 24.25 (inclusive). The difference vanishes as $n$ grows (Exercise 2): state the method for small samples, ignore it for millions of positions. Formally, quantiles invert the [[Cumulative Distribution Function]] (or, for data, the [[Empirical Cumulative Distribution Function]]); the bounds $\mu \pm 1.96\,\sigma$ of a [[Normal Distribution]] are its 2.5th and 97.5th percentiles.

### Quantile normalization

Microarray intensities differ between arrays for technical reasons as well as biological ones. **Quantile normalization** makes the distribution of intensities identical across arrays: sort each array, average the sorted values across arrays rank by rank, and give each probe the average of its rank.[^bolstad] Bolstad and colleagues found that this simple method, which uses all arrays at once, performed favorably against methods that normalize each array against a baseline array.[^bolstad] Afterwards, the box plots of all arrays are identical ([[Box Plot]]).

## Advanced (L3)

### N50: a length-weighted median

![[n50-length-weighted-median.svg]]

The N50 length of an assembly is "the largest length $L$ such that 50 % of all nucleotides are contained in contigs of size at least $L$".[^lander] Sort contigs from longest to shortest and accumulate their lengths: N50 is the length of the contig in which the running total crosses half of the assembly. It is the median contig length when each **base**, not each contig, gets one vote, so it exceeds the ordinary median (70 kb versus 40 kb in the figure). Replacing 50 % by 90 % gives N90.

What it does not measure follows from the definition. Its denominator is the assembly itself, so discarding short contigs raises N50 without improving anything (Exercise 4); using the expected genome size as denominator closes this loophole. It also rewards joins, right or wrong: contiguity must be read with misassemblies and gene completeness ([[Assembly Quality Assessment]]).

### What quantile normalization assumes

By construction, every column ends up with the same distribution, so a genuine global difference between samples (most genes higher in one condition) is erased along with the technical one. The method is safe when most features do not change between conditions, and misleading otherwise: a real global increase would be reported as no change, and unchanged genes as decreased.

### Quantiles of very large data

Sorting costs $O(n \log n)$ time and $O(n)$ memory, which is heavy for the billions of positions of a large genome. Depth and Phred scores are small integers, so a count array (a [[Frequency Distribution]]) gives exact quantiles in one pass, with memory proportional to the number of distinct values: accumulate counts until the running total reaches $p\,n$. Count arrays from several chromosomes or files merge by addition.

## Mathematical representation

- Order statistics $x_{(1)} \le \dots \le x_{(n)}$. Exclusive rule: $h = (n + 1)\,p$ and $\hat Q(p) = x_{(\lfloor h \rfloor)} + (h - \lfloor h \rfloor)\,\big(x_{(\lfloor h \rfloor + 1)} - x_{(\lfloor h \rfloor)}\big)$, clamped to $[x_{(1)}, x_{(n)}]$. Inclusive rule: $h = (n - 1)\,p + 1$.
- Population quantile: $Q(p) = \inf\{x : F(x) \ge p\}$, with $F$ the CDF.
- N50: with contig lengths $\ell_{(1)} \ge \dots \ge \ell_{(m)}$ and total $T = \sum_i \ell_i$, $\mathrm{N50} = \ell_{(j^*)}$ where $j^* = \min\{j : \sum_{i \le j} \ell_{(i)} \ge T/2\}$.
- Quantile normalization of a matrix $X$ (probes $i$ × arrays $j = 1, \dots, m$): with $x^{(j)}_{(k)}$ the $k$-th smallest value of array $j$, $\bar s_k = \frac{1}{m} \sum_j x^{(j)}_{(k)}$ and $r_j(i)$ the rank of $X_{ij}$ in its array, $X'_{ij} = \bar s_{r_j(i)}$.

## Computational representation

```python
import statistics

def n50(lengths):
    """Largest L such that contigs of length >= L hold at least half of all bases."""
    half, run = sum(lengths) / 2, 0
    for length in sorted(lengths, reverse=True):
        run += length
        if run >= half:
            return length

def quantile_normalize(columns):
    """One list per sample (same length, no ties); every sample gets the mean sorted profile."""
    reference = [statistics.mean(row) for row in zip(*(sorted(c) for c in columns))]
    out = []
    for col in columns:
        new = [0.0] * len(col)
        for rank, idx in enumerate(sorted(range(len(col)), key=col.__getitem__)):
            new[idx] = reference[rank]
        out.append(new)
    return out

def quantile_from_counts(counts, p):
    """Lower p-quantile of integer data, from counts[v] = number of values equal to v."""
    target, run = p * sum(counts), 0
    for value, c in enumerate(counts):
        run += c
        if run >= target:
            return value

depth = [0, 3, 8, 12, 14, 15, 17, 18, 18, 19, 20, 21, 22, 22, 24, 25, 27, 30, 41, 96]  # invented
print("quartiles, exclusive ((n+1) rule):", statistics.quantiles(depth, n=4))
print("quartiles, inclusive:", statistics.quantiles(depth, n=4, method="inclusive"))
print("10th percentile:", round(statistics.quantiles(depth, n=10)[0], 2), " mean:", statistics.mean(depth))
print("N50:", n50([90, 70, 50, 40, 30, 20, 10]), "kb")          # contig lengths in kb, invented
arrays = [[5.0, 2.0, 3.0, 4.0], [4.0, 1.0, 4.5, 2.0], [3.0, 4.0, 6.0, 8.0]]  # 3 arrays x 4 probes, invented
print([[round(v, 2) for v in col] for col in quantile_normalize(arrays)])
hist = [3, 5, 9, 20, 41, 60, 52, 30, 12, 6, 2]                  # positions with depth 0, 1, ..., 10 (invented)
print("5th, 50th, 95th percentile:", [quantile_from_counts(hist, p) for p in (0.05, 0.5, 0.95)])
```

Output:

```text
quartiles, exclusive ((n+1) rule): [14.25, 19.5, 24.75]
quartiles, inclusive: [14.75, 19.5, 24.25]
10th percentile: 3.5  mean: 22.6
N50: 70 kb
[[5.83, 2.0, 3.0, 4.67], [4.67, 2.0, 5.83, 3.0], [2.0, 3.0, 4.67, 5.83]]
5th, 50th, 95th percentile: [2, 5, 8]
```

The three normalized arrays contain the same four values, each in its own probe order.

## Worked example

> [!example] N50 versus median for seven contigs (invented, as in the figure)
> Contigs (kb): 90, 70, 50, 40, 30, 20, 10; total $T = 310$ kb, half 155 kb.
>
> 1. Sorted from longest, the running totals are 90, 160, 210, ... kb. The total first reaches 155 kb inside the 70 kb contig: **N50 = 70 kb**.
> 2. The median contig is the 4th of 7: **40 kb**.
> 3. Reading: half of the assembled bases lie in contigs of 70 kb or more, although a typical contig is 40 kb. N50 describes where the bases are; the median describes what the contigs are.

## Common misconceptions

> [!warning] "The 90th percentile means 90 %"
> A percentile is a rank, not a score: the 90th percentile has 90 % of the values the same or lower.[^os23] A position at the 90th percentile of depth may have 25× or 250×.

> [!warning] "Quartiles have one correct formula"
> Methods differ for small $n$ (14.25 versus 14.75 above). Neither is wrong: state the method, or use enough data for the difference to vanish.

> [!warning] "N50 is the median contig, and a higher N50 means a better assembly"
> N50 weights contigs by their length, and it increases when short contigs are discarded or contigs are wrongly joined. It measures contiguity only.

## Exercises

> [!question] Exercise 1 (L1)
> Eleven read lengths (bp): 88, 92, 95, 99, 100, 101, 101, 103, 110, 120, 150. Compute $Q_1$, the median, $Q_3$ and the IQR with the $(n + 1)$ rule.

> [!success]- Solution
> $n + 1 = 12$, so the positions are 3, 6 and 9: $Q_1 = 95$, median $= 101$, $Q_3 = 110$, IQR $= 15$ bp. The 150-bp read changes none of them.

> [!question] Exercise 2 (L2, Python)
> Compare `statistics.quantiles(..., n=4)` with the exclusive and inclusive methods on the read lengths 101, 98, 150, 120, 99, 100, 140, 97, then on 10,000 values drawn with `random.Random(42).gauss(300, 30)`. Explain the difference.

> [!success]- Solution
> Exclusive gives [98.25, 100.5, 135.0] and inclusive [98.75, 100.5, 125.0]: with 8 values, $Q_3$ differs by 10 bp because the two rules interpolate at different places in a sparse upper tail. With 10,000 values the quartiles agree to 0.01 (279.28 versus 279.29 for $Q_1$): neighbouring order statistics are nearly equal.

> [!question] Exercise 3 (L2)
> Quantile-normalize two arrays of three probes: A = (2, 6, 4) and B = (3, 5, 9).

> [!success]- Solution
> Sorted A: 2, 4, 6; sorted B: 3, 5, 9; rank means 2.5, 4.5, 7.5. A becomes (2.5, 7.5, 4.5) and B (2.5, 4.5, 7.5). Both arrays now hold exactly {2.5, 4.5, 7.5}: only the ranks within each array survive. Probe 2 is still the highest in A and the middle one in B.

> [!question] Exercise 4 (L3, Python)
> An assembly has contigs of 50, 40 and 30 kb plus 100 contigs of 1 kb. Compute N50, then N50 after discarding contigs shorter than 2 kb. Which assembly is better?

> [!success]- Solution
> `n50([50, 40, 30] + [1] * 100)` returns 30: the total is 220 kb and the running total 50, 90, 120 crosses 110 kb in the 30 kb contig. After filtering, the total is 120 kb and the half-point (60 kb) falls in the 40 kb contig: N50 = 40. The long contigs are identical and 100 kb of sequence was discarded; N50 rose only because its denominator shrank. Compare assemblies on a common denominator (the expected genome size) and with other metrics ([[Assembly Quality Assessment]]).

## Mastery checklist

- [ ] 1 Recognized: I can define percentile, quartile and IQR, and say what N50 summarizes.
- [ ] 2 Understood: I can explain why quantiles resist extreme values, why software disagrees for small $n$, and why N50 is a length-weighted median.
- [ ] 3 Practiced: I can compute quantiles by hand and in Python, including from a count array, and implement N50 and quantile normalization.
- [ ] 4 Applied: on real data I report depth percentiles and the fraction of a target above 20×, and I compute N50 and N90 of a real assembly next to its median contig length.
- [ ] 5 Explained: I can teach the assumptions behind quantile normalization and how N50 can be inflated.

## References

[^os23]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 2 "Descriptive Statistics", section 2.3 "Measures of the Location of the Data" (percentiles and quartiles, the position $i = \frac{k}{100}(n+1)$, the percentile of a value, interpretation of percentiles).
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x, exploratory data analysis and robust summaries.
[^pydocs]: [[Python Documentation]], Library Reference, `statistics` module: `quantiles` and its `exclusive` and `inclusive` methods.
[^lander]: [[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]], *Nature* 409:860-921, definition of the N50 length of an assembly.
[^bolstad]: [[Bolstad 2003 - A Comparison of Normalization Methods for High Density Oligonucleotide Array Data]], *Bioinformatics* 19(2):185-193, abstract and methods (complete-data methods, quantile normalization).
