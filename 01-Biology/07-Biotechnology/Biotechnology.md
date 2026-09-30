---
aliases:
  - Biotechnologie
  - Laboratory Techniques
tags:
  - type/moc
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Molecular Biology]]"
  - "[[Biochemistry]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Microbiology (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[MIT 7.01SC - Fundamentals of Biology]]"
  - "[[MIT 7.016 - Introductory Biology]]"
  - "[[MIT 7.91J - Foundations of Computational and Systems Biology]]"
  - "[[MIT - Course 7 Biology]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[ETH Zurich - BSc Biology]]"
  - "[[Saiki 1988 - Primer-Directed Enzymatic Amplification of DNA]]"
  - "[[Sanger 1977 - DNA Sequencing with Chain-Terminating Inhibitors]]"
---

# Biotechnology

> [!abstract]
> The laboratory techniques that turn molecules into data: amplifying, cutting, cloning, sequencing, hybridizing, editing and weighing nucleic acids and proteins, with the biases each one leaves in the data.

## Why it matters for bioinformatics

- Every dataset carries the fingerprint of the technique that produced it: PCR duplicates, GC bias, error profiles of [[Next-Generation Sequencing]] and [[Long-Read Sequencing]], probe effects of [[Microarray|microarrays]]. Quality control in [[NGS Data Analysis]] is the correction of these artifacts.
- Choosing an analysis starts with the assay: [[Whole-Genome Sequencing]], [[Exome Sequencing]] or [[Amplicon Sequencing]], [[Sequencing Library Preparation|library]] design, [[Mass Spectrometry]] mode for [[Proteomics]].
- Many design problems are computational: primer design for the [[Polymerase Chain Reaction]], restriction maps, guide RNA design for [[CRISPR-Cas9]].

## Before you start

- [[Molecular Biology]]: [[Base Pairing]], [[DNA Replication]], [[Transcription]]; [[Reverse Transcription]] before item 9.
- [[Biochemistry]]: [[Enzyme]], [[Protein]].

## Learning path

Order: the classic recombinant DNA toolkit and first-generation sequencing (L1, taught in introductory biology),[^intro] then hybridization, quantification and high-throughput methods (L2), then the current genomic technologies (L3), which bioinformatics programs teach as their own course.[^genomic] The reference texts give the mechanisms behind each method.[^mboc]

### Stage 1 - Foundations (L1)

1. [[Restriction Enzyme]] (L1): explain how restriction enzymes cut DNA at specific palindromic sites, and find those sites in a sequence.
2. [[Gel Electrophoresis]] (L1): separate nucleic acid fragments by size and read a gel against a ladder.
3. [[Polymerase Chain Reaction]] (L1): explain cycles of denaturation, annealing and extension, and design a primer pair.
4. [[Molecular Cloning]] (L1): follow the insertion of a DNA fragment into a vector, transformation of host cells and selection of recombinant clones.
5. [[DNA Sequencing]] (L1): define sequencing as reading base order, and compare technology generations by read length, accuracy and throughput.
6. [[Sanger Sequencing]] (L1): explain chain termination by dideoxynucleotides and read a chromatogram.

### Stage 2 - Core (L2)

7. [[Nucleic Acid Hybridization]] (L2): explain probe-target annealing and stringency, and their use in blots and in situ hybridization.
8. [[Microarray]] (L2): explain how hybridization to arrayed probes measures expression or genotypes, and the biases of the signal.
9. [[Quantitative Polymerase Chain Reaction]] (L2): interpret amplification curves and threshold cycles, and quantify relative expression against a reference gene.
10. [[Sequencing Library Preparation]] (L2): follow fragmentation, adapter ligation, indexing and amplification, and the artifacts each step adds (duplicates, size and GC bias).
11. [[Next-Generation Sequencing]] (L2): explain massively parallel short-read sequencing by synthesis, paired-end reads and per-base quality scores.
12. [[Flow Cytometry]] (L2): explain how cells are measured and sorted by fluorescence, and read a gating plot.
13. [[Mass Spectrometry]] (L2): explain ionization, separation by mass-to-charge ratio and tandem MS for peptide identification.

### Stage 3 - Advanced (L3)

