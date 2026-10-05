---
aliases:
  - Computational Genomics
tags:
  - type/moc
  - domain/bioinformatics
  - domain/biology
  - domain/computer-science
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Sequence Analysis]]"
  - "[[NGS Data Analysis]]"
  - "[[Genetics]]"
  - "[[Molecular Biology]]"
  - "[[Discrete Mathematics]]"
  - "[[Algorithms]]"
projects:
  - "[[03-genome-diff]]"
  - "[[06-mutation-lab]]"
  - "[[09-genome-browser]]"
  - "[[10-genomic-pipeline]]"
  - "[[bio-core]]"
sources:
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[An Introduction to Bioinformatics Algorithms (Jones)]]"
  - "[[Coursera UCSD - Bioinformatics Specialization]]"
  - "[[Coursera JHU - Genomic Data Science Specialization]]"
  - "[[Peking University - Bioinformatics Introduction and Methods]]"
  - "[[Galaxy Training Network - Training Material]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[Shanghai Jiao Tong University - BS Bioinformatics]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]]"
  - "[[Ensembl]]"
---

# Genomics

> [!abstract]
> Whole genomes as data: how they are assembled and annotated, how their variants are represented and interpreted, how genomes are compared, and how epigenomes and microbial communities are read.

## Why it matters for bioinformatics

Genomics is the largest consumer of bioinformatics: assembly, annotation and variant interpretation are the daily work of sequencing cores, clinical labs and biodiversity projects. It also contains some of the discipline's most elegant algorithms (de Bruijn graphs, genome rearrangements). The draft human genome made bioinformatics central to biology,[^lander] and computational genomics is now a required course of computational biology majors and a core course of bioinformatics majors.[^cmu][^sjtu]

## Before you start

- [[Genetics]]: [[Gene]], [[Genome]], [[Chromosome]], [[Mutation]], [[Single Nucleotide Polymorphism]], [[Indel]], [[Structural Variant]], [[Copy Number Variation]], [[Transposable Element]].
- [[Molecular Biology]]: [[Gene Expression]], [[Transcription Factor]], [[Enhancer]], [[RNA Processing]], [[Chromatin]], [[Epigenetics]], [[DNA Methylation]], [[Histone Modification]].
- [[Evolution]]: [[Ortholog]], [[Paralog]], [[Gene Duplication]]; [[Microbiology]]: [[Microbiome]], [[16S Ribosomal RNA]], [[Microbial Taxonomy]].
- [[Sequence Analysis]]: [[Sequence Alignment]], [[K-mer]], [[Gene Finding]], [[Profile Hidden Markov Model]], [[Protein Family]].
- [[NGS Data Analysis]]: [[Sequencing Read]], [[Read Mapping]], [[Sequencing Coverage]], [[Variant Calling]]; [[Biotechnology]]: [[Whole-Genome Sequencing]], [[Amplicon Sequencing]], [[Long-Read Sequencing]].
- [[Discrete Mathematics]]: [[Graph]], [[Directed Graph]], [[Eulerian Path]], [[Hamiltonian Path]]; [[Algorithms]]: [[Graph Traversal]], [[NP-Completeness]].
- [[Bioinformatics Foundations]]: [[GFF Format]], [[VCF Format]], [[Genomic Coordinate System]], [[Gene Ontology Annotation]].

## Learning path

### Stage 2 - Core (L2)

1. [[Shotgun Sequencing]] (L2): explain whole-genome and hierarchical shotgun strategies and why they turn a genome into an assembly puzzle.
2. [[Lander-Waterman Model]] (L2): predict the expected number of gaps and contigs from coverage, read length and genome size.
3. [[Genome Assembly]] (L2): state the assembly problem, the role of repeats, and the difference between contigs and scaffolds.
4. [[Overlap-Layout-Consensus]] (L2): assemble reads through an overlap graph and see why a Hamiltonian path formulation does not scale.
5. [[De Bruijn Graph]] (L2): assemble from k-mers as an Eulerian path and reason about the choice of k.
6. [[K-mer Spectrum]] (L2): estimate genome size, heterozygosity and error rate from k-mer counts (GenomeScope-style).
7. [[Assembly Quality Assessment]] (L2): evaluate an assembly with N50, misassemblies and gene completeness (QUAST, BUSCO).
8. [[Repeat Masking]] (L2): identify and mask repeats and transposable elements before annotation.
9. [[Gene Annotation]] (L2): produce structural annotation by combining ab initio prediction, transcript and protein evidence.
10. [[Genetic Variant]] (L2): represent SNVs, indels, MNVs and structural variants relative to a reference.
11. [[Variant Normalization]] (L2): left-align and decompose variants so that the same change has one representation.

