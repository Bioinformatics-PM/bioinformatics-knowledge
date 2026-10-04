---
aliases:
  - Conformation
  - Conformer
  - Newman Projection
  - Chair Conformation
  - Analyse conformationnelle
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/physics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Orbital Hybridization]]"
  - "[[Skeletal Formula]]"
  - "[[Isomer]]"
related:
  - "[[Peptide Bond]]"
  - "[[Ramachandran Plot]]"
  - "[[Protein Structure]]"
  - "[[Carbohydrate]]"
  - "[[Boltzmann Distribution]]"
  - "[[Stereochemistry]]"
  - "[[Molecular Dynamics Simulation]]"
projects: []
sources:
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[MIT 5.12 - Organic Chemistry I]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
---

# Conformational Analysis

> [!abstract]
> Single bonds rotate, so one molecule takes many shapes, its conformations. Conformational analysis finds which shapes have low energy and how often each is populated: the same question, scaled up, as the shape of a protein backbone or a sugar ring.

## Definition

**Conformations** (conformers) are the different three-dimensional arrangements of a molecule that result from rotation about single bonds; they interconvert without breaking bonds. **Conformational analysis** compares their energies, which differ by torsional strain (repulsion between eclipsed bonds) and steric strain (atoms forced too close).[^os3][^512]

## Why it matters

- **A protein structure is a set of torsion angles.** With bond lengths and angles nearly fixed, the backbone is described by its rotatable angles φ and ψ per residue, and the [[Ramachandran Plot]] maps which combinations are allowed ([[Peptide Bond]], [[Protein Structure]]).
- **Sugar rings are not flat.** Pyranoses adopt chairs and furanoses puckered envelopes; which atoms are axial or equatorial decides the shape of polysaccharides and nucleic acid backbones ([[Carbohydrate]]).[^berg]
- **Docking and simulation sample conformations.** A ligand bound to a protein is in one of its conformations, and [[Molecular Docking]] and [[Molecular Dynamics Simulation]] spend most of their effort exploring torsional space.
- **Energies become populations.** A few kJ/mol of difference decides whether a conformation is dominant or rare, through the [[Boltzmann Distribution]].[^pboc]

## Core (L1)

**Rotation about a σ bond.** A σ bond keeps its overlap as one end turns ([[Orbital Hybridization]]), so groups on either side rotate. In ethane the **staggered** conformation (C–H bonds of the two carbons as far apart as possible) is the lowest in energy and the **eclipsed** one (bonds aligned) the highest, 12 kJ/mol above; this barrier is small enough for rotation to be very fast at room temperature.[^os3]

