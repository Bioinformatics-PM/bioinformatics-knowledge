---
aliases:
  - Hybridization
  - Hybrid Orbital
  - sp3 Hybridization
  - sp2 Hybridization
  - Hybridation des orbitales
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Atomic Orbital]]"
  - "[[Electron Configuration]]"
  - "[[Covalent Bond]]"
  - "[[Lewis Structure]]"
  - "[[Molecular Geometry]]"
related:
  - "[[Molecular Orbital Theory]]"
  - "[[Resonance (Chemistry)]]"
  - "[[Peptide Bond]]"
  - "[[Ramachandran Plot]]"
  - "[[Nucleotide]]"
  - "[[DNA]]"
  - "[[Base Pairing]]"
  - "[[Intermolecular Force]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Watson 1953 - Molecular Structure of Nucleic Acids]]"
  - "[[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]]"
---

# Orbital Hybridization

> [!abstract]
> Hybridization explains why an atom's bonds point to the corners of a tetrahedron, lie flat at 120°, or line up at 180°: the type of hybrid predicts the shape, and the p orbitals left over make the flat, non-rotating double bonds of peptide bonds and DNA bases.

## Definition

**Orbital hybridization** is the valence bond description in which the valence s and p [[Atomic Orbital|atomic orbitals]] of one atom are combined into a set of equivalent **hybrid orbitals** pointing toward the bonded atoms and lone pairs. The number of hybrids equals the number of atomic orbitals combined: s + 3 p gives four **sp3** hybrids (109.5° apart), s + 2 p gives three **sp2** hybrids (120°, in a plane) and leaves one p orbital, s + p gives two **sp** hybrids (180°) and leaves two p orbitals.[^c2e82][^5111]

## Why it matters

- **Flat or tetrahedral.** Building 3D coordinates from a 2D formula, or checking a structure, needs the local geometry of each atom, which the hybridization summarizes ([[Molecular Geometry]]).
- **What can rotate.** Single (σ) bonds rotate, double bonds do not. This sets the degrees of freedom of a molecule: the planar [[Peptide Bond]] leaves two free backbone angles per residue, the coordinates of the [[Ramachandran Plot]].[^berg]
- **Flat rings stack.** The bases of [[DNA]] are rings of sp2 atoms: flat plates that stack along the helix axis, and stacking contributes most of duplex stability.[^watson][^yakovchuk]

## Core (L1)

**Assigning a hybridization**, from a [[Lewis Structure]]:

1. Count the **regions of electron density** around the atom: bonded atoms plus lone pairs (a double or triple bond counts as one region). This is the steric number of [[Molecular Geometry|VSEPR]].
2. Read the hybrid set: 2 regions → sp (linear), 3 → sp2 (trigonal planar), 4 → sp3 (tetrahedral).[^c2e82]
3. Each p orbital left over can overlap side by side with a p orbital of a neighbor to make a **π bond**.

![[orbital-hybridization-sp3-sp2-sp.svg]]

**σ and π bonds.** A σ bond is end-to-end overlap along the internuclear axis; a π bond is side-by-side overlap of two parallel p orbitals, above and below the axis. A double bond is one σ plus one π bond; a triple bond is one σ plus two π bonds.[^c2e83]

**Rotation.** Turning one end of a σ bond keeps the overlap, so σ bonds rotate freely. A π bond needs its two p orbitals parallel: in ethene, C₂H₄, all six atoms lie in one plane, and twisting would destroy the π overlap. Double bonds therefore lock the atoms around them in a plane.[^c2e83]

**Atoms of biomolecules.**

| Atom | Bonded atoms + lone pairs | Hybridization | Local shape |
|---|---|---|---|
| Cα of an amino acid | 4 + 0 | sp3 | tetrahedral |
| O of water | 2 + 2 | sp3 | bent, 104.5°[^c2e82] |
| C of a C=O group (peptide, carboxylate) | 3 + 0 | sp2 | trigonal planar |
| ring C and N of A, C, G, T, U | 3 regions | sp2 | flat ring |
| C of CO₂ | 2 + 0 | sp | linear |

**Bio: flat bases stack.** The rings of the bases are built from sp2 atoms, so each base is planar ([[Nucleotide]]).[^berg] In B-DNA, the flat base pairs are stacked 3.4 Å apart along the axis ([[DNA]]),[^watson] and this stacking, more than the hydrogen bonds of [[Base Pairing]], stabilizes the double helix.[^yakovchuk]

