---
aliases:
  - Unit Analysis
  - Dimensional Homogeneity
  - SI Units
  - Analyse dimensionnelle
tags:
  - type/concept
  - domain/physics
  - domain/chemistry
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Mole]]"
  - "[[Derivative]]"
related:
  - "[[Molar Concentration]]"
  - "[[Kinematics]]"
  - "[[Work (Physics)]]"
  - "[[Temperature]]"
  - "[[Order-of-Magnitude Estimation]]"
  - "[[Stokes' Law]]"
  - "[[Reynolds Number]]"
  - "[[Gibbs Free Energy]]"
projects: []
sources:
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[University Physics (OpenStax)]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Svoboda 1994 - Force and Velocity Measured for Single Kinesin Molecules]]"
  - "[[Schnitzer 1997 - Kinesin Hydrolyses One ATP per 8-nm Step]]"
---

# Dimensional Analysis

> [!abstract]
> Every physical quantity is a number times a unit; carrying the units through a calculation converts them for free and exposes most errors, because both sides of a correct equation must have the same dimensions.

## Definition

A **physical quantity** is a number multiplied by a unit, $Q = \{Q\}\,[Q]$: 8 nm is the number 8 times the unit nanometre. Its **dimension** expresses it through the base quantities length (L), mass (M), time (T), electric current (I), temperature (Θ), amount of substance (N) and luminous intensity (J), whose SI base units are the metre, kilogram, second, ampere, kelvin, mole and candela.[^nist][^up1] **Dimensional analysis** uses one rule: terms that are added, subtracted or equated must have the same dimension (**dimensional homogeneity**).[^up1]

## Why it matters

- **Biology mixes scales.** Concentrations come in M, mM, µM and nM ([[Molar Concentration]]); lengths in bp, nm and µm; forces in pN; energies in kJ/mol, kcal/mol, pN·nm or $k_B T$. Each conversion is a chance for a factor of 1000 to slip.
- **Units catch bugs.** A rate constant in M⁻¹ s⁻¹ cannot be compared with one in s⁻¹; a formula that adds a force to a length is wrong before any number is computed. Writing the unit next to every variable in code is a cheap test.
- **The $k_B T$ yardstick.** Molecular energies are compared with the thermal energy $k_B T$, the currency of [[Boltzmann Distribution|Boltzmann factors]] and of single-molecule biophysics.[^pboc]

## Core (L1)

**Derived units** are products of base units:[^nist][^up1]

| Quantity | Unit | In base units | Dimension |
|---|---|---|---|
| force | newton, N | kg m s⁻² | M L T⁻² |
| energy, work | joule, J = N·m | kg m² s⁻² | M L² T⁻² |
| pressure | pascal, Pa = N/m² | kg m⁻¹ s⁻² | M L⁻¹ T⁻² |
| concentration | M = mol/L | 10³ mol m⁻³ | N L⁻³ |

**Prefixes** scale a unit by powers of ten: p = 10⁻¹², n = 10⁻⁹, µ = 10⁻⁶, m = 10⁻³, k = 10³, M = 10⁶, G = 10⁹.[^nist] So 1 pN·nm = 10⁻¹² N × 10⁻⁹ m = 10⁻²¹ J.

**Converting = multiplying by 1.** A conversion factor such as $\frac{10^{-9}\ \text{m}}{1\ \text{nm}}$ equals 1, so it can multiply anything; choose it so that the unwanted unit cancels.[^up1] For 25 µM in nM: $25\ \mu\text{M} \times \frac{10^{-6}\ \text{M}}{1\ \mu\text{M}} \times \frac{1\ \text{nM}}{10^{-9}\ \text{M}} = 25{,}000$ nM.

**Checking an equation.** For the position of an object with constant acceleration, $x = x_0 + v_0 t + \frac{1}{2} a t^2$ ([[Kinematics]]): $[v_0 t] = \text{L T}^{-1} \cdot \text{T} = \text{L}$ and $[a t^2] = \text{L T}^{-2} \cdot \text{T}^2 = \text{L}$, so every term is a length. A version with $v_0 t^2$ would fail. Homogeneity is necessary, not sufficient: the factor $\frac{1}{2}$ is dimensionless and invisible to the check.[^up1]

**The units of biology.** Molecular biophysics works at its own scale:

| Quantity | Working unit | In SI | Example |
|---|---|---|---|
| length | nm | 10⁻⁹ m | kinesin advances 8 nm per step[^schnitzer] |
| force | pN | 10⁻¹² N | kinesin moves against loads up to 5-6 pN[^svoboda] |
| energy | pN·nm, $k_B T$ | 10⁻²¹ J, 4.1 × 10⁻²¹ J | thermal energy at 298 K (below) |
| concentration | nM | 10⁻⁹ mol L⁻¹ | in an *E. coli* cell, 1 nM is about one molecule[^pboc1] |

