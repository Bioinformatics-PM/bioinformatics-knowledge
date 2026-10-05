---
aliases: []
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
kind: tool
tier: C
authors:
  - Peter J. A. Cock
institution: Biopython Project (international open-source community)
year:
edition:
url: https://biopython.org
access: free
---

# Biopython

> [!abstract]
> An open-source collection of Python libraries for computational molecular biology, developed by an international community of volunteers, with an official Tutorial and Cookbook.

## Why this source

Biopython is the standard Python toolkit for sequences, file formats, alignments, structures and NCBI access. In this vault it has two roles: a **test oracle** for what you implement by hand in the Lab (your reverse complement or translation must match Biopython's), and a **productivity tool** once a concept is mastered. Tier C: it documents a tool and never backs a concept claim alone.

## Coverage

Key publication: Cock PJA, Antao T, Chang JT, Chapman BA, Cox CJ, Dalke A, Friedberg I, Hamelryck T, Kauff F, Wilczynski B, de Hoon MJL. "Biopython: freely available Python tools for computational molecular biology and bioinformatics". *Bioinformatics* 25(11):1422-1423 (2009). It lists modules for sequence file formats and multiple sequence alignments, 3D macromolecular structures, interfaces to tools such as BLAST, ClustalW and EMBOSS, online database access, and numerical methods for statistical learning. The Tutorial and Cookbook (versioned with each release on biopython.org) has chapters on sequence objects, sequence annotation, `Bio.SeqIO`, alignments and `Bio.Entrez`.

| Part | Content | Vault notes |
|---|---|---|
| Sequence objects | Sequences and their operations | [[DNA]], [[Translation]], [[01-dna-engine]], [[02-sequence-translation]] |
| `Bio.SeqIO` | Reading and writing sequence formats | [[FASTA Format]], [[FASTQ Format]], [[NCBI GenBank]] |
| Alignments | Pairwise and multiple alignments | [[Sequence Alignment]], [[Multiple Sequence Alignment]], [[04-alignment-engine]] |
| `Bio.Entrez` | Access to NCBI databases | [[NCBI]], [[PubMed]] |
| Structures | 3D macromolecular structures | [[Protein Structure]], [[RCSB Protein Data Bank]] |
| Tool interfaces | Running and parsing BLAST and others | [[NCBI BLAST]] |

## How to use it

- **L2**: only after implementing a concept by hand (see [[Conventions]], section 7): use Biopython in the tests of [[01-dna-engine]] and [[02-sequence-translation]] to check your outputs; parse a GenBank record with `Bio.SeqIO`.
- **L3**: script NCBI downloads with `Bio.Entrez` and parse BLAST+ results for [[05-sequence-search]] and [[10-genomic-pipeline]]; compare [[bio-core]] objects with Biopython's design.

## Caveats

- The API evolves between releases: pin the version in each project and read the tutorial matching that version.
- Using it before writing the algorithm yourself skips the learning the Lab is built for.
- Launch year was not verified in this pass. Verified: the 2009 paper (authors, citation, abstract) and the tutorial's chapter list.
