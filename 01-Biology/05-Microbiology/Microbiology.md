---
aliases:
  - Microbiologie
tags:
  - type/moc
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Cell Biology]]"
  - "[[Molecular Biology]]"
  - "[[Genetics]]"
projects: []
sources:
  - "[[Microbiology (OpenStax)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Tsinghua University - BS Biological Sciences]]"
---

# Microbiology

> [!abstract]
> Bacteria, archaea and viruses as a bioinformatician meets them: their diversity and classification, how their genomes exchange genes, and the communities and pathogens that metagenomics and pathogen genomics study.

## Why it matters for bioinformatics

- Most sequenced genomes are microbial, and most microbes are known only from sequence: [[Metagenomics]] and amplicon surveys rely on [[16S Ribosomal RNA]], [[Microbial Taxonomy]] and [[Microbial Ecology]].
- Bacterial genomes are shaped by [[Horizontal Gene Transfer]] and [[Plasmid|plasmids]], which break the tree-like assumptions of [[Phylogenetics]] and drive [[Antimicrobial Resistance]].
- Pathogen genomics (outbreak tracing, resistance-gene detection, viral variants) and the [[CRISPR-Cas System]] that became [[CRISPR-Cas9]] both start here.

## Before you start

- [[Cell Biology]]: [[Prokaryote]], [[Cell Membrane]].
- [[Molecular Biology]]: [[DNA Replication]], [[Operon]], [[Reverse Transcription]].
- [[Biochemistry]]: [[Metabolism]], [[ATP]].

## Learning path

Order: who the microbes are, then their metabolism and genetics, then diversity and classification from sequence, then the applied topics (resistance, microbiome). Metabolism and microbial genetics are the core chapters for this curriculum;[^micro] diversity follows the introductory text.[^openstax] The weight is deliberately light: microbiology is an elective in biology programs,[^thu] kept here for what metagenomics and pathogen genomics need.

### Stage 1 - Foundations (L1)

1. [[Microorganism]] (L1): define the microbial world (bacteria, archaea, microbial eukaryotes, viruses) and its size scale.
2. [[Bacteria]] (L1): describe bacterial cell structure, shapes and the Gram-positive versus Gram-negative envelope.
3. [[Archaea]] (L1): explain why archaea form a domain of their own despite looking like bacteria, and what they share with eukaryotes.
4. [[Virus]] (L1): describe virus structure and replication cycle, and why viruses are not cells.
5. [[Bacterial Growth]] (L1): read a growth curve (lag, exponential, stationary, death phases) and compute a doubling time.

### Stage 2 - Core (L2)

6. [[Microbial Metabolism]] (L2): compare respiration, fermentation, photosynthesis and chemolithotrophy as microbial ways to make ATP.
7. [[Plasmid]] (L2): describe plasmids as extrachromosomal replicons that carry accessory genes such as resistance genes.
8. [[Horizontal Gene Transfer]] (L2): explain transformation, transduction and conjugation, and how they move genes across lineages.
9. [[Bacteriophage]] (L2): contrast lytic and lysogenic cycles, and the role of phages in bacterial evolution and in molecular tools.
10. [[Baltimore Classification]] (L2): classify viruses into seven groups by genome type and replication strategy.
11. [[16S Ribosomal RNA]] (L2): explain why the 16S rRNA gene, with its conserved and variable regions, is the marker for bacterial phylogeny and amplicon surveys.
12. [[Microbial Taxonomy]] (L2): explain how bacterial species are delimited (16S identity, average nucleotide identity) and why taxonomy is being rebuilt from genomes.
13. [[Microbial Ecology]] (L2): describe microbial communities, niches and interactions, and why most microbes cannot be cultured.
14. [[Pathogen]] (L2): explain virulence factors, pathogenicity islands and the steps of an infection.
15. [[Antibiotic]] (L2): link each major antibiotic class to the cellular target it inhibits.

### Stage 3 - Advanced (L3)

16. [[Antimicrobial Resistance]] (L3): explain resistance mechanisms and how resistance genes spread by horizontal transfer, the target of resistance-gene detection.
17. [[CRISPR-Cas System]] (L3): explain CRISPR arrays as a prokaryotic adaptive immune memory of past infections, and how to spot them in a genome.
18. [[Microbiome]] (L3): describe the human microbiome, its variation between body sites and individuals, and its links with health.

> [!tip] How to study it
> Read the metabolism and microbial genetics chapters of [[Microbiology (OpenStax)]] (ch. 8, 11 and 12) closely and skim the rest. The clinical and disease chapters are optional context for pathogen genomics.

## Uses from other domains

- [[Molecular Biology]]: [[Ribosome]] and [[Non-Coding RNA]] (with [[16S Ribosomal RNA]]).
- [[Evolution]]: [[Tree of Life]] (three domains), [[Speciation]] (with [[Microbial Taxonomy]]).
- [[Physiology]]: [[Innate Immunity]] and [[Adaptive Immunity]] (with [[Pathogen]]).
- [[Biotechnology]]: [[Polymerase Chain Reaction]] and [[Amplicon Sequencing]] (16S surveys), [[Molecular Cloning]] (plasmid vectors).
- [[Mathematical Modeling]]: [[Logistic Growth]] (with [[Bacterial Growth]]), [[Lotka-Volterra Model]] (with [[Microbial Ecology]]).
- [[Genomics]]: [[Metagenomics]], [[Taxonomic Classification]], [[Metagenomic Binning]], [[Amplicon Sequence Variant]], [[Pangenome]], [[Comparative Genomics]], where this syllabus is applied.

## Reference courses

No dedicated microbiology course note yet; the reference books below cover the syllabus.

## Reference books

- [[Microbiology (OpenStax)]]: ch. 8 "Microbial Metabolism", ch. 11 "Mechanisms of Microbial Genetics", ch. 12 "Modern Applications of Microbial Genetics" (L1 to L2).
- [[Biology 2e (OpenStax)]]: Unit 5 "Biological Diversity" for viruses and prokaryotes (L1).

## Lab projects

No Lab project implements microbiology yet. It is the biological ground of a metagenomics or pathogen genomics specialization after Stage 4.

## References

[^micro]: [[Microbiology (OpenStax)]]: ch. 8 "Microbial Metabolism", ch. 11 "Mechanisms of Microbial Genetics" (replication, expression, mutation, gene transfer), ch. 12 "Modern Applications of Microbial Genetics".
[^openstax]: [[Biology 2e (OpenStax)]], Unit 5 "Biological Diversity".
[^thu]: [[Tsinghua University - BS Biological Sciences]]: microbiology is a major restricted elective, next to biophysics, biostatistics and introductory bioinformatics.
