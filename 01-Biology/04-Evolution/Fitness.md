---
aliases:
  - Darwinian Fitness
  - Relative Fitness
  - Absolute Fitness
  - Selection Coefficient
  - Valeur sélective
  - Fitness darwinienne
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Natural Selection]]"
  - "[[Allele]]"
  - "[[Genotype]]"
  - "[[Logarithm]]"
related:
  - "[[Adaptation]]"
  - "[[Allele Frequency]]"
  - "[[Hardy-Weinberg Equilibrium]]"
  - "[[Genetic Drift]]"
  - "[[Fixation Probability]]"
  - "[[Mutation-Selection Balance]]"
  - "[[Balancing Selection]]"
  - "[[Epistasis]]"
  - "[[Experimental Evolution]]"
  - "[[Linear Regression]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[bio-simulation]]"
sources:
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Evolution (Futuyma)]]"
  - "[[Biology 2e (OpenStax)]]"
---

# Fitness

> [!abstract]
> Fitness measures how many offspring a type leaves compared with the other types in the same population; a selection coefficient of 0.05 means 5 % more offspring per generation, an edge that compounds over generations.

## Definition

The **absolute fitness** $W$ of a genotype is the expected number of offspring that an individual of that genotype contributes to the next generation, combining survival to reproductive age and fecundity. Its **relative fitness** $w$ is its absolute fitness divided by that of a reference genotype, often the fittest one. The **selection coefficient** $s$ measures the difference from the reference: $w = 1 + s$ for an advantaged genotype, or $w = 1 - s$ for a disadvantaged one.[^hartl][^griffiths][^os19]

## Why it matters

- **Model parameters.** Every selection model in [[07-evolution-simulator]] is specified by one fitness value per genotype; $s$ is the number a user sets.
- **Measuring fitness from reads.** When the frequencies of competing variants are measured from sequencing read counts at several time points ([[Experimental Evolution]]), the slope of their log-odds over generations estimates $s$ (derived below, with code).
- **Variant interpretation.** Whether a variant is deleterious, neutral or beneficial is a statement about its fitness effect; conservation-based predictors infer it indirectly from what selection has removed ([[Purifying Selection]], [[Variant Annotation]]).
- **Selection versus chance.** Whether a given $s$ matters depends on population size ([[Genetic Drift]], [[Fixation Probability]]).

## Core (L1)

**Reproductive success, not strength.** Survival counts only as far as it leads to reproduction: a strong, long-lived individual that leaves no offspring has fitness zero.[^futuyma]

**Relative, not absolute.** What changes allele frequencies is how a type reproduces compared with the others in the same population and environment. An invented example:

| Genotype | Mean offspring $W$ | $w$ relative to $a$ | $w$ relative to the fittest |
|---|---:|---:|---:|
| $A$ | 2.4 | 1.2 ($s = 0.2$ in favour of $A$) | 1 |
| $a$ | 2.0 | 1 | 0.833 ($s = 0.167$ against $a$) |

Both normalizations describe the same dynamics, because only the ratio $W_A / W_a = 1.2$ enters the recursion (Deeper).

**Fitness belongs to a genotype in an environment.** In polluted woods with soot-darkened bark, dark peppered moths survived bird predation better than light ones; on clean, lichen-covered bark the advantage reverses.[^os19] The same genotype has different fitnesses in different environments.

## Deeper (L2)

### Components

Absolute fitness is a product of components: the probability of surviving to reproductive age (viability), mating success and the number of offspring produced (fecundity).[^hartl][^futuyma] Selection can act on any of them.

### Diploid genotypes and dominance

For a locus with alleles $A$ (frequency $p$) and $a$ (frequency $q$), the standard parameterization of selection against $a$ is:[^hartl]

| Genotype | $AA$ | $Aa$ | $aa$ |
|---|---:|---:|---:|
| Relative fitness | $1$ | $1 - hs$ | $1 - s$ |

The **dominance coefficient** $h$ places the heterozygote: $h = 0$, $a$ is recessive (harmful only in $aa$); $h = 1/2$, effects are additive; $h = 1$, $a$ is dominant. With genotypes in [[Hardy-Weinberg Equilibrium|Hardy-Weinberg]] proportions before selection, the mean fitness and the allele frequency after selection are[^hartl]

$$\bar w = p^2 + 2pq(1 - hs) + q^2(1 - s), \qquad q' = \frac{q\,[\,p(1 - hs) + q(1 - s)\,]}{\bar w}.$$

