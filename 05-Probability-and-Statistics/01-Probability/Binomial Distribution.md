---
aliases:
  - Bin(n, p)
  - Binomial Law
  - Binomial Sampling
  - Loi binomiale
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Bernoulli Distribution]]"
  - "[[Binomial Coefficient]]"
  - "[[Independence (Probability)]]"
  - "[[Expected Value]]"
  - "[[Variance]]"
related:
  - "[[Poisson Distribution]]"
  - "[[Normal Distribution]]"
  - "[[Multinomial Distribution]]"
  - "[[Hypergeometric Distribution]]"
  - "[[Beta Distribution]]"
  - "[[Beta-Binomial Model]]"
  - "[[Genotype Likelihood]]"
  - "[[Variant Calling]]"
  - "[[Wright-Fisher Model]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[MIT 18.05 - Introduction to Probability and Statistics]]"
  - "[[Harvard Stat 110 - Probability]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Nielsen 2011 - Genotype and SNP Calling from Next-Generation Sequencing Data]]"
  - "[[Principles of Population Genetics (Hartl)]]"
---

# Binomial Distribution

> [!abstract]
> The binomial distribution counts the successes among $n$ independent trials that each succeed with the same probability $p$: the reads showing the alternative allele among the $n$ reads covering a heterozygous site, or the copies of an allele drawn into the next generation of a finite population.

## Definition

A random variable $X$ has the **binomial distribution** with parameters $n \in \{1, 2, \dots\}$ and $p \in [0, 1]$, written $X \sim \mathrm{Bin}(n, p)$, if it is the number of successes in $n$ independent [[Bernoulli Distribution|Bernoulli]] trials with success probability $p$:

$$P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \qquad k = 0, 1, \dots, n.$$

Its mean is $np$ and its variance $np(1-p)$.[^blitz3][^1805-4a][^stat110] It is the basic generative model for counts of successes, the starting point for tests and intervals on proportions ([[Hypothesis Testing]], [[Confidence Interval]]).[^holmes1]

## Why it matters

- **Allele counts in sequencing.** At a heterozygous site the number of reads showing the alternative allele is close to $\mathrm{Bin}(n, 1/2)$; at a homozygous reference site, alternative reads come only from errors. Comparing these binomial models is how genotype likelihoods are built ([[Genotype Likelihood]], [[Variant Calling]], [[10-genomic-pipeline]]).[^nielsen]
- **Proportions measured by reads.** Methylated reads among the reads covering a CpG ([[Bisulfite Sequencing]]), reads from one allele among a gene's reads, mutant cells among sequenced cells: each proportion carries binomial sampling noise, which sets how much depth a question needs.
- **Genetic drift.** The Wright-Fisher model forms each generation by drawing $2N$ gene copies binomially from the previous one ([[Wright-Fisher Model]], [[Genetic Drift]]).[^hartl] This is the core step of [[07-evolution-simulator]].

## Core (L1)

### Counting successes

Four conditions make a count binomial: a **fixed** number $n$ of trials, **two** outcomes per trial, **independent** trials, and the **same** success probability $p$ for each. Under them, any particular arrangement with $k$ successes, such as SSFF…F, has probability $p^k(1-p)^{n-k}$ (multiply, by independence), and there are $\binom{n}{k}$ arrangements ([[Binomial Coefficient]]). They are disjoint events, so their probabilities add.

![[binomial-pmf-shapes.svg]]

For $p = 1/2$ the PMF is symmetric; for small $p$ it is right-skewed and piled up near 0. The center is $np$ and the spread $\sqrt{np(1-p)}$ grows only like $\sqrt n$, so the **proportion** $X/n$ concentrates as $n$ grows.

### Mean and variance from Bernoulli trials

Write $X = X_1 + \dots + X_n$ with $X_i \sim \mathrm{Bern}(p)$ independent. Linearity gives $E[X] = np$ ([[Expected Value]]); independence lets the variances $p(1-p)$ add, $\operatorname{Var}(X) = np(1-p)$ ([[Variance]]).[^blitz4][^1805-5a] For the proportion, $E[X/n] = p$ and $\mathrm{SD}(X/n) = \sqrt{p(1-p)/n}$.

