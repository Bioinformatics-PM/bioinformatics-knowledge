---
aliases:
  - CI
  - Interval Estimate
  - Margin of Error
  - Confidence Level
  - Score Interval
  - Intervalle de confiance
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Sampling Distribution]]"
  - "[[Normal Distribution]]"
  - "[[Binomial Distribution]]"
related:
  - "[[Student's t-Distribution]]"
  - "[[Hypothesis Testing]]"
  - "[[P-Value]]"
  - "[[Effect Size]]"
  - "[[Bootstrap]]"
  - "[[Bayesian Inference]]"
  - "[[Allele Frequency]]"
projects: []
sources:
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Wasserstein 2016 - The ASA Statement on p-Values]]"
---

# Confidence Interval

> [!abstract]
> A confidence interval is a range computed from the data by a recipe that captures the true value in a stated fraction of experiments, such as 95 %; it reports an estimate together with its uncertainty.

## Definition

A **confidence interval** at level $1 - \alpha$ for a parameter $\theta$ is a pair of statistics $[L, U]$, computed from the sample, such that $P(L \le \theta \le U) = 1 - \alpha$ (or at least $1 - \alpha$) whatever the true value of $\theta$. The probability refers to the random interval before the data are seen: in repeated experiments, a fraction $1 - \alpha$ of the intervals contain $\theta$.[^os8][^1805-ci]

## Why it matters

- **An estimate without an interval is incomplete.** A log2 fold change of 1.1 from three replicates may be compatible with no change at all; the interval says so, the point estimate does not ([[Log Fold Change]], [[Effect Size]]).[^ph525]
- **Allele frequencies, variant allele fractions, proportions of cell types and error rates** are all proportions estimated from finite samples of chromosomes, reads or cells, and are reported with intervals ([[Allele Frequency]]).
- **Intervals and tests are two views of one calculation.** A 95 % interval for a difference that excludes 0 corresponds to a two-sided test rejecting "no difference" at the 5 % level, and the interval also shows how large the effect could be.[^1805-ci] The ASA statement lists confidence intervals among the approaches that complement p-values.[^asa]
- **Rare variants break the textbook recipe.** For allele frequencies near 0 the usual "estimate ± 1.96 SE" interval covers the truth much less often than promised (Deeper).

## Core (L1)

### The recipe: estimate ± critical value × standard error

When an estimate $\hat\theta$ is approximately normal around $\theta$ with standard error SE ([[Sampling Distribution]]), the interval

$$\hat\theta \pm z_{1-\alpha/2}\,\mathrm{SE}$$

has coverage close to $1 - \alpha$, where $z_{1-\alpha/2}$ is the normal quantile: 1.645 for 90 %, 1.96 for 95 %, 2.576 for 99 % ([[Normal Distribution]]).[^os8] The half-width $z_{1-\alpha/2}\,\mathrm{SE}$ is the **margin of error**.

