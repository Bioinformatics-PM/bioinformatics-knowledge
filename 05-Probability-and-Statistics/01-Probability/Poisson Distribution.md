---
aliases:
  - Poisson Law
  - Pois(λ)
  - Law of Rare Events
  - Loi de Poisson
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
  - "[[Random Variable]]"
  - "[[Probability Distribution]]"
  - "[[Expected Value]]"
  - "[[Variance]]"
  - "[[Binomial Distribution]]"
  - "[[Exponential Function]]"
  - "[[Limit]]"
  - "[[Infinite Series]]"
related:
  - "[[Bernoulli Distribution]]"
  - "[[Poisson Process]]"
  - "[[Exponential Distribution]]"
  - "[[Negative Binomial Distribution]]"
  - "[[Normal Distribution]]"
  - "[[Sequencing Coverage]]"
  - "[[Lander-Waterman Model]]"
  - "[[Mutation Rate]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Harvard Stat 110 - Probability]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Lander 1988 - Genomic Mapping by Fingerprinting Random Clones]]"
  - "[[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
---

# Poisson Distribution

> [!abstract]
> The Poisson distribution counts events that have many chances to happen, each very unlikely and independent of the others: reads covering a base, new mutations in a child's genome. One number, the mean $\lambda$, fixes it, and it is also the variance.

## Definition

A random variable $X$ with values in $\{0, 1, 2, \dots\}$ has the **Poisson distribution** with parameter $\lambda > 0$, written $X \sim \mathrm{Pois}(\lambda)$, if

$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \qquad k = 0, 1, 2, \dots$$

It models the number of events in a fixed interval of time or space when events occur independently at a constant average rate; its mean and its variance both equal $\lambda$.[^openstax][^blitz][^stat110]

## Why it matters

- **Sequencing coverage.** With reads dropped at random on a genome, the depth at a base is approximately Poisson with mean the coverage $c$. This is how one plans how much to sequence and predicts the fraction of the genome left uncovered ([[Sequencing Coverage]], [[Lander-Waterman Model]]).[^lw]
- **Mutation counts.** The number of new mutations in a genome per generation, or of substitutions in a gene, is a count of rare independent events across billions of sites: a natural model for [[Mutation Rate]] estimates and for [[07-evolution-simulator]].[^kong]
- **Count data baseline.** Read counts per gene are the starting model for RNA-seq; their excess variance over the Poisson is what the [[Negative Binomial Distribution]] captures in differential expression tools.[^holmes]
- **Simulation.** Drawing a Poisson number of events, then placing them, is a simple way to simulate mutations, reads or crossovers ([[Poisson Process]], [[Random Variate Generation]]).

## Core (L1)

**When to use it.** Four conditions make a count approximately Poisson:[^blitz][^openstax]

1. a large number $n$ of opportunities (bases, reads, cells, time slices);
2. each opportunity yields an event with a small probability $p$;
3. opportunities behave independently;
4. the expected total $\lambda = np$ is moderate and known or estimated.

Then only $\lambda$ matters: $n = 10^9$ sites with $p = 3 \times 10^{-9}$ and $n = 10^6$ with $p = 3 \times 10^{-6}$ give essentially the same distribution of counts, $\mathrm{Pois}(3)$.

**The binomial limit.** The exact count of events in $n$ independent trials is $\mathrm{Bin}(n, p)$ ([[Binomial Distribution]]). If $n \to \infty$ while $np = \lambda$ stays fixed, the binomial probabilities converge to the Poisson ones (derivation in Mathematical representation).[^blitz] The figure shows the convergence for $\lambda = 3$: already at $n = 100$ the two are hard to tell apart.

![[poisson-binomial-limit.svg]]

**Shape.** The distribution is on the non-negative integers, right-skewed for small $\lambda$ and increasingly symmetric as $\lambda$ grows. Mean $E[X] = \lambda$ and variance $\operatorname{Var}(X) = \lambda$ ([[Expected Value]], [[Variance]]), so the standard deviation is $\sqrt{\lambda}$ and the relative spread $\sqrt{\lambda}/\lambda = 1/\sqrt{\lambda}$ shrinks as counts grow.[^blitz] Two values recur: $P(X = 0) = e^{-\lambda}$ (no event at all) and $P(X \ge 1) = 1 - e^{-\lambda}$; for coverage, $e^{-c}$ is the expected fraction of the genome that no read touches.

