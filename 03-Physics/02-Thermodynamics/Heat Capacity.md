---
aliases:
  - Specific Heat
  - Specific Heat Capacity
  - Molar Heat Capacity
  - Cp
  - Cv
  - Heat Capacity Change
  - Capacité thermique
tags:
  - type/concept
  - domain/physics
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Heat]]"
  - "[[Temperature]]"
  - "[[Mole]]"
related:
  - "[[Enthalpy]]"
  - "[[Internal Energy]]"
  - "[[Calorimetry]]"
  - "[[Protein Folding]]"
  - "[[Hydrophobic Effect]]"
  - "[[Phase Transition]]"
  - "[[Equipartition Theorem]]"
  - "[[Water]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[University Physics (OpenStax)]]"
  - "[[Myers 1995 - Denaturant m Values and Heat Capacity Changes]]"
---

# Heat Capacity

> [!abstract]
> The heat capacity of a sample is the heat it must absorb to warm by one kelvin; for proteins it jumps when they unfold, and that jump bends the stability curve so that a protein is most stable at one temperature and unfolds both on heating and on cooling.

## Definition

The **heat capacity** $C$ of a body is the heat needed to raise its temperature by one kelvin (J K⁻¹), so that a temperature change $\Delta T$ requires $Q = C\,\Delta T$. Per unit mass it is the **specific heat** $c$ (J g⁻¹ K⁻¹), with $Q = m c \Delta T$; per mole it is the **molar heat capacity** $C_m$ (J mol⁻¹ K⁻¹), with $Q = n C_m \Delta T$.[^chem5][^up1] For liquid water, $c = 4.184$ J g⁻¹ °C⁻¹.[^chem5]

## Why it matters

- **Thermal mass in the lab.** Heating, cooling and thermocycling times scale with the heat capacity of the sample and the block ([[Polymerase Chain Reaction]]).
- **A structural signal in calorimetry.** The heat capacity change on unfolding, $\Delta C_p$, correlates with the protein surface exposed to solvent; it is measured by differential scanning calorimetry ([[Calorimetry]]).[^myers]
- **Temperature dependence of stability.** A nonzero $\Delta C_p$ makes $\Delta H$ and $\Delta S$ of unfolding depend on temperature ([[Enthalpy]]), which is why stability data must be reported with their temperature.
- **The hydrophobic signature.** Exposure of protein surface to water on unfolding is what raises the heat capacity,[^myers] linking $\Delta C_p$ to the [[Hydrophobic Effect]].

## Core (L1)

**Three ways to normalize.** A sample's heat capacity $C$ is extensive; $c = C/m$ and $C_m = C/n$ are intensive properties of the material. Water: $c = 4.184$ J g⁻¹ K⁻¹ and, with $M = 18.015$ g/mol,[^chemaw] $C_m = 75.4$ J mol⁻¹ K⁻¹. Because only temperature *differences* enter, J g⁻¹ °C⁻¹ and J g⁻¹ K⁻¹ are the same unit. Warming a 50 µL PCR reaction (about 50 mg of water) from 55 to 95 °C takes $Q = 0.050 \times 4.184 \times 40 = 8.4$ J (Exercise 1). The same formula, read backwards, turns a measured heat into a temperature change: this is the principle of a calorimeter.[^chem5]

**Constant volume or constant pressure.** Heat depends on the path ([[Heat]]), so heat capacity does too:

- at constant volume, all the heat raises the internal energy: $C_V = (\partial U/\partial T)_V$;
- at constant pressure, part of the heat pays for expansion work: $C_P = (\partial H/\partial T)_P$ ([[Enthalpy]]).

For an ideal gas $C_{P,m} = C_{V,m} + R$, and a monatomic ideal gas has $C_{V,m} = \frac{3}{2}R = 12.5$ J mol⁻¹ K⁻¹, because its internal energy is only translational kinetic energy ([[Internal Energy]], [[Equipartition Theorem]]).[^up3] Liquids and solids barely expand, so the two heat capacities differ little; biochemistry uses $C_p$.

