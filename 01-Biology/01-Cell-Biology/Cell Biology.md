---
aliases:
  - Biologie cellulaire
tags:
  - type/moc
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[General Chemistry]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Molecular Cell Biology (Lodish)]]"
  - "[[The Cell (Cooper)]]"
  - "[[MIT 7.016 - Introductory Biology]]"
  - "[[MIT - Course 7 Biology]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[ETH Zurich - BSc Biology]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
---

# Cell Biology

> [!abstract]
> The cell as the unit of life: its plan and compartments, its division, how it senses signals and how cells specialize, up to the cell types that single-cell data now catalog.

## Why it matters for bioinformatics

- Every omics measurement is made on cells: bulk samples average them, single-cell methods separate them. Reading [[Transcriptomics]] data means knowing what a [[Cell Type]], a [[Cell Cycle]] phase or an [[Apoptosis|apoptotic]] cell looks like in expression space.
- Localization and signal peptide predictors, transmembrane topology tools and pathway databases all encode cell biology: [[Protein Targeting]], [[Membrane Transport]], [[Cell Signaling]].
- [[Cancer]] biology frames most of [[Clinical Genomics]] and cancer genomics.

## Before you start

- [[General Chemistry]]: atoms, bonds, water and pH.
- The molecules of life at L1 only: [[Lipid]], [[Carbohydrate]], [[Amino Acid]], [[Protein]] ([[Biochemistry]]) and [[Nucleotide]] ([[Molecular Biology]]).

## Learning path

Order: the cell plan (prokaryote versus eukaryote), then compartments, then division; then communication, death and specialization; then the multicellular and disease level. This is the order of introductory texts and of the programs that teach cells in year 1 and multicellularity in year 2.[^openstax][^eth][^cam] Scope: the cell biology that biology and computational biology majors keep in their required core.[^core]

### Stage 1 - Foundations (L1)

1. [[Cell]] (L1): state the cell theory and list what every cell shares: membrane, cytoplasm, genome, ribosomes.
2. [[Microscopy]] (L1): explain resolution and contrast, and what light, fluorescence and electron microscopy can and cannot show.
3. [[Prokaryote]] (L1): describe the bacterial and archaeal cell plan: no nucleus, a nucleoid chromosome, often plasmids.
4. [[Eukaryote]] (L1): describe the compartmentalized cell and contrast it with prokaryotes, down to genome organization.
5. [[Cell Membrane]] (L1): explain the lipid bilayer, membrane proteins and selective permeability.
6. [[Organelle]] (L1): name the main organelles and map each one to its function.
7. [[Cell Nucleus]] (L1): describe the nuclear envelope, pores and nucleolus, and why eukaryotes separate transcription from translation.
8. [[Mitochondrion]] (L1): explain its role in energy conversion, its own small genome and its endosymbiotic origin.
9. [[Endomembrane System]] (L1): follow a secreted protein from the endoplasmic reticulum through the Golgi apparatus and vesicles.
10. [[Cytoskeleton]] (L1): distinguish actin filaments, microtubules and intermediate filaments and their roles in shape, transport and division.
11. [[Cell Cycle]] (L1): describe the G1, S, G2 and M phases and the checkpoints that gate them.
12. [[Mitosis]] (L1): follow chromosome segregation stage by stage and explain why daughter cells are genetically identical.
13. [[Meiosis]] (L1): explain reduction division, crossing over and independent assortment as the cellular basis of Mendel's laws.

### Stage 2 - Core (L2)

14. [[Membrane Transport]] (L2): distinguish passive diffusion, channels, carriers and pumps, and relate them to transmembrane protein families.
15. [[Protein Targeting]] (L2): explain how signal peptides and sorting signals send each protein to its compartment, the logic behind localization predictors.
16. [[Cell Signaling]] (L2): trace a signal from a receptor through second messengers and kinase cascades to a transcriptional response, and name the main receptor classes.
17. [[Apoptosis]] (L2): describe programmed cell death, its intrinsic and extrinsic pathways, and why its failure matters in cancer.
18. [[Cell Differentiation]] (L2): explain how cells with the same genome acquire distinct and stable expression programs.
19. [[Stem Cell]] (L2): define potency and self-renewal, and distinguish embryonic, adult and induced pluripotent stem cells.

