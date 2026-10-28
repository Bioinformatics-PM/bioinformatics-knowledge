---
aliases:
  - Ising Chain
  - One-Dimensional Ising Model
  - Lattice Gas Model
  - Nearest-Neighbor Model
  - Modèle d'Ising
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Two-State Model]]"
  - "[[Partition Function]]"
  - "[[Boltzmann Distribution]]"
  - "[[Matrix Multiplication]]"
  - "[[Eigenvalues and Eigenvectors]]"
related:
  - "[[Helix-Coil Transition]]"
  - "[[Cooperativity]]"
  - "[[Allosteric Regulation]]"
  - "[[Hill Function]]"
  - "[[Ligand Binding]]"
  - "[[DNA]]"
  - "[[Phase Transition]]"
  - "[[Markov Chain]]"
  - "[[Markov Chain Monte Carlo]]"
  - "[[Metropolis-Hastings Algorithm]]"
  - "[[Detailed Balance]]"
  - "[[Hidden Markov Model]]"
  - "[[Forward-Backward Algorithm]]"
  - "[[Dynamic Programming]]"
  - "[[Direct Coupling Analysis]]"
  - "[[Coevolution]]"
projects: []
sources:
  - "[[Molecular Driving Forces (Dill)]]"
  - "[[Information Theory, Inference, and Learning Algorithms (MacKay)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]]"
  - "[[Morcos 2011 - Direct-Coupling Analysis of Residue Coevolution Captures Native Contacts Across Many Protein Families]]"
---

# Ising Model

> [!abstract]
> The Ising model is a row (or lattice) of two-state units in which each unit interacts only with its neighbors. That local coupling is enough to make units switch together: binding curves become steep and transitions sharp, without any unit "knowing" about the others. In one dimension its partition function is a product of $2\times 2$ matrices, the same computation as the forward algorithm of a hidden Markov model.

## Definition

The **Ising model** assigns to each site $i$ of a lattice a two-state variable $s_i = \pm 1$ and the energy
$$E(\mathbf s) = -J\sum_{\langle ij\rangle} s_is_j - h\sum_i s_i,$$
where $\langle ij\rangle$ runs over nearest-neighbor pairs, $J$ is the coupling ($J > 0$ favors equal neighbors) and $h$ a field that favors one state.[^dill26][^mackay] Biophysics usually writes the equivalent **lattice-gas** form, with $n_i \in \{0, 1\}$ (empty or bound, closed or open) and Boltzmann weight
$$W(\mathbf n) = x^{\sum_i n_i}\,\omega^{\sum_i n_in_{i+1}},$$
where $x$ is the weight of one bound site (proportional to ligand concentration, as in the [[Two-State Model]]) and $\omega$ the extra factor for each pair of adjacent bound sites: $\omega > 1$ is cooperative, $\omega = 1$ independent, $\omega < 1$ anticooperative. With $s_i = 2n_i - 1$, $\omega = e^{4J/k_BT}$ (Exercise 2).

## Why it matters

- **The minimal model of cooperativity.** Cooperative binding along DNA or filaments, sequential models of allostery, DNA melting and helix formation are coupled two-state units ([[Cooperativity]], [[Allosteric Regulation]], [[Helix-Coil Transition]]).[^dill26]
- **Partition functions by dynamic programming.** A chain's $2^N$ configurations are summed in $O(N)$ by transfer matrices, the algorithm of HMM decoding: site occupancies are forward-backward posteriors ([[Forward-Backward Algorithm]], [[Dynamic Programming]]).
- **The benchmark of Monte Carlo sampling.** Ising models are the standard test case of Monte Carlo methods and of phase transitions ([[Markov Chain Monte Carlo]], [[Phase Transition]]).[^mackay]
- **Coevolution.** Its multi-state version, fitted to a multiple sequence alignment, predicts which residues are in contact in a protein structure (Frontier, [[Direct Coupling Analysis]]).[^morcos]

## Core (L2)

### From independent to coupled sites