**Bio: proteins change heat capacity when they unfold.** An unfolded protein has a larger heat capacity than the folded one: $\Delta C_p = C_{p,U} - C_{p,N} > 0$. Across proteins, $\Delta C_p$ correlates with the surface area newly exposed to solvent on unfolding.[^myers] The next section shows what this does to stability.

## Deeper (L2)

**From $\Delta C_p$ to a stability curve.** Take a two-state protein (folded N, unfolded U) with melting temperature $T_m$, where $\Delta G_u(T_m) = 0$, unfolding enthalpy $\Delta H_m$ at $T_m$, and constant $\Delta C_p$. Integrating $d\Delta H = \Delta C_p\, dT$ and $d\Delta S = \Delta C_p\, dT/T$ from $T_m$, with $\Delta S_m = \Delta H_m/T_m$ (because $\Delta G_u = 0$ at $T_m$):

$$\Delta H_u(T) = \Delta H_m + \Delta C_p (T - T_m), \qquad \Delta S_u(T) = \frac{\Delta H_m}{T_m} + \Delta C_p \ln\frac{T}{T_m},$$

$$\Delta G_u(T) = \Delta H_m\left(1 - \frac{T}{T_m}\right) + \Delta C_p\left[T - T_m - T\ln\frac{T}{T_m}\right].$$

![[protein-stability-curve-heat-capacity.svg]]

Consequences, for the invented protein of the figure ($T_m = 333.15$ K, $\Delta H_m = 300$ kJ/mol, $\Delta C_p = 8$ kJ mol⁻¹ K⁻¹; code below):

- **Curvature.** $d^2\Delta G_u/dT^2 = -\Delta C_p/T < 0$: the curve bends down. With $\Delta C_p = 0$ it would be a straight line, and stability would keep increasing on cooling.
- **Maximum stability** where $\Delta S_u = 0$: $T_s = T_m e^{-\Delta H_m/(T_m \Delta C_p)} = 297.7$ K, with $\Delta G_u = 16.3$ kJ/mol. At 25 °C the curve is 15 kJ/mol below the straight-line extrapolation.
- **Cold denaturation.** The curve crosses zero a second time, here at 263.6 K: the model predicts unfolding on cooling as well as on heating. For this protein that is below 0 °C, in supercooled water.
- **Marginal stability.** Even at its best, $\Delta G_u$ is a few tens of kJ/mol, the difference of two large terms ($\Delta H$ and $T\Delta S$, each hundreds of kJ/mol near $T_m$) ([[Gibbs Free Energy]], [[Protein Folding]]).

## Advanced (L3)

- **What a scanning calorimeter sees.** Differential scanning calorimetry records $C_p(T)$ of a protein solution against buffer. Because $C_p = (\partial H/\partial T)_P$, the area of the excess peak around $T_m$ is the unfolding enthalpy, and the step between the pre- and post-transition baselines is $\Delta C_p$ ([[Calorimetry]], [[Phase Transition]]). Fitting the two-state model to such curves is a standard data-analysis task.
- **Structure-based estimates.** Since $\Delta C_p$ and the denaturant m value both track the surface exposed on unfolding,[^myers] they can be estimated from a 3D structure (accessible surface area of the folded state versus an unfolded model), and a measured value far from the estimate suggests that unfolding is not two-state.

## Mathematical representation

- Definitions: $C = \delta Q/dT$ along a specified path; $C_V = (\partial U/\partial T)_V$, $C_P = (\partial H/\partial T)_P$; $c = C/m$, $C_m = C/n$.
- Heat over a range: $Q = \int_{T_1}^{T_2} C(T)\, dT$, which reduces to $C\,\Delta T$ for constant $C$.
- Entropy from heat capacity: $\Delta S = \int_{T_1}^{T_2} \frac{C_P}{T}\, dT = C_P \ln(T_2/T_1)$ for constant $C_P$ ([[Thermodynamic Entropy]]).
- Kirchhoff: $\Delta H(T_2) = \Delta H(T_1) + \int_{T_1}^{T_2} \Delta C_P\, dT$; stability curve as above.

## Computational representation

