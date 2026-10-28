---
aliases:
  - SantaLucia 1998
  - Unified nearest-neighbor parameters
tags:
  - type/source
  - domain/chemistry
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - John SantaLucia Jr.
journal: Proceedings of the National Academy of Sciences of the United States of America
year: 1998
url: "https://doi.org/10.1073/pnas.95.4.1460"
access: free
---

# SantaLucia 1998 - A Unified View of Polymer, Dumbbell, and Oligonucleotide DNA Nearest-Neighbor Thermodynamics

> [!abstract]
> The paper that reconciled the published DNA nearest-neighbor parameter sets and proposed one unified set of Watson-Crick stacking enthalpies and entropies for predicting duplex stability and melting temperatures.

## Why this source

Primer and probe melting temperatures are computed by summing the enthalpy and entropy of each dinucleotide step of a duplex. Before this paper, laboratories had published sets that seemed to disagree because they used different data, analysis methods and salt conditions. SantaLucia put seven sets in a common format, showed that six of them agree closely, and derived one set from 108 oligonucleotide duplexes that describes both polymers and oligomers, together with empirical salt-dependence relationships. It is the natural primary citation for a nearest-neighbor Tm calculation.

## Coverage

Citation: SantaLucia J Jr. "A unified view of polymer, dumbbell, and oligonucleotide DNA nearest-neighbor thermodynamics". *Proceedings of the National Academy of Sciences of the USA* 95(4):1460-1465 (17 February 1998). doi:10.1073/pnas.95.4.1460. Free at PMC19045.

| Part | Content | Vault notes |
|---|---|---|
| Comparison | Nearest-neighbor parameters from seven laboratories in one format; six agree closely | [[Van 't Hoff Equation]], [[DNA]] |
| Unified parameters | One set of Watson-Crick nearest-neighbor $\Delta H^\circ$ and $\Delta S^\circ$ (with initiation and symmetry terms, 1 M NaCl), derived from 108 oligonucleotide duplexes | [[Van 't Hoff Equation]], [[Polymerase Chain Reaction]], [[Nucleic Acid Hybridization]] |
| Salt dependence | Empirical relationships for other salt concentrations | [[Polymerase Chain Reaction]] |

Cited in [[Van 't Hoff Equation]].

## How to use it

- **L2**: compute the $\Delta H^\circ$, $\Delta S^\circ$ and melting temperature of a short duplex by hand with the unified table ([[Van 't Hoff Equation#Worked example]]).
- **L3**: implement the model, then compare your values with a primer-design tool and see how much the salt correction and the strand concentration move the result.

## Caveats

- Verified in this pass: the citation (journal, volume, issue, pages, date, DOI, PMC record) and the abstract (seven parameter sets compared, six in agreement, a unified set from 108 duplexes, salt dependence).
- The parameter values quoted in the vault were cross-checked against an independent implementation, the `DNA_NN3` table of Biopython 1.85 (`Bio.SeqUtils.MeltingTemp`), which attributes the same values to Allawi and SantaLucia (1997); they were not re-read in the paper's own table in this pass.
- The unified set covers perfectly matched Watson-Crick duplexes in 1 M NaCl. Mismatches, dangling ends and other salt conditions need further parameters, and later sets (for example SantaLucia and Hicks 2004) change the initiation terms: record which set a tool uses.
