---
aliases:
  - Boltzmann Factor
  - Boltzmann Weight
  - Boltzmann Law
  - Canonical Distribution
  - Gibbs Distribution
  - Distribution de Boltzmann
tags:
  - type/concept
  - domain/physics
  - domain/chemistry
  - domain/bioinformatics
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Microstate]]"
  - "[[Boltzmann Entropy]]"
  - "[[Exponential Function]]"
  - "[[Probability Distribution]]"
  - "[[Temperature]]"
related:
  - "[[Partition Function]]"
  - "[[Two-State Model]]"
  - "[[Statistical Ensemble]]"
  - "[[Gibbs Free Energy]]"
  - "[[Chemical Equilibrium]]"
  - "[[Activation Energy]]"
  - "[[Conformational Analysis]]"
  - "[[Ligand Binding]]"
  - "[[RNA Secondary Structure Prediction]]"
  - "[[Hidden Markov Model]]"
  - "[[Logistic Regression]]"
  - "[[Detailed Balance]]"
  - "[[Simulated Annealing]]"
projects: []
sources:
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[MIT 8.592J - Statistical Physics in Biology]]"
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[MIT 6.036 - Introduction to Machine Learning]]"
  - "[[Information Theory, Inference, and Learning Algorithms (MacKay)]]"
---

# Boltzmann Distribution

> [!abstract]
> At temperature $T$, a molecule visits each of its states with a probability proportional to $e^{-E/k_BT}$: low-energy states are favored, every extra $k_BT$ of energy costs a factor $e \approx 2.7$, and this one rule sets the populations of conformations, the occupancy of binding sites and, in disguise, the scores of many bioinformatics algorithms.

## Definition

For a system in thermal equilibrium with its surroundings at absolute temperature $T$, the probability of finding it in [[Microstate|microstate]] $i$, of energy $E_i$, is
$$p_i = \frac{e^{-E_i/k_BT}}{Z}, \qquad Z = \sum_j e^{-E_j/k_BT},$$
where $k_B$ is the Boltzmann constant, $e^{-E_i/k_BT}$ the **Boltzmann factor** (statistical weight) of state $i$, and $Z$ the [[Partition Function]], the sum of the weights of all states.[^pboc]

## Why it matters

- **Occupancy is a ratio of weights.** The fraction of a protein in each conformation, or of a receptor or promoter with a ligand or transcription factor bound, is computed by listing states and their Boltzmann weights, the approach of the two-state and lattice models of physical biology.[^pboc][^pboc7]
- **RNA folding is an ensemble.** Folding programs compute not only the minimum free energy structure but Boltzmann-weighted probabilities over all secondary structures, a statistical-physics treatment of biopolymers ([[RNA Secondary Structure Prediction]]).[^8592]
- **Scores are log-probabilities.** Substitution scores are log-odds ratios,[^durbin2] and HMM algorithms multiply probabilities along paths:[^durbin3] exponentiating a score gives a Boltzmann weight (L3).
- **The same formula runs machine learning and search.** The softmax layer of a classifier,[^6036] Metropolis sampling[^mackay] and [[Simulated Annealing]] are Boltzmann distributions with a chosen "energy" and "temperature".
- **The Arrhenius factor** $e^{-E_a/RT}$ of reaction rates is a Boltzmann factor ([[Activation Energy]]).

## Core (L1)

### The thermal energy scale

Energies only matter compared with $k_BT$ (per molecule) or $RT = N_A k_BT$ (per mole), computed from the exact CODATA constants:[^nist]

| | $k_BT$ | $k_BT$ (pN nm) | $RT$ (kJ/mol) | $RT\ln 10$ (kJ/mol) |
|---|---:|---:|---:|---:|
| 25 °C (298.15 K) | $4.116 \times 10^{-21}$ J | 4.12 | 2.479 | 5.71 |
| 37 °C (310.15 K) | $4.282 \times 10^{-21}$ J | 4.28 | 2.579 | 5.94 |

Rule of thumb at 37 °C: every 5.9 kJ/mol of energy difference divides a population by 10 ([[Temperature]]).