## Deeper (L2)

### Operations on Poisson counts

- **Sums.** If $X \sim \mathrm{Pois}(\lambda)$ and $Y \sim \mathrm{Pois}(\mu)$ are independent, then $X + Y \sim \mathrm{Pois}(\lambda + \mu)$ (proof in Mathematical representation).[^blitz] Mutations from the father and from the mother add up to a Poisson total.
- **Thinning.** If each of $N \sim \mathrm{Pois}(\lambda)$ events is kept independently with probability $q$, the number kept is $\mathrm{Pois}(\lambda q)$, and the numbers kept and discarded are independent.[^blitz] If a fraction $q$ of the genome is coding, the coding de novo mutations of a child are again Poisson, with mean $\lambda q$.
- **Along a sequence.** Events scattered independently along a genome at rate $r$ per base give a $\mathrm{Pois}(r\ell)$ count in any window of length $\ell$, independent counts in disjoint windows, and exponential gaps between events: the [[Poisson Process]], whose waiting times follow the [[Exponential Distribution]].
- **Large $\lambda$.** $\mathrm{Pois}(\lambda)$ is close to $\mathcal{N}(\lambda, \lambda)$: for integer $\lambda$ it is a sum of $\lambda$ independent $\mathrm{Pois}(1)$ counts, and the [[Central Limit Theorem]] applies. A depth of 30 has standard deviation $\sqrt{30} \approx 5.5$ ([[Normal Distribution]]).

### Lander-Waterman: coverage, gaps and islands

Lander and Waterman analyzed genome mapping from clones placed at random, deriving the expected numbers of islands and gaps from the number of clones, their length, the genome length and the overlap needed to detect a join.[^lw] In sequencing language: $N$ reads of length $L$ on a genome of length $G$, **coverage** $c = NL/G$.

- **Depth at a base.** A read covers a fixed base if it starts at one of the $L$ positions ending at that base, probability $L/G$. The depth is $\mathrm{Bin}(N, L/G) \approx \mathrm{Pois}(c)$ because $N$ is large and $L/G$ tiny. Fraction uncovered: $e^{-c}$.
- **Islands (contigs).** Suppose two reads are joined when they overlap by at least $\theta L$ bases ($0 \le \theta < 1$). A read is the last of its island when no other read starts in the $(1 - \theta)L$ positions after its own start. The number of such starts is $\approx \mathrm{Pois}(c(1 - \theta))$, so each read ends an island with probability $e^{-c(1-\theta)}$ and the expected number of islands is $N e^{-c(1-\theta)}$ (Exercise 4).
- **Assumptions.** Uniform placement and perfect overlap detection. Anything that makes some regions harder to sequence or to join violates them, so the model gives a best case.

## Advanced (L3)

### Overdispersion and the negative binomial

Real counts often vary more than a Poisson with the same mean. The reason is usually that $\lambda$ itself differs between units, for example the expression of a gene between biological replicates.[^holmes] The same happens to coverage when some regions are systematically easier to sequence than others: the depth becomes a Poisson mixture with a heavier low-depth tail. If $X \mid \lambda \sim \mathrm{Pois}(\lambda)$ with $\lambda$ random, the law of total variance ([[Conditional Expectation]]) gives

$$\operatorname{Var}(X) = E[\operatorname{Var}(X \mid \lambda)] + \operatorname{Var}(E[X \mid \lambda]) = E[\lambda] + \operatorname{Var}(\lambda) \;\ge\; E[X].$$

With a gamma-distributed $\lambda$ the mixture is exactly the [[Negative Binomial Distribution]], the count model of RNA-seq differential expression.[^holmes] For de novo mutations, Kong et al. found that the father's age drives most of the variation between children, about two extra mutations per year of paternal age:[^kong] children of fathers of different ages form a Poisson mixture (Exercise 5).

### The Poisson paradigm

