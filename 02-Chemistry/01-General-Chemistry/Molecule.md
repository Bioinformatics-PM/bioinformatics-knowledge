---
aliases:
  - Molecular Formula
  - Empirical Formula
  - Molecular Mass
  - Molécule
tags:
  - type/concept
  - domain/chemistry
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Atom]]"
  - "[[Isotope]]"
  - "[[Covalent Bond]]"
related:
  - "[[Mole]]"
  - "[[Isomer]]"
  - "[[Ionic Bond]]"
  - "[[Monoisotopic Mass]]"
  - "[[Mass Spectrometry]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[NIST Atomic Weights and Isotopic Compositions]]"
  - "[[PubChem]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Steen 2004 - The ABC's and XYZ's of Peptide Sequencing]]"
---

# Molecule

> [!abstract]
> A molecule is a group of atoms held together by covalent bonds; its formula counts the atoms, and adding up their masses gives the number a mass spectrometer measures and a database stores.

## Definition

A **molecule** is a group of two or more atoms joined by covalent bonds, the smallest particle of a molecular substance. Its **molecular formula** lists the elements present with subscripts giving the number of atoms of each (glucose, C₆H₁₂O₆); the **empirical formula** gives only the simplest whole-number ratio (CH₂O); a **structural formula** also shows which atoms are bonded. Ionic compounds such as NaCl are not made of molecules: their formula is a ratio of ions ([[Ionic Bond]]).[^c2e2] The **molecular mass** is the sum of the atomic masses of all its atoms, in atomic mass units (u, also called daltons, Da); one mole of molecules weighs the same number in grams ([[Mole]]).[^c2e3]

## Why it matters

- **Databases store formulas and masses.** Each [[PubChem]] compound record carries a molecular formula string, a molecular weight and a monoisotopic mass, computed from the formula; reading and recomputing them is the first check of any chemical data.[^pubchem]
- **Mass spectrometry measures molecules.** Identifying a metabolite or a peptide starts by comparing an observed mass with masses computed from candidate formulas ([[Mass Spectrometry]], [[Monoisotopic Mass]]).[^steen]
- **A formula is not a structure.** Glucose and fructose are both C₆H₁₂O₆ in PubChem,[^pubchem] and ethanol and dimethyl ether are both C₂H₆O: same atoms, different molecules ([[Isomer]]). Search by formula returns candidates, not an answer.

## Core (L1)

**Three ways to write a molecule.** Glucose (C₆H₁₂O₆), acetic acid (C₂H₄O₂, structurally CH₃–COOH) and ribose (C₅H₁₀O₅, the sugar of RNA) all have the empirical formula CH₂O: the empirical formula is the least informative, the structural formula the most.[^c2e2]

**Molecular mass.** Multiply each atom count by its atomic mass and add.[^c2e3] With the average atomic masses computed from NIST isotope data in [[Isotope]] (H 1.00794, C 12.01074, N 14.00670, O 15.99941),[^nist] water weighs $2(1.00794) + 15.99941 = 18.01529$ u.

**Bio: the mass of a peptide.** Each [[Peptide Bond]] forms by condensation, releasing one water, so a peptide of $k$ amino acids has the summed formula of its amino acids minus $(k - 1)$ H₂O.[^berg] The pentapeptide Leu-enkephalin, Tyr-Gly-Gly-Phe-Leu, is C₂₈H₃₇N₅O₇ with a molecular weight of 555.6 in PubChem;[^pubchem] the worked example derives both.

## Deeper (L2)

**Which mass?** The average mass (555.62 u for Leu-enkephalin) describes the population of molecules; the monoisotopic mass (555.26930 u) is that of the molecules made only of the lightest isotopes, the first peak of the isotope cluster. High-resolution mass spectrometry works with the second ([[Isotope]], [[Monoisotopic Mass]]).[^steen]

**Formula strings as PubChem writes them.** Carbon first, then hydrogen, then the other elements alphabetically (C10H16N5O13P3 for ATP); without carbon, all elements alphabetically; a net charge as a suffix. The phosphate ion is `O4P-3`, molecular weight 94.971.[^pubchem] That value equals the sum of the atomic masses: the three extra electrons (0.0016 u, see [[Atom]]) are not counted, a convention to keep in mind when computing exact masses of ions.

## Advanced (L3)

**From sequence to m/z.** A mass spectrometer measures mass-to-charge ratios, and peptides are usually seen as protonated ions $[M + zH]^{z+}$.[^steen] With the proton mass 1.00727 u,[^c2e23] the singly and doubly protonated Leu-enkephalin ions appear at $m/z$ 556.2766 and 278.6419 (Exercise 3). Proteomics software does exactly this for every peptide of a database, using residue masses instead of whole formulas ([[Monoisotopic Mass]], [[Peptide-Spectrum Match]]).

## Mathematical representation

