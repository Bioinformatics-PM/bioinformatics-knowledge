---
aliases:
  - Log P
  - logP
  - Octanol-Water Partition Coefficient
  - Pow
  - Partition Ratio
  - Log D
  - Distribution Coefficient
  - Coefficient de partage
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/industry
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Chemical Potential]]"
  - "[[Chemical Equilibrium]]"
  - "[[Hydrophobic Effect]]"
  - "[[Henderson-Hasselbalch Equation]]"
  - "[[Logarithm]]"
related:
  - "[[Cell Membrane]]"
  - "[[Lipid Bilayer]]"
  - "[[Fick's Law]]"
  - "[[Hydropathy Plot]]"
  - "[[Amino Acid]]"
  - "[[ADMET]]"
  - "[[Lead Optimization]]"
  - "[[Quantitative Structure-Activity Relationship]]"
  - "[[Van 't Hoff Equation]]"
projects: []
sources:
  - "[[IUPAC Gold Book]]"
  - "[[OECD 1995 - Test No. 107, Partition Coefficient (n-Octanol-Water), Shake Flask Method]]"
  - "[[Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Kyte 1982 - A Simple Method for Displaying the Hydropathic Character of a Protein]]"
  - "[[Chothia 1974 - Hydrophobic Bonding and Accessible Surface Area in Proteins]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Partition Coefficient

> [!abstract]
> The partition coefficient P is the ratio of a solute's concentrations in two immiscible solvents at equilibrium, by convention n-octanol over water; its logarithm, log P, is a free energy of transfer in disguise and the standard measure of how hydrophobic a molecule is.

## Definition

IUPAC calls this quantity a **partition ratio**: the ratio of the concentration of a substance in a single definite form in the extract to its concentration in the same form in the other phase, at equilibrium.[^iupac-p] The **distribution ratio** $D$ instead compares the total concentrations of the solute in each phase, whatever its chemical form, and therefore varies with conditions such as pH; for aqueous/organic systems the organic phase goes in the numerator.[^iupac-d] In pharmacology and cheminformatics, "the" partition coefficient is the n-octanol/water ratio of the neutral species, $P = c_{\text{octanol}}/c_{\text{water}}$, reported as $\log P$; the shake-flask method measures it for $\log P$ between −2 and 4.[^oecd] Its pH-dependent counterpart for ionizable molecules is $\log D$.

## Why it matters

- **Drug-likeness filters.** The rule of 5 flags likely poor absorption or permeation when, among other criteria, a compound's calculated log P exceeds 5;[^lipinski] log P is therefore computed for every molecule of a virtual library ([[ADMET]], [[Lead Optimization]], [[Quantitative Structure-Activity Relationship]]).
- **Passive permeation.** The smaller a molecule and the more soluble it is in oil, the faster it diffuses across a protein-free lipid bilayer[^alberts] ([[Cell Membrane]]); the model below makes permeability proportional to $P$.
- **Hydrophobicity of residues.** Hydropathy scales and transfer free energies say how strongly side chains avoid water: the inputs of [[Hydropathy Plot|hydropathy plots]] and of folding arguments ([[Hydrophobic Effect]], [[Amino Acid]]).
- **A chemical-potential problem.** $P$ is what equal chemical potentials look like when the two regions are different solvents ([[Chemical Potential]]).

## Core (L2)

### Equal chemical potentials, unequal concentrations

At equilibrium the solute has the same chemical potential in both phases, $\mu^\circ_w + RT\ln(c_w/c^\circ) = \mu^\circ_o + RT\ln(c_o/c^\circ)$, so

$$P = \frac{c_o}{c_w} = e^{-(\mu^\circ_o - \mu^\circ_w)/RT}, \qquad \Delta G^\circ_{w\to o} = \mu^\circ_o - \mu^\circ_w = -RT\ln P = -RT\ln 10 \cdot \log P.$$

