---
aliases:
  - p-value
  - P value
  - Observed Significance Level
  - p-value histogram
  - Valeur p
  - Probabilité critique
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Hypothesis Testing]]"
  - "[[Uniform Distribution]]"
  - "[[Cumulative Distribution Function]]"
  - "[[Conditional Probability]]"
related:
  - "[[Sampling Distribution]]"
  - "[[Confidence Interval]]"
  - "[[Effect Size]]"
  - "[[Statistical Power]]"
  - "[[Multiple Testing Correction]]"
  - "[[False Discovery Rate]]"
  - "[[Q-Value]]"
  - "[[P-Hacking]]"
  - "[[E-Value]]"
projects:
  - "[[05-sequence-search]]"
sources:
  - "[[Wasserstein 2016 - The ASA Statement on p-Values]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[HarvardX PH525x - Data Analysis for the Life Sciences]]"
  - "[[Ioannidis 2005 - Why Most Published Research Findings Are False]]"
---

# P-Value

> [!abstract]
> A p-value answers one narrow question: if the null hypothesis and the rest of the model were true, how often would data at least this extreme turn up? Small values signal that the data and the model disagree; they do not give the probability that the hypothesis is true, nor the size of the effect.

## Definition

The **p-value** of an observed test statistic $t_{\text{obs}}$ is the probability, computed under the null hypothesis $H_0$, of obtaining a statistic at least as extreme as $t_{\text{obs}}$: $p = P_{H_0}(T \ge t_{\text{obs}})$ for an upper-tailed test.[^1805][^os9][^ph525] In the words of the American Statistical Association, it is "the probability under a specified statistical model that a statistical summary of the data would be equal to or more extreme than its observed value".[^asa]

## Why it matters

- **It is the currency of genomics output.** Differential expression tables have a `pvalue` column and an adjusted one; association studies plot $-\log_{10} p$ along the genome; enrichment tools rank terms by p-value ([[Differential Expression Analysis]], [[Genome-Wide Association Study]]).[^holmes]
- **Its histogram is a quality check.** The distribution of thousands of p-values from one screen reveals real signal, lack of power, or a broken null model before any correction is applied (Deeper).[^holmes]
- **Multiple-testing procedures take p-values as input.** Bonferroni, Benjamini-Hochberg and q-values all assume p-values are uniform under the null ([[Multiple Testing Correction]], [[Benjamini-Hochberg Procedure]], [[Q-Value]]).
- **It is the most misread number in science.** The ASA issued its 2016 statement because of widespread misuse; reading a p-value correctly is a basic skill of a bioinformatician who reports results.[^asa]
- **Sequence search** reports significance as E-values, which are expected counts of chance hits rather than p-values but rest on the same null-distribution logic ([[E-Value]], [[05-sequence-search]]).

## Core (L1)

### Computing a p-value

1. Fix $H_0$ and a test statistic $T$ whose null distribution is known ([[Hypothesis Testing]]).
2. Compute $t_{\text{obs}}$ from the data.
3. Take the null probability of the region "as or more extreme", in the direction(s) of $H_1$:[^os9]

| Alternative | p-value |
|---|---|
| upper ($\mu > \mu_0$) | $P_{H_0}(T \ge t_{\text{obs}})$ |
| lower ($\mu < \mu_0$) | $P_{H_0}(T \le t_{\text{obs}})$ |
| two-sided, symmetric null | $P_{H_0}(\lvert T\rvert \ge \lvert t_{\text{obs}}\rvert) = 2\,P_{H_0}(T \ge \lvert t_{\text{obs}}\rvert)$ |

For a z statistic of 2.3: one-sided $p = 1 - \Phi(2.3) = 0.0107$, two-sided $p = 0.0214$ ([[Normal Distribution]]). For a discrete statistic, "at least as extreme" includes the observed value: 8 alternative-allele reads out of 10 at a heterozygous site give an exact binomial two-sided $p = 2 \times P(X \ge 8) = 2 \times 56/1024 = 0.109$ ([[Binomial Distribution]]).