The events need not share one probability. A sum of many independent (or weakly dependent) rare indicators with probabilities $p_i$ is approximately $\mathrm{Pois}(\sum_i p_i)$.[^blitz] Even if sites differ in mutability, the total number of new mutations is still close to Poisson given the total rate: heterogeneity **across sites** within one genome keeps the Poisson form, heterogeneity **across genomes** creates overdispersion.

### Variance stabilization and regression

Because $\operatorname{Var}(X) = \lambda$ grows with the mean, raw counts are heteroscedastic. The delta method with $g(x) = \sqrt{x}$ gives $\operatorname{Var}(\sqrt{X}) \approx g'(\lambda)^2 \lambda = 1/4$ for large $\lambda$, independent of $\lambda$: the square root stabilizes Poisson variance, and $\log(x + 1)$ does a similar job for overdispersed counts ([[Data Transformation]]). When the mean depends on covariates, [[Poisson Regression]] models $\log E[Y] = \log(\text{exposure}) + \mathbf{x}^\top \boldsymbol\beta$, with library size or region length as the exposure.

## Mathematical representation

**Normalization.** From the exponential series $e^{\lambda} = \sum_{k \ge 0} \lambda^k / k!$ ([[Taylor Series]]), $\sum_{k \ge 0} e^{-\lambda}\lambda^k/k! = e^{-\lambda} e^{\lambda} = 1$.

**Mean and variance.**

$$E[X] = \sum_{k \ge 1} k \frac{e^{-\lambda}\lambda^k}{k!} = \lambda \sum_{k \ge 1} \frac{e^{-\lambda}\lambda^{k-1}}{(k-1)!} = \lambda, \qquad E[X(X-1)] = \lambda^2 \sum_{k \ge 2} \frac{e^{-\lambda}\lambda^{k-2}}{(k-2)!} = \lambda^2,$$

so $\operatorname{Var}(X) = E[X(X-1)] + E[X] - E[X]^2 = \lambda^2 + \lambda - \lambda^2 = \lambda$.

**Generating function.** $G_X(s) = E[s^X] = e^{\lambda(s - 1)}$. For independent $X, Y$, $G_{X+Y} = G_X G_Y = e^{(\lambda + \mu)(s-1)}$, the generating function of $\mathrm{Pois}(\lambda + \mu)$.

**Poisson as the limit of the binomial.** Let $X_n \sim \mathrm{Bin}(n, \lambda/n)$ and fix $k$. Then

$$P(X_n = k) = \binom{n}{k}\left(\frac{\lambda}{n}\right)^k\left(1 - \frac{\lambda}{n}\right)^{n-k} = \frac{\lambda^k}{k!} \cdot \underbrace{\frac{n(n-1)\cdots(n-k+1)}{n^k}}_{\to 1} \cdot \underbrace{\left(1 - \frac{\lambda}{n}\right)^{n}}_{\to e^{-\lambda}} \cdot \underbrace{\left(1 - \frac{\lambda}{n}\right)^{-k}}_{\to 1}.$$

The first bracket is a product of $k$ factors $(n - j)/n \to 1$ ($k$ is fixed); the second uses $(1 + x/n)^n \to e^{x}$ ([[Limit]]); the third has a fixed exponent. Hence $P(X_n = k) \to e^{-\lambda}\lambda^k/k!$ for every $k$.

**Recurrence.** $P(X = k) = P(X = k - 1) \cdot \lambda / k$: the probabilities increase while $k < \lambda$ and decrease after, so the mode is $\lfloor \lambda \rfloor$ (and also $\lambda - 1$ when $\lambda$ is an integer).

## Computational representation

Direct evaluation of $\lambda^k / k!$ overflows for large $k$; compute in log space with `math.lgamma(k + 1)` $= \ln k!$, or accumulate the recurrence. `poisson_cdf` below starts from $e^{-\lambda}$, which underflows to 0 for $\lambda$ above about 745: use log-space sums there.

