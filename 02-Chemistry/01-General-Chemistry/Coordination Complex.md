---
aliases:
  - Coordination Compound
  - Metal Complex
  - Chelate
  - Chelation
  - Coordinate Covalent Bond
  - Dative Bond
  - Coordination Number
  - Complexe de coordination
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Lewis Structure]]"
  - "[[Electron Configuration]]"
  - "[[Ionic Bond]]"
  - "[[Covalent Bond]]"
  - "[[Molecular Geometry]]"
  - "[[Acid-Base Reaction]]"
related:
  - "[[Cofactor]]"
  - "[[ATP]]"
  - "[[Enzyme Catalysis]]"
  - "[[DNA Replication]]"
  - "[[Transcription Factor]]"
  - "[[Cooperativity]]"
  - "[[Redox Reaction]]"
  - "[[PDB Format]]"
  - "[[Molecular Orbital Theory]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Yang 2006 - Making and Breaking Nucleic Acids - Two-Mg2+-Ion Catalysis and Substrate Specificity]]"
  - "[[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]]"
---

# Coordination Complex

> [!abstract]
> A coordination complex is a metal ion surrounded by molecules or ions, its ligands, that each donate an electron pair to it; how many ligands it holds and how they are arranged give the complex its geometry, and in proteins they decide where a metal binds and what it does.

## Definition

A **coordination complex** (coordination compound) is a central metal atom or ion bonded to a set of **ligands**: molecules or ions that each donate at least one electron pair. Each metal-ligand bond is a **coordinate covalent bond**, both of whose electrons come from the ligand, a Lewis base; the metal acts as a Lewis acid ([[Acid-Base Reaction]]). The **coordination number** is the number of donor atoms bonded to the metal. A ligand that binds through one donor atom is **monodentate**; one that binds through several is **polydentate**, and the complex it forms is a **chelate**, from the Greek for claw.[^c2e192]

## Why it matters

- **Metals in structure files.** A metal in an experimental structure is one atom whose ligands are the protein or nucleic acid atoms around it: finding the site, its coordination number and its geometry is a computation on coordinates ([[PDB Format]], Computational representation). AlphaFold 2 models a single protein chain, so a predicted metal site comes without its metal.[^jumper]
- **Every polymerase is a metalloenzyme.** All DNA and RNA polymerases hold two Mg²⁺ ions at their active site,[^yang] so any reaction that uses one, from [[DNA Replication]] to a [[Polymerase Chain Reaction]], needs Mg²⁺, and a chelator that captures it stops the enzyme (Exercise 5).
- **ATP is used as a metal complex.** The true substrate of essentially all NTP-dependent enzymes is the Mg²⁺ complex of the nucleotide, not the free nucleotide ([[ATP]]).[^berg9]
- **DNA binding and oxygen transport.** Zinc fingers, a family of DNA-binding motifs of [[Transcription Factor|transcription factors]], fold around a zinc ion;[^alberts] myoglobin and hemoglobin carry O₂ on the iron of heme.[^lehninger]

## Core (L2)

![[metal-sites-heme-iron-zinc-finger.svg]]

### Coordination number and geometry

The common geometries are tetrahedral or square planar for coordination number 4 and octahedral for coordination number 6.[^c2e192] The ideal angles follow from placing the donor atoms as far apart as possible, as for the electron pairs of VSEPR ([[Molecular Geometry]]):

| Coordination number | Geometry | Ideal L–M–L angles | Biological example |
|---:|---|---|---|
| 4 | tetrahedral | 109.5° (× 6) | Zn²⁺ of a Cys₂His₂ zinc finger |
| 4 | square planar | 90° (× 4), 180° (× 2) | the four porphyrin N of heme, the equatorial plane of the iron |
| 5 | square pyramidal | 90° (× 8), 180° (× 2) | deoxy heme iron: four N + His |
| 6 | octahedral | 90° (× 12), 180° (× 3) | oxy heme iron: four N + His + O₂ |

### Charge and electron count

