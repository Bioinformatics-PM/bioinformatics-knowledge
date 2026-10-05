---
aliases:
  - Covalent Bonding
  - Bond Order
  - Single Bond
  - Double Bond
  - Triple Bond
  - Liaison covalente
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Electron Configuration]]"
  - "[[Electronegativity]]"
  - "[[Chemical Bond]]"
related:
  - "[[Ionic Bond]]"
  - "[[Molecule]]"
  - "[[Lewis Structure]]"
  - "[[Orbital Hybridization]]"
  - "[[Resonance (Chemistry)]]"
  - "[[Peptide Bond]]"
  - "[[Phosphate Ester]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[PubChem]]"
---

# Covalent Bond

> [!abstract]
> A covalent bond is a pair of electrons shared by two atoms; sharing two or three pairs makes double and triple bonds, each shorter and stronger than the last, and these bonds are the permanent skeleton of every biomolecule.

## Definition

A **covalent bond** is a chemical bond in which two atoms share a pair of electrons; it typically forms between nonmetal atoms. When the two atoms have the same [[Electronegativity]] the sharing is equal (**nonpolar covalent**); otherwise the shared pair is pulled toward the more electronegative atom (**polar covalent**).[^c2e72][^5111] Two atoms can share one, two or three pairs: a **single**, **double** or **triple bond**, of **bond order** 1, 2 or 3.[^c2e73]

## Why it matters

- **Molecules are graphs.** Atoms joined by covalent bonds define a molecule's connectivity; the SMILES and InChI strings stored with each compound in [[PubChem]] are text encodings of that graph ([[Molecule]], [[Skeletal Formula]]).[^pubchem]
- **Biopolymers are covalent chains.** Residues are joined by [[Peptide Bond|peptide bonds]] and nucleotides by phosphodiester bonds ([[Phosphate Ester]]); disulfide bonds between two cysteines are covalent cross-links within or between protein chains.[^berg]
- **Bond order sets geometry and flexibility.** Double bonds are shorter and do not rotate, which fixes the planar peptide unit and the flat bases ([[Orbital Hybridization]]); bond lengths are also what a program compares with coordinates to check a structure (Computational representation).

## Core (L1)

**Sharing a pair.** In H₂ each atom contributes one electron, and the shared pair is counted by both atoms; the energy minimum of that arrangement is the bond ([[Chemical Bond]]).[^c2e72] Each shared pair also counts toward the octet of both partners, which is why C makes four bonds, N three, O two and H one ([[Electron Configuration]]).

**Single, double, triple.** Ethane (H₃C–CH₃), ethene (H₂C=CH₂) and ethyne (HC≡CH) share one, two and three pairs between their carbons; O=C=O, H–C≡N and N≡N are other multiple bonds.[^c2e73] The more pairs shared between the same two atoms, the shorter and stronger the bond:[^c2e75]

| Bond | Average length (Å) | Average bond energy (kJ/mol) |
|---|---:|---:|
| C–C | 1.54 | 345 |
| C=C | 1.34 | 611 |
| C≡C | 1.20 | 837 |
| C–O | 1.43 | 350 |
| C=O | 1.23 | 741 |

**Polar and nonpolar.** C–C and C–H bonds are (nearly) nonpolar; C–O, C=O, N–H and O–H are polar covalent. The degree of polarity is read from $\Delta\chi$ ([[Electronegativity]]); the borderline with ionic bonds is in [[Chemical Bond]].

