---
aliases:
  - Ne
  - N_e
  - Effective Size
  - Variance Effective Size
  - Inbreeding Effective Size
  - Taille efficace de population
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Genetic Drift]]"
  - "[[Heterozygosity]]"
  - "[[Allele Frequency]]"
related:
  - "[[Wright-Fisher Model]]"
  - "[[Coalescent Theory]]"
  - "[[Nucleotide Diversity]]"
  - "[[Watterson Estimator]]"
  - "[[Demographic Inference]]"
  - "[[Inbreeding]]"
  - "[[Gene Flow]]"
  - "[[Natural Selection]]"
  - "[[Neutral Theory of Molecular Evolution]]"
  - "[[Linkage Disequilibrium]]"
  - "[[Mutation Rate]]"
projects:
  - "[[07-evolution-simulator]]"
sources:
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Wright 1931 - Evolution in Mendelian Populations]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]]"
---

# Effective Population Size

> [!abstract]
> The effective population size $N_e$ is the size of an ideal population that would drift as fast as the real one; unequal sex ratios, unequal family sizes and past crashes make it much smaller than the number of individuals, and it is $N_e$, not the census, that sets the pace of drift and the level of diversity.

## Definition

The **effective population size** $N_e$ of a population is the number of individuals of an idealized Wright-Fisher population that would show the same amount of genetic drift, measured either by the variance of allele-frequency change between generations or by the rate of loss of heterozygosity.[^hartl] The concept goes back to Sewall Wright's 1931 theory of evolution in Mendelian populations.[^wright] It is usually smaller than the **census size** $N$, the number of individuals counted.[^hartl]

## Why it matters

