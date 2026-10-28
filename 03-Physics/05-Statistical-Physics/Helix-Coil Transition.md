---
aliases:
  - Zimm-Bragg Model
  - Helix-Coil Theory
  - Coil-Helix Transition
  - Nucleation-Propagation Model
  - Transition hélice-pelote
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - domain/chemistry
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Ising Model]]"
  - "[[Partition Function]]"
  - "[[Microstate]]"
  - "[[Two-State Model]]"
  - "[[Protein Secondary Structure]]"
related:
  - "[[Protein Folding]]"
  - "[[DNA]]"
  - "[[Nucleic Acid Hybridization]]"
  - "[[Polymerase Chain Reaction]]"
  - "[[Van 't Hoff Equation]]"
  - "[[Cooperativity]]"
  - "[[Secondary Structure Prediction]]"
  - "[[Hydrogen Bond]]"
  - "[[Phase Transition]]"
  - "[[Free Energy Landscape]]"
  - "[[Forward-Backward Algorithm]]"
projects: []
sources:
  - "[[Zimm 1959 - Theory of the Phase Transition Between Helix and Random Coil in Polypeptide Chains]]"
  - "[[Molecular Driving Forces (Dill)]]"
  - "[[Pauling 1951 - Two Hydrogen-Bonded Helical Configurations of the Polypeptide Chain]]"
  - "[[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]]"
  - "[[SantaLucia 1998 - A Unified View of Polymer, Dumbbell, and Oligonucleotide DNA Nearest-Neighbor Thermodynamics]]"
  - "[[Biochemistry (Berg)]]"
  - "[[MIT 8.592J - Statistical Physics in Biology]]"
---

# Helix-Coil Transition

> [!abstract]
> A polypeptide or a nucleic-acid duplex switches between an ordered helix and a disordered coil over a narrow range of temperature or solvent conditions. The Zimm-Bragg model explains why: extending a helix is cheap, starting one is expensive, so units convert in long runs. Two numbers, the propagation weight $s$ and the nucleation factor $\sigma$, set where the transition happens and how sharp it is.

## Definition

The **helix-coil transition** is the cooperative conversion of a chain molecule between a helix, such as the α helix of a polypeptide held by backbone hydrogen bonds[^pauling] or the double helix of a nucleic acid, and a disordered coil. In the **Zimm-Bragg model** each unit (residue) is helical (h) or coil (c): a coil unit has weight 1, a helical unit that continues a helix has weight $s$, and a helical unit that starts a helix has weight $\sigma s$, where $\sigma \ll 1$ is a correction factor for helix initiation.[^zimm][^dill26] A configuration therefore weighs
$$W = \sigma^{\,\text{number of helices}}\; s^{\,\text{number of helical units}}.$$

## Why it matters