**Bio: the bonds that define a sequence.** Hydrolysis of a peptide or phosphodiester bond cuts the chain; heating, salt or detergents do not. That is why a protein or DNA sequence survives denaturation while its 3D structure, held by non-covalent interactions, does not ([[Chemical Bond#Deeper (L2)]]).[^berg]

## Deeper (L2)

**σ and π.** A double bond is one σ bond plus one π bond; a triple bond is one σ and two π bonds ([[Orbital Hybridization]]).[^c2e83] The table gives a rough price for each: the π part of C=C is $611 - 345 = 266$ kJ/mol, less than the σ bond, and the second π of C≡C adds $837 - 611 = 226$. A double bond is therefore weaker than two single bonds, which is why turning C=C into two C–C, as in polymerization, releases energy (Exercise 3).

**Estimating reaction enthalpies.** Breaking bonds costs energy and forming them releases it, so with average bond energies $D$ (gas phase):[^c2e75]

$$\Delta H \approx \sum_{\text{broken}} D \;-\; \sum_{\text{formed}} D.$$

Because the values are averages over many molecules, the estimate is only good to a few tens of kJ/mol; when two estimates differ by less than that, the method cannot decide ([[Enthalpy]], worked example).

**Bond orders between 1 and 2.** Some measured bonds are intermediate in length between single and double: the C–N of the peptide bond, the two C–O of a carboxylate. No single drawing with integer bond orders describes them; [[Resonance (Chemistry)]] does.[^berg]

## Mathematical representation

- Bond order $b \in \{1, 2, 3\}$: number of shared pairs; $2b$ shared electrons.
- Bond-energy estimate: $\Delta H \approx \sum_{i \in \text{broken}} D_i - \sum_{j \in \text{formed}} D_j$, with $D$ the average bond energy (kJ/mol). Bonds present on both sides cancel and can be left out.
- Bond perception: atoms $i, j$ at distance $d_{ij}$ are assigned the tabulated bond $k$ with length $L_k$ that minimizes $|d_{ij} - L_k|$, provided $|d_{ij} - L_k| \le \tau$ (tolerance $\tau$); otherwise no bond.

## Computational representation

```python
import math

# Chemistry 2e, average bond lengths (Å) and bond energies (kJ/mol)
BONDS = {"C-C": (1.54, 345), "C=C": (1.34, 611), "C#C": (1.20, 837),
         "C-O": (1.43, 350), "C=O": (1.23, 741)}

def assign_bond(el1: str, el2: str, distance: float, tol: float = 0.06) -> str | None:
    """Tabulated bond between el1 and el2 whose length is within tol Å of the distance."""
    pair = sorted((el1, el2))
    hits = [(abs(length - distance), b) for b, (length, _) in BONDS.items()
            if sorted((b[0], b[2])) == pair and abs(length - distance) <= tol]
    return min(hits)[1] if hits else None

def delta_h(broken: list[str], formed: list[str]) -> int:
    """Bond-energy estimate of a reaction enthalpy: energy in (broken) minus energy out (formed)."""
    return sum(BONDS[b][1] for b in broken) - sum(BONDS[b][1] for b in formed)

print("pi part of C=C:", BONDS["C=C"][1] - BONDS["C-C"][1], "  second pi of C#C:", BONDS["C#C"][1] - BONDS["C=C"][1])

atoms = {"C1": (0.0, 0.0, 0.0), "C2": (1.52, 0.0, 0.0),   # toy fragment C-C(=O)-O, invented coordinates (Å)
         "O1": (2.14, 1.06, 0.0), "O2": (2.24, -1.23, 0.0)}
names = list(atoms)
for i, a in enumerate(names):
    for b in names[i + 1:]:
        d = math.dist(atoms[a], atoms[b])
        print(f"{a}-{b} {d:.2f} Å -> {assign_bond(a[0], b[0], d)}")

print("ethene -> polyethylene, per monomer:", delta_h(["C=C"], ["C-C", "C-C"]), "kJ/mol")
print("aldehyde + alcohol -> hemiacetal:  ", delta_h(["C=O"], ["C-O", "C-O"]), "kJ/mol")
```

```text
pi part of C=C: 266   second pi of C#C: 226
C1-C2 1.52 Å -> C-C
C1-O1 2.39 Å -> None
C1-O2 2.56 Å -> None
C2-O1 1.23 Å -> C=O
C2-O2 1.43 Å -> C-O
O1-O2 2.29 Å -> None
ethene -> polyethylene, per monomer: -79 kJ/mol
aldehyde + alcohol -> hemiacetal:   41 kJ/mol
```

Distance-based perception needs lengths for every element pair (C–N, C–S, P–O...) and a choice of tolerance; it is a sanity check, not a substitute for the bonds recorded with a compound.

## Worked example

> [!example] Can bond energies tell whether a sugar closes into a ring?
> An aldehyde R–CH=O reacts with an alcohol R'–OH to give a **hemiacetal** R–CH(OH)–OR'; a sugar such as glucose does this within one molecule, its own OH attacking its own C=O to close a ring.[^mcmurry]
> 1. **Bonds broken**: the C=O (741) and the alcohol's O–H.
> 2. **Bonds formed**: a C–O from the former carbonyl O (350), a new C–OR' (350) and a new O–H on the former carbonyl O.
> 3. **Cancel** the O–H broken against the O–H formed: $\Delta H \approx 741 - 2 \times 350 = +41$ kJ/mol.
> 4. **Verdict.** +41 kJ/mol is within the error of average bond energies, and the estimate ignores the solvent and entropy. Which form dominates must come from measured free energies ([[Gibbs Free Energy]]), not from bond counting.

## Common misconceptions

> [!warning] "A double bond is twice as strong as a single bond"
> C=C (611 kJ/mol) is weaker than two C–C (690 kJ/mol): the π bond is weaker than the σ bond.[^c2e75]

> [!warning] "Covalent means equal sharing"
> Only bonds between atoms of equal electronegativity share equally. C–O, N–H and O–H are covalent and polar; their partial charges drive hydrogen bonding ([[Electronegativity]]).[^c2e72]

## Exercises

> [!question] Exercise 1 (L1)
> How many electrons are shared in N≡N, O=O and H–H? Without the table, rank C–O and C=O by length and by bond energy.

> [!success]- Solution
> 6, 4 and 2. C=O is shorter (two pairs pull the nuclei closer) and stronger than C–O; the table confirms: 1.23 Å and 741 kJ/mol against 1.43 Å and 350 kJ/mol.

> [!question] Exercise 2 (L1)
> List the bonds of acetic acid, CH₃–C(=O)–OH, as single or double and as polar or nonpolar.

> [!success]- Solution
> Single: three C–H (nearly nonpolar), C–C (nonpolar), C–O (polar), O–H (polar). Double: C=O (polar). Eight bonds in total, one of them double.

> [!question] Exercise 3 (L2)
> Using only C–C and C=C, estimate $\Delta H$ per monomer for ethene → polyethylene. Why do the C–H bonds not enter the calculation?

> [!success]- Solution
> Each monomer turns its C=C into a C–C and forms one new C–C to its neighbor: $611 - 2 \times 345 = -79$ kJ/mol, exothermic. The four C–H bonds of each monomer are present before and after, so they cancel.

> [!question] Exercise 4 (L2, Python)
> Apply `assign_bond("C", "O", d)` to $d$ = 1.21, 1.31, 1.36 and 1.52 Å, with the default tolerance and with `tol=0.12`. What do the results say about intermediate lengths?

> [!success]- Solution
> ```python
> for d in (1.21, 1.31, 1.36, 1.52):
>     print(d, assign_bond("C", "O", d), assign_bond("C", "O", d, tol=0.12))
> ```
> Output: `1.21 C=O C=O`, `1.31 None C=O`, `1.36 None C-O`, `1.52 None C-O`. With a strict tolerance, 1.31 and 1.36 Å match nothing: a sign of a bond order between 1 and 2. A loose tolerance forces an integer answer and hides the information.

## Mastery checklist

- [ ] 1 Recognized: I can define a covalent bond and name single, double and triple bonds.
- [ ] 2 Understood: I can explain why more shared pairs give shorter, stronger bonds, and tell polar from nonpolar covalent bonds.
- [ ] 3 Practiced: I can estimate reaction enthalpies from bond energies and assign bonds from coordinates in Python.
- [ ] 4 Applied: I checked bond lengths in a real PDB ligand or residue against the table and found the bonds that do not fit integer orders.
- [ ] 5 Explained: I can explain σ and π contributions, the limits of average bond energies, and why intermediate bond lengths call for resonance.

## References

[^c2e72]: [[Chemistry 2e (OpenStax)]], ch. 7 "Chemical Bonding and Molecular Geometry", §7.2 "Covalent Bonding" (shared electron pairs, nonmetals, polar and nonpolar covalent bonds).
[^c2e73]: [[Chemistry 2e (OpenStax)]], ch. 7, §7.3 "Lewis Symbols and Structures" (single, double and triple bonds).
[^c2e75]: [[Chemistry 2e (OpenStax)]], ch. 7, §7.5 "Strengths of Ionic and Covalent Bonds" (bond energies as gas-phase averages, table of average bond lengths and energies, enthalpy estimates from bond energies).
[^c2e83]: [[Chemistry 2e (OpenStax)]], ch. 8, §8.3 "Multiple Bonds" (σ and π bonds).
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], Unit II "Chemical Bonding & Structure", Lecture 9 "Periodic Table; Ionic and Covalent Bonds".
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein structure (peptide bond, its partial double-bond character, disulfide bonds) and of nucleic acid backbones.
[^mcmurry]: [[Organic Chemistry (OpenStax)]], treatment of carbohydrates (cyclic hemiacetal forms of sugars; chapter not verified).
[^pubchem]: [[PubChem]], compound records (SMILES and InChI line notations).
