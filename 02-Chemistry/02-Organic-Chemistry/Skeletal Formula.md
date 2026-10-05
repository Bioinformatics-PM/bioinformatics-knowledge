---
aliases:
  - Line-Angle Formula
  - Skeletal Structure
  - Bond-Line Formula
  - Formule topologique
tags:
  - type/concept
  - domain/chemistry
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Lewis Structure]]"
  - "[[Covalent Bond]]"
  - "[[Molecular Geometry]]"
related:
  - "[[Functional Group]]"
  - "[[Isomer]]"
  - "[[Stereochemistry]]"
  - "[[Aromaticity]]"
  - "[[Molecular Representation]]"
  - "[[Graph]]"
projects: []
sources:
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Weininger 1988 - SMILES, a Chemical Language and Information System]]"
  - "[[OpenSMILES Specification]]"
  - "[[PubChem]]"
---

# Skeletal Formula

> [!abstract]
> A skeletal formula draws a molecule as a zigzag of lines: carbons sit at every corner and line end, the hydrogens on carbon are left out because you can count them, and every other atom is written.

## Definition

A **skeletal formula** (line-angle formula) represents an organic molecule by its bonds only. By convention: (1) a carbon atom is assumed at each intersection of two lines and at the end of each line; (2) hydrogens bonded to carbon are not drawn, because carbon always has a valence of 4; (3) atoms other than carbon and hydrogen are drawn, with their hydrogens.[^os112]

## Why it matters

- **Every structure you will meet is drawn this way.** Metabolites in pathway maps, ligands in PDB entries and compound records in [[PubChem]] are shown as skeletal formulas; reading them is the entry point to [[Functional Group|functional groups]], [[Stereochemistry]] and reaction mechanisms.
- **It is a graph, and so is SMILES.** A skeletal formula is a hydrogen-suppressed molecular [[Graph]]. SMILES, the text notation stored in compound tables, writes the same graph as a string, and it also leaves hydrogens implicit.[^weininger][^osm] Counting the implied hydrogens gives the molecular formula, hence the mass matched by metabolomics and proteomics software ([[Monoisotopic Mass]]).

## Core (L1)

![[skeletal-formula-conventions.svg]]

**Counting hydrogens.** Each carbon gets as many hydrogens as it needs to make 4 bonds: a line end is a CH₃, a two-way corner a CH₂, a three-way corner a CH, a four-way corner a C with no H.[^os112] A double bond counts twice, a triple bond three times: the carboxyl carbon of alanine (one single bond to C, one double bond to O, one single bond to O) has no hydrogen left.

**Heteroatoms are explicit.** O, N, S, P and halogens are written with their hydrogens (`OH`, `NH₂`, `SH`), so an unlabelled corner is always carbon and a bare `O` at a line end is a carbonyl oxygen, not a hydroxyl.[^os112]

**Why zigzag.** Lines are drawn at about 120° to each other, which mimics the tetrahedral (109.5°) or trigonal (120°) bond angles of carbon ([[Molecular Geometry]], [[Orbital Hybridization]]). The drawing is flat: a wedge marks a bond toward the viewer and a dashed wedge a bond away from it, the minimum needed to show 3D arrangement ([[Stereochemistry]]).[^os1]

**Four ways to write ethanol.** Molecular formula C₂H₆O (composition only, shared with dimethyl ether, see [[Isomer]]); condensed formula CH₃CH₂OH; skeletal formula, a two-line zigzag ending in OH; SMILES `CCO`, the same graph as a string.

## Deeper (L2)

**Rings and aromatic rings.** A ring is a closed polygon: a hexagon of plain lines is cyclohexane, C₆H₁₂ (six CH₂). A benzene ring is drawn with three alternating double bonds, one of its resonance forms ([[Resonance (Chemistry)]], [[Aromaticity]]). SMILES writes atoms in order, adjacent atoms bonded (single by default, `=` double, `#` triple), parentheses for branches and a repeated digit to close a ring: alanine is `CC(N)C(=O)O`, cyclohexane `C1CCCCC1`, and aromatic atoms may be lowercase (`c1ccccc1`).[^osm] **Charges.** At pH 7 amino acids are drawn as zwitterions, `NH₃⁺` and `COO⁻`: a charge changes the hydrogen count, so it must be written on the atom ([[Amino Acid]]). In SMILES, charged atoms, explicit hydrogen counts, isotopes and stereo marks go inside brackets, for example `[NH3+]`; only uncharged atoms of the organic subset (B, C, N, O, P, S, halogens) may be written bare, and they receive implicit hydrogens from their normal valences.[^osm]