## Deeper (L2)

**The model follows the geometry.** Hybridization describes an observed shape; it does not cause it. The peptide nitrogen has 3 bonded atoms and a lone pair, so step 2 predicts sp3, yet the peptide unit is planar: the lone pair is delocalized into the C=O ([[Resonance (Chemistry)]]), giving the C–N bond partial double-bond character, so the nitrogen is described as sp2.[^berg] The same holds for a ring nitrogen bonded to three atoms, such as N9 of a purine, whose lone pair belongs to the ring's π system, as in pyrrole.[^mcmurry]

**Conjugation.** When sp2 atoms alternate single and double bonds, all their p orbitals are parallel and the π electrons are shared over the whole system, as in benzene; such conjugated systems must be planar.[^c2e83] The conjugated rings of the bases and of Phe, Tyr and Trp are why these groups absorb UV light ([[Molecular Orbital Theory]], [[Spectroscopy]]).

**Bent water.** With 4 regions, water's oxygen is sp3, but its H–O–H angle, 104.5°, is smaller than 109.5°.[^c2e82] In the formula below, a smaller angle means more p character in the O–H bonds, which leaves more s character for the lone pairs.

**Beyond four regions.** Chemistry 2e extends the scheme to sp3d and sp3d2 for 5 and 6 regions;[^c2e82] for C, N and O, the atoms that make the backbones of biomolecules, 2 to 4 regions cover every case.

## Mathematical representation

- An **sp^n hybrid** pointing along the unit vector $\mathbf{e}$ is $h = \dfrac{s + \sqrt{n}\, p_{\mathbf{e}}}{\sqrt{1 + n}}$, where $s$ is the normalized s orbital and $p_{\mathbf{e}}$ the normalized p orbital along $\mathbf{e}$; its **s character** is $\dfrac{1}{1 + n}$ (sp3: 25 %, sp2: 33 %, sp: 50 %).
- Using $\langle s | s \rangle = 1$, $\langle s | p \rangle = 0$ and $\langle p_{\mathbf{e}_1} | p_{\mathbf{e}_2} \rangle = \cos\theta$, two equivalent hybrids at angle $\theta$ are orthogonal when
$$\langle h_1 | h_2 \rangle = \frac{1 + n\cos\theta}{1 + n} = 0 \quad\Longleftrightarrow\quad \cos\theta = -\frac{1}{n}.$$
- $n = 1, 2, 3$ give $\theta = 180°$, $120°$, $109.47°$. Inverted, $n = -1/\cos\theta$: water's 104.5° gives $n \approx 3.99$, about 20 % s character in each O–H hybrid.
- **Torsion angle.** For bonded atoms A-B-C-D, the torsion $\omega \in (-180°, 180°]$ is the angle between the planes ABC and BCD. Rotation about B–C changes $\omega$; a π bond between B and C pins $\omega$ near $0°$ (cis) or $180°$ (trans).
- **Bond counts.** A molecule has one σ bond per bonded pair of atoms and $\sum_{\text{bonds}} (\text{order} - 1)$ π bonds.

## Computational representation

Structure files store coordinates, not hybridizations. Code either predicts the hybridization from connectivity or infers the local shape from angles and torsions:

