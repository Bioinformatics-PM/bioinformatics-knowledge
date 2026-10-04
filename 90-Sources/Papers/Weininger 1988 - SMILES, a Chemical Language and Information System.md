---
aliases:
  - Weininger 1988
  - SMILES paper
  - "SMILES, a chemical language and information system. 1. Introduction to methodology and encoding rules"
tags:
  - type/source
  - domain/chemistry
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - David Weininger
journal: Journal of Chemical Information and Computer Sciences
year: 1988
url: "https://doi.org/10.1021/ci00057a005"
access: paid
---

# Weininger 1988 - SMILES, a Chemical Language and Information System

> [!abstract]
> The paper that introduced SMILES, a line notation that writes a molecular structure as a short string of characters, based on molecular graph theory and designed for both chemists and computers.

## Why this source

SMILES became the most common text representation of small-molecule structures in compound databases, ligand files and cheminformatics toolkits. The paper presents it as a notation with a very small grammar, grounded in molecular graph theory, that allows rigorous structure specification and fast machine processing; it lists the applications this enables: generating a unique notation, constant-speed database retrieval, substructure searching and property prediction.

## Coverage

Citation: Weininger D. *J. Chem. Inf. Comput. Sci.* 28(1):31-36 (1988). doi:10.1021/ci00057a005

| Part | Content | Vault notes |
|---|---|---|
| Methodology | A molecule as a graph of atoms and bonds, written as a linear string | [[Skeletal Formula]], [[Graph]] |
| Encoding rules | How a structure is spelled as a string (the paper's title topic) | [[Skeletal Formula]], [[Molecular Representation]] |
| Applications | Unique notation, database retrieval, substructure search, property prediction | [[Molecular Representation]], [[Molecular Fingerprint]] |

## How to use it

- L1: read the abstract and the encoding examples after learning to read a [[Skeletal Formula]].
- L2-L3: for the exact, current grammar (bracket atoms, stereo marks, aromaticity) use [[OpenSMILES Specification]]; this paper is the historical origin.

## Caveats

- Only the bibliographic record, abstract and the scope stated in the title were verified; section-level content was not checked.
- A second part, by D. Weininger, A. Weininger and J. L. Weininger, followed; it is not described here.
- The journal has since been renamed *Journal of Chemical Information and Modeling*. Open-access status of the publisher PDF not verified.