- **Charge bookkeeping.** The charge of a complex is the metal's charge plus the ligands' charges. Neutral donors (water, the imidazole of His) add nothing; anionic ones (Cys thiolate, Asp or Glu carboxylate, phosphate oxygens) cancel part of the metal's charge.
- **d electrons.** Transition metals lose their 4s electrons first: Fe²⁺ is [Ar] 3d⁶ and Zn²⁺ [Ar] 3d¹⁰, while Mg²⁺ has the configuration of neon ([[Electron Configuration]]).[^c2e64] With its d shell full, Zn²⁺ has no electronic reason to prefer the square-planar arrangement, and its four ligands spread to the corners of a tetrahedron, as four bonding pairs do in VSEPR.

### Chelates

A polydentate ligand grips the metal at several points: ethylenediamine (two N) is bidentate and the porphyrin of heme (four N) is tetradentate.[^c2e192] EDTA, ethylenediamine-tetraacetate, carries two amine nitrogens and four carboxylates, six donor atoms in one molecule: wrapped around one metal ion, it fills all six positions of an octahedron.

### Bio: four metal sites

- **Mg²⁺ and ATP.** In cells ATP is mostly complexed with Mg²⁺, which binds oxygens of the phosphate chain, shields part of its negative charge and influences its conformation;[^lehninger] Mg²⁺-NTP complexes are the true substrates of essentially all NTP-dependent enzymes.[^berg9]
- **Two Mg²⁺ in polymerases.** In all DNA and RNA polymerases, and in many nucleases and transposases, two Mg²⁺ ions are held jointly by catalytic residues of the enzyme and by the nucleic acid substrate. Mg²⁺ is sensitive to the geometry and charge of its ligands, so the pair also helps the enzyme accept only a correctly placed substrate.[^yang]
- **Zinc fingers.** In the Cys-Cys-His-His family of zinc finger proteins, named after the residues that grasp the zinc, a Zn²⁺ ion holds an α helix and a β sheet together; fingers often come in tandem, the helix of each contacting the major groove of DNA.[^alberts] Here the zinc is structural: it holds the fold together.
- **Heme iron.** In myoglobin and hemoglobin, the Fe²⁺ of heme has six coordination bonds: four to the nitrogens of the flat porphyrin ring and two perpendicular to it, one to a histidine of the protein (the proximal His) and one for O₂. Only Fe²⁺ binds O₂ reversibly, not Fe³⁺, and burying the heme inside the protein protects the iron from oxidation.[^lehninger] In deoxyhemoglobin the iron sits slightly out of the porphyrin plane; O₂ binding pulls it into the plane, dragging the proximal His and its helix, a motion that is passed on between subunits ([[Cooperativity]]).[^berg10]

## Advanced (L3)

- **Metal ions are Lewis-acid catalysts.** Enzymes use bound metal ions to stabilize negative charges that develop during a reaction and to make bound water more acidic.[^berg9] In carbonic anhydrase, a Zn²⁺ held by three His also binds a water molecule whose pKa drops from 15.7 to about 7, so the zinc-bound hydroxide, a strong nucleophile, is present at neutral pH and attacks CO₂.[^berg9] At pH 7.4, 72 % of the zinc-bound water is OH⁻, against 5 × 10⁻⁹ for free water (code below).
- **Two-metal-ion catalysis.** In the polymerase reaction, the 3′-OH of the primer attacks the α-phosphate of the incoming nucleotide and pyrophosphate leaves.[^berg27] The two Mg²⁺ ions sit between the enzyme's catalytic residues and these phosphates;[^yang] like any metal-ion catalyst, they position the reacting groups and stabilize the negative charge of the transition state.[^berg9]
- **Crystal field theory.** The colors and magnetic properties of transition-metal complexes come from the splitting of the metal's d-orbital energies by its ligands, the subject of crystal field theory; this curriculum only skims it.[^c2e19]
- **Metal sites in structural data.** Assigning a metal and its ligands from coordinates depends on the distance cutoff: too short and real ligands are missed, too long and second-shell atoms are counted as ligands (Exercise 4). A predicted model needs its metals added and checked separately (Exercise 6).[^jumper]

## Mathematical representation