14. [[Long-Read Sequencing]] (L3): compare nanopore and single-molecule real-time sequencing, their error profiles, and what long reads resolve that short reads cannot.
15. [[Whole-Genome Sequencing]] (L3): explain resequencing designs (depth, read type) and what a whole genome reveals that targeted assays miss.
16. [[Exome Sequencing]] (L3): explain hybrid capture of exons, its uneven coverage, and its trade-offs against whole-genome sequencing.
17. [[Amplicon Sequencing]] (L3): explain PCR-based targeting of a few loci (marker genes, gene panels, viral genomes) and its amplification biases.
18. [[CRISPR-Cas9]] (L3): explain guide-RNA-directed cutting, repair outcomes and guide design, and how pooled CRISPR screens are read out by sequencing.

> [!tip] How to study it
> For each technique, write down the data it outputs and its main error modes before moving on: that list is what [[NGS Data Analysis]] corrects. Pair [[Polymerase Chain Reaction]] with [[Saiki 1988 - Primer-Directed Enzymatic Amplification of DNA]] and [[Sanger Sequencing]] with [[Sanger 1977 - DNA Sequencing with Chain-Terminating Inhibitors]].

## Uses from other domains

- [[Microbiology]]: [[Plasmid]] (cloning vectors), [[Bacteriophage]], [[16S Ribosomal RNA]] (amplicon surveys), [[CRISPR-Cas System]] (origin of [[CRISPR-Cas9]]).
- [[Genetics]]: [[Genetic Screen]] (CRISPR screens), [[Single Nucleotide Polymorphism]] and [[Copy Number Variation]] (genotyping arrays).
- [[Cell Biology]]: [[Microscopy]] (imaging), [[Cell Type]] (with [[Flow Cytometry]]).
- [[Sequence Analysis]]: [[Reverse Complement]], [[GC Content]] and [[Sequence Motif]] (primers, restriction sites, guides).
- [[Probability]]: [[Poisson Distribution]] (sequencing coverage).
- [[Bioinformatics Foundations]]: [[FASTQ Format]] (the output of item 11).
- [[NGS Data Analysis]]: [[Sequencing Read]], [[Read Quality Control]], [[Duplicate Read]], [[Library Complexity]], [[Sequencing Coverage]], the analysis side of Stage 2 and 3.
- [[Genomics]], [[Transcriptomics]] and [[Proteomics]]: the assays built on these techniques, such as [[Shotgun Sequencing]], [[ChIP-Seq]], [[Bisulfite Sequencing]], [[RNA Sequencing]], [[Single-Cell RNA Sequencing]], [[Tandem Mass Spectrometry]].
- [[Clinical Genomics]]: [[Gene Panel]] (a clinical use of items 16 and 17).

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 7.01SC - Fundamentals of Biology]] | MIT | L1 | Recombinant DNA unit: general recombinant DNA techniques |
| [[MIT 7.016 - Introductory Biology]] | MIT | L1 | Applications: therapeutics and tools for advancing research |
| [[MIT 7.91J - Foundations of Computational and Systems Biology]] | MIT | L3 | Lecture 1: DNA sequencing technologies |

## Reference books

- [[Biology 2e (OpenStax)]]: ch. 17 "Biotechnology and Genomics" (cloning, PCR, sequencing, genomics) for the L1 pass.
- [[Microbiology (OpenStax)]]: ch. 12 "Modern Applications of Microbial Genetics" (genetic engineering and genomics tools).
- [[Molecular Biology of the Cell (Alberts)]]: methods for manipulating DNA, RNA and proteins (L2).

## Lab projects

- [[10-genomic-pipeline]]: real [[Next-Generation Sequencing]] data from reads to variants (Stage 3).

## References

[^intro]: [[Biology 2e (OpenStax)]], ch. 17 "Biotechnology and Genomics"; [[MIT 7.01SC - Fundamentals of Biology]], recombinant DNA unit; [[Microbiology (OpenStax)]], ch. 12. [[MIT - Course 7 Biology]] also requires 7.002 "Fundamentals of Experimental Molecular Biology".
[^genomic]: [[UC San Diego - BS Bioinformatics]]: BENG 183 "Applied Genomic Technologies" in the upper-division bioinformatics courses; [[ETH Zurich - BSc Biology]]: "Bioanalytics" in year 2; [[MIT 7.91J - Foundations of Computational and Systems Biology]] opens with DNA sequencing technologies.
[^mboc]: [[Molecular Biology of the Cell (Alberts)]], methods part (manipulating DNA, RNA and proteins); chapter numbers not verified.
