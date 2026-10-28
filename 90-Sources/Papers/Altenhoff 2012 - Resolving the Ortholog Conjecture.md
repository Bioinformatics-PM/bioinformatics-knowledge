---
aliases:
  - Altenhoff 2012
  - Ortholog conjecture paper
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Adrian M. Altenhoff
  - Romain A. Studer
  - Marc Robinson-Rechavi
  - Christophe Dessimoz
journal: PLoS Computational Biology
year: 2012
url: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3355068/"
access: free
---

# Altenhoff 2012 - Resolving the Ortholog Conjecture

> [!abstract]
> A test of the "ortholog conjecture" on experimentally supported Gene Ontology annotations from 13 genomes: once annotation biases are controlled, orthologs are weakly but significantly more similar in function than paralogs.

## Why this source

The ortholog conjecture, or standard model of phylogenomics, holds that protein function changes rapidly after duplication, leading to paralogs with different functions, while orthologs retain the ancestral function. Transferring annotations between species relies on it. This paper tested it on experimental annotations and showed that the answer depends on controlling biases in the annotation data: authorship bias, variation of GO term frequency among species, variation of background similarity among species pairs, and propagated annotation bias. After these controls, orthologs generally have more similar functional annotations than paralogs, an effect that is especially strong for subcellular localization. It is also a model of how to test a biological rule of thumb on database annotations.

## Coverage

Citation: Altenhoff AM, Studer RA, Robinson-Rechavi M, Dessimoz C. "Resolving the ortholog conjecture: orthologs tend to be weakly, but significantly, more similar in function than paralogs". *PLoS Computational Biology* 8(5):e1002514 (2012). Free at PMC3355068.

| Part | Content | Vault notes |
|---|---|---|
| Question | The ortholog conjecture as the basis of function transfer | [[Ortholog]], [[Functional Annotation]] |
| Data | Experimentally supported GO annotations of homologs from 13 genomes | [[Gene Ontology Annotation]] |
| Biases | Authorship, GO term frequency, background similarity, propagated annotations | [[Gene Ontology Annotation]] |
| Result | Orthologs more similar in function than paralogs, weak but significant; strongest for subcellular localization | [[Ortholog]], [[Paralog]] |

## How to use it

- L3: read the abstract and author summary after [[Ortholog]].
- M1: read the bias controls as a case study before analysing annotation data ([[Gene Ontology Annotation]]). Compare with an earlier test of the conjecture on mammalian data: Nehrt NL, Clark WT, Radivojac P, Hahn MW, "Testing the ortholog conjecture with comparative functional genomic data from mammals", *PLoS Computational Biology* 7(6):e1002073 (2011).

## Caveats

- Verified in this pass (web search): authors, title, journal, date (May 2012), article number, the free PMC record and the content of the abstract summarized above. For the 2011 study only the citation was verified, not its results; the methods of both papers were not checked in the full text.
