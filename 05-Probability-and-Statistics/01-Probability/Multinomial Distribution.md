---
aliases:
  - Mult(n, p)
  - Multinomial Law
  - Categorical Counts
  - Loi multinomiale
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - domain/bioinformatics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Binomial Distribution]]"
  - "[[Binomial Coefficient]]"
  - "[[Combinatorics]]"
  - "[[Independence (Probability)]]"
  - "[[Expected Value]]"
  - "[[Variance]]"
related:
  - "[[Joint Distribution]]"
  - "[[Covariance]]"
  - "[[Dirichlet Distribution]]"
  - "[[Position Weight Matrix]]"
  - "[[Sequence Motif]]"
  - "[[Profile Hidden Markov Model]]"
  - "[[Hardy-Weinberg Equilibrium]]"
  - "[[Chi-Square Test]]"
  - "[[Kullback-Leibler Divergence]]"
  - "[[Hypergeometric Distribution]]"
  - "[[Compositional Data Analysis]]"
projects:
  - "[[07-evolution-simulator]]"
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Mendel 1866 - Experiments in Plant Hybridization]]"
  - "[[Anders 2010 - Differential Expression Analysis for Sequence Count Data]]"
---

# Multinomial Distribution

> [!abstract]
> The multinomial distribution counts how $n$ independent trials fall into several categories: the four nucleotides in one column of aligned binding sites, or the three genotypes AA, Aa and aa among sampled individuals. It is the binomial with more than two outcomes.

## Definition

Perform $n$ independent trials, each falling into one of $m$ categories with probabilities $p_1, \dots, p_m$ ($p_i \ge 0$, $\sum_i p_i = 1$). The vector of counts $X = (X_1, \dots, X_m)$ has the **multinomial distribution** $\mathrm{Mult}(n; p_1, \dots, p_m)$:[^blitz7][^durbin11]

$$P(X_1 = x_1, \dots, X_m = x_m) = \frac{n!}{x_1!\,x_2!\cdots x_m!}\;p_1^{x_1}p_2^{x_2}\cdots p_m^{x_m}, \qquad x_i \ge 0,\ \sum_i x_i = n,$$

with $E[X_i] = np_i$, $\operatorname{Var}(X_i) = np_i(1-p_i)$ and $\operatorname{Cov}(X_i, X_j) = -np_ip_j$ for $i \ne j$. With $m = 2$ it is the [[Binomial Distribution]].

## Why it matters

- **Motif columns.** The counts of A, C, G and T in one column of aligned binding sites (a column of a position frequency matrix) are a multinomial draw; the estimated probabilities, with pseudocounts, give the [[Position Weight Matrix]] used to scan genomes for a [[Sequence Motif]], and profile HMMs estimate their match-state emissions from alignment columns the same way ([[Profile Hidden Markov Model]]).[^compeau][^durbin5] Nucleotide counts along a sequence are likewise modeled as multinomial.[^holmes1]
- **Genotype counts.** Under Hardy-Weinberg proportions, the numbers of AA, Aa and aa individuals in a sample of $n$ are $\mathrm{Mult}(n; p^2, 2pq, q^2)$, the model behind Hardy-Weinberg tests in genotype quality control ([[Hardy-Weinberg Equilibrium]], [[Chi-Square Test]]).[^hartl] In [[07-evolution-simulator]], drawing genotypes or alleles of a new generation is a multinomial draw.

## Core (L2)

### Counting arrangements

One particular sequence of outcomes with counts $x_1, \dots, x_m$ has probability $p_1^{x_1}\cdots p_m^{x_m}$, by independence. The number of such sequences is the **multinomial coefficient** $\frac{n!}{x_1!\cdots x_m!} = \binom{n}{x_1}\binom{n - x_1}{x_2}\cdots$: choose the positions of category 1, then of category 2 among the rest, and so on ([[Binomial Coefficient]]). A column of 10 aligned sites with A6 C1 G2 T1 can arise in $10!/(6!\,1!\,2!\,1!) = 2520$ orders; with uniform bases each has probability $4^{-10}$, so the column has probability $2520/4^{10} = 0.0024$.

### Marginals and lumping

