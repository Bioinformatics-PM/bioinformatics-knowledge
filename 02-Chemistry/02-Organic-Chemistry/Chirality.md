---
aliases:
  - Chiral
  - Stereocenter
  - Enantiomer
  - Cahn-Ingold-Prelog Rules
  - Chiralité
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/computer-science
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Stereochemistry]]"
  - "[[Isomer]]"
  - "[[Skeletal Formula]]"
related:
  - "[[Fischer Projection]]"
  - "[[Amino Acid]]"
  - "[[Carbohydrate]]"
  - "[[Diastereomer]]"
  - "[[Permutation]]"
  - "[[Graph]]"
projects: []
sources:
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[OpenSMILES Specification]]"
---

# Chirality

> [!abstract]
> A chiral molecule differs from its mirror image the way a left hand differs from a right hand. The usual cause is a carbon carrying four different groups; the Cahn-Ingold-Prelog rules name its two mirror forms R and S, and life builds its proteins from one form only.

## Definition

An object is **chiral** when it cannot be superimposed on its mirror image. In organic molecules, the most common cause is a **stereocenter** (chirality center): a tetrahedral carbon bonded to four different groups. The two mirror-image forms of a chiral molecule are **enantiomers**.[^os5] The **Cahn-Ingold-Prelog (CIP) rules** rank the four groups and label each stereocenter **R** or **S**.[^os55]

## Why it matters

- **Proteins use one hand.** Every amino acid except glycine has a stereocenter at Cα, and proteins are built from L-amino acids only.[^berg] For 19 of the 20, L means S; for cysteine, L means R, a naming effect explained below.[^os26]
- **Enantiomers are different drugs.** Receptors and enzymes are chiral, so the two enantiomers of a chiral drug can have different biological effects ([[Stereochemistry]]).[^os512]
- **Files must carry it.** SMILES writes each stereocenter with `@` or `@@`; structure files give coordinates from which R or S must be computed. A tool that ignores stereo merges enantiomers.[^osm]

## Core (L1)

**Finding stereocenters.** Look for sp³ carbons with four different substituents. A CH₃ or CH₂ (two identical H), a C=O or C=C carbon (only three groups) can never be one. "Different" means the whole branch: in citric acid, the central carbon carries OH, COOH and two identical CH₂COOH arms, so it is not a stereocenter.

| Molecule | Stereocenters |
|---|---|
| Glycine | none (two H on Cα)[^berg] |
| Alanine, serine, cysteine | one, Cα |
| Threonine, isoleucine | two: Cα and Cβ[^lehninger] |
| Glyceraldehyde | one, C2 |
| Citric acid | none |

![[enantiomers-mirror-alanine.svg]]

**Assigning R or S (CIP).**[^os55]

1. **Rank** the four atoms attached to the stereocenter by atomic number: the higher, the higher the priority (so H is last).
2. **Break ties** by moving outward: compare the sets of atoms attached to the tied atoms, highest first, and stop at the first point of difference.
3. **Multiple bonds** count as duplicated atoms: C=O is treated as C bonded to two O.
4. **Look** at the molecule with the lowest-priority group pointing away. If 1 → 2 → 3 turns clockwise, the center is **R** (*rectus*); anticlockwise, **S** (*sinister*).

**Bio: L-alanine is S.** Priorities NH₂ (N, 7) > COOH (C with O, O, O) > CH₃ (C with H, H, H) > H. With H behind, NH₂ → COOH → CH₃ runs anticlockwise in L-alanine: S. Its enantiomer, D-alanine, is R (figure).

## Deeper (L2)

**Three labels that do not agree.** D/L compares a molecule with glyceraldehyde in a [[Fischer Projection]] (a relative convention used for sugars and amino acids); R/S is an absolute label from the CIP rules; (+)/(−) is the measured direction in which a sample rotates polarized light. They are independent: there is no simple correlation between R/S and the sign of rotation.[^os5] L-cysteine is R and L-serine S although both have the L arrangement: the sulfur of CH₂SH outranks the oxygens of COOH, while the CH₂OH of serine does not.[^os26]

