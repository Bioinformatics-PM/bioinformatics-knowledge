---
aliases:
  - Lewis Formula
  - Lewis Dot Structure
  - Formal Charge
  - Lone Pair
  - Structure de Lewis
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
  - "[[Covalent Bond]]"
related:
  - "[[Molecular Geometry]]"
  - "[[Resonance (Chemistry)]]"
  - "[[Molecular Orbital Theory]]"
  - "[[Phosphate Ester]]"
  - "[[Skeletal Formula]]"
  - "[[Hydrogen Bond]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Biochemistry (Berg)]]"
---

# Lewis Structure

> [!abstract]
> A Lewis structure is a bookkeeping drawing of all the valence electrons of a molecule: shared pairs as bonds, unshared pairs as dots, and a formal charge on each atom that shows where an ion's charge is placed.

## Definition

A **Lewis symbol** is an element symbol surrounded by one dot per valence electron. A **Lewis structure** shows every valence electron of a molecule or ion: each shared pair as a line (a [[Covalent Bond]]), each unshared or **lone pair** as two dots; in the usual case each atom ends with eight electrons (two for hydrogen).[^c2e73][^5111] The **formal charge** of an atom is the charge it would carry if every bonding pair were split equally between its two atoms: valence electrons of the free atom, minus its lone-pair electrons, minus half its bonding electrons.[^c2e74]

## Why it matters

- **Every structural formula is one.** Metabolite, drug and residue drawings in databases are Lewis structures with shortcuts (implicit C and H in a [[Skeletal Formula]]); reading them means knowing where the hidden electrons are.
- **Lone pairs do chemistry.** The lone pairs on N and O are the hydrogen-bond acceptors of proteins and nucleic acids and the electron pairs a nucleophile donates ([[Hydrogen Bond]], [[Nucleophile]]).
- **Charges of biological groups.** Formal charges locate the + of –NH₃⁺ and the − of –COO⁻ and of phosphate. Each phosphodiester of the DNA backbone carries one negative charge, which makes DNA a polyanion ([[Phosphate Ester]], Exercise 3).[^berg]

## Core (L1)

**Drawing a Lewis structure** (Chemistry 2e):[^c2e73]

1. Count the valence electrons of all atoms; add one per negative charge, remove one per positive charge.
2. Draw the skeleton with single bonds; the least electronegative atom is usually central, and H is never central.
3. Complete the octets of the outer atoms with lone pairs.
4. Put any electrons left on the central atom.
5. If the central atom still lacks an octet, turn lone pairs of outer atoms into double or triple bonds.

**Water, ammonia, ammonium.** H₂O has $6 + 2 = 8$ valence electrons: two O–H bonds use 4, two lone pairs on O hold the other 4. NH₃ has 8: three bonds and one lone pair. NH₄⁺ has $5 + 4 - 1 = 8$: four bonds, no lone pair.

```text
   water            ammonia           ammonium
    ••                ••                 H    +
  H–O–H             H–N–H              H–N–H
    ••                |                  |
                      H                  H
```

**Formal charges.** O in water: $6 - 4 - \tfrac{4}{2} = 0$. N in NH₄⁺: $5 - 0 - \tfrac{8}{2} = +1$: the charge of the ion is placed on nitrogen. The formal charges of all atoms always add up to the charge of the species.[^c2e74]

**Choosing between structures.** When several structures satisfy the rules, prefer the one whose formal charges are closest to zero, with any negative formal charge on the more electronegative atom.[^c2e74]

**Bio: phosphate.** PO₄³⁻ has $5 + 4(6) + 3 = 32$ valence electrons (worked example). With four P–O single bonds every atom has an octet, P carries +1 and each O −1. Turning one lone pair into a P=O bond gives P a formal charge of 0 and leaves −1 on three oxygens: the structure the formal-charge rule prefers, with 10 electrons around P, which period-3 atoms can accommodate.[^c2e74][^5111b]

## Deeper (L2)

**When the octet rule breaks.** Molecules with an odd number of electrons (radicals such as NO) cannot pair them all; some atoms are electron-deficient; atoms from period 3 on (P, S) can hold more than eight electrons.[^c2e73][^5111b] [[Electron Configuration]] gives the electron-count side of the same story.

**Resonance.** When equally good Lewis structures differ only in where the electrons are placed, the real molecule is an average of them.[^c2e74] Phosphate has four ways to place its P=O, so its four oxygens are equivalent and each carries $-3/4$ on average; carboxylate shares its double bond between two oxygens. [[Resonance (Chemistry)]] treats this in detail.

**What a Lewis structure cannot show.** It does not give the shape: water is drawn straight but is bent ([[Molecular Geometry]]). It pairs every electron of O₂, yet O₂ has two unpaired electrons (it is paramagnetic), which only [[Molecular Orbital Theory]] explains.[^c2e8] And formal charges are not the real distribution of charge, which follows [[Electronegativity]].