```python
import math


def delta_g_unfold(T: float, Tm: float, dHm: float, dCp: float) -> float:
    """Unfolding free energy (kJ/mol) at T (K) for a two-state protein with constant dCp (kJ/(mol K)).
    dHm: unfolding enthalpy at the melting temperature Tm, where dG = 0."""
    return dHm * (1 - T / Tm) + dCp * (T - Tm - T * math.log(T / Tm))


def max_stability_temperature(Tm: float, dHm: float, dCp: float) -> float:
    """Temperature where dS_unfold = 0, i.e. where dG_unfold is largest."""
    return Tm * math.exp(-dHm / (Tm * dCp))


def cold_denaturation_temperature(Tm, dHm, dCp, lo=150.0):
    """Second root of dG_unfold(T) = 0, below the maximum, by bisection."""
    hi = max_stability_temperature(Tm, dHm, dCp)
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if delta_g_unfold(mid, Tm, dHm, dCp) < 0 else (lo, mid)
    return hi


Tm, dHm, dCp = 333.15, 300.0, 8.0         # invented two-state protein: 60 C, kJ/mol, kJ/(mol K)
print(f"T_s = {max_stability_temperature(Tm, dHm, dCp):.1f} K, "
      f"cold denaturation at {cold_denaturation_temperature(Tm, dHm, dCp):.1f} K")
for T in (270, 298.15, 310.15, 333.15, 340):
    print(f"T = {T:6.2f} K: dG_unfold = {delta_g_unfold(T, Tm, dHm, dCp):6.2f} kJ/mol, "
          f"same without dCp = {delta_g_unfold(T, Tm, dHm, 0.0):6.2f}")
```

```text
T_s = 297.7 K, cold denaturation at 263.6 K
T = 270.00 K: dG_unfold =   5.64 kJ/mol, same without dCp =  56.87
T = 298.15 K: dG_unfold =  16.27 kJ/mol, same without dCp =  31.52
T = 310.15 K: dG_unfold =  14.21 kJ/mol, same without dCp =  20.71
T = 333.15 K: dG_unfold =   0.00 kJ/mol, same without dCp =   0.00
T = 340.00 K: dG_unfold =  -6.73 kJ/mol, same without dCp =  -6.17
```

Ignoring $\Delta C_p$ is harmless near $T_m$ but doubles the predicted stability at 25 °C and gets it wrong by a factor of 10 at 270 K: extrapolating melting data far from $T_m$ requires $\Delta C_p$.

## Worked example

> [!example] Water versus the cell's other components
> 1. **Molar heat capacity of water.** $C_m = c\,M = 4.184 \times 18.015 = 75.4$ J mol⁻¹ K⁻¹.
> 2. **Compare with a monatomic ideal gas.** $\frac{3}{2}R = 12.5$ J mol⁻¹ K⁻¹: liquid water stores about six times more energy per mole and per kelvin: a molecule of a liquid has more ways to store energy than translation alone ([[Equipartition Theorem]], [[Water]]).
> 3. **Consequence.** Warming 1 L of water (1000 g) by 1 K takes 4.18 kJ. A cell, mostly water, changes temperature slowly for a given heat release.

## Common misconceptions

> [!warning] "Heat capacity and specific heat are the same thing"
> $C$ (J/K) belongs to an object and doubles with its size; $c$ (J g⁻¹ K⁻¹) and $C_m$ (J mol⁻¹ K⁻¹) belong to the material. Mixing them gives errors by factors of the mass or the amount.

> [!warning] "$\Delta H$ and $\Delta S$ of unfolding are constants"
> They are constant only if $\Delta C_p = 0$. For proteins $\Delta C_p > 0$,[^myers] so both change with temperature, and a $\Delta H$ quoted without its temperature is incomplete.

> [!warning] "Cooling always stabilizes a protein"
> With $\Delta C_p > 0$ the stability curve has a maximum; below $T_s$ cooling destabilizes, and the model predicts cold denaturation.

## Exercises

> [!question] Exercise 1 (L1)
> How much heat does a 50 µL PCR reaction (treat it as 50 mg of water) absorb when heated from the annealing temperature, 55 °C, to the denaturation temperature, 95 °C?

