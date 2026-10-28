---
aliases:
  - Power (Statistics)
  - Power Analysis
  - Sample Size Calculation
  - Sample Size Determination
  - Puissance statistique
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - domain/scientific-practice
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Hypothesis Testing]]"
  - "[[P-Value]]"
  - "[[Sampling Distribution]]"
  - "[[Normal Distribution]]"
  - "[[Student's t-Distribution]]"
  - "[[Student's t-Test]]"
related:
  - "[[Effect Size]]"
  - "[[Experimental Design]]"
  - "[[Biological Replicate]]"
  - "[[Pilot Study]]"
  - "[[Sequencing Experiment Design]]"
  - "[[Multiple Testing Correction]]"
  - "[[False Discovery Rate]]"
  - "[[Genome-Wide Association Study]]"
  - "[[Differential Expression Analysis]]"
  - "[[Negative Binomial Distribution]]"
  - "[[Monte Carlo Method]]"
projects: []
sources:
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Experimental Design for Laboratory Biologists (Lazic)]]"
  - "[[Schurch 2016 - How Many Biological Replicates Are Needed in an RNA-Seq Experiment]]"
  - "[[Love 2014 - Moderated Estimation of Fold Change and Dispersion for RNA-Seq Data with DESeq2]]"
  - "[[Benjamini 1995 - Controlling the False Discovery Rate]]"
  - "[[Risch 1996 - The Future of Genetic Studies of Complex Human Diseases]]"
  - "[[Clarke 2011 - Basic Statistical Analysis in Genetic Case-Control Studies]]"
  - "[[Ioannidis 2005 - Why Most Published Research Findings Are False]]"
---

# Statistical Power

> [!abstract]
> Statistical power is the probability that an experiment detects an effect that is really there. It is fixed before any data are collected, by the size of the effect, the noise, the significance threshold and the number of replicates; planning it is how one decides how many RNA-seq replicates or GWAS cases to collect.

## Definition

The **power** of a test against a specific alternative is the probability of rejecting the null hypothesis when that alternative is true: $1 - \beta$, where $\beta$ is the type II error rate ([[Hypothesis Testing]]). Seen as a function of the true parameter, it is the **power function** of the test. Power increases with the size of the true effect, the significance level $\alpha$ and the sample size, and decreases with the variability of the measurements.[^1805][^lazic]

## Why it matters