**$k_B T$.** The Boltzmann constant $k_B = 1.380649 \times 10^{-23}$ J K⁻¹ and the Avogadro constant $N_A = 6.02214076 \times 10^{23}$ mol⁻¹ are exact since the 2019 SI revision.[^nist] At $T = 298.15$ K:

$$k_B T = 4.116 \times 10^{-21}\ \text{J} = 4.116\ \text{pN·nm}, \qquad N_A k_B T = RT = 2.479\ \text{kJ/mol} = 0.592\ \text{kcal/mol},$$

with 1 cal = 4.184 J.[^chem] Dividing an energy by $k_B T$ gives a pure number: how many "thermal kicks" it is worth ([[Temperature]]).

![[energy-scale-kbt-benchmarks.svg]]

## Deeper (L2)

**Per molecule or per mole.** Chemistry tabulates energies per mole, single-molecule physics per molecule; the bridge is $N_A$: $E_{\text{molar}} = N_A E_{\text{molecule}}$, and $R = N_A k_B$.[^nist] The same ratio $E/k_B T = E_{\text{molar}}/RT$ appears in a Boltzmann factor written either way.

**Units reveal the order of a rate law.** If the rate $d[P]/dt$ is in M s⁻¹, then in $d[P]/dt = k[A]$ the constant $k$ is in s⁻¹, and in $d[P]/dt = k[A][B]$ it is in M⁻¹ s⁻¹ ([[Rate Law]]). An equilibrium dissociation constant $K_d = [A][B]/[AB]$ has the unit M; that is why affinities are quoted as "a 10 nM binder".

**Scaling from dimensions alone.** Suppose a time $t$ depends only on a distance $L$ and a diffusion coefficient $D$ (unit m² s⁻¹). The only combination with dimension T is $L^2/D$, so $t \propto L^2/D$: ten times farther takes a hundred times longer, whatever the mechanism's details ([[Diffusion]]). The general rule (the **Buckingham π theorem**) is a counting argument: with $n$ quantities whose dimensions involve $r$ independent combinations of base dimensions, the physics can be written with $n - r$ dimensionless groups (Mathematical representation). Dimensionless numbers such as the [[Reynolds Number]] are those groups.

## Advanced (L3)

- **Logarithms need a reference.** $\ln c$ is meaningless when $c$ has a unit, because $e^x = 1 + x + x^2/2 + \dots$ adds powers of $x$. Thermodynamics therefore writes $\ln(c/c^\circ)$ with a standard concentration $c^\circ$ (1 M); changing $c^\circ$ shifts the tabulated $\Delta G^\circ$ by $RT \ln$ of the ratio ([[Gibbs Free Energy]]). The same holds for fold changes: $\log_2(x_1/x_0)$ is fine because the ratio is dimensionless.
- **Reduced units in simulations.** Choosing the characteristic scales of a problem (nm, $k_B T$, a molecular time) as units makes most numbers of order 1, keeps floating-point arithmetic well conditioned and makes the dimensionless groups visible. Reading a simulation's output then requires converting back, the classic source of a factor-of-10 error between Å and nm.

## Mathematical representation

Write the dimension of $Q$ as $[Q] = \text{L}^{a_1}\text{M}^{a_2}\text{T}^{a_3}\text{I}^{a_4}\Theta^{a_5}\text{N}^{a_6}\text{J}^{a_7}$ and its **dimension vector** $d(Q) = (a_1, \dots, a_7) \in \mathbb{Z}^7$. Then

$$d(AB) = d(A) + d(B), \qquad d(A/B) = d(A) - d(B), \qquad d(A^k) = k\,d(A),$$

and $A + B$ or $A = B$ is meaningful only if $d(A) = d(B)$. A derivative divides dimensions: $d\!\left(\frac{dx}{dt}\right) = d(x) - d(t)$ ([[Derivative]]); an integral multiplies them. Arguments of $\exp$, $\ln$, $\sin$ must have $d = 0$, by the series argument above.

**Dimensionless groups.** Put the vectors of $n$ quantities $Q_1, \dots, Q_n$ as columns of a $7 \times n$ matrix $D$. A product $\prod_i Q_i^{k_i}$ is dimensionless exactly when $Dk = 0$, so the independent dimensionless groups form a basis of the null space of $D$, of dimension $n - \operatorname{rank}(D)$ by the rank-nullity theorem ([[Linear Algebra]]).

## Computational representation

A quantity is stored as an SI value plus its 7-exponent vector; multiplication adds exponents, addition demands equal ones.

