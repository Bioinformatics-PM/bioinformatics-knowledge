---
aliases:
  - Fischer Formula
  - D and L Configuration
  - D,L Nomenclature
  - Projection de Fischer
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Stereochemistry]]"
  - "[[Chirality]]"
  - "[[Skeletal Formula]]"
related:
  - "[[Carbohydrate]]"
  - "[[Amino Acid]]"
  - "[[Isomer]]"
  - "[[Diastereomer]]"
  - "[[Conformational Analysis]]"
projects: []
sources:
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
---

# Fischer Projection

> [!abstract]
> A Fischer projection flattens a chain of stereocenters into a column of crosses, with a fixed rule for which bonds point toward you, so that the D or L label of a sugar or an amino acid can be read at a glance.

## Definition

A **Fischer projection** draws a stereocenter as a cross: the carbon sits at the intersection, the **horizontal** bonds come out of the page toward the viewer and the **vertical** bonds go back into the page.[^os252] For a carbon chain, the chain is drawn vertically with C1 (the carbonyl end of a sugar, the carboxyl of an amino acid) at the top, and each crossing is one stereocenter.[^os252][^os253]

**D and L** compare one stereocenter with glyceraldehyde. In a sugar, the reference is the stereocenter **farthest from the carbonyl**: if its OH points right, as in (R)-glyceraldehyde, the sugar is D; if left, L.[^os253] In an α-amino acid drawn with the carboxylate on top and the side chain at the bottom, the amino group points **left** in the L form.[^os261][^lehninger]

## Why it matters

- **Biology picks one series.** The amino acids of proteins are L, and most sugars in organisms, including the ribose and deoxyribose of nucleic acids, are D.[^lehninger] A D/L prefix is therefore not a detail: D- and L-glucose are enantiomers that enzymes tell apart ([[Chirality]]).
- **Reading sugar structures.** Carbohydrate tables and textbooks give the open-chain form of every monosaccharide as a Fischer projection; epimers and families of aldoses are compared column by column ([[Carbohydrate]], [[Diastereomer]]).[^os254]
- **Checking structures.** Since ribosomes build proteins from L-amino acids only, a D residue in a model of an ordinary protein is a red flag to check, while D residues in bacterial cell-wall peptides or peptide antibiotics are real.[^lehninger]

## Core (L1)

![[fischer-projection-wedge-to-cross.svg]]

**Drawing rules.**[^os252]

1. Put the carbon chain vertical, C1 on top.
2. At each stereocenter, the two chain bonds (up and down) point **away** from you; the two side bonds (left and right) point **toward** you.
3. Each intersection is a carbon; carbons and hydrogens are not written at the crossing.

**Reading D or L in a sugar.** Find the stereocenter with the highest number (the one next to the terminal CH₂OH) and look at its OH: right = D, left = L.[^os253] Only that center decides; the other OH groups distinguish sugars of the same series (glucose from mannose, galactose, ...).[^os254]

```text
        CHO          C1
    H — C — OH       C2
   HO — C — H        C3
    H — C — OH       C4
    H — C — OH       C5   <- reference center: OH on the right, so D
        CH2OH        C6
           D-glucose
```

**Reading D or L in an amino acid.** Put COO⁻ on top and the side chain R at the bottom; the α-amino group on the left means L.[^os261] All amino acids of proteins are L, except glycine, which has two H on Cα and is not chiral.[^lehninger]

**Allowed moves.** A Fischer projection may be turned by 180° in the plane of the page; turning it by 90°, or swapping two groups, draws the **enantiomer** (see the Mathematical representation for why).[^os252]

## Deeper (L2)

**D/L is not R/S, and neither is the sign of rotation.** D/L is a *relative* label, a comparison with glyceraldehyde; R/S is assigned from CIP priorities ([[Chirality]]); (+)/(−) is the measured rotation of polarized light. A D sugar can be dextrorotatory or levorotatory.[^os253] The two letter systems usually line up within a family, but not always: L-alanine is S, while L-cysteine is R, because the CH₂SH side chain (S, atomic number 16) outranks COO⁻ (O, 8) at the first point of difference. Same spatial arrangement, different priority order (computed below).

**R/S from a Fischer projection.** Trace priorities 1 → 2 → 3. If the lowest-priority group is on a vertical bond (pointing away), the direction read is the answer (clockwise = R). If it is on a horizontal bond, as the H usually is, reverse the answer (it points toward you, which inverts the apparent direction).

