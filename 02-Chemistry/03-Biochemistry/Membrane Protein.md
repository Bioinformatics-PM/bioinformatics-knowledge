---
aliases:
  - Integral Membrane Protein
  - Transmembrane Protein
  - Peripheral Membrane Protein
  - Membrane Protein Topology
  - Protéine membranaire
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Cell Membrane]]"
  - "[[Lipid]]"
  - "[[Protein Secondary Structure]]"
  - "[[Protein Tertiary Structure]]"
  - "[[Hydrophobic Effect]]"
related:
  - "[[Hydropathy Plot]]"
  - "[[Protein Targeting]]"
  - "[[Endomembrane System]]"
  - "[[Ion Channel]]"
  - "[[Hidden Markov Model]]"
  - "[[Lipid Bilayer]]"
  - "[[Functional Annotation]]"
projects: []
sources:
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Kyte 1982 - A Simple Method for Displaying the Hydropathic Character of a Protein]]"
  - "[[von Heijne 1992 - Membrane Protein Structure Prediction]]"
  - "[[Krogh 2001 - Predicting Transmembrane Protein Topology with a Hidden Markov Model]]"
---

# Membrane Protein

> [!abstract]
> Membrane proteins live in or on the lipid bilayer: some cross it with hydrophobic α helices or β barrels, others hang on by a lipid chain or by binding its surface, and the sequence of a transmembrane protein often reveals how it sits in the membrane.

## Definition

A **membrane protein** is a protein associated with a biological membrane. **Integral** membrane proteins are embedded in the bilayer and can be extracted only with detergents that disrupt it; **peripheral** membrane proteins bind the membrane surface, through other proteins or lipid head groups, and are released by gentle treatments such as high or low ionic strength or extreme pH.[^alberts] Integral proteins include **transmembrane** proteins, which cross the bilayer once (single-pass) or several times (multipass), and proteins anchored by a covalently attached lipid or by an amphipathic helix lying in one leaflet.[^alberts]

## Why it matters

- **A large share of every proteome.** A hidden Markov model applied to complete genomes estimated that 20 to 30 % of the genes of most genomes encode membrane proteins.[^krogh] Transmembrane prediction is therefore part of annotating a proteome ([[Functional Annotation]]).
- **Topology is readable from sequence.** Transmembrane helices are long hydrophobic stretches, visible in a [[Hydropathy Plot]];[^kyte] their orientation follows from the charges of the connecting loops (positive-inside rule).[^vonheijne]
- **Function at the cell boundary.** Channels, transporters and receptors are membrane proteins ([[Cell Membrane]], [[Ion Channel]]); the large family of seven-transmembrane-helix receptors detects hormones and other signals.[^berg]
- **Pitfalls for predictors.** Signal peptides are hydrophobic too and lower the accuracy of topology predictors,[^krogh] and the strands of β barrels escape window-based hydropathy analysis (Exercise 4).

## Core (L2)

![[membrane-protein-types.svg]]

### Ways to associate with a bilayer

All modes but the last make integral proteins, which only detergents extract; peripheral proteins come off with salt or pH.[^alberts]

| Mode | How the protein holds on | Example |
|---|---|---|
| Single-pass transmembrane | one α helix crosses the bilayer | glycophorin of red blood cells[^alberts] |
| Multipass transmembrane | several α helices | bacteriorhodopsin, 7 helices[^berg] |
| β barrel | a closed sheet of β strands | porins[^alberts][^berg] |
| Amphipathic helix | helices lying in one leaflet | prostaglandin H2 synthase[^berg] |
| Lipid anchor | covalent fatty acyl or prenyl chain (cytosolic face), or glycosylphosphatidylinositol (GPI, outer face)[^alberts] | |
| Peripheral | noncovalent binding to another membrane protein or to head groups[^alberts] | |

### Why α helices and β barrels