- **Coordination shell.** For a metal at $\mathbf m$ and candidate donors at $\mathbf x_a$: $L(\mathbf m) = \{a : \lVert \mathbf x_a - \mathbf m \rVert \le r_c\}$, coordination number $n = |L|$, with $r_c$ a chosen cutoff.
- **Angles.** With unit vectors $\mathbf u_a = (\mathbf x_a - \mathbf m)/\lVert \mathbf x_a - \mathbf m \rVert$, the $\binom n2$ ligand-metal-ligand angles are $\theta_{ab} = \arccos(\mathbf u_a \cdot \mathbf u_b)$. For a regular tetrahedron with vertices $(1,1,1)$, $(1,-1,-1)$, $(-1,1,-1)$, $(-1,-1,1)$, $\cos\theta = -\frac13$, so $\theta = 109.47°$.
- **Geometry score.** Sort the measured angles $\theta_{(i)}$ and those of each ideal geometry $g$ with the same $n$; $\mathrm{RMS}_g = \sqrt{\binom n2^{-1} \sum_i (\theta_{(i)} - \theta^{g}_{(i)})^2}$, and the smallest RMS names the geometry.
- **Charge.** $q_{\text{complex}} = q_M + \sum_{a \in L} q_a$.
- **Lewis acidity as a pKa shift.** A metal-bound water with acid constant $K_a$ is present as hydroxide in the fraction $f = 1/(1 + 10^{\,\mathrm{p}K_a - \mathrm{pH}})$ ([[Henderson-Hasselbalch Equation]]).

## Computational representation

A metal site is a point with neighbours: distances give the shell, angles the geometry.

```python
import math

S3 = 1 / math.sqrt(3)
IDEAL = {   # unit vectors from the metal to its donor atoms
    "tetrahedral": [(S3, S3, S3), (S3, -S3, -S3), (-S3, S3, -S3), (-S3, -S3, S3)],
    "square planar": [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)],
    "square pyramidal": [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1)],
    "trigonal bipyramidal": [(1, 0, 0), (-0.5, 3 ** 0.5 / 2, 0), (-0.5, -(3 ** 0.5) / 2, 0), (0, 0, 1), (0, 0, -1)],
    "octahedral": [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)],
}


def angle(u, v) -> float:
    cos = sum(a * b for a, b in zip(u, v)) / (math.hypot(*u) * math.hypot(*v))
    return math.degrees(math.acos(max(-1.0, min(1.0, cos))))


def pair_angles(vectors) -> list[float]:
    """All ligand-metal-ligand angles, sorted."""
    return sorted(angle(vectors[i], vectors[j])
                  for i in range(len(vectors)) for j in range(i + 1, len(vectors)))


def shell(metal, atoms: dict, cutoff: float = 2.6) -> dict:
    """Donor atoms within `cutoff` Å of the metal -> vector from the metal to the atom."""
    return {name: tuple(b - a for a, b in zip(metal, xyz))
            for name, xyz in atoms.items() if math.dist(metal, xyz) <= cutoff}


def classify(vectors) -> list[tuple[float, str]]:
    """Ideal geometries with the same coordination number, ranked by RMS angle deviation (degrees)."""
    measured = pair_angles(vectors)
    ranking = []
    for name, ideal in IDEAL.items():
        if len(ideal) == len(vectors):
            ref = pair_angles(ideal)
            rms = math.sqrt(sum((m - r) ** 2 for m, r in zip(measured, ref)) / len(ref))
            ranking.append((round(rms, 1), name))
    return sorted(ranking)


# Invented toy coordinates (Å), metal at the origin
ZINC_SITE = {"SG Cys1": (1.38, 1.27, 1.31), "SG Cys2": (1.29, -1.36, -1.30),
             "NE2 His1": (-1.22, 1.15, -1.17), "NE2 His2": (-1.15, -1.21, 1.19),
             "CB Cys1": (2.20, 2.40, 1.10), "CE1 His1": (-2.10, 1.60, -1.90), "O water": (0.50, 0.20, 3.60)}
HEME_OXY = {"N pyrrole A": (2.00, 0.03, 0.01), "N pyrrole B": (-0.02, 2.01, 0.02),
            "N pyrrole C": (-2.01, -0.02, -0.01), "N pyrrole D": (0.01, -1.99, 0.03),
            "NE2 His prox": (0.05, -0.04, -2.12), "O1 dioxygen": (0.06, 0.12, 1.82),
            "O2 dioxygen": (0.20, 1.10, 2.60), "C porphyrin": (2.85, 1.10, 0.00)}

for label, atoms in (("zinc site", ZINC_SITE), ("oxy heme", HEME_OXY)):
    s = shell((0.0, 0.0, 0.0), atoms)
    angles = pair_angles(list(s.values()))
    print(label, "CN =", len(s), {n: round(math.hypot(*v), 2) for n, v in s.items()})
    print("   angles", round(angles[0], 1), "to", round(angles[-1], 1), "->", classify(list(s.values())))
```