### Stage 3 - Advanced (L3)

12. [[Scaffolding]] (L3): order and orient contigs with paired reads, long reads or Hi-C links.
13. [[Long-Read Assembly]] (L3): assemble with long accurate or noisy reads and reach chromosome-scale, telomere-to-telomere genomes.
14. [[Functional Annotation]] (L3): assign function to predicted genes from homology, domains and GO terms (InterProScan-style).
15. [[Variant Annotation]] (L3): predict the consequence of a variant on transcripts and proteins (VEP, SnpEff) and attach population frequencies.
16. [[Variant Effect Prediction]] (L3): interpret computational deleteriousness scores (SIFT, PolyPhen, CADD) and their limits.
17. [[Comparative Genomics]] (L3): compare gene content, order and sequence across genomes to infer function and history.
18. [[Orthology Inference]] (L3): infer orthologs at genome scale (reciprocal best hits, orthogroups) and recognize its pitfalls.
19. [[Whole-Genome Alignment]] (L3): align entire genomes with anchors and chains and read the result in a browser.
20. [[Synteny]] (L3): detect conserved gene order and use it to trace duplications and rearrangements.
21. [[Genome Rearrangement]] (L3): compute reversal and breakpoint distances between genomes.
22. [[Evolutionary Constraint]] (L3): find functional elements from cross-species conservation (phastCons, phyloP).
23. [[Epigenomics]] (L3): map genome-wide chromatin states, histone marks and DNA methylation and relate them to gene regulation.
24. [[ChIP-Seq]] (L3): design and analyze a chromatin immunoprecipitation sequencing experiment with its controls.
25. [[Peak Calling]] (L3): call enriched regions against input with a statistical model (MACS-style) and control the FDR.
26. [[ATAC-Seq]] (L3): measure chromatin accessibility and handle fragment sizes and Tn5 insertion sites.
27. [[Bisulfite Sequencing]] (L3): call DNA methylation levels per CpG from converted reads.
28. [[Metagenomics]] (L3): study a microbial community from shotgun reads of mixed genomes.
29. [[Amplicon Sequence Variant]] (L3): denoise 16S amplicon reads into exact variants and build an ASV table (DADA2).
30. [[Taxonomic Classification]] (L3): assign reads to taxa with k-mer and marker-gene classifiers and estimate abundances.

### Stage 4 - Frontier (M1)

31. [[Metagenomic Binning]] (M1): group assembled contigs into metagenome-assembled genomes by coverage and composition.
32. [[Pangenome]] (M1): represent the genomes of a species as a core and accessory gene set or as a variation graph.
33. [[Hi-C]] (M1): read chromosome contact maps, compartments and topologically associating domains.

> [!tip]
> Implement the de Bruijn graph assembler (items 3 to 5) on simulated error-free reads before touching real data. For items 23 to 33, pick one track first (epigenomics or metagenomics) rather than all of them.

## Uses from other domains

