---
aliases:
  - Amide Bond
  - Peptide Linkage
  - Liaison peptidique
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Amino Acid]]"
  - "[[Covalent Bond]]"
  - "[[Functional Group]]"
  - "[[Hydrolysis]]"
  - "[[Resonance (Chemistry)]]"
related:
  - "[[Protein]]"
  - "[[Protein Structure]]"
  - "[[Translation]]"
  - "[[Ribosome]]"
  - "[[Cis-Trans Isomerism]]"
  - "[[Ramachandran Plot]]"
  - "[[Protein Secondary Structure]]"
  - "[[Monoisotopic Mass]]"
  - "[[Bottom-Up Proteomics]]"
projects: []
sources:
  - "[[Biochemistry (Berg)]]"
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biology 2e (OpenStax)]]"
---

# Peptide Bond

> [!abstract]
> The peptide bond is the amide link that chains amino acids together: it is flat and stiff, so a protein can only bend between the links, and it gives every chain a direction, read from its amino end to its carboxyl end.

## Definition

A **peptide bond** is the amide bond formed between the α-carboxyl group of one amino acid and the α-amino group of the next, with the loss of a water molecule (a condensation, or dehydration, reaction).[^berg][^os3][^mcmurry] Amino acids joined this way form a **polypeptide**: a backbone of repeating N–Cα–C units, with one side chain on each Cα.[^berg]

## Why it matters

- **Direction of every protein sequence.** Files, databases and tools write proteins from the N-terminus to the C-terminus, the direction in which the [[Ribosome]] makes them ([[Translation]]).[^berg][^alberts]
- **Masses.** A peptide's mass is the sum of its residue masses plus one water, because each peptide bond removed one ([[Monoisotopic Mass]]).
- **Proteomics cuts peptide bonds.** Proteases hydrolyze specific peptide bonds: trypsin cleaves on the carboxyl side of Lys and Arg, which is how [[Bottom-Up Proteomics]] turns proteins into predictable peptides.[^berg]
- **Geometry of structure.** Because the bond is planar, a residue has only two free backbone angles, φ and ψ: the coordinates of the [[Ramachandran Plot]], of secondary structure assignment and of structure prediction ([[Protein Structure]]).[^berg]

## Core (L1)

**Formation.** The carboxyl of residue $i$ and the amino group of residue $i+1$ condense into –CO–NH–, releasing H₂O.[^berg][^os3] A chain of $n$ residues contains $n - 1$ peptide bonds. In cells the bond is not made by simple condensation: the [[Ribosome]] transfers the growing chain onto the next aminoacyl-tRNA, paid for by the activation of amino acids ([[Translation]]).[^alberts]

**Stable, but not at equilibrium.** The equilibrium of the reaction lies on the side of hydrolysis, so making a peptide bond requires energy; yet without a catalyst hydrolysis is extremely slow (the lifetime of a peptide bond in water approaches 1000 years). Proteins are kinetically stable, and proteases supply the catalysis when the cell wants them cut.[^berg]

**Direction.** A polypeptide has a free α-amino group at one end, the **N-terminus** (amino terminus), and a free α-carboxyl group at the other, the **C-terminus**. By convention the sequence is written from the N-terminus: `GAS` means Gly-Ala-Ser, with Gly carrying the free amino group, and it is a different molecule from `SAG`.[^berg] This is also the order of synthesis: the ribosome adds residues to the C-terminal end, reading the mRNA 5' → 3' ([[Translation]]).[^alberts]

![[peptide-bond-planarity.svg]]

**Planar and rigid.** The six atoms Cα(i), C, O, N, H and Cα(i+1) lie in one plane, and there is essentially no rotation about the C–N bond.[^berg]

**Usually trans.** In almost all peptide bonds the two Cα atoms lie on opposite sides of the C–N bond (**trans**); the cis form brings their side chains into steric clash.[^berg]

## Deeper (L2)

**Why planar: resonance.** The lone pair of the nitrogen is delocalized into the carbonyl, so the bond is a hybrid of two structures, O=C–N and O⁻–C=N⁺ ([[Resonance (Chemistry)]]).[^berg][^mcmurry] The partial double-bond character shows in the lengths:[^berg]

