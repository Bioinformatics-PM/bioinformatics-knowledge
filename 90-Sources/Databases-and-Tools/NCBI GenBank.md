---
aliases:
  - GenBank
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
  - Eric W. Sayers
institution: NCBI/NLM/NIH
year: 1982
edition:
url: https://www.ncbi.nlm.nih.gov/genbank/
access: free
---

# NCBI GenBank

> [!abstract]
> NCBI's public archive of annotated nucleotide sequences, built from laboratory and sequencing-project submissions and synchronized daily with the European Nucleotide Archive and the DNA Data Bank of Japan.

## Why this source

GenBank is the primary archive: the place a sequence is deposited when it is published. Reading one GenBank record (organism, references, feature table, sequence) is the fastest way to see what a [[Gene Annotation]] looks like in practice, and its records are the raw material of most Lab projects.

> [!info] History
> GenBank grew out of the Los Alamos Sequence Database started by Walter Goad; the public GenBank was created in 1982 at Los Alamos National Laboratory and moved to [[NCBI]] in 1992.

## Coverage

Key publication: Sayers EW, Cavanaugh M, Frisse L, Pruitt KD, Schneider VA, Underwood BA, Yankie L, Karsch-Mizrachi I. "GenBank 2025 update". *Nucleic Acids Res* 53(D1) (2025). doi:10.1093/nar/gkae1114. At that update: 34 trillion base pairs from over 4.7 billion sequences, for 581,000 formally described species.

| Part | Content | Vault notes |
|---|---|---|
| Records | Nucleotide sequences with organism, references and feature annotation | [[Genome]], [[Gene Annotation]], [[FASTA Format]] |
| Features | Annotated regions such as genes and coding sequences | [[Open Reading Frame]], [[02-sequence-translation]] |
| Submission | Submission Portal; BioProject and BioSample records | [[Research Data Management]] |
| Access | Web, programming (API) and command-line interfaces | [[NCBI]], [[Biopython]] |
| Exchange | Daily exchange with ENA and DDBJ | [[European Nucleotide Archive]] |

## How to use it

- **L1**: open the record of a well-known gene, read the header, the feature table and the sequence; download it in [[FASTA Format]].
- **L2**: parse the GenBank flat file with `Bio.SeqIO` ([[Biopython]]) and check the annotated coding sequence against your own translation in [[02-sequence-translation]]; collect homologous sequences for [[08-phylogenetic-engine]].
- **L3**: follow BioProject and BioSample links to the experimental metadata; decide when an archival record is good enough and when a curated reference collection is needed.

## Caveats

- An archive, not a curated reference: records reflect what submitters provided, so redundancy and annotation quality vary. NCBI's curated reference collections were not reviewed in this pass.
- Size figures grow with every release: always quote them with their date.
- Verified in this pass: the 2025 update (authors, DOI, abstract), the 1982 origin and the INSDC data exchange.