The bracket is the **marginal fitness** of allele $a$: the average fitness of the genotypes it sits in. A rare recessive allele sits almost only in heterozygotes, where it is invisible to selection, so it declines very slowly; this is one reason harmful recessive alleles persist ([[Mutation-Selection Balance]]).

### Only ratios matter

In the haploid model $p' = p W_A / (p W_A + q W_a)$. Dividing $W_A$ and $W_a$ by any constant leaves $p'$ unchanged, so $p'/q' = (W_A/W_a)(p/q)$. Two consequences: the choice of reference genotype is a convention, and a type can increase in frequency while its numbers fall, if the other type falls faster (Exercise 5).

### Log-odds grow linearly

Iterating the haploid recursion ([[Natural Selection#Deeper (L2)]]) gives

$$\ln\frac{p_t}{q_t} = \ln\frac{p_0}{q_0} + t\,\ln(1+s).$$

The log-odds of $A$ are a straight line in $t$ with slope $\ln(1+s)$. Estimating $s$ is therefore a [[Linear Regression]] of observed log-odds on time, and two time points suffice for a rough estimate.

## Advanced (L3)

**Fitness is not a constant.** It depends on the environment (the moth example), on the genetic background, where the effect of an allele depends on alleles at other loci ([[Epistasis]], fitness landscapes),[^futuyma] and on the composition of the population: under frequency-dependent selection a type's fitness changes with its own frequency.[^os19] Then no single $s$ describes the dynamics, and variation can be maintained ([[Balancing Selection]]).

**Mean fitness.** With constant fitnesses at one haploid locus, $\bar w_t = 1 + s p_t$ and $p_t$ moves in the direction of $s$, so $\bar w$ never decreases (Exercise 6). This is a property of constant fitnesses, not a law: with frequency dependence, selection can lower mean fitness ([[Adaptation#Advanced (L3)]]).

**Distribution of fitness effects.** Among new mutations that affect fitness, deleterious ones are much more common than beneficial ones.[^futuyma] Whether a small $s$ is "seen" by selection depends on its size relative to $1/N$ ([[Natural Selection#Advanced (L3)]], [[Fixation Probability]]).

**Continuous time.** If two types grow exponentially at rates $r_A$ and $r_a$ per generation (Malthusian parameters), $W = e^{r}$ and the log-odds grow at rate $r_A - r_a$; hence $\ln(1+s) = r_A - r_a$, and $s \approx r_A - r_a$ when the difference is small.

## Mathematical representation

| Symbol | Meaning |
|---|---|
| $W_g$ | absolute fitness of genotype $g$: expected number of offspring |
| $w_g = W_g / W_{\text{ref}}$ | relative fitness |
| $s$ | selection coefficient: $w = 1 \pm s$ |
| $h$ | dominance coefficient of the heterozygote |
| $\bar w = \sum_g f_g w_g$ | mean fitness, $f_g$ the genotype frequencies |

**Estimator of $s$ (haploid).** From frequencies $p_0$ and $p_t$ at generations 0 and $t$:

$$\hat s = \exp\!\left(\frac{\operatorname{logit}(p_t) - \operatorname{logit}(p_0)}{t}\right) - 1, \qquad \operatorname{logit}(p) = \ln\frac{p}{1-p}.$$

With $k$ time points $(t_i, y_i)$, $y_i = \operatorname{logit}(\hat p_{t_i})$, the least-squares slope is $b = \sum (t_i - \bar t)(y_i - \bar y) / \sum (t_i - \bar t)^2$ and $\hat s = e^{b} - 1$. Frequencies estimated from read counts $k_i$ out of $n_i$ reads give $y_i = \ln\frac{k_i}{n_i - k_i}$.

## Computational representation

Fitness values are a dictionary keyed by genotype; frequencies are floats; estimation uses log-odds. The read counts below are simulated with known $s$ to check the estimator (invented parameters).

```python
import math
import random

# 1. Absolute -> relative fitness (invented mean offspring numbers)
W = {"A": 2.4, "a": 2.0}
w_vs_a = {g: W[g] / W["a"] for g in W}            # reference = a
w_vs_max = {g: W[g] / max(W.values()) for g in W}  # reference = the fittest
print(w_vs_a, "s =", round(w_vs_a["A"] - 1, 3))
print({g: round(v, 3) for g, v in w_vs_max.items()}, "s =", round(1 - w_vs_max["a"], 3))

# 2. Diploid viability selection against allele a: w_AA = 1, w_Aa = 1 - h*s, w_aa = 1 - s
def diploid_step(q: float, s: float, h: float) -> tuple[float, float]:
    p = 1 - q
    w_AA, w_Aa, w_aa = 1, 1 - h * s, 1 - s
    w_bar = p * p * w_AA + 2 * p * q * w_Aa + q * q * w_aa
    q_next = q * (p * w_Aa + q * w_aa) / w_bar      # marginal fitness of a, over w_bar
    return q_next, w_bar

for h in (0, 0.5, 1):
    q_next, w_bar = diploid_step(0.1, 0.2, h)
    print(f"h={h}: w_bar={w_bar:.4f}  q: 0.1 -> {q_next:.4f}")

# 3. Estimating s from allele counts in sequencing reads (simulated, invented parameters)
random.seed(7)
s_true, p0, depth = 0.05, 0.1, 2000
gens = [0, 5, 10, 15, 20, 25, 30]
logits = []
for t in gens:
    odds = p0 / (1 - p0) * (1 + s_true) ** t           # exact haploid dynamics
    p = odds / (1 + odds)
    k = sum(random.random() < p for _ in range(depth))  # reads carrying A
    logits.append(math.log(k / (depth - k)))
mt, ml = sum(gens) / len(gens), sum(logits) / len(logits)
slope = sum((t - mt) * (y - ml) for t, y in zip(gens, logits)) / sum((t - mt) ** 2 for t in gens)
print("logits", [round(y, 3) for y in logits])
print(f"slope={slope:.4f}  s_hat={math.exp(slope) - 1:.4f}  (true s={s_true})")
```

Output:

```text
{'A': 1.2, 'a': 1.0} s = 0.2
{'A': 1.0, 'a': 0.833} s = 0.167
h=0: w_bar=0.9980  q: 0.1 -> 0.0982
h=0.5: w_bar=0.9800  q: 0.1 -> 0.0908
h=1: w_bar=0.9620  q: 0.1 -> 0.0832
logits [-2.132, -1.946, -1.723, -1.437, -1.313, -0.922, -0.659]
slope=0.0491  s_hat=0.0504  (true s=0.05)
```

The recessive case ($h = 0$) barely moves $q$ in one generation, the dominant case most. Sampling 2,000 reads per time point adds noise to each log-odds value, but the regression recovers $s$ within 1 %.

## Worked example

> [!example] Relative fitness from a competition experiment (invented counts)
> Two strains, $A$ and $a$, are mixed and propagated for 12 generations. Sequencing reads at the start: 150 of 1,000 carry $A$; after 12 generations: 420 of 1,000.
>
> 1. **Log-odds at the start**: $\ln(150/850) = -1.7346$.
> 2. **Log-odds at the end**: $\ln(420/580) = -0.3228$.
> 3. **Slope**: $(-0.3228 + 1.7346)/12 = 0.11765$ per generation.
> 4. **Selection coefficient**: $\hat s = e^{0.11765} - 1 = 0.1249$.
> 5. **Reading**: under these conditions $A$ leaves about 12.5 % more offspring per generation than $a$, whatever the absolute growth of the culture. The estimate assumes a constant $s$; plotting log-odds at intermediate time points checks that the line is straight.

## Common misconceptions

> [!warning] "Fitness means strength, health or longevity"
> Fitness is reproductive success. Longevity matters only through the offspring it allows.[^futuyma]

> [!warning] "A genotype has one fitness value"
> Fitness depends on the environment, on the genetic background and sometimes on the frequency of the genotype itself.[^os19][^futuyma] Report the conditions with every estimate of $s$.

> [!warning] "A type whose numbers fall is being selected against"
> Selection is relative. If both types decline but $a$ declines faster, $A$ increases in frequency and has $s > 0$ (Exercise 5).

> [!warning] "An advantage of 1 % is negligible"
> It compounds: from 1 % to 99 % in about 924 generations at $s = 0.01$, a short time for microbes and a modest one on evolutionary time scales ([[Natural Selection]]).

## Exercises

> [!question] Exercise 1 (L1)
> Genotype $B_1$ leaves on average 3.0 surviving offspring, $B_2$ 2.7 (invented). Give the relative fitnesses and $s$ with $B_1$ as reference, then with $B_2$ as reference.

> [!success]- Solution
> Reference $B_1$: $w_{B_1} = 1$, $w_{B_2} = 2.7/3.0 = 0.9$, so $s = 0.1$ against $B_2$. Reference $B_2$: $w_{B_1} = 3.0/2.7 = 1.111$, so $s = 0.111$ in favour of $B_1$. Same ratio, same dynamics; always state the convention.

> [!question] Exercise 2 (L1)
> A mule is strong and lives long. What is its fitness?

> [!success]- Solution
> Zero: mules are sterile hybrids of a horse and a donkey,[^os18] so they leave no offspring. Strength and lifespan do not enter fitness except through reproduction.

> [!question] Exercise 3 (L2)
> With $s = 0.2$, $h = 0.5$ and $q = 0.1$, compute $\bar w$ and $q'$ by hand.

> [!success]- Solution
> $\bar w = 0.81 \times 1 + 2 \times 0.09 \times 0.9 + 0.01 \times 0.8 = 0.81 + 0.162 + 0.008 = 0.98$. Marginal fitness of $a$: $0.9 \times 0.9 + 0.1 \times 0.8 = 0.89$. $q' = 0.1 \times 0.89 / 0.98 = 0.0908$, as in the code output.

> [!question] Exercise 4 (L2, Python)
> Using `logits` and `gens` from the code, estimate $s$ from the first and last time points only, and compare with the regression estimate.

> [!success]- Solution
> ```python
> print(round(math.exp((logits[-1] - logits[0]) / (gens[-1] - gens[0])) - 1, 4))   # 0.0503
> ```
>
> Here the two-point estimate (0.0503) is close to the regression (0.0504) because these endpoints happen to lie near the line. In general the two-point estimate uses only two noisy measurements and is more variable; the regression averages the noise of all time points and lets you check for curvature, a sign that $s$ is not constant.

> [!question] Exercise 5 (L3)
> In one generation, strain $A$ goes from 1,000 to 800 cells and strain $a$ from 1,000 to 500 (invented). Compute $W_A$, $W_a$, $s$ and the new frequency of $A$.

> [!success]- Solution
> $W_A = 0.8$, $W_a = 0.5$: both decline. $w_A / w_a = 1.6$, so $s = 0.6$ in favour of $A$, and $p' = 800/1300 = 0.615$ (from 0.5). Selection is about relative success; whether the population as a whole survives is a separate, demographic question.

> [!question] Exercise 6 (L3)
> Show that in the haploid model with constant $s$, mean fitness never decreases from one generation to the next.

> [!success]- Solution
> $\bar w_t = p_t(1+s) + q_t = 1 + s p_t$, so $\bar w_{t+1} - \bar w_t = s\,(p_{t+1} - p_t) = s \cdot \frac{s p_t q_t}{1 + s p_t} = \frac{s^2 p_t q_t}{\bar w_t} \ge 0$, with equality only if $s = 0$ or one allele is fixed. The increase is proportional to the variance in fitness, $s^2 p_t q_t$: selection improves mean fitness only as fast as there is variation to select on.

## Mastery checklist

- [ ] 1 Recognized: I can define absolute fitness, relative fitness and the selection coefficient.
- [ ] 2 Understood: I can explain why fitness is relative, environment-dependent and not the same as survival.
- [ ] 3 Practiced: I can compute $\bar w$ and $q'$ with dominance, and estimate $s$ from frequency data in Python.
- [ ] 4 Applied: in [[07-evolution-simulator]], I parameterize genotypes by $s$ and $h$ and recover $s$ from simulated read counts.
- [ ] 5 Explained: I can teach why only fitness ratios matter, when mean fitness increases, and why frequency dependence breaks the picture.

## References

[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed. (2006), treatment of natural selection (relative fitness, selection and dominance coefficients, one-locus selection models).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), population genetics (Darwinian fitness and selection).
[^futuyma]: [[Evolution (Futuyma)]], 5th ed. (2023), natural selection, fitness and its components, and the effects of mutations on fitness (chapter numbers not verified).
[^os19]: [[Biology 2e (OpenStax)]], ch. 19 "The Evolution of Populations", section "Adaptive Evolution" (peppered moth; frequency-dependent selection).
[^os18]: [[Biology 2e (OpenStax)]], ch. 18 "Evolution and the Origin of Species" (reproductive isolation; hybrid sterility of the mule).
