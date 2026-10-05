---
aliases:
  - pOH
  - Ion Product of Water
  - Kw
  - Potential of Hydrogen
  - Potentiel hydrogène
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Water]]"
  - "[[Acid-Base Reaction]]"
  - "[[Molar Concentration]]"
  - "[[Logarithm]]"
  - "[[Chemical Equilibrium]]"
related:
  - "[[Acid-Base Equilibrium]]"
  - "[[Henderson-Hasselbalch Equation]]"
  - "[[Buffer Solution]]"
  - "[[Mitochondrion]]"
  - "[[Endomembrane System]]"
  - "[[Blood]]"
  - "[[Homeostasis]]"
  - "[[Isoelectric Point]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Molecular Cell Biology (Lodish)]]"
  - "[[Llopis 1998 - Measurement of Cytosolic, Mitochondrial, and Golgi pH in Single Living Cells with Green Fluorescent Proteins]]"
  - "[[Anatomy and Physiology 2e (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
---

# pH

> [!abstract]
> pH is a logarithmic measure of how many hydronium ions a solution contains: each unit down means ten times more, neutral water sits at 7 at 25 °C, and each compartment of a cell keeps its own value, from about 4.7 in lysosomes to about 8 in the mitochondrial matrix.

## Definition

The **pH** of an aqueous solution is $\mathrm{pH} = -\log_{10}[\mathrm{H_3O^+}]$, with the hydronium concentration in mol/L; likewise $\mathrm{pOH} = -\log_{10}[\mathrm{OH^-}]$. Water ionizes slightly, $\mathrm{2\,H_2O \rightleftharpoons H_3O^+ + OH^-}$, with the equilibrium constant $K_w = [\mathrm{H_3O^+}][\mathrm{OH^-}] = 1.0 \times 10^{-14}$ at 25 °C (the **ion product of water**), so $\mathrm{pH} + \mathrm{pOH} = 14.00$ at that temperature. A solution is neutral when $[\mathrm{H_3O^+}] = [\mathrm{OH^-}]$, acidic when $\mathrm{pH} < 7$ and basic when $\mathrm{pH} > 7$ (at 25 °C).[^chem14] $\mathrm{H^+}$ and $\mathrm{H_3O^+}$ are used interchangeably below.

## Why it matters

- **Charge follows pH.** Whether a side chain, a nucleotide or a drug is charged depends on pH relative to its pKa ([[Henderson-Hasselbalch Equation]]); a protein's net charge and [[Isoelectric Point]] are computed at a stated pH.
- **Compartments differ.** A protein in the lysosome works at a pH about 2.5 units below one in the cytosol;[^alberts][^lodish] localization predictions ([[Endomembrane System]]) therefore imply a chemical environment.
- **Gradients store energy.** The pH difference across the inner membrane of the [[Mitochondrion]] is part of the proton-motive force that makes ATP.
- **Every protocol states a pH.** Buffers, enzyme assays and chromatography are specified by pH, and reproducing a result means reproducing it ([[Buffer Solution]]).

## Core (L1)

### A logarithmic scale

| $[\mathrm{H_3O^+}]$ (M) | $10^{-2}$ | $10^{-4.75}$ | $10^{-7}$ | $10^{-8}$ | $10^{-12}$ |
|---|---:|---:|---:|---:|---:|
| pH | 2 | 4.75 | 7 | 8 | 12 |
| pOH (25 °C) | 12 | 9.25 | 7 | 6 | 2 |

One pH unit is a factor of 10 in $[\mathrm{H_3O^+}]$; two units, a factor of 100 ([[Logarithm]]).

### Using $K_w$

In any aqueous solution at 25 °C, $[\mathrm{OH^-}] = K_w/[\mathrm{H_3O^+}]$: knowing one concentration gives the other.[^chem14] A strong acid such as HCl ionizes completely, so $[\mathrm{H_3O^+}]$ equals its concentration, and 1.0 × 10⁻³ M HCl has pH 3.00; a strong base sets $[\mathrm{OH^-}]$ the same way ([[Acid-Base Reaction]]).[^chem14] Weak acids need their $K_a$ ([[Acid-Base Equilibrium]]).

