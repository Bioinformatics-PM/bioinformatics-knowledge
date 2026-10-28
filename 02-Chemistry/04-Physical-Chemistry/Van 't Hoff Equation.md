---
aliases:
  - Van 't Hoff Plot
  - Van 't Hoff Isochore
  - Van 't Hoff Enthalpy
  - Équation de van 't Hoff
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/bioinformatics
  - domain/physics
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Chemical Equilibrium]]"
  - "[[Gibbs Free Energy]]"
  - "[[Enthalpy]]"
  - "[[Logarithm]]"
  - "[[Derivative]]"
related:
  - "[[Le Chatelier's Principle]]"
  - "[[Heat Capacity]]"
  - "[[Polymerase Chain Reaction]]"
  - "[[Nucleic Acid Hybridization]]"
  - "[[DNA]]"
  - "[[Protein Folding]]"
  - "[[Two-State Model]]"
  - "[[Activation Energy]]"
  - "[[Linear Regression]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[NobelPrize.org]]"
  - "[[SantaLucia 1998 - A Unified View of Polymer, Dumbbell, and Oligonucleotide DNA Nearest-Neighbor Thermodynamics]]"
  - "[[Untergasser 2012 - Primer3 New Capabilities and Interfaces]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]]"
  - "[[Myers 1995 - Denaturant m Values and Heat Capacity Changes]]"
---

# Van 't Hoff Equation

> [!abstract]
> The van 't Hoff equation says how an equilibrium constant changes with temperature: the slope of ln K against 1/T is −ΔH°/R, so measuring K, or a melting curve, at several temperatures gives the enthalpy of a reaction, of a DNA duplex or of protein unfolding.

## Definition

For a reaction of standard enthalpy change $\Delta H^\circ$, the equilibrium constant $K$ varies with the absolute temperature $T$ as

$$\frac{d\ln K}{dT} = \frac{\Delta H^\circ}{RT^2} \qquad\Longleftrightarrow\qquad \frac{d\ln K}{d(1/T)} = -\frac{\Delta H^\circ}{R},$$

with $R$ the gas constant. It follows from $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$ and $\Delta G^\circ = -RT\ln K$[^chem16] (Mathematical representation). When $\Delta H^\circ$ and $\Delta S^\circ$ are constant over the range studied, $\ln K$ is a straight line in $1/T$:

$$\ln K = -\frac{\Delta H^\circ}{R}\,\frac{1}{T} + \frac{\Delta S^\circ}{R}, \qquad \ln\frac{K_2}{K_1} = -\frac{\Delta H^\circ}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right).$$

The equation is named after J. H. van 't Hoff, awarded the first Nobel Prize in Chemistry (1901) for the discovery of "the laws of chemical dynamics and osmotic pressure in solutions".[^nobel]

## Why it matters

- **Primer and probe design.** Melting temperatures of PCR primers, qPCR probes and hybridization probes can be computed from duplex $\Delta H^\circ$ and $\Delta S^\circ$ predicted by nearest-neighbor models;[^santalucia] Primer3 uses such thermodynamic models rather than simple counting rules ([[Polymerase Chain Reaction]], [[Nucleic Acid Hybridization]]).[^primer3]
- **Protein stability from melting curves.** Any signal that tells folded from unfolded molecules, recorded while heating, gives a melting temperature $T_m$ and a van 't Hoff enthalpy; a mutation or a bound ligand that changes the stability moves $T_m$ ([[Protein Folding]], [[Heat Capacity]]).
- **Converting constants between temperatures.** Binding constants and $K'$ values are measured at one temperature (often 25 °C) and used at another (37 °C); the equation says how much they move ([[Chemical Equilibrium]]).

## Core (L2)

### Reading the equation

Combining $\Delta G^\circ = -RT\ln K$ with $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$ gives $\ln K = -\Delta H^\circ/RT + \Delta S^\circ/R$: the enthalpy sets the temperature dependence, the entropy the level.

