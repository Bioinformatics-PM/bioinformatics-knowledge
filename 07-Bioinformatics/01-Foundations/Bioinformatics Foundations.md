---
aliases:
  - Introduction to Bioinformatics
  - Bioinformatics Data and Formats
tags:
  - type/moc
  - domain/bioinformatics
  - domain/computer-science
  - level/L1
  - level/L2
prerequisites:
  - "[[Molecular Biology]]"
  - "[[Genetics]]"
  - "[[Programming]]"
  - "[[Data Structures]]"
projects:
  - "[[01-dna-engine]]"
  - "[[02-sequence-translation]]"
  - "[[03-genome-diff]]"
  - "[[08-phylogenetic-engine]]"
  - "[[09-genome-browser]]"
  - "[[10-genomic-pipeline]]"
  - "[[bio-core]]"
sources:
  - "[[EMBL-EBI - Introductory Bioinformatics]]"
  - "[[Galaxy Training Network - Training Material]]"
  - "[[UC San Diego - BS Bioinformatics]]"
  - "[[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]]"
  - "[[Carnegie Mellon University - BS Computational Biology]]"
  - "[[ISCB - Bioinformatics Core Competencies]]"
  - "[[NCBI]]"
  - "[[NCBI GenBank]]"
  - "[[European Nucleotide Archive]]"
  - "[[UniProt]]"
  - "[[RCSB Protein Data Bank]]"
  - "[[Ensembl]]"
  - "[[UCSC Genome Browser]]"
  - "[[Gene Ontology]]"
---

# Bioinformatics Foundations

> [!abstract]
> Where biological data lives and how it is written down: databases, identifiers, reference genomes and coordinate systems, the standard file formats and the ontologies that make data findable and comparable.

## Why it matters for bioinformatics

Every analysis starts by fetching a sequence, an annotation or a variant file and ends by writing one. Many silent bugs in bioinformatics are data bugs: a wrong assembly version, an off-by-one coordinate, a gene identifier that maps to two genes. This syllabus makes the data layer explicit before any algorithm is learned, which is why programs that hook students early start with an introduction to bioinformatics in the first year,[^psisv][^cmu] and why introductory training begins with primary and secondary databases and with describing data consistently.[^ebi]

## Before you start

- [[Molecular Biology]] Stage 1: [[DNA]], [[RNA]], [[Central Dogma]]; [[Genetics]]: [[Gene]], [[Genome]], [[Chromosome]].
- [[Programming]]: [[Python Programming]], [[File Input and Output]], [[Regular Expression]]; [[Data Structures]]: [[String]], [[Hash Table]].
- [[Computer Systems]]: [[Unix Shell]], [[Unix Text Processing]]: most files in this syllabus are handled on the command line.

## Learning path

### Stage 1 - Foundations (L1)

1. [[Omics]] (L1): name the omics layers (genome, transcriptome, proteome, metabolome) and the kind of data each one produces.
2. [[Biological Database]] (L1): distinguish primary archives ([[NCBI GenBank]], [[European Nucleotide Archive]]) from curated knowledge bases ([[UniProt]], [[RCSB Protein Data Bank]], [[Ensembl]]) and pick one for a question.
3. [[Accession Number]] (L1): read a stable database identifier and its version (NM_000546.6) and know why analyses cite versions.
4. [[IUPAC Nucleotide Code]] (L1): validate a sequence and interpret ambiguity codes (N, R, Y) instead of rejecting them.
5. [[FASTA Format]] (L1): parse and write single and multi-record FASTA, headers included.
6. [[GenBank Format]] (L1): read a flat-file record with its features (gene, CDS, exon) and qualifiers.
7. [[Reference Genome]] (L1): explain what an assembly release (GRCh37, GRCh38, T2T-CHM13) is and why coordinates are meaningless without it.
8. [[Genomic Coordinate System]] (L1): convert between 0-based half-open and 1-based closed coordinates without off-by-one errors.
9. [[BED Format]] (L1): represent genomic intervals and features in the 0-based BED convention.
10. [[GFF Format]] (L1): read GFF3 and GTF gene models (gene, transcript, exon, CDS) and their parent-child hierarchy.
11. [[Genome Browser]] (L1): navigate a locus in the [[UCSC Genome Browser]], Ensembl or IGV and load your own tracks.
12. [[FASTQ Format]] (L1): read sequencing reads with their per-base quality strings.

### Stage 2 - Core (L2)

