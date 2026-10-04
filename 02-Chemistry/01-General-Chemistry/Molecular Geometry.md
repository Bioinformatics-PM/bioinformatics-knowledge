---
aliases:
  - VSEPR
  - VSEPR Theory
  - Valence Shell Electron Pair Repulsion
  - Molecular Shape
  - Géométrie moléculaire
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Lewis Structure]]"
  - "[[Covalent Bond]]"
  - "[[Electronegativity]]"
related:
  - "[[Orbital Hybridization]]"
  - "[[Water]]"
  - "[[Chirality]]"
  - "[[Phosphate Ester]]"
  - "[[Hydrogen Bond]]"
  - "[[Protein Structure]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Organic Chemistry (OpenStax)]]"
---

# Molecular Geometry

> [!abstract]
> Electron pairs around an atom push each other as far apart as possible; counting them predicts whether a molecule is linear, flat or tetrahedral, which in turn decides whether it is polar and whether it can be chiral.

## Definition

**Molecular geometry** (molecular structure) is the three-dimensional arrangement of the atoms of a molecule. **Valence shell electron-pair repulsion (VSEPR)** theory predicts it from the [[Lewis Structure]]: the electron groups around a central atom (bonded atoms and lone pairs, a double or triple bond counting as one group) adopt the arrangement that keeps them farthest apart. The arrangement of all groups is the **electron-pair geometry**; the shape named from the atoms alone is the **molecular structure**.[^c2e76][^5111]

## Why it matters

- **Shape decides polarity.** Whether bond dipoles cancel depends on geometry: bent water is polar, linear CO₂ is not ([[Electronegativity]], [[Water]]).
- **Tetrahedral carbon makes chirality.** A carbon with four different substituents has two mirror-image arrangements that cannot be superimposed; proteins are built from one of the two forms of each amino acid, and enzymes tell them apart ([[Chirality]]).[^mcmurry]
- **Geometry is a structure check.** Ideal angles (109.5°, 120°, 180°) are what bond angles computed from PDB coordinates are compared with ([[Orbital Hybridization]] computes them from coordinates; [[Protein Structure]]).

## Core (L1)

**Groups and shapes.** With 2 to 6 electron groups around a central atom, the groups point to the corners of these figures:[^c2e76]

| Electron groups | Electron-pair geometry | Ideal angle | Example |
|---|---|---|---|
| 2 | linear | 180° | CO₂, HCN |
| 3 | trigonal planar | 120° | H₂C=O, the C of C=O |
| 4 | tetrahedral | 109.5° | CH₄, NH₄⁺, PO₄³⁻ |
| 5 | trigonal bipyramidal | 90° and 120° | PCl₅ |
| 6 | octahedral | 90° | SF₆ |

**Lone pairs.** A lone pair is an electron group but not an atom, so it changes the name of the shape: 4 groups with 1 lone pair (NH₃) give a **trigonal pyramid**; with 2 lone pairs (H₂O) a **bent** molecule. Lone pairs repel more than bonding pairs (lone pair–lone pair > lone pair–bonding pair > bonding pair–bonding pair), so they squeeze the bond angles below the ideal value:[^c2e76] 109.5° in CH₄, 107.3° in NH₃, 104.5° in H₂O.[^c2e82]

![[vsepr-water-ammonia-methane-phosphate.svg]]

**Procedure.** Draw the Lewis structure; count the groups on the central atom; read the electron-pair geometry; place the atoms and name the shape.[^c2e76][^5111]

**Bio: three shapes everywhere.**

- **Tetrahedral carbon.** Every sp3 carbon of a biomolecule, including the Cα of amino acids, points its four bonds to the corners of a tetrahedron; with four different groups it is a stereocenter ([[Chirality]]).[^mcmurry]
- **Tetrahedral phosphate.** P in phosphate and in each phosphodiester of DNA and RNA has four electron groups and no lone pair: tetrahedral, whichever resonance structure is drawn ([[Phosphate Ester]]).
- **Bent water.** Two bonds and two lone pairs on O: the bend gives water its dipole and lets each molecule donate two and accept two hydrogen bonds ([[Water]], [[Hydrogen Bond]]).

## Deeper (L2)

**Molecules with several centers.** VSEPR is applied atom by atom: in glycine, H₂N–CH₂–COOH, the N is trigonal pyramidal, the CH₂ carbon tetrahedral and the carboxyl carbon trigonal planar.[^c2e76] The shape of a large molecule is then fixed by rotations around single bonds ([[Conformational Analysis]]).

**Why 109.5°.** Put four groups on alternate corners of a cube, along $(1,1,1)$, $(1,-1,-1)$, $(-1,1,-1)$, $(-1,-1,1)$. Any two have a dot product of $-1$ and lengths $\sqrt{3}$, so $\cos\theta = -1/3$, $\theta = 109.47°$. [[Orbital Hybridization]] reaches the same angle from orthogonal sp3 orbitals ($\cos\theta = -1/n$ with $n = 3$): two models, one geometry.

