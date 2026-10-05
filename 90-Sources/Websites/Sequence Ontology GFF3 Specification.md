---
aliases:
  - GFF3 specification
  - Generic Feature Format Version 3
tags:
  - type/source
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
kind: website
tier: A
authors:
  - Lincoln Stein
institution: Sequence Ontology Project
year: 2020
edition: "Version 1.26 (18 August 2020)"
url: "https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md"
access: free
---

# Sequence Ontology GFF3 Specification

> [!abstract]
> The official definition of GFF3, the nine-column, tab-delimited text format for genomic features, maintained by the Sequence Ontology project.

## Why this source

GFF had fragmented into incompatible dialects; GFF3 was written to fix the most common extensions while staying backward compatible. It adds multi-level feature hierarchies (the `Parent` attribute), separates feature identity (`ID`) from display names, constrains feature types to the Sequence Ontology, lets one feature belong to several parents, and defines conventions for alignments and discontinuous features. Every rule a GFF3 parser must follow is in this one page, with a worked "canonical gene" example.

## Coverage

| Section | Content | Vault notes |
|---|---|---|
| Description of the format | Nine columns, `.` for undefined fields, percent-encoding (tab, newline, carriage return, `%`, control characters; `;` `=` `&` `,` in column 9), split on tabs only | [[GFF Format]] |
| Columns | seqid, source, type (SO term), 1-based start and end with start ≤ end, score, strand (`+ - . ?`), phase (required for CDS), attributes | [[GFF Format]], [[Genomic Coordinate System]] |
| Reserved attributes | `ID`, `Name`, `Alias`, `Parent`, `Target`, `Gap`, `Derives_from`, `Note`, `Dbxref`, `Ontology_term`, `Is_circular`; case-sensitive tags | [[GFF Format]] |
| The canonical gene | Gene EDEN with three transcripts, shared exons and four CDSs; notes on orphan exons, UTRs and start and stop codons inside the CDS | [[GFF Format]], [[Gene]], [[Alternative Splicing]] |
| Circular genomes, Parent relationships, alignments | Features crossing the origin, part-of semantics and cycles, `Gap` and `Target` | [[GFF Format]], [[Genomic Coordinate System]] |
| Directives | `##gff-version`, `##sequence-region`, `###`, `##FASTA` | [[GFF Format]] |

Cited in [[GFF Format]] and [[Genomic Coordinate System]].

## How to use it

- L1: read "Description of the Format" and "The Canonical Gene" with [[GFF Format]] open.
- L2: read "Parent (part_of) Relationships", "Circular Genomes" and "Other Syntax" before writing a parser.
- L3: read the alignment sections (`Gap`, `Target`) when annotating alignments or converting from SAM or PSL.

## Caveats

- GFF3 only: GFF2 and GTF are separate dialects (see the [[UCSC Genome Browser]] format FAQ and [[Ensembl]] for GTF).
- The canonical gene is a schematic illustration: two of its CDSs have lengths that are not multiples of 3.
- A validator is linked from the page (modENCODE-DCC), not part of it.
- Verified in this pass: the full text of version 1.26 (author, date, all sections listed above).