13. [[SAM Format]] (L2): decode an alignment record (FLAG, CIGAR, MAPQ, tags) and its binary forms BAM and CRAM.
14. [[VCF Format]] (L2): read a variant record (REF, ALT, QUAL, FILTER, INFO, per-sample genotypes) and its header.
15. [[PDB Format]] (L2): read atoms, residues, chains and coordinates from legacy PDB and PDBx/mmCIF files.
16. [[Newick Format]] (L2): parse and write a tree with branch lengths and labels.
17. [[Genomic File Indexing]] (L2): explain how bgzip, tabix, BAI and FAI indexes give random access to large genomic files.
18. [[Genomic Interval Arithmetic]] (L2): intersect, merge, subtract and compute coverage of interval sets (the bedtools operations).
19. [[Biological Ontology]] (L2): use a controlled vocabulary organized as a directed acyclic graph of terms and relations.
20. [[Gene Ontology Annotation]] (L2): read and use annotations of genes to [[Gene Ontology]] terms (function, process, component) with their evidence codes.
21. [[Identifier Mapping]] (L2): convert gene and protein identifiers across databases (Ensembl, Entrez, HGNC, UniProt) and handle one-to-many mappings.
22. [[Programmatic Database Access]] (L2): query [[NCBI]] E-utilities, the Ensembl REST API or UniProt from Python, with rate limits and caching.

> [!tip]
> Study items 1 to 12 together with [[01-dna-engine]]: each format is a parser to write and test. Do the coordinate exercises (items 7 to 9) twice: once now, once when you build [[09-genome-browser]].

## Uses from other domains

- [[Metadata]], [[Persistent Identifier]] and [[FAIR Principles]] (from [[Research Data Management]]): why a file without metadata is not reusable.
- [[Relational Database]] and [[Hierarchical Data Format]] (from [[Databases]]): the storage models behind most biological databases and large binary data files.
- [[Directed Acyclic Graph]] (from [[Discrete Mathematics]]): the structure of ontologies.
- [[Interval Tree]] (from [[Data Structures]]): the index behind interval queries.

## Reference courses

| Course | Institution | Level | Covers |
|---|---|---|---|
| [[EMBL-EBI - Introductory Bioinformatics]] | EMBL-EBI | L1 | "Bioinformatics for the terrified" (primary and secondary databases, describing data consistently); finding genes with Ensembl; protein sequence, function and structure resources[^ebi] |
| [[Galaxy Training Network - Training Material]] | Galaxy Project | L1-L2 | Topics "Introduction to Galaxy Analyses", "Sequence Analysis" and "FAIR Data, Workflows, and Research"[^gtn] |
| BIMM 182 Biological Databases, in [[UC San Diego - BS Bioinformatics]] | UC San Diego | L3 | Biological databases as a dedicated course of the bioinformatics major[^ucsd] |

## Reference books

No textbook is organized around data formats. The format specifications (SAM/BAM, VCF, GFF3, BED) and the database documentation are the primary references; the database source notes linked above are the entry points.

## Lab projects

- [[01-dna-engine]]: FASTA parsing, IUPAC validation.
- [[02-sequence-translation]]: sequence records and features.
- [[03-genome-diff]]: VCF output.
- [[08-phylogenetic-engine]]: Newick output.
- [[09-genome-browser]]: FASTA, GFF, VCF, coordinates, indexing.
- [[10-genomic-pipeline]]: FASTQ, SAM/BAM, VCF.
- [[bio-core]]: the typed domain model reading these formats.

## References

The placement of this syllabus at the start of the curriculum follows the programs that introduce bioinformatics in the first year;[^psisv][^cmu] its opening on databases and consistent data description follows EMBL-EBI's introductory pathway;[^ebi] the weight given to databases follows the programs that teach them as a dedicated course.[^ucsd] The ISCB competency framework is the outcome check for the data-handling skills listed here.[^iscb]

[^psisv]: [[Université Paris-Saclay - Licence Double Diplôme Informatique Sciences de la Vie]]: "Introduction to bioinformatics" is an L1 unit next to Python programming.
[^cmu]: [[Carnegie Mellon University - BS Computational Biology]]: Great Ideas in Computational Biology is taken in the first year.
[^ebi]: [[EMBL-EBI - Introductory Bioinformatics]], "Bioinformatics for the terrified" and the resource tutorials (Ensembl, UniProt, protein structures).
[^gtn]: [[Galaxy Training Network - Training Material]], topics "Introduction to Galaxy Analyses", "Sequence Analysis" and "FAIR Data, Workflows, and Research".
[^ucsd]: [[UC San Diego - BS Bioinformatics]]: BIMM 182 Biological Databases is part of the named upper-division bioinformatics sequence.
[^iscb]: [[ISCB - Bioinformatics Core Competencies]].
