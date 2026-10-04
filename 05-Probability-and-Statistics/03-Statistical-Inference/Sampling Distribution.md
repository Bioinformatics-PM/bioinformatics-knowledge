---
aliases:
  - Distribution of a Statistic
  - Standard Error
  - SE
  - Standard Error of the Mean
  - SEM
  - Distribution d'échantillonnage
  - Erreur type
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Sampling]]"
  - "[[Random Variable]]"
  - "[[Expected Value]]"
  - "[[Variance]]"
  - "[[Normal Distribution]]"
related:
  - "[[Central Limit Theorem]]"
  - "[[Law of Large Numbers]]"
  - "[[Confidence Interval]]"
  - "[[Hypothesis Testing]]"
  - "[[Student's t-Distribution]]"
  - "[[Bootstrap]]"
  - "[[Estimator]]"
  - "[[Biological Replicate]]"
projects: []
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Experimental Design for Laboratory Biologists (Lazic)]]"
  - "[[Hurlbert 1984 - Pseudoreplication and the Design of Ecological Field Experiments]]"
---

# Sampling Distribution

> [!abstract]
> A number computed from a sample, such as a mean, would change if the experiment were repeated; the sampling distribution describes how it changes, and its standard deviation, the standard error, measures how precise the number is.

## Definition

A **statistic** $T = t(X_1, \dots, X_n)$ is any quantity computed from a random sample, so it is itself a [[Random Variable]]. Its **sampling distribution** is the probability distribution of $T$ over all the samples of size $n$ that could have been drawn. The **standard error** (SE) of $T$ is the standard deviation of its sampling distribution; for the sample mean of independent observations with standard deviation $\sigma$ it is $\sigma/\sqrt{n}$.[^os7][^blitz]

## Why it matters

- **Every error bar, interval and test is built on one.** A [[Confidence Interval]] is a range of plausible parameter values derived from the sampling distribution of an estimate; a [[Hypothesis Testing|test]] compares the observed statistic with its sampling distribution under the null hypothesis.[^1805][^ph525]
- **Replicates buy precision slowly.** The standard error of a mean [[Log Fold Change]] falls like $1/\sqrt{n}$: four times as many [[Biological Replicate|biological replicates]] only halve it. This sets the cost of an expression experiment ([[Experimental Design]]).
- **Sequencing depth is a sample size.** The fraction of reads carrying an allele at a site is a sample proportion, whose standard error shrinks with depth like any other ([[Binomial Distribution]]).[^holmes8]
- **The right $n$ is the number of independent units.** Technical replicates and repeated measurements of one sample do not reduce the variability between biological units; counting them as $n$ understates the standard error ([[Pseudoreplication]]).[^lazic][^hurlbert]

## Core (L1)

### One statistic, many possible samples

Imagine repeating the same experiment many times: three new mice per group, new RNA extractions, new sequencing. Each repetition gives a different sample and therefore a different mean. The histogram of all those means is the sampling distribution of the mean. In practice the experiment is done once, so the sampling distribution is obtained by theory (formulas below), by simulation, or by resampling the one sample ([[Bootstrap]]).[^os7]

![[sampling-distribution-mean-sqrt-n.svg]]

### Mean and standard error of the sample mean

For $n$ independent observations with mean $\mu$ and variance $\sigma^2$, the sample mean $\bar X$ satisfies[^os7][^blitz]

$$E[\bar X] = \mu, \qquad \mathrm{Var}(\bar X) = \frac{\sigma^2}{n}, \qquad \mathrm{SE}(\bar X) = \frac{\sigma}{\sqrt n}.$$

The mean is centered on the truth, and its spread shrinks with $\sqrt n$, not with $n$ (derivation in the Mathematical representation, from the rules of [[Variance]]).

**Bio: precision of a mean fold change.** Suppose a gene's log2 fold change varies between biological replicates with $\sigma = 0.8$ around a true $\mu = 1$ (a doubling; invented values). One replicate has SE 0.80; three give $0.8/\sqrt 3 = 0.46$; twelve give 0.23. With three replicates the mean can still fall below 0, the wrong direction, with probability 0.015; with twelve, $7.5 \times 10^{-6}$ (figure).

### Shape: exact for normal data, approximate for large $n$

- If the observations are normal, $\bar X \sim \mathcal N(\mu, \sigma^2/n)$ exactly ([[Normal Distribution]]).
- Whatever their distribution (with finite variance), $\bar X$ is approximately normal for large $n$: the [[Central Limit Theorem]].[^os7][^blitz] For skewed data, "large" can mean dozens: in the simulation below, means of exponential observations keep a visible skew at $n = 16$.

