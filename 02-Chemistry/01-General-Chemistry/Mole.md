---
aliases:
  - mol
  - Amount of Substance
  - Avogadro Constant
  - Avogadro's Number
  - Molar Mass
  - Mole (unit)
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Atom]]"
  - "[[Isotope]]"
  - "[[Molecule]]"
  - "[[Exponential Function]]"
related:
  - "[[Molar Concentration]]"
  - "[[Stoichiometry]]"
  - "[[Monoisotopic Mass]]"
  - "[[Plasmid]]"
  - "[[Molecular Cloning]]"
  - "[[Polymerase Chain Reaction]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
---

# Mole

> [!abstract]
> A mole is a fixed number of things, 6.022 × 10²³, chosen so that a mole of a substance weighs its molecular mass in grams. It is the bridge between what a balance measures (nanograms of DNA) and what biology counts (copies of a plasmid).

## Definition

The **mole** (mol) is the unit of amount of substance: one mole contains $N_A = 6.022 \times 10^{23}$ entities (atoms, molecules, ions, base pairs), the **Avogadro constant**. The **molar mass** $M$ of a substance, in g/mol, is numerically equal to its formula (molecular) mass in atomic mass units, so 1 mol of water weighs 18.015 g.[^c2e31] Biochemists express molecular masses in **daltons** (1 Da = 1 u): a 50 kDa protein has a molar mass of 50,000 g/mol.[^berg]

## Why it matters

- **Template copies.** A protocol gives DNA in nanograms, but a [[Polymerase Chain Reaction|PCR]] amplifies molecules: converting mass to copies tells how many templates a reaction starts from ([[Quantitative Polymerase Chain Reaction]]).
- **Cloning ratios.** Insert and vector are mixed in molar, not mass, ratios, because ligation joins molecules ([[Molecular Cloning]]).
- **Masses in data.** A mass spectrum reports masses in daltons per molecule, i.e. g/mol ([[Mass Spectrometry]], [[Monoisotopic Mass]]); reaction and metabolic bookkeeping is in moles ([[Stoichiometry]]).

## Core (L1)

**Three quantities, two conversions.** Mass $m$ (g), amount $n$ (mol) and number of entities $N$:[^c2e31]

```mermaid
flowchart LR
  M["mass m (g)"] -->|"÷ molar mass M (g/mol)"| N["amount n (mol)"]
  N -->|"× N_A"| P["number of entities N"]
  P -->|"÷ N_A"| N
  N -->|"× M"| M
```

**Molar mass from a formula.** Add the standard atomic weights of the atoms: H₂O = 2 × 1.008 + 15.999 = 18.015 g/mol.[^c2eaw] These weights are averages over natural [[Isotope|isotopes]], which is why they are not integers.[^c2e23]

**Bio: copies of a plasmid in 1 ng.** For double-stranded DNA of length $L$ base pairs with an average mass $\bar m_{bp}$ per base pair,

$$N = \frac{m}{L\, \bar m_{bp}}\, N_A.$$

The base-pair mass follows from atomic weights (Deeper): about 618 g/mol. A 3,000 bp plasmid (toy size) therefore weighs $1.85 \times 10^6$ g/mol, and 1 ng contains

$$\frac{10^{-9}}{3000 \times 617.9} \times 6.022 \times 10^{23} \approx 3.2 \times 10^{8} \text{ copies}.$$

## Deeper (L2)

**Mass of a base pair, derived.** A nucleotide inside a DNA chain is a base plus deoxyribose (C₅H₁₀O₄) plus phosphoric acid (H₃PO₄), minus three water molecules: one for the glycosidic bond, one for the phosphate ester, one for the phosphodiester link to the next nucleotide ([[Nucleotide]], [[Nucleic Acid]]). With the base formulas (adenine C₅H₅N₅, cytosine C₄H₅N₃O, guanine C₅H₅N₅O, thymine C₅H₆N₂O₂)[^berg] and standard atomic weights,[^c2eaw] the code below gives residue masses of 313.21 (dA), 289.18 (dC), 329.21 (dG) and 304.19 g/mol (dT), with the formulas in its output. An A·T pair weighs 617.40 g/mol and a G·C pair 618.39: composition barely matters, and 617.9 g/mol per bp is a good average. This is the acid form, with H⁺ on each phosphate. If every phosphate carries Na⁺ instead (a sodium salt), add $2 \times (22.990 - 1.008)$ per base pair: 661.9 g/mol. The 7 % difference between the two forms bounds the error of any rounded value; a circular plasmid has no end groups, and for long linear DNA they are negligible.

**Genomes per nanogram.** With $\bar m_{bp} = 617.9$ g/mol:

