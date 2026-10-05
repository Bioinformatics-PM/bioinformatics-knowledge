---
aliases:
  - Levels of Protein Structure
  - Primary Structure
  - Structure des protéines
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Protein]]"
  - "[[Amino Acid]]"
  - "[[Peptide Bond]]"
  - "[[Hydrophobic Effect]]"
  - "[[Hydrogen Bond]]"
related:
  - "[[Protein Secondary Structure]]"
  - "[[Protein Tertiary Structure]]"
  - "[[Protein Quaternary Structure]]"
  - "[[Protein Folding]]"
  - "[[Protein Domain]]"
  - "[[Ramachandran Plot]]"
  - "[[Secondary Structure Assignment]]"
  - "[[Secondary Structure Prediction]]"
  - "[[Contact Map]]"
  - "[[Protein Structure Prediction]]"
  - "[[PDB Format]]"
  - "[[Structural Bioinformatics]]"
  - "[[Missense Mutation]]"
projects: []
sources:
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[MIT 5.07SC - Biological Chemistry I]]"
  - "[[RCSB Protein Data Bank]]"
  - "[[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]]"
  - "[[AlphaFold Protein Structure Database]]"
---

# Protein Structure

> [!abstract]
> A protein's structure is described at four levels: the order of its amino acids (primary), the local helices and sheets of its backbone (secondary), the 3D fold of the whole chain (tertiary), and the packing of several chains together (quaternary).

## Definition

**Protein structure** is described as a hierarchy of four levels:[^berg][^lehninger][^os3][^507]

1. **Primary**: the amino acid sequence of the polypeptide chain(s), including the positions of any disulfide bonds.[^lehninger]
2. **Secondary**: the local, regular conformations of the backbone, mainly the α helix and the β sheet, stabilized by hydrogen bonds between backbone groups.
3. **Tertiary**: the three-dimensional arrangement of all atoms of one chain, side chains included.
4. **Quaternary**: the spatial arrangement of several chains (subunits) in a multi-subunit protein.

## Why it matters

- **Each level has its data type and its tools.** Primary: sequences and [[Sequence Alignment|alignments]]. Secondary: per-residue states assigned from coordinates ([[Secondary Structure Assignment]]) or predicted from sequence ([[Secondary Structure Prediction]]). Tertiary and quaternary: atomic coordinates in the PDB ([[PDB Format]]).[^pdb]
- **Prediction.** AlphaFold 2 predicts the tertiary structure of single chains with high accuracy from sequence and multiple sequence alignments; its database covers over 214 million sequences ([[Protein Structure Prediction]]).[^jumper][^afdb]
- **Function and variants.** Function lives in the fold (an active site, a binding surface), so the effect of a [[Missense Mutation]] depends on where the residue sits: buried, on the surface, in an interface between subunits.
- **Homology beyond sequence.** Structure is more conserved than sequence during evolution, which lets [[Structural Alignment]] detect relationships that sequence comparison misses.[^berg]

## Core (L1)

![[protein-structure-levels.svg]]

| Level | Describes | Stabilized by | Example |
|---|---|---|---|
| Primary | order of residues, N → C | covalent [[Peptide Bond\|peptide bonds]] (and disulfide bonds)[^lehninger] | the β-globin sequence |
| Secondary | local backbone patterns | hydrogen bonds between backbone C=O and N–H[^berg] | α helix, β sheet, turns |
| Tertiary | fold of one chain | [[Hydrophobic Effect\|hydrophobic effect]], hydrogen bonds, ionic interactions (salt bridges), van der Waals contacts, disulfide bonds[^os3][^berg] | myoglobin |
| Quaternary | assembly of chains | the same noncovalent interactions between subunits (sometimes disulfides)[^os3][^berg] | hemoglobin, α₂β₂ |

**The α helix.** The backbone coils into a right-handed spiral in which the C=O of residue $i$ is hydrogen-bonded to the N–H of residue $i + 4$. There are 3.6 residues per turn, a rise of 1.5 Å per residue, hence a pitch of 5.4 Å; the side chains point outward.[^berg]