| Bond | Length |
|---|---:|
| C–N single bond | 1.49 Å |
| **C–N peptide bond** | **1.32 Å** |
| C=N double bond | 1.27 Å |

As for a C=C double bond, rotation would break the π overlap, which locks the six atoms in a plane ([[Cis-Trans Isomerism]]).

**Trans versus cis in numbers.** For most residues the trans form is favored by about 1000 to 1. Before a proline (an X–Pro bond), the residue's ring creates steric clashes in both forms, the two have similar energies, and cis X–Pro bonds are much more common.[^berg]

**Polar but uncharged.** The peptide bond carries no charge, which lets chains pack tightly; its C=O is a hydrogen-bond acceptor and its N–H a donor.[^berg] These backbone groups make the hydrogen bonds of α helices and β sheets ([[Protein Secondary Structure]]). Proline, whose nitrogen is bonded to its own side chain, has no N–H to donate.[^berg]

**Three torsion angles per residue.** Along the backbone, rotation is free about the N–Cα bond (angle **φ**, phi) and the Cα–C bond (angle **ψ**, psi); many (φ, ψ) pairs are still forbidden by steric clashes, which the [[Ramachandran Plot]] maps.[^berg] The torsion about the peptide bond itself, **ω** (omega), stays near 180° (trans) or 0° (cis). A chain of $n$ residues therefore has about $2n$ free backbone angles, not $3n$.

## Mathematical representation

- **Counting.** A linear chain $a_1 a_2 \dots a_n$ has $n - 1$ peptide bonds. Its molecular mass is $M = \sum_{i=1}^{n} m(a_i) - (n-1)\, m(\text{H}_2\text{O})$ with $m(a)$ the free amino acid masses, or equivalently $\sum_i r(a_i) + m(\text{H}_2\text{O})$ with $r(a) = m(a) - m(\text{H}_2\text{O})$ the **residue** masses ([[Monoisotopic Mass]]).
- **Direction.** A sequence is an ordered word; reversal is not a symmetry: $a_1 \dots a_n$ and $a_n \dots a_1$ are different molecules (unless the word is a palindrome).
- **Torsion angle.** For four atoms $p_0, p_1, p_2, p_3$, let $\hat b = (p_2 - p_1)/\lVert p_2 - p_1 \rVert$, and $v$, $w$ the components of $p_0 - p_1$ and $p_3 - p_2$ perpendicular to $\hat b$. Then
$$\theta = \operatorname{atan2}\big((\hat b \times v) \cdot w,\; v \cdot w\big) \in (-180°, 180°].$$
With $(p_0, \dots, p_3) = (\text{C}\alpha_i, \text{C}_i, \text{N}_{i+1}, \text{C}\alpha_{i+1})$ this is ω: $\pm 180°$ for trans, $0°$ for cis. The same formula gives φ from $(\text{C}_{i-1}, \text{N}_i, \text{C}\alpha_i, \text{C}_i)$ and ψ from $(\text{N}_i, \text{C}\alpha_i, \text{C}_i, \text{N}_{i+1})$.
- **Conformational count.** If each of the $2n$ free angles had only $k$ allowed values, a chain would have $k^{2n}$ backbone conformations: $3^{200} \approx 2.7 \times 10^{95}$ for $n = 100$ and $k = 3$, the combinatorial problem discussed in [[Protein Folding]].

## Computational representation

Sequence tools need only the convention (strings written N → C); structure tools compute torsion angles from coordinates ([[PDB Format]]); proteomics tools simulate the cutting of peptide bonds.