| DNA | Length | Mass of one copy | Copies in 1 ng |
|---|---:|---:|---:|
| haploid human genome | $3.055 \times 10^9$ bp[^nurk] | 3.1 pg | 319 |
| *E. coli* K-12 genome | 4,639,221 bp[^blattner] | 4.8 fg | $2.1 \times 10^5$ |

A diploid human cell holds about 6.3 pg of nuclear DNA, so 10 ng of human genomic DNA is only about 1,600 cells' worth of templates: the limit of detection of a rare variant in a sample is set by this count ([[Variant Calling]]).

**Proteins.** The mean mass of an amino acid residue is about 110 g/mol,[^berg] so a 450-residue protein is near 50 kDa, and 1 µg of it is $10^{-6}/50{,}000 = 2 \times 10^{-11}$ mol: 20 pmol, $1.2 \times 10^{13}$ molecules.

## Mathematical representation

- $n = m/M$ and $N = n\,N_A$, so $N = m\,N_A/M$. Units: g ÷ (g/mol) = mol; mol × mol⁻¹ = dimensionless count.
- **Polymer of residues**: $M \approx \sum_{i=1}^{L} M_{r}(s_i)$ plus end groups; for a duplex of length $L$, $M \approx L\,\bar m_{bp}$, so copies $N = m N_A/(L \bar m_{bp})$ scale as $1/L$: the same mass of a ten-times longer DNA holds ten times fewer molecules.

## Computational representation

```python
import re
from collections import Counter

N_A = 6.022e23   # mol^-1, Avogadro constant
WEIGHT = {"H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999, "P": 30.974, "Na": 22.990}  # g/mol
BASES = {"A": "C5H5N5", "C": "C4H5N3O", "G": "C5H5N5O", "T": "C5H6N2O2"}

def parse(formula: str) -> Counter:
    """'C5H10O4' -> Counter({'H': 10, 'C': 5, 'O': 4})."""
    counts = Counter()
    for element, n in re.findall(r"([A-Z][a-z]?)(\d*)", formula):
        counts[element] += int(n or 1)
    return counts

def molar_mass(counts: Counter) -> float:
    return sum(WEIGHT[el] * n for el, n in counts.items())

def dna_residue(base: str) -> Counter:
    """One nucleotide inside a DNA chain (free acid): base + deoxyribose + H3PO4 - 3 H2O."""
    c = parse(BASES[base]) + parse("C5H10O4") + parse("H3PO4")
    for _ in range(3):          # glycosidic bond, 5'-phosphate ester, 3'-phosphodiester link
        c -= parse("H2O")
    return c

def formula(c: Counter) -> str:
    return "".join(f"{el}{c[el] if c[el] > 1 else ''}" for el in ("C", "H", "N", "O", "P") if c[el])

def copies(mass_g: float, length_bp: float, bp_mass: float) -> float:
    """Number of double-stranded molecules of length_bp in mass_g, at bp_mass g/mol per base pair."""
    return mass_g / (length_bp * bp_mass) * N_A

residue = {b: molar_mass(dna_residue(b)) for b in "ACGT"}
for b in "ACGT":
    print(b, formula(dna_residue(b)), round(residue[b], 2))
at, gc = residue["A"] + residue["T"], residue["G"] + residue["C"]
bp_acid = (at + gc) / 2                                  # 50 % GC
bp_na = bp_acid + 2 * (WEIGHT["Na"] - WEIGHT["H"])       # one Na+ per phosphate instead of H+
print(f"A-T {at:.2f}, G-C {gc:.2f}, mean {bp_acid:.1f} g/mol per bp; sodium salt {bp_na:.1f}")

print(f"3,000 bp plasmid, 1 ng: {copies(1e-9, 3000, bp_acid):.2e} (acid) {copies(1e-9, 3000, bp_na):.2e} (Na salt)")
human, ecoli = 3.055e9, 4_639_221
print(f"haploid human genomes per ng: {copies(1e-9, human, bp_acid):.0f}; "
      f"diploid genome mass: {2 * human * bp_acid / N_A * 1e12:.2f} pg")
print(f"E. coli genome: {ecoli * bp_acid / N_A * 1e15:.2f} fg; genomes per ng: {copies(1e-9, ecoli, bp_acid):.2e}")
```

```text
A C10H12N5O5P 313.21
C C9H12N3O6P 289.18
G C10H12N5O6P 329.21
T C10H13N2O7P 304.19
A-T 617.40, G-C 618.39, mean 617.9 g/mol per bp; sodium salt 661.9
3,000 bp plasmid, 1 ng: 3.25e+08 (acid) 3.03e+08 (Na salt)
haploid human genomes per ng: 319; diploid genome mass: 6.27 pg
E. coli genome: 4.76 fg; genomes per ng: 2.10e+05
```