```text
zinc site CN = 4 {'SG Cys1': 2.29, 'SG Cys2': 2.28, 'NE2 His1': 2.04, 'NE2 His2': 2.05}
   angles 107.2 to 112.0 -> [(1.5, 'tetrahedral'), (42.6, 'square planar')]
oxy heme CN = 6 {'N pyrrole A': 2.0, 'N pyrrole B': 2.01, 'N pyrrole C': 2.01, 'N pyrrole D': 1.99, 'NE2 His prox': 2.12, 'O1 dioxygen': 1.82}
   angles 85.7 to 179.7 -> [(2.0, 'octahedral')]
```

The Lewis acidity of the carbonic anhydrase zinc in numbers:

```python
def fraction_hydroxide(pka: float, ph: float) -> float:
    """Fraction of a metal-bound water present as OH- (Henderson-Hasselbalch)."""
    return 1 / (1 + 10 ** (pka - ph))


zn, free = fraction_hydroxide(7.0, 7.4), fraction_hydroxide(15.7, 7.4)
print(f"Zn-bound: {zn:.3f}  free water: {free:.1e}  ratio: {zn / free:.1e}")
```

```text
Zn-bound: 0.715  free water: 5.0e-09  ratio: 1.4e+08
```

## Worked example

> [!example] Reading two metal sites from coordinates
> With the toy coordinates above (invented, built on ideal geometries):
> 1. **Shell.** With $r_c = 2.6$ Å the zinc keeps four atoms, two S at 2.28 and 2.29 Å and two N at 2.04 and 2.05 Å. The Cys CB (3.4 Å), the His CE1 (3.3 Å) and a water (3.6 Å) stay outside.
> 2. **Angles.** The six angles lie between 107.2° and 112.0°, close to 109.5°: RMS 1.5° from tetrahedral against 42.6° from square planar.
> 3. **Heme.** The oxy iron keeps six atoms: four pyrrole N at 1.99 to 2.01 Å, the His NE2 at 2.12 Å and one O of O₂ at 1.82 Å. The second O of O₂ (2.8 Å) and a porphyrin carbon (3.0 Å) stay outside. Angles from 85.7° to 179.7° score 2.0° from octahedral.
> 4. **Charge.** If both Cys bind as thiolates (S⁻) and both His as neutral imidazoles, the zinc site carries $+2 - 2 + 0 = 0$.

## Common misconceptions

> [!warning] "A coordinate bond is not a real covalent bond"
> Once formed, it is a shared electron pair like any covalent bond; "coordinate" only records that both electrons came from the ligand.[^c2e192]

> [!warning] "The coordination number equals the metal's charge"
> Zn²⁺ in a zinc finger has four ligands and heme Fe²⁺ has six, with the same charge: the coordination number counts donor atoms.

> [!warning] "Every metal in a protein is a catalyst"
> The zinc of a zinc finger holds a fold,[^alberts] while the zinc of carbonic anhydrase is the catalyst.[^berg9] In these two examples the ligand set gives it away: four protein ligands for the structural zinc, three plus a water for the catalytic one.

## Exercises

> [!question] Exercise 1 (L2)
> Give the coordination number and the geometry of: (a) heme Fe²⁺ in oxymyoglobin; (b) the same iron in deoxymyoglobin; (c) Zn²⁺ in a Cys₂His₂ zinc finger; (d) [Co(en)₃]³⁺, en being ethylenediamine; (e) a metal ion wrapped by one EDTA.

