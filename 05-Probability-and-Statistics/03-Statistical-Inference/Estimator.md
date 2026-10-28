---
aliases:
  - Point Estimator
  - Point Estimate
  - Bias (Statistics)
  - Unbiased Estimator
  - Mean Squared Error
  - MSE
  - Consistent Estimator
  - Estimateur
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Statistical Model]]"
  - "[[Sampling Distribution]]"
  - "[[Expected Value]]"
  - "[[Variance]]"
  - "[[Law of Large Numbers]]"
related:
  - "[[Method of Moments]]"
  - "[[Maximum Likelihood Estimation]]"
  - "[[Measure of Dispersion]]"
  - "[[Bias-Variance Tradeoff]]"
  - "[[Fisher Information]]"
  - "[[Empirical Bayes]]"
  - "[[Heterozygosity]]"
  - "[[Nucleotide Diversity]]"
  - "[[Watterson Estimator]]"
  - "[[Confidence Interval]]"
projects:
  - "[[07-evolution-simulator]]"
sources:
  - "[[MIT 18.650 - Statistics for Applications]]"
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Nei 1978 - Estimation of Average Heterozygosity and Genetic Distance from a Small Number of Individuals]]"
  - "[[Watterson 1975 - On the Number of Segregating Sites in Genetical Models Without Recombination]]"
  - "[[Principles of Population Genetics (Hartl)]]"
---

# Estimator

> [!abstract]
> An estimator is a recipe that turns data into a guess of a parameter. Because the data are random, so is the guess, and its quality is judged by where it lands on average (bias), how much it scatters (variance), both together (mean squared error), and whether it homes in on the truth as data accumulate (consistency).

## Definition

In a [[Statistical Model]] with parameter $\theta$, an **estimator** is a statistic $\hat\theta = t(X_1, \dots, X_n)$ used to guess $\theta$; its value on the observed data is an **estimate**. Its quality is measured by its **bias** $E_\theta[\hat\theta] - \theta$, its **variance**, its **mean squared error** $\mathrm{MSE} = E_\theta[(\hat\theta - \theta)^2]$, which equals bias² + variance, and its behavior as $n$ grows: it is **consistent** if $\hat\theta_n$ converges in probability to $\theta$.[^18650]

## Why it matters

- **Every number in a results table is an estimate**: an allele frequency, a log fold change, a dispersion, a mutation rate, a diversity $\theta$. Each has a bias and a standard error, the standard deviation of its [[Sampling Distribution]].
- **Small samples make bias visible.** With 3 replicates, dividing a sum of squares by $n$ or by $n - 1$ changes the variance by 50 % ([[Measure of Dispersion]]).
- **Diversity statistics are estimators with known biases.** Heterozygosity computed from a few individuals underestimates the population value,[^nei] and the number of segregating sites must be rescaled to estimate $\theta$ ([[Nucleotide Diversity]], [[Watterson Estimator]]).[^watterson]
- **The best estimator is a trade-off.** Accepting a little bias can remove a lot of variance; this is how shrinkage methods stabilize thousands of noisy per-gene estimates ([[Empirical Bayes]], [[Bias-Variance Tradeoff]]).

## Core (L2)

### Estimator, estimate, standard error

The estimator is the rule ($\bar X$, "the sample mean"); the estimate is a number ($\bar x = 1.03$). Applied to a new sample, the rule gives a new number: the spread of these numbers over repeated samples is the **standard error** of the estimator, the quantity behind every [[Confidence Interval]].

### Bias: why the sample variance divides by $n - 1$

