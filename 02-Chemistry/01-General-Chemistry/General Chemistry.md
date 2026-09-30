---
aliases:
  - Chimie générale
tags:
  - type/moc
  - domain/chemistry
  - level/L1
  - level/L2
prerequisites:
  - "[[Mathematical Foundations]]"
projects: []
sources:
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT - Course 7 Biology]]"
  - "[[ETH Zurich - BSc Biology]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]]"
  - "[[Meselson 1958 - The Replication of DNA in Escherichia coli]]"
---

# General Chemistry

> [!abstract]
> First-year chemistry of atoms, bonds and solutions: enough to explain why water dissolves ions, why DNA strands pair and how to make up a 50 mM solution, before the quantitative equilibria of [[Physical Chemistry]].

## Why it matters for bioinformatics

- **Molecular recognition is non-covalent chemistry.** [[Base Pairing]], protein folding and protein-ligand binding are [[Hydrogen Bond|hydrogen bonds]] and other [[Intermolecular Force|intermolecular forces]] in [[Water]].
- **Mass spectrometry reads atoms.** Peptide and metabolite masses come from atomic masses and [[Isotope]] distributions.
- **Protocols are written in moles.** [[Molar Concentration]] and [[Stoichiometry]] are needed to read a methods section, to check a reagent amount, and later to write the stoichiometric matrix of a metabolic model.
- **Energy metabolism is electron transfer.** [[Redox Reaction|Redox]] chemistry is how NADH and the respiratory chain extract energy.
- **Structure files contain metals.** Mg2+ at ATP and polymerase active sites, Zn2+ in zinc fingers and iron in heme are [[Coordination Complex|coordination complexes]].

## Before you start

- [[Mathematical Foundations]]: [[Exponential Function]] and [[Logarithm]] (scientific notation, orders of magnitude).
- No prior chemistry is assumed.

## Learning path

### Stage 1 - Foundations (L1)

1. [[Atom]] (L1): describe protons, neutrons and electrons, atomic number and mass number; name the elements of life (C, H, N, O, P, S).
2. [[Isotope]] (L1): explain why atomic masses are not integers; tell [[Monoisotopic Mass|monoisotopic]] from average mass. Bio: isotope patterns in [[Mass Spectrometry]], 15N density labeling in the Meselson-Stahl experiment.[^meselson]
3. [[Atomic Orbital]] (L1): read quantum numbers and the shapes of s, p and d orbitals as probability clouds for an electron.
4. [[Electron Configuration]] (L1): fill orbitals (aufbau, Pauli, Hund) and count valence electrons. Bio: why carbon makes four bonds, nitrogen three, oxygen two.
5. [[Periodic Table]] (L1): predict atomic size, ionization energy and typical valence from position.
6. [[Electronegativity]] (L1): predict bond polarity, partial charges and molecular dipoles. Bio: polar N-H and O-H groups are the hydrogen-bond donors of proteins and nucleic acids.
7. [[Chemical Bond]] (L1): explain why atoms bond (lower energy) and place bonds on the ionic-covalent continuum.
8. [[Ionic Bond]] (L1): describe ions, salts and lattices. Bio: Na+, K+ and Cl- gradients across membranes; salt bridges between Lys or Arg and Asp or Glu.
9. [[Covalent Bond]] (L1): compare single, double and triple bonds by length and energy; polar and nonpolar bonds.
10. [[Molecule]] (L1): read molecular and empirical formulas and compute a molecular mass. Bio: the mass of a peptide from its formula.
11. [[Lewis Structure]] (L1): draw valence electrons, lone pairs and formal charges for small molecules (water, ammonia, phosphate).
12. [[Molecular Geometry]] (L1): predict shapes and bond angles with VSEPR. Bio: tetrahedral carbon and phosphate, bent water.
13. [[Orbital Hybridization]] (L1): assign sp3, sp2 and sp hybridization and relate it to geometry and bond rotation. Bio: flat sp2 nucleobases stack in DNA.
14. [[Intermolecular Force]] (L1): rank dispersion, dipole-dipole and ion-dipole interactions by strength and range. Bio: the forces that hold folded proteins and complexes together.
15. [[Hydrogen Bond]] (L1): identify donors and acceptors and the geometry of a hydrogen bond. Bio: two hydrogen bonds in A-T pairs, three in G-C pairs; helices and sheets.
16. [[Water]] (L1): explain its polarity, hydrogen-bond network, high dielectric constant and power as a solvent. Bio: the solvent of life and the origin of the [[Hydrophobic Effect]].
17. [[Mole]] (L1): convert between mass, amount and number of particles with the Avogadro constant. Bio: copy number of a plasmid in 1 ng of DNA.
18. [[Molar Concentration]] (L1): compute molarity and dilutions ($C_1 V_1 = C_2 V_2$), convert between mM, µM and nM. Bio: every protocol and every dissociation constant.
19. [[Stoichiometry]] (L1): balance equations, find the limiting reagent and the yield. Bio: the same bookkeeping as the [[Stoichiometric Matrix]] of a metabolic model.
20. [[Aqueous Solution]] (L1): distinguish electrolytes and non-electrolytes, solubility and precipitation ("like dissolves like"). Bio: ethanol precipitation of DNA, ionic strength of buffers.
21. [[Acid-Base Reaction]] (L1): identify Brønsted acids, bases and conjugate pairs; strong versus weak acids. The quantitative treatment (pH, pKa, buffers) is in [[Physical Chemistry]].
22. [[Redox Reaction]] (L1): assign oxidation states, identify oxidant and reductant, balance half-reactions. Bio: NAD+/NADH, oxidative damage to DNA bases.

