---
aliases:
  - Plasma Membrane
  - Cytoplasmic Membrane
  - Fluid Mosaic Model
  - Selective Permeability
  - Membrane plasmique
tags:
  - type/concept
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Cell]]"
  - "[[Lipid]]"
  - "[[Protein]]"
  - "[[Hydrophobic Effect]]"
related:
  - "[[Lipid Bilayer]]"
  - "[[Membrane Protein]]"
  - "[[Membrane Transport]]"
  - "[[Membrane Potential]]"
  - "[[Diffusion]]"
  - "[[Hydropathy Plot]]"
  - "[[Amino Acid]]"
  - "[[Endomembrane System]]"
  - "[[Organelle]]"
  - "[[Protein Targeting]]"
  - "[[Cell Signaling]]"
projects: []
sources:
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Kyte 1982 - A Simple Method for Displaying the Hydropathic Character of a Protein]]"
  - "[[Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
---

# Cell Membrane

> [!abstract]
> The cell membrane is a film 5 to 10 nm thick, made of two layers of lipids studded with proteins, that encloses every cell. Oily inside, it lets small uncharged molecules through but stops ions and large polar molecules, which cross only through dedicated proteins.

## Definition

The **cell membrane**, or plasma membrane, is the boundary of every cell: a **lipid bilayer**, two sheets of phospholipids whose hydrophobic tails face each other, in which proteins are embedded or attached. It is **selectively permeable**: some substances cross it freely, others only through transport proteins, others hardly at all.[^os51][^os52] All biological membranes, including the internal membranes of eukaryotic organelles, share this general structure.[^alberts-mem]

## Why it matters

- **Membrane proteins show in their sequence.** A segment that crosses the bilayer is typically an α helix of about 20 hydrophobic amino acids,[^alberts-mem] so a sliding average of hydrophobicity along a protein sequence flags candidate transmembrane segments, a classic sequence-based prediction ([[Membrane Protein]], [[Hydropathy Plot]]).[^kyte]
- **Drugs must cross membranes.** Lipinski's "rule of 5" flags compounds likely to be poorly absorbed or to permeate poorly: more than 5 hydrogen-bond donors, more than 10 acceptors, a molecular weight above 500, or a calculated log P above 5 ([[Drug Discovery]]).[^lipinski]
- **Signals stop at the surface.** Large or hydrophilic signal molecules cannot cross the membrane and act through cell-surface receptors ([[Cell Signaling]]).[^os9]
- **Gradients make potentials.** Because ions cannot cross the bilayer on their own, a cell can keep different ion concentrations inside and outside, which is the basis of membrane potentials ([[Membrane Potential]]).[^alberts-tr]

## Core (L1)

![[lipid-bilayer-membrane.svg]]

### A bilayer of two-faced lipids

A phospholipid has a hydrophilic head, containing a phosphate group, and two hydrophobic fatty-acid tails: it is **amphipathic**.[^os51] In water, such lipids assemble spontaneously into a bilayer, heads facing the water on both sides and tails hidden inside ([[Lipid]], [[Hydrophobic Effect]]).[^alberts-mem] The bilayer is about 5 nm thick, the membrane with its proteins 5 to 10 nm,[^alberts-mem][^os51] and one square micrometre of bilayer holds about 5 million lipid molecules.[^alberts-mem]

### The fluid mosaic model

Proposed by Singer and Nicolson in 1972, the **fluid mosaic model** describes the membrane as a mosaic of components that move within the plane of a fluid lipid sheet.[^os51]

| Component | Where | Role |
|---|---|---|
| Phospholipids | both layers (leaflets) | the fabric of the membrane and its barrier[^os51] |
| Cholesterol | between the phospholipids of animal cell membranes | moderates fluidity[^os51] |
| Integral proteins | inserted in the bilayer, often spanning it | channels, transporters, receptors[^os51] |
| Peripheral proteins | on one surface, bound to lipids or to integral proteins | enzymes, attachment points[^os51] |
| Carbohydrates | outer surface only, on glycoproteins and glycolipids | cell recognition[^os51][^alberts-mem] |