- **Every drift formula uses it.** $\operatorname{Var}(\Delta p) = pq/2N_e$, $H_t = H_0(1 - 1/2N_e)^t$ and the $4N_e$ generations to fixation of [[Genetic Drift]] and [[Heterozygosity]] hold with $N_e$, not $N$.
- **Diversity and selection.** Neutral diversity is proportional to $\theta = 4N_e\mu$,[^hartl] the parameter that [[Nucleotide Diversity]] and the [[Watterson Estimator]] estimate; and selection is effective only when $|s|$ is large compared with $1/N_e$ ([[Natural Selection#Advanced (L3)]]).[^hartl]
- **Demographic inference.** Reconstructing $N_e$ through time from genomes is a central task of population genomics ([[Demographic Inference]], [[Coalescent Theory]]), and simulators take $N_e$ as their population-size parameter ([[Coalescent Simulation]], [[07-evolution-simulator]]).
- **Small populations.** How fast a captive or endangered population loses heterozygosity and becomes inbred is set by $N_e$, which management can raise by equalizing sex ratios and family sizes ([[Inbreeding]]).

## Core (L2)

### The ideal population and three classical departures

The Wright-Fisher population has a constant size, random union of gametes, offspring numbers that vary only by chance (approximately Poisson) and non-overlapping generations.[^hartl] Real populations depart from it, mostly in ways that increase drift:[^hartl]

| Departure | Effective size | Examples (code below) |
|---|---|---|
| Unequal numbers of breeding males $N_m$ and females $N_f$ | $N_e = \dfrac{4N_mN_f}{N_m + N_f}$ | 50 + 50: 100; 10 + 90: 36; 1 male + 50 females: 3.9 |
| Size $N_1, \dots, N_t$ changing over $t$ generations | harmonic mean, $N_e = \dfrac{t}{\sum_i 1/N_i}$ | the history in the figure: 92.6, not 804 |
| Variance $V_k$ of offspring number per individual, constant $N$ | $N_e = \dfrac{4N - 2}{V_k + 2}$ | $N = 100$: $V_k = 2$ (Poisson) 99.5; $V_k = 10$: 33.2; $V_k = 0$: 199 |

- **Sex ratio.** Half of every generation's genes come from males, half from females, so the rarer sex is a narrow channel through which half of the gene pool must pass: $1/N_e = 1/4N_m + 1/4N_f$.
- **Fluctuating size.** Heterozygosity is multiplied by $1 - 1/2N_i$ in each generation, so the smallest generations dominate the product, which is what the harmonic mean expresses.
- **Family size.** When a few parents leave many offspring, the next generation descends from fewer genomes than were present; when every parent leaves exactly two offspring ($V_k = 0$), $N_e$ approaches $2N$, the reason breeding programs equalize contributions.

### Bottlenecks

A **bottleneck** is a drastic reduction in population size; the survivors' gene pool can differ markedly from the original one.[^os19]

![[bottleneck-harmonic-mean.svg]]

In the invented history of the figure, two generations at 20 individuals in a population of 1,000 bring $N_e$ over the ten generations down to 92.6. They cost more heterozygosity (4.9%) than the eight generations at 1,000 combined (0.4%), and an allele at 5% before the crash is lost with probability 0.129 in the first bottleneck generation and 0.272 by the end of the second (Worked example). A short bottleneck therefore removes rare alleles far more than it reduces heterozygosity, to which rare alleles contribute little ([[Heterozygosity]]).

### Founder events

A **founder effect** arises when a few individuals start a new population: the new gene pool contains only the founders' alleles, at frequencies that can differ by chance from the source population, so founder populations can carry unusually high frequencies of particular alleles, including disease alleles.[^os19] With $n$ diploid founders ($2n$ copies), an allele at frequency $p$ is absent from the founders with probability $(1 - p)^{2n}$, and a fraction $1/2n$ of the heterozygosity is lost on average. With 5 founders, an allele at 5% is missing with probability $0.95^{10} = 0.60$, while heterozygosity drops by only 10%. The small founding generation then stays in the harmonic mean of every later generation.

## Advanced (L3)

- **Several effective sizes.** The variance effective size (from $\operatorname{Var}(\Delta p)$) and the inbreeding effective size (from the loss of heterozygosity) coincide in the ideal population but can differ when the population changes in size, so an estimate must say which one it is.[^hartl] The coalescent effective size summarizes the rate at which lineages coalesce backward in time ([[Coalescent Theory]]).
- **Estimating $N_e$ from data.**
  1. *Temporal method*: allele-frequency change between samples taken $t$ generations apart has expectation $E[(p_t - p_0)^2] = p_0q_0[1 - (1 - 1/2N_e)^t]$ ([[Genetic Drift#Mathematical representation]]); averaging over many loci gives $\hat N_e$ (Exercise 5). Sampling noise from finite samples inflates $(\Delta p)^2$ and biases $\hat N_e$ downward unless it is subtracted.
  2. *Decay of heterozygosity* in replicated or monitored populations ([[Heterozygosity]]).
  3. *Diversity*: $\pi \approx \theta = 4N_e\mu$ gives $N_e = \pi/4\mu$. With the human germline rate $\mu = 1.20 \times 10^{-8}$ per nucleotide per generation[^kong] and an invented $\pi = 0.001$, $N_e \approx 20{,}800$. This is a long-term average over the population's history, not its present size ([[Nucleotide Diversity]]).
  4. *Linkage disequilibrium and genome-wide coalescent methods* reconstruct $N_e$ through time ([[Linkage Disequilibrium]], [[Demographic Inference]]).
- **Selection in small populations.** Because drift scales with $1/N_e$, a selection coefficient that decides an allele's fate in a large population can be effectively neutral in a small one ([[Neutral Theory of Molecular Evolution]]).[^hartl]
- **Recovery is slow.** After the census recovers, lost alleles return only by new mutation or by migration from other populations ([[Gene Flow]]), so the genetic footprint of a bottleneck outlasts it by many generations.

## Mathematical representation

- **Variance effective size**: $\operatorname{Var}(p_{t+1} \mid p_t) = \dfrac{p_tq_t}{2N_e}$.
- **Inbreeding (heterozygosity) effective size**: $H_{t+1} = \left(1 - \dfrac{1}{2N_e}\right)H_t$.
- **Harmonic mean.** $\dfrac{H_t}{H_0} = \prod_{i=1}^{t}\left(1 - \dfrac{1}{2N_i}\right) \approx \exp\left(-\sum_i \dfrac{1}{2N_i}\right)$, and setting this equal to $\exp(-t/2N_e)$ gives $\dfrac{1}{N_e} = \dfrac{1}{t}\sum_{i=1}^{t}\dfrac{1}{N_i}$.
- **Separate sexes.** Two genes drawn from different offspring are both paternal with probability about $1/4$, and then copies of the same paternal gene with probability $1/2N_m$; both maternal with probability about $1/4$, and then identical with probability $1/2N_f$. Their probability of coalescing in one generation is $\frac{1}{8N_m} + \frac{1}{8N_f}$, which equals $\frac{1}{2N_e}$ for $N_e = \frac{4N_mN_f}{N_m + N_f}$.
- **Founders.** $P(\text{allele absent among } 2n \text{ founder copies}) = (1-p)^{2n}$; $E[H_{\text{founded}}] = \left(1 - \frac{1}{2n}\right)H_{\text{source}}$.
- **Temporal estimator.** Over $L$ loci, $\hat F = \frac{1}{L}\sum_{l} \dfrac{(p_{t,l} - p_{0,l})^2}{p_{0,l}\,q_{0,l}}$ and $\hat N_e = \dfrac{1}{2\left[1 - (1 - \hat F)^{1/t}\right]} \approx \dfrac{t}{2\hat F}$.

## Computational representation

The three classical formulas, and the exact probability that an allele is lost through a few small generations, obtained by propagating the binomial distribution of allele counts (small sizes only: large binomial coefficients overflow floating point).

```python
from math import comb


def ne_sex_ratio(n_males: int, n_females: int) -> float:
    """Effective size with separate sexes: 4 Nm Nf / (Nm + Nf)."""
    return 4 * n_males * n_females / (n_males + n_females)


def ne_harmonic(sizes: list[int]) -> float:
    """Effective size over generations of changing size: the harmonic mean."""
    return len(sizes) / sum(1 / n for n in sizes)


def ne_family_variance(n: int, v_k: float) -> float:
    """Effective size for constant N when offspring numbers have variance v_k (Poisson: 2)."""
    return (4 * n - 2) / (v_k + 2)


def loss_probability(p: float, sizes: list[int]) -> float:
    """Exact P(an allele at frequency p is lost) through Wright-Fisher generations of given sizes."""
    dist = {p: 1.0}                                        # frequency -> probability
    for n in sizes:
        two_n, new = 2 * n, {}
        for f, w in dist.items():
            for k in range(two_n + 1):
                pk = comb(two_n, k) * f ** k * (1 - f) ** (two_n - k)
                new[k / two_n] = new.get(k / two_n, 0.0) + w * pk
        dist = new
    return dist.get(0.0, 0.0)


print(ne_sex_ratio(50, 50), ne_sex_ratio(10, 90), round(ne_sex_ratio(1, 50), 2))
print(ne_family_variance(100, 2), round(ne_family_variance(100, 10), 1), ne_family_variance(100, 0))

sizes = [1000, 1000, 20, 20, 1000, 1000, 1000, 1000, 1000, 1000]     # invented history, 10 generations
kept = 1.0
for n in sizes:
    kept *= 1 - 1 / (2 * n)                                          # heterozygosity kept per generation
print(sum(sizes) / len(sizes), round(ne_harmonic(sizes), 1), round(kept, 4), round((1 - 1 / 2000) ** 10, 4))
print(round(loss_probability(0.05, [20]), 4), round(loss_probability(0.05, [20, 20]), 4))
```

```text
100.0 36.0 3.92
99.5 33.2 199.0
804.0 92.6 0.9468 0.995
0.1285 0.2722
```

## Worked example

> [!example] The bottleneck of the figure (invented history)
> A population of 1,000 individuals crashes to 20 for two generations, then recovers; we follow ten generations.
> 1. **Arithmetic mean**: $(8 \times 1000 + 2 \times 20)/10 = 804$.
> 2. **Effective size**: $10 / (8/1000 + 2/20) = 10 / 0.108 = 92.6$.
> 3. **Heterozygosity kept**: $(1 - 1/2000)^8 \times (1 - 1/40)^2 = 0.9960 \times 0.9506 = 0.9468$, against 0.995 at a constant 1,000. An ideal population of 92.6 would keep $(1 - 1/185.2)^{10} = 0.9473$, nearly the same: the harmonic mean does its job. The two bottleneck generations account for 93% of the loss.
> 4. **Rare alleles**: an allele at 5% before the crash is absent from the 40 gene copies of the first bottleneck generation with probability $0.95^{40} = 0.129$, and lost by the end of the second with probability 0.272 (exact computation in the code).
> 5. **Reading**: the census is back at 1,000 for six generations, yet the population has lost about a quarter of its 5% variants and drifts, on average over the period, like a population of 93.

## Common misconceptions

> [!warning] "The effective size is the number of adults, or of breeders"
> Even counting only individuals that reproduce, an unequal sex ratio or unequal family sizes make $N_e$ smaller: one male and 50 females behave like 3.9 ideal individuals. $N_e$ is defined by the rate of drift, not by a head count.

> [!warning] "The effective size is the average size over time"
> It is close to the harmonic mean, which the smallest generations dominate: 92.6, not 804, in the figure.

> [!warning] "When the census recovers, diversity recovers"
> Alleles lost in a bottleneck come back only by new mutation or migration, which is slow; heterozygosity rebuilds on the time scale of mutation, not of reproduction.

> [!warning] "$N_e$ is always smaller than $N$"
> Usually, but not necessarily: with exactly equal family sizes ($V_k = 0$), $N_e = 2N - 1$, nearly twice the census.

## Exercises

> [!question] Exercise 1 (L2)
> A breeding group has 4 males and 36 females. Compute $N_e$, then the number of generations needed to lose 10% of the heterozygosity, compared with an ideal population of 40.

> [!success]- Solution
> $N_e = 4 \times 4 \times 36 / 40 = 14.4$. Solve $(1 - 1/2N_e)^t = 0.9$: $t = \ln 0.9 / \ln(1 - 1/28.8) = 3.0$ generations, against $\ln 0.9 / \ln(1 - 1/80) = 8.4$ for 40 ideal individuals. Adding males is the most efficient way to slow the loss.

> [!question] Exercise 2 (L2)
> A population counts 500, 50, 500, 500 and 5,000 individuals in five successive generations. Compute its effective size over this period and compare with the arithmetic mean.

> [!success]- Solution
> $N_e = 5 / (1/500 + 1/50 + 1/500 + 1/500 + 1/5000) = 5/0.0262 = 190.8$, against an arithmetic mean of 1,310. The single generation at 50 contributes 0.02 of the 0.0262 in the denominator; the expansion to 5,000 hardly helps.

> [!question] Exercise 3 (L2)
> Three individuals found a new island population. What is the probability that an allele with frequency 0.1 in the source population is absent from the founders, and what fraction of heterozygosity is expected to remain?

> [!success]- Solution
> The founders carry 6 copies: $P(\text{absent}) = 0.9^6 = 0.531$. Expected heterozygosity kept: $1 - 1/6 = 0.833$. More often than not, a 10% allele is missing from the new population, while heterozygosity falls by only a sixth.

> [!question] Exercise 4 (L3, Python)
> Continuing the code above, simulate random mating with separate sexes, each offspring receiving one random gene of a random father and one of a random mother. Starting from random genotypes at $p = 0.5$, compare the fraction of heterozygosity ($2pq$) kept after 10 generations, over 4,000 replicates, with the predictions for $N_e$ and for the census, for 25 males + 25 females and for 5 males + 45 females.

> [!success]- Solution
> ```python
> import random
>
>
> def gene_pool_het(pop: list[tuple[bool, bool]]) -> float:
>     """2pq of the 2N allele copies of a population (True = allele A)."""
>     p = sum(a + b for a, b in pop) / (2 * len(pop))
>     return 2 * p * (1 - p)
>
>
> def heterozygosity_ratio(n_males: int, n_females: int, generations: int, reps: int, seed: int) -> float:
>     """Mean 2pq after `generations` of random mating with separate sexes, over its starting mean."""
>     rng = random.Random(seed)
>     n = n_males + n_females
>     start = end = 0.0
>     for _ in range(reps):
>         pop = [(rng.random() < 0.5, rng.random() < 0.5) for _ in range(n)]   # random start, p near 0.5
>         start += gene_pool_het(pop)
>         for _ in range(generations):
>             fathers, mothers = pop[:n_males], pop[n_males:]
>             pop = [(rng.choice(rng.choice(fathers)), rng.choice(rng.choice(mothers))) for _ in range(n)]
>         end += gene_pool_het(pop)
>     return end / start
>
>
> t = 10
> for nm, nf in ((25, 25), (5, 45)):
>     ne = ne_sex_ratio(nm, nf)
>     print(nm, nf, ne, round(heterozygosity_ratio(nm, nf, t, 4000, seed=3), 3),
>           round((1 - 1 / (2 * ne)) ** t, 3), round((1 - 1 / (2 * (nm + nf))) ** t, 3))
> ```
> ```text
> 25 25 50.0 0.907 0.904 0.904
> 5 45 18.0 0.76 0.754 0.904
> ```
> With 5 males, 50 individuals keep 76% of their heterozygosity, as an ideal population of 18 would (75.4%), not 90% as the census suggests. The formula is an approximation that degrades in extreme cases: with 2 males and 18 females, `heterozygosity_ratio(2, 18, 10, 4000, seed=3)` gives 0.52 where it predicts 0.487.

> [!question] Exercise 5 (L3, Python)
> Continuing the code above, simulate 1,000 independent neutral loci drifting for 10 generations in a population of $N_e = 50$, then estimate $N_e$ from the starting and final frequencies with the temporal estimator, as if the truth were unknown.

> [!success]- Solution
> ```python
> rng = random.Random(5)
> true_ne, t, loci = 50, 10, 1000
> two_n = 2 * true_ne
> p0, pt = [], []
> for _ in range(loci):                                     # 1,000 neutral loci, independent
>     count = rng.randint(20, 80)                           # starting frequency between 0.2 and 0.8
>     p0.append(count / two_n)
>     for _ in range(t):                                    # 10 generations of drift at Ne = 50
>         count = sum(rng.random() < count / two_n for _ in range(two_n))
>     pt.append(count / two_n)
> f_hat = sum((b - a) ** 2 / (a * (1 - a)) for a, b in zip(p0, pt)) / loci
> ne_hat = 1 / (2 * (1 - (1 - f_hat) ** (1 / t)))
> print(round(f_hat, 4), round(ne_hat, 1), round(1 - (1 - 1 / two_n) ** t, 4))
> ```
> Output: `0.0939 50.9 0.0956`. $\hat F = 0.094$ against an expected 0.096, and $\hat N_e = 50.9$ for a true 50. Here the frequencies are known exactly; with real samples of a few dozen individuals, sampling noise adds to $(\Delta p)^2$ and must be subtracted, or $\hat N_e$ is biased low. Each locus is a single noisy draw, which is why the method needs many loci.

## Mastery checklist

- [ ] 1 Recognized: I can define $N_e$ as the size of the ideal population that drifts at the same rate, and say why it is usually below the census.
- [ ] 2 Understood: I can explain the sex-ratio, harmonic-mean and family-size formulas, and what bottlenecks and founder events do to heterozygosity and to rare alleles.
- [ ] 3 Practiced: I can compute $N_e$ for a given demography and estimate it from simulated allele-frequency changes.
- [ ] 4 Applied: in [[07-evolution-simulator]], I ran populations with skewed sex ratios and a bottleneck and recovered $N_e$ from the simulated loss of heterozygosity.
- [ ] 5 Explained: I can teach the different definitions of $N_e$, the main ways of estimating it from genomes, and why a species' long-term $N_e$ can be far from its census.

## References

[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed. (2006), treatment of effective population size (the idealized population; unequal sex ratio, fluctuating size and the harmonic mean, variance in offspring number; variance and inbreeding effective sizes; $\theta = 4N_e\mu$; drift versus selection in small populations).
[^wright]: [[Wright 1931 - Evolution in Mendelian Populations]], *Genetics* 16:97-159.
[^os19]: [[Biology 2e (OpenStax)]], ch. 19 "The Evolution of Populations", section "Population Genetics" (bottleneck effect, founder effect).
[^kong]: [[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]], *Nature* 488:471-475.
