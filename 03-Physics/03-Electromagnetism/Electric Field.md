---
aliases:
  - E-field
  - Electrostatic Field
  - Field Lines
  - Champ électrique
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Coulomb's Law]]"
  - "[[Vector]]"
  - "[[Newton's Laws of Motion]]"
related:
  - "[[Electric Potential]]"
  - "[[Capacitance]]"
  - "[[Lorentz Force]]"
  - "[[Magnetic Field]]"
  - "[[Gauss's Law]]"
  - "[[Gel Electrophoresis]]"
  - "[[Electrophoretic Mobility]]"
  - "[[Mass Spectrometry]]"
  - "[[Membrane Potential]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Lee 2012 - Agarose Gel Electrophoresis for the Separation of DNA Fragments]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
---

# Electric Field

> [!abstract]
> The electric field is the force per unit charge that a set of charges creates at every point of space: it points away from positive charges and toward negative ones, it is uniform between two parallel plates, and it is what pulls DNA through a gel and launches ions in a mass spectrometer.

## Definition

The **electric field** $\vec E$ at a point is the electric force on a small positive test charge $q_0$ placed there, divided by that charge: $\vec E = \vec F / q_0$. Its unit is N/C, equivalent to V/m. A point charge $q$ creates the field $\vec E = k\,q\,\hat r / r^2$, with $\hat r$ the unit vector pointing away from the charge and $k = 1/4\pi\varepsilon_0$; the field of several charges is the vector sum of their fields.[^up5] Any charge $q$ placed in a field feels $\vec F = q\vec E$.

## Why it matters

- **Gel and capillary electrophoresis** apply a field to move negatively charged DNA toward the anode; the applied voltage is one of the factors that set band positions.[^lee] Field strength times mobility gives the speed of a band ([[Gel Electrophoresis]], [[Electrophoretic Mobility]]).
- **Mass spectrometry** accelerates ions with electric fields; in a time-of-flight instrument the flight time after acceleration reveals $m/z$ ([[Mass Spectrometry]]).[^berg]
- **Membranes** sustain a field of about $10^7$ V/m across a few nanometres of lipid ([[Membrane Potential]], Deeper (L2)).
- **Structural biology**: the field and potential around proteins and DNA are what continuum electrostatics computes to explain how charged partners approach ([[Electric Potential]], [[Poisson-Boltzmann Equation]]).

## Core (L1)

**Field of a point charge.** $E = k|q|/r^2$, radially outward for $q > 0$ and inward for $q < 0$.[^up5] The field exists whether or not a test charge is there: it describes what *would* happen to a charge placed at each point.

**Superposition.** $\vec E = \sum_i k\,q_i\,\hat r_i / r_i^2$, a [[Vector]] sum.[^up5] A **dipole** (charges $+q$ and $-q$ a distance $a$ apart) has a field that falls as $1/r^3$ far away, faster than a single charge, because the two contributions nearly cancel (checked numerically below).

**Field lines** are a drawing convention:[^up5]
1. at each point the field is tangent to the line, pointing along the arrows;
2. lines start on positive charges and end on negative charges (or at infinity);
3. the number of lines per unit area is proportional to the field strength;
4. lines never cross, since the field has one direction at each point.

![[electric-field-lines-dipole-plates.svg]]

**Uniform field between two plates.** A large plane with surface charge density $\sigma$ (C/m²) creates a field $\sigma/2\varepsilon_0$ on each side, independent of distance.[^upplates] For two parallel plates with $+\sigma$ and $-\sigma$, superposition gives
$$E = \frac{\sigma}{2\varepsilon_0} + \frac{\sigma}{2\varepsilon_0} = \frac{\sigma}{\varepsilon_0} \text{ between the plates}, \qquad E = 0 \text{ outside},$$
pointing from the positive to the negative plate (edge effects ignored). If the plates are held at a voltage $\Delta V$ a distance $d$ apart, $E = \Delta V / d$ ([[Electric Potential]], [[Capacitance]]).