- A formula is a function $n : E \to \mathbb{N}$ from elements to counts (a multiset of atoms). Masses are linear in it: $M = \sum_{e} n_e\, m_e$, with $m_e$ the monoisotopic or the average atomic mass.
- Empirical formula: $n / g$ with $g = \gcd_e(n_e)$. Condensation of $k$ monomers: $n_{\text{polymer}} = \sum_{i=1}^{k} n_{(i)} - (k - 1)\, n_{\text{H}_2\text{O}}$.
- Protonated ion of charge $z$: $m/z = (M + z\, m_p)/z$, $m_p$ the proton mass.

## Computational representation

PubChem formula strings have no parentheses, so a flat parser with an optional charge suffix reads them (the [[Atom]] note parses nested groups; [[Isotope]] derives the masses).

```python
import re
from collections import Counter
from functools import reduce
from math import gcd

# (monoisotopic, average) atomic masses in u, from the NIST isotope table as computed in Isotope
MASS = {"H": (1.00782503223, 1.00794), "C": (12.0, 12.01074), "N": (14.00307400443, 14.00670),
        "O": (15.99491461957, 15.99941), "P": (30.97376199842, 30.97376), "S": (31.9720711744, 32.06479)}
FORMULA = re.compile(r"((?:[A-Z][a-z]?\d*)+)([+-]\d*)?")

def parse(formula: str) -> tuple[Counter, int]:
    """PubChem-style formula -> (element counts, net charge): 'O4P-3' -> ({'O': 4, 'P': 1}, -3)."""
    m = FORMULA.fullmatch(formula)
    if not m:
        raise ValueError(f"not a flat molecular formula: {formula!r}")
    counts = Counter()
    for el, n in re.findall(r"([A-Z][a-z]?)(\d*)", m.group(1)):
        counts[el] += int(n or 1)
    sign = m.group(2) or ""
    return counts, ((1 if sign[0] == "+" else -1) * int(sign[1:] or 1) if sign else 0)

def formula_string(counts: Counter) -> str:
    """C, then H, then the rest alphabetically (all alphabetical if no carbon)."""
    order = (["C", "H"] + sorted(set(counts) - {"C", "H"})) if "C" in counts else sorted(counts)
    return "".join(el + (str(counts[el]) if counts[el] > 1 else "") for el in order if counts[el])

def mass(counts: Counter, kind: str = "average") -> float:
    return sum(n * MASS[el][0 if kind == "mono" else 1] for el, n in counts.items())

def empirical(counts: Counter) -> str:
    g = reduce(gcd, counts.values())
    return formula_string(Counter({el: n // g for el, n in counts.items()}))

AMINO_ACIDS = {"Y": "C9H11NO3", "G": "C2H5NO2", "F": "C9H11NO2", "L": "C6H13NO2"}  # PubChem formulas

def peptide(seq: str) -> Counter:
    """Amino acids joined by len(seq) - 1 condensations, each releasing H2O."""
    total = sum((parse(AMINO_ACIDS[aa])[0] for aa in seq), Counter())
    total.subtract({"H": 2 * (len(seq) - 1), "O": len(seq) - 1})
    return total

for f in ["C6H12O6", "C10H16N5O13P3", "O4P-3"]:
    counts, q = parse(f)
    print(f"{f:14} charge {q:+d}  empirical {empirical(counts):13} "
          f"average {mass(counts):8.3f}  monoisotopic {mass(counts, 'mono'):9.5f}")
enk = peptide("YGGFL")
print(formula_string(enk), round(mass(enk), 2), round(mass(enk, "mono"), 5))
```

```text
C6H12O6        charge +0  empirical CH2O          average  180.156  monoisotopic 180.06339
C10H16N5O13P3  charge +0  empirical C10H16N5O13P3 average  507.182  monoisotopic 506.99575
O4P-3          charge -3  empirical O4P           average   94.971  monoisotopic  94.95342
C28H37N5O7 555.62 555.2693
```

PubChem gives 180.16 (glucose), 507.18 (ATP), 94.971 (phosphate) and 555.6 (Leu-enkephalin): the calculator agrees to the digits shown.[^pubchem] An element missing from `MASS` raises a `KeyError` rather than guessing.

## Worked example

> [!example] Leu-enkephalin from its sequence
> 1. **Amino acids** (PubChem formulas):[^pubchem] Tyr C₉H₁₁NO₃, Gly C₂H₅NO₂ (twice), Phe C₉H₁₁NO₂, Leu C₆H₁₃NO₂.
> 2. **Sum**: C $9+2+2+9+6 = 28$, H $11+5+5+11+13 = 45$, N 5, O $3+2+2+2+2 = 11$.
> 3. **Four peptide bonds, four waters out**: H $45 - 8 = 37$, O $11 - 4 = 7$: C₂₈H₃₇N₅O₇, the PubChem formula.
> 4. **Average mass**: $28(12.01074) + 37(1.00794) + 5(14.00670) + 7(15.99941) = 336.30072 + 37.29378 + 70.03350 + 111.99587 = 555.624$ u, PubChem's 555.6.
> 5. **Monoisotopic mass**: the same sum with ¹²C, ¹H, ¹⁴N, ¹⁶O gives 555.2693 u, 0.35 u lighter: the value to match in a high-resolution spectrum.

