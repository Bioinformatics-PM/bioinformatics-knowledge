---
aliases:
  - Osmosis
  - Osmolarity
  - Osmolality
  - Van 't Hoff Law
  - Colligative Property
  - Pression osmotique
tags:
  - type/concept
  - domain/chemistry
  - domain/physics
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Chemical Potential]]"
  - "[[Pressure]]"
  - "[[Ideal Gas Law]]"
  - "[[Aqueous Solution]]"
  - "[[Molar Concentration]]"
related:
  - "[[Cell Membrane]]"
  - "[[Membrane Transport]]"
  - "[[Protein Purification]]"
  - "[[Ligand Binding]]"
  - "[[Water]]"
  - "[[Van 't Hoff Equation]]"
  - "[[Gibbs Free Energy]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[NobelPrize.org]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Osmotic Pressure

> [!abstract]
> Dissolved particles lower the chemical potential of water, so water flows through a membrane toward the more concentrated side; the osmotic pressure Π is the pressure that stops this flow, and for dilute solutions Π = cRT, whatever the particles are.

## Definition

The **osmotic pressure** $\Pi$ of a solution is the pressure that must be applied to it to stop the net flow of pure solvent into it through a semipermeable membrane, one that lets the solvent through but not the solute. For a dilute solution it follows the van 't Hoff law

$$\Pi = cRT,$$

with $c$ the molar concentration of dissolved particles, $R$ the gas constant and $T$ the absolute temperature.[^chem11] Van 't Hoff received the first Nobel Prize in Chemistry (1901) for "the laws of chemical dynamics and osmotic pressure in solutions".[^nobel] The [[Pressure]] and [[Ideal Gas Law]] notes introduce the formula; this note explains where it comes from and what it controls.

## Why it matters

- **Cells live or burst by it.** An animal cell, bounded only by its membrane, swells in a hypotonic medium and shrinks in a hypertonic one; walled plant cells build turgor pressure instead.[^bio] Any buffer, lysis solution or culture medium whose osmolarity differs from the cell's changes its volume ([[Cell Membrane]]).
- **Recipes must balance particles, not formula units.** 150 mM NaCl contributes about 300 mOsm/L, 150 mM glucose only 150 ([[Aqueous Solution]]).
- **Dialysis.** A membrane that retains proteins but passes water and small molecules exchanges the buffer of a sample:[^berg] the chemical-potential balance of this note, applied to the solutes that can cross ([[Protein Purification]]).
- **Molar masses.** Colligative properties give molar masses;[^chem11] for macromolecules only the osmotic pressure is large enough to measure (Worked example).

## Core (L2)

### Why water flows

In an ideal solution the chemical potential of water is $\mu_w = \mu_w^* + RT\ln x_w$, with $\mu_w^*$ that of pure water and $x_w < 1$ its mole fraction ([[Chemical Potential]]). Solute lowers $\mu_w$, so water flows from pure water into the solution, down its chemical potential. Pressure raises the chemical potential of water by $\bar V_w\,\Delta p$ ($\bar V_w$: molar volume of water). The flow stops when the extra pressure on the solution compensates exactly:

$$\bar V_w\,\Pi = -RT\ln x_w \approx RT\,x_s \approx RT\,\frac{n_s}{n_w} \qquad\Rightarrow\qquad \Pi \approx \frac{n_s}{n_w\bar V_w}RT = cRT,$$