**The β sheet.** Nearly extended chains (β strands, 3.5 Å per residue) lie side by side and are hydrogen-bonded to each other; neighbouring strands can run in the same direction (parallel) or in opposite directions (antiparallel).[^berg] **Turns and loops** reverse the direction of the chain, usually at the protein surface.[^berg]

**Tertiary structure.** Myoglobin, the first protein structure solved at atomic detail (Kendrew), is a single chain of 153 residues, about 70 % of it in α helices; its interior consists almost entirely of nonpolar residues, while polar and charged residues face the water.[^berg] This "oily core, polar surface" pattern is the signature of the [[Hydrophobic Effect]] in water-soluble proteins.

**Quaternary structure.** Hemoglobin is made of two α and two β subunits, each folded much like myoglobin.[^berg] A single-chain protein has no quaternary level.

**The rule that ties them.** The primary structure determines the others: an unfolded chain can refold to its native structure without help, given the right conditions (Anfinsen; [[Protein Folding]]).[^berg]

## Deeper (L2)

**Why secondary structures exist.** Because the [[Peptide Bond|peptide unit]] is planar, the backbone has two free angles per residue, φ and ψ; the α helix and the β strand are the regular conformations that satisfy steric constraints while saturating backbone hydrogen bonds ([[Ramachandran Plot]], [[Protein Secondary Structure]]).[^berg]

**Residue preferences.** Some residues favor helices (Ala, Glu, Leu, Met), others strands (Val, Ile and other β-branched or aromatic residues); Pro and Gly are common in turns, and Pro disrupts helices because it lacks an N–H and is rigid.[^berg] These preferences are tendencies, the basis of the first sequence-based prediction methods ([[Secondary Structure Prediction]]).

**Between secondary and tertiary.** Recurring combinations of secondary elements form **motifs** (supersecondary structures, such as a helix-turn-helix); many proteins are built from **domains**, compact regions that fold on their own and often carry a distinct function ([[Protein Domain]], [[Protein Tertiary Structure]]).[^berg]

**Strengths of the stabilizing forces.** Covalent disulfide bonds aside, each interaction is weak; a fold is stable because many of them act together, with the hydrophobic effect as the main driving force ([[Protein Folding]]).[^berg]

**How structures are determined.** Atomic structures have come mainly from X-ray crystallography and NMR spectroscopy ([[X-ray Crystallography]]; see also [[Cryo-Electron Microscopy]]).[^berg] In each PDB entry, read the experimental method and the resolution before trusting atomic details.[^pdb]

## Advanced (L3)

**Representing a structure.** Tertiary structure is a set of 3D coordinates; for most analyses the Cα trace suffices. Coordinates change under rotation and translation, distances do not: a **distance matrix** or a thresholded **contact map** describes the fold independently of its orientation ([[Contact Map]], [[Distance Matrix]]). Comparing two structures requires superposing them first ([[Kabsch Algorithm]], [[Root-Mean-Square Deviation]]).

**Prediction changed the field.** AlphaFold 2, validated in the blind CASP14 assessment, combines multiple sequence alignments and templates with a network that outputs atomic coordinates and a per-residue confidence.[^jumper] A predicted model is not an experiment: low-confidence regions should be treated as unknown, and the 2021 method addresses single chains, not assemblies.[^jumper][^afdb] RCSB.org shows experimental structures and computed models side by side, so always check which one you are looking at.[^pdb]

**Structure is dynamic.** The four levels describe an average structure. Proteins move: hemoglobin changes its quaternary structure when it binds O₂ ([[Allosteric Regulation]]),[^berg] and some proteins or segments have no fixed structure at all ([[Intrinsically Disordered Region]]).[^lehninger] A static structure is a snapshot of an ensemble ([[Free Energy Landscape]]).

## Mathematical representation