```python
BASE = ("m", "kg", "s", "A", "K", "mol", "cd")   # the 7 SI base units

class Q:
    """A value in SI base units, with its dimension as 7 exponents."""

    def __init__(self, value, dims):
        self.value, self.dims = value, tuple(dims)

    def __mul__(self, other):
        if not isinstance(other, Q):                      # plain number
            return Q(self.value * other, self.dims)
        return Q(self.value * other.value, [a + b for a, b in zip(self.dims, other.dims)])

    __rmul__ = __mul__

    def __truediv__(self, other):
        if not isinstance(other, Q):
            return Q(self.value / other, self.dims)
        return Q(self.value / other.value, [a - b for a, b in zip(self.dims, other.dims)])

    def __rtruediv__(self, number):
        return Q(number / self.value, [-a for a in self.dims])

    def __pow__(self, n):
        return Q(self.value ** n, [a * n for a in self.dims])

    def __add__(self, other):
        if self.dims != other.dims:
            raise TypeError(f"cannot add [{self.unit()}] and [{other.unit()}]")
        return Q(self.value + other.value, self.dims)

    def to(self, target):
        """Numerical value of self expressed in the unit `target`."""
        if self.dims != target.dims:
            raise TypeError(f"cannot convert [{self.unit()}] to [{target.unit()}]")
        return self.value / target.value

    def unit(self):
        return " ".join(b if e == 1 else f"{b}^{e}" for b, e in zip(BASE, self.dims) if e) or "1"

def base(name):
    return Q(1.0, [int(b == name) for b in BASE])

m, kg, s, K, mol = base("m"), base("kg"), base("s"), base("K"), base("mol")
N = kg * m / s**2
J = N * m
L = (0.1 * m) ** 3                       # 1 L = 1 dm^3
nm, um, pN, nM = 1e-9 * m, 1e-6 * m, 1e-12 * N, 1e-9 * mol / L

k_B = 1.380649e-23 * J / K               # exact (SI 2019, CODATA)
N_A = 6.02214076e23 / mol                # exact (SI 2019, CODATA)

kT = k_B * (298.15 * K)
print(f"k_B T = {kT.to(pN * nm):.3f} pN nm = {(kT * N_A).to(1e3 * J / mol):.3f} kJ/mol")
count = nM * um**3 * N_A
print(f"1 nM in 1 um^3 = {count.value:.2f} molecules, dimension [{count.unit()}]")
print("[8 nm / 10 ms] =", ((8 * nm) / (0.01 * s)).unit())
try:
    (5 * pN) + (8 * nm)
except TypeError as err:
    print("TypeError:", err)
```

```text
k_B T = 4.116 pN nm = 2.479 kJ/mol
1 nM in 1 um^3 = 0.60 molecules, dimension [1]
[8 nm / 10 ms] = m s^-1
TypeError: cannot add [m kg s^-2] and [m]
```

## Worked example

> [!example] The energy of one ATP, in three units
> In a living cell, ATP hydrolysis releases about 57 kJ/mol.[^os64] How does that compare with $k_B T$ and with the work of a motor step?
> 1. **Per molecule.** $\dfrac{57 \times 10^{3}\ \text{J mol}^{-1}}{6.022 \times 10^{23}\ \text{mol}^{-1}} = 9.47 \times 10^{-20}$ J. The mol⁻¹ cancels.
> 2. **In pN·nm.** 1 pN·nm = 10⁻²¹ J, so $9.47 \times 10^{-20}$ J = 94.7 pN·nm.
> 3. **In $k_B T$.** $94.7 / 4.116 = 23.0$ at 298 K (22.1 at 310 K, body temperature): a dimensionless number, independent of the unit system.
> 4. **Against mechanics.** A kinesin step of 8 nm against a 6 pN load costs $6 \times 8 = 48$ pN·nm $\approx 11.7\ k_B T$, about half the ATP budget ([[Work (Physics)]]).[^schnitzer][^svoboda]
> 5. **Check.** Every intermediate carries a unit; the final ratio has none, as a comparison of two energies must.

## Common misconceptions

> [!warning] "$k_B T$ is a temperature"
> $k_B T$ is an energy (J, or pN·nm). The constant $k_B$ converts kelvins into joules, and $k_B T$ is the energy scale of thermal motion at temperature $T$.

> [!warning] "A dimensionally correct formula is correct"
> Homogeneity is necessary, not sufficient: $x = v_0 t + a t^2$ passes the check and is wrong by a factor $\frac{1}{2}$. Dimensional analysis fixes the form of a law up to dimensionless constants and functions of dimensionless groups.

> [!warning] "M and mol/m³ are the same unit"
> M means mol/L, built on the litre (1 L = 10⁻³ m³), whereas a formula written in SI base units expects mol m⁻³: 1 M = 1000 mol m⁻³. Plugging molar values into an SI formula silently multiplies or divides results by 1000.

## Exercises