using $x_s = 1 - x_w \ll 1$ and $n_w\bar V_w \approx V$ for a dilute solution. $\Pi$ is therefore not a push of solute molecules on the membrane: it is the pressure that brings the chemical potential of water back to that of pure water ([[Pressure#Common misconceptions]]). Gibbs-Duhem gives the same result ([[Chemical Potential#Exercises]], Exercise 5).

![[osmotic-pressure-osmometer-cell-volume.svg]]

### Osmolarity: count the particles

$\Pi$ counts dissolved particles, not formula units: $c = \sum_j i_j c_j$, where the van 't Hoff factor $i_j$ is the number of particles each formula unit releases (2 for NaCl, 1 for glucose). Measured factors of electrolytes are a little smaller than these ideal values because ions partly pair.[^chem11] The particle concentration is the **osmolarity** (osmol per liter of solution); per kilogram of water it is the **osmolality**, practically equal in dilute aqueous solutions. With $R = 8.314\,462\,618$ J mol⁻¹ K⁻¹,[^nist] 150 mM NaCl (0.300 osmol/L, ideal) gives $\Pi = 774$ kPa = 7.6 atm at 37 °C (code).

### One cause, four colligative properties

Lowering the chemical potential of water by about $RT\,x_s$ changes four measurable properties, which depend only on the number of solute particles (colligative):[^chem11]

| Property | Law | 0.300 osmol per kg of water |
|---|---|---|
| Vapor pressure lowering | Raoult: $p_w = x_w\,p_w^*$ | $x_s = 0.300/55.8$: lowered by 0.5 % |
| Boiling-point elevation | $\Delta T_b = K_b\,m$, $K_b = 0.512$ K kg/mol | 0.154 K |
| Freezing-point depression | $\Delta T_f = K_f\,m$, $K_f = 1.86$ K kg/mol | 0.558 K |
| Osmotic pressure (37 °C) | $\Pi = cRT$ | 774 kPa (7.6 atm) |

$m$ is the molality of particles, and the constants are those of water.[^chem11] They are not independent numbers: equating the chemical potential of ice with that of water in the solution gives $K_f = RT_f^2M_w/\Delta H_{\text{fus}}$, and with $\Delta H_{\text{fus}} = 6.01$ kJ/mol[^chem] and $M_w = 18.015$ g/mol ([[Water]]) this predicts 1.860 K kg/mol (code). The table also shows why osmotic pressure is the amplifier: a solution that lowers the freezing point by half a kelvin holds back more than seven atmospheres.

### Bio: cell volume

A cell membrane lets water through much faster than ions ([[Cell Membrane#Selective permeability]]). At equilibrium, the osmolarity inside equals the osmolarity outside. If the cell holds $n$ mol of particles that cannot cross, in an osmotically active volume $V - V_b$ (the rest, $V_b$, is solids), then $n/(V - V_b) = c_{\text{out}}$ and

$$V = V_b + \frac{n}{c_{\text{out}}}, \qquad \frac{V}{V_0} = b + (1-b)\,\frac{c_0}{c_{\text{out}}},$$

a straight line in $1/c_{\text{out}}$ (figure, panel b; $b = V_b/V_0$ and $c_0$ the initial osmolarity). Halving the outside osmolarity swells a cell with $b = 0.4$ (invented) by 60 %. Only solutes that cannot cross count: a permeant solute equilibrates and leaves no lasting pressure difference, which is why biologists describe media by their **tonicity**, their effect on cell volume, rather than by osmolarity alone.[^bio]

### Lab: dialysis

In dialysis, a protein solution is held in a membrane whose pores are too small for the protein, in a large volume of buffer; water and small molecules cross.[^berg] Each permeant solute reaches the same concentration on both sides, so one equilibration with a buffer volume $V_d$ leaves a fraction $V_s/(V_s + V_d)$ of the small solute in a sample of volume $V_s$, and $k$ successive changes leave $(V_s/(V_s+V_d))^k$. A 2 mL sample dialyzed three times against 500 mL keeps $6.3 \times 10^{-8}$ of its salt (code), far less than with one change of 1.5 L (Exercise 6).

## Advanced (L3)

- **Equilibrium dialysis measures binding.** If the protein is confined to one side and a ligand can cross, the *free* ligand concentration is the same on both sides at equilibrium (equal chemical potential). The excess of ligand on the protein side is the bound ligand, so a single pair of measurements gives the bound fraction and $K_d$ ([[Ligand Binding]], Exercise 5).
- **Non-ideal solutions.** For macromolecules, $\Pi$ grows faster than linearly with concentration. Writing $c_m$ for the mass concentration, $\Pi/c_m = RT\,(1/M + B\,c_m + \dots)$: the first term is the van 't Hoff law, $B$ collects the interactions between solute molecules. Extrapolating $\Pi/c_m$ to $c_m = 0$ gives the molar mass $M$; a single measurement at finite concentration underestimates it (Exercise 4).
- **Why animal cells pump.** A cell contains macromolecules and metabolites that cannot leave, and without a wall it would keep taking up water. Animal cells balance this osmotic load with the Na⁺-K⁺ pump, which keeps Na⁺ out and so makes it behave as an impermeant solute outside the cell.[^alberts] Plant cells instead resist the pressure with their wall, which turns it into turgor ([[Membrane Transport]]).[^bio]

## Mathematical representation

- Water in an ideal solution under pressure $p$: $\mu_w = \mu_w^* + RT\ln x_w + \bar V_w(p - p^\circ)$.
- Osmotic equilibrium: $\Pi = -(RT/\bar V_w)\ln x_w \approx RT\sum_j i_jc_j$.
- Freezing point: $\ln x_w = -(\Delta H_{\text{fus}}/R)(1/T - 1/T_f)$, hence $\Delta T_f \approx (RT_f^2M_w/\Delta H_{\text{fus}})\,m = K_f\,m$; boiling point likewise with $\Delta H_{\text{vap}}$ and $T_b$.
- Cell volume with impermeant solutes: $V/V_0 = b + (1-b)\,c_0/c_{\text{out}}$.
- Dialysis with $k$ buffer changes: remaining fraction $\left(V_s/(V_s + V_d)\right)^k$.
- Non-ideal solute of molar mass $M$: $\Pi/c_m = RT\,(1/M + B\,c_m + O(c_m^2))$.

## Computational representation

Units are the trap: $\Pi = cRT$ gives pascals only with $c$ in mol/m³ (1 mM = 1 mol/m³). Constants from CODATA;[^nist] colligative constants of water from Chemistry 2e:[^chem11]

```python
import math

R = 8.314462618       # J/(mol K), CODATA (exact)
ATM = 101_325.0       # Pa, standard atmosphere (exact)
G = 9.80665           # m/s^2, standard acceleration of gravity (exact)
K_F, K_B = 1.86, 0.512    # K kg/mol, freezing-point and boiling-point constants of water


def osmotic_pressure(osmolarity: float, t: float) -> float:
    """Van 't Hoff osmotic pressure (Pa) for an osmolarity in osmol/L (ideal, dilute)."""
    return osmolarity * 1000 * R * t          # osmol/L -> mol/m^3


def relative_volume(c_out: float, c_in0: float = 0.300, b: float = 0.4) -> float:
    """V/V0 of a cell whose osmotically active water follows c_out; b = non-osmotic fraction."""
    return b + (1 - b) * c_in0 / c_out


def remaining_after_dialysis(v_sample: float, v_buffer: float, changes: int) -> float:
    """Fraction of a small solute left in the sample after equilibrating with fresh buffer `changes` times."""
    return (v_sample / (v_sample + v_buffer)) ** changes


# 150 mM NaCl: up to 2 particles per formula unit
osm = 2 * 0.150
pi = osmotic_pressure(osm, 310.15)
print(f"150 mM NaCl: {osm:.3f} osmol/L, Pi = {pi / 1000:.0f} kPa = {pi / ATM:.2f} atm")
print(f"freezing point depression {K_F * osm:.3f} K, boiling point elevation {K_B * osm:.3f} K")

# the same lowering of water's chemical potential predicts K_f from the enthalpy of fusion
kf = R * 273.15**2 * 0.018015 / 6010
print(f"K_f from R Tf^2 M / dH_fus = {kf:.3f} K kg/mol (tabulated 1.86)")

for c_out in (0.600, 0.300, 0.150):
    print(f"outside {c_out * 1000:.0f} mOsm: V/V0 = {relative_volume(c_out):.2f}")

print(f"after 3 changes of 500 mL for a 2 mL sample: {remaining_after_dialysis(2, 500, 3):.2e} of the salt left")
```

```text
150 mM NaCl: 0.300 osmol/L, Pi = 774 kPa = 7.64 atm
freezing point depression 0.558 K, boiling point elevation 0.154 K
K_f from R Tf^2 M / dH_fus = 1.860 K kg/mol (tabulated 1.86)
outside 600 mOsm: V/V0 = 0.70
outside 300 mOsm: V/V0 = 1.00
outside 150 mOsm: V/V0 = 1.60
after 3 changes of 500 mL for a 2 mL sample: 6.32e-08 of the salt left
```

The colligative formulas use molality and $\Pi = cRT$ uses molarity; for dilute aqueous solutions the code treats them as equal, which is accurate to about the density of water (about 1.0 g/mL[^chem]).

## Worked example

> [!example] Why osmotic pressure, not freezing point, weighs a protein
> A solution holds 10.0 g/L of a protein of molar mass 66,000 g/mol (invented values), at 25 °C.
> 1. **Molar concentration**: $c = 10.0/66\,000 = 1.515 \times 10^{-4}$ M $= 0.1515$ mol/m³.
> 2. **Osmotic pressure**: $\Pi = cRT = 0.1515 \times 8.314 \times 298.15 = 375.6$ Pa. In an osmometer this is a column of water $h = \Pi/(\rho g) = 375.6/(1000 \times 9.80665) = 3.83$ cm ([[Pressure]]): easy to read.
> 3. **Freezing-point depression**: $\Delta T_f = K_f\,m = 1.86 \times 1.515 \times 10^{-4} = 2.8 \times 10^{-4}$ K: a third of a millikelvin, out of reach of an ordinary thermometer.
> 4. **Read it**: both effects count the same few particles, but $\Pi$ converts them into a centimeter-scale signal. Inverting, $M = c_m RT/\Pi$ recovers the molar mass, provided the solution is dilute enough to be ideal (Exercise 4).

## Common misconceptions

> [!warning] "Water moves from the concentrated solution to the dilute one"
> Water moves toward the side with **more** solute particles: from high to low chemical potential of water. Solutes, when they can cross, move the other way.

> [!warning] "Every dissolved solute shrinks or swells cells"
> Only solutes that cannot cross the membrane change cell volume at equilibrium; a permeant solute equalizes on both sides. Osmolarity and tonicity are different quantities.[^bio]

> [!warning] "150 mM NaCl is a 150 mOsm solution"
> Each NaCl gives two particles: about 300 mOsm/L ideally, a little less in reality because ions pair.[^chem11]

> [!warning] "Dialysis removes the small molecules"
> It dilutes them to equilibrium, once per buffer change. The final concentration depends on the volume ratio and on the number of changes, and splitting the same buffer volume into several changes works far better (Exercise 6).

## Exercises

> [!question] Exercise 1 (L2)
> Compute the ideal osmolarity of 150 mM NaCl and its osmotic pressure at 37 °C in atmospheres. Would a measurement give more or less?

> [!success]- Solution
> $2 \times 0.150 = 0.300$ osmol/L, $\Pi = 300 \times 8.314 \times 310.15 = 7.74 \times 10^5$ Pa $= 7.64$ atm. A measurement gives somewhat less: ions partly pair, so the effective number of particles per NaCl is below 2.[^chem11]

> [!question] Exercise 2 (L2)
> For the same solution, compute the freezing-point depression and the boiling-point elevation, and compare them with the osmotic pressure.

> [!success]- Solution
> $\Delta T_f = 1.86 \times 0.300 = 0.558$ K and $\Delta T_b = 0.512 \times 0.300 = 0.154$ K, against 7.6 atm of osmotic pressure. The same particle count produces tiny temperature shifts and a large pressure.

> [!question] Exercise 3 (L2)
> A cell with an internal osmolarity of 300 mOsm and a non-osmotic fraction $b = 0.4$ (invented values) is moved to a 200 mOsm medium. Predict its relative volume, assuming the solutes inside cannot leave.

> [!success]- Solution
> $V/V_0 = 0.4 + 0.6 \times 300/200 = 1.30$: the cell swells by 30 %. Water enters until the internal osmolarity drops to 200 mOsm, which only the osmotically active 60 % of the volume can achieve.

> [!question] Exercise 4 (L3, Python)
> Invented osmotic pressures of a protein solution at 25 °C: 76.9, 157.5, 241.6, 329.3 and 420.7 Pa at 2, 4, 6, 8 and 10 g/L. Estimate the molar mass by extrapolating $\Pi/c_m$ to zero concentration, and compare with the single-point estimate at 10 g/L.

> [!success]- Solution
> ```python
> conc = [2.0, 4.0, 6.0, 8.0, 10.0]                 # g/L
> pi_obs = [76.9, 157.5, 241.6, 329.3, 420.7]       # Pa at 25 C, invented
> y = [p / cg for p, cg in zip(pi_obs, conc)]       # Pa per (g/L)
> mx, my = sum(conc) / 5, sum(y) / 5
> slope = sum((a - mx) * (b - my) for a, b in zip(conc, y)) / sum((a - mx) ** 2 for a in conc)
> icept = my - slope * mx
> print(f"Pi/c = {icept:.2f} + {slope:.3f} c  ->  M = {1000 * R * 298.15 / icept:,.0f} g/mol")
> print(f"single point at 10 g/L: M = {1000 * R * 298.15 * 10 / 420.7:,.0f} g/mol")
> ```
> ```text
> Pi/c = 37.56 + 0.451 c  ->  M = 66,006 g/mol
> single point at 10 g/L: M = 58,925 g/mol
> ```
> $\Pi/c_m$ rises with concentration (interactions, $B > 0$); the intercept is the ideal value $RT/M$ (the factor 1000 converts g/L to g/m³). The single point treats the non-ideal excess as extra particles and underestimates $M$ by 11 %.

> [!question] Exercise 5 (L3)
> In an equilibrium dialysis experiment (invented values), a chamber holds a protein at 10.0 µM total; at equilibrium the ligand is 6.0 µM in the protein-free chamber and 15.0 µM in total in the protein chamber. Assuming one site per protein, compute $K_d$.

> [!success]- Solution
> Free ligand is equal on both sides: 6.0 µM. Bound ligand: $15.0 - 6.0 = 9.0$ µM, so free protein is $10.0 - 9.0 = 1.0$ µM. $K_d = [\mathrm{P}][\mathrm{L}]/[\mathrm{PL}] = 1.0 \times 6.0/9.0 = 0.67$ µM ([[Chemical Equilibrium#Deeper (L2)]]).

> [!question] Exercise 6 (L3, Python)
> A 2 mL sample is dialyzed with 1.5 L of buffer in total. Compare one change of 1500 mL with three changes of 500 mL using `remaining_after_dialysis`, and explain the difference.

> [!success]- Solution
> ```python
> print(f"one change of 1500 mL: {remaining_after_dialysis(2, 1500, 1):.2e}; three of 500 mL: {remaining_after_dialysis(2, 500, 3):.2e}")
> ```
> Output: `one change of 1500 mL: 1.33e-03; three of 500 mL: 6.32e-08`. Each equilibration multiplies the remaining fraction by $V_s/(V_s + V_d)$; three small factors multiply to a far smaller number than one large dilution. The cost is time, since each step must reach equilibrium.

## Mastery checklist

- [ ] 1 Recognized: I can define osmotic pressure and write $\Pi = cRT$ with $c$ the osmolarity.
- [ ] 2 Understood: I can derive $\Pi$ from the chemical potential of water and explain why all colligative properties count particles.
- [ ] 3 Practiced: I can compute osmolarities, osmotic pressures, freezing-point shifts, cell volumes and dialysis schedules in Python with correct units.
- [ ] 4 Applied: I checked the osmolarity of a real buffer or culture medium recipe and predicted its effect on cell volume.
- [ ] 5 Explained: I can teach tonicity versus osmolarity, equilibrium dialysis, non-ideal extrapolation for molar masses, and why animal cells must pump ions.

## References

[^chem11]: [[Chemistry 2e (OpenStax)]], ch. 11 "Solutions and Colloids", treatment of colligative properties (Raoult's law; boiling-point elevation and freezing-point depression, with $K_b = 0.512$ and $K_f = 1.86$ K kg/mol for water; osmosis and osmotic pressure $\Pi = MRT$; molar masses from colligative properties; van 't Hoff factors of electrolytes and ion pairing) (section not verified).
[^chem]: [[Chemistry 2e (OpenStax)]], enthalpy of fusion of water (6.01 kJ/mol) and density of water (about 1.0 g/mL).
[^nobel]: [[NobelPrize.org]], "The Nobel Prize in Chemistry 1901" (J. H. van 't Hoff, sole laureate; the prize motivation cites the discovery of "the laws of chemical dynamics and osmotic pressure in solutions").
[^bio]: [[Biology 2e (OpenStax)]], Unit 2 "The Cell", treatment of osmosis and tonicity (osmolarity; animal cells in hypotonic and hypertonic solutions; turgor of walled cells) (chapter not verified).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein purification (dialysis through a semipermeable membrane retains proteins and lets small molecules pass).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of membrane transport (osmotic balance of animal cells and the role of the Na⁺-K⁺ pump).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]]: molar gas constant (exact), standard atmosphere 101 325 Pa and standard acceleration of gravity 9.80665 m/s² (exact, conventional values).
