---
aliases:
  - Beer's Law
  - Lambert-Beer Law
  - Absorbance
  - A260
  - A280
  - Loi de Beer-Lambert
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/bioinformatics
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Spectroscopy]]"
  - "[[Molar Concentration]]"
  - "[[Logarithm]]"
related:
  - "[[Nucleic Acid]]"
  - "[[DNA]]"
  - "[[Protein]]"
  - "[[Amino Acid]]"
  - "[[Reaction Kinetics]]"
  - "[[Linear Regression]]"
  - "[[System of Linear Equations]]"
  - "[[Sequencing Library Preparation]]"
projects: []
sources:
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Barbas 2007 - Quantitation of DNA and RNA]]"
---

# Beer-Lambert Law

> [!abstract]
> The Beer-Lambert law says that the absorbance of a solution grows in proportion to the concentration of the absorbing molecules and to the distance light travels through it, so measuring absorbance measures concentration.

## Definition

When monochromatic light of intensity $I_0$ crosses a solution and emerges with intensity $I$, the **absorbance** is $A = \log_{10}(I_0/I)$, and the **Beer-Lambert law** states[^leh]

$$A = \varepsilon\, c\, l,$$

where $c$ is the molar concentration of the absorbing species, $l$ the path length (usually 1 cm) and $\varepsilon$ the **molar absorption coefficient** (molar extinction coefficient, in M⁻¹ cm⁻¹), a property of the molecule at that wavelength.[^leh] The **transmittance** is $T = I/I_0 = 10^{-A}$.

## Why it matters

- **Sample QC before sequencing.** DNA and RNA are quantified by their absorbance at 260 nm, and their purity screened by absorbance ratios, before [[Sequencing Library Preparation]] and other assays.[^barbas]
- **Protein concentration.** Absorbance at 280 nm, due mainly to tryptophan and tyrosine, gives protein concentrations without reagents.[^leh][^berg] The coefficient can be estimated from the sequence (L2).
- **Rates.** Enzyme assays follow a product or cofactor by its absorbance over time; NADH, for example, absorbs at 340 nm where NAD⁺ does not ([[Reaction Kinetics]]).[^leh]
- **Plate-reader data.** Absorbance tables from 96-well readers are a common input to analysis scripts: blank subtraction, standard curves and dilution factors are code.

## Core (L1)

![[beer-lambert-cuvette.svg]]

**Absorbance is logarithmic.** Each unit of absorbance divides the transmitted light by 10:

| $A$ | 0.1 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| light transmitted | 79.4 % | 10 % | 1 % | 0.1 % |

The logarithm turns the exponential loss of light with depth into a quantity that is linear in concentration and in path length: doubling either doubles $A$ ([[Logarithm]]).

**From absorbance to concentration.** Rearranged, $c = A/(\varepsilon l)$. Remember the dilution factor: if the sample was diluted 20-fold before measuring, multiply the result by 20.

**Bio: A260 for nucleic acids.** The bases of DNA and RNA absorb ultraviolet light strongly near 260 nm.[^leh][^berg] For a 1 cm path, an absorbance of 1.0 at 260 nm corresponds to 50 µg/mL of double-stranded DNA or 40 µg/mL of RNA.[^barbas] So

$$\rho_{\text{dsDNA}} \,(\mu\text{g/mL}) = A_{260} \times 50 \times \text{dilution}, \qquad \rho_{\text{RNA}} = A_{260} \times 40 \times \text{dilution}.$$

**Bio: A280 for proteins.** The aromatic side chains of tryptophan and tyrosine absorb near 280 nm, so $A_{280}$ measures protein concentration once the protein's $\varepsilon_{280}$ is known.[^leh][^berg]

**Bio: the A260/A280 purity ratio.** Pure DNA has $A_{260}/A_{280} \approx 1.8$ and pure RNA about 2.0.[^barbas] Because proteins absorb most near 280 nm,[^leh][^berg] protein contamination lowers the ratio, though by less than one might expect (L2).

## Deeper (L2)

