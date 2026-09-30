---
aliases:
  - DDBJ/ENA/GenBank Feature Table Definition
  - Feature Table Definition
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
kind: website
tier: A
authors:
  - DDBJ, ENA and GenBank (INSDC)
institution: International Nucleotide Sequence Database Collaboration (INSDC)
year: 2024
edition: "Version 11.3 (October 2024)"
url: https://www.insdc.org/submitting-standards/feature-table/
access: free
---

# INSDC Feature Table Definition

> [!abstract]
> The shared specification, maintained jointly by DDBJ, ENA and GenBank, of how annotated features (genes, coding sequences, exons...) are described on nucleotide sequence records: feature keys, locations and qualifiers.

## Why this source

Every GenBank, ENA and DDBJ record describes its annotation with the same feature table, whatever the flat-file layout. This document defines the vocabulary: which feature keys exist, how a location such as `complement(join(...))` is written and read, and which qualifiers each feature may carry. It is the reference behind the features section of [[GenBank Format]] and the ground truth for any parser written in [[02-sequence-translation]].

## Coverage

Version 11.3, October 2024, published on the INSDC website and mirrored by the three partners.

| Part | Content | Vault notes |
|---|---|---|
| Feature table format | A feature is a feature key (functional group), a location (instructions for finding the feature on the sequence) and qualifiers (auxiliary information) | [[GenBank Format]] |
| Location (section 3.4) | Syntax and conventions of feature locations | [[GenBank Format]], [[Genomic Coordinate System]] |
| Feature keys and qualifiers | Controlled lists of keys (such as gene, mRNA, CDS, exon, source) and of qualifiers with their value formats | [[Gene Annotation]], [[Gene]], [[Open Reading Frame]] |
| Layout in the EMBL-style flat file | Feature lines prefixed `FT`, feature key starting in column 6 | [[European Nucleotide Archive]] |

## How to use it

- **L1**: read the overview of feature keys, locations and qualifiers, then find each element in one real record.
- **L2**: use the location section as the specification of a location parser; test it on `join`, `complement` and partial (`<`, `>`) locations.
- **L3**: check the list of qualifiers allowed for `CDS` before relying on one in a pipeline, and follow the version number when the definition is revised.

## Caveats

- A normative, dense document: read it with a record open next to it.
- The definition is revised over time: note the version used by a parser.
- Verified in this pass: title, version and date, the joint maintenance by DDBJ, ENA and GenBank, the three components of a feature, the existence of the location section 3.4, and the `FT` line layout of the EMBL-style format. Individual key and qualifier definitions were not quoted here.