### p-values and decisions

Rejecting $H_0$ when $p \le \alpha$ is the same rule as rejecting when $t_{\text{obs}}$ falls in the level-$\alpha$ rejection region.[^1805] The p-value adds a graded summary: $p = 0.049$ and $p = 10^{-9}$ both reject at 5 % but are not equally surprising under $H_0$. $\alpha$ is chosen before the data; $p$ is computed from them.

### What a p-value does not mean

The ASA statement summarizes the correct reading in six principles:[^asa]

| ASA principle (paraphrased) | Consequence for a gene with $p = 0.01$ |
|---|---|
| 1. p-values can indicate how incompatible the data are with a specified model | The data would be unusual (1 % or less) if the gene did not change **and** the model's assumptions held. |
| 2. They do not measure the probability that the hypothesis is true, nor that the data were produced by chance alone | Not "a 1 % chance the gene is unchanged" ([[Bayes' Theorem]]). |
| 3. Conclusions should not rest only on whether $p$ passes a threshold | 0.049 and 0.051 are nearly the same evidence. |
| 4. Proper inference requires full reporting and transparency | A p-value chosen among many analyses loses its meaning ([[P-Hacking]]). |
| 5. A p-value does not measure the size of an effect or its importance | Report the fold change and its interval ([[Effect Size]], [[Confidence Interval]]). |
| 6. By itself, a p-value is not a good measure of evidence about a model or hypothesis | Combine with effect size, design, prior plausibility and replication. |

### Bio: the p-value histogram of a genome-wide screen

When $H_0$ is true and $T$ is continuous, the p-value is uniform on $[0, 1]$ ([[Uniform Distribution#p-values are uniform under the null hypothesis]]).[^blitz5] A screen of 20,000 genes mixes null genes, whose p-values spread evenly, with real effects, which pile up near 0. Plotting the histogram of all p-values is the first thing to do with a screen.[^holmes]

![[p-value-histogram-diagnostic-shapes.svg]]

## Deeper (L2)

### A p-value is a random variable

Repeat the same experiment and the p-value changes, often a lot. Ten simulated replications of a study whose power at $\alpha = 0.05$ is exactly 0.5 (true effect $1.96$ standard errors) give:

```text
0.005 0.006 0.986 0.070 0.011 0.017 0.351 0.229 0.026 0.467
```

The same true effect produces $p = 0.005$ and $p = 0.986$. Under $H_0$ the p-value is uniform; under $H_1$ its distribution is pushed toward 0, more strongly as power grows ([[Statistical Power]]). A single p-value is a noisy summary of one experiment.

### Reading the four shapes

The figure shows four simulated screens of 10,000 tests each (code below):[^holmes]

- **A. Flat**: all genes null. About 5 % fall below 0.05 (504 of 10,000): these are the false positives that any threshold of 0.05 lets through. A flat histogram can also mean real effects tested with no power.
- **B. Spike over a flat floor**: 8,000 null and 2,000 real effects. The floor is the null part, and its height estimates the null fraction $\pi_0$: here $\hat\pi_0 = 0.81$ from the p-values above 0.5 ([[Uniform Distribution#Advanced (L3)]], [[Q-Value]]). This is the shape that [[False Discovery Rate]] procedures expect.
- **C. Mass near 1**: exact tests on sites with 2 to 8 reads. With so few reads most outcomes are compatible with $H_0$, and the discrete p-values cannot be small (with 2 reads the smallest two-sided binomial p-value is 0.5): a conservative test, with 48 % of the p-values exactly equal to 1. Remove features that cannot reach significance before testing; the $\pi_0$ estimate (1.36) is meaningless here.
- **D. Slope, no real effect**: all genes null, but the test assumed an SD of 1 while the real SD was 1.3 (biological variability or a batch effect left out of the model). Small p-values are inflated everywhere: 1,278 genes below 0.05 instead of about 500, and a $\pi_0$ estimate of 0.78 suggests 22 % real effects where there are none. The fix is the model, not the multiple-testing correction ([[Batch Effect]]).

### The $-\log_{10}$ scale

Small p-values span many orders of magnitude, so plots use $-\log_{10} p$: $p = 0.05$ is 1.3, $p = 10^{-8}$ is 8. Volcano plots put $-\log_{10} p$ against the log fold change and so show the evidence and the [[Effect Size]] on two separate axes; Manhattan plots show $-\log_{10} p$ along the genome.

### The p-value mixes effect size and sample size

For a z-test, $z = \hat\delta/\mathrm{SE}$ and $\mathrm{SE} \propto 1/\sqrt n$. A tiny effect measured precisely and a large effect measured roughly can give the same $p$. A log2 fold change of 0.05 with SE 0.01 ($p = 5.7 \times 10^{-7}$) is more "significant" than a fourfold change of 2.0 with SE 0.5 ($p = 6.3 \times 10^{-5}$).[^asa]

## Advanced (L3)

- **Validity is all that is required.** A p-value is **valid** if $P_{H_0}(p \le \alpha) \le \alpha$ for every $\alpha$; it is exactly uniform for continuous statistics and conservative (below the diagonal) for discrete ones ([[Cumulative Distribution Function#Advanced (L3)]]). A permutation p-value computed from $B$ random permutations as $(b + 1)/(B + 1)$, where $b$ permutations are at least as extreme as the data, is valid and never 0; it cannot fall below $1/(B + 1)$, so tiny p-values need many permutations ([[Permutation Test]]).
- **p just below 0.05 is weak evidence.** In screen B, 20 % of the genes with $p \le 0.05$ are null, but among genes with $0.04 < p \le 0.05$ the null fraction is 68 % (78 null, 37 real). Real effects mostly produce much smaller p-values, so a borderline p-value is more likely to come from a null gene than its "significance" suggests. Low power and few real effects make it worse.[^ioannidis]
- **Replication is a coin flip at the threshold.** If the true effect equals the one observed at $p = 0.05$ (two-sided, $z = 1.96$), an identical replication has $z \sim \mathcal N(1.96, 1)$ and reaches $p \le 0.05$ in the same direction with probability $\Phi(0) = 0.5$. "Significant" results near the threshold fail to replicate about half the time even when the effect is real.
- **Selection breaks uniformity.** If several analyses are tried (normalizations, covariates, outlier rules, subsets) and the smallest p-value is reported, the reported value is no longer uniform under $H_0$: it is the minimum of several p-values ([[Uniform Distribution#Advanced (L3)]]). This is why ASA principle 4 asks for full reporting ([[P-Hacking]], [[Analytical Flexibility]]).[^asa]
- **Far tails depend on the model.** A p-value of $10^{-12}$ is a statement about the far tail of the null distribution, where approximations (normal, chi-square) and small model violations matter most ([[Normal Distribution#Advanced (L3)]]). Rank genes by such values, but do not read their exact size literally.

## Mathematical representation

- **Upper-tailed**: $p(x) = P_{H_0}\big(T(X) \ge T(x)\big) = 1 - F_0\big(T(x)^-\big)$, where $x$ is the observed data, $X$ a hypothetical sample drawn under $H_0$, $F_0$ the null CDF of $T$, and $T(x)^-$ means the limit from the left (so the observed value is included when $T$ is discrete).
- **Two-sided, symmetric null**: $p = P_{H_0}(|T| \ge |t_{\text{obs}}|)$; for a z statistic, $p = 2[1 - \Phi(|z|)]$.
- **Composite null** $H_0: \theta \in \Theta_0$: $p(x) = \sup_{\theta \in \Theta_0} P_\theta(T(X) \ge T(x))$.
- **Validity**: $P_{H_0}(p(X) \le \alpha) \le \alpha$ for all $\alpha \in [0, 1]$, with equality when $F_0$ is continuous (probability integral transform).[^blitz5]
- **Decision**: reject at level $\alpha$ $\iff$ $p \le \alpha$ $\iff$ $t_{\text{obs}}$ lies in the level-$\alpha$ rejection region.
- **Under $H_1$** (z-test, true standardized effect $\Delta$): $P(p \le \alpha) = \Phi(\Delta - z_{1-\alpha/2}) + \Phi(-\Delta - z_{1-\alpha/2})$, the power.

## Computational representation

The script computes normal and exact binomial p-values, simulates replications, and builds the four screens of the figure with one seeded generator.

```python
import math
import random
from statistics import NormalDist

PHI = NormalDist()


def p_two_sided_z(z):
    return 2 * (1 - PHI.cdf(abs(z)))


def p_binom_two_sided(x, n, p=0.5):
    """Exact two-sided binomial p-value: total probability of outcomes no more likely than x."""
    pmf = [math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]
    return min(1.0, sum(q for q in pmf if q <= pmf[x] * (1 + 1e-9)))


# 1. Computing p-values
print(f"z = 2.3: one-sided {1 - PHI.cdf(2.3):.4f}, two-sided {p_two_sided_z(2.3):.4f}")
print(f"8 alternative reads out of 10 at a heterozygous site: p = {p_binom_two_sided(8, 10):.3f}")

rng = random.Random(2026)

# 2. Same experiment, ten replications, true effect with power 0.5 at alpha = 0.05
print("ten replications:", " ".join(f"{p_two_sided_z(rng.gauss(1.96, 1)):.3f}" for _ in range(10)))


# 3. Four genome-wide screens of 10,000 tests each (all invented)
def histogram(ps, bins=10):
    counts = [0] * bins
    for p in ps:
        counts[min(int(p * bins), bins - 1)] += 1
    return counts


screens = {
    "A no signal": [p_two_sided_z(rng.gauss(0, 1)) for _ in range(10_000)],
    "B signal": [p_two_sided_z(rng.gauss(0, 1)) for _ in range(8_000)]
                + [p_two_sided_z(rng.gauss(3, 1)) for _ in range(2_000)],
    "C low counts": [p_binom_two_sided(sum(rng.random() < 0.5 for _ in range(d)), d)
                     for d in (rng.randint(2, 8) for _ in range(10_000))],
    "D wrong null": [p_two_sided_z(rng.gauss(0, 1.3)) for _ in range(10_000)],
}
for name, ps in screens.items():
    small = sum(p <= 0.05 for p in ps)
    pi0 = sum(p > 0.5 for p in ps) / (0.5 * len(ps))
    print(f"{name:13s} bins {histogram(ps)}  p<=0.05: {small:5d}  pi0 estimate {pi0:.2f}")

# 4. Screen B: how often is a 'significant' gene null, overall and just below 0.05?
null_b, alt_b = screens["B signal"][:8_000], screens["B signal"][8_000:]
for lo, hi in ((0.0, 0.05), (0.04, 0.05)):
    n0 = sum(lo < p <= hi for p in null_b)
    n1 = sum(lo < p <= hi for p in alt_b)
    print(f"p in ({lo}, {hi}]: {n0} null, {n1} real, fraction null {n0 / (n0 + n1):.2f}")
```

```text
z = 2.3: one-sided 0.0107, two-sided 0.0214
8 alternative reads out of 10 at a heterozygous site: p = 0.109
ten replications: 0.005 0.006 0.986 0.070 0.011 0.017 0.351 0.229 0.026 0.467
A no signal   bins [977, 990, 963, 1026, 976, 1022, 992, 1043, 988, 1023]  p<=0.05:   504  pi0 estimate 1.01
B signal      bins [2635, 858, 847, 755, 877, 817, 798, 814, 799, 800]  p<=0.05:  2138  pi0 estimate 0.81
C low counts  bins [242, 335, 957, 475, 462, 747, 1365, 594, 0, 4823]  p<=0.05:    77  pi0 estimate 1.36
D wrong null  bins [2043, 1230, 1031, 917, 886, 839, 812, 779, 753, 710]  p<=0.05:  1278  pi0 estimate 0.78
p in (0.0, 0.05]: 423 null, 1715 real, fraction null 0.20
p in (0.04, 0.05]: 78 null, 37 real, fraction null 0.68
```

The binomial p-value matches SciPy's `binomtest(8, 10).pvalue` (0.109375). The tolerance `1 + 1e-9` keeps outcomes whose probability equals that of $x$ despite rounding.

## Worked example

> [!example] Reading screen B before correcting anything
> A differential expression screen returns 10,000 p-values with the histogram of panel B (simulated).
> 1. **Shape**: a spike in the first bin over a flat floor: signal plus well-behaved nulls. Proceed.
> 2. **Null fraction**: 4,028 p-values exceed 0.5; a uniform floor would put $\pi_0 \times 10{,}000 \times 0.5$ there, so $\hat\pi_0 = 4{,}028/5{,}000 = 0.81$ (true value 0.80).
> 3. **Expected false positives at 0.05**: $0.05 \times \hat\pi_0 \times 10{,}000 \approx 403$ (the simulation has 423).
> 4. **Discoveries at 0.05**: 2,138, so roughly $403/2{,}138 \approx 19\%$ of them are expected to be false: an estimate of the false discovery proportion at this threshold ([[False Discovery Rate]], [[Benjamini-Hochberg Procedure]]).
> 5. **What not to say**: "gene X has $p = 0.003$, so it is 99.7 % likely to be differentially expressed". The p-value is a probability about the data under $H_0$, not about $H_0$.

## Common misconceptions

> [!warning] "$p$ is the probability that the null hypothesis is true"
> $p = P(\text{data this extreme} \mid H_0)$, while the probability that $H_0$ is true given the data is $P(H_0 \mid \text{data})$, which also depends on the prior fraction of true nulls and on power ([[Bayes' Theorem]]). Near $p = 0.05$ the two can differ by an order of magnitude (68 % null in screen B).[^asa]

> [!warning] "$p = 0.03$ means a 3 % chance that the result is due to chance"
> The calculation assumes chance alone (and the model) is at work; it cannot also be the probability of that assumption. ASA principle 2 rejects this reading explicitly.[^asa]

> [!warning] "$p > 0.05$ shows there is no effect"
> Large p-values arise under $H_1$ whenever power is low: in the ten replications above, a real effect gave $p = 0.986$. Only an interval that excludes meaningful effects supports "no important effect".

> [!warning] "A smaller p-value means a bigger effect"
> $p$ depends on effect size and on precision. A 3.5 % change can have a smaller p-value than a fourfold change (Deeper).[^asa]

## Exercises

> [!question] Exercise 1 (L1)
> A z statistic equals $-2.5$. Give the lower-tailed, upper-tailed and two-sided p-values. Which one answers "is there any difference?"

> [!success]- Solution
> Lower: $\Phi(-2.5) = 0.0062$. Upper: $1 - \Phi(-2.5) = 0.9938$. Two-sided: $2 \times 0.0062 = 0.0124$. "Any difference" is the two-sided question; the one-sided values are valid only if the direction was fixed in advance.

> [!question] Exercise 2 (L1)
> Which statements about $p = 0.02$ for a gene are correct? (a) If the gene did not change and the model is right, data at least this extreme occur 2 % of the time. (b) The gene has a 98 % chance of being differentially expressed. (c) The fold change is large. (d) At $\alpha = 0.05$, $H_0$ is rejected.

> [!success]- Solution
> (a) and (d) are correct. (b) confuses $P(\text{data} \mid H_0)$ with $P(H_0 \mid \text{data})$ (ASA principle 2). (c) is not implied: the p-value does not measure effect size (principle 5).

> [!question] Exercise 3 (L2)
> At a site with 5 reads, all 5 carry the alternative allele. Compute the exact two-sided binomial p-value against $p = 0.5$. What is the smallest p-value achievable with 4 reads, and what does this imply for the histogram of a low-depth screen?

> [!success]- Solution
> $P(X = 5) = 1/32$, and by symmetry the outcome 0 is as extreme: $p = 2/32 = 0.0625$. With 4 reads the smallest is $2/16 = 0.125$. Low-depth sites can never reach 0.05; their p-values are discrete and pile up toward 1 (panel C), so they add tests without adding discoveries and should be filtered before testing.

> [!question] Exercise 4 (L2)
> A histogram of 15,000 p-values has about 600 p-values in each of the 19 bins from 0.05 to 1 and 3,600 in the first bin. Estimate $\pi_0$ and the number of true effects, and say whether the shape looks healthy.

> [!success]- Solution
> A flat floor of 600 per bin of width 0.05 corresponds to $600 \times 20 = 12{,}000$ null p-values over $[0, 1]$, so $\hat\pi_0 = 12{,}000/15{,}000 = 0.8$ and about 3,000 true effects. Of the 3,600 in the first bin, about 600 are null. Flat floor plus spike: healthy (panel B).

> [!question] Exercise 5 (L3, Python)
> Show by simulation (seed 5, 100,000 runs) that if the true standardized effect equals 1.96, an exact replication of a study reaches two-sided $p \le 0.05$ in the same direction about half the time. What is that probability if the true effect is 2.8 (80 % power)?

> [!success]- Solution
> ```python
> import random
>
> rng = random.Random(5)
> for delta in (1.96, 2.8):
>     hits = sum(rng.gauss(delta, 1) >= 1.96 for _ in range(100_000))
>     print(delta, hits / 100_000)
> ```
> Output: `1.96 0.49886` and `2.8 0.80018`. A replication succeeds with probability equal to the power; an effect that only just reached significance has about 50 % power, which is why borderline findings often fail to replicate.

> [!question] Exercise 6 (L3)
> An analyst tries 5 independent analysis variants on data where $H_0$ is true and reports the smallest p-value. What is the probability that the reported value is at most 0.05? What would the histogram of such reported p-values look like?

> [!success]- Solution
> The minimum of 5 independent uniforms satisfies $P(\min \le 0.05) = 1 - 0.95^5 = 0.226$, not 0.05. Its density is $5(1 - p)^4$, a histogram decreasing steeply from 0 to 1 with no flat floor. Real variants are correlated, which brings the rate down toward 0.05, reached only if all variants gave the same p-value.

## Mastery checklist

- [ ] 1 Recognized: I can define the p-value as a tail probability under $H_0$ and relate it to $\alpha$.
- [ ] 2 Understood: I can state the six ASA principles and explain why $P(\text{data} \mid H_0) \ne P(H_0 \mid \text{data})$.
- [ ] 3 Practiced: I can compute one- and two-sided, normal and exact p-values, and simulate p-value distributions under $H_0$ and $H_1$.
- [ ] 4 Applied: I read the p-value histogram of a real screen, estimated $\pi_0$ and diagnosed conservative or miscalibrated tests before correcting.
- [ ] 5 Explained: I can explain validity, discreteness, selection effects, replication probability and why borderline p-values are weak evidence.

## References

[^asa]: [[Wasserstein 2016 - The ASA Statement on p-Values]], *The American Statistician* 70(2):129-133 (informal definition and principles 1 to 6).
[^1805]: [[MIT 18.05 - Introduction to Probability and Statistics]], Spring 2022, Readings 17b, 18 and 19 "Null Hypothesis Significance Testing I, II and III".
[^os9]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 9 "Hypothesis Testing with One Sample" (p-values, decision and conclusion).
[^blitz5]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 5 "Continuous Random Variables" (universality of the uniform).
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], treatment of hypothesis testing and multiple testing (the p-value histogram).
[^ph525]: [[HarvardX PH525x - Data Analysis for the Life Sciences]], PH525.1x (statistical inference: p-values and confidence intervals).
[^ioannidis]: [[Ioannidis 2005 - Why Most Published Research Findings Are False]], *PLoS Medicine* 2(8):e124.