The plug-in variance $\hat\sigma^2_n = \frac{1}{n}\sum (X_i - \bar X)^2$ has $E[\hat\sigma^2_n] = \frac{n-1}{n}\sigma^2$: deviations are measured from $\bar X$, which is fitted to the same data and sits closer to them than the true mean $\mu$ does (proof in [[Variance#Advanced (L3)]]).[^blitz] Dividing by $n - 1$ instead gives $S^2$, unbiased.

A second view explains the $n - 1$ directly. For two **different** observations, $E[(X_i - X_j)^2/2] = \sigma^2$, and

$$S^2 = \frac{1}{n(n-1)} \sum_{i < j} (X_i - X_j)^2,$$

the average of $(X_i - X_j)^2/2$ over the $n(n-1)/2$ distinct pairs. The plug-in version averages over all $n^2$ ordered pairs, including the $n$ pairs of an observation with itself, which contribute 0: that dilution is exactly the factor $(n-1)/n$. The same structure reappears below for genetic diversity.

### Variance and mean squared error

Bias is not the only error. Dividing the sum of squares by $c$ gives a family of estimators; for normal data their sampling distributions are scaled [[Chi-Square Distribution|chi-square]] curves:

![[variance-estimators-bias-mse.svg]]

| Divisor $c$ ($n = 5$, $\sigma^2 = 1$) | Mean | Bias | Variance | MSE |
|---|---|---|---|---|
| $n - 1 = 4$ (unbiased $S^2$) | 1.000 | 0 | 0.500 | 0.500 |
| $n = 5$ (plug-in) | 0.800 | −0.200 | 0.320 | 0.360 |
| $n + 1 = 6$ | 0.667 | −0.333 | 0.222 | 0.333 |

Shrinking the estimate lowers its variance faster than it raises its squared bias: for normal data the divisor $n + 1$ minimizes the MSE (Mathematical representation). Unbiasedness is one criterion, not a guarantee of being closest to the truth. $S^2$ remains the convention because tests and intervals ([[Student's t-Distribution]]) are built on it.

### Consistency

An estimator is consistent if, for every tolerance $\varepsilon > 0$, $P(|\hat\theta_n - \theta| > \varepsilon) \to 0$ as $n \to \infty$.[^18650] A sufficient condition is that both bias and variance tend to 0 ($\mathrm{MSE} \to 0$). The sample mean is consistent by the [[Law of Large Numbers]]; $\hat\sigma^2_n$ is biased but consistent, since its bias $-\sigma^2/n$ vanishes. Unbiased does not imply consistent: $X_1$ alone is an unbiased estimator of $\mu$ whose variance never shrinks.

### Bio: estimating genetic diversity

The **gene diversity** (expected [[Heterozygosity|heterozygosity]]) at a locus with allele frequencies $p_k$ is $H = 1 - \sum_k p_k^2$: the probability that two independently drawn gene copies carry different alleles.[^nei] Its plug-in estimate from $n$ sampled chromosomes, $1 - \sum_k \hat p_k^2$, is biased downward by the factor $(n-1)/n$, and the unbiased estimator multiplies it by $n/(n-1)$ (for $n$ diploid individuals, $2n/(2n-1)$).[^nei]

The pair view explains it again: $\frac{n}{n-1}(1 - \sum_k \hat p_k^2)$ is exactly the fraction of **distinct** pairs of sampled chromosomes that carry different alleles, while the plug-in also compares each chromosome with itself. Averaging over distinct pairs is also how [[Nucleotide Diversity]] is defined. In simulation (code below, true $H = 0.700$): with 4 chromosomes the plug-in averages 0.524, the corrected estimator 0.699; with 50 chromosomes, 0.686 and 0.700.

## Advanced (L3)

### Unbiasedness does not survive transformations

If $\hat\theta$ is unbiased for $\theta$, $g(\hat\theta)$ is generally biased for $g(\theta)$ unless $g$ is linear. $S^2$ is unbiased for $\sigma^2$, but $S$ underestimates $\sigma$ because the square root is concave: for 3 normal observations, $E[S] = 0.886\,\sigma$ (from the chi distribution with 2 degrees of freedom). Likewise the log of an unbiased mean count is a biased estimate of the log mean, which matters for [[Log Fold Change|log fold changes]] at low counts.

### Efficiency

Between two unbiased estimators, the one with smaller variance is more **efficient**. For normal data with $n = 12$, the median has standard error 0.275 against 0.230 for the mean (simulation in [[Sampling Distribution#Deeper (L2)]]): its relative efficiency is $(0.230/0.275)^2 = 0.70$, so it wastes about 30 % of the data; for heavy-tailed data the order reverses. The lowest variance an unbiased estimator can reach is set by the curvature of the log-likelihood (the Cramér-Rao bound, [[Fisher Information]]), and [[Maximum Likelihood Estimation|maximum likelihood estimators]] approach it in large samples.

### Watterson's estimator: unbiased, slowly consistent

Under the neutral infinite-sites model without recombination, the number $S$ of segregating sites among $n$ sequences of a locus has mean $a_n\theta$ and variance $a_n\theta + b_n\theta^2$, with $a_n = \sum_{i=1}^{n-1} 1/i$ and $b_n = \sum_{i=1}^{n-1} 1/i^2$.[^watterson] Hence $\hat\theta_W = S/a_n$ is unbiased ([[Watterson Estimator]]), with variance $\theta/a_n + b_n\theta^2/a_n^2$. For $\theta = 10$:

| Sequences $n$ | 10 | 100 | 1,000 | 10,000 |
|---|---|---|---|---|
| $a_n$ | 2.83 | 5.18 | 7.48 | 9.79 |
| SD($\hat\theta_W$) | 4.77 (48 %) | 2.83 (28 %) | 2.07 (21 %) | 1.65 (17 %) |

The variance tends to 0, so the estimator is consistent, but only like $1/\log n$: a thousandfold more sequences barely divides the error by three. The $\theta^2$ term does not shrink with $n$ because all sequences of one locus share a single random genealogy ([[Coalescent Theory]]); independent loci average genealogies out (Exercise 5). Nucleotide diversity estimates the same $\theta$ with different weights on the genealogy, and [[Tajima's D]] compares the two estimators.[^hartl]

### Shrinkage: buying precision with bias

When thousands of genes are each estimated from few replicates, pulling every estimate toward a common value adds bias to each but removes much of the noise. In Exercise 6, shrinking 2,000 noisy log fold changes cuts the average MSE from 1.007 to 0.192, while genes with large true effects are pulled hardest toward 0. Choosing how much to shrink from the data themselves is the idea of [[Empirical Bayes]]; the same trade-off governs model complexity in [[Bias-Variance Tradeoff|prediction]].

## Mathematical representation

- **Error decomposition.** Writing $\hat\theta - \theta = (\hat\theta - E\hat\theta) + (E\hat\theta - \theta)$ and squaring, the cross term has expectation 0:
$$\mathrm{MSE}(\hat\theta) = E[(\hat\theta - \theta)^2] = \mathrm{Var}(\hat\theta) + \mathrm{bias}(\hat\theta)^2.$$
- **Consistency from MSE.** By Markov's inequality, $P(|\hat\theta_n - \theta| > \varepsilon) \le \mathrm{MSE}(\hat\theta_n)/\varepsilon^2$, so $\mathrm{MSE} \to 0$ implies consistency.
- **Variance estimators.** $SS = \sum (X_i - \bar X)^2$ has $E[SS] = (n-1)\sigma^2$. For normal data $SS/\sigma^2 \sim \chi^2_{n-1}$, so $\mathrm{Var}(SS/c) = 2(n-1)\sigma^4/c^2$ and
$$\frac{\mathrm{MSE}(SS/c)}{\sigma^4} = \frac{2(n-1)}{c^2} + \left(\frac{n-1}{c} - 1\right)^2 = \frac{(n-1)(n+1)}{c^2} - \frac{2(n-1)}{c} + 1,$$
a quadratic in $u = 1/c$ minimized at $u = 1/(n+1)$.
- **Pairwise form.** $\sum_{i<j} (X_i - X_j)^2 = n\,SS$, so $S^2 = \frac{1}{n(n-1)}\sum_{i<j}(X_i - X_j)^2$; each term has $E[(X_i - X_j)^2] = 2\sigma^2$.
- **Gene diversity.** With counts $N_k$ among $n$ chromosomes, $N_k \sim \mathrm{Bin}(n, p_k)$ marginally, so $E[\hat p_k^2] = p_k^2 + p_k(1-p_k)/n$ and, since $\sum_k p_k(1 - p_k) = H$,
$$E\Big[1 - \sum_k \hat p_k^2\Big] = H - \frac{H}{n} = \frac{n-1}{n}H.$$
The number of ordered pairs of distinct chromosomes carrying different alleles is $\sum_k N_k(n - N_k) = n^2 - \sum_k N_k^2$; dividing by $n(n-1)$ gives $\frac{n}{n-1}(1 - \sum_k \hat p_k^2)$.
- **Watterson.** $E[S] = a_n\theta$, $\mathrm{Var}(S) = a_n\theta + b_n\theta^2$,[^watterson] hence $\mathrm{Var}(\hat\theta_W) = \theta/a_n + b_n\theta^2/a_n^2$, with $a_n \approx \ln n + 0.577$ and $b_n \to \pi^2/6$.

## Computational representation

Bias, variance and MSE are expectations over repeated samples, so simulation measures them directly.

```python
import math
import random
import statistics as st

rng = random.Random(5)

# 1. Three estimators of a variance: sum of squared deviations / c, n = 5 normal observations, sigma^2 = 1
n, REPS = 5, 100_000
estimates = {c: [] for c in (n - 1, n, n + 1)}
for _ in range(REPS):
    xs = [rng.gauss(0.0, 1.0) for _ in range(n)]
    xbar = st.fmean(xs)
    ss = sum((x - xbar) ** 2 for x in xs)
    for c in estimates:
        estimates[c].append(ss / c)
print("divisor   mean    bias  variance   MSE  (theory MSE)")
for c, vals in estimates.items():
    mean, var = st.fmean(vals), st.pvariance(vals)
    mse = st.fmean((e - 1.0) ** 2 for e in vals)
    theory = 2 * (n - 1) / c ** 2 + ((n - 1) / c - 1) ** 2
    print(f"{c:7d}  {mean:.3f}  {mean - 1:+.3f}  {var:8.3f}  {mse:.3f}  ({theory:.3f})")

# 2. Gene diversity (expected heterozygosity) from a sample of chromosomes; invented allele frequencies
freqs = {"A1": 0.4, "A2": 0.3, "A3": 0.2, "A4": 0.1}
H = 1 - sum(p * p for p in freqs.values())


def gene_diversity(sample: list[str]) -> tuple[float, float]:
    """Plug-in 1 - sum(p_hat^2) and its unbiased version n/(n-1) times it."""
    n = len(sample)
    plug_in = 1 - sum((sample.count(a) / n) ** 2 for a in set(sample))
    return plug_in, plug_in * n / (n - 1)


alleles, weights = list(freqs), list(freqs.values())
print(f"true H = {H:.3f}")
for n in (4, 10, 50):
    res = [gene_diversity(rng.choices(alleles, weights, k=n)) for _ in range(20_000)]
    print(f"n = {n:2d} chromosomes: mean plug-in {st.fmean(r[0] for r in res):.3f} "
          f"(theory {H * (n - 1) / n:.3f}), mean unbiased {st.fmean(r[1] for r in res):.3f}")

# 3. Watterson's estimator of theta: standard deviation from its variance formula (theta = 10 per locus)
theta = 10
for n in (10, 100, 1000, 10_000):
    a = sum(1 / i for i in range(1, n))
    b = sum(1 / i ** 2 for i in range(1, n))
    sd = math.sqrt(theta / a + b * theta ** 2 / a ** 2)
    print(f"n = {n:5d} sequences: a_n = {a:5.2f}, SD(theta_W) = {sd:.2f} (CV {sd / theta:.0%})")
```

```text
divisor   mean    bias  variance   MSE  (theory MSE)
      4  1.000  -0.000     0.500  0.500  (0.500)
      5  0.800  -0.200     0.320  0.360  (0.360)
      6  0.667  -0.333     0.222  0.333  (0.333)
true H = 0.700
n =  4 chromosomes: mean plug-in 0.524 (theory 0.525), mean unbiased 0.699
n = 10 chromosomes: mean plug-in 0.630 (theory 0.630), mean unbiased 0.700
n = 50 chromosomes: mean plug-in 0.686 (theory 0.686), mean unbiased 0.700
n =    10 sequences: a_n =  2.83, SD(theta_W) = 4.77 (CV 48%)
n =   100 sequences: a_n =  5.18, SD(theta_W) = 2.83 (CV 28%)
n =  1000 sequences: a_n =  7.48, SD(theta_W) = 2.07 (CV 21%)
n = 10000 sequences: a_n =  9.79, SD(theta_W) = 1.65 (CV 17%)
```

`statistics.variance` returns the unbiased $S^2$ and `statistics.pvariance` the plug-in; NumPy's `var` defaults to the plug-in (`ddof=0`).

## Worked example

> [!example] Diversity at a microsatellite from five individuals
> Five diploid individuals give 10 chromosomes with alleles A1 ×4, A2 ×3, A3 ×2, A4 ×1 (invented).
> 1. **Plug-in.** $\hat p = (0.4, 0.3, 0.2, 0.1)$, $1 - \sum \hat p_k^2 = 1 - 0.30 = 0.700$.
> 2. **Unbiased.** $\frac{10}{9} \times 0.700 = 0.778$.[^nei]
> 3. **Check by pairs.** Ordered pairs of distinct chromosomes: $10 \times 9 = 90$. Pairs with different alleles: $10^2 - (16 + 9 + 4 + 1) = 70$. Fraction: $70/90 = 0.778$, the unbiased value.
> 4. **Reading.** With 10 chromosomes the plug-in understates diversity by 10 %, enough to make a small-sample population look less diverse than a well-sampled one. One locus also gives a noisy estimate; averaging over many loci is the more effective way to gain precision, so few individuals suffice when many loci are typed and heterozygosity is low.[^nei]

## Common misconceptions

> [!warning] "Unbiased means accurate"
> Unbiased means right on average over hypothetical repetitions. A single unbiased estimate can be far off: Watterson's $\hat\theta_W$ from 10 sequences of one locus has a 48 % coefficient of variation.

> [!warning] "The unbiased estimator is always the best one"
> MSE combines bias and variance. For normal data, dividing by $n + 1$ beats dividing by $n - 1$ in MSE, and shrinkage estimators beat raw per-gene estimates on average. Unbiasedness is a convenient property, not an optimality criterion.

> [!warning] "$S^2$ is unbiased, so $S$ is too"
> Expectation does not commute with non-linear functions. $E[S] < \sigma$, by 11 % with 3 normal observations.

> [!warning] "More data fixes any bias"
> More data removes biases that vanish with $n$ (like $-\sigma^2/n$). A systematic bias, such as reads favoring the reference allele or a mis-specified model, converges to the wrong value: the estimator is precise but not consistent ([[Measurement Error]]).

## Exercises

> [!question] Exercise 1 (L2)
> For $n = 3$ normal observations, compute bias, variance and MSE (in units of $\sigma^4$) of $SS/c$ for $c = 2, 3, 4$. Which divisor minimizes the MSE?

> [!success]- Solution
> Bias $= ((n-1)/c - 1)\sigma^2$, variance $= 2(n-1)\sigma^4/c^2$. $c = 2$: bias 0, variance 1, MSE 1. $c = 3$: bias −0.333, variance 0.444, MSE 0.556. $c = 4$: bias −0.5, variance 0.25, MSE 0.5. The minimum is at $c = n + 1 = 4$, as the general formula predicts.

> [!question] Exercise 2 (L2)
> Show that $X_1$ is an unbiased but inconsistent estimator of $\mu$, and that $\bar X_n + 1/n$ is biased but consistent.

> [!success]- Solution
> $E[X_1] = \mu$, but $P(|X_1 - \mu| > \varepsilon)$ does not depend on $n$, so it does not tend to 0 (unless $X$ is constant). $E[\bar X_n + 1/n] = \mu + 1/n$: biased. Its MSE is $\sigma^2/n + 1/n^2 \to 0$, so it is consistent.

> [!question] Exercise 3 (L2)
> At a SNP, 6 sampled chromosomes carry A, A, A, G, G, G. Compute the plug-in and unbiased gene diversities, and check the second by counting pairs.

> [!success]- Solution
> Plug-in: $1 - (0.5^2 + 0.5^2) = 0.5$. Unbiased: $\frac{6}{5} \times 0.5 = 0.6$. Pairs: of the $\binom{6}{2} = 15$ unordered pairs of distinct chromosomes, $3 \times 3 = 9$ pair an A with a G: $9/15 = 0.6$.

> [!question] Exercise 4 (L3)
> Derive $E[1 - \sum_k \hat p_k^2] = \frac{n-1}{n}H$ using indicators: write $\sum_k \hat p_k^2$ as the fraction of the $n^2$ ordered pairs $(a, b)$ of sampled chromosomes, including $a = b$, that carry the same allele.

> [!success]- Solution
> $\sum_k \hat p_k^2 = \frac{1}{n^2}\sum_{a,b} \mathbf{1}[A_a = A_b]$. The $n$ pairs with $a = b$ always match; each of the $n(n-1)$ pairs with $a \ne b$ matches with probability $\sum_k p_k^2 = 1 - H$. So $E[\sum_k \hat p_k^2] = \frac{n + n(n-1)(1-H)}{n^2}$ and $E[1 - \sum_k \hat p_k^2] = \frac{n(n-1)H}{n^2} = \frac{n-1}{n}H$. The self-pairs, which can never differ, cause the bias.

> [!question] Exercise 5 (L3, Python)
> With $\theta = 5$ per locus, compare the standard deviation of Watterson's estimate from (a) one locus sequenced in 100 individuals' chromosomes, and (b) the average over 10 independent loci, each sequenced in 10 chromosomes (the same 100 locus-sequences). Which design would you choose?

> [!success]- Solution
> ```python
> import math
>
> def sd_w(n, theta):
>     a = sum(1 / i for i in range(1, n))
>     b = sum(1 / i ** 2 for i in range(1, n))
>     return math.sqrt(theta / a + b * theta ** 2 / a ** 2)
>
> theta = 5
> print("1 locus, 100 sequences:", round(sd_w(100, theta), 2))
> print("10 loci, 10 sequences each (mean of 10 independent loci):", round(sd_w(10, theta) / math.sqrt(10), 2))
> ```
> Output: 1.58 against 0.81. Independent loci have independent genealogies, so averaging them divides the whole variance by 10; adding sequences of one locus re-samples a single genealogy. For estimating $\theta$, sequence more loci rather than more individuals at one locus.

> [!question] Exercise 6 (L3, Python)
> Simulate 2,000 genes with true log fold changes $\theta_g \sim \mathcal N(0, 0.5^2)$, each observed with noise $x_g = \theta_g + \varepsilon_g$, $\varepsilon_g \sim \mathcal N(0, 1)$ (seed 3). Estimate the spread of true effects from the data, shrink each $x_g$ by $B = \hat\tau^2/(\hat\tau^2 + 1)$, and compare the average MSE of raw and shrunk estimates, overall and for genes with $\theta_g > 1$.

> [!success]- Solution
> ```python
> import random
> import statistics as st
>
> rng = random.Random(3)
> G, TAU, SIGMA = 2_000, 0.5, 1.0
> true = [rng.gauss(0.0, TAU) for _ in range(G)]                 # true log2 fold changes (invented scale)
> obs = [t + rng.gauss(0.0, SIGMA) for t in true]                # noisy estimates, SE 1 each (few replicates)
> tau2_hat = max(st.pvariance(obs) - SIGMA ** 2, 0.0)            # spread of true effects, from all genes
> B = tau2_hat / (tau2_hat + SIGMA ** 2)                         # shrinkage factor
> shrunk = [B * x for x in obs]
> mse = lambda est: st.fmean((e - t) ** 2 for e, t in zip(est, true))
> print(f"B = {B:.3f}; MSE raw = {mse(obs):.3f}, MSE shrunk = {mse(shrunk):.3f}")
> big = [i for i, t in enumerate(true) if t > 1.0]
> print(f"genes with true effect > 1: {len(big)}, mean true {st.fmean(true[i] for i in big):.2f}, "
>       f"mean raw {st.fmean(obs[i] for i in big):.2f}, mean shrunk {st.fmean(shrunk[i] for i in big):.2f}")
> ```
> Output: `B = 0.232; MSE raw = 1.007, MSE shrunk = 0.192`, then `genes with true effect > 1: 47, mean true 1.17, mean raw 1.20, mean shrunk 0.28`. Shrinkage divides the average error by five, but the 47 genes with large real effects are strongly underestimated: a single normal prior shrinks everything alike. Better priors adapt the shrinkage to each gene's precision or allow heavier tails, so that large effects are pulled less ([[Empirical Bayes]]).

## Mastery checklist

- [ ] 1 Recognized: I can define estimator, estimate, bias, variance, MSE and consistency.
- [ ] 2 Understood: I can explain the $n - 1$ of the sample variance in two ways (fitted mean, distinct pairs) and why an unbiased estimator can lose to a biased one.
- [ ] 3 Practiced: I can measure bias, variance and MSE of any estimator by simulation and derive them for variance and diversity estimators.
- [ ] 4 Applied: I compared estimators of diversity ($H$, $\hat\theta_W$) on populations simulated with a known $\theta$ in [[07-evolution-simulator]], checking their bias and spread against theory.
- [ ] 5 Explained: I can teach efficiency, slow consistency of $\hat\theta_W$, the effect of transformations on bias, and when shrinkage pays.

## References

[^18650]: [[MIT 18.650 - Statistics for Applications]], estimation part (properties of estimators: bias, variance, mean squared error, consistency).
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the sample mean and sample variance and of the law of large numbers.
[^nei]: [[Nei 1978 - Estimation of Average Heterozygosity and Genetic Distance from a Small Number of Individuals]], *Genetics* 89(3):583-590: bias of sample heterozygosity, unbiased estimator, many loci versus many individuals.
[^watterson]: [[Watterson 1975 - On the Number of Segregating Sites in Genetical Models Without Recombination]], *Theoretical Population Biology* 7(2):256-276: mean and variance of the number of segregating sites; unbiased estimator of $\theta$.
[^hartl]: [[Principles of Population Genetics (Hartl)]], molecular population genetics (estimators of $\theta$ from sequence data).