## Advanced (L3)

**One molecule, many strings.** SMILES writes the graph along a walk that can start at any atom and take branches in any order: `CCO`, `OCC` and `C(O)C` are all ethanol. Databases therefore compute a **canonical** SMILES, a unique string per structure, which turns "is this compound already stored?" into a string comparison; generating such a unique notation was one of the applications announced with SMILES.[^weininger] Canonicalization is a [[Graph]] canonical-labelling problem, harder than it looks for symmetric molecules. Compound records also carry InChI strings alongside SMILES.[^pubchem]

**The string is a spanning tree.** Bonds written by adjacency and branches form a spanning tree of the molecular graph, and each pair of ring digits adds one of the remaining edges (Exercise 4). Similarity and machine-learning methods start from the same graphs ([[Molecular Representation]], [[Molecular Fingerprint]]).

## Mathematical representation

A molecule is a labelled graph $G = (V, E, \ell, b)$: $V$ the heavy (non-hydrogen) atoms, $E$ the bonds between them, $\ell(v)$ the element of atom $v$ and $b(e) \in \{1, 2, 3\}$ the bond order. With $\mathrm{val}(\ell)$ the valence of the element (C 4, N 3, O 2, halogen 1), the implicit hydrogen count of an uncharged atom is

$$h(v) = \mathrm{val}(\ell(v)) - \sum_{e \ni v} b(e).$$

**Rings plus π bonds** (degree of unsaturation). For a connected molecule, the number of rings is the cyclomatic number $r = |E| - |V| + 1$ and the number of π bonds is $\pi = \sum_e (b(e) - 1)$. Summing valences over all atoms counts every bond twice: $4C + 3N + 2O + X + H = 2(|E| + \pi + H)$, where $C, N, O, X, H$ count carbons, nitrogens, oxygens, halogens and hydrogens and $|V| = C + N + O + X$. Eliminating $|E|$:

$$r + \pi = \frac{2C + 2 + N - H - X}{2} \quad \text{(oxygen, of valence 2, cancels).}$$

## Computational representation

A minimal parser for SMILES without brackets or lowercase aromatic letters: it builds the graph, applies the implicit-hydrogen rule and returns the molecular formula in Hill order (C, H, then alphabetical).

