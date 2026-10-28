---
aliases:
  - Z
  - Canonical Partition Function
  - Sum over States
  - Fonction de partition
tags:
  - type/concept
  - domain/physics
  - domain/chemistry
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Boltzmann Distribution]]"
  - "[[Microstate]]"
  - "[[Boltzmann Entropy]]"
  - "[[Helmholtz Free Energy]]"
  - "[[Expected Value]]"
  - "[[Variance]]"
  - "[[Partial Derivative]]"
related:
  - "[[Statistical Ensemble]]"
  - "[[Two-State Model]]"
  - "[[Ising Model]]"
  - "[[Helix-Coil Transition]]"
  - "[[Free Energy Landscape]]"
  - "[[Ligand Binding]]"
  - "[[Transcription Factor]]"
  - "[[Gene Regulation]]"
  - "[[Heat Capacity]]"
  - "[[Calorimetry]]"
  - "[[Generating Function]]"
  - "[[RNA Secondary Structure Prediction]]"
  - "[[Forward-Backward Algorithm]]"
  - "[[Binding Free Energy]]"
  - "[[Numerical Stability]]"
projects: []
sources:
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Molecular Driving Forces (Dill)]]"
  - "[[Understanding Molecular Simulation (Frenkel)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Partition Function

> [!abstract]
> The partition function $Z$ adds up the Boltzmann weights of every state of a system. Once you have it, each probability is a weight divided by $Z$, averages and fluctuations are derivatives of $\ln Z$, and the free energy is $F = -k_BT\ln Z$: a table of states and weights is enough to predict a binding curve, a melting curve or a calorimetry peak.

## Definition

For a system in equilibrium with a heat bath at temperature $T$, with microstates $i$ of energy $E_i$, the (canonical) partition function is
$$Z = \sum_i e^{-E_i/k_BT} = \sum_\ell g_\ell\, e^{-E_\ell/k_BT},$$
the second sum running over energy levels $\ell$ of degeneracy $g_\ell$. It normalizes the [[Boltzmann Distribution]], $p_i = e^{-E_i/k_BT}/Z$, and its logarithm is the [[Helmholtz Free Energy]], $F = -k_BT\ln Z$.[^pboc6][^dill]

## Why it matters

