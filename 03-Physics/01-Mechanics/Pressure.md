---
aliases:
  - Hydrostatic Pressure
  - Gauge Pressure
  - Pression
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Dimensional Analysis]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Momentum]]"
related:
  - "[[Work (Physics)]]"
  - "[[Ideal Gas Law]]"
  - "[[Osmotic Pressure]]"
  - "[[Blood]]"
  - "[[Cell Membrane]]"
  - "[[Temperature]]"
  - "[[Viscosity]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[Anatomy and Physiology 2e (OpenStax)]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Pressure

> [!abstract]
> Pressure is force spread over an area; in a fluid it pushes equally in all directions and grows with depth, and it is how a physician reads your arteries and how water pushes on a cell.

## Definition

**Pressure** is the magnitude of the force acting perpendicular to a surface divided by the area of that surface, $p = F/A$. It is a scalar; its SI unit is the **pascal**, 1 Pa = 1 N/m². In a fluid at rest, pressure acts perpendicular to every surface and increases with depth $h$ as $p = p_0 + \rho g h$, where $\rho$ is the density of the fluid and $p_0$ the pressure at the surface.[^up14]

## Why it matters

- **Clinical data are pressures.** Arterial blood pressure is recorded as systolic over diastolic pressure in mmHg, 120/80 being a normal adult value.[^ap] Datasets of physiological phenotypes carry these numbers, and their units and reference level matter for any analysis ([[Phenotype]]).
- **Water moves under osmotic pressure.** The pressure needed to stop water from flowing across a membrane into a more concentrated solution is the [[Osmotic Pressure]], several atmospheres for concentration differences of a few hundred millimolar; it decides whether a cell swells, shrinks or, with a wall, becomes turgid.[^chem][^bio]
- **Pressure is energy per volume.** 1 Pa = 1 N/m² = 1 J/m³, so pressure converts molecular energies into macroscopic ones: one $k_B T$ per cubic nanometer is 42 atm (computed below). Work against a pressure is $p\,\Delta V$ ([[Work (Physics)]]).
- **Gas pressure is molecular collisions.** Its kinetic derivation (L2) leads to the [[Ideal Gas Law]] and to the van 't Hoff law of osmotic pressure.

## Core (L1)

**Units.** 1 standard atmosphere = 101 325 Pa (exact, conventional) = 760 mmHg, so 1 mmHg = 101 325 / 760 = 133.322 Pa.[^up14][^nist] Physiology uses mmHg and kPa; chemistry uses atm and bar; physics uses Pa.

**Pressure is not a force.** It has no direction of its own: the same pressure pushes on a surface with a force $pA$ perpendicular to it, whatever the surface's orientation. A sharp needle concentrates a small force on a tiny area into a large pressure.