- **Each count is binomial**: a trial either falls in category $i$ or not, so $X_i \sim \mathrm{Bin}(n, p_i)$.
- **Merging categories** gives a multinomial with summed probabilities: $(X_A + X_T,\, X_C + X_G) \sim \mathrm{Mult}(n;\, p_A + p_T,\, p_C + p_G)$, so the G+C count of a sequence of independent bases is binomial ([[GC Content]]).
- Lumping Mendel's four classes ([[Mendelian Inheritance]]) by seed shape gives 423 round and 133 wrinkled seeds, one draw from $\mathrm{Bin}(556, 3/4)$ under his model (Exercise 2).[^mendel]

### Negative covariance: competing for a fixed total

$\operatorname{Cov}(X_i, X_j) = -np_ip_j$: with $n$ fixed, every trial that lands in category $i$ is lost to category $j$. The correlation is $-\sqrt{p_ip_j/\big((1-p_i)(1-p_j)\big)}$, $-1/3$ for two of four equally likely bases. In sequencing, a library holds a fixed number of reads, so a few very highly expressed genes take reads from all the others; this is why DESeq does not use the total count as the measure of library depth ([[Size Factor Estimation]], [[Compositional Data Analysis]]).[^anders]

### Poisson counts conditioned on their total

If $X_1, \dots, X_m$ are independent with $X_i \sim \mathrm{Pois}(\lambda_i)$, then given $X_1 + \dots + X_m = n$ they are $\mathrm{Mult}(n; \lambda_1/\Lambda, \dots, \lambda_m/\Lambda)$ with $\Lambda = \sum_i \lambda_i$ (proof in Mathematical representation; two categories in [[Binomial Distribution#Two Poisson counts, conditioned on their total]]). Independent Poisson counts per gene and a multinomial split of a library of fixed size are therefore the same model of relative abundances (Exercise 3).

## Advanced (L3)

### Estimating a motif column: maximum likelihood and pseudocounts

The maximum-likelihood estimate of a column is $\hat p_i = x_i/n$ (Mathematical representation). With few sites, a base never observed gets $\hat p_i = 0$, its log-odds score is $-\infty$, and any site carrying it is rejected, however good the rest. **Pseudocounts** fix this: $\hat p_i = (x_i + a_i)/(n + \sum_j a_j)$; adding 1 to every count is Laplace's rule of succession.[^compeau][^durbin11] The estimate is the posterior mean of $p$ under a Dirichlet prior with parameters $a_i$, the conjugate prior of the multinomial ([[Dirichlet Distribution]], [[Conjugate Prior]]).[^durbin11] The Worked example compares both estimates on invented sites.

### Scores are log-likelihood ratios

Scoring a site $s_1 \dots s_L$ with a position weight matrix adds $\log_2(p_{j, s_j}/q_{s_j})$ over positions, where $q$ is the background composition: it is the log-likelihood ratio of the site under the motif model (independent columns, one categorical draw each) against the background. Averaged over sites drawn from the motif, the score of a column is $\sum_b p_b \log_2(p_b/q_b)$, the relative entropy of the column to the background ([[Kullback-Leibler Divergence]], [[Shannon Entropy]]).

### Hardy-Weinberg as a one-parameter multinomial

![[hardy-weinberg-de-finetti-simplex.svg]]

Every genotype frequency vector $(f_{AA}, f_{Aa}, f_{aa})$ is a point of the triangle above, the set of possible parameters of a 3-category multinomial; Hardy-Weinberg proportions $(p^2, 2pq, q^2)$ form one curve inside it.[^hartl] The likelihood of genotype counts under Hardy-Weinberg,

$$L(p) = \frac{n!}{n_{AA}!\,n_{Aa}!\,n_{aa}!}\,2^{n_{Aa}}\,p^{n_A}q^{n_a}, \qquad n_A = 2n_{AA} + n_{Aa},\quad n_a = 2n - n_A,$$

depends on $p$ only through the allele count $n_A$, so the maximum-likelihood estimate is gene counting, $\hat p = n_A/2n$ ([[Allele Frequency]]). Both invented samples of the figure have $\hat p = 0.6$ and lie on the same vertical line, but sample 2 sits far below the curve: a heterozygote deficit. Conditioning on $n_A$ removes $p$ altogether. Under Hardy-Weinberg the $2n$ alleles are independent, so $n_A \sim \mathrm{Bin}(2n, p)$, and dividing $L$ by $\binom{2n}{n_A}p^{n_A}q^{n_a}$ gives

$$P(n_{AA}, n_{Aa}, n_{aa} \mid n_A) = \frac{n!\; n_A!\; n_a!\; 2^{n_{Aa}}}{n_{AA}!\; n_{Aa}!\; n_{aa}!\; (2n)!},$$

which contains no unknown parameter: this is why the exact Hardy-Weinberg test can be computed without knowing $p$ ([[Hardy-Weinberg Equilibrium#Testing a sample]]).

## Frontier (M1)

### Dirichlet priors for alignment columns

For protein profiles, uniform pseudocounts waste prior knowledge: some columns are hydrophobic, others charged. Durbin et al. estimate the emission probabilities of profile HMMs with pseudocounts derived from Dirichlet priors, including mixtures of Dirichlet densities that represent several typical kinds of columns.[^durbin5] Each mixture component is a different guess of $p$ for a column; the observed counts weight the components by their likelihood under the multinomial.

### Overdispersed category counts: the Dirichlet-multinomial

When the probability vector itself varies between samples (allele proportions across individuals, taxon proportions across microbiomes), draw $p \sim \mathrm{Dirichlet}(a_1, \dots, a_m)$ and then $X \mid p \sim \mathrm{Mult}(n; p)$. With $A = \sum_i a_i$ and $\bar p_i = a_i/A$, the law of total variance gives

$$\operatorname{Var}(X_i) = n\bar p_i(1 - \bar p_i)\,\frac{n + A}{1 + A},$$

the multinomial variance inflated by a factor that grows with $n$ (Exercise 4): the multi-category version of the [[Beta-Binomial Model]] and the analogue of the [[Negative Binomial Distribution]] for counts with a fixed total ([[Overdispersion]]).

## Mathematical representation

- **Normalization** by the multinomial theorem: $\sum_{x_1 + \dots + x_m = n} \frac{n!}{x_1!\cdots x_m!}\prod_i p_i^{x_i} = (p_1 + \dots + p_m)^n = 1$.
- **Moments by indicators.** Trial $t$ falls in category $C_t$; let $I_{t,i} = 1$ if $C_t = i$. Then $E[I_{t,i}] = p_i$, $\operatorname{Var}(I_{t,i}) = p_i(1 - p_i)$ and, since $I_{t,i}I_{t,j} = 0$ for $i \ne j$, $\operatorname{Cov}(I_{t,i}, I_{t,j}) = -p_ip_j$. Summing over $n$ independent trials, the covariance matrix of $X$ is $n\big(\operatorname{diag}(p) - pp^\top\big)$ ([[Covariance]]). Its rows sum to 0 because $\sum_i X_i = n$ is constant: the matrix is singular.
- **Maximum likelihood.** Maximize $\sum_i x_i \ln p_i$ subject to $\sum_i p_i = 1$: a Lagrange multiplier gives $x_i/p_i = \lambda$ for all $i$, hence $\hat p_i = x_i/n$ ([[Maximum Likelihood Estimation]]).
- **Poisson conditioning.** With $\Lambda = \sum_i \lambda_i$ and $\sum_i X_i \sim \mathrm{Pois}(\Lambda)$,

$$P\Big(X = x \,\Big|\, \sum_i X_i = n\Big) = \frac{\prod_i e^{-\lambda_i}\lambda_i^{x_i}/x_i!}{e^{-\Lambda}\Lambda^n/n!} = \frac{n!}{\prod_i x_i!}\prod_i\Big(\frac{\lambda_i}{\Lambda}\Big)^{x_i}.$$


## Computational representation

Compute the PMF in log space with `math.lgamma`; sample by tallying `random.choices`, which draws independent categorical trials.

```python
import math
import random
from collections import Counter

BASES = "ACGT"


def multinomial_pmf(counts: list[int], probs: list[float]) -> float:
    """P(X = counts) for X ~ Mult(n, probs) with n = sum(counts), computed in log space."""
    n = sum(counts)
    log_p = math.lgamma(n + 1) + sum(x * math.log(p) - math.lgamma(x + 1)
                                     for x, p in zip(counts, probs) if x > 0)
    return math.exp(log_p)


def multinomial_sample(n: int, probs: list[float], rng: random.Random) -> list[int]:
    """n independent categorical draws over BASES, tallied as counts of A, C, G, T."""
    tally = Counter(rng.choices(BASES, weights=probs, k=n))
    return [tally[b] for b in BASES]


print("P(A6 C1 G2 T1 | uniform):", round(multinomial_pmf([6, 1, 2, 1], [0.25] * 4), 4))
bg = [0.3, 0.2, 0.2, 0.3]                           # invented AT-rich background
rng = random.Random(20)
cols = [multinomial_sample(20, bg, rng) for _ in range(100_000)]
mean_a = sum(c[0] for c in cols) / len(cols)
mean_t = sum(c[3] for c in cols) / len(cols)
var_a = sum((c[0] - mean_a) ** 2 for c in cols) / len(cols)
cov_at = sum((c[0] - mean_a) * (c[3] - mean_t) for c in cols) / len(cols)
print(f"E[X_A] {mean_a:.3f} (np = 6), Var(X_A) {var_a:.3f} (np(1-p) = 4.2), Cov(X_A, X_T) {cov_at:.3f} (-np_A p_T = -1.8)")
```

```text
P(A6 C1 G2 T1 | uniform): 0.0024
E[X_A] 6.010 (np = 6), Var(X_A) 4.205 (np(1-p) = 4.2), Cov(X_A, X_T) -1.807 (-np_A p_T = -1.8)
```

The simulated columns of 20 sites reproduce the mean, variance and negative covariance of the formulas. `numpy.random.Generator.multinomial` and `scipy.stats.multinomial` provide the same operations on arrays.

## Worked example

> [!example] From aligned sites to a scoring matrix
> Eight invented binding sites of length 6 are aligned. Each column is a multinomial sample of size 8; its probabilities are estimated without and with a pseudocount of 1 per base, and two candidate sites are scored against a uniform background. Continuing the code above:
>
> ```python
> sites = ["TATAAT", "TATAAT", "TACAAT", "TATACT", "GATAAT", "TATGAT", "TATAAT", "AATAAT"]   # invented sites
> pfm = [[sum(s[j] == b for s in sites) for b in BASES] for j in range(len(sites[0]))]
> print("counts (A, C, G, T) per position:", pfm)
>
>
> def pwm(pfm: list[list[int]], pseudocount: float, background: float = 0.25) -> list[list[float]]:
>     """log2((count + a) / (n + 4a) / background) for each position and base; -inf for a zero estimate."""
>     rows = []
>     for col in pfm:
>         total = sum(col) + 4 * pseudocount
>         rows.append([math.log2((x + pseudocount) / total / background) if x + pseudocount > 0 else -math.inf
>                      for x in col])
>     return rows
>
>
> def score(seq: str, w: list[list[float]]) -> float:
>     return sum(w[j][BASES.index(b)] for j, b in enumerate(seq))
>
>
> for a in (0, 1):
>     w = pwm(pfm, a)
>     print(f"pseudocount {a}: position 2 = {[round(v, 2) for v in w[1]]}, "
>           f"score(TATAAT) = {score('TATAAT', w):.2f}, score(TCTAAT) = {score('TCTAAT', w):.2f}")
> ```
>
> ```text
> counts (A, C, G, T) per position: [[1, 0, 1, 6], [8, 0, 0, 0], [0, 1, 0, 7], [7, 0, 1, 0], [7, 1, 0, 0], [0, 0, 0, 8]]
> pseudocount 0: position 2 = [2.0, -inf, -inf, -inf], score(TATAAT) = 11.01, score(TCTAAT) = -inf
> pseudocount 1: position 2 = [1.58, -1.58, -1.58, -1.58], score(TATAAT) = 8.64, score(TCTAAT) = 5.47
> ```
>
> 1. **Counts.** Position 2 is A in all 8 sites; the maximum-likelihood estimate is $\hat p_A = 1$ and $\hat p_C = \hat p_G = \hat p_T = 0$.
> 2. **Without pseudocounts.** Any site with a C at position 2 scores $-\infty$: `TCTAAT`, which matches the consensus at five of six positions, is impossible under the model. Eight sites are not enough to conclude that a base never occurs.
> 3. **With a pseudocount of 1.** Position 2 becomes $(9, 1, 1, 1)/12$: A scores $\log_2(0.75/0.25) = 1.58$ bits and the others $\log_2(0.083/0.25) = -1.58$. The consensus still scores highest (8.64), and `TCTAAT` gets a finite, lower score (5.47).
> 4. **Price.** The pseudocount pulls every estimate toward uniform, lowering the consensus score from 11.01 to 8.64. With more sites the counts dominate the pseudocounts and the two estimates converge.

## Common misconceptions

> [!warning] "The category counts are independent binomials"
> Each count is binomial, but they are not independent: they sum to $n$, and every pair has covariance $-np_ip_j$. Treating them as independent (for example when testing several bases of a column separately) overcounts the evidence.

> [!warning] "A zero count means a zero probability"
> With 8 sites, a base of probability 0.05 is missing from a column with probability $0.95^8 = 0.66$. The maximum-likelihood estimate 0 is an artefact of small samples; pseudocounts or a prior are needed before taking logarithms.

## Exercises

> [!question] Exercise 1 (L2)
> Compute the probability of a column of 10 sites with A6 C1 G2 T1 under the background $(0.3, 0.2, 0.2, 0.3)$ for (A, C, G, T), and compare with the uniform background.

> [!success]- Solution
> $\frac{10!}{6!\,1!\,2!\,1!} \times 0.3^6 \times 0.2 \times 0.2^2 \times 0.3 = 2520 \times 1.7496 \times 10^{-6} = 0.0044$, against $0.0024$ with uniform bases (Computational representation). An A-rich column is less surprising against an AT-rich background, which is why motif scores must use the right background composition.

> [!question] Exercise 2 (L2)
> Mendel's dihybrid F2 counts are 315 round yellow, 108 round green, 101 wrinkled yellow and 32 wrinkled green.[^mendel] Lump them by seed shape and by seed colour. Under the $9:3:3:1$ model, what are the distributions, means and standard deviations of the round and yellow counts, and how far are the observations? Show that the two lumped counts have zero covariance under the model.

> [!success]- Solution
> Round: $315 + 108 = 423$; yellow: $315 + 101 = 416$. Each is $\mathrm{Bin}(556, 3/4)$: mean 417, SD $\sqrt{556 \times 0.75 \times 0.25} = 10.21$. The observations are $+0.59$ and $-0.10$ SD from the mean. With $p_1 = 9/16$ (round yellow), $p_2 = 3/16$ (round green), $p_3 = 3/16$ (wrinkled yellow):
> $$\operatorname{Cov}(X_1 + X_2, X_1 + X_3) = n\big[p_1(1 - p_1) - p_1p_3 - p_2p_1 - p_2p_3\big] = n\Big[\frac{63}{256} - \frac{27}{256} - \frac{27}{256} - \frac{9}{256}\Big] = 0.$$
> Independent assortment makes the $9:3:3:1$ probabilities a product of $3:1$ and $3:1$; the shape and colour of a seed are independent, and so are their totals.

> [!question] Exercise 3 (L3, Python)
> Continuing the code above, draw independent Poisson counts with means $(50, 30, 20)$ for three genes, keep the draws whose total is exactly 100, and compare the mean and variance of the first count and the frequency of the outcome $(50, 30, 20)$ with $\mathrm{Mult}(100; 0.5, 0.3, 0.2)$.

> [!success]- Solution
> ```python
> def poisson_sample(mu: float, rng: random.Random) -> int:
>     u, k = rng.random(), 0
>     p = cdf = math.exp(-mu)
>     while u > cdf:
>         k += 1
>         p *= mu / k
>         cdf += p
>     return k
>
>
> lam = [50, 30, 20]
> rng = random.Random(5)
> kept = []
> while len(kept) < 20_000:
>     x = [poisson_sample(m, rng) for m in lam]
>     if sum(x) == 100:
>         kept.append(x)
> m1 = sum(x[0] for x in kept) / len(kept)
> v1 = sum((x[0] - m1) ** 2 for x in kept) / len(kept)
> f = sum(x == [50, 30, 20] for x in kept) / len(kept)
> print(f"given total 100: mean X1 {m1:.2f} (50), var X1 {v1:.2f} (25), "
>       f"P(50, 30, 20) {f:.4f} vs multinomial {multinomial_pmf([50, 30, 20], [0.5, 0.3, 0.2]):.4f}")
> ```
>
> ```text
> given total 100: mean X1 49.96 (50), var X1 24.90 (25), P(50, 30, 20) 0.0099 vs multinomial 0.0091
> ```
>
> Given the total, the first count has mean $100 \times 0.5$ and variance $100 \times 0.5 \times 0.5 = 25$, half its unconditional Poisson variance of 50: fixing the total removes the variation of the total itself. The frequency of $(50, 30, 20)$ agrees with the multinomial PMF within the simulation noise (about $\pm 0.0007$).

> [!question] Exercise 4 (M1, Python)
> Derive $\operatorname{Var}(X_i) = n\bar p_i(1 - \bar p_i)(n + A)/(1 + A)$ for the Dirichlet-multinomial, using $\operatorname{Var}(p_i) = \bar p_i(1 - \bar p_i)/(1 + A)$ for a Dirichlet. Then, continuing the code above, check it with $a = (3, 2, 2, 3)$ and $n = 50$, drawing Dirichlet vectors as normalized gamma variables.

> [!success]- Solution
> Law of total variance: $E[\operatorname{Var}(X_i \mid p)] = nE[p_i(1 - p_i)] = n\big(\bar p_i(1 - \bar p_i) - \operatorname{Var}(p_i)\big)$ and $\operatorname{Var}(E[X_i \mid p]) = n^2\operatorname{Var}(p_i)$. The sum is $n\bar p_i(1 - \bar p_i) + n(n-1)\operatorname{Var}(p_i) = n\bar p_i(1 - \bar p_i)\big[1 + \frac{n-1}{1 + A}\big] = n\bar p_i(1 - \bar p_i)\frac{n + A}{1 + A}$.
>
> ```python
> rng = random.Random(6)
> alphas = [3.0, 2.0, 2.0, 3.0]                      # invented Dirichlet parameters, A = 10
> A = sum(alphas)
> n = 50
> xs = []
> for _ in range(50_000):
>     g = [rng.gammavariate(a_i, 1.0) for a_i in alphas]
>     probs = [gi / sum(g) for gi in g]               # one Dirichlet draw
>     xs.append(multinomial_sample(n, probs, rng)[0])
> m = sum(xs) / len(xs)
> v = sum((x - m) ** 2 for x in xs) / len(xs)
> p = alphas[0] / A
> print(f"mean {m:.2f} ({n * p}), variance {v:.2f} (multinomial {n * p * (1 - p):.1f}, "
>       f"Dirichlet-multinomial {n * p * (1 - p) * (n + A) / (1 + A):.2f})")
> ```
>
> ```text
> mean 14.89 (15.0), variance 56.86 (multinomial 10.5, Dirichlet-multinomial 57.27)
> ```
>
> With $A = 10$ and $n = 50$, sample-to-sample variation of $p$ multiplies the variance by $60/11 = 5.5$. As for the negative binomial, deeper sampling (larger $n$) makes the inflation worse, not better: only more samples average it out.

## Mastery checklist

- [ ] 1 Recognized: I can write the multinomial PMF, its means $np_i$ and its covariances $-np_ip_j$, and recognize count data with a fixed total.
- [ ] 2 Understood: I can explain marginals and lumping, the negative covariance, and the link between Poisson counts and a multinomial given the total.
- [ ] 3 Practiced: I can compute multinomial probabilities in log space, simulate columns, and build a position weight matrix with pseudocounts in Python.
- [ ] 4 Applied: in [[07-evolution-simulator]], I draw genotype or allele counts multinomially each generation and check Hardy-Weinberg proportions in the simulated populations.
- [ ] 5 Explained: I can teach why zero counts need pseudocounts, why the allele count suffices to estimate $p$, and when category counts are overdispersed (Dirichlet-multinomial).

## References

[^blitz7]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 7 "Joint Distributions" (the multinomial distribution: marginals, lumping, covariance).
[^durbin11]: [[Biological Sequence Analysis (Durbin)]], ch. 11 "Background on probability" (multinomial and Dirichlet distributions; estimating probabilities from counts with pseudocounts).
[^durbin5]: [[Biological Sequence Analysis (Durbin)]], ch. 5 "Profile HMMs for sequence families" (emission probabilities from alignment columns; pseudocounts, Dirichlet priors and Dirichlet mixtures).
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "Which DNA Patterns Play the Role of Molecular Clocks?" (count and profile matrices of motifs; pseudocounts and Laplace's rule of succession).
[^holmes1]: [[Modern Statistics for Modern Biology (Holmes)]], ch. 1 "Generative Models for Discrete Data" (multinomial models of nucleotide counts).
[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed. (2006), material on random mating and Hardy-Weinberg proportions (genotype frequencies $p^2$, $2pq$, $q^2$; gene counting).
[^mendel]: [[Mendel 1866 - Experiments in Plant Hybridization]], dihybrid F2 counts (315, 108, 101, 32 among 556 seeds).
[^anders]: [[Anders 2010 - Differential Expression Analysis for Sequence Count Data]], *Genome Biology* 11(10):R106: total read counts are unreliable as a depth measure because a few highly expressed genes can dominate them; median-of-ratios size factors.
