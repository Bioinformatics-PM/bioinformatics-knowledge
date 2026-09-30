---
aliases:
  - Genomic tRNA Database
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: database
tier: A
authors:
  - Patricia P. Chan
  - Todd M. Lowe
institution: University of California, Santa Cruz (Lowe Lab)
year: 2016
url: "https://gtrnadb.ucsc.edu/"
access: free
---

# GtRNAdb

> [!abstract]
> The Genomic tRNA Database: tRNA genes predicted with tRNAscan-SE in complete and draft genomes, browsable per organism, per amino acid and per anticodon.

## Why this source

It is the reference catalogue of tRNA genes, built by the authors of tRNAscan-SE ([[Chan 2021 - tRNAscan-SE 2.0]]). Each genome page summarizes how many tRNA genes were predicted, how many pass the "high confidence" filter, and how they are distributed among amino acids and anticodons. It turns [[Transfer RNA]] from a textbook molecule into data: which anticodons a genome actually encodes, and in how many copies.

## Coverage

The database is described in Chan PP, Lowe TM, "GtRNAdb 2.0: an expanded database of transfer RNA genes identified in complete and draft genomes", *Nucleic Acids Research* 44(D1), article starting at page D184 (2016).

| Part | Content | Vault notes |
|---|---|---|
| Genome summaries | Predicted tRNA genes per genome, high-confidence set, pseudogenes | [[Transfer RNA]], [[Gene Annotation]] |
| Human (hg38, GRCh38) | High-confidence set of 429 tRNA genes: 428 decoding the 20 standard amino acids and 1 selenocysteine tRNA (anticodon TCA) | [[Transfer RNA]], [[Genetic Code]] |
| Method | tRNAscan-SE analysis of each genome | [[Chan 2021 - tRNAscan-SE 2.0]] |

Cited in [[Transfer RNA]].

## How to use it

- L2: open the human page and count the anticodons represented for one amino acid; compare with the codons of that amino acid in the [[Genetic Code]].
- L3: compare a bacterium and a eukaryote, and relate their tRNA gene sets to wobble rules and [[Codon Usage Bias]].

## Caveats

- Counts depend on the genome assembly and on the tRNAscan-SE version; cite the assembly (hg38 above) with any number.
- Verified in this pass through search results: the human hg38 high-confidence count and its composition, and that the database presents tRNAscan-SE analyses of complete and draft genomes. The site was reached through its development mirror (trna-dev.ucsc.edu/GtRNAdb) in search results; the canonical address is given in `url`.