The interior of a bilayer contains no water, so the polar peptide groups of a chain crossing it must hydrogen-bond one another. An α helix pairs all its backbone N–H and C=O groups internally ([[Protein Secondary Structure]]), and this is how most transmembrane proteins cross the bilayer.[^alberts] A single β strand cannot pair its own groups, so strands cross only as a closed **β barrel**, in which every strand is hydrogen-bonded to its two neighbours; porins of this type form water-filled channels in the outer membranes of many bacteria, of mitochondria and of chloroplasts.[^alberts]

The surfaces follow the solvent. A transmembrane helix exposes about 20 hydrophobic residues to the lipid tails,[^alberts] $20 \times 1.5 = 30$ Å of helix. Porin has an inside-out polarity compared with a soluble protein: its outer surface, facing the lipids, is mostly nonpolar, while polar and charged residues line the water-filled channel inside.[^berg] Because side chains alternate between the two faces of a strand, barrel strands alternate between lipid-facing and pore-facing residues.

### Topology and the positive-inside rule

The **topology** of a transmembrane protein is the number of membrane-crossing segments and the side of the membrane on which its N-terminus and each loop lie. It is fixed when the protein is inserted during synthesis and does not flip afterwards ([[Protein Targeting]], [[Endomembrane System]]).[^alberts] Loops alternate sides, so the N- and C-termini are on the same side exactly when the number of segments is even.

Which side is which is written in the loops: positively charged residues (Lys, Arg) are enriched in the loops that stay in the cytoplasm, the **positive-inside rule**. Combining hydrophobicity analysis, the generation of all possible topologies and their ranking by this rule predicted the correct topology of 23 of 24 bacterial inner membrane proteins of known topology.[^vonheijne]

### Bio: topology prediction from a hydropathy plot

1. **Profile.** Average a hydropathy scale over a sliding window; Kyte and Doolittle used 19 residues ([[Hydropathy Plot]]).[^kyte]
2. **Segments.** Windows averaging above 1.6 mark candidate transmembrane helices.[^kyte]
3. **Loops.** The candidate segments cut the sequence into an N-terminal tail, loops and a C-terminal tail.
4. **Orientation.** The side with more Lys + Arg in its loops is the cytoplasm.[^vonheijne]
5. **Output.** A topology string, such as `in | TM 14-32 | out | TM 50-68 | in`.

A single threshold misses short or amphipathic helices and flags hydrophobic segments of soluble proteins, such as signal peptides.[^kyte] Hidden Markov models learn the whole grammar (loops, helix cores and their lengths) from proteins of known topology; TMHMM predicted 97 to 98 % of transmembrane helices correctly ([[Hidden Markov Model]]).[^krogh]

## Advanced (L3)

**Topology is written in the sequence and read at insertion.** During co-translational insertion into the endoplasmic reticulum membrane, start-transfer and stop-transfer signals (hydrophobic segments) decide which parts cross the membrane; their combination sets the topology of multipass proteins.[^alberts] Predictors and the insertion machinery thus read the same features: hydrophobic segments and flanking charges ([[Protein Targeting]]).

