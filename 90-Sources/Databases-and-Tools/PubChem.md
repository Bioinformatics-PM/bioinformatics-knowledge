---
aliases:
  - PubChem Compound
  - NCBI PubChem
tags:
  - type/source
  - domain/chemistry
  - domain/bioinformatics
  - level/L1
  - level/L2
kind: database
tier: A
authors: []
institution: National Center for Biotechnology Information (NCBI), NIH
year: 2025
edition:
url: https://pubchem.ncbi.nlm.nih.gov
access: free
---

# PubChem

> [!abstract]
> The NIH's open chemistry database: one record per compound, with its structure, molecular formula, computed masses and links to bioactivity data and literature.

## Why this source

- The reference place to look up a small molecule (a metabolite, a drug, a reagent) and read its formula and masses, as stored and used by software.
- Programmatic access (PUG-REST) returns computed properties by name, which makes it the natural check for a formula parser or a mass calculator written in the vault.

## Coverage

Key publication: Kim S et al. "PubChem 2025 update". *Nucleic Acids Research* 53(D1), 2025 (PMC11701734). It describes more than 1000 data sources, 119 million compounds, 322 million substances and 295 million bioactivities, and new interfaces such as a consolidated literature panel and a patent knowledge panel.

| Part | Content | Vault notes |
|---|---|---|
| Compound records | Structure, molecular formula, computed properties | [[Molecule]], [[Lewis Structure]] |
| Computed properties (PUG-REST names) | `MolecularFormula`, `MolecularWeight` (sum of atomic weights, natural isotopic abundance assumed, g/mol), `ExactMass`, `MonoisotopicMass` | [[Molecule]], [[Monoisotopic Mass]] |
| Line notations | SMILES and InChI strings of each compound | [[Lewis Structure]] |
| Bioactivity | Results of biological assays | [[Biological Database]] |

## How to use it

- L1: look up glucose or ATP, read the molecular formula and molecular weight, and recompute them by hand ([[Molecule]]).
- L2: query computed properties for a list of compounds through PUG-REST (`/rest/pug/compound/cid/{cid}/property/MolecularFormula,MolecularWeight/JSON`) and compare them with your own calculator.

## Caveats

- Computed properties come from PubChem's own software; average masses depend on the atomic weights used, so the last decimal can differ from another tool.
- Database statistics change with every release; the numbers above are those of the 2025 update.
- Pages of the 2025 update article and the full list of PUG-REST properties were verified through search-engine extracts only, not by opening the documentation.
