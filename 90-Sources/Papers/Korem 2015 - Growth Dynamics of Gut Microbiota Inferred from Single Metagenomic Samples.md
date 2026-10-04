---
aliases:
  - Peak-to-trough ratio
  - PTR
  - Korem et al. 2015
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
kind: paper
tier: S
authors:
  - Tal Korem
  - David Zeevi
  - Jotham Suez
  - et al.
  - Eran Segal
journal: Science
year: 2015
url: "https://doi.org/10.1126/science.aac4812"
access: paid
---

# Korem 2015 - Growth Dynamics of Gut Microbiota Inferred from Single Metagenomic Samples

> [!abstract]
> "Growth dynamics of gut microbiota in health and disease inferred from single metagenomic samples": the sequencing coverage of a growing bacterial genome peaks at the replication origin and dips at the terminus, and the peak-to-trough ratio (PTR) measures the growth rate.

## Why this source

It turns a replication fact into a growth measurement from sequence data alone, one of the cleanest examples of biology read off read-depth patterns.

## Coverage

Citation: Korem T, Zeevi D, Suez J, et al., Segal E. *Science* 349(6252):1101-1106 (2015).

| Part | Content | Vault notes |
|---|---|---|
| Coverage pattern | A single peak at the replication origin and a single trough; the peak-to-trough coverage ratio quantifies growth rate | [[Bacterial Growth]], [[Sequencing Coverage]], [[Prokaryote]] |
| Validation | Shown in vitro, in vivo, under different growth conditions and in complex communities | [[Metagenomics]] |
| Application | For several species, PTRs, but not relative abundances, were associated with inflammatory bowel disease and type II diabetes | [[Microbiome]] |

Cited in [[Bacterial Growth]].

## How to use it

- L3: read with [[Bacterial Growth#Advanced (L3)]] and the replication model of [[Prokaryote#Mathematical representation]].

## Caveats

- Requires a complete or near-complete reference genome to order the coverage along the chromosome; later methods relaxed this.
- Metadata and the main claims verified in this pass; the author list is abbreviated.
