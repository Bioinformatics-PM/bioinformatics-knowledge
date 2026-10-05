---
aliases:
  - Pauling Electronegativity
  - Bond Polarity
  - Partial Charge
  - Électronégativité
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Atom]]"
  - "[[Electron Configuration]]"
  - "[[Periodic Table]]"
related:
  - "[[Chemical Bond]]"
  - "[[Covalent Bond]]"
  - "[[Ionic Bond]]"
  - "[[Molecular Geometry]]"
  - "[[Hydrogen Bond]]"
  - "[[Water]]"
  - "[[Drug Discovery]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability]]"
---

# Electronegativity

> [!abstract]
> Electronegativity measures how hard an atom pulls on the electrons it shares; comparing two atoms tells which end of a bond is slightly negative, and adding the bonds up tells whether a whole molecule is polar.

## Definition

**Electronegativity** ($\chi$) is the tendency of an atom to attract the electrons of a bond toward itself. Linus Pauling built the first scale by comparing bond energies; on it fluorine, the most electronegative element, has 4.0. Electronegativity increases from left to right across a period and decreases down a group.[^c2e72] When two bonded atoms differ in $\chi$, the shared electrons spend more time near the more electronegative one, which carries a **partial negative charge** $\delta-$, its partner $\delta+$: the bond is **polar**.[^c2e72][^5111]

## Why it matters

- **Hydrogen-bond donors.** A hydrogen bonded to N or O carries a large $\delta+$ and can be shared with another electronegative atom: these N–H and O–H groups are the hydrogen-bond donors that hold helices, sheets and base pairs together ([[Hydrogen Bond]]).[^alberts]
- **Polar against nonpolar surfaces.** C–H bonds are nearly nonpolar, so hydrocarbon side chains and lipid tails interact poorly with water, the starting point of the [[Hydrophobic Effect]] and of "like dissolves like" ([[Water]], [[Aqueous Solution]]).
- **Descriptors of drug-likeness.** Lipinski's rule of 5 counts hydrogen-bond donors and acceptors, two electronegativity-based descriptors that a program computes from a structure ([[Drug Discovery]]).[^lipinski]

## Core (L1)

**The scale for the elements of life** (Pauling values as tabulated in Chemistry 2e):[^c2e72]

| Element | H | C | N | O | P | S | F | Na | K | Cl |
|---|---|---|---|---|---|---|---|---|---|---|
| $\chi$ | 2.1 | 2.5 | 3.0 | 3.5 | 2.1 | 2.5 | 4.0 | 0.9 | 0.8 | 3.0 |

The trend follows the [[Periodic Table]]: across period 2, C < N < O < F as the nuclear charge grows; down group 16, O > S. Metals (Na, K) hold their electrons loosely, nonmetals (N, O, Cl) attract them strongly.[^c2e72]

**Bond polarity.** The difference $\Delta\chi$ sets how unequal the sharing is: equal for C–C, slight for C–H (0.4), strong for O–H (1.4), and so large for Na–Cl (2.1) that the electron is transferred ([[Chemical Bond]] places the bonds of biology on this continuum).[^c2e72] A polar bond is written H$^{\delta+}$–O$^{\delta-}$, or drawn with an arrow pointing to the negative end.

**Molecular polarity.** Each polar bond has a **bond dipole**; the molecule's dipole is their **vector sum**, so it depends on the shape ([[Molecular Geometry]]). The two C=O dipoles of linear CO₂ point in opposite directions and cancel: a nonpolar molecule made of polar bonds. In bent H₂O the two O–H dipoles add up: water is polar, with O negative and the H atoms positive.[^c2e76]

**Bio: donors and acceptors.** Hydrogen bonds form between an H attached to O or N and another electronegative atom carrying a lone pair.[^alberts] In biomolecules:[^berg]

| Group | Where | Role |
|---|---|---|
| backbone N–H | every residue except proline | donor |
| C=O | backbone, Asn, Gln, Asp, Glu, bases | acceptor (O) |
| O–H | Ser, Thr, Tyr side chains; sugars; the 2'-OH of RNA | donor and acceptor |
| N–H and –NH₂ | Asn, Gln, Lys, Arg, His, Trp; ring N–H and amino groups of the bases | donor |

## Deeper (L2)

**Dipole moment.** Two charges $+Q$ and $-Q$ a distance $r$ apart have a dipole moment $\mu = Qr$, a vector; a molecule is polar when the vector sum of its bond dipoles is non-zero.[^c2e76] For a bent molecule AX₂ with two equal bond dipoles $\mu_b$ at angle $\theta$, the components perpendicular to the bisector cancel and the parallel ones add:

$$|\boldsymbol{\mu}| = 2\,\mu_b \cos(\theta/2).$$

At 180° (CO₂) this is 0; at water's 104.5°[^c2e82] it is $1.22\,\mu_b$. Symmetric shapes with identical outer atoms (linear AX₂, trigonal planar AX₃, tetrahedral AX₄) are always nonpolar; replacing one outer atom (CH₃Cl instead of CH₄) or adding lone pairs (NH₃, H₂O) breaks the cancellation.[^c2e76]

