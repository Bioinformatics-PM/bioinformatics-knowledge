---
aliases:
  - Likelihood
  - Log-Likelihood
  - Log-Likelihood Function
  - Relative Likelihood
  - Likelihood Interval
  - Vraisemblance
tags:
  - type/concept
  - domain/statistics
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Statistical Model]]"
  - "[[Probability Distribution]]"
  - "[[Binomial Distribution]]"
  - "[[Independence (Probability)]]"
  - "[[Logarithm]]"
related:
  - "[[Maximum Likelihood Estimation]]"
  - "[[Allele Frequency]]"
  - "[[Hardy-Weinberg Equilibrium]]"
  - "[[Genotype Likelihood]]"
  - "[[Law of Total Probability]]"
  - "[[Bayes' Theorem]]"
  - "[[Likelihood Ratio Test]]"
  - "[[Fisher Information]]"
  - "[[Felsenstein Pruning Algorithm]]"
  - "[[Floating-Point Arithmetic]]"
projects:
  - "[[08-phylogenetic-engine]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[MIT 18.650 - Statistics for Applications]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Nielsen 2011 - Genotype and SNP Calling from Next-Generation Sequencing Data]]"
  - "[[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]]"
  - "[[Goldberg 1991 - What Every Computer Scientist Should Know About Floating-Point Arithmetic]]"
---

# Likelihood Function

> [!abstract]
> The likelihood turns the probability of the observed data into a function of the unknown parameter: it scores each candidate value by how probable it makes what was actually seen. Its logarithm, a sum over independent observations, is what estimation maximizes and what tests compare.

## Definition

Given a [[Statistical Model]] with density or mass function $f(x; \theta)$ and observed data $x$, the **likelihood function** is $L(\theta) = L(\theta; x) = f(x; \theta)$, viewed as a function of $\theta$ with $x$ held fixed. For independent observations it is a product, $L(\theta) = \prod_{i=1}^n f(x_i; \theta)$, and the **log-likelihood** is the sum $\ell(\theta) = \sum_{i=1}^n \ln f(x_i; \theta)$. Factors that do not depend on $\theta$ can be dropped: only ratios $L(\theta_1)/L(\theta_2)$ carry information.[^18650][^durbin]

## Why it matters

