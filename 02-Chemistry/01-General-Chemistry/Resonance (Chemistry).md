---
aliases:
  - Resonance
  - Resonance Structure
  - Resonance Hybrid
  - Contributing Structure
  - Electron Delocalization
  - Mesomerism
  - Résonance (chimie)
  - Mésomérie
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Lewis Structure]]"
  - "[[Covalent Bond]]"
  - "[[Electronegativity]]"
  - "[[Orbital Hybridization]]"
related:
  - "[[Molecular Orbital Theory]]"
  - "[[Aromaticity]]"
  - "[[Peptide Bond]]"
  - "[[Functional Group]]"
  - "[[Phosphate Ester]]"
  - "[[Acid-Base Reaction]]"
  - "[[ATP]]"
  - "[[Tautomer]]"
  - "[[Ramachandran Plot]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[OpenSMILES Specification]]"
---

# Resonance (Chemistry)

> [!abstract]
> When no single Lewis structure places a molecule's electrons correctly, the molecule is one hybrid of several drawings that differ only in where the electrons sit: the electrons are delocalized, the bonds are intermediate, and the hybrid is more stable than any one drawing.

## Definition

**Resonance structures** (contributing structures) are Lewis structures of the same species that keep every atom in place and differ only in the placement of π electrons and lone pairs. The real species, the **resonance hybrid**, is a weighted average of them: a single structure, written with a double-headed arrow ↔ between its contributors, whose **delocalized** electrons are spread over three or more atoms.[^c2e74][^osres]

## Why it matters

- **Protein backbone geometry.** Resonance gives the peptide C–N bond partial double-bond character, so the peptide unit is planar and the chain turns only at the Cα atoms: a backbone conformation is two angles per residue, φ and ψ ([[Peptide Bond]], [[Ramachandran Plot]]).[^berg]
- **Charges in structure models.** The two oxygens of a carboxylate (Asp, Glu, C-terminus) and the two non-bridging oxygens of each backbone phosphate of DNA and RNA share one negative charge equally. A model that puts charges on atoms, from a [[Force Field]] to an electrostatics calculation, must spread that charge, and a structure file's two names for equivalent oxygens are a labeling choice, not chemistry (Exercise 5).
- **Acidity and energy.** Spreading a charge stabilizes it: this is why carboxylic acids are acids while alcohols barely are ([[Acid-Base Reaction]], [[Functional Group]]), why Arg stays protonated, and part of why [[ATP]] hydrolysis releases so much free energy (L3).
- **Molecules as strings.** A SMILES string writes one Kekulé structure, or writes aromatic atoms in lowercase and leaves the choice of double bonds to the software ([[Skeletal Formula]]).[^smiles] Two strings that differ only by a resonance drawing describe the same molecule, which canonicalization has to recognize.

## Core (L2)

![[resonance-carboxylate-phosphodiester-hybrids.svg]]

### Rules for drawing resonance structures

1. **Only electrons move.** π electrons and lone pairs shift; atoms, σ bonds and hybridization stay. A drawing that moves an atom, such as a proton, is another molecule ([[Tautomer]]).[^osres]
2. **Every drawing is a valid [[Lewis Structure]]**, with the same number of electrons and the same net charge, and no second-row atom beyond an octet.[^osres][^c2e74]
3. **Curved arrows** record the move: each starts at a lone pair or a π bond and ends where that pair goes (figure, top left).[^osres]
4. **The hybrid is one structure.** It never flips between the drawings: ↔ is not the equilibrium arrow ⇌.[^osres]
5. **Weights follow stability.** Equivalent drawings contribute equally. Otherwise the more important drawing has more bonds, complete octets, fewer formal charges and any negative charge on the more electronegative atom ([[Electronegativity]]).[^c2e74][^osres]
6. **Delocalization stabilizes.** The hybrid is more stable than any single drawing, and the more resonance forms, the more stable the species.[^osres] The Mathematical representation shows why equivalent drawings give the largest effect.