- **Primary.** $s = s_1 \dots s_n \in \mathcal{A}^n$, written N → C, plus a set of disulfide pairs $D \subseteq \{(i, j) : i < j,\ s_i = s_j = \mathrm{C}\}$.
- **Secondary.** A string $\sigma \in \{H, E, C\}^n$ aligned with $s$ (helix, strand, other). Fractions $f_X = \#_X(\sigma)/n$; segments are the maximal runs of one state.
- **Ideal helix geometry.** Residue $k$ of an ideal α helix sits at angle $\theta_k = k \cdot 360°/3.6 = 100°\,k$ around the axis and height $z_k = 1.5\,k$ Å.[^berg] A helix of $L$ residues is $1.5L$ Å long; a strand of $L$ residues about $3.5L$ Å.
- **Tertiary.** Coordinates $X = (x_1, \dots, x_n) \in \mathbb{R}^{n \times 3}$ (one point per residue for a Cα trace). Distance matrix $d_{ij} = \lVert x_i - x_j \rVert$ and contact map $C_{ij} = \mathbf{1}[d_{ij} < \delta]$ for a threshold $\delta$ (8 Å below). For any rotation $R$ and translation $t$, $\lVert (Rx_i + t) - (Rx_j + t) \rVert = \lVert x_i - x_j \rVert$: $d$ and $C$ are invariant.
- **Quaternary.** A set of chains with stoichiometry, e.g. $\{(\alpha, 2), (\beta, 2)\}$, and their relative positions.

## Computational representation

Each level maps to a data structure: a string (primary), a string of states of the same length (secondary), an array of coordinates (tertiary), a list of chains (quaternary). The sketch builds toy Cα traces with the ideal geometry above (the helix radius of 2.3 Å is a toy parameter), computes distances and contacts, and segments a secondary structure string.

```python
import math
from itertools import groupby

Coord = tuple[float, float, float]


def ideal_helix(n: int, radius: float = 2.3, rise: float = 1.5, turn: float = 100.0) -> list[Coord]:
    """Toy Cα trace of an α helix: residue k at angle k*turn degrees and height k*rise Å."""
    return [(radius * math.cos(math.radians(turn * k)), radius * math.sin(math.radians(turn * k)), rise * k)
            for k in range(n)]


def ideal_strand(n: int, step: float = 3.5) -> list[Coord]:
    """Toy Cα trace of a fully extended β strand: 3.5 Å per residue along x."""
    return [(step * k, 0.0, 0.0) for k in range(n)]


def distance_matrix(xyz: list[Coord]) -> list[list[float]]:
    return [[math.dist(a, b) for b in xyz] for a in xyz]


def contacts(xyz: list[Coord], cutoff: float = 8.0, min_sep: int = 3) -> int:
    """Number of residue pairs closer than cutoff, at least min_sep apart in sequence."""
    d = distance_matrix(xyz)
    n = len(xyz)
    return sum(d[i][j] < cutoff for i in range(n) for j in range(i + min_sep, n))


def rotate_z(xyz: list[Coord], degrees: float) -> list[Coord]:
    c, s = math.cos(math.radians(degrees)), math.sin(math.radians(degrees))
    return [(c * x - s * y, s * x + c * y, z) for x, y, z in xyz]


def segments(ss: str) -> list[tuple[str, int, int]]:
    """Run-length encode a secondary structure string: (state, start, end), 1-based inclusive."""
    out, pos = [], 1
    for state, run in groupby(ss):
        length = len(list(run))
        out.append((state, pos, pos + length - 1))
        pos += length
    return out


helix, strand = ideal_helix(12), ideal_strand(12)
d = distance_matrix(helix)
print("helix d(i, i+k):", [round(d[0][k], 1) for k in range(1, 7)])
print("contacts |i-j|>=3:", "helix", contacts(helix), "strand", contacts(strand))
moved = rotate_z(helix, 37.0)
print("distances unchanged by rotation:",
      max(abs(a - b) for r1, r2 in zip(d, distance_matrix(moved)) for a, b in zip(r1, r2)) < 1e-9)

ss = "CCHHHHHHHHHHHHHHCCEEEEEECCEEEEEECC"   # invented 3-state assignment
print([s for s in segments(ss) if s[0] != "C"])
print({state: round(ss.count(state) / len(ss), 2) for state in "HEC"})
```