**Hydrostatic pressure, derived.** Take a horizontal slab of fluid at rest, area $A$, thickness $dh$, at depth $h$. Its weight is $\rho g A\,dh$. Vertical balance ([[Newton's Laws of Motion]]): the push from below equals the push from above plus the weight,

$$p(h + dh)\,A = p(h)\,A + \rho g A\,dh \quad\Rightarrow\quad \frac{dp}{dh} = \rho g \quad\Rightarrow\quad p(h) = p_0 + \rho g h$$

for a fluid of constant density. Pressure depends only on depth, not on the shape of the container.[^up14] Ten meters of water add about one atmosphere.

![[hydrostatic-pressure-column.svg]]

**Gauge versus absolute.** Gauges and clinical instruments report the **gauge pressure** $p - p_{atm}$, the excess over atmospheric pressure; the absolute pressure adds about 760 mmHg.[^up14] A blood pressure of 120/80 mmHg means 120 and 80 mmHg above atmospheric, 16.0 and 10.7 kPa.

**Bio: posture.** Blood is a fluid column, so in a standing person the pressure in a vessel depends on its height relative to the heart (figure): with blood approximated as water, 1.2 m below the heart adds 88 mmHg, 0.4 m above removes 29 mmHg (worked example).

## Deeper (L2)

**Kinetic origin of gas pressure.** A molecule of mass $m$ hitting a wall perpendicular to $x$ with velocity component $v_x$ bounces back and transfers momentum $2 m v_x$ ([[Momentum]]). In a box of length $L$ it returns every $2L/v_x$, so it pushes on the wall with average force $m v_x^2 / L$. Summing over $N$ molecules and dividing by the wall area $A = V/L$:

$$p = \frac{N}{V}\,m\langle v_x^2\rangle.$$

Temperature fixes $\tfrac12 m\langle v_x^2 \rangle = \tfrac12 k_B T$,[^upv2] which gives $p = \frac{N}{V}k_B T$, the [[Ideal Gas Law]] ([[Temperature]]).

**Pressure as an energy density.** Since 1 Pa = 1 J/m³, a pressure measures energy per volume. At 310 K, $k_B T$ per nm³ is $4.28 \times 10^{-21}$ J / $10^{-27}$ m³ = 4.28 MPa, about 42 atm. Molecular forces acting over molecular areas easily reach tens of atmospheres (Exercise 3).

**Osmotic and turgor pressure.** For a dilute solution separated from pure water by a membrane permeable only to water, the **osmotic pressure**, the pressure that must be applied to stop the net flow of water into the solution, is $\Pi = cRT$ (van 't Hoff), with $c$ the molar concentration of dissolved particles.[^chem] A difference of 300 mM of particles at 310 K corresponds to 7.6 atm, and even 1 mM gives 19 mmHg, comparable to blood pressure differences (code, Exercise 5). An animal cell, bounded only by its [[Cell Membrane]], swells in a hypotonic medium and shrinks in a hypertonic one; a plant cell in a hypotonic medium takes up water until its rigid wall pushes back, and the internal pressure built against the wall is the **turgor pressure** that keeps plant tissues firm.[^bio] The full treatment is in [[Osmotic Pressure]] and [[Chemical Potential]].

## Mathematical representation

- $p = F_\perp / A$ (Pa = N m⁻² = J m⁻³), $F_\perp$ the normal force (N), $A$ the area (m²).
- Hydrostatics: $dp/dh = \rho g$, $p(h) = p_0 + \rho g h$; $\rho$ in kg m⁻³, $g = 9.80665$ m s⁻² (standard gravity[^nist]), $h$ depth in m.
- Gauge pressure $p_g = p - p_{atm}$.
- Kinetic theory: $p = \frac{N}{V} m\langle v_x^2 \rangle = \frac{1}{3}\frac{N}{V} m\langle v^2 \rangle = \frac{N}{V} k_B T$.
- Osmotic pressure (ideal, dilute): $\Pi = cRT$, $c$ in mol m⁻³ (1 mM = 1 mol m⁻³), $R = 8.314462618$ J mol⁻¹ K⁻¹ exact.[^nist]

## Computational representation

Unit conversions are where pressure calculations go wrong; keep constants in one place and convert explicitly.

```python
G = 9.80665                 # m/s^2, standard acceleration of gravity (exact)
ATM = 101_325.0             # Pa, standard atmosphere (exact)
MMHG = ATM / 760            # Pa per mmHg (1 atm = 760 mmHg)
R = 8.314462618             # J/(mol K), molar gas constant (exact)
KB = 1.380649e-23           # J/K, Boltzmann constant (exact)


def hydrostatic(rho: float, depth: float) -> float:
    """Pressure increase (Pa) at a depth (m) below the surface of a fluid of density rho (kg/m^3)."""
    return rho * G * depth


def osmotic(c_mM: float, temp: float = 310.0) -> float:
    """Van 't Hoff osmotic pressure (Pa) of an ideal dilute solution; 1 mM = 1 mol/m^3 of particles."""
    return c_mM * R * temp


print(f"1 mmHg = {MMHG:.3f} Pa;  120/80 mmHg = {120 * MMHG / 1000:.1f}/{80 * MMHG / 1000:.1f} kPa above atmospheric")
dp = hydrostatic(1000.0, 1.2)         # blood approximated by water, heart to feet 1.2 m (illustrative)
print(f"1.2 m column of water: {dp / 1000:.1f} kPa = {dp / MMHG:.0f} mmHg")
print(f"10 m of water: {hydrostatic(1000.0, 10.0) / ATM:.2f} atm")
pi = osmotic(300.0)                    # 300 mM of solute particles (illustrative)
print(f"300 mM at 310 K: {pi / 1000:.0f} kPa = {pi / ATM:.1f} atm = {pi / MMHG:.0f} mmHg")
print(f"kBT per nm^3 at 310 K: {KB * 310 / 1e-27 / 1e6:.2f} MPa = {KB * 310 / 1e-27 / ATM:.0f} atm")
```

```text
1 mmHg = 133.322 Pa;  120/80 mmHg = 16.0/10.7 kPa above atmospheric
1.2 m column of water: 11.8 kPa = 88 mmHg
10 m of water: 0.97 atm
300 mM at 310 K: 773 kPa = 7.6 atm = 5800 mmHg
kBT per nm^3 at 310 K: 4.28 MPa = 42 atm
```

## Worked example

> [!example] Blood pressure from head to feet (heights illustrative)
> A standing adult has 120/80 mmHg at heart level. Estimate arterial pressure at the feet (1.2 m below the heart) and in the head (0.4 m above), counting only hydrostatics and approximating blood by water ($\rho = 1000$ kg/m³).
>
> 1. **Feet.** $\Delta p = \rho g h = 1000 \times 9.81 \times 1.2 = 11.8$ kPa $= 11\,800 / 133.3 = 88$ mmHg, so about 208/168 mmHg.
> 2. **Head.** $\Delta p = -1000 \times 9.81 \times 0.4 = -3.9$ kPa $= -29$ mmHg, so about 91/51 mmHg.
> 3. **Check the units.** kg m⁻³ × m s⁻² × m = kg m⁻¹ s⁻² = N m⁻² = Pa.
> 4. **Limits.** Real values also depend on flow and vessel resistance ([[Viscosity]]); the point is the size of the hydrostatic term: a blood pressure value is only meaningful with the height at which it was measured.

## Common misconceptions

> [!warning] "Pressure is a force"
> It is force per area, a scalar. The force it exerts on a surface is $pA$, perpendicular to that surface, whatever its orientation.

> [!warning] "A bigger or wider container gives a higher pressure at the bottom"
> Hydrostatic pressure depends only on depth and density, $p_0 + \rho g h$, not on the amount of fluid or the shape of the vessel.

> [!warning] "120 mmHg is the pressure inside the artery"
> It is a gauge pressure, 120 mmHg above atmospheric; the absolute pressure is about 880 mmHg.

> [!warning] "Osmotic pressure is pushed by the solute molecules on the membrane"
> It is defined operationally: the pressure that must be applied to the solution to stop net water entry.[^chem] $\Pi = cRT$ looks like the ideal gas law, but the mechanism is the flow of water, treated with [[Chemical Potential]].

## Exercises

> [!question] Exercise 1 (L1)
> A 70 kg person stands on two shoes with a total contact area of 300 cm², then shifts all the weight onto one heel of 1.0 cm². Compute both pressures in kPa and atm.

> [!success]- Solution
> Weight $70 \times 9.81 = 686$ N. Shoes: $686 / 0.030 = 22.9$ kPa. Heel: $686 / 1.0 \times 10^{-4} = 6.86$ MPa $\approx 68$ atm. Same force, 300 times smaller area, 300 times higher pressure.

> [!question] Exercise 2 (L1)
> Mean arterial pressure at heart level is 100 mmHg (illustrative). What is it in a hand raised 0.40 m above the heart?

> [!success]- Solution
> $\Delta p = \rho g h = 1000 \times 9.81 \times 0.40 = 3.9$ kPa $= 29.4$ mmHg, so $100 - 29.4 = 70.6$ mmHg. Measuring with the arm raised underestimates blood pressure.

> [!question] Exercise 3 (L2)
> A protein pushes on a membrane with a force of 10 pN spread over a 10 nm × 10 nm patch. Express the pressure in MPa and atm.

> [!success]- Solution
> $p = 10 \times 10^{-12} / (10 \times 10^{-9})^2 = 10^{-11} / 10^{-16} = 10^5$ Pa $= 0.1$ MPa $\approx 1$ atm. Piconewton forces on nanometer patches are atmospheric pressures.

> [!question] Exercise 4 (L2)
> Using $p = \frac{N}{V}k_B T$, compute the number density of air molecules at 101 325 Pa and 298.15 K, per m³ and per nm³, and the mean spacing between molecules.

> [!success]- Solution
> $N/V = 101\,325 / (1.380649 \times 10^{-23} \times 298.15) = 2.46 \times 10^{25}$ m⁻³ $= 0.0246$ nm⁻³. Mean spacing $(N/V)^{-1/3} = 3.4$ nm: one molecule per cube of 3.4 nm side.

> [!question] Exercise 5 (L2, Python)
> With `osmotic` and `MMHG` from the code, compute the osmotic pressure of a 1 mM concentration difference at 310 K in Pa and mmHg. Why must animal cells keep their internal osmolarity matched to their surroundings?

> [!success]- Solution
> ```python
> print(round(osmotic(1.0)), round(osmotic(1.0) / MMHG, 1))
> # 2577 19.3
> ```
>
> A mere 1 mM imbalance corresponds to 19 mmHg, and a 300 mM one to 7.6 atm. A membrane without a wall cannot resist such pressures, so an animal cell would swell or shrink until concentrations match; walled cells instead hold turgor pressure.[^bio]

## Mastery checklist

- [ ] 1 Recognized: I can define $p = F/A$, its unit, and convert between Pa, atm and mmHg.
- [ ] 2 Understood: I can derive $p = p_0 + \rho g h$, distinguish gauge from absolute pressure, and explain pressure as energy per volume.
- [ ] 3 Practiced: I can compute hydrostatic differences, molecular-scale pressures and osmotic pressures, with units checked in code.
- [ ] 4 Applied: I read blood pressure and other physiological pressures in datasets with correct units and reference level.
- [ ] 5 Explained: I can teach the kinetic origin of gas pressure and why osmotic pressure forces cells either to balance osmolarity or to build walls.

## References

[^up14]: [[University Physics (OpenStax)]], Volume 1, ch. 14 "Fluid Mechanics", §14.1 "Fluids, Density, and Pressure" (definition of pressure, variation with depth, 1 atm = 760 mmHg) and the treatment of gauge and absolute pressure in the same chapter.
[^upv2]: [[University Physics (OpenStax)]], Volume 2, kinetic theory of gases (molecular origin of pressure, temperature and mean kinetic energy) (chapter not verified).
[^ap]: [[Anatomy and Physiology 2e (OpenStax)]], section "Blood Flow, Blood Pressure, and Resistance" (systolic over diastolic pressure in mmHg, 120/80 as a normal adult value, measured at the brachial artery) (verified as §20.2 in the first edition).
[^chem]: [[Chemistry 2e (OpenStax)]], ch. 11 "Solutions and Colloids", colligative properties (osmosis, osmotic pressure $\Pi = MRT$) (section not verified).
[^bio]: [[Biology 2e (OpenStax)]], Unit 2 "The Cell", treatment of osmosis and tonicity (animal cells in hypotonic and hypertonic solutions, turgor of walled plant cells) (chapter not verified).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]]: standard atmosphere 101 325 Pa and standard acceleration of gravity 9.80665 m/s² (exact, conventional values), Boltzmann constant and molar gas constant (exact).