### Recurring patterns

| Pattern | Drawings | In biomolecules |
|---|---|---|
| Lone pair next to a π bond | X–C=O ↔ X⁺=C–O⁻ | amide: the [[Peptide Bond]] |
| Charge shared by equivalent atoms | O=C–O⁻ ↔ ⁻O–C=O | carboxylate of Asp, Glu, C-terminus |
| One P=O spread over several oxygens | 2 drawings (diester), 4 (PO₄³⁻) | DNA and RNA backbone, [[ATP]], [[Phosphate Ester\|phosphate esters]] |
| Positive charge spread over three N | C=N⁺ moves among the three N | guanidinium of Arg |
| Alternating π bonds around a ring | two Kekulé structures | Phe, Tyr, Trp, nucleobases ([[Aromaticity]]) |

### Bio: the peptide bond

Drawing I, O=C–N–H, carries no formal charges; drawing II, ⁻O–C=N⁺–H, separates two charges and is the minor contributor (rule 5). Its contribution is still large enough to measure: the peptide C–N bond is 1.32 Å long, between a C–N single bond (1.49 Å) and a C=N double bond (1.27 Å). Rotation about it would break the π overlap, so Cα, C, O, N, H and the next Cα lie in one plane, almost always in the trans arrangement.[^berg] Drawing II also puts partial negative charge on O and partial positive charge on N–H: the acceptor and the donor of the backbone hydrogen bonds of helices and sheets ([[Protein Secondary Structure]]).[^berg]

### Bio: equivalent oxygens

- **Carboxylate.** Two equivalent drawings: each C–O bond has order 3/2 and each oxygen carries −1/2. Bond lengths confirm it: both C–O bonds of sodium formate measure 127 pm, between the C=O (120 pm) and the C–O (134 pm) of formic acid.[^os202]
- **Phosphate.** The phosphodiester linking two nucleotides carries one negative charge,[^berg] shared by its two non-bridging oxygens: P–O order 3/2 and −1/2 per oxygen (figure, bottom). Free PO₄³⁻ has four equivalent drawings: order 5/4 and −3/4 per oxygen ([[Lewis Structure]]).[^c2e74]

## Advanced (L3)

- **Delocalization energy is measurable.** Benzene releases about 150 kJ/mol less on hydrogenation than a ring of three isolated C=C bonds would: the stabilization of its hybrid ([[Aromaticity]]).[^os152]
- **Delocalized charges set pKa values.** A conjugate base whose charge is spread is more stable, so its acid is stronger: carboxylic acids against alcohols.[^os202] Run for a conjugate acid, the same logic explains Arg: its protonated guanidinium spreads the charge over three nitrogens and is a very weak acid, with a side-chain pKa of about 12.5, the highest among the standard amino acids.[^lehninger] An amide nitrogen, whose lone pair is delocalized into the carbonyl, is not basic at all,[^osamide] so the backbone N–H of a protein is not protonated at physiological pH while the amine of Lys (pKa about 10.5) is.[^lehninger]
- **Resonance and the energy of ATP.** Inorganic phosphate has more resonance forms than the terminal phosphoryl group bound in ATP; this extra stabilization of the products is one of the reasons ATP hydrolysis releases a large amount of free energy ([[ATP]]).[^berg]
- **Two languages for one physics.** Resonance is the valence-bond description of delocalization. [[Molecular Orbital Theory]] describes the same electrons with orbitals spread over the whole π system; its bond orders give the central bond of butadiene partial double-bond character without drawing any resonance structure. Both need parallel p orbitals, so conjugated groups are planar ([[Orbital Hybridization]]).[^c2e83]

## Mathematical representation

**Averaging over drawings.** Let structures $S_1, \dots, S_K$ assign bond orders $b^{(k)}_{ij}$ between atoms $i$ and $j$ and formal charges $q^{(k)}_i$, with weights $w_k \ge 0$, $\sum_k w_k = 1$. The hybrid has

