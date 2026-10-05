---
aliases:
  - Computational Structural Biology
tags:
  - type/moc
  - domain/bioinformatics
  - domain/chemistry
  - domain/physics
  - domain/computer-science
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Sequence Analysis]]"
  - "[[Biochemistry]]"
  - "[[Biophysics]]"
  - "[[Linear Algebra]]"
  - "[[Optimization]]"
  - "[[Statistical Learning]]"
projects: []
sources:
  - "[[Biological Sequence Analysis (Durbin)]]"
  - "[[MIT 7.91J - Foundations of Computational and Systems Biology]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[EMBL-EBI - Introductory Bioinformatics]]"
  - "[[Shanghai Jiao Tong University - BS Bioinformatics]]"
  - "[[RCSB Protein Data Bank]]"
  - "[[AlphaFold Protein Structure Database]]"
  - "[[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]]"
---

# Structural Bioinformatics

> [!abstract]
> The computational study of three-dimensional macromolecular structure: describing, comparing and classifying protein and RNA structures, and predicting them from sequence, up to deep-learning methods such as AlphaFold.

## Why it matters for bioinformatics

Function follows structure: binding sites, catalytic residues and the effect of a missense variant are read from 3D coordinates. Since 2021, predicted structures have become a routine lookup for most proteins without an experimental structure,[^afdb] so every bioinformatician now handles structural models and must know how far to trust them. Computational structural biology is a named core course of bioinformatics majors.[^sjtu]

## Before you start

- [[Biochemistry]]: [[Amino Acid]], [[Peptide Bond]], [[Protein Structure]], [[Protein Secondary Structure]], [[Protein Tertiary Structure]], [[Protein Folding]], [[Hydrophobic Effect]], [[Membrane Protein]].
- [[Physical Chemistry]]: [[Gibbs Free Energy]]; [[Statistical Physics]]: [[Boltzmann Distribution]], [[Free Energy Landscape]].
- [[Biophysics]]: [[Binding Free Energy]], [[Lennard-Jones Potential]]; experimental structures from [[X-ray Crystallography]], [[Nuclear Magnetic Resonance Spectroscopy]] and [[Cryo-Electron Microscopy]], deposited in the [[RCSB Protein Data Bank]].
- [[Molecular Biology]]: [[Non-Coding RNA]]; [[Bioinformatics Foundations]]: [[PDB Format]].
- [[Sequence Analysis]]: [[Multiple Sequence Alignment]], [[Profile Hidden Markov Model]], [[Protein Family]].
- [[Linear Algebra]]: [[Matrix]], [[Singular Value Decomposition]]; [[Optimization]]: [[Gradient Descent]], [[Simulated Annealing]].
- [[Algorithms]]: [[Dynamic Programming]]; [[Statistical Learning]]: [[Neural Network]], [[Transformer (Deep Learning)]].

## Learning path

### Stage 2 - Core (L2)

1. [[Ramachandran Plot]] (L2): read backbone dihedral angles (phi, psi) and the allowed regions of secondary structure, and use the plot to validate a model.
2. [[Secondary Structure Assignment]] (L2): assign helices and strands from hydrogen-bond patterns in coordinates (DSSP).
3. [[Secondary Structure Prediction]] (L2): predict helix, strand and coil from sequence, from propensity methods to profile-based neural networks.
4. [[Hydropathy Plot]] (L2): locate hydrophobic segments and candidate transmembrane helices from a sequence.
5. [[Molecular Visualization]] (L2): display and inspect a structure (PyMOL, ChimeraX): chains, surfaces, contacts, ligands.
6. [[Root-Mean-Square Deviation]] (L2): measure the distance between two superposed structures and its dependence on length.
7. [[Kabsch Algorithm]] (L2): find the optimal rigid superposition of two coordinate sets with a singular value decomposition.
8. [[RNA Secondary Structure]] (L2): represent RNA base-pair structures (stems, loops, pseudoknots) in dot-bracket notation.

### Stage 3 - Advanced (L3)

