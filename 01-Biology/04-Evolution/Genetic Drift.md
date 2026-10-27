---
aliases:
  - Random Genetic Drift
  - Allelic Drift
  - Drift
  - Dérive génétique
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - domain/statistics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Allele Frequency]]"
  - "[[Hardy-Weinberg Equilibrium]]"
  - "[[Binomial Distribution]]"
  - "[[Natural Selection]]"
  - "[[Sampling]]"
related:
  - "[[Effective Population Size]]"
  - "[[Heterozygosity]]"
  - "[[Wright-Fisher Model]]"
  - "[[Moran Model]]"
  - "[[Fixation Probability]]"
  - "[[Neutral Theory of Molecular Evolution]]"
  - "[[Coalescent Theory]]"
  - "[[Gene Flow]]"
  - "[[Fixation Index]]"
  - "[[Absorbing Markov Chain]]"
  - "[[Random Number Generation]]"
  - "[[Experimental Evolution]]"
projects:
  - "[[07-evolution-simulator]]"
  - "[[bio-simulation]]"
sources:
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Evolution (Futuyma)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Kimura 1968 - Evolutionary Rate at the Molecular Level]]"
  - "[[Wright 1931 - Evolution in Mendelian Populations]]"
  - "[[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]]"
---

# Genetic Drift

> [!abstract]
> Genetic drift is the change of allele frequencies by pure chance, because each generation inherits a finite sample of its parents' genes: it has no direction, its steps are larger in smaller populations, and it ends with every allele either lost or fixed.

## Definition

**Genetic drift** is the random change in allele frequencies from one generation to the next that results from the sampling of gametes in a finite population: which individuals reproduce, how many offspring they leave and which of their two alleles each offspring receives all vary by chance.[^hartl][^futuyma] Its effect is stronger in small populations.[^os19] Sewall Wright's 1931 paper gave the first detailed quantitative theory of how population size, together with mutation, migration and selection, changes gene frequencies.[^wright]

## Why it matters

- **Most of the genome drifts.** Kimura argued that most molecular changes fixed in evolution are selectively neutral and fixed by drift.[^kimura] Drift is therefore the null model of molecular evolution, and tests for selection ask whether data depart from it ([[Neutral Theory of Molecular Evolution]], [[Selection Scan]]).
- **Time series need a noise model.** When allele frequencies are measured over generations, in an evolution experiment or in repeated samples of a population, a change counts as evidence of selection only if it exceeds the drift variance $pq/2N_e$ accumulated over the interval ([[Experimental Evolution]], [[Fitness]]).
- **Small populations lose diversity.** Captive, endangered, laboratory and founder populations lose heterozygosity and alleles at a rate set by their size ([[Heterozygosity]], [[Effective Population Size]]).
- **The random engine of simulators.** One line of binomial sampling per generation is the [[Wright-Fisher Model]] at the core of [[07-evolution-simulator]] and [[bio-simulation]], run with reproducible seeds ([[Random Number Generation]]).

## Core (L2)

### Drift is sampling

