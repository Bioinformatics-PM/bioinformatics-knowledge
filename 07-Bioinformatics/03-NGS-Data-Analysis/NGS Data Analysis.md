---
aliases:
  - Next-Generation Sequencing Data Analysis
  - High-Throughput Sequencing Analysis
tags:
  - type/moc
  - domain/bioinformatics
  - domain/computer-science
  - domain/statistics
  - level/L2
  - level/L3
  - level/M1
prerequisites:
  - "[[Bioinformatics Foundations]]"
  - "[[Sequence Analysis]]"
  - "[[Biotechnology]]"
  - "[[String Algorithms]]"
  - "[[Statistical Inference]]"
  - "[[Computer Systems]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[Bioinformatics Algorithms (Compeau)]]"
  - "[[Galaxy Training Network - Training Material]]"
  - "[[Coursera UCSD - Bioinformatics Specialization]]"
  - "[[Coursera JHU - Genomic Data Science Specialization]]"
  - "[[Peking University - Bioinformatics Introduction and Methods]]"
  - "[[UC San Diego - BS Bioinformatics]]"
---

# NGS Data Analysis

> [!abstract]
> From raw sequencing output to trustworthy variant calls: reads and their qualities, quality control, read mapping, coverage, and germline and somatic variant calling.

## Why it matters for bioinformatics

Almost every modern omics experiment ends as FASTQ files. The steps in this syllabus (QC, mapping, duplicate handling, calling) are shared by genomics, transcriptomics and epigenomics, and each one hides a statistical model of sequencing error. Getting them right is the difference between a biological finding and an artifact. Applied genomic technologies are a named course of dedicated bioinformatics majors,[^ucsd] and introductory courses treat read mapping, variant-calling models and analysis pipelines as one block.[^pku]

## Before you start