Proteins make up about half of the mass of a typical plasma membrane; lipids being much smaller, that is still about 50 lipid molecules for each protein.[^alberts-mem]

### Selective permeability

A protein-free bilayer sorts molecules by size and charge:[^alberts-tr]

| Class | Examples | Crossing |
|---|---|---|
| Small nonpolar | O₂, CO₂, N₂ | fast |
| Small uncharged polar | H₂O, urea, glycerol | slower |
| Large uncharged polar | glucose, sucrose | very slow |
| Ions | Na⁺, K⁺, Cl⁻, Ca²⁺, H⁺ | essentially none |

What the bilayer blocks, membrane transport proteins carry: **channels** open a water-filled pore, **transporters** (carriers and pumps) bind their cargo and change shape ([[Membrane Transport]]).[^alberts-tr][^os52]

## Deeper (L2)

### A two-dimensional fluid

Lipids exchange places with their neighbors within a leaflet so often that a lipid diffuses laterally with a coefficient of about $10^{-8}$ cm²/s, crossing the length of a large bacterium (about 2 µm) in about one second. Moving from one leaflet to the other ("flip-flop") is rare: less than once a month for a given lipid.[^alberts-mem] Lateral diffusion is measured by fluorescence recovery after photobleaching: a laser bleaches the fluorescent molecules of a small area, and the speed at which unbleached molecules move back in gives the diffusion coefficient ([[Microscopy]], [[Diffusion]]).[^alberts-mem]

Fluidity depends on temperature and composition: the kinks of unsaturated fatty acids keep tails from packing tightly, and cholesterol buffers fluidity against temperature changes.[^os51][^alberts-mem]

### Two different faces

