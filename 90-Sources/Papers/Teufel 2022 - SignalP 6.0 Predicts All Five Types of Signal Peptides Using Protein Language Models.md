---
aliases:
  - SignalP 6.0
  - SignalP
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
  - level/M1
kind: paper
tier: A
authors:
  - Felix Teufel
  - et al.
journal: Nature Biotechnology
year: 2022
url: "https://pubmed.ncbi.nlm.nih.gov/34980915/"
access: free
---

# Teufel 2022 - SignalP 6.0 Predicts All Five Types of Signal Peptides Using Protein Language Models

> [!abstract]
> The paper behind SignalP 6.0, the current version of the reference signal peptide predictor: a model built on a protein language model that detects all five known types of signal peptides and their internal regions.

## Why this source

SignalP is the tool most annotation pipelines use to call signal peptides, and this short paper shows how its approach changed: from networks trained on curated signal peptides alone to a model that first learns from millions of unannotated sequences. It is the natural reference for the "logic behind localization predictors" and for what protein language models add to sequence annotation.

## Coverage

Citation: Teufel F, et al. "SignalP 6.0 predicts all five types of signal peptides using protein language models". *Nature Biotechnology* 40(7):1023-1025 (2022). doi:10.1038/s41587-021-01156-3. PMID 34980915; free author manuscript PMC9287161.

| Part | Content | Vault notes |
|---|---|---|
| Problem | Signal peptides control protein secretion and translocation in all living organisms; existing algorithms could not detect all known types | [[Protein Targeting]] |
| Model | Protein language models that use information from millions of unannotated sequences across all domains of life; applicable to metagenomic data | [[Protein Language Model]] |
| Output | The five signal peptide types, and the n-, h- and c-regions of each signal peptide | [[Protein Targeting]] |
| Types | One example: Sec/SPIII signal peptides control the translocation of type IV pilin-like proteins in prokaryotes | [[Bacteria]] |
| Generalization | Better than SignalP 5.0 on sequences distantly related to the training data (preprint version) | [[Cross-Validation]] |

## How to use it

- **L2**: run the SignalP web service on a known secreted protein and compare its predicted cleavage site with the UniProt annotation.
- **L3**: read the figure of predicted regions next to a hand-made rule (the toy sorter of [[Protein Targeting]]).
- **M1**: read the method as a case of transfer learning from a protein language model, and the benchmark as a lesson in homology-aware evaluation.

## Caveats

- A short communication: the details are in the supplementary material and in the bioRxiv preprint (doi:10.1101/2021.06.09.447770).
- Verified in this pass (web search): the citation, DOI, PMID and PMC numbers, the abstract claims, the Sec/SPIII example, and the generalization claim of the preprint. The names of the other four types and the full author list (abbreviated here) were not verified.