**When the law bends.** The law assumes monochromatic light, a dilute solution of molecules absorbing independently, and no scattering. At high absorbance so little light reaches the detector ($A = 3$ leaves 0.1 %) that stray light and detector noise dominate and readings fall below the line; particles and aggregates scatter light and add apparent absorbance. Practical rule: dilute into the range where a dilution series is linear, and check it with a standard curve.

**Absorbances add.** For several absorbing species at one wavelength, $A = l \sum_i \varepsilon_i c_i$. Measuring at as many wavelengths as there are species gives a [[System of Linear Equations]] whose solution is the composition (Exercise 4); with more wavelengths than species it becomes a least-squares fit.

**Melting changes absorbance.** Double-stranded DNA absorbs less at 260 nm than the same strands separated, so absorbance rises when DNA is heated through its melting transition; this is how melting curves are recorded.[^leh][^berg] A DNA conversion factor is therefore specific to its state.

**Coefficients from sequence.** Because tryptophan and tyrosine dominate absorbance at 280 nm and absorbances add, a protein's $\varepsilon_{280}$ can be estimated by summing per-residue contributions over its sequence, using published per-residue coefficients (this note gives none). It remains an estimate, since the surroundings of each aromatic ring in the folded protein can change its absorbance.

**Ratios are weak screens.** Because nucleic acids absorb strongly at 260 nm, a modest amount of a weakly absorbing contaminant barely moves $A_{260}/A_{280}$ (Exercise 5). A ratio near 1.8 is necessary, not sufficient, for a clean DNA sample.

## Mathematical representation

Light intensity decays exponentially with depth $x$ in the sample, $I(x) = I_0\, 10^{-\varepsilon c x}$, so

$$A = \log_{10}\frac{I_0}{I(l)} = \varepsilon c l.$$

For $n$ species measured at $m$ wavelengths, $\mathbf{a} = l\, E\, \mathbf{c}$, with $\mathbf{a} \in \mathbb{R}^m$ the absorbances, $E \in \mathbb{R}^{m \times n}$ the coefficients $\varepsilon_{ji}$ of species $i$ at wavelength $j$, and $\mathbf{c} \in \mathbb{R}^n$ the concentrations; for $m = n$ and invertible $E$, $\mathbf{c} = E^{-1}\mathbf{a}/l$. With mass concentrations, $A = a\,\rho\,l$, where $a$ is the specific absorbance per µg/mL: for double-stranded DNA at 260 nm, $a = 1/50 = 0.020$ (µg/mL)⁻¹ cm⁻¹.[^barbas]

## Computational representation

```python
import statistics

# ug/mL giving A260 = 1.0 in a 1 cm cell (Barbas 2007)
A260_FACTOR = {"dsDNA": 50.0, "RNA": 40.0}

def molar_concentration(absorbance: float, epsilon: float, path_cm: float = 1.0) -> float:
    """c = A / (epsilon * l), in mol/L when epsilon is in L mol^-1 cm^-1."""
    return absorbance / (epsilon * path_cm)

def nucleic_acid_ug_per_ml(a260: float, kind: str, dilution: float = 1.0, path_cm: float = 1.0) -> float:
    """Mass concentration of the undiluted sample from its A260."""
    return a260 / path_cm * A260_FACTOR[kind] * dilution

def standard_curve(conc: list[float], absorb: list[float]):
    """Least-squares line A = slope * c + intercept; returns a function A -> c."""
    slope, intercept = statistics.linear_regression(conc, absorb)
    return slope, intercept, (lambda a: (a - intercept) / slope)

for a in (0.1, 1.0, 2.0, 3.0):
    print(f"A = {a}: transmitted {100 * 10 ** -a:.3g} %")

print("c =", molar_concentration(0.42, 12_000), "M")            # invented epsilon
print(nucleic_acid_ug_per_ml(0.36, "dsDNA", dilution=20), "ug/mL dsDNA")
print("A260/A280 =", round(0.36 / 0.20, 2))

# invented standards (ug/mL) and their absorbances
slope, intercept, to_conc = standard_curve([0, 10, 20, 40, 80], [0.002, 0.051, 0.098, 0.203, 0.398])
print(f"slope {slope:.5f} per ug/mL, intercept {intercept:.4f}; unknown A = 0.150 -> {to_conc(0.150):.1f} ug/mL")
```

