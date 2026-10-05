---
aliases:
  - Biologie moléculaire
tags:
  - type/moc
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
prerequisites:
  - "[[Cell Biology]]"
  - "[[General Chemistry]]"
projects:
  - "[[01-dna-engine]]"
  - "[[02-sequence-translation]]"
  - "[[03-genome-diff]]"
  - "[[06-mutation-lab]]"
  - "[[bio-core]]"
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Molecular Cell Biology (Lodish)]]"
  - "[[The Cell (Cooper)]]"
  - "[[MIT 7.01SC - Fundamentals of Biology]]"
  - "[[MIT 7.016 - Introductory Biology]]"
  - "[[MIT 6.047 - Computational Biology]]"
  - "[[MIT - Course 7 Biology]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[University of Cambridge - Natural Sciences Tripos]]"
  - "[[Watson 1953 - Molecular Structure of Nucleic Acids]]"
  - "[[Meselson 1958 - The Replication of DNA in Escherichia coli]]"
  - "[[Nirenberg 1961 - Cell-Free Protein Synthesis and Synthetic Polyribonucleotides]]"
  - "[[Crick 1970 - Central Dogma of Molecular Biology]]"
---

# Molecular Biology

> [!abstract]
> How genetic information is stored in nucleic acids, copied, expressed into RNA and protein, and regulated: the flow of information that every sequence analysis assumes.

## Why it matters for bioinformatics

- Bioinformatics is, first, the computational side of the [[Central Dogma]]: a FASTA file is a [[DNA]] strand, an [[Open Reading Frame]] is a hypothesis about [[Translation]], an RNA-seq count is a measure of [[Gene Expression]].
- Every tool bakes in molecular facts: strand orientation and [[Base Pairing]] ([[Reverse Complement]]), the [[Genetic Code]] (translation tables), [[RNA Processing]] and [[Alternative Splicing]] (spliced aligners, isoform quantification), [[Transcription Factor]] binding ([[Sequence Motif|motif]] finding), [[Chromatin]] and [[Epigenetics]] ([[Epigenomics]]).
- It feeds [[Sequence Analysis]], [[Genomics]], [[Transcriptomics]] and the [[Gene Regulatory Network|regulatory networks]] of [[Systems Biology]].

## Before you start

- [[Cell Biology]] Stage 1: [[Cell]], [[Prokaryote]], [[Eukaryote]], [[Cell Nucleus]].
- [[General Chemistry]]: covalent and hydrogen bonds, acids and bases.
- [[Biochemistry]] at L1: [[Amino Acid]], [[Protein]].

## Learning path

Order: molecules, then the flow of information (replication, transcription, translation), then its regulation, then the epigenetic and RNA-level layers. Introductory courses and textbooks follow this order,[^openstax][^mit701][^mit7016] regulation is a second-year subject,[^cam] and the L3 items are those that computational biology courses revisit as data or algorithmic problems.[^mit6047] The reference texts give the depth for L2 and L3.[^mboc]

### Stage 1 - Foundations (L1)

1. [[Nucleotide]] (L1): draw a nucleotide (base, sugar, phosphate) and tell purines from pyrimidines and DNA from RNA building blocks.
2. [[Nucleic Acid]] (L1): explain the sugar-phosphate backbone and why every strand has a 5' to 3' direction.
3. [[DNA]] (L1): describe the antiparallel double helix and why genomes are stored as double-stranded DNA.
4. [[Base Pairing]] (L1): apply the A-T and G-C pairing rules and derive the complementary strand of any sequence.
5. [[RNA]] (L1): contrast RNA with DNA (ribose, uracil, single strand) and name the main classes of RNA.
6. [[Central Dogma]] (L1): state the flow DNA to RNA to protein, its known exceptions, and where each step happens in the cell.
7. [[DNA Replication]] (L1): explain semiconservative copying, origins, forks, leading and lagging strands and polymerase fidelity.
8. [[Transcription]] (L1): describe how RNA polymerase copies a template strand into RNA, from initiation to termination.
9. [[Messenger RNA]] (L1): identify the parts of an mRNA: 5' untranslated region, coding sequence, 3' untranslated region, and the cap and poly(A) tail of eukaryotes.
10. [[Codon]] (L1): read a coding sequence as nucleotide triplets and spot start and stop codons.
11. [[Genetic Code]] (L1): use the codon table, explain its redundancy and wobble, and know that alternative codes exist.
12. [[Reading Frame]] (L1): enumerate the six reading frames of a double-stranded sequence.
13. [[Open Reading Frame]] (L1): define an ORF and find all ORFs of a sequence, the core task of [[02-sequence-translation]].
14. [[Transfer RNA]] (L1): explain how the anticodon and the attached amino acid make tRNA the adaptor of the code.
15. [[Ribosome]] (L1): describe the two subunits, the catalytic role of rRNA and the A, P and E sites.
16. [[Translation]] (L1): follow initiation, elongation and termination, from mRNA to polypeptide.
17. [[Gene Expression]] (L1): define expression as the amount of functional product made from a gene, and how it is measured at the RNA and protein levels.

