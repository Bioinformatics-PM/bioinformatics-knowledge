---
aliases:
  - Secondary Structure
  - Alpha Helix
  - α helix
  - Beta Sheet
  - β sheet
  - Beta Turn
  - Structure secondaire des protéines
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
  - "[[Peptide Bond]]"
  - "[[Amino Acid]]"
  - "[[Hydrogen Bond]]"
related:
  - "[[Ramachandran Plot]]"
  - "[[Secondary Structure Assignment]]"
  - "[[Secondary Structure Prediction]]"
  - "[[Protein Tertiary Structure]]"
  - "[[Protein Folding]]"
  - "[[Membrane Protein]]"
  - "[[Hydrophobic Effect]]"
  - "[[Contact Map]]"
  - "[[Missense Mutation]]"
projects: []
sources:
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Pauling 1951 - Two Hydrogen-Bonded Helical Configurations of the Polypeptide Chain]]"
  - "[[Kabsch 1983 - Dictionary of Protein Secondary Structure]]"
---

# Protein Secondary Structure

> [!abstract]
> Secondary structure is the local shape of a protein backbone: a few regular patterns (α helix, β sheet, turns) in which backbone N–H and C=O groups pair through hydrogen bonds, each pattern corresponding to a typical pair of backbone angles φ and ψ.

## Definition

**Secondary structure** is the local spatial arrangement of the polypeptide backbone, without regard to side-chain conformations. Its regular forms, the **α helix** and the **β sheet** (built from β strands), are stabilized by hydrogen bonds between backbone C=O and N–H groups and are connected by **turns** and **loops**.[^berg][^lehninger] It is the second of the four levels of [[Protein Structure]].

## Why it matters

- **Labels computed from structures.** DSSP reads atomic coordinates and gives every residue one of eight state codes from its backbone hydrogen-bond pattern ([[Secondary Structure Assignment]]).[^dssp]
- **Prediction from sequence.** Helix, strand or coil is predicted per residue, from residue preferences to profile-based neural networks ([[Secondary Structure Prediction]]); a prediction is scored by comparing it with the DSSP states of a solved structure (Exercise 5).
- **Model validation.** Each regular structure occupies its own region of (φ, ψ) space, which is what a [[Ramachandran Plot]] checks in an experimental or predicted model.
- **Variant interpretation.** Proline lacks the backbone N–H that a helix needs and is a helix breaker,[^berg] so a [[Missense Mutation]] that puts a proline inside a helix is suspicious even before any 3D model is built.
- **Periodic sequence signals.** A helix turns every 3.6 residues and a strand alternates its side chains between two faces,[^berg] which leaves periodic hydrophobicity patterns in sequences ([[Hydrophobic Effect]], [[Membrane Protein]]).

## Core (L2)

![[secondary-structure-hydrogen-bonds.svg]]

### Why only a few regular structures

The [[Peptide Bond|peptide unit]] is planar, so each residue has two free backbone torsions, φ (about N–Cα) and ψ (about Cα–C); local steric clashes exclude most (φ, ψ) combinations ([[Ramachandran Plot]]).[^berg] In 1951 Pauling, Corey and Branson used the planar peptide and the requirement that backbone N–H and C=O groups form hydrogen bonds to derive helical structures of the chain; one of them, with about 3.7 residues per turn, is the α helix.[^pauling] Pauling and Corey proposed the β pleated sheet the same year.[^berg] Repeating one (φ, ψ) pair along consecutive residues produces a regular structure (Mathematical representation).

| Structure | Typical (φ, ψ) | Backbone hydrogen bonds | Geometry |
|---|---|---|---|
| α helix | (−57°, −47°)[^lehninger] | C=O of $i$ to N–H of $i + 4$[^berg] | 3.6 residues per turn, 1.5 Å rise per residue, pitch 5.4 Å[^berg] |
| Antiparallel β sheet | (−139°, +135°)[^lehninger] | N–H and C=O of a residue to one partner residue on the adjacent strand[^berg] | about 3.5 Å per residue[^berg] |
| Parallel β sheet | (−119°, +113°)[^lehninger] | N–H to residue $j - 1$, C=O to residue $j + 1$ of the adjacent strand[^berg] | about 3.5 Å per residue[^berg] |
| β turn | varies | C=O of $i$ to N–H of $i + 3$[^berg] | reverses the chain |