```text
A = 0.1: transmitted 79.4 %
A = 1.0: transmitted 10 %
A = 2.0: transmitted 1 %
A = 3.0: transmitted 0.1 %
c = 3.5e-05 M
360.0 ug/mL dsDNA
A260/A280 = 1.8
slope 0.00497 per ug/mL, intercept 0.0014; unknown A = 0.150 -> 29.9 ug/mL
```

A standard curve replaces a tabulated $\varepsilon$ when the absorbing species is a reaction product (colorimetric assays) or when the instrument's linear range must be checked: its slope is $\varepsilon l$ in the units of the standards.

## Worked example

> [!example] Quantifying a plasmid preparation (invented readings)
> A DNA sample is diluted 1:20 (5 µL in 95 µL of buffer) and read in a 1 cm cuvette against a buffer blank: $A_{260} = 0.36$, $A_{280} = 0.20$.
> 1. **In range?** 0.36 is a moderate absorbance (44 % transmitted): reliable.
> 2. **Concentration:** $0.36 \times 50 \times 20 = 360$ µg/mL of double-stranded DNA in the original sample.[^barbas]
> 3. **Amount:** a 50 µL preparation holds $360 \times 0.05 = 18$ µg.
> 4. **Purity:** $0.36/0.20 = 1.8$, the value expected for pure DNA.[^barbas] It rules out gross contamination, not small amounts of protein (L2).
> 5. **Record:** dilution factor, blank, path length and factor used, so that the number can be recomputed.

## Common misconceptions

> [!warning] "An absorbance of 1 means 100 % of the light is absorbed"
> $A = 1$ means 10 % is transmitted (90 % absorbed); $A = 2$ means 1 % transmitted. Absorbance is a logarithm, not a percentage.

> [!warning] "The higher the absorbance, the more precise the measurement"
> Above the linear range, too little light reaches the detector and readings become unreliable; dilute and multiply by the dilution factor instead.

> [!warning] "50 µg/mL per A260 unit works for any nucleic acid"
> That factor is for double-stranded DNA; RNA uses 40.[^barbas] Short or unusual molecules need their own coefficient.

> [!warning] "A ratio of 1.8 proves the DNA is pure"
> The ratio is insensitive to moderate amounts of weakly absorbing contaminants and blind to contaminants that absorb like DNA (Exercise 5).

## Exercises

> [!question] Exercise 1 (L1)
> What fraction of light is transmitted at $A = 0.5$? What absorbance corresponds to 25 % transmission?

> [!success]- Solution
> $T = 10^{-0.5} = 0.316$, about 32 %. $A = -\log_{10} 0.25 = 0.602$.

> [!question] Exercise 2 (L1)
> A compound with $\varepsilon = 12{,}000$ M⁻¹ cm⁻¹ (invented value) gives $A = 0.42$ in a 1 cm cuvette, after a 10-fold dilution. What is the concentration of the original solution?

> [!success]- Solution
> $c = 0.42/(12{,}000 \times 1) = 3.5 \times 10^{-5}$ M = 35 µM in the cuvette; the original solution is 10 times more concentrated: 350 µM.

> [!question] Exercise 3 (L1)
> An RNA extract is diluted 1:50 and reads $A_{260} = 0.25$ (1 cm). Give its concentration and the total RNA in 50 µL.

> [!success]- Solution
> $0.25 \times 40 \times 50 = 500$ µg/mL;[^barbas] in 50 µL, $500 \times 0.05 = 25$ µg.

> [!question] Exercise 4 (L2)
> Two species X and Y (invented coefficients, 1 cm path) have $\varepsilon_X = 10{,}000$ and $\varepsilon_Y = 3{,}000$ M⁻¹ cm⁻¹ at $\lambda_1$, and $\varepsilon_X = 2{,}000$ and $\varepsilon_Y = 8{,}000$ at $\lambda_2$. A mixture reads $A_1 = 0.62$ and $A_2 = 0.52$. Find both concentrations.

