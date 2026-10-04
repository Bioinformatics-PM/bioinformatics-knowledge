---
aliases:
  - Ideal Gas Equation
  - Perfect Gas Law
  - PV = nRT
  - Equation of State of an Ideal Gas
  - Loi des gaz parfaits
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
  - "[[Temperature]]"
  - "[[Pressure]]"
  - "[[Mole]]"
  - "[[Momentum]]"
  - "[[Kinetic Energy]]"
related:
  - "[[Osmotic Pressure]]"
  - "[[Internal Energy]]"
  - "[[Equipartition Theorem]]"
  - "[[Chemical Potential]]"
  - "[[Diffusion]]"
  - "[[Boltzmann Distribution]]"
  - "[[Dimensional Analysis]]"
  - "[[Thermodynamic System]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Anatomy and Physiology 2e (OpenStax)]]"
---

# Ideal Gas Law

> [!abstract]
> For a dilute gas, pressure times volume equals the number of molecules times the thermal energy, PV = N k_B T = nRT; the same law, read for solute particles instead of gas molecules, gives the osmotic pressure that cells must balance.

## Definition

An **ideal gas** is a gas of point-like molecules that interact only through elastic collisions; real gases approach it at low density.[^up21][^chemgas] Its pressure $P$, volume $V$, temperature $T$ and amount obey the equation of state

$$PV = nRT = N k_B T,$$

where $n$ is the amount in moles, $N = n N_A$ the number of molecules, $R$ the molar gas constant and $k_B$ the Boltzmann constant.[^up21] The two constants are related by $R = N_A k_B = 8.314\,462\,618\ldots$ J mol⁻¹ K⁻¹, exact since the 2019 SI.[^nist]

## Why it matters

- **$RT$ is everywhere.** The factor $RT$ (2.48 kJ/mol at 25 °C) of $\Delta G^\circ = -RT\ln K$ is the same one that sets the pressure of a gas ([[Gibbs Free Energy]], [[Temperature]]).
- **Osmotic pressure.** Dilute solute particles push on a semipermeable membrane like gas molecules on a wall: $\Pi = cRT$ has the form of the ideal gas law ([[Osmotic Pressure]]). It governs cell volume, turgor and dialysis.[^chemsol]
- **Gas exchange.** In a gas mixture each gas contributes its own partial pressure, and oxygen and CO₂ move between lungs and blood down their partial-pressure differences.[^ap][^chemgas]
- **Unit sanity.** Pa × m³ = J: the law is a dimension check that every conversion between pressures, volumes and energies passes through ([[Dimensional Analysis]]).

## Core (L1)

**Units.** In SI, $P$ in Pa, $V$ in m³, $n$ in mol, $T$ in K, $R$ in J mol⁻¹ K⁻¹; then $PV$ is in joules. With litres and atmospheres, $R = 0.082\,057$ L atm mol⁻¹ K⁻¹ (1 atm = 101,325 Pa exactly[^nist]). Temperature must be absolute ([[Temperature]]).

**Special cases.** Holding two variables fixed recovers the historical gas laws:[^chemgas]

| Fixed | Law | Statement |
|---|---|---|
| $n$, $T$ | Boyle | $P \propto 1/V$ |
| $n$, $P$ | Charles | $V \propto T$ |
| $P$, $T$ | Avogadro | $V \propto n$: equal volumes contain equal numbers of molecules |
| $n$, $V$ | Amontons (gas thermometer) | $P \propto T$ |

**Numbers to know** (computed below): the molar volume is 22.414 L/mol at 0 °C and 1 atm, and 24.79 L/mol at 25 °C and 1 bar. At 25 °C and 1 atm a gas holds $P/k_B T = 2.46 \times 10^{25}$ molecules per m³, whatever the gas.

**Mixtures: Dalton's law.** In a mixture of ideal gases each component behaves as if alone: its **partial pressure** is $P_i = x_i P$, with $x_i = n_i/n$ its mole fraction, and the partial pressures add up to the total pressure.[^chemgas]