- [[Bioinformatics Foundations]]: [[FASTQ Format]], [[SAM Format]], [[VCF Format]], [[Reference Genome]], [[Genomic File Indexing]].
- [[Biotechnology]]: [[Next-Generation Sequencing]], [[Sequencing Library Preparation]], [[Whole-Genome Sequencing]], [[Exome Sequencing]], [[Long-Read Sequencing]], [[Polymerase Chain Reaction]].
- [[Genetics]]: [[Genotype]], [[Ploidy]], [[Single Nucleotide Polymorphism]], [[Indel]], [[Structural Variant]], [[Copy Number Variation]], [[Somatic Mutation]].
- [[Sequence Analysis]]: [[Sequence Alignment]], [[Semi-Global Alignment]], [[Seed and Extend]].
- [[String Algorithms]]: [[Burrows-Wheeler Transform]], [[FM-Index]], [[Suffix Array]], [[Minimizer]].
- [[Probability]]: [[Binomial Distribution]], [[Poisson Distribution]], [[Bayes' Theorem]]; [[Statistical Inference]]: [[Maximum Likelihood Estimation]].
- [[Computer Systems]]: [[Unix Shell]], [[Parallel Computing]].

## Learning path

### Stage 2 - Core (L2)

1. [[Sequencing Read]] (L2): describe a read (length, orientation, single or paired) and how read type depends on platform and library.
2. [[Base Calling]] (L2): explain how signals become bases and why error profiles differ between Illumina, PacBio and Nanopore.
3. [[Phred Quality Score]] (L2): convert between quality characters, Q values and error probabilities ($Q = -10 \log_{10} p$).
4. [[Paired-End Read]] (L2): use mate pairs, insert size and orientation to constrain mapping.
5. [[Demultiplexing]] (L2): assign pooled reads to samples by index barcodes and handle index errors.
6. [[Read Quality Control]] (L2): read a FastQC or MultiQC report (per-base quality, GC, duplication, adapter content) and decide what to do.
7. [[Read Trimming]] (L2): remove adapters and low-quality ends and measure the effect on downstream steps.
8. [[Read Mapping]] (L2): place millions of short reads on a reference with FM-index based mappers (BWA, Bowtie2).
9. [[Mapping Quality]] (L2): interpret MAPQ as the probability of wrong placement and handle multi-mapping reads.
10. [[Duplicate Read]] (L2): detect PCR and optical duplicates and explain why they bias variant calling.
11. [[Sequencing Coverage]] (L2): compute depth and breadth, and model coverage with a Poisson distribution.

### Stage 3 - Advanced (L3)

12. [[Library Complexity]] (L3): estimate the number of distinct molecules in a library and predict the return of deeper sequencing.
13. [[Base Quality Score Recalibration]] (L3): correct systematic quality errors with covariates and known variant sites.
14. [[Genotype Likelihood]] (L3): compute the likelihood of each genotype from read bases and qualities under a binomial error model.
15. [[Variant Calling]] (L3): call SNVs and indels with a Bayesian caller and local haplotype assembly (GATK HaplotypeCaller style).
16. [[Joint Genotyping]] (L3): genotype a cohort together from per-sample gVCFs and explain the gain over single-sample calling.
17. [[Variant Filtering]] (L3): apply hard filters and model-based recalibration and evaluate against a truth set (precision, recall).
18. [[Structural Variant Calling]] (L3): detect deletions, duplications, inversions, translocations and copy-number changes from read-pair, split-read and depth signals.
19. [[Long-Read Alignment]] (L3): map error-prone long reads with minimizer-based chaining (minimap2) and know what long reads resolve.

### Stage 4 - Frontier (M1)

20. [[Somatic Variant Calling]] (M1): call tumor variants against a matched normal, with low allele fractions, purity and panels of normals.

> [!tip]
> Build items 6 to 17 as the stages of [[10-genomic-pipeline]], on a small public dataset first (a bacterial genome or one human chromosome). Keep every intermediate QC report: they are the evidence for your calls.

## Uses from other domains

- [[Hypothesis Testing]] and [[Multiple Testing Correction]] (from [[Statistical Inference]]): filtering and significance of calls.
- [[Sequencing Experiment Design]] (from [[Experimental Design]]): depth, read length and replicates chosen before sequencing.
- [[Workflow Management System]] (from [[Bioinformatics Engineering]]): running the steps reproducibly.
- [[Variant Annotation]] and [[Variant Normalization]] (from [[Genomics]]): what happens to calls next.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[Galaxy Training Network - Training Material]] | Galaxy Project | L2-L3 | "Sequence Analysis" tutorials "Quality Control" and "Mapping"; "Variant Analysis" tutorials "Exome sequencing data analysis for diagnosing a genetic disease" and "Identification of somatic and germline variants from tumor and normal sample pairs"[^gtn] |
| [[Peking University - Bioinformatics Introduction and Methods]] | Peking University | L2-L3 | Features of NGS, read mapping, variant-calling models, analysis pipelines[^pku] |
| [[Coursera JHU - Genomic Data Science Specialization]] | Johns Hopkins | L2-L3 | "Algorithms for DNA Sequencing" (read mapping) and "Command Line Tools for Genomic Data Science"[^jhu] |
| [[Coursera UCSD - Bioinformatics Specialization]] | UC San Diego | L3 | VI. Finding Mutations in DNA and Proteins (read mapping)[^coursera] |
| BENG 183 Applied Genomic Technologies, in [[UC San Diego - BS Bioinformatics]] | UC San Diego | L3 | Sequencing technologies and their data[^ucsd] |

## Reference books

- [[Bioinformatics Algorithms (Compeau)]]: "How Do We Locate Disease-Causing Mutations?" for read mapping with suffix trees, suffix arrays and the Burrows-Wheeler transform (item 8).[^compeau]

## Lab projects

- [[10-genomic-pipeline]]: QC, mapping, duplicate marking, variant calling and filtering on real data.

## References

The scope (QC, mapping, germline and somatic calling) and order follow the Galaxy training sequence from quality control to mapping to variant analysis[^gtn] and the NGS block of the Peking University course;[^pku] the algorithmic core of read mapping follows the pattern-matching chapter of the reference textbook.[^compeau]

[^ucsd]: [[UC San Diego - BS Bioinformatics]]: BENG 183 Applied Genomic Technologies is part of the named bioinformatics sequence.
[^pku]: [[Peking University - Bioinformatics Introduction and Methods]], next-generation sequencing part.
[^gtn]: [[Galaxy Training Network - Training Material]], topics "Sequence Analysis" and "Variant Analysis" (tutorial titles as listed in the table).
[^jhu]: [[Coursera JHU - Genomic Data Science Specialization]], courses "Algorithms for DNA Sequencing" and "Command Line Tools for Genomic Data Science".
[^coursera]: [[Coursera UCSD - Bioinformatics Specialization]], course VI "Finding Mutations in DNA and Proteins".
[^compeau]: [[Bioinformatics Algorithms (Compeau)]], chapter "How Do We Locate Disease-Causing Mutations?".