- [[False Discovery Rate]] (from [[Statistical Inference]]): peak calling and differential signal.
- [[Compositional Data Analysis]] (from [[Multivariate Analysis]]): relative abundances in items 28 to 30.
- [[Hidden Markov Model]] (from [[Stochastic Processes]]): gene prediction and chromatin state models.
- [[Interval Tree]] (from [[Data Structures]]) and [[Genome Browser]] (from [[Bioinformatics Foundations]]): displaying annotations and variants.
- [[Variant Nomenclature]] and [[Variant Classification]] (from [[Clinical Genomics]]): how annotated variants are named and interpreted in the clinic.
- [[Phylogenetic Tree]] (from [[Phylogenetics]]): comparative genomics across many species.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Coursera UCSD - Bioinformatics Specialization]] | UC San Diego | L2-L3 | II. Genome Sequencing (items 3 to 5); III. Comparing Genes, Proteins, and Genomes (item 21)[^coursera] |
| [[Coursera JHU - Genomic Data Science Specialization]] | Johns Hopkins | L2-L3 | "Introduction to Genomic Technologies"; "Algorithms for DNA Sequencing" (assembly)[^jhu] |
| [[Galaxy Training Network - Training Material]] | Galaxy Project | L2-M1 | "Assembly" ("An Introduction to Genome Assembly", "De Bruijn Graph Assembly", "Genome Assembly Quality Control"); "Genome Annotation" ("Genome annotation with Prokka", "Functional annotation of protein sequences"); "Epigenetics" ("ATAC-Seq data analysis", "DNA Methylation data analysis"); "Microbiome" ("Building an amplicon sequence variant (ASV) table from 16S data using DADA2", "Taxonomic Profiling and Visualization of Metagenomic Data", "Binning of metagenomic sequencing data")[^gtn] |
| [[MIT 6.047 - Computational Biology]] | MIT | L3-M1 | Gene finding, comparative genomics, regulatory genomics, epigenomics, personal genomics[^mit6047] |
| [[Peking University - Bioinformatics Introduction and Methods]] | Peking University | L2-L3 | Functional prediction of genetic variants (item 16)[^pku] |
| 02-510 Computational Genomics, in [[Carnegie Mellon University - BS Computational Biology]] | CMU | L3 | Required computational genomics course[^cmu] |
| Introduction to Functional Genomics, in [[Shanghai Jiao Tong University - BS Bioinformatics]] | SJTU | L3 | Bioinformatics core course[^sjtu] |

## Reference books

- [[Bioinformatics Algorithms (Compeau)]]: "How Do We Assemble Genomes?" (items 3 to 5) and "Are There Fragile Regions in the Human Genome?" (item 21).[^compeau]
- [[An Introduction to Bioinformatics Algorithms (Jones)]]: graph algorithms for assembly.[^jones]
- [[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]]: the landmark genome paper, a worked example of items 1, 3, 8 and 9 at human scale.[^lander]

## Lab projects

- [[03-genome-diff]]: genetic variants, normalization and VCF output.
- [[06-mutation-lab]]: molecular consequence of a variant, the core of variant annotation.
- [[09-genome-browser]]: gene annotation and variants displayed on a genome, compared with [[Ensembl]].
- [[10-genomic-pipeline]]: variant annotation at the end of the pipeline.
- [[bio-core]]: the typed genome, gene and variant objects.

## References

The core sequence (assembly, annotation, variants, comparison) follows the reference textbook, its companion course and the Galaxy training topics;[^compeau][^coursera][^gtn] epigenomics and comparative genomics as parts of the same syllabus follow MIT 6.047;[^mit6047] placement after sequence analysis follows the order of dedicated bioinformatics majors.[^ucsd]

[^lander]: [[Lander 2001 - Initial Sequencing and Analysis of the Human Genome]]: clone-based shotgun strategy and assembly, repeats and transposable elements, gene content.
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: 02-510 Computational Genomics is in the computational biology core.
[^sjtu]: [[Shanghai Jiao Tong University - BS Bioinformatics]]: Introduction to Functional Genomics is in the bioinformatics core.
[^ucsd]: [[UC San Diego - BS Bioinformatics]]: sequence analysis, then databases, then applied genomic technologies.
[^coursera]: [[Coursera UCSD - Bioinformatics Specialization]], courses II "Genome Sequencing" and III "Comparing Genes, Proteins, and Genomes".
[^jhu]: [[Coursera JHU - Genomic Data Science Specialization]], courses "Introduction to Genomic Technologies" and "Algorithms for DNA Sequencing".
[^gtn]: [[Galaxy Training Network - Training Material]], topics "Assembly", "Genome Annotation", "Epigenetics" and "Microbiome" (tutorial titles as listed in the table).
[^mit6047]: [[MIT 6.047 - Computational Biology]], "Genomes", "Networks" and "Evolution" parts.
[^pku]: [[Peking University - Bioinformatics Introduction and Methods]], genetic variants part.
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapters "How Do We Assemble Genomes?" and "Are There Fragile Regions in the Human Genome?".
[^jones]: [[An Introduction to Bioinformatics Algorithms (Jones)]], graph algorithms for assembly.