> [!success]- Solution
> (a) 6 (four porphyrin N, His, O₂): octahedral. (b) 5, the O₂ position empty: square pyramidal, the iron slightly out of the plane. (c) 4: tetrahedral. (d) en is bidentate,[^c2e192] 3 × 2 = 6: octahedral. (e) Six donor atoms (2 N, 4 O) from one hexadentate ligand: 6, octahedral.

> [!question] Exercise 2 (L2)
> Write the electron configurations of Mg²⁺, Fe²⁺, Fe³⁺ and Zn²⁺. Which oxidation state of heme iron carries O₂, and what happens to a hemoglobin molecule whose iron is oxidized?

> [!success]- Solution
> Mg²⁺ [Ne]; Fe²⁺ [Ar] 3d⁶; Fe³⁺ [Ar] 3d⁵; Zn²⁺ [Ar] 3d¹⁰ (4s electrons leave first).[^c2e64] Only Fe²⁺ binds O₂ reversibly; an oxidized Fe³⁺ heme does not bind O₂, so that molecule stops carrying oxygen.[^lehninger] The oxidation is a [[Redox Reaction]] at a metal center.

> [!question] Exercise 3 (L2)
> The zinc-bound water of carbonic anhydrase has a pKa of about 7. What fraction is hydroxide at pH 6.4, 7.4 and 8.4, and how should activity change over this range if the hydroxide is the nucleophile?

> [!success]- Solution
> `[round(fraction_hydroxide(7.0, ph), 2) for ph in (6.4, 7.4, 8.4)]` gives `[0.2, 0.72, 0.96]`. Activity should rise with pH across this range, half-maximal near pH 7, as the catalytic hydroxide is formed.[^berg9]

> [!question] Exercise 4 (L3, Python)
> Deoxy heme, toy version: remove O₂ from `HEME_OXY`, move the iron 0.35 Å out of the plane toward the His, and move the His with it. Classify the site with cutoffs of 2.0, 2.6 and 3.2 Å. What does each cutoff get right or wrong?

> [!success]- Solution
> ```python
> FE_DEOXY = (0.0, 0.0, -0.35)                       # iron 0.35 Å out of plane, toward the His (invented)
> HEME_DEOXY = {k: v for k, v in HEME_OXY.items() if "dioxygen" not in k}
> HEME_DEOXY["NE2 His prox"] = (0.05, -0.04, -2.47)  # the His follows the iron
> for cutoff in (2.0, 2.6, 3.2):
>     s = shell(FE_DEOXY, HEME_DEOXY, cutoff)
>     print(cutoff, len(s), classify(list(s.values()))[:2] if s else "no ligand")
> ```
> Output: `2.0 0 no ligand`, `2.6 5 [(11.3, 'square pyramidal'), (16.7, 'trigonal bipyramidal')]`, `3.2 6 [(22.6, 'octahedral')]`. At 2.0 Å nothing is found: the cutoff is shorter than the Fe–N bonds. At 2.6 Å the five ligands appear and square pyramidal wins, with an RMS of 11.3° because the out-of-plane iron bends the trans N–Fe–N angles below 180°. At 3.2 Å a porphyrin carbon joins the shell and the site is wrongly called octahedral; its poor score (22.6°) is the warning sign. Cutoffs should depend on the metal and the donor element, and a poor geometry score should send you back to the structure.

> [!question] Exercise 5 (L3)
> A PCR fails after a large volume of DNA stored in an EDTA-containing buffer is added, and works again when extra MgCl₂ is added. Explain with coordination chemistry, and say why adding more polymerase would not help.

> [!success]- Solution
> The polymerase needs two Mg²⁺ ions in its active site.[^yang] EDTA, with six donor atoms in one molecule, chelates free Mg²⁺ and leaves those sites empty. Adding Mg²⁺ in excess over the EDTA restores free Mg²⁺. More enzyme only adds more empty active sites, not the missing metal.

> [!question] Exercise 6 (L3, Python)
> A predicted model of a zinc finger has its two Cys and two His side chains in place but no zinc.[^jumper] Using the four donor atoms of `ZINC_SITE` as stand-ins, place a zinc at their centroid and check its distances and geometry.