```text
helix d(i, i+k): [3.8, 5.4, 5.1, 6.2, 8.7, 9.8]
contacts |i-j|>=3: helix 17 strand 0
distances unchanged by rotation: True
[('H', 3, 16), ('E', 19, 24), ('E', 27, 32)]
{'H': 0.41, 'E': 0.35, 'C': 0.24}
```

In the helix, residue $i + 3$ and $i + 4$ come back close to residue $i$ (5.1 and 6.2 Å): the geometry behind the $i \to i + 4$ hydrogen bonds, and the band next to the diagonal that marks helices in a contact map. An isolated strand has no such contacts; β sheets show up as contacts between strands far apart in sequence.

## Worked example

> [!example] Sickle-cell hemoglobin across the four levels
> 1. **Primary.** In sickle-cell hemoglobin, the glutamate at position 6 of the β chain is replaced by valine (classical numbering; written p.Glu7Val in HGVS, see [[Missense Mutation]]).[^berg]
> 2. **Secondary and tertiary.** Each β chain still folds into its normal globin fold: the change is one surface residue, charged replaced by nonpolar.[^berg]
> 3. **Quaternary and beyond.** The new nonpolar patch on the surface of deoxygenated hemoglobin S sticks to a complementary site on another tetramer, and the tetramers polymerize into long fibers that deform red blood cells.[^berg]
> 4. **Lesson.** One change at the primary level acts through the hydrophobic effect at an *intermolecular* surface. Predicting it requires knowing where the residue sits in the 3D and assembled structure, not just the substitution.

## Common misconceptions

> [!warning] "Secondary structure is held by side-chain interactions"
> α helices and β sheets are defined by hydrogen bonds between **backbone** C=O and N–H groups; side chains influence which structure forms, but do not define it.[^berg]

> [!warning] "Hydrogen bonds are the main driving force of folding"
> The unfolded chain already makes hydrogen bonds with water. Burying nonpolar side chains (the hydrophobic effect) is the main driving force; hydrogen bonds and salt bridges then select the specific structure ([[Hydrophobic Effect]]).[^berg]

> [!warning] "Every protein has four levels of structure"
> Quaternary structure exists only for proteins made of several chains, such as hemoglobin; myoglobin, a single chain, has none. Intrinsically disordered segments lack a stable tertiary structure.[^berg][^lehninger]

> [!warning] "A PDB structure or an AlphaFold model is the structure"
> An experimental entry is a model fitted to data at a given resolution; a prediction is a model with confidence values. Both are snapshots of a molecule that moves.[^pdb][^jumper]

## Exercises

> [!question] Exercise 1 (L1)
> Match each statement to a level: (a) Cys 32 and Cys 95 are disulfide-bonded; (b) residues 10 to 25 form an α helix; (c) the protein is a dimer of identical chains; (d) Leu 48 is buried next to Phe 112; (e) the sequence starts with MKT.

> [!success]- Solution
> (a) Primary (covalent; Lehninger counts disulfide positions in the primary structure),[^lehninger] although the bond also stabilizes the tertiary fold. (b) Secondary. (c) Quaternary. (d) Tertiary (long-range packing of side chains). (e) Primary.

> [!question] Exercise 2 (L1)
> A transmembrane segment is often an α helix of about 20 residues ([[Cell Membrane]]). How long is it along its axis, how many turns does it make, and how long would the same 20 residues be as an extended β strand?

> [!success]- Solution
> Helix: $20 \times 1.5 = 30$ Å, $20 / 3.6 \approx 5.6$ turns. Strand: $20 \times 3.5 = 70$ Å. The helix packs the same residues into less than half the length.