### Stage 3 - Advanced (L3)

20. [[Developmental Biology]] (L3): outline how a zygote becomes an organism: axes, germ layers, morphogen gradients and master regulatory genes.
21. [[Cell Type]] (L3): discuss how cell types are defined (morphology, function, lineage, transcriptome) and how single-cell atlases classify them.
22. [[Cancer]] (L3): explain cancer as the clonal evolution of cells that escape growth control, and list the hallmarks of cancer.
23. [[Oncogene]] (L3): explain how gain-of-function changes turn a proto-oncogene into a driver of proliferation.
24. [[Tumor Suppressor Gene]] (L3): explain loss of function, the two-hit hypothesis, and how driver-gene catalogs tell tumor suppressors from oncogenes.

> [!tip] How to study it
> Read [[Meiosis]] in the same week as [[Mendelian Inheritance]] and [[Genetic Recombination]]: it is one story told twice. Plant-specific cell biology (chloroplast, cell wall) and cell mechanics can be skimmed; they rarely appear in sequence data.

## Uses from other domains

- [[Molecular Biology]]: [[DNA Replication]] (S phase), [[Gene Regulation]] and [[Chromatin]] (differentiation).
- [[Genetics]]: [[Chromosome]], [[Genetic Recombination]] (meiosis), [[Somatic Mutation]] (cancer).
- [[Evolution]]: [[Natural Selection]] (cancer as clonal evolution).
- [[Biochemistry]]: [[Enzyme]], [[Metabolism]] and [[ATP]] (mitochondrion), [[Membrane Protein]] (membrane transport), [[Post-Translational Modification]] (signaling).
- [[Biophysics]]: [[Diffusion]] and [[Membrane Potential]] (membrane transport).
- [[Transcriptomics]]: [[Single-Cell RNA Sequencing]] and [[Cell Type Annotation]], the data side of [[Cell Type]].

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 7.016 - Introductory Biology]] | MIT | L1 | Cell biology part: integration of molecules into cells and of cells into multicellular organisms |

## Reference books

- [[Biology 2e (OpenStax)]]: Unit 2 "The Cell" for the L1 pass; Unit 3 for meiosis.
- [[The Cell (Cooper)]]: compact L1 to L2 alternative; parts on cell structure and regulation.
- [[Molecular Biology of the Cell (Alberts)]]: the L2 to L3 reference for membranes, transport, compartments, signaling, cytoskeleton and cell division.[^mboc]
- [[Molecular Cell Biology (Lodish)]]: cell structure and function, with the experiments behind each result.

## Lab projects

No Lab project implements cell biology directly. It is the biological context of the single-cell and cancer genomics specializations after Stage 4.

## References

[^openstax]: [[Biology 2e (OpenStax)]], Unit 2 "The Cell" (cell structure, membranes, metabolism, cell division) comes before Unit 3 "Genetics".
[^eth]: [[ETH Zurich - BSc Biology]]: "Foundations of Biology 2: cells" in year 1, "Foundations of Biology 3: multicellularity" in year 2.
[^cam]: [[University of Cambridge - Natural Sciences Tripos]]: Biology of Cells in Part IA (year 1), Cell and Developmental Biology in Part IB (year 2).
[^core]: [[MIT - Course 7 Biology]] (7.06 Cell Biology in the molecular core) and [[Carnegie Mellon University - BS Computational Biology]] (03-320 Cell Biology in the biological core).
[^mboc]: [[Molecular Biology of the Cell (Alberts)]], parts on internal organization and on cell division; chapter numbers not verified.