### Alternative-allele reads at a heterozygous site

Ignoring errors, each of the $n = 20$ reads at a heterozygous site shows the alternative allele with probability $1/2$, so $X \sim \mathrm{Bin}(20, 1/2)$:

| Alternative reads | $k = 10$ | $k = 8$ | $k = 5$ | $k \le 5$ | $k \le 3$ |
|---|---:|---:|---:|---:|---:|
| Probability | 0.176 | 0.120 | 0.015 | 0.021 | 0.0013 |

The mean is 10 and the SD $\sqrt 5 = 2.24$, so the allele fraction has SD 0.11. The "expected" 10 of 20 occurs less than one time in five, and about 2 % of true heterozygotes at depth 20 show an allele fraction of 25 % or less. At depth 4 a heterozygote shows no alternative read with probability $(1/2)^4 = 1/16$: low coverage hides heterozygotes.

## Deeper (L2)

### When $p$ is not 1/2

The binomial model stays, but $p$ changes with the biology and the technology:

- **Sequencing errors**: $p = 1/2 - \varepsilon/3$ at a heterozygous site and $\varepsilon/3$ at a homozygous reference site ([[Bernoulli Distribution#Core (L1)]]).
- **Copy number**: in a region present in three copies, one alternative copy gives $p = 1/3$ and two give $2/3$ ([[Copy Number Variation]]).
- **Tumor purity**: a heterozygous somatic mutation carried by every tumor cell, in a sample with a fraction $\pi$ of tumor cells, gives $p = \pi/2$ in a diploid region, so impure samples give low allele fractions ([[Somatic Variant Calling]]).

### Binomial sampling in the Wright-Fisher model

A population of $N$ diploid individuals carries $2N$ gene copies. In the Wright-Fisher model each generation draws its $2N$ copies independently, with replacement, from the gene pool of the previous one: if $X_t$ copies carry allele A,[^hartl]

$$X_{t+1} \mid X_t \sim \mathrm{Bin}\!\left(2N, \frac{X_t}{2N}\right).$$

With $p_t = X_t/2N$, the binomial mean and variance give the two laws of drift:

- $E[p_{t+1} \mid p_t] = p_t$: **drift has no direction**; the expected frequency never changes, although each population wanders. A directional change needs selection, mutation or migration.[^hartl]
- $\operatorname{Var}(p_{t+1} \mid p_t) = p_t(1 - p_t)/2N$: **drift is stronger in small populations**.
- Consequently the expected heterozygosity $H_t = E[2p_t(1-p_t)]$ decays as $H_t = H_0 (1 - 1/2N)^t$ ([[Heterozygosity]]), until the allele is fixed or lost; a neutral allele is fixed with probability equal to its initial frequency ([[Fixation Probability]], [[Absorbing Markov Chain]]).[^hartl] Exercise 3 checks these laws by simulation.

### Approximations and sums

- **Poisson**: for large $n$ and small $p$, $\mathrm{Bin}(n, p) \approx \mathrm{Pois}(np)$ (derivation in [[Poisson Distribution#Mathematical representation]]): errors among many reads, mutations among many sites.
- **Normal**: for large $np(1-p)$, $(X - np)/\sqrt{np(1-p)}$ is close to a standard normal ([[Normal Distribution]], [[Central Limit Theorem]]).[^blitz] With a continuity correction, $P(X \le 5)$ for $\mathrm{Bin}(20, 1/2)$ is approximated by $\Phi\big((5.5 - 10)/\sqrt 5\big) = 0.022$, against the exact 0.021.
- **Sums**: independent $\mathrm{Bin}(n, p)$ and $\mathrm{Bin}(m, p)$ add to $\mathrm{Bin}(n + m, p)$ (both count successes of independent trials with the same $p$): pooling the reads of two lanes keeps a binomial.

## Advanced (L3)

### Overdispersion: the beta-binomial

If $p$ itself varies between units (individuals at an allele-specific expression site, replicates at a methylated CpG), the count is a mixture. With $X \mid P \sim \mathrm{Bin}(n, P)$ and $P$ following a [[Beta Distribution]] with mean $\mu$ and $\rho = 1/(a + b + 1)$, the law of total variance gives

$$\operatorname{Var}(X) = n\mu(1-\mu)\,\big[1 + (n - 1)\rho\big],$$

larger than the binomial by a factor that **grows with depth** (Exercise 4). Deep sequencing of variable samples is therefore far noisier than binomial sampling suggests: the same lesson as the negative binomial for counts ([[Beta-Binomial Model]], [[Overdispersion]]).

### Bayesian estimation of $p$

A $\mathrm{Beta}(a, b)$ prior for $p$ and $k$ successes in $n$ trials give a $\mathrm{Beta}(a + k, b + n - k)$ posterior: the prior acts as $a$ pseudo-successes and $b$ pseudo-failures.[^blitz] This conjugacy makes allele-fraction or methylation estimates at low depth stable ([[Conjugate Prior]], [[Bayesian Inference]]).

### Two Poisson counts, conditioned on their total

If $X \sim \mathrm{Pois}(\lambda)$ and $Y \sim \mathrm{Pois}(\mu)$ are independent, then given $X + Y = m$,

$$X \mid X + Y = m \;\sim\; \mathrm{Bin}\!\left(m, \frac{\lambda}{\lambda + \mu}\right),$$

because $P(X = k \mid X + Y = m) = \frac{e^{-\lambda}\lambda^k/k! \cdot e^{-\mu}\mu^{m-k}/(m-k)!}{e^{-(\lambda+\mu)}(\lambda + \mu)^m/m!}$, which simplifies to the binomial PMF.[^blitz] Comparing two counts (mutations in two regions, reads in two samples) thus reduces to an exact binomial test on their split (Exercise 5). With covariates, binomial counts are modeled by [[Logistic Regression]], a [[Generalized Linear Model]].

## Mathematical representation

- **Normalization.** $\sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} = (p + 1 - p)^n = 1$ (binomial theorem).
- **Mean, directly.** With $k\binom{n}{k} = n\binom{n-1}{k-1}$: $E[X] = np \sum_{k \ge 1} \binom{n-1}{k-1} p^{k-1}(1-p)^{n-k} = np$.
- **Recurrence and mode.** $\dfrac{P(X = k+1)}{P(X = k)} = \dfrac{n - k}{k + 1} \cdot \dfrac{p}{1 - p}$, which exceeds 1 while $k < (n+1)p - 1$: the mode is $\lfloor (n+1)p \rfloor$.
- **Generating function.** $G_X(s) = (1 - p + ps)^n$, the product of $n$ Bernoulli generating functions; $G_X G_Y = (1 - p + ps)^{n + m}$ proves the sum rule.
- **Wright-Fisher.** $E[p_{t+1}(1 - p_{t+1}) \mid p_t] = p_t - \big(p_t^2 + p_t(1-p_t)/2N\big) = p_t(1 - p_t)(1 - 1/2N)$, hence $H_t = H_0(1 - 1/2N)^t$. Since $E[p_{t+1} \mid p_t] = p_t$, $E[p_t] = p_0$ for all $t$; when $t \to \infty$, $p_t$ is 0 or 1, so $P(\text{fixation}) = p_0$.

## Computational representation

`math.comb(n, k) * p**k * (1 - p)**(n - k)` is fine for small $n$; log space (`math.lgamma`, `math.log1p`) avoids overflow and underflow at sequencing depths in the thousands.

```python
import math
import random


def binomial_pmf(k: int, n: int, p: float) -> float:
    """P(X = k) for X ~ Bin(n, p), computed in log space so that large n does not overflow."""
    if not 0 <= k <= n:
        return 0.0
    if p in (0.0, 1.0):
        return float(k == round(n * p))
    log_pmf = (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
               + k * math.log(p) + (n - k) * math.log1p(-p))
    return math.exp(log_pmf)


def binomial_cdf(k: int, n: int, p: float) -> float:
    """P(X <= k)."""
    return sum(binomial_pmf(j, n, p) for j in range(min(k, n) + 1))


def binomial_sample(n: int, p: float, rng: random.Random) -> int:
    """Number of successes in n Bernoulli(p) trials: O(n), simple and exact."""
    return sum(rng.random() < p for _ in range(n))


n, p = 20, 0.5                                   # 20 reads at a heterozygous site
print("P(X = 10), P(X = 8), P(X = 5):", [round(binomial_pmf(k, n, p), 4) for k in (10, 8, 5)])
print("P(X <= 5) =", round(binomial_cdf(5, n, p), 4), "| P(X <= 3) =", round(binomial_cdf(3, n, p), 4))
rng = random.Random(12)
draws = [binomial_sample(n, p, rng) for _ in range(100_000)]
m = sum(draws) / len(draws)
v = sum((x - m) ** 2 for x in draws) / (len(draws) - 1)
print(f"simulated mean {m:.3f} (np = {n * p:g}), variance {v:.3f} (np(1-p) = {n * p * (1 - p):g})")
print("simulated P(X <= 5):", sum(x <= 5 for x in draws) / len(draws))
```

```text
P(X = 10), P(X = 8), P(X = 5): [0.1762, 0.1201, 0.0148]
P(X <= 5) = 0.0207 | P(X <= 3) = 0.0013
simulated mean 10.001 (np = 10), variance 4.967 (np(1-p) = 5)
simulated P(X <= 5): 0.0201
```

The sampler costs $O(n)$ per draw, fine for a simulator with populations of hundreds of copies. Python 3.12 adds `random.binomialvariate(n, p)`, and NumPy (`Generator.binomial`) and SciPy (`scipy.stats.binom`) provide fast samplers, PMFs and tail probabilities.

## Worked example

> [!example] Calling a genotype from 12 reads
> A site is covered by $n = 12$ reads, $k = 3$ of which show the alternative base; the error probability is $\varepsilon = 0.01$ per read. Continuing the code above:
>
> ```python
> def p_alt_read(alt_copies: int, error: float) -> float:      # read model of Bernoulli Distribution
>     from_alt = alt_copies / 2
>     return from_alt * (1 - error) + (1 - from_alt) * error / 3
>
>
> n, k, error = 12, 3, 0.01
> prior = {0: 0.998, 1: 0.001, 2: 0.001}                       # illustrative prior, not estimated
> like = {g: binomial_pmf(k, n, p_alt_read(g, error)) for g in prior}
> evidence = sum(prior[g] * like[g] for g in prior)
> for g in prior:
>     print(g, f"likelihood {like[g]:.3g}", f"posterior {prior[g] * like[g] / evidence:.3f}")
> ```
>
> ```text
> 0 likelihood 7.91e-06 posterior 0.124
> 1 likelihood 0.0559 posterior 0.876
> 2 likelihood 2.13e-16 posterior 0.000
> ```
>
> 1. **Likelihoods.** $P(k = 3 \mid G) = \mathrm{Bin}(3; 12, p_G)$ with $p_G = \varepsilon/3$, $1/2 - \varepsilon/3$, $1 - \varepsilon$ for 0, 1, 2 alternative copies. The binomial coefficient is the same for every genotype, so it cancels in comparisons.
> 2. **Comparison.** Heterozygous beats homozygous reference by a factor $0.0559/7.91 \times 10^{-6} \approx 7000$: three errors to the same base among 12 reads are very unlikely. Homozygous alternative is excluded, since it would need nine errors.
> 3. **Prior.** With an illustrative prior of 0.001 on each non-reference genotype ([[Bayes' Theorem]]), the posterior probability of a heterozygote is 0.876, not 0.9999: a strong likelihood ratio can still leave real doubt when the prior is small.
> 4. **Limits.** Real callers use each read's own base quality, model mapping errors and estimate the prior from the population ([[Genotype Likelihood]], [[Variant Calling]]).[^nielsen]

## Common misconceptions

> [!warning] "A heterozygous site shows half of its reads with the alternative allele"
> The fraction fluctuates around one half: at depth 20, exactly 10 alternative reads has probability 0.176, and 2 % of heterozygotes show 5 or fewer. Allele-balance filters must allow for binomial noise, all the more at low depth.

> [!warning] "Any count out of $n$ is binomial"
> Only with independent trials and a common $p$. PCR duplicates break independence ([[Duplicate Read]]); copy number, tumor purity and variation between samples change or spread $p$ (beta-binomial). Sampling without replacement from a small pool is hypergeometric ([[Hypergeometric Distribution]]).

> [!warning] "With large $n$ the normal approximation is always fine"
> What must be large is $np(1-p)$, not $n$. For $\mathrm{Bin}(1000, 0.001)$, $P(X = 0) = 0.368$, while the normal with the same mean and variance puts 16 % of its mass below 0. Rare-variant counts need the exact binomial or the Poisson.

## Exercises

> [!question] Exercise 1 (L1)
> At a heterozygous site (ignore errors), what is the probability that $n$ reads contain no alternative read? What minimum depth gives at least one alternative read with probability 0.99? At depth 10, what is the probability of at least two alternative reads?

> [!success]- Solution
> $P(X = 0) = (1/2)^n$. We need $(1/2)^n \le 0.01$, i.e. $n \ge \log_2 100 = 6.64$, so $n = 7$. At depth 10, $P(X \ge 2) = 1 - (1 + 10)/2^{10} = 1 - 11/1024 = 0.989$.

> [!question] Exercise 2 (L2)
> At a heterozygous SNP in an RNA-seq sample, 35 of 50 reads come from one allele. Test equal expression of the two alleles with an exact two-sided binomial test.

> [!success]- Solution
> Under the null, $X \sim \mathrm{Bin}(50, 1/2)$. $P(X \ge 35) = 0.0033$, and by symmetry $P(X \le 15) = 0.0033$, so the two-sided p-value is 0.0066 ([[P-Value]]). The imbalance is unlikely under binomial sampling alone. Before concluding allele-specific expression, check for mapping bias and duplicates, and remember that biological variation between samples makes counts beta-binomial rather than binomial.

> [!question] Exercise 3 (L2, Python)
> Continuing the code above, simulate 1,000 Wright-Fisher populations of 50 diploids ($2N = 100$) starting at $p_0 = 0.2$. At $t = 10, 50, 100$ generations, compare the mean frequency and the mean heterozygosity $2p(1-p)$ with theory, and report the fractions of populations that have fixed or lost the allele.

> [!success]- Solution
> ```python
> rng = random.Random(7)
> two_n, p0, reps = 100, 0.2, 1_000          # 50 diploids = 100 gene copies; 1,000 replicate populations
> freqs = [p0] * reps
> print("t  mean_p  mean_H  theory_H  fixed  lost")
> for t in range(1, 101):
>     freqs = [binomial_sample(two_n, f, rng) / two_n for f in freqs]      # one Wright-Fisher generation
>     if t in (10, 50, 100):
>         mean = sum(freqs) / reps
>         het = sum(2 * f * (1 - f) for f in freqs) / reps                # H = 2p(1 - p)
>         theory = 2 * p0 * (1 - p0) * (1 - 1 / two_n) ** t
>         print(t, round(mean, 3), round(het, 3), round(theory, 3),
>               sum(f == 1 for f in freqs) / reps, sum(f == 0 for f in freqs) / reps)
> # t  mean_p  mean_H  theory_H  fixed  lost
> # 10 0.199 0.288 0.289 0.0 0.026
> # 50 0.202 0.2 0.194 0.004 0.392
> # 100 0.201 0.127 0.117 0.043 0.588
> ```
>
> The mean frequency stays at 0.2 (no direction) while heterozygosity decays as $(1 - 1/2N)^t$ within the noise of 1,000 replicates. After 100 generations 59 % of the populations have lost the allele and 4 % have fixed it; as $t$ grows, the fixed fraction tends to $p_0 = 0.2$ ([[Fixation Probability]]).

> [!question] Exercise 4 (L3, Python)
> Derive $\operatorname{Var}(X) = n\mu(1-\mu)[1 + (n-1)\rho]$ for the beta-binomial, using $\operatorname{Var}(P) = \mu(1-\mu)\rho$. Then, continuing the code above, check it for $n = 50$, $\mu = 0.5$, $\rho = 0.05$.

> [!success]- Solution
> Law of total variance: $E[\operatorname{Var}(X \mid P)] = n E[P(1-P)] = n\big(\mu - \operatorname{Var}(P) - \mu^2\big)$ and $\operatorname{Var}(E[X \mid P]) = n^2 \operatorname{Var}(P)$. Summing, $n\mu(1-\mu) + n(n-1)\operatorname{Var}(P) = n\mu(1-\mu)[1 + (n-1)\rho]$.
>
> ```python
> rng = random.Random(21)
> n, mu, rho = 50, 0.5, 0.05
> a = b = mu * (1 / rho - 1)                 # Beta(a, b): mean mu, rho = 1 / (a + b + 1)
> counts = [binomial_sample(n, rng.betavariate(a, b), rng) for _ in range(20_000)]
> m = sum(counts) / len(counts)
> v = sum((x - m) ** 2 for x in counts) / (len(counts) - 1)
> print(round(m, 2), round(v, 2), "| binomial:", n * mu * (1 - mu), "| beta-binomial:", n * mu * (1 - mu) * (1 + (n - 1) * rho))
> # 24.94 43.36 | binomial: 12.5 | beta-binomial: 43.125
> ```
>
> A modest $\rho = 0.05$ multiplies the variance by 3.45 at depth 50, and the factor keeps growing with $n$: a binomial test on such data would report far too many significant imbalances.

> [!question] Exercise 5 (L3)
> Two genomic regions of equal size and equal expected mutation rate carry 14 and 4 mutations. Using the Poisson-to-binomial conditioning, test whether the rates differ.

> [!success]- Solution
> Under equal rates, the split of the $m = 18$ mutations is $\mathrm{Bin}(18, 1/2)$. $P(X \ge 14) = \big[\binom{18}{14} + \binom{18}{15} + \binom{18}{16} + \binom{18}{17} + \binom{18}{18}\big]/2^{18} = 4048/262{,}144 = 0.0154$, two-sided 0.031. The unknown common rate has disappeared by conditioning on the total, which is what makes the test exact. If the regions differ in size or in callable length, use $p = \lambda/(\lambda + \mu)$ with rates proportional to those sizes.

## Mastery checklist

- [ ] 1 Recognized: I can write the binomial PMF, its mean $np$ and variance $np(1-p)$, and list the four conditions of a binomial count.
- [ ] 2 Understood: I can derive the PMF by counting arrangements, explain the allele-fraction noise at a heterozygous site and the two laws of drift in the Wright-Fisher model.
- [ ] 3 Practiced: I can compute PMFs and tails in log space, run an exact binomial test, and simulate binomial sampling and drift in Python.
- [ ] 4 Applied: I compute genotype likelihoods from real read counts in [[10-genomic-pipeline]] and implement binomial resampling of alleles in [[07-evolution-simulator]], checking fixation probabilities and heterozygosity decay against theory.
- [ ] 5 Explained: I can teach when the binomial fails (dependence, varying $p$, small $np$), the beta-binomial correction, and the conditioning argument behind exact tests on two counts.

## References

[^blitz3]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 3 "Random Variables and Their Distributions" (Bernoulli and binomial distributions).
[^blitz4]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 4 "Expectation" (mean and variance of the binomial through indicator random variables).
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the central limit theorem (normal approximation to the binomial), of beta-binomial conjugacy, and of the connection between the Poisson and the binomial (conditioning on a total).
[^1805-4a]: [[MIT 18.05 - Introduction to Probability and Statistics]], Spring 2022, Reading 4a "Discrete Random Variables".
[^1805-5a]: [[MIT 18.05 - Introduction to Probability and Statistics]], Spring 2022, Reading 5a "Variance of Discrete Random Variables".
[^stat110]: [[Harvard Stat 110 - Probability]], random variables and the named distributions.
[^holmes1]: [[Modern Statistics for Modern Biology (Holmes)]], ch. 1 "Generative Models for Discrete Data".
[^nielsen]: [[Nielsen 2011 - Genotype and SNP Calling from Next-Generation Sequencing Data]], Nielsen R et al., *Nature Reviews Genetics* 12(6):443-451: genotype likelihoods from read data, probabilistic genotype and SNP calling.
[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed. (2006), material on random genetic drift (binomial sampling of gene copies, decay of heterozygosity, fixation of neutral alleles).