- **Sharp transitions from weak interactions.** The model shows how a small free energy per residue becomes a transition that looks all-or-none, the statistical-physics explanation of cooperativity in biopolymers ([[Cooperativity]]). MIT 8.592J applies this toolkit to the DNA double helix, RNA secondary structure and protein folding.[^8592]
- **Helix content of peptides and proteins.** Helicity depends on the sequence (through $s$ per residue) and on chain length (through nucleation): the physics behind per-residue helix propensities ([[Protein Secondary Structure]], [[Secondary Structure Prediction]]).
- **DNA melting and primer design.** Duplex stability is predicted from nearest-neighbor stacking parameters plus an initiation term,[^santalucia] the same nucleation-propagation logic; the melting temperatures of PCR primers and hybridization probes are midpoints of such transitions ([[Polymerase Chain Reaction]], [[Nucleic Acid Hybridization]], [[Van 't Hoff Equation]]).

## Core (L2)

### Nucleation and propagation

![[zimm-bragg-helix-coil.svg]]

In the Zimm-Bragg model a hydrogen bond links each group to the third preceding one,[^zimm] so a new helix must fix several residues in helical geometry before its first bond closes: a cost paid once per helix, which is $\sigma$. Continuing a helix fixes one more residue and gains one more bond: weight $s$, above or below 1 depending on temperature and solvent. Counting alone favors the coil: in the toy model of [[Microstate#Exercises]], each residue has two non-helical conformations for one helical, so a helical residue wins only if it is favored energetically (Exercise 2).

### The partition function of a chain

Each residue is in state c or h, and its weight depends only on its own state and its predecessor's: c after anything weighs 1, h after c weighs $\sigma s$, h after h weighs $s$. The transfer matrix (row: residue $i$, column: residue $i + 1$) and the partition function are
$$\mathbf M = \begin{pmatrix} 1 & \sigma s\\ 1 & s\end{pmatrix}, \qquad Z_N = \begin{pmatrix}1 & \sigma s\end{pmatrix}\mathbf M^{N-1}\begin{pmatrix}1\\ 1\end{pmatrix},$$
where $(1, \sigma s)$ is the first residue, coil or starting a helix ([[Ising Model#The transfer matrix]]). Derivatives of $\ln Z_N$ give the averages ([[Partition Function#Core (L2)]]):
$$\theta = \frac{1}{N}\frac{\partial\ln Z_N}{\partial\ln s}\ \ (\text{fraction helical}), \qquad \nu = \frac{1}{N}\frac{\partial\ln Z_N}{\partial\ln\sigma}\ \ (\text{helices per residue}),$$
and $\theta/\nu$ is the mean number of residues per helix.

### Long chains: sigma sets the sharpness

For long chains $Z_N \approx C\lambda_1^N$ with the largest eigenvalue
$$\lambda_1 = \frac{1 + s + \sqrt{(1 - s)^2 + 4\sigma s}}{2}, \qquad \theta = \frac{d\ln\lambda_1}{d\ln s}.$$
Three results, checked numerically below: the chain is half helical at $s = 1$ whatever $\sigma$; the slope there is $d\theta/d\ln s = 1/(4\sqrt\sigma)$; and helices are on average $1 + 1/\sqrt\sigma$ residues long. A smaller $\sigma$ makes fewer, longer helices and a sharper transition: $\sigma = 10^{-4}$ gives helices of about 100 residues and a slope 25 times that of independent residues.

### Short chains: the nucleation cost

A chain of $N$ residues can hold at most a few helices, so it must recover $\sigma$ from the propagation weights of one helix: roughly $\sigma s^{N} > 1$. Short peptides are therefore much less helical than long ones under the same conditions. With $\sigma = 10^{-3}$ and $s = 1.3$, the code below gives $\theta$ = 0.095 for 10 residues, 0.54 for 20, 0.86 for 50 and 0.985 for a long chain.

### Temperature

Helix propagation is driven by enthalpy, so write $\ln s = -\frac{\Delta H}{R}\left(\frac1T - \frac1{T^*}\right)$, with $\Delta H < 0$ the propagation enthalpy per residue and $T^*$ the temperature where $s = 1$. Near $T^*$,
$$\frac{d\theta}{dT} = \frac{d\theta}{d\ln s}\,\frac{d\ln s}{dT} = \frac{1}{4\sqrt\sigma}\,\frac{\Delta H}{RT^2}:$$
cooperativity multiplies the temperature sensitivity of a single residue by $1/(4\sqrt\sigma)$. With an illustrative $\Delta H = -4$ kJ/mol per residue, a long chain melts from 90 % to 10 % helix over 36 K if $\sigma = 10^{-3}$ and 11 K if $\sigma = 10^{-4}$, whereas independent residues would spread the change over hundreds of kelvins (Exercise 4).

### Bio: peptides and DNA

- **Peptides.** The model predicts helicity that grows with chain length and with residue-specific $s$ values, and partial helices that fray at the ends, since end residues have fewer helical neighbors ([[Protein Secondary Structure]]).
- **DNA.** Base pairs replace residues and the closed (stacked) state plays the helix. Stacking between neighboring base pairs contributes most of duplex stability[^yakovchuk] and acts as the propagation weight; forming a duplex, or opening a bubble inside one, has an initiation cost. The nearest-neighbor model that predicts duplex stability sums a $\Delta H^\circ$ and a $\Delta S^\circ$ for each base-pair step, plus initiation terms,[^santalucia] and G-C-rich DNA melts at higher temperature.[^berg] For a short duplex, $\sigma \ll 1$ makes partly melted states rare and the melt is close to two-state ([[Two-State Model]], [[Van 't Hoff Equation]]); in a long heterogeneous duplex the model predicts melting region by region, A-T-rich stretches first.

## Advanced (L3)

- **It is an Ising chain.** A chain with $k$ helical residues and $p$ adjacent helical pairs contains $k - p$ helices, so $W = \sigma^{k-p}s^k = (\sigma s)^k\,(1/\sigma)^p$: the lattice gas of the [[Ising Model]] with $x = \sigma s$ and $\omega = 1/\sigma$. Its results carry over: half saturation at $x = 1/\omega$ (that is, $s = 1$), Hill slope $\sqrt\omega = 1/\sqrt\sigma$, runs of mean length $1 + 1/\sqrt\sigma$ (Exercise 3).
- **Heterogeneous sequences.** Residue-specific weights $s_i$ (and $\sigma_i$) replace $\mathbf M$ by a different matrix at each step; $Z_N$ is still computed in $O(N)$, and the probability that residue $i$ is helical comes from forward and backward vectors, exactly as posterior decoding in an HMM ([[Forward-Backward Algorithm]]). Sequence-dependent stacking free energies of DNA steps[^yakovchuk] enter the same way.
- **Limits.** The model couples only nearest neighbors. It ignores the entropy of large loops closed between distant helical regions, specific side-chain interactions further along the chain, and tertiary contacts; a protein's folding couples residues far apart in sequence and needs more than helix-coil theory ([[Protein Folding]], [[Free Energy Landscape]]). The textbook treatment places the model alongside the Ising and Landau models of cooperativity.[^dill26]

## Mathematical representation

- Configuration $\mathbf u \in \{c, h\}^N$; $W(\mathbf u) = \sigma^{n_{\text{helices}}(\mathbf u)}\,s^{n_h(\mathbf u)}$; $Z_N = \sum_{\mathbf u}W(\mathbf u) = (1, \sigma s)\,\mathbf M^{N-1}(1, 1)^{\mathsf T}$ with $\mathbf M = \begin{pmatrix}1 & \sigma s\\ 1 & s\end{pmatrix}$.
- $\theta = N^{-1}\,\partial\ln Z_N/\partial\ln s$; $\nu = N^{-1}\,\partial\ln Z_N/\partial\ln\sigma$; mean helix length $\theta/\nu$.
- Long chain: $\lambda_1 = \frac12\left[1 + s + \sqrt{(1 - s)^2 + 4\sigma s}\right]$; $\theta(s = 1) = \frac12$; $d\theta/d\ln s\,|_{s=1} = 1/(4\sqrt\sigma)$; mean helix length at $s = 1$: $1 + 1/\sqrt\sigma$.

## Computational representation

The forward recursion over the states (c, h), renormalized at each residue, checked against brute force over all $2^N$ strings; then helicity versus chain length, and the long-chain slope and helix length at $s = 1$:

```python
from itertools import product
from math import exp, log, sqrt


def ln_z(N, s, sigma):
    """Zimm-Bragg chain: forward recursion over coil (c) and helix (h) states, renormalized."""
    c, h, log_scale = 1.0, sigma * s, 0.0      # residue 1: coil (1) or first helical residue (sigma s)
    for _ in range(N - 1):
        c, h = c + h, sigma * s * c + s * h    # coil after anything; helix starts after c, grows after h
        tot = c + h
        c, h, log_scale = c / tot, h / tot, log_scale + log(tot)
    return log_scale + log(c + h)


def z_brute(N, s, sigma):
    """Sum of sigma^(number of helices) * s^(number of helical residues) over all 2^N strings."""
    total = 0.0
    for conf in product("ch", repeat=N):
        starts = sum(1 for i, r in enumerate(conf) if r == "h" and (i == 0 or conf[i - 1] == "c"))
        total += sigma ** starts * s ** conf.count("h")
    return total


def helicity(N, s, sigma, d=1e-5):
    """theta = (1/N) dlnZ/dln s; helices per residue = (1/N) dlnZ/dln sigma."""
    theta = (ln_z(N, s * exp(d), sigma) - ln_z(N, s * exp(-d), sigma)) / (2 * d * N)
    helices = (ln_z(N, s, sigma * exp(d)) - ln_z(N, s, sigma * exp(-d))) / (2 * d * N)
    return theta, helices


print(round(z_brute(8, 1.3, 0.01), 6), round(exp(ln_z(8, 1.3, 0.01)), 6))
for N in (10, 20, 50, 200, 5000):              # chain length at s = 1.3, sigma = 1e-3
    th, hx = helicity(N, 1.3, 1e-3)
    print(N, round(th, 3), round(th / hx, 1))
for sigma in (1e-2, 1e-4):                     # long chain at the midpoint s = 1
    th, hx = helicity(20_000, 1.0, sigma)
    slope = (helicity(20_000, exp(1e-3), sigma)[0] - helicity(20_000, exp(-1e-3), sigma)[0]) / 2e-3
    print(sigma, round(th, 3), round(slope, 2), round(1 / (4 * sqrt(sigma)), 2), round(th / hx, 1))
```

```text
2.036208 2.036208
10 0.095 5.7
20 0.54 13.4
50 0.859 38.2
200 0.954 118.7
5000 0.985 287.7
0.01 0.5 2.5 2.5 11.0
0.0001 0.498 24.85 25.0 100.5
```

The middle block gives, for each chain length, the fraction helical and the mean helix length: at 10 residues the few helices present are short, at 5000 residues they average 288 residues. The last two lines give $\theta$ at $s = 1$, the numerical slope, $1/(4\sqrt\sigma)$ and the mean helix length, against the predicted $1 + 1/\sqrt\sigma$ = 11 and 101.

## Worked example

> [!example] A three-residue peptide, by hand (invented $\sigma = 0.01$, $s = 1.5$)
> 1. **List the configurations.** `ccc`: 1. One helical residue (`hcc`, `chc`, `cch`): $\sigma s$ each, total $3\sigma s = 0.045$. Two adjacent (`hhc`, `chh`): $\sigma s^2$ each, total 0.045. Two separate helices (`hch`): $\sigma^2s^2 = 0.000225$. All helical (`hhh`): $\sigma s^3 = 0.03375$.
> 2. **Sum.** $Z_3 = 1 + 3\sigma s + 2\sigma s^2 + \sigma^2s^2 + \sigma s^3 = 1.12397$.
> 3. **Read off.** $P(\texttt{ccc}) = 1/Z_3 = 0.890$. Helical residues: $(1 \times 0.045 + 2 \times 0.045 + 2 \times 0.000225 + 3 \times 0.03375)/Z_3 = 0.2106$ on average, so $\theta = 0.2106/3 = 0.070$.
> 4. **Interpret.** Each continuing residue is favored ($s = 1.5 > 1$), yet the peptide is 89 % fully coil: a three-residue helix cannot repay the nucleation factor ($\sigma s^3 = 0.034 \ll 1$). The same code gives $\theta = 0.84$ for 30 residues and 0.94 for 300 with these parameters. The two-helix state `hch` pays $\sigma$ twice and is negligible: helices are few and long.

## Common misconceptions

> [!warning] "Helix formation is a two-state transition"
> Long chains contain partial helices with frayed ends and coil gaps. Only short chains with $\sigma \ll 1$, where partial states are rare, approach two-state behavior.

> [!warning] "s > 1 means the chain is helical"
> Only for long chains. A short peptide also has to pay the nucleation factor, so it needs $s$ well above 1 (Worked example).

> [!warning] "A sharp melting curve is a phase transition"
> The chain is one-dimensional, with only nearest-neighbor coupling: no true phase transition at finite temperature ([[Ising Model]]). The sharpness is set by $1/\sqrt\sigma$ and by the chain length.

> [!warning] "σ measures the strength of the helix hydrogen bonds"
> $\sigma$ multiplies the number of helices, not the number of helical residues: it is the cost of starting a helix. The per-residue stability, bonds included, is in $s$.

## Exercises

> [!question] Exercise 1 (L2)
> In a 12-residue chain, compare the weight of one 7-residue helix with that of two helices of 3 and 4 residues, and evaluate the ratio for $\sigma = 10^{-3}$.

> [!success]- Solution
> One helix: $\sigma s^7$. Two helices: $\sigma s^3 \cdot \sigma s^4 = \sigma^2s^7$. Same number of helical residues, so the ratio is $1/\sigma = 1000$: merging two helices into one removes one nucleation penalty. This is why helical residues gather into few long helices.

> [!question] Exercise 2 (L2)
> Use the toy model of [[Microstate#Exercises]]: each residue has one helical conformation of energy $\varepsilon_h$ and two coil conformations of energy 0. Express $s$ (helical residue relative to coil residue) and find the condition for $s > 1$ at 37 °C ($RT = 2.579$ kJ/mol).

> [!success]- Solution
> A coil residue weighs $2e^0 = 2$ and a helical one $e^{-\varepsilon_h/RT}$, so $s = \frac12 e^{-\varepsilon_h/RT}$. $s > 1$ requires $\varepsilon_h < -RT\ln 2 = -1.79$ kJ/mol: the helical conformation must be favored by more than the conformational entropy it loses, $R\ln 2$ per residue in this toy. With equal energies ($s = \frac12$) the coil wins, as the counting of the Microstate exercise showed.

> [!question] Exercise 3 (L3)
> Show that the Zimm-Bragg weight equals the Ising lattice-gas weight with $x = \sigma s$ and $\omega = 1/\sigma$, and deduce the Hill slope and the midpoint slope of the long chain from the [[Ising Model]] results.

> [!success]- Solution
> In a linear chain each helix of $L$ residues contains $L - 1$ adjacent helical pairs, so with $k$ helical residues and $p$ pairs there are $k - p$ helices and $W = \sigma^{k-p}s^k = (\sigma s)^k\,\sigma^{-p}$: $x = \sigma s$, $\omega = 1/\sigma$. The Ising midpoint $x = 1/\omega$ becomes $\sigma s = \sigma$, i.e. $s = 1$. The Hill slope $\sqrt\omega = 1/\sqrt\sigma$ is $4\,d\theta/d\ln x$, and at fixed $\sigma$, $d\ln x = d\ln s$, so $d\theta/d\ln s = 1/(4\sqrt\sigma)$, as the code found.

> [!question] Exercise 4 (L3, Python)
> With $\ln s = -\frac{\Delta H}{R}\left(\frac1T - \frac1{T^*}\right)$, $\Delta H = -4$ kJ/mol per residue and $T^* = 320$ K (invented), compute for long chains the temperatures where $\theta = 0.9$ and $\theta = 0.1$, for $\sigma = 10^{-2}$, $10^{-3}$ and $10^{-4}$. Compare the width with the estimate $\ln 81\,\sqrt\sigma\,RT^{*2}/|\Delta H|$ from the midpoint slope.

> [!success]- Solution
> ```python
> from math import exp, log, sqrt
>
> R = 8.314462618e-3                 # kJ/(mol K)
> dH, Tm = -4.0, 320.0               # helix propagation enthalpy per residue (kJ/mol) and T where s = 1 (invented)
>
>
> def theta_long(s, sigma):
>     """Long-chain helicity d ln(lambda)/d ln s, lambda = [1 + s + sqrt((1 - s)^2 + 4 sigma s)] / 2."""
>     root = sqrt((1 - s) ** 2 + 4 * sigma * s)
>     lam = (1 + s + root) / 2
>     dlam = (1 + (s - 1 + 2 * sigma) / root) / 2
>     return s * dlam / lam
>
>
> def s_of_T(T):
>     return exp(-dH / R * (1 / T - 1 / Tm))     # ln s = -(dH/R)(1/T - 1/Tm)
>
>
> def crossing(target, sigma, lo=150.0, hi=600.0):
>     """Temperature where theta = target (theta decreases with T), by bisection."""
>     for _ in range(100):
>         mid = (lo + hi) / 2
>         lo, hi = (mid, hi) if theta_long(s_of_T(mid), sigma) > target else (lo, mid)
>     return mid
>
>
> for sigma in (1e-2, 1e-3, 1e-4):
>     t90, t10 = crossing(0.9, sigma), crossing(0.1, sigma)
>     print(sigma, round(t90, 1), round(t10, 1), round(t10 - t90, 1),
>           round(log(81) * sqrt(sigma) * R * Tm ** 2 / abs(dH), 1))
> ```
>
> ```text
> 0.01 271.9 388.8 116.8 93.5
> 0.001 303.0 339.0 36.0 29.6
> 0.0001 314.4 325.8 11.4 9.4
> ```
>
> The 90-to-10 % width shrinks from 117 K to 11 K as $\sigma$ drops a hundredfold, roughly as $\sqrt\sigma$. The midpoint-slope estimate is close for small $\sigma$ and too low for $\sigma = 10^{-2}$, where the curve is broad and not symmetric in $T$. The same weak residue enthalpy gives a sharp melt only when nucleation is costly.

## Mastery checklist

- [ ] 1 Recognized: I can state the Zimm-Bragg weights ($1$, $s$, $\sigma s$) and say what $s$ and $\sigma$ represent.
- [ ] 2 Understood: I can explain why helices form in few long runs, why short peptides are poorly helical, and why $\sigma$ sets the sharpness.
- [ ] 3 Practiced: I can compute $Z_N$, $\theta$ and the mean helix length with a transfer matrix, and derive the long-chain results.
- [ ] 4 Applied: I can relate the model to DNA melting with nearest-neighbor parameters and to per-residue helix probabilities along a sequence.
- [ ] 5 Explained: I can teach the mapping onto the Ising chain, the temperature sensitivity amplified by $1/(4\sqrt\sigma)$, and the limits of a nearest-neighbor model for protein folding.

## References

[^zimm]: [[Zimm 1959 - Theory of the Phase Transition Between Helix and Random Coil in Polypeptide Chains]], *The Journal of Chemical Physics* 31(2):526 (bonding between each group and the third preceding one; statistical weight for helix continuation and correction factor for helix initiation).
[^dill26]: [[Molecular Driving Forces (Dill)]], 2nd ed. (2010), ch. 26 "Cooperativity: The Helix-Coil, Ising, and Landau Models".
[^pauling]: [[Pauling 1951 - Two Hydrogen-Bonded Helical Configurations of the Polypeptide Chain]], *PNAS* 37(4):205-211 (the α helix as a hydrogen-bonded configuration of the backbone).
[^yakovchuk]: [[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]], *Nucleic Acids Research* 34(2):564-574 (stacking free energies of base-pair steps; stacking dominates duplex stability).
[^santalucia]: [[SantaLucia 1998 - A Unified View of Polymer, Dumbbell, and Oligonucleotide DNA Nearest-Neighbor Thermodynamics]], *PNAS* 95(4):1460-1465 (unified nearest-neighbor $\Delta H^\circ$ and $\Delta S^\circ$ with initiation terms).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of DNA denaturation (G-C-rich DNA melts at higher temperature).
[^8592]: [[MIT 8.592J - Statistical Physics in Biology]]: biopolymers part (DNA double helix, RNA secondary structure, protein folding).