```python
import math

HYBRID = {2: "sp", 3: "sp2", 4: "sp3"}


def hybridization(sigma_partners: int, lone_pairs: int) -> str:
    """Hybrid set predicted from the steric number (sigma-bonded atoms + lone pairs)."""
    return HYBRID[sigma_partners + lone_pairs]


def hybrid_angle(n: float) -> float:
    """Angle (degrees) between two equivalent sp^n hybrids: cos(theta) = -1/n."""
    return math.degrees(math.acos(-1 / n))


def bond_angle(a, center, b) -> float:
    """Angle a-center-b (degrees) from 3D coordinates."""
    u = [x - c for x, c in zip(a, center)]
    v = [x - c for x, c in zip(b, center)]
    cos = sum(x * y for x, y in zip(u, v)) / (math.dist(a, center) * math.dist(b, center))
    return math.degrees(math.acos(cos))


def torsion(p0, p1, p2, p3) -> float:
    """Dihedral angle (degrees) about the bond p1-p2: 0 = cis (eclipsed), 180 = trans."""
    def sub(a, b): return [x - y for x, y in zip(a, b)]
    def cross(a, b): return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
    def dot(a, b): return sum(x * y for x, y in zip(a, b))
    b0, b1, b2 = sub(p1, p0), sub(p2, p1), sub(p3, p2)
    n1, n2 = cross(b0, b1), cross(b1, b2)
    m = cross(n1, [x / math.sqrt(dot(b1, b1)) for x in b1])
    return math.degrees(math.atan2(dot(m, n2), dot(n1, n2)))


def ring_torsions(ring) -> list[int]:
    """The six torsion angles around a six-membered ring."""
    return [round(torsion(*(ring[(k + j) % 6] for j in range(4)))) for k in range(6)]


atoms = {"alanine C-alpha": (4, 0), "carbonyl C": (3, 0), "carbonyl O": (1, 2),
         "water O": (2, 2), "CO2 carbon": (2, 0), "HCN carbon": (2, 0)}
for name, (sigma, lone) in atoms.items():
    print(f"{name:16s} {hybridization(sigma, lone)}")
print([round(hybrid_angle(n), 2) for n in (1, 2, 3)])

# Toy coordinates in Å (invented): ideal sp3 center, flat hexagon, puckered ring
c, hs = (0, 0, 0), [(0.63, 0.63, 0.63), (0.63, -0.63, -0.63), (-0.63, 0.63, -0.63)]
print(round(bond_angle(hs[0], c, hs[1]), 2))
flat = [(1.39 * math.cos(math.radians(60 * k)), 1.39 * math.sin(math.radians(60 * k)), 0.0) for k in range(6)]
chair = [(x, y, 0.25 * (-1) ** k) for k, (x, y, _) in enumerate(flat)]
print(ring_torsions(flat))
print(ring_torsions(chair))
```

```text
alanine C-alpha  sp3
carbonyl C       sp2
carbonyl O       sp2
water O          sp3
CO2 carbon       sp
HCN carbon       sp
[180.0, 120.0, 109.47]
109.47
[0, 0, 0, 0, 0, 0]
[61, -61, 61, -61, 61, -61]
```

The steric-number rule fails exactly where resonance matters (the peptide N, ring N bonded to a sugar), so real tools also look at neighbors and observed planarity. Torsions are the variables of conformation: all zero for a flat ring, alternating signs for a puckered one.

## Worked example

> [!example] The peptide unit, atom by atom
> Backbone fragment `Cα(i)–C(=O)–N(H)–Cα(i+1)`:
> 1. **Cα(i)**: 4 bonded atoms, no lone pair → sp3, tetrahedral.
> 2. **C**: bonded to Cα, O and N (3 regions) → sp2; its p orbital makes the C=O π bond.
> 3. **O**: 1 bonded atom + 2 lone pairs → sp2 by the rule.
> 4. **N**: the rule says sp3 (3 atoms + 1 lone pair), but resonance makes C–N partly double, so N is sp2 and the six atoms Cα, C, O, N, H, Cα lie in one plane ([[Peptide Bond]]).[^berg]
> 5. **Rotation**: N–Cα (φ) and Cα–C (ψ) are single σ bonds, free to rotate; C–N (ω) is locked near 180° (trans). Two free angles per residue, which is why one 2D plot of (φ, ψ) describes backbone conformation ([[Ramachandran Plot]]).

## Common misconceptions

> [!warning] "An atom first chooses a hybridization, then takes its shape"
> Hybridization is a model fitted to geometry. When the counting rule disagrees with the observed shape, as for the planar peptide nitrogen, the observation wins.[^berg]

> [!warning] "Lone pairs do not count"
> They occupy hybrid orbitals like bonds do. Water has 2 bonds and 2 lone pairs: sp3, bent, not sp and linear.[^c2e82]

> [!warning] "A double bond is two identical bonds"
> It is one σ bond plus one π bond of different shape. The π component is what forbids rotation and forces planarity.[^c2e83]

> [!warning] "DNA bases are held flat by their hydrogen bonds"
> Each base is flat on its own, because its ring atoms are sp2. Hydrogen bonds pair the bases; stacking of the flat pairs contributes more to duplex stability.[^yakovchuk]

## Exercises