**Newman projection.** Look along the C–C bond: the front carbon is a point where its three bonds meet, the back carbon a circle from which its bonds emerge. The **dihedral angle** between two substituents is the angle between their bonds in this view ([[Peptide Bond#Mathematical representation]] computes it from coordinates).[^os3]

![[newman-butane-cyclohexane-chair.svg]]

**Butane.** Along C2–C3, the two methyls can be 180° apart (**anti**, lowest), 60° apart (**gauche**, 3.8 kJ/mol higher, from steric strain between the methyls) or aligned (**eclipsed**, 19 kJ/mol, the highest).[^os37] Staggered beats eclipsed (torsional strain), and among staggered forms, anti beats gauche (steric strain).

**Cyclohexane chair.** The six-membered ring puckers into a **chair**: each carbon carries one **axial** bond, parallel to the ring axis and alternately up and down, and one **equatorial** bond pointing outward around the ring. A **ring flip** converts one chair into the other and exchanges all axial and equatorial positions.[^os4] In methylcyclohexane, the axial methyl is crowded by the two axial hydrogens on the same side of the ring (1,3-diaxial interactions, 3.8 kJ/mol each, the same steric strain as gauche butane), so the equatorial chair is more stable by 7.6 kJ/mol.[^os47]

**Bio: the glucose chair.** In the chair of β-D-glucopyranose, all axial positions carry hydrogens and the bulkier –OH and –CH₂OH groups are equatorial, which is why this chair predominates.[^berg]

## Deeper (L2)

**From energy to population.** At temperature $T$, a conformation of energy $E_i$ and multiplicity $g_i$ is populated in proportion to $g_i\, e^{-E_i / RT}$ ([[Boltzmann Distribution]]).[^pboc] At 25 °C, $RT = 2.48$ kJ/mol: butane is about 70 % anti and 30 % gauche (two gauche forms, ±60°), and methylcyclohexane about 95 % equatorial (computed below). Nothing is frozen: every conformation with an energy of a few $RT$ is present.

**Rings beyond cyclohexane.** Five-membered rings pucker too: a furanose takes an **envelope** form with four atoms nearly coplanar and the fifth out of the plane. In the ribose of most biomolecules, C2 or C3 is the out-of-plane atom, on the same side as C5: the **C2-endo** and **C3-endo** puckers.[^berg] Sugar pucker is therefore one of the conformational variables of a nucleic acid backbone, alongside its torsion angles.

**Proteins in the same language.** Rotation about N–Cα (φ) and Cα–C (ψ) is free in the σ-bond sense, but many (φ, ψ) pairs are excluded by steric clashes, exactly the butane logic applied to a backbone; the peptide bond itself (ω) is locked near 180° or 0° ([[Peptide Bond]], [[Ramachandran Plot]]).[^berg]

## Advanced (L3)

- **Conformational explosion.** Each rotatable bond with three staggered minima multiplies the count by 3, so molecules have exponentially many conformations: enumerating them all is impossible for a protein and costly for a flexible drug, which is why docking and folding methods sample instead ([[Protein Folding]], [[Molecular Docking]]).
- **Energy landscapes.** Combining all torsions gives a multidimensional energy surface; minima are conformers, saddle points the barriers between them, and simulations estimate how populations and transitions follow from it ([[Free Energy Landscape]], [[Molecular Dynamics Simulation]]).
- **Structure validation.** Because staggered torsions and allowed (φ, ψ) regions are strongly preferred, unusual torsion angles in an experimental or predicted model flag possible errors ([[Ramachandran Plot]]).

## Mathematical representation

**Dihedral angle.** For bonded atoms A–B–C–D, $\varphi \in (-180°, 180°]$ is the angle between the planes ABC and BCD, read in the Newman projection along B–C ([[Orbital Hybridization#Mathematical representation]]).

**Torsional energy.** $E(\varphi)$ is periodic, so a short Fourier series is a natural model. For ethane, three identical eclipsing barriers per turn give $E(\varphi) = \tfrac{V_3}{2}(1 + \cos 3\varphi)$ with $V_3 = 12$ kJ/mol ($\varphi$ between two H, $0°$ eclipsed). For butane, with $\varphi$ the CH₃–C–C–CH₃ dihedral, the model $E(\varphi) = a + b \cos\varphi + c \cos 3\varphi$ through $E(0°) = E_0$, $E(60°) = E_{60}$, $E(180°) = E_{180}$ gives, since $\cos 3\varphi$ equals $1, -1, -1$ at these angles:

$$a = \frac{E_0 + E_{180}}{2}, \qquad b = \frac{2}{3}\left(\frac{E_0 - E_{180}}{2} + E_{60} - a\right), \qquad c = \frac{E_0 - E_{180}}{2} - b.$$

**Populations.** With multiplicities $g_i$, gas constant $R$ and temperature $T$: $p_i = g_i e^{-E_i/RT} / \sum_j g_j e^{-E_j/RT}$. For two states separated by $\Delta E$, the minor fraction is $1/(1 + e^{\Delta E/RT})$.

## Computational representation

Fit the butane torsion profile to the three textbook energies, locate its minima, then compare a three-state population estimate with the Boltzmann factor integrated over the angle.

```python
import math

RT = 8.314e-3 * 298.15                      # kJ/mol at 25 °C
E0, E60, E180 = 19.0, 3.8, 0.0              # butane: eclipsed, gauche, anti (kJ/mol)

# E(phi) = a + b cos(phi) + c cos(3 phi) through the three points (derivation in the text)
a = (E0 + E180) / 2
s, t = (E0 - E180) / 2, E60 - a
b = 2 * (s + t) / 3
c = s - b

def energy(phi_deg: float) -> float:
    phi = math.radians(phi_deg)
    return a + b * math.cos(phi) + c * math.cos(3 * phi)

print(f"E(phi) = {a:.2f} + {b:.2f} cos(phi) + {c:.2f} cos(3 phi)")
print("E(120) =", round(energy(120), 1), "kJ/mol")
print("minima at", [p for p in range(360) if energy(p) < min(energy(p - 1), energy(p + 1))])

# Populations: three discrete states versus the Boltzmann factor integrated over the angle
w = math.exp(-E60 / RT)                     # one gauche state relative to anti; there are two
print("three states: anti", round(1 / (1 + 2 * w), 3))
weights = [math.exp(-energy(i / 10) / RT) for i in range(3600)]
print("continuous:   anti", round(sum(weights[1200:2400]) / sum(weights), 3))

# Methylcyclohexane: the equatorial chair is lower by 7.6 kJ/mol
K = math.exp(7.6 / RT)
print("equatorial fraction", round(K / (1 + K), 3))
```

```text
E(phi) = 9.50 + 2.53 cos(phi) + 6.97 cos(3 phi)
E(120) = 15.2 kJ/mol
minima at [62, 180, 298]
three states: anti 0.698
continuous:   anti 0.686
equatorial fraction 0.955
```

The fitted curve has minima at anti (180°) and near ±60° (62° and 298°), as it should, and predicts about 15 kJ/mol for the eclipsed form with CH₃ facing H, between gauche and fully eclipsed. The two population estimates agree within about 1 %: the three-state picture is a good approximation when wells are deep compared with $RT$.

## Worked example

> [!example] Reading a Newman projection of butane at 120°
> 1. **Place the groups.** Front carbon: CH₃ up, H at 120° and 240°. Rotate the back carbon so its CH₃ sits at 120°: the back groups are now at 120°, 240° and 0°, directly behind the front ones.
> 2. **Classify.** Eclipsed (back bonds aligned with front bonds), with CH₃ eclipsing H, H eclipsing H, and H eclipsing CH₃.
> 3. **Energy.** Higher than any staggered form (torsional strain), lower than the CH₃/CH₃ eclipsed form at 0°; the model above puts it at 15.2 kJ/mol.
> 4. **Population.** $e^{-15.2/2.48} \approx 0.002$ relative to anti: an eclipsed conformation is a transition between staggered ones, almost never a resting state.

## Common misconceptions

> [!warning] "Conformations are different molecules"
> Anti and gauche butane interconvert many times per second at room temperature; they are one compound, present as a mixture. Isomers require breaking bonds to interconvert ([[Isomer]]).[^os3]

> [!warning] "Only the lowest-energy conformation exists"
> Populations follow the Boltzmann distribution: 30 % of butane is gauche at 25 °C. Structure files show one conformation, a snapshot or an average, not the only one.

> [!warning] "A ring flip turns an up substituent into a down one"
> A ring flip exchanges axial and equatorial positions, but a group that points up (on the top face) stays on the top face. Up/down (cis/trans relations) is configuration; axial/equatorial is conformation ([[Cis-Trans Isomerism]]).[^os4]

## Exercises

> [!question] Exercise 1 (L1)
> For butane, classify the CH₃–C2–C3–CH₃ dihedral angles 0°, 60°, 120°, 180°, 240° and 300° as staggered or eclipsed, and name the staggered ones (anti or gauche). Rank them by energy.

> [!success]- Solution
> Staggered: 60° and 300° (gauche), 180° (anti). Eclipsed: 0° (CH₃/CH₃), 120° and 240° (CH₃/H). Energy: anti (0) < gauche (3.8 kJ/mol) < CH₃/H eclipsed < CH₃/CH₃ eclipsed (19 kJ/mol).[^os37]

> [!question] Exercise 2 (L1)
> How many axial and how many equatorial hydrogens does the cyclohexane chair have? After a ring flip, where is a hydrogen that was axial and pointing up?

> [!success]- Solution
> Six of each, one axial and one equatorial per carbon. After the flip that hydrogen is equatorial, still on the top face of the ring.[^os4]

> [!question] Exercise 3 (L2, Python)
> Compute the gauche fraction of butane at 200 K, 298.15 K and 400 K with the three-state model. Then find the energy difference that would make a conformation 99 % dominant at 25 °C.

> [!success]- Solution
> ```python
> import math
> for T in (200, 298.15, 400):
>     w = math.exp(-3.8 / (8.314e-3 * T))
>     print(T, round(2 * w / (1 + 2 * w), 3))
> print(round(8.314e-3 * 298.15 * math.log(99), 1))
> ```
> Output: 0.169, 0.302, 0.389, then 11.4 kJ/mol. Heating populates higher conformations (the gauche fraction tends to 2/3 at infinite temperature, the ratio of multiplicities). A 99:1 ratio needs $\Delta E = RT \ln 99 \approx 11.4$ kJ/mol, three 1,3-diaxial interactions' worth: a group that bulky is practically locked equatorial.

> [!question] Exercise 4 (L3)
> In water at equilibrium, D-glucose is about one-third α and two-thirds β.[^lehninger] The anomers differ at C1: in the β chair the C1–OH is equatorial, in the α chair it is axial. Estimate the free-energy difference implied by the ratio at 25 °C, compare it with the 7.6 kJ/mol of an axial methyl, and say what this suggests.

> [!success]- Solution
> $\Delta G = RT \ln(2/1) = 2.48 \times 0.693 \approx 1.7$ kJ/mol in favor of β. This is far less than the 7.6 kJ/mol penalty of an axial methyl. An OH is smaller than a methyl, and the ring oxygen next to C1 changes the energetics at that carbon, so the equatorial preference of the anomeric OH is weak. Cyclohexane values are a first guide for sugars, not a substitute for sugar-specific data ([[Carbohydrate]]).

## Mastery checklist

- [ ] 1 Recognized: I can name staggered, eclipsed, anti, gauche, chair, axial and equatorial.
- [ ] 2 Understood: I can read and draw Newman projections and chairs, and explain torsional versus steric strain.
- [ ] 3 Practiced: I can fit a torsion profile and convert energy differences into populations at a given temperature.
- [ ] 4 Applied: I measured backbone torsions or a sugar pucker in a real PDB structure and related them to allowed conformations.
- [ ] 5 Explained: I can explain why molecules are conformational mixtures, why sampling is needed for flexible molecules, and how ring flips differ from configuration changes.

## References

[^os3]: [[Organic Chemistry (OpenStax)]], ch. 3 "Organic Compounds: Alkanes and Their Stereochemistry" (conformations of ethane, torsional strain, Newman projections).
[^os37]: [[Organic Chemistry (OpenStax)]], ch. 3, section 3.7 "Conformations of Other Alkanes" (butane: anti, gauche 3.8 kJ/mol, eclipsed 19 kJ/mol).
[^os4]: [[Organic Chemistry (OpenStax)]], ch. 4 "Organic Compounds: Cycloalkanes and Their Stereochemistry" (chair conformation, axial and equatorial bonds, ring flip).
[^os47]: [[Organic Chemistry (OpenStax)]], ch. 4, section 4.7 "Conformations of Monosubstituted Cyclohexanes" (methylcyclohexane, 1,3-diaxial interactions, 7.6 kJ/mol).
[^512]: [[MIT 5.12 - Organic Chemistry I]], Spring 2005, lecture handout on conformational analysis.
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of carbohydrates (chair form of β-D-glucopyranose, envelope forms and C2-endo and C3-endo puckers of furanoses) and of protein structure (torsion angles φ and ψ, steric exclusion, planar peptide bond).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of carbohydrates (anomers of D-glucose at equilibrium).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], treatment of statistical mechanics (Boltzmann distribution, thermal energy scale).
