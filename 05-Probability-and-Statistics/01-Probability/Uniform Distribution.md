---
aliases:
  - Uniform Law
  - Discrete Uniform Distribution
  - Continuous Uniform Distribution
  - Unif(a, b)
  - Rectangular Distribution
  - Loi uniforme
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Random Variable]]"
  - "[[Probability Distribution]]"
  - "[[Cumulative Distribution Function]]"
  - "[[Probability Density Function]]"
related:
  - "[[P-Value]]"
  - "[[Multiple Testing Correction]]"
  - "[[False Discovery Rate]]"
  - "[[Family-Wise Error Rate]]"
  - "[[Random Number Generation]]"
  - "[[Random Variate Generation]]"
  - "[[Monte Carlo Method]]"
  - "[[Lander-Waterman Model]]"
  - "[[Sequencing Coverage]]"
  - "[[Exponential Distribution]]"
  - "[[Beta Distribution]]"
  - "[[Noninformative Prior]]"
projects:
  - "[[06-mutation-lab]]"
  - "[[07-evolution-simulator]]"
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Harvard Stat 110 - Probability]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[Modern Statistics for Modern Biology (Holmes)]]"
  - "[[Lander 1988 - Genomic Mapping by Fingerprinting Random Clones]]"
  - "[[Bayesian Data Analysis (Gelman)]]"
---

# Uniform Distribution

> [!abstract]
> The uniform distribution spreads probability evenly: each of $n$ values has probability $1/n$, or every stretch of the same length inside an interval has the same probability. It models "no position is special", such as a random read start along a genome, and it is the distribution of p-values when the null hypothesis is true.

## Definition

