---
aliases:
  - H-bond
  - Hydrogen Bonding
  - Hydrogen-Bond Donor
  - Hydrogen-Bond Acceptor
  - Liaison hydrogène
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Electronegativity]]"
  - "[[Covalent Bond]]"
  - "[[Lewis Structure]]"
  - "[[Intermolecular Force]]"
related:
  - "[[Water]]"
  - "[[Base Pairing]]"
  - "[[DNA]]"
  - "[[Protein Structure]]"
  - "[[Protein Secondary Structure]]"
  - "[[Secondary Structure Assignment]]"
  - "[[Hydrophobic Effect]]"
  - "[[Orbital Hybridization]]"
  - "[[Drug Discovery]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Watson 1953 - Molecular Structure of Nucleic Acids]]"
  - "[[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]]"
  - "[[Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability]]"
---

# Hydrogen Bond

> [!abstract]
> A hydrogen bond is the attraction between a hydrogen atom already bonded to N or O and a lone pair on another N or O. It is weak, short and directional, which makes it the alphabet of molecular recognition: base pairs, helices and sheets are patterns of hydrogen bonds.

## Definition

A **hydrogen bond** D–H···A forms when a hydrogen atom covalently bonded to a very electronegative atom (the **donor** D: N, O or F) is attracted to a lone pair of another N, O or F atom (the **acceptor** A). The D–H bond is so polar that the hydrogen carries a large partial positive charge: a hydrogen bond is an unusually strong dipole-dipole attraction, the strongest [[Intermolecular Force]] between neutral molecules.[^c2e101] In biomolecules the donor and acceptor are N or O, about 0.30 nm apart, and the bond is strongest when the three atoms lie on a straight line.[^alberts]

## Why it matters

- **Recognition rules.** [[Base Pairing]] is a donor-acceptor matching problem: A-T and G-C are the pairs in which every donor faces an acceptor ([[DNA]]).[^berg]
- **Secondary structure.** Helices and sheets are defined by backbone hydrogen-bond patterns; tools that annotate them from coordinates look for those patterns ([[Protein Secondary Structure]], [[Secondary Structure Assignment]]).[^berg]
- **Drug-likeness filters.** Counts of hydrogen-bond donors and acceptors are standard descriptors of small molecules; Lipinski's rule of 5 flags poor absorption above 5 donors or 10 acceptors ([[Drug Discovery]]).[^lipinski]

## Core (L1)

![[hydrogen-bond-geometry.svg]]

**Finding donors and acceptors.** Draw the [[Lewis Structure]]:

1. Each H bonded to N or O is a **donor** H. An H bonded to C is not: C–H is nearly nonpolar ([[Electronegativity]]).[^c2e101]
2. Each lone pair on N or O can **accept**. An O–H group is both donor and acceptor; a C=O oxygen is an acceptor only.
3. A lone pair shared with a neighbouring π system is not available: the peptide N has a lone pair, but it is delocalized into the C=O, so the N–H of a peptide donates and its N does not accept ([[Orbital Hybridization]]).[^berg]

| Group | Donor | Acceptor | Where |
|---|---|---|---|
| O–H | yes | yes | water, Ser, Thr, Tyr, sugars, ribose 2'-OH |
| N–H of amides and aromatic rings | yes | no: lone pair delocalized (rule 3) | backbone, Asn, Gln, Trp, bases |
| –NH₃⁺ (Lys), guanidinium (Arg) | yes | no (no free lone pair) | positive side chains |
| C=O, –COO⁻ | no | yes | backbone, Asp, Glu, bases |
| ring N without H | no | yes | bases (N1 of A, N3 of C), His |

**Geometry and strength.** The donor-acceptor distance is about 0.30 nm, longer than a covalent bond (0.15 nm). Alberts lists 16.7 kJ/mol in vacuum, about 4 % of a covalent bond (377 kJ/mol), and only 4.2 kJ/mol in water, which competes with every donor and acceptor.[^alberts] The interaction is directional: it is strongest when D–H points straight at A and weakens as the D–H···A angle bends (figure).[^alberts]

**Bio: base pairs.** A-T pairs share two hydrogen bonds and G-C pairs three, between donors and acceptors on the facing edges of the bases ([[Base Pairing]]):[^berg] these patterns assume each base in its usual keto form.[^watson]

![[watson-crick-pair-hydrogen-bonds.svg]]