At 25 °C each log unit is worth 5.71 kJ/mol ([[Hydrophobic Effect#Deeper (L2)]]): a solute of log P 3 is 17.1 kJ/mol more stable in octanol, and 99.9 % of it sits in the octanol when the volumes are equal (code). For dilute solutions $P$ does not depend on concentration (the Nernst partition law); dissociation or association of the solute breaks this.[^oecd]

### Measuring log P: the shake flask

The OECD guideline fixes what a valid measurement needs: a temperature between 20 and 25 °C held within ±1 °C; three runs with different octanol/water volume ratios, each in duplicate; separation of the phases, usually by centrifugation; analysis by photometry, gas chromatography or HPLC; and agreement of the six log P values within ±0.3. It does not apply to surface-active substances.[^oecd] If the amount added is known, analysing one phase is enough, the mass balance gives the other (Worked example). Varying the volume ratio is a built-in check: a true partition constant must not depend on it.

### log D: ionizable molecules

Most drugs are weak acids or bases. If only the neutral form enters octanol, $D$ is $P$ times the neutral fraction given by the [[Henderson-Hasselbalch Equation]]:

$$\log D = \log P - \log_{10}\!\left(1 + 10^{\,\mathrm{pH} - \mathrm{p}K_a}\right) \ \text{(acid)}, \qquad \log D = \log P - \log_{10}\!\left(1 + 10^{\,\mathrm{p}K_a - \mathrm{pH}}\right) \ \text{(base)}.$$

Beyond the pKa, on the side where the molecule is ionized, log D falls by one unit per pH unit (figure, panel b). An invented acid with pKa 4.5 and log P 3.0 has log D 3.0 at pH 2 but 0.1 at pH 7.4: at neutral pH it behaves as a hydrophilic molecule.

![[octanol-water-partition-log-d.svg]]

### Bio: membranes, residues and drugs

- **Permeability follows P.** Treat the bilayer as an oily slab of thickness $d$. At each face the solute equilibrates with the water next to it, so just inside the slab its concentration is $K c$; it then diffuses across with coefficient $D_m$. Fick's law across the slab gives $J = (KD_m/d)(c_1 - c_2)$, so the permeability coefficient $P_m = KD_m/d$ is proportional to the partition coefficient $K$ ([[Fick's Law]], [[Cell Membrane#Mathematical representation]]). This is the quantitative form of the observation that oil-soluble molecules cross bilayers faster.[^alberts]
- **Hydrophobicity scales.** A scale gives one number per side chain; Kyte and Doolittle's runs from 4.5 for isoleucine to −4.5 for arginine.[^kyte] A scale built from partition measurements expresses each side chain as $-RT\ln P$ of a side-chain analogue: a transfer free energy, the quantity behind Kauzmann's "hydrophobic bond", the free energy gained when nonpolar residues move from water into the protein interior, which Chothia related to the surface area that folding buries.[^chothia] Scales built on different reference phases rank borderline residues differently, so record which one a tool uses ([[Hydropathy Plot]]).
- **Drug-likeness.** For an ionizable drug the number that matters at a given pH is log D, not log P; the rule of 5, which uses calculated log P, is a filter for poor absorption, not a prediction of it.[^lipinski]

## Advanced (L3)

- **Additivity.** If the groups of a molecule contribute independently to the transfer free energy, $\log P$ is a sum of group contributions, and each CH₂ of a homologous series adds the same increment (Exercise 5). The rule of 5 uses calculated log P values, estimated from structure;[^lipinski] the simplest such estimate is a sum of fragment contributions, and its errors come from intramolecular interactions that additivity ignores.
- **Octanol is a convention, not a membrane.** A bilayer is a thin, structured film with polar interfaces ([[Cell Membrane]], [[Lipid Bilayer]]), not a bulk solvent. Log P ranks passive permeation; it does not include transport proteins, and substrates of transporters are among the compounds that escape the rule of 5, as its authors noted for some compound classes.[^lipinski]
- **Temperature.** $P$ is an equilibrium constant, so it follows the [[Van 't Hoff Equation]]: $d\ln P/d(1/T) = -\Delta H_{tr}/R$. With a transfer enthalpy of −33.5 kJ/mol (invented), one kelvin moves log P by 0.02 (Exercise 6): small against the ±0.3 acceptance, but systematic, one reason why the guideline holds the temperature within ±1 °C.[^oecd]

## Mathematical representation

- $P = c_o/c_w$ for one species; $\log P = \log_{10} P$; $D = \sum_{\text{forms}} c_o \big/ \sum_{\text{forms}} c_w$.
- $\Delta G^\circ_{w\to o} = \mu^\circ_o - \mu^\circ_w = -RT\ln P$.
- Phase volumes $V_o$, $V_w$: fraction in octanol $\varphi_o = PV_o/(PV_o + V_w)$; mass balance $c_o = (n - c_wV_w)/V_o$.
- Neutral fraction $\alpha_0 = 1/(1 + 10^{\mathrm{pH} - \mathrm{p}K_a})$ for an acid, $1/(1 + 10^{\mathrm{p}K_a - \mathrm{pH}})$ for a base; $D = \alpha_0 P$ if ions stay in water.
- Slab permeation: $P_m = KD_m/d$, $J = P_m(c_1 - c_2)$.
- Additivity: $\log P \approx \sum_j n_j f_j$; for a homologous series $\log P(n) = a + b\,n$, with $-RT\ln 10 \cdot b$ the transfer free energy of one CH₂.
- Temperature: $d\ln P/d(1/T) = -\Delta H_{tr}/R$.

## Computational representation

Four small functions cover the note; free energies in kJ/mol with $R$ from CODATA:[^nist]

```python
import math

R = 8.314462618e-3   # kJ/(mol K), CODATA (exact)


def dg_transfer(log_p: float, t: float = 298.15) -> float:
    """Standard free energy (kJ/mol) of moving the solute from water to octanol."""
    return -R * t * math.log(10) * log_p


def fraction_in_octanol(log_p: float, v_oct: float, v_water: float) -> float:
    p = 10 ** log_p
    return p * v_oct / (p * v_oct + v_water)


def log_d(log_p: float, pka: float, ph: float, kind: str) -> float:
    """log D when only the neutral form enters octanol; kind is 'acid' or 'base'."""
    x = ph - pka if kind == "acid" else pka - ph
    return log_p - math.log10(1 + 10 ** x)


def shake_flask_log_p(n_total: float, c_water: float, v_oct: float, v_water: float) -> float:
    """log P from the amount added (mol), the measured water concentration (M) and volumes (L)."""
    c_oct = (n_total - c_water * v_water) / v_oct          # mass balance
    return math.log10(c_oct / c_water)


for lp in (-1, 0, 1, 2, 3, 5):
    print(f"log P = {lp:2d}: dG(w->o) = {dg_transfer(lp) + 0.0:6.1f} kJ/mol, "
          f"in octanol at equal volumes: {fraction_in_octanol(lp, 1, 1):.4f}")

for kind, pka in (("acid", 4.5), ("base", 9.0)):              # invented drugs with log P = 3.0
    print(kind, [round(log_d(3.0, pka, ph, kind), 2) for ph in (2.0, 7.4)])

# invented shake-flask run: 1.00 umol per vessel, three volume ratios in duplicate
runs = [(0.010, 0.010, 0.97e-6), (0.010, 0.010, 1.02e-6),
        (0.005, 0.010, 1.90e-6), (0.005, 0.010, 2.05e-6),
        (0.010, 0.005, 0.98e-6), (0.010, 0.005, 1.03e-6)]
values = [shake_flask_log_p(1.00e-6, cw, vo, vw) for vo, vw, cw in runs]
print([round(v, 2) for v in values])
mean = sum(values) / len(values)
print(f"mean log P = {mean:.2f}, spread {min(values) - mean:+.2f} to {max(values) - mean:+.2f}")
```

```text
log P = -1: dG(w->o) =    5.7 kJ/mol, in octanol at equal volumes: 0.0909
log P =  0: dG(w->o) =    0.0 kJ/mol, in octanol at equal volumes: 0.5000
log P =  1: dG(w->o) =   -5.7 kJ/mol, in octanol at equal volumes: 0.9091
log P =  2: dG(w->o) =  -11.4 kJ/mol, in octanol at equal volumes: 0.9901
log P =  3: dG(w->o) =  -17.1 kJ/mol, in octanol at equal volumes: 0.9990
log P =  5: dG(w->o) =  -28.5 kJ/mol, in octanol at equal volumes: 1.0000
acid [3.0, 0.1]
base [-4.0, 1.39]
[2.01, 1.99, 2.01, 1.98, 2.01, 1.98]
mean log P = 2.00, spread -0.02 to +0.02
```

In compound tables, record whether a value is measured or calculated, and whether it is log P or log D (at which pH): the four are not interchangeable.

## Worked example

> [!example] A shake-flask log P with the guideline's design (invented data)
> 1.00 µmol of a neutral compound goes into each of six vessels: two with 10 mL octanol and 10 mL water, two with 5 + 10 mL, two with 10 + 5 mL. After shaking, centrifugation and analysis of the water phase: $c_w$ = 0.97, 1.02, 1.90, 2.05, 0.98 and 1.03 µM.
> 1. **Mass balance, first vessel**: water holds $0.97\ \mu\text{M} \times 0.010\ \text{L} = 0.0097$ µmol, so octanol holds $1.00 - 0.0097 = 0.9903$ µmol in 10 mL: $c_o = 99.03$ µM.
> 2. **Partition coefficient**: $P = 99.03/0.97 = 102.1$, $\log P = 2.01$.
> 3. **All six vessels** (`shake_flask_log_p`): 2.01, 1.99, 2.01, 1.98, 2.01, 1.98; mean 2.00, spread ±0.02, well inside the ±0.3 acceptance.[^oecd]
> 4. **Read it**: $\Delta G^\circ_{w\to o} = -11.4$ kJ/mol. With 99 % of the compound in octanol, the small water concentration carries all the measurement error; reducing the octanol volume leaves more compound in the water phase to measure, one reason to vary the volume ratio.

## Common misconceptions

> [!warning] "log P and log D are the same number"
> $P$ refers to one chemical form, $D$ to all forms together, and $D$ changes with pH.[^iupac-p][^iupac-d] For the invented acid of the figure they differ by 2.9 units at pH 7.4.

> [!warning] "The higher the log P, the better the drug"
> Hydrophobicity speeds passive permeation, but the rule of 5 treats a calculated log P above 5 as a warning sign for poor absorption or permeation.[^lipinski] Drug design looks for a window, not a maximum.

> [!warning] "Octanol/water reproduces a cell membrane"
> It is a reproducible convention for ranking molecules. A bilayer is a thin, structured film with interfaces, and many molecules cross membranes through proteins ([[Membrane Transport]]).

> [!warning] "A measured partition ratio is a constant of the molecule"
> Only for one defined form at a given temperature. Measuring an ionizable compound without controlling the pH gives a distribution ratio, not $P$,[^iupac-d] and dissociation or association of the solute makes the apparent value depend on concentration.[^oecd]

## Exercises

> [!question] Exercise 1 (L2)
> A compound has log P = 2.0. Compute its transfer free energy from water to octanol at 25 °C, and the fraction in octanol for equal volumes and for an octanol volume one tenth of the water volume.

> [!success]- Solution
> $\Delta G^\circ_{w\to o} = -5.71 \times 2.0 = -11.42$ kJ/mol. Fractions: $100/(100 + 1) = 0.9901$ and $100 \times 0.1/(100 \times 0.1 + 1) = 0.9091$ (`fraction_in_octanol(2, 0.1, 1)`). Shrinking the octanol volume tenfold leaves 9 % of the compound in water instead of 1 %.

> [!question] Exercise 2 (L2)
> An invented weak acid has pKa 4.2 and log P 3.5. Compute log D at pH 1.5 and at pH 7.4.

> [!success]- Solution
> pH 1.5: $3.5 - \log_{10}(1 + 10^{-2.7}) = 3.50$, the acid is neutral. pH 7.4: $3.5 - \log_{10}(1 + 10^{3.2}) = 3.5 - 3.20 = 0.30$. Three pH units above the pKa cost about three log units of apparent hydrophobicity.

> [!question] Exercise 3 (L2)
> An invented weak base has pKa 9.5 and log P 2.0. Compute log D at pH 7.4 and at pH 9.5.

> [!success]- Solution
> pH 7.4: $2.0 - \log_{10}(1 + 10^{2.1}) = -0.10$, mostly protonated and hydrophilic. pH 9.5 (= pKa): half neutral, $\log D = 2.0 - \log_{10} 2 = 1.70$. For a base, log D rises with pH until the pKa is passed.

> [!question] Exercise 4 (L3, Python)
> Two invented molecules of the same size have log P 1 and 3; with the slab model their permeability coefficients are $10^{-7}$ and $10^{-5}$ cm/s. For a spherical cell of radius 10 µm, compute the equilibration time $\tau = r/(3P_m)$ of each ([[Cell Membrane#Mathematical representation]]).

> [!success]- Solution
> ```python
> r_cm = 10e-4
> for lp, pm in ((1, 1e-7), (3, 1e-5)):
>     print(f"log P {lp}: P_m = {pm:.0e} cm/s, tau = r/(3 P_m) = {r_cm / (3 * pm):.3g} s")
> ```
> ```text
> log P 1: P_m = 1e-07 cm/s, tau = r/(3 P_m) = 3.33e+03 s
> log P 3: P_m = 1e-05 cm/s, tau = r/(3 P_m) = 33.3 s
> ```
> Two log units of $P$ are two orders of magnitude in permeability at equal size and diffusion coefficient: about an hour against half a minute.

> [!question] Exercise 5 (L3, Python)
> Invented log P values of a homologous series with 1 to 5 CH₂ groups: 0.02, 0.51, 1.05, 1.53, 2.07. Fit a line and convert the increment per CH₂ into a transfer free energy.

> [!success]- Solution
> ```python
> n = [1, 2, 3, 4, 5]
> lp_obs = [0.02, 0.51, 1.05, 1.53, 2.07]      # invented homologous series
> mx, my = sum(n) / 5, sum(lp_obs) / 5
> slope = sum((a - mx) * (b - my) for a, b in zip(n, lp_obs)) / sum((a - mx) ** 2 for a in n)
> print(f"increment per CH2 = {slope:.3f} log units = {dg_transfer(slope):.2f} kJ/mol")
> ```
> Output: `increment per CH2 = 0.512 log units = -2.92 kJ/mol`. A constant increment is additivity: each CH₂ buries the same extra nonpolar area, in line with a hydrophobic free energy proportional to area.[^chothia]

> [!question] Exercise 6 (L3, Python)
> Invented measurements give log P = 2.10 at 20 °C and 2.00 at 25 °C. Estimate the transfer enthalpy with the van 't Hoff equation, and how much a 1 K error in temperature shifts log P near 25 °C.

> [!success]- Solution
> ```python
> lp20, lp25 = 2.10, 2.00
> dh_tr = 8.314462618 * math.log(10 ** (lp25 - lp20)) / (1 / 293.15 - 1 / 298.15)
> shift = -dh_tr / (8.314462618 * math.log(10)) * (1 / 297.15 - 1 / 298.15)
> print(f"dH_tr = {dh_tr / 1000:.1f} kJ/mol; log P at 24 C minus log P at 25 C = {shift:+.3f}")
> ```
> Output: `dH_tr = -33.5 kJ/mol; log P at 24 C minus log P at 25 C = +0.020`. Transfer into octanol is exothermic here, so cooling favors it. A kelvin shifts log P by 0.02: negligible against ±0.3, but a systematic bias if every run is off in the same direction.

## Mastery checklist

- [ ] 1 Recognized: I can define log P and log D and say which phase goes in the numerator.
- [ ] 2 Understood: I can derive $P$ from equal chemical potentials, convert log P to a transfer free energy, and explain why log D depends on pH.
- [ ] 3 Practiced: I can analyse a shake-flask experiment, compute log D curves and permeation times in Python.
- [ ] 4 Applied: I compared measured and calculated log P values of real compounds from a database, and filtered a compound set with the rule of 5.
- [ ] 5 Explained: I can teach the slab model of permeation, additivity and its failures, and why octanol/water is a convention rather than a membrane.

## References

[^iupac-p]: [[IUPAC Gold Book]], entry "partition ratio, $K_D$" (P04440): ratio of the concentration of a substance in a single definite form in the extract to its concentration in the same form in the other phase at equilibrium; distribution coefficient, distribution ratio, partition constant and extraction constant are not to be used as synonyms.
[^iupac-d]: [[IUPAC Gold Book]], entry "distribution ratio, $D$" (D01817): ratio of the total analytical concentrations of a solute in the two phases, regardless of chemical form, varying with conditions such as pH; organic phase in the numerator for aqueous/organic systems.
[^oecd]: [[OECD 1995 - Test No. 107, Partition Coefficient (n-Octanol-Water), Shake Flask Method]] (range $\log P$ −2 to 4, surface-active substances excluded, Nernst partition law and deviations from dissociation or association, 20 to 25 °C within ±1 °C, three volume ratios in duplicate, centrifugation and analysis, six values within ±0.3).
[^lipinski]: [[Lipinski 1997 - Experimental and Computational Approaches to Estimate Solubility and Permeability]], *Advanced Drug Delivery Reviews* 23:3-25 (the rule of 5 with calculated log P above 5; estimating properties from structure; exceptions such as transporter substrates).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of membrane transport of small molecules (the rate of diffusion across a protein-free bilayer depends on the size of the molecule and its relative solubility in oil).
[^kyte]: [[Kyte 1982 - A Simple Method for Displaying the Hydropathic Character of a Protein]], *Journal of Molecular Biology* 157:105-132, the hydropathy scale.
[^chothia]: [[Chothia 1974 - Hydrophobic Bonding and Accessible Surface Area in Proteins]], *Nature* 248:338-339 (the hydrophobic bond as the free energy of transferring nonpolar residues from water to the protein interior, related to buried accessible surface area).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA value of the molar gas constant, $R = 8.314\,462\,618\ldots$ J mol⁻¹ K⁻¹ (exact).