9. [[Nussinov Algorithm]] (L3): maximize RNA base pairs by dynamic programming over intervals.
10. [[RNA Secondary Structure Prediction]] (L3): predict the minimum free energy structure with nearest-neighbor parameters (Zuker, ViennaRNA-style) and base-pair probabilities.
11. [[Protein Domain]] (L3): delimit compact, independently folding units in a structure and see why they are the unit of classification and evolution.
12. [[Structural Alignment]] (L3): align proteins in 3D independently of sequence (DALI, TM-align) to detect remote homology.
13. [[TM-Score]] (L3): compare structures with a length-independent similarity score and interpret its thresholds.
14. [[Protein Structure Classification]] (L3): navigate fold hierarchies (SCOP, CATH) from class to family.
15. [[Contact Map]] (L3): represent a structure as residue-residue contacts and reconstruct geometry from them.
16. [[Solvent Accessible Surface Area]] (L3): compute residue exposure and relate it to function and variant effect.
17. [[Intrinsically Disordered Region]] (L3): recognize protein segments without a fixed structure and predict them from sequence.
18. [[Force Field]] (L3): read an empirical energy function (bonds, angles, torsions, van der Waals, electrostatics) and its parameters.
19. [[Protein Structure Prediction]] (L3): frame the problem, its blind assessment (CASP) and the families of methods.
20. [[Homology Modeling]] (L3): build a model from a template structure (MODELLER, SWISS-MODEL) and know when sequence identity is too low.
21. [[Protein Threading]] (L3): recognize a fold by fitting a sequence onto template structures.
22. [[Ab Initio Protein Structure Prediction]] (L3): predict without a template by fragment assembly and energy minimization (Rosetta-style).

### Stage 4 - Frontier (M1)

23. [[Stochastic Context-Free Grammar]] (M1): model RNA families and their structure probabilistically (Infernal, Rfam).
24. [[Direct Coupling Analysis]] (M1): predict residue contacts from coevolution in deep multiple sequence alignments.
25. [[AlphaFold]] (M1): explain how AlphaFold 2 predicts structures from MSAs and templates (Evoformer, structure module) and what AlphaFold 3 adds for complexes.
26. [[Structure Model Quality Assessment]] (M1): judge a model with lDDT, GDT, pLDDT and predicted aligned error, and spot disordered regions.
27. [[Protein Language Model]] (M1): use sequence embeddings learned on millions of proteins for structure and function prediction (ESM family).
28. [[Molecular Dynamics Simulation]] (M1): simulate motion under a force field and read what a trajectory can and cannot tell.

> [!tip]
> Download an experimental structure and the [[AlphaFold Protein Structure Database]] model of the same protein early (item 5), then come back to them after items 6, 13 and 26: comparing them is the best exercise of this syllabus.

## Uses from other domains

- [[Markov Chain Monte Carlo]] (from [[Bayesian Statistics]]): sampling conformations.
- [[Molecular Docking]] and [[Virtual Screening]] (from [[Drug Discovery]]): the main downstream uses of structures in industry.
- [[Missense Mutation]] (from [[Genetics]]): interpreting variants on structures.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 7.91J - Foundations of Computational and Systems Biology]] | MIT | L3-M1 | Structural modeling and structure prediction[^mit791] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | RNA structure[^mit6047] |
| [[EMBL-EBI - Introductory Bioinformatics]] | EMBL-EBI | L1-L2 | "Searching for protein structures"[^ebi] |
| Computational Structural Biology, in [[Shanghai Jiao Tong University - BS Bioinformatics]] | SJTU | L3 | Named bioinformatics core course[^sjtu] |

## Reference books

- [[Biological Sequence Analysis (Durbin)]]: ch. 9 "Transformational grammars" and ch. 10 "RNA structure analysis" for items 8 to 10 and 23.[^durbin]
- [[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]]: the AlphaFold 2 paper for item 25.[^alphafold]

## Lab projects

No Lab project validates this syllabus yet. A structure toolkit (PDB parsing, Kabsch superposition, RMSD, contact maps) would reuse [[bio-core]] and [[bio-visualization]]; it is not planned in [[Bioinformatics Lab]].

## References

Structure description and comparison come before prediction, and template-based prediction before deep learning, which follows the course progression from structural modeling to structure prediction;[^mit791] the AlphaFold items are anchored in the landmark paper and in the database that distributes its models with their confidence measures.[^alphafold][^afdb] RNA structure follows the reference textbook.[^durbin]

[^sjtu]: [[Shanghai Jiao Tong University - BS Bioinformatics]]: Computational Structural Biology is in the bioinformatics core.
[^mit791]: [[MIT 7.91J - Foundations of Computational and Systems Biology]], structure part.
[^mit6047]: [[MIT 6.047 - Computational Biology]], "Genomes" part.
[^ebi]: [[EMBL-EBI - Introductory Bioinformatics]], "Searching for protein structures".
[^durbin]: [[Biological Sequence Analysis (Durbin)]], ch. 9 "Transformational grammars" and ch. 10 "RNA structure analysis".
[^afdb]: [[AlphaFold Protein Structure Database]]: AlphaFold 2 predictions for more than 214 million sequences, with predicted aligned error and confidence colouring.
[^alphafold]: [[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]].