**Barrels need another signal.** A strand of about 10 residues alternating lipid-facing hydrophobic and pore-facing polar residues averages to a modest hydropathy, but has a strong period-2 component (Exercise 4): the period-2 analogue of the hydrophobic moment of amphipathic helices ([[Hydrophobic Effect#Advanced (L3)]]). Window averages built for 19-residue helices cannot see it.

**From heuristics to models.** The positive-inside rule and the hydropathy window are interpretable features; a hidden Markov model scores the same features jointly and gives probabilities instead of a single threshold, and it separates membrane from soluble proteins with better than 99 % sensitivity and specificity.[^krogh] Newer deep-learning predictors have since replaced TMHMM on its own server;[^krogh] check any prediction against an experimental structure when one exists ([[Protein Structure Prediction]]).

## Mathematical representation

- **Hydropathy profile.** For a sequence $a_1 \dots a_n$, a scale $h$ and a window $w$: $H_i = \frac{1}{w}\sum_{k=0}^{w-1} h(a_{i+k})$ ([[Cell Membrane#Mathematical representation]]). A candidate segment is a maximal run of windows with $H_i > \theta$, represented here by its best window.
- **Loops and sides.** $m$ segments cut the sequence into loops $L_0, \dots, L_m$ ($L_0$ the N-terminal tail, $L_m$ the C-terminal tail). Sides alternate: $L_k$ is on the side of $L_0$ if $k$ is even, on the other side if $k$ is odd. So the termini are on the same side if and only if $m$ is even.
- **Positive-inside decision.** With $\mathrm{KR}(L)$ the number of Lys and Arg in loop $L$: N-terminus inside if $\sum_{k \text{ even}} \mathrm{KR}(L_k) \ge \sum_{k \text{ odd}} \mathrm{KR}(L_k)$, outside otherwise.
- **Lengths.** A helix of $L$ residues spans $1.5L$ Å along its axis, an extended strand $3.5L$ Å ([[Protein Secondary Structure]]): a strand crossing $d$ Å perpendicular to the membrane needs about $d/3.5$ residues, more if tilted by an angle $\alpha$ ($d / (3.5\cos\alpha)$).
- **Alternation score** over a window of $w$ residues: $A_i = \frac{1}{w}\sum_{k=0}^{w-1} (-1)^k h(a_{i+k})$. For an ideal alternation $h(a_{i+k}) = \bar h + \delta(-1)^k$ and even $w$, the mean gives $H_i = \bar h$ and $A_i = \delta$: averaging hides exactly what the alternation score shows.

## Computational representation

The script reuses the Kyte-Doolittle profile of [[Cell Membrane#Computational representation]], keeps the best window of each run above the threshold, and orients the segments with the positive-inside rule.

```python
KD = {  # Kyte-Doolittle hydropathy index (Kyte and Doolittle 1982)
    "I": 4.5, "V": 4.2, "L": 3.8, "F": 2.8, "C": 2.5, "M": 1.9, "A": 1.8,
    "G": -0.4, "T": -0.7, "S": -0.8, "W": -0.9, "Y": -1.3, "P": -1.6,
    "H": -3.2, "E": -3.5, "Q": -3.5, "D": -3.5, "N": -3.5, "K": -3.9, "R": -4.5,
}


def hydropathy(seq: str, window: int = 19) -> list[float]:
    """Mean hydropathy of each window; entry i covers residues i+1 .. i+window (1-based)."""
    return [sum(KD[a] for a in seq[i:i + window]) / window for i in range(len(seq) - window + 1)]


def tm_segments(seq: str, window: int = 19, threshold: float = 1.6) -> list[tuple[int, int]]:
    """One candidate helix per run of windows above threshold: the best window (1-based, inclusive)."""
    prof, segs, i = hydropathy(seq, window), [], 0
    while i < len(prof):
        if prof[i] > threshold:
            j = i
            while j + 1 < len(prof) and prof[j + 1] > threshold:
                j += 1
            best = max(range(i, j + 1), key=prof.__getitem__)
            segs.append((best + 1, best + window))
            i = j + 1
        else:
            i += 1
    return segs


def topology(seq: str) -> str:
    """Orient the segments with the positive-inside rule: the loops with more Lys + Arg face the cytosol."""
    segs = tm_segments(seq)
    bounds = [0] + [x for s, e in segs for x in (s - 1, e)] + [len(seq)]
    loops = [seq[bounds[k]:bounds[k + 1]] for k in range(0, len(bounds), 2)]
    kr = [loop.count("K") + loop.count("R") for loop in loops]
    even_in = sum(kr[0::2]) >= sum(kr[1::2])          # N-terminal tail and every second loop
    sides = [("in" if (k % 2 == 0) == even_in else "out") for k in range(len(loops))]
    parts = [f"{sides[0]} (K+R={kr[0]})"]
    for (s, e), side, n in zip(segs, sides[1:], kr[1:]):
        parts += [f"TM {s}-{e}", f"{side} (K+R={n})"]
    return " | ".join(parts)


TOY = ("MSKRNKEQPKRS" + "LLAVIGLLFAVLIVAFLAGVL" + "DGSEDNTPQEGSDTGE"
       + "IVALFLGVAIILPFWAVLAAI" + "KRKNPESKRLKQSE")      # invented two-pass protein
print(len(TOY), tm_segments(TOY))
print(topology(TOY))
```

```text
84 [(14, 32), (50, 68)]
in (K+R=5) | TM 14-32 | out (K+R=0) | TM 50-68 | in (K+R=6)
```

The two hydrophobic stretches (residues 13 to 33 and 50 to 70 of the invented sequence) are found, each reported as its best 19-residue window, which can be one residue off at each end. The tails carry 11 Lys + Arg and the middle loop none: both termini are cytoplasmic, the loop is outside. Even number of segments, termini on the same side, as the parity rule requires.

## Worked example

> [!example] A seven-helix receptor, checked by hand
> A receptor of the seven-transmembrane-helix family[^berg] is predicted with 7 segments and an extracellular N-terminus.
> 1. **Parity.** $m = 7$ is odd, so the C-terminus is on the other side: in the cytoplasm. A prediction with the C-terminus outside would contradict itself.
> 2. **Loops.** 7 segments give 8 loops: $L_0$ (N-tail, outside), $L_1$ inside, $L_2$ outside, ..., $L_7$ (C-tail, inside). The 4 cytoplasmic ones are $L_1, L_3, L_5, L_7$.
> 3. **Positive-inside check.** Count Lys + Arg in $L_1, L_3, L_5, L_7$ against $L_0, L_2, L_4, L_6$. If the first sum is larger, the orientation is consistent; if not, the prediction (or a missed segment) needs a second look.[^vonheijne]
> 4. **Length check.** Each segment should cover about 20 residues;[^alberts] a "segment" of 40 hydrophobic residues may be two helices joined by a short loop that a 19-residue window cannot resolve.

## Common misconceptions

> [!warning] "Membrane proteins are hydrophobic all over"
> Only the belt in contact with the lipid tails is. Loops and domains outside the bilayer are as polar as any soluble protein, and the channel of a porin is lined with polar and charged residues.[^berg]

> [!warning] "Every transmembrane segment is an α helix"
> β barrels cross the membrane with β strands, in the outer membranes of bacteria, mitochondria and chloroplasts.[^alberts] Their strands are short and alternate polar and nonpolar residues, so helix-oriented hydropathy windows miss them.

> [!warning] "A hydropathy plot gives the topology"
> It gives candidate segments. The orientation comes from the loops (positive-inside rule),[^vonheijne] and N-terminal signal peptides can be mistaken for transmembrane helices.[^kyte][^krogh]

## Exercises

> [!question] Exercise 1 (L2)
> Protein P is released from membranes by 1 M NaCl; protein Q only by a detergent; protein R carries a GPI anchor. Classify them.

> [!success]- Solution
> P is peripheral: high ionic strength breaks its electrostatic binding.[^alberts] Q is integral: only disrupting the bilayer frees it. R is a lipid-anchored protein on the outer face (GPI), attached covalently to a lipid of the bilayer, hence integral by the extraction criterion.[^alberts]

> [!question] Exercise 2 (L2)
> How long is a transmembrane helix of 20 residues? How many residues does an extended β strand need to cover the same 30 Å perpendicular to the membrane, and why does this matter for a 19-residue hydropathy window?

> [!success]- Solution
> Helix: $20 \times 1.5 = 30$ Å. Strand: $30 / 3.5 \approx 9$ residues, more if tilted. A window of 19 residues spans two barrel strands and the turn between them; it averages strands that are themselves half polar: the signal is diluted below the threshold (Exercise 4).

> [!question] Exercise 3 (L3, Python)
> Move the charges of the toy protein: make the tails acidic and the middle loop rich in Lys and Arg, keeping the same hydrophobic segments. Predict, then run `topology`.

> [!success]- Solution
> ```python
> FLIPPED = ("MSDENGEQPTDS" + "LLAVIGLLFAVLIVAFLAGVL" + "KGSRKNTPKRGSKTGR"
>            + "IVALFLGVAIILPFWAVLAAI" + "DEQNPESTDLEQSE")   # same segments, charges moved
> print(topology(FLIPPED))
> ```
> ```text
> out (K+R=0) | TM 14-32 | in (K+R=7) | TM 50-68 | out (K+R=0)
> ```
> Same segments, opposite orientation: the hydrophobic stretches say where the protein crosses, the loop charges say which way.[^vonheijne]

> [!question] Exercise 4 (L3, Python)
> The invented strand `VKITLEFNVD` alternates hydrophobic and polar residues. Compute its mean Kyte-Doolittle hydropathy and its alternation score $A$, and explain why barrels escape hydropathy-based predictors.

> [!success]- Solution
> ```python
> STRAND = "VKITLEFNVD"                                   # invented amphipathic beta strand
> w = len(STRAND)
> mean_h = sum(KD[a] for a in STRAND) / w
> alternation = sum((-1) ** k * KD[a] for k, a in enumerate(STRAND)) / w
> print(f"window mean {mean_h:.2f} (threshold 1.6), alternation score {alternation:.2f}")
> # window mean 0.44 (threshold 1.6), alternation score 3.46
> ```
> The mean (0.44) is far below the threshold, though five residues are among the most hydrophobic (V, I, L, F, V): the polar residues facing the pore cancel them. The alternation score is large, because each residue sits on the opposite face of the strand from its neighbours.[^berg] β-barrel predictors look for this period-2 pattern over short strands, not for long hydrophobic stretches.

> [!question] Exercise 5 (L3)
> A protein has one strongly hydrophobic segment at residues 3 to 22 and nothing else. List two interpretations and how you would decide between them.

> [!success]- Solution
> (a) A cleavable signal peptide: the protein is secreted (or soluble in an organelle) and has no transmembrane segment after cleavage; (b) an uncleaved N-terminal signal anchor: a single-pass membrane protein. Signal peptides are a known source of errors for topology predictors,[^krogh] so run a dedicated signal peptide predictor (which looks for a cleavage site, [[Protein Targeting]]), check homologs with known localization, and, if available, experimental evidence such as a mass spectrometry peptide covering residues 1 to 22.

## Mastery checklist

- [ ] 1 Recognized: I can distinguish integral, lipid-anchored and peripheral proteins, and single-pass, multipass and β-barrel transmembrane proteins.
- [ ] 2 Understood: I can explain why bilayer-crossing segments are α helices or closed β barrels, and how topology and the positive-inside rule work.
- [ ] 3 Practiced: I can compute a hydropathy profile, extract segments, orient them with loop charges, and apply the parity rule.
- [ ] 4 Applied: I predicted the topology of real membrane proteins and compared it with their annotation or structure.
- [ ] 5 Explained: I can teach the limits of hydropathy-based prediction (signal peptides, amphipathic helices, β barrels) and what probabilistic models add.

## References

[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of membrane proteins (ways of association with the bilayer, glycophorin as a single-pass protein, integral and peripheral proteins and their extraction, detergents, α helices and hydrogen bonding of the backbone in the bilayer, about 20 hydrophobic residues per transmembrane helix, β barrels and porins of bacteria, mitochondria and chloroplasts, lipid anchors and GPI) and of insertion into the endoplasmic reticulum membrane (start-transfer and stop-transfer signals, topology of multipass proteins).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of membrane proteins (bacteriorhodopsin with seven transmembrane helices, porin with a nonpolar outer surface and a polar channel, prostaglandin H2 synthase-1 anchored by amphipathic helices), of β strands with side chains alternating between faces, and of seven-transmembrane-helix receptors in signal transduction.
[^kyte]: [[Kyte 1982 - A Simple Method for Displaying the Hydropathic Character of a Protein]], *Journal of Molecular Biology* 157:105-132.
[^vonheijne]: [[von Heijne 1992 - Membrane Protein Structure Prediction]], *Journal of Molecular Biology* 225:487-494.
[^krogh]: [[Krogh 2001 - Predicting Transmembrane Protein Topology with a Hidden Markov Model]], *Journal of Molecular Biology* 305:567-580.