```python
import math
import random

def poisson_pmf(k: int, lam: float) -> float:
    """P(X = k) for X ~ Pois(lam), computed in log space so large k and lam do not overflow."""
    if k < 0:
        return 0.0
    return math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1))

def poisson_cdf(k: int, lam: float) -> float:
    """P(X <= k), accumulating the recurrence p(j) = p(j - 1) * lam / j."""
    p = total = math.exp(-lam)
    for j in range(1, k + 1):
        p *= lam / j
        total += p
    return total

def poisson_sample(lam: float, rng: random.Random) -> int:
    """Inversion: walk up the CDF until it passes a uniform draw (fine for moderate lam)."""
    u, k = rng.random(), 0
    p = cdf = math.exp(-lam)
    while u > cdf:
        k += 1
        p *= lam / k
        cdf += p
    return k

print(round(poisson_pmf(2, 3.0), 4), round(poisson_cdf(2, 3.0), 4))
rng = random.Random(2024)
draws = [poisson_sample(3.0, rng) for _ in range(100_000)]
m = sum(draws) / len(draws)
v = sum((x - m) ** 2 for x in draws) / (len(draws) - 1)
print(f"mean {m:.3f}, variance {v:.3f}")
```

Output:

```text
0.224 0.4232
mean 3.002, variance 3.016
```

The simulated mean and variance agree with $\lambda = 3$. In practice, NumPy's `Generator.poisson` and `scipy.stats.poisson` provide the same operations.

## Worked example

> [!example] Coverage from simulated reads (Lander-Waterman)
> Reads of $L = 100$ bp are placed uniformly on a circular genome of $G = 10^6$ bp at coverage $c = 5$, so $N = cG/L = 50{,}000$ reads. Continuing the code above:
>
> ```python
> def simulate_depth(genome_len: int, read_len: int, coverage: float, seed: int) -> list[int]:
>     """Drop reads uniformly on a circular genome; return the depth at every position."""
>     rng = random.Random(seed)
>     depth = [0] * genome_len
>     for _ in range(round(coverage * genome_len / read_len)):
>         start = rng.randrange(genome_len)
>         for i in range(start, start + read_len):
>             depth[i % genome_len] += 1               # modulo: reads wrap around the origin
>     return depth
>
> G, L, c = 1_000_000, 100, 5.0
> depth = simulate_depth(G, L, c, seed=1)
> mean = sum(depth) / G
> var = sum((d - mean) ** 2 for d in depth) / G
> print(f"mean depth {mean:.3f}, variance {var:.3f}")
> for k in (0, 1, 3, 5, 8, 10):
>     print(k, f"{sum(d == k for d in depth) / G:.4f}", f"{poisson_pmf(k, c):.4f}")
> ```
>
> ```text
> mean depth 5.000, variance 5.080
> 0 0.0074 0.0067
> 1 0.0344 0.0337
> 3 0.1405 0.1404
> 5 0.1728 0.1755
> 8 0.0662 0.0653
> 10 0.0185 0.0181
> ```
>
> 1. **Mean.** Exactly 5: on a circle every read contributes $L$ bases of depth, so total depth is $NL = cG$.
> 2. **Variance ≈ mean.** 5.08 against the Poisson value 5: the signature of a Poisson count.
> 3. **Uncovered fraction.** 0.74 % observed against $e^{-5} = 0.67$ %. The residual difference is sampling noise: neighbouring bases share reads, so the $10^6$ depths are strongly correlated and behave like far fewer independent draws.
> 4. **Scaling up.** For a human genome ($G = 3.055 \times 10^9$ bp)[^nurk] at $c = 30$, `poisson_cdf(15, 30)` gives $P(\text{depth} \le 15) \approx 0.0019$: even under ideal random sampling, about 6 Mb would have depth 15 or less. Any systematic bias in real libraries makes this low-depth tail heavier (Advanced (L3)).