### Population ratios do not need Z

For two microstates, $Z$ cancels:
$$\frac{p_j}{p_i} = e^{-(E_j - E_i)/k_BT}.$$
At 37 °C, a state higher by $\Delta E$ = 1, 2.5, 5, 10, 20 and 40 kJ/mol is populated relative to the lower one by 0.679, 0.379, 0.144, 0.0207, $4.3 \times 10^{-4}$ and $1.8 \times 10^{-7}$. Differences of a few $RT$ leave both states populated; differences of tens of $RT$ make the upper state effectively absent. Only energy **differences** matter: adding the same constant to every $E_i$ multiplies all weights and $Z$ by the same factor. Absolute probabilities, by contrast, need $Z$, the sum over **all** accessible states: forgetting a state inflates the others. The [[Partition Function]] note develops $Z$ as a computational object (averages, $F = -k_BT\ln Z$).

### Degenerate states: energy against counting

If a macrostate contains $g$ microstates of the same energy $E$, its weight is
$$g\,e^{-E/k_BT} = e^{-(E - T k_B\ln g)/k_BT},$$
the exponent of an energy minus $T$ times a [[Boltzmann Entropy]]: a free energy. A higher-energy state can dominate if it has enough microstates, and raising $T$ favors it (Worked example). This is why populations of coarse states (folded, bound) follow free energies, $p_B/p_A = e^{-\Delta G/RT}$, and why an equilibrium constant is a Boltzmann ratio ([[Gibbs Free Energy]], [[Chemical Equilibrium]]).

### Bio: two-state occupancy of conformations and binding sites

![[two-state-binding-occupancy.svg]]

**Two conformations** A and B (closed or open channel, folded or unfolded protein) with $\Delta E = E_B - E_A$: $p_B = 1/(1 + e^{\Delta E/k_BT})$, a sigmoid that equals 1/2 at $\Delta E = 0$.[^pboc7] Conformational populations of small molecules follow the same rule ([[Conformational Analysis]]).

**Ligand binding** in the lattice model:[^pboc] $L$ ligands occupy $\Omega$ cells of a solution, one receptor can bind one ligand with energy $\Delta\varepsilon$ relative to solution. Counting placements, the bound and unbound states have weights in the ratio $\binom{\Omega}{L-1} e^{-\Delta\varepsilon/k_BT} \big/ \binom{\Omega}{L} \approx (L/\Omega)\, e^{-\Delta\varepsilon/k_BT}$ for $L \ll \Omega$, so
$$p_{\text{bound}} = \frac{(c/c_0)\,e^{-\Delta\varepsilon/k_BT}}{1 + (c/c_0)\,e^{-\Delta\varepsilon/k_BT}} = \frac{c}{c + K_d}, \qquad K_d = c_0\, e^{\Delta\varepsilon/k_BT},$$
with $c$ the ligand concentration and $c_0$ the reference concentration set by the cell volume. Half occupancy needs $\Delta\varepsilon = k_BT\ln(c/c_0)$: $-13.8\,k_BT$ at 1 µM with $c_0 = 1$ M, because binding removes the ligand's translational entropy ([[Boltzmann Entropy#Deeper (L2)]]). Each tenfold increase in $c$ shifts the curve by $\ln 10 = 2.3\,k_BT$. Cooperativity and titration curves are developed in [[Two-State Model]] and [[Ligand Binding]].

### The Arrhenius factor

A reaction proceeds through molecules that reach the top of an energy barrier $E_a$, and their fraction scales as $e^{-E_a/RT}$: the Arrhenius equation $k = A\,e^{-E_a/RT}$ ([[Activation Energy]]). For $E_a = 50$ kJ/mol, warming from 25 °C to 37 °C multiplies the rate by 2.18.

## Deeper (L2)

### Derivation from counting