Picture the $2N$ gene copies of $N$ diploid individuals as marbles in an urn. The next generation is formed by drawing $2N$ copies from the gametes of the current one. Even when no genotype is fitter than another, some individuals leave more offspring by luck, and a heterozygote passes A or a to each offspring with probability 1/2, so the frequency in the new urn differs from the old one by chance.[^os19][^hartl] In the idealized Wright-Fisher version, the $2N$ copies are drawn independently with replacement, and two laws follow from the binomial distribution (derived in [[Binomial Distribution#Deeper (L2)]]):

1. **No direction**: $E[p' \mid p] = p$. The expected frequency never changes.
2. **Steps scale with $1/N$**: $\operatorname{Var}(p' \mid p) = pq/2N$.

| Population size $N$ | SD of one generation's change at $p = 0.5$ |
|---:|---:|
| 10 | 0.112 |
| 1,000 | 0.011 |
| 1,000,000 | 0.00035 |

### Four consequences

1. **Every allele is eventually lost or fixed.** Frequencies 0 and 1 are absorbing: once an allele is gone, drift cannot bring it back. A neutral allele at frequency $p_0$ is fixed with probability $p_0$, so a new mutation, present as one copy among $2N$, is fixed with probability $1/2N$.[^hartl]
2. **Heterozygosity decays** by a factor $1 - 1/2N$ per generation, $H_t = H_0(1 - 1/2N)^t$ ([[Heterozygosity]]).[^hartl]
3. **Replicate populations diverge.** Started from the same $p_0$, isolated populations spread apart: their variance grows as $p_0q_0\left[1 - (1 - 1/2N)^t\right]$ (Mathematical representation), which is why isolated populations become genetically different without any selection ([[Fixation Index]]). Migration counteracts this ([[Gene Flow]]).
4. **The clock runs in units of $N$.** Heterozygosity halves in about $1.39N$ generations, and a new neutral mutation that does reach fixation takes on average about $4N$ generations to get there.[^hartl]

![[genetic-drift-trajectories.svg]]

*Ten simulated Wright-Fisher populations per panel, all starting at $p = 0.5$ (code below, fixed seeds). With $N = 10$, all ten populations had fixed or lost the allele by generation 60. With $N = 100$, frequencies wander ten times more slowly; one population still lost the allele.*

### Bottlenecks and founders

Drift is strongest when the population is smallest. A drastic random reduction of a population (**bottleneck effect**) or the start of a new population by a few individuals (**founder effect**) leaves a gene pool that can differ markedly from the original one.[^os19] Their long-term weight is quantified in [[Effective Population Size]].

### Drift and selection together

Selection pushes allele frequencies in one direction; drift adds noise of variance $pq/2N$ around that push. The deterministic recursion of [[Natural Selection]] is a good description when the selection coefficient $|s|$ is large compared with $1/N$; when $|s|$ is much smaller than $1/N$, the allele behaves as if neutral.[^hartl] Two corollaries: most new mutations, even advantageous ones, are lost by chance while still rare ([[Fixation Probability]]), and slightly deleterious alleles can drift to fixation in small populations ([[Natural Selection#Advanced (L3)]]).

## Advanced (L3)

- **A Markov chain with two absorbing states.** The number of copies $X_t \in \{0, \dots, 2N\}$ is a [[Markov Chain]] with binomial transitions, absorbed at 0 and $2N$ ([[Absorbing Markov Chain]]). Because $p_t$ keeps its expectation, $P(\text{fixation}) = p_0$. For large $N$, the [[Diffusion Approximation]] gives fixation and loss times in closed form, the source of the $4N$ result.[^hartl]
- **Backward in time: coalescence.** Two gene copies of one generation derive from the same parental copy with probability $1/2N$. The number of generations back to their common ancestor is geometric with mean $2N$: the starting point of [[Coalescent Theory]], which describes the genealogy that drift generates instead of its forward effect.
- **The neutral substitution rate.** In a diploid population, $2N\mu$ new neutral mutations arise per generation and each is fixed with probability $1/2N$, so neutral substitutions accumulate at rate $\mu$, independent of population size. This was Kimura's argument for a nearly constant rate of molecular evolution.[^kimura] It is why neutral sites behave as a [[Molecular Clock]] (Exercise 6).
- **Other idealizations.** The [[Moran Model]] replaces whole generations by one birth and one death at a time; with overlapping generations the bookkeeping changes but the laws above keep their form.
- **Real populations drift faster than their census suggests.** Unequal sex ratios, variable family sizes and fluctuating size make a population of $N$ individuals drift like a smaller ideal one ([[Effective Population Size]]).

## Mathematical representation

- **Wright-Fisher sampling.** With $X_t$ copies of A among $2N$ and $p_t = X_t/2N$: $X_{t+1} \mid X_t \sim \mathrm{Bin}(2N, p_t)$, so $E[p_{t+1} \mid p_t] = p_t$ and $\operatorname{Var}(p_{t+1} \mid p_t) = p_tq_t/2N$.
- **Heterozygosity.** $E[p_{t+1}q_{t+1} \mid p_t] = p_t - E[p_{t+1}^2 \mid p_t] = p_t - p_t^2 - p_tq_t/2N = \lambda\,p_tq_t$ with $\lambda = 1 - 1/2N$; iterating, $E[p_tq_t] = \lambda^t p_0q_0$.
- **Divergence of replicates.** $E[p_t] = p_0$ and $E[p_t^2] = E[p_t] - E[p_tq_t] = p_0 - \lambda^t p_0q_0$, so
$$\operatorname{Var}(p_t) = p_0q_0\left(1 - \lambda^t\right) \xrightarrow[t \to \infty]{} p_0q_0,$$
the variance of a Bernoulli($p_0$) variable: in the limit, a fraction $p_0$ of populations is fixed and $q_0$ has lost the allele.
- **Fixation.** $p_t$ is a bounded martingale absorbed at 0 or 1, so $p_0 = E[p_\infty] = P(\text{fixation})$.
- **Coalescence.** $P(T_2 > t) = \lambda^t$ and $E[T_2] = 2N$ generations.

## Computational representation

The simulation follows many independent populations and compares them with the formulas. Standard library only; summing $2N$ Bernoulli draws costs $O(N)$ per generation, which is fine for teaching sizes (a vectorized binomial generator does the same draw directly).

```python
import random


def wf_generation(count: int, two_n: int, rng: random.Random) -> int:
    """One Wright-Fisher generation: 2N copies drawn with replacement from the current pool."""
    p = count / two_n
    return sum(rng.random() < p for _ in range(two_n))


def replicate_populations(two_n: int, p0: float, generations: int, reps: int, seed: int) -> list[float]:
    """Allele frequency in `reps` independent populations after `generations` of drift."""
    rng = random.Random(seed)
    finals = []
    for _ in range(reps):
        count = round(p0 * two_n)
        for _ in range(generations):
            if count in (0, two_n):            # lost or fixed: absorbing states
                break
            count = wf_generation(count, two_n, rng)
        finals.append(count / two_n)
    return finals


p0, t, reps = 0.5, 20, 2000
for n in (10, 100):                           # N diploid individuals = 2N gene copies
    two_n = 2 * n
    f = replicate_populations(two_n, p0, t, reps, seed=n)
    mean = sum(f) / reps
    var = sum((x - mean) ** 2 for x in f) / reps
    het = sum(2 * x * (1 - x) for x in f) / reps
    decay = (1 - 1 / two_n) ** t
    print(f"N={n:3d} mean={mean:.3f} var={var:.4f} (theory {p0 * (1 - p0) * (1 - decay):.4f}) "
          f"H={het:.3f} (theory {2 * p0 * (1 - p0) * decay:.3f}) "
          f"lost={sum(x == 0 for x in f) / reps:.3f} fixed={sum(x == 1 for x in f) / reps:.3f}")
```

```text
N= 10 mean=0.500 var=0.1572 (theory 0.1604) H=0.186 (theory 0.179) lost=0.242 fixed=0.236
N=100 mean=0.496 var=0.0236 (theory 0.0238) H=0.453 (theory 0.452) lost=0.000 fixed=0.000
```

The mean stays at 0.5 in both cases; the variance among populations and the loss of heterozygosity are what $N$ controls. Agreement with theory is within the Monte Carlo noise of 2,000 replicates ([[Monte Carlo Method]]).

## Worked example

> [!example] Ten breeding individuals, predicted then simulated
> A population of $N = 10$ diploids (20 gene copies) starts at $p_0 = 0.5$, with no selection, mutation or migration.
> 1. **One generation.** $\mathrm{SD} = \sqrt{0.25/20} = 0.112$. The new frequency is $X/20$ with $X \sim \mathrm{Bin}(20, 0.5)$; a jump to 0.3 or below, or 0.7 or above ($X \le 6$ or $X \ge 14$), has probability $2 \times 0.0577 = 0.115$.
> 2. **Twenty generations.** $\lambda^{20} = 0.95^{20} = 0.358$. Expected heterozygosity $0.5 \times 0.358 = 0.179$; variance among replicate populations $0.25 \times (1 - 0.358) = 0.160$, an SD of 0.40, larger than the SD of a uniform distribution on [0, 1] (0.29): the distribution has become U-shaped, piled up near 0 and 1.
> 3. **Simulation** (code above, 2,000 populations): variance 0.157, heterozygosity 0.186, 24.2% lost and 23.6% fixed, mean still 0.500.
> 4. **Ten times larger.** With $N = 100$ the variance is only 0.024 (SD 0.15) and no population is fixed or lost after 20 generations.
> 5. **Reading.** One generation of drift is small in a large population, but it accumulates without any restoring force, at a pace set by $N$.

## Common misconceptions

> [!warning] "Drift pushes rare alleles toward loss"
> Drift has no direction: $E[p'] = p$ at every frequency. A rare allele is usually lost because it starts close to 0, but in the rare runs where it drifts up it can reach fixation, which balances the expectation exactly ($P(\text{fix}) = p_0$).

> [!warning] "Drift only matters in small populations"
> It acts in every finite population. Each new mutation starts as one copy, so its early fate is decided by chance whatever the population size, and at neutral sites drift is the only force over the long term.[^kimura]

> [!warning] "Drift needs a catastrophe"
> Bottlenecks are extreme cases. Ordinary variation in the number of offspring and the 1/2 lottery of Mendelian segregation produce drift in every generation.[^os19][^hartl]

> [!warning] "A common allele must have been favored by selection"
> Drift alone raises some neutral alleles to high frequency or fixation, and can fix slightly deleterious ones in small populations. Frequency alone is not evidence of selection; the comparison with a neutral model is ([[Neutral Theory of Molecular Evolution]]).

## Exercises

> [!question] Exercise 1 (L2)
> An allele has frequency 0.2. Compute the standard deviation of its change over one generation in populations of $N = 10$ and $N = 10{,}000$ diploids.

> [!success]- Solution
> $\sqrt{0.2 \times 0.8 / 20} = 0.089$ and $\sqrt{0.2 \times 0.8 / 20000} = 0.0028$. In the small population, a change from 0.2 to 0.3 in one generation is unremarkable; in the large one it would be a 35-SD event that only selection, migration or a sampling artifact could explain.

> [!question] Exercise 2 (L2)
> (a) A neutral allele has frequency 0.3. What is the probability that it will eventually be fixed? (b) A new neutral mutation appears in a population of 500 diploids. What is its probability of fixation, and of loss?

> [!success]- Solution
> (a) 0.3: the fixation probability of a neutral allele is its current frequency. (b) One copy among $2N = 1000$: fixation $1/1000$, loss $999/1000$. The fate of almost every new mutation is to be lost within a few generations.

> [!question] Exercise 3 (L2)
> Two isolated populations of $N = 50$ start at $p = 0.5$. After 50 generations, what is the expected variance of $p$ in each, and the typical difference between them?

> [!success]- Solution
> $\lambda^{50} = 0.99^{50} = 0.605$, so $\operatorname{Var}(p_{50}) = 0.25 \times 0.395 = 0.099$ (SD 0.31). The two populations drift independently, so their difference has variance $2 \times 0.099 = 0.197$, an SD of 0.44. Without migration, drift alone makes them strongly differentiated ([[Fixation Index]]).

> [!question] Exercise 4 (L2, Python)
> Using `replicate_populations` from the code above, check by simulation that the fixation probability of a neutral allele equals its starting frequency, for $p_0 = 0.1, 0.3, 0.5$ in populations of 10 diploids, running long enough for every population to be absorbed.

> [!success]- Solution
> ```python
> for p_start in (0.1, 0.3, 0.5):
>     f = replicate_populations(20, p_start, 1000, 2000, seed=7)   # 1,000 generations: all absorbed
>     print(p_start, sum(x == 1 for x in f) / len(f), sum(0 < x < 1 for x in f))
> ```
> ```text
> 0.1 0.1005 0
> 0.3 0.299 0
> 0.5 0.502 0
> ```
> Fixed fractions 0.1005, 0.299 and 0.502, within the binomial noise of 2,000 replicates ($\mathrm{SD} \le 0.011$), and no population is left unabsorbed.

> [!question] Exercise 5 (L3, Python)
> Continuing the code above, introduce a single new mutant copy into a population of $N = 25$ diploids, 20,000 times. Estimate its fixation probability, the mean time to fixation when it fixes, the mean time to loss when it is lost, and the fraction of all runs lost in the very first generation. Compare with $1/2N$, $4N$ and $(1 - 1/2N)^{2N}$.

> [!success]- Solution
> ```python
> rng = random.Random(2024)
> two_n, reps = 50, 20_000                      # N = 25 diploids; one new mutant copy each time
> fixed_times, lost_times = [], []
> for _ in range(reps):
>     count, t = 1, 0
>     while 0 < count < two_n:
>         count = wf_generation(count, two_n, rng)
>         t += 1
>     (fixed_times if count == two_n else lost_times).append(t)
> print(len(fixed_times) / reps, 1 / two_n)                                   # P(fixation)
> print(round(sum(fixed_times) / len(fixed_times), 1), 2 * two_n)            # mean time if fixed, 4N
> print(round(sum(lost_times) / len(lost_times), 2),                         # mean time if lost
>       sum(t == 1 for t in lost_times) / reps, round((1 - 1 / two_n) ** two_n, 3))
> ```
> ```text
> 0.0208 0.02
> 97.6 100
> 7.21 0.36615 0.364
> ```
> About 2% of new mutations fix, as $1/2N$ predicts, and those that do take about $4N$ generations. Lost mutations disappear fast: 7 generations on average, and 37% of all mutations vanish in the first generation, when none of the 50 copies drawn is the mutant, with probability $(1 - 1/50)^{50}$.

> [!question] Exercise 6 (L3)
> Using the human germline mutation rate of $1.20 \times 10^{-8}$ per nucleotide per generation[^kong] and an illustrative population of $N = 10{,}000$ diploids, compute per neutral site: the number of new mutant copies per generation, the fixation probability of each, and the substitution rate. How many substitutions per site accumulate in $10^6$ generations, and how would the answer change with $N = 10^6$?

> [!success]- Solution
> New copies: $2N\mu = 2 \times 10^4 \times 1.2 \times 10^{-8} = 2.4 \times 10^{-4}$ per site per generation; each fixes with probability $1/2N = 5 \times 10^{-5}$; substitution rate $2.4 \times 10^{-4} \times 5 \times 10^{-5} = 1.2 \times 10^{-8} = \mu$. Over $10^6$ generations: 0.012 substitutions per site. With $N = 10^6$, a hundred times more mutations arise but each is a hundred times less likely to fix: the rate is unchanged.[^kimura] Neutral divergence measures time and mutation rate, not population size ([[Molecular Clock]]).

## Mastery checklist

- [ ] 1 Recognized: I can define drift as sampling error between generations and say why it is stronger in small populations.
- [ ] 2 Understood: I can explain $E[p'] = p$ and $\operatorname{Var}(p') = pq/2N$ and derive the four consequences: fixation or loss, decay of heterozygosity, divergence of populations, time scale proportional to $N$.
- [ ] 3 Practiced: I can simulate Wright-Fisher drift with a fixed seed and check fixation probabilities, heterozygosity and among-population variance against theory.
- [ ] 4 Applied: in [[07-evolution-simulator]], built on [[bio-simulation]], I combined drift with selection and showed for which $s$ and $N$ the deterministic prediction fails.
- [ ] 5 Explained: I can teach drift as the null model of molecular evolution, its link with the coalescent and the molecular clock, and how bottlenecks and founder events amplify it.

## References

[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed. (2006), treatment of random genetic drift (Wright-Fisher sampling, fixation probability and time, decay of heterozygosity, drift and selection).
[^futuyma]: [[Evolution (Futuyma)]], 5th ed. (2023), genetic drift (chapter numbers not verified).
[^os19]: [[Biology 2e (OpenStax)]], ch. 19 "The Evolution of Populations", section "Population Genetics" (genetic drift, bottleneck effect, founder effect).
[^kimura]: [[Kimura 1968 - Evolutionary Rate at the Molecular Level]], *Nature* 217:624-626.
[^wright]: [[Wright 1931 - Evolution in Mendelian Populations]], *Genetics* 16:97-159.
[^kong]: [[Kong 2012 - Rate of De Novo Mutations and the Importance of Father's Age to Disease Risk]], *Nature* 488:471-475.