> [!success]- Solution
> Absorbances add: $10{,}000\,x + 3{,}000\,y = 0.62$ and $2{,}000\,x + 8{,}000\,y = 0.52$. The determinant is $8 \times 10^7 - 6 \times 10^6 = 7.4 \times 10^7$. By Cramer's rule, $x = (0.62 \times 8{,}000 - 3{,}000 \times 0.52)/7.4 \times 10^7 = 4.59 \times 10^{-5}$ M and $y = (10{,}000 \times 0.52 - 2{,}000 \times 0.62)/7.4 \times 10^7 = 5.35 \times 10^{-5}$ M. Two wavelengths, two unknowns: the system is solvable when the two spectra differ enough to make the determinant far from zero.

> [!question] Exercise 5 (L2, Python)
> Use the DNA factors (A260 = 1 per 50 µg/mL, ratio 1.8)[^barbas] and invented protein coefficients (0.00057 at 260 nm and 0.001 at 280 nm per µg/mL) to compute $A_{260}/A_{280}$ of 50 µg/mL DNA mixed with 0, 50, 200 and 1,000 µg/mL protein. What does the ratio detect?

> [!success]- Solution
> ```python
> DNA_260 = 1 / 50              # A260 per ug/mL of dsDNA, 1 cm (Barbas 2007)
> DNA_280 = DNA_260 / 1.8       # pure DNA ratio 1.8 (Barbas 2007)
> P_260, P_280 = 0.00057, 0.001 # invented protein coefficients per ug/mL
> for protein in (0, 50, 200, 1000):     # ug/mL of protein added to 50 ug/mL DNA
>     a260 = 50 * DNA_260 + protein * P_260
>     a280 = 50 * DNA_280 + protein * P_280
>     print(protein, round(a260, 3), round(a280, 3), round(a260 / a280, 2))
> # 0 1.0 0.556 1.8
> # 50 1.028 0.606 1.7
> # 200 1.114 0.756 1.47
> # 1000 1.57 1.556 1.01
> ```
>
> Under these assumptions, as much protein as DNA by mass lowers the ratio only from 1.8 to 1.7, within the scatter of routine readings; it takes a fourfold excess to reach 1.47. The ratio flags gross contamination; sensitive detection of protein needs another assay.

## Mastery checklist

- [ ] 1 Recognized: I can write $A = \varepsilon c l$ and define absorbance, transmittance and molar absorption coefficient.
- [ ] 2 Understood: I can explain why absorbance is logarithmic, why A260 and A280 report nucleic acids and proteins, and when the law fails.
- [ ] 3 Practiced: I can compute concentrations with dilution factors, nucleic acid yields and purity ratios, and fit a standard curve in Python.
- [ ] 4 Applied: I can process plate-reader or spectrophotometer exports into concentrations with recorded metadata, and resolve a two-component mixture.
- [ ] 5 Explained: I can teach the assumptions behind the law, the limits of purity ratios and how coefficients are estimated from sequence.

## References

[^leh]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of light absorption (the Lambert-Beer law, absorbance and molar extinction coefficient; absorbance of tryptophan and tyrosine near 280 nm), of nucleotides and nucleic acids (UV absorbance of bases near 260 nm, increase in absorbance on DNA denaturation) and of nicotinamide cofactors (NADH absorbance at 340 nm) (chapter numbers not verified).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein composition (aromatic amino acids absorb near 280 nm) and of nucleic acid structure (UV absorbance of bases, melting of double-stranded DNA followed by absorbance).
[^barbas]: [[Barbas 2007 - Quantitation of DNA and RNA]], *Cold Spring Harbor Protocols*, doi:10.1101/pdb.ip47 (A260 of 1.0 for 50 µg/mL dsDNA and 40 µg/mL RNA in a 1 cm path; A260/A280 of about 1.8 for pure DNA and 2.0 for pure RNA).
