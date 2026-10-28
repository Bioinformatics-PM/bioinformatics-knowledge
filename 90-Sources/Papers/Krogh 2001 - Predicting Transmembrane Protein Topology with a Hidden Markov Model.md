---
aliases:
  - TMHMM paper
  - Krogh 2001
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L3
  - level/M1
kind: paper
tier: S
authors:
  - Anders Krogh
  - Björn Larsson
  - Gunnar von Heijne
  - Erik L. L. Sonnhammer
journal: Journal of Molecular Biology
year: 2001
url: "https://pubmed.ncbi.nlm.nih.gov/11152613/"
access: partial
---

# Krogh 2001 - Predicting Transmembrane Protein Topology with a Hidden Markov Model

> [!abstract]
> The TMHMM paper: a hidden Markov model that predicts transmembrane helices and their orientation in one pass, applied to complete genomes to estimate how many genes encode membrane proteins.

## Why this source

It replaces the window-and-threshold heuristics of hydropathy plots with a probabilistic model whose states encode the grammar of a membrane protein (cytoplasmic loop, helix core and caps, non-cytoplasmic loop), the standard example of a hidden Markov model in protein bioinformatics. Its genome-wide estimate is the usual reference for the share of membrane proteins.

## Coverage

Citation: Krogh A, Larsson B, von Heijne G, Sonnhammer ELL. "Predicting transmembrane protein topology with a hidden Markov model: application to complete genomes". *Journal of Molecular Biology* 305(3):567-580 (2001). PMID 11152613.

| Part | Content | Vault notes |
|---|---|---|
| Model | A hidden Markov model of membrane protein topology (TMHMM) | [[Hidden Markov Model]], [[Membrane Protein]] |
| Accuracy | 97-98 % of transmembrane helices correctly predicted; better than 99 % specificity and sensitivity in separating membrane from soluble proteins, lower when signal peptides are present | [[Membrane Protein]] |
| Genomes | 20 to 30 % of the genes of most genomes encode membrane proteins | [[Membrane Protein]], [[Functional Annotation]] |

## How to use it

- **L3**: read the abstract and the model architecture after [[Hidden Markov Model]]; run a topology predictor on proteins of known structure.
- **M1**: compare its predictions with newer deep-learning predictors and with experimental structures.

## Caveats

- TMHMM 2.0 is old: its server at DTU Health Tech marks it as outdated and points to a newer deep-learning predictor. Use the paper for the method and the genome-scale estimate.
- Verified in this pass: authors, title, journal, volume, issue, pages, year and PMID, and the accuracy figures and genome estimate of the abstract. Table values behind the estimate were not checked.