### Stage 2 - Core (L2)

18. [[DNA Repair]] (L2): relate the main repair pathways (mismatch, base and nucleotide excision, double-strand break repair) to the mutations they prevent.
19. [[Reverse Transcription]] (L2): explain RNA-to-DNA copying by reverse transcriptase, in retroviruses and in the cDNA step of [[RNA Sequencing]].
20. [[Promoter]] (L2): locate core promoter elements and the transcription start site, and contrast bacterial and eukaryotic promoters.
21. [[Gene Regulation]] (L2): list the levels at which expression is controlled, from chromatin to protein degradation.
22. [[Operon]] (L2): explain the lac and trp operons as the model of bacterial transcriptional control.
23. [[Transcription Factor]] (L2): explain how DNA-binding proteins recognize short sequence motifs to activate or repress transcription.
24. [[Enhancer]] (L2): describe distal cis-regulatory elements and how they act on promoters through DNA looping.
25. [[Chromatin]] (L2): describe the nucleosome and the difference between open euchromatin and compact heterochromatin.
26. [[RNA Processing]] (L2): describe capping, intron splicing and polyadenylation, which turn a pre-mRNA into a mature mRNA.
27. [[Alternative Splicing]] (L2): explain how one gene yields several transcript isoforms, and why isoforms complicate annotation and quantification.
28. [[Non-Coding RNA]] (L2): survey rRNA, tRNA, snRNA, miRNA and lncRNA, and what functional RNAs do without being translated.

### Stage 3 - Advanced (L3)

29. [[Epigenetics]] (L3): define heritable changes in gene activity that do not change the DNA sequence, and how they survive cell division.
30. [[DNA Methylation]] (L3): explain CpG methylation and its link to silencing at [[CpG Island|CpG islands]], the signal read by [[Bisulfite Sequencing]].
31. [[Histone Modification]] (L3): read the main histone marks (for example H3K4me3, H3K27ac, H3K27me3) as signs of active or repressed chromatin, the signal profiled by [[ChIP-Seq]].
32. [[MicroRNA]] (L3): explain miRNA biogenesis and seed-based target repression, the basis of target prediction.
33. [[Nonsense-Mediated Decay]] (L3): explain how premature stop codons trigger mRNA decay, and why it matters when predicting loss of function.

> [!tip] How to study it
> Stage 1 is one story: read items 1 to 17 in order, then build [[01-dna-engine]] and [[02-sequence-translation]] before starting Stage 2. Pair each step with its landmark experiment: [[Watson 1953 - Molecular Structure of Nucleic Acids|Watson and Crick]] with [[DNA]], [[Meselson 1958 - The Replication of DNA in Escherichia coli|Meselson and Stahl]] with [[DNA Replication]], [[Nirenberg 1961 - Cell-Free Protein Synthesis and Synthetic Polyribonucleotides|Nirenberg and Matthaei]] with [[Genetic Code]], [[Crick 1970 - Central Dogma of Molecular Biology|Crick 1970]] with [[Central Dogma]].

## Uses from other domains

