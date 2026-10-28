---
aliases:
  - Exp(λ)
  - Exponential Law
  - Negative Exponential Distribution
  - Waiting Time Distribution
  - Loi exponentielle
tags:
  - type/concept
  - domain/statistics
  - domain/mathematics
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Probability Density Function]]"
  - "[[Cumulative Distribution Function]]"
  - "[[Exponential Function]]"
  - "[[Improper Integral]]"
  - "[[Poisson Distribution]]"
  - "[[Geometric Distribution]]"
related:
  - "[[Poisson Process]]"
  - "[[Gamma Distribution]]"
  - "[[Continuous-Time Markov Chain]]"
  - "[[Nucleotide Substitution Model]]"
  - "[[Jukes-Cantor Model]]"
  - "[[Coalescent Theory]]"
  - "[[Gillespie Algorithm]]"
  - "[[Stochastic Gene Expression]]"
  - "[[Survival Analysis]]"
  - "[[Rate Law]]"
  - "[[Messenger RNA]]"
projects: []
sources:
  - "[[Introduction to Probability (Blitzstein)]]"
  - "[[Introductory Statistics (OpenStax)]]"
  - "[[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]]"
  - "[[Molecular Evolution (Yang)]]"
  - "[[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]]"
  - "[[Principles of Population Genetics (Hartl)]]"
  - "[[Schwanhäusser 2011 - Global Quantification of Mammalian Gene Expression Control]]"
  - "[[Gillespie 1977 - Exact Stochastic Simulation of Coupled Chemical Reactions]]"
---

# Exponential Distribution

> [!abstract]
> The exponential distribution is the waiting time for an event that has the same chance of happening at every instant, whatever happened before: the lifetime of an mRNA molecule under first-order decay, or the time until the next substitution at a site along a branch of a phylogenetic tree.

## Definition

A random variable $T \ge 0$ has the **exponential distribution** with rate $\lambda > 0$, $T \sim \mathrm{Exp}(\lambda)$, if its density is $f(t) = \lambda e^{-\lambda t}$ for $t \ge 0$ ([[Probability Density Function]]). Then

$$F(t) = 1 - e^{-\lambda t}, \qquad P(T > t) = e^{-\lambda t}, \qquad E[T] = \frac{1}{\lambda}, \qquad \operatorname{Var}(T) = \frac{1}{\lambda^2},$$

and the median is $\ln 2/\lambda$. It is **memoryless**, $P(T > s + t \mid T > s) = P(T > t)$, and it is the only continuous distribution with this property.[^blitz5][^openstax5]

## Why it matters