- **Sign.** If $\Delta H^\circ > 0$ (endothermic), $K$ grows with $T$; if $\Delta H^\circ < 0$, it falls. This is the quantitative form of the temperature rule of [[Le Chatelier's Principle]].
- **Size.** The larger $|\Delta H^\circ|$, the steeper the dependence. Duplex formation of a 20-mer releases about 650 kJ/mol, so its $K$ drops a thousandfold between 60 and 70 °C (code below): hybridization is switched on and off by a few degrees.

### The van 't Hoff plot

Measure $K$ at several temperatures and plot $\ln K$ against $1/T$: the slope is $-\Delta H^\circ/R$ and the intercept $\Delta S^\circ/R$. The enthalpy obtained this way, from the temperature dependence of an equilibrium rather than from heat, is the **van 't Hoff enthalpy** $\Delta H_{vH}$.

![[van-t-hoff-plot-melting-curves.svg]]

### Two-state melting curves

For a unimolecular transition N ⇌ U (a protein unfolding, a hairpin opening), $K = f/(1-f)$ with $f$ the unfolded fraction. At the midpoint $K = 1$, so $T_m = \Delta H^\circ/\Delta S^\circ$, and

$$f(T) = \frac{1}{1 + \exp\!\left[\dfrac{\Delta H^\circ}{R}\left(\dfrac{1}{T} - \dfrac{1}{T_m}\right)\right]}, \qquad \left.\frac{df}{dT}\right|_{T_m} = \frac{\Delta H^\circ}{4RT_m^2}.$$

The width of the transition scales as $RT_m^2/\Delta H^\circ$: a cooperative transition with a large enthalpy is sharp (figure, panel a). Transforming $f$ into $\ln[f/(1-f)]$ turns the curve into a van 't Hoff line (panel b), which is how $\Delta H_{vH}$ is extracted from a thermal unfolding curve (`vant_hoff_fit` below).

### Bio: DNA duplexes and primer melting temperature

Heating separates the two strands of DNA, and G-C-rich DNA melts at a higher temperature;[^berg] stacking between neighboring base pairs provides most of the stability ([[DNA#Deeper (L2)]]).[^yakovchuk] Two features distinguish duplex melting from protein unfolding:

- **It is bimolecular.** For $\mathrm{A + B \rightleftharpoons D}$, $K = [\mathrm{D}]/([\mathrm{A}][\mathrm{B}])$. With both strands at $C_T/2$, half of the strands are paired at $T_m$, so $[\mathrm{D}] = [\mathrm{A}] = [\mathrm{B}] = C_T/4$ and $K(T_m) = 4/C_T$:
$$T_m = \frac{\Delta H^\circ}{\Delta S^\circ + R\ln(C_T/4)}.$$
The melting temperature depends on strand concentration. For a self-complementary strand $K(T_m) = 1/C_T$; for a primer in large excess at concentration $c$ over its template, $K(T_m) = 1/c$.
- **$\Delta H^\circ$ and $\Delta S^\circ$ are predicted from sequence.** In the nearest-neighbor model they are sums over the $n - 1$ dinucleotide steps of the duplex, plus an initiation term for each terminal pair and a symmetry term for self-complementary duplexes. SantaLucia put the parameter sets of seven laboratories in one format, found six in close agreement, and derived a unified set from 108 oligonucleotide duplexes, with empirical salt corrections.[^santalucia] The unified values are the `NN`, `INIT` and `SYMMETRY` entries of the code below: ten stacks, from −7.2 kcal/mol (AT/TA) to −10.6 kcal/mol (CG/GC) in $\Delta H^\circ$.

They hold for 1 M NaCl (1 kcal = 4.184 kJ). The ten steps cover all sixteen dinucleotides, because a step and its reverse complement are the same stack seen from the other strand (TT/AA is AA/TT). At other salt concentrations a salt correction is applied:[^santalucia] record the parameter set, the salt correction and the strand concentration with every Tm you report.

## Advanced (L3)

- **A second van 't Hoff method.** Rearranging the bimolecular $T_m$ gives $1/T_m = (R/\Delta H^\circ)\ln(C_T/4) + \Delta S^\circ/\Delta H^\circ$: melting the same duplex at several concentrations and plotting $1/T_m$ against $\ln(C_T/4)$ yields $\Delta H^\circ$ without fitting the shape of any single curve (Exercise 4).
- **Curved plots.** $\Delta H^\circ$ itself changes with temperature when the heat capacity changes, $d\Delta H^\circ/dT = \Delta C_p$. For proteins, $\Delta C_p$ of unfolding is large and correlates with the surface area newly exposed to solvent;[^myers] the van 't Hoff plot then curves, and the stability curve bends down on both sides of a maximum, down to cold denaturation ([[Heat Capacity#Deeper (L2)]]). A straight-line fit over a wide range returns only an average $\Delta H$.
- **Van 't Hoff versus calorimetric enthalpy.** A calorimeter measures the total heat of unfolding directly (the area of the excess heat capacity peak, [[Heat Capacity]]), while $\Delta H_{vH}$ comes from the *shape* of the transition under a two-state assumption. A protein that unfolds through intermediates, or as independent domains, melts more broadly than a two-state protein of the same total enthalpy, so its $\Delta H_{vH}$ is smaller (Exercise 5). Agreement of the two enthalpies is the classic test of two-state behavior ([[Two-State Model]]).
- **The kinetic twin.** The Arrhenius plot of $\ln k$ against $1/T$ has slope $-E_a/R$ ([[Activation Energy]]). Since $K = k_f/k_r$ for an elementary step ([[Chemical Equilibrium#Advanced (L3)]]), the two plots are linked: $\Delta H^\circ = E_{a,f} - E_{a,r}$.

## Mathematical representation

- **Gibbs-Helmholtz.** From $G = H - TS$ and $(\partial G/\partial T)_p = -S$: $\dfrac{\partial (G/T)}{\partial T} = \dfrac{1}{T}\dfrac{\partial G}{\partial T} - \dfrac{G}{T^2} = -\dfrac{S}{T} - \dfrac{H - TS}{T^2} = -\dfrac{H}{T^2}$. Applied to $\Delta G^\circ/T = -R\ln K$, it gives $d\ln K/dT = \Delta H^\circ/RT^2$, valid even when $\Delta H^\circ$ depends on $T$.
- **Constant $\Delta H^\circ$, $\Delta S^\circ$**: $\ln K = -\Delta H^\circ/RT + \Delta S^\circ/R$.
- **Unimolecular two-state**: $K = f/(1-f)$, $T_m = \Delta H^\circ/\Delta S^\circ$, $f(T)$ as above; the 10 % to 90 % width satisfies $1/T_{10} - 1/T_{90} = 2R\ln 9/\Delta H^\circ$, about $2RT_m^2\ln 9/\Delta H^\circ$ in kelvin.
- **Bimolecular**: $K(T_m) = x/c$ and $T_m = \Delta H^\circ/(\Delta S^\circ + R\ln(c/x))$, with $x = 4$ for two strands at $c/2$ each, $x = 1$ for a self-complementary strand at total $c$ or for one strand in excess at $c$.
- **Nearest-neighbor model** for $s = s_1 \dots s_n$: $\Delta H^\circ = \sum_{i=1}^{n-1}\Delta H^\circ(s_is_{i+1}) + \Delta H^\circ_{\text{init}}(s_1) + \Delta H^\circ_{\text{init}}(s_n)$ (+ symmetry term), and likewise for $\Delta S^\circ$.

## Computational representation

The parameters live in a dictionary keyed by the ten unique steps; a missing step is looked up through its reverse complement. Energies are converted to SI once, at the end, with $R$ from CODATA:[^nist]

```python
import math

R = 8.314462618        # J/(mol K), CODATA (exact)
CAL = 4.184            # J per thermochemical calorie

# Unified nearest-neighbor parameters in 1 M NaCl (SantaLucia 1998):
# 5'-XY-3' step paired with its complement -> (dH kcal/mol, dS cal/(mol K))
NN = {"AA": (-7.9, -22.2), "AT": (-7.2, -20.4), "TA": (-7.2, -21.3),
      "CA": (-8.5, -22.7), "GT": (-8.4, -22.4), "CT": (-7.8, -21.0),
      "GA": (-8.2, -22.2), "CG": (-10.6, -27.2), "GC": (-9.8, -24.4),
      "GG": (-8.0, -19.9)}
INIT = {"G": (0.1, -2.8), "C": (0.1, -2.8), "A": (2.3, 4.1), "T": (2.3, 4.1)}  # per terminal pair
SYMMETRY = (0.0, -1.4)          # self-complementary duplexes only
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def reverse_complement(s: str) -> str:
    return s.translate(COMPLEMENT)[::-1]


def duplex_thermo(seq: str) -> tuple[float, float]:
    """dH (J/mol) and dS (J/(mol K)) of seq paired with its perfect complement."""
    dh = ds = 0.0
    for i in range(len(seq) - 1):
        step = seq[i:i + 2]
        h, s = NN[step] if step in NN else NN[reverse_complement(step)]
        dh, ds = dh + h, ds + s
    for end in (seq[0], seq[-1]):
        dh, ds = dh + INIT[end][0], ds + INIT[end][1]
    if seq == reverse_complement(seq):
        dh, ds = dh + SYMMETRY[0], ds + SYMMETRY[1]
    return dh * 1000 * CAL, ds * CAL


def tm_duplex(dh: float, ds: float, c: float, x: int = 4) -> float:
    """Two-state Tm (K), where K(Tm) = x / c. x = 4: two strands at c/2 each (c = total);
    x = 1: a self-complementary strand at total c, or one strand in large excess at c."""
    return dh / (ds + R * math.log(c / x))


def vant_hoff_fit(temps: list[float], fractions: list[float]) -> tuple[float, float, float]:
    """Least-squares line ln K = -dH/(RT) + dS/R with K = f/(1 - f); returns dH, dS, Tm."""
    pts = [(1 / t, math.log(f / (1 - f))) for t, f in zip(temps, fractions)]
    mx = sum(x for x, _ in pts) / len(pts)
    my = sum(y for _, y in pts) / len(pts)
    slope = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, _ in pts)
    intercept = my - slope * mx
    return -R * slope, R * intercept, -slope / intercept


primer = "AGCTTGCAGTCCATGGTACG"           # invented 20-mer
dh, ds = duplex_thermo(primer)
print(f"dH = {dh / 1000:.1f} kJ/mol, dS = {ds:.1f} J/(mol K), dG(37 C) = {(dh - 310.15 * ds) / 1000:.1f} kJ/mol")
print(f"Tm, both strands 0.25 uM: {tm_duplex(dh, ds, 0.5e-6) - 273.15:.1f} C; "
      f"primer in excess at 0.5 uM: {tm_duplex(dh, ds, 0.5e-6, x=1) - 273.15:.1f} C")
for t_c in (60, 70):
    k = math.exp(-dh / (R * (t_c + 273.15)) + ds / R)
    print(f"K at {t_c} C = {k:.3g} per M")

# invented melting curve of a small protein: fraction unfolded at six temperatures
temps = [322.0, 325.0, 328.0, 331.0, 334.0, 337.0]
f_unf = [0.03, 0.10, 0.28, 0.61, 0.85, 0.96]
dh_vh, ds_vh, tm_vh = vant_hoff_fit(temps, f_unf)
print(f"protein: dH_vH = {dh_vh / 1000:.0f} kJ/mol, dS = {ds_vh:.0f} J/(mol K), Tm = {tm_vh - 273.15:.1f} C")
```

```text
dH = -656.5 kJ/mol, dS = -1764.0 J/(mol K), dG(37 C) = -109.4 kJ/mol
Tm, both strands 0.25 uM: 73.1 C; primer in excess at 0.5 uM: 75.2 C
K at 60 C = 6.13e+10 per M
K at 70 C = 6.13e+07 per M
protein: dH_vH = 399 kJ/mol, dS = 1210 J/(mol K), Tm = 56.7 C
```

These Tm values are for 1 M NaCl, without salt correction. Biopython's `Bio.SeqUtils.MeltingTemp.Tm_NN`, called with its table `DNA_NN3` (the same values) and no salt correction, returns the same 73.07 °C and 75.18 °C: a useful test for your own implementation, not a substitute for it.

## Worked example

> [!example] Melting temperature of a 10-bp duplex (invented sequence)
> Duplex 5'-GACTGCATCG-3' with its complement, 1 µM total strands, 1 M NaCl.
> 1. **Steps.** Nine steps; those absent from the table are read through their reverse complement (AC is GT/CA, TG is CA/GT, TC is GA/CT):
>
> | Step | GA | AC | CT | TG | GC | CA | AT | TC | CG |
> |---|---|---|---|---|---|---|---|---|---|
> | $\Delta H^\circ$ (kcal/mol) | −8.2 | −8.4 | −7.8 | −8.5 | −9.8 | −8.5 | −7.2 | −8.2 | −10.6 |
> | $\Delta S^\circ$ (cal mol⁻¹ K⁻¹) | −22.2 | −22.4 | −21.0 | −22.7 | −24.4 | −22.7 | −20.4 | −22.2 | −27.2 |
>
> Sums over the nine steps: −77.2 kcal/mol and −205.2 cal mol⁻¹ K⁻¹.
>
> 2. **Ends and symmetry.** Both terminal pairs are G·C: add $2 \times (+0.1, -2.8)$. The reverse complement, CGATGCAGTC, differs from the sequence, so there is no symmetry term. Total: $\Delta H^\circ = -77.0$ kcal/mol $= -322.2$ kJ/mol, $\Delta S^\circ = -210.8$ cal mol⁻¹ K⁻¹ $= -882.0$ J mol⁻¹ K⁻¹.
> 3. **Melting temperature.** $K(T_m) = 4/C_T$: the denominator is $-882.0 + 8.314\ln(2.5 \times 10^{-7}) = -882.0 - 126.4 = -1008.4$ J mol⁻¹ K⁻¹, so $T_m = 322\,200/1008.4 = 319.5$ K $= 46.3$ °C (`duplex_thermo` and `tm_duplex` agree).
> 4. **Read it.** At 37 °C, $\Delta G^\circ = -322.2 + 310.15 \times 0.882 = -48.6$ kJ/mol, a strongly favorable duplex, yet half of it melts by 46 °C: with such a large $\Delta H^\circ$, every few degrees change $K$ by orders of magnitude.

## Common misconceptions

> [!warning] "The melting temperature is a property of the sequence"
> For a bimolecular duplex it also depends on strand concentration (Exercise 4: about 3.5 °C per tenfold for a 20-mer) and on salt, through the correction applied to 1 M NaCl parameters.[^santalucia] A Tm without its conditions cannot be compared with another.

> [!warning] "A straight van 't Hoff plot proves a two-state transition"
> A least-squares line always returns some enthalpy. Two independent domains give an almost straight plot and a $\Delta H_{vH}$ far below the true total (Exercise 5); only comparison with the calorimetric enthalpy tests the two-state model.

> [!warning] "GC content alone sets the melting temperature"
> The nearest-neighbor model sums stacks, not bases: two invented 10-mers with the same composition and the same ends melt 4.4 °C apart (Exercise 6). Composition-only rules are rough approximations of this sum.

> [!warning] "A duplex with a higher Tm is more stable at every temperature"
> Stability at temperature $T$ is $\Delta G^\circ(T) = \Delta H^\circ - T\Delta S^\circ$. Two duplexes with different $\Delta H^\circ/\Delta S^\circ$ have $\Delta G^\circ$ lines that can cross, so their order of stability at the annealing temperature can differ from their order of $T_m$.

## Exercises

> [!question] Exercise 1 (L2)
> A binding reaction has $K = 1.0 \times 10^6$ M⁻¹ at 25 °C and $\Delta H^\circ = -40$ kJ/mol (invented). Estimate $K$ at 37 °C. Does warming strengthen or weaken binding?

> [!success]- Solution
> $\ln(K_2/K_1) = -(\Delta H^\circ/R)(1/T_2 - 1/T_1) = (40\,000/8.314)(1/310.15 - 1/298.15) = -0.624$, so $K_{37} = 1.0 \times 10^6 \times 0.536 = 5.36 \times 10^5$ M⁻¹. An exothermic binding weakens on warming, as Le Chatelier predicts.

> [!question] Exercise 2 (L2)
> An equilibrium constant is 50 at 20 °C and 5 at 40 °C. Estimate $\Delta H^\circ$, assuming it is constant.

> [!success]- Solution
> $\Delta H^\circ = R\ln(K_2/K_1)/(1/T_1 - 1/T_2) = 8.314 \times \ln(0.1)/(1/293.15 - 1/313.15) = 8.314 \times (-2.303)/(2.179 \times 10^{-4}) = -87.9$ kJ/mol. A tenfold drop over 20 K means a strongly exothermic reaction.

> [!question] Exercise 3 (L2)
> A two-state protein unfolds with $\Delta H^\circ = 300$ kJ/mol and $T_m = 330$ K. Between which temperatures does the unfolded fraction go from 10 % to 90 %?

> [!success]- Solution
> $f = 0.1$ and $0.9$ mean $\ln K = \mp\ln 9$, so $1/T = 1/T_m \pm R\ln 9/\Delta H^\circ$: $T_{10} = 323.5$ K and $T_{90} = 336.8$ K, a width of 13.3 K, equal to the approximation $2RT_m^2\ln 9/\Delta H^\circ = 13.3$ K. Doubling $\Delta H^\circ$ would halve it.

> [!question] Exercise 4 (L3, Python)
> With `duplex_thermo` and `tm_duplex`, compute the $T_m$ of the invented 20-mer at total strand concentrations of 0.1, 1 and 10 µM. Then recover $\Delta H^\circ$ from the slope of $1/T_m$ against $\ln(C_T/4)$.

> [!success]- Solution
> ```python
> cs = [1e-7, 1e-6, 1e-5]
> inv_tm = [1 / tm_duplex(dh, ds, c) for c in cs]
> for c, y in zip(cs, inv_tm):
>     print(f"C_T = {c:.0e} M: Tm = {1 / y - 273.15:.1f} C")
> xs = [math.log(c / 4) for c in cs]
> mx, my = sum(xs) / 3, sum(inv_tm) / 3
> slope = sum((x - mx) * (y - my) for x, y in zip(xs, inv_tm)) / sum((x - mx) ** 2 for x in xs)
> print(f"dH = R / slope = {R / slope / 1000:.1f} kJ/mol")
> ```
> ```text
> C_T = 1e-07 M: Tm = 70.6 C
> C_T = 1e-06 M: Tm = 74.1 C
> C_T = 1e-05 M: Tm = 77.7 C
> dH = R / slope = -656.5 kJ/mol
> ```
> Each tenfold increase in concentration raises $T_m$ by about 3.5 °C, and the slope returns the model's $\Delta H^\circ$ exactly. With measured melting temperatures, this plot gives $\Delta H^\circ$ without fitting the shape of any curve.

> [!question] Exercise 5 (L3, Python)
> An invented protein has two independent domains, each two-state with $\Delta H^\circ = 300$ kJ/mol, melting at 330 and 340 K. Simulate the average unfolded fraction from 310 to 360 K, keep the points with $0.1 < f < 0.9$, and fit them with `vant_hoff_fit`. Compare with the total enthalpy, 600 kJ/mol, that a calorimeter would measure.

> [!success]- Solution
> ```python
> def unfolded(t, dh_, tm_):
>     return 1 / (1 + math.exp(dh_ / R * (1 / t - 1 / tm_)))
> grid = [310 + 0.5 * i for i in range(101)]                       # 310 to 360 K
> f2 = [(unfolded(t, 300e3, 330.0) + unfolded(t, 300e3, 340.0)) / 2 for t in grid]
> sel = [(t, f) for t, f in zip(grid, f2) if 0.1 < f < 0.9]
> dh_app, _, tm_app = vant_hoff_fit([t for t, _ in sel], [f for _, f in sel])
> print(f"apparent dH_vH = {dh_app / 1000:.0f} kJ/mol (true total 600), apparent Tm = {tm_app:.1f} K")
> ```
> Output: `apparent dH_vH = 201 kJ/mol (true total 600), apparent Tm = 334.9 K`. The combined transition is broad, so a two-state fit sees a small enthalpy, smaller even than one domain's. A ratio $\Delta H_{vH}/\Delta H_{\text{cal}}$ well below 1 is the signature of a transition that is not two-state.

> [!question] Exercise 6 (L3, Python)
> Compare the predicted $T_m$ (1 µM total, 1 M NaCl) of the invented duplexes GGGGGAAAAA and GAGAGAGAGA. Same composition, same terminal pairs: why do they differ?

> [!success]- Solution
> ```python
> for s in ("GGGGGAAAAA", "GAGAGAGAGA"):
>     d, e = duplex_thermo(s)
>     print(f"{s}: dH = {d / 1000:.1f} kJ/mol, dS = {e:.1f} J/(mol K), Tm(1 uM) = {tm_duplex(d, e, 1e-6) - 273.15:.1f} C")
> ```
> ```text
> GGGGGAAAAA: dH = -290.4 kJ/mol, dS = -792.0 J/(mol K), Tm(1 uM) = 43.0 C
> GAGAGAGAGA: dH = -292.0 kJ/mol, dS = -810.4 J/(mol K), Tm(1 uM) = 38.6 C
> ```
> The first has GG/CC and AA/TT stacks, the second alternates GA/CT stacks with AG steps (the CT/GA entry); their enthalpies are almost equal, but the alternating duplex pays a larger entropy cost. Stability is a property of stacks, which is why composition-only formulas can be wrong by several degrees.

## Mastery checklist

- [ ] 1 Recognized: I can state $d\ln K/dT = \Delta H^\circ/RT^2$ and say what the slope of a van 't Hoff plot is.
- [ ] 2 Understood: I can explain why melting curves are sharp when $\Delta H^\circ$ is large, why duplex $T_m$ depends on strand concentration, and how the nearest-neighbor model predicts $\Delta H^\circ$ and $\Delta S^\circ$.
- [ ] 3 Practiced: I can compute a nearest-neighbor $T_m$ and fit a van 't Hoff enthalpy to a melting curve in Python.
- [ ] 4 Applied: I compared my $T_m$ for real primers with a primer-design tool, matching its parameter set, salt correction and concentration.
- [ ] 5 Explained: I can teach the van 't Hoff versus calorimetric enthalpy test, the effect of $\Delta C_p$ on the plot, and the limits of two-state and nearest-neighbor models.

## References

[^chem16]: [[Chemistry 2e (OpenStax)]], ch. 16 "Thermodynamics", §16.4 "Free Energy" ($\Delta G = \Delta H - T\Delta S$, $\Delta G^\circ = -RT\ln K$).
[^nobel]: [[NobelPrize.org]], "The Nobel Prize in Chemistry 1901" (J. H. van 't Hoff, sole laureate; the prize motivation cites the discovery of "the laws of chemical dynamics and osmotic pressure in solutions").
[^santalucia]: [[SantaLucia 1998 - A Unified View of Polymer, Dumbbell, and Oligonucleotide DNA Nearest-Neighbor Thermodynamics]], *PNAS* 95(4):1460-1465 (seven parameter sets compared, six in agreement; unified nearest-neighbor $\Delta H^\circ$ and $\Delta S^\circ$ in 1 M NaCl from 108 duplexes; empirical salt dependence).
[^primer3]: [[Untergasser 2012 - Primer3 New Capabilities and Interfaces]], *Nucleic Acids Research* 40(15):e115 (thermodynamic models for melting temperature, hairpins and primer dimers).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of DNA structure (strand separation on heating, higher melting temperature of G-C-rich DNA).
[^yakovchuk]: [[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]], *Nucleic Acids Research* (stacking as the main contribution to duplex stability).
[^myers]: [[Myers 1995 - Denaturant m Values and Heat Capacity Changes]], *Protein Science* 4(10):2138-2148 ($\Delta C_p$ of unfolding correlates with the surface area exposed on unfolding).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA value of the molar gas constant, $R = 8.314\,462\,618\ldots$ J mol⁻¹ K⁻¹ (exact).
