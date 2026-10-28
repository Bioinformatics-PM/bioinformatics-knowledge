---
aliases:
  - Tertiary Structure
  - Protein Fold
  - Fold
  - Structure tertiaire des protéines
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
  - "[[Protein Secondary Structure]]"
  - "[[Hydrophobic Effect]]"
  - "[[Amino Acid]]"
  - "[[Hydrogen Bond]]"
related:
  - "[[Protein Domain]]"
  - "[[Protein Quaternary Structure]]"
  - "[[Protein Folding]]"
  - "[[Molecular Visualization]]"
  - "[[PDB Format]]"
  - "[[Solvent Accessible Surface Area]]"
  - "[[Contact Map]]"
  - "[[Protein Structure Classification]]"
  - "[[Structural Alignment]]"
  - "[[Missense Mutation]]"
  - "[[Coulomb's Law]]"
  - "[[Water]]"
projects: []
sources:
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[RCSB Protein Data Bank]]"
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Chothia 1974 - Hydrophobic Bonding and Accessible Surface Area in Proteins]]"
  - "[[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]]"
  - "[[AlphaFold Protein Structure Database]]"
---

# Protein Tertiary Structure

> [!abstract]
> Tertiary structure is the complete 3D shape of one folded chain: how its helices, strands and loops pack around a water-free core, held by many weak interactions and sometimes by covalent disulfide bonds.

## Definition

**Tertiary structure** is the overall three-dimensional arrangement of all the atoms of one polypeptide chain, side chains included: it places residues that are far apart in the sequence next to each other, and it includes the pattern of disulfide bonds.[^berg][^lehninger] Two words describe it: a **fold**, the arrangement and connectivity of the secondary structure elements, and a **domain**, a compact region that folds on its own ([[Protein Domain]]).[^berg][^lehninger]

## Why it matters

- **Function sits in the fold.** Binding and active sites are built from residues that only meet once the chain is folded; myoglobin's oxygen-binding site uses two histidines buried inside the fold.[^berg]
- **Variant interpretation needs burial.** Folding gains free energy by burying nonpolar surface,[^chothia] so the same substitution means different things in the core and at the surface ([[Missense Mutation]], [[Solvent Accessible Surface Area]]).
- **Coordinates are the data.** A tertiary structure is a list of atoms with $x, y, z$ coordinates in a PDB entry ([[PDB Format]]); its experimental method and resolution must be read before trusting the details.[^pdb]
- **Folds outlive sequences.** Structure is more conserved than sequence in evolution,[^berg] so fold comparison ([[Structural Alignment]]) and fold classification ([[Protein Structure Classification]]) find relatives that sequence search misses.

## Core (L2)

![[tertiary-structure-domains-forces.svg]]

### From secondary elements to folds and domains

- **Motifs** (supersecondary structures) are recurring combinations of secondary elements, such as the helix-turn-helix of many DNA-binding proteins,[^berg] or a β hairpin (two antiparallel strands joined by a turn, [[Protein Secondary Structure]]).
- **Domains** are compact globular units of about 30 to 400 residues, often joined by flexible segments; the cell-surface protein CD4 has four similar domains of about 100 residues each.[^berg] How domains are delimited and classified is the subject of [[Protein Domain]].
- **Folds** are classified by their secondary structure content into classes such as all α, all β, α/β (helices and strands alternating along the chain) and α + β (helices and strands in separate regions), the top level of databases such as SCOP.[^lehninger]

### What holds a fold together

| Interaction | Between | Role in the fold |
|---|---|---|
| [[Hydrophobic Effect]] | nonpolar side chains, away from water | main driving force: builds the core[^berg] |
| van der Waals contacts | closely packed atoms | many weak contacts in a compact interior[^berg] |
| [[Hydrogen Bond\|Hydrogen bonds]] | backbone (helices, sheets) and polar side chains | pair the polar groups, including buried ones[^berg] |
| Ionic interactions (salt bridges) | Lys, Arg with Asp, Glu | screened by water, about 80 times weaker than in vacuum[^berg][^uphys] |
| Disulfide bonds | two Cys, covalent S–S | mainly in extracellular proteins[^alberts] |