| Parameter | Interval | Condition |
|---|---|---|
| Mean, $\sigma$ known | $\bar x \pm z_{1-\alpha/2}\,\sigma/\sqrt n$ | normal data, or large $n$ |
| Mean, $\sigma$ unknown | $\bar x \pm t_{n-1,\,1-\alpha/2}\,s/\sqrt n$ | normal data ([[Student's t-Distribution]]) |
| Proportion | $\hat p \pm z_{1-\alpha/2}\sqrt{\hat p(1-\hat p)/n}$ | at least about 5 successes and 5 failures |

These are the standard intervals for a mean and a proportion.[^os8] With $\sigma$ unknown, the $t$ quantile replaces $z$: with 3 replicates it is 4.303 instead of 1.96.

### What "95 %" means

![[confidence-interval-coverage-20-intervals.svg]]

The 95 % is a property of the **procedure**: before the experiment, the interval it will produce has a 95 % chance of covering $\mu$. Once computed, a particular interval such as $[0.12, 1.36]$ either contains $\mu$ or does not; it is not true that $\mu$ lies in it "with probability 0.95", because $\mu$ is a fixed number, not a random one.[^1805-ci] In the figure, 19 of 20 simulated experiments produce an interval containing the true mean.

### Bio: an interval for an allele frequency

100 unrelated individuals are genotyped at a SNP; 46 of their 200 chromosomes carry the alternative allele (invented counts).

1. Estimate: $\hat p = 46/200 = 0.23$.
2. Standard error: $\sqrt{0.23 \times 0.77 / 200} = 0.0298$.
3. 95 % interval: $0.23 \pm 1.96 \times 0.0298 = 0.23 \pm 0.058$, that is $[0.172, 0.288]$.

Counting 200 independent chromosomes assumes that the two alleles of a person are independent draws, true under [[Hardy-Weinberg Equilibrium]] and with unrelated individuals; related samples or population structure make the real uncertainty larger.

### Width and sample size

The width is $2 z_{1-\alpha/2}\,\mathrm{SE}$, so it shrinks like $1/\sqrt n$: halving it costs four times the sample. Solving the margin $m = z\sqrt{p(1-p)/n}$ for $n$ gives the sample size $n = z^2 p(1-p)/m^2$: to estimate an allele frequency near 0.3 within $\pm 0.02$, about 2,017 chromosomes (1,009 people); 2,401 in the worst case $p = 0.5$. A higher confidence level widens the interval: at 99 % the multiplier is 2.576 instead of 1.96.

## Deeper (L2)

### Coverage is a claim that can fail

Coverage holds only if the recipe matches the data. A seeded simulation with 3 normal replicates (Computational representation) shows:

| Recipe | Simulated coverage |
|---|---|
| $\bar x \pm 1.96\,\sigma/\sqrt3$, $\sigma$ known | 0.951 |
| $\bar x \pm 1.96\,s/\sqrt3$, estimated $s$ plugged into $z$ | 0.814 |
| $\bar x \pm 4.303\,s/\sqrt3$ ($t$ with 2 df) | 0.951 |

Plugging $s$ into the normal recipe gives "95 %" intervals that miss one time in five; the exact value is $P(|T_2| \le 1.96) = 1.96/\sqrt{2 + 1.96^2} = 0.811$ for the $t$ distribution with 2 degrees of freedom.

### The score interval for proportions

The Wald recipe of the table uses $\hat p$ inside the standard error. For rare alleles this fails: with $x = 0$ it gives $[0, 0]$, and its exact coverage for 200 chromosomes drops to 0.926 at $p = 0.05$ and 0.865 at $p = 0.01$. A better interval keeps every $p$ that a two-sided z-test would not reject when the standard error is computed at $p$ itself:

$$\left\{p : |\hat p - p| \le z\sqrt{p(1-p)/n}\right\},$$

a quadratic inequality in $p$ whose solution is given in the Mathematical representation. This **score interval** has exact coverage 0.967 and 0.948 at the same frequencies, never collapses to a point, and costs nothing extra to compute.

### Intervals and tests are dual

A $1 - \alpha$ interval contains exactly the parameter values $\theta_0$ that a two-sided level-$\alpha$ test of $H_0: \theta = \theta_0$ does not reject.[^1805-ci] So a 95 % interval for a mean log2 fold change that excludes 0 is the same statement as a two-sided [[Student's t-Test|t-test]] with $p < 0.05$, plus the information about how large the effect may be. The duality also builds intervals where no "± SE" formula exists, by inverting a test (Advanced).

### Differences

For a difference between two groups, the same recipe applies to $\bar x_1 - \bar x_2$ with standard error $\sqrt{s_1^2/n_1 + s_2^2/n_2}$, and a $t$ quantile with Welch's degrees of freedom ([[Student's t-Test]]). For paired data, it applies to the mean of the within-pair differences.

## Advanced (L3)

- **Zero observed: the rule of three.** If no alternative allele is seen among $n$ chromosomes, the exact one-sided 95 % upper bound solves $(1 - p)^n = 0.05$: $p_U = 1 - 0.05^{1/n} \approx 3/n$, since $-\ln 0.05 = 3.0$. For $n = 1{,}000$, $p_U = 0.00299$. "Absent from our cohort" therefore means "probably below 0.3 %", which is why absence from a reference panel of a given size bounds, but never excludes, a variant's frequency ([[Allele Frequency]]).
- **Exact intervals by inverting a test.** In general, the set of $p$ whose binomial tail probabilities $P(X \ge x)$ and $P(X \le x)$ both exceed $\alpha/2$ is an interval with coverage at least $1 - \alpha$ for every $p$; it is computed by bisection, and is conservative because the binomial is discrete ([[Binomial Distribution]], [[Cumulative Distribution Function#Advanced (L3)]]).
- **Many intervals at once.** Report 95 % intervals for 20,000 genes and about 1,000 will miss their true value. Worse, intervals reported only for genes selected because they were significant are biased away from 0: selection keeps the experiments where noise inflated the estimate. Multiplicity affects intervals as it does tests ([[Multiple Testing Correction]]).
- **Other routes to an interval.** The [[Bootstrap]] builds intervals from the resampled sampling distribution when no formula exists.[^1805-boot] A Bayesian credible interval answers a different question, the probability that $\theta$ lies in a range given the data and a prior, which is the reading people often wrongly give to a confidence interval ([[Bayesian Inference]]).[^1805-bayes]

## Mathematical representation

- **Definition**: statistics $L(X), U(X)$ with $P_\theta(L(X) \le \theta \le U(X)) \ge 1 - \alpha$ for all $\theta$, where $X$ is the sample and $P_\theta$ its distribution when the parameter equals $\theta$.
- **Pivot**: for normal data, $T = \frac{\bar X - \mu}{S/\sqrt n} \sim t_{n-1}$ whatever $\mu$ and $\sigma$. Then $P(-t^* \le T \le t^*) = 1 - \alpha$ with $t^* = t_{n-1,1-\alpha/2}$, and rearranging the inequalities gives $P\big(\bar X - t^* S/\sqrt n \le \mu \le \bar X + t^* S/\sqrt n\big) = 1 - \alpha$.
- **Wald interval for a proportion**: $\hat p \pm z\sqrt{\hat p(1-\hat p)/n}$, with $\hat p = x/n$ and $z = z_{1-\alpha/2}$.
- **Score interval**: squaring $|\hat p - p| \le z\sqrt{p(1-p)/n}$ gives a quadratic in $p$ whose roots are
$$\frac{\hat p + \frac{z^2}{2n}}{1 + \frac{z^2}{n}} \pm \frac{z}{1 + \frac{z^2}{n}}\sqrt{\frac{\hat p(1-\hat p)}{n} + \frac{z^2}{4n^2}}.$$
- **Sample size** for margin $m$: $n = z^2\sigma^2/m^2$ for a mean, $n = z^2 p(1-p)/m^2$ for a proportion.
- **Exact coverage** of a proportion interval $I(x)$: $C(p) = \sum_{x=0}^{n} \binom{n}{x}p^x(1-p)^{n-x}\,\mathbf 1[p \in I(x)]$.

## Computational representation

Standard library only: `statistics.NormalDist` gives $z$ quantiles, and the few $t$ quantiles needed are copied from [[Student's t-Distribution]] (which shows how to compute them).

```python
import math
import random
import statistics as st
from statistics import NormalDist

Z975 = NormalDist().inv_cdf(0.975)        # 1.95996...
T975 = {2: 4.303, 4: 2.776}               # 97.5 % quantiles of t, from Student's t-Distribution


def t_interval(xs, t_crit):
    m, se = st.fmean(xs), st.stdev(xs) / math.sqrt(len(xs))
    return m - t_crit * se, m + t_crit * se


def wald(x, n, z=Z975):
    p = x / n
    h = z * math.sqrt(p * (1 - p) / n)
    return p - h, p + h


def score(x, n, z=Z975):
    """All p not rejected by the two-sided z-test that uses the SE computed at p itself."""
    p = x / n
    center = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z / (1 + z * z / n) * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return center - h, center + h


# 1. Allele frequency: 46 alternative alleles among 200 chromosomes (invented)
print("Wald ", [round(v, 3) for v in wald(46, 200)], " score", [round(v, 3) for v in score(46, 200)])

# 2. Mean log2 fold change from 3 replicates (invented values)
print("t-interval", [round(v, 2) for v in t_interval([1.32, 0.54, 1.47], T975[2])])

# 3. Coverage of three recipes with n = 3 normal replicates (seed 1)
rng = random.Random(1)
MU, SIGMA, N, REPS = 1.0, 0.8, 3, 20_000
hits = {"z, sigma known": 0, "z, s plugged in": 0, "t, s": 0}
for _ in range(REPS):
    xs = [rng.gauss(MU, SIGMA) for _ in range(N)]
    m, s = st.fmean(xs), st.stdev(xs)
    hits["z, sigma known"] += abs(m - MU) <= Z975 * SIGMA / math.sqrt(N)
    hits["z, s plugged in"] += abs(m - MU) <= Z975 * s / math.sqrt(N)
    hits["t, s"] += abs(m - MU) <= T975[2] * s / math.sqrt(N)
for k, v in hits.items():
    print(f"coverage {k:15s} {v / REPS:.3f}")


# 4. Exact coverage of Wald and score intervals for an allele frequency, 200 chromosomes
def coverage(method, p, n):
    total = 0.0
    for x in range(n + 1):
        lo, hi = method(x, n)
        if lo <= p <= hi:
            total += math.comb(n, x) * p ** x * (1 - p) ** (n - x)
    return total


for p in (0.3, 0.05, 0.01):
    print(f"p = {p:<4}: Wald {coverage(wald, p, 200):.3f}  score {coverage(score, p, 200):.3f}")

# 5. Zero alternative alleles among 1,000 chromosomes: exact one-sided 95 % upper bound
print("upper bound", round(1 - 0.05 ** (1 / 1000), 5), " rule of three", 3 / 1000)
```

```text
Wald  [0.172, 0.288]  score [0.177, 0.293]
t-interval [-0.13, 2.35]
coverage z, sigma known  0.951
coverage z, s plugged in 0.814
coverage t, s            0.951
p = 0.3 : Wald 0.944  score 0.947
p = 0.05: Wald 0.926  score 0.967
p = 0.01: Wald 0.865  score 0.948
upper bound 0.00299  rule of three 0.003
```

Coverage of a proportion interval is computed exactly by summing binomial probabilities, without simulation. The score interval agrees with SciPy's `binomtest(46, 200).proportion_ci(method="wilson")`, which returns $[0.177, 0.293]$.

## Worked example

> [!example] Three replicates, a doubling, and an interval that includes zero
> A gene's log2 fold change is measured in three independent biological replicates: 1.32, 0.54, 1.47 (invented).
> 1. **Estimate**: $\bar x = 1.11$, about a 2.2-fold increase ($2^{1.11}$).
> 2. **Standard error**: $s = 0.499$, $\mathrm{SE} = 0.499/\sqrt3 = 0.288$.
> 3. **Critical value**: $t_{2,\,0.975} = 4.303$ (not 1.96: $\sigma$ is estimated from 3 values).
> 4. **Interval**: $1.11 \pm 4.303 \times 0.288 = 1.11 \pm 1.24 = [-0.13, 2.35]$.
> 5. **Reading**: the data are compatible with anything from a slight decrease ($2^{-0.13} = 0.91$-fold) to a fivefold increase ($2^{2.35}$). The interval includes 0, so a two-sided t-test of "no change" gives $p > 0.05$. That is not evidence of no effect: the experiment is too small to tell, and the interval says so honestly.

## Common misconceptions

> [!warning] "There is a 95 % probability that the true value is in my interval"
> The true value is fixed; the interval is what varies between experiments. 95 % is the long-run success rate of the procedure. The probability statement about $\theta$ given the data belongs to a Bayesian credible interval, which needs a prior ([[Bayesian Inference]]).

> [!warning] "A 95 % interval for the mean contains 95 % of the data"
> It describes the uncertainty of the mean, which shrinks like $1/\sqrt n$. The range holding 95 % of individual observations is about $\mu \pm 1.96\,\sigma$ and does not shrink with $n$ ([[Sampling Distribution]]).

> [!warning] "If two 95 % intervals overlap, the groups are not significantly different"
> For two independent means with equal standard errors SE, the intervals overlap whenever the difference is below $2 \times 1.96\,\mathrm{SE} = 3.92\,\mathrm{SE}$, but the difference is significant at 5 % once it exceeds $1.96\sqrt2\,\mathrm{SE} = 2.77\,\mathrm{SE}$. A difference of 3 SE gives overlapping intervals and $p = 0.034$. Compare groups with an interval for the difference.

> [!warning] "The normal-approximation interval works for any proportion"
> For rare alleles or low-depth allele fractions, the Wald interval undercovers (0.865 instead of 0.95 at $p = 0.01$ with 200 chromosomes) and collapses to $[0, 0]$ when nothing is observed. Use the score interval, an exact interval, or the rule of three.

## Exercises

> [!question] Exercise 1 (L1)
> Nine replicate measurements of a gene's log2 expression have mean 7.4; the platform's SD is known to be $\sigma = 0.6$. Give the 95 % and 99 % confidence intervals for the mean.

> [!success]- Solution
> $\mathrm{SE} = 0.6/3 = 0.2$. 95 %: $7.4 \pm 1.96 \times 0.2 = [7.008, 7.792]$. 99 %: $7.4 \pm 2.576 \times 0.2 = 7.4 \pm 0.515 = [6.885, 7.915]$. More confidence costs a wider interval.

> [!question] Exercise 2 (L1)
> A colleague reports the allele-frequency interval $[0.172, 0.288]$ and writes "the allele frequency has a 95 % chance of being in this range". Rewrite the sentence correctly.

> [!success]- Solution
> "This interval was produced by a method that captures the true allele frequency in 95 % of studies like ours." Or, more simply: "the data are compatible with allele frequencies between 0.17 and 0.29 at the 95 % confidence level."

> [!question] Exercise 3 (L2)
> How many unrelated individuals must be genotyped to estimate an allele frequency near 0.3 within $\pm 0.02$ at 95 % confidence? And to estimate a frequency that could be anywhere?

> [!success]- Solution
> Chromosomes: $1.96^2 \times 0.21 / 0.02^2 = 2{,}017$, so 1,009 people. Unknown frequency: use the worst case $p(1-p) = 0.25$, giving $1.96^2 \times 0.25/0.0004 = 2{,}401$ chromosomes, 1,201 people.

> [!question] Exercise 4 (L2)
> No carrier of a variant is found among 1,500 unrelated individuals. Give a 95 % upper bound for its allele frequency, and explain why the Wald interval cannot be used.

> [!success]- Solution
> 3,000 chromosomes with zero alternative alleles: $p_U = 1 - 0.05^{1/3000} \approx 3/3000 = 0.001$. Wald uses $\hat p = 0$, so its standard error is 0 and the interval is $[0, 0]$, which would claim certainty that the variant is absent from the population.

> [!question] Exercise 5 (L3, Python)
> Extend `coverage` from the Computational representation to plot or print the exact coverage of the Wald and score intervals for $n = 200$ and $p$ from 0.005 to 0.5. Where does each fall below 0.93?

> [!success]- Solution
> ```python
> for p in (0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5):
>     print(p, round(coverage(wald, p, 200), 3), round(coverage(score, p, 200), 3))
> ```
> Output (one line per $p$): `0.005 0.632 0.92`, `0.01 0.865 0.948`, `0.02 0.908 0.933`, `0.05 0.926 0.967`, `0.1 0.927 0.956`, `0.2 0.941 0.958`, `0.3 0.944 0.947`, `0.5 0.944 0.944`. The Wald interval falls below 0.93 for $p \le 0.1$ and reaches 0.632 at $p = 0.005$ (one expected alternative allele). The score interval stays between 0.92 and 0.97. Coverage jumps irregularly with $p$ because counts are discrete.

> [!question] Exercise 6 (L3)
> Two groups have means 2.0 and 2.9 with standard errors 0.3 each (independent). Do their 95 % intervals overlap? Is the difference significant at 5 %? What interval should be reported?

> [!success]- Solution
> Intervals: $[1.41, 2.59]$ and $[2.31, 3.49]$, which overlap. Difference $0.9$, SE $\sqrt{0.3^2 + 0.3^2} = 0.424$, $z = 2.12$, two-sided $p = 0.034$: significant. Report the interval for the difference, $0.9 \pm 1.96 \times 0.424 = [0.07, 1.73]$, which excludes 0.

## Mastery checklist

- [ ] 1 Recognized: I can state what a 95 % confidence interval is and read one in a paper.
- [ ] 2 Understood: I can explain coverage, the role of the standard error and of the critical value, and why the interpretation is about the procedure.
- [ ] 3 Practiced: I can compute t-intervals for means and Wald and score intervals for proportions, and check coverage by simulation or exact summation.
- [ ] 4 Applied: I reported fold changes or allele frequencies from real data with appropriate intervals, including rare variants.
- [ ] 5 Explained: I can explain the duality with tests, the failure of the Wald interval for rare events, selection effects on reported intervals, and the difference from credible intervals.

## References

[^os8]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 8 "Confidence Intervals" (a single population mean with known standard deviation and with the Student t distribution, a population proportion, sample size).
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x (statistical inference: p-values and confidence intervals).
[^1805-ci]: [[MIT 18.05 - Introduction to Probability and Statistics]], Spring 2022, Reading 22 "Confidence Intervals Based on Normal Data" and Reading 23a "Confidence Intervals: Three Views".
[^1805-boot]: [[MIT 18.05 - Introduction to Probability and Statistics]], Spring 2022, Reading 24 "Bootstrap Confidence Intervals".
[^1805-bayes]: [[MIT 18.05 - Introduction to Probability and Statistics]], Bayesian statistics part (prior and posterior; comparison with frequentist inference).
[^asa]: [[Wasserstein 2016 - The ASA Statement on p-Values]], *The American Statistician* 70(2):129-133.