The two leaflets have different lipid compositions, and sugar chains are found only on the face away from the cytosol.[^alberts-mem] Membrane proteins also have a fixed orientation, set when they are inserted during synthesis; the lumen of the endoplasmic reticulum corresponds to the outside of the cell ([[Endomembrane System#Deeper (L2)]]).

### Membrane proteins

**Integral** proteins cross the bilayer once (single-pass) or several times (multipass), usually as α helices of hydrophobic residues; some form β barrels instead. **Peripheral** proteins attach to the surface without entering the hydrophobic core ([[Membrane Protein]]).[^alberts-mem] Kyte and Doolittle gave each amino acid a hydropathy value, from 4.5 for isoleucine to −4.5 for arginine, and averaged it along the sequence: with a window of 19 residues, segments averaging above 1.6 are candidate transmembrane helices.[^kyte]

### Not every membrane is built the same

Archaeal membranes are made of isoprenoid chains linked to glycerol by ether bonds, not of fatty acids linked by ester bonds ([[Prokaryote]]).[^ospro]

## Advanced (L3)

- **Permeability is a number.** The flow of a solute across a bilayer is proportional to its concentration difference times a permeability coefficient $P$, and $P$ differs by many orders of magnitude between the classes of the table.[^alberts-tr] The Mathematical representation turns $P$ into an equilibration time.
- **Hydropathy is the first step of topology prediction.** A hydrophobic window marks a candidate helix, not a proof: signal peptides and buried hydrophobic cores of soluble proteins also score high, and short or amphipathic helices are missed.[^kyte] Statistical topology predictors replaced the single threshold; the logic of signal sequences is in [[Protein Targeting]] and [[Endomembrane System#Advanced (L3)]].
- **Physics of the bilayer.** Thickness, bending and elasticity of bilayers, and liposomes as model membranes, belong to [[Lipid Bilayer]].

## Mathematical representation

**Hydropathy profile.** For a protein $a_1 \dots a_n$, a hydropathy scale $h$ (one value per amino acid) and an odd window length $w$, the profile is

$$H_i = \frac{1}{w}\sum_{j=i}^{i+w-1} h(a_j), \qquad i = 1, \dots, n - w + 1,$$

and residues $i \dots i + w - 1$ are flagged when $H_i > \theta$. Kyte and Doolittle used $w = 19$ and $\theta = 1.6$.[^kyte]

**Passive permeation.** The flux (moles per unit area per unit time) is $J = P\,(C_{\mathrm{out}} - C_{\mathrm{in}})$, with $P$ the permeability coefficient in cm/s.[^alberts-tr] For a spherical cell of radius $r$, area over volume is $3/r$, so

$$\frac{dC_{\mathrm{in}}}{dt} = \frac{3P}{r}\left(C_{\mathrm{out}} - C_{\mathrm{in}}\right) \;\Rightarrow\; C_{\mathrm{in}}(t) = C_{\mathrm{out}}\left(1 - e^{-t/\tau}\right), \qquad \tau = \frac{r}{3P},$$

starting from $C_{\mathrm{in}}(0) = 0$ with a constant outside concentration.

**Lateral diffusion.** In two dimensions, the mean squared displacement grows as $\langle r^2 \rangle = 4Dt$,[^pboc] so covering a distance $x$ takes about $t \approx x^2/(4D)$. Check: $x = 2$ µm $= 2 \times 10^{-4}$ cm and $D = 10^{-8}$ cm²/s give $t = 1$ s, as stated above.

## Computational representation

The Kyte-Doolittle profile in a few lines:

```python
KD = {  # Kyte-Doolittle hydropathy index of each amino acid (Kyte and Doolittle 1982)
    "I": 4.5, "V": 4.2, "L": 3.8, "F": 2.8, "C": 2.5, "M": 1.9, "A": 1.8,
    "G": -0.4, "T": -0.7, "S": -0.8, "W": -0.9, "Y": -1.3, "P": -1.6,
    "H": -3.2, "E": -3.5, "Q": -3.5, "D": -3.5, "N": -3.5, "K": -3.9, "R": -4.5,
}


def hydropathy(seq: str, window: int = 19) -> list[float]:
    """Mean hydropathy of each window; entry i covers residues i+1 .. i+window (1-based)."""
    values = [KD[aa] for aa in seq]
    return [sum(values[i:i + window]) / window for i in range(len(values) - window + 1)]


def candidate_segments(seq: str, window: int = 19, threshold: float = 1.6) -> list[tuple[int, int]]:
    """Merge windows whose mean exceeds the threshold into 1-based inclusive segments."""
    segments = []
    for i, h in enumerate(hydropathy(seq, window)):
        if h > threshold:
            start, end = i + 1, i + window
            if segments and start <= segments[-1][1]:
                segments[-1] = (segments[-1][0], end)      # overlapping window: extend
            else:
                segments.append((start, end))
    return segments


TOY = {  # invented sequences
    "soluble": "MSEKPQTDNGRKLEESAKDTGQPNESRKAGDLEKTHQEPSNGKDE",
    "single_pass": "MSDNKERQTPEGSKD" + "LLAVIGLLFAVLIVAFLAGVL" + "RKRNQEESDKPQTSGEDR",
}
for name, seq in TOY.items():
    profile = hydropathy(seq)
    best = max(range(len(profile)), key=profile.__getitem__)
    print(name, len(seq), (best + 1, best + 19), round(profile[best], 2), candidate_segments(seq))
```

```text
soluble 45 (13, 31) -1.79 []
single_pass 54 (17, 35) 2.99 [(11, 39)]
```

The soluble toy protein never approaches the threshold. In the membrane toy protein, the hydrophobic stretch occupies residues 16 to 36; the best window (17 to 35) sits inside it, but the merged candidate segment (11 to 39) is wider, because windows that only partly overlap the stretch still average above 1.6. A window locates a helix; it blurs its ends.

## Worked example

> [!example] A spherical cell 10 µm across, by the numbers
> 1. **Lipids.** Surface $\pi d^2 = \pi \times 10^2 \approx 314$ µm²; at about $5 \times 10^6$ lipids per µm²,[^alberts-mem] about $1.6 \times 10^9$ lipid molecules, in line with the figure of about $10^9$ that Alberts gives for the plasma membrane of a small animal cell.[^alberts-mem]
> 2. **Lateral diffusion.** Across the cell: $t \approx x^2/(4D) = (10^{-3})^2 / (4 \times 10^{-8}) = 25$ s. A lipid can travel around the cell within a minute, yet it switches leaflets less than once a month.[^alberts-mem]
> 3. **Permeation.** With radius $r = 5$ µm $= 5 \times 10^{-4}$ cm, $\tau = r/(3P)$: for illustrative coefficients $P = 10^{-2}$, $10^{-6}$ and $10^{-10}$ cm/s, $\tau \approx 0.017$ s, 167 s and $1.7 \times 10^6$ s (about 19 days).
> 4. **Reading.** A solute in the fast class equilibrates in a fraction of a second; an ion-like coefficient makes the bare bilayer practically sealed, which is why cells move ions through channels and pumps.

## Common misconceptions

> [!warning] "The membrane is a rigid wall"
> It is a two-dimensional fluid: lipids and many proteins diffuse within the plane of the membrane.[^alberts-mem][^os51]

> [!warning] "Water cannot cross a lipid bilayer"
> Water is a small uncharged polar molecule and crosses a bare bilayer, more slowly than O₂ or CO₂.[^alberts-tr]

> [!warning] "Ions are stopped because they are too big"
> Ions are smaller than glucose yet cross far less: their charge, and the water shell it holds, keep them out of the hydrophobic core.[^alberts-tr]

> [!warning] "Lipids swap freely between the two layers"
> Flip-flop is rare, which is why the two leaflets can keep different compositions.[^alberts-mem]

## Exercises

> [!question] Exercise 1 (L1)
> Rank by speed of crossing a protein-free bilayer: Na⁺, O₂, glucose, H₂O, CO₂, urea. Justify with size and charge.

> [!success]- Solution
> O₂ and CO₂ (small, nonpolar) > H₂O and urea (small, uncharged polar) > glucose (large, polar) > Na⁺ (charged: essentially none). Nonpolar molecules dissolve in the hydrophobic core; polarity and size slow crossing; charge nearly forbids it.

> [!question] Exercise 2 (L1)
> Explain why phospholipids placed in water form a bilayer, and why its inside is a barrier to ions.

> [!success]- Solution
> Each phospholipid has a hydrophilic head and hydrophobic tails. In a bilayer, every head touches water and every tail is hidden among other tails, which the hydrophobic effect favors. The core of the bilayer is then a layer of hydrocarbon chains, into which a charged ion, surrounded by water, does not dissolve.

> [!question] Exercise 3 (L2)
> Predict the effect on membrane fluidity of: (a) replacing saturated with unsaturated fatty acids; (b) cooling the cell; (c) cholesterol, at high and at low temperature.

> [!success]- Solution
> (a) More fluid: the kinks of unsaturated tails prevent tight packing. (b) Less fluid: tails pack more tightly in the cold. (c) Cholesterol restrains phospholipid movement at high temperature and prevents tight packing at low temperature: it buffers fluidity against temperature changes.

> [!question] Exercise 4 (L2, Python)
> Derive $\tau = r/(3P)$ from $J = P\,\Delta C$, then compute $\tau$ for a cell of radius 5 µm and illustrative coefficients $10^{-2}$, $10^{-6}$ and $10^{-10}$ cm/s. How does $\tau$ change for a cell ten times larger?

> [!success]- Solution
> The amount inside, $V C_{\mathrm{in}}$, changes by the flux times the area: $V\,dC_{\mathrm{in}}/dt = A\,P\,(C_{\mathrm{out}} - C_{\mathrm{in}})$. With $A/V = 3/r$ the solution relaxes with time constant $r/(3P)$.
> ```python
> def equilibration_time_s(radius_um: float, p_cm_s: float) -> float:
>     """tau = r / (3P) for a spherical cell (radius converted from um to cm)."""
>     return radius_um * 1e-4 / (3 * p_cm_s)
>
>
> for p in (1e-2, 1e-6, 1e-10):                   # illustrative permeability coefficients, cm/s
>     tau = equilibration_time_s(5, p)
>     print(f"P = {p:.0e} cm/s: tau = {tau:.3g} s ({tau / 86400:.2g} days)")
> ```
> Output:
> ```text
> P = 1e-02 cm/s: tau = 0.0167 s (1.9e-07 days)
> P = 1e-06 cm/s: tau = 167 s (0.0019 days)
> P = 1e-10 cm/s: tau = 1.67e+06 s (19 days)
> ```
> $\tau$ is proportional to $r$: a cell ten times larger equilibrates ten times more slowly through its bilayer.

> [!question] Exercise 5 (L3, Python)
> Using `KD` and `hydropathy` from the Computational representation, write `runs_above(profile, threshold, window)` returning the residue spans covered by consecutive windows above the threshold. Apply it to the invented sequence below with windows of 19 and 7, and interpret the difference.

> [!success]- Solution
> ```python
> def runs_above(profile, threshold, window):
>     """1-based (start, end) residue spans covered by consecutive windows above threshold."""
>     spans, start = [], None
>     for i, h in enumerate(profile + [float("-inf")]):
>         if h > threshold and start is None:
>             start = i
>         elif h <= threshold and start is not None:
>             spans.append((start + 1, i - 1 + window))
>             start = None
>     return spans
>
>
> # Invented: a short hydrophobic N-terminal stretch, then a 22-residue hydrophobic stretch.
> seq = "MKLLVLAFSAQASTDPRNEKSGQ" + "WLVAILLGFVAVLLIAAFLLKV" + "RQRSDEENKPTEDGSKQ"
> for window in (19, 7):
>     profile = hydropathy(seq, window)
>     print(window, round(max(profile), 2), runs_above(profile, 1.6, window))
> ```
> Output:
> ```text
> 19 3.19 [(20, 47)]
> 7 3.59 [(1, 10), (23, 45)]
> ```
> With 19 residues, only the long stretch passes, as expected for a membrane-spanning helix. With 7, the short N-terminal stretch also passes: short windows are noisier and catch hydrophobic patches too short to span the bilayer, such as parts of signal peptides. The window length encodes a hypothesis about the size of the structure sought.

## Mastery checklist

- [ ] 1 Recognized: I can draw the bilayer with its proteins, cholesterol and sugars, and name the fluid mosaic model.
- [ ] 2 Understood: I can explain bilayer self-assembly, fluidity, asymmetry and which molecules cross a bare bilayer.
- [ ] 3 Practiced: I can compute a hydropathy profile and equilibration times in code.
- [ ] 4 Applied: I ran a hydropathy analysis on real membrane and soluble proteins and compared it with their annotated transmembrane regions.
- [ ] 5 Explained: I can teach why ions need proteins to cross, and the limits of window-based transmembrane prediction.

## References

[^os51]: [[Biology 2e (OpenStax)]], section 5.1 "Components and Structure" (the fluid mosaic model of Singer and Nicolson, membrane thickness, phospholipids, cholesterol, integral and peripheral proteins, carbohydrates, fluidity).
[^os52]: [[Biology 2e (OpenStax)]], section 5.2 "Passive Transport" (selective permeability).
[^os9]: [[Biology 2e (OpenStax)]], chapter "Cell Communication" (cell-surface receptors for signals that cannot cross the membrane).
[^ospro]: [[Biology 2e (OpenStax)]], chapter "Prokaryotes: Bacteria and Archaea" (archaeal membrane lipids).
[^alberts-mem]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of membrane structure (the common structure of biological membranes, amphipathic lipids and spontaneous bilayer formation, bilayer thickness, about $5 \times 10^6$ lipids per µm² and about $10^9$ in a small animal cell, lateral diffusion and flip-flop, fluorescence recovery after photobleaching, fluidity, asymmetry and glycolipids, membrane proteins as half of the membrane mass, α helices and β barrels).
[^alberts-tr]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of membrane transport of small molecules (relative permeability of a protein-free bilayer to classes of molecules, flow as permeability coefficient times concentration difference, channels and transporters, ion gradients).
[^kyte]: [[Kyte 1982 - A Simple Method for Displaying the Hydropathic Character of a Protein]], *Journal of Molecular Biology* 157:105-132.
[^lipinski]: [[Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability]], *Advanced Drug Delivery Reviews* 23:3-25 (the rule of 5).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., treatment of diffusion (mean squared displacement).
