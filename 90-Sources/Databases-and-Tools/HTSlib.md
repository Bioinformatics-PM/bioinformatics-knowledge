---
aliases:
  - htslib
  - samtools faidx
  - bgzip
  - tabix
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
kind: tool
tier: A
authors:
  - James K. Bonfield
institution: samtools project
year: 2021
edition: "manual pages of htslib and samtools 1.24 (2026); faidx(5) format page (2018)"
url: "https://www.htslib.org"
access: free
---

# HTSlib

> [!abstract]
> The C library behind samtools and bcftools that reads and writes the high-throughput sequencing formats (SAM, BAM, CRAM, VCF, BCF) and their compressed, indexed forms; its manual pages document the `bgzip` and `tabix` utilities and the FASTA index format (`.fai`).

## Why this source

The hts-specs documents define the formats ([[GA4GH hts-specs]]); HTSlib implements them and lives in the same GitHub organization (`samtools`). Its manual pages fill the gaps the specifications leave open, above all the `.fai` index of FASTA and FASTQ files, which no hts-specs document defines. It is the reference to check your own parsers and indexes against.

## Coverage

Key publication: Bonfield JK et al. "HTSlib: C library for reading/writing high-throughput sequencing data". *GigaScience* 10(2):giab007 (2021). doi:10.1093/gigascience/giab007. The abstract describes a library extracted from the original SAMtools implementation, with a focus on performance and robustness, used directly by an estimated 900 GitHub projects and incorporated into Perl, Python, Rust and R, under MIT/BSD licences.

| Part | Content | Vault notes |
|---|---|---|
| `faidx(5)` | The `.fai` index: one line per sequence with five tab-separated columns (NAME, LENGTH, OFFSET, LINEBASES, LINEWIDTH), a sixth (QUALOFFSET) for FASTQ; "well-formatted" sequences (equal line lengths except the last); worked examples for LF and CR-LF line endings | [[Genomic File Indexing]], [[FASTA Format]] |
| `bgzip(1)` | Compression into a series of small (less than 64K) BGZF blocks, compatible with gzip, so that indexes can be built on the compressed file | [[Genomic File Indexing]] |
| `tabix(1)` | Indexing of position-sorted, bgzip-compressed TAB-delimited files into `.tbi` or `.csi`; presets `gff`, `bed`, `sam`, `vcf`; regions `chr:beginPos-endPos`, 1-based and inclusive; `.tbi` and BAI handle chromosomes up to 512 Mbp ($2^{29}$ bases), CSI beyond; retrieval over the network | [[Genomic File Indexing]], [[VCF Format]], [[BED Format]] |
| `samtools-faidx(1)` | Indexing a FASTA file and extracting regions; BGZF-compressed input with a `.gzi` index | [[Genomic File Indexing]] |

Cited in [[Genomic File Indexing]], [[SAM Format]] and [[VCF Format]].

## How to use it

- L2: read `faidx(5)` together with [[FASTA Format]], then the DESCRIPTION sections of `bgzip(1)` and `tabix(1)` before indexing your own files.
- L3: use the library through samtools, bcftools or a language binding in [[10-genomic-pipeline]], and use it as a test oracle for the parsers and indexes you write by hand.

## Caveats

- Tool documentation describes one implementation: when it and a specification disagree, the specification defines the format. Tier A as the reference implementation of the hts-specs formats, with a peer-reviewed description; it backs format facts, not biology.
- Manual pages change with releases: cite the version read (1.24 for `bgzip`, `tabix` and `samtools-faidx`; the `faidx(5)` page is dated June 2018).
- Verified in this pass: the 2021 paper (lead author, title, journal, volume, issue, article number, DOI and abstract) by search; `faidx(5)`, `bgzip(1)`, `tabix(1)` and `samtools-faidx(1)` read in the source repositories (samtools/htslib and samtools/samtools on GitHub). The full author list of the paper was not checked.
