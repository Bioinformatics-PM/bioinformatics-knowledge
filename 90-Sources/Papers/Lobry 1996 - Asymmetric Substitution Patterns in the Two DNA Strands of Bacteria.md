---
aliases:
  - GC skew paper
tags:
  - type/source
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Jean R. Lobry
journal: Molecular Biology and Evolution
year: 1996
url: "https://doi.org/10.1093/oxfordjournals.molbev.a025626"
access: paid
---

# Lobry 1996 - Asymmetric Substitution Patterns in the Two DNA Strands of Bacteria

> [!abstract]
> The analysis showing that base composition differs between the leading and lagging strands of bacterial chromosomes, with switches at the replication origin and terminus.

## Why this source

In the genomes of *Escherichia coli*, *Bacillus subtilis* and *Haemophilus influenzae*, Lobry found departures from equal frequencies of G and C (and of A and T) within one strand, whose sign changes exactly at the origin and terminus of replication. The explanation is that the two strands are replicated differently and accumulate different substitutions. It is the biological basis of the GC skew method for finding replication origins from sequence alone.

## Coverage

Citation: Lobry JR. "Asymmetric substitution patterns in the two DNA strands of bacteria". *Molecular Biology and Evolution* 13(5):660-665 (1996). doi:10.1093/oxfordjournals.molbev.a025626.

| Part | Content | Vault notes |
|---|---|---|
| Data | Base composition along three bacterial genomes | [[GC Content]], [[Genome]] |
| Result | Strand compositional asymmetry switching at origin and terminus | [[DNA Replication]] |
| Interpretation | Different substitution patterns on leading and lagging strands | [[Mutation]], [[Molecular Evolution]] |

Cited in [[DNA Replication]].

## How to use it

- L2: read it with the GC skew section and Exercise 6 of [[DNA Replication]], then compute a cumulative skew on the *E. coli* genome and locate its minimum.
- The same origin-finding problem opens [[Bioinformatics Algorithms (Compeau)]].

## Caveats

- Skew is strong in many bacteria but weak or absent in others, and eukaryotic genomes with many origins show no simple global pattern.
- Metadata (author, journal, volume, issue, pages, DOI) verified in this pass; free access not verified.