- **It is a design decision.** The number of replicates, patients or sequencing runs is chosen so that the smallest effect worth detecting has a high probability (for example 80 %) of being detected; after the experiment, it is too late ([[Experimental Design]]).[^lazic]
- **RNA-seq replicates.** In an experiment with 48 biological replicates per condition, subsets of three replicates let most tools find only 20 to 40 % of the differentially expressed genes; the authors recommend at least six replicates, and at least twelve to find them at all fold changes.[^schurch]
- **GWAS cases.** Genes of modest effect are out of reach of linkage studies of realistic size but within reach of association studies, provided they are large enough to pass a genome-wide threshold of $5 \times 10^{-8}$ ([[Genome-Wide Association Study]]).[^risch]
- **Low power corrupts the literature.** In underpowered studies a significant result is less likely to be true, and when it is, its effect size is exaggerated ([[Hypothesis Testing#Advanced (L3)]]).[^ioannidis]

## Core (L2)

### Four quantities: fix three, solve for the fourth

| Change | Effect on power | Why |
|---|---|---|
| larger true effect $\delta$ | up | the alternative distribution moves away from the null |
| larger noise $\sigma$ | down | both distributions widen and overlap more |
| more replicates $n$ | up | the standard error shrinks like $1/\sqrt n$ ([[Sampling Distribution]]) |
| smaller $\alpha$ | down | the rejection region moves outward |

The one-sample version of these formulas, with its figure, is in [[Hypothesis Testing#Deeper (L2)]]; this note extends it to the designs used in practice.

### Two independent groups

Comparing two groups of $n$ samples each, with between-sample SD $\sigma$, the difference of means has standard error $\sigma\sqrt{2/n}$: both means are estimated. The two-sided test at level $\alpha$ has, in the normal approximation,

$$1 - \beta = \Phi\!\left(\frac{\delta}{\sigma\sqrt{2/n}} - z_{1-\alpha/2}\right) + \Phi\!\left(-\frac{\delta}{\sigma\sqrt{2/n}} - z_{1-\alpha/2}\right), \qquad n \approx \frac{2(z_{1-\alpha/2} + z_{1-\beta})^2\sigma^2}{\delta^2}.$$

For a doubling of expression ($\delta = 1$ on the log2 scale) with $\sigma = 0.8$, the formula asks for 11 samples per group for 80 % power. With few samples the normal approximation is optimistic, because the t-test must also estimate $\sigma$ ([[Student's t-Distribution]]): the exact t-test power is 0.220 with 3 per group (against 0.334 for the approximation) and 0.796 with 11, so 12 per group are needed (code below). Welch's test, which does not assume equal variances, has even less power with 3 per group (0.166 by simulation).

### Bio: how many RNA-seq replicates?

Model the reads of one gene with a [[Negative Binomial Distribution|negative binomial]]: mean $\mu$ reads per sample and variance $\mu + \varphi\mu^2$, where $\varphi$ is the dispersion (written $\alpha$ in other notes; here $\alpha$ is the significance level).[^love] By the delta method, the log of a mean of $n$ replicates has variance about $(1/\mu + \varphi)/n$ ([[Variance#Advanced (L3)]]), so the estimated log fold change between groups with means $\mu$ and $\mu \cdot \mathrm{FC}$ has

$$\mathrm{Var}(\widehat{\ln \mathrm{FC}}) \approx \frac{1}{n}\left(\frac{1}{\mu} + \frac{1}{\mu\,\mathrm{FC}} + 2\varphi\right).$$

Two consequences follow. **Depth** only reduces the $1/\mu$ terms: once $1/\mu$ is small next to $\varphi$, more reads change almost nothing. **Replicates** divide the whole variance by $n$, including the biological part. With $\varphi = 0.1$ and a per-gene threshold $\alpha = 0.001$ (code below), a two-fold change in a gene with 100 reads per sample is detected with probability 0.24 with 3 replicates per group, 0.65 with 6 and 0.97 with 12, and 8 replicates reach 80 %. Ten times more reads only moves these to 0.27, 0.69 and 0.98; at 10 reads, 13 replicates are needed; a 1.5-fold change at 100 reads needs 23.

![[rnaseq-power-replicates-depth.svg]]

Why a per-gene $\alpha$ of 0.001? The Benjamini-Hochberg procedure at a false discovery rate of 5 % finds the largest $k$ such that the $k$-th smallest p-value is at most $k \times 0.05/m$, and calls those $k$ genes;[^bh] if 1,000 of $m = 20{,}000$ genes are called, the largest called p-value is at most $1{,}000 \times 0.05/20{,}000 = 0.0025$ ([[Benjamini-Hochberg Procedure]]). The model is optimistic for small $n$, because it treats $\varphi$ as known while each gene's dispersion must be estimated from the same few replicates ([[Dispersion Estimation]]); empirical benchmarks with many replicates are the check on such calculations.[^schurch]

### Bio: how many GWAS cases?

The allelic test compares the frequency of an allele between the $2N$ chromosomes of cases and the $2N$ of controls ([[Chi-Square Test]], [[Contingency Table]]).[^clarke] If the allele has frequency $p_0$ in controls and multiplies the odds of disease by OR per copy, its frequency in cases is $p_1 = \mathrm{OR}\,p_0 / (1 - p_0 + \mathrm{OR}\,p_0)$. At the genome-wide threshold $5 \times 10^{-8}$,[^risch] the cases needed for 80 % power (with as many controls) are:

| Control allele frequency | OR 1.1 | OR 1.2 | OR 1.5 |
|---|---|---|---|
| 0.30 | 20,384 | 5,486 | 1,074 |
| 0.05 | 87,966 | 23,145 | 4,262 |

Halving the log odds ratio roughly quadruples the sample, and rarer alleles carry less information per subject. Studies of thousands to hundreds of thousands of subjects follow directly from this arithmetic.

## Advanced (L3)

### Power by simulation

When no formula fits the analysis (a Welch test with 3 samples, a negative binomial GLM, a permutation test), simulate it: generate data under the alternative from a [[Statistical Model]], run the real analysis, and count rejections. With $R$ simulated experiments, the estimate has standard error $\sqrt{\hat\pi(1 - \hat\pi)/R}$ ([[Monte Carlo Method]]). Simulation also checks formulas: the Welch test's 0.166 with 3 samples per group is half the normal approximation's 0.334.

### Multiple testing raises the bar

Testing $m$ hypotheses at a Bonferroni level $\alpha/m$ ([[Family-Wise Error Rate]]) multiplies the required sample by $\left[(z_{1-\alpha/(2m)} + z_{1-\beta})/(z_{1-\alpha/2} + z_{1-\beta})\right]^2$. For $m = 20{,}000$ genes, $z_{1-\alpha/(2m)} = 4.71$ and the factor is 3.92: about four times more replicates than a single test. Control of the [[False Discovery Rate]] needs less, by an amount that depends on how many genes truly change ([[Multiple Testing Correction]]).

### Low power exaggerates what is found

Simulate experiments with a true effect of 0.5 SD and 10 samples per group: power is 0.20. Over all experiments the estimated effect averages 0.501, unbiased. Among the 20 % that reach significance, it averages 1.116: **2.2 times the truth**, because only the experiments where noise added to the effect cross the threshold; 0.5 % of the significant ones even have the wrong sign. Selecting on significance in low-power studies guarantees inflated effect sizes. An independent replication, not selected on its own significance, estimates the effect without this inflation, so discovered effects appear to shrink when they are replicated ([[Effect Size]]).

### Power computed after the experiment says nothing new

"Observed power", computed by plugging the observed effect into the power formula, is a function of the p-value alone: an observed $|z| = z_{1-\alpha/2}$ (that is, $p = \alpha$) gives power $\Phi(0) + \Phi(-2z_{1-\alpha/2}) \approx 0.5$; $p = 0.2$ ($|z| = 1.282$) gives $\Phi(-0.678) + \Phi(-3.24) = 0.249$ and $p = 0.5$ gives 0.104. A non-significant result always has low observed power, so this number cannot rescue or condemn it. After the experiment, report the [[Confidence Interval]] of the effect; power belongs to planning.

## Mathematical representation

- **Two groups, known $\sigma$.** $T = (\bar X_B - \bar X_A)/(\sigma\sqrt{2/n}) \sim \mathcal N(\lambda, 1)$ with $\lambda = \delta/(\sigma\sqrt{2/n})$, so $\pi = \Phi(\lambda - z_{1-\alpha/2}) + \Phi(-\lambda - z_{1-\alpha/2})$. Neglecting the far tail and solving $\lambda = z_{1-\alpha/2} + z_{1-\beta}$ gives $n = 2(z_{1-\alpha/2} + z_{1-\beta})^2\sigma^2/\delta^2$.
- **Two groups, estimated $\sigma$.** The pooled t statistic follows a noncentral t distribution with $2n - 2$ degrees of freedom and noncentrality $\lambda$; $\pi = P(|T'| > t_{1-\alpha/2,\,2n-2})$.
- **Negative binomial counts.** With $\mathrm{Var}(K) = \mu + \varphi\mu^2$ and $g = \ln$, $\mathrm{Var}(\ln \bar K) \approx (\mu + \varphi\mu^2)/(n\mu^2) = (1/\mu + \varphi)/n$; the log fold change sums two such independent terms, and $\pi = \Phi(|\ln \mathrm{FC}|/\mathrm{SE} - z_{1-\alpha/2}) + \Phi(-|\ln \mathrm{FC}|/\mathrm{SE} - z_{1-\alpha/2})$.
- **Allelic test.** $p_1 = \mathrm{OR}\,p_0/(1 - p_0 + \mathrm{OR}\,p_0)$; under $H_0$ the difference $\hat p_1 - \hat p_0$ has $\mathrm{SE}_0 = \sqrt{\bar p(1-\bar p)\left(\frac{1}{2N_1} + \frac{1}{2N_0}\right)}$, under $H_1$ $\mathrm{SE}_1 = \sqrt{\frac{p_1(1-p_1)}{2N_1} + \frac{p_0(1-p_0)}{2N_0}}$, and $\pi = \Phi\!\left(\frac{|p_1 - p_0| - z_{1-\alpha/2}\mathrm{SE}_0}{\mathrm{SE}_1}\right)$ plus a negligible far tail.

## Computational representation

Power formulas need only `statistics.NormalDist`; the exact t-test power uses SciPy's noncentral t distribution.

```python
import math
from statistics import NormalDist

from scipy import stats

Z = NormalDist()


def power_two_groups(delta, sigma, n, alpha=0.05):
    """Normal approximation: two-sided test of a difference of two means, n per group."""
    shift = delta / (sigma * math.sqrt(2 / n))
    c = Z.inv_cdf(1 - alpha / 2)
    return Z.cdf(shift - c) + Z.cdf(-shift - c)


def power_t(delta, sigma, n, alpha=0.05):
    """Exact power of the two-sample t-test (equal variances, n per group): noncentral t distribution."""
    df, ncp = 2 * n - 2, delta / (sigma * math.sqrt(2 / n))
    c = stats.t.ppf(1 - alpha / 2, df)
    return stats.nct.sf(c, df, ncp) + stats.nct.cdf(-c, df, ncp)


def power_rnaseq(fold_change, mu, phi, n, alpha):
    """Wald test of a log fold change for negative binomial counts (delta method), n replicates per group."""
    var = (1 / mu + 1 / (mu * fold_change) + 2 * phi) / n
    shift = abs(math.log(fold_change)) / math.sqrt(var)
    c = Z.inv_cdf(1 - alpha / 2)
    return Z.cdf(shift - c) + Z.cdf(-shift - c)


def gwas_power(p0, odds_ratio, cases, controls, alpha=5e-8):
    """Allelic test: alternative-allele frequency in 2*cases versus 2*controls chromosomes."""
    p1 = odds_ratio * p0 / (1 - p0 + odds_ratio * p0)
    pbar = (cases * p1 + controls * p0) / (cases + controls)
    se0 = math.sqrt(pbar * (1 - pbar) * (1 / (2 * cases) + 1 / (2 * controls)))    # SE under H0
    se1 = math.sqrt(p1 * (1 - p1) / (2 * cases) + p0 * (1 - p0) / (2 * controls))   # SE under H1
    c, d = Z.inv_cdf(1 - alpha / 2), p1 - p0
    return Z.cdf((d - c * se0) / se1) + Z.cdf((-d - c * se0) / se1)


def smallest_n(power_of_n, target=0.8):
    """Smallest n (from 2 upward) whose power reaches the target."""
    n = 2
    while power_of_n(n) < target:
        n += 1
    return n


# 1. Two groups: a doubling (delta = 1 on the log2 scale) with between-sample SD 0.8
n80 = smallest_n(lambda n: power_two_groups(1, 0.8, n))
n80_t = smallest_n(lambda n: power_t(1, 0.8, n))
print(f"n per group for 80 % power: normal approximation {n80}, exact t-test {n80_t}")
for n in (3, 6, 11):
    print(f"  n = {n:2d}: normal approximation {power_two_groups(1, 0.8, n):.3f}, exact t-test {power_t(1, 0.8, n):.3f}")

# 2. RNA-seq: power per gene (dispersion 0.1, per-gene alpha 0.001) and replicates for 80 %
print("RNA-seq        n=3    n=6   n=12   n for 80 %")
for fc, mu in ((2, 10), (2, 100), (2, 1000), (1.5, 100)):
    row = "  ".join(f"{power_rnaseq(fc, mu, 0.1, n, 0.001):.3f}" for n in (3, 6, 12))
    need = smallest_n(lambda n: power_rnaseq(fc, mu, 0.1, n, 0.001))
    print(f"FC {fc:<3} mu {mu:<5} {row}   {need}")

# 3. GWAS: cases needed (as many controls) for 80 % power at the genome-wide threshold 5e-8
for p0 in (0.3, 0.05):
    needs = [smallest_n(lambda n: gwas_power(p0, oratio, n, n)) for oratio in (1.1, 1.2, 1.5)]
    print(f"control allele frequency {p0}: cases for OR 1.1, 1.2, 1.5 = {needs}")
```

```text
n per group for 80 % power: normal approximation 11, exact t-test 12
  n =  3: normal approximation 0.334, exact t-test 0.220
  n =  6: normal approximation 0.581, exact t-test 0.498
  n = 11: normal approximation 0.834, exact t-test 0.796
RNA-seq        n=3    n=6   n=12   n for 80 %
FC 2   mu 10    0.104  0.337  0.779   13
FC 2   mu 100   0.242  0.645  0.970   8
FC 2   mu 1000  0.269  0.689  0.980   8
FC 1.5 mu 100   0.037  0.124  0.392   23
control allele frequency 0.3: cases for OR 1.1, 1.2, 1.5 = [20384, 5486, 1074]
control allele frequency 0.05: cases for OR 1.1, 1.2, 1.5 = [87966, 23145, 4262]
```

Simulation answers what the formulas cannot. Continuing the code above, NumPy runs 100,000 experiments at once:

```python
import numpy as np

rng = np.random.default_rng(8)
R = 100_000
a = rng.normal(0.0, 0.8, size=(R, 3))
b = rng.normal(1.0, 0.8, size=(R, 3))                      # true difference 1 (a doubling on log2 scale)
p = stats.ttest_ind(b, a, axis=1, equal_var=False).pvalue
print(f"Welch t-test, 3 vs 3: simulated power {np.mean(p <= 0.05):.3f} "
      f"(normal approximation {power_two_groups(1, 0.8, 3):.3f})")

# Significance filter: true effect 0.5 SD, 10 per group, z-test with known SD
delta, n = 0.5, 10
se = math.sqrt(2 / n)
est = rng.normal(delta, se, size=R)                        # estimated differences over R experiments
sig = np.abs(est / se) >= 1.96
print(f"power {sig.mean():.3f}; mean estimate {est.mean():.3f}; "
      f"mean significant estimate {est[sig].mean():.3f}; wrong sign among significant {np.mean(est[sig] < 0):.3f}")
```

```text
Welch t-test, 3 vs 3: simulated power 0.166 (normal approximation 0.334)
power 0.201; mean estimate 0.501; mean significant estimate 1.116; wrong sign among significant 0.005
```

## Worked example

> [!example] Planning an RNA-seq experiment
> A lab wants to detect two-fold changes in genes with about 100 normalized reads per sample. Published data for the same tissue suggest a dispersion around 0.1 (an assumption to state in the plan).
> 1. **Variance of the log fold change** with $n$ replicates per group: $(1/100 + 1/200 + 0.2)/n = 0.215/n$.
> 2. **Threshold.** Thousands of genes are tested, so use a per-gene level of 0.001 ($z = 3.29$) rather than 0.05.
> 3. **Power with 3 replicates:** $|\ln 2| / \sqrt{0.215/3} = 0.693/0.268 = 2.59$, so power $\approx \Phi(2.59 - 3.29) = \Phi(-0.70) = 0.24$: three of four real two-fold changes would be missed.
> 4. **Replicates for 80 %:** 8 per group (code below). Sequencing ten times deeper instead (1,000 reads) leaves the variance at $0.2015/n$ and the requirement at 8: the money is better spent on replicates.
> 5. **Margin.** The calculation treats the dispersion as known and uses a normal approximation; with dispersions estimated from few samples, real power is lower, and empirical benchmarks recommend at least six replicates, twelve to catch small fold changes.[^schurch] A plan of 8 to 10 replicates per group is defensible; 3 is not.

## Common misconceptions

> [!warning] "The study was not significant, but its observed power was low, so the effect may still exist"
> Observed power is a transformation of the p-value: every non-significant result has observed power below about 0.5. The informative statement is the confidence interval, which shows which effect sizes remain compatible with the data.

> [!warning] "More sequencing depth is as good as more replicates"
> Depth reduces only the Poisson part of the variance. With dispersion 0.1, going from 100 to 1,000 reads per gene changes the variance of the log fold change from $0.215/n$ to $0.2015/n$; doubling the replicates halves it.

> [!warning] "80 % power means 80 % of my significant genes are real"
> Power is $P(\text{significant} \mid \text{real effect})$. The fraction of significant results that are real also depends on $\alpha$ and on how many tested effects are real ([[Hypothesis Testing#Advanced (L3)]], [[False Discovery Rate]]).


## Exercises

> [!question] Exercise 1 (L2)
> Two groups, $\sigma = 1$, $\delta = 0.5$, $\alpha = 0.05$: how many samples per group give 80 % power (normal approximation)? Starting from this design, by what factor does the required $n$ change if (a) the effect is halved, (b) the SD is halved, (c) $\alpha$ becomes 0.001, (d) the target power becomes 0.9?

> [!success]- Solution
> $n = 2(1.960 + 0.842)^2/0.5^2 = 62.8$, so 63 per group. Since $n \propto (z_{1-\alpha/2} + z_{1-\beta})^2\sigma^2/\delta^2$: (a) ×4. (b) ÷4: reducing noise (pairing, blocking, better protocols) is as powerful as enlarging effects ([[Paired Design]]). (c) $[(3.29 + 0.84)/(1.96 + 0.84)]^2 = 2.18$. (d) $[(1.96 + 1.28)/(1.96 + 0.84)]^2 = 1.34$.

> [!question] Exercise 2 (L2, bio)
> A gene has about 20 reads per sample and dispersion 0.1. Using `power_rnaseq` and `smallest_n` from the code above, compute the power to detect a two-fold change with 3 replicates per group at $\alpha = 0.001$, and the replicates needed for 80 %.

> [!success]- Solution
> `power_rnaseq(2, 20, 0.1, 3, 0.001)` gives 0.158 and `smallest_n(lambda n: power_rnaseq(2, 20, 0.1, n, 0.001))` gives 10. At 20 reads, the Poisson terms $1/20 + 1/40 = 0.075$ add a third to the biological $2\varphi = 0.2$: weakly expressed genes need more replicates for the same fold change.

> [!question] Exercise 3 (L3, bio)
> A risk allele has frequency 0.2 in controls and odds ratio 1.3. Using `gwas_power` and `smallest_n`, find the cases needed for 80 % power at $5 \times 10^{-8}$ with one control per case, then with four controls per case. Compare total sample sizes.

> [!success]- Solution
> One control per case: 3,342 cases (6,684 subjects). Four controls per case: 2,020 cases and 8,080 controls (10,100 subjects). Extra controls can substitute for scarce cases, at the price of a larger total. With $k$ controls per case the variance of the frequency difference scales roughly like $(1 + 1/k)/N_{\text{cases}}$, so beyond four controls per case at most a further 20 % of variance can be saved.

> [!question] Exercise 4 (L3, Python)
> The true SD is 0.8 and the target effect 1. A lab estimates the SD from a [[Pilot Study|pilot]] of 4 samples (normal data, so $s = 0.8\sqrt{\chi^2_3/3}$), plans $n$ per group with the normal formula, and runs the experiment. Simulate 10,000 such plans (NumPy, seed 9) with the functions above and report the median planned $n$, the median actual power and the fraction of plans with power below 0.5.

> [!success]- Solution
> ```python
> rng = np.random.default_rng(9)
> SIGMA, DELTA = 0.8, 1.0
> s = SIGMA * np.sqrt(rng.chisquare(3, size=10_000) / 3)     # SD estimated from a 4-sample pilot
> planned = [smallest_n(lambda n, sd=sd: power_two_groups(DELTA, sd, n)) for sd in s]
> actual = np.array([power_two_groups(DELTA, SIGMA, n) for n in planned])
> print(f"median planned n {np.median(planned):.0f}; actual power: median {np.median(actual):.2f}, "
>       f"P(actual < 0.5) = {np.mean(actual < 0.5):.2f}")
> ```
> Output: `median planned n 8; actual power: median 0.71, P(actual < 0.5) = 0.25`. A variance from 4 samples has a relative SD of $\sqrt{2/3} = 82\,\%$ ([[Variance#Advanced (L3)]]), and the pilot SD is usually too small (the median of $\chi^2_3/3$ is below 1): the median plan has 8 samples per group instead of the 11 the true $\sigma$ requires, and a quarter of the plans run at less than 50 % power. Plan with a pessimistic value of $\sigma$, such as an upper confidence bound or the variability of comparable published data.

## Mastery checklist

- [ ] 1 Recognized: I can define power, the power function and the four quantities that determine it.
- [ ] 2 Understood: I can explain why depth and replicates affect RNA-seq power differently, why GWAS need thousands of cases, and why observed power is uninformative.
- [ ] 3 Practiced: I can compute power and sample sizes for two-group, count and allelic tests, by formula and by simulation.
- [ ] 4 Applied: I planned the replicates of a real RNA-seq experiment or the size of an association study from published variability, with a documented effect size and threshold.
- [ ] 5 Explained: I can teach how multiple testing, uncertain pilot variances and significance filtering change power and the trustworthiness of results.

## References

[^1805]: [[MIT 18.05 - Introduction to Probability and Statistics]], frequentist statistics part (significance testing: type I and type II errors, power).
[^lazic]: [[Experimental Design for Laboratory Biologists (Lazic)]], material on planning an experiment (replication and sample size).
[^schurch]: [[Schurch 2016 - How Many Biological Replicates Are Needed in an RNA-Seq Experiment]], *RNA* 22(6):839-851: 48 biological replicates per condition; recovery of differentially expressed genes against replicate number; recommendations of at least 6 and at least 12 replicates.
[^love]: [[Love 2014 - Moderated Estimation of Fold Change and Dispersion for RNA-Seq Data with DESeq2]], *Genome Biology* 15:550: negative binomial counts with variance $\mu + \alpha\mu^2$.
[^bh]: [[Benjamini 1995 - Controlling the False Discovery Rate]].
[^risch]: [[Risch 1996 - The Future of Genetic Studies of Complex Human Diseases]], *Science* 273:1516-1517: power of linkage versus association for modest effects; the $5 \times 10^{-8}$ genome-wide threshold.
[^clarke]: [[Clarke 2011 - Basic Statistical Analysis in Genetic Case-Control Studies]], *Nature Protocols* 6(2):121-133: allelic test and odds ratios in case-control studies.
[^ioannidis]: [[Ioannidis 2005 - Why Most Published Research Findings Are False]], *PLoS Medicine* 2(8):e124.