- **Occupancy from a table.** The probability that a promoter carries RNA polymerase, or a site a [[Transcription Factor]], is a ratio of sums of weights: the "states and weights" bookkeeping of physical biology turns copy numbers and binding energies into occupancies.[^pboc6] Thermodynamic models of [[Gene Regulation]] are built this way (Advanced).
- **Ensemble predictions in RNA folding and HMMs.** RNA folding programs sum Boltzmann weights over all secondary structures to obtain an ensemble free energy and base-pair probabilities ([[RNA Secondary Structure Prediction]], [[Boltzmann Distribution#Advanced (L3)]]); the forward algorithm of a [[Hidden Markov Model]] computes the same kind of sum over paths ([[Forward-Backward Algorithm]]).
- **Melting curves and calorimetry.** The excess heat capacity of a melting protein is the variance of its enthalpy, a second derivative of $\ln Z$ ([[Heat Capacity]], [[Calorimetry]]).
- **Binding free energies.** Molecular simulations estimate ratios of partition functions, not partition functions ([[Binding Free Energy]], Frontier).[^frenkel]

## Core (L2)

### The states-and-weights table

Every partition-function calculation follows one recipe:[^pboc6]

1. **Enumerate** the states: microstates, or coarse states with their multiplicities.
2. Give each an **energy** $E_s$ and a **multiplicity** $g_s$ ([[Microstate]]).
3. Compute its **weight** $w_s = g_s\, e^{-E_s/k_BT}$. Only energy differences matter, so measure energies from a convenient reference state.
4. **Sum**: $Z = \sum_s w_s$.
5. **Read off** probabilities $p_s = w_s/Z$ and averages $\langle A\rangle = \sum_s p_s A_s$.

The Worked example applies it to RNA polymerase and a promoter.

### Averages and fluctuations are derivatives of ln Z

With $\beta = 1/k_BT$, differentiating $Z = \sum_i e^{-\beta E_i}$ brings down a factor $-E_i$ in every term:
$$\langle E\rangle = -\frac{\partial \ln Z}{\partial\beta}, \qquad \operatorname{Var}(E) = \langle E^2\rangle - \langle E\rangle^2 = \frac{\partial^2 \ln Z}{\partial\beta^2} = k_BT^2\, C_V,$$
where $C_V = \partial\langle E\rangle/\partial T$ is the [[Heat Capacity]] per molecule (per mole, replace $k_B$ by $R$). The trick works for any variable that enters the weights: if state $s$ has $n_s$ bound ligands and weight $\propto x^{n_s}$ with $x = c/K_d$, then $\langle n\rangle = \partial\ln Z/\partial\ln x$ and $\operatorname{Var}(n) = \partial^2\ln Z/\partial(\ln x)^2$. $Z$ is a [[Generating Function]]: a binding curve is its first logarithmic derivative, and the steepness of that curve is the second.

### The free energy is ln Z

From $\ln p_i = -\beta E_i - \ln Z$, the entropy $S = -k_B\sum_i p_i\ln p_i$ equals $k_B(\beta\langle E\rangle + \ln Z)$, hence
$$F = \langle E\rangle - TS = -k_BT\ln Z, \qquad S = -\frac{\partial F}{\partial T}.$$
For $g$ states all of energy 0, $Z = g$ and $F = -k_BT\ln g = -TS$ with $S = k_B\ln g$, the [[Boltzmann Entropy]]. In general $Z$ is the **effective number of accessible states**, each discounted by its Boltzmann factor, and $F$ is that number on a logarithmic energy scale.

### Macrostates have partial partition functions

Grouping microstates into a macrostate $A$ (folded, bound, open) gives a partial sum $Z_A = \sum_{i\in A} w_i$, a free energy $F_A = -k_BT\ln Z_A$, and
$$p_A = \frac{Z_A}{Z}, \qquad \frac{p_B}{p_A} = \frac{Z_B}{Z_A} = e^{-(F_B - F_A)/k_BT}.$$
This is why the [[Two-State Model]] uses free energies rather than energies: each of its two states is a sum over many microstates. An equilibrium constant is a ratio of partial partition functions ([[Chemical Equilibrium]]).

### Independent parts multiply

If the energy is a sum over independent parts, $E = E^{(1)} + E^{(2)}$, the sum over all combinations factorizes: $Z = Z_1 Z_2$ and $F = F_1 + F_2$. For $N$ identical independent binding sites, $Z = (1 + x)^N$ and $\langle n\rangle = Nx/(1 + x)$: occupancy is binomial (Exercise 2). Interactions between sites break the factorization, and cooperativity is what appears in its place ([[Ising Model]]).

## Advanced (L3)

### Thermodynamic models of gene regulation

Add a repressor that excludes the polymerase from the promoter. The states are: empty (weight 1), polymerase bound ($x_P = \frac{P}{N_{NS}}e^{-\Delta\varepsilon_P/k_BT}$), repressor bound ($x_R = \frac{R}{N_{NS}}e^{-\Delta\varepsilon_R/k_BT}$); both together are forbidden. Then
$$p_{\text{bound}} = \frac{x_P}{1 + x_P + x_R}, \qquad \text{fold-change} = \frac{p_{\text{bound}}(R)}{p_{\text{bound}}(0)} = \frac{1 + x_P}{1 + x_P + x_R} \approx \frac{1}{1 + \frac{R}{N_{NS}}e^{-\Delta\varepsilon_R/k_BT}}$$
for a weak promoter ($x_P \ll 1$). Such models predict expression from repressor copy numbers and binding energies,[^pboc] and a [[Position Weight Matrix]] score can stand in for $-\Delta\varepsilon$ ([[Boltzmann Distribution#Exercises]]). Exercise 3 computes one.

### What a calorimeter measures

![[two-state-unfolding-heat-capacity.svg]]

For two-state unfolding, $Z = 1 + e^{-\Delta G(T)/RT}$ per mole of protein, with $\Delta G = \Delta H(1 - T/T_m)$ when $\Delta C_p = 0$. The enthalpy is either 0 or $\Delta H$, so $\operatorname{Var}(H) = p_U(1 - p_U)\,\Delta H^2$ and
$$C_{\text{ex}}(T) = \frac{\operatorname{Var}(H)}{RT^2} = \frac{\Delta H^2}{RT^2}\,p_U(1 - p_U), \qquad C_{\max} \approx \frac{\Delta H^2}{4RT_m^2}.$$
The peak area is $\int C_{\text{ex}}\,dT = \Delta H$, the calorimetric enthalpy, while the height grows as $\Delta H^2$. The enthalpy deduced from the shape, $\Delta H_{vH} = 4RT_m^2 C_{\max}/\Delta H_{\text{cal}}$ (van 't Hoff, see [[Van 't Hoff Equation]]), equals the area only if the whole molecule melts as one unit: smaller independent units give the same area but a lower, broader peak (Exercise 4; measurement in [[Heat Capacity#Advanced (L3)]]).

### Sums over chains are matrix products

A chain of $N$ two-state units has $2^N$ states, but when each unit interacts only with its neighbors the sum collapses into a product of $2\times 2$ matrices, computed in $O(N)$: the transfer matrix of the [[Ising Model]] and the [[Helix-Coil Transition]], and the same dynamic-programming logic as the forward algorithm ([[Dynamic Programming]]). The RNA ensemble sums of [[Boltzmann Distribution#Advanced (L3)]] replace the counting recursion of [[Microstate#Exercises]] by a weighted one.

## Frontier (M1)

### Free energies from simulations

The $Z$ of a protein in water is never computed; ratios are, because a ratio is an average. For two potential energies $U_0$ and $U_1$ over the same configurations (ligand coupled or not, wild type or mutant),
$$\frac{Z_1}{Z_0} = \frac{\int e^{-\beta U_1}}{\int e^{-\beta U_0}} = \left\langle e^{-\beta(U_1 - U_0)}\right\rangle_0 \quad\Rightarrow\quad \Delta F = -k_BT\ln\left\langle e^{-\beta\,\Delta U}\right\rangle_0,$$
an exact identity (free energy perturbation): sample state 0, average the exponential of the energy change. The free-energy methods of molecular simulation, such as perturbation in small steps and thermodynamic integration, refine this ratio;[^frenkel] applied to a ligand in a binding site and in solution, they give relative [[Binding Free Energy|binding free energies]]. The weakness is statistical: the average is dominated by rare configurations of state 0 that resemble state 1, and in one direction the estimator has infinite variance (Exercise 5).

## Mathematical representation

- $\beta = 1/k_BT$; states $i$ with energies $E_i$ (or levels $\ell$ with degeneracies $g_\ell$); $Z(\beta) = \sum_i e^{-\beta E_i}$; $p_i = e^{-\beta E_i}/Z$.
- $F = -k_BT\ln Z$; $U = \langle E\rangle = -\partial_\beta\ln Z$; $\operatorname{Var}(E) = \partial_\beta^2\ln Z = k_BT^2C_V$; $S = (U - F)/T = -\partial F/\partial T$.
- Conjugate variables: if $E_i = E_i^0 - \lambda X_i$, then $\langle X\rangle = k_BT\,\partial_\lambda\ln Z$ and $\operatorname{Var}(X) = (k_BT)^2\,\partial_\lambda^2\ln Z$. For ligands, $\lambda$ is the chemical potential and $X$ the number bound, so $\partial/\partial(\beta\lambda) = \partial/\partial\ln x$ ([[Statistical Ensemble]]).
- Log-sum-exp: $\ln\sum_i e^{a_i} = a^* + \ln\sum_i e^{a_i - a^*}$ with $a^* = \max_i a_i$, so every term of the second sum is at most 1.

## Computational representation

Store states as (energy, degeneracy) pairs, energies in kJ/mol with $R = N_A k_B$ from the exact CODATA constants,[^nist] and work with $\ln Z$, never with $Z$, as HMM and softmax code does ([[Numerical Stability]]):

```python
from math import exp, log

R = 8.314462618e-3          # kJ/(mol K), exact (CODATA)


def log_sum_exp(a):
    """ln(sum_i exp(a_i)), shifted by the maximum so that nothing overflows."""
    m = max(a)
    return m + log(sum(exp(x - m) for x in a))


def thermo(states, T):
    """states: (energy in kJ/mol, degeneracy) pairs. Returns ln Z, probabilities, U, Var(E), F, S."""
    RT = R * T
    log_w = [log(g) - E / RT for E, g in states]          # ln of each Boltzmann weight
    lnZ = log_sum_exp(log_w)
    p = [exp(lw - lnZ) for lw in log_w]
    U = sum(pi * E for pi, (E, _) in zip(p, states))       # mean energy
    var = sum(pi * (E - U) ** 2 for pi, (E, _) in zip(p, states))
    F = -RT * lnZ                                          # free energy
    return lnZ, p, U, var, F, (U - F) / T                  # S = (U - F) / T


states = [(0.0, 1), (4.0, 3), (8.0, 10)]   # closed, intermediate, open (invented)
T = 310.15
lnZ, p, U, var, F, S = thermo(states, T)
print(f"ln Z = {lnZ:.4f}, p = {[round(x, 3) for x in p]}")
print(f"U = {U:.3f} kJ/mol, F = {F:.3f} kJ/mol, S = {1000 * S:.2f} J/(mol K)")

# check: U = -d lnZ / d beta and Var(E) = R T^2 C, by finite differences
h = 1e-4
lnZ_at = lambda t: thermo(states, t)[0]
beta = 1 / (R * T)
dlnZ_dbeta = (lnZ_at(1 / (R * (beta + h))) - lnZ_at(1 / (R * (beta - h)))) / (2 * h)
C = (thermo(states, T + 0.01)[2] - thermo(states, T - 0.01)[2]) / 0.02
print(f"-dlnZ/dbeta = {-dlnZ_dbeta:.3f}   Var(E) = {var:.3f}   R T^2 C = {R * T * T * C:.3f}")

# absolute force-field energies overflow a naive sum, not the log-sum-exp
big = [(-2000.0, 1), (-1995.0, 1)]
try:
    print(sum(g * exp(-E / (R * T)) for E, g in big))
except OverflowError as err:
    print("naive sum:", err)
print(f"log-sum-exp: F = {thermo(big, T)[4]:.2f} kJ/mol")
```

```text
ln Z = 0.7350, p = [0.48, 0.305, 0.216]
U = 2.944 kJ/mol, F = -1.895 kJ/mol, S = 15.60 J/(mol K)
-dlnZ/dbeta = 2.944   Var(E) = 10.005   R T^2 C = 10.005
naive sum: math range error
log-sum-exp: F = -2000.35 kJ/mol
```

The finite differences confirm $\langle E\rangle = -\partial\ln Z/\partial\beta$ and $\operatorname{Var}(E) = RT^2C$. The open state has the highest energy but the most microstates, so it still holds 22 % of the population. Force-field energies are hundreds of $RT$, so `exp` overflows; shifting by the maximum loses nothing, because only differences matter.

## Worked example

> [!example] RNA polymerase on a promoter: a states-and-weights table (toy numbers, invented)
> A bacterium has $P = 500$ polymerases, all bound to DNA: either at one of $N_{NS} = 5\times 10^6$ nonspecific sites (energy $\varepsilon_{NS}$ each) or at one promoter (energy $\varepsilon_S$), with $\Delta\varepsilon = \varepsilon_S - \varepsilon_{NS} = -8\,k_BT$.[^pboc6]
>
> | State | Energy | Multiplicity | Weight |
> |---|---|---|---|
> | promoter empty | $P\varepsilon_{NS}$ | $\binom{N_{NS}}{P}$ | $\binom{N_{NS}}{P}e^{-\beta P\varepsilon_{NS}}$ |
> | promoter occupied | $(P-1)\varepsilon_{NS} + \varepsilon_S$ | $\binom{N_{NS}}{P-1}$ | $\binom{N_{NS}}{P-1}e^{-\beta[(P-1)\varepsilon_{NS} + \varepsilon_S]}$ |
>
> 1. **Ratio of weights.** $\binom{N_{NS}}{P-1}\big/\binom{N_{NS}}{P} = \frac{P}{N_{NS} - P + 1} \approx \frac{P}{N_{NS}} = 10^{-4}$; the energies contribute $e^{-\beta\Delta\varepsilon} = e^{8} = 2981$. Occupied over empty: $x = 0.298$.
> 2. **Partition function**, relative to the empty state: $Z = 1 + x = 1.298$.
> 3. **Occupancy**: $p_{\text{bound}} = x/(1 + x) = 0.230$.
> 4. **Reading.** $p_{\text{bound}} = \dfrac{(P/N_{NS})\,e^{-\beta\Delta\varepsilon}}{1 + (P/N_{NS})\,e^{-\beta\Delta\varepsilon}}$ is a binding curve with $P/N_{NS}$ in place of $c/c_0$ ([[Boltzmann Distribution#Bio: two-state occupancy of conformations and binding sites]]): the genome is the "solvent", and millions of weak decoy sites compete with one strong site.
>
> The binomials have thousands of digits, so the code works with their logarithms:
>
> ```python
> from math import exp, lgamma
>
>
> def log_binom(n, k):
>     """ln C(n, k) via log-gamma: C(5e6, 500) has thousands of digits."""
>     return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)
>
>
> def p_bound(P, N_ns, d_eps):
>     """P polymerases, N_ns nonspecific sites, d_eps = eps_S - eps_NS in units of kT."""
>     lw_empty = log_binom(N_ns, P)                  # all P on nonspecific DNA
>     lw_bound = log_binom(N_ns, P - 1) - d_eps      # one on the promoter (common factors removed)
>     return 1 / (1 + exp(lw_empty - lw_bound))
>
>
> P, N_ns = 500, 5_000_000                           # invented, bacterial-scale numbers
> print([round(p_bound(P, N_ns, d), 4) for d in (-4, -6, -8, -10)])
> print([round(p_bound(P, n, -8), 3) for n in (5_000_000, 50_000, 5_000)])
> x = P / N_ns * exp(8)                              # the approximation P/N_ns
> print(round(x / (1 + x), 4))
> ```
>
> ```text
> [0.0054, 0.0388, 0.2297, 0.6878]
> [0.23, 0.968, 0.997]
> 0.2296
> ```
>
> The exact binomials and the approximation agree (0.2297 and 0.2296). Every $2\,k_BT$ of binding energy multiplies $x$ by $e^2 = 7.4$, and shrinking the decoy pool to $5\times 10^4$ sites nearly saturates the promoter.

## Common misconceptions

> [!warning] "Z is only a normalization constant"
> $\ln Z$ is the free energy; its derivatives are the mean energy, the heat capacity and the binding curve; ratios of partial sums are equilibrium constants. Normalizing is the least interesting thing it does.

> [!warning] "Unlikely states can be left out of the table"
> Each nonspecific site is unlikely, but there are millions: dropping them takes the promoter of the Worked example from 0.23 to nearly 1. A class of states can be omitted only when its **total** weight, multiplicity included, is negligible.

> [!warning] "Fluctuations are noise to average away"
> The variance of the energy is $k_BT^2$ times the heat capacity, and the variance of the number of bound ligands is the steepness of the binding curve. Fluctuations are thermodynamic quantities that experiments measure.

## Exercises

> [!question] Exercise 1 (L2)
> Three levels have energies $0$, $1$ and $2\,k_BT$ and degeneracies 1, 2 and 3. Compute $Z$, the probability of each level, $\langle E\rangle$, $F$ and $S$ (in units of $k_BT$ and $k_B$).

> [!success]- Solution
> Weights $1$, $2e^{-1} = 0.7358$ and $3e^{-2} = 0.4060$, so $Z = 2.1418$ and $p = (0.467, 0.344, 0.190)$. $\langle E\rangle = 0.344 + 2 \times 0.190 = 0.723\,k_BT$; $F = -\ln 2.1418 = -0.762\,k_BT$; $S/k_B = \langle E\rangle/k_BT - F/k_BT = 1.484$, more than $\ln 1 = 0$ because six microstates share the probability.

> [!question] Exercise 2 (L2)
> A protein has $N$ identical independent binding sites, each bound with relative weight $x = c/K_d$. Write $Z$, then obtain $\langle n\rangle$ and $\operatorname{Var}(n)$ as derivatives with respect to $\ln x$. Which distribution is this?

> [!success]- Solution
> Each site contributes $1 + x$, so $Z = (1 + x)^N$. $\langle n\rangle = x\,\partial_x\ln Z = Nx/(1 + x)$ and $\operatorname{Var}(n) = x\,\partial_x\langle n\rangle = Nx/(1 + x)^2 = Np(1 - p)$ with $p = x/(1 + x)$: a [[Binomial Distribution]]. Expanding $(1 + x)^N$, the coefficient $\binom{N}{n}$ of $x^n$ counts the microstates with $n$ ligands bound.

> [!question] Exercise 3 (L3)
> In the regulation model of the Advanced section, take $N_{NS} = 5\times 10^6$, $\Delta\varepsilon_R = -15\,k_BT$ and the polymerase of the Worked example ($x_P = 0.298$). Compute the fold-change for $R = 10$ and $R = 100$ repressors, exactly and in the weak-promoter approximation. How many repressors give a 100-fold repression in the approximation? (Invented parameters.)

> [!success]- Solution
> $x_R = \frac{R}{N_{NS}}e^{15} = 0.6538\,R$. $R = 10$: $x_R = 6.54$, approximation $1/(1 + 6.54) = 0.133$, exact $(1 + 0.298)/(1.298 + 6.54) = 0.166$. $R = 100$: $x_R = 65.4$, giving 0.0151 and 0.0195. The approximation overstates repression when the promoter is not weak. A 100-fold repression needs $x_R = 99$, so $R = 99\,N_{NS}e^{-15} \approx 151$.

> [!question] Exercise 4 (L3)
> A protein unfolds in two states with $\Delta H = 300$ kJ/mol at $T_m = 330$ K ($\Delta C_p = 0$, invented). Show that its excess heat capacity peaks near $\Delta H^2/4RT_m^2$ and evaluate it. Then model the protein as two independent halves, each unfolding with $\Delta H/2$ at the same $T_m$: compare the areas, the peak heights and the ratio $\Delta H_{vH}/\Delta H_{\text{cal}}$.

> [!success]- Solution
> $C_{\text{ex}} = \frac{\Delta H^2}{RT^2}p_U(1 - p_U)$ and $p_U(1 - p_U) \le \frac14$, reached at $T_m$ where $p_U = \frac12$: $C_{\max} \approx \frac{300^2}{4 \times 8.314\times 10^{-3} \times 330^2} = 24.85$ kJ mol⁻¹ K⁻¹. Independent halves add their partition functions' logarithms, so their heat capacities add: $C_{\max} = 2 \times \frac{150^2}{4RT_m^2} = 12.42$, half the height, while the area stays $2 \times 150 = 300$ kJ/mol. Then $\Delta H_{vH} = 4RT_m^2C_{\max}/\Delta H_{\text{cal}} = 150$ kJ/mol and the ratio is 0.5: a ratio below 1 says that the unit melting cooperatively is smaller than the molecule ([[Calorimetry]]).

> [!question] Exercise 5 (M1, Python)
> A bead is held by a spring of stiffness $k_0 = 1$ or $k_1 = 4$ (in $k_BT/\text{nm}^2$, invented). Show that $\Delta F = F_1 - F_0 = \frac{k_BT}{2}\ln(k_1/k_0)$. Then estimate it by free energy perturbation, sampling state 0 (forward) or state 1 (reverse), with $10^2$, $10^4$ and $10^6$ samples, and explain the difference.

> [!success]- Solution
> $Z_k = \int e^{-kx^2/2k_BT}\,dx = \sqrt{2\pi k_BT/k}$, so $\Delta F = -k_BT\ln(Z_1/Z_0) = \frac{k_BT}{2}\ln 4 = 0.693\,k_BT$.
> ```python
> import random
> from math import exp, log, sqrt
>
> k0, k1 = 1.0, 4.0                              # spring constants in kT/nm^2 (invented)
> exact = 0.5 * log(k1 / k0)                     # Delta F / kT = (1/2) ln(k1/k0)
>
>
> def fep(k_from, k_to, n, rng):
>     """-ln < exp(-(U_to - U_from)) >_from, sampling the 'from' state exactly."""
>     sd = 1 / sqrt(k_from)
>     acc = 0.0
>     for _ in range(n):
>         x = rng.gauss(0, sd)
>         acc += exp(-0.5 * (k_to - k_from) * x * x)
>     return -log(acc / n)
>
>
> rng = random.Random(1)
> print(f"exact {exact:.4f}")
> for n in (100, 10_000, 1_000_000):
>     fwd = fep(k0, k1, n, rng)                  # sample the broad well, perturb to the narrow one
>     rev = -fep(k1, k0, n, rng)                 # sample the narrow well, perturb to the broad one
>     print(n, round(fwd, 4), round(rev, 4))
> ```
>
> ```text
> exact 0.6931
> 100 0.6196 0.5488
> 10000 0.6905 0.7132
> 1000000 0.6942 0.6853
> ```
>
> The forward estimate converges; the reverse one wanders. In state 1, $x$ has variance $1/4$ and the averaged quantity $e^{+1.5x^2}$ has a finite mean (2) but an infinite variance, because $\langle e^{3x^2}\rangle$ diverges once $2 \times 3 \times \frac14 > 1$: rare large $|x|$ dominate the sum. Sampling the broad state to reach the narrow one is safe, the reverse is not, and practical calculations insert intermediate states so that neighbors overlap.[^frenkel]

## Mastery checklist

- [ ] 1 Recognized: I can define $Z$ as the sum of Boltzmann weights and state $F = -k_BT\ln Z$.
- [ ] 2 Understood: I can explain why derivatives of $\ln Z$ give averages and fluctuations, why macrostates have partial partition functions, and why independent parts multiply.
- [ ] 3 Practiced: I can build a states-and-weights table for a binding problem and compute $\ln Z$, probabilities, $\langle E\rangle$ and $\operatorname{Var}(E)$ stably in Python.
- [ ] 4 Applied: I can model promoter occupancy and repression from copy numbers and binding energies, and read a calorimetry peak as an enthalpy fluctuation.
- [ ] 5 Explained: I can teach the van 't Hoff test of two-state behavior and why free energy perturbation converges in one direction and not in the other.

## References

[^pboc6]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), ch. 6 "Entropy Rules!" (Boltzmann distribution and partition function; states and weights for ligand-receptor and polymerase-promoter binding).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of transcriptional regulation (thermodynamic models of repression).
[^dill]: [[Molecular Driving Forces (Dill)]], 2nd ed. (2010), treatment of the Boltzmann law and partition functions.
[^frenkel]: [[Understanding Molecular Simulation (Frenkel)]], 2nd ed. (2002), treatment of free energy calculations.
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA values of the Boltzmann and Avogadro constants (exact since the 2019 SI revision), $R = N_A k$.