```python
import math

Vec = tuple[float, float, float]


def sub(a: Vec, b: Vec) -> Vec: return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def dot(a: Vec, b: Vec) -> float: return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def cross(a: Vec, b: Vec) -> Vec:
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dihedral(p0: Vec, p1: Vec, p2: Vec, p3: Vec) -> float:
    """Torsion angle (degrees, -180..180) about the p1-p2 bond."""
    b0, b1, b2 = sub(p0, p1), sub(p2, p1), sub(p3, p2)
    norm = math.sqrt(dot(b1, b1))
    b1 = (b1[0] / norm, b1[1] / norm, b1[2] / norm)
    v = sub(b0, tuple(dot(b0, b1) * c for c in b1))   # parts perpendicular to the bond
    w = sub(b2, tuple(dot(b2, b1) * c for c in b1))
    return math.degrees(math.atan2(dot(cross(b1, v), w), dot(v, w)))


def tryptic_peptides(protein: str) -> list[str]:
    """Textbook rule: trypsin cuts the peptide bond after every Lys (K) or Arg (R)."""
    peptides, start = [], 0
    for i, aa in enumerate(protein):
        if aa in "KR":
            peptides.append(protein[start:i + 1])
            start = i + 1
    return peptides + ([protein[start:]] if start < len(protein) else [])


# Idealized coordinates in Å (invented geometry): Cα(i), C, N, then three choices for Cα(i+1)
ca1, c, n = (-0.5, 1.4, 0.0), (0.0, 0.0, 0.0), (1.32, 0.0, 0.0)
for name, ca2 in (("trans", (1.82, -1.4, 0.0)), ("cis", (1.82, 1.4, 0.0)), ("twisted", (1.82, -0.7, 1.2))):
    print(f"omega {name:8}{dihedral(ca1, c, n, ca2):8.1f}")

protein = "MASKGLEWRAVDKTGRPLE"            # invented sequence
peptides = tryptic_peptides(protein)
print(peptides)
print(len(protein) - 1, "peptide bonds,", len(peptides) - 1, "cut by trypsin")
```

```text
omega trans      180.0
omega cis          0.0
omega twisted    120.3
['MASK', 'GLEWR', 'AVDK', 'TGR', 'PLE']
18 peptide bonds, 4 cut by trypsin
```

A "twisted" ω of 120° does not occur in real peptide bonds: a structure-validation program would flag it. The trypsin rule here is the textbook one; digestion tools add refinements, such as rules for a Pro after the Lys or Arg (here `R|P`), described in [[Bottom-Up Proteomics]].

## Worked example

> [!example] Building the tripeptide Gly-Ala-Ser
> 1. **Bonds.** Gly-COOH + H₂N-Ala gives the first peptide bond and one H₂O; Ala-COOH + H₂N-Ser gives the second. Three residues, two peptide bonds, two waters.
> 2. **Ends.** Gly keeps the free α-amino group (N-terminus), Ser the free α-carboxyl group (C-terminus). The name and the one-letter string `GAS` are both written N → C.
> 3. **Mass.** With molecular weights 75 (Gly), 89 (Ala) and 105 (Ser),[^lehninger] $M = 75 + 89 + 105 - 2 \times 18 = 233$.
> 4. **Geometry.** Two planar peptide units; the free backbone angles are φ and ψ of the middle residue, ψ of Gly and φ of Ser (the terminal φ of Gly and ψ of Ser are not defined by a following or preceding peptide unit).
> 5. **Reversal.** `SAG` has the same composition and mass, but Ser now carries the amino group: a different molecule, with different chemistry and a different sequence in any database.

## Common misconceptions

> [!warning] "Peptide bonds are fragile; that is why proteins are degraded"
> Uncatalyzed hydrolysis is extremely slow. Proteins are degraded because cells use proteases, not because the bond falls apart.[^berg]

> [!warning] "The chain can rotate around each of its backbone bonds"
> Rotation about the C–N peptide bond is blocked by its partial double-bond character; only φ and ψ are free, and even they are restricted by steric clashes.[^berg]

## Exercises

> [!question] Exercise 1 (L1)
> A polypeptide has 146 residues. How many peptide bonds does it contain, and how many water molecules were released in forming them? Which group is free at each end?

> [!success]- Solution
> $146 - 1 = 145$ peptide bonds and 145 waters. The first residue keeps its α-amino group (N-terminus), the last its α-carboxyl group (C-terminus).

