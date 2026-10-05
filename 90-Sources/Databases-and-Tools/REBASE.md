---
aliases:
  - The Restriction Enzyme Database
  - REBASE restriction enzyme database
tags:
  - type/source
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
kind: database
tier: A
authors:
  - Richard J. Roberts
institution: New England Biolabs
year: 2023
edition:
url: "http://rebase.neb.com"
access: free
---

# REBASE

> [!abstract]
> The curated reference database of restriction-modification systems: recognition and cleavage sites of restriction enzymes and DNA methyltransferases, their methylation sensitivity and commercial availability.

## Why this source

REBASE is the authority on what a restriction enzyme recognizes and where it cuts. It grew from the collection of restriction enzymes kept by Richard J. Roberts since before 1980, is hosted at New England Biolabs, and is described in regular database papers in *Nucleic Acids Research* (the latest verified here appeared on 6 January 2023). Textbooks give a handful of classic enzymes; REBASE gives the full, curated list that restriction-site software uses.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Enzyme records | Recognition sequence and cleavage position of restriction enzymes | [[Restriction Enzyme]] |
| Methyltransferases | The modification half of restriction-modification systems | [[Restriction Enzyme]], [[DNA Methylation]] |
| Methylation sensitivity | Whether methylation of a site blocks cutting | [[Restriction Enzyme]] |
| Commercial availability | Which suppliers sell each enzyme | [[Molecular Cloning]] |

## How to use it

- L1: look up the site and cut position of an enzyme before writing it into code or a cloning plan ([[Restriction Enzyme]]).
- L2: check methylation sensitivity when a digest of plasmid DNA grown in *E. coli* fails.

## Caveats

- Verified in this pass: the database's scope (recognition and cleavage sites, methyltransferases, methylation sensitivity, commercial availability), its origin in Roberts' collection, its hosting at New England Biolabs and the 2023 *Nucleic Acids Research* publication; the volume, pages and full author list of that paper were not copied here.
- The cut positions of BamHI, HindIII, SmaI and PstI cited in the vault were cross-checked against New England Biolabs' chart "Alphabetized list of recognition specificities" (supplier documentation, tier C).