$$\bar b_{ij} = \sum_k w_k\, b^{(k)}_{ij}, \qquad \bar q_i = \sum_k w_k\, q^{(k)}_i, \qquad \sum_i \bar q_i = Q,$$

the last because the formal charges of every drawing add up to the net charge $Q$ ([[Lewis Structure#Mathematical representation]]). When one π bond and a total charge $q$ are shared by $n$ equivalent atoms, each bond has order $1 + \frac1n$ and each atom carries $\frac qn$: carboxylate ($n = 2$, $q = -1$), guanidinium ($n = 3$, $q = +1$), PO₄³⁻ ($n = 4$, $q = -3$).

**Why the hybrid is lower in energy (a two-state model).** Treat two drawings as orthonormal states of energies $E_1 \le E_2$, gap $\Delta = E_2 - E_1$, coupled by $\beta < 0$. The hybrid is the lowest eigenvector $(c_1, c_2)$ of

$$\mathbf H = \begin{pmatrix} E_1 & \beta \\ \beta & E_2 \end{pmatrix}, \qquad E_{\text{hybrid}} = \frac{E_1 + E_2}{2} - \sqrt{\frac{\Delta^2}{4} + \beta^2} \;\le\; E_1 .$$

The **resonance energy** $E_1 - E_{\text{hybrid}} = \sqrt{\Delta^2/4 + \beta^2} - \Delta/2$ is largest, $|\beta|$, for equivalent drawings ($\Delta = 0$, weights $c_1^2 = c_2^2 = \frac12$) and decays toward $\beta^2/\Delta$ when the second drawing is costly, together with its weight $w_2 = c_2^2/(c_1^2 + c_2^2)$. Rules 5 and 6 are the qualitative reading of this formula, and it is the same 2 × 2 problem as a bonding orbital in [[Molecular Orbital Theory]].

## Computational representation

A resonance structure is a set of bond orders and formal charges on a fixed molecular graph, and the hybrid is their weighted average. Exact fractions keep 1/3 from becoming 0.333:

```python
from fractions import Fraction


def hybrid(structures, weights=None):
    """Weighted average of bond orders and formal charges over resonance structures.
    Each structure is a pair (bond_orders, formal_charges); equal weights by default."""
    weights = weights or [Fraction(1, len(structures))] * len(structures)
    bonds, charges = {}, {}
    for w, (b, q) in zip(weights, structures):
        for key, order in b.items():
            bonds[key] = bonds.get(key, 0) + w * order
        for atom, c in q.items():
            charges[atom] = charges.get(atom, 0) + w * c
    return bonds, charges


def one_double(center, ligands, q_double, q_single):
    """One structure per ligand: that ligand double-bonded to the center, the others single."""
    return [({f"{center}-{l}": 2 if l == d else 1 for l in ligands},
             {l: q_double if l == d else q_single for l in ligands}) for d in ligands]


GROUPS = {
    "carboxylate": one_double("C", ["O1", "O2"], 0, -1),
    "phosphodiester": one_double("P", ["O1", "O2"], 0, -1),        # non-bridging O only
    "phosphate PO4(3-)": one_double("P", ["O1", "O2", "O3", "O4"], 0, -1),
    "guanidinium (Arg)": one_double("C", ["N1", "N2", "N3"], 1, 0),
}
for name, structures in GROUPS.items():
    bonds, charges = hybrid(structures)
    print(f"{name:18} K={len(structures)}  bond order {set(map(str, bonds.values()))}"
          f"  charge per atom {set(map(str, charges.values()))}")

# Peptide bond: I (O=C-N) and II (-O-C=N+) are not equivalent; w = 1/3 is only an illustration
peptide = [({"C-O": 2, "C-N": 1}, {"O": 0, "N": 0}), ({"C-O": 1, "C-N": 2}, {"O": -1, "N": 1})]
w = Fraction(1, 3)
bonds, charges = hybrid(peptide, [1 - w, w])
print("peptide, w = 1/3:", {k: str(v) for k, v in bonds.items()}, {k: str(v) for k, v in charges.items()})
```

```text
carboxylate        K=2  bond order {'3/2'}  charge per atom {'-1/2'}
phosphodiester     K=2  bond order {'3/2'}  charge per atom {'-1/2'}
phosphate PO4(3-)  K=4  bond order {'5/4'}  charge per atom {'-3/4'}
guanidinium (Arg)  K=3  bond order {'4/3'}  charge per atom {'1/3'}
peptide, w = 1/3: {'C-O': '5/3', 'C-N': '4/3'} {'O': '-1/3', 'N': '1/3'}
```

Real toolkits enumerate resonance structures on the same kind of graph; what no program can supply is the weights of non-equivalent drawings, which come from energies. The two-state model gives them:

```python
import math


def mix_two(delta, beta=-1.0):
    """Lowest eigenvector of [[0, beta], [beta, delta]]: weight of the higher drawing, resonance energy."""
    e_low = delta / 2 - math.sqrt(delta ** 2 / 4 + beta ** 2)
    ratio = e_low / beta                      # c2/c1, from the first row: beta*c2 = e_low*c1
    return ratio ** 2 / (1 + ratio ** 2), -e_low


for delta in (0, 1, 2, 4):
    w2, e_res = mix_two(delta)
    print(f"delta = {delta}|beta|: weight of higher drawing {w2:.3f}, resonance energy {e_res:.3f}|beta|")
```

```text
delta = 0|beta|: weight of higher drawing 0.500, resonance energy 1.000|beta|
delta = 1|beta|: weight of higher drawing 0.276, resonance energy 0.618|beta|
delta = 2|beta|: weight of higher drawing 0.146, resonance energy 0.414|beta|
delta = 4|beta|: weight of higher drawing 0.053, resonance energy 0.236|beta|
```

## Worked example

> [!example] Reading resonance from bond lengths
> 1. **Carboxylate.** Two equivalent drawings predict one length for both C–O bonds, between C=O and C–O. Sodium formate: 127 pm for both; formic acid: 120 and 134 pm.[^os202] On a straight line from single (0) to double (1), 127 pm sits at $(134 - 127)/(134 - 120) = 0.50$: halfway, as order 3/2 predicts.
> 2. **Peptide.** C–N 1.32 Å, single 1.49 Å, double 1.27 Å:[^berg] the index is $(1.49 - 1.32)/(1.49 - 1.27) = 0.77$.
> 3. **How far to trust the index.** Length is not linear in bond order: with the Chemistry 2e averages C–C 1.54 Å, C=C 1.34 Å and C≡C 1.20 Å, the second bond shortens the distance by 0.20 Å but the third only by 0.14 Å ([[Covalent Bond]]).[^c2e75] The index ranks bonds (the peptide C–N is far from a plain single bond) but is neither a bond order nor the weight of drawing II.
> 4. **Consequence.** A partial double bond does not rotate freely: the peptide unit is planar and nearly always trans, which is what structure models assume ([[Peptide Bond]], [[Cis-Trans Isomerism]]).[^berg]

## Common misconceptions

> [!warning] "The molecule flips back and forth between its resonance structures"
> The hybrid is one structure at every instant; the drawings are bookkeeping for a bonding pattern that a single Lewis structure cannot show. ↔ is not an equilibrium.[^osres]

> [!warning] "Resonance and tautomerism are the same thing"
> Tautomers differ in the position of an atom, usually a proton, and are distinct molecules that interconvert by a reaction (a ketone and its enol). Resonance structures never move an atom.[^osres]

> [!warning] "All resonance structures contribute equally"
> Only equivalent ones do. The charge-separated drawing of the peptide bond is a minor contributor; a drawing with an incomplete octet hardly counts.[^c2e74][^osres]

> [!warning] "The negative charge of a carboxylate sits on the oxygen drawn with a single bond"
> Which oxygen gets the single bond is an arbitrary choice of the drawing. Both oxygens carry −1/2 and both C–O bonds have the same length.[^os202]

## Exercises

> [!question] Exercise 1 (L2)
> Draw the resonance structures of the guanidinium group of Arg with curved arrows, and give the C–N bond order and the charge on each nitrogen in the hybrid, assuming equal weights.

> [!success]- Solution
> The C=N⁺ bond can sit on any of the three nitrogens. To go from one drawing to the next, an arrow takes the lone pair of a neutral nitrogen into its C–N bond, which becomes C=N⁺, and a second arrow moves the old C=N⁺ π pair onto its nitrogen, which becomes neutral. Three drawings give each C–N an order of $1 + \frac13 = \frac43$ and each N $+\frac13$ (code output `4/3`, `1/3`). The weights are only nearly equal, since one nitrogen carries the side chain.

> [!question] Exercise 2 (L2)
> Which pairs are resonance structures? (a) the two Kekulé structures of benzene; (b) acetone and its enol CH₂=C(OH)–CH₃; (c) O=C–NH₂ and ⁻O–C=NH₂⁺ in an amide; (d) the cis and trans forms of a peptide bond.

> [!success]- Solution
> (a) Yes: only π electrons move. (b) No: a proton moves from carbon to oxygen, so these are tautomers, two molecules. (c) Yes: a lone pair and a π pair move. (d) No: atoms move by rotation, giving isomers ([[Cis-Trans Isomerism]]); the rotation is hindered precisely because resonance makes the C–N bond partly double.

> [!question] Exercise 3 (L2)
> A linear single-stranded DNA of 20 nucleotides has 19 phosphodiester groups. Over how many oxygens is the backbone charge spread, how much charge does each carry, and what is the P–O bond order of a non-bridging oxygen?

> [!success]- Solution
> One negative charge per phosphodiester, shared by its two non-bridging oxygens: 38 oxygens, −1/2 each, total −19. Each non-bridging P–O has order 3/2 (code output for `phosphodiester`).

> [!question] Exercise 4 (L3)
> With the two-state model, compare the resonance energy and the weight of the higher drawing for $\Delta = 0$ and $\Delta = 2|\beta|$. Why is a carboxylate stabilized more than an anion whose two drawings differ in energy?

> [!success]- Solution
> $\Delta = 0$: resonance energy $|\beta|$, weight 0.5. $\Delta = 2|\beta|$: $\sqrt{1 + 1} - 1 = 0.414|\beta|$ and weight 0.146 (table above). The carboxylate's two drawings are identical, which is the $\Delta = 0$ case: the largest stabilization the model allows. The more unequal the drawings, the more the hybrid looks like the better one and the less it gains.

> [!question] Exercise 5 (L3, Python)
> Two structures of the same protein have been superimposed; below is the same Asp side chain in each (toy coordinates, invented). Compute the RMSD over CB, CG, OD1 and OD2 as labelled, then allowing the two carboxylate oxygens to swap names. Which number measures the real difference?
> ```python
> import math
>
> ref = {"CB": (0.00, 0.00, 0.00), "CG": (1.52, 0.00, 0.00),
>        "OD1": (2.15, 1.07, 0.00), "OD2": (2.15, -1.07, 0.00)}
> model = {"CB": (0.04, 0.03, 0.00), "CG": (1.55, -0.02, 0.03),
>          "OD1": (2.19, -1.03, 0.05), "OD2": (2.11, 1.10, -0.04)}   # invented, already superimposed
> ```

> [!success]- Solution
> ```python
> def rmsd(a, b):
>     return math.sqrt(sum(math.dist(a[k], b[k]) ** 2 for k in a) / len(a))
>
>
> swapped = dict(model, OD1=model["OD2"], OD2=model["OD1"])
> print(round(rmsd(ref, model), 2), round(min(rmsd(ref, model), rmsd(ref, swapped)), 2))
> ```
> Output: `1.51 0.06`. Resonance makes the two oxygens equivalent, so which one is called OD1 is arbitrary: the 1.51 Å is an artifact of naming, and 0.06 Å is the real difference. Any comparison of structures (RMSD, contact maps, charge assignment) should treat atoms made equivalent by resonance as interchangeable.

> [!question] Exercise 6 (L3)
> The nitrogen of a peptide bond has a lone pair, like the nitrogen of an amine, yet the protein backbone is not protonated at pH 7 while the side chain of Lys is. Explain with resonance, and predict the geometry at the amide nitrogen.

> [!success]- Solution
> The amide lone pair is delocalized into the carbonyl (drawing II); protonating the nitrogen would take that pair out of the π system and lose the resonance stabilization, so amides are not basic.[^osamide] Lys's amine nitrogen holds a localized lone pair and is basic (pKa about 10.5).[^lehninger] The delocalized amide nitrogen is sp² and planar, not pyramidal like an amine nitrogen: the planarity of the peptide unit ([[Orbital Hybridization]]).

## Mastery checklist

- [ ] 1 Recognized: I can say what a resonance hybrid is and read the ↔ arrow.
- [ ] 2 Understood: I can state the rules (only electrons move, valid Lewis structures, weights by stability) and explain the peptide bond, carboxylate and phosphate cases.
- [ ] 3 Practiced: I can draw resonance structures with curved arrows and compute hybrid bond orders and charges by hand and in Python.
- [ ] 4 Applied: I treat resonance-equivalent atoms (Asp, Glu, Arg, backbone phosphates) correctly when comparing real structures or assigning charges.
- [ ] 5 Explained: I can teach why delocalization stabilizes (two-state model), how it sets pKa values and backbone planarity, and where the resonance picture hands over to molecular orbitals.

## References

[^c2e74]: [[Chemistry 2e (OpenStax)]], ch. 7, §7.4 "Formal Charges and Resonance" (formal charge, rules for choosing a structure, resonance forms and the resonance hybrid).
[^c2e75]: [[Chemistry 2e (OpenStax)]], ch. 7, §7.5 "Strengths of Ionic and Covalent Bonds" (table of average bond lengths and bond energies).
[^c2e83]: [[Chemistry 2e (OpenStax)]], ch. 8, §8.3 "Multiple Bonds" (σ and π bonds, delocalized π systems).
[^osres]: [[Organic Chemistry (OpenStax)]], treatment of resonance (forms differ only in the placement of π and nonbonding electrons; rules for resonance forms; curved arrows; the hybrid is more stable than any single form) (chapter not verified).
[^os202]: [[Organic Chemistry (OpenStax)]], §20.2 "Structure and Properties of Carboxylic Acids" (resonance-stabilized carboxylate; both C–O bonds of sodium formate 127 pm, against 120 pm and 134 pm in formic acid).
[^os152]: [[Organic Chemistry (OpenStax)]], sec. 15.2 "Structure and Stability of Benzene".
[^osamide]: [[Organic Chemistry (OpenStax)]], treatment of amines and amides (amides are not basic because the nitrogen lone pair is delocalized into the carbonyl) (chapter not verified).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein structure (peptide bond lengths 1.32, 1.49 and 1.27 Å, planarity, trans configuration, backbone hydrogen bonds), of nucleic acid backbones (one negative charge per phosphodiester) and of the phosphoryl-transfer potential of ATP (resonance stabilization of orthophosphate).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), table of properties of the common amino acids (side-chain pKa: Arg 12.48, Lys 10.53).
[^smiles]: [[OpenSMILES Specification]] (aromatic atoms written in lowercase).
