---
aliases:
  - DSSP paper
  - Kabsch and Sander 1983
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Wolfgang Kabsch
  - Chris Sander
journal: Biopolymers
year: 1983
url: "https://doi.org/10.1002/bip.360221211"
access: partial
---

# Kabsch 1983 - Dictionary of Protein Secondary Structure

> [!abstract]
> The paper that defined secondary structure operationally, from backbone hydrogen-bond patterns found in atomic coordinates, and introduced the DSSP program and its one-letter state codes.

## Why this source

Before this paper, helices and strands were assigned by eye and by inconsistent criteria. DSSP turned the assignment into a reproducible pattern-recognition procedure, so every structure can be labeled the same way: its states are the reference labels used to describe structures, train and evaluate predictors, and compare models.

## Coverage

Citation: Kabsch W, Sander C. "Dictionary of protein secondary structure: pattern recognition of hydrogen-bonded and geometrical features". *Biopolymers* 22(12):2577-2637 (1983). doi:10.1002/bip.360221211.

| Part | Content | Vault notes |
|---|---|---|
| Hydrogen-bond patterns | Backbone hydrogen bonds found from coordinates; elementary patterns "turn" (C=O of residue i to N–H of residue i + n, n = 3, 4, 5) and "bridge" (between residues far apart); repeated turns make helices, repeated bridges make ladders and sheets | [[Secondary Structure Assignment]] |
| State codes | H α helix (4-turn), G 3₁₀ helix (3-turn), I π helix (5-turn), E extended strand in a ladder, B isolated β bridge, T hydrogen-bonded turn, S bend, blank for none | [[Protein Secondary Structure]], [[Secondary Structure Prediction]] |

## How to use it

- **L2**: learn the eight codes and what each pattern means in [[Protein Secondary Structure]], then the full procedure in [[Secondary Structure Assignment]].
- **L3**: run a DSSP implementation on a structure and compare its output with the structure's helices and sheets in a viewer.

## Caveats

- Software and databank are now maintained by other groups and cite later papers; implementations differ in details (version, treatment of special cases), so record which one produced a given assignment.
- Verified in this pass: authors, title, journal, volume, issue, pages, year and DOI (several citing records), and the meaning of the eight codes (DSSP documentation pages). The full text was not read; the description of turns and bridges follows the paper's summary of its method.