**Motion in a uniform field.** A charge of mass $m$ feels a constant force $q\vec E$, hence a constant acceleration $\vec a = q\vec E/m$ ([[Newton's Laws of Motion]]): uniformly accelerated motion, as for a falling body.

**Bio 1: the field across a gel.** A gel box is close to a parallel-plate geometry: two electrodes at opposite ends, the buffer and gel between them. With an illustrative 100 V across 20 cm, $E = 100/0.20 = 500$ V/m (5 V/cm). The field points from the anode (+) to the cathode (−); DNA, negative, is pulled the opposite way, toward the anode.[^lee] On a 1,000 bp linear duplex (bare charge $-1998e$, [[Electric Charge]]) the force is $1998 \times 1.6 \times 10^{-19} \times 500 = 0.16$ pN, about $1.6 \times 10^7$ times its weight. In the gel this force is balanced almost at once by friction, so DNA drifts at constant speed ([[Electrophoretic Mobility]]).

**Bio 2: launching ions in a mass spectrometer.** A singly charged peptide of 1,000 Da ($m = 1\ \text{kg mol}^{-1}/N_A = 1.66 \times 10^{-24}$ kg) in an assumed field of $10^6$ V/m accelerates at $a = eE/m \approx 9.6 \times 10^{10}$ m/s², reaching $4.4 \times 10^4$ m/s after 1 cm. Because $a = (z/m)\,eE$, ions with the same $m/z$ follow the same motion: the field sorts by mass-to-charge ratio, not by mass (Exercise 4). In vacuum nothing slows them; the energy view is in [[Electric Potential]], magnetic steering in [[Lorentz Force]].

## Deeper (L2)

**The field across a membrane.** A lipid bilayer is about 5 nm thick, and resting potentials range from about −20 to −200 mV depending on the cell.[^alberts] Taking 70 mV across 5 nm, $E \approx 0.07/(5 \times 10^{-9}) = 1.4 \times 10^7$ V/m: nearly 30,000 times the gel field above, from a voltage a thousand times smaller. This is the field that voltage-gated channels sense ([[Ion Channel]]).[^alberts]

**Field from potential.** The field is minus the [[Gradient]] of the potential, $\vec E = -\nabla V$; in one dimension $E_x = -dV/dx$. A large field comes from a modest voltage over a short distance, which is the whole story of the membrane ([[Electric Potential]]).

**Line charge: the field around DNA.** A long straight line of charge density $\lambda$ creates a radial field $E = \lambda / (2\pi\varepsilon_0 \varepsilon_r r)$, falling as $1/r$ rather than $1/r^2$.[^upplates] With DNA's $\lambda \approx -9.4 \times 10^{-10}$ C/m ([[Electric Charge]]) and $\varepsilon_r = 80$, this gives $E \approx 10^8$ V/m at 2 nm from the axis, before counterions screen it ([[Debye Length]]). Such results follow most simply from [[Gauss's Law]] (L2).

## Mathematical representation

- **Definition**: $\vec E(\vec r) = \vec F / q_0$ (V/m), for a test charge $q_0$ small enough not to disturb the sources.
- **Discrete sources** $q_i$ at $\vec r_i$: $\vec E(\vec r) = \dfrac{1}{4\pi\varepsilon_0}\displaystyle\sum_i q_i\,\frac{\vec r - \vec r_i}{|\vec r - \vec r_i|^3}$.
- **Dipole on its axis**, far away ($r \gg a$): $E \approx \dfrac{2kqa}{r^3}$ (from expanding $\dfrac{kq}{(r - a/2)^2} - \dfrac{kq}{(r + a/2)^2}$).
- **Parallel plates**: $E = \sigma/\varepsilon_0 = \Delta V/d$, uniform.
- **Force and motion**: $\vec F = q\vec E$, $\vec a = q\vec E/m$; from rest in a uniform field, $x = \tfrac12 a t^2$ and $v = \sqrt{2ax}$.

## Computational representation

A field is a function from points to vectors; on a computer it is evaluated by superposition at each point of a grid. The figure above was drawn the same way, by stepping along the computed field direction from each charge. Constants: CODATA 2022 and the standard acceleration of gravity.[^nist]

```python
import math

E_CHARGE = 1.602176634e-19       # C, exact
EPS0 = 8.8541878188e-12          # F m^-1, CODATA 2022
N_A = 6.02214076e23              # mol^-1, exact
G_N = 9.80665                    # m s^-2, standard acceleration of gravity
K_C = 1 / (4 * math.pi * EPS0)


def field(charges, point):
    """Superposition: field vector (V/m) at point from [(q in C, (x, y) in m), ...]."""
    ex = ey = 0.0
    for q, (x, y) in charges:
        dx, dy = point[0] - x, point[1] - y
        r = math.hypot(dx, dy)
        ex += K_C * q * dx / r**3
        ey += K_C * q * dy / r**3
    return ex, ey


a = 0.1e-9                       # toy dipole: +e at -a/2, -e at +a/2 (invented)
dipole = [(E_CHARGE, (-a / 2, 0.0)), (-E_CHARGE, (a / 2, 0.0))]
for r in (1e-9, 2e-9, 4e-9):
    ex, ey = field(dipole, (r, 0.0))
    print(f"on the axis, r = {r * 1e9:.0f} nm: E_x = {ex:.3e} V/m")

# Gel: uniform field, illustrative box of 100 V across 20 cm
E_gel = 100 / 0.20
q_dna = -1998 * E_CHARGE                 # 1 kb linear duplex, bare charge
m_dna = 1000 * 617.9e-3 / N_A            # kg, 617.9 g/mol per bp
f_el = abs(q_dna) * E_gel
print(f"gel: E = {E_gel:.0f} V/m, |F| = {f_el * 1e12:.2f} pN, F/weight = {f_el / (m_dna * G_N):.1e}")

# Mass spectrometer: 1000 Da ion, z = +1, field 1e6 V/m over 1 cm (assumed values)
m_ion = 1.0 / N_A                        # kg: 1000 g/mol = 1 kg/mol
acc = E_CHARGE * 1e6 / m_ion
print(f"ion: a = {acc:.2e} m/s^2, speed after 1 cm = {math.sqrt(2 * acc * 0.01):.2e} m/s")
```

```text
on the axis, r = 1 nm: E_x = -2.894e+08 V/m
on the axis, r = 2 nm: E_x = -3.604e+07 V/m
on the axis, r = 4 nm: E_x = -4.501e+06 V/m
gel: E = 500 V/m, |F| = 0.16 pN, F/weight = 1.6e+07
ion: a = 9.65e+10 m/s^2, speed after 1 cm = 4.39e+04 m/s
```

Doubling the distance divides the dipole field by 8.0: the $1/r^3$ law. The sign is negative because, to the right of the dipole, the nearer charge is $-e$ and the field points toward it.

## Worked example

> [!example] Which way does DNA go, and how hard is it pulled?
> A gel box has its electrodes 20 cm apart and the power supply is set to 100 V (illustrative values); the wells are at the cathode end.[^lee]
> 1. **Field.** Treat the box as two plates: $E = \Delta V/d = 500$ V/m, pointing from the anode to the cathode.
> 2. **Charge.** A 1,000 bp linear duplex: $q = -1998e = -3.2 \times 10^{-16}$ C.
> 3. **Force.** $\vec F = q\vec E$: magnitude $1.6 \times 10^{-13}$ N $= 0.16$ pN; since $q < 0$, the force points against $\vec E$, from the wells toward the anode.
> 4. **Scale.** The weight of the molecule, $m g = 1.0 \times 10^{-20}$ N, is $10^7$ times smaller: gravity plays no role.
> 5. **Size dependence.** A 2,000 bp fragment feels twice the force but has twice the mass and charge; the field alone does not separate them, the gel does ([[Electric Charge#Deeper (L2)]]).

## Common misconceptions

> [!warning] "Field lines are the paths that charges follow"
> A line gives the direction of the force, not of the velocity. A charge with inertia, like an ion in the vacuum of a mass spectrometer, can cross field lines. In water, friction dominates and velocity follows force ([[Reynolds Number]]), so ions and DNA do drift along field lines.

> [!warning] "A bigger voltage always means a bigger field"
> $E = \Delta V/d$. A 70 mV membrane carries a field about 30,000 times stronger than a 100 V gel, because its thickness is 5 nm instead of 20 cm.

> [!warning] "The field between two plates is strongest near each plate"
> Each plate's field does not depend on distance, so between ideal plates the field is the same everywhere (figure, panel b). Only near the edges does it bend and weaken.

## Exercises

> [!question] Exercise 1 (L1)
> Compute the field magnitude of a Ca²⁺ ion at 1 nm, in vacuum and in water ($\varepsilon_r \approx 80$, [[Coulomb's Law#Deeper (L2)]]). Which way does it point?

> [!success]- Solution
> $E = k(2e)/r^2 = 8.99 \times 10^9 \times 3.20 \times 10^{-19}/10^{-18} = 2.9 \times 10^9$ V/m in vacuum, $3.6 \times 10^7$ V/m in water; radially away from the ion.

> [!question] Exercise 2 (L1)
> Two plates 1.0 cm apart are held at 50 V. Find the field, the force on an electron, and the force on a 100 bp linear duplex. Which plate does each move toward?

> [!success]- Solution
> $E = 50/0.01 = 5000$ V/m. Electron: $F = eE = 8.0 \times 10^{-16}$ N. Duplex: $z = -198$, $F = 198 \times 1.602 \times 10^{-19} \times 5000 = 1.6 \times 10^{-13}$ N. Both are negative, so both move toward the positive plate.

> [!question] Exercise 3 (L2)
> For the toy dipole of the code ($\pm e$, 0.1 nm apart), compute the field at the midpoint and give its direction. Compare with the far-field formula at 4 nm.

> [!success]- Solution
> At the midpoint both charges are 0.05 nm away and both fields point from $+e$ toward $-e$: $E = 2ke/(0.05 \times 10^{-9})^2 = 1.15 \times 10^{12}$ V/m. Far field at 4 nm: $2kea/r^3 = 2 \times 8.99 \times 10^9 \times 1.602 \times 10^{-19} \times 10^{-10}/(4 \times 10^{-9})^3 = 4.50 \times 10^6$ V/m, matching the code's $4.501 \times 10^6$.

> [!question] Exercise 4 (L2, Python)
> Ions start at rest in a uniform field of $10^6$ V/m across a 1 cm gap (assumed values). Compute the time to cross for (1000 Da, $z = 1$), (2000 Da, $z = 1$) and (2000 Da, $z = 2$). What does the field actually measure?

> [!success]- Solution
> ```python
> import math
> E_CHARGE, N_A = 1.602176634e-19, 6.02214076e23
> E_field, gap = 1e6, 0.01                    # V/m and m (assumed)
> for mass_da, z in [(1000, 1), (2000, 1), (2000, 2)]:
>     m = mass_da * 1e-3 / N_A
>     acc = z * E_CHARGE * E_field / m
>     t = math.sqrt(2 * gap / acc)            # from gap = a t^2 / 2
>     print(f"m = {mass_da} Da, z = {z}: a = {acc:.2e} m/s^2, t = {t * 1e9:.0f} ns")
> ```
> Output: 455 ns, 644 ns, 455 ns. $t = \sqrt{2 d m/(zeE)} \propto \sqrt{m/z}$: the doubly charged 2000 Da ion is indistinguishable from the singly charged 1000 Da one. A spectrometer measures $m/z$, which is why charge states must be deconvolved ([[Mass Spectrometry]]).

## Mastery checklist

- [ ] 1 Recognized: I can define $\vec E = \vec F/q_0$, give its units and draw field lines of a point charge, a dipole and two plates.
- [ ] 2 Understood: I can explain superposition, the $1/r^2$, $1/r^3$ and uniform cases, and why field lines are not trajectories.
- [ ] 3 Practiced: I can compute fields and forces for ions, DNA in a gel and ions in a spectrometer, and evaluate a field by superposition in Python.
- [ ] 4 Applied: I estimated the field and force in a real gel run from the power-supply voltage and box size, and checked the result against band migration.
- [ ] 5 Explained: I can teach why a membrane field dwarfs a gel field, why a spectrometer sorts by $m/z$, and when field lines do or do not predict motion.

## References

[^up5]: [[University Physics (OpenStax)]], Volume 2, ch. 5 "Electric Charges and Fields" (definition of the field, point charges, superposition, field lines, dipoles).
[^upplates]: [[University Physics (OpenStax)]], Volume 2, fields of continuous charge distributions (infinite plane, parallel plates, infinite line); chapter not verified.
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA 2022 values: elementary charge, Avogadro constant (exact), vacuum electric permittivity; standard acceleration of gravity $g_n = 9.806\,65$ m s⁻² (exact).
[^lee]: [[Lee 2012 - Agarose Gel Electrophoresis for the Separation of DNA Fragments]], *Journal of Visualized Experiments*, abstract (migration toward the anode; voltage among the factors of migration).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of mass spectrometry of proteins (ions accelerated by an electric field, time of flight, mass-to-charge ratio).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), membrane structure (bilayer about 5 nm thick) and section "Ion Channels and the Electrical Properties of Membranes" (resting potentials, voltage-gated channels).
