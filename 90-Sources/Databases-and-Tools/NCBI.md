---
aliases:
  - National Center for Biotechnology Information
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
kind: website
tier: A
authors:
  - Eric W. Sayers
institution: NCBI/NLM/NIH
year: 1988
edition:
url: https://www.ncbi.nlm.nih.gov
access: free
---

# NCBI

> [!abstract]
> The portal of the US National Center for Biotechnology Information (part of the National Library of Medicine, NIH): one search entry point to GenBank, PubMed, BLAST, Bookshelf and many other linked databases.

## Why this source

Most first contacts with biological data go through NCBI: a sequence in GenBank, a paper in PubMed, a similarity search with BLAST. Following the links between its databases (a gene to its sequences, proteins, papers and taxonomy) teaches the shape of the whole [[Biological Database]] landscape. NCBI publishes a yearly inventory of its resources in the *Nucleic Acids Research* database issue, which makes it easy to keep this note current.

## Coverage

Key publication: Sayers EW et al. "Database resources of the National Center for Biotechnology Information in 2025". *Nucleic Acids Res* 53(D1):D20-D29 (2025). It describes search and retrieval across 31 repositories and knowledgebases, with the E-utilities as the programming interface.

| Part | Content | Vault notes |
|---|---|---|
| Sequences | GenBank, Sequence Read Archive | [[NCBI GenBank]], [[Next-Generation Sequencing]], [[FASTA Format]] |
| Similarity search | BLAST | [[NCBI BLAST]], [[BLAST]], [[05-sequence-search]] |
| Literature | PubMed, PubMed Central, Bookshelf | [[PubMed]], [[NCBI Bookshelf]], [[Scientific Literature]] |
| Organisms | Taxonomy | [[Phylogenetics]] |
| Proteins | Conserved Domain Database, iCn3D structure viewer | [[Protein Structure]] |
| Programmatic access | E-utilities | [[Biopython]], [[10-genomic-pipeline]] |

The resources named above are those the 2025 paper lists as significantly updated; the full catalogue is larger.

## How to use it

- **L1**: search a gene name met in a biology course from the home page, then follow the links from the gene record to its nucleotide and protein sequences and to PubMed.
- **L2**: download sequences in [[FASTA Format]] as test data for [[01-dna-engine]] and [[04-alignment-engine]]; run a BLAST search on the same sequences.
- **L3**: script queries through the E-utilities (for example with `Bio.Entrez` in [[Biopython]]) instead of clicking, so every data download becomes a reproducible step of [[10-genomic-pipeline]].

## Caveats

- Database names and interfaces change; the yearly NAR database-resources paper is the reliable inventory.
- GenBank exchanges data daily with the [[European Nucleotide Archive]] and DDBJ, so the same nucleotide data can be reached from Europe or Japan too.
- Verified in this pass: establishment in November 1988 at the NLM (legislation signed that month), and the citation and abstract of the 2025 NAR paper. Individual databases are covered in their own notes.
