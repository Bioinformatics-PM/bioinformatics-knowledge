---
aliases:
  - ENA
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
  - Colman O'Cathail
institution: EMBL-EBI
year:
edition:
url: https://www.ebi.ac.uk/ena
access: free
---

# European Nucleotide Archive

> [!abstract]
> EMBL-EBI's open archive for the deposition of and access to nucleotide sequencing data, Europe's partner in the international exchange with GenBank and the DNA Data Bank of Japan.

## Why this source

ENA is where published sequencing experiments can be found and downloaded with their study and sample metadata. For a learner it is the entry point to real raw data: the accession in a paper's data availability statement leads here, and from here to the files that feed [[10-genomic-pipeline]].

## Coverage

Key publication: O'Cathail C et al. "The European Nucleotide Archive in 2024". *Nucleic Acids Res* (published online 18 November 2024). doi:10.1093/nar/gkae975. It reports the year's changes toward three goals: interoperability, globalisation of the service, and scaling the platform. ENA publishes such an update every year (a 2025 update also exists).

| Part | Content | Vault notes |
|---|---|---|
| Sequencing data | Open nucleotide sequencing data, from reads to annotated sequences | [[Next-Generation Sequencing]], [[FASTQ Format]], [[Genome Assembly]] |
| Metadata | Studies and samples behind each dataset | [[Research Data Management]], [[Reproducibility]] |
| Deposition | Submission services for new data | [[Scientific Practice]] |
| Exchange | Daily exchange with GenBank and DDBJ (INSDC) | [[NCBI GenBank]] |

## How to use it

- **L2**: take an accession from a paper you read, find its study in ENA, and list its samples and sequencing runs.
- **L3**: download the reads of one small run for [[10-genomic-pipeline]]; store the accessions in the project so the analysis can be rerun from scratch.
- **M1**: learn the submission model (study, sample, run) before depositing your own data.

## Caveats

- Metadata quality depends on submitters; check sample descriptions before comparing datasets.
- Datasets are large: start with the smallest run that answers your question.
- Because the partners exchange data, the same dataset may also be reached through [[NCBI]]; keep the original accession in your notes.
- Launch year was not verified in this pass. Verified: the 2024 paper (first author, DOI, abstract) and the INSDC daily exchange.