> [!example] New mutations in a child's genome
> Kong et al. measured a de novo rate of $\mu = 1.20 \times 10^{-8}$ per nucleotide per generation (average father's age 29.7 years).[^kong] A diploid genome has about $n = 2 \times 3.055 \times 10^9 = 6.11 \times 10^9$ sites.[^nurk] If each site mutates independently with probability $\mu$, the count is $\mathrm{Bin}(n, \mu) \approx \mathrm{Pois}(\lambda)$ with
>
> $$\lambda = n\mu \approx 6.11 \times 10^9 \times 1.20 \times 10^{-8} \approx 73.$$
>
> This back-of-the-envelope value extrapolates the rate to the whole diploid genome; a study observes only the part of the genome it can genotype reliably, so its counts per child are lower. Under the model, the standard deviation is $\sqrt{73.3} \approx 8.6$ and about 95 % of children would carry between 57 and 91 new mutations (central interval from `poisson_cdf`). Kong et al. found a larger spread, explained mainly by the father's age: see Advanced (L3).

## Common misconceptions

> [!warning] "The Poisson is for small counts"
> $\lambda$ can be 73 or 10,000. What must be small is the probability per opportunity, not the count. For large $\lambda$ the Poisson simply looks normal.

> [!warning] "Coverage 30× means each base is read 30 times"
> 30 is the mean depth. Under the ideal Poisson model the depth has standard deviation 5.5, and a fraction $e^{-30}$ of bases is still missed; real data are more variable than the model.

> [!warning] "Count data are Poisson"
> Poisson is the baseline, not the default. Counts from different biological samples usually show variance greater than the mean.[^holmes] A test that assumes Poisson variance then underestimates the noise and reports too many significant differences. Check the variance-to-mean ratio before using it.

## Exercises

> [!question] Exercise 1 (L1)
> A 10 kb region is sequenced in 1,000 children (both parental copies). With $\mu = 1.2 \times 10^{-8}$ per base per generation, what is the probability of observing at least one de novo mutation in the region across all children? At least two?

> [!success]- Solution
> Opportunities: $n = 2 \times 10^4 \times 1000 = 2 \times 10^7$ base-generations, so $\lambda = n\mu = 0.24$. Then $P(X \ge 1) = 1 - e^{-0.24} = 0.213$ and $P(X \ge 2) = 1 - e^{-0.24}(1 + 0.24) = 0.025$. Even 1,000 trios rarely show two new mutations in a 10 kb region: recurrent de novo hits in a small region are surprising under this null model, and worth a closer look.

> [!question] Exercise 2 (L1)
> Under the Lander-Waterman model, what coverage leaves at most 1 % of the genome uncovered? What coverage makes the expected number of uncovered bases of a 3.055 Gb genome smaller than 1?

> [!success]- Solution
> Uncovered fraction $e^{-c} \le 0.01 \iff c \ge \ln 100 \approx 4.61$. For the expected count: $G e^{-c} < 1 \iff c > \ln G = \ln(3.055 \times 10^9) \approx 21.8$. Coverage requirements grow only logarithmically with genome size, but real sequencing needs more because placement is not uniform.

> [!question] Exercise 3 (L2, Python)
> Using `poisson_pmf` and `poisson_cdf` from above, compute the total variation distance $\tfrac12 \sum_k |P(\mathrm{Bin}(n, 3/n) = k) - P(\mathrm{Pois}(3) = k)|$ for $n = 10, 100, 1000$. How fast does it shrink?

> [!success]- Solution
> ```python
> def binomial_pmf(k: int, n: int, p: float) -> float:
>     return math.comb(n, k) * p**k * (1 - p) ** (n - k)
>
> for n in (10, 100, 1000):
>     tv = 0.5 * sum(abs(binomial_pmf(k, n, 3 / n) - poisson_pmf(k, 3.0)) for k in range(n + 1))
>     tv += 0.5 * (1 - poisson_cdf(n, 3.0))      # Poisson mass above n, where the binomial has none
>     print(n, round(tv, 4))
> # 10 0.0864
> # 100 0.0076
> # 1000 0.0008
> ```
>
> Each tenfold increase of $n$ divides the distance by about ten: the error of the approximation is of order $1/n$ (more precisely of order $p$ for fixed $\lambda$). With $n$ in the billions (bases of a genome), the Poisson is exact for all practical purposes.

> [!question] Exercise 4 (L2)
> A bacterial genome of $G = 5$ Mb (round number) is sequenced with reads of $L = 150$ bp at $c = 10$. Two reads are joined if they overlap by at least 30 bp. Using the Lander-Waterman argument, how many reads are there, how many islands (contigs) do you expect, and how many uncovered bases? Redo it if any overlap could be detected.

> [!success]- Solution
> $N = cG/L = 10 \times 5 \times 10^6 / 150 \approx 333{,}333$ reads. $\theta = 30/150 = 0.2$, so the expected number of islands is $N e^{-c(1-\theta)} = 333{,}333 \times e^{-8} \approx 112$. With $\theta = 0$: $N e^{-10} \approx 15$. Uncovered bases: $G e^{-c} = 5 \times 10^6 \times e^{-10} \approx 227$. The overlap requirement matters more than one might think: requiring 20 % overlap multiplies the number of contigs by $e^{2} \approx 7.4$. These are best cases: repeats longer than the reads cannot be joined unambiguously, which the model ignores.

> [!question] Exercise 5 (L3, Python)
> In an invented model, a child whose father is $a$ years old carries $X \sim \mathrm{Pois}(70 + 2(a - 30))$ new mutations (the slope of 2 per year follows Kong et al.; the intercept is invented), and fathers' ages are uniform on $[20, 40]$. Derive $E[X]$ and $\operatorname{Var}(X)$, then check by simulation with `poisson_sample`.

> [!success]- Solution
> With $\Lambda = 70 + 2(a - 30)$: $E[\Lambda] = 70$ and $\operatorname{Var}(\Lambda) = 4\operatorname{Var}(a) = 4 \times 20^2/12 \approx 133.3$ (variance of a uniform, [[Uniform Distribution]]). By the law of total variance, $E[X] = 70$ and $\operatorname{Var}(X) = E[\Lambda] + \operatorname{Var}(\Lambda) \approx 203.3$.
>
> ```python
> rng = random.Random(7)
> counts = []
> for _ in range(50_000):
>     age = rng.uniform(20, 40)            # invented distribution of fathers' ages
>     lam = 70 + 2 * (age - 30)            # invented intercept, slope from Kong et al.
>     counts.append(poisson_sample(lam, rng))
> m = sum(counts) / len(counts)
> v = sum((x - m) ** 2 for x in counts) / (len(counts) - 1)
> print(f"mean {m:.1f}, variance {v:.1f}, variance/mean {v / m:.2f}")
> # mean 69.9, variance 202.9, variance/mean 2.90
> ```
>
> The variance is almost three times the mean: pooled over fathers of different ages, the counts are overdispersed although each child's count is exactly Poisson. Conditioning on the father's age (a covariate in a [[Poisson Regression]]) restores the Poisson structure.

## Mastery checklist

- [ ] 1 Recognized: I can write the Poisson pmf, state that mean and variance both equal $\lambda$, and name coverage and mutation counts as examples.
- [ ] 2 Understood: I can derive the Poisson as the limit of $\mathrm{Bin}(n, \lambda/n)$ and explain the four conditions that make a count Poisson.
- [ ] 3 Practiced: I can compute pmf and CDF values stably in Python, sample Poisson variates, and simulate read coverage to check $e^{-c}$.
- [ ] 4 Applied: on a real BAM file, I compare the depth distribution with $\mathrm{Pois}(c)$ and explain the departures ([[10-genomic-pipeline]]); I draw Poisson mutation counts per generation in [[07-evolution-simulator]].
- [ ] 5 Explained: I can teach the Lander-Waterman island formula, the difference between heterogeneity across sites and across units, and why overdispersion leads to the negative binomial.

## References

[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the Poisson distribution (definition, mean and variance, sums of independent Poissons, splitting, and the Poisson approximation and paradigm).
[^openstax]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 4 "Discrete Random Variables".
[^stat110]: [[Harvard Stat 110 - Probability]], named distributions (the Poisson).
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], treatment of discrete models and of count data from high-throughput sequencing (overdispersion, negative binomial).
[^lw]: [[Lander 1988 - Genomic Mapping by Fingerprinting Random Clones]], Lander ES, Waterman MS, *Genomics* 2(3):231-239.
[^kong]: [[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]], Kong A et al., *Nature* 488:471-475: rate of $1.20 \times 10^{-8}$ per nucleotide per generation and about two additional mutations per year of father's age.
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], Nurk S et al., *Science* 376:44-53: T2T-CHM13 genome of 3.055 Gbp.
