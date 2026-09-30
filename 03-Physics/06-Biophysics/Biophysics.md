---
aliases:
  - Biophysique
  - Physical Biology
tags:
  - type/moc
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Statistical Physics]]"
  - "[[Electromagnetism]]"
  - "[[Waves and Optics]]"
  - "[[Physical Chemistry]]"
  - "[[Biochemistry]]"
  - "[[Cell Biology]]"
projects: []
sources:
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[MIT 8.592J - Statistical Physics in Biology]]"
  - "[[Biochemistry (Berg)]]"
  - "[[RCSB Protein Data Bank]]"
  - "[[Tsinghua University - BS Biological Sciences]]"
---

# Biophysics

> [!abstract]
> Physical models of molecules and cells: diffusion and transport, membranes and their potentials, the mechanics of biopolymers and motors, the energetics of binding and the physics under force fields, and the methods that solve structures (X-ray crystallography, NMR, cryo-EM).

## Why it matters for bioinformatics

- **Structures come from instruments.** Every entry in the PDB records an experimental method and a resolution to read before trusting it.[^pdb] Knowing how [[X-ray Crystallography]], [[Nuclear Magnetic Resonance Spectroscopy]] and [[Cryo-Electron Microscopy]] work tells what a resolution, a B-factor or an NMR ensemble means.
- **Simulation and docking are physics.** [[Molecular Dynamics Simulation|Molecular dynamics]] and [[Molecular Docking|docking]] score conformations with a [[Force Field|force field]] built from [[Hooke's Law|springs]], [[Lennard-Jones Potential|Lennard-Jones]] and [[Coulomb's Law|Coulomb]] terms; affinity prediction targets the [[Binding Free Energy]].
- **Diffusion sets cellular timescales.** How fast a transcription factor finds its site or a signal crosses a cell is a [[Diffusion]] problem ([[Diffusion-Limited Reaction]]).
- **Chromosomes are polymers.** [[Persistence Length]] and random-walk chain models explain DNA packaging and how Hi-C contact frequencies fall with genomic distance.
- **Numbers keep models honest.** [[Order-of-Magnitude Estimation]] of sizes, copy numbers and rates is the first check of any quantitative claim about a cell.[^pboc1]

## Before you start