**Limits.** VSEPR predicts the ideal arrangement and the direction of deviations (lone pairs close angles), not their size: the 107.3° and 104.5° are measured values.[^c2e82] It says nothing about why electron pairs form bonds; that is the job of [[Orbital Hybridization]] and [[Molecular Orbital Theory]].

## Mathematical representation

- Steric number $s = a + \ell$, with $a$ the number of bonded atoms and $\ell$ the number of lone pairs on the central atom.
- VSEPR places $s$ unit vectors $\mathbf{d}_1, \dots, \mathbf{d}_s$ on a sphere so that the smallest angle between them is as large as possible: $s = 2$ antipodal ($180°$), $s = 3$ an equilateral triangle in a plane ($120°$), $s = 4$ a regular tetrahedron ($\cos\theta = -1/3$), $s = 6$ an octahedron ($90°$).
- With identical outer atoms and equal bond dipoles $\mu_b$, the molecular dipole is $\mu_b \left|\sum_{k=1}^{a} \mathbf{d}_k\right|$: zero when $\ell = 0$ (the vectors of a regular figure sum to zero), non-zero for the bent and pyramidal shapes.

## Computational representation

```python
import math
from itertools import combinations

S3 = math.sqrt(3) / 2
DIRECTIONS = {                                              # ideal directions of 2, 3, 4 groups
    2: [(0, 0, 1), (0, 0, -1)],                               # linear
    3: [(1, 0, 0), (-0.5, S3, 0), (-0.5, -S3, 0)],             # trigonal planar
    4: [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)],     # tetrahedral (cube corners)
}
ELECTRON_GEOMETRY = {2: "linear", 3: "trigonal planar", 4: "tetrahedral"}
SHAPE = {(2, 0): "linear", (3, 0): "trigonal planar", (2, 1): "bent",
         (4, 0): "tetrahedral", (3, 1): "trigonal pyramidal", (2, 2): "bent"}

def angle(u, v) -> float:
    dot = sum(a * b for a, b in zip(u, v))
    return math.degrees(math.acos(dot / (math.hypot(*u) * math.hypot(*v))))

def vsepr(bonded_atoms: int, lone_pairs: int) -> dict:
    """Electron-pair geometry, shape, ideal angle, and whether equal bond dipoles cancel."""
    groups = bonded_atoms + lone_pairs                      # steric number
    dirs = DIRECTIONS[groups]
    bonds = [tuple(c / math.hypot(*d) for c in d) for d in dirs[:bonded_atoms]]
    resultant = math.hypot(*(sum(c) for c in zip(*bonds)))
    return {"groups": groups, "electron geometry": ELECTRON_GEOMETRY[groups],
            "shape": SHAPE[(bonded_atoms, lone_pairs)], "ideal angle": round(angle(dirs[0], dirs[1]), 2),
            "equal dipoles cancel": resultant < 1e-9}

SPECIES = {"CO2": (2, 0), "H2C=O": (3, 0), "CH4": (4, 0), "NH4+": (4, 0), "PO4(3-)": (4, 0),
           "NH3": (3, 1), "H2O": (2, 2)}
for name, (b, lp) in SPECIES.items():
    r = vsepr(b, lp)
    print(f"{name:8} {r['groups']} groups  {r['electron geometry']:16} {r['shape']:19} "
          f"ideal {r['ideal angle']:6}  cancel: {r['equal dipoles cancel']}")
print(sorted({round(angle(u, v), 2) for u, v in combinations(DIRECTIONS[4], 2)}))
```

```text
CO2      2 groups  linear           linear              ideal  180.0  cancel: True
H2C=O    3 groups  trigonal planar  trigonal planar     ideal  120.0  cancel: True
CH4      4 groups  tetrahedral      tetrahedral         ideal 109.47  cancel: True
NH4+     4 groups  tetrahedral      tetrahedral         ideal 109.47  cancel: True
PO4(3-)  4 groups  tetrahedral      tetrahedral         ideal 109.47  cancel: True
NH3      4 groups  tetrahedral      trigonal pyramidal  ideal 109.47  cancel: False
H2O      4 groups  tetrahedral      bent                ideal 109.47  cancel: False
[109.47]
```

All six pairs of tetrahedral directions make the same 109.47° angle. The `cancel` column assumes identical outer atoms; H₂C=O shows what happens when that assumption is false (Exercise 3).

## Worked example