## Worked example

> [!example] Template copies for a qPCR standard
> A plasmid of 3,000 bp (toy) is at 1 ng/µL. How many copies are in 1 µL, and what dilution gives $10^4$ copies/µL?
> 1. **Mass of one mole of plasmid**: $3000 \times 617.9 = 1.854 \times 10^6$ g/mol.
> 2. **Amount in 1 ng**: $10^{-9} / 1.854 \times 10^6 = 5.39 \times 10^{-16}$ mol (0.54 fmol).
> 3. **Copies**: $5.39 \times 10^{-16} \times 6.022 \times 10^{23} = 3.25 \times 10^8$ per µL (code output).
> 4. **Dilution**: $3.25 \times 10^8 / 10^4 = 3.25 \times 10^4$-fold, made in steps ([[Molar Concentration#Core (L1)]]). With the sodium-salt mass the count is $3.03 \times 10^8$: the base-pair mass moves the answer by 7 %, small next to pipetting and quantification errors.

## Common misconceptions

> [!warning] "A nanogram of DNA is a nanogram of DNA"
> The number of molecules in 1 ng is inversely proportional to length: 1 ng holds $3.2 \times 10^8$ copies of a 3 kb plasmid but only 319 haploid human genomes.

> [!warning] "Molar masses are whole numbers"
> Standard atomic weights average over isotopes (C 12.011, not 12),[^c2eaw][^c2e23] so molar masses are not integers; a mass spectrometer resolving single isotopes uses monoisotopic masses instead ([[Monoisotopic Mass]]).

## Exercises

> [!question] Exercise 1 (L1)
> Using the residue masses above, estimate the mass of 1 pmol of a 20-nucleotide single-stranded DNA primer (toy, 5 of each base), ignoring end groups.

> [!success]- Solution
> Mean residue mass $(313.21 + 289.18 + 329.21 + 304.19)/4 = 308.95$ g/mol; 20 residues: 6,179 g/mol. 1 pmol $= 10^{-12} \times 6179$ g $= 6.2$ ng.

> [!question] Exercise 2 (L2)
> A tumour DNA sample provides 10 ng of human genomic DNA. How many haploid genome copies does it contain, and what is the smallest fraction of copies a variant can occupy if it must be seen in at least 5 copies?

> [!success]- Solution
> $10 \times 319 = 3{,}190$ haploid copies (about 1,600 diploid cells). Five copies out of 3,190 is 0.16 %: no assay can detect a variant rarer than this in this input, however deep the sequencing, because the molecules are not there.

> [!question] Exercise 3 (L2, Python)
> With `copies`, compute the copies per µL of a 5,000 bp plasmid at 25 ng/µL, and the volume that contains $10^6$ copies.

> [!success]- Solution
> ```python
> per_ul = copies(25e-9, 5000, 617.9)
> print(f"{per_ul:.2e} copies/µL; {1e6 / per_ul:.2e} µL for 1e6 copies")
> ```
> Output: `4.87e+09 copies/µL; 2.05e-04 µL for 1e6 copies`. No pipette delivers 0.2 nL: dilute first, for example 1:1000 then 1:10, to $4.87 \times 10^5$ copies/µL ([[Molar Concentration]]).

## Mastery checklist

- [ ] 1 Recognized: I can state $N_A = 6.022 \times 10^{23}$ mol⁻¹ and the meaning of g/mol and Da.
- [ ] 2 Understood: I can convert between mass, amount and number of particles, and explain why molar masses are not integers.
- [ ] 3 Practiced: I can derive the mass of a DNA base pair from atomic weights and compute copy numbers in code.
- [ ] 4 Applied: I computed the template copies of a real PCR or library preparation from its DNA input.
- [ ] 5 Explained: I can explain how input mass limits sensitivity (copies per ng) and which assumptions the conversion hides.

## References

[^c2e31]: [[Chemistry 2e (OpenStax)]], ch. 3, §3.1 "Formula Mass and the Mole Concept" (Avogadro's number 6.022 × 10²³, molar mass numerically equal to formula mass).
[^c2eaw]: [[Chemistry 2e (OpenStax)]], standard atomic weights (H 1.008, C 12.011, N 14.007, O 15.999, Na 22.990, P 30.974).
[^c2e23]: [[Chemistry 2e (OpenStax)]], ch. 2, §2.3 "Atomic Structure and Symbolism" (isotopes, average atomic mass).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), structures of the nucleic acid bases; protein masses in daltons and mean residue mass of about 110 g/mol.
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science* (T2T-CHM13, about 3.055 × 10⁹ bp).
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science* (4,639,221 bp).