### The pH of a cell's compartments

![[ph-scale-compartments-side-chain-pka.svg]]

| Compartment | Typical pH | How it is kept |
|---|---|---|
| Lysosome lumen | 4.5 to 5.0[^alberts][^lodish] | ATP-driven V-type proton pumps in the lysosomal membrane[^alberts][^lodish] |
| Golgi (medial/trans) | about 6.6 (6.58 in HeLa cells)[^llopis] | see [[Endomembrane System]] |
| Cytosol | about 7.2[^alberts]; 7.34 measured in HeLa cells[^llopis] | buffers ([[Buffer Solution]]) |
| Mitochondrial matrix | about 8 (7.98 in HeLa cells)[^llopis] | protons pumped out of the matrix by the respiratory chain[^alberts] ([[Mitochondrion]]) |
| Blood plasma (for comparison) | 7.35 to 7.45[^ap] | bicarbonate buffer and breathing ([[Buffer Solution]]) |

Lysosomal hydrolases work best at acidic pH. If they leak into the cytosol, near pH 7.2, they are largely inactive, which protects the cell from digesting itself.[^alberts] Measured values depend on cell type and state; the Llopis values come from pH-sensitive fluorescent proteins targeted to each compartment of living cells.[^llopis]

## Deeper (L2)

**Temperature.** $K_w$ increases with temperature, so neutral water has a pH below 7 when warmer than 25 °C: "neutral" means $[\mathrm{H_3O^+}] = [\mathrm{OH^-}] = \sqrt{K_w}$, not pH 7.[^chem14] Body-temperature work should use $K_w$ at 37 °C, and buffers are specified at their temperature of use.

**Very dilute acids.** Water itself supplies $10^{-7}$ M $\mathrm{H_3O^+}$ at 25 °C. For 1.0 × 10⁻⁸ M HCl the naive answer, pH 8, would make an acid solution basic. Counting both sources (charge balance $[\mathrm{H_3O^+}] = c + [\mathrm{OH^-}]$ with $[\mathrm{OH^-}] = K_w/[\mathrm{H_3O^+}]$) gives pH 6.98 (Exercise 3).

**Averaging pH is wrong.** pH is a logarithm, so averaging pH values averages exponents, not concentrations. Mixing equal volumes of strong-acid solutions at pH 3 and pH 5 gives pH 3.30, not 4 (Exercise 4). The same caution applies to summarizing pH data: compute means of $[\mathrm{H_3O^+}]$, or report medians.