- **It is the common engine of inference.** [[Maximum Likelihood Estimation]] maximizes it, the [[Likelihood Ratio Test]] compares its maxima, [[Bayes' Theorem]] multiplies it by a prior, and [[Model Selection]] criteria penalize it.
- **Variant calling is likelihood bookkeeping.** A caller computes, for each candidate genotype, the probability of the observed reads given that genotype: a [[Genotype Likelihood]] built from base qualities.[^nielsen]
- **Phylogenetics scores trees by likelihood.** The probability of an alignment under a tree and a substitution model, summed over unobserved ancestral states, is the quantity behind maximum likelihood trees ([[Felsenstein Pruning Algorithm]], [[08-phylogenetic-engine]]).[^felsenstein81]
- **It must be computed on the log scale.** Products of thousands of per-read or per-site probabilities underflow to 0 in floating point; sums of logarithms do not ([[Floating-Point Arithmetic]]).

## Core (L2)

### Same formula, two questions

The binomial formula $P(K = k) = \binom{n}{k}p^k(1-p)^{n-k}$ answers two different questions:

| Fixed | Varies | Name | Sums or integrates to 1? |
|---|---|---|---|
| parameter $p$ | data $k = 0, \dots, n$ | probability mass function | yes, over $k$ |
| data $k$ | parameter $p \in [0, 1]$ | likelihood $L(p)$ | no: its area is $1/(n+1)$ |

The likelihood is not a probability distribution over $p$, so "the probability that $p = 0.2$" cannot be read from it (Advanced).

### Bio: the likelihood of an allele frequency

A sample of $n$ chromosomes contains $k$ copies of the alternative allele. If chromosomes are sampled independently, $K \sim \mathrm{Bin}(n, p)$ and, dropping the constant $\binom{n}{k}$,

$$L(p) \propto p^k(1-p)^{n-k}, \qquad \ell(p) = k\ln p + (n-k)\ln(1-p).$$

With 46 alternative alleles among 200 chromosomes (invented; the sample of [[Confidence Interval#Core (L1)]]):

| $p$ | 0.15 | 0.20 | 0.23 | 0.25 | 0.30 |
|---|---|---|---|---|---|
| $\ell(p)$ | −112.30 | −108.40 | −107.86 | −108.07 | −110.31 |
| $L(p)/L(0.23)$ | 0.012 | 0.581 | 1 | 0.805 | 0.086 |

The data are most probable at $p = 0.23 = 46/200$, and 11.7 times more probable at $p = 0.23$ than at $p = 0.30$: that ratio is the evidence the sample carries for one value against the other ([[Allele Frequency]]).[^holmes]

![[allele-frequency-likelihood-curves.svg]]

### Reading the curve

- **Ratios, not heights.** The value $L(0.23) = 1.4 \times 10^{-47}$ (without the binomial constant) means nothing alone; it shrinks with every added observation. The **relative likelihood** $L(p)/L(\hat p)$, between 0 and 1, is what the top panel shows.
- **Width is information.** With 5 alternative alleles among 20 chromosomes the curve is wide; with 46 among 200 it is narrow. Ten times more chromosomes make it about $\sqrt{10} \approx 3$ times narrower, the same $\sqrt n$ law as the [[Sampling Distribution]].
- **Log scale.** The log-likelihood (bottom panel) turns products into sums and is close to a parabola near its maximum; its curvature measures precision ([[Fisher Information]]). The values of $p$ whose log-likelihood lies within 1.92 of the maximum form an approximate 95 % **likelihood interval**: 1.92 is half the 95 % quantile of $\chi^2_1$, by Wilks' theorem ([[Chi-Square Distribution]], [[Likelihood Ratio Test]]).[^18650] For 46/200 it is $[0.175, 0.291]$; for 5/20, $[0.10, 0.46]$, asymmetric as a proportion near 0 should be.

### From genotypes: only allele counts matter

Under [[Hardy-Weinberg Equilibrium]], a sample of $N$ unrelated people with genotype counts $n_{AA}, n_{Aa}, n_{aa}$ has probabilities $p^2, 2p(1-p), (1-p)^2$ per person,[^hartl] so

$$\ell(p) = (2n_{AA} + n_{Aa})\ln p + (2n_{aa} + n_{Aa})\ln(1-p) + n_{Aa}\ln 2.$$

This is the allele-count log-likelihood plus a constant: two samples with the same allele counts carry the same evidence about $p$, whatever their genotype counts. With 6 AA, 34 Aa and 60 aa people (46 A alleles among 200), the two log-likelihoods differ by exactly $34 \ln 2 = 23.567$ at every $p$ (code below). The genotype counts still matter for other questions, such as testing Hardy-Weinberg itself ([[Chi-Square Test]]).

## Advanced (L3)

### Hidden variables: sum over what you cannot see

Often the model involves quantities that are not observed, and the likelihood sums over them ([[Law of Total Probability]]):

- **Allele frequency from reads without calling genotypes.** For individual $i$ with reads $D_i$, $P(D_i \mid p) = \sum_{g=0}^{2} P(D_i \mid g)\,P(g \mid p)$, where $P(D_i \mid g)$ is the genotype likelihood and $P(g \mid p)$ the Hardy-Weinberg probability. The likelihood of $p$ is the product over individuals. At low depth this is more faithful than counting alleles in hard genotype calls, which treat uncertain calls as certain.[^nielsen] In Exercise 5, ten people sequenced at about 3× give $\hat p = 0.235$ from the reads but 0.25 from hard calls: one person with two alternative reads was called homozygous, although under the population model a heterozygote is more probable (0.62).
- **Tree likelihood.** The probability of a column of an alignment is a sum over all states of the internal nodes of the tree; Felsenstein's pruning algorithm computes it efficiently by dynamic programming from the leaves to the root.[^felsenstein81]
- **Mixture models.** The likelihood of data from several populations sums over the unknown population of each observation; maximizing it is the job of the [[Expectation-Maximization Algorithm]] ([[Mixture Model]]).

### The likelihood is not a density for the parameter

- **Area.** $\int_0^1 \binom{n}{k}p^k(1-p)^{n-k}\,dp = \frac{1}{n+1}$, not 1 (computed for 46/200 below).
- **Reparameterization.** Rewriting the model with $\eta = \ln\frac{p}{1-p}$ moves the curve but not its maximum or its ratios: $\hat\eta = \ln\frac{\hat p}{1 - \hat p}$. Areas under the curve, however, change with the parameterization, so they have no meaning without a prior. Turning a likelihood into probabilities for $\theta$ requires [[Bayes' Theorem]]: posterior ∝ likelihood × prior ([[Bayesian Inference]]).

### Combining evidence

Independent datasets multiply their likelihoods, so log-likelihoods add: two surveys of the same population give $\ell(p) = \ell_1(p) + \ell_2(p)$. Comparing the best fit with a shared $p$ against separate values for each survey is a [[Likelihood Ratio Test]] (Exercise 4).

## Mathematical representation

- **Definition.** $L(\theta; x) = c(x)\, f(x; \theta)$ for any $c(x) > 0$ not depending on $\theta$; for i.i.d. data $\ell(\theta) = \sum_i \ln f(x_i; \theta) + \text{const}$.
- **Binomial.** $\ell(p) = k\ln p + (n-k)\ln(1-p)$; $\ell'(p) = \frac{k}{p} - \frac{n-k}{1-p}$; $\ell''(p) = -\frac{k}{p^2} - \frac{n-k}{(1-p)^2} < 0$, so $\ell$ is concave with a single maximum ([[Maximum Likelihood Estimation]]).
- **Relative likelihood** $R(\theta) = L(\theta)/L(\hat\theta) \in (0, 1]$; **likelihood interval** $\{\theta : \ell(\theta) \ge \ell(\hat\theta) - \tfrac12\chi^2_{1, 0.95}\} = \{\theta : \ell(\hat\theta) - \ell(\theta) \le 1.92\}$.
- **Hardy-Weinberg genotypes.** $L(p) = (p^2)^{n_{AA}}\,(2p(1-p))^{n_{Aa}}\,((1-p)^2)^{n_{aa}} = 2^{n_{Aa}}\,p^{2n_{AA} + n_{Aa}}(1-p)^{2n_{aa} + n_{Aa}}$.
- **Hidden genotypes.** $L(p) = \prod_{i} \sum_{g=0}^{2} P(D_i \mid g) \binom{2}{g} p^g (1-p)^{2-g}$.
- **Area.** $\int_0^1 \binom{n}{k}p^k(1-p)^{n-k}dp = \binom{n}{k} B(k+1, n-k+1) = \binom{n}{k}\frac{k!\,(n-k)!}{(n+1)!} = \frac{1}{n+1}$.
- **Log-sum-exp.** $\ln\sum_j e^{a_j} = m + \ln\sum_j e^{a_j - m}$ with $m = \max_j a_j$: sums of probabilities computed from their logarithms without underflow.

## Computational representation

```python
import math


def binom_loglik(p: float, k: int, n: int) -> float:
    """Log-likelihood of an allele frequency p given k copies among n chromosomes (constant ln C(n, k) dropped)."""
    return k * math.log(p) + (n - k) * math.log(1 - p)


k, n = 46, 200                                  # invented: 46 alternative alleles among 200 chromosomes
ll_max = binom_loglik(k / n, k, n)
for p in (0.15, 0.20, 0.23, 0.25, 0.30):
    ll = binom_loglik(p, k, n)
    print(f"p = {p:.2f}: log-likelihood {ll:8.2f}, relative likelihood {math.exp(ll - ll_max):.4f}")
print(f"likelihood ratio L(0.23) / L(0.30) = {math.exp(binom_loglik(0.23, k, n) - binom_loglik(0.30, k, n)):.1f}")

grid = [i / 10_000 for i in range(1, 10_000)]
inside = [p for p in grid if binom_loglik(p, k, n) >= ll_max - 1.92]
print(f"log-likelihood within 1.92 of its maximum for p in [{inside[0]:.3f}, {inside[-1]:.3f}]")
area = sum(math.comb(n, k) * p ** k * (1 - p) ** (n - k) for p in grid) / 10_000
print(f"area under L(p) = {area:.6f}; 1/(n + 1) = {1 / (n + 1):.6f}")

# Genotype counts under Hardy-Weinberg: the log-likelihood differs from the allele-count one by a constant
n_AA, n_Aa, n_aa = 6, 34, 60                    # invented genotypes of 100 people: 2*6 + 34 = 46 alleles


def hwe_loglik(p: float) -> float:
    return n_AA * math.log(p * p) + n_Aa * math.log(2 * p * (1 - p)) + n_aa * math.log((1 - p) ** 2)


print("HWE minus allele-count log-likelihood:",
      [round(hwe_loglik(p) - binom_loglik(p, 2 * n_AA + n_Aa, 200), 4) for p in (0.1, 0.23, 0.5)])

# Products of many probabilities underflow; sums of their logarithms do not
probs = [0.01] * 200
product = 1.0
for q in probs:
    product *= q
print("product:", product, "| sum of logs:", round(sum(math.log(q) for q in probs), 2))
```

```text
p = 0.15: log-likelihood  -112.30, relative likelihood 0.0118
p = 0.20: log-likelihood  -108.40, relative likelihood 0.5810
p = 0.23: log-likelihood  -107.86, relative likelihood 1.0000
p = 0.25: log-likelihood  -108.07, relative likelihood 0.8047
p = 0.30: log-likelihood  -110.31, relative likelihood 0.0858
likelihood ratio L(0.23) / L(0.30) = 11.7
log-likelihood within 1.92 of its maximum for p in [0.175, 0.291]
area under L(p) = 0.004975; 1/(n + 1) = 0.004975
HWE minus allele-count log-likelihood: [23.567, 23.567, 23.567]
product: 0.0 | sum of logs: -921.03
```

A grid is enough to plot and explore a one-parameter likelihood; [[Maximum Likelihood Estimation]] finds the maximum exactly or with an optimizer. The product of 200 probabilities of 0.01 is $10^{-400}$, below the smallest positive (denormalized) double, $2^{-1074} \approx 4.9 \times 10^{-324}$, so it is stored as 0.0.[^goldberg]

## Worked example

> [!example] What do 46 alternative alleles among 200 chromosomes say about $p$?
> 1. **Write the log-likelihood.** $\ell(p) = 46\ln p + 154\ln(1-p)$, maximal at $\hat p = 0.23$, where $\ell = -107.86$.
> 2. **Compare two hypotheses.** A published frequency of 0.30 for this population gives $\ell(0.30) = -110.31$: a log-likelihood ratio of 2.45, a likelihood ratio of $e^{2.45} = 11.7$ in favor of 0.23. Against 0.25, the ratio is only $1/0.805 = 1.24$: the data barely distinguish 0.23 from 0.25.
> 3. **Interval.** Values within 1.92 log-units of the maximum: $[0.175, 0.291]$. The Wald interval of [[Confidence Interval]] is $[0.172, 0.288]$ and the score interval $[0.177, 0.293]$: with 200 chromosomes the three agree to within 0.005.
> 4. **Reading.** A frequency of 0.30 lies just outside the likelihood interval, so this sample is mild evidence that the population differs from the published value; the [[Likelihood Ratio Test]] makes this precise ($2 \times 2.45 = 4.9 > 3.84$).
> 5. **Small sample.** With 5 of 20 the interval is $[0.10, 0.46]$, against a Wald interval of $[0.06, 0.44]$: for small counts the likelihood interval respects the asymmetry near 0 that the symmetric Wald recipe ignores.

## Common misconceptions

> [!warning] "$L(p)$ is the probability that $p$ is the true value"
> It is the probability of the data for each $p$. It does not integrate to 1 over $p$ (area $1/(n+1)$ for the binomial) and changes shape under reparameterization. Probabilities of parameter values need a prior ([[Bayesian Inference]]).

> [!warning] "A likelihood of $10^{-47}$ means the model fits badly"
> Likelihood values shrink with every observation and depend on dropped constants. Only ratios between parameter values (or between models) on the same data are meaningful.

> [!warning] "Comparing likelihoods across datasets"
> $L_1(\theta)$ for one dataset and $L_2(\theta)$ for another are not on a common scale. Likelihoods are compared across parameter values for fixed data, never across data.

> [!warning] "Multiply the probabilities, then take the log"
> By then the product has already underflowed to 0. Sum logarithms from the start, and use log-sum-exp when probabilities must be added (sums over genotypes, ancestral states or mixture components).

## Exercises

> [!question] Exercise 1 (L2)
> At a site, 12 of 40 reads carry the alternative allele. Write $\ell(p)$ for the per-read alternative fraction $p$ and compute $L(0.5)/L(0.3)$. What does it suggest about a germline heterozygote ($p = 0.5$)?

> [!success]- Solution
> $\ell(p) = 12\ln p + 28\ln(1-p)$. $\ln\frac{L(0.5)}{L(0.3)} = 12\ln\frac{0.5}{0.3} + 28\ln\frac{0.5}{0.7} = 6.130 - 9.421 = -3.291$, so $L(0.5)/L(0.3) = 0.037$: the reads are 27 times more probable if the fraction is 0.3. That is evidence against a balanced heterozygote: allelic imbalance, a subclonal (somatic) variant or a mapping bias are candidates ([[Genotype Likelihood]]).

> [!question] Exercise 2 (L2)
> Genotype counts are AA 50, Aa 40, aa 10. Write the log-likelihood of the A frequency $p$ under Hardy-Weinberg and find its maximum.

> [!success]- Solution
> $\ell(p) = (100 + 40)\ln p + (20 + 40)\ln(1-p) + 40\ln 2 = 140\ln p + 60\ln(1-p) + \text{const}$. $\ell'(p) = 140/p - 60/(1-p) = 0$ gives $\hat p = 140/200 = 0.7$: gene counting ([[Allele Frequency]]).

> [!question] Exercise 3 (L2)
> Show that $\int_0^1 \binom{n}{k}p^k(1-p)^{n-k}\,dp = 1/(n+1)$ for every $k$, and explain why this proves that a likelihood is not a probability density for $p$.

> [!success]- Solution
> The Beta integral gives $\int_0^1 p^k(1-p)^{n-k}dp = \frac{k!\,(n-k)!}{(n+1)!}$; multiplying by $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ leaves $\frac{n!}{(n+1)!} = \frac{1}{n+1}$. A density must integrate to 1; this area is $1/(n+1)$, and it would change again if the constant $\binom{n}{k}$ were dropped, which leaves all likelihood ratios unchanged.

> [!question] Exercise 4 (L3, Python)
> Two surveys of one population find 46 of 200 and 30 of 100 alternative alleles. Using `binom_loglik`, compare the maximized log-likelihood with separate frequencies and with a shared one. Is a shared frequency compatible with the data at the 5 % level (critical value 3.84)?

> [!success]- Solution
> ```python
> studies = [(46, 200), (30, 100)]
> sep = sum(binom_loglik(kk / nn, kk, nn) for kk, nn in studies)
> pooled_p = sum(kk for kk, _ in studies) / sum(nn for _, nn in studies)
> pooled = sum(binom_loglik(pooled_p, kk, nn) for kk, nn in studies)
> print(f"pooled p_hat = {pooled_p:.4f}; 2 * (separate - pooled) = {2 * (sep - pooled):.2f}")
> ```
> Output: `pooled p_hat = 0.2533; 2 * (separate - pooled) = 1.70`. The separate-frequency model has one more parameter; twice the gain in log-likelihood, 1.70, is below 3.84, so a shared frequency is compatible with both surveys ([[Likelihood Ratio Test]]).

> [!question] Exercise 5 (L3, Python)
> Ten people are sequenced at low depth; their (reference, alternative) read counts at a site are (4, 0), (2, 1), (3, 0), (0, 2), (5, 0), (1, 1), (3, 0), (2, 0), (2, 2), (4, 0) (invented). With error rate 0.01 and per-read alternative probabilities $\varepsilon/3$, $1/2 - \varepsilon/3$, $1 - \varepsilon$ for 0, 1, 2 alternative copies (as in [[Binomial Distribution]]), compute the likelihood of $p$ summed over hidden genotypes, its maximum on a grid, and compare with the frequency from hard genotype calls.

> [!success]- Solution
> ```python
> import math
>
> EPS = 0.01
> reads = [(4, 0), (2, 1), (3, 0), (0, 2), (5, 0), (1, 1), (3, 0), (2, 0), (2, 2), (4, 0)]   # (ref, alt) per person, invented
>
>
> def read_lik(ref: int, alt: int, g: int) -> float:
>     """P(reads | g alternative copies), up to a constant; per-read alt probability as in Binomial Distribution."""
>     q = (EPS / 3, 0.5 - EPS / 3, 1 - EPS)[g]
>     return q ** alt * (1 - q) ** ref
>
>
> def freq_loglik(p: float) -> float:
>     """Sum over individuals of log sum over hidden genotypes of P(reads | g) P(g | p) (Hardy-Weinberg)."""
>     hw = ((1 - p) ** 2, 2 * p * (1 - p), p ** 2)
>     return sum(math.log(sum(read_lik(r, a, g) * hw[g] for g in range(3))) for r, a in reads)
>
>
> grid = [i / 1000 for i in range(1, 1000)]
> p_reads = max(grid, key=freq_loglik)
> calls = [max(range(3), key=lambda g: read_lik(r, a, g)) for r, a in reads]
> print("hard calls:", calls, "-> frequency", sum(calls) / (2 * len(reads)))
> print("maximum likelihood from reads:", p_reads)
> for r, a in ((0, 2), (2, 0)):                  # posterior genotype probabilities at p_reads
>     hw = ((1 - p_reads) ** 2, 2 * p_reads * (1 - p_reads), p_reads ** 2)
>     post = [read_lik(r, a, g) * hw[g] for g in range(3)]
>     print((r, a), [round(x / sum(post), 3) for x in post])
> ```
> Output: `hard calls: [0, 1, 0, 2, 0, 1, 0, 0, 1, 0] -> frequency 0.25`, `maximum likelihood from reads: 0.235`, then `(0, 2) [0.0, 0.621, 0.379]` and `(2, 0) [0.865, 0.135, 0.0]`. Hard calls count the person with reads (0, 2) as two alternative copies, but with only two reads a heterozygote is plausible: at $\hat p = 0.235$ its posterior genotype probabilities are 0.62 (heterozygote) and 0.38 (homozygote). Conversely, the person with reads (2, 0) keeps a 0.135 probability of being a missed heterozygote. The likelihood weighs every person by the evidence, instead of rounding each to a certain genotype.[^nielsen]

> [!question] Exercise 6 (L3, Python)
> Continuing the code of Exercise 5: a deeply sequenced person has 1,520 reference and 1,480 alternative reads. Compute $\ln P(D \mid g)$ for $g = 0, 1, 2$ (same model as Exercise 5), show that exponentiating underflows, and compute $\ln \sum_g P(D \mid g)$ with log-sum-exp.

> [!success]- Solution
> ```python
> def logsumexp(xs):
>     m = max(xs)
>     return m + math.log(sum(math.exp(x - m) for x in xs))
>
>
> ref, alt = 1520, 1480
> logs = [alt * math.log(q) + ref * math.log(1 - q) for q in (EPS / 3, 0.5 - EPS / 3, 1 - EPS)]
> print([round(x, 1) for x in logs], [math.exp(x) for x in logs])
> print("naive sum:", sum(math.exp(x) for x in logs), "| log-sum-exp:", round(logsumexp(logs), 2))
> ```
> Output: `[-8446.7, -2079.2, -7014.7] [0.0, 0.0, 0.0]`, then `naive sum: 0.0 | log-sum-exp: -2079.24`. Every probability is far below the smallest double, yet the log-likelihoods are ordinary numbers, and the heterozygote dominates by thousands of log-units. Factoring out the largest term keeps the sum exact.

## Mastery checklist

- [ ] 1 Recognized: I can define the likelihood and the log-likelihood and say how they differ from a probability distribution.
- [ ] 2 Understood: I can explain why only likelihood ratios matter, why more data narrow the curve, and why Hardy-Weinberg genotype counts and allele counts give the same evidence about $p$.
- [ ] 3 Practiced: I can write, plot and compare log-likelihoods, compute likelihood intervals, and sum over hidden variables with log-sum-exp.
- [ ] 4 Applied: I computed genotype likelihoods and an allele-frequency likelihood from real reads in [[10-genomic-pipeline]], or a site likelihood on a tree in [[08-phylogenetic-engine]].
- [ ] 5 Explained: I can teach the likelihood as the common core of maximum likelihood, likelihood ratio tests and Bayesian inference, including what it cannot say about parameters without a prior.

## References

[^18650]: [[MIT 18.650 - Statistics for Applications]], estimation and testing parts (likelihood, maximum likelihood, likelihood ratio tests).
[^durbin]: [[Biological Sequence Analysis (Durbin)]], ch. 1 "Introduction" (probability and inference basics: likelihood and maximum likelihood).
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], treatment of statistical modeling (likelihood and maximum likelihood estimation of a binomial proportion).
[^hartl]: [[Principles of Population Genetics (Hartl)]], Hardy-Weinberg genotype frequencies.
[^nielsen]: [[Nielsen 2011 - Genotype and SNP Calling from Next-Generation Sequencing Data]], Nielsen R et al., *Nature Reviews Genetics* 12(6):443-451: genotype likelihoods from read bases and qualities, probabilistic calling, and inference from low-coverage data without hard genotype calls.
[^felsenstein81]: [[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]], *J Mol Evol* 17:368-376: likelihood of a tree computed recursively from the tips to the root.
[^goldberg]: [[Goldberg 1991 - What Every Computer Scientist Should Know About Floating-Point Arithmetic]], section on the IEEE standard (double format, denormalized numbers).