- [[Statistical Physics]]: [[Boltzmann Distribution]], [[Partition Function]], [[Brownian Motion]], [[Free Energy Landscape]].
- [[Electromagnetism]]: [[Coulomb's Law]], [[Capacitance]], [[RC Circuit]], [[Dielectric Constant]], [[Magnetic Field]].
- [[Waves and Optics]]: [[Diffraction]], [[Fluorescence Microscopy]], [[Laser]].
- [[Mechanics]]: [[Hooke's Law]], [[Stokes' Law]], [[Reynolds Number]].
- [[Physical Chemistry]]: [[Chemical Potential]], [[Nernst Equation]], [[Fluorescence]].
- [[Biochemistry]]: [[Protein Structure]], [[Protein Folding]], [[Ligand Binding]], [[Membrane Protein]]; [[Cell Biology]]: [[Cell Membrane]].
- Mathematics: [[Ordinary Differential Equation]], [[Random Walk]], [[Fourier Transform]] (structure determination).

## Learning path

> [!tip] What to skip compared with a full physics licence
> A physics-department biophysics track would add continuum elasticity and beam theory beyond persistence length, the fluid dynamics of flagella and flows, neural network dynamics, quantum biology and the crystallographic mathematics of space groups. Skip them. Spend the time on reasoning with $k_B T$, diffusion times and free energies, and on what each structural method can and cannot show.

### Stage 1 - Foundations (L1)

1. [[Order-of-Magnitude Estimation]] (L1): estimate sizes, copy numbers, concentrations and rates in a cell (in an *E. coli* cell, 1 nM is about one molecule). Bio: sanity-check any quantitative claim.[^pboc1]
2. [[Diffusion]] (L1): explain diffusion as random molecular spreading, the diffusion coefficient D, and the time $t \sim x^2 / 2D$. Bio: diffusion is fast across a bacterium and hopeless along an axon.
3. [[Membrane Potential]] (L1): explain how ion gradients and selective permeability create a resting potential of tens of millivolts. Bio: neurons, mitochondria, bacteria.

### Stage 2 - Core (L2)

4. [[Fick's Law]] (L2): relate flux to a concentration gradient and solve the diffusion equation in simple geometries. Bio: morphogen gradients, nutrient uptake.
5. [[Stokes-Einstein Relation]] (L2): compute $D = k_B T / 6\pi\eta r$ and estimate a diffusion coefficient from molecular size.
6. [[Diffusion-Limited Reaction]] (L2): compute the Smoluchowski limit on encounter rates. Bio: enzymes at the diffusion limit; transcription factors that combine 3D diffusion with 1D sliding on DNA.
7. [[Lipid Bilayer]] (L2): describe self-assembly, thickness, fluidity, permeability and bending of bilayers. Bio: the environment of membrane proteins; liposomes.
8. [[Ion Channel]] (L2): describe selectivity, conductance and gating, and read a patch-clamp recording. Bio: channelopathies, drug targets.
9. [[Goldman-Hodgkin-Katz Equation]] (L2): compute a resting potential from the permeabilities and concentrations of several ions.
10. [[Action Potential]] (L2): describe the all-or-none spike produced by voltage-gated Na+ and K+ channels: threshold, refractory period, propagation along an axon. Bio: how a [[Neuron]] signals.
11. [[Debye Length]] (L2): explain electrostatic screening by salt and compute the screening length. Bio: why salt concentration changes binding affinities and DNA stiffness.
12. [[Lennard-Jones Potential]] (L2): model van der Waals attraction and steric repulsion between atoms. Bio: the nonbonded term of force fields; packing of protein cores.
13. [[Binding Free Energy]] (L2): relate $\Delta G_{bind}$ to $K_d$; split it into enthalpy and entropy and recognize enthalpy-entropy compensation. Bio: affinity prediction and [[Molecular Docking]] scores.
14. [[Freely Jointed Chain]] (L2): model a polymer as a random walk with end-to-end distance growing as $\sqrt{N}$. Bio: unfolded proteins, chromatin at large scales.
15. [[Persistence Length]] (L2): measure bending stiffness as a persistence length (about 50 nm for double-stranded DNA). Bio: DNA looping and packaging.
16. [[Molecular Motor]] (L2): describe kinesin, myosin, dynein, ATP synthase and polymerases as motors (step size, stall force, speed, efficiency). Bio: the energy budget of transport and replication.

### Stage 3 - Advanced (L3)

17. [[Hodgkin-Huxley Model]] (L3): model the action potential as voltage-gated conductances in a membrane RC circuit and simulate it as a system of ODEs.
18. [[Poisson-Boltzmann Equation]] (L3): compute the electrostatic potential around a macromolecule in salt water. Bio: electrostatic surfaces of proteins and DNA.
19. [[Worm-Like Chain]] (L3): model semiflexible polymers and their force-extension curves (entropic elasticity). Bio: single-molecule stretching of DNA; polymer models of chromatin.
20. [[Brownian Ratchet]] (L3): explain how rectified thermal fluctuations produce directed motion. Bio: protein translocation, polymerization-driven motion.
21. [[Optical Tweezers]] (L3): explain how a focused laser traps a bead and measures piconewton forces. Bio: motor steps, DNA and protein unfolding.
22. [[X-ray Crystallography]] (L3): explain crystals, Bragg diffraction, structure factors, the phase problem, electron density maps, resolution and R-factors.
23. [[Nuclear Magnetic Resonance Spectroscopy]] (L3): explain nuclear spins in a magnetic field, chemical shifts, couplings and NOE distance restraints, and why NMR structures are ensembles.
24. [[Cryo-Electron Microscopy]] (L3): explain single-particle imaging, the contrast transfer function, 2D classification, 3D reconstruction and resolution estimates.

> [!tip] Order of study
> Stage 1 can start with [[Cell Biology]]. Stage 2 comes in Stage 3 of the [[Curriculum]], after [[Statistical Physics]]. Items 22 to 24 pair with [[Structural Bioinformatics]] in Stage 4, where [[Force Field]] and [[Molecular Dynamics Simulation]] are taught on top of items 11, 12 and 13 and of [[Statistical Ensemble]], [[Equipartition Theorem]] and [[Langevin Equation]] ([[Statistical Physics]]).

## Uses from other domains

- [[Structural Bioinformatics]]: structures from items 22 to 24; [[Force Field]] and [[Molecular Dynamics Simulation]] built on items 11 to 13.
- [[Drug Discovery]] ([[Industry and Innovation]]): [[Binding Free Energy]] as the target of docking and affinity prediction.
- [[Chromatin]] ([[Molecular Biology]]): polymer models ([[Freely Jointed Chain]], [[Worm-Like Chain]]).
- [[Neuron]] ([[Physiology]]): its signaling is explained by [[Membrane Potential]], [[Ion Channel]], [[Action Potential]] and the [[Hodgkin-Huxley Model]].
- [[Systems Biology]]: diffusion and binding set the rates of network models.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 8.592J - Statistical Physics in Biology]] | MIT | L3-M1 | Biopolymers (DNA double helix, RNA secondary structure, protein folding), protein motors, membranes[^8592] |

## Reference books

- [[Physical Biology of the Cell (Phillips)]]: ch. 1 "Why: Biology by the Numbers" (item 1), ch. 5 "Mechanical and Chemical Equilibrium in the Living Cell", ch. 10 "Beam Theory: Architecture for Cells and Skeletons", ch. 18 "Light and Life"; the other chapters are not yet mapped to items.[^pboc]
- [[Biochemistry (Berg)]]: the part on exploring proteins and genes, for the experimental side of structure determination.[^berg]

## Lab projects

No Lab project implements biophysics directly.

## References

Scope: biophysics appears as a restricted elective in Tsinghua's biology program,[^thu] and as a graduate survey at MIT whose biopolymer, motor and membrane parts define Stage 2.[^8592] PBoC sets the L2 style (simple physical models, estimates) and the chapters on equilibrium, filaments and light.[^pboc] Structure determination is included because every PDB entry depends on it.[^pdb]

[^pboc1]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., ch. 1 "Why: Biology by the Numbers".
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., ch. 1, 5, 10 and 18.
[^8592]: [[MIT 8.592J - Statistical Physics in Biology]], course topics: biopolymers; force, motion and packaging (protein motors, membranes).
[^berg]: [[Biochemistry (Berg)]], 5th ed., part on the molecular design of life ("exploring proteins and genes").
[^thu]: [[Tsinghua University - BS Biological Sciences]]: Biophysics among the major restricted electives.
[^pdb]: [[RCSB Protein Data Bank]]: experimental structures, with method and resolution per entry.
