---
aliases:
  - Quaternary Structure
  - Protein Complex
  - Oligomer
  - Subunit Assembly
  - Structure quaternaire des protéines
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Protein Structure]]"
  - "[[Protein Tertiary Structure]]"
  - "[[Hydrophobic Effect]]"
related:
  - "[[Cooperativity]]"
  - "[[Allosteric Regulation]]"
  - "[[Ligand Binding]]"
  - "[[PDB Format]]"
  - "[[Molecular Visualization]]"
  - "[[Protein Structure Prediction]]"
  - "[[AlphaFold]]"
  - "[[Protein-Protein Interaction Network]]"
  - "[[Missense Mutation]]"
projects: []
sources:
  - "[[Biochemistry (Berg)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[RCSB Protein Data Bank]]"
  - "[[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]]"
---

# Protein Quaternary Structure

> [!abstract]
> Quaternary structure is the way several folded chains pack into one working protein: which subunits, how many of each, and how they are arranged, most often symmetrically.

## Definition

**Quaternary structure** is the spatial arrangement of the subunits of a protein made of more than one polypeptide chain, and the nature of their contacts.[^berg] Identical subunits make a **homo-oligomer** (a dimer of identical chains, written $\alpha_2$); different subunits make a **hetero-oligomer**, described by its **stoichiometry** (hemoglobin is $\alpha_2\beta_2$).[^berg] A protein made of a single chain, such as myoglobin, has no quaternary structure ([[Protein Structure]]).

## Why it matters

- **Function can exist only in the assembly.** Subtle changes in the arrangement of its four subunits let hemoglobin carry oxygen from the lungs to the tissues with great efficiency ([[Cooperativity]], [[Allosteric Regulation]]).[^berg]
- **PDB files need care.** The coordinate file of a crystal structure usually holds one asymmetric unit, which may or may not be the biological assembly; interfaces must be analyzed on the assembly ([[PDB Format]]).[^pdb]
- **Prediction.** AlphaFold 2 (2021) predicts single chains;[^jumper] an assembly needs a method built for complexes ([[AlphaFold]], [[Protein Structure Prediction]]).
- **Interfaces carry variants.** A residue buried between two subunits looks exposed in a single-chain model, so the effect of a [[Missense Mutation]] at an interface is easy to misread (Worked example).

## Core (L2)

![[quaternary-symmetry-assemblies.svg]]

### Subunits, stoichiometry, interfaces

- The simplest case is a dimer of identical subunits, such as the DNA-binding protein Cro of phage λ.[^berg]
- Human hemoglobin has two α and two β subunits: an $\alpha_2\beta_2$ tetramer, more precisely a pair of αβ dimers.[^berg] Each subunit folds much like myoglobin ([[Protein Tertiary Structure]]).
- Viruses reuse one kind of subunit in symmetric arrays: the coat of rhinovirus, the common-cold virus, holds 60 copies of each of four subunits in a nearly spherical shell.[^berg]

