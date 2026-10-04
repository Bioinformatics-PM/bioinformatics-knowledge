---
aliases:
  - Geometric Isomerism
  - E-Z Isomerism
  - Cis-Trans Isomer
  - Isomérie cis-trans
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Isomer]]"
  - "[[Stereochemistry]]"
  - "[[Orbital Hybridization]]"
related:
  - "[[Chirality]]"
  - "[[Diastereomer]]"
  - "[[Conformational Analysis]]"
  - "[[Lipid]]"
  - "[[Peptide Bond]]"
projects: []
sources:
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Biochemistry (Berg)]]"
---

# Cis-Trans Isomerism

> [!abstract]
> When a bond cannot rotate, two groups can sit on the same side of it (cis) or on opposite sides (trans), giving two different molecules with the same atoms and the same connections.

## Definition

**Cis-trans isomers** are stereoisomers that differ only in the placement of substituents on either side of a bond that cannot rotate, a C=C double bond or a ring: **cis** when two reference groups are on the same side, **trans** when they are on opposite sides.[^os74][^os] They exist only if each of the two carbons carries two different groups.[^os74] For any substitution pattern, the **E/Z** system replaces cis/trans: rank the two groups on each carbon by the Cahn-Ingold-Prelog rules; **Z** (*zusammen*, together) if the higher-ranked groups are on the same side, **E** (*entgegen*, opposite) if not.[^os75]

## Why it matters

- **Same formula, different shape.** Oleate and its trans isomer, elaidate, have identical constitutions; only the double-bond geometry tells them apart, so a structure or a lipid name without it is ambiguous ([[Lipid]]).[^lehninger]
- **Membrane physics.** Natural unsaturated fatty acids are almost all cis, and the cis kink keeps membranes fluid.[^lehninger]
- **Vision.** The primary event of seeing is a cis → trans isomerization of retinal.[^berg][^lehninger]
- **Protein structure.** Peptide bonds are planar and almost always trans; cis bonds cluster before proline, and a cis bond elsewhere in a model deserves a check ([[Peptide Bond]]).[^berg]

## Core (L1)

**Why the double bond locks.** In a C=C bond both carbons are sp² and the π bond is the side-by-side overlap of their parallel p orbitals ([[Orbital Hybridization]]). Twisting one end breaks that overlap, so the barrier to rotation is at least the strength of the π bond, about 350 kJ/mol: cis and trans isomers do not interconvert at room temperature.[^os74] Single bonds rotate freely, which only produces conformations ([[Conformational Analysis]]).

**When isomers exist.** 2-Butene (CH₃–CH=CH–CH₃) has a cis and a trans form; 1-butene does not, because one alkene carbon carries two H.[^os74]

```text
   H3C       CH3          H3C       H
      \     /                \     /
       C = C                  C = C
      /     \                /     \
     H       H              H       CH3
   cis-2-butene (Z)        trans-2-butene (E)
```

**Rings.** A ring blocks full rotation too: in a 1,2-disubstituted cycloalkane, both groups can point to the same face of the ring (cis) or to opposite faces (trans).[^os]

**Cis-trans isomers are diastereomers.** They are stereoisomers that are not mirror images, so they differ in physical properties (melting point, polarity, packing), unlike enantiomers ([[Chirality]], [[Diastereomer]]).

**Biological cases.**

| Bond | Cis form | Trans form | Consequence |
|---|---|---|---|
| C=C of fatty acids | natural unsaturated chains | rare in nature | cis kink: looser packing, lower melting point[^lehninger] |
| C11=C12 of retinal | 11-*cis*-retinal in rhodopsin | all-*trans*-retinal after light | shape change triggers the visual signal[^berg][^lehninger] |
| C–N of peptide bonds | before proline | the usual form | trans favored about 1000:1 for most residues[^berg] |
| C=C of butenedioate | maleate | fumarate (citric acid cycle) | fumarase hydrates fumarate only[^lehninger] |

## Deeper (L2)

**E/Z is the general system.** Cis/trans is unambiguous only for disubstituted double bonds.[^os75] In 2-bromo-2-butene, CH₃C(Br)=CHCH₃, the two methyls can be cis while the higher-ranked groups (Br on one carbon, CH₃ on the other) are on opposite sides: "cis" by methyls, yet **E** (computed below). For fatty acid chains the cases agree: on each alkene carbon the chain carbon outranks H, so cis = Z, hence the lipid shorthand `18:1(9Z)` ([[Lipid]]).

