---
aliases:
  - Statistical Mechanics
  - Physique statistique
tags:
  - type/moc
  - domain/physics
  - level/L1
  - level/L2
prerequisites:
  - "[[Thermodynamics]]"
  - "[[Probability]]"
projects: []
sources:
  - "[[MIT 8.592J - Statistical Physics in Biology]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[MIT 8.01SC - Classical Mechanics]]"
---

# Statistical Physics

> [!abstract]
> How thermodynamics emerges from counting microscopic states: the Boltzmann distribution and the partition function, two-state and cooperative models, Brownian motion and detailed balance. The toolkit behind protein folding, binding, DNA melting and molecular simulation.

## Why it matters for bioinformatics

- **Binding is a partition function.** The probability that a site is occupied (a ligand on a receptor, a transcription factor on a promoter) is a ratio of Boltzmann-weighted states; [[Two-State Model|two-state]] and [[Ising Model|Ising]] models add cooperativity.
- **Folding and melting are cooperative transitions.** [[Free Energy Landscape|Free energy landscapes]], the [[Helix-Coil Transition]] and DNA melting are treated with one statistical toolkit, which is also applied to sequence information and biopolymer structure in MIT 8.592J.[^8592]
- **Simulations sample the Boltzmann distribution.** Molecular dynamics and Monte Carlo generate [[Statistical Ensemble|ensembles]]; [[Detailed Balance]] is the condition on which Metropolis sampling, and hence [[Markov Chain Monte Carlo]] in Bayesian phylogenetics, is built.
- **Entropy is one idea.** [[Boltzmann Entropy]] and [[Shannon Entropy]] have the same form; information content in sequence logos is the second.

## Before you start

- [[Thermodynamics]]: all of Stage 1, and [[Helmholtz Free Energy]].
- [[Probability]]: [[Probability Distribution]], [[Expected Value]], [[Variance]], [[Normal Distribution]].
- [[Discrete Mathematics]]: [[Combinatorics]] (counting microstates).
- [[Mechanics]]: [[Potential Energy]], [[Harmonic Oscillator]]; energy and momentum are the entry point to this subdomain.[^801]

## Learning path

> [!tip] What to skip compared with a full physics licence
> Quantum statistics (Fermi-Dirac, Bose-Einstein, blackbody radiation), the grand-canonical formalism beyond what binding problems need, critical phenomena and the renormalization group, the exact solution of the 2D Ising model, mean-field theory of magnets, transport coefficients from kinetic theory, and fluctuation theorems.

### Stage 1 - Foundations (L1)

1. [[Microstate]] (L1): distinguish microstates from macrostates and count microstates (multiplicity) with combinatorics. Bio: the number of conformations of a chain.
2. [[Boltzmann Entropy]] (L1): use $S = k_B \ln W$ and connect it to thermodynamic entropy. Bio: the conformational entropy lost on folding or binding.
3. [[Boltzmann Distribution]] (L1): compute state probabilities $p_i \propto e^{-E_i / k_B T}$ and population ratios. Bio: occupancy of conformations and binding states; the Arrhenius factor.

### Stage 2 - Core (L2)

4. [[Partition Function]] (L2): compute Z, average energies and $F = -k_B T \ln Z$ from a table of states and weights. Bio: the probability that a ligand or a transcription factor is bound.
5. [[Statistical Ensemble]] (L2): distinguish microcanonical, canonical and grand canonical ensembles; time versus ensemble averages (ergodicity). Bio: which ensemble a simulation samples (NVE, NVT, NPT).
6. [[Equipartition Theorem]] (L2): assign $\frac{1}{2} k_B T$ per quadratic degree of freedom. Bio: temperature in molecular dynamics; calibrating an optical trap from the fluctuations of a bead.
7. [[Two-State Model]] (L2): compute the occupancy of a two-state system as a function of an energy difference or a ligand concentration. Bio: ion channel gating, ligand binding, folded and unfolded proteins.
8. [[Ising Model]] (L2): model coupled two-state units and see cooperativity emerge from nearest-neighbor interactions (transfer matrix in one dimension). Bio: cooperative binding, allostery, DNA melting.
9. [[Helix-Coil Transition]] (L2): model helix formation with nucleation and propagation parameters (Zimm-Bragg). Bio: sharp cooperative transitions of peptides and DNA.
10. [[Free Energy Landscape]] (L2): describe a system by its free energy along reaction coordinates: basins, barriers, the folding funnel, the potential of mean force. Bio: protein folding and conformational change.
11. [[Brownian Motion]] (L2): describe the random thermal motion of a particle in a fluid and its mean-square displacement $\langle x^2 \rangle = 2Dt$ in one dimension. Bio: motion of proteins and vesicles in the cytoplasm.
12. [[Langevin Equation]] (L2): write Newton's law with friction and a random force and relate the two (fluctuation and dissipation). Bio: Langevin thermostats and Brownian dynamics simulations.
13. [[Detailed Balance]] (L2): state the equilibrium condition on transition rates and use it to design a Monte Carlo move. Bio: the [[Metropolis-Hastings Algorithm]]; kinetic schemes that must close thermodynamic cycles.
14. [[Nonequilibrium Steady State]] (L2): recognize driven systems with constant fluxes that break detailed balance. Bio: living cells, ATP-driven motors and pumps, kinetic proofreading.

## Uses from other domains

- [[Markov Chain Monte Carlo]] and [[Metropolis-Hastings Algorithm]] ([[Bayesian Statistics]]): samplers built to satisfy [[Detailed Balance]]; [[Reversible Markov Chain]] ([[Stochastic Processes]]) is its mathematical form.
- [[Random Walk]] and [[Markov Chain]] ([[Stochastic Processes]]): the discrete and mathematical counterparts of [[Brownian Motion]] and of transition-rate dynamics.
- [[Shannon Entropy]] ([[Probability]]): the information-theoretic twin of [[Boltzmann Entropy]].
- [[Protein Folding]], [[Cooperativity]], [[Allosteric Regulation]] ([[Biochemistry]]).
- [[Diffusion]], [[Binding Free Energy]], [[Freely Jointed Chain]] ([[Biophysics]]); [[Molecular Dynamics Simulation]] ([[Structural Bioinformatics]]): ensembles, equipartition, Langevin thermostats.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 8.592J - Statistical Physics in Biology]] | MIT | L3-M1 | Statistical physics applied to DNA information, biopolymers (DNA, RNA secondary structure, protein folding), motors, membranes and networks; read after Stage 2[^8592] |

## Reference books

- [[Physical Biology of the Cell (Phillips)]]: ch. 5 "Mechanical and Chemical Equilibrium in the Living Cell" (free energy and equilibrium in cells).[^pboc]
- Molecular Driving Forces (Dill), planned source note: the standard introduction to statistical thermodynamics for chemists and biologists.

## Lab projects

No Lab project implements statistical physics directly. [[07-evolution-simulator]] uses the same mathematics ([[Markov Chain]], [[Random Number Generation]]) that a Monte Carlo or Brownian dynamics simulation would.

## References

Scope: 8.592J assumes a prior statistical mechanics course,[^8592] which this MOC supplies at L1-L2 with the biological applications of PBoC.[^pboc] Physics-licence topics without biological use are skipped (see the tip above).

[^8592]: [[MIT 8.592J - Statistical Physics in Biology]]: course topics and prerequisites (assumes statistical mechanics).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., ch. 5 "Mechanical and Chemical Equilibrium in the Living Cell".
[^801]: [[MIT 8.01SC - Classical Mechanics]]: energy and momentum as the entry point to statistical mechanics.