With $\omega = 1$ the weight factorizes, $Z = (1 + x)^N$, occupancy is binomial and the binding curve has a Hill slope of 1 ([[Partition Function#Core (L2)]]). With $\omega > 1$, configurations in which bound sites touch are favored: bound sites gather into runs, the distribution of the number bound becomes bimodal (Worked example), and the curve steepens.

![[ising-chain-cooperative-binding.svg]]

### The transfer matrix

A configuration is a path through the states (0 or 1) of sites $1, 2, \dots, N$, and its weight is a product of factors that each involve only two consecutive sites. Collect them in the **transfer matrix** (row: state of site $i$; column: state of site $i + 1$; entry: weight added by site $i + 1$)
$$\mathbf T = \begin{pmatrix} 1 & x\\ 1 & x\omega\end{pmatrix}, \qquad Z_N = \begin{pmatrix}1 & x\end{pmatrix}\mathbf T^{N-1}\begin{pmatrix}1\\ 1\end{pmatrix}.$$
The row vector $(1, x)$ is the first site, empty or bound; each multiplication by $\mathbf T$ adds a site ([[Matrix Multiplication]]); the final sum closes the chain. This replaces $2^N$ terms by $N$ products of $2\times 2$ matrices. For a long chain $Z_N \approx C\lambda_+^N$, where $\lambda_+$ is the largest eigenvalue of $\mathbf T$ ([[Eigenvalues and Eigenvectors]]):
$$\lambda_\pm = \frac{1 + x\omega \pm \sqrt{(1 - x\omega)^2 + 4x}}{2}, \qquad \theta = \frac{\partial\ln\lambda_+}{\partial\ln x},$$
with $\theta$ the fraction of sites bound. Three results follow (Exercises 1, 3 and 4):

- **Half saturation** at $x = 1/\omega$, by symmetry between bound and empty sites.
- **Hill slope** at half saturation $n_H = \sqrt\omega$: $\omega = 100$ gives a curve ten times steeper than independent binding.
- **Runs**: at half saturation, bound sites form runs of mean length $1 + \sqrt\omega$, and correlations decay over $\xi = 1/\ln(\lambda_+/\lambda_-)$ sites.

### No phase transition in one dimension

For finite $\omega$ and $T > 0$, $\lambda_+$ is a smooth function of $x$ and $T$, and $\xi$ is finite: the occupancy changes continuously, however steeply. A one-dimensional Ising chain has no true phase transition; in two dimensions the model has one, at a critical temperature, which Monte Carlo simulation reveals.[^mackay] Biological chains are one-dimensional and finite: their transitions are sharp because $\omega$ is large, not because they are phase transitions.

### Bio: cooperative binding, allostery, DNA melting

- **Cooperative binding on a lattice.** Proteins that bind adjacent sites along DNA or a filament and contact their bound neighbors gain $\omega = e^{-\varepsilon_{\text{contact}}/k_BT}$ per contact. The figure shows how $\omega$ from 1 to 1000 turns a gradual curve into a switch.
- **Allostery.** Hemoglobin's cooperativity has two classic descriptions:[^berg] the **concerted** model, where all subunits switch together (the MWC model of [[Two-State Model#States within states: the MWC model]], an infinitely strong coupling inside the oligomer), and the **sequential** model, where each subunit changes shape when it binds and influences its neighbors, an Ising-like coupling. Both build cooperative binding out of coupled two-state units.[^pboc7]
- **DNA melting.** Each base pair is closed or open, and stacking between neighboring pairs, which dominates duplex stability,[^yakovchuk] couples them: opening a pair next to an open one breaks fewer stacks than opening an isolated pair. The duplex therefore melts in runs rather than base by base; the [[Helix-Coil Transition]] note adds the cost of starting a run (nucleation).

## Advanced (L3)

- **Transfer matrices are HMMs.** Read the sites as positions of a sequence, the two states as hidden states, $\mathbf T$ as transition-times-emission factors: $Z_N$ is the forward algorithm's total, and the probability that site $i$ is bound is $\alpha_i(1)\beta_i(1)/Z$ with forward and backward vectors, the posterior decoding of a [[Hidden Markov Model]]. Site-dependent weights $x_i$ (binding energies from a [[Position Weight Matrix]]) only change the matrix at each step. Normalized by its eigenvector, $\mathbf T$ even defines a [[Markov Chain]] along the lattice, from which the run lengths follow (Exercise 4).
- **Mean field fails in one dimension.** Replacing the neighbors of a site by their average gives the self-consistent equation $\theta = x\omega^{2\theta}/(1 + x\omega^{2\theta})$. At $x = 1/\omega$ its slope at $\theta = \frac12$ is $\frac12\ln\omega$, larger than 1 when $\omega > e^2 \approx 7.4$: the approximation then predicts two stable solutions and a discontinuous jump, a phase transition that the exact transfer matrix shows does not exist.
- **Sampling.** Metropolis Monte Carlo with single-site flips converges to the transfer-matrix answer, but slowly when $\omega$ is large: a run of bound sites must dissolve one site at a time against the coupling (Exercise 5, [[Metropolis-Hastings Algorithm]], [[Detailed Balance]]).

## Frontier (M1)

**Potts models of protein families.** Give each column of a multiple sequence alignment $q = 21$ states (20 amino acids and the gap) instead of 2, a field $h_i(a)$ per column and state, and a coupling $J_{ij}(a, b)$ per pair of columns: $P(\text{sequence}) \propto \exp\big[\sum_i h_i(a_i) + \sum_{i<j}J_{ij}(a_i, a_j)\big]$. Fitted so that its single-column and pair frequencies match the alignment, this is the maximum-entropy model with those constraints (the derivation of [[Boltzmann Distribution#Mathematical representation]] with pairwise terms). Correlations between columns spread along chains of contacts; couplings separate direct from indirect ones, and the strongest couplings recover native residue contacts across many protein families.[^morcos] This is [[Direct Coupling Analysis]], the coevolution signal used for contact prediction ([[Coevolution]], [[Contact Map]], [[Multiple Sequence Alignment]]). Exercise 6 counts its parameters.

## Mathematical representation

- Spin form: $s_i = \pm 1$, $E(\mathbf s) = -J\sum_i s_is_{i+1} - h\sum_i s_i$, $Z = \sum_{\mathbf s}e^{-\beta E(\mathbf s)}$, $\beta = 1/k_BT$.
- Lattice-gas form: $n_i = (s_i + 1)/2$, $W(\mathbf n) = x^{\sum n_i}\omega^{\sum n_in_{i+1}}$; on a ring, $\omega = e^{4\beta J}$ and $x = e^{2\beta h - 4\beta J}$.
- Transfer matrix $\mathbf T = \begin{pmatrix}1 & x\\ 1 & x\omega\end{pmatrix}$; open chain $Z_N = (1, x)\,\mathbf T^{N-1}(1, 1)^{\mathsf T}$; ring $Z_N = \operatorname{tr}(\mathbf T_s^N)$ with the symmetric form $\mathbf T_s = \begin{pmatrix}1 & \sqrt x\\ \sqrt x & x\omega\end{pmatrix}$.
- Long chain: $\ln Z_N \approx N\ln\lambda_+$, $\theta = \partial\ln\lambda_+/\partial\ln x$, $x_{1/2} = 1/\omega$, $n_H = \sqrt\omega$, mean run length $1 + \sqrt\omega$, $\xi = 1/\ln(\lambda_+/\lambda_-)$.

## Computational representation

The open chain in standard-library Python: brute force over all $2^N$ configurations against the transfer-matrix recursion, then a long chain at half saturation, with derivatives of $\ln Z$ by finite differences ([[Partition Function#Core (L2)]]). The recursion is renormalized at each site, since $Z$ grows like $\lambda_+^N$:

```python
from itertools import product
from math import exp, log, sqrt


def weight(config, x, w):
    """Lattice-gas Ising weight: x per bound site, w per pair of adjacent bound sites."""
    bound = sum(config)
    pairs = sum(a * b for a, b in zip(config, config[1:]))
    return x ** bound * w ** pairs


def z_brute(N, x, w):
    """Sum over all 2^N configurations."""
    return sum(weight(c, x, w) for c in product((0, 1), repeat=N))


def ln_z(N, x, w):
    """Transfer matrix T = [[1, x], [1, x w]]: forward recursion, renormalized at each site."""
    e, b, log_scale = 1.0, x, 0.0           # site 1 empty or bound
    for _ in range(N - 1):
        e, b = e + b, x * e + x * w * b     # next site empty (weight 1) or bound (x, times w if b)
        s = e + b
        e, b, log_scale = e / s, b / s, log_scale + log(s)
    return log_scale + log(e + b)


print(round(z_brute(12, 0.3, 5.0), 6), round(exp(ln_z(12, 0.3, 5.0)), 6))

N, h = 4000, 1e-3                           # a long chain approximates the infinite one
for w in (1, 10, 100, 1000):
    x = 1 / w                               # half saturation of the infinite chain
    lz = [ln_z(N, x * exp(k * h), w) for k in (-1, 0, 1)]
    theta = (lz[2] - lz[0]) / (2 * h * N)                 # (1/N) d lnZ / d ln x
    dtheta = (lz[2] - 2 * lz[1] + lz[0]) / (h * h * N)    # d theta / d ln x
    pairs = (ln_z(N, x, w * exp(h)) - ln_z(N, x, w * exp(-h))) / (2 * h * N)   # pairs per site
    print(w, round(theta, 3), round(4 * dtheta, 2), round(sqrt(w), 2), round(theta / (theta - pairs), 1))
```

```text
882.133012 882.133012
1 0.5 1.0 1.0 2.0
10 0.5 3.16 3.16 4.2
100 0.499 9.98 10.0 11.0
1000 0.496 31.38 31.62 32.4
```

Columns: $\omega$, $\theta$ at $x = 1/\omega$, Hill slope $4\,d\theta/d\ln x$, $\sqrt\omega$, and mean run length (bound sites per run, $\theta$ divided by the number of runs per site, $\theta$ minus the pairs per site). The slope matches $\sqrt\omega$ and the runs $1 + \sqrt\omega$. At $\omega = 1000$ the chain ends, where sites have one neighbor, lower $\theta$ slightly: 4000 sites are not quite infinite when runs are 32 long.

## Worked example

> [!example] Three coupled sites by hand (invented coupling $\omega = 50$)
> 1. **Configurations and weights.** `000`: 1; `100`, `010`, `001`: $x$ each; `110`, `011`: $x^2\omega$ each; `101`: $x^2$ (not adjacent); `111`: $x^3\omega^2$ (two adjacent pairs).
> 2. **Partition function.** $Z = 1 + 3x + (2\omega + 1)x^2 + \omega^2x^3 = 1 + 3x + 101x^2 + 2500x^3$.
> 3. **Transfer-matrix check.** $(1, x)\,\mathbf T = (1 + x,\ x + x^2\omega)$, then $(1, x)\,\mathbf T^2 = (1 + 2x + x^2\omega,\ x + x^2 + x^2\omega + x^3\omega^2)$, whose sum is the same $Z$.
> 4. **Distribution of the number bound** at $x = 0.0737$, chosen so that empty and full are equally likely ($2500x^3 = 1$): $Z = 2.769$ and $P(n = 0, 1, 2, 3) = 0.361, 0.080, 0.198, 0.361$. Independent sites at half saturation ($\omega = 1$, $x = 1$) give the binomial $0.125, 0.375, 0.375, 0.125$.
> 5. **Steepness.** $\operatorname{Var}(n) = 1.691$ against 0.75 for independent sites, so the Hill slope $\operatorname{Var}(n)/[3\theta(1 - \theta)]$ is 2.26 against 1.0 ([[Two-State Model#How steep can binding be?]]). Cooperativity means weight moved from partly filled to all-empty and all-full configurations.

## Common misconceptions

> [!warning] "Cooperativity requires all sites to switch together"
> Nearest-neighbor coupling is enough: no site interacts with distant ones, yet runs form and the binding curve steepens. All-or-none binding (the Hill function) and the concerted MWC model are limits, not requirements.

> [!warning] "The Ising model has a phase transition"
> Not in one dimension at $T > 0$: $\lambda_+$ is smooth and $\xi$ finite. The famous transition belongs to two and more dimensions.

> [!warning] "The Hill coefficient is the number of binding sites"
> It is a slope. On a long lattice $n_H = \sqrt\omega$ has nothing to do with a number of sites; for one molecule with $n$ sites it is at most $n$, and usually less.

> [!warning] "Mean field is a harmless approximation"
> In one dimension it predicts a discontinuous transition for $\omega > e^2$ that the exact solution does not have. Check approximations against an exact method when one exists.

## Exercises

> [!question] Exercise 1 (L2)
> On a ring of $N$ sites, exchange bound and empty sites ($n_i \to 1 - n_i$). Show that the weight of a configuration with $k$ bound sites and $p$ bound pairs becomes that of a model with $x' = 1/(x\omega^2)$, and deduce that half saturation occurs at $x = 1/\omega$.

> [!success]- Solution
> On a ring with $N$ bonds, $2k = 2p + (\text{bound-empty bonds})$, so the empty-empty pairs number $N - 2k + p$. After the exchange there are $N - k$ bound sites and $N - 2k + p$ bound pairs: $x^{N-k}\omega^{N-2k+p} = (x\omega)^N\,(x\omega^2)^{-k}\,\omega^p$. Up to a constant, this is the original model with $x' = 1/(x\omega^2)$, so $\theta(x) = 1 - \theta(1/(x\omega^2))$. The fixed point $x = 1/(x\omega^2)$, i.e. $x = 1/\omega$, gives $\theta = 1/2$.

> [!question] Exercise 2 (L2)
> Substitute $s_i = 2n_i - 1$ into $E = -J\sum_i s_is_{i+1} - h\sum_i s_i$ on a ring and identify $\omega$ and $x$. What does $h = 0$ correspond to?

> [!success]- Solution
> $s_is_{i+1} = 4n_in_{i+1} - 2n_i - 2n_{i+1} + 1$, and on a ring each $n_i$ appears in two bonds: $\sum_i s_is_{i+1} = 4\sum n_in_{i+1} - 4\sum n_i + N$, $\sum_i s_i = 2\sum n_i - N$. So $E = -4J\sum n_in_{i+1} - (2h - 4J)\sum n_i + \text{const}$ and $e^{-\beta E} \propto (e^{4\beta J})^{\text{pairs}}(e^{2\beta h - 4\beta J})^{\text{bound}}$: $\omega = e^{4\beta J}$, $x = e^{2\beta h - 4\beta J}$. $h = 0$ gives $x = e^{-4\beta J} = 1/\omega$: zero field is half saturation.

> [!question] Exercise 3 (L3)
> Show that the Hill slope of the infinite chain at half saturation is $n_H = 4\,d\theta/d\ln x = \sqrt\omega$.

> [!success]- Solution
> With $R = \sqrt{(1 - x\omega)^2 + 4x}$, at $x = 1/\omega$: $R = 2/\sqrt\omega$, $\lambda_+ = 1 + 1/\sqrt\omega$, $\lambda_+' = (\omega + \sqrt\omega)/2$ and $\lambda_+'' = (\omega^{5/2} - \omega^{3/2})/4$ (differentiate $R$ twice). Then $\frac{d\theta}{d\ln x} = \frac{x\lambda'}{\lambda} + \frac{x^2\lambda''}{\lambda} - \left(\frac{x\lambda'}{\lambda}\right)^2 = \frac12 + \frac{\sqrt\omega - 1}{4} - \frac14 = \frac{\sqrt\omega}{4}$, and $n_H = 4 \times \frac{\sqrt\omega}{4} = \sqrt\omega$, as the code found (9.98 for $\omega = 100$).

> [!question] Exercise 4 (L3)
> At half saturation, compute the correlation length $\xi = 1/\ln(\lambda_+/\lambda_-)$ and the mean run length of bound sites for $\omega = 100$ and $\omega = 10^4$. (Hint: along the chain, a bound site is followed by a bound one with probability $x\omega/\lambda_+$.)

> [!success]- Solution
> At $x = 1/\omega$, $\lambda_\pm = 1 \pm 1/\sqrt\omega$. $\omega = 100$: $\xi = 1/\ln(1.1/0.9) = 4.98$ sites; $\omega = 10^4$: $\xi = 1/\ln(1.01/0.99) = 50.0$ sites. The continuation probability is $x\omega/\lambda_+ = \sqrt\omega/(\sqrt\omega + 1)$, so runs are geometric with mean $1/(1 - \text{that}) = 1 + \sqrt\omega$: 11 and 101 sites. Strong coupling means long blocks of bound sites, and correlations over tens of sites.

> [!question] Exercise 5 (L3, Python)
> Sample a 50-site open chain with single-site Metropolis flips (accept with probability $\min(1, W_{\text{new}}/W_{\text{old}})$) and compare $\theta$ with the transfer-matrix value, for $(x, \omega) = (0.3, 4)$ and $(0.012, 100)$, with four independent runs of 5000 sweeps each.

> [!success]- Solution
> ```python
> import random
> from math import log
>
>
> def ln_z(N, x, w):
>     """ln Z of the open lattice-gas chain (transfer-matrix recursion, renormalized)."""
>     e, b, log_scale = 1.0, x, 0.0
>     for _ in range(N - 1):
>         e, b = e + b, x * e + x * w * b
>         s = e + b
>         e, b, log_scale = e / s, b / s, log_scale + log(s)
>     return log_scale + log(e + b)
>
>
> def metropolis_theta(N, x, w, sweeps, rng):
>     """Single-site flips accepted with min(1, weight ratio); returns the mean fraction bound."""
>     n = [0] * N
>     total, count = 0, 0
>     for sweep in range(sweeps):
>         for _ in range(N):
>             i = rng.randrange(N)
>             neighbors = (n[i - 1] if i > 0 else 0) + (n[i + 1] if i < N - 1 else 0)
>             ratio = x * w ** neighbors            # weight(bound) / weight(empty) at site i
>             if n[i]:
>                 ratio = 1 / ratio                 # proposing to unbind instead
>             if ratio >= 1 or rng.random() < ratio:
>                 n[i] = 1 - n[i]
>         if sweep >= sweeps // 10:                 # discard the first 10 % (burn-in)
>             total, count = total + sum(n), count + 1
>     return total / (count * N)
>
>
> N, h = 50, 1e-6
> rng = random.Random(5)
> for x, w in ((0.3, 4.0), (0.012, 100.0)):
>     exact = (ln_z(N, x * (1 + h), w) - ln_z(N, x * (1 - h), w)) / (2 * h * N)
>     runs = [metropolis_theta(N, x, w, 5000, rng) for _ in range(4)]
>     print(w, round(exact, 3), [round(r, 3) for r in runs])
> ```
>
> ```text
> 4.0 0.578 [0.583, 0.579, 0.579, 0.583]
> 100.0 0.73 [0.727, 0.719, 0.739, 0.716]
> ```
>
> Both samplers are centered on the exact values, since the acceptance rule satisfies [[Detailed Balance]] with respect to $W$. At $\omega = 100$ the runs scatter about three times more: long runs of bound sites change slowly under single-site moves, so successive sweeps are strongly correlated. The transfer matrix gives the exact answer in microseconds; Monte Carlo is needed only when no such solution exists, as in two or three dimensions.

> [!question] Exercise 6 (M1)
> Count the parameters of a Potts model of an alignment with $L = 100$ columns and $q = 21$ states. Compare with an alignment of a few thousand sequences, and explain why the fitted couplings, unlike raw correlations, can single out direct contacts.

> [!success]- Solution
> Fields: $Lq = 2100$. Couplings: $\binom{L}{2}q^2 = 4950 \times 441 = 2{,}182{,}950$; about $2.2\times 10^6$ in total, far more than the $10^5$ to $10^6$ amino acids of a few thousand sequences of length 100: the fit needs regularization (and gauge fixing, since fields and couplings are not separately identifiable). If residue A contacts B and B contacts C, A and C covary although they do not touch; a model with explicit pairwise terms explains the A-C correlation through the A-B and B-C couplings, leaving $J_{AC}$ small. Correlations are marginal statistics; couplings are conditional, direct interactions.[^morcos]

## Mastery checklist

- [ ] 1 Recognized: I can write the Ising energy and its lattice-gas form, and say what $J$ (or $\omega$) and $h$ (or $x$) mean for a binding lattice.
- [ ] 2 Understood: I can explain how nearest-neighbor coupling produces runs, bimodal occupancy and steep binding curves, and why a one-dimensional chain has no phase transition.
- [ ] 3 Practiced: I can compute $Z$ by brute force and by transfer matrices, and derive $x_{1/2} = 1/\omega$ and $n_H = \sqrt\omega$.
- [ ] 4 Applied: I can model cooperative binding or melting along a sequence with site-dependent weights, and validate a Monte Carlo sampler against the exact transfer-matrix result.
- [ ] 5 Explained: I can teach the link between transfer matrices and HMMs, the failure of mean field in one dimension, and how Potts models extract contacts from alignments.

## References

[^dill26]: [[Molecular Driving Forces (Dill)]], 2nd ed. (2010), ch. 26 "Cooperativity: The Helix-Coil, Ising, and Landau Models".
[^mackay]: [[Information Theory, Inference, and Learning Algorithms (MacKay)]], treatment of Ising models (Monte Carlo simulation, phase transition in two dimensions).
[^pboc7]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), ch. 7 "Two-State Systems: From Ion Channels to Cooperative Binding".
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of hemoglobin (cooperative oxygen binding; concerted and sequential models).
[^yakovchuk]: [[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]], *Nucleic Acids Research* 34(2):564-574 (stacking dominates duplex stability).
[^morcos]: [[Morcos 2011 - Direct-Coupling Analysis of Residue Coevolution Captures Native Contacts Across Many Protein Families]], *PNAS* 108(49):E1293-E1301.