> [!question] Exercise 3 (L2, Python)
> Using `segments` from the code above, list the helices of the invented assignment `CHHHHCCHHHHHHHHHCCEEEECHHHC` and report the longest one. Is the 3-residue "helix" plausible?

> [!success]- Solution
> ```python
> ss2 = "CHHHHCCHHHHHHHHHCCEEEECHHHC"
> helices = [s for s in segments(ss2) if s[0] == "H"]
> print(helices, max(helices, key=lambda s: s[2] - s[1]))
> # [('H', 2, 5), ('H', 8, 16), ('H', 24, 26)] ('H', 8, 16)
> ```
> The longest helix is residues 8 to 16. The segment 24 to 26 has 3 residues, less than one turn (3.6 residues): an $i \to i + 4$ hydrogen bond spans 5 residues, so this segment cannot contain a single one. Such fragments in a per-residue prediction deserve suspicion ([[Secondary Structure Prediction]]).

> [!question] Exercise 4 (L3, Python)
> Using `ideal_helix`, `distance_matrix` and `contacts`, explain why contacts at sequence separation 3 and 4 appear in a helix but not at 5, with the 8 Å cutoff. Then explain why predicting distances or contacts, rather than coordinates, is convenient for a learning method.

> [!success]- Solution
> The printed distances are 5.1 Å ($i + 3$), 6.2 Å ($i + 4$) and 8.7 Å ($i + 5$): each residue turns 100° and rises 1.5 Å, so residues 3 to 4 apart come back to the same side of the helix and are close, while at 5 apart the rise (7.5 Å) alone almost reaches the cutoff. Distances and contacts do not change when the molecule is rotated or translated (the code checks it), so a method predicting them needs no arbitrary reference frame; coordinates can then be rebuilt from them, up to a mirror image ([[Contact Map]]).

> [!question] Exercise 5 (L3)
> You download the AlphaFold model of a human protein that is known to work as an α₂β₂ tetramer. Which levels of structure does the model describe reliably, what do low-confidence regions mean, and where would you look for the assembly?

> [!success]- Solution
> The model covers one chain: secondary and tertiary structure, with per-residue confidence.[^jumper] Low-confidence regions are unknown (often flexible or disordered), not structures to interpret.[^afdb] The 2021 method does not model the α₂β₂ assembly; look for an experimental structure of the complex in the PDB (check method and resolution), or a model from a method built for complexes.[^pdb][^jumper]

## Mastery checklist

- [ ] 1 Recognized: I can name the four levels and give an example of each.
- [ ] 2 Understood: I can explain which interactions stabilize each level and why the primary structure determines the others.
- [ ] 3 Practiced: I can compute helix and strand lengths, segment secondary structure strings, and build distance matrices and contact maps in Python.
- [ ] 4 Applied: I opened a real structure (e.g. hemoglobin) in the PDB, identified its chains, helices and buried residues, and compared it with its AlphaFold model.
- [ ] 5 Explained: I can teach how a single primary-structure change propagates to higher levels, and the limits of experimental and predicted structures.

## References

[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein structure: levels, α helix and β sheet geometry, turns, residue preferences, motifs and domains, myoglobin and hemoglobin, sickle-cell hemoglobin, Anfinsen's experiments, X-ray crystallography and NMR, and conservation of structure in evolution.
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of the levels of protein structure (primary structure including disulfide bonds) and of intrinsically disordered proteins.
[^507]: [[MIT 5.07SC - Biological Chemistry I]], module on the building blocks of the cell and protein structure.
[^os3]: [[Biology 2e (OpenStax)]], Unit 1, chapter "Biological Macromolecules", section on protein structure (interactions stabilizing tertiary and quaternary structure).
[^pdb]: [[RCSB Protein Data Bank]], experimental structures and computed structure models on RCSB.org; experimental method and resolution of each entry.
[^jumper]: [[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]], *Nature* 596:583-589.
[^afdb]: [[AlphaFold Protein Structure Database]], Varadi M et al., *Nucleic Acids Research* 52:D368-D375 (2024).