**Interconversion requires breaking the π bond.** Three routes matter in biology:

- **Light.** Absorbing a photon promotes an electron out of the π bond and lets the bond twist: 11-*cis*-retinal, bound to the protein opsin through a Schiff base with a lysine, becomes all-*trans*, and the change of shape switches rhodopsin to its active form, which starts the visual cascade.[^berg][^lehninger]
- **Enzymes.** Oxidizing oleate, the cell meets a cis double bond that the β-oxidation hydratase cannot use; an enoyl-CoA isomerase turns the cis-Δ³ intermediate into trans-Δ², the normal substrate.[^lehninger] Peptidyl-prolyl cis-trans isomerases speed up the slow cis/trans switch of X–Pro bonds during protein folding.[^lehninger]
- **Stereospecific enzymes discriminate isomers.** Fumarase adds water to fumarate (trans) but not to maleate (cis), and succinate dehydrogenase makes only fumarate.[^lehninger]

**Processing creates trans fats.** Partial hydrogenation of vegetable oils isomerizes some cis bonds to trans; trans chains pack more like saturated ones.[^lehninger]

## Mathematical representation

For a double bond $C_1{=}C_2$ with substituent $a$ on $C_1$ and $b$ on $C_2$, the geometry is the dihedral angle $\theta(a, C_1, C_2, b)$: $\theta \approx 0°$ is cis, $\theta \approx 180°$ is trans; intermediate values are not stable because they break the π overlap. Equivalently, with $\mathbf{u} = C_2 - C_1$ the bond axis and $\mathbf{p}_x$ the component of a bond vector perpendicular to $\mathbf{u}$,

