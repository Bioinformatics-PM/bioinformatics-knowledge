---
aliases:
  - NCBI BLAST+
  - BLAST web service
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
kind: tool
tier: A
authors:
  - Christiam Camacho
institution: NCBI/NLM/NIH
year:
edition:
url: https://blast.ncbi.nlm.nih.gov/
access: free
---

# NCBI BLAST

> [!abstract]
> NCBI's web service and downloadable command-line suite (BLAST+) for finding sequences similar to a query in large sequence databases.

## Why this source

It is the reference implementation of the heuristic described in [[Altschul 1990 - Basic Local Alignment Search Tool]]. The concept note [[BLAST]] explains how it works; this service lets you run it on real databases, read real significance statistics, and benchmark your own engine from [[05-sequence-search]] against it.

## Coverage

Key publications:
- "NCBI BLAST: a better web interface". *Nucleic Acids Res* (2008): reengineered web interface with simplified search forms, a list of recent results, saved search strategies and a documentation directory.
- Camacho C, Coulouris G, Avagyan V, Ma N, Papadopoulos J, Bealer K, Madden TL. "BLAST+: architecture and applications". *BMC Bioinformatics* 10:421 (2009): rewritten command-line applications that split long queries into chunks and retrieve only the relevant parts of long database sequences.

| Part | Content | Vault notes |
|---|---|---|
| Web search forms | Nucleotide and protein queries against NCBI databases | [[BLAST]], [[Sequence Alignment\|Local Alignment]], [[Sequence Homology]] |
| Result page | Hit list with scores, E-values and pairwise alignments | [[E-value]], [[Substitution Matrix]], [[Sequence Alignment]] |
| BLAST+ | Command-line applications and local databases | [[05-sequence-search]], [[10-genomic-pipeline]] |
| Algorithm | Seed-and-extend heuristic | [[Seed and Extend\|Seed-and-Extend]], [[k-mer]] |

## How to use it

- **L1**: paste a short sequence in [[FASTA Format]] into a nucleotide search and read the top hit: identity, query coverage, E-value.
- **L2**: search a coding sequence at the nucleotide level and its translation at the protein level, then compare the hits; change the scoring parameters and watch the E-values move. Compare one alignment with the exact [[Smith-Waterman Algorithm]] in [[04-alignment-engine]].
- **L3**: install BLAST+, build a local database from your own FASTA files and run the same queries as your [[05-sequence-search]] engine to compare speed and sensitivity.

## Caveats

- An E-value depends on the database searched, so record the database and its date with every result; default databases and parameters change over time.
- The launch year of the web service was not verified in this pass; the algorithm itself dates from the 1990 paper.
- Verified in this pass: the citations and abstract contents of the 2008 and 2009 papers, and BLAST+ as the currently supported download.
