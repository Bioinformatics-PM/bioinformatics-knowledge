---
aliases:
  - RefSeq
  - NCBI Reference Sequence Database
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
kind: database
tier: A
authors:
  - Nuala A. O'Leary
institution: NCBI/NLM/NIH
year:
edition:
url: https://www.ncbi.nlm.nih.gov/refseq/
access: free
---

# NCBI RefSeq

> [!abstract]
> NCBI's curated, non-redundant collection of reference genomic, transcript and protein sequences, built from the public archives by computation, manual curation and collaboration.

## Why this source

RefSeq is the textbook example of a secondary database built on a primary archive: it takes sequences submitted to the INSDC ([[NCBI GenBank]], [[European Nucleotide Archive]], DDBJ) and produces one stable reference record per molecule. Its identifiers (`NM_`, `NP_`, `NC_`...) are the ones used in clinical variant descriptions and in most human gene annotations, which makes them the first identifiers a bioinformatician learns to read ([[Accession Number]]).

## Coverage

Key publications:

- O'Leary NA et al. "Reference sequence (RefSeq) database at NCBI: current status, taxonomic expansion, and functional annotation". *Nucleic Acids Res* 44(D1):D733-D745 (2016). PMID 26553804. RefSeq leverages INSDC data, computation, manual curation and collaboration to produce a standard set of stable, non-redundant reference sequences; at release 71 it covered more than 55,000 organisms.
- "NCBI RefSeq: reference sequence standards through 25 years of curation and annotation". *Nucleic Acids Res* 53(D1):D243-D257 (2025). PMID 39526381. Status of the eukaryotic, prokaryotic and viral collections, with a focus on eukaryotic annotation.
- NLM support documentation on the RefSeq accession format: a two-letter prefix, an underscore, a series of digits, then `.version`; the version changes when the sequence changes and persists through updates of references, source information and other non-sequence data.

| Part | Content | Vault notes |
|---|---|---|
| Accession prefixes | `NC_` complete genomic molecule, `NG_` genomic region, `NM_` mRNA, `NR_` non-coding RNA, `NP_` protein, `NT_`/`NW_` contig or scaffold; `XM_`, `XR_`, `XP_` predicted models | [[Accession Number]] |
| Known and model records | Known RefSeq records are reviewed by NCBI staff or collaborators; model records come from an automated pipeline | [[Biological Database]], [[Gene Annotation]] |
| Versions | `accession.version`, incremented when the sequence is updated | [[Accession Number]], [[Data Provenance]] |
| Collections | Genomic, transcript and protein records across the tree of life | [[Genome]], [[Transcriptome]], [[Proteome]] |

## How to use it

- **L1**: open the RefSeq mRNA of a gene you know and identify its prefix, number and version; compare with the protein record it links to.
- **L2**: when a pipeline needs "the" transcript of a gene, prefer a versioned RefSeq accession and record it in the configuration ([[10-genomic-pipeline]]).
- **L3**: compare a known (`NM_`) and a model (`XM_`) record of the same gene family and list what differs in their evidence.

## Caveats

- Model (`X`-prefixed) records are predictions; treat them like unreviewed annotation.
- Record counts change with every release: quote them with the release number.
- Verified in this pass: the 2016 and 2025 papers (titles, journal, volume, pages, PubMed identifiers, abstracts), the URL, and the accession format and prefix table from NLM documentation. Launch year not verified; `year` is left empty.