$$\text{cis} \iff \mathbf{p}_{a - C_1} \cdot \mathbf{p}_{b - C_2} > 0, \qquad \mathbf{p}_{\mathbf{v}} = \mathbf{v} - \frac{\mathbf{v} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\,\mathbf{u}.$$

Z/E is the same test applied to the highest-ranked substituent on each carbon. A molecule with $m$ independent stereogenic double bonds has $2^m$ geometric isomers.

## Computational representation

Structure files store 3D coordinates, not the words cis or trans: the label is computed from geometry. The function below implements the perpendicular-component test.

```python
def _perp(atom, base, axis):
    """Component of (atom - base) perpendicular to the double-bond axis."""
    v = [a - b for a, b in zip(atom, base)]
    k = sum(p * q for p, q in zip(v, axis)) / sum(q * q for q in axis)
    return [p - k * q for p, q in zip(v, axis)]


def relation(c1, c2, sub1, sub2):
    """'cis' if sub1 (bonded to c1) and sub2 (bonded to c2) lie on the same side of c1=c2."""
    axis = [b - a for a, b in zip(c1, c2)]
    dot = sum(p * q for p, q in zip(_perp(sub1, c1, axis), _perp(sub2, c2, axis)))
    return "cis" if dot > 0 else "trans"


def e_or_z(c1, c2, top1, top2):
    """top1, top2: the higher-CIP-priority substituent on each alkene carbon."""
    return "Z" if relation(c1, c2, top1, top2) == "cis" else "E"


# Idealized planar coordinates in ångström (invented, 120° angles).
C2, C3 = (0.0, 0.0, 0.0), (1.34, 0.0, 0.0)
CH3_on_C2 = (-0.75, 1.30, 0.0)
CH3_on_C3_up, CH3_on_C3_down = (2.09, 1.30, 0.0), (2.09, -1.30, 0.0)
Br_on_C2 = (-0.95, -1.65, 0.0)

print("2-butene, methyls up/up:  ", relation(C2, C3, CH3_on_C2, CH3_on_C3_up),
      e_or_z(C2, C3, CH3_on_C2, CH3_on_C3_up))
print("2-butene, methyls up/down:", relation(C2, C3, CH3_on_C2, CH3_on_C3_down),
      e_or_z(C2, C3, CH3_on_C2, CH3_on_C3_down))
# 2-bromo-2-butene: on C2, Br outranks CH3; on C3, CH3 outranks H.
print("2-bromo-2-butene, methyls up/up: methyls", relation(C2, C3, CH3_on_C2, CH3_on_C3_up),
      "-> descriptor", e_or_z(C2, C3, Br_on_C2, CH3_on_C3_up))
```

```text
2-butene, methyls up/up:   cis Z
2-butene, methyls up/down: trans E
2-bromo-2-butene, methyls up/up: methyls cis -> descriptor E
```

## Worked example

> [!example] Fumarate or maleate?
> Both are ⁻OOC–CH=CH–COO⁻.
> 1. **Can they be cis-trans isomers?** Each alkene carbon carries COO⁻ and H, two different groups: yes.[^os74]
> 2. **Rank on each carbon.** COO⁻ (C with O, O, O) outranks H.
> 3. **Assign.** Carboxylates on opposite sides: trans, **E**: fumarate. Same side: cis, **Z**: maleate.
> 4. **Biology.** Succinate dehydrogenase produces fumarate in the citric acid cycle and fumarase hydrates only fumarate; maleate is not a substrate.[^lehninger] Same formula, same connections, different biology.

## Common misconceptions

> [!warning] "Cis always means Z"
> Cis/trans compares two chosen groups; E/Z compares the highest-ranked group on each carbon. In 2-bromo-2-butene the methyls are cis but the descriptor is E. They coincide for fatty acid chains, which is why the lipid literature can use both.[^os75]

> [!warning] "Rotating around the double bond turns cis into trans"
> Rotation would have to break the π bond, about 350 kJ/mol; cis and trans forms are distinct compounds that need light, heat or an enzyme to interconvert.[^os74] Rotations around single bonds only change conformation.

> [!warning] "Cis-trans isomers are mirror images"
> They are diastereomers: not mirror images, with different physical properties. A trans-2-butene molecule is superimposable on its own mirror image.

## Exercises

> [!question] Exercise 1 (L1)
> Which of these have cis-trans isomers: propene, 2-butene, 1,1-dichloroethene, 1,2-dichloroethene, 1,2-dimethylcyclohexane?

> [!success]- Solution
> 2-Butene, 1,2-dichloroethene and 1,2-dimethylcyclohexane. Propene and 1,1-dichloroethene each have an alkene carbon with two identical groups (two H, two Cl), so swapping sides gives the same molecule.[^os74]

> [!question] Exercise 2 (L1)
> Oleate is cis-Δ⁹-octadecenoate. Is its double bond Z or E, and why does it melt lower than stearate (18:0)?

> [!success]- Solution
> Z: on C9 and C10 the chain carbon outranks H, and the chains are on the same side. The cis bond kinks the chain, so oleate chains pack less tightly than straight stearate chains and melt at a lower temperature.[^lehninger]

> [!question] Exercise 3 (L2)
> Linoleate is 18:2(9Z,12Z). How many geometric isomers of these two double bonds exist? Name them.

> [!success]- Solution
> $2^2 = 4$: (9Z,12Z), the natural one, plus (9Z,12E), (9E,12Z) and (9E,12E).

> [!question] Exercise 4 (L2, Python)
> Toy, idealized coordinates (invented) for the retinal fragment C10–C11=C12–C13: C11 = (0, 0, 0), C12 = (1.34, 0, 0), C10 = (−0.75, 1.30, 0); C13 is at (2.09, 1.30, 0) before illumination and at (2.09, −1.30, 0) after. Classify both with `relation`, and say which bond had to lose its π overlap.

> [!success]- Solution
> `relation(C11, C12, C10, C13)` prints `cis` before and `trans` after: 11-*cis* → all-*trans*. The C11=C12 π bond is transiently broken by the absorbed photon, which lets the bond twist.[^berg]

## Mastery checklist

- [ ] 1 Recognized: I can spot cis and trans forms of a double bond or ring.
- [ ] 2 Understood: I can explain why the π bond blocks rotation and when cis-trans isomers exist.
- [ ] 3 Practiced: I can assign E/Z with CIP priorities, including cases where cis ≠ Z, and classify geometry from coordinates.
- [ ] 4 Applied: I read double-bond geometry from lipid names and checked cis peptide bonds in a real structure.
- [ ] 5 Explained: I can explain fatty acid kinks, retinal photoisomerization and X–Pro cis bonds as one phenomenon.

## References

[^os74]: [[Organic Chemistry (OpenStax)]], sec. 7.4 "Cis–Trans Isomerism in Alkenes".
[^os75]: [[Organic Chemistry (OpenStax)]], sec. 7.5 "Alkene Stereochemistry and the E,Z Designation".
[^os]: [[Organic Chemistry (OpenStax)]], treatment of cis-trans isomerism in cycloalkanes.
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021).