**Partial charges are not formal charges.** $\delta+$ and $\delta-$ describe how shared electrons are actually distributed; the formal charge of a [[Lewis Structure]] is a bookkeeping count that splits every bond equally. In NH₄⁺ the formal charge +1 sits on N, yet N is more electronegative than H, so the positive charge is carried mostly by the hydrogens.

## Advanced (L3)

**Counting donors and acceptors.** Lipinski's rule of 5 flags poor absorption or permeation when a compound has more than 5 hydrogen-bond donors (counted as the sum of OH and NH groups), more than 10 acceptors (the sum of N and O atoms), a molecular weight above 500 or a calculated log P above 5.[^lipinski] The acceptor count needs only the [[Molecule|molecular formula]]; the donor count needs the connectivity, because only H bonded to N or O counts (Exercise 3). Counting every N and O as an acceptor is a deliberate simplification of the electronegativity picture, and the rule itself is a heuristic with known exceptions.[^lipinski]

## Mathematical representation

- $\chi_A$: electronegativity of atom $A$ (dimensionless). For a bond A–B, $\Delta\chi = |\chi_A - \chi_B|$; the atom with the larger $\chi$ carries $\delta-$.
- Charges $q_i$ at positions $\mathbf{r}_i$: $\boldsymbol{\mu} = \sum_i q_i \mathbf{r}_i$. For a neutral molecule ($\sum_i q_i = 0$), shifting the origin by $\mathbf{a}$ gives $\sum_i q_i (\mathbf{r}_i - \mathbf{a}) = \boldsymbol{\mu} - \mathbf{a}\sum_i q_i = \boldsymbol{\mu}$: the dipole does not depend on the origin.
- With bond dipoles $\mu_b$ along unit vectors $\mathbf{u}_b$, $\boldsymbol{\mu} \approx \sum_b \mu_b \mathbf{u}_b$, which gives $2\mu_b\cos(\theta/2)$ for AX₂ (Deeper).

## Computational representation

A molecule is a list of bonds between numbered atoms; electronegativities are a lookup table:

```python
import re

# Pauling electronegativities as tabulated in Chemistry 2e (one decimal)
EN = {"H": 2.1, "C": 2.5, "N": 3.0, "O": 3.5, "P": 2.1, "S": 2.5}

def element(label: str) -> str:
    return label.rstrip("0123456789")

def ends(bond: str) -> list[str]:
    return re.split(r"[-=#]", bond)          # 'C2=O1' -> ['C2', 'O1']

def polarity(bond: str) -> tuple[float, str]:
    """Delta chi of a bond and the atom that carries delta-minus ('-' if nonpolar)."""
    a, b = ends(bond)
    d = EN[element(b)] - EN[element(a)]
    return round(abs(d), 1), (b if d > 0 else a if d < 0 else "-")

def donors_acceptors(bonds: list[str]) -> tuple[int, int]:
    """Donors: H bonded to N or O. Acceptors: N and O atoms (Lipinski's counting)."""
    donors = sum(sorted(map(element, ends(b))) in (["H", "N"], ["H", "O"]) for b in bonds)
    atoms = {x for b in bonds for x in ends(b)}
    return donors, sum(element(x) in ("N", "O") for x in atoms)

MOLECULES = {   # two C2H6O isomers and glycine, H2N-CH2-COOH
    "ethanol": ["C1-H1", "C1-H2", "C1-H3", "C1-C2", "C2-H4", "C2-H5", "C2-O1", "O1-H6"],
    "dimethyl ether": ["C1-H1", "C1-H2", "C1-H3", "C1-O1", "C2-O1", "C2-H4", "C2-H5", "C2-H6"],
    "glycine": ["N1-H1", "N1-H2", "C1-N1", "C1-H3", "C1-H4", "C1-C2", "C2=O1", "C2-O2", "O2-H5"],
}
for name, bonds in MOLECULES.items():
    polar = sorted({(polarity(b)[0], re.sub(r"\d", "", b)) for b in bonds if polarity(b)[0] >= 0.5},
                   reverse=True)
    print(f"{name:15} donors, acceptors = {donors_acceptors(bonds)}  {polar}")
```

```text
ethanol         donors, acceptors = (1, 1)  [(1.4, 'O-H'), (1.0, 'C-O')]
dimethyl ether  donors, acceptors = (0, 1)  [(1.0, 'C-O')]
glycine         donors, acceptors = (3, 3)  [(1.4, 'O-H'), (1.0, 'C=O'), (1.0, 'C-O'), (0.9, 'N-H'), (0.5, 'C-N')]
```

Ethanol and dimethyl ether share the formula C₂H₆O, yet only ethanol has a donor. Bonds below 0.5 (C–H) are left out of the polar list; that cut-off is a display choice, not a law.

## Worked example