> [!question] Exercise 1 (L1)
> Which of these can be correct, with $x$ a length, $v$ a speed, $a$ an acceleration, $t$ a time? (a) $v^2 = 2ax$; (b) $x = vt^2$; (c) $t = \sqrt{2x/a}$; (d) $v = a + t$.

> [!success]- Solution
> (a) L² T⁻² on both sides: possible. (b) L vs L T: wrong. (c) $\sqrt{\text{L}/(\text{L T}^{-2})} = \text{T}$: possible. (d) adds L T⁻² and T: meaningless. (a) and (c) are in fact the constant-acceleration results of [[Kinematics]].

> [!question] Exercise 2 (L2)
> A diffusion time depends only on the distance $L$ and the diffusion coefficient $D$. Assuming an illustrative $D = 10$ µm² s⁻¹ (not a measured value), estimate the time to diffuse 1 µm and 1 mm. What do you conclude?

> [!success]- Solution
> Dimensions force $t \sim L^2/D$. For 1 µm: $10^{-12}\ \text{m}^2 / 10^{-11}\ \text{m}^2\,\text{s}^{-1} = 0.1$ s. For 1 mm: $10^{-6} / 10^{-11} = 10^5$ s ≈ 28 h. A factor 1000 in distance gives $10^6$ in time: diffusion suffices inside a bacterium, not along a long cell, which is why cells use motors ([[Cytoskeleton]]).

> [!question] Exercise 3 (L2)
> The drag force $F$ on a small sphere depends on the fluid viscosity $\eta$ (Pa·s), the radius $r$ and the speed $v$. Find the form of $F$ by dimensional analysis.

> [!success]- Solution
> $[\eta] = \text{M L}^{-1}\text{T}^{-1}$. Write $F = C \eta^a r^b v^c$: mass gives $1 = a$; time gives $-2 = -a - c$, so $c = 1$; length gives $1 = -a + b + c$, so $b = 1$. Hence $F = C\,\eta r v$. Dimensions cannot give $C$; hydrodynamics gives $C = 6\pi$ ([[Stokes' Law]]).

> [!question] Exercise 4 (L3, Python)
> With the class `Q` above, search all exponents $a, b, c \in \{-2, \dots, 2\}$ for which $F \eta^a r^b v^c$ is dimensionless, and relate the result to Exercise 3 and to the null space of the dimension matrix.

> [!success]- Solution
> ```python
> from itertools import product
>
> eta = kg / (m * s)                       # viscosity, Pa s
> r, v, F = m, m / s, N
> for a, b, c in product(range(-2, 3), repeat=3):
>     if (F * eta**a * r**b * v**c).unit() == "1":
>         print("F eta^%d r^%d v^%d is dimensionless" % (a, b, c))
> # F eta^-1 r^-1 v^-1 is dimensionless
> ```
>
> One group, $F/(\eta r v)$: four quantities, three independent dimensions (M, L, T), so $4 - 3 = 1$ dimensionless group, as the rank-nullity count predicts. Its value is the constant $6\pi$ of Exercise 3.

## Mastery checklist

- [ ] 1 Recognized: I can name the SI base units and the prefixes from pico to giga.
- [ ] 2 Understood: I can explain dimensional homogeneity, why $\ln c$ needs a reference concentration, and what $k_B T$ measures.
- [ ] 3 Practiced: I convert nM, pN·nm, kJ/mol and $k_B T$ without error and check equations by their dimensions; I can run the unit checker.
- [ ] 4 Applied: I annotate units in every quantitative script I write and catch at least one unit bug with them.
- [ ] 5 Explained: I can derive scaling laws (diffusion time, Stokes drag) from dimensions and explain the null-space count of dimensionless groups.

## References

[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]]: SI base units and prefixes; CODATA values of the Boltzmann and Avogadro constants, exact since the 2019 SI revision, and $R = N_A k_B$.
[^up1]: [[University Physics (OpenStax)]], Volume 1, ch. 1 "Units and Measurement" (SI units, unit conversion, dimensional analysis).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012): $k_B T$ as the energy scale of molecular biophysics.
[^pboc1]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), ch. 1 "Why: Biology by the Numbers" (1 nM is about one molecule per *E. coli* cell).
[^chem]: [[Chemistry 2e (OpenStax)]]: the calorie, 1 cal = 4.184 J.
[^os64]: [[Biology 2e (OpenStax)]], section 6.4 "ATP: Adenosine Triphosphate" (about −57 kJ/mol, −14 kcal/mol, for ATP hydrolysis in a living cell).
[^svoboda]: [[Svoboda 1994 - Force and Velocity Measured for Single Kinesin Molecules]], *Cell* 77:773-784 (loads up to 5-6 pN).
[^schnitzer]: [[Schnitzer 1997 - Kinesin Hydrolyses One ATP per 8-nm Step]], *Nature* 388:386-390 (8-nm steps, one ATP per step).