Put the system in contact with a large reservoir, the pair being isolated with total energy $E_{\text{tot}}$. When the system is in microstate $i$, the reservoir has energy $E_{\text{tot}} - E_i$ and $W_R(E_{\text{tot}} - E_i)$ microstates; all joint microstates are equally likely ([[Microstate]]), so $p_i \propto W_R(E_{\text{tot}} - E_i) = e^{S_R(E_{\text{tot}} - E_i)/k_B}$. Expanding the reservoir entropy to first order, with $\partial S_R/\partial E = 1/T$:[^pboc]
$$p_i \propto e^{S_R(E_{\text{tot}})/k_B}\, e^{-E_i/k_BT} \propto e^{-E_i/k_BT}.$$
The exponential comes from the reservoir: a state that takes energy $E_i$ leaves the surroundings with fewer microstates.

### Averages and limits

Any observable has the thermal average $\langle A \rangle = \sum_i p_i A_i$ (for example the mean energy, or the fraction of time a site is bound, see [[Expected Value]]). As $T \to 0$, all probability collapses on the lowest-energy states; as $T \to \infty$, all microstates become equally likely (not all energy levels: degenerate levels keep their weight $g$). Temperature therefore tunes between optimization (only the minimum counts) and pure counting (only multiplicity counts).

## Advanced (L3)

