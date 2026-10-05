---
aliases:
  - Stereoisomer
  - Stereoisomerism
  - Configuration (Chemistry)
  - Stéréochimie
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/mathematics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Isomer]]"
  - "[[Molecular Geometry]]"
  - "[[Conformational Analysis]]"
related:
  - "[[Chirality]]"
  - "[[Fischer Projection]]"
  - "[[Cis-Trans Isomerism]]"
  - "[[Diastereomer]]"
  - "[[Enzyme]]"
  - "[[Ligand Binding]]"
  - "[[Drug Target]]"
  - "[[Protein Structure]]"
projects: []
sources:
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[OpenSMILES Specification]]"
---

# Stereochemistry

> [!abstract]
> Stereochemistry is chemistry in three dimensions: two molecules with the same atoms and the same bonds can still differ by how those atoms are arranged in space, and biological molecules, being three-dimensional themselves, tell the difference.

## Definition

**Stereochemistry** studies the three-dimensional arrangement of atoms in molecules and its consequences. **Stereoisomers** have the same molecular formula and the same connectivity but a different spatial arrangement; they are **enantiomers** when they are non-superimposable mirror images of each other and **diastereomers** otherwise.[^os5] The fixed arrangement that distinguishes stereoisomers is a **configuration**: changing it requires breaking bonds, unlike a change of **conformation**.[^os4]

## Why it matters

- **Recognition is three-dimensional.** Enantiomers have the same physical properties but usually different biological properties: receptors are chiral, so only one enantiomer fits, as only a right hand fits a right glove. Racemic fluoxetine is an antidepressant without activity against migraine, while its pure S enantiomer prevents migraine.[^os512]
- **Biology picks one hand.** Proteins are built from L-amino acids, nucleic acids from D-sugars, and the α helix and the DNA double helix are right-handed.[^berg] An enzyme built from L residues is a chiral environment for every substrate ([[Enzyme]], [[Ligand Binding]]).
- **Stereo is easy to lose in data.** SMILES marks configuration with `@`, `@@`, `/` and `\`; a string without them describes every stereoisomer at once.[^osm] Converting between file formats, or drawing without wedges, silently drops this information ([[Molecular Representation]]).
- **Distances do not know handedness.** A structure and its mirror image have identical interatomic distances (proved below), so any method that rebuilds coordinates from distances must fix the hand separately ([[Protein Structure]]).

## Core (L1)

**Configuration versus conformation.** Rotating butane about its central bond changes its conformation ([[Conformational Analysis]]). Exchanging two groups on a carbon that carries four different groups, or turning a cis double bond into a trans one, changes its configuration: a different stereoisomer, separable in principle and stable at room temperature.[^os4][^os5]

**Two families of stereoisomers.**

| Relation | Definition | Biological example |
|---|---|---|
| Enantiomers | non-superimposable mirror images | L- and D-alanine ([[Chirality]]) |
| Diastereomers | stereoisomers that are not mirror images | glucose and galactose; cis and trans double bonds ([[Diastereomer]], [[Cis-Trans Isomerism]]) |

**Showing 3D on paper.** Wedge and dashed bonds on a [[Skeletal Formula]] (toward and away from the viewer); the [[Fischer Projection]] for sugars and amino acids; the Newman projection for conformations; SMILES stereo marks in files; and, in structure files, plain 3D coordinates, from which configuration must be computed.

**Why a site recognizes one enantiomer.** If a binding site contacts a molecule at three points with three different pockets, the molecule's three groups must sit in a specific clockwise order. Its mirror image has the opposite order: it can be turned in the plane, but only two of its groups, or one, can match at a time, and flipping it over would push its fourth group into the site.

![[three-point-binding-enantiomers.svg]]

## Deeper (L2)

**Same in a mirror-symmetric world, different in a chiral one.** Enantiomers have identical melting points, solubilities and spectra in ordinary conditions; they differ only toward something chiral: plane-polarized light, which they rotate by equal angles in opposite directions, or another chiral molecule such as a receptor.[^os5][^os512] A 50:50 mixture of enantiomers is a **racemic** mixture and does not rotate light.[^os5] Diastereomers, in contrast, differ in all their properties, which is why glucose and galactose are distinct sugars in every context.

**Counting stereoisomers.** Each stereocenter or stereogenic double bond doubles the possibilities: $k$ of them give at most $2^k$ stereoisomers, fewer when the molecule has internal symmetry ([[Diastereomer]], [[Carbohydrate]]).

**Homochirality as a design constraint.** Because the cell's catalysts are all built from one hand, an enzyme generally acts on one enantiomer of a chiral substrate.[^berg] Drug discovery therefore asks which enantiomer binds the target, as the fluoxetine example shows ([[Drug Target]]).[^os512]

## Advanced (L3)

- **Proper and improper motions.** Moving a rigid molecule (rotation plus translation) can never turn it into its mirror image; a reflection can. Mathematically, chirality is the absence of any improper symmetry, and the sign of a determinant detects it (Mathematical representation).
- **Mirror ambiguity in structure determination.** Distances, contact maps and distance matrices are invariant under reflection ([[Protein Structure]]). A model rebuilt from them is as likely to be the mirror image: helices would then be left-handed and amino acids D. Choosing the hand is a separate step, using the known handedness of α helices or of Cα atoms.[^berg]
- **Stereo-aware identifiers.** A canonical identifier of a compound can include or omit its stereo layer: "same compound" in a database may mean same constitution or same configuration, a choice to check before merging records ([[Isomer]]).

## Mathematical representation

**Rigid motions.** A rigid motion maps each atom position $x \in \mathbb{R}^3$ to $Qx + t$, with $t$ a translation and $Q$ an orthogonal matrix ($Q^\top Q = I$, so $\det Q = \pm 1$). Rotations have $\det Q = +1$ (proper); reflections have $\det Q = -1$ (improper). Both preserve every distance: $\lVert (Qx + t) - (Qy + t) \rVert = \lVert Q(x - y) \rVert = \lVert x - y \rVert$.

**Signed volume.** For a center $c$ and three substituent positions $p_1, p_2, p_3$, with $u_i = p_i - c$,

$$V = u_1 \cdot (u_2 \times u_3) = \det\,[\,u_1 \; u_2 \; u_3\,].$$

Under a motion, $V \mapsto \det(Q)\, V$: a rotation keeps the sign, a reflection flips it. Exchanging two substituents swaps two columns and also flips the sign. The sign of $V$ for a fixed priority order of the substituents therefore labels the configuration ([[Chirality]] turns it into R or S).

**Chiral object.** An object is chiral when no proper motion maps it onto its mirror image; for a molecule, conformational changes are allowed in that search.

## Computational representation

Configuration is computed from coordinates with the signed volume. The toy center below uses invented, idealized coordinates.

```python
import math
from itertools import combinations

