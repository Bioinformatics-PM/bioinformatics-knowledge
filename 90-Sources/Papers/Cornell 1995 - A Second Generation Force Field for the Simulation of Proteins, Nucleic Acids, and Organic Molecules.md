---
aliases:
  - Cornell 1995
  - Cornell et al. force field
tags:
  - type/source
  - domain/bioinformatics
  - domain/chemistry
  - domain/physics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Wendy D. Cornell
  - Piotr Cieplak
  - Christopher I. Bayly
  - Ian R. Gould
  - Kenneth M. Merz Jr.
  - David M. Ferguson
  - David C. Spellmeyer
  - Thomas Fox
  - James W. Caldwell
  - Peter A. Kollman
journal: Journal of the American Chemical Society
year: 1995
url: "https://doi.org/10.1021/ja00124a002"
access: paid
---

# Cornell 1995 - A Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules

> [!abstract]
> The paper that derived a widely used molecular mechanics force field of the AMBER family for proteins, nucleic acids and organic molecules in condensed phases.

## Why this source

It is a primary, citable statement of what a biomolecular force field is: a potential energy function made of simple terms (harmonic bond stretching and angle bending, periodic torsions, Lennard-Jones and Coulomb interactions between nonbonded atoms) whose parameters are fitted to experimental and quantum-chemical data. It is the reference for the physics notes that introduce these terms ([[Potential Energy]], [[Hooke's Law]]) and for [[Force Field]] and [[Molecular Dynamics Simulation]] later.

## Coverage

Citation: Cornell WD, Cieplak P, Bayly CI, Gould IR, Merz KM, Ferguson DM, Spellmeyer DC, Fox T, Caldwell JW, Kollman PA. "A Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules". *J. Am. Chem. Soc.* 117(19):5179-5197 (1995). doi:10.1021/ja00124a002.

| Part | Content | Vault notes |
|---|---|---|
| Scope | A molecular mechanical force field for structures, conformational energies and interaction energies of proteins, nucleic acids and related organic molecules in condensed phases | [[Force Field]], [[Molecular Dynamics Simulation]] |
| Functional form | Energy as a sum of bond-stretching and angle-bending terms of the form $K(r - r_{eq})^2$, torsional Fourier terms, and nonbonded $A/R^{12} - B/R^{6}$ plus Coulomb terms | [[Potential Energy]], [[Hooke's Law]], [[Lennard-Jones Potential]] |
| Parameters | Bonded parameters adapted from earlier AMBER work and modified to reproduce experimental vibrational frequencies and structures | [[Harmonic Oscillator]] |

Cited in [[Potential Energy]], [[Hooke's Law]].

## How to use it

- **L2**: read the functional form only, to see that each term is a familiar potential (springs, Lennard-Jones, Coulomb).
- **L3**: read how the parameters were fitted, as preparation for [[Force Field]] and for judging what a simulation can be trusted for.

## Caveats

- A 1995 force field: later AMBER versions and other families (CHARMM, OPLS, GROMOS) revised the parameters; use a current release for real simulations.
- The bond and angle terms are written without the factor $\frac{1}{2}$ of $\frac{1}{2}kx^2$, so the tabulated force constants are half the spring constants $k$.
- Verified in this pass by web search: the citation, the DOI and the abstract (scope; bonded parameters modified to reproduce vibrational frequencies and structures). The functional form is the widely reproduced equation of the paper; it was not re-read from the full text in this pass.