```python
import re
from collections import Counter

# Default valences of the SMILES organic subset: the lowest value that fits is used.
VALENCES = {"B": (3,), "C": (4,), "N": (3, 5), "O": (2,), "P": (3, 5), "S": (2, 4, 6),
            "F": (1,), "Cl": (1,), "Br": (1,), "I": (1,)}
TOKEN = re.compile(r"Cl|Br|[BCNOPSFI]|[-=#()]|\d")
BOND = {"-": 1, "=": 2, "#": 3}

def parse_smiles(smiles: str):
    """Organic-subset SMILES without brackets or aromatic letters -> (atoms, bonds)."""
    tokens = TOKEN.findall(smiles)
    assert "".join(tokens) == smiles, f"unsupported characters in {smiles!r}"
    atoms, bonds = [], []                  # atoms: symbols; bonds: (i, j, order)
    branch, prev, order, open_rings = [], None, 1, {}
    for tok in tokens:
        if tok in BOND:
            order = BOND[tok]
        elif tok == "(":
            branch.append(prev)
        elif tok == ")":
            prev = branch.pop()
        elif tok.isdigit():                # ring digit: first use opens, second closes
            if tok in open_rings:
                j, o = open_rings.pop(tok)
                bonds.append((j, prev, max(o, order)))
            else:
                open_rings[tok] = (prev, order)
            order = 1
        else:                              # an atom
            atoms.append(tok)
            if prev is not None:
                bonds.append((prev, len(atoms) - 1, order))
            prev, order = len(atoms) - 1, 1
    return atoms, bonds

def implicit_hydrogens(atoms, bonds) -> list[int]:
    """Hydrogens each atom needs to reach its lowest default valence."""
    used = [0] * len(atoms)
    for i, j, o in bonds:
        used[i] += o
        used[j] += o
    return [next(v for v in VALENCES[a] if v >= u) - u for a, u in zip(atoms, used)]

def molecular_formula(smiles: str) -> str:
    atoms, bonds = parse_smiles(smiles)
    counts = Counter(atoms)
    counts["H"] += sum(implicit_hydrogens(atoms, bonds))
    order = ["C", "H"] + sorted(e for e in counts if e not in ("C", "H"))
    return "".join(e + (str(counts[e]) if counts[e] > 1 else "") for e in order if counts[e])

def rings_plus_pi_bonds(smiles: str) -> int:
    atoms, bonds = parse_smiles(smiles)
    return (len(bonds) - len(atoms) + 1) + sum(o - 1 for _, _, o in bonds)


for name, smi in [("ethanol", "CCO"), ("alanine", "CC(N)C(=O)O"), ("cyclohexane", "C1CCCCC1"),
                  ("paracetamol (Kekule)", "CC(=O)NC1=CC=C(O)C=C1")]:
    print(f"{name:21} {smi:22} {molecular_formula(smi):8} rings+pi = {rings_plus_pi_bonds(smi)}")
atoms, bonds = parse_smiles("CC(N)C(=O)O")
print(list(zip(atoms, implicit_hydrogens(atoms, bonds))))
```

```text
ethanol               CCO                    C2H6O    rings+pi = 0
alanine               CC(N)C(=O)O            C3H7NO2  rings+pi = 1
cyclohexane           C1CCCCC1               C6H12    rings+pi = 1
paracetamol (Kekule)  CC(=O)NC1=CC=C(O)C=C1  C8H9NO2  rings+pi = 5
[('C', 3), ('C', 1), ('N', 2), ('C', 0), ('O', 0), ('O', 1)]
```

The last line is the figure's panel B in numbers: CH₃, CH, NH₂, C with no H, carbonyl O, OH. Real toolkits add bracket atoms, aromaticity and stereo marks to this core; test any string on two of them ([[OpenSMILES Specification]] lists the rules they share).

## Worked example

> [!example] Reading paracetamol
> Paracetamol (acetaminophen) is a benzene ring carrying an OH and, opposite to it, an NH bonded to an acetyl group (structure as in its PubChem record).[^pubchem]
> 1. **Carbons.** The ring has 6 corners; the acetyl group adds a CH₃ line end and a carbonyl carbon: 8 C.
> 2. **Hydrogens on carbon.** Four ring corners have only two ring bonds (one of them double): 1 H each. The two substituted ring carbons and the carbonyl carbon have none. The methyl has 3: 4 + 3 = 7.
> 3. **Heteroatoms with their H.** OH (1 H), NH (1 H), C=O: 9 H in total, 1 N, 2 O. Formula C₈H₉NO₂, as the code prints.
> 4. **Check by unsaturation.** $(2 \cdot 8 + 2 + 1 - 9)/2 = 5$: one ring + three ring C=C + one C=O. The amide and the phenol OH are the [[Functional Group|functional groups]] that decide its polarity and metabolism.

## Common misconceptions

> [!warning] "A line end is a hydrogen"
> A line end is a carbon carrying 3 hydrogens. A terminal `O` without H is a C=O oxygen. And the drawing fixes connectivity only: it covers every rotation about single bonds ([[Conformational Analysis]]) and, without wedges, every stereoisomer.

> [!warning] "In SMILES, as in drawings, only carbons get implicit hydrogens"
> In the SMILES organic subset every bare atom gets implicit hydrogens: `OCC` is HO–CH₂–CH₃ and `CN` is CH₃–NH₂. Only bracket atoms have exactly the hydrogens written.[^osm]

> [!warning] "Two different strings are two different molecules"
> `CCO` and `OCC` are the same graph written from different ends. Compare canonical SMILES, or the graphs, never raw strings.[^weininger]