## Mathematical representation

For atoms $i$ with valence electrons $v_i$, a species of charge $q$, bonds of order $b$, and $B_i$ the sum of the orders of the bonds of atom $i$:

- Valence electrons $N = \sum_i v_i - q$; bonding electrons $2B$ with $B = \sum_{\text{bonds}} b$; lone electrons $L = N - 2B = \sum_i L_i$.
- Formal charge $F_i = v_i - L_i - B_i$; octet condition $L_i + 2B_i = 8$ (2 for H).
- Each bond contributes its order to both atoms, so $\sum_i B_i = 2B$ and $\sum_i F_i = \sum_i v_i - L - 2B = \sum_i v_i - N = q$: formal charges always add up to the net charge.

## Computational representation

A Lewis structure is a graph with bond orders; lone pairs and formal charges follow from counting:

```python
VALENCE = {"H": 1, "C": 4, "N": 5, "O": 6, "P": 5, "S": 6}

def lewis(atoms: list[str], bonds: list[tuple[int, int, int]], charge: int = 0):
    """Place lone pairs (outer atoms first, octet or H duet), then compute formal charges.
    bonds: (i, j, order). Returns total valence electrons, lone electrons, formal charges,
    and electrons around each atom (lone + 2 x shared pairs)."""
    total = sum(VALENCE[a] for a in atoms) - charge
    order, degree = [0] * len(atoms), [0] * len(atoms)
    for i, j, b in bonds:
        order[i] += b; order[j] += b
        degree[i] += 1; degree[j] += 1
    left = total - 2 * sum(b for _, _, b in bonds)
    lone = [0] * len(atoms)
    for k in sorted(range(len(atoms)), key=lambda k: degree[k] > 1):   # outer atoms first
        lone[k] = min(max(0, (2 if atoms[k] == "H" else 8) - 2 * order[k]), left)
        left -= lone[k]
    lone[degree.index(max(degree))] += left       # leftovers go to the central atom
    formal = [VALENCE[a] - lone[k] - order[k] for k, a in enumerate(atoms)]
    return total, lone, formal, [lone[k] + 2 * order[k] for k in range(len(atoms))]

EXAMPLES = {
    "H2O":          (["O", "H", "H"], [(0, 1, 1), (0, 2, 1)], 0),
    "NH3":          (["N", "H", "H", "H"], [(0, 1, 1), (0, 2, 1), (0, 3, 1)], 0),
    "NH4+":         (["N", "H", "H", "H", "H"], [(0, k, 1) for k in range(1, 5)], +1),
    "PO4(3-), P-O": (["P", "O", "O", "O", "O"], [(0, k, 1) for k in range(1, 5)], -3),
    "PO4(3-), P=O": (["P", "O", "O", "O", "O"], [(0, 1, 2)] + [(0, k, 1) for k in range(2, 5)], -3),
}
for name, (atoms, bonds, q) in EXAMPLES.items():
    total, lone, formal, shell = lewis(atoms, bonds, q)
    print(f"{name:13} N={total:2}  lone={lone}  formal={formal}  shell={shell}")
```

```text
H2O           N= 8  lone=[4, 0, 0]  formal=[0, 0, 0]  shell=[8, 2, 2]
NH3           N= 8  lone=[2, 0, 0, 0]  formal=[0, 0, 0, 0]  shell=[8, 2, 2, 2]
NH4+          N= 8  lone=[0, 0, 0, 0, 0]  formal=[1, 0, 0, 0, 0]  shell=[8, 2, 2, 2, 2]
PO4(3-), P-O  N=32  lone=[0, 6, 6, 6, 6]  formal=[1, -1, -1, -1, -1]  shell=[8, 8, 8, 8, 8]
PO4(3-), P=O  N=32  lone=[0, 4, 6, 6, 6]  formal=[0, 0, -1, -1, -1]  shell=[10, 8, 8, 8, 8]
```

The skeleton and bond orders are input: the code checks a proposed structure, it does not invent one. A `shell` above 8 flags an expanded octet, acceptable for P and S, not for C, N or O.

## Worked example

> [!example] The phosphate ion, PO₄³⁻
> 1. **Count**: P has 5 valence electrons, each O 6, plus 3 for the charge: $5 + 24 + 3 = 32$.
> 2. **Skeleton**: P in the center (less electronegative than O), four P–O single bonds: 8 electrons used, 24 left.
> 3. **Outer octets**: three lone pairs on each O use the 24 electrons. P has 8 electrons from its four bonds: done.
> 4. **Formal charges**: P $= 5 - 0 - 4 = +1$; each O $= 6 - 6 - 1 = -1$; total $+1 - 4 = -3$ ✓.
> 5. **Minimize**: making one P=O gives P $= 5 - 0 - 5 = 0$ and that O $= 6 - 4 - 2 = 0$; total still −3, with smaller formal charges.[^c2e74] Four equivalent positions for the P=O mean four resonance structures: the drawing chooses one, the ion does not.