> [!question] Exercise 1 (L1)
> Give the hybridization and local shape of: C in CH₄, C in H₂C=O, C in HCN, N in NH₃, O in H₂O. Count the σ and π bonds of H₂C=O and of HCN.

> [!success]- Solution
> CH₄: 4 regions, sp3, tetrahedral. H₂C=O: C has 3 regions, sp2, trigonal planar. HCN: C has 2 regions (H and the triple bond), sp, linear. NH₃: 3 atoms + 1 lone pair = 4, sp3 (trigonal pyramidal). H₂O: 2 + 2 = 4, sp3, bent. Bonds: H₂C=O has 3 σ and 1 π; HCN has 2 σ (C–H, and the σ of C≡N) and 2 π.

> [!question] Exercise 2 (L1)
> Alanine is H₂N–CαH(CH₃)–COOH. Classify its three carbons as sp3 or sp2, and say which of its bonds cannot rotate.

> [!success]- Solution
> Cα and the methyl carbon have 4 bonded atoms: sp3. The carboxyl carbon has 3 regions (Cα, =O, –OH): sp2. Only the C=O double bond is locked; all the single bonds rotate.

> [!question] Exercise 3 (L2)
> With $\cos\theta = -1/n$, find $n$ and the s character for bond angles of 120° and of a hypothetical measured 107°. Why must a planar hexagon of sp2 atoms be strain-free, while a ring of six sp3 atoms puckers?

> [!success]- Solution
> 120°: $n = 2.00$, s character 0.333 (sp2). 107°: $n = -1/\cos 107° = 3.42$, s character $1/4.42 = 0.226$. A regular planar hexagon has internal angles of exactly 120°, the sp2 angle; six atoms that prefer 109.5° cannot close a flat hexagon, so the ring puckers out of the plane to bring its angles near 109.5° (Exercise 4).

> [!question] Exercise 4 (L2, Python)
> Using `ring_torsions` and `bond_angle` from the code above, write `is_planar(ring, tol=10)` (all ring torsions within `tol` degrees of 0). Test it on the toy rings `flat` and `chair`, and print one ring bond angle of each.

> [!success]- Solution
> ```python
> def is_planar(ring, tol: float = 10.0) -> bool:
>     """A ring is flat when every ring torsion is within tol degrees of 0."""
>     return all(abs(t) <= tol for t in ring_torsions(ring))
>
>
> print(is_planar(flat), is_planar(chair))
> print(round(bond_angle(flat[0], flat[1], flat[2]), 1), round(bond_angle(chair[0], chair[1], chair[2]), 1))
> ```
> Output: `True False`, then `120.0 109.2`. The flat ring has sp2 angles; puckering the toy ring by ±0.25 Å brings its angles to about 109°, the sp3 value. The same test, applied to real coordinates of a nucleobase, is a quick sanity check of a structure.

## Mastery checklist

- [ ] 1 Recognized: I can name sp3, sp2 and sp hybrids with their angles (109.5°, 120°, 180°).
- [ ] 2 Understood: I can explain σ versus π bonds and why π bonds block rotation and enforce planarity.
- [ ] 3 Practiced: I can assign the hybridization of every heavy atom of an amino acid or a base, and derive $\cos\theta = -1/n$.
- [ ] 4 Applied: I computed bond angles and torsions from real structure coordinates to check planarity of bases and peptide units.
- [ ] 5 Explained: I can teach why the model fails for the peptide nitrogen, and how flatness of sp2 rings leads to base stacking.

## References

[^c2e82]: [[Chemistry 2e (OpenStax)]], ch. 8 "Advanced Theories of Covalent Bonding", §8.2 "Hybrid Atomic Orbitals".
[^c2e83]: [[Chemistry 2e (OpenStax)]], ch. 8, §8.3 "Multiple Bonds" (σ and π bonds, planar ethene, delocalized π systems).
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], molecular electronic structure and bonding (course description).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of the peptide bond (planarity, partial double-bond character) and of the nucleic acid bases.
[^mcmurry]: [[Organic Chemistry (OpenStax)]], treatment of aromatic heterocycles (the nitrogen lone pair of pyrrole in the aromatic π system).
[^watson]: [[Watson 1953 - Molecular Structure of Nucleic Acids]], *Nature*.
[^yakovchuk]: [[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]], *Nucleic Acids Research*.
