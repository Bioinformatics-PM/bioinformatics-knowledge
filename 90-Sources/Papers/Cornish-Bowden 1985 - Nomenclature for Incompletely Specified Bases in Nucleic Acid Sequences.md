---
aliases:
  - IUPAC nucleotide codes
  - NC-IUB 1984 recommendations
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
kind: paper
tier: S
authors:
  - Athel Cornish-Bowden (for the NC-IUB)
journal: Nucleic Acids Research
year: 1985
url: "https://doi.org/10.1093/nar/13.9.3021"
access: free
---

# Cornish-Bowden 1985 - Nomenclature for Incompletely Specified Bases in Nucleic Acid Sequences

> [!abstract]
> The official recommendations defining the one-letter codes for ambiguous nucleotides (R, Y, N and others) used in every sequence file format.

## Why this source

When a position can be one of several bases, sequence files use single letters such as R (A or G), Y (C or T) or N (any base). This paper, the Nomenclature Committee of the International Union of Biochemistry's recommendations of 1984, is where those symbols and their complements are defined. It is the primary reference behind the IUPAC codes accepted by FASTA parsers and databases.

## Coverage

Citation: Cornish-Bowden A. "Nomenclature for incompletely specified bases in nucleic acid sequences: recommendations 1984". *Nucleic Acids Research* 13(9):3021-3030 (1985). doi:10.1093/nar/13.9.3021. Free at PMC341218; also reproduced on the IUBMB nomenclature website.

| Part | Content | Vault notes |
|---|---|---|
| Symbols | One-letter codes for sets of two, three or four bases | [[Nucleotide]], [[FASTA Format]] |
| Complements | Complementary symbol of each code | [[Reverse Complement]], [[Base Pairing]] |

Cited in [[Nucleotide]].

## How to use it

- L1: read the table of symbols and check the count of 15 codes in [[Nucleotide]].
- L2: use the complement table as the specification for a reverse-complement function that accepts ambiguity codes in [[01-dna-engine]].

## Caveats

- Covers ambiguity symbols, not modified bases or gaps, which file formats handle separately.
- Metadata (author, journal, volume, issue, pages, DOI, PMC record) verified in this pass.