**Microscopic derivation.** Put $N$ molecules of mass $m$ in a box of length $L$ along $x$ and wall area $A$ ($V = AL$):

![[ideal-gas-wall-collision.svg]]

1. An elastic bounce reverses $v_x$, so the wall receives momentum $2mv_x$ ([[Momentum]]).
2. The molecule comes back to the same wall after a round trip of $2L$, every $\Delta t = 2L/v_x$.
3. Its average force on the wall is $2mv_x/\Delta t = m v_x^2/L$; for $N$ molecules, $F = N m\langle v_x^2\rangle/L$.
4. With no preferred direction, $\langle v^2\rangle = 3\langle v_x^2\rangle$, so $P = F/A = \frac{1}{3}\frac{N}{V} m\langle v^2\rangle$.
5. Comparing with $PV = N k_B T$:
$$\left\langle \tfrac{1}{2} m v^2 \right\rangle = \tfrac{3}{2} k_B T, \qquad v_{\text{rms}} = \sqrt{\langle v^2\rangle} = \sqrt{\frac{3 k_B T}{m}} = \sqrt{\frac{3RT}{M}}.$$

Temperature measures the mean translational kinetic energy of the molecules ([[Kinetic Energy]]).[^up2] At 37 °C, O₂ molecules move at about 490 m/s on average (root mean square).