> [!example] The phosphorus of a DNA phosphodiester
> 1. **Lewis structure.** P bonded to two bridging O (to C3' and C5' of the sugars) and two non-bridging O, one drawn as P=O, the other carrying −1 ([[Lewis Structure]]).
> 2. **Groups on P.** Four bonded atoms, no lone pair; the P=O counts as one group: steric number 4.
> 3. **Shape.** Tetrahedral, ideal O–P–O angle 109.5°. Moving the P=O to the other non-bridging oxygen (the other resonance structure) changes nothing: the geometry does not depend on which drawing is chosen.
> 4. **Size.** For an assumed P–O distance $d = 1.5$ Å, two oxygens at tetrahedral corners are $d\sqrt{8/3} = 2.45$ Å apart ($\sqrt{2 - 2\cos 109.47°} = \sqrt{8/3}$).

## Common misconceptions

> [!warning] "The shape is the electron-pair geometry"
> NH₃ has a tetrahedral electron-pair geometry but a trigonal pyramidal shape: the shape names only the positions of atoms.[^c2e76]

> [!warning] "A double bond counts as two groups"
> A multiple bond occupies one region between two atoms and counts once: H₂C=O has three groups on C, trigonal planar.[^c2e76]

## Exercises

> [!question] Exercise 1 (L1)
> Predict the electron-pair geometry and the shape of H₂S, HCN, NH₄⁺ and SO₄²⁻ (S central, no lone pair).

> [!success]- Solution
> H₂S: S has 2 bonds and 2 lone pairs (like O), tetrahedral pairs, bent shape. HCN: 2 groups on C, linear. NH₄⁺: 4 bonds, tetrahedral. SO₄²⁻: 4 groups, no lone pair, tetrahedral, like phosphate.

> [!question] Exercise 2 (L1)
> Rank the H–X–H angles of CH₄, NH₃ and H₂O and explain the order.

> [!success]- Solution
> CH₄ (109.5°) > NH₃ (107.3°) > H₂O (104.5°). All three have 4 electron groups, but each lone pair repels more strongly than a bond and pushes the bonds together; water has two.[^c2e82]

> [!question] Exercise 3 (L2, Python)
> `vsepr(3, 0)` says equal dipoles cancel for H₂C=O, yet formaldehyde is polar. Weight each bond direction by $\chi_{\text{outer}} - \chi_{\text{C}}$ (H 2.1, C 2.5, O 3.5) and recompute the resultant.

> [!success]- Solution
> ```python
> EN = {"H": 2.1, "C": 2.5, "O": 3.5}
> outer = ["O", "H", "H"]                     # along DIRECTIONS[3], C at the origin
> vec = [sum((EN[x] - EN["C"]) * d[i] for x, d in zip(outer, DIRECTIONS[3])) for i in range(3)]
> print([round(c, 2) for c in vec], round(math.hypot(*vec), 2))
> ```
> Output: `[1.4, 0.0, 0.0] 1.4`. The C=O dipole points toward O and the two C–H dipoles point toward C, so they add along the C=O axis instead of cancelling. Symmetry of the shape guarantees cancellation only when the outer atoms are identical.

> [!question] Exercise 4 (L2)
> Why can the Cα of alanine (bonded to H, CH₃, NH₂ and COOH) be chiral, while the carboxyl carbon of the same molecule cannot?

> [!success]- Solution
> Cα is tetrahedral with four different groups: its mirror image cannot be superimposed on it, so it is a stereocenter.[^mcmurry] The carboxyl carbon is trigonal planar with three groups; a planar arrangement is its own mirror image after a rotation, so it cannot be a stereocenter ([[Chirality]]).

## Mastery checklist

- [ ] 1 Recognized: I can name linear, trigonal planar, tetrahedral, trigonal pyramidal and bent shapes with their ideal angles.
- [ ] 2 Understood: I can explain the difference between electron-pair geometry and molecular shape, and why lone pairs close bond angles.
- [ ] 3 Practiced: I can predict the shape at each atom of an amino acid or a nucleotide and derive 109.47° from vectors.
- [ ] 4 Applied: I measured bond angles at a Cα, a phosphate and a water oxygen in a real structure file and compared them with VSEPR.
- [ ] 5 Explained: I can explain how geometry links to polarity and chirality, and what VSEPR cannot predict.

## References

[^c2e76]: [[Chemistry 2e (OpenStax)]], ch. 7 "Chemical Bonding and Molecular Geometry", §7.6 "Molecular Structure and Polarity" (VSEPR, electron-pair geometry and molecular structure, lone-pair repulsion order, multicenter molecules).
[^c2e82]: [[Chemistry 2e (OpenStax)]], ch. 8, §8.2 "Hybrid Atomic Orbitals" (observed angles of NH₃, 107.3°, and H₂O, 104.5°).
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], Unit II "Chemical Bonding & Structure", Lecture 12 "The Shapes of Molecules: VSEPR Theory".
[^mcmurry]: [[Organic Chemistry (OpenStax)]], ch. 5 "Stereochemistry at Tetrahedral Centers" (stereocenters, enantiomers, chirality in nature) and ch. 26 "Biomolecules: Amino Acids, Peptides, and Proteins" (configuration of the amino acids of proteins).