- [[Genetics]]: [[Gene]], [[Chromosome]], [[Genome]] (from Stage 1), [[Mutation]] (with [[DNA Repair]]), [[Transposable Element]] (with [[Reverse Transcription]]).
- [[Biochemistry]]: [[Enzyme]] (polymerases, reverse transcriptase), [[Protein Structure]] and [[Protein Folding]] (after [[Translation]]), [[Post-Translational Modification]] (the last layer of [[Gene Regulation]]).
- [[Sequence Analysis]]: [[Reverse Complement]] and [[GC Content]] (with [[DNA]]), [[Sequence Motif]] (with [[Transcription Factor]]).
- [[Microbiology]]: [[Virus]] (with [[Reverse Transcription]]).
- [[Structural Bioinformatics]]: [[RNA Secondary Structure]] (after [[Non-Coding RNA]]).
- [[Genomics]] and [[Transcriptomics]]: [[ChIP-Seq]], [[ATAC-Seq]], [[Bisulfite Sequencing]], [[RNA Sequencing]], the assays that measure Stage 2 and 3 at genome scale.
- [[Data Structures]]: [[String]] and [[Hash Table]], to implement sequences and codon tables.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[MIT 7.01SC - Fundamentals of Biology]] | MIT | L1 | Molecular biology unit: DNA replication and the basics of gene expression; recombinant DNA unit |
| [[MIT 7.016 - Introductory Biology]] | MIT | L1 | Structure and regulation of genes; structure and synthesis of proteins |
| [[MIT 6.047 - Computational Biology]] | MIT | L3 | Networks part: microRNAs, regulatory genomics, epigenomics, the computational view of Stage 3 |

## Reference books

- [[Biology 2e (OpenStax)]]: ch. 14 "DNA Structure and Function", ch. 15 "Genes and Proteins", ch. 16 "Gene Expression" (L1).
- [[The Cell (Cooper)]]: fundamentals of molecular biology and flow of genetic information (L1 to L2).
- [[Molecular Biology of the Cell (Alberts)]]: basic genetic mechanisms, from DNA to protein, and gene regulation (L2 to L3 reference).
- [[Molecular Cell Biology (Lodish)]]: molecular genetics and gene control, with the experimental evidence (L2 to L3).

## Lab projects

- [[01-dna-engine]]: [[Nucleotide]], [[DNA]], [[Base Pairing]] (Stage 1).
- [[02-sequence-translation]]: [[Central Dogma]], [[Transcription]], [[Genetic Code]], [[Codon]], [[Reading Frame]], [[Open Reading Frame]], [[Translation]] (Stage 1).
- [[03-genome-diff]] and [[06-mutation-lab]]: the [[Genetic Code]] turns a nucleotide change into a protein change (Stage 2).
- [[bio-core]]: typed [[DNA]], [[RNA]] and [[Codon]] objects shared by every project.

## References

[^openstax]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function" (structure, replication, repair), ch. 15 "Genes and Proteins" (genetic code, transcription, translation), ch. 16 "Gene Expression" (regulation in prokaryotes and eukaryotes), in that order.
[^mit701]: [[MIT 7.01SC - Fundamentals of Biology]], molecular biology unit: DNA replication, then the basics of gene expression.
[^mit7016]: [[MIT 7.016 - Introductory Biology]], molecular biology and genetics part: structure and regulation of genes, structure and synthesis of proteins.
[^cam]: [[University of Cambridge - Natural Sciences Tripos]], Part IB (year 2) Biochemistry and Molecular Biology: genome to RNA and protein, regulation, protein structure and function. Molecular biology is also an upper-division requirement in [[UC San Diego - BS Bioinformatics]] (BIMM 100) and part of the introductory core of [[MIT - Course 7 Biology]].
[^mit6047]: [[MIT 6.047 - Computational Biology]], networks part: microRNAs, regulatory genomics, epigenomics.
[^mboc]: [[Molecular Biology of the Cell (Alberts)]], parts on basic genetic mechanisms, from DNA to protein, and gene regulation; chapter numbers not verified. Cross-check with [[Molecular Cell Biology (Lodish)]].