**Bio: helices and sheets.** In the α helix, the C=O of residue $i$ accepts a hydrogen bond from the N–H of residue $i + 4$, with 3.6 residues per turn. In a β sheet, the bonds link the backbones of neighbouring strands, parallel or antiparallel ([[Protein Structure]]).[^berg]

## Deeper (L2)

**Specificity more than stability.** Groups that pair inside a protein or a duplex were hydrogen-bonded to water before, so forming the internal bond is an exchange with a small net gain.[^berg] What a hydrogen bond adds is **selectivity**: a donor left facing a donor, or a buried group left without a partner, costs energy, so only matched partners assemble. In DNA, pairing selects the partner while stacking of the flat base pairs contributes most of the stability ([[DNA#Deeper (L2)]]).[^yakovchuk]

**Directionality builds lattices.** Because each bond points along D–H toward a lone pair, a molecule with two donors and two acceptors arranged tetrahedrally, like water, builds an open three-dimensional network ([[Water]]).

**Ends and edges.** A regular pattern leaves groups unsatisfied at its borders: the first four N–H and the last four C=O of a helix have no partner within it (Worked example), and the outer strands of a sheet expose free donors and acceptors. These are the places where the chain contacts water, side chains or ligands.

## Advanced (L3)

**Hydrogen bonds in data.**

- **From coordinates.** A structure gives positions; a hydrogen bond is a *decision* based on distances and angles (Computational representation). When hydrogen positions are not in the file, tools place them or use the D···A distance alone. Different cut-offs give different counts, so report the criterion with any count.
- **From a formula.** Lipinski's rule counts donors as the sum of OH and NH groups and acceptors as the sum of N and O atoms.[^lipinski] This is deliberately crude: the count ignores delocalized lone pairs (amide N) and treats a water O–H₂ as a single donor group (Computational representation).
- **From a sequence.** A perfect duplex of $n$ base pairs with GC fraction $g$ has $n(2 + g)$ base-pair hydrogen bonds ([[Base Pairing#Deeper (L2)]]); since stacking dominates stability, this count is a poor predictor of melting on its own.[^yakovchuk]

## Mathematical representation

- Positions $\mathbf{d}, \mathbf{h}, \mathbf{a} \in \mathbb{R}^3$ of donor, hydrogen and acceptor. Distance $r_{DA} = \lVert \mathbf{a} - \mathbf{d} \rVert$ and angle
$$\theta = \angle(\mathbf{d}, \mathbf{h}, \mathbf{a}) = \arccos \frac{(\mathbf{d} - \mathbf{h}) \cdot (\mathbf{a} - \mathbf{h})}{\lVert \mathbf{d} - \mathbf{h} \rVert\, \lVert \mathbf{a} - \mathbf{h} \rVert}, \qquad \theta = 180° \text{ for a linear bond.}$$
- A geometric criterion is a predicate $\mathrm{HB}(\mathbf{d}, \mathbf{h}, \mathbf{a}) = [r_{DA} \le r_{\max}] \wedge [\theta \ge \theta_{\min}]$ with chosen cut-offs ($r_{\max} = 3.5$ Å, $\theta_{\min} = 120°$ below: an illustrative convention).
- **Helix pattern.** For a helical segment of residues $1, \dots, n$, the backbone bonds are $\{(i, i+4) : 1 \le i \le n - 4\}$: $n - 4$ bonds, with N–H of residues $1..4$ and C=O of residues $n-3..n$ free. The fraction of satisfied backbone N–H groups is $(n-4)/n$, which approaches 1 only for long helices.

## Computational representation

```python
import math

def angle(a, b, c) -> float:
    """Angle a-b-c in degrees, from 3D coordinates."""
    u = [x - y for x, y in zip(a, b)]
    v = [x - y for x, y in zip(c, b)]
    cos = sum(x * y for x, y in zip(u, v)) / (math.dist(a, b) * math.dist(c, b))
    return math.degrees(math.acos(max(-1.0, min(1.0, cos))))

def is_hbond(donor, hydrogen, acceptor, max_da: float = 3.5, min_angle: float = 120.0):
    """Geometric test (the cut-offs are a convention): D...A distance and D-H...A angle."""
    d, theta = math.dist(donor, acceptor), angle(donor, hydrogen, acceptor)
    return d <= max_da and theta >= min_angle, round(d, 2), round(theta, 1)

def helix_hbonds(first: int, last: int) -> list[tuple[int, int]]:
    """Backbone hydrogen bonds of an ideal alpha helix: C=O of residue i accepts from N-H of i + 4."""
    return [(i, i + 4) for i in range(first, last - 3)]

def lipinski_counts(atoms: list[tuple[str, int]]) -> tuple[int, int]:
    """Crude counts from (element, attached H) pairs: donors = N or O bearing H, acceptors = all N and O."""
    donors = sum(1 for el, h in atoms if el in "NO" and h > 0)
    acceptors = sum(1 for el, _ in atoms if el in "NO")
    return donors, acceptors


# Toy geometries in Å (invented): O-H donor along x, acceptor O at 2.9 Å or 4.0 Å
O_d = (0.0, 0.0, 0.0)
H_lin = (0.96, 0.0, 0.0)
H_bent = (0.96 * math.cos(math.radians(50)), 0.96 * math.sin(math.radians(50)), 0.0)
print("linear   ", is_hbond(O_d, H_lin, (2.9, 0.0, 0.0)))
print("bent     ", is_hbond(O_d, H_bent, (2.9, 0.0, 0.0)))
print("too far  ", is_hbond(O_d, H_lin, (4.0, 0.0, 0.0)))

pairs = helix_hbonds(1, 12)
print(len(pairs), pairs[:3], "...")
print("free N-H:", [r for r in range(1, 13) if r not in {j for _, j in pairs}],
      "free C=O:", [r for r in range(1, 13) if r not in {i for i, _ in pairs}])

molecules = {
    "water": [("O", 2)],
    "glycine (neutral form)": [("N", 2), ("C", 2), ("C", 0), ("O", 0), ("O", 1)],
    "N-methylacetamide": [("C", 3), ("C", 0), ("O", 0), ("N", 1), ("C", 3)],
}
for name, atoms in molecules.items():
    print(f"{name:24s} donors, acceptors = {lipinski_counts(atoms)}")
```

```text
linear    (True, 2.9, 180.0)
bent      (False, 2.9, 112.1)
too far   (False, 4.0, 180.0)
8 [(1, 5), (2, 6), (3, 7)] ...
free N-H: [1, 2, 3, 4] free C=O: [9, 10, 11, 12]
water                    donors, acceptors = (1, 1)
glycine (neutral form)   donors, acceptors = (2, 3)
N-methylacetamide        donors, acceptors = (1, 2)
```

The Lipinski-style counts say water has 1 donor and 1 acceptor, while chemically it has 2 donor hydrogens and 2 lone pairs; for N-methylacetamide (a model peptide unit) they count the amide N as an acceptor. Simple descriptors trade chemistry for speed: know what they count.

## Worked example

> [!example] Backbone hydrogen bonds of a 12-residue helix
> 1. **Pattern**: C=O($i$) ··· H–N($i+4$) for $i = 1, \dots, 8$: 8 bonds, $n - 4$ with $n = 12$.
> 2. **Free groups**: N–H of residues 1-4 and C=O of residues 9-12 have no partner inside the helix (code output). Only $8/12 = 67\%$ of the backbone N–H groups are satisfied, against 95 % for an 80-residue helix.
> 3. **Consequence**: the ends need other partners (side chains, water, ligands), so helix ends are polar spots on a protein. On real coordinates, `is_hbond` on each (N, H of $i+4$; O of $i$) triple flags distorted turns.

## Common misconceptions

> [!warning] "Any hydrogen can form a hydrogen bond"
> Only H bonded to N, O or F carries enough positive charge.[^c2e101] The many C–H groups of a protein or a lipid are not donors.

> [!warning] "A hydrogen bond is a covalent bond to hydrogen"
> The covalent bond is D–H. The hydrogen bond is the extra attraction H···A, about 0.30 nm long and a small fraction of a covalent bond's strength.[^alberts]

> [!warning] "Hydrogen bonds are what fold proteins and hold DNA together"
> They decide which partners and which structure, but the unfolded chain and the separated strands already hydrogen-bond with water. The hydrophobic effect drives folding, and stacking stabilizes the duplex ([[Hydrophobic Effect]], [[DNA]]).[^berg][^yakovchuk]

## Exercises

> [!question] Exercise 1 (L1)
> Count donor hydrogens and acceptor lone pairs on N and O in: H₂O, NH₃, CH₄, H₂C=O, CH₃OH.

> [!success]- Solution
> H₂O: 2 donors, 2 lone pairs. NH₃: 3 donors, 1 lone pair. CH₄: none (C–H). H₂C=O: 0 donors, 2 lone pairs on O. CH₃OH: 1 donor (O–H), 2 lone pairs on O; the C–H are not donors.

> [!question] Exercise 2 (L1)
> At pH 7, classify the side chains of Ser, Asp, Lys, Asn, Leu and Phe as donor, acceptor, both or neither.

> [!success]- Solution
> Ser (–OH): both. Asp (–COO⁻): acceptor. Lys (–NH₃⁺): donor; its N has no free lone pair. Asn (–CONH₂): both, N–H donors and C=O acceptor. Leu and Phe: neither (only C–H).

> [!question] Exercise 3 (L2)
> A helix of 20 residues: how many backbone hydrogen bonds, and what fraction of its N–H groups are satisfied? How long must a helix be for this fraction to exceed 90 %?

> [!success]- Solution
> $20 - 4 = 16$ bonds; $16/20 = 80\%$. $(n-4)/n > 0.9 \iff n > 40$: at least 41 residues. Short helices always carry a large share of unsatisfied ends.

> [!question] Exercise 4 (L2, Python)
> With `is_hbond`, keep the acceptor at 2.9 Å and tilt the O–H away from the O···O axis by 0°, 20°, 40° and 60°. Print the angle, the H···A distance and the verdict.

> [!success]- Solution
> ```python
> for tilt in (0, 20, 40, 60):
>     H = (0.96 * math.cos(math.radians(tilt)), 0.96 * math.sin(math.radians(tilt)), 0.0)
>     ok, d, theta = is_hbond(O_d, H, (2.9, 0.0, 0.0))
>     print(f"tilt {tilt:2d} deg: angle {theta:6.1f}, H...A {math.dist(H, (2.9, 0, 0)):.2f} Å, hbond={ok}")
> ```
> Output: angles 180.0, 150.7, 124.1, 101.0 with H···A 1.94, 2.02, 2.25, 2.56 Å; the verdict turns `False` at 60°. The D···A distance never changed: a distance-only criterion would keep the bent case, which is why angles matter.

> [!question] Exercise 5 (L3)
> Lipinski's counts for N-methylacetamide are 1 donor and 2 acceptors. Which count is chemically wrong, and why might a drug-likeness filter still use it?

> [!success]- Solution
> The amide N is counted as an acceptor, but its lone pair is delocalized into the C=O ([[Orbital Hybridization]]), so only the O accepts.[^berg] The rule counts atoms because that needs no 3D structure or electronic analysis and is fast on millions of compounds; as a coarse filter, its errors are tolerated.[^lipinski]

## Mastery checklist

- [ ] 1 Recognized: I can define D–H···A and name typical donors and acceptors.
- [ ] 2 Understood: I can explain why only H on N, O or F donates, why the bond is directional, and why water weakens it.
- [ ] 3 Practiced: I can list the donors and acceptors of amino acid side chains and bases, and test hydrogen bonds from coordinates in code.
- [ ] 4 Applied: I counted backbone hydrogen bonds in a real protein structure and compared two cut-off conventions.
- [ ] 5 Explained: I can explain why hydrogen bonds give specificity more than stability, in base pairing and in folding.

## References

[^c2e101]: [[Chemistry 2e (OpenStax)]], ch. 10, §10.1 "Intermolecular Forces" (hydrogen bonding: H bonded to F, O or N attracted to a lone pair of F, O or N; an unusually strong dipole-dipole attraction).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of cell chemistry: table of covalent and noncovalent bonds (hydrogen bond length 0.30 nm, strength in vacuum and in water), hydrogen bonds strongest when the three atoms lie in a straight line.
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), §1.3 "Chemical Bonds in Biochemistry" and treatment of the Watson-Crick base pairs, of the peptide bond (delocalized nitrogen lone pair) and of α helix and β sheet hydrogen bonding.
[^watson]: [[Watson 1953 - Molecular Structure of Nucleic Acids]], *Nature* (bases in their keto forms).
[^yakovchuk]: [[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]], *Nucleic Acids Research*.
[^lipinski]: [[Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability]], *Advanced Drug Delivery Reviews* 23:3-25 (rule of 5: donors as the sum of OHs and NHs, acceptors as the sum of Ns and Os).
