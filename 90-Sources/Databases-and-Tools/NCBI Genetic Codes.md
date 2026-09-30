---
aliases:
  - The Genetic Codes
  - NCBI translation tables
  - transl_table
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
kind: database
tier: A
authors:
  - Andrzej (Anjay) Elzanowski
  - Jim Ostell
institution: NCBI/NLM/NIH
year:
edition:
url: "https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi"
access: free
---

# NCBI Genetic Codes

> [!abstract]
> NCBI's page "The Genetic Codes", the numbered list of translation tables (standard, mitochondrial and other variant codes) with their start codons, used to translate every coding sequence in GenBank.

## Why this source

The standard genetic code is not universal. NCBI maintains the reference list of known variant codes, each with an identifier used in GenBank records as the `/transl_table` qualifier of a coding sequence. Getting the table right is how NCBI keeps the translation of each record correct, and it is how your own translation code should choose its codon table. The page is compiled by Andrzej Elzanowski and Jim Ostell, based primarily on reviews by Osawa and colleagues.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Standard code | Table 1, with its alternative start codons | [[Genetic Code]], [[Codon]] |
| Variant codes | Mitochondrial and nuclear variant tables, each listing differences from the standard code | [[Genetic Code]], [[Mitochondrial DNA]] |
| Start codons | Initiation codons allowed in each table | [[Open Reading Frame]], [[Translation]] |
| Use in databases | The `/transl_table` qualifier on coding sequences | [[NCBI GenBank]] |

Cited in [[Genetic Code]].

## How to use it

- L1: compare table 1 with table 2 (vertebrate mitochondrial) and list the codons whose meaning changes.
- L2: implement table selection in [[02-sequence-translation]] and test it against [[Biopython]], whose codon tables follow the NCBI numbering.

## Caveats

- Updated occasionally (the last update seen in this pass was dated 23 September 2024); check the page for new tables.
- Numbering has gaps where tables were merged or withdrawn; do not assume consecutive identifiers.
- Verified in this pass: page title, URL, compilers, purpose and sources; individual table contents not checked.