- **Discrete uniform** on a finite set $C$ of $n$ elements: $P(X = x) = 1/n$ for every $x \in C$, so $P(X \in A) = |A|/n$ for $A \subseteq C$.[^blitz][^stat110]
- **Continuous uniform** on $[a, b]$, written $X \sim \mathrm{Unif}(a, b)$ with $a < b$: density $f(x) = \frac{1}{b - a}$ for $a \le x \le b$ and $0$ elsewhere; CDF $F(x) = \frac{x - a}{b - a}$ on $[a, b]$, $0$ before $a$ and $1$ after $b$. Probability is proportional to length: $P(c \le X \le d) = \frac{d - c}{b - a}$ for $a \le c \le d \le b$.[^blitz5][^openstax5]
- **Summaries.** Continuous: $E[X] = \frac{a + b}{2}$ and $\operatorname{Var}(X) = \frac{(b - a)^2}{12}$. Discrete on $\{1, \dots, n\}$: $\frac{n + 1}{2}$ and $\frac{n^2 - 1}{12}$ (derived in [[#Mathematical representation]]).

## Why it matters

- **Null p-values.** For a test statistic with a continuous distribution, the p-value is $\mathrm{Unif}(0, 1)$ when the null hypothesis is true.[^blitz5] In a genome-wide screen the p-value histogram is therefore flat where null hypotheses dominate, with a spike near 0 from real effects; reading it is a basic check before any multiple-testing correction.[^holmes] See [[P-Value]], [[Multiple Testing Correction]], [[False Discovery Rate]].
- **Random positions.** The Lander-Waterman analysis of mapping by random clones, later applied to shotgun reads, places clones at random along the genome ([[Lander-Waterman Model]], [[Sequencing Coverage]]).[^lw] Intervals placed uniformly at random also give a null model for questions such as "do these peaks overlap promoters more than by chance?" ([[Permutation Test]], [[Genomic Interval Arithmetic]]).
- **Simulation.** Computers generate standard uniform numbers, and other distributions are obtained by transforming them, for instance through an inverse CDF ([[Random Number Generation]], [[Random Variate Generation]]).[^blitz5]
- **Uniform mutation models.** [[06-mutation-lab]] gives every point mutation the same probability: a discrete uniform over the $3L$ single-base changes of a sequence of length $L$.

## Core (L1)

### Discrete uniform: probability by counting

With $n$ equally likely values, a probability is a count divided by $n$, the naive definition of [[Probability Space]]. Under the uniform random-sequence model: a base has probability $1/4$, a codon $1/64$, a k-mer $4^{-k}$, a position in a sequence of length $L$ $1/L$.

**Bio: a random point mutation.** In the uniform model of [[06-mutation-lab]], each of the 9 single-base changes of a codon is equally likely. For the tryptophan codon TGG they are AGG, CGG, GGG (first position), TAG, TCG, TTG (second) and TGA, TGC, TGT (third). TAG and TGA are stop codons ([[Genetic Code]]), so $P(\text{nonsense}) = 2/9$; none is silent, since TGG is the only tryptophan codon. Every change of the methionine codon ATG, by contrast, is missense.

### Continuous uniform: probability is length

The density is flat at height $1/(b - a)$, so a sub-interval's probability is its length divided by the total length. If a read starts at a uniformly random position of a chromosome of length $L$, the probability that it starts in a given window of width $w$ is $w/L$, wherever the window lies. Positions are integers; treating them as real numbers is an approximation that is harmless when $L$ is large. The height $1/(b - a)$ exceeds 1 when $b - a < 1$: it is a density, not a probability ([[Probability Density Function]]). The **standard uniform** $U \sim \mathrm{Unif}(0, 1)$ has $F(u) = u$ for $0 \le u \le 1$.[^openstax5]

### p-values are uniform under the null hypothesis

Let $T$ be a test statistic whose null distribution has a continuous CDF $F$, with upper-tail p-value $p = 1 - F(T)$. Under the null hypothesis $F(T) \sim \mathrm{Unif}(0, 1)$ (the probability integral transform, [[Cumulative Distribution Function#Advanced (L3)]]),[^blitz5] hence so is $p$, and

$$P(p \le \alpha) = \alpha \quad \text{for every } \alpha \in [0, 1].$$

At $\alpha = 0.05$, 5 % of the true null hypotheses are rejected whatever the test: 10,000 null genes give about 500 false positives. The p-value histogram of a screen mixes a flat part (the nulls) with mass concentrated near 0 (the real effects):

![[p-value-histogram-null-uniform.svg]]

## Deeper (L2)

### Location, scale and symmetry

If $U \sim \mathrm{Unif}(0, 1)$, then $a + (b - a)U \sim \mathrm{Unif}(a, b)$ and $1 - U \sim \mathrm{Unif}(0, 1)$ (Exercise 3). The second fact is why lower-tail and upper-tail p-values are both uniform under the null. For read starts on $[0, L]$, the mean is $L/2$ and the standard deviation $L/\sqrt{12} \approx 0.29\,L$ ([[Expected Value]], [[Variance]]).

### Universality of the uniform

If $F$ is a continuous, strictly increasing CDF and $U \sim \mathrm{Unif}(0, 1)$, then $X = F^{-1}(U)$ has CDF $F$; conversely, if $X$ has CDF $F$, then $F(X) \sim \mathrm{Unif}(0, 1)$.[^blitz5] A single uniform generator thus produces any distribution whose CDF can be inverted. The exponential CDF $F(x) = 1 - e^{-\lambda x}$ inverts to $X = -\ln(1 - U)/\lambda$ ([[Exponential Distribution]]), checked in the code below. The discrete version is in [[Cumulative Distribution Function#Deeper (L2)]].

### Two-step sampling must weight the first step

Choosing a chromosome uniformly and then a uniform position on it does **not** give a uniform position in the genome: bases of short chromosomes are oversampled. Choosing the chromosome with probability proportional to its length does, since $\frac{L_c}{L_{\text{total}}} \cdot \frac{1}{L_c} = \frac{1}{L_{\text{total}}}$ for every base, by the [[Law of Total Probability]] (Exercise 4).

## Advanced (L3)

- **Reading a p-value histogram.** A spike near 0 over a flat floor is the expected shape for a screen with real effects, and the height of the floor estimates the fraction $\pi_0$ of null hypotheses: p-values above $\lambda$ come almost only from nulls, so $\#\{p_i > \lambda\} \approx \pi_0\, n\, (1 - \lambda)$ (code below). A floor that is not flat means the null p-values are not uniform: discrete statistics give conservative p-values that pile up near 1 ([[Cumulative Distribution Function#Advanced (L3)]]), and a wrong null model shifts mass in either direction. The shape should be understood before a [[False Discovery Rate]] procedure is applied.[^holmes]
- **The smallest p-value of a screen.** For $n$ independent null p-values, $P(\min_i p_i \le t) = 1 - (1 - t)^n$ and $E[\min_i p_i] = 1/(n + 1)$. The threshold $t = 0.05/n$ keeps the probability of any false positive near $1 - e^{-0.05} \approx 0.049$: the Bonferroni correction ([[Family-Wise Error Rate]], [[#Worked example]]). More generally, the $k$-th smallest of $n$ independent standard uniforms follows a [[Beta Distribution]] with mean $k/(n + 1)$,[^blitz] the expected positions against which the sorted p-values of a screen are compared in a [[Q-Q Plot]].
- **No uniform distribution on an unbounded set.** A constant density on $\mathbb{R}$ integrates to 0 or $\infty$, never 1, and equal masses on the integers cannot sum to 1 under countable additivity. "A random integer" is therefore not a distribution, and a flat prior on an unbounded parameter is **improper**: it can still be used when the resulting posterior is a proper distribution, which must be checked ([[Noninformative Prior]]).[^gelman]
- **Reproducible uniforms.** Python's generator, like those of the simulations in these notes, is deterministic given its seed: rerunning a seeded simulation reproduces the same uniforms and therefore the same results ([[Random Number Generation]]).

## Mathematical representation

- **Discrete** on $\{1, \dots, n\}$: $E[X] = \frac{1}{n}\sum_{k=1}^{n} k = \frac{n + 1}{2}$, $E[X^2] = \frac{1}{n}\sum_{k=1}^{n} k^2 = \frac{(n + 1)(2n + 1)}{6}$, so $\operatorname{Var}(X) = \frac{(n + 1)(2n + 1)}{6} - \frac{(n + 1)^2}{4} = \frac{n^2 - 1}{12}$.
- **Continuous** on $[a, b]$: $E[X] = \int_a^b \frac{x\,dx}{b - a} = \frac{a + b}{2}$, $E[X^2] = \frac{a^2 + ab + b^2}{3}$, so $\operatorname{Var}(X) = \frac{a^2 + ab + b^2}{3} - \frac{(a + b)^2}{4} = \frac{(b - a)^2}{12}$.
- **Linear map.** For $Y = a + (b - a)U$: $F_Y(y) = P\big(U \le \frac{y - a}{b - a}\big) = \frac{y - a}{b - a}$ on $[a, b]$.
- **Universality.** $P(F^{-1}(U) \le x) = P(U \le F(x)) = F(x)$. For continuous, strictly increasing $F$: $P(F(X) \le u) = P(X \le F^{-1}(u)) = F(F^{-1}(u)) = u$.
- **Null p-values.** With $p = 1 - F(T)$ and $F$ continuous: $P(p \le \alpha) = P(F(T) \ge 1 - \alpha) = \alpha$.
- **Minimum of $n$ independent uniforms.** $P(\min_i U_i > t) = \prod_i P(U_i > t) = (1 - t)^n$, and for a non-negative variable $E[M] = \int_0^\infty P(M > t)\,dt$, so $E[\min_i U_i] = \int_0^1 (1 - t)^n\,dt = \frac{1}{n + 1}$.

## Computational representation

`random.uniform(a, b)` and `random.random()` return uniform draws; a seeded `random.Random` makes them reproducible. The script checks the continuous uniform on read starts, simulates p-values of z-tests ([[Normal Distribution]]) under the null and under a mixture, and turns uniforms into exponential draws.

```python
import math
import random

rng = random.Random(2024)

# 1. Continuous uniform: read starts on a chromosome of length L (invented), as real numbers
L = 1_000_000
starts = [rng.uniform(0, L) for _ in range(100_000)]
in_window = sum(250_000 <= s < 260_000 for s in starts) / len(starts)
mean = sum(starts) / len(starts)
sd = (sum((s - mean) ** 2 for s in starts) / (len(starts) - 1)) ** 0.5
print(f"P(start in a 10 kb window): simulated {in_window:.4f}, exact {10_000 / L:.4f}")
print(f"mean {mean:,.0f} (exact {L / 2:,.0f}), sd {sd:,.0f} (exact L/sqrt(12) = {L / math.sqrt(12):,.0f})")

# 2. p-values of z-tests: 9,000 null genes (z ~ N(0, 1)), 1,000 with a true shift of 3 (invented)
def two_sided_p(z: float) -> float:
    """P(|Z| >= |z|) for a standard normal Z."""
    return math.erfc(abs(z) / math.sqrt(2))

null_p = [two_sided_p(rng.gauss(0, 1)) for _ in range(9_000)]
alt_p = [two_sided_p(rng.gauss(3, 1)) for _ in range(1_000)]
for name, ps in (("null only", null_p), ("null + alternative", null_p + alt_p)):
    bins = [0] * 10
    for p in ps:
        bins[min(int(p * 10), 9)] += 1
    print(f"{name:19s}", " ".join(f"{b / len(ps):.3f}" for b in bins))

ps = null_p + alt_p
lam = 0.5
pi0_hat = sum(p > lam for p in ps) / (len(ps) * (1 - lam))
print(f"estimated null fraction = {pi0_hat:.3f} (true 0.9); p <= 0.05: "
      f"{sum(p <= 0.05 for p in ps)} genes, of which {sum(p <= 0.05 for p in null_p)} null")

# 3. Universality of the uniform: X = -ln(1 - U) / rate is exponential with mean 1 / rate
rate = 0.2                                # e.g. a waiting distance of 0.2 events per kb (invented)
xs = [-math.log(1 - rng.random()) / rate for _ in range(100_000)]
print(f"inverse transform: mean {sum(xs) / len(xs):.3f} (exact {1 / rate}), "
      f"P(X > 10) {sum(x > 10 for x in xs) / len(xs):.4f} (exact {math.exp(-rate * 10):.4f})")
```

```text
P(start in a 10 kb window): simulated 0.0103, exact 0.0100
mean 499,776 (exact 500,000), sd 289,314 (exact L/sqrt(12) = 288,675)
null only           0.102 0.100 0.098 0.104 0.103 0.101 0.096 0.101 0.097 0.098
null + alternative  0.183 0.094 0.090 0.094 0.093 0.091 0.087 0.091 0.087 0.089
estimated null fraction = 0.890 (true 0.9); p <= 0.05: 1300 genes, of which 461 null
inverse transform: mean 5.004 (exact 5.0), P(X > 10) 0.1348 (exact 0.1353)
```

The null p-values fill the ten bins evenly; the 1,000 real effects lift the first bin to 0.183 over a floor near 0.09, and the floor gives $\hat\pi_0 = 0.890$. Of the 1,300 genes with $p \le 0.05$, 461 are null (expected $0.05 \times 9{,}000 = 450$): 35 % of these "discoveries" are false, as [[Bayes' Theorem#Advanced (L3)]] predicts from $\pi_0$. The figure above shows the same simulation with 20 bins.

## Worked example

> [!example] A screen in which nothing happens
> 20,000 genes are tested and, unknown to the analyst, none is differentially expressed (invented scenario). The tests are independent with continuous statistics, so the 20,000 p-values are i.i.d. $\mathrm{Unif}(0, 1)$.
>
> 1. **False positives at 0.05.** Each gene has $P(p \le 0.05) = 0.05$, so about $20{,}000 \times 0.05 = 1{,}000$ genes are "significant", all of them false ([[Expected Value]]).
> 2. **At least one.** $P(\min_i p_i \le 0.05) = 1 - 0.95^{20{,}000}$, which is 1 to machine precision.
> 3. **Bonferroni threshold.** With $t = 0.05/20{,}000 = 2.5 \times 10^{-6}$: $P(\min_i p_i \le t) = 1 - (1 - 2.5 \times 10^{-6})^{20{,}000} \approx 1 - e^{-0.05} = 0.0488$.
> 4. **Histogram.** With 20 bins of width 0.05, each bin expects 1,000 p-values: the flat panel A of the figure is what "no signal" looks like.
> 5. **Interpretation.** The uniform law of null p-values tells exactly how many small p-values chance alone produces; every multiple-testing procedure is built on it ([[Multiple Testing Correction]]).

## Common misconceptions

> [!warning] "Under the null hypothesis, p-values tend to be large"
> They are uniform: a null gene is as likely to give $p \in [0, 0.1]$ as $p \in [0.9, 1]$. A p-value of 0.6 is no "more null" than one of 0.3, and 5 % of null genes fall below 0.05.

> [!warning] "Uniformly random positions are evenly spread"
> Uniform means that every position is equally likely, not that positions are equally spaced. Random read starts cluster in places and leave gaps elsewhere, so coverage varies even under the ideal model ([[Poisson Distribution]], [[Lander-Waterman Model]]).

> [!warning] "A random chromosome, then a random position, is a random position in the genome"
> Only if the chromosome is drawn with probability proportional to its length (Exercise 4). The same mistake appears when drawing a random gene and then a random base within it.

> [!warning] "A density of 5 cannot be right"
> $\mathrm{Unif}(0, 0.2)$ has density 5 on its support. A density is probability per unit length; only its area must equal 1 ([[Probability Density Function]]).

## Exercises

> [!question] Exercise 1 (L1)
> Under the uniform point-mutation model, a random single-base change hits the tyrosine codon TAC. Using the standard [[Genetic Code]], compute the probability that the change is silent, nonsense or missense.

> [!success]- Solution
> The 9 changes: AAC (Asn), CAC (His), GAC (Asp); TCC (Ser), TGC (Cys), TTC (Phe); TAA (stop), TAG (stop), TAT (Tyr). Silent $1/9$, nonsense $2/9$, missense $6/9$. All three third-position changes are stops or silent, while TGG has no silent change and ATG only missense ones: the class probabilities depend on the codon, which is why [[06-mutation-lab]] computes them codon by codon.

> [!question] Exercise 2 (L1)
> A read starts at a uniformly random position of a circular chromosome of 5 Mb (invented). What is the probability that it starts in a given 2 kb gene? Among $10^6$ independent reads, how many starts are expected in the gene? Give the mean and standard deviation of the start position, measured from an arbitrary origin.

> [!success]- Solution
> $P = 2{,}000/5{,}000{,}000 = 4 \times 10^{-4}$, the same for every 2 kb window (a circle has no ends). Expected starts: $10^6 \times 4 \times 10^{-4} = 400$ ([[Expected Value]]). Mean $2.5$ Mb, standard deviation $5/\sqrt{12} = 1.44$ Mb.

> [!question] Exercise 3 (L2)
> Let $U \sim \mathrm{Unif}(0, 1)$. Using CDFs, show that $1 - U \sim \mathrm{Unif}(0, 1)$ and $a + (b - a)U \sim \mathrm{Unif}(a, b)$. Deduce that a lower-tail p-value $F(T)$ and an upper-tail p-value $1 - F(T)$ are both uniform under the null, for a continuous $F$.

> [!success]- Solution
> For $0 \le u \le 1$: $P(1 - U \le u) = P(U \ge 1 - u) = 1 - (1 - u) = u$. For $a \le y \le b$: $P(a + (b - a)U \le y) = P\big(U \le \frac{y - a}{b - a}\big) = \frac{y - a}{b - a}$, the CDF of $\mathrm{Unif}(a, b)$. Under the null, $F(T)$ is uniform by the probability integral transform, and $1 - F(T)$ is uniform by the first identity.

> [!question] Exercise 4 (L2, Python)
> An invented genome has chromosomes of 5, 3 and 2 Mb. Sample 60,000 positions by (a) choosing a chromosome uniformly, then a uniform position on it; (b) choosing the chromosome with probability proportional to its length. Compare the fraction of positions per chromosome with the uniform target.

> [!success]- Solution
> ```python
> import random
> from collections import Counter
>
> CHROMS = {"chr1": 5_000_000, "chr2": 3_000_000, "chr3": 2_000_000}   # invented 10 Mb genome
> TOTAL = sum(CHROMS.values())
>
> def random_position(rng: random.Random, weighted: bool) -> tuple[str, int]:
>     """Pick a chromosome (uniformly, or with probability proportional to its length),
>     then a uniform 0-based position on it."""
>     names = list(CHROMS)
>     if weighted:
>         name = rng.choices(names, weights=[CHROMS[c] for c in names])[0]
>     else:
>         name = rng.choice(names)
>     return name, rng.randrange(CHROMS[name])
>
> rng = random.Random(7)
> n = 60_000
> print("target  ", {c: CHROMS[c] / TOTAL for c in CHROMS})
> for weighted in (False, True):
>     counts = Counter(random_position(rng, weighted)[0] for _ in range(n))
>     print("weighted" if weighted else "naive   ", {c: round(counts[c] / n, 3) for c in CHROMS})
> ```
>
> ```text
> target   {'chr1': 0.5, 'chr2': 0.3, 'chr3': 0.2}
> naive    {'chr1': 0.334, 'chr2': 0.333, 'chr3': 0.333}
> weighted {'chr1': 0.504, 'chr2': 0.297, 'chr3': 0.199}
> ```
>
> The naive scheme gives each base of chr3 probability $\frac13 \cdot \frac{1}{2 \times 10^6}$, 1.7 times the uniform $10^{-7}$, and each base of chr1 only $0.67 \times 10^{-7}$. Weighting by length makes every base's probability $\frac{L_c}{L_{\text{total}}} \cdot \frac{1}{L_c} = 10^{-7}$.

> [!question] Exercise 5 (L3, Python)
> Simulate 2,000 screens of 1,000 independent null tests (seed 5). Estimate $P(\min p \le 0.05)$, $P(\min p \le 0.05/1000)$ and $E[\min p]$, and compare with $1 - (1 - t)^n$ and $1/(n + 1)$.

> [!success]- Solution
> ```python
> import random
>
> rng = random.Random(5)
> n_tests, screens = 1_000, 2_000
> alpha = 0.05
> minima = [min(rng.random() for _ in range(n_tests)) for _ in range(screens)]   # null p-values ~ U(0, 1)
> for t in (alpha, alpha / n_tests):
>     exact = 1 - (1 - t) ** n_tests
>     sim = sum(m <= t for m in minima) / screens
>     print(f"P(min p <= {t:g}): exact {exact:.4f}, simulated {sim:.4f}")
> print(f"mean of min p: simulated {sum(minima) / screens:.6f}, exact 1/(n+1) = {1 / (n_tests + 1):.6f}")
> ```
>
> ```text
> P(min p <= 0.05): exact 1.0000, simulated 1.0000
> P(min p <= 5e-05): exact 0.0488, simulated 0.0475
> mean of min p: simulated 0.001001, exact 1/(n+1) = 0.000999
> ```
>
> Without correction, every screen has a false positive. The Bonferroni threshold brings the probability down to 0.049 (simulated 0.0475, standard error 0.005). The smallest of 1,000 null p-values is about 0.001 on average: a p-value of 0.001 among 1,000 tests is exactly what chance predicts.

## Mastery checklist

- [ ] 1 Recognized: I can write the PMF of a discrete uniform and the density and CDF of $\mathrm{Unif}(a, b)$, and state that null p-values are uniform.
- [ ] 2 Understood: I can explain why probability is proportional to length, why a uniform density can exceed 1 and why continuous null p-values are uniform.
- [ ] 3 Practiced: I can derive the mean and variance, sample uniform genome positions correctly, transform uniforms into other distributions and simulate p-value histograms with a seed in Python.
- [ ] 4 Applied: I read the p-value histogram of a real screen before correcting for multiple testing, and I implement the uniform point-mutation model of [[06-mutation-lab]].
- [ ] 5 Explained: I can teach the probability integral transform, the law of the smallest p-value and Bonferroni, why discrete p-values are not uniform, and why there is no uniform distribution on an unbounded set.

## References

[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the discrete uniform distribution and of order statistics of uniforms (Beta distributions).
[^blitz5]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 5 "Continuous Random Variables" (the uniform distribution, universality of the uniform, generating uniforms by computer).
[^stat110]: [[Harvard Stat 110 - Probability]], random variables and the named distributions.
[^openstax5]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 5 "Continuous Random Variables" (the uniform distribution).
[^holmes]: [[Modern Statistics for Modern Biology (Holmes)]], treatment of multiple testing (the p-value histogram).
[^lw]: [[Lander 1988 - Genomic Mapping by Fingerprinting Random Clones]], Lander ES, Waterman MS, *Genomics* 2(3):231-239: clones placed at random along the genome.
[^gelman]: [[Bayesian Data Analysis (Gelman)]], 3rd ed., treatment of noninformative and improper prior distributions.