def sub(p, q):
    return tuple(a - b for a, b in zip(p, q))

def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])

def signed_volume(center, p1, p2, p3) -> float:
    """(p1 - c) . ((p2 - c) x (p3 - c)): its sign is the handedness of p1 -> p2 -> p3 around c."""
    a, b, c = sub(p1, center), sub(p2, center), sub(p3, center)
    return sum(x * y for x, y in zip(a, cross(b, c)))

def rotate(p, ax_deg, az_deg):
    """Rotation about x, then about z (a proper rigid motion, determinant +1)."""
    x, y, z = p
    ca, sa = math.cos(math.radians(ax_deg)), math.sin(math.radians(ax_deg))
    y, z = ca * y - sa * z, sa * y + ca * z
    cb, sb = math.cos(math.radians(az_deg)), math.sin(math.radians(az_deg))
    return (cb * x - sb * y, sb * x + cb * y, z)

def mirror(p):
    """Reflection through the yz plane (determinant -1)."""
    return (-p[0], p[1], p[2])

def distances(mol: dict) -> list[float]:
    return [round(math.dist(mol[a], mol[b]), 6) for a, b in combinations(sorted(mol), 2)]

# Toy tetrahedral center (invented coordinates, arbitrary units)
mol = {"C": (0, 0, 0), "N": (1, 1, 1), "COOH": (1, -1, -1), "CH3": (-1, 1, -1), "H": (-1, -1, 1)}
order = ("N", "COOH", "CH3")
turned = {k: rotate(p, 70, 30) for k, p in mol.items()}
image = {k: mirror(p) for k, p in mol.items()}
for name, m in (("molecule", mol), ("rotated", turned), ("mirror image", image)):
    print(f"{name:13} signed volume {signed_volume(m['C'], *(m[g] for g in order)):+.3f}")
