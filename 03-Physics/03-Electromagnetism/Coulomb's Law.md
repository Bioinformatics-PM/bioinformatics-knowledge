---
aliases:
  - Coulomb Force
  - Coulomb Interaction
  - Electrostatic Force
  - Loi de Coulomb
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
  - "[[Electric Charge]]"
  - "[[Vector]]"
  - "[[Newton's Laws of Motion]]"
  - "[[Potential Energy]]"
related:
  - "[[Electric Field]]"
  - "[[Electric Potential]]"
  - "[[Ionic Bond]]"
  - "[[Water]]"
  - "[[Dielectric Constant]]"
  - "[[Debye Length]]"
  - "[[Intermolecular Force]]"
  - "[[Poisson-Boltzmann Equation]]"
projects: []
sources:
  - "[[University Physics (OpenStax)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Watson 1953 - Molecular Structure of Nucleic Acids]]"
---

# Coulomb's Law

> [!abstract]
> Two charges push or pull on each other with a force that grows with the product of the charges and falls as the square of their distance; in water the interaction is about 80 times weaker, so two unit charges more than 0.7 nm apart interact more weakly than thermal motion.

## Definition

Two point charges $q_1$ and $q_2$ a distance $r$ apart exert on each other forces of magnitude
$$F = k\,\frac{|q_1 q_2|}{r^2}, \qquad k = \frac{1}{4\pi\varepsilon_0} \approx 8.988 \times 10^{9}\ \text{N m}^2\,\text{C}^{-2},$$
directed along the line joining them: repulsive for like charges, attractive for unlike charges.[^up5] $\varepsilon_0 = 8.854\,187\,8188(14) \times 10^{-12}$ F m⁻¹ is the vacuum permittivity (CODATA 2022).[^nist] The corresponding **potential energy**, zero at infinite separation, is $U = k\,q_1 q_2 / r$.[^up7]

## Why it matters

- **Salt bridges and charged contacts.** The attraction between a Lys or Arg side chain and an Asp or Glu side chain is a Coulomb interaction; how strong it is depends on distance and on the surrounding medium ([[Ionic Bond]], [[Protein Tertiary Structure]]).[^berg]
- **From coordinates to energies.** Given atomic coordinates (a PDB file) and charges, the electrostatic energy is a sum of Coulomb terms over pairs: the starting point of the electrostatics in a [[Force Field]] and of continuum models ([[Poisson-Boltzmann Equation]]).
- **Salt changes binding.** Dissolved ions screen charges, which is why ionic strength is a parameter of every binding or hybridization experiment ([[Debye Length]]).[^pboc]
- **The $k_B T$ yardstick.** Comparing a Coulomb energy with the thermal energy $k_B T$ tells whether an interaction survives thermal agitation: the [[#Deeper (L2)|Bjerrum length]] answers it in one number.[^pboc]

## Core (L1)

**Vector form.** The force exerted by $q_1$ on $q_2$ is
$$\vec F_{12} = k\,\frac{q_1 q_2}{r^2}\,\hat r_{12},$$
where $\hat r_{12}$ is the unit vector from $q_1$ to $q_2$ ([[Vector]]). A positive product pushes $q_2$ away; a negative product pulls it in. $\vec F_{21} = -\vec F_{12}$: the pair obeys Newton's third law ([[Newton's Laws of Motion]]).[^up5]

**Superposition.** The force on a charge due to several others is the vector sum of the pair forces, each computed as if the others were absent.[^up5] All of electrostatics, from fields to the energy of a protein, is built from this rule.