## Common misconceptions

> [!warning] "The formal charge is the real charge on the atom"
> It is a bookkeeping count that splits every bond equally. The actual charge distribution depends on electronegativity: in NH₄⁺ the +1 is drawn on N, but N pulls electrons from the H atoms ([[Electronegativity]]).[^c2e74]

> [!warning] "Phosphate has one double bond and three single bonds"
> The P=O drawing is one of four equivalent resonance structures; the four P–O bonds of the ion are equivalent ([[Resonance (Chemistry)]]).[^c2e74]

## Exercises

> [!question] Exercise 1 (L1)
> Draw the Lewis structures of HCN and of the hydroxide ion OH⁻. Give the lone pairs and formal charges.

> [!success]- Solution
> HCN: $1 + 4 + 5 = 10$ electrons; H–C≡N with one lone pair on N; all formal charges 0. OH⁻: $6 + 1 + 1 = 8$; O–H with three lone pairs on O; O $= 6 - 6 - 1 = -1$: the charge sits on oxygen.

> [!question] Exercise 2 (L2, Python)
> Use `lewis` to compare O=C=O with O–C≡O for CO₂. Which does the formal-charge rule prefer?

> [!success]- Solution
> ```python
> print(lewis(["C", "O", "O"], [(0, 1, 2), (0, 2, 2)]))
> print(lewis(["C", "O", "O"], [(0, 1, 1), (0, 2, 3)]))
> ```
> Output: `(16, [0, 4, 4], [0, 0, 0], [8, 8, 8])` and `(16, [0, 6, 2], [0, -1, 1], [8, 8, 8])`. Both satisfy every octet, but O=C=O has all formal charges zero, so it is preferred.

> [!question] Exercise 3 (L2, Python)
> Dimethyl phosphate, (CH₃O)₂PO₂⁻, models one phosphodiester of the DNA backbone. Compute its formal charges with one P=O. How many negative charges does a single-stranded DNA of 20 nucleotides carry on its phosphodiesters?

> [!success]- Solution
> ```python
> atoms = ["P", "O", "O", "O", "O", "C", "C"] + ["H"] * 6   # O1 (=O), O2 (-O-), O3 and O4 bridging
> bonds = [(0, 1, 2), (0, 2, 1), (0, 3, 1), (0, 4, 1), (3, 5, 1), (4, 6, 1),
>          (5, 7, 1), (5, 8, 1), (5, 9, 1), (6, 10, 1), (6, 11, 1), (6, 12, 1)]
> total, lone, formal, shell = lewis(atoms, bonds, -1)
> print(total, lone[:7], formal[:7])
> ```
> Output: `44 [0, 4, 6, 4, 4, 0, 0] [0, 0, -1, 0, 0, 0, 0]`. The −1 sits on a non-bridging oxygen (shared with the other one by resonance); the bridging oxygens, bonded to carbon, are neutral. A 20-nucleotide strand has 19 phosphodiesters, hence 19 negative charges: DNA is a polyanion, which is why it migrates toward the anode in [[Gel Electrophoresis]].[^berg]

## Mastery checklist

- [ ] 1 Recognized: I can read a Lewis structure: bonds, lone pairs and formal charges.
- [ ] 2 Understood: I can apply the five-step procedure and the formal-charge rule to choose between structures.
- [ ] 3 Practiced: I can draw water, ammonia, ammonium and phosphate by hand and check them with code.
- [ ] 4 Applied: I located the charged groups and lone pairs of a real amino acid or nucleotide record and related them to its hydrogen bonds.
- [ ] 5 Explained: I can explain where the octet rule fails, why phosphate needs resonance, and why formal charges are not real charges.

## References

[^c2e73]: [[Chemistry 2e (OpenStax)]], ch. 7 "Chemical Bonding and Molecular Geometry", §7.3 "Lewis Symbols and Structures" (Lewis symbols, the drawing procedure, multiple bonds, exceptions to the octet rule).
[^c2e74]: [[Chemistry 2e (OpenStax)]], ch. 7, §7.4 "Formal Charges and Resonance" (formal charge, rules for choosing a structure, resonance).
[^c2e8]: [[Chemistry 2e (OpenStax)]], ch. 8 "Advanced Theories of Covalent Bonding" (molecular orbital description and paramagnetism of O₂; section not verified).
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], Unit II "Chemical Bonding & Structure", Lecture 10 "Introduction to Lewis Structures".
[^5111b]: [[MIT 5.111SC - Principles of Chemical Science]], Unit II, Lecture 11 "Lewis Structures: Breakdown of the Octet Rule".
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of nucleic acid structure (negatively charged phosphodiester backbone) and of DNA electrophoresis.