> [!example] Water against carbon dioxide
> 1. **Bonds.** O–H: $\Delta\chi = 3.5 - 2.1 = 1.4$, O is $\delta-$. C=O: $\Delta\chi = 3.5 - 2.5 = 1.0$, O is $\delta-$. Both molecules have polar bonds.
> 2. **Shapes.** CO₂ is linear (180°); H₂O is bent (104.5°) because of its two lone pairs ([[Molecular Geometry]]).[^c2e82]
> 3. **Vector sum.** CO₂: $2\mu_b\cos 90° = 0$, nonpolar. H₂O: $2\mu_b\cos 52.25° = 1.22\,\mu_b$, polar, pointing along the bisector with O at the negative end: each water molecule can both accept and donate hydrogen bonds ([[Water]]).

## Common misconceptions

> [!warning] "A molecule with polar bonds is a polar molecule"
> CO₂ has two polar C=O bonds and no dipole, because they cancel by symmetry. Polarity of the molecule needs both polar bonds and an asymmetric shape.[^c2e76]

> [!warning] "Electronegativity is the same as electron affinity"
> Electron affinity is a measured energy for an isolated gas-phase atom gaining an electron. Electronegativity describes an atom inside a bond: a dimensionless, calculated scale.[^c2e72]

## Exercises

> [!question] Exercise 1 (L1)
> In the peptide unit –C(=O)–N(H)–, which atom is the hydrogen-bond donor and which the acceptor?

> [!success]- Solution
> The H on N (N–H, $\Delta\chi = 0.9$) is the donor; the O of C=O, $\delta-$ with lone pairs, is the acceptor. Pairing the N–H of one residue with the C=O of another is how backbone hydrogen bonds form ([[Hydrogen Bond]]).

> [!question] Exercise 2 (L2)
> CCl₄, CHCl₃ and CH₂Cl₂ are all tetrahedral around carbon. Which are polar?

> [!success]- Solution
> CCl₄: four identical C–Cl dipoles at tetrahedral angles cancel, nonpolar. CHCl₃ and CH₂Cl₂: C–H ($\Delta\chi = 0.4$, C negative) and C–Cl ($0.5$, Cl negative) dipoles differ, so the sum no longer vanishes: both are polar. Same shape, different polarity.

> [!question] Exercise 3 (L3, Python)
> Encode β-glucopyranose (ring C1–C5 and O5; OH on C1, C2, C3, C4 and C6) as a bond list, check that it has the formula C₆H₁₂O₆, and count donors and acceptors. Which count could you get from the formula alone? Does glucose break Lipinski's donor or acceptor limits?

> [!success]- Solution
> ```python
> glucose = ["C1-O5", "C1-C2", "C2-C3", "C3-C4", "C4-C5", "C5-O5", "C5-C6",
>            "C1-O1", "O1-H1", "C2-O2", "O2-H2", "C3-O3", "O3-H3", "C4-O4", "O4-H4", "C6-O6", "O6-H6",
>            "C1-H7", "C2-H8", "C3-H9", "C4-H10", "C5-H11", "C6-H12", "C6-H13"]
> atoms = {x for b in glucose for x in ends(b)}
> print(sorted({element(x): sum(element(y) == element(x) for y in atoms) for x in atoms}.items()))
> print(donors_acceptors(glucose))
> ```
> Output: `[('C', 6), ('H', 12), ('O', 6)]` then `(5, 6)`. Acceptors (6 O) follow from the formula; donors (5 O–H) need the structure, since the ring oxygen O5 carries no H. With 5 donors and 6 acceptors glucose stays within both limits; only "more than 5" donors would flag it.[^lipinski]

## Mastery checklist

- [ ] 1 Recognized: I can define electronegativity and give the order F > O > N > C ≈ S > H.
- [ ] 2 Understood: I can predict the δ+ and δ− ends of a bond and explain why CO₂ is nonpolar and water polar.
- [ ] 3 Practiced: I can compute bond polarities and donor and acceptor counts in Python, and sum bond dipoles for AX₂ shapes.
- [ ] 4 Applied: I identified the donors and acceptors of a real residue or nucleotide in a structure and checked them against its hydrogen bonds.
- [ ] 5 Explained: I can explain the difference between partial and formal charges and the limits of donor/acceptor counting rules.

## References

[^c2e72]: [[Chemistry 2e (OpenStax)]], ch. 7 "Chemical Bonding and Molecular Geometry", §7.2 "Covalent Bonding" (electronegativity, Pauling scale and values, periodic trends, bond polarity, electronegativity versus electron affinity).
[^c2e76]: [[Chemistry 2e (OpenStax)]], ch. 7, §7.6 "Molecular Structure and Polarity" (bond dipoles, dipole moment $\mu = Qr$, polar and nonpolar molecules).
[^c2e82]: [[Chemistry 2e (OpenStax)]], ch. 8, §8.2 "Hybrid Atomic Orbitals" (H–O–H angle of water, 104.5°).
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], Unit II "Chemical Bonding & Structure", Lecture 9 "Periodic Table; Ionic and Covalent Bonds".
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of cell chemistry: hydrogen bonds between an H attached to O or N and another electronegative atom.
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of amino acid side chains, the polypeptide backbone (proline lacks the backbone N–H) and nucleic acid bases.
[^lipinski]: [[Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability]], *Advanced Drug Delivery Reviews* 23:3-25 (the rule of 5 and how donors and acceptors are counted).