- **RNA partition functions.** Summing $e^{-G(s)/RT}$ over all secondary structures $s$ of a sequence gives $Z$; the probability of a structure is its weight over $Z$, and summing over the structures that contain a pair gives base-pair probabilities. The minimum free energy structure is only the single most probable state, often with a modest probability (Exercise 5).[^8592] The counting recursion of [[Microstate#Exercises]] becomes this sum when each structure contributes its weight instead of 1.
- **Log-odds scores are energies.** A substitution score is $s(a,b) = \frac{1}{\lambda}\ln\frac{p_{ab}}{q_a q_b}$, with target frequencies $p_{ab}$ and background frequencies $q_a$, $q_b$.[^durbin2] Inverting, $p_{ab} = q_a q_b\, e^{\lambda s(a,b)}$: Boltzmann weights with energy $-s$ and "temperature" $1/\lambda$. In an [[Hidden Markov Model]], the joint probability of a sequence and a path is a product of transition and emission probabilities, $e^{-E(\pi)}$ with $E = -\ln P$; the Viterbi algorithm finds the minimum-energy path, the forward algorithm sums over all paths as a partition function does.[^durbin3]
- **Softmax.** A classifier turns scores $z_i$ into probabilities $e^{z_i/\tau}/\sum_j e^{z_j/\tau}$:[^6036] a Boltzmann distribution with $E_i = -z_i$ and $k_BT = \tau$. With two classes it is the logistic function of the score difference ([[Logistic Regression]]), the two-state occupancy above.
- **Sampling and annealing.** The Metropolis method accepts a move that changes the energy by $\Delta E$ with probability $\min(1, e^{-\Delta E/k_BT})$, which makes the Boltzmann distribution the stationary distribution of the chain;[^mackay] see [[Detailed Balance]] and [[Metropolis-Hastings Algorithm]]. Lowering $T$ step by step concentrates the samples on low-energy states: [[Simulated Annealing]].
- **Scope.** The derivation assumes equilibrium with a heat bath. Processes driven by a continuous energy supply (ATP-consuming motors, pumps, proofreading) need not follow Boltzmann populations ([[Nonequilibrium Steady State]]).

## Mathematical representation

- $\beta = 1/(k_BT)$; microstates $i$ with energies $E_i$; weights $w_i = e^{-\beta E_i}$; $Z = \sum_i w_i$; $p_i = w_i / Z$.
- Levels $\ell$ with degeneracy $g_\ell$: $Z = \sum_\ell g_\ell e^{-\beta E_\ell}$, $p_\ell = g_\ell e^{-\beta E_\ell}/Z$.
- Shift invariance: $E_i \to E_i + C$ gives $Z \to e^{-\beta C} Z$ and leaves every $p_i$ unchanged.
- Two states: $p_B = 1/(1 + e^{\beta \Delta E})$, the logistic function of $-\beta\Delta E$.
- Lattice binding: $p_{\text{bound}} = c/(c + K_d)$ with $K_d = c_0 e^{\beta\Delta\varepsilon}$.
- Maximum entropy: maximizing $S = -k_B\sum_i p_i \ln p_i$ under $\sum_i p_i = 1$ and $\sum_i p_i E_i = U$, with Lagrange multipliers $\alpha$ and $\lambda$, gives $-k_B(\ln p_i + 1) - \alpha - \lambda E_i = 0$, so $p_i \propto e^{-\lambda E_i/k_B}$: the Boltzmann distribution, with $\lambda = 1/T$. It is the least-biased distribution with a given mean energy.

## Computational representation

Store states as parallel lists of energies (and degeneracies), with $R$ from the exact CODATA constants ($R = N_A k_B$); compute weights after subtracting the minimum energy, which avoids overflow and changes nothing (shift invariance). The partition function is then a plain sum:

```python
from math import exp

R = 8.314462618e-3        # kJ/(mol K), exact (CODATA)


def boltzmann(energies, T, degeneracies=None):
    """(Z, probabilities) with Z = sum_i g_i exp(-(E_i - E_min) / RT); energies in kJ/mol."""
    g = degeneracies or [1] * len(energies)
    e_min = min(energies)
    weights = [gi * exp(-(e - e_min) / (R * T)) for gi, e in zip(g, energies)]
    Z = sum(weights)                       # partition function (relative to e_min)
    return Z, [w / Z for w in weights]


T = 310.15
Z, p = boltzmann([0.0, 1.5, 6.0], T)                 # three conformations (invented energies)
print(round(Z, 4), [round(x, 3) for x in p])
_, p_shift = boltzmann([100.0, 101.5, 106.0], T)     # same differences, shifted energies
print(p_shift == p)
# a closed state (1 microstate) versus an open state 6 kJ/mol higher but with 20 microstates
for t_c in (4, 37, 60):
    _, (p_closed, p_open) = boltzmann([0.0, 6.0], t_c + 273.15, degeneracies=[1, 20])
    print(t_c, round(p_closed, 3), round(p_open, 3))
```

```text
1.6566 [0.604, 0.337, 0.059]
True
4 0.403 0.597
37 0.339 0.661
60 0.304 0.696
```

Softmax is the same computation with scores in place of negative energies:

```python
from math import exp


def softmax(scores: list[float], tau: float = 1.0) -> list[float]:
    """Boltzmann distribution with energies E_i = -score_i and temperature kT = tau."""
    m = max(scores)
    w = [exp((s - m) / tau) for s in scores]
    Z = sum(w)
    return [wi / Z for wi in w]


scores = [2.0, 1.0, 0.1]                  # invented classifier scores (logits)
for tau in (0.1, 1.0, 10.0):
    print(tau, [round(p, 3) for p in softmax(scores, tau)])
# two classes: softmax reduces to the logistic function of the score difference
a, b = 1.3, -0.4
print(round(softmax([a, b])[0], 6), round(1 / (1 + exp(-(a - b))), 6))
```

```text
0.1 [1.0, 0.0, 0.0]
1.0 [0.659, 0.242, 0.099]
10.0 [0.366, 0.331, 0.303]
0.845535 0.845535
```

Low $\tau$ approaches the argmax (the ground state), high $\tau$ the uniform distribution, exactly the temperature limits of L2.

## Worked example

> [!example] Energy versus multiplicity: a loop that opens (toy model, invented numbers)
> A protein loop is either closed (one conformation, energy 0) or open (20 conformations, each 6 kJ/mol higher).
> 1. **Weights at 37 °C** ($RT = 2.579$ kJ/mol): closed $1$; open $20\, e^{-6/2.579} = 20 \times 0.0976 = 1.95$.
> 2. **Partition function**: $Z = 1 + 1.95 = 2.95$.
> 3. **Populations**: $p_{\text{closed}} = 1/2.95 = 0.339$, $p_{\text{open}} = 0.661$. Each open conformation is 10 times less likely than the closed one, yet the open **state** wins by number.
> 4. **Free-energy reading**: $\Delta G = \Delta E - T\Delta S = 6 - RT\ln 20 = 6 - 7.73 = -1.73$ kJ/mol, and $e^{1.73/2.579} = 1.95$, the same ratio.
> 5. **Temperature**: the code gives $p_{\text{open}}$ = 0.597 at 4 °C and 0.696 at 60 °C: heating favors the state with more microstates.

## Common misconceptions

> [!warning] "The lowest-energy state is the most populated"
> True for single microstates, false for macrostates: a state with many microstates can outweigh a lower-energy one (Worked example). Populations follow free energies, not energies.

> [!warning] "$e^{-E/k_BT}$ is the probability of the state"
> It is a weight. Probabilities need the normalization by $Z$, which depends on every other state; only ratios of weights are probabilities without further work.

> [!warning] "$k_B$ and kJ/mol go together"
> $e^{-5/(k_BT)}$ with 5 in kJ/mol is meaningless: per-mole energies go with $RT$ (2.58 kJ/mol at 37 °C), per-molecule energies with $k_BT$ ($4.28 \times 10^{-21}$ J).

## Exercises

> [!question] Exercise 1 (L1)
> Two conformations differ by 4 kJ/mol. Compute the population ratio (upper/lower) at 25 °C and at 37 °C.

> [!success]- Solution
> $e^{-4/2.479} = 0.199$ at 25 °C and $e^{-4/2.579} = 0.212$ at 37 °C: heating brings the populations closer.

> [!question] Exercise 2 (L1)
> What energy gap puts 99 % of the molecules in the lower of two states at 37 °C? Express it in kJ/mol and in units of $RT$.

> [!success]- Solution
> $p_{\text{low}} = 1/(1 + e^{-\Delta E/RT}) = 0.99$ gives $e^{\Delta E/RT} = 99$, $\Delta E = RT\ln 99 = 2.579 \times 4.595 = 11.85$ kJ/mol, about $4.6\,RT$.

> [!question] Exercise 3 (L2)
> Toy unfolding model (invented): the unfolded state is $\Delta H = 150$ kJ/mol above the folded one and has $\Delta S = 0.45$ kJ mol⁻¹ K⁻¹ more entropy. Treat it as a two-state system with $\Delta G = \Delta H - T\Delta S$. Compute the unfolded fraction at 25, 37, 50, 60 and 70 °C and the melting temperature.

> [!success]- Solution
> $p_U = 1/(1 + e^{\Delta G/RT})$. $\Delta G$ = 15.83, 10.43, 4.58, 0.08 and −4.42 kJ/mol give $p_U$ = 0.0017, 0.0172, 0.154, 0.493 and 0.825. $T_m = \Delta H/\Delta S = 333.3$ K (60.2 °C), where $\Delta G = 0$. The transition is sharp because $\Delta G$ changes by $\Delta S \times 10$ K = 4.5 kJ/mol, almost $2RT$, every 10 degrees; see [[Two-State Model]].

> [!question] Exercise 4 (L2)
> In the lattice model with $c_0 = 1$ M, a transcription factor binds its site with $\Delta\varepsilon = -15\,k_BT$. Compute $K_d$ and the occupancy at 1 µM.

> [!success]- Solution
> $K_d = c_0 e^{\Delta\varepsilon/k_BT} = e^{-15}$ M $= 3.06 \times 10^{-7}$ M $\approx 0.31$ µM. $p_{\text{bound}} = c/(c + K_d) = 1/(1 + 0.306) = 0.766$.

> [!question] Exercise 5 (L3, Python)
> Five secondary structures of an RNA have free energies −42.0, −40.5, −40.0, −35.0 and −30.0 kJ/mol (invented; a real sequence has many more). Compute their Boltzmann probabilities and the ensemble free energy $G_{\text{ens}} = -RT\ln\sum_s e^{-G_s/RT}$ at 310.15 K, 100 K and 30 K.

> [!success]- Solution
> ```python
> from math import exp, log
>
> R = 8.314462618e-3                       # kJ/(mol K)
> G = [-42.0, -40.5, -40.0, -35.0, -30.0]  # free energies of 5 structures, kJ/mol (invented)
>
> for T in (310.15, 100.0, 30.0):
>     RT = R * T
>     w = [exp(-(g - min(G)) / RT) for g in G]
>     Z = sum(w)
>     G_ens = min(G) - RT * log(Z)         # ensemble free energy -RT ln(sum exp(-G_i/RT))
>     print(T, [round(x / Z, 3) for x in w], round(G_ens, 2))
> ```
> Output: `310.15 [0.477, 0.267, 0.22, 0.032, 0.005] -43.91`, `100.0 [0.797, 0.131, 0.072, 0.0, 0.0] -42.19`, `30.0 [0.997, 0.002, 0.0, 0.0, 0.0] -42.0`. At body temperature the minimum free energy structure holds less than half of the population, and two alternatives within $0.8\,RT$ hold another half: predicting one structure hides this. $G_{\text{ens}}$ is below the minimum because alternatives add weight; as $T \to 0$ it converges to the minimum and the ensemble collapses onto it.

> [!question] Exercise 6 (L3)
> A position weight matrix gives a sequence $x$ the log-odds score $S = \log_2[P(x \mid \text{site})/P(x \mid \text{background})]$ ([[Position Weight Matrix]]). With prior probability $\pi$ that a position is a site, show that the posterior probability of a site is a two-state Boltzmann occupancy in $S$. Evaluate it for $\pi = 10^{-3}$ and $S$ = 8 and 12 bits.

> [!success]- Solution
> By [[Bayes' Theorem]], $P(\text{site} \mid x) = \dfrac{\pi\, 2^{S}}{\pi\, 2^{S} + (1 - \pi)} = \dfrac{1}{1 + \frac{1-\pi}{\pi}\, 2^{-S}}$. This is $1/(1 + e^{\Delta E/k_BT})$ with "energy" $\Delta E/k_BT = \ln\frac{1-\pi}{\pi} - S\ln 2$: the score plays minus an energy and the prior plays the concentration term of the binding curve. For $\pi = 10^{-3}$: $S = 8$ gives $1/(1 + 999/256) = 0.204$; $S = 12$ gives 0.804. A score must exceed $\log_2 999 \approx 10$ bits before a hit is more likely real than not, a midpoint like $\Delta\varepsilon = k_BT\ln(c/c_0)$.

## Mastery checklist

- [ ] 1 Recognized: I can write $p_i \propto e^{-E_i/k_BT}$, name the Boltzmann factor and the partition function, and give $k_BT$ and $RT$ at 37 °C.
- [ ] 2 Understood: I can explain why ratios do not need $Z$, why degeneracy turns energies into free energies, and derive the distribution from a system plus reservoir.
- [ ] 3 Practiced: I can compute populations, two-state and binding occupancies and softmax probabilities in Python with a numerically stable sum.
- [ ] 4 Applied: I can interpret base-pair probabilities, log-odds scores and HMM path probabilities as Boltzmann weights, and estimate the binding energy a site needs at a given concentration.
- [ ] 5 Explained: I can teach the temperature limits (optimization versus counting), the link to the Arrhenius factor and to simulated annealing, and when equilibrium assumptions fail in cells.

## References

[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of statistical mechanics (Boltzmann distribution, partition function, lattice model of ligand-receptor binding).
[^pboc7]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), ch. 7 "Two-State Systems: From Ion Channels to Cooperative Binding".
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA recommended values: Boltzmann constant and Avogadro constant (exact since the 2019 SI revision), $R = N_A k$.
[^8592]: [[MIT 8.592J - Statistical Physics in Biology]]: biopolymers part (RNA secondary structure treated with statistical physics).
[^durbin2]: [[Biological Sequence Analysis (Durbin)]], ch. 2 "Pairwise alignment" (substitution scores as log-odds ratios).
[^durbin3]: [[Biological Sequence Analysis (Durbin)]], ch. 3 "Markov chains and hidden Markov models" (Viterbi and forward algorithms).
[^6036]: [[MIT 6.036 - Introduction to Machine Learning]]: supervised learning, classification models (multiclass outputs).
[^mackay]: [[Information Theory, Inference, and Learning Algorithms (MacKay)]], treatment of Monte Carlo methods (Metropolis method).
