---
aliases:
  - Chimie physique
tags:
  - type/moc
  - domain/chemistry
  - domain/physics
  - level/L1
  - level/L2
prerequisites:
  - "[[General Chemistry]]"
  - "[[Thermodynamics]]"
  - "[[Calculus]]"
projects: []
sources:
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[University Physics (OpenStax)]]"
  - "[[MIT - Course 7 Biology]]"
  - "[[MIT - Course 6-7 Computer Science and Molecular Biology]]"
---

# Physical Chemistry

> [!abstract]
> Why reactions go (enthalpy, free energy, equilibrium), how fast they go (kinetics), how protons and electrons distribute (pH, buffers, redox potentials) and how light measures molecules (spectroscopy basics), at L1-L2 and with biological systems as the running example.

## Why it matters for bioinformatics

- **Free energy is the common currency.** Folding stability, binding affinity and metabolic direction are all [[Gibbs Free Energy]] differences, and $\Delta G^\circ = -RT \ln K$ turns them into measurable [[Chemical Equilibrium|equilibrium constants]].
- **Charge depends on pH.** [[Acid-Base Equilibrium|pKa]] values decide which side chains are charged; computing an [[Isoelectric Point]] from a sequence is a standard protein statistic.
- **Rates make models.** [[Rate Law|Rate laws]] and the [[Steady-State Approximation]] are the origin of enzyme kinetics and of the ordinary differential equations of [[Systems Biology]].
- **Instruments are spectroscopy.** DNA and protein quantification ([[Beer-Lambert Law]], A260 and A280), [[Fluorescence]] in qPCR, sequencing and imaging, [[Förster Resonance Energy Transfer|FRET]] distances and [[Circular Dichroism]] of secondary structure.
- **Primer design is thermodynamics.** Duplex melting temperatures follow from the temperature dependence of equilibrium ([[Van 't Hoff Equation]]).

## Before you start

- [[General Chemistry]], all of Stage 1.
- [[Thermodynamics]] Stage 1: [[Laws of Thermodynamics]], [[Heat]], [[Thermodynamic Entropy]].
- [[Calculus]]: [[Derivative]], [[Integral]] (integrated rate laws); [[Logarithm]] from [[Mathematical Foundations]].
- [[Waves and Optics]] Stage 1, before item 13: [[Photon]], [[Electromagnetic Spectrum]].

## Learning path

### Stage 1 - Foundations (L1)

1. [[Enthalpy]] (L1): define ΔH as heat exchanged at constant pressure; use Hess's law and bond enthalpies; tell exothermic from endothermic.
2. [[Gibbs Free Energy]] (L1): predict spontaneity with $\Delta G = \Delta H - T\Delta S$; relate ΔG to ΔG° and the reaction quotient; use the biochemical standard state ΔG°′.
3. [[Chemical Equilibrium]] (L1): write equilibrium constants, compare Q with K, and convert with $\Delta G^\circ = -RT \ln K$.
4. [[Le Chatelier's Principle]] (L1): predict how an equilibrium shifts after a change in concentration, pressure or temperature. Bio: O2 loading by hemoglobin in the lungs and unloading in tissues.
5. [[pH]] (L1): compute pH and pOH, use $K_w$, and know the pH of cell compartments (cytosol, lysosome, mitochondrial matrix).
6. [[Acid-Base Equilibrium]] (L1): use $K_a$ and pKa of weak acids and bases. Bio: pKa of ionizable side chains.
7. [[Henderson-Hasselbalch Equation]] (L1): compute the protonated fraction of a group at a given pH. Bio: the charge of histidine near pH 7.
8. [[Buffer Solution]] (L1): choose a buffer (pKa close to the target pH) and estimate its capacity. Bio: phosphate and bicarbonate in cells and blood; Tris and HEPES in the lab.
9. [[Reaction Kinetics]] (L1): define reaction rate, rate constant and molecularity; measure a rate.
10. [[Rate Law]] (L1): determine reaction orders; integrate zero-, first- and second-order rate laws; use half-lives. Bio: mRNA and protein decay are first order.
11. [[Activation Energy]] (L1): explain energy barriers and the Arrhenius equation; compute how a rate changes with temperature.
12. [[Catalysis]] (L1): explain how a catalyst lowers the barrier without changing ΔG or K.
13. [[Spectroscopy]] (L1): explain absorption and emission as transitions between quantized energy levels; map spectral regions to electronic, vibrational and nuclear-spin transitions.
14. [[Beer-Lambert Law]] (L1): compute a concentration from an absorbance ($A = \varepsilon c l$). Bio: A260 for nucleic acids, A280 for proteins, the A260/A280 purity ratio.

### Stage 2 - Core (L2)

15. [[Chemical Potential]] (L2): write $\mu = \mu^\circ + RT \ln c$ and see equilibrium as equal chemical potentials. Bio: the driving force of transport, binding and osmosis.
16. [[Van 't Hoff Equation]] (L2): extract ΔH° from the temperature dependence of K. Bio: DNA duplex melting and primer melting temperature; thermal unfolding curves of proteins.
17. [[Osmotic Pressure]] (L2): compute osmotic pressure from solute concentration ($\Pi = cRT$) and relate it to other colligative properties. Bio: cell volume, dialysis.
18. [[Partition Coefficient]] (L2): define log P and relate it to the free energy of transfer between water and oil. Bio: hydrophobicity scales, membrane permeability, drug-likeness.
19. [[Isoelectric Point]] (L2): compute the pI of a protein from its sequence and side-chain pKa values. Bio: isoelectric focusing and 2D gels; a sequence statistic you can implement.
20. [[Reduction Potential]] (L2): use standard reduction potentials and $\Delta G = -nF\Delta E$. Bio: the energetics of electron transfer from NADH to O2.
21. [[Nernst Equation]] (L2): compute a potential from concentrations. Bio: the equilibrium potential of an ion across a membrane, the basis of [[Membrane Potential]].
22. [[Steady-State Approximation]] (L2): set the rate of change of an intermediate to zero and derive the rate law of a multistep mechanism. Bio: the derivation of [[Michaelis-Menten Kinetics]]; quasi-steady-state reductions of network models.
23. [[Transition State Theory]] (L2): relate a rate constant to the activation free energy (Eyring equation). Bio: enzymes accelerate reactions by stabilizing the transition state.
24. [[Fluorescence]] (L2): explain excitation, emission, Stokes shift, quantum yield and quenching with a Jablonski diagram. Bio: dyes in [[Quantitative Polymerase Chain Reaction|qPCR]] and sequencing, GFP, [[Fluorescence Microscopy]].
25. [[Förster Resonance Energy Transfer]] (L2): use the $1/r^6$ distance dependence of energy transfer between two dyes. Bio: a molecular ruler of 1 to 10 nm for conformational changes and interactions.
26. [[Circular Dichroism]] (L2): explain the differential absorption of left and right circularly polarized light by chiral molecules. Bio: estimate helix and sheet content, follow unfolding.

> [!tip] Order of study and what to skip
> Items 1 to 12 come in Stage 2 of the [[Curriculum]], right after [[Thermodynamics]] Stage 1 and before [[Biochemistry]]; items 13 and 14 as soon as lab data appear. Stage 2 of this MOC belongs to Stage 3 of the Curriculum, except item 22, read just before [[Michaelis-Menten Kinetics]]. Skip quantum chemistry (solving the Schrödinger equation, term symbols), phase diagrams, gas-phase kinetics and galvanic-cell engineering; the statistical derivations belong to [[Statistical Physics]].

## Uses from other domains

- [[Ordinary Differential Equation]] ([[Differential Equations]]): rate laws are ODEs; systems of them are the models of [[Systems Biology]].
- [[Boltzmann Distribution]] ([[Statistical Physics]]): the microscopic origin of the Arrhenius factor and of equilibrium constants.
- [[Membrane Potential]] ([[Biophysics]]): built on the [[Nernst Equation]].
- [[Polymerase Chain Reaction]] ([[Biotechnology]]): primer melting temperatures.
- [[Michaelis-Menten Kinetics]] and [[Ligand Binding]] ([[Biochemistry]]): steady state and equilibrium applied to enzymes and receptors.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 5.111SC - Principles of Chemical Science]] | MIT | L1 | Thermodynamics, acid-base and redox equilibria, kinetics and catalysis, with biological examples (Stage 1)[^5111] |

## Reference books

- [[Chemistry 2e (OpenStax)]]: ch. 5 "Thermochemistry" (item 1), ch. 13 "Fundamental Equilibrium Concepts" (items 3 and 4), ch. 14 "Acid-Base Equilibria" (items 5 to 8), ch. 12 "Kinetics" (items 9 to 12).[^chem2e]
- [[Physical Biology of the Cell (Phillips)]]: ch. 5 "Mechanical and Chemical Equilibrium in the Living Cell" for free energy and equilibrium in cells; ch. 18 "Light and Life" for light-matter interactions.[^pboc]
- [[University Physics (OpenStax)]]: Volume 3, modern physics unit (photons, atomic structure) as background for spectroscopy.[^up]

## Lab projects

No Lab project implements physical chemistry directly.

## References

Scope: MIT requires physical chemistry separately from general chemistry (5.601 and 5.602 Thermodynamics I, Thermodynamics II and Kinetics for biology majors; 5.601 for computer science-molecular biology).[^mit7][^mit67] The L1 core (thermodynamics, acid-base and redox equilibria, kinetics and catalysis) is part of a general chemistry course such as 5.111SC,[^5111] and the L2 items extend it toward biological applications (membranes, binding, spectroscopy).[^pboc]

[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], course description (thermodynamics, acid-base and redox equilibria, chemical kinetics and catalysis).
[^chem2e]: [[Chemistry 2e (OpenStax)]], ch. 5 "Thermochemistry", ch. 12 "Kinetics", ch. 13 "Fundamental Equilibrium Concepts", ch. 14 "Acid-Base Equilibria".
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., ch. 5 "Mechanical and Chemical Equilibrium in the Living Cell" and ch. 18 "Light and Life".
[^up]: [[University Physics (OpenStax)]], Volume 3, Unit 2 "Modern Physics".
[^mit7]: [[MIT - Course 7 Biology]]: 5.601 and 5.602 Thermodynamics I, Thermodynamics II and Kinetics (or 20.110).
[^mit67]: [[MIT - Course 6-7 Computer Science and Molecular Biology]]: 5.601 Thermodynamics I.
