---
aliases:
  - Computational Proteomics
  - Mass Spectrometry Data Analysis
tags:
  - type/moc
  - domain/bioinformatics
  - domain/chemistry
  - domain/statistics
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Sequence Analysis]]"
  - "[[Biochemistry]]"
  - "[[Biotechnology]]"
  - "[[Statistical Inference]]"
projects: []
sources:
  - "[[Galaxy Training Network - Training Material]]"
  - "[[UniProt]]"
---

# Proteomics

> [!abstract]
> Identifying and quantifying the proteins of a sample from mass spectrometry data: spectra, peptide identification with error control, protein inference and quantification.

## Why it matters for bioinformatics

Proteins do most of the work in a cell, and their abundance is only loosely predicted by mRNA levels. Mass spectrometry proteomics is therefore a core omics layer for biomarker discovery, drug target validation and systems biology. Its central problems are computational: matching millions of spectra to sequences, controlling false identifications and quantifying with missing values.

## Before you start

- [[Biochemistry]]: [[Amino Acid]], [[Peptide Bond]], [[Protein]], [[Protein Structure]], [[Post-Translational Modification]]; [[Molecular Biology]]: [[Alternative Splicing]].
- [[Biotechnology]]: [[Mass Spectrometry]].
- [[Sequence Analysis]]: [[Protein Family]]; [[Bioinformatics Foundations]]: [[FASTA Format]], [[Biological Database]].
- [[Statistical Inference]]: [[Hypothesis Testing]], [[False Discovery Rate]], [[Multiple Testing Correction]]; [[Descriptive Statistics]]: [[Missing Data]].
- [[Algorithms]]: [[Dynamic Programming]], [[Graph Traversal]] (spectrum graphs).

## Learning path

### Stage 2 - Core (L2)

1. [[Proteome]] (L2): describe the protein complement of a cell and why it is more complex than the genome (isoforms, modifications).
2. [[Bottom-Up Proteomics]] (L2): follow the shotgun workflow from protein digestion with trypsin to LC-MS/MS of peptides.
3. [[Monoisotopic Mass]] (L2): compute peptide masses from residue masses and read isotope patterns and charge states.
4. [[Mass Spectrum]] (L2): read a spectrum as intensities over mass-to-charge ratios and recognize its peaks and noise.
5. [[Peptide Mass Fingerprinting]] (L2): identify a protein from the masses of its digested peptides.
6. [[Tandem Mass Spectrometry]] (L2): explain peptide fragmentation into b and y ions in MS/MS.
7. [[Theoretical Spectrum]] (L2): generate the expected fragment masses of a peptide and compare it with an observed spectrum.

### Stage 3 - Advanced (L3)

8. [[Peptide-Spectrum Match]] (L3): score spectra against a protein database built from [[UniProt]] (SEQUEST, Mascot-style search) with mass tolerances.
9. [[Target-Decoy Approach]] (L3): estimate the false discovery rate of identifications with reversed or shuffled decoy databases.
10. [[De Novo Peptide Sequencing]] (L3): read a peptide sequence directly from a spectrum with a spectrum graph.
11. [[Protein Inference]] (L3): infer proteins from identified peptides, including shared peptides and protein groups.
12. [[Label-Free Quantification]] (L3): quantify proteins from spectral counts or precursor intensities across runs.
13. [[Label-Based Quantification]] (L3): quantify with isotopic (SILAC) or isobaric (TMT, iTRAQ) labels and know their biases.
14. [[Differential Abundance Analysis]] (L3): test protein abundance changes with missing values, normalization and moderated statistics.

### Stage 4 - Frontier (M1)

15. [[Data-Independent Acquisition]] (M1): analyze DIA runs with spectral libraries and compare them with data-dependent acquisition.
16. [[Modification Site Localization]] (M1): identify post-translational modifications and score their position within a peptide.
17. [[Proteogenomics]] (M1): search spectra against sample-specific databases built from genomic and transcriptomic data.
18. [[Metabolomics]] (M1): transfer the same mass spectrometry logic to small molecules (feature detection, annotation).

> [!tip]
> Implement items 3 and 7 by hand (a table of residue masses is all you need), then run a full identification on a small public dataset with a Galaxy workflow to see items 8 to 11 in practice.

## Uses from other domains

- [[Shortest Path]] and [[Dynamic Programming]] (from [[Algorithms]]): spectrum graphs in de novo sequencing.
- [[Linear Regression]] (from [[Linear Models]]) and [[Empirical Bayes]] (from [[Bayesian Statistics]]): moderated tests of abundance.
- [[Protein-Protein Interaction Network]] (from [[Systems Biology]]): interpreting affinity-purification data.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Galaxy Training Network - Training Material]] | Galaxy Project | L2-M1 | "Proteomics" ("Protein FASTA Database Handling", "Peptide and Protein ID using SearchGUI and PeptideShaker", "Label-free data analysis using MaxQuant", "Label-free versus Labelled - How to Choose Your Quantitation Method", "Statistical analysis of DIA data", "Proteogenomics 1: Database Creation")[^gtn] |

## Reference books

No reference book is in `90-Sources/` yet; the Galaxy proteomics topic is the working reference, and a computational proteomics textbook is a planned source.

## Lab projects

No Lab project validates this syllabus yet. A small peptide identification engine (theoretical spectra, database search, target-decoy FDR) would fit the Lab's pattern; it is not planned in [[Bioinformatics Lab]].

## References

The progression from spectra to identification to quantification, and the frontier topics (DIA, proteogenomics), follow the Galaxy proteomics training topic.[^gtn]

[^gtn]: [[Galaxy Training Network - Training Material]], topic "Proteomics" (tutorial titles as listed in the table).