### The α helix

The backbone coils tightly inside a rod and the side chains point outward. The C=O of residue $i$ bonds the N–H of residue $i + 4$, so all main-chain C=O and N–H groups are paired except near the helix ends. Each residue rises 1.5 Å and turns 100°: residues 3 and 4 apart in sequence are close in space, residues 2 apart sit on opposite sides.[^berg] Both screw senses are allowed by the Ramachandran diagram, but the right-handed helix has fewer clashes between side chains and backbone, and essentially all α helices in proteins are right-handed.[^berg] Helical content ranges from none to almost 100 % (about 75 % in ferritin). Single helices are usually shorter than 45 Å, while two or more helices wound into a coiled coil can exceed 1000 Å, as in myosin, tropomyosin, fibrin and keratin.[^berg]

### The β sheet

A β strand is almost fully extended: 3.5 Å per residue against 1.5 Å in a helix, with the side chains of consecutive residues pointing to opposite sides. Two or more strands, adjacent in sequence or far apart, link through hydrogen bonds into a sheet, running in opposite directions (**antiparallel**) or the same direction (**parallel**). Sheets usually hold 4 or 5 strands (10 or more occur), can be purely antiparallel, purely parallel or mixed, and are typically twisted rather than flat.[^berg] An isolated strand has no internal hydrogen bonds: its partners are on the neighbouring strands (Computational representation).

### Turns and loops

Compact proteins reverse their chain many times. In a **reverse turn** (β turn), the C=O of residue $i$ bonds the N–H of residue $i + 3$; **loops** are longer reversals without a periodic structure, yet often rigid and well defined. Turns and loops lie at the protein surface, where they often mediate interactions with other molecules.[^berg] Types I and II are the most common β turns; Gly (small and flexible) and Pro (whose peptide bond readily adopts the cis form) are frequent in them.[^lehninger]

### Residue preferences

Some residues are more frequent in one structure than in others:[^berg]

- **Helix**: Ala, Glu, Leu and Met are enriched. β-branched residues (Val, Thr, Ile) destabilize helices through steric clashes; Ser, Asp and Asn compete with the backbone for its hydrogen bonds; Pro breaks helices, having no N–H and a rigid ring.
- **Strand**: β-branched and aromatic residues (Val, Ile, Tyr, Phe, Trp) are enriched.
- **Turn**: Gly, Pro, Asn, Asp and Ser are enriched.

These are frequencies, not rules: the same short sequence can be a helix in one protein and a strand in another (Common misconceptions).[^berg]

### What DSSP assigns, what predictors predict

DSSP detects backbone hydrogen bonds in the coordinates and recognizes two elementary patterns, the **turn** (C=O of $i$ to N–H of $i + n$, $n = 3, 4, 5$) and the **bridge** (between residues far apart); repeated turns form helices, repeated bridges form ladders and sheets. Each residue receives one code: **H** α helix (4-turn), **G** 3₁₀ helix (3-turn), **I** π helix (5-turn), **E** extended strand in a ladder, **B** isolated β bridge, **T** hydrogen-bonded turn, **S** bend (a purely geometric criterion), or blank.[^dssp]

Predictors usually output three states per residue, helix, strand and coil, so the eight codes are grouped before scoring; the grouping used in the code below is H, G, I → H; E, B → E; the rest → C ([[Secondary Structure Prediction]]).

## Advanced (L3)