**Counting stereoisomers.** An aldose with $n$ carbons has $n - 2$ stereocenters (C2 to C$n-1$), hence $2^{n-2}$ stereoisomers, half D and half L: 16 aldohexoses, 8 of them D, among which glucose, mannose and galactose.[^os254] Two D-aldoses that differ at one center other than the reference are **epimers** (glucose and galactose at C4); see [[Diastereomer]].

**What the projection hides.** Because both vertical bonds at every carbon point back, a Fischer column depicts each C–C bond in an eclipsed arrangement, with the chain curling away from the viewer. It is a bookkeeping device for configuration, not a picture of the molecule's preferred shape ([[Conformational Analysis]]). Cyclic sugars are drawn with Haworth or chair formulas instead ([[Carbohydrate]]).[^lehninger]

## Mathematical representation

Let the four positions of a cross be $P = \{t, r, b, l\}$ (top, right, bottom, left) and let a drawing be a bijection $f: P \to G$ onto the four distinct groups $G$. Placing the groups at the vertices of a tetrahedron ($t, b$ behind the page, $l, r$ in front), the configuration is the sign of the oriented volume

$$\chi(f) = \operatorname{sign} \det\big[\mathbf{v}_{2} - \mathbf{v}_{1},\ \mathbf{v}_{3} - \mathbf{v}_{1},\ \mathbf{v}_{4} - \mathbf{v}_{1}\big],$$

where $\mathbf{v}_i$ is the position vector of the group of priority $i$. An oriented volume changes sign when two vertices are exchanged, so for a permutation $\sigma$ of the positions, $\chi(f \circ \sigma) = \operatorname{sgn}(\sigma)\, \chi(f)$. A 180° turn is $(t\,b)(l\,r)$, two transpositions, even: the **same molecule**. A 90° turn is the 4-cycle $(t\,r\,b\,l)$, three transpositions, odd: the **enantiomer**. One swap is odd, two swaps are even. A molecule with $k$ independent stereocenters has $2^k$ stereoisomers; fixing the reference center leaves $2^{k-1}$ of the D series.

## Computational representation

Map each position to a 3D direction (vertical bonds back, $z < 0$; horizontal bonds forward, $z > 0$) and take the sign of the triple product of the priority-1, -2 and -3 directions. Negative means clockwise seen with priority 4 away: R. A sugar's open chain can be stored as the tuple of OH sides at each stereocenter.

```python
from itertools import product

# Fischer cross as 3D bond directions: vertical bonds go back (z < 0),
# horizontal bonds come toward the viewer (z > 0).
POS = {"top": (0, 1, -1), "right": (1, 0, 1), "bottom": (0, -1, -1), "left": (-1, 0, 1)}


def triple(a, b, c):
    """Scalar triple product a . (b x c)."""
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def cip_label(fischer: dict, rank: dict) -> str:
    """fischer: position -> group; rank: group -> CIP priority (1 = highest)."""
    where = {group: POS[pos] for pos, group in fischer.items()}
    a, b, c = (where[g] for g in sorted(rank, key=rank.get)[:3])
    return "R" if triple(a, b, c) < 0 else "S"


def rotate(fischer: dict, quarter_turns: int) -> dict:
    """Rotate the drawing clockwise in the plane of the page."""
    order = ["top", "right", "bottom", "left"]
    return {order[(order.index(p) + quarter_turns) % 4]: g for p, g in fischer.items()}


d_glyceraldehyde = {"top": "CHO", "right": "OH", "bottom": "CH2OH", "left": "H"}
l_alanine = {"top": "COO-", "right": "H", "bottom": "CH3", "left": "NH3+"}
l_cysteine = {"top": "COO-", "right": "H", "bottom": "CH2SH", "left": "NH3+"}

print("D-glyceraldehyde", cip_label(d_glyceraldehyde, {"OH": 1, "CHO": 2, "CH2OH": 3, "H": 4}))
ala_rank = {"NH3+": 1, "COO-": 2, "CH3": 3, "H": 4}
print("L-alanine", cip_label(l_alanine, ala_rank))
print("L-cysteine", cip_label(l_cysteine, {"NH3+": 1, "CH2SH": 2, "COO-": 3, "H": 4}))
print("L-alanine turned 180°:", cip_label(rotate(l_alanine, 2), ala_rank),
      "| turned 90°:", cip_label(rotate(l_alanine, 1), ala_rank))

# Aldohexoses: stereocenters C2-C5, each OH drawn on the left or the right.
isomers = list(product(("left", "right"), repeat=4))
d_sugars = [s for s in isomers if s[-1] == "right"]   # C5 is the reference center
print(len(isomers), "aldohexoses,", len(d_sugars), "of them D")
d_glucose = ("right", "left", "right", "right")      # OH sides at C2, C3, C4, C5
print("D-glucose is D:", d_glucose in d_sugars)
```