**The core.** Myoglobin, 153 residues folded into a compact 45 × 35 × 25 Å molecule with about 70 % of its chain in eight α helices, is the reference case. Its interior holds almost only nonpolar residues (Leu, Val, Met, Phe); Asp, Glu, Lys and Arg are absent from it; the only polar residues inside are two histidines that bind the iron and the oxygen. The surface carries both polar and nonpolar residues.[^berg] In a nonpolar core there is no water to hydrogen-bond the backbone N–H and C=O groups; helices and sheets pair them internally ([[Protein Secondary Structure]]), which is how the chain can cross its own core.

**Charges.** Water's dielectric constant, about 80, divides the Coulomb energy between two charges by 80 relative to vacuum ([[Coulomb's Law]]).[^uphys] A surface salt bridge is therefore worth only a few kJ/mol (Exercise 4), and moving a charge into the low-dielectric core costs its hydration, which is why charged side chains sit mostly at the surface ([[Water#Deeper (L2)]]).

**Disulfides.** Extracellular proteins are often cross-linked by disulfide bonds, formed in the endoplasmic reticulum as the proteins are prepared for export. They do not form in the cytosol, where a high concentration of reducing agents converts S–S bonds back to –SH groups.[^alberts] Most intracellular proteins therefore fold and stay folded without them ([[Endomembrane System]]).

### Inspecting a structure in a viewer

A viewer turns the coordinate list into a picture you can question ([[Molecular Visualization]]): the RCSB.org 3D viewer, PyMOL or ChimeraX. A minimal inspection routine:[^pdb]

1. **Read the entry**: experimental method and resolution, number of chains, ligands (HETATM records, such as a heme).
2. **Cartoon, colored N → C**: follow the chain through its helices and strands; find the domains.
3. **Show nonpolar side chains** (or a surface colored by hydrophobicity): they should fill the interior.
4. **Look for specific contacts**: Cys–Cys pairs (disulfides), Lys/Arg next to Asp/Glu (salt bridges), the residues around a ligand.
5. **Compare with a predicted model** of the same protein, colored by confidence.[^afdb]

## Advanced (L3)

**Burial as a number.** The hydrophobic free energy relates to the accessible surface area buried on folding,[^chothia] so residue exposure is computed from coordinates: as solvent accessible surface area ([[Solvent Accessible Surface Area]]) or, more crudely, by counting neighbors (Computational representation). Exposure is a natural first structural feature to check for a variant: in the core, a substitution changes packing and the hydrophobic balance; at the surface, it mostly changes contacts with water and with partners.

**Fold space.** Because structure is more conserved than sequence,[^berg] proteins with undetectable sequence similarity can share a fold. Classification databases organize structures from class down to family ([[Protein Structure Classification]]), and [[Structural Alignment]] compares two folds directly, independently of sequence.

**Predicted folds.** AlphaFold 2 predicts the tertiary structure of single chains with a per-residue confidence; low-confidence regions should be treated as unknown, not as a structure to interpret.[^jumper][^afdb] Domain boundaries, buried residues and contacts read from a model inherit its confidence ([[Protein Structure Prediction]]).

## Mathematical representation

- **Coordinates.** A chain of $N$ residues is $X = (x_1, \dots, x_N) \in \mathbb{R}^{N \times 3}$ (one point per residue for a Cα trace, or one per atom). Its shape is invariant under rotation and translation, so it is compared through distances $d_{ij} = \lVert x_i - x_j \rVert$ or after superposition ([[Contact Map]], [[Root-Mean-Square Deviation]]).
- **Radius of gyration**, with centroid $\bar{x} = \frac{1}{N}\sum_i x_i$: $R_g = \sqrt{\frac{1}{N}\sum_{i=1}^{N} \lVert x_i - \bar{x} \rVert^2}$.
- **Compact versus extended.** If each residue occupies a volume $v_0$, a compact globule has volume $N v_0$ and radius $R = (3 N v_0 / 4\pi)^{1/3}$, so $R_g \propto N^{1/3}$ (for a uniform sphere $R_g = \sqrt{3/5}\,R$). A straight chain of $N$ points spaced by $a$ has $R_g = a\sqrt{(N^2 - 1)/12} \approx aN/\sqrt{12}$, proportional to $N$.
- **Burial proxy.** $n_i = \sum_{j \ne i} \mathbf{1}[d_{ij} < r_c]$, the number of atoms within a radius $r_c$ of residue $i$; larger means more buried.
- **Interactions as distance predicates.** A disulfide when $d(\mathrm{S}\gamma_i, \mathrm{S}\gamma_j) < \delta_{SS}$; a salt bridge when the closest charged N and O atoms satisfy $d < \delta_{ion}$. The thresholds ($2.5$ and $4.0$ Å below) are choices to report with any result.
- **Screened Coulomb energy** of two charges $q_1, q_2$ (in units of $e$) at distance $r$ in a medium of dielectric constant $\varepsilon$: $E = \dfrac{k\, q_1 q_2}{\varepsilon\, r}$, with $k = \dfrac{e^2 N_A}{4\pi\varepsilon_0} \approx 1389$ kJ Å mol⁻¹ ($e$ the elementary charge, $N_A$ Avogadro's number, $\varepsilon_0$ the vacuum permittivity; Exercise 4).[^nist]

## Computational representation

A structure file is a table of atoms. The PDB format fixes each field to columns (residue name in columns 18 to 20, coordinates in 31 to 54), so a few slices read it ([[PDB Format]]). The first part finds a disulfide and a salt bridge in invented coordinates; the second builds a toy three-helix bundle (ideal helices of [[Protein Structure#Computational representation]], one pseudo side-chain atom per residue) and measures burial and compactness.

```python
import math
from itertools import combinations

PDB = """\
ATOM    101  SG  CYS A  12      10.000   5.000   3.000  1.00 20.00           S
ATOM    170  NZ  LYS A  21      15.000  12.000   1.000  1.00 20.00           N
ATOM    230  SG  CYS A  30       2.000  14.000   8.000  1.00 20.00           S
ATOM    260  NH1 ARG A  33       4.000   2.000  12.000  1.00 20.00           N
ATOM    261  NH2 ARG A  33       4.800   1.200  13.600  1.00 20.00           N
ATOM    360  OE1 GLU A  45      17.600  13.200   1.500  1.00 20.00           O
ATOM    361  OE2 GLU A  45      17.900  11.300   0.400  1.00 20.00           O
ATOM    480  SG  CYS A  58      11.950   5.400   3.300  1.00 20.00           S
ATOM    560  OD1 ASP A  70       9.000   2.500  12.500  1.00 20.00           O
ATOM    561  OD2 ASP A  70       9.900   3.300  11.700  1.00 20.00           O
"""  # invented coordinates in the PDB fixed-column layout


def parse_atoms(text: str) -> list[dict]:
    """Read ATOM/HETATM records by column position."""
    return [{"atom": line[12:16].strip(), "res": line[17:20], "num": int(line[22:26]),
             "xyz": (float(line[30:38]), float(line[38:46]), float(line[46:54]))}
            for line in text.splitlines() if line.startswith(("ATOM  ", "HETATM"))]


POSITIVE = {("LYS", "NZ"), ("ARG", "NE"), ("ARG", "NH1"), ("ARG", "NH2")}
NEGATIVE = {("ASP", "OD1"), ("ASP", "OD2"), ("GLU", "OE1"), ("GLU", "OE2")}


def disulfides(atoms: list[dict], cutoff: float = 2.5) -> list[tuple]:
    sg = [a for a in atoms if (a["res"], a["atom"]) == ("CYS", "SG")]
    return [(a["num"], b["num"], round(math.dist(a["xyz"], b["xyz"]), 2))
            for a, b in combinations(sg, 2) if math.dist(a["xyz"], b["xyz"]) < cutoff]


def ion_pairs(atoms: list[dict]) -> dict[tuple, float]:
    """Shortest distance between each basic and each acidic side chain (charged atoms only)."""
    best = {}
    for p in (a for a in atoms if (a["res"], a["atom"]) in POSITIVE):
        for n in (a for a in atoms if (a["res"], a["atom"]) in NEGATIVE):
            key = (f"{p['res']}{p['num']}", f"{n['res']}{n['num']}")
            best[key] = min(best.get(key, math.inf), round(math.dist(p["xyz"], n["xyz"]), 2))
    return best


atoms = parse_atoms(PDB)
print("disulfides:", disulfides(atoms))
print("salt bridges (< 4 Å):", {k: d for k, d in ion_pairs(atoms).items() if d < 4.0})


def bundle(n_res: int = 16, n_helix: int = 3, r_bundle: float = 7.0) -> list[dict]:
    """Toy fold: parallel ideal helices around the z axis; Cα 2.3 Å from each helix axis
    (100° and 1.5 Å per residue), one pseudo side-chain atom 4.7 Å from the helix axis."""
    out = []
    for h in range(n_helix):
        c = 2 * math.pi * h / n_helix
        cx, cy = r_bundle * math.cos(c), r_bundle * math.sin(c)
        for k in range(n_res):
            a = math.radians(100 * k + 40 * h)
            out.append({"helix": h, "k": k,
                        "ca": (cx + 2.3 * math.cos(a), cy + 2.3 * math.sin(a), 1.5 * k),
                        "sc": (cx + 4.7 * math.cos(a), cy + 4.7 * math.sin(a), 1.5 * k)})
    return out


def burial(fold: list[dict], radius: float = 8.0) -> list[int]:
    """Burial proxy: Cα atoms of the other helices within radius of each side chain."""
    return [sum(math.dist(r["sc"], q["ca"]) < radius for q in fold if q["helix"] != r["helix"])
            for r in fold]


def radius_of_gyration(points: list[tuple]) -> float:
    c = [sum(p[k] for p in points) / len(points) for k in range(3)]
    return math.sqrt(sum(math.dist(p, c) ** 2 for p in points) / len(points))


fold = bundle()
contacts = burial(fold)
buried = [r["k"] for r, n in zip(fold, contacts) if r["helix"] == 0 and n > 0]
print("helix 0 buried positions:", buried, "spacings:", [b - a for a, b in zip(buried, buried[1:])])
extended = [(3.5 * i, 0.0, 0.0) for i in range(len(fold))]
print(f"Rg: folded {radius_of_gyration([r['ca'] for r in fold]):.1f} Å, "
      f"extended {radius_of_gyration(extended):.1f} Å ({len(fold)} residues)")
```

```text
disulfides: [(12, 58, 2.01)]
salt bridges (< 4 Å): {('LYS21', 'GLU45'): 2.91}
helix 0 buried positions: [2, 5, 6, 9, 12, 13] spacings: [3, 1, 3, 3, 1]
Rg: folded 10.1 Å, extended 48.5 Å (48 residues)
```

Cys 30 is free and Arg 33 sits 4.53 Å from Asp 70, just beyond the threshold: a different cutoff changes the list, which is why thresholds must be reported. In the bundle, the residues facing the other helices recur at positions $i, i + 3, i + 4, i + 7$: each residue turns 100°, so 3 and 4 residues later the side chain points within 60° of the same direction, and 7 residues (700°) almost exactly so. A sequence that folds into this bundle must put its nonpolar residues at these positions to bury them. Folding shrinks the 48-residue chain from $R_g$ = 48.5 Å (extended, $\propto N$) to 10.1 Å.

## Worked example

> [!example] Inspecting myoglobin in a viewer
> PDB entry **1MBN** is sperm whale myoglobin, determined by X-ray crystallography at 2 Å resolution (Watson and Kendrew).[^pdb]
> 1. **Entry.** Myoglobin is a single chain carrying one heme group;[^berg] in the file, the heme is a HETATM ligand. Note the method and the 2 Å resolution before discussing atomic details.
> 2. **Cartoon.** About 70 % of the 153 residues form eight α helices,[^berg] so about 107 helical residues, about 13 per helix, or $13 \times 1.5 \approx 20$ Å per helix: each helix spans roughly half of the 45 Å longest dimension, and the chain crosses the molecule back and forth.
> 3. **Nonpolar side chains** (Leu, Val, Met, Phe) fill the interior; no Asp, Glu, Lys or Arg is buried.[^berg]
> 4. **The heme pocket.** Two histidines, the only polar residues inside, sit at the heme: they bind the iron and the oxygen.[^berg] The exception confirms the rule: these buried polar groups are there because the function needs them.
> 5. **What is not there.** A single chain has no quaternary structure; compare with hemoglobin, made of four myoglobin-like chains ([[Protein Quaternary Structure]]).

## Common misconceptions

> [!warning] "A salt bridge is as strong as an ionic bond in a salt crystal"
> In water, the Coulomb energy is divided by about 80:[^uphys] about −4 kJ/mol at 4 Å instead of about −350 kJ/mol in vacuum (Exercise 4). Surface salt bridges are weak, and burying charges is costly. The fold is driven by burying nonpolar groups, not by ion pairs.[^berg]

> [!warning] "Disulfide bonds are what hold proteins together"
> Most intracellular proteins have none: the cytosol is reducing.[^alberts] Disulfides stabilize many extracellular proteins, but the fold itself is encoded by the whole sequence, and native disulfides form correctly only when the chain folds correctly ([[Protein Folding]]).

> [!warning] "Nonpolar residues are inside, polar residues outside, without exception"
> It is a strong tendency, not a law: myoglobin's surface carries nonpolar residues too, and two polar histidines are buried for function.[^berg] Buried polar groups are hydrogen-bonded or coordinated, otherwise they cost stability.

## Exercises

> [!question] Exercise 1 (L2)
> Name the interaction in each case (invented distances): (a) Cys 15 Sγ to Cys 88 Sγ, 2.0 Å; (b) Lys 40 Nζ to Asp 12 Oδ1, 3.0 Å; (c) Leu 30 and Phe 75 side chains packed in the interior; (d) Ser 52 Oγ to the backbone O of residue 49, 2.8 Å; (e) Lys 40 Nζ to Arg 77 Nη1, 3.5 Å.

> [!success]- Solution
> (a) Disulfide: a covalent bond, the only one in the list. (b) Salt bridge (ionic interaction screened by water). (c) Hydrophobic packing with van der Waals contacts. (d) Side chain to backbone hydrogen bond. (e) Two positive charges close together: repulsive, a destabilizing contact, unless something negative or a hydrogen-bonding network sits between them.

> [!question] Exercise 2 (L2)
> A cytosolic enzyme and a secreted toxin each contain six cysteines. Which is likely to carry disulfide bonds? A biotechnologist expresses the toxin in the cytosol of a cell: what may go wrong?

> [!success]- Solution
> The secreted toxin: disulfides form in the endoplasmic reticulum on the way out, while the reducing cytosol keeps the enzyme's cysteines as free –SH groups.[^alberts] Made in the cytosol, the toxin cannot form its disulfides, so it may fold poorly, be unstable or aggregate, even though its sequence is unchanged ([[Protein Folding]]).

> [!question] Exercise 3 (L2)
> A compact 100-residue domain has $R_g = 13$ Å (invented value). Predict $R_g$ for a compact single domain of 400 residues, and for the 100-residue chain fully extended at 3.5 Å per residue. A 400-residue protein is measured at $R_g = 35$ Å: give two explanations.

> [!success]- Solution
> Compact: $R_g \propto N^{1/3}$, so $13 \times 4^{1/3} = 13 \times 1.587 \approx 20.6$ Å. Extended: $3.5\sqrt{(100^2 - 1)/12} \approx 101$ Å. 35 Å is far above the compact estimate: the protein is not a single compact globule, for example several domains joined by linkers, an elongated fold, or a partly unfolded chain.

> [!question] Exercise 4 (L3, Python)
> Compute $k = e^2 N_A / 4\pi\varepsilon_0$ in kJ Å mol⁻¹, then the energy of a +1/−1 pair at 3, 4 and 6 Å for $\varepsilon = 1$ (vacuum), 4 (a toy low-dielectric interior) and 80 (water). What does the table say about surface and buried salt bridges?

> [!success]- Solution
> ```python
> e, eps0, NA = 1.602176634e-19, 8.8541878128e-12, 6.02214076e23   # C, F/m, 1/mol
> k = e ** 2 * NA / (4 * math.pi * eps0) * 1e10 / 1000             # J·m/mol -> kJ·Å/mol
> print(f"k = {k:.1f} kJ·Å/mol")
> for eps in (1, 4, 80):
>     print(eps, [round(-k / (eps * r), 1) for r in (3.0, 4.0, 6.0)])
> ```
> ```text
> k = 1389.4 kJ·Å/mol
> 1 [-463.1, -347.3, -231.6]
> 4 [-115.8, -86.8, -57.9]
> 80 [-5.8, -4.3, -2.9]
> ```
> At the surface ($\varepsilon \approx 80$),[^uphys] a salt bridge is worth a few kJ/mol, about one or two $RT$ at room temperature. In a low-dielectric interior the attraction is 20 times stronger, but each charge first loses its hydration ([[Water#Deeper (L2)]]): a buried ion pair is not automatically a gain, and an unpaired buried charge is a large cost. The constants are from the CODATA set.[^nist]

> [!question] Exercise 5 (L3, Python)
> Model a charge reversal K21E in the toy structure by renaming Lys 21 Nζ as a Glu Oε1 at the same position. Recompute the salt bridges and list acidic pairs closer than 4 Å. What would you predict for stability?

> [!success]- Solution
> ```python
> mutant = PDB.replace("NZ  LYS A  21", "OE1 GLU A  21")    # same columns, toy charge reversal
> m = parse_atoms(mutant)
> print("salt bridges:", {key: d for key, d in ion_pairs(m).items() if d < 4.0})
> acidic = [a for a in m if (a["res"], a["atom"]) in NEGATIVE]
> same = {}
> for a, b in combinations(acidic, 2):
>     if a["num"] != b["num"]:
>         key = (f"{a['res']}{a['num']}", f"{b['res']}{b['num']}")
>         same[key] = min(same.get(key, math.inf), round(math.dist(a["xyz"], b["xyz"]), 2))
> print("acidic pairs < 4 Å:", {key: d for key, d in same.items() if d < 4.0})
> ```
> ```text
> salt bridges: {}
> acidic pairs < 4 Å: {('GLU21', 'GLU45'): 2.91}
> ```
> The attraction is lost and replaced by a repulsion between two carboxylates at 2.9 Å. In a real protein the side chains would move apart, so the cost is smaller than the frozen picture suggests, but the substitution is predicted to destabilize; on the surface, where screening is strong, the effect is modest. Checking which charged partners a residue has in the structure is a first step of variant interpretation ([[Missense Mutation]]).

> [!question] Exercise 6 (L3)
> Open 1MBN on RCSB.org, then the AlphaFold model of a myoglobin. Which features should agree, where would you expect disagreement, and which entry would you trust for the heme pocket?

> [!success]- Solution
> The eight-helix fold and the nonpolar core should agree: they are what the sequence encodes. The heme is a ligand: a model of the chain alone has no heme, so side chains of the pocket may differ, and low-confidence termini should not be interpreted.[^jumper][^afdb] For the pocket, trust the experimental entry, after checking its method and resolution.[^pdb] Different species add sequence differences: compare like with like.

## Mastery checklist

- [ ] 1 Recognized: I can define tertiary structure, fold, motif and domain, and give myoglobin as an example.
- [ ] 2 Understood: I can explain the hydrophobic core, why buried backbone needs secondary structure, why salt bridges are weak in water and why disulfides are extracellular.
- [ ] 3 Practiced: I can parse PDB atom records, find disulfides and salt bridges with stated thresholds, and compute burial and radius of gyration.
- [ ] 4 Applied: I inspected real entries in a viewer (core, ligands, disulfides) and compared an experimental structure with its predicted model.
- [ ] 5 Explained: I can teach how burial and electrostatics guide variant interpretation, and what experimental resolution and prediction confidence allow us to conclude.

## References

[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of tertiary structure (residues far apart in sequence, disulfide pattern), myoglobin (153 residues, 45 × 35 × 25 Å, about 70 % of the chain in eight α helices, nonpolar interior, two buried histidines, mixed surface), motifs and domains (helix-turn-helix, CD4, 30 to 400 residues), noncovalent bonds and the hydrophobic driving force, fold classes conserved more than sequence.
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of tertiary structure, folds and domains, and structural classification of proteins (SCOP classes all α, all β, α/β, α + β).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of extracellular proteins stabilized by disulfide bonds formed in the endoplasmic reticulum, and of the reducing cytosol.
[^pdb]: [[RCSB Protein Data Bank]], entry pages (experimental method, resolution, chains and ligands) and 3D viewer; entry 1MBN, "The stereochemistry of the protein myoglobin", sperm whale, X-ray diffraction at 2 Å (checked on the wwPDB archive record).
[^uphys]: [[University Physics (OpenStax)]], Volume 2: Coulomb's law and dielectrics (dielectric constant of water about 80).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA values of the elementary charge, the Avogadro constant and the vacuum electric permittivity.
[^chothia]: [[Chothia 1974 - Hydrophobic Bonding and Accessible Surface Area in Proteins]], *Nature* 248:338-339.
[^jumper]: [[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]], *Nature* 596:583-589.
[^afdb]: [[AlphaFold Protein Structure Database]], Varadi M et al., *Nucleic Acids Research* 52:D368-D375 (2024).
