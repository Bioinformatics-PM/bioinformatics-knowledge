---
aliases:
  - hts-specs
  - SAM/BAM and related specifications
  - GA4GH BED v1.0
  - SAMv1 specification
  - VCF specification
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
kind: website
tier: A
authors:
  - GA4GH Large Scale Genomics work stream
institution: Global Alliance for Genomics and Health (GA4GH)
year: 2026
edition: master branch as read in 2026
url: "https://github.com/samtools/hts-specs"
access: free
---

# GA4GH hts-specs

> [!abstract]
> The repository of canonical specifications for high-throughput sequencing file formats (SAM, BAM, CRAM, VCF, BCF, BED, tabix and CSI indexes), maintained by the GA4GH Large Scale Genomics work stream.

## Why this source

These documents are the formal definitions that tools implement: when two programs disagree about a SAM field, a VCF position or a BED column, this is where the answer is. Each specification is a LaTeX source with a PDF build (also served at samtools.github.io/hts-specs), versioned in git, so the exact version used can be cited. The SAM specification also contains a short glossary of the two genomic coordinate conventions, and the BED specification formalizes the UCSC description of BED.

## Coverage

| Document | Content | Vault notes |
|---|---|---|
| `SAMv1.tex` | SAM, BAM and BAI; glossary of 1-based and 0-based coordinate systems (SAM, VCF, GFF, Wiggle are 1-based; BAM, BCFv2, BED, PSL are 0-based); Phred scale; `@SQ` header tags (`AS` assembly, `M5` MD5 of the sequence, `AN` alternative names, `AH` alternate locus) | [[SAM Format]], [[Genomic Coordinate System]], [[Reference Genome]], [[FASTQ Format]] |
| `VCFv4.5.tex` (and 4.1 to 4.4) | VCF and BCF; `POS` is 1-based; `##contig` and `##reference` header lines | [[VCF Format]], [[Genomic Coordinate System]] |
| `BEDv1.tex` | GA4GH BED v1.0 by Jeffrey Niu, Danielle Denisko and Michael M. Hoffman: the 12 BED fields, 0-based half-open coordinates, BED*n*, BED*n*+*m*, blocks, sorting, out-of-band information, UCSC track lines | [[BED Format]] |
| `tabix.tex`, `CSIv1.tex` | Index formats for position-sorted files | [[Genomic File Indexing]] |
| `CRAMv3.tex` | Reference-based compressed alignments | [[SAM Format]] |
| README | Unaligned formats are not defined here; FASTQ "has no formal definition and several incompatible variants" and is described by Cock et al. | [[FASTQ Format]] |

Cited in [[BED Format]], [[Genomic Coordinate System]], [[Reference Genome]] and [[FASTQ Format]].

## How to use it

- L1: read the "Terminology" glossary of `SAMv1` and the whole of `BEDv1` (short), with [[Genomic Coordinate System]] and [[BED Format]].
- L2: read the field tables of `SAMv1` and `VCFv4.x` when writing parsers for [[10-genomic-pipeline]] and [[03-genome-diff]].
- L3: read the index specifications when implementing region queries in [[09-genome-browser]].

## Caveats

- Living documents: cite the specification version (for VCF, 4.x) and, for precision, the commit or PDF date.
- GA4GH BED v1.0 was announced in March 2022; it formalizes "reasonable interpretations" of the UCSC description and flags interoperability issues, so older tools may accept or produce files it forbids.
- Verified in this pass: README (maintainer, list of documents, FASTQ statement), `BEDv1.tex` (fields, rules, examples, authors), the coordinate glossary, Phred definition, `QUAL` encoding and `@SQ` tags of `SAMv1.tex`, and the `POS` definition and contig header lines of `VCFv4.5.tex`.