Subunits stick together with the forces that build a fold, buried nonpolar surface first, then hydrogen bonds and ion pairs, and sometimes disulfide bonds ([[Hydrophobic Effect]], [[Protein Tertiary Structure#What holds a fold together]]).[^berg]

### Why build from subunits

Building large structures from repeated subunits needs little genetic information; assembly and disassembly can be controlled, because subunits are held by many weak bonds; and malformed subunits can be excluded during assembly.[^alberts][^berg] Contacts between subunits also let the binding of a ligand to one subunit change its neighbours, as in hemoglobin ([[Cooperativity]]).[^berg]

The geometry of the binding sites decides the shape. A subunit whose binding site is complementary to the same site on a partner forms a symmetric dimer. A subunit with two different sites that bind each other head-to-tail forms a helical filament, or a closed ring when the sites are suitably oriented; larger closed shells, such as virus capsids, follow the same logic.[^alberts]

### Symmetry

Subunits of one kind usually sit in equivalent environments, related by rotations. Proteins are built from L-amino acids,[^berg] so an assembly cannot contain a subunit and its mirror image: only rotations (and screw motions along filaments) are possible symmetries.

| Symmetry | Operations | Copies of one subunit | Example |
|---|---|---|---|
| Cyclic $C_n$ | rotations by $360°/n$ about one axis | $n$ | dimer ($C_2$), rings |
| Dihedral $D_n$ | one $n$-fold axis and $n$ perpendicular 2-fold axes | $2n$ | $D_2$ tetramers |
| Icosahedral | 6 five-fold, 10 three-fold and 15 two-fold axes | 60 | virus shells: 60 copies of each of rhinovirus's four coat proteins[^berg] |

In hemoglobin, one exact 2-fold axis exchanges the two αβ dimers; because α and β fold alike, the tetramer also looks approximately like a $D_2$ assembly (pseudo-symmetry).[^berg] Two kinds of interfaces follow from the geometry (Computational representation): a 2-fold axis makes a **self-complementary** interface, the same surface patch on both partners; a ring of 3 or more makes **head-to-tail** interfaces, patch A of one subunit against patch B of the next.

### Biological assemblies in PDB entries

The **asymmetric unit** is the smallest part of a crystal from which the symmetry operations generate the whole unit cell. The primary coordinate file of a crystal structure typically contains one asymmetric unit, which may or may not be the **biological assembly**, the functional form of the molecule. Hemoglobin acts as a tetramer, yet some entries deposit only 2 chains (half a tetramer) and others 8 or more (several tetramers). For icosahedral viruses, usually one chain is deposited and the 60 copies of the capsid are generated. The entry stores the symmetry operations that build each assembly, and assembly coordinates can be downloaded directly.[^pdb]

## Advanced (L3)

**Quaternary change is function.** When hemoglobin binds oxygen, its two αβ dimers rotate by about 15° relative to each other.[^berg] Treating each dimer as rigid, the contacts inside a dimer ($\alpha_1\beta_1$) are preserved while the contacts between dimers ($\alpha_1\beta_2$) are remade: the switch between low- and high-affinity states is written in an interface. This is the structural basis of [[Cooperativity]] and of the concerted model of [[Allosteric Regulation]].

**An interface in a crystal is a hypothesis.** The symmetry operations of a crystal pack each molecule against its lattice neighbours,[^pdb] so a contact seen in a file does not by itself prove a biological interface. Check the assembly annotated in the entry, then look for independent evidence: the same interface in other crystal forms, solution measurements, conservation of the interface residues.

**Symmetry as compression.** An assembly with symmetry group $G$ is fully described by one subunit and $|G|$ operations, which is how a capsid can be deposited as one chain.[^pdb] Predicting complexes is a frontier of structure prediction: the 2021 AlphaFold method was designed and assessed for single chains,[^jumper] and methods for complexes are covered in [[AlphaFold]]. Assemblies seen in structures are the high-resolution end of interaction data, whose large-scale, lower-resolution side is the [[Protein-Protein Interaction Network]].

## Mathematical representation

- **Assembly.** A set of chains $c$, each with an entity label $e(c)$ (chains with identical sequences share an entity) and coordinates $X_c$. The stoichiometry is the multiset of entity counts, e.g. $\{\alpha: 2, \beta: 2\}$.
- **Symmetry.** A finite group $G$ of rotations such that, for every $g \in G$ and every chain $c$, $g(X_c) = X_{c'}$ for some chain $c'$ of the same entity: each $g$ permutes the chains. Rotation about $z$: $R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}$, and $C_n = \{R_z(360°k/n) : k = 0, \dots, n - 1\}$, with $R_z(360°/n)^n = I$. The group orders are $|C_n| = n$, $|D_n| = 2n$, and 12, 24 and 60 for the tetrahedral, octahedral and icosahedral groups: the number of equivalent positions for one kind of subunit.
- **Interfaces.** If $g$ has order 2 and chains $c$ and $g(c)$ touch, $g$ maps the interface onto itself: the contact patch on $c$ equals the image of the patch on $g(c)$ (self-complementary). For $g$ of order $n \ge 3$ in a ring, the patch of $c$ facing $g(c)$ differs from the patch facing $g^{-1}(c)$ (head-to-tail).
- **Interface types.** Unordered chain pairs are grouped into orbits under $G$; each orbit is one interface type, which is why an $\alpha_2\beta_2$ tetramer with one 2-fold has 6 chain pairs but only 4 types (Exercise 4).

## Computational representation

The code groups chains into entities to write a stoichiometry, then builds toy rings (one subunit, an arc of points, and its rotated copies), checks which rotations are symmetries and classifies the interfaces by comparing the contact positions on both sides.

```python
import math
from collections import Counter
from itertools import combinations


def stoichiometry(chains: dict[str, str]) -> str:
    """Group chains with identical sequences into entities, most copies first: e.g. 'A2B2'."""
    counts = Counter(chains.values()).most_common()
    return "".join(f"{chr(65 + i)}{n if n > 1 else ''}" for i, (_, n) in enumerate(counts))


CHAINS = {"A": "GSKLVEELKK", "B": "PDTRAQWNEV", "C": "GSKLVEELKK", "D": "PDTRAQWNEV"}  # invented
print("stoichiometry:", stoichiometry(CHAINS), "| homodimer:", stoichiometry({"A": "MKV", "B": "MKV"}))


def rot_z(deg: float):
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return lambda p: (c * p[0] - s * p[1], s * p[0] + c * p[1], p[2])


def cyclic_assembly(n: int, r: float = 8.0, points: int = 5) -> list[list[tuple]]:
    """Toy Cn ring: one subunit (an arc of points) and its n - 1 rotated copies about z."""
    half = 180 / n - 10                       # each subunit spans a wedge 20° narrower than 360°/n
    angles = [-half + 2 * half * i / (points - 1) for i in range(points)]
    subunit = [(r * math.cos(math.radians(a)), r * math.sin(math.radians(a)), 0.0) for a in angles]
    return [[rot_z(360 * k / n)(p) for p in subunit] for k in range(n)]


def is_symmetric(assembly: list[list[tuple]], op, tol: float = 1e-6) -> bool:
    """True if the operation maps every point onto a point of the assembly."""
    pts = [p for s in assembly for p in s]
    return all(any(math.dist(op(p), q) < tol for q in pts) for p in pts)


def interfaces(assembly: list[list[tuple]], cutoff: float = 4.0) -> dict:
    """Touching subunit pairs, with the contact positions on each side."""
    out = {}
    for i, j in combinations(range(len(assembly)), 2):
        a = sorted({u for u, p in enumerate(assembly[i]) for q in assembly[j] if math.dist(p, q) < cutoff})
        b = sorted({v for v, q in enumerate(assembly[j]) for p in assembly[i] if math.dist(p, q) < cutoff})
        if a:
            out[(i, j)] = (a, b, "self-complementary" if a == b else "head-to-tail")
    return out


for n in (2, 3):
    ring = cyclic_assembly(n)
    print(f"C{n}: {360 / n:.0f}° rotation symmetric {is_symmetric(ring, rot_z(360 / n))}, "
          f"{180 / n:.0f}° {is_symmetric(ring, rot_z(180 / n))}; interfaces {interfaces(ring)}")
```

```text
stoichiometry: A2B2 | homodimer: A2
C2: 180° rotation symmetric True, 90° False; interfaces {(0, 1): ([0, 4], [0, 4], 'self-complementary')}
C3: 120° rotation symmetric True, 60° False; interfaces {(0, 1): ([4], [0], 'head-to-tail'), (0, 2): ([0], [4], 'head-to-tail'), (1, 2): ([4], [0], 'head-to-tail')}
```

In the dimer, positions 0 and 4 of each subunit touch the same positions of the other: one self-complementary interface. In the trimer, position 4 of one subunit touches position 0 of the next, three times: three equivalent head-to-tail interfaces. Real tools do the same with residues instead of points, after building the assembly from the operations stored in the entry.

## Worked example

> [!example] A hemoglobin entry that deposits half a tetramer
> Suppose a crystal entry of hemoglobin contains 2 chains, as some do.[^pdb]
> 1. **Deposited file.** Chains α and β: stoichiometry $\alpha\beta$, one interface ($\alpha_1\beta_1$).
> 2. **Assembly.** Applying the stored 2-fold operation creates $\alpha_2$ and $\beta_2$: stoichiometry $\alpha_2\beta_2$, the functional tetramer.[^berg]
> 3. **New interfaces.** Six chain pairs now exist, in four types: $\alpha_1\beta_1 \equiv \alpha_2\beta_2$, $\alpha_1\beta_2 \equiv \alpha_2\beta_1$, $\alpha_1\alpha_2$ and $\beta_1\beta_2$ (Exercise 4). The $\alpha_1\beta_2$ contacts, between the two dimers, are the ones remade when the dimers rotate on oxygen binding.[^berg]
> 4. **Consequence.** A residue of the $\alpha_1\beta_2$ interface appears exposed in the deposited file. Judged on that file, a substitution there would be called a harmless surface change, while it sits in the switch region of the tetramer. Always compute exposure and contacts on the biological assembly.

## Common misconceptions

> [!warning] "The coordinate file is the molecule"
> A crystal entry's file usually holds one asymmetric unit: part of an assembly (half a hemoglobin tetramer, one chain of a 60-chain capsid) or several copies of it.[^pdb] Download or build the biological assembly before analyzing interfaces.

> [!warning] "A heme or a bound drug gives a protein quaternary structure"
> Quaternary structure concerns several polypeptide chains.[^berg] A prosthetic group or a ligand bound to one chain is part of that chain's structure and function, not a quaternary contact; myoglobin with its heme is still a single-chain protein.

> [!warning] "Subunits are glued together once and for all"
> Subunits are held by many weak bonds, so assemblies can be built and taken apart under control,[^alberts] and their arrangement can change with function, as in the 15° rotation of hemoglobin's dimers.[^berg]

## Exercises

> [!question] Exercise 1 (L2)
> How many polypeptide chains form a rhinovirus coat? How many subunits and how many 2-fold axes does a $D_3$ assembly of one protein have, and how many subunits does a $C_5$ ring have?

> [!success]- Solution
> $60 \times 4 = 240$ chains (60 copies of each of four subunits).[^berg] $D_3$: $2 \times 3 = 6$ subunits, one 3-fold axis and three perpendicular 2-fold axes. $C_5$: 5 subunits.

> [!question] Exercise 2 (L2)
> An assembly has six chains: A, B and C have the same sequence, D and E another, F a third. Write the stoichiometry. Can the whole assembly have a rotational symmetry?

> [!success]- Solution
> $\mathrm{A_3B_2C}$ in the code's notation. A symmetry maps each chain onto a chain of the same entity, so it must map F, the only chain of its entity, onto itself; a single asymmetric chain is not invariant under any rotation other than the identity, so the whole assembly has no symmetry. Parts of it can: the three chains of the first entity could form a $C_3$ trimer, D and E a $C_2$ dimer.

> [!question] Exercise 3 (L2)
> Treat each αβ dimer of hemoglobin as a rigid body that rotates by about 15° relative to the other. Which interfaces keep their contacts, and which must change?

> [!success]- Solution
> Contacts inside a rigid body cannot change: $\alpha_1\beta_1$ and $\alpha_2\beta_2$ keep theirs. Every contact between the two bodies changes: $\alpha_1\beta_2$ and $\alpha_2\beta_1$, and the $\alpha_1\alpha_2$ and $\beta_1\beta_2$ contacts if present. The rotation itself is a measured fact;[^berg] which contacts change is the geometry of rigid bodies.

> [!question] Exercise 4 (L3, Python)
> Write `pair_orbits(chains, group)` that groups unordered chain pairs into orbits, a symmetry operation being a permutation of chain names. Apply it to hemoglobin with its exact 2-fold, then to a $D_2$ homotetramer whose three 2-folds swap $(s_1 s_2)(s_3 s_4)$, $(s_1 s_3)(s_2 s_4)$ and $(s_1 s_4)(s_2 s_3)$.

> [!success]- Solution
> ```python
> def pair_orbits(chains: list[str], group: list[dict]) -> list[list[tuple]]:
>     """Group unordered chain pairs that a symmetry operation (a chain permutation) maps onto each other."""
>     orbits = []
>     for pair in combinations(chains, 2):
>         images = {tuple(sorted(g[c] for c in pair)) for g in group}
>         for orbit in orbits:
>             if tuple(sorted(orbit[0])) in images:
>                 orbit.append(pair)
>                 break
>         else:
>             orbits.append([pair])
>     return orbits
>
>
> identity = {c: c for c in ["a1", "b1", "a2", "b2"]}
> twofold = {"a1": "a2", "a2": "a1", "b1": "b2", "b2": "b1"}            # hemoglobin's exact axis
> print(pair_orbits(["a1", "b1", "a2", "b2"], [identity, twofold]))
> s = ["s1", "s2", "s3", "s4"]                                            # D2 homotetramer
> d2 = [dict(zip(s, p)) for p in (s, ["s2", "s1", "s4", "s3"], ["s3", "s4", "s1", "s2"], ["s4", "s3", "s2", "s1"])]
> print(pair_orbits(s, d2))
> ```
> ```text
> [[('a1', 'b1'), ('a2', 'b2')], [('a1', 'a2')], [('a1', 'b2'), ('b1', 'a2')], [('b1', 'b2')]]
> [[('s1', 's2'), ('s3', 's4')], [('s1', 's3'), ('s2', 's4')], [('s1', 's4'), ('s2', 's3')]]
> ```
> Hemoglobin has 4 interface types among 6 pairs; the $D_2$ homotetramer has 3, one per 2-fold axis, and each is self-complementary because it is generated by a 2-fold. An analysis of interfaces needs one representative per orbit, not one per pair.

> [!question] Exercise 5 (L3, Python)
> Build a $C_6$ ring with `cyclic_assembly(6)`. Which rotations among 60°, 120°, 180° and 90° are symmetries? How many interfaces does the ring have, and of which kind? Relate the answer to the subgroups of $C_6$.

> [!success]- Solution
> ```python
> ring = cyclic_assembly(6)
> print([f"{a}°: {is_symmetric(ring, rot_z(a))}" for a in (60, 120, 180, 90)])
> print(len(interfaces(ring)), set(v[2] for v in interfaces(ring).values()))
> # ['60°: True', '120°: True', '180°: True', '90°: False']
> # 6 {'head-to-tail'}
> ```
> The ring is also symmetric under 120° and 180°: $C_6$ contains $C_3$ and $C_2$ as subgroups, while 90° belongs to $C_4$, which is not one of them. Its 6 interfaces are all head-to-tail and equivalent, one orbit. The 180° operation relates opposite subunits, which do not touch here, so it creates no self-complementary interface.

## Mastery checklist

- [ ] 1 Recognized: I can define quaternary structure, subunit, stoichiometry, homo- and hetero-oligomer, with hemoglobin as example.
- [ ] 2 Understood: I can explain why proteins assemble from subunits, the cyclic, dihedral and icosahedral symmetries, and the two kinds of interfaces.
- [ ] 3 Practiced: I can compute a stoichiometry, test a rotation symmetry and group interfaces into orbits in Python.
- [ ] 4 Applied: I downloaded the biological assembly of a real entry, compared it with the deposited asymmetric unit, and analyzed its interfaces.
- [ ] 5 Explained: I can teach how hemoglobin's quaternary change supports cooperativity and why interfaces from crystals or predictions must be checked.

## References

[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of quaternary structure (λ Cro dimer, hemoglobin as $\alpha_2\beta_2$ or a pair of αβ dimers, rhinovirus coat with 60 copies of each of four subunits, economy of genetic information), of the forces between subunits, of L-amino acids in proteins, and of hemoglobin's structural change on oxygen binding (rotation of the αβ dimers by about 15°).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of protein assemblies: dimers, helical filaments and rings from the geometry of binding sites, virus capsids, and the advantages of building large structures from subunits.
[^pdb]: [[RCSB Protein Data Bank]], PDB-101 "Guide to Understanding PDB Data", page "Introduction to Biological Assemblies and the PDB Archive": asymmetric unit, biological assembly, hemoglobin entries with 2 or 8 or more chains, icosahedral viruses, stored symmetry operations and assembly files.
[^jumper]: [[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]], *Nature* 596:583-589.