**Every regular backbone is a helix.** Identical (φ, ψ, ω) at every residue means the same rigid motion carries each residue onto the next, and a repeated rigid motion is a screw (Mathematical representation). The α helix and the β strand are two screws of the same chain: 3.6 against about 2 residues per turn (Computational representation). The twist of real β sheets is the deviation of strands from exactly 2 residues per turn.

**Context decides.** The six-residue sequence VDLLKN forms an α helix in one protein and a β strand in another:[^berg] local preferences are biased coins, and tertiary contacts settle the outcome. A window of residue preferences alone therefore cannot be fully accurate; how predictors add more information is the subject of [[Secondary Structure Prediction]].

**Signatures in a contact map.** In a [[Contact Map]], a helix gives contacts at sequence separations 3 and 4, a band along the diagonal ([[Protein Structure#Computational representation]]). Two antiparallel strands pair residues $(i, j), (i + 1, j - 1), \dots$, with $i + j$ constant: a line perpendicular to the diagonal. Parallel strands pair $(i, j), (i + 1, j + 1), \dots$, with $j - i$ constant: a line parallel to it. Secondary structure can thus be read off a contact map, predicted or observed.

**Periodicity as a feature.** A helix with one hydrophobic face repeats its hydrophobicity every 3.6 residues (hydrophobic moment, [[Hydrophobic Effect#Advanced (L3)]]). A strand with one face buried alternates hydrophobic and polar residues with period 2; in membrane β barrels, this alternation replaces the long hydrophobic stretch of a transmembrane helix ([[Membrane Protein]]).

## Mathematical representation

- **Backbone torsions** of residue $i$: $\varphi_i = \tau(\mathrm{C}_{i-1}, \mathrm{N}_i, \mathrm{C}\alpha_i, \mathrm{C}_i)$, $\psi_i = \tau(\mathrm{N}_i, \mathrm{C}\alpha_i, \mathrm{C}_i, \mathrm{N}_{i+1})$, and $\omega_i \approx 180°$ for a trans peptide, with $\tau$ the torsion angle of four points defined in [[Peptide Bond#Mathematical representation]].
- **Regular segment.** If $\varphi_i = \varphi$ and $\psi_i = \psi$ for all $i$ in a segment, the rigid motion $x \mapsto Rx + t$ (rotation matrix $R$, translation $t$) mapping residue $i$ onto residue $i + 1$ is the same for every $i$. By Chasles' theorem, a rigid motion that is not a pure translation is a **screw**: a rotation by $\theta$ about an axis $u$ combined with a translation $d$ along $u$. Then
$$\cos\theta = \frac{\operatorname{tr}R - 1}{2}, \qquad n = \frac{360°}{\theta}, \qquad d = t \cdot u, \qquad p = n\,d,$$
with $n$ the residues per turn, $d$ the rise per residue and $p$ the pitch; taking $\theta \in (0°, 180°)$ and $u$ from the antisymmetric part of $R$, $d > 0$ means right-handed. For the α helix, $n = 3.6$ and $d = 1.5$ Å give $p = 5.4$ Å.[^berg]
- **Hydrogen-bond pattern.** A helix of type $k$ ($k = 3, 4, 5$ for 3₁₀, α, π) bonds C=O$(i)$ to N–H$(i + k)$. An ideal α helix of $L$ residues contains $L - 4$ such bonds; the N–H groups of its first four residues and the C=O groups of its last four have no partner inside the helix.
- **Propensity** of amino acid $a$ for state $S$, from $N$ residues of known structures: $P_S(a) = \dfrac{N_{a,S}/N_a}{N_S/N}$, with $N_a$ the residues of type $a$, $N_S$ the residues in state $S$, and $N_{a,S}$ both. $P_S(a) > 1$ means enriched.

## Computational representation

The script builds an ideal backbone from one (φ, ψ) pair by placing each atom from a bond length, a bond angle and a torsion (bond lengths and angles are approximate toy values; C–N is the [[Peptide Bond]] length), then measures the screw and finds backbone hydrogen bonds with a simple geometric criterion. DSSP itself uses an electrostatic energy, not this criterion.[^dssp] The second part reduces DSSP strings to three states and computes propensities on invented data.

```python
import math
from collections import Counter

Vec = tuple[float, float, float]


def sub(a: Vec, b: Vec) -> Vec: return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def dot(a: Vec, b: Vec) -> float: return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def cross(a: Vec, b: Vec) -> Vec: return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
def unit(a: Vec) -> Vec: n = math.sqrt(dot(a, a)); return (a[0] / n, a[1] / n, a[2] / n)


def angle(a: Vec, b: Vec, c: Vec) -> float:
    """Angle abc in degrees."""
    return math.degrees(math.acos(max(-1.0, min(1.0, dot(unit(sub(a, b)), unit(sub(c, b)))))))


def place(a: Vec, b: Vec, c: Vec, bond: float, ang: float, torsion: float) -> Vec:
    """Atom d bonded to c: |cd| = bond, angle bcd = ang, torsion abcd = torsion (degrees)."""
    bc = unit(sub(c, b))
    n = unit(cross(sub(b, a), bc))
    m = cross(n, bc)
    t, p = math.radians(ang), math.radians(torsion)
    x, y, z = -bond * math.cos(t), bond * math.sin(t) * math.cos(p), bond * math.sin(t) * math.sin(p)
    return tuple(c[k] + x * bc[k] + y * m[k] + z * n[k] for k in range(3))


def build_backbone(phi: float, psi: float, n: int, omega: float = 180.0) -> list[dict[str, Vec]]:
    """N, CA, C, O, H of n residues repeating one (phi, psi); approximate bond lengths and angles."""
    res = [{"N": (0.0, 1.0, 0.0), "CA": (0.0, 0.0, 0.0), "C": (1.52, 0.0, 0.0)}]
    for _ in range(n):
        p = res[-1]
        N = place(p["N"], p["CA"], p["C"], 1.32, 116.0, psi)        # C-N: the peptide bond
        CA = place(p["CA"], p["C"], N, 1.46, 122.0, omega)
        C = place(p["C"], N, CA, 1.52, 111.0, phi)
        p["O"] = place(N, p["CA"], p["C"], 1.23, 121.0, 180.0)       # C=O in the peptide plane
        res.append({"N": N, "CA": CA, "C": C, "H": place(p["C"], CA, N, 1.01, 119.0, 180.0)})
    return res[1:-1]                             # keep residues that have both H and O


def screw(res: list[dict[str, Vec]], i: int) -> tuple[float, float]:
    """Rotation (degrees) and rise (Å, > 0 right-handed) of the motion taking residue i to i+1."""
    def frame(r):
        e1 = unit(sub(r["C"], r["CA"]))
        e2 = unit(cross(e1, sub(r["N"], r["CA"])))
        return [e1, e2, cross(e2, e1)]
    F, G = frame(res[i]), frame(res[i + 1])
    R = [[sum(G[k][a] * F[k][b] for k in range(3)) for b in range(3)] for a in range(3)]
    theta = math.degrees(math.acos(max(-1.0, min(1.0, (R[0][0] + R[1][1] + R[2][2] - 1) / 2))))
    axis = unit((R[2][1] - R[1][2], R[0][2] - R[2][0], R[1][0] - R[0][1]))
    t = sub(res[i + 1]["CA"], tuple(dot(R[a], res[i]["CA"]) for a in range(3)))
    return theta, dot(t, axis)


def hbonds(res: list[dict[str, Vec]]) -> Counter:
    """Backbone C=O(i)...H-N(j) bonds by offset j - i (toy criterion: H...O < 2.5 Å, N-H...O > 120°)."""
    return Counter(j - i for i in range(len(res)) for j in range(i + 3, len(res))
                   if math.dist(res[i]["O"], res[j]["H"]) < 2.5
                   and angle(res[j]["N"], res[j]["H"], res[i]["O"]) > 120)


for name, (phi, psi) in {"alpha helix": (-57, -47), "beta strand": (-139, 135)}.items():
    bb = build_backbone(phi, psi, 14)
    theta, rise = screw(bb, 5)
    print(f"{name}: {360 / theta:.2f} residues/turn, rise {rise:+.2f} Å/residue, "
          f"H-bonds by offset {dict(hbonds(bb))}")

# Eight DSSP states reduced to three (mapping chosen here: H, G, I -> H; E, B -> E; rest -> C)
TO3 = {"H": "H", "G": "H", "I": "H", "E": "E", "B": "E"}


def to_three(dssp: str) -> str:
    return "".join(TO3.get(s, "C") for s in dssp)


def propensity(data: list[tuple[str, str]], state: str) -> dict[str, float]:
    """P(a) = (fraction of residues a in state) / (fraction of all residues in state)."""
    n_aa, n_in = Counter(), Counter()
    for seq, dssp in data:
        for a, s in zip(seq, to_three(dssp)):
            n_aa[a] += 1
            n_in[a] += s == state
    f_state = sum(n_in.values()) / sum(n_aa.values())
    return {a: round(n_in[a] / n_aa[a] / f_state, 2) for a in sorted(n_aa)}


TOY = [  # invented sequences with invented DSSP strings (space = no assignment)
    ("MAEELLKKAEELGKPGVTVKVEVNGS", " HHHHHHHHHHHTT  EEEEEETTEE"),
    ("SPEALKKLAEEAGNGKVIVYVDGTPD", "  GGGHHHHHHHTSS BEEEEE SS "),
]
helix = propensity(TOY, "H")
print({a: helix[a] for a in "AELKGPV"})
```

```text
alpha helix: 3.62 residues/turn, rise +1.55 Å/residue, H-bonds by offset {4: 9}
beta strand: 2.01 residues/turn, rise +3.46 Å/residue, H-bonds by offset {}
{'A': 2.48, 'E': 2.17, 'L': 2.48, 'K': 1.41, 'G': 0.0, 'P': 0.0, 'V': 0.0}
```

From two numbers per residue, the builder recovers the textbook geometry: 3.6 residues per turn, 1.5 Å rise and only $i \to i + 4$ bonds for (−57°, −47°); 2 residues per turn, about 3.5 Å per residue and no internal bonds for (−139°, +135°). The 13-residue helix has $13 - 4 = 9$ bonds, as predicted above. On 52 invented residues the propensities are extreme: 0 for G, P and V only because none of them happens to fall in a helix. Real tables are counted over many solved structures, and even then they describe each residue independently of its neighbours and of the fold, which the VDLLKN case defeats.

## Worked example

> [!example] Reading a DSSP string (invented protein; `-` marks a blank DSSP state)
> ```text
> position  ....+....1....+....2....+....3....+..
> sequence  MSPEELLKKAAELAKGNPDGKVTVKVDGITVEVTVKE
> DSSP      ---HHHHHHHHHHHTT----EEEEEETTEEEEEE---
> 3-state   CCCHHHHHHHHHHHCCCCCCEEEEEECCEEEEEECCC
> ```
> 1. **Segments.** Helix 4 to 14 (11 residues), strands 21 to 26 and 29 to 34, joined by the turn D27-G28.
> 2. **Helix geometry.** 11 residues make $11/3.6 \approx 3.1$ turns and $11 \times 1.5 = 16.5$ Å. As an ideal helix it would hold $11 - 4 = 7$ backbone hydrogen bonds; the N–H groups of E4 to L7 and the C=O groups of A11 to A14 point out of the helix ends without a partner.
> 3. **Hairpin pairing.** Two strands joined by a two-residue turn are antiparallel: residue 26 faces 29, 25 faces 30, down to 21 facing 34, so $i + j = 55$ for every pair. In a [[Contact Map]] these pairs form a line perpendicular to the diagonal.
> 4. **Two faces.** Side chains alternate between the faces of a strand: V22, V24, V26 on one side, K21, T23, K25 on the other. Paired residues of the two strands sit at the same level of the pleated sheet, so I29, V31, V33 (paired with 26, 24, 22) join the valines: one face is hydrophobic, the other polar, the signature of a hairpin packed against the rest of the protein. The loops (G16 to G20, D27-G28) are rich in the turn-favoring Gly, Pro, Asn and Asp.

## Common misconceptions

> [!warning] "A sequence has its own secondary structure"
> Preferences are statistical. The sequence VDLLKN is an α helix in one protein and a β strand in another;[^berg] tertiary contacts decide, which caps the accuracy of methods that only look at a local window.

> [!warning] "Every residue of a helix is hydrogen-bonded on both sides"
> The C=O of residue $i$ bonds the N–H of $i + 4$, so the first four N–H and the last four C=O groups of a helix have no partner inside it.[^berg] Their partners, if any, come from outside the helix (side chains, water, other parts of the protein), and this is also where Pro is tolerated (Exercise 3).

> [!warning] "Coil means disordered"
> In a three-state string, C only means "neither H nor E". It groups well-defined turns, bends and loops, which are often rigid,[^berg] with genuinely flexible regions ([[Intrinsically Disordered Region]]).

## Exercises

> [!question] Exercise 1 (L2)
> An α helix spans 18 residues. How many turns does it make, how long is it, how many $i \to i + 4$ hydrogen bonds does it contain, and how many backbone N–H and C=O groups lack a partner inside it? How long would the same residues be as a β strand?

> [!success]- Solution
> $18 / 3.6 = 5$ turns and $18 \times 1.5 = 27$ Å. Bonds: $18 - 4 = 14$. Unpaired: the N–H of residues 1 to 4 and the C=O of residues 15 to 18, 8 groups. As a strand: $18 \times 3.5 = 63$ Å, more than twice as long.

> [!question] Exercise 2 (L2)
> Strand A (residues 40 to 45) pairs with strand B (residues 60 to 65). List the pairs if the strands are antiparallel with 45 facing 60, then if they are parallel with 40 facing 60. Describe the line each pattern draws in a contact map.

> [!success]- Solution
> Antiparallel: (45, 60), (44, 61), (43, 62), (42, 63), (41, 64), (40, 65); $i + j = 105$, a line perpendicular to the diagonal. Parallel: (40, 60), (41, 61), ..., (45, 65); $j - i = 20$, a line parallel to the diagonal, 20 positions away from it. In the antiparallel case, every second pair carries the two hydrogen bonds; in the parallel case each bonded residue reaches residues $j - 1$ and $j + 1$ of the other strand.[^berg]

> [!question] Exercise 3 (L2)
> A variant replaces a residue by Pro. Explain why the effect differs between the first turn of a helix (residues 1 to 4) and its middle.

> [!success]- Solution
> In a helix, the N–H of residue $i$ bonds the C=O of residue $i - 4$. Residues 1 to 4 have no such partner anyway, so a Pro there loses no hydrogen bond. In the middle, Pro removes one bond (it has no N–H) and its rigid ring does not fit the helix,[^berg] so the helix is broken or kinked. Position matters as much as the substitution, which is why variant interpretation needs the secondary structure ([[Missense Mutation]]).

> [!question] Exercise 4 (L3, Python)
> With `build_backbone`, `screw` and `hbonds` from the code above, build 14 residues with (φ, ψ) = (−49°, −26°) and with (+57°, +47°). Report residues per turn, rise and hydrogen-bond offsets, then name each structure.

> [!success]- Solution
> ```python
> for name, (phi, psi) in {"tighter": (-49, -26), "mirror": (57, 47)}.items():
>     bb = build_backbone(phi, psi, 14)
>     theta, rise = screw(bb, 5)
>     print(f"{name}: {360 / theta:.2f} residues/turn, rise {rise:+.2f} Å, H-bonds {dict(hbonds(bb))}")
> ```
> ```text
> tighter: 2.98 residues/turn, rise +1.99 Å, H-bonds {3: 10}
> mirror: 3.62 residues/turn, rise -1.55 Å, H-bonds {4: 9}
> ```
> The first is a tighter, more elongated helix with 3 residues per turn and $i \to i + 3$ bonds: the pattern DSSP labels G (3₁₀ helix).[^dssp] The second is the mirror image of the α helix: same pitch and bonds, negative rise, so left-handed. It is allowed by the backbone alone, but with L-amino acids the right-handed helix has fewer side-chain clashes, and essentially all α helices in proteins are right-handed.[^berg]

> [!question] Exercise 5 (L3, Python)
> Score an invented prediction against an invented DSSP assignment: compute the three-state string, the overall fraction of correct residues (Q3) and the fraction of each observed state recovered.
> ```text
> DSSP        "  HHHHHHHHHHGGGTT EEEEEEB SS EEEEEE  "
> prediction  "CCCHHHHHHHHHHHCCCCCEEEECCCCCEEEEEECCC"
> ```

> [!success]- Solution
> ```python
> dssp = "  HHHHHHHHHHGGGTT EEEEEEB SS EEEEEE  "
> pred = "CCCHHHHHHHHHHHCCCCCEEEECCCCCEEEEEECCC"
> obs = to_three(dssp)
> q3 = sum(o == p for o, p in zip(obs, pred)) / len(obs)
> per_state = {s: round(sum(o == p == s for o, p in zip(obs, pred)) / obs.count(s), 2) for s in "HEC"}
> print(obs, round(q3, 3), per_state)
> # CCHHHHHHHHHHHHHCCCEEEEEEECCCCEEEEEECC 0.811 {'H': 0.85, 'E': 0.69, 'C': 0.91}
> ```
> Q3 is 0.811, but strands are recovered worse (0.69) than coil (0.91): a single accuracy hides the weakest state. The GGG residues were grouped into H by our mapping; another grouping changes the score, so the mapping must be stated with any accuracy ([[Secondary Structure Prediction]]).

## Mastery checklist

- [ ] 1 Recognized: I can name the α helix, the β sheet (parallel, antiparallel) and the β turn, and say what holds each together.
- [ ] 2 Understood: I can give the hydrogen-bond pattern, typical (φ, ψ), residues per turn and rise of each structure, and the residue preferences with their reasons.
- [ ] 3 Practiced: I can build a backbone from (φ, ψ), measure its screw and hydrogen bonds, reduce DSSP strings to three states and compute propensities and Q3.
- [ ] 4 Applied: I computed the DSSP assignment of a real PDB structure, compared it with the helices and sheets shown in a viewer, and with a sequence-based prediction.
- [ ] 5 Explained: I can teach why every regular backbone is a helix, how context overrides propensities, and what DSSP states and their three-state grouping mean for prediction scores.

## References

[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of secondary structure: Pauling and Corey's α helix and β pleated sheet (1951); α-helix geometry (hydrogen bonds from $i$ to $i + 4$, 1.5 Å rise, 100° rotation, 3.6 residues per turn, pitch 5.4 Å, right-handedness); helical content (ferritin), helix length and coiled coils; residues that destabilize helices; β strands and parallel and antiparallel sheets; reverse turns and loops; relative frequencies of residues in secondary structures; the VDLLKN sequence in two conformations.
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of secondary structure: typical φ and ψ values of the α helix and of parallel and antiparallel β sheets; β turns (types I and II, Gly and Pro).
[^pauling]: [[Pauling 1951 - Two Hydrogen-Bonded Helical Configurations of the Polypeptide Chain]], Pauling L, Corey RB, Branson HR, *PNAS* 37:205-211.
[^dssp]: [[Kabsch 1983 - Dictionary of Protein Secondary Structure]], Kabsch W, Sander C, *Biopolymers* 22:2577-2637.