**Stereo in SMILES.** A bracket atom such as `[C@@H]` or `[C@H]` carries a tag: looking from the first neighbour (the atom written before it), the remaining neighbours, in the order written, run anticlockwise for `@` and clockwise for `@@`; an implicit H in the bracket counts as the neighbour immediately after the first.[^osm] The tag therefore depends on the writing order: the same molecule written in another order may need the other tag. With the neighbours of Cα written in the order N, H, side chain, carboxyl, as in `N[C@@H](C)C(=O)O`, the `@@` tag is the L arrangement: viewed from N, H → CH₃ → COOH run clockwise; viewed from the side opposite H, NH₂ → COOH → CH₃ then run anticlockwise, which is S, L-alanine.

## Advanced (L3)

- **Computing from 3D coordinates.** With the substituents ranked, the sign of the signed volume $V = u_1 \cdot (u_2 \times u_3)$ of the bond vectors to priorities 1, 2, 3 gives the label: $V > 0$ is S and $V < 0$ is R (check: the toy center of [[Stereochemistry#Computational representation]], N, COOH, CH₃ in priority order, has $V > 0$ and is S by the viewing rule). The same test, run on every Cα of a protein model, confirms that all residues are L.
- **Graph algorithms.** Detecting stereocenters is a [[Graph]] problem: compare the four branches leaving a vertex. For trees, canonical branch strings decide equality exactly (code below). Rings make branches infinite; the full CIP procedure explores outward from the center along paths and handles ties branch by branch, and is best left to tested toolkits for complex molecules.
- **Chirality without a stereocenter.** Helices are chiral as a whole: the α helix and B-DNA are right-handed, and their mirror images are not what cells make ([[Protein Secondary Structure]], [[DNA]]).[^berg]

## Mathematical representation

**Stereocenter.** In a molecular graph $G$ ([[Skeletal Formula#Mathematical representation]]), let $v$ be an sp³ atom with four substituents $s_1, \dots, s_4$ (heavy neighbours plus implicit hydrogens) and $B(v, s_i)$ the branch reached through $s_i$. Then $v$ is a stereocenter when the four branches are pairwise non-isomorphic as rooted labelled graphs.

**Labels as parity.** Rank the substituents $1 > 2 > 3 > 4$ with the CIP rules and take the reference order $r = (4, 1, 2, 3)$. If a SMILES string lists the neighbours in an order $w$ with tag $\tau \in \{@, @@\}$, let $\pi$ be the permutation taking $r$ to $w$ and $\sigma(\pi) \in \{0, 1\}$ its parity (number of inversions mod 2). Then

$$\text{label} = \begin{cases} \text{S} & \text{if } [\tau = @@] \oplus \sigma(\pi) = 1, \\ \text{R} & \text{otherwise,} \end{cases}$$

where $\oplus$ is exclusive or. In words: written as "lowest, 1, 2, 3", `@@` is S; each exchange of two neighbours flips the answer ([[Permutation]]).

## Computational representation

A toy pipeline on hydrogen-suppressed bond lists (as in [[Functional Group]]): find stereocenters by comparing canonical branch strings, rank substituents by a simplified CIP comparison (atomic numbers sphere by sphere), and read R or S from a SMILES-style neighbour order and tag.

```python
import re

Z = {"H": 1, "C": 6, "N": 7, "O": 8, "S": 16}
VALENCE = {"C": 4, "N": 3, "O": 2, "S": 2}

def build(spec: str):
    """'N1-C2 C2=O3' -> (elements, {atom: {neighbour: bond order}}, implicit H counts)."""
    el, adj = {}, {}
    for e1, i, b, e2, j in re.findall(r"([A-Z])(\d+)([-=])([A-Z])(\d+)", spec):
        el[i], el[j] = e1, e2
        adj.setdefault(i, {})[j] = adj.setdefault(j, {})[i] = 1 if b == "-" else 2
    return el, adj, {a: VALENCE[el[a]] - sum(adj[a].values()) for a in el}

def branch(mol, a, parent) -> str:
    """Canonical string of the branch entered at atom a from parent (acyclic molecules)."""
    el, adj, h = mol
    kids = sorted(f"{adj[a][b]}{branch(mol, b, a)}" for b in adj[a] if b != parent)
    return el[a] + "H" * h[a] + "(" + ",".join(kids) + ")"

def stereocenters(mol) -> list[str]:
    """sp3 atoms whose four substituents (heavy branches and implicit H) are pairwise different."""
    el, adj, h = mol
    subs = {a: [branch(mol, b, a) for b in adj[a]] + ["H"] * h[a] for a in el}
    return [a for a in el if len(subs[a]) == 4 and set(adj[a].values()) == {1} and len(set(subs[a])) == 4]

def cip_key(mol, start, center, depth=6) -> list[list[int]]:
    """Simplified CIP: atomic numbers sphere by sphere (high to low); a double bond duplicates its atom."""
    el, adj, h = mol
    key, frontier = [], [(start, center)]
    for _ in range(depth):
        key.append(sorted((1 if a == "H" else Z[el[a]] for a, _ in frontier), reverse=True))
        nxt = []
        for a, parent in frontier:
            if a != "H":
                nxt += [(b, a) for b, order in adj[a].items() if b != parent for _ in range(order)]
                nxt += [("H", a)] * h[a]
        if not nxt:
            break
        frontier = nxt
    return key

def rs_label(mol, center, written, tag) -> str:
    """R or S from the neighbours in SMILES order and the OpenSMILES tag '@' or '@@'."""
    ranked = sorted(written, key=lambda s: cip_key(mol, s, center), reverse=True)  # priority 1..4
    reference = [ranked[3]] + ranked[:3]       # lowest first, then 1, 2, 3: '@@' here means S
    perm = [reference.index(s) for s in written]
    odd = sum(x > y for i, x in enumerate(perm) for y in perm[i + 1:]) % 2
    return "S" if (tag == "@@") != bool(odd) else "R"

AMINO_ACIDS = {   # hydrogen-suppressed graphs: N1, C-alpha C2, side chain from C3, carboxyl C4
    "glycine": "N1-C2 C2-C4 C4=O5 C4-O6",
    "alanine": "N1-C2 C2-C3 C2-C4 C4=O5 C4-O6",
    "serine": "N1-C2 C2-C3 C3-O7 C2-C4 C4=O5 C4-O6",
    "cysteine": "N1-C2 C2-C3 C3-S7 C2-C4 C4=O5 C4-O6",
    "threonine": "N1-C2 C2-C3 C3-O7 C3-C8 C2-C4 C4=O5 C4-O6",
    "isoleucine": "N1-C2 C2-C3 C3-C7 C7-C8 C3-C9 C2-C4 C4=O5 C4-O6",
}
for name, spec in AMINO_ACIDS.items():
    mol = build(spec)
    centers = stereocenters(mol)
    # L arrangement: neighbours of C-alpha written N, H, side chain, carboxyl, with tag '@@'
    label = rs_label(mol, "2", ["1", "H", "3", "4"], "@@") if "2" in centers else "-"
    print(f"{name:11} stereocenters {centers}  L form at C-alpha: {label}")
citric = build("C1-O2 C1-C3 C3=O4 C3-O5 C1-C6 C6-C7 C7=O8 C7-O9 C1-C10 C10-C11 C11=O12 C11-O13")
print("citric acid stereocenters", stereocenters(citric))
```

```text
glycine     stereocenters []  L form at C-alpha: -
alanine     stereocenters ['2']  L form at C-alpha: S
serine      stereocenters ['2']  L form at C-alpha: S
cysteine    stereocenters ['2']  L form at C-alpha: R
threonine   stereocenters ['2', '3']  L form at C-alpha: S
isoleucine  stereocenters ['2', '3']  L form at C-alpha: S
citric acid stereocenters []
```

One spatial arrangement, two names: the code reproduces the textbook exception of cysteine.[^os26] The sphere comparison is a simplification of rule 2 that is exact for these molecules; it does not handle rings (the branch recursion assumes a tree).

## Worked example

> [!example] Why L-cysteine is R
> 1. **Atoms on Cα.** N (Z = 7), C of CH₂SH (6), C of COOH (6), H (1). Rule 1: N first, H last; the two carbons tie.
> 2. **Next sphere.** CH₂SH carries {S, H, H}; COOH carries {O, O, O} (C=O duplicated). Compare highest first: S (16) beats O (8), so CH₂SH wins at the first point of difference, even though COOH has more heavy atoms.
> 3. **Priorities.** NH₂ (1), CH₂SH (2), COOH (3), H (4). In L-alanine they were NH₂ (1), COOH (2), CH₃ (3).
> 4. **Same arrangement, swapped ranks.** L-cysteine has the same 3D arrangement as L-alanine with SH added to the methyl. Exchanging the ranks of two groups reverses the sense of 1 → 2 → 3: anticlockwise becomes clockwise, and S becomes R. R/S describes priorities, not biology: "all natural amino acids are L" is true; "all are S" is not.[^os26]

## Common misconceptions

> [!warning] "R/S tells you the sign of optical rotation"
> R and S come from a naming convention; (+) and (−) are measured. An R compound can be (+) or (−), and so can S.[^os5]

> [!warning] "More heavy atoms means higher priority"
> CIP compares atomic numbers at the first point of difference, highest first: {S, H, H} beats {O, O, O} because 16 > 8, regardless of how many atoms follow.[^os55]

> [!warning] "A carbon bonded to two CH₂ groups cannot be a stereocenter"
> Only identical **branches** disqualify it. In isoleucine, Cβ carries CH₃ and CH₂CH₃: both start with a carbon, but the branches differ, so Cβ is a stereocenter.[^lehninger]

## Exercises

> [!question] Exercise 1 (L1)
> Mark the stereocenters of lactic acid (CH₃–CH(OH)–COOH), glycerol (HOCH₂–CH(OH)–CH₂OH), butan-2-ol and glyceraldehyde (HOCH₂–CH(OH)–CHO).

> [!success]- Solution
> Lactic acid: C2 (CH₃, OH, COOH, H). Glycerol: none, C2 has two identical CH₂OH arms. Butan-2-ol: C2 (CH₃, C₂H₅, OH, H). Glyceraldehyde: C2 (CHO, CH₂OH, OH, H). Check glyceraldehyde with `stereocenters(build("O1-C2 C2-C3 C3-O4 C3-C5 C5=O6"))`, which returns `['3']`, its central carbon.

> [!question] Exercise 2 (L1)
> Rank the substituents of the stereocenter of glyceraldehyde: –OH, –CHO, –CH₂OH, –H.

> [!success]- Solution
> –OH (O, 8) first and –H last. –CHO and –CH₂OH tie on C; next sphere: CHO carries {O, O, H} (duplicated O), CH₂OH carries {O, H, H}. First difference at the second atom: O beats H, so –CHO > –CH₂OH. Order: OH > CHO > CH₂OH > H.[^os55]

> [!question] Exercise 3 (L2, Python)
> Using `rs_label` on alanine, show that `C[C@@H](C(=O)O)N` (neighbour order CH₃, H, COOH, N) describes the same molecule as `N[C@@H](C)C(=O)O`, and that `N[C@H](C)C(=O)O` is its enantiomer.

> [!success]- Solution
> ```python
> ala = build(AMINO_ACIDS["alanine"])
> print(rs_label(ala, "2", ["3", "H", "4", "1"], "@@"), rs_label(ala, "2", ["1", "H", "3", "4"], "@"))
> ```
> Output: `S R`. The first string reorders the neighbours by an even permutation of N, H, CH₃, COOH (a 3-cycle of N, CH₃ and COOH), so the same tag gives the same configuration, L-alanine. Changing only the tag gives the mirror image, D-alanine (R). A database must compare configurations, not strings.

> [!question] Exercise 4 (L2, Python)
> In a protein, how many stereocenters do the residues contribute? Write a function for a sequence, apply it to the invented peptide `GAVLITGCSA`, and give the number of stereoisomers with this constitution.

> [!success]- Solution
> Every residue except Gly has a Cα stereocenter, and Ile and Thr have a second one.[^berg][^lehninger]
> ```python
> def stereocenter_count(seq: str) -> int:
>     return sum(aa != "G" for aa in seq) + seq.count("I") + seq.count("T")
>
> k = stereocenter_count("GAVLITGCSA")
> print(k, 2 ** k)
> ```
> Output: `10 1024`. A ten-residue peptide already has 1024 stereoisomers with the same sequence of bonds; the ribosome makes one of them. For a 300-residue protein the number is astronomically large, which shows how strict the cell's choice of L-amino acids is.

> [!question] Exercise 5 (L3)
> Prove, from the parity rule, that (a) exchanging any two neighbours in a SMILES stereo atom while keeping the tag gives the enantiomer, and (b) cyclically rotating the last three neighbours keeps the configuration. Then explain why the first neighbour cannot simply be moved to the end.

> [!success]- Solution
> (a) An exchange is a transposition, an odd permutation: $\sigma$ changes from 0 to 1 or back, so the label flips. (b) A cyclic rotation of three elements is a 3-cycle, a product of two transpositions, hence even: $\sigma$ is unchanged. Moving the first neighbour to the end of four is a 4-cycle, a product of three transpositions: odd, so the tag would have to change to describe the same molecule. Geometrically, "looking from the first neighbour" changes the viewpoint; the rule hides this in the parity ([[Permutation]]).[^osm]

## Mastery checklist

- [ ] 1 Recognized: I can define chirality, stereocenter and enantiomer, and spot stereocenters in amino acids and simple sugars.
- [ ] 2 Understood: I can assign R or S with the CIP rules and explain why L-cysteine is R.
- [ ] 3 Practiced: I can detect stereocenters and compute R/S from a SMILES order and tag in code.
- [ ] 4 Applied: I checked the stereocenters and configurations of real compounds or protein residues from database records or structure files.
- [ ] 5 Explained: I can explain the independence of D/L, R/S and (+)/(−), and the parity logic behind stereo marks in SMILES.

## References

[^os5]: [[Organic Chemistry (OpenStax)]], ch. 5 "Stereochemistry at Tetrahedral Centers" (chirality, chirality centers, enantiomers, optical activity, meso compounds).
[^os55]: [[Organic Chemistry (OpenStax)]], ch. 5, section 5.5 "Sequence Rules for Specifying Configuration" (Cahn-Ingold-Prelog rules).
[^os512]: [[Organic Chemistry (OpenStax)]], ch. 5, section 5.12 "Chirality in Nature and Chiral Environments".
[^os26]: [[Organic Chemistry (OpenStax)]], ch. 26 "Biomolecules: Amino Acids, Peptides, and Proteins" (L-amino acids have the S configuration except cysteine, which is R).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of amino acids (L configuration, achiral glycine) and of protein and DNA helices (right-handed).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of amino acids (second stereocenter of isoleucine and threonine).
[^osm]: [[OpenSMILES Specification]], stereochemistry (`@` and `@@`: order of neighbours seen from the first neighbour).