- **Substitutions along a branch.** In continuous-time Markov models of sequence evolution, a site keeps its base for an exponentially distributed time whose rate is the total rate of leaving that base, then changes; branch lengths count the expected substitutions that result ([[Nucleotide Substitution Model]], [[Continuous-Time Markov Chain]]).[^yang]
- **mRNA lifetimes.** Under first-order decay each molecule has the same chance of being degraded at every instant, so lifetimes are exponential, with half-life $\ln 2/k$ for decay rate $k$ ([[Rate Law#Bio: mRNA and protein decay are first order]], [[Messenger RNA]]). Schwanhäusser et al. measured mRNA and protein turnover for more than 5,000 genes and fitted synthesis-degradation models gene by gene.[^schwan]
- **Gaps between random events.** Events scattered at a constant rate, in time or along a genome, are separated by exponential gaps ([[Poisson Process]], [[Poisson Distribution]]).[^6041]
- **Genealogies.** In the coalescent, the waiting times between successive common-ancestor events of sampled lineages are approximately exponential ([[Coalescent Theory]]).[^hartl][^yang]
- **Stochastic simulation.** The Gillespie algorithm advances a reaction network from one event to the next by exponential waiting times ([[Gillespie Algorithm]], [[Stochastic Gene Expression]]).[^gillespie]

## Core (L2)

### A constant hazard

The **hazard** is the rate at which the event happens at time $t$ among those that have not yet had it: $h(t) = f(t)/P(T > t)$. For the exponential, $h(t) = \lambda e^{-\lambda t}/e^{-\lambda t} = \lambda$ at every $t$: the event comes at a constant rate, whatever the age. This is the continuous version of the [[Geometric Distribution]], independent trials in tiny time steps $dt$, each succeeding with probability $\lambda\,dt$ (limit in Mathematical representation). Hazards that change with age lead beyond the exponential, to [[Survival Analysis]].

### Half-life, mean lifetime and memorylessness

![[exponential-survival-memoryless.svg]]

- **Half-life.** $P(T > t_{1/2}) = 1/2$ gives $t_{1/2} = \ln 2/\lambda$: half of the molecules are gone after one half-life, three quarters after two, seven eighths after three.
- **Mean lifetime.** $E[T] = 1/\lambda = t_{1/2}/\ln 2 \approx 1.44\,t_{1/2}$, above the median: the distribution is right-skewed, and a fraction $e^{-1} \approx 37$ % of the molecules outlive the mean lifetime.
- **Memorylessness.** $P(T > s + t \mid T > s) = e^{-\lambda(s+t)}/e^{-\lambda s} = e^{-\lambda t}$: molecules still present at 3 h face the same survival curve as new ones (dashed curve). An old molecule is not "due" to decay.

### From molecules to populations

If $N_0$ molecules decay independently with rate $k$, each is still present at time $t$ with probability $e^{-kt}$, so the number present is $\mathrm{Bin}(N_0, e^{-kt})$, with mean $N_0e^{-kt}$ ([[Binomial Distribution]]). The deterministic first-order integrated rate law is the expectation of this stochastic model ([[Rate Law]]); the fluctuations around it, of order $\sqrt{N_0e^{-kt}(1 - e^{-kt})}$, matter when copy numbers are small.

### Waiting times in a Poisson process

Events arriving at rate $\lambda$ give $P(\text{no event in } [0, t]) = P(\mathrm{Pois}(\lambda t) = 0) = e^{-\lambda t}$, so the time to the first event is $\mathrm{Exp}(\lambda)$, and by memorylessness the gaps between successive events are independent $\mathrm{Exp}(\lambda)$ ([[Poisson Process]]).[^6041][^blitz5] The time to the $n$-th event, a sum of $n$ independent exponential gaps, follows the [[Gamma Distribution]].[^blitz]

## Advanced (L3)

### Competing exponentials: the first event and the winner

If $T_1, \dots, T_m$ are independent with $T_i \sim \mathrm{Exp}(\lambda_i)$, then

$$\min_i T_i \sim \mathrm{Exp}\Big(\sum_i \lambda_i\Big), \qquad P(T_j \text{ comes first}) = \frac{\lambda_j}{\sum_i \lambda_i},$$

and which event comes first is independent of when it comes (Mathematical representation).[^blitz] Two algorithms rest on this fact:

- **Continuous-time Markov chains.** From base $i$, the substitutions to the other bases compete at rates $q_{ij}$: the site keeps base $i$ for an $\mathrm{Exp}\big(\sum_{j \ne i} q_{ij}\big)$ time, then changes to $j$ with probability $q_{ij}/\sum_{l \ne i} q_{il}$ ([[Continuous-Time Markov Chain]]).[^yang] Exercise 4 applies it to a transition-rich rate matrix.
- **The Gillespie algorithm.** In a well-mixed reaction network, the time to the next reaction is exponential with rate equal to the total propensity of all reactions, and a second random number chooses which reaction fires, in proportion to the propensities.[^gillespie] Exercise 5 simulates mRNA synthesis and decay this way.

### From substitution events to observed differences

In Felsenstein's 1981 model, substitution events at a site occur at a constant rate, and each event draws the new base from fixed base frequencies, possibly the same base as before.[^f81] With equal frequencies this is the Jukes-Cantor model:[^yang] replacement events at rate $u$, each producing any of the four bases with probability 1/4. Only three quarters of the events change the base, so substitutions occur at rate $3u/4$, and a branch of duration $t$ has length $d = 3ut/4$ expected substitutions per site. The two ends of the branch differ if at least one event occurred ($1 - e^{-ut}$) and the last event drew a different base (3/4):

$$p = \frac{3}{4}\Big(1 - e^{-4d/3}\Big) \quad\Longleftrightarrow\quad d = -\frac{3}{4}\ln\Big(1 - \frac{4p}{3}\Big).$$

The proportion of differing sites $p$ underestimates $d$ because of multiple hits, and inverting $p(d)$ gives the Jukes-Cantor distance ([[Jukes-Cantor Model]], Exercise 3).

### Coalescence times

Looking backward in a population of $N$ diploids ($2N$ gene copies), two lineages find their common ancestor in the previous generation with probability $1/(2N)$, so their coalescence time is geometric with mean $2N$ generations, approximately exponential; with $j$ lineages, the next coalescence comes after an approximately exponential time with rate $\binom{j}{2}/(2N)$ per generation.[^hartl][^yang] Summing the means from $j = n$ down to 2,

$$E[T_{\mathrm{MRCA}}] = \sum_{j=2}^{n}\frac{2N}{\binom{j}{2}} = 4N\sum_{j=2}^{n}\Big(\frac{1}{j-1} - \frac{1}{j}\Big) = 4N\Big(1 - \frac{1}{n}\Big)$$

generations. The last two lineages alone take $2N$ generations on average, more than half of the total (Exercise 6).

## Mathematical representation

- **Normalization** ([[Improper Integral]]): $\int_0^\infty \lambda e^{-\lambda t}\,dt = \big[-e^{-\lambda t}\big]_0^\infty = 1$.
- **Moments.** For $T \ge 0$, $E[T] = \int_0^\infty P(T > t)\,dt = \int_0^\infty e^{-\lambda t}\,dt = 1/\lambda$, and $E[T^2] = \int_0^\infty 2t\,P(T > t)\,dt = 2/\lambda^2$, so $\operatorname{Var}(T) = 1/\lambda^2$: the standard deviation equals the mean.
- **Scaling.** If $T \sim \mathrm{Exp}(1)$ then $T/\lambda \sim \mathrm{Exp}(\lambda)$: the rate is an inverse time scale.
- **The only memoryless law.** With $G(t) = P(T > t)$, memorylessness reads $G(s + t) = G(s)G(t)$. For a non-increasing $G$ with $G(0) = 1$ the solutions are $G(t) = e^{-\lambda t}$ (Cauchy's functional equation for $\ln G$), so $T$ is exponential.
- **Minimum and winner.** $P(\min_i T_i > t) = \prod_i e^{-\lambda_i t} = e^{-(\sum_i\lambda_i)t}$. For two variables, $P(T_1 < T_2,\ T_1 > t) = \int_t^\infty \lambda_1e^{-\lambda_1 s}e^{-\lambda_2 s}\,ds = \frac{\lambda_1}{\lambda_1 + \lambda_2}e^{-(\lambda_1+\lambda_2)t}$, the product of $P(T_1 < T_2)$ and $P(\min > t)$: the winner is independent of the time.
- **Limit of the geometric.** If a trial of length $\Delta$ succeeds with probability $\lambda\Delta$ and $X \sim \mathrm{Geom}(\lambda\Delta)$, then $P(X\Delta > t) = (1 - \lambda\Delta)^{\lfloor t/\Delta \rfloor} \to e^{-\lambda t}$ as $\Delta \to 0$ ([[Limit]]).
- **Maximum likelihood with censoring.** Observe $d$ lifetimes $t_1, \dots, t_d$, and $c$ molecules still present at times $s_1, \dots, s_c$ when observation stops. The likelihood $\prod_i \lambda e^{-\lambda t_i}\prod_j e^{-\lambda s_j}$ is maximized at

$$\hat\lambda = \frac{d}{\sum_i t_i + \sum_j s_j} = \frac{\text{number of events}}{\text{total time at risk}}$$

  ([[Maximum Likelihood Estimation]]). Dropping the censored molecules removes the longest lifetimes and overestimates $\lambda$.

## Computational representation

Inverse-transform sampling gives $T = -\ln U/\lambda$ for $U$ uniform on $(0, 1]$ ([[Uniform Distribution#Universality of the uniform]]); `random.expovariate(lambd)` does the same job.

```python
import math
import random


def exp_sample(rate: float, rng: random.Random) -> float:
    """Inverse transform: T = -ln(U) / rate, with U uniform on (0, 1] (see Uniform Distribution)."""
    return -math.log(1.0 - rng.random()) / rate


rng = random.Random(42)
half_life = 2.0                                    # hours, illustrative
k = math.log(2) / half_life                        # decay rate per hour
life = sorted(exp_sample(k, rng) for _ in range(100_000))
print(f"k = {k:.4f} per h | mean lifetime {sum(life) / len(life):.3f} h (1/k = {1 / k:.3f}) | median {life[50_000]:.3f} h")
for t in (2, 4, 6):
    print(t, "h: surviving fraction", round(sum(x > t for x in life) / len(life), 4), "| exp(-kt) =", round(math.exp(-k * t), 4))
rest = [x - 3 for x in life if x > 3]              # molecules alive at 3 h: their remaining lifetime
print(f"alive at 3 h: {len(rest)} | mean remaining {sum(rest) / len(rest):.3f} h | P(> 2 h more) {sum(x > 2 for x in rest) / len(rest):.4f}")

from scipy import stats
print("SciPy expon(scale = 1/k): mean", round(stats.expon(scale=1 / k).mean(), 3), "| P(T > 2) =", round(stats.expon(scale=1 / k).sf(2), 4))
```

```text
k = 0.3466 per h | mean lifetime 2.890 h (1/k = 2.885) | median 2.003 h
2 h: surviving fraction 0.5007 | exp(-kt) = 0.5
4 h: surviving fraction 0.2506 | exp(-kt) = 0.25
6 h: surviving fraction 0.1254 | exp(-kt) = 0.125
alive at 3 h: 35414 | mean remaining 2.891 h | P(> 2 h more) 0.4985
SciPy expon(scale = 1/k): mean 2.885 | P(T > 2) = 0.5
```

The simulated lifetimes reproduce the mean $1/k$, the median $t_{1/2}$ and the survival curve. The 35,414 molecules still present at 3 h have the same mean remaining lifetime and the same 50 % chance of lasting 2 more hours as new molecules: memorylessness. SciPy's `expon`, like NumPy's `Generator.exponential`, takes the **scale** $1/\lambda$, not the rate.

## Worked example

> [!example] Estimating a half-life when the experiment ends too early
> 200 labelled transcripts (illustrative, true half-life 3 h) are followed for 8 h; each decay is timed, and the transcripts still present at 8 h are censored. Continuing the code above:
>
> ```python
> rng = random.Random(8)
> true_k = math.log(2) / 3.0                         # true half-life 3 h (illustrative)
> times = [rng.expovariate(true_k) for _ in range(200)]
> stop = 8.0                                         # end of the experiment (h)
> observed = [t for t in times if t <= stop]         # decays seen before the end
> d = len(observed)
> at_risk = sum(observed) + stop * (len(times) - d)  # total time under observation
> k_hat = d / at_risk                                # decays per hour at risk
> k_naive = d / sum(observed)                        # ignores the censored molecules
> print(f"decays seen {d} of {len(times)} | k_hat {k_hat:.3f} (true {true_k:.3f}) | naive {k_naive:.3f}")
> print(f"half-life: censored MLE {math.log(2) / k_hat:.2f} h, naive {math.log(2) / k_naive:.2f} h")
> ```
>
> ```text
> decays seen 167 of 200 | k_hat 0.236 (true 0.231) | naive 0.377
> half-life: censored MLE 2.94 h, naive 1.84 h
> ```
>
> 1. **Data.** 167 decays are timed; 33 transcripts outlive the experiment, and for them only "longer than 8 h" is known.
> 2. **Censored maximum likelihood.** Events divided by total time at risk gives $\hat k = 0.236$ per hour, a half-life of 2.94 h, close to the true 3 h.
> 3. **Naive estimate.** Averaging only the observed lifetimes discards the 33 longest ones and gives a half-life of 1.84 h, 39 % too short: censoring biases toward instability unless the time at risk is counted.
> 4. **Population data.** When only the number of molecules remaining is measured at a few time points, the same rate is fitted through the integrated rate law $\ln N(t) = \ln N_0 - kt$ ([[Rate Law]]).

## Common misconceptions

> [!warning] "Old molecules are about to be degraded"
> Under first-order decay a molecule that has survived 5 h is exactly as likely to be degraded in the next hour as a new one: $1 - e^{-k}$ for both. If measured lifetimes show a hazard that rises with age, decay is not a single exponential step, which is itself informative (Exercise 2).

> [!warning] "The mean lifetime is the half-life"
> The mean lifetime $1/k$ is 1.44 times the half-life $\ln 2/k$. Mixing them up changes a rate by 44 %. Check also whether a library or a paper parameterizes by rate or by scale.

> [!warning] "The proportion of differing sites is the number of substitutions"
> Along long branches a site can change twice, or change back. The proportion $p$ of differing sites is always below the branch length $d$ and saturates at 3/4; only a model such as Jukes-Cantor recovers $d$ (Exercise 3).

## Exercises

> [!question] Exercise 1 (L2)
> An mRNA has a half-life of 30 min. Give its decay rate per hour, its mean lifetime, the probability that a molecule survives 2 h, and the probability that it outlives twice the mean lifetime.

> [!success]- Solution
> $k = \ln 2/0.5\,\text{h} = 1.386$ per hour; mean lifetime $1/k = 0.721$ h, about 43 min. Two hours are four half-lives: $P(T > 2) = 2^{-4} = 0.0625$. $P(T > 2/k) = e^{-2} = 0.135$, whatever the half-life.

> [!question] Exercise 2 (L2)
> Prove memorylessness from the survival function. A transcript has already survived 5 h: is it more likely than a new transcript to be degraded during the next hour? What would a hazard that increases with age suggest?

> [!success]- Solution
> $P(T > 5 + t \mid T > 5) = e^{-k(5 + t)}/e^{-5k} = e^{-kt} = P(T > t)$, so both transcripts are degraded within the hour with probability $1 - e^{-k}$. A hazard rising with age means that the molecule "remembers" time, for instance because degradation requires several successive steps: a sum of independent exponential steps has a gamma distribution, whose hazard increases ([[Gamma Distribution]]).

> [!question] Exercise 3 (L2)
> Under the Jukes-Cantor model, for branch lengths $d = 0.1$ and $d = 0.5$ substitutions per site, compute the probability of no substitution, of at least one, and of observing a difference between the two ends. Check that the Jukes-Cantor formula recovers $d$.

> [!success]- Solution
> Substitutions occur at rate $3u/4$, so $P(\text{none}) = e^{-d}$: 0.905 and 0.607; at least one: 0.095 and 0.393. Differences: $p = \frac34(1 - e^{-4d/3}) = 0.0936$ and $0.365$. Inverting, $-\frac34\ln(1 - \frac43 \times 0.0936) = 0.1$ and the same for 0.5. At $d = 0.5$, 7 % of the sites that underwent substitutions show no difference ($1 - 0.365/0.393$): counting differences underestimates evolutionary distance more and more as branches lengthen.

> [!question] Exercise 4 (L3)
> In an illustrative rate matrix, a site with base A changes to C, G and T at rates 0.1, 0.4 and 0.1 per unit time (the transition A → G is favoured). Give the distribution and the mean of the time spent as A, the probability that the next base is G, and the probability that the site has not changed at all after one unit of time.

> [!success]- Solution
> The three changes are competing exponentials, so the time spent as A is $\mathrm{Exp}(0.6)$, with mean $1/0.6 = 1.67$ units. The next base is G with probability $0.4/0.6 = 2/3$, independently of when the change happens. $P(\text{no change in 1 unit}) = e^{-0.6} = 0.549$. The probability of *being* A after one unit is larger, since the site can leave A and come back; computing it needs the whole rate matrix ([[Continuous-Time Markov Chain]]).

> [!question] Exercise 5 (L3, Python)
> Continuing the code above, simulate with the Gillespie algorithm a gene whose mRNA is synthesized at rate $\beta = 20$ per hour and decays with half-life 2 h (illustrative values). Compare the time-averaged mean and variance of the copy number with $\beta/k$. Why are they equal?

> [!success]- Solution
> ```python
> def gillespie_mrna(beta: float, k: float, t_end: float, rng: random.Random) -> tuple[float, float]:
>     """Exact simulation of synthesis (rate beta) and first-order decay (rate k per molecule).
>     Returns the time-weighted mean and variance of the copy number after a burn-in of t_end / 10."""
>     t, m, burn = 0.0, 0, t_end / 10
>     w0 = w1 = w2 = 0.0
>     while t < t_end:
>         total = beta + k * m                       # total rate of all possible events
>         dt = rng.expovariate(total)                # waiting time to the next event: Exp(total)
>         w = min(t + dt, t_end) - max(t, burn)      # time spent in state m after the burn-in
>         if w > 0:
>             w0, w1, w2 = w0 + w, w1 + w * m, w2 + w * m * m
>         t += dt
>         m += 1 if rng.random() < beta / total else -1   # which event: probability proportional to its rate
>     mean = w1 / w0
>     return mean, w2 / w0 - mean**2
>
>
> rng = random.Random(77)
> beta, k_deg = 20.0, math.log(2) / 2.0              # 20 transcripts per hour, half-life 2 h (illustrative)
> mean, var = gillespie_mrna(beta, k_deg, 5_000.0, rng)
> print(f"steady state: mean {mean:.1f}, variance {var:.1f}, beta/k = {beta / k_deg:.1f}")
> ```
>
> ```text
> steady state: mean 57.2, variance 58.5, beta/k = 57.7
> ```
>
> Mean and variance both match $\beta/k = 57.7$ within the simulation noise. At steady state, the probability flow from $m$ to $m + 1$ balances the flow back: $\pi(m)\beta = \pi(m+1)(m+1)k$, so $\pi(m+1)/\pi(m) = (\beta/k)/(m+1)$, the recurrence of the [[Poisson Distribution]] with mean $\beta/k$. A measured variance well above the mean therefore points to mechanisms that this one-step model lacks ([[Stochastic Gene Expression]]).

> [!question] Exercise 6 (L3, Python)
> Continuing the code above, simulate the coalescence times of a sample of $n = 10$ gene copies, with time in units of $2N$ generations (so $j$ lineages coalesce at rate $\binom{j}{2}$). Compare the mean time to the most recent common ancestor with $2(1 - 1/n)$, and convert it to generations for $N = 10{,}000$.

> [!success]- Solution
> ```python
> rng = random.Random(10)
> n_samples, reps = 10, 100_000
> tmrca = []
> for _ in range(reps):
>     t = 0.0
>     for j in range(n_samples, 1, -1):              # j lineages coalesce at rate j(j-1)/2 per 2N generations
>         t += rng.expovariate(j * (j - 1) / 2)
>     tmrca.append(t)
> print(f"mean TMRCA {sum(tmrca) / reps:.3f} (theory 2(1 - 1/n) = {2 * (1 - 1 / n_samples):.3f}) in units of 2N generations")
> ```
>
> ```text
> mean TMRCA 1.799 (theory 2(1 - 1/n) = 1.800) in units of 2N generations
> ```
>
> With $N = 10{,}000$, $2N \times 1.8 = 36{,}000$ generations, which is $4N(1 - 1/n)$. The last step, from 2 lineages to 1, has mean 1 unit ($2N$ generations) out of 1.8: adding more samples barely changes the depth of the genealogy, because the extra lineages coalesce quickly near the present.

## Mastery checklist

- [ ] 1 Recognized: I can write the exponential density, the survival function $e^{-\lambda t}$, the mean $1/\lambda$ and the half-life $\ln 2/\lambda$.
- [ ] 2 Understood: I can explain the constant hazard and memorylessness, and the links with the geometric distribution, the Poisson process and the first-order rate law.
- [ ] 3 Practiced: I can sample by inversion, estimate a rate from censored lifetimes, and simulate competing events with the Gillespie algorithm in Python.
- [ ] 4 Applied: on real data, I estimated a decay rate from a public mRNA time course or computed Jukes-Cantor distances from an alignment, and checked whether the exponential model fits.
- [ ] 5 Explained: I can teach how competing exponentials define substitution models and stochastic simulation, why observed differences underestimate substitutions, and how coalescence times add up in a genealogy.

## References

[^blitz5]: [[Introduction to Probability (Blitzstein)]], 2nd ed., ch. 5 "Continuous Random Variables" (the exponential distribution, memorylessness, Poisson processes).
[^blitz]: [[Introduction to Probability (Blitzstein)]], 2nd ed., treatment of the minimum of independent exponentials and of sums of exponentials (the gamma distribution).
[^openstax5]: [[Introductory Statistics (OpenStax)]], 2nd ed., ch. 5 "Continuous Random Variables" (the exponential distribution and its memoryless property).
[^6041]: [[MIT 6.041SC - Probabilistic Systems Analysis and Applied Probability]], the Poisson process (exponential interarrival times).
[^yang]: [[Molecular Evolution (Yang)]], 2014: Markov chain models of nucleotide substitution (waiting times and changes of state; the Jukes-Cantor model) and the coalescent.
[^f81]: [[Felsenstein 1981 - Evolutionary Trees from DNA Sequences]], *J Mol Evol* 17(6):368-376: the F81 model, in which substitution events occur at a constant rate and draw the new base from fixed base frequencies.
[^hartl]: [[Principles of Population Genetics (Hartl)]], 4th ed. (2006), material on the coalescent (probability $1/2N$ per generation that two gene copies coalesce; waiting times between coalescences).
[^schwan]: [[Schwanhäusser 2011 - Global Quantification of Mammalian Gene Expression Control]], *Nature* 473:337-342: mRNA and protein turnover for more than 5,000 genes in NIH3T3 cells by metabolic pulse labelling, with per-gene synthesis-degradation models.
[^gillespie]: [[Gillespie 1977 - Exact Stochastic Simulation of Coupled Chemical Reactions]], *J Phys Chem* 81(25):2340-2361: exponential waiting time to the next reaction from the total propensity, and choice of the reaction in proportion to its propensity.