**Energy from force.** Bringing $q_2$ from infinity to $r$ against the Coulomb force stores the work (derivation, [[Potential Energy]], [[Integral]]):
$$U(r) = \int_r^{\infty} k\,\frac{q_1 q_2}{r'^2}\,dr' = k\,\frac{q_1 q_2}{r}, \qquad F_r = -\frac{dU}{dr}.$$
Force falls as $1/r^2$, energy as $1/r$. $U < 0$ means a bound (attractive) pair: energy must be supplied to separate it.

**Molecular scale.** With $k_B T = 4.12 \times 10^{-21}$ J at 25 °C as the energy unit (computed below):

| Pair | Medium | Force | Energy |
|---|---|---:|---:|
| $+e$, $-e$ at 1 nm | vacuum | 231 pN | −56 $k_B T$ |
| $+e$, $-e$ at 1 nm | water | 2.9 pN | −0.70 $k_B T$ |
| salt bridge, charges 0.4 nm apart (assumed) | vacuum | 1442 pN | −140 $k_B T$ |
| salt bridge, charges 0.4 nm apart (assumed) | water | 18 pN | −1.75 $k_B T$ |

The same salt bridge in kJ/mol is computed in [[Ionic Bond]]: a strong bond in vacuum, a weak and reversible contact in water.

**Bio: the DNA backbone repels itself.** Each phosphate carries $-e$ ([[Electric Charge]]). In the 1953 model, phosphates sit 10 Å from the axis, with a rise of 3.4 Å and a turn of 36° per residue;[^watson] neighbouring phosphates of one strand are then 0.705 nm apart (Worked example), and each pair repels with about 79 $k_B T$ in vacuum and 1 $k_B T$ in water.

![[coulomb-energy-vs-distance.svg]]

## Deeper (L2)

**Screening by a dielectric.** In a uniform insulating medium, the molecules polarize: their dipoles orient around each charge and partly cancel its field, so force and energy are divided by the medium's **dielectric constant** $\varepsilon_r$:[^updiel]
$$F = \frac{k}{\varepsilon_r}\,\frac{q_1 q_2}{r^2}, \qquad U = \frac{k}{\varepsilon_r}\,\frac{q_1 q_2}{r}.$$
Water's dielectric constant is about 80,[^updiel][^lehninger] which is why ions separate easily in water and why salt bridges are weak at a protein surface ([[Water]], [[Dielectric Constant]]).

**Bjerrum length.** Setting $|U| = k_B T$ for two elementary charges defines the distance below which their interaction beats thermal motion:
$$\ell_B = \frac{e^2}{4\pi\varepsilon_0\,\varepsilon_r\,k_B T}, \qquad \frac{U}{k_B T} = z_1 z_2\,\frac{\ell_B}{r}$$
for charges $z_1 e$ and $z_2 e$. In water at 25 °C, $\ell_B = 0.70$ nm (computed below), the value of about 0.7 nm used in physical biology.[^pboc] In vacuum $\ell_B = 56$ nm; with an assumed $\varepsilon_r = 4$ for a protein interior (an illustrative value, as in [[Water]]) it is 14 nm: inside a protein, charges interact strongly over the whole molecule, which is why burying an unpaired charge is costly ([[Dielectric Constant]]).

**Many charges: superposition on the backbone.** A single pair of neighbouring phosphates costs only about 1 $k_B T$ in water, but every phosphate repels all the others. Summing over one strand (Exercise 4), the unscreened energy of a central phosphate grows by about 9.5 $k_B T$ each time the strand gets ten times longer: it never levels off. In cells this repulsion is offset by bound cations and by histones rich in positive residues,[^alberts] and in solution dissolved salt screens it beyond a few nanometres ([[Debye Length]], L2).[^pboc]

## Advanced (L3)

- **Long range is the computational problem.** $N$ charges form $N(N-1)/2$ pairs. In a medium of uniform charge density $\rho$, the charge in a shell between $r$ and $r + dr$ around a given charge grows as $4\pi r^2 \rho\,dr$ while each partner contributes $\propto 1/r$: distant shells contribute $\propto r\,dr$, so the sum cannot be truncated at a short cutoff. Neutrality and screening are what make it converge, which is why [[Molecular Dynamics Simulation]] and continuum solvers ([[Poisson-Boltzmann Equation]]) treat electrostatics with dedicated methods.
- **Where the continuum fails.** $\varepsilon_r$ is a property of bulk matter, an average over many polarized molecules.[^updiel] At contact distances of one or two water molecules, and inside heterogeneous proteins, a single number is a model choice, not a measurement ([[Dielectric Constant]]).

## Mathematical representation

- **Pair force** on charge $j$ from charge $i$, at positions $\vec r_i, \vec r_j$ with $r_{ij} = |\vec r_j - \vec r_i|$:
$$\vec F_{ij} = \frac{1}{4\pi\varepsilon_0 \varepsilon_r}\,\frac{q_i q_j}{r_{ij}^3}\,(\vec r_j - \vec r_i).$$
- **Superposition**: $\vec F_j = \sum_{i \ne j} \vec F_{ij}$.
- **Energy of a system**: $U = \sum_{i<j} \dfrac{q_i q_j}{4\pi\varepsilon_0 \varepsilon_r\, r_{ij}}$, and $\vec F_j = -\nabla_j U$ ([[Gradient]]).
- **Thermal units**: $U/k_B T = \sum_{i<j} z_i z_j\,\ell_B / r_{ij}$, with $k_B$ the Boltzmann constant, $T$ the absolute temperature and $\ell_B$ the Bjerrum length.

## Computational representation

Work in SI units inside functions and convert only for display (pN, nm, $k_B T$). Constants: $e$ and $k_B$ exact, $\varepsilon_0$ from CODATA 2022;[^nist] phosphate positions from the 1953 helix geometry.[^watson]

```python
import math

E_CHARGE = 1.602176634e-19       # C, exact
EPS0 = 8.8541878188e-12          # F m^-1, CODATA 2022
K_B = 1.380649e-23               # J K^-1, exact
K_C = 1 / (4 * math.pi * EPS0)   # Coulomb constant, N m^2 C^-2


def coulomb_force(q1, q2, r, eps_r=1.0):
    """Radial force (N) between point charges q1, q2 (C) at distance r (m): > 0 repulsive."""
    return K_C * q1 * q2 / (eps_r * r**2)


def coulomb_energy(q1, q2, r, eps_r=1.0):
    """Interaction energy (J), zero at infinite separation: < 0 attractive."""
    return K_C * q1 * q2 / (eps_r * r)


def bjerrum_length(T=298.15, eps_r=80.0):
    """Distance (m) at which two elementary charges interact with energy k_B T."""
    return E_CHARGE**2 / (4 * math.pi * EPS0 * eps_r * K_B * T)


kT = K_B * 298.15
print(f"k = {K_C:.4e} N m2 C-2, kT = {kT:.3e} J")
for label, r, eps in [("+e/-e 1 nm, vacuum", 1e-9, 1), ("+e/-e 1 nm, water", 1e-9, 80),
                      ("salt bridge 0.4 nm, vacuum", 0.4e-9, 1), ("salt bridge 0.4 nm, water", 0.4e-9, 80)]:
    f = coulomb_force(E_CHARGE, -E_CHARGE, r, eps)
    u = coulomb_energy(E_CHARGE, -E_CHARGE, r, eps)
    print(f"{label:27s} F = {f * 1e12:8.1f} pN   U = {u / kT:8.2f} kBT")
for T, eps in [(298.15, 80), (298.15, 1), (298.15, 4)]:
    print(f"Bjerrum length T = {T} K, eps_r = {eps:2d}: {bjerrum_length(T, eps) * 1e9:.2f} nm")


def strand_phosphates(n, radius=1.0e-9, rise=0.34e-9, twist_deg=36.0):
    """Positions (m) of n successive phosphates of one B-DNA strand (1953 model geometry)."""
    return [(radius * math.cos(math.radians(twist_deg * i)),
             radius * math.sin(math.radians(twist_deg * i)),
             rise * i) for i in range(n)]


p0, p1 = strand_phosphates(2)
d = math.dist(p0, p1)
for eps in (1, 80):
    u = coulomb_energy(-E_CHARGE, -E_CHARGE, d, eps)
    print(f"neighbours {d * 1e9:.3f} nm apart, eps_r = {eps:2d}: U = {u / kT:6.2f} kBT")
```

```text
k = 8.9876e+09 N m2 C-2, kT = 4.116e-21 J
+e/-e 1 nm, vacuum          F =   -230.7 pN   U =   -56.05 kBT
+e/-e 1 nm, water           F =     -2.9 pN   U =    -0.70 kBT
salt bridge 0.4 nm, vacuum  F =  -1441.9 pN   U =  -140.11 kBT
salt bridge 0.4 nm, water   F =    -18.0 pN   U =    -1.75 kBT
Bjerrum length T = 298.15 K, eps_r = 80: 0.70 nm
Bjerrum length T = 298.15 K, eps_r =  1: 56.05 nm
Bjerrum length T = 298.15 K, eps_r =  4: 14.01 nm
neighbours 0.705 nm apart, eps_r =  1: U =  79.45 kBT
neighbours 0.705 nm apart, eps_r = 80: U =   0.99 kBT
```

## Worked example

> [!example] Two neighbouring phosphates of a DNA strand
> 1. **Geometry.** Radius $R = 1.0$ nm, rise $h = 0.34$ nm, twist $36°$ per residue.[^watson] Projected on the plane perpendicular to the axis, the two phosphates are a chord $2R\sin 18° = 0.618$ nm apart; along the axis they are $h$ apart. Distance: $r = \sqrt{0.618^2 + 0.34^2} = 0.705$ nm.
> 2. **Vacuum.** $U = k e^2/r = 2.307 \times 10^{-28} / 0.705 \times 10^{-9} = 3.27 \times 10^{-19}$ J $= 79\ k_B T$; force $k e^2/r^2 = 464$ pN, repulsive.
> 3. **Water** ($\varepsilon_r \approx 80$): $U = 0.99\ k_B T$, $F = 5.8$ pN. Equivalently, $U/k_B T = \ell_B/r = 0.70/0.705$.
> 4. **Reading.** One pair is at the thermal scale, so water makes the backbone chemically possible. But each phosphate has hundreds of partners, and the sum grows without limit (Exercise 4): counterions and salt are part of the structure of DNA, not an afterthought.

## Common misconceptions

> [!warning] "Coulomb energy also falls as 1/r²"
> The force does; the energy falls as $1/r$. Doubling the distance divides the force by 4 but the energy only by 2, which is why electrostatics reaches further than intuition suggests.

> [!warning] "In water, electrostatics is negligible"
> One pair of unit charges at 1 nm is below $k_B T$ in water, but energies add over many charges (Exercise 4), multivalent ions multiply them ($z_1 z_2$), and a protein interior (assumed $\varepsilon_r = 4$) makes them 20 times stronger again.

> [!warning] "$\varepsilon_r = 80$ holds at every distance"
> The dielectric constant is a bulk average over many water molecules.[^updiel] For two charges in contact, separated by less than a water molecule or buried in a protein, there is no single correct value.

> [!warning] "A larger force means a negative number"
> The sign carries direction, not size: $q_1 q_2 > 0$ is repulsion, $q_1 q_2 < 0$ attraction. A negative energy means the pair is bound relative to infinite separation.

## Exercises

> [!question] Exercise 1 (L1)
> Compute the force (pN) and energy ($k_B T$ at 25 °C) between Na⁺ and Cl⁻ at an assumed distance of 0.28 nm in vacuum. Is the pair attractive?

> [!success]- Solution
> $F = k e^2/r^2 = 2.307 \times 10^{-28}/(0.28 \times 10^{-9})^2 = 2.94 \times 10^{-9}$ N $\approx 2900$ pN. $U = -k e^2/r = -8.24 \times 10^{-19}$ J $= -200\ k_B T$. Attractive (opposite charges): in vacuum such a pair never separates thermally.

> [!question] Exercise 2 (L2)
> A Mg²⁺ ion is placed (toy geometry) exactly midway between two phosphates 0.705 nm apart, in water. Find the net force on Mg²⁺ and the total energy of the three charges in $k_B T$.

> [!success]- Solution
> By symmetry the two attractions on Mg²⁺ cancel: net force zero. Energy, in units of $u = k e^2/(\varepsilon_r d) = 0.99\ k_B T$: phosphate-phosphate $(-1)(-1)/1 = +1$; each Mg-phosphate $(+2)(-1)/(1/2) = -4$, twice. Total $(1 - 8)\,u = -7.0\ k_B T$: one divalent ion turns a repulsive pair into a bound trio. On each phosphate, the pull of Mg²⁺ ($8u/d$ in force units) beats the push of the other phosphate ($u/d$).

> [!question] Exercise 3 (L2, Python)
> Using `bjerrum_length`, compute $\ell_B$ at 25 °C and 37 °C for $\varepsilon_r = 80$ and for the assumed $\varepsilon_r = 4$. Which matters more, temperature or medium?

> [!success]- Solution
> ```python
> for T in (298.15, 310.15):
>     for eps in (80, 4):
>         print(f"T = {T} K, eps_r = {eps:2d}: l_B = {bjerrum_length(T, eps) * 1e9:5.2f} nm")
> ```
> Output: `0.70`, `14.01`, `0.67` and `13.47` nm. Twelve kelvin change $\ell_B$ by 4 %; the medium changes it 20-fold. (This keeps $\varepsilon_r$ fixed: water's own dielectric constant also varies with temperature.)

> [!question] Exercise 4 (L3, Python)
> With `strand_phosphates`, compute the unscreened energy (in water) of the central phosphate of a strand of $n$ phosphates with all the others, for $n$ = 3, 11, 101, 1001, 10001. Explain the trend.

> [!success]- Solution
> ```python
> def central_energy_kT(n, eps_r=80.0):
>     """Unscreened Coulomb energy (kBT) of the middle phosphate with all others of its strand."""
>     pts = strand_phosphates(n)
>     mid = pts[n // 2]
>     return sum(K_C * E_CHARGE**2 / (eps_r * math.dist(mid, p)) for p in pts if p is not mid) / kT
>
>
> for n in (3, 11, 101, 1001, 10001):
>     print(f"n = {n:5d}: U = {central_energy_kT(n):5.2f} kBT")
> ```
> Output: `1.99`, `4.88`, `13.54`, `22.98`, `32.47` $k_B T$. Far away, partners lie every 0.34 nm along the axis on each side, so the sum behaves like $2\,(\ell_B/0.34\ \text{nm}) \sum 1/j$, a harmonic series that grows as $\ln n$: about $4.1 \ln 10 \approx 9.5\ k_B T$ per decade, as observed. Without screening the energy diverges with length; dissolved salt cuts it off ([[Debye Length]]).

## Mastery checklist

- [ ] 1 Recognized: I can write Coulomb's law for force and energy and give the value of $k$.
- [ ] 2 Understood: I can explain superposition, the $1/r^2$ versus $1/r$ dependence, dielectric screening and the meaning of the Bjerrum length.
- [ ] 3 Practiced: I can compute forces in pN and energies in $k_B T$ for ions, salt bridges and phosphates, in vacuum and in water.
- [ ] 4 Applied: I computed pairwise electrostatic energies between charged residues of a real protein structure and compared buried and exposed pairs.
- [ ] 5 Explained: I can teach why electrostatics is long-ranged, why salt and the protein interior change it, and where the continuum $\varepsilon_r$ picture fails.

## References

[^up5]: [[University Physics (OpenStax)]], Volume 2, ch. 5 "Electric Charges and Fields" (Coulomb's law, vector form, superposition).
[^up7]: [[University Physics (OpenStax)]], Volume 2, ch. 7 "Electric Potential" (electric potential energy of two point charges, zero at infinity).
[^updiel]: [[University Physics (OpenStax)]], Volume 2, dielectrics (dielectric constant, representative values, molecular model of a dielectric).
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA 2022 values: vacuum electric permittivity $\varepsilon_0 = 8.854\,187\,8188(14) \times 10^{-12}$ F m⁻¹; elementary charge and Boltzmann constant (exact).
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of electrostatics in salty solutions (Bjerrum length of about 0.7 nm in water, screening by salt) and of $k_B T$ as the energy scale of the cell.
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of water (dielectric constant, screening of dissolved ions).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of electrostatic interactions (salt bridges) between charged side chains in proteins.
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), DNA packaging (histones rich in positively charged amino acids).
[^watson]: [[Watson 1953 - Molecular Structure of Nucleic Acids]], *Nature* (phosphates 10 Å from the axis, 3.4 Å rise, 10 residues per turn).
