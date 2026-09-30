---
aliases:
  - Pearson 2013
  - An Introduction to Sequence Similarity (Homology) Searching
tags:
  - type/source
  - domain/bioinformatics
  - domain/statistics
  - level/L1
  - level/L2
  - level/L3
kind: paper
tier: B
authors:
  - William R. Pearson
journal: Current Protocols in Bioinformatics
year: 2013
url: "https://doi.org/10.1002/0471250953.bi0301s42"
access: free
---

# Pearson 2013 - An Introduction to Sequence Similarity Searching

> [!abstract]
> A peer-reviewed tutorial by the author of the FASTA programs on how sequence similarity searches detect homologs, and on the statistics that make the inference reliable.

## Why this source

It states precisely the logic behind every [[BLAST]] or FASTA search: homologous sequences share a common ancestor, and homology is **inferred** from excess similarity, that is, statistically significant similarity that reflects common ancestry. It gives practical numbers: DNA:DNA alignments have a 5 to 10-fold shorter evolutionary look-back time than protein:protein or translated DNA:protein alignments, rarely detecting homology after 200 to 400 million years of divergence, while protein:protein alignments routinely detect homology in sequences that last shared an ancestor more than 2.5 billion years ago (for example humans and bacteria). It also contrasts significance thresholds: protein:protein expectation values below 0.001 can reliably be used to infer homology, whereas DNA:DNA expectation values below $10^{-6}$ often occur by chance and $10^{-10}$ is a more widely accepted threshold.

## Coverage

Citation: Pearson WR. "An introduction to sequence similarity ('homology') searching". *Current Protocols in Bioinformatics* 42:3.1.1-3.1.8 (2013). doi:10.1002/0471250953.bi0301s42. Free at PMC3820096.

| Part | Content | Vault notes |
|---|---|---|
| Homology and similarity | Homology inferred from statistically significant (excess) similarity | [[Sequence Homology]], [[Sequence Alignment]] |
| DNA versus protein | Evolutionary look-back time of DNA:DNA and protein:protein comparisons | [[Sequence Homology]], [[BLAST]] |
| Statistics | Expectation values and thresholds for inferring homology | [[E-Value]] |

Cited in [[Sequence Homology]] and [[Sequence Alignment]].

## How to use it

- L1: read the introduction with [[Sequence Homology]].
- L2: return to it with [[BLAST]] and [[E-Value]], then run the same query at the DNA and protein level with [[NCBI BLAST]] and compare the hits.

## Caveats

- An overview unit; the detailed protocols are in companion units of the same chapter.
- Verified in this pass: citation metadata, the definition of homology inference, the look-back times and the expectation-value thresholds quoted above.