> [!success]- Solution
> $Q = m c \Delta T = 0.050 \text{ g} \times 4.184 \text{ J g}^{-1}\text{K}^{-1} \times 40 \text{ K} = 8.37$ J. The sample itself needs only a few joules per cycle.

> [!question] Exercise 2 (L2)
> Derive $\Delta S_u(T)$ and $\Delta G_u(T)$ for constant $\Delta C_p$, then show that $\Delta G_u$ is maximal where $\Delta S_u = 0$.

> [!success]- Solution
> $d\Delta S = \Delta C_p\, dT/T$ integrates to $\Delta S_u(T) = \Delta S_m + \Delta C_p\ln(T/T_m)$ with $\Delta S_m = \Delta H_m/T_m$. Then $\Delta G_u = \Delta H_u - T\Delta S_u$ gives the formula in Deeper (L2). Its derivative is $d\Delta G_u/dT = -\Delta S_u$ (differentiate, or use $dG = -S\,dT$ at constant $P$), which vanishes where $\Delta S_u = 0$; the second derivative $-\Delta C_p/T < 0$ makes it a maximum.

> [!question] Exercise 3 (L3, Python)
> With the functions above, compute $T_s$, $\Delta G_u(T_s)$, the cold-denaturation temperature and $\Delta G_u$ at 37 °C for $\Delta C_p$ = 4, 8 and 16 kJ mol⁻¹ K⁻¹ (same $T_m$ and $\Delta H_m$). What does a larger $\Delta C_p$ do?

> [!success]- Solution
> ```python
> for d in (4.0, 8.0, 16.0):
>     Ts = max_stability_temperature(Tm, dHm, d)
>     print(d, round(Ts, 1), round(delta_g_unfold(Ts, Tm, dHm, d), 1),
>           round(cold_denaturation_temperature(Tm, dHm, d), 1), round(delta_g_unfold(310.15, Tm, dHm, d), 1))
> ```
> Output: `4.0 266.0 31.4 204.1 17.5`, `8.0 297.7 16.3 263.6 14.2`, `16.0 314.9 8.3 297.0 7.7`. A larger $\Delta C_p$ curves the stability curve more: the maximum moves up toward $T_m$ and drops, and cold denaturation moves up into the measurable range (297 K for the largest value). At fixed $T_m$ and $\Delta H_m$, a protein with a larger $\Delta C_p$ is less stable at body temperature.

## Mastery checklist

- [ ] 1 Recognized: I can define heat capacity, specific heat and molar heat capacity with their units.
- [ ] 2 Understood: I can explain why $C_P$ differs from $C_V$ and why $\Delta C_p > 0$ bends a protein stability curve.
- [ ] 3 Practiced: I compute heat from temperature changes and the stability curve, $T_s$ and cold denaturation from $T_m$, $\Delta H_m$ and $\Delta C_p$.
- [ ] 4 Applied: I extract $\Delta H$ and $\Delta C_p$ from a calorimetry or melting dataset and extrapolate stability to 37 °C correctly.
- [ ] 5 Explained: I can teach the structural meaning of $\Delta C_p$ and why proteins are only marginally stable.

## References

[^chem5]: [[Chemistry 2e (OpenStax)]], ch. 5 "Thermochemistry" (heat capacity, specific heat, $q = mc\Delta T$, specific heat of water 4.184 J g⁻¹ °C⁻¹, calorimetry).
[^chemaw]: [[Chemistry 2e (OpenStax)]], standard atomic weights (H 1.008, O 15.999).
[^up1]: [[University Physics (OpenStax)]], Volume 2, ch. 1 (heat capacity, specific heat and molar heat capacity).
[^up3]: [[University Physics (OpenStax)]], Volume 2, ch. 3 "The First Law of Thermodynamics" (heat capacities of an ideal gas at constant volume and constant pressure, $C_p = C_V + R$, monatomic $C_V = \frac{3}{2}R$).
[^myers]: [[Myers 1995 - Denaturant m Values and Heat Capacity Changes]], *Protein Science* 4(10):2138-2148 (heat capacity change of unfolding correlated with the surface area exposed on unfolding).
