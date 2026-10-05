---
aliases:
  - Thermodynamique
tags:
  - type/moc
  - domain/physics
  - domain/chemistry
  - level/L1
  - level/L2
prerequisites:
  - "[[Mechanics]]"
  - "[[Calculus]]"
  - "[[General Chemistry]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[MIT - Course 7 Biology]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
---

# Thermodynamics

> [!abstract]
> Macroscopic energy bookkeeping: temperature, heat, work, internal energy, the laws of thermodynamics and entropy (L1), then reversibility, free energy, phase transitions and calorimetry (L2), the tools used to describe folding, binding and melting.

## Why it matters for bioinformatics

- **Stability is thermodynamics.** Folding and binding are measured as free-energy differences; DNA and protein melting curves are cooperative transitions ([[Phase Transition]]); [[Calorimetry]] measures their enthalpy.
- **Life runs against the second law.** The [[Laws of Thermodynamics]] explain why a cell needs a constant supply of free energy ([[ATP]]) to stay ordered.
- **It is the macroscopic face of statistical physics.** [[Thermodynamic Entropy]] meets [[Boltzmann Entropy]] and [[Shannon Entropy]] in [[Statistical Physics]]: the same logarithm of a count of states.
- **Physical chemistry builds on it.** [[Enthalpy]], [[Gibbs Free Energy]] and [[Chemical Equilibrium]] ([[Physical Chemistry]]) start from the first and second laws.

## Before you start

- [[Mechanics]]: [[Work (Physics)]], [[Kinetic Energy]], [[Conservation of Energy]], [[Pressure]].
- [[Calculus]]: [[Derivative]], [[Integral]], [[Partial Derivative]] (for Stage 2).
- [[General Chemistry]]: [[Mole]].

## Learning path

> [!tip] What to skip compared with a full physics licence
> Heat engines, refrigerators and the Carnot cycle, Maxwell relations and systematic partial-derivative identities, real gases (van der Waals), heat transfer (conduction, convection, radiation), phase diagrams beyond melting, and the third law beyond its statement. Chemical thermodynamics ([[Enthalpy]], [[Gibbs Free Energy]], [[Chemical Potential]]) is in [[Physical Chemistry]].

### Stage 1 - Foundations (L1)

1. [[Thermodynamic System]] (L1): define system and surroundings, open, closed and isolated systems, state variables, state functions and equilibrium. Bio: a cell is an open system.
2. [[Temperature]] (L1): define temperature through thermal equilibrium (zeroth law), use kelvins, and read $k_B T$ as the thermal energy scale. Bio: $k_B T \approx 4.1$ pN nm at room temperature, the yardstick of molecular energies.
3. [[Heat]] (L1): distinguish heat (energy transfer) from temperature (a state variable).
4. [[Heat Capacity]] (L1): compute heat from a temperature change; molar and specific heat capacities. Bio: proteins change heat capacity when they unfold.
5. [[Internal Energy]] (L1): define U as a state function and distinguish it from heat and work.
6. [[Laws of Thermodynamics]] (L1): state and apply the zeroth, first (energy conservation, $\Delta U = Q + W$), second and third laws.
7. [[Ideal Gas Law]] (L1): use $PV = nRT = N k_B T$ and relate R to the Boltzmann constant. Bio: the ideal model behind osmotic pressure; gas exchange.
8. [[Thermodynamic Entropy]] (L1): define an entropy change as $\delta Q_{rev}/T$ and apply the second law to decide spontaneity. Bio: the hydrophobic effect and folding are entropy stories.

### Stage 2 - Core (L2)

9. [[Reversible Process]] (L2): distinguish reversible, irreversible and quasi-static processes; relate reversibility to maximum work. Bio: why motors and pumps dissipate heat.
10. [[Helmholtz Free Energy]] (L2): define $F = U - TS$ and its minimum at constant temperature and volume; obtain the free energies from U by Legendre transform. Bio: the bridge to $F = -k_B T \ln Z$ in [[Statistical Physics]].
11. [[Phase Transition]] (L2): describe first-order transitions, latent heat and cooperative transitions. Bio: lipid membrane melting, DNA melting, two-state protein unfolding.
12. [[Calorimetry]] (L2): measure heat changes; interpret differential scanning calorimetry and isothermal titration calorimetry. Bio: ΔH, heat-capacity change and melting temperature of unfolding; ΔH, $K_d$ and stoichiometry of binding.

## Uses from other domains

- [[Enthalpy]], [[Gibbs Free Energy]], [[Chemical Equilibrium]], [[Van 't Hoff Equation]] ([[Physical Chemistry]]).
- [[Boltzmann Entropy]], [[Partition Function]] ([[Statistical Physics]]): the microscopic explanation of entropy and free energy.
- [[Protein Folding]] and [[ATP]] ([[Biochemistry]]): stability and energy coupling.
- [[Binding Free Energy]] ([[Biophysics]]): calorimetry data and enthalpy-entropy decomposition.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 5.111SC - Principles of Chemical Science]] | MIT | L1 | Thermodynamics part: energy and spontaneity, from the chemist's side[^5111] |

## Reference books

- [[University Physics (OpenStax)]]: Volume 2, thermodynamics part (before electricity and magnetism).[^up]
- [[Physical Biology of the Cell (Phillips)]]: ch. 5 "Mechanical and Chemical Equilibrium in the Living Cell".[^pboc]
- Molecular Driving Forces (Dill), planned source note: thermodynamics and statistical thermodynamics taught with chemical and biological examples.

## Lab projects

No Lab project implements thermodynamics directly.

## References

Scope: thermodynamics is required as its own subject in MIT's biology major (5.601 and 5.602, Thermodynamics I and II and Kinetics) and in its computer science-molecular biology major (5.601 Thermodynamics I),[^mit7][^mit67] and it is the first part of Volume 2 of a calculus-based physics text.[^up] The vault splits it: physical thermodynamics here, chemical thermodynamics in [[Physical Chemistry]], microscopic foundations in [[Statistical Physics]]. The biological motivation (free energy and equilibrium in the living cell) follows PBoC.[^pboc]

[^up]: [[University Physics (OpenStax)]], Volume 2: thermodynamics, electricity and magnetism.
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], course description (thermodynamics among the course topics).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., ch. 5 "Mechanical and Chemical Equilibrium in the Living Cell".
[^mit7]: [[MIT - Course 7 Biology]]: 5.601 and 5.602 Thermodynamics I, Thermodynamics II and Kinetics.
[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]]: 5.601 Thermodynamics I.