## Exercises

> [!question] Exercise 1 (L1)
> Describe the skeletal formula of CH₃CH(OH)CH₂CH₃ (butan-2-ol): number of line ends and corners, hydrogens on each carbon, molecular formula.

> [!success]- Solution
> Three lines in a zigzag: line end (CH₃), corner bearing a line to OH (3 bonds to heavy atoms → CH), corner (CH₂), line end (CH₃). Formula C₄H₁₀O: 3 + 1 + 2 + 3 = 9 H on carbon plus the OH hydrogen.

> [!question] Exercise 2 (L1)
> Ibuprofen is C₁₃H₁₈O₂ and contains one benzene ring and one carboxylic acid. Compute rings + π bonds from the formula and account for every unit.

> [!success]- Solution
> $(2 \cdot 13 + 2 - 18)/2 = 5$. The benzene ring gives 1 ring + 3 π bonds, the carboxyl C=O one more π bond: 5. Nothing else is unsaturated, so the rest of the molecule is saturated chains. Check: `molecular_formula("CC(C)CC1=CC=C(C=C1)C(C)C(=O)O")` prints `C13H18O2`, and `rings_plus_pi_bonds` returns 5.

> [!question] Exercise 3 (L2, Python)
> Write SMILES for open-chain glucose (an aldehyde at C1, OH on C2 to C6) and open-chain fructose (a ketone at C2, OH on C1 and C3 to C6), then compute their formulas and rings + π with the code above. What do you conclude?

> [!success]- Solution
> ```python
> print(molecular_formula("OCC(O)C(O)C(O)C(O)C=O"), molecular_formula("OCC(O)C(O)C(O)C(=O)CO"))
> print(rings_plus_pi_bonds("OCC(O)C(O)C(O)C(O)C=O"), rings_plus_pi_bonds("OCC(O)C(O)C(O)C(=O)CO"))
> # C6H12O6 C6H12O6
> # 1 1
> ```
> Same formula, same unsaturation (one C=O each), different graphs: they are constitutional isomers ([[Isomer]], [[Carbohydrate]]). A formula, or a mass, cannot tell them apart.

> [!question] Exercise 4 (L3)
> Prove that the number of ring-closure digit pairs in any valid SMILES of a connected molecule equals its number of rings $|E| - |V| + 1$, whatever the starting atom.

> [!success]- Solution
> Every atom except the first is bonded, at the moment it is written, to exactly one earlier atom (the previous atom or the branch point): these $|V| - 1$ bonds connect all atoms without a cycle, so they form a spanning tree. Every other bond must be written with a ring-closure pair, one pair per bond: $|E| - (|V| - 1)$ pairs. This count depends only on the graph, not on the walk, which is why all SMILES of a molecule have the same number of ring pairs even though the digits sit in different places.

## Mastery checklist

- [ ] 1 Recognized: I can say what corners, line ends, wedges and dashes mean in a skeletal formula.
- [ ] 2 Understood: I can count the hydrogens of every atom of a drawn structure and convert between molecular, condensed, skeletal and SMILES forms.
- [ ] 3 Practiced: I can compute a molecular formula and rings + π bonds by hand and with the parser above.
- [ ] 4 Applied: I read real metabolite and drug structures from PubChem records and checked their formulas from their SMILES.
- [ ] 5 Explained: I can explain why many SMILES exist per molecule, what canonicalization solves and how implicit hydrogens differ between drawings and SMILES.

## References

[^os112]: [[Organic Chemistry (OpenStax)]], ch. 1 "Structure and Bonding", section 1.12 "Drawing Chemical Structures".
[^os1]: [[Organic Chemistry (OpenStax)]], ch. 1 "Structure and Bonding".
[^weininger]: [[Weininger 1988 - SMILES, a Chemical Language and Information System]], *J. Chem. Inf. Comput. Sci.* 28(1):31-36.
[^osm]: [[OpenSMILES Specification]], atoms (organic subset and bracket atoms), bonds, branches and ring closures, aromaticity.
[^pubchem]: [[PubChem]], compound records (structure, molecular formula, SMILES and InChI).