### Stage 2 - Core (L2)

23. [[Resonance (Chemistry)]] (L2): draw resonance structures and explain electron delocalization. Bio: partial double-bond character of the peptide bond; equivalent oxygens of carboxylate and phosphate.
24. [[Molecular Orbital Theory]] (L2): build bonding and antibonding orbitals and explain conjugated π systems. Bio: why nucleobases absorb near 260 nm and aromatic residues near 280 nm.
25. [[Coordination Complex]] (L2): describe metal-ligand bonds and coordination geometry. Bio: Mg2+ with ATP and in polymerase active sites, zinc fingers, heme iron.
26. [[Radioactive Decay]] (L2): model decay as a first-order process and compute half-life and activity. Bio: 32P and 35S labeling in classic molecular biology experiments.

> [!tip] What to skim
> Gas laws beyond the [[Ideal Gas Law]], phase diagrams, descriptive chemistry of the main-group elements, crystal field theory and nuclear chemistry beyond decay kinetics. Thermochemistry, equilibrium and kinetics, which a general chemistry course also teaches, live in [[Physical Chemistry]] and [[Thermodynamics]] in this vault.

## Uses from other domains

- [[Base Pairing]] and [[DNA]] ([[Molecular Biology]]): [[Hydrogen Bond]], [[Orbital Hybridization]], stacking of flat rings.
- [[Mass Spectrometry]] ([[Biotechnology]]) and [[Monoisotopic Mass]] ([[Proteomics]]): [[Isotope]] patterns and molecular masses.
- [[Stoichiometric Matrix]] and [[Flux Balance Analysis]] ([[Systems Biology]]): [[Stoichiometry]] as a matrix.
- [[Protein Folding]] ([[Biochemistry]]): [[Intermolecular Force|intermolecular forces]] and [[Water]].

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 5.111SC - Principles of Chemical Science]] | MIT | L1 | Unit I "The Atom", then molecular structure and bonding; acid-base and redox chemistry, taught with biological examples[^5111] |

## Reference books

- [[Chemistry 2e (OpenStax)]]: chapters 1 to 4 (matter, atoms, molecules, stoichiometry) and ch. 7 "Chemical Bonding and Molecular Geometry" for Stage 1.[^chem2e]

## Lab projects

No Lab project implements general chemistry directly. [[01-dna-engine]] relies on [[Base Pairing]], which is explained by [[Hydrogen Bond|hydrogen bonds]].

## References

Scope: general chemistry is a first-block requirement in every program checked (MIT's science core, 13 ECTS in ETH's first year, CMU's general science core, UC San Diego's lower division), and the Paris-Saclay computer science and life sciences double licence opens L1 with a chemistry-biology unit.[^mit7][^eth][^cmu][^ucsd][^saclay] The order (atom, then bonds, then solutions and reactions) follows 5.111SC and Chemistry 2e.[^5111][^chem2e]

[^5111]: [[MIT 5.111SC - Principles of Chemical Science]]: course description (atomic and molecular electronic structure, thermodynamics, acid-base and redox equilibria, kinetics, with biological, inorganic and organic examples) and Unit I "The Atom".
[^chem2e]: [[Chemistry 2e (OpenStax)]], chapters 1 to 4 (titles not verified) and ch. 7 "Chemical Bonding and Molecular Geometry".
[^mit7]: [[MIT - Course 7 Biology]]: GIR chemistry (5.111, 5.112 or 3.091) in the science core taken first.
[^eth]: [[ETH Zurich - BSc Biology]]: chemistry 13 ECTS in year 1.
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: 09-105 Introduction to Modern Chemistry I in the general science core.
[^ucsd]: [[UC San Diego - BS Bioinformatics]]: CHEM 6A and 6B in the lower division.
[^saclay]: [[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]]: L1 unit "Chemistry-Biology: at the origins of life".
[^meselson]: [[Meselson 1958 - The Replication of DNA in Escherichia coli]]: cells grown on 15N, then shifted to 14N; DNA separated by density.