### Proportions

A proportion is a mean of 0/1 indicators. If $X \sim \mathrm{Bin}(n, p)$ counts successes, $\hat p = X/n$ has $E[\hat p] = p$ and $\mathrm{SE}(\hat p) = \sqrt{p(1-p)/n}$ ([[Binomial Distribution]]).[^os7] An allele frequency of 0.3 estimated from 400 sampled chromosomes has SE $\sqrt{0.21/400} = 0.023$.

### Standard deviation versus standard error

| | Standard deviation $\sigma$ (or $s$) | Standard error $\sigma/\sqrt n$ |
|---|---|---|
| Describes | spread of individual observations | spread of the statistic over repeated samples |
| As $n$ grows | stays the same (estimated better) | shrinks to 0 |
| Answers | "How different are two mice?" | "How well do I know the mean?" |

## Deeper (L2)

### The standard error is usually estimated

$\sigma$ is unknown, so the reported SE is $s/\sqrt n$, with $s$ the sample standard deviation ([[Measure of Dispersion]]). With three replicates $s$ is itself very imprecise ([[Variance#Estimating a variance from a few replicates]]), and the ratio $(\bar X - \mu)/(s/\sqrt n)$ is not normal but follows [[Student's t-Distribution]] with $n - 1$ degrees of freedom for normal data. Intervals and tests on few replicates must use it.[^blitz]

### Each statistic has its own sampling distribution

The formula $\sigma/\sqrt n$ is for the mean only. Other statistics have other standard errors, which simulation reveals directly (code below):

- For normal data with $n = 12$, the median has SE 0.275 against 0.230 for the mean: the mean is more precise.
- For heavy-tailed (Laplace) data with the same variance, the order flips: 0.342 for the median against 0.410 for the mean (Exercise 5). Which estimator is best depends on the shape of the data ([[Estimator]], [[Nonparametric Statistics]]).
- For normal data, $(n-1)S^2/\sigma^2$ follows a [[Chi-Square Distribution]] with $n - 1$ degrees of freedom: the sampling distribution of the variance.[^blitz]

### Which replicates count: variance components

$\mathrm{Var}(\bar X) = \sigma^2/n$ needs independent observations. Real designs nest measurements: $b$ biological replicates, each measured $t$ times. With between-animal variance $\sigma_B^2$ and technical variance $\sigma_T^2$,

$$\mathrm{Var}(\bar X) = \frac{\sigma_B^2}{b} + \frac{\sigma_T^2}{b\,t}.$$

Technical repeats only shrink the second term: however large $t$ is, the SE never falls below $\sigma_B/\sqrt b$. Twelve measurements spent as 12 animals × 1 beat 3 animals × 4 (Exercise 3). Treating the 12 technical measurements as $n = 12$ is [[Pseudoreplication]].[^lazic][^hurlbert]

More generally, $n$ observations with common variance $\sigma^2$ and pairwise correlation $\rho$ give $\mathrm{Var}(\bar X) = \frac{\sigma^2}{n}\,[1 + (n-1)\rho]$, an effective sample size of $n/[1 + (n-1)\rho]$ (Exercise 4). Cells from one donor, or samples from one batch ([[Batch Effect]]), are correlated in exactly this way.

## Advanced (L3)

- **When no formula exists, resample.** The standard error of a median, a correlation or a clustering-derived score has no simple formula. The [[Bootstrap]] approximates the sampling distribution by recomputing the statistic on samples drawn with replacement from the data.[^1805]
- **Transformations.** For a smooth function $g$, the delta method gives $\mathrm{SE}(g(\bar X)) \approx |g'(\mu)|\,\mathrm{SE}(\bar X)$ ([[Variance#Delta method and variance stabilization]]). For example, $\mathrm{SE}(\log \bar X) \approx \mathrm{SE}(\bar X)/\mu$: the coefficient of variation of the mean. This is why fold changes are analyzed on the log scale, where their errors are closer to symmetric ([[Log Fold Change]]).
- **Depth is precision, not accuracy.** At a heterozygous site the alternative-allele fraction among $d$ reads has SE $\sqrt{0.25/d}$: 0.091 at 30× and 0.025 at 400× (Exercise 6). More reads shrink sampling noise but leave mapping or capture biases untouched, the same lesson as biased sampling in [[Sampling#Advanced (L3)]].[^holmes8]
- **The null distribution is a sampling distribution.** A test statistic's distribution when the null hypothesis holds is its sampling distribution under that hypothesis; [[P-Value|p-values]] are tail areas of it ([[Hypothesis Testing]]).
- **Normality arrives slowly for skewed data.** Cumulants of independent variables add, so the skewness of a mean of $n$ observations is the population skewness divided by $\sqrt n$: 2 for one exponential observation, 1 at $n = 4$, 0.5 at $n = 16$, 0.25 at $n = 64$; the simulation gives 2.09, 1.03, 0.50 and 0.30, close given the noise of a skewness estimate.

## Mathematical representation

- **Sample**: $X_1, \dots, X_n$ independent and identically distributed (i.i.d.) with mean $\mu$ and variance $\sigma^2$. **Statistic**: $T_n = t(X_1, \dots, X_n)$; its sampling distribution is the distribution of $T_n$ induced by the joint distribution of the sample.
- **Mean**: $\bar X = \frac1n \sum_{i=1}^n X_i$. By linearity, $E[\bar X] = \frac1n \sum E[X_i] = \mu$. By independence, $\mathrm{Var}(\bar X) = \frac1{n^2}\sum \mathrm{Var}(X_i) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}$.
- **Standard error**: $\mathrm{SE}(\bar X) = \sigma/\sqrt n$, estimated by $\widehat{\mathrm{SE}} = S/\sqrt n$ with $S^2 = \frac{1}{n-1}\sum (X_i - \bar X)^2$.
- **Proportion**: $\hat p = X/n$ with $X \sim \mathrm{Bin}(n, p)$: $E[\hat p] = p$, $\mathrm{Var}(\hat p) = p(1-p)/n$.
- **Shape**: normal data give $\bar X \sim \mathcal N(\mu, \sigma^2/n)$; in general $\frac{\bar X - \mu}{\sigma/\sqrt n}$ converges in distribution to $\mathcal N(0, 1)$ (central limit theorem).[^blitz]
- **Correlated observations**: with $\mathrm{Cov}(X_i, X_j) = \rho\sigma^2$ for $i \ne j$, $\mathrm{Var}(\bar X) = \frac{1}{n^2}\left[n\sigma^2 + n(n-1)\rho\sigma^2\right] = \frac{\sigma^2}{n}[1 + (n-1)\rho]$.
- **Nested design**: $X_{jk} = \mu + B_j + E_{jk}$ with independent $B_j \sim (0, \sigma_B^2)$, $E_{jk} \sim (0, \sigma_T^2)$, $j \le b$, $k \le t$: $\bar X = \mu + \bar B + \bar E$, so $\mathrm{Var}(\bar X) = \sigma_B^2/b + \sigma_T^2/(bt)$.

## Computational representation

A sampling distribution is simulated by repeating the experiment in code: draw a sample, compute the statistic, store it, many times. A seeded `random.Random` makes the result reproducible ([[Random Number Generation]]).

```python
import random
import statistics as st

rng = random.Random(42)
MU, SIGMA = 1.0, 0.8   # invented: per-replicate log2 fold change of one gene
REPS = 20_000          # simulated experiments per sample size

print(" n  mean(xbar)  SD(xbar)  sigma/sqrt(n)")
for n in (1, 3, 12, 48):
    means = [st.fmean(rng.gauss(MU, SIGMA) for _ in range(n)) for _ in range(REPS)]
    print(f"{n:2d}  {st.fmean(means):10.3f}  {st.stdev(means):8.3f}  {SIGMA / n ** 0.5:13.3f}")


def skewness(xs):
    m, s = st.fmean(xs), st.pstdev(xs)
    return st.fmean(((x - m) / s) ** 3 for x in xs)


# A skewed population: exponential with mean 1 and SD 1 (invented expression levels of single cells)
for n in (1, 4, 16, 64):
    means = [st.fmean(rng.expovariate(1.0) for _ in range(n)) for _ in range(REPS)]
    print(f"exponential n = {n:2d}: SD(xbar) = {st.stdev(means):.3f}  skewness = {skewness(means):.2f}")

# Mean versus median of n = 12 normal replicates
means, medians = [], []
for _ in range(REPS):
    xs = [rng.gauss(MU, SIGMA) for _ in range(12)]
    means.append(st.fmean(xs))
    medians.append(st.median(xs))
print(f"n = 12: SE(mean) = {st.stdev(means):.3f}, SE(median) = {st.stdev(medians):.3f}")
```

```text
 n  mean(xbar)  SD(xbar)  sigma/sqrt(n)
 1       0.997     0.799          0.800
 3       1.005     0.465          0.462
12       0.999     0.232          0.231
48       0.999     0.116          0.115
exponential n =  1: SD(xbar) = 0.995  skewness = 2.09
exponential n =  4: SD(xbar) = 0.505  skewness = 1.03
exponential n = 16: SD(xbar) = 0.251  skewness = 0.50
exponential n = 64: SD(xbar) = 0.125  skewness = 0.30
n = 12: SE(mean) = 0.230, SE(median) = 0.275
```

The simulated SD of the means matches $\sigma/\sqrt n$ to within simulation noise, and the skewness of exponential means falls roughly like $2/\sqrt n$.

## Worked example

> [!example] How many replicates for a target precision?
> A pilot gives a biological SD of $\sigma = 0.8$ for a gene's log2 fold change (invented). The team wants the mean fold change to have SE at most 0.1.
> 1. **Current design**, 3 replicates: SE $= 0.8/\sqrt3 = 0.462$. About 95 % of experiments give a mean within $\pm 1.96 \times 0.462 = \pm 0.91$ of the truth: a true doubling ($\mu = 1$) could be measured anywhere from almost no change to nearly fourfold.
> 2. **Solve for $n$**: $0.8/\sqrt n \le 0.1 \iff \sqrt n \ge 8 \iff n \ge 64$.
> 3. **Reading**: 64 replicates per gene-level precision of 0.1 is unrealistic for most labs. The $\sqrt n$ law says precision must be bought elsewhere too: reduce $\sigma$ (better-controlled samples, pairing, [[Paired Design]]) or borrow information across genes ([[Empirical Bayes]]).
> 4. **Check the units**: technical repeats of the same RNA do not count toward these 64 (Deeper, variance components).

## Common misconceptions

> [!warning] "Error bars show the spread of the data"
> Only if they are SD bars. SE bars are $\sqrt n$ times narrower and describe the precision of the mean. A figure must say which it shows; with $n = 3$, SE bars are 1.7 times narrower than SD bars, which makes groups look more distinct than individual samples are.

> [!warning] "A larger sample makes the data less variable"
> The spread of individual observations ($\sigma$) does not change with $n$; only the spread of the statistic does. Doubling the number of mice does not make mice more alike.

> [!warning] "The sampling distribution is the histogram of my data"
> The histogram of one sample estimates the population distribution. The sampling distribution is the distribution of a statistic over hypothetical repeated samples; it is never observed directly from one experiment.

> [!warning] "The central limit theorem makes my measurements normal"
> It makes the mean of many independent observations approximately normal. Individual measurements keep their own distribution, and for strongly skewed data and small $n$ even the mean is not yet normal.

## Exercises

> [!question] Exercise 1 (L1)
> Replicate log2 expression values have $\sigma = 0.6$. Give the standard error of the mean for $n = 4$ and $n = 16$. How many replicates halve the standard error obtained with $n = 4$?

> [!success]- Solution
> $0.6/\sqrt4 = 0.30$ and $0.6/\sqrt{16} = 0.15$. Halving the SE requires multiplying $\sqrt n$ by 2, so $n$ by 4: 16 replicates.

> [!question] Exercise 2 (L1)
> In a population the frequency of an allele is $p = 0.3$. You genotype 200 unrelated individuals (400 chromosomes). Give the standard error of the sample allele frequency and the range that contains it in about 95 % of studies.

> [!success]- Solution
> $\hat p$ is a proportion of 400 chromosomes: $\mathrm{SE} = \sqrt{0.3 \times 0.7 / 400} = 0.023$. By the normal approximation, $0.3 \pm 1.96 \times 0.023 = 0.3 \pm 0.045$, about $[0.255, 0.345]$. Counting 400 independent chromosomes assumes the two alleles of a person are independent draws, which holds under [[Hardy-Weinberg Equilibrium]].

> [!question] Exercise 3 (L2)
> Biological SD $\sigma_B = 0.8$, technical SD $\sigma_T = 0.3$ (invented). Compare the standard error of the mean for design A (3 animals × 4 technical measurements) and design B (12 animals × 1 measurement).

> [!success]- Solution
> A: $0.64/3 + 0.09/12 = 0.2208$, SE $= 0.470$. B: $0.64/12 + 0.09/12 = 0.0608$, SE $= 0.247$. The same 12 measurements give half the SE when spent on independent animals; design A is barely better than 3 animals measured once ($0.8^2/3 + 0.3^2/3 = 0.243$, SE 0.493).

> [!question] Exercise 4 (L2)
> Ten measurements share a common SD and pairwise correlation $\rho = 0.5$ (for instance, cells from one donor). What is the effective sample size, and by what factor is the naive SE $\sigma/\sqrt{10}$ too small?

> [!success]- Solution
> $n_{\mathrm{eff}} = 10/(1 + 9 \times 0.5) = 1.82$. The true SE is $\sigma\sqrt{5.5/10} = 0.742\,\sigma$, against $\sigma/\sqrt{10} = 0.316\,\sigma$ for the naive formula: 2.3 times too small.

> [!question] Exercise 5 (L3, Python)
> With seed 7, simulate 20,000 samples of size 12 from a normal distribution with variance 2 and from a Laplace distribution with scale 1 (also variance 2), and compare the standard errors of the mean and of the median. Which estimator would you use for heavy-tailed data?

> [!success]- Solution
> ```python
> import random
> import statistics as st
>
> rng = random.Random(7)
>
>
> def laplace(scale: float = 1.0) -> float:
>     """Heavy-tailed draw: exponential magnitude with a random sign."""
>     return rng.choice((-1, 1)) * rng.expovariate(1 / scale)
>
>
> for name, draw in (("normal", lambda: rng.gauss(0, 2 ** 0.5)), ("Laplace", laplace)):
>     means, medians = [], []
>     for _ in range(20_000):
>         xs = [draw() for _ in range(12)]
>         means.append(st.fmean(xs))
>         medians.append(st.median(xs))
>     print(f"{name:8s} SE(mean) = {st.stdev(means):.3f}  SE(median) = {st.stdev(medians):.3f}")
> ```
> Output: `normal   SE(mean) = 0.408  SE(median) = 0.484`, then `Laplace  SE(mean) = 0.410  SE(median) = 0.342`. Both means have SE $\sqrt{2/12} = 0.408$, as the formula predicts for any distribution with that variance. The median wins for heavy tails, because a few extreme values move the mean but not the median: a reason for robust and rank-based methods ([[Nonparametric Statistics]]).

> [!question] Exercise 6 (L3)
> At a heterozygous site, each read carries the alternative allele with probability 0.5. Give the standard error of the observed allele fraction at 30× depth, and the depth needed for SE 0.025. Does more depth fix a reference-mapping bias that lowers the alternative fraction to 0.45?

> [!success]- Solution
> $\sqrt{0.25/30} = 0.091$; $\sqrt{0.25/d} \le 0.025 \iff d \ge 0.25/0.025^2 = 400$. No: depth shrinks the SE around the biased value 0.45, so the estimate converges to the wrong number. Precision and accuracy are separate properties.

## Mastery checklist

- [ ] 1 Recognized: I can say what a sampling distribution and a standard error are, and how they differ from the data's distribution and SD.
- [ ] 2 Understood: I can derive $E[\bar X] = \mu$ and $\mathrm{SE} = \sigma/\sqrt n$ and explain why precision grows with $\sqrt n$.
- [ ] 3 Practiced: I can simulate the sampling distribution of any statistic with a seeded generator and compute standard errors of means and proportions.
- [ ] 4 Applied: I chose the number of biological replicates or the sequencing depth of a real experiment from a target standard error.
- [ ] 5 Explained: I can explain variance components, correlated replicates and pseudoreplication, and when the bootstrap or the t distribution must replace the simple formula.

## References

[^os7]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 7 "The Central Limit Theorem" (sampling distribution of the sample mean, standard error, central limit theorem for means and sums).
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the sample mean, the law of large numbers and the central limit theorem, and of the chi-square and Student-t distributions.
[^1805]: [[MIT 18.05 - Introduction to Probability and Statistics]], Spring 2022, frequentist statistics part (Readings 17b to 19 on significance testing, 22 and 23a on confidence intervals, 24 "Bootstrap Confidence Intervals").
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x (statistical inference: p-values and confidence intervals).
[^holmes8]: [[Modern Statistics for Modern Biology (Holmes)]], ch. 8 "High-Throughput Count Data" (sampling noise of read counts).
[^lazic]: [[Experimental Design for Laboratory Biologists (Lazic)]], material on experimental units, biological and technical replication, and pseudoreplication.
[^hurlbert]: [[Hurlbert 1984 - Pseudoreplication and the Design of Ecological Field Experiments]].
