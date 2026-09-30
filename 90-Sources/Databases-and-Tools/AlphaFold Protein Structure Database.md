---
aliases:
  - AlphaFold DB
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - domain/computer-science
  - level/L2
  - level/L3
  - level/M1
kind: database
tier: A
authors:
  - Mihaly Varadi
institution: Google DeepMind and EMBL-EBI
year: 2021
edition:
url: https://alphafold.ebi.ac.uk
access: free
---

# AlphaFold Protein Structure Database

> [!abstract]
> An open database of protein structure predictions made with Google DeepMind's AlphaFold 2, launched with EMBL-EBI in July 2021 and grown to cover more than 214 million protein sequences.

## Why this source

It turned predicted structure into a routine lookup: for most proteins without an experimental structure, a model now exists. It is the best place to learn to read a predicted model critically, confidence first, and to compare prediction with experiment in the [[RCSB Protein Data Bank]].

## Coverage

Key publication: Varadi M et al. "AlphaFold Protein Structure Database in 2024: providing structure coverage for over 214 million protein sequences". *Nucleic Acids Res* 52(D1):D368-D375 (2024). doi:10.1093/nar/gkad1011. It describes growth from the initial release of 2021 through releases covering model organisms, global health proteomes and Swiss-Prot; integration of the predictions into PDB, UniProt, Ensembl, InterPro and MobiDB; access from FTP files to Google Cloud Public Datasets; and improvements to the Predicted Aligned Error viewer, the 3D viewer and search.

| Part | Content | Vault notes |
|---|---|---|
| Predicted models | One entry per protein sequence | [[Protein Structure]], [[Protein Folding]] |
| Confidence | Predicted Aligned Error viewer and confidence colouring | [[Structural Bioinformatics]] |
| Integration | Models shown in partner resources | [[UniProt]], [[RCSB Protein Data Bank]], [[Ensembl]] |
| Bulk access | FTP and Google Cloud Public Datasets | [[Research Data Management]] |
| Method background | Deep learning prediction | [[Statistical Learning\|Machine Learning]], [[Neural Network]] |

## How to use it

- **L2**: open the model of a protein you already looked up in [[UniProt]]; read the confidence colouring and the Predicted Aligned Error plot before the 3D shape.
- **L3**: compare the model with an experimental structure of the same protein and list where they agree; mark low-confidence regions.
- **M1**: read the data-access section of the paper and plan a bulk analysis on a whole proteome.

## Caveats

- A prediction is not an experiment: treat low-confidence regions as unknown, not as structure.
- Model coverage follows the UniProt sequences included in each release; record the release used.
- Verified in this pass: the 2024 paper (citation, DOI, abstract) and the July 2021 launch by DeepMind and EMBL-EBI.
