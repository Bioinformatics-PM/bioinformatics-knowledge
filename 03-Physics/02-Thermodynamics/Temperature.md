---
aliases:
  - Absolute Temperature
  - Thermodynamic Temperature
  - Kelvin
  - Thermal Energy Scale
  - kBT
  - Zeroth Law of Thermodynamics
  - Température
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
  - "[[Thermodynamic System]]"
  - "[[Kinetic Energy]]"
  - "[[Mole]]"
  - "[[Dimensional Analysis]]"
related:
  - "[[Heat]]"
  - "[[Laws of Thermodynamics]]"
  - "[[Ideal Gas Law]]"
  - "[[Thermodynamic Entropy]]"
  - "[[Boltzmann Distribution]]"
  - "[[Equipartition Theorem]]"
  - "[[Gibbs Free Energy]]"
  - "[[Molecular Dynamics Simulation]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
---

# Temperature

> [!abstract]
> Temperature is the quantity that two bodies share once heat has stopped flowing between them; multiplied by the Boltzmann constant it becomes an energy, $k_B T \approx 4.1$ pN nm per molecule at room temperature, the yardstick against which every molecular energy in biology is measured.

## Definition

Two systems in thermal contact exchange heat until they reach **thermal equilibrium**. **Temperature** is the property that is then equal in both. The **zeroth law of thermodynamics** makes it well defined: if A and B are each in thermal equilibrium with C, then A and B are in thermal equilibrium with each other, so C can serve as a thermometer.[^up11]

The SI unit is the **kelvin** (K). Its scale starts at absolute zero, and Celsius temperatures are shifted by a fixed offset, $T/\mathrm{K} = t/{}^\circ\mathrm{C} + 273.15$; a temperature *difference* is the same in K and °C.[^up1] Since the 2019 revision of the SI, the kelvin is defined by fixing the **Boltzmann constant** at exactly $k_B = 1.380\,649 \times 10^{-23}$ J K⁻¹.[^nist]

## Why it matters

