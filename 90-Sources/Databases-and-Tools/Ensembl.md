---
aliases: []
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
  - level/M1
kind: database
tier: A
authors: []
institution: EMBL-EBI
year:
edition:
url: https://www.ensembl.org
access: free
---

# Ensembl

> [!abstract]
> An open platform integrating public genomics data across the tree of life, focused on eukaryotic species related to human health, agriculture and biodiversity: genome browser, gene and transcript annotation, comparative genomics and variation tools.

## Why this source

Ensembl puts gene models, genetic variation, homology and regulation on the same genome coordinates, with a consistent annotation pipeline across species. It is the reference to learn how [[Gene Annotation]] is produced and how a [[Genetic Variant]] is interpreted, and the natural data source for [[09-genome-browser]] and [[10-genomic-pipeline]].

> [!info] History
> The Ensembl project started in 1999, as a joint project of EMBL-EBI and the Sanger Centre (now the Wellcome Sanger Institute), to annotate the human genome automatically and make the annotation public.

## Coverage

Key publication: "Ensembl 2025". *Nucleic Acids Res* 53(D1) (2025), PMID 39656687. At that release: more than 4,800 eukaryotic and 31,300 prokaryotic genomes; a new beta site with more than 2,700 eukaryotic assemblies (genome, gene, transcript, homology and variation views) that will replace the Rapid Release site; improved regulatory annotation for human, mouse and agricultural species; an expanded Variant Effect Predictor (VEP).

| Part | Content | Vault notes |
|---|---|---|
| Genome browser | Assemblies with annotation tracks | [[Genome]], [[09-genome-browser]] |
| Genes and transcripts | Evidence-based gene models | [[Gene Annotation]], [[Gene]], [[GFF Format]] |
| Comparative genomics | Homology and gene trees | [[Sequence Homology]], [[Phylogenetic Tree]] |
| Variation and VEP | Variant data and consequence prediction | [[Genetic Variant]], [[Variant Annotation]], [[10-genomic-pipeline]] |
| Regulation | Regulatory annotation | [[Gene Regulation]] |

## How to use it

- **L2**: look up a human gene, compare its transcripts and exons, then export the annotation of a region to load in [[09-genome-browser]].
- **L3**: run VEP on a small [[VCF Format|VCF]] produced by [[03-genome-diff]] or [[10-genomic-pipeline]] and compare its consequence calls with your own.
- **M1**: explore gene trees and homology views for a gene family; follow the regulatory annotation of a locus.

## Caveats

- Annotation is versioned by release: record the release and assembly with every download.
- Before mixing files from Ensembl and the [[UCSC Genome Browser]], check assembly version, chromosome naming and coordinate convention.
- The interface is in transition (beta site replacing Rapid Release in 2025).
- Launch year and author list were not verified in this pass; `year` and `authors` are left empty.