**Gradients as stored free energy.** A pH difference across a membrane is a concentration gradient of protons: $\Delta G = 2.303\,RT\,\Delta\mathrm{pH}$ per mole of protons for the chemical part ([[Gibbs Free Energy#Deeper (L2)]]). The lysosome keeps $[\mathrm{H^+}]$ about 280 times higher than the cytosol (pH 4.75 against 7.2) and pays for it with ATP.[^alberts] Across the inner mitochondrial membrane, taking the matrix at 7.98 and the intermembrane space at the cytosolic 7.34 (assuming the outer membrane equilibrates the two, [[Mitochondrion]]), $\Delta\mathrm{pH} = 0.64$, worth $0.64 \times 61.5 \approx 39$ mV at 37 °C, added to the membrane potential in the proton-motive force.

## Advanced (L3)

- **Few free protons.** Concentrations hide small numbers. An *E. coli*-sized volume of about 1 µm³[^pboc] at pH 7.4 holds about 24 free hydronium ions on average (Exercise 5). Most protons in a cell sit on buffers, proteins and metabolites, so "the pH" of a tiny compartment is a time average of a fluctuating, buffered quantity.
- **Measuring pH in living cells.** Electrodes cannot enter organelles; genetically encoded sensors whose fluorescence depends on protonation, targeted by signal sequences, read pH compartment by compartment.[^llopis] Their readout is a [[Henderson-Hasselbalch Equation|Henderson-Hasselbalch]] curve of the sensor's chromophore, calibrated in situ.
- **pH as a signal.** Because compartments differ, the same molecule changes charge as it moves: a histidine-rich peptide or a drug with a pKa near 6 is neutral in the cytosol and positive in an endosome or lysosome, and its interactions with membranes and other molecules change accordingly ([[Henderson-Hasselbalch Equation]]).

## Mathematical representation

- $\mathrm{pH} = -\log_{10} h$ with $h = [\mathrm{H_3O^+}]/(1\,\mathrm{M})$; inversely $h = 10^{-\mathrm{pH}}$. Generally $\mathrm{p}X = -\log_{10} X$ (pOH, $\mathrm{p}K_w$, pKa).
- $K_w = h \cdot [\mathrm{OH^-}]$, hence $\mathrm{pH} + \mathrm{pOH} = \mathrm{p}K_w$ (14.00 at 25 °C); neutrality: $\mathrm{pH} = \mathrm{p}K_w/2$.
- Ratio between two solutions: $h_1/h_2 = 10^{\mathrm{pH}_2 - \mathrm{pH}_1}$.
- Strong monoprotic acid at concentration $c$, exactly: $h = c + K_w/h$, so $h = \dfrac{c + \sqrt{c^2 + 4K_w}}{2}$, which tends to $c$ when $c \gg 10^{-7}$ and to $\sqrt{K_w}$ when $c \to 0$.
- Mixing volumes $V_i$ of strong-acid solutions: $h = \sum_i V_i h_i / \sum_i V_i$ (when $h_i \gg 10^{-7}$), then $\mathrm{pH} = -\log_{10} h$.

## Computational representation

```python
import math

KW_25C = 1.0e-14   # ion product of water at 25 C


def ph_from_h(h: float) -> float:
    return -math.log10(h)


def h_from_ph(ph: float) -> float:
    return 10 ** (-ph)


def poh_from_ph(ph: float, kw: float = KW_25C) -> float:
    return -math.log10(kw) - ph


def ph_strong_acid(c: float, kw: float = KW_25C) -> float:
    """Exact pH of a strong monoprotic acid at concentration c (M), counting water's own H+."""
    h = (c + math.sqrt(c * c + 4 * kw)) / 2   # from h = c + kw / h
    return ph_from_h(h)


# Typical compartment pH (cited in the note); lysosome: middle of 4.5-5.0
COMPARTMENTS = {"lysosome": 4.75, "Golgi": 6.58, "cytosol": 7.2, "blood": 7.4, "mitochondrial matrix": 7.98}
for name, ph in COMPARTMENTS.items():
    print(f"{name:21s} pH {ph:5.2f}  [H+] = {h_from_ph(ph):.1e} M  pOH (25 C) = {poh_from_ph(ph):.2f}")
ratio = h_from_ph(COMPARTMENTS["lysosome"]) / h_from_ph(COMPARTMENTS["cytosol"])
print(f"lysosome / cytosol [H+] ratio: {ratio:.0f}")
print(f"1e-3 M HCl: pH {ph_strong_acid(1e-3):.2f}; 1e-8 M HCl: pH {ph_strong_acid(1e-8):.2f}")
```

```text
lysosome              pH  4.75  [H+] = 1.8e-05 M  pOH (25 C) = 9.25
Golgi                 pH  6.58  [H+] = 2.6e-07 M  pOH (25 C) = 7.42
cytosol               pH  7.20  [H+] = 6.3e-08 M  pOH (25 C) = 6.80
blood                 pH  7.40  [H+] = 4.0e-08 M  pOH (25 C) = 6.60
mitochondrial matrix  pH  7.98  [H+] = 1.0e-08 M  pOH (25 C) = 6.02
lysosome / cytosol [H+] ratio: 282
1e-3 M HCl: pH 3.00; 1e-8 M HCl: pH 6.98
```

The pOH column uses $K_w$ at 25 °C, a simplification for compartments at 37 °C. Store pH as a float with its temperature in metadata; convert to concentrations before any averaging.

## Worked example

> [!example] From the lysosome to the cytosol
> A lysosome at pH 4.75 and the cytosol at pH 7.2 (values from the table).
> 1. **Concentrations**: lysosome $10^{-4.75} = 1.8 \times 10^{-5}$ M; cytosol $10^{-7.2} = 6.3 \times 10^{-8}$ M.
> 2. **Ratio**: $10^{7.2 - 4.75} = 10^{2.45} \approx 280$: protons are about 280 times more concentrated inside.
> 3. **pOH** (25 °C approximation): $14 - 4.75 = 9.25$ inside, $[\mathrm{OH^-}] = 5.6 \times 10^{-10}$ M.
> 4. **Read it**: the lysosomal membrane holds a 280-fold proton gradient, which its ATP-driven pumps maintain.[^alberts] A 2.45-unit difference looks small on the pH scale; in concentrations it is more than two orders of magnitude.

## Common misconceptions

> [!warning] "pH 7 is always neutral"
> Neutral means $[\mathrm{H_3O^+}] = [\mathrm{OH^-}]$. Because $K_w$ grows with temperature, neutral water is below pH 7 when warmer than 25 °C.[^chem14]

> [!warning] "pH 4 is twice as acidic as pH 8"
> pH 4 has $10^4 = 10{,}000$ times more hydronium than pH 8. The scale is logarithmic.

> [!warning] "The cell has one pH"
> Each compartment has its own, from about 4.5 in lysosomes to about 8 in the mitochondrial matrix.[^alberts][^llopis] "Physiological pH 7.4" describes blood plasma, not the inside of a cell.[^ap]

> [!warning] "Diluting an acid tenfold forever raises the pH by one each time"
> Only while the acid dominates. Near $10^{-7}$ M, water's own ionization takes over and the pH approaches 7 without crossing it.

## Exercises

> [!question] Exercise 1 (L1)
> A solution has $[\mathrm{H_3O^+}] = 3.2 \times 10^{-5}$ M at 25 °C. Give its pH, pOH and $[\mathrm{OH^-}]$. Is it acidic?

> [!success]- Solution
> pH $= -\log_{10}(3.2 \times 10^{-5}) = 4.49$; pOH $= 14.00 - 4.49 = 9.51$; $[\mathrm{OH^-}] = 10^{-14}/3.2 \times 10^{-5} = 3.1 \times 10^{-10}$ M. Acidic (pH < 7), close to lysosomal acidity.

> [!question] Exercise 2 (L1)
> How many times higher is $[\mathrm{H^+}]$ in the lysosome (pH 4.5) than in the mitochondrial matrix (pH 8.0)?

> [!success]- Solution
> $10^{8.0 - 4.5} = 10^{3.5} \approx 3200$. Three and a half pH units separate the most acidic and most basic common compartments of a human cell.

> [!question] Exercise 3 (L2)
> Compute the pH of 1.0 × 10⁻⁸ M HCl at 25 °C, and explain why the answer is not 8.

> [!success]- Solution
> Charge balance: $h = 10^{-8} + 10^{-14}/h$, so $h^2 - 10^{-8}h - 10^{-14} = 0$ and $h = (10^{-8} + \sqrt{10^{-16} + 4 \times 10^{-14}})/2 = 1.05 \times 10^{-7}$ M, pH 6.98. Water contributes ten times more $\mathrm{H_3O^+}$ than the acid; adding acid can only lower the pH.

> [!question] Exercise 4 (L2)
> Equal volumes of two strong-acid solutions, pH 3.0 and pH 5.0, are mixed. Find the pH of the mixture.

> [!success]- Solution
> $h = (10^{-3} + 10^{-5})/2 = 5.05 \times 10^{-4}$ M, pH 3.30. The more acidic solution dominates; the average of the pH values (4.0) is meaningless.

> [!question] Exercise 5 (L3, Python)
> Count free hydronium ions (a) in a 1 µm³ volume, the size of an *E. coli* cell, at pH 7.4 (an assumed value); (b) in a spherical lysosome of diameter 0.5 µm (an assumed size) at pH 4.75, and in the same volume at pH 7.2. Use $N_A = 6.022 \times 10^{23}$ mol⁻¹. What does the result mean for "pH" at this scale?

> [!success]- Solution
> ```python
> N_A = 6.022e23
> def free_protons(ph: float, volume_um3: float) -> float:
>     """Number of free H+ (hydronium) ions in a volume given in cubic micrometres (1 um^3 = 1e-15 L)."""
>     return h_from_ph(ph) * volume_um3 * 1e-15 * N_A
> print(f"1 um^3 at pH 7.4: {free_protons(7.4, 1.0):.0f}")
> v_lys = 4 / 3 * math.pi * 0.25 ** 3
> print(f"lysosome 0.5 um diameter: V = {v_lys:.3f} um^3, at pH 4.75: {free_protons(4.75, v_lys):.0f}, at pH 7.2: {free_protons(7.2, v_lys):.2f}")
> ```
> Output: `1 um^3 at pH 7.4: 24`, then `lysosome 0.5 um diameter: V = 0.065 um^3, at pH 4.75: 701, at pH 7.2: 2.49`. A bacterium contains a few dozen free protons and a cytosol-like lysosome would contain two or three: pH is an average over time of a number that fluctuates, and it is held steady by buffers that carry far more bound protons ([[Buffer Solution]]).[^pboc]

## Mastery checklist

- [ ] 1 Recognized: I can define pH and pOH and give the pH of neutral water at 25 °C.
- [ ] 2 Understood: I can explain $K_w$, the logarithmic scale and why each compartment has its own pH.
- [ ] 3 Practiced: I can convert between pH, $[\mathrm{H_3O^+}]$, pOH and $[\mathrm{OH^-}]$, and handle dilute acids and mixtures, by hand and in Python.
- [ ] 4 Applied: I can state the pH a protein experiences given its localization, and compute its charge there with the right pKa values.
- [ ] 5 Explained: I can teach why pH 7 is not always neutral, why pH values must not be averaged, and what pH means in a volume containing a few protons.

## References

[^chem14]: [[Chemistry 2e (OpenStax)]], ch. 14 "Acid-Base Equilibria" (autoionization of water and $K_w$, its temperature dependence, pH and pOH, strong acids and bases).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of lysosomes (acid hydrolases, lumen pH about 4.5 to 5.0 maintained by an ATP-driven H⁺ pump, cytosol pH about 7.2, inactivity of leaked hydrolases at cytosolic pH) and of mitochondria (protons pumped out of the matrix by the respiratory chain).
[^lodish]: [[Molecular Cell Biology (Lodish)]], 4th ed. (2000), treatment of V-class H⁺ ATPases that keep lysosomes and vacuoles acidic (lumen pH 4.5 to 5.0).
[^llopis]: [[Llopis 1998 - Measurement of Cytosolic, Mitochondrial, and Golgi pH in Single Living Cells with Green Fluorescent Proteins]], *PNAS* 95(12):6803-6808 (matrix 7.98 ± 0.07, Golgi 6.58 and cytosol 7.34 in HeLa cells).
[^ap]: [[Anatomy and Physiology 2e (OpenStax)]], treatment of acid-base balance (normal blood pH 7.35 to 7.45).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., ch. 1 "Why: Biology by the Numbers" (an *E. coli* cell as a volume of about 1 µm³).