print("same distances, molecule vs mirror:", distances(mol) == distances(image))
```

```text
molecule      signed volume +4.000
rotated       signed volume +4.000
mirror image  signed volume -4.000
same distances, molecule vs mirror: True
```

Rotation keeps the sign, reflection flips it, and the ten interatomic distances cannot tell the two hands apart. The same test, applied to the N, C and Cβ atoms around each Cα, checks that a protein model contains only L residues.

## Worked example

> [!example] Same molecule or enantiomer?
> Two drawings show a carbon with groups N, COOH, CH₃ and H. In the second, the COOH and CH₃ positions are exchanged, and the whole drawing is turned by 120°.
> 1. **Turning** is a rotation: it changes nothing ($\det Q = +1$).
> 2. **One exchange** of two groups flips the sign of $V$: the second drawing is the mirror configuration, the enantiomer.
> 3. **A second exchange** (say N with H) would flip it back: an even number of exchanges gives the same molecule, an odd number its enantiomer, the parity rule of [[Permutation|permutations]].
> 4. **Biological reading.** If the first drawing is L-alanine, the second is D-alanine: same formula, same bonds, same distances, but a protein's binding site, built from L residues, sees them differently.[^os512]

## Common misconceptions

> [!warning] "Enantiomers have different physical properties"
> In an achiral environment their melting points, solubilities and spectra are identical; they differ only toward chiral things (polarized light, enzymes, receptors).[^os5]

> [!warning] "Every molecule has a different mirror image"
> Only chiral molecules do. Glycine or ethanol superimpose on their mirror images after a rotation: they have no enantiomer ([[Chirality]]).

> [!warning] "A SMILES or a formula identifies a drug"
> Without stereo marks, `CC(N)C(=O)O` stands for L-alanine, D-alanine and any mixture of them. Compound identity at the level biology cares about needs the configuration.[^osm]

## Exercises

> [!question] Exercise 1 (L1)
> Which are chiral: a hand, a screw, a coffee mug, a sphere, the DNA double helix, glycine, alanine?

> [!success]- Solution
> Chiral: hand, screw, DNA double helix (right-handed[^berg]), alanine (four different groups on Cα). Achiral: coffee mug (a mirror plane through the handle), sphere, glycine (two H on Cα).

> [!question] Exercise 2 (L1)
> Configuration change or conformation change? (a) rotating about the C2–C3 bond of butane; (b) exchanging the H and the OH on a stereocenter; (c) a cyclohexane ring flip; (d) turning a cis C=C into trans.

> [!success]- Solution
> (a) Conformation. (b) Configuration (it makes the enantiomer or a diastereomer, and requires breaking bonds). (c) Conformation (axial and equatorial exchange; up and down faces are kept). (d) Configuration: rotation about a double bond requires breaking the π bond ([[Cis-Trans Isomerism]]).

> [!question] Exercise 3 (L2, Python)
> Using `signed_volume` and the toy `mol`, compute the sign for all 6 orderings of N, COOH and CH₃. Relate the result to permutation parity.

> [!success]- Solution
> ```python
> from itertools import permutations
> for perm in permutations(("N", "COOH", "CH3")):
>     print(perm, "+" if signed_volume(mol["C"], *(mol[g] for g in perm)) > 0 else "-")
> ```
> Output: `('N', 'COOH', 'CH3') +`, `('N', 'CH3', 'COOH') -`, `('COOH', 'N', 'CH3') -`, `('COOH', 'CH3', 'N') +`, `('CH3', 'N', 'COOH') +`, `('CH3', 'COOH', 'N') -`. Even permutations (cyclic shifts) keep the sign, odd ones (one exchange) flip it: the determinant is antisymmetric in its columns. This is why reading the groups "in priority order" matters when assigning R or S.

> [!question] Exercise 4 (L3)
> A method reconstructs a protein's Cα coordinates from a predicted distance matrix and returns two candidate models that are mirror images. Explain why the distances cannot decide, and propose a check that does.

> [!success]- Solution
> Reflection preserves all distances (Mathematical representation), so both models fit the matrix equally well. Handedness must come from outside the distances: α helices in proteins are right-handed,[^berg] so compute the signed volume (or torsion) of four consecutive Cα atoms in a predicted helix. The sign is opposite in the two models; keep the model whose helices are right-handed. With full backbone atoms, the same test applied at each Cα checks that every residue is L.

## Mastery checklist

- [ ] 1 Recognized: I can define stereoisomer, enantiomer, diastereomer, configuration and conformation.
- [ ] 2 Understood: I can explain why chiral receptors distinguish enantiomers while ordinary physical measurements do not.
- [ ] 3 Practiced: I can compute a signed volume, predict the effect of rotations, reflections and substituent exchanges, and read stereo marks in SMILES.
- [ ] 4 Applied: I checked the configuration of ligands or residues in a real structure file, or the stereo marks of compounds in a dataset.
- [ ] 5 Explained: I can explain mirror ambiguity in distance-based structure methods and why identity in databases depends on stereo layers.

## References

[^os4]: [[Organic Chemistry (OpenStax)]], ch. 4 "Organic Compounds: Cycloalkanes and Their Stereochemistry" (stereoisomers; configuration versus conformation).
[^os5]: [[Organic Chemistry (OpenStax)]], ch. 5 "Stereochemistry at Tetrahedral Centers" (enantiomers, diastereomers, optical activity, racemic mixtures).
[^os512]: [[Organic Chemistry (OpenStax)]], ch. 5, section 5.12 "Chirality in Nature and Chiral Environments" (different biological properties of enantiomers, chiral receptors, fluoxetine).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of amino acids (L configuration), carbohydrates (D sugars), protein structure (right-handed α helix), DNA structure (right-handed double helix) and enzyme specificity.
[^osm]: [[OpenSMILES Specification]], stereochemistry (`@`, `@@` for tetrahedral centers; `/`, `\` for double bonds).
