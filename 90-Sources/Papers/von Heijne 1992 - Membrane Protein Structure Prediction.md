---
aliases:
  - von Heijne 1992
  - TopPred paper
  - Positive-inside rule
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Gunnar von Heijne
journal: Journal of Molecular Biology
year: 1992
url: "https://pubmed.ncbi.nlm.nih.gov/1593632/"
access: partial
---

# von Heijne 1992 - Membrane Protein Structure Prediction

> [!abstract]
> The paper that turned hydropathy plots into topology predictions: candidate transmembrane segments from hydrophobicity analysis, all possible topologies generated, and the best one chosen with the positive-inside rule.

## Why this source

A hydropathy plot says where the membrane-spanning segments are, not which way they run. This paper adds the missing step with a simple, interpretable rule (positively charged residues are enriched in the loops that stay on the cytoplasmic side) and shows how far it goes on proteins of known topology. It is the logic behind TopPred and the starting point of later statistical predictors.

## Coverage

Citation: von Heijne G. "Membrane protein structure prediction. Hydrophobicity analysis and the positive-inside rule". *Journal of Molecular Biology* 225:487-494 (1992). PMID 1593632.

| Part | Content | Vault notes |
|---|---|---|
| Hydrophobicity analysis | Candidate transmembrane segments from a hydrophobicity profile | [[Hydropathy Plot]], [[Membrane Protein]] |
| Topology generation and ranking | All possible topologies generated automatically, then ranked by the positive-inside rule | [[Membrane Protein]] |
| Evaluation | Correct topology for 23 of 24 bacterial inner membrane proteins of known topology; 135 transmembrane segments found with one overprediction | [[Membrane Protein]] |

## How to use it

- **L2**: read the abstract after [[Hydropathy Plot]], then implement the orientation step on a toy sequence ([[Membrane Protein#Computational representation]]).
- **L3**: compare with hidden Markov model predictors, which learn the same grammar from data ([[Krogh 2001 - Predicting Transmembrane Protein Topology with a Hidden Markov Model]]).

## Caveats

- Evaluated on bacterial inner membrane proteins; the method concerns α-helical proteins, not β barrels.
- Verified in this pass: author, title, journal, volume, pages, year and PMID (abstract records), and the abstract-level results listed above. The full text was not read, so details of the method (window, thresholds, loop-length limits) are not quoted in the vault.
