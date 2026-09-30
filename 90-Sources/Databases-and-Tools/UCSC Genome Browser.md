---
aliases:
  - UCSC Genome Browser database
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
  - level/M1
kind: database
tier: A
authors:
  - Gerardo Perez
institution: University of California, Santa Cruz (UCSC)
year: 2001
edition:
url: https://genome.ucsc.edu
access: free
---

# UCSC Genome Browser

> [!abstract]
> A web-based tool for visualizing and analyzing genomic data, displaying annotation tracks on more than 4,000 genome assemblies from diverse organisms, released in 2001.

## Why this source

The UCSC browser is the classic genome browser: one coordinate axis, many stacked annotation tracks, zoom and pan. It is the model to study before building [[09-genome-browser]], and a quick way to see genes and variants around any locus of a reference [[Genome]].

## Coverage

Key publication: Perez G, Barber GP, Benet-Pages A, et al. "The UCSC Genome Browser database: 2025 update". *Nucleic Acids Res* 53(D1) (2025). doi:10.1093/nar/gkae974. The update adds more than 25 annotation tracks (including gnomAD 4.1 on the human GRCh38/hg38 assembly), three public hubs, expansions of the Genome Archive (GenArk), a popup dialog on the browser page, right-click zoom options on gene tracks, grouping for track hubs, and a new Clinical Genetics tutorial.

| Part | Content | Vault notes |
|---|---|---|
| Browser | Assemblies displayed with stacked tracks, zoom and pan | [[Genome]], [[09-genome-browser]] |
| Annotation tracks | Genes, population variation and more | [[Gene Annotation]], [[Genetic Variant]] |
| Track hubs and GenArk | Community hubs and archived assemblies | [[Genome Assembly]] |
| Tutorials | Including Clinical Genetics | [[Clinical Genomics]] |

## How to use it

- **L2**: open the human hg38 assembly, go to a gene you know, switch tracks on and off, zoom and pan: this is the interaction [[09-genome-browser]] rebuilds.
- **L3**: display your own variant calls from [[10-genomic-pipeline]] next to the public variation tracks (as your own track or a track hub) and check what is already known at each position.
- **M1**: use GenArk assemblies and public hubs for non-model organisms.

## Caveats

- Each track has its own data provider, version and terms: read the track description before relying on it.
- Before mixing UCSC and [[Ensembl]] files, check assembly version, chromosome naming and coordinate convention.
- Verified in this pass: the 2025 update (authors, DOI, abstract), including the 2001 release date and assembly count.
