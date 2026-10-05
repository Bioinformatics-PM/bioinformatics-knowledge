---
aliases:
  - vt normalize
  - Variant normalization paper
tags:
  - type/source
  - domain/bioinformatics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Adrian Tan
  - Gonçalo R. Abecasis
  - Hyun Min Kang
journal: Bioinformatics
year: 2015
url: "https://doi.org/10.1093/bioinformatics/btv112"
access: free
---

# Tan 2015 - Unified Representation of Genetic Variants

> [!abstract]
> A short applications note that formally defines variant normalization for VCF records (left-aligned and parsimonious) and provides the `vt normalize` tool that implements it.

## Why this source

The same insertion or deletion can be written in several valid VCF records, especially inside repeats. Tan, Abecasis and Kang showed that sequence analysis tools represented variants inconsistently, which magnifies discrepancies between call sets and complicates filtering and duplicate removal. They gave precise definitions: a VCF entry is **left aligned** if its position is the smallest among all entries with the same allele length that represent the same variant; it is **parsimonious** if it has the shortest allele length among all entries representing the same variant; it is **normalized** if and only if it is both. These definitions are what every normalization step in a variant pipeline implements.

## Coverage

Citation: Tan A, Abecasis GR, Kang HM. "Unified representation of genetic variants". *Bioinformatics* 31(13):2202-2204 (2015). doi:10.1093/bioinformatics/btv112. Free at PMC4481842. Software: `vt` (github.com/atks/vt).

| Part | Content | Vault notes |
|---|---|---|
| Problem | Inconsistent representation of the same variant across tools | [[Variant Normalization]], [[VCF Format]] |
| Definitions | Left-aligned, parsimonious, normalized VCF entries | [[Indel]], [[Variant Normalization]] |
| Tool | `vt normalize` | [[03-genome-diff]], [[10-genomic-pipeline]] |

Cited in [[Indel]].

## How to use it

- L2: read the definitions, then normalize the indels of [[Indel]] by hand before running any tool.
- L3: normalize the output of [[03-genome-diff]] and compare it with a normalized call set from another caller.

## Caveats

- It covers representation in VCF (left alignment). Clinical nomenclature (HGVS) shifts indels the other way, to the 3' side ([[den Dunnen 2016 - HGVS Recommendations for the Description of Sequence Variants]]).
- Verified in this pass: authors, title, journal, volume, issue, pages, PMC record, the three definitions and the stated motivation.