> [!success]- Solution
> ```python
> donors = [ZINC_SITE[k] for k in ("SG Cys1", "SG Cys2", "NE2 His1", "NE2 His2")]
> zinc = tuple(sum(c) / 4 for c in zip(*donors))      # centroid of the four donor atoms
> vectors = [tuple(b - a for a, b in zip(zinc, d)) for d in donors]
> print([round(c, 2) for c in zinc], [round(math.hypot(*v), 2) for v in vectors], classify(vectors)[0])
> ```
> Output: `[0.08, -0.04, 0.01] [2.26, 2.22, 2.12, 2.07] (1.8, 'tetrahedral')`. The centroid lands within 0.1 Å of the toy site's zinc (the origin), with distances between 2.07 and 2.26 Å and tetrahedral angles. It is a good first guess for a tetrahedral site; a better placement would weight each donor by its own metal-donor distance, longer for S than for N.

## Mastery checklist

- [ ] 1 Recognized: I can define ligand, coordination number, denticity and chelate, and name the metal of a zinc finger, of heme and of a polymerase active site.
- [ ] 2 Understood: I can explain the metal-ligand bond as a Lewis acid-base bond and predict the geometry of Zn²⁺ and heme iron sites from their ligands.
- [ ] 3 Practiced: I can compute coordination shells, angles and geometry scores from coordinates in Python.
- [ ] 4 Applied: I examined real metal sites in PDB entries (a zinc finger, myoglobin, a polymerase with two Mg²⁺) and checked their geometry.
- [ ] 5 Explained: I can teach how metal ions catalyze (Lewis acidity, two-metal-ion catalysis), how heme carries O₂, and the pitfalls of assigning metals from coordinates or predicted models.

## References

[^c2e192]: [[Chemistry 2e (OpenStax)]], ch. 19, §19.2 "Coordination Chemistry of Transition Metals" (ligands and coordinate covalent bonds, coordination number, monodentate and polydentate ligands, chelates, ethylenediamine as a bidentate ligand, the tetradentate porphyrin of heme; tetrahedral or square planar geometry for coordination number 4, octahedral for 6).
[^c2e19]: [[Chemistry 2e (OpenStax)]], ch. 19 "Transition Metals and Coordination Chemistry" (crystal field theory; section not verified).
[^c2e64]: [[Chemistry 2e (OpenStax)]], ch. 6, §6.4 "Electronic Structure of Atoms (Electron Configurations)".
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of bioenergetics (ATP complexed with Mg²⁺, which shields its negative charges and influences the conformation of its phosphates) and of protein function (heme Fe²⁺ with six coordination bonds, four to the porphyrin nitrogens and two perpendicular, to the proximal His and to O₂; only Fe²⁺ binds O₂ reversibly; heme sequestered in the protein against oxidation) (chapter numbers not verified).
[^berg9]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of catalytic strategies (metal ion catalysis; carbonic anhydrase, its Zn²⁺ bound to three His and a water whose pKa drops from 15.7 to about 7; Mg²⁺-NTP complexes as the true substrates of essentially all NTP-dependent enzymes).
[^berg10]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of hemoglobin (iron out of the porphyrin plane in deoxyhemoglobin, moving into it on O₂ binding and pulling the proximal His and its helix).
[^berg27]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of DNA polymerases (attack of the primer 3′-OH on the α-phosphate of the incoming dNTP, release of pyrophosphate).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of DNA-binding motifs of gene regulatory proteins (zinc fingers of the Cys-Cys-His-His family: an α helix and a β sheet held together by zinc; tandem fingers contacting the major groove).
[^yang]: [[Yang 2006 - Making and Breaking Nucleic Acids - Two-Mg2+-Ion Catalysis and Substrate Specificity]], *Molecular Cell* (two Mg²⁺ ions jointly coordinated by the substrate and catalytic residues in all DNA and RNA polymerases and many nucleases and transposases; Mg²⁺ geometry and electrostatics and substrate specificity).
[^jumper]: [[Jumper 2021 - Highly Accurate Protein Structure Prediction with AlphaFold]], *Nature* 596:583-589 (AlphaFold 2 predicts single protein chains; other molecules are handled by later versions).