> [!question] Exercise 2 (L1)
> An mRNA reads `5'-AUG GCU UCU UGG UAA-3'`. Write the peptide in three-letter and one-letter code, and say which residue is N-terminal.

> [!success]- Solution
> Met-Ala-Ser-Trp, `MASW` ([[Genetic Code]]). Met is N-terminal: the first codon read (5' end) gives the N-terminus, the last sense codon the C-terminus.[^alberts]

> [!question] Exercise 3 (L2)
> The peptide C–N bond is 1.32 Å long. Using the single (1.49 Å) and double (1.27 Å) C–N lengths, estimate by linear interpolation its "fraction of double-bond character", and explain why this makes the bond planar.

> [!success]- Solution
> $(1.49 - 1.32)/(1.49 - 1.27) = 0.17/0.22 \approx 0.77$: by this crude interpolation, the bond is closer to a double bond than to a single one. The double-bond component comes from π overlap between N, C and O orbitals, which requires the atoms around the bond to be coplanar; rotating would break the overlap, as for C=C ([[Cis-Trans Isomerism]]).[^berg]

> [!question] Exercise 4 (L2, Python)
> With `dihedral` from the code above, compute ω for Cα(i) = (−0.5, 1.4, 0), C = (0, 0, 0), N = (1.32, 0, 0) and Cα(i+1) = (1.82, 1.4, 0.4). Classify the bond as cis or trans, and say what a value like this would mean in a real structure.

> [!success]- Solution
> ```python
> print(round(dihedral((-0.5, 1.4, 0), (0, 0, 0), (1.32, 0, 0), (1.82, 1.4, 0.4)), 1))   # 15.9
> ```
> ω ≈ 16°: close to 0°, so a (slightly distorted) cis bond. Real peptide bonds deviate from planarity only by small amounts. A cis bond not preceding a proline is rare (about 1 in 1000 for other residues),[^berg] so in a structure it deserves a check: real, or a modelling error?

> [!question] Exercise 5 (L2, Python)
> Use `tryptic_peptides` on the invented protein `MKRGASKKLER`. How many peptides are produced, and which are single residues? Why are very short peptides of little use for identifying a protein?

> [!success]- Solution
> ```python
> print(tryptic_peptides("MKRGASKKLER"))   # ['MK', 'R', 'GASK', 'K', 'LER']
> ```
> Five peptides, two of them single residues (`R`, `K`) produced by consecutive cut sites. A short peptide has few possible sequences (there are only 400 dipeptides), so the same short sequence, and its mass, occurs in many proteins: it identifies none. Identification relies on longer peptides ([[Peptide Mass Fingerprinting]], [[Bottom-Up Proteomics]]).

## Mastery checklist

- [ ] 1 Recognized: I can draw a peptide bond between two amino acids and name the N- and C-termini.
- [ ] 2 Understood: I can explain the condensation, the kinetic stability, planarity through resonance, and the trans preference.
- [ ] 3 Practiced: I can count bonds and waters, compute ω, φ and ψ from coordinates, and simulate a tryptic digest in Python.
- [ ] 4 Applied: I measured backbone torsion angles on a real structure from the PDB and found its cis peptide bonds, if any.
- [ ] 5 Explained: I can teach why only φ and ψ are free, why X–Pro bonds are special, and how the N → C convention links genes, ribosomes and files.

## References

[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of primary structure: formation of the peptide bond, equilibrium and kinetic stability, the N → C convention, planarity, bond lengths, trans and cis forms (X–Pro), torsion angles φ and ψ, and the specificity of trypsin.
[^mcmurry]: [[Organic Chemistry (OpenStax)]], ch. 26 "Biomolecules: Amino Acids, Peptides, and Proteins" (peptides as amides, amide resonance).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), table of properties of the common amino acids (molecular weights).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of translation (peptidyl transfer on the ribosome, growth of the chain from N- to C-terminus).
[^os3]: [[Biology 2e (OpenStax)]], Unit 1, chapter "Biological Macromolecules" (dehydration synthesis; peptide bonds).