```text
D-glyceraldehyde R
L-alanine S
L-cysteine R
L-alanine turned 180°: S | turned 90°: R
16 aldohexoses, 8 of them D
D-glucose is D: True
```

## Worked example

> [!example] From a name to a Fischer projection: L-serine
> 1. **Skeleton.** Cα at the crossing, COO⁻ on top, side chain CH₂OH at the bottom ([[Amino Acid]]).
> 2. **L means amino group left.** NH₃⁺ on the left, H on the right.[^os261]
> 3. **Check with CIP.** Priorities: NH₃⁺ (N) > COO⁻ (C with O, O, O) > CH₂OH (C with O, H, H) > H. The H is horizontal, so read 1 → 2 → 3 and reverse: NH₃⁺ (left) → COO⁻ (top) → CH₂OH (bottom) runs clockwise, reversed gives **S**.
> 4. **Its enantiomer.** Swap NH₃⁺ and H: D-serine, R. Turning the drawing by 90° would also give D-serine, which is why only 180° turns are allowed.

## Common misconceptions

> [!warning] "D means dextrorotatory"
> D and L describe configuration relative to glyceraldehyde. The direction of optical rotation is measured, not deduced from the letter: a D sugar can rotate light to the left.[^os253]

> [!warning] "L amino acids are all S"
> Most are, but L-cysteine is R: the sulfur of its side chain changes the CIP priorities, not the spatial arrangement. D/L and R/S answer different questions.

> [!warning] "Every OH on the right means D"
> Only the reference stereocenter (farthest from the carbonyl) decides. D-glucose has its C3 OH on the left and is still D.[^os253]

## Exercises

> [!question] Exercise 1 (L1)
> An aldopentose is drawn with CHO on top, CH₂OH at the bottom and the OH groups of C2, C3 and C4 all on the right. Is it D or L? Which nucleic-acid sugar is it?

> [!success]- Solution
> The reference center is C4 (next to CH₂OH); its OH is on the right, so the sugar is D. All three OH on the right is D-ribose, the sugar of RNA.[^lehninger]

> [!question] Exercise 2 (L2)
> A student turns the projection of D-glyceraldehyde by 90° clockwise and then swaps the groups now at the top and bottom. Which compound does the final drawing represent?

> [!success]- Solution
> A 90° turn is odd (enantiomer); one swap is odd again. Odd + odd = even: the final drawing is D-glyceraldehyde again, although it looks nothing like the standard projection. Check with `cip_label(rotate(...))` after swapping the top and bottom entries: it prints R.

> [!question] Exercise 3 (L2, Python)
> Extend the code to aldopentoses (stereocenters C2 to C4). How many stereoisomers, and how many D? List the D ones as tuples of OH sides.

> [!success]- Solution
> `product(("left", "right"), repeat=3)` gives $2^3 = 8$ isomers; fixing C4 on the right leaves 4 D-aldopentoses, the four combinations of C2 and C3 sides. They are D-ribose (right, right), D-arabinose (left, right), D-xylose (right, left) and D-lyxose (left, left), listed as (C2, C3).[^os254]

## Mastery checklist

- [ ] 1 Recognized: I can say which bonds of a Fischer cross point toward me and which point away.
- [ ] 2 Understood: I can read D or L for any aldose or amino acid and explain why only the reference center matters.
- [ ] 3 Practiced: I can convert between Fischer, wedge-dash and R/S, and justify the 180°-only rule with permutation parity.
- [ ] 4 Applied: I translated a D/L sugar or amino acid name into per-center configurations and checked them against a structure record.
- [ ] 5 Explained: I can explain why D/L, R/S and (+)/(−) are three different labels, with L-cysteine as the counterexample.

## References

[^os252]: [[Organic Chemistry (OpenStax)]], sec. 25.2 "Representing Carbohydrate Stereochemistry: Fischer Projections".
[^os253]: [[Organic Chemistry (OpenStax)]], sec. 25.3 "D,L Sugars".
[^os254]: [[Organic Chemistry (OpenStax)]], sec. 25.4 "Configurations of the Aldoses".
[^os261]: [[Organic Chemistry (OpenStax)]], sec. 26.1 "Structures of Amino Acids".
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021).