## Common misconceptions

> [!warning] "A peptide weighs the sum of its amino acids"
> Each peptide bond releases a water: a pentapeptide is $4 \times 18.015 = 72.06$ u lighter than its five free amino acids.[^berg]

> [!warning] "Molecular weight is in grams"
> One molecule of glucose weighs 180.16 u; it is one **mole** of glucose that weighs 180.16 g ([[Mole]]).[^c2e3]

## Exercises

> [!question] Exercise 1 (L1)
> Give the empirical formulas of ribose C₅H₁₀O₅, deoxyribose C₅H₁₀O₄ and benzene C₆H₆, and the average molecular masses of CO₂ and NH₃.

> [!success]- Solution
> CH₂O, C₅H₁₀O₄ (the counts share no common factor), CH. $M(\text{CO}_2) = 12.01074 + 2(15.99941) = 44.00956$ u; $M(\text{NH}_3) = 14.00670 + 3(1.00794) = 17.03052$ u.

> [!question] Exercise 2 (L2, Python)
> A compound contains 40.0 % C, 6.7 % H and 53.3 % O by mass; its molar mass is about 180 g/mol. Find its empirical and molecular formulas.

> [!success]- Solution
> ```python
> pct = {"C": 40.0, "H": 6.7, "O": 53.3}
> moles = {el: p / MASS[el][1] for el, p in pct.items()}
> print({el: round(n / min(moles.values()), 2) for el, n in moles.items()})
> print(round(mass(parse("CH2O")[0]), 3), round(180 / mass(parse("CH2O")[0]), 2))
> ```
> Output: `{'C': 1.0, 'H': 2.0, 'O': 1.0}` then `30.026 5.99`. Empirical formula CH₂O, multiple 6: C₆H₁₂O₆. Composition alone could not separate it from acetic acid (C₂H₄O₂, also CH₂O); the molar mass does, but not from fructose.

> [!question] Exercise 3 (L3, Python)
> Compute the $m/z$ of the [M+H]⁺ and [M+2H]²⁺ ions of Leu-enkephalin from its monoisotopic mass, with $m_p = 1.00727$ u.

> [!success]- Solution
> ```python
> m = mass(peptide("YGGFL"), "mono")
> for z in (1, 2):
>     print(z, round((m + z * 1.00727) / z, 4))
> ```
> Output: `1 556.2766` and `2 278.6419`. The 2+ ion appears at about half the mass: the charge state must be known (from isotope spacing, [[Isotope]]) before a peak can be turned into a mass.

## Mastery checklist

- [ ] 1 Recognized: I can tell molecular, empirical and structural formulas apart.
- [ ] 2 Understood: I can explain why a formula does not identify a compound and why ionic compounds have formula units instead of molecules.
- [ ] 3 Practiced: I can parse PubChem formula strings and compute empirical formulas, average and monoisotopic masses and peptide formulas in Python.
- [ ] 4 Applied: I checked my calculator against PubChem records and matched a computed peptide m/z to a real spectrum peak.
- [ ] 5 Explained: I can explain which mass to use when, the charge and electron conventions of ion formulas, and why formula search returns isomers.

## References

[^c2e2]: [[Chemistry 2e (OpenStax)]], ch. 2 "Atoms, Molecules, and Ions" (molecules, molecular, empirical and structural formulas, ionic versus molecular compounds; section not verified).
[^c2e3]: [[Chemistry 2e (OpenStax)]], formula mass, the mole and empirical formulas from percent composition (chapter not verified).
[^c2e23]: [[Chemistry 2e (OpenStax)]], ch. 2, §2.3 "Atomic Structure and Symbolism" (Table 2.1, mass of the proton).
[^nist]: [[NIST Atomic Weights and Isotopic Compositions]], relative atomic masses and isotopic compositions of H, C, N, O, P, S.
[^pubchem]: [[PubChem]], compound records for glucose, fructose, ATP, the phosphate ion (CID 1061, `O4P-3`, 94.971 g/mol), tyrosine, glycine, phenylalanine, leucine and Leu-enkephalin (C₂₈H₃₇N₅O₇, 555.6 g/mol).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of the peptide bond (formation with loss of a water molecule).
[^steen]: [[Steen 2004 - The ABC's and XYZ's of Peptide Sequencing]], *Nature Reviews Molecular Cell Biology* (m/z, protonated peptide ions, monoisotopic peaks).