- **The unit of molecular energy.** Biophysics expresses energies in units of $k_B T$ ($\approx 4.1$ pN nm), because what matters is how an energy compares with thermal agitation.[^pboc] A force-spectroscopy trace in pN, a binding energy in kJ/mol and a motor's work per step meet on this one scale.
- **Every equilibrium constant contains $T$.** $\Delta G^\circ = -RT \ln K$ ([[Gibbs Free Energy]]), and populations follow $e^{-\Delta E/k_B T}$ ([[Boltzmann Distribution]]); $T$ must be in kelvin in both.
- **Melting temperatures.** DNA duplexes, primers and proteins are characterized by the temperature at which half of them have melted ([[Polymerase Chain Reaction]], [[Phase Transition]]); the temperature dependence of stability is the subject of [[Heat Capacity]] and the [[Van 't Hoff Equation]].
- **Simulations.** A molecular dynamics run is set at a temperature, and its "instantaneous temperature" is computed from atomic velocities (Exercise 5, [[Molecular Dynamics Simulation|molecular dynamics]]).

## Core (L1)

**The zeroth law as a sorting rule.** "Is in thermal equilibrium with" is reflexive, symmetric and, by the zeroth law, transitive: it splits all systems into classes, and a temperature is a label for a class.[^up11] A thermometer is any system with a property that changes monotonically with that label (the length of a mercury column, the pressure of a gas at fixed volume, the resistance of a wire).

**Absolute zero and the kelvin scale.** The gas thermometer shows why a natural zero exists: at fixed volume and amount, the pressure of a dilute gas is proportional to $T$ ([[Ideal Gas Law]]), and extrapolates to zero at $0$ K $= -273.15$ °C.[^up1] Ratios of temperatures are only meaningful in kelvin.

**What temperature measures.** For a dilute gas, kinetic theory gives the mean translational kinetic energy of a molecule,

$$\left\langle \tfrac{1}{2} m v^2 \right\rangle = \tfrac{3}{2} k_B T,$$

so temperature measures the average energy of random molecular motion ([[Kinetic Energy]]; derivation in [[Ideal Gas Law#Core (L1)]]).[^up2] Each molecule's energy fluctuates; temperature describes the distribution, not a single molecule.

**$k_B T$, the thermal energy scale.** Multiplying by $k_B$ turns a temperature into an energy per molecule; multiplying by the Avogadro constant $N_A$ gives an energy per mole, $RT$, with $R = N_A k_B$ ([[Mole]]).[^nist] Computed from the exact SI constants (code below):

| $t$ (°C) | $T$ (K) | $k_B T$ (J) | $k_B T$ (pN nm) | $RT$ (kJ/mol) | $RT$ (kcal/mol) |
|---:|---:|---:|---:|---:|---:|
| 20 | 293.15 | 4.047 × 10⁻²¹ | 4.047 | 2.437 | 0.583 |
| 25 | 298.15 | 4.116 × 10⁻²¹ | 4.116 | 2.479 | 0.592 |
| 26.85 | 300.00 | 4.142 × 10⁻²¹ | 4.142 | 2.494 | 0.596 |
| 37 | 310.15 | 4.282 × 10⁻²¹ | 4.282 | 2.579 | 0.616 |

The kcal column uses 1 cal = 4.184 J.[^chem5] The piconewton-nanometre is natural at the molecular scale: $1$ pN nm $= 10^{-12}$ N $\times\, 10^{-9}$ m $= 10^{-21}$ J.

**Bio: the yardstick.** Comparing molecular energies with $k_B T$ sorts them into those that thermal motion constantly breaks and those it essentially never breaks:

![[kbt-energy-ladder.svg]]

A hydrogen bond in water, about 4.2 kJ/mol, is only 1.7 $k_B T$, while a covalent bond, about 377 kJ/mol, is about 150 $k_B T$.[^alberts] The standard free energy of ATP hydrolysis, −30.5 kJ/mol,[^berg] is about 12 $k_B T$: enough to drive one molecular step, not enough to break a covalent bond. This is why noncovalent structures (folded proteins, duplexes, membranes) are held together by many weak interactions acting together ([[Intermolecular Force]]).

## Deeper (L2)

**The thermodynamic definition.** The zeroth law says temperature exists; the second law says what it is. At constant volume no work is done, so a reversible heat input $\delta Q_{\text{rev}} = dU$ changes the entropy by $dS = \delta Q_{\text{rev}}/T$ ([[Thermodynamic Entropy]]). Hence

$$\frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_{V, N}.$$

Temperature measures how much entropy a system gains per joule received: a cold system gains a lot, a hot one little. This definition does not refer to any substance, and in [[Statistical Physics]] it is computed from the number of microstates ([[Boltzmann Entropy]]).

**Why heat flows from hot to cold.** Let two bodies at $T_1 > T_2$ exchange a small amount of heat, $dU_2 = -dU_1 = \delta Q$ flowing into body 2. The total entropy changes by

$$dS = \frac{dU_1}{T_1} + \frac{dU_2}{T_2} = \delta Q \left( \frac{1}{T_2} - \frac{1}{T_1} \right),$$

which is positive only if $\delta Q > 0$, that is, heat flows into the colder body. Flow stops when $T_1 = T_2$: thermal equilibrium, recovering the zeroth law ([[Laws of Thermodynamics]]).

**Energy gaps in units of $k_B T$.** At equilibrium, the population ratio of two states separated by $\Delta E$ is $e^{-\Delta E/k_B T}$ ([[Boltzmann Distribution]]). The exponential makes $k_B T$ the natural unit:

| $\Delta E$ | 1 $k_B T$ | 3 $k_B T$ | 5 $k_B T$ | 10 $k_B T$ |
|---|---:|---:|---:|---:|
| upper/lower population | 0.37 | 0.050 | 0.0067 | 4.5 × 10⁻⁵ |

A few $k_B T$ separate "both states populated" from "only the lower one". Raising $T$ from 25 to 37 °C changes $k_B T$ by only 4 %, but because it sits in an exponent, rates and equilibria that involve large energies are very temperature-sensitive ([[Activation Energy]], [[Van 't Hoff Equation]]).

## Advanced (L3)

- **Temperature in simulations.** With three translational degrees of freedom per molecule, $T = \frac{2\langle E_k \rangle}{3 k_B}$ estimates the temperature from velocities ([[Equipartition Theorem]] generalizes it to all quadratic degrees of freedom). For a handful of molecules the estimate fluctuates strongly; thermostats in [[Molecular Dynamics Simulation|molecular dynamics]] control its average, not its instantaneous value (Exercise 5).
- **Temperature as a sampling parameter.** In $p_i \propto e^{-E_i/k_B T}$, a high $T$ flattens the distribution and a low $T$ concentrates it on the lowest energies. The same exponential form, with a "temperature" parameter, is used outside physics to sharpen or flatten a probability distribution over scores ([[Boltzmann Distribution]]).
- **Melting temperature is a parameter, not a state.** $T_m$ is the temperature at which a two-state transition is half complete, where $\Delta G = 0$; it summarizes a free-energy curve rather than describing a thermal equilibrium between bodies ([[Phase Transition]], [[Calorimetry]]).

## Mathematical representation

- Zeroth law: the relation $A \sim B$ ("in thermal equilibrium") is an equivalence relation; $T$ maps each equivalence class to a positive real number, increasing with the direction of spontaneous heat flow.
- Scales: $T = t + 273.15$ (K, °C); $\Delta T$ is identical in both units.
- Thermal energies: $\varepsilon_{\text{th}} = k_B T$ (J per molecule), $RT = N_A k_B T$ (J per mole). An energy $E$ (per molecule) or $E_m$ (per mole) in thermal units is $E/k_B T = E_m/RT$, a dimensionless number.
- Thermodynamic temperature: $1/T = (\partial S/\partial U)_{V,N}$.
- Kinetic temperature of $N$ molecules of mass $m$: $T = \dfrac{1}{3 N k_B} \sum_{i=1}^{N} m \lVert \mathbf{v}_i \rVert^2$.

## Computational representation

Keep constants in one place, exact values from the 2019 SI, and convert at the boundaries of the program:

```python
# Exact constants of the 2019 SI (CODATA, NIST)
K_B = 1.380649e-23          # J/K, Boltzmann constant
N_A = 6.02214076e23         # 1/mol, Avogadro constant
R = N_A * K_B               # J/(mol K), molar gas constant
CAL = 4.184                 # J per thermochemical calorie


def kelvin(t_celsius: float) -> float:
    return t_celsius + 273.15


def thermal_energy(T: float) -> dict[str, float]:
    """k_B T per molecule and R T per mole, in the units used in biophysics."""
    e = K_B * T
    return {"J": e, "pN nm": e / 1e-21, "kJ/mol": R * T / 1e3, "kcal/mol": R * T / 1e3 / CAL}


def in_kbt(energy_kj_per_mol: float, T: float) -> float:
    """Express a molar energy in units of k_B T (equivalently R T)."""
    return energy_kj_per_mol * 1e3 / (R * T)


print(f"R = N_A k_B = {R:.9f} J/(mol K)")
for t_c in (25.0, 37.0):
    e = thermal_energy(kelvin(t_c))
    print(f"{t_c:4.1f} C: {e['pN nm']:.3f} pN nm = {e['kJ/mol']:.3f} kJ/mol = {e['kcal/mol']:.3f} kcal/mol")
for name, value in (("H bond in water", 4.2), ("ATP hydrolysis, standard", 30.5), ("covalent bond", 377)):
    print(f"{name:25}: {value:6.1f} kJ/mol = {in_kbt(value, 298.15):6.1f} k_BT at 25 C")
```

```text
R = N_A k_B = 8.314462618 J/(mol K)
25.0 C: 4.116 pN nm = 2.479 kJ/mol = 0.592 kcal/mol
37.0 C: 4.282 pN nm = 2.579 kJ/mol = 0.616 kcal/mol
H bond in water          :    4.2 kJ/mol =    1.7 k_BT at 25 C
ATP hydrolysis, standard :   30.5 kJ/mol =   12.3 k_BT at 25 C
covalent bond            :  377.0 kJ/mol =  152.1 k_BT at 25 C
```

Store temperatures in kelvin internally; Celsius belongs to input and display only.

## Worked example

> [!example] What can one ATP do?
> Standard free energy of ATP hydrolysis: $\Delta G^{\circ\prime} = -30.5$ kJ/mol.[^berg] Body temperature: 37 °C.
> 1. **Per molecule.** $30.5 \times 10^3 / 6.022 \times 10^{23} = 5.06 \times 10^{-20}$ J $= 50.6$ pN nm.
> 2. **In thermal units.** $k_B T = 4.28$ pN nm at 310.15 K, so $50.6/4.28 = 11.8\ k_B T$.
> 3. **As a force.** If a motor converted all of it into work over a step of $d = 8$ nm (assumed), the largest force it could sustain is $W/d = 50.6/8 = 6.3$ pN ([[Work (Physics)]]).
> 4. **Reading.** About 12 $k_B T$ is large compared with thermal kicks ($e^{-11.8} \approx 8 \times 10^{-6}$: thermal motion alone almost never supplies it), yet small compared with a covalent bond. The free energy actually available in a cell differs from the standard value because concentrations are not 1 M ([[Gibbs Free Energy]]).

## Common misconceptions

> [!warning] "Temperature is the amount of heat a body contains"
> Bodies contain [[Internal Energy|internal energy]], not heat; heat is energy in transit ([[Heat]]). Temperature measures the mean energy per degree of freedom: a bathtub of lukewarm water has more internal energy than a red-hot needle.

> [!warning] "20 °C is twice as hot as 10 °C"
> Ratios require the absolute scale: $293.15/283.15 = 1.035$, so $k_B T$ differs by 3.5 %. Plugging Celsius into $e^{-\Delta E/k_B T}$ or $-RT\ln K$ is a classic bug.

> [!warning] "$k_B T$ and $RT$ are different energies"
> They are the same thermal energy, per molecule and per mole: $RT = N_A k_B T$. 2.48 kJ/mol and 4.1 pN nm describe one scale at 25 °C.

> [!warning] "A single molecule has a temperature"
> Temperature characterizes an equilibrium distribution. One molecule's kinetic energy fluctuates widely; only an average over many molecules (or over time) gives $T$ (Exercise 5).

## Exercises

> [!question] Exercise 1 (L1)
> Convert 37 °C to kelvin and give $k_B T$ in J, pN nm, kJ/mol and kcal/mol.

> [!success]- Solution
> $T = 310.15$ K. $k_B T = 1.380649 \times 10^{-23} \times 310.15 = 4.282 \times 10^{-21}$ J $= 4.282$ pN nm. Per mole: $RT = 8.314 \times 310.15 = 2579$ J/mol $= 2.579$ kJ/mol $= 0.616$ kcal/mol.

> [!question] Exercise 2 (L1)
> A thermometer placed in tube A, then in tube B (never in contact with A), shows the same reading. Can heat flow between A and B if you put them in contact? Which law justifies your answer?

> [!success]- Solution
> No net heat flows: A and B are each in equilibrium with the thermometer, so by the zeroth law they are in equilibrium with each other. Without this law a thermometer reading would not let you compare two systems.

> [!question] Exercise 3 (L2)
> Two conformations of a loop differ in energy by 2.5 kJ/mol. Compute the population ratio (upper/lower) at 25 °C and at 37 °C.

> [!success]- Solution
> $e^{-\Delta E/RT}$: at 298.15 K, $2500/2479 = 1.009$ and $e^{-1.009} = 0.365$; at 310.15 K, $2500/2579 = 0.969$ and $e^{-0.969} = 0.379$. A 1 $k_B T$ gap leaves both states well populated; warming barely changes the ratio because the gap is small.

> [!question] Exercise 4 (L2)
> Using $dS = \delta Q/T$ for each body, show that two bodies at different temperatures cannot reach equilibrium by heat flowing from the colder to the hotter one.

> [!success]- Solution
> See Deeper (L2): with heat $\delta Q$ entering body 2, $dS_{\text{total}} = \delta Q(1/T_2 - 1/T_1)$. If $T_2 > T_1$ (heat into the hotter body), the bracket is negative and $dS_{\text{total}} < 0$, forbidden by the second law for the isolated pair. Heat flows only toward lower temperature, and stops when temperatures are equal.

> [!question] Exercise 5 (L3, Python)
> Draw random velocities for $N$ = 10, 100 and 10,000 O₂ molecules at 310.15 K (each Cartesian component Gaussian with variance $k_B T/m$, seed 1) and estimate the temperature from $T = 2\langle E_k\rangle/3k_B$. Comment.

> [!success]- Solution
> ```python
> import math
> import random
>
> K_B, N_A = 1.380649e-23, 6.02214076e23
> random.seed(1)
> m = 2 * 15.999e-3 / N_A                     # kg per O2 molecule (O: 15.999 g/mol)
> sigma = math.sqrt(K_B * 310.15 / m)         # m/s per Cartesian component
>
>
> def kinetic_temperature(velocities, mass):
>     """T = 2 <KE> / (3 k_B), with 3 translational degrees of freedom per molecule."""
>     mean_ke = sum(0.5 * mass * (vx * vx + vy * vy + vz * vz) for vx, vy, vz in velocities) / len(velocities)
>     return 2 * mean_ke / (3 * K_B)
>
>
> for n in (10, 100, 10_000):
>     v = [(random.gauss(0, sigma), random.gauss(0, sigma), random.gauss(0, sigma)) for _ in range(n)]
>     print(f"N = {n:6}: T = {kinetic_temperature(v, m):6.1f} K")
> ```
> Output: `N =     10: T =  245.7 K`, `N =    100: T =  291.0 K`, `N =  10000: T =  309.2 K`. The relative fluctuation shrinks roughly as $1/\sqrt{N}$: temperature is a property of many particles, which is why a small simulated system shows a noisy instantaneous temperature.

## Mastery checklist

- [ ] 1 Recognized: I can state the zeroth law and convert between °C and K.
- [ ] 2 Understood: I can explain what temperature measures (mean molecular energy, entropy gained per joule) and why heat flows from hot to cold.
- [ ] 3 Practiced: I compute $k_B T$ in J, pN nm, kJ/mol and kcal/mol, and express any molecular energy in units of $k_B T$.
- [ ] 4 Applied: I read binding, force-spectroscopy or simulation data in units of $k_B T$ and check that every exponential uses kelvin.
- [ ] 5 Explained: I can teach the hierarchy of molecular energies relative to $k_B T$ and the difference between a temperature and a melting temperature.

## References

[^up11]: [[University Physics (OpenStax)]], Volume 2, ch. 1, §1.1 "Temperature and Thermal Equilibrium" (thermal equilibrium, zeroth law).
[^up1]: [[University Physics (OpenStax)]], Volume 2, ch. 1 (temperature scales, absolute zero, Celsius-kelvin conversion, constant-volume gas thermometer).
[^up2]: [[University Physics (OpenStax)]], Volume 2, ch. 2 (kinetic theory of gases: mean translational kinetic energy $\frac{3}{2}k_B T$).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], Boltzmann constant $k = 1.380\,649 \times 10^{-23}$ J K⁻¹ and Avogadro constant $6.022\,140\,76 \times 10^{23}$ mol⁻¹ (exact since the 2019 SI), $R = N_A k$.
[^chem5]: [[Chemistry 2e (OpenStax)]], ch. 5 "Thermochemistry" (the calorie, 1 cal = 4.184 J).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. ($k_BT \approx 4.1$ pN nm as the reference energy scale of the book; chapter not verified).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), table of covalent and noncovalent bond strengths (hydrogen bond 4.2 kJ/mol in water, covalent bond 377 kJ/mol).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), $\Delta G^{\circ\prime} = -30.5$ kJ/mol for ATP hydrolysis.
