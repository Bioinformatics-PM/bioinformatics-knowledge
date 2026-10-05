---
aliases:
  - IGV
  - igv.js
  - IGV-Web
tags:
  - type/source
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
kind: tool
tier: A
authors:
  - James T. Robinson
  - Helga Thorvaldsdóttir
  - Jill P. Mesirov
institution: Broad Institute
year: 2011
edition:
url: "https://igv.org"
access: free
---

# Integrative Genomics Viewer

> [!abstract]
> IGV, an open-source (MIT) interactive viewer for genomic data, available as a desktop application, a web application (IGV-Web) and an embeddable JavaScript component (igv.js), with its user documentation.

## Why this source

IGV is the genome browser that runs on your own machine with your own files: reads, variants, annotations and signal tracks, local or remote. Where the [[UCSC Genome Browser]] and [[Ensembl]] are databases with a browser, IGV is a viewer, which makes it the natural tool to inspect the outputs of [[10-genomic-pipeline]] and the closest model of what [[09-genome-browser]] builds. Its documentation states plainly that the reference genome "serves as the coordinate system for displaying the tracks".

## Coverage

Key publication: Robinson JT, Thorvaldsdóttir H, Winckler W, Guttman M, Lander ES, Getz G, Mesirov JP. "Integrative Genomics Viewer". *Nature Biotechnology* 29:24-26 (2011). doi:10.1038/nbt.1754. Free at PMC3346182. It presents IGV as a lightweight tool for real-time exploration of large, diverse genomic datasets (aligned reads, mutations, copy number, expression, methylation, annotations) on standard desktop computers, loading local and remote data. A longer description is Thorvaldsdóttir H, Robinson JT, Mesirov JP, *Briefings in Bioinformatics* 14:178-192 (2013).

| Part (desktop documentation) | Content | Vault notes |
|---|---|---|
| Reference genome | A reference genome is required; GRCh38/hg38 is loaded by default; switching genome clears the session | [[Reference Genome]], [[Genome Browser]] |
| Loading and removing tracks | *File > Load from File* and *Load from URL* (with the index file for indexed formats; web servers must support byte-range requests), hosted tracks | [[Genome Browser]], [[Genomic File Indexing]] |
| Navigating the view | Locus box (`chr5:90,339,000-90,349,000` or a gene symbol), zoom, pan, whole-genome view | [[Genome Browser]], [[Genomic Coordinate System]] |
| File formats | BAM/SAM (sorted and indexed; one-based), BED (zero-based, end excluded), GFF2, GFF3 and GTF (recognized by extension), bigBed, bigWig, VCF | [[BED Format]], [[GFF Format]], [[SAM Format]], [[VCF Format]] |

Cited in [[Genome Browser]] and [[Reference Genome]].

## How to use it

- L1: install the desktop application, open a BED file of your own on hg38 and navigate to one feature by typing its coordinates.
- L2: load a sorted, indexed BAM and a VCF from [[10-genomic-pipeline]] and inspect a variant call in its reads.
- L3: embed igv.js in a web page as a reference implementation to compare with [[09-genome-browser]].

## Caveats

- Documentation describes the current desktop release; menus and defaults change between versions (release notes are listed per version).
- Tier A as a tool from a leading institute with peer-reviewed descriptions; its documentation describes the tool, not biology.
- Verified in this pass: the documentation pages listed above (source repository igvteam/igv-docs), the MIT license, the citation of the 2011 paper and its abstract, and the citation of the 2013 paper.