**Bio: osmotic pressure.** For dilute solutes, the osmotic pressure across a membrane permeable to water only is $\Pi = cRT$, with $c$ the molar concentration of solute particles (van 't Hoff).[^chemsol] It is the ideal gas law with $n/V$ replaced by $c$: an illustrative 0.30 M difference in particle concentration at 37 °C gives $\Pi = 300 \times 8.314 \times 310.15 = 7.7 \times 10^5$ Pa, about 7.6 atm. That is why a cell placed in pure water swells and can burst ([[Osmotic Pressure]], [[Cell Membrane]]).

**Bio: gas exchange.** The partial pressure of O₂ in alveolar air is about 104 mm Hg; O₂ diffuses from the alveoli into blood that arrives with a lower partial pressure.[^ap] With 760 mm Hg total, Dalton's law gives an O₂ mole fraction of $104/760 = 0.137$, and the ideal gas law gives its concentration in alveolar gas at 37 °C: $P_{\mathrm{O_2}}/RT = 5.38$ mol/m³, i.e. 5.38 mM (code below; see [[Diffusion]] for the transport itself).

## Deeper (L2)

**When the model fails.** The two ideal assumptions, negligible molecular volume and no attractions, break down at high pressure and low temperature, where molecules are close together; the gas then deviates from $PV = nRT$, measured by the compressibility factor $Z = PV/nRT \neq 1$.[^chemgas] At room temperature and 1 atm the deviations of air are small, which is why the law serves for physiology and lab gases. (Equations of state for real gases are beyond this vault's scope.)

**Internal energy of an ideal gas.** With no interactions, the internal energy is purely kinetic: $U = \frac{3}{2}nRT$ for a monatomic gas. It depends on $T$ only, so any isothermal process of an ideal gas has $\Delta U = 0$ ([[Internal Energy]]); molecules that rotate store more energy per kelvin ([[Equipartition Theorem]], [[Heat Capacity]]).

**Isothermal work.** Expanding $n$ mol reversibly at constant $T$ from $V_1$ to $V_2$, the work done on the gas is
$$W = -\int_{V_1}^{V_2} P\,dV = -nRT\int_{V_1}^{V_2}\frac{dV}{V} = -nRT\ln\frac{V_2}{V_1},$$
and since $\Delta U = 0$, the gas absorbs $Q = nRT\ln(V_2/V_1)$. This result gives the entropy of expansion and of mixing ([[Thermodynamic Entropy]]).

**Why solutes behave like a gas.** In a dilute solution, solute particles are far apart and interact mostly with the solvent; their contribution to the free energy has the same logarithmic form as for an ideal gas, which leads to $\Pi = cRT$ ([[Chemical Potential]], [[Osmotic Pressure]]).

## Advanced (L3)

- **Free energy of an ideal gas.** At constant $T$, $dG = V\,dP$ (from $G = H - TS$ and the fundamental relation, [[Gibbs Free Energy]]). With $V = nRT/P$, integration from a standard pressure $P^\circ$ gives
$$G(P) = G^\circ + nRT\ln\frac{P}{P^\circ}.$$
Replacing $P/P^\circ$ by $c/c^\circ$ for an ideal solute gives the chemical potential $\mu = \mu^\circ + RT\ln(c/c^\circ)$, the origin of the $RT\ln Q$ term in every reaction free energy ([[Chemical Potential]], [[Chemical Equilibrium]]).
- **Density in a field.** In a gravitational or centrifugal field an ideal gas, or a dilute suspension, is denser where its potential energy is lower, with a Boltzmann factor $e^{-\Delta E_p/k_B T}$ ([[Boltzmann Distribution]], [[Centrifugation]]).
- **The ideal reference.** Because the ideal gas has no interactions, it is the natural reference state: subtracting the ideal term $RT\ln(c/c^\circ)$ from a chemical potential leaves the "excess" part, which isolates the effect of interactions such as solvation or binding ([[Binding Free Energy]]).

## Mathematical representation

- Equation of state: $PV = nRT = Nk_BT$, $R = N_A k_B$; molar form $P V_m = RT$; number density $N/V = P/k_BT$; molar concentration $n/V = P/RT$.
- Dalton: $P = \sum_i P_i$, $P_i = x_i P$.
- Kinetic theory: $P = \frac{1}{3}\frac{N}{V}m\langle v^2\rangle$; $\langle \frac{1}{2}mv^2\rangle = \frac{3}{2}k_BT$; $v_{\text{rms}} = \sqrt{3RT/M}$ with $M$ in kg/mol.
- Isothermal reversible work on the gas: $W = -nRT\ln(V_2/V_1)$.
- Van 't Hoff osmotic pressure (dilute): $\Pi = cRT$, $c$ in mol/m³ for $\Pi$ in Pa.

## Computational representation

```python
import math

K_B = 1.380649e-23           # J/K (exact, 2019 SI)
N_A = 6.02214076e23          # 1/mol (exact)
R = N_A * K_B                # J/(mol K)
ATM = 101_325.0              # Pa, standard atmosphere (exact by definition)
MMHG = ATM / 760             # Pa per mmHg


def molar_volume(T: float, P: float) -> float:
    """V/n (L/mol) of an ideal gas."""
    return R * T / P * 1e3


def number_density(T: float, P: float) -> float:
    """N/V (molecules per m^3) = P / (k_B T)."""
    return P / (K_B * T)


def rms_speed(T: float, molar_mass_g: float) -> float:
    """sqrt(<v^2>) = sqrt(3 R T / M), in m/s."""
    return math.sqrt(3 * R * T / (molar_mass_g * 1e-3))


print(f"R = {R:.6f} J/(mol K) = {R / ATM * 1e3:.6f} L atm/(mol K)")
print(f"V_m at 0 C, 1 atm:   {molar_volume(273.15, ATM):.3f} L/mol")
print(f"V_m at 25 C, 1 bar:  {molar_volume(298.15, 1e5):.3f} L/mol")
print(f"N/V at 25 C, 1 atm:  {number_density(298.15, ATM):.3e} m^-3")
for gas, M in (("O2", 2 * 15.999), ("N2", 2 * 14.007), ("CO2", 12.011 + 2 * 15.999)):
    print(f"v_rms({gas}) at 37 C: {rms_speed(310.15, M):.0f} m/s")

# Gas exchange: alveolar O2 (partial pressure 104 mmHg) at body temperature
p_o2 = 104 * MMHG
print(f"alveolar O2: {p_o2:.0f} Pa, {p_o2 / (R * 310.15):.2f} mol/m^3 (mM), mole fraction {104 / 760:.3f}")

# Van 't Hoff osmotic pressure for an illustrative 0.30 M difference of solute particles
c = 0.30e3                   # mol/m^3
print(f"osmotic pressure: {c * R * 310.15 / 1e3:.0f} kPa = {c * R * 310.15 / ATM:.1f} atm")
```

```text
R = 8.314463 J/(mol K) = 0.082057 L atm/(mol K)
V_m at 0 C, 1 atm:   22.414 L/mol
V_m at 25 C, 1 bar:  24.790 L/mol
N/V at 25 C, 1 atm:  2.461e+25 m^-3
v_rms(O2) at 37 C: 492 m/s
v_rms(N2) at 37 C: 526 m/s
v_rms(CO2) at 37 C: 419 m/s
alveolar O2: 13866 Pa, 5.38 mol/m^3 (mM), mole fraction 0.137
osmotic pressure: 774 kPa = 7.6 atm
```

Molar masses come from standard atomic weights (C 12.011, N 14.007, O 15.999).[^chemaw] Every function works in SI internally; litres, mm Hg and atmospheres appear only at the edges.

## Worked example

> [!example] Air in a culture flask
> A 250 mL flask is sealed at 25 °C and 1 atm, then warmed to 37 °C in an incubator.
> 1. **Amount.** $n = PV/RT = (101{,}325 \times 2.50 \times 10^{-4})/(8.314 \times 298.15) = 1.022 \times 10^{-2}$ mol, i.e. $6.15 \times 10^{21}$ molecules.
> 2. **Warming at constant volume** (Amontons): $P_2 = P_1 T_2/T_1 = 1 \times 310.15/298.15 = 1.040$ atm. The cap must hold 4 % overpressure.
> 3. **Oxygen available.** With an O₂ mole fraction of about 0.21 in air (assumed here), $n_{\mathrm{O_2}} = 0.21 \times 1.022 \times 10^{-2} = 2.1 \times 10^{-3}$ mol: a closed flask holds a finite oxygen budget, which a dense culture can consume ([[Thermodynamic System]]: closed, not open).

## Common misconceptions

> [!warning] "Use Celsius in PV = nRT"
> $T$ must be in kelvin: at 0 °C the formula would give zero volume. Only temperature *differences* may be in °C.

> [!warning] "Heavier gases exert more pressure"
> At the same $N$, $V$ and $T$, every ideal gas has the same pressure: heavier molecules move more slowly, and $m\langle v^2\rangle = 3k_BT$ is the same for all.

> [!warning] "Osmotic pressure depends on what the solute is"
> In the dilute limit, $\Pi$ counts particles, not their identity: 0.1 M NaCl, which dissociates into two ions, gives about twice the osmotic pressure of 0.1 M glucose.[^chemsol]

## Exercises

> [!question] Exercise 1 (L1)
> How many moles and molecules of gas are in 1.00 L at 25 °C and 1 atm?

> [!success]- Solution
> $n = PV/RT = 101{,}325 \times 10^{-3}/(8.314 \times 298.15) = 0.0409$ mol, i.e. $0.0409 \times 6.022 \times 10^{23} = 2.46 \times 10^{22}$ molecules (consistent with $2.46 \times 10^{25}$ m⁻³).

> [!question] Exercise 2 (L1)
> A syringe holds 50 mL of air at 1.0 atm. You block the tip and push the plunger to 20 mL at constant temperature. What is the new pressure?

> [!success]- Solution
> Boyle: $P_2 = P_1 V_1/V_2 = 1.0 \times 50/20 = 2.5$ atm.

> [!question] Exercise 3 (L2)
> Show that the work done on 1 mol of ideal gas compressed reversibly and isothermally at 37 °C to half its volume is $RT\ln 2$, and evaluate it in kJ/mol and in units of $RT$.

> [!success]- Solution
> $W = -nRT\ln(V_2/V_1) = -RT\ln(1/2) = RT\ln 2 = 2.579 \times 0.693 = 1.79$ kJ/mol, i.e. $0.693\,RT$. The gas releases the same amount as heat, since $\Delta U = 0$. Halving the space available to molecules costs $RT\ln 2$ per mole: the same quantity appears in the entropy of confinement ([[Thermodynamic Entropy]]).

> [!question] Exercise 4 (L2)
> Two compartments are separated by a membrane permeable to water only. One holds 0.15 M NaCl (assume full dissociation), the other 0.15 M glucose. Which way does water move, and what pressure would stop it at 37 °C?

> [!success]- Solution
> Particle concentrations: 0.30 M for NaCl, 0.15 M for glucose; water moves toward the NaCl side. $\Pi = \Delta c\,RT = 150 \times 8.314 \times 310.15 = 3.87 \times 10^5$ Pa, about 3.8 atm ([[Osmotic Pressure]]).

> [!question] Exercise 5 (L3, Python)
> Treat an alveolus as a sphere of radius 100 µm (assumed). Using `MMHG`, `R` and `N_A` from the code, compute the number of O₂ molecules it contains at $P_{\mathrm{O_2}} = 104$ mm Hg and 37 °C. Then compute the O₂ partial pressure that would correspond to 0.21 mole fraction at 760 mm Hg, and the ratio of the two concentrations.

> [!success]- Solution
> ```python
> V = 4 / 3 * math.pi * (100e-6) ** 3                # m^3
> c_alv = 104 * MMHG / (R * 310.15)                  # mol/m^3
> print(f"{V:.3e} m^3, {c_alv * V * N_A:.3e} O2 molecules")
> print(f"{0.21 * 760:.0f} mmHg, ratio {104 / (0.21 * 760):.2f}")
> ```
> Output: `4.189e-12 m^3, 1.356e+13 O2 molecules`, then `160 mmHg, ratio 0.65`. At the same temperature, concentrations are proportional to partial pressures, so alveolar gas carries about two thirds of the O₂ concentration that the assumed 0.21 mole fraction would give at 760 mm Hg.

## Mastery checklist

- [ ] 1 Recognized: I can write $PV = nRT = Nk_BT$ and relate $R$ to $k_B$ and $N_A$.
- [ ] 2 Understood: I can derive pressure from molecular collisions and explain why $\Pi = cRT$ has the form of the ideal gas law.
- [ ] 3 Practiced: I solve gas-law, partial-pressure and osmotic-pressure problems in SI units, with temperature in kelvin.
- [ ] 4 Applied: I convert between partial pressures and concentrations for physiological gases and compute osmotic pressures of real buffers.
- [ ] 5 Explained: I can teach when a gas or a solution behaves ideally and how $RT\ln(P/P^\circ)$ leads to the $RT\ln Q$ of chemical equilibrium.

## References

[^up21]: [[University Physics (OpenStax)]], Volume 2, ch. 2, §2.1 "Molecular Model of an Ideal Gas" (ideal gas law in the forms $pV = nRT$ and $pV = Nk_BT$; ideal gas as the low-density limit).
[^up2]: [[University Physics (OpenStax)]], Volume 2, ch. 2 (pressure from molecular collisions, mean translational kinetic energy $\frac{3}{2}k_BT$, rms speed).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], molar gas constant $R = 8.314\,462\,618\ldots$ J mol⁻¹ K⁻¹ (exact), $R = N_A k$, and the standard atmosphere, 101 325 Pa.
[^chemgas]: [[Chemistry 2e (OpenStax)]], treatment of gases (Boyle's, Charles's and Avogadro's laws, the ideal gas law, Dalton's law of partial pressures, deviations of real gases at high pressure and low temperature).
[^chemsol]: [[Chemistry 2e (OpenStax)]], treatment of colligative properties (osmotic pressure $\Pi = MRT$, electrolytes and the number of dissolved particles).
[^chemaw]: [[Chemistry 2e (OpenStax)]], standard atomic weights (C 12.011, N 14.007, O 15.999).
[^ap]: [[Anatomy and Physiology 2e (OpenStax)]], treatment of gas exchange in the respiratory system (alveolar partial pressure of O₂ about 104 mm Hg; gases move down their partial-pressure gradients).
