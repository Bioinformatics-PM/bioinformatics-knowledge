---
aliases:
  - Orbital
  - Orbitale atomique
  - Quantum Numbers
tags:
  - type/concept
  - domain/chemistry
  - domain/physics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Atom]]"
  - "[[Probability Density Function]]"
related:
  - "[[Electron Configuration]]"
  - "[[Periodic Table]]"
  - "[[Orbital Hybridization]]"
  - "[[Molecular Orbital Theory]]"
  - "[[Spectroscopy]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
---

# Atomic Orbital

> [!abstract]
> An atomic orbital is a region where an electron is likely to be found, described by a probability cloud and labeled by quantum numbers; s orbitals are spheres, p orbitals dumbbells along an axis, d orbitals mostly four-lobed.

## Definition

An **atomic orbital** is a wavefunction $\psi$ describing one electron in an atom. It is labeled by three quantum numbers, $n$, $l$ and $m_l$, and $|\psi|^2$ gives the **probability density** of finding the electron at each point in space. An electron has no definite trajectory: the orbital is drawn as the surface enclosing most of that probability.[^c2e63]

## Why it matters

- **Geometry comes from orbitals.** The tetrahedral carbon of every amino acid, the flat nucleobases that stack in [[DNA]] and the planar [[Peptide Bond|peptide bond]] follow from how s and p orbitals combine ([[Orbital Hybridization]], [[Molecular Geometry]]). Every bond angle in a structure file is a consequence.
- **Light is absorbed by electrons changing orbitals.** An atom absorbs or emits a photon whose energy equals the difference between two electronic levels.[^c2e6] In molecules the same principle, with [[Molecular Orbital Theory|molecular orbitals]], underlies UV absorbance and fluorescence measurements ([[Spectroscopy]], [[Fluorescence Microscopy]]).
- **A probability model of matter.** An orbital is a [[Probability Density Function]] over 3D space: the same mathematics as a statistical model, with normalization, cumulative probability and most probable values (Exercise 4).

## Core (L1)

**Four quantum numbers.**[^c2e63]

| Symbol | Name | Allowed values | Determines |
|---|---|---|---|
| $n$ | principal | 1, 2, 3, … | shell: size and (mostly) energy |
| $l$ | angular momentum (azimuthal) | 0, 1, …, $n - 1$ | subshell shape: $l$ = 0, 1, 2, 3 is s, p, d, f |
| $m_l$ | magnetic | $-l, \dots, 0, \dots, +l$ | orientation: $2l + 1$ orbitals per subshell |
| $m_s$ | spin | $+\tfrac12$ or $-\tfrac12$ | the electron's spin, two per orbital |

A subshell is named by $n$ and the letter for $l$: 1s, 2p, 3d. Shell $n$ contains $n$ subshells and $n^2$ orbitals.

**Shapes.**[^c2e63]

![[atomic-orbital-shapes-s-p-d.svg]]

- **s** ($l = 0$): one spherical orbital per shell; larger as $n$ increases.
- **p** ($l = 1$): three dumbbells along $x$, $y$ and $z$, each with two lobes of opposite sign separated by a **nodal plane** through the nucleus.
- **d** ($l = 2$): five orbitals; four have four lobes ($d_{xy}$, $d_{xz}$, $d_{yz}$, $d_{x^2-y^2}$), and $d_{z^2}$ has two lobes along $z$ plus a ring.
- The colors (sign of $\psi$) do not change the probability, which depends on $|\psi|^2$; they matter when orbitals of two atoms overlap to form a bond ([[Molecular Orbital Theory]]).

## Deeper (L2)

- **Nodes.** A node is a surface where $\psi = 0$, so the electron is never found there. An orbital has $l$ angular nodes (planes or cones through the nucleus) and $n - l - 1$ radial nodes (spheres): 2s has one radial node, 2p one nodal plane, 3d two angular nodes.[^5111]
- **Probability at a distance.** For a spherical orbital, the probability of finding the electron between $r$ and $r + dr$ is $P(r)\,dr = 4\pi r^2 |\psi(r)|^2\, dr$. The density $|\psi|^2$ of 1s is highest at the nucleus, but $P(r)$ peaks at a finite radius because the shell volume $4\pi r^2 dr$ grows with $r$ (Exercise 3).
- **Energy order in many-electron atoms.** In hydrogen, the energy depends on $n$ only. With several electrons, inner electrons shield the nucleus, and within a shell s orbitals lie lower than p, then d, which sets the filling order of the [[Electron Configuration]].[^c2e64]
- **Bohr's orbits were a step, not the answer.** Bohr's model reproduced hydrogen's energy levels with orbit radii $r_n = n^2 a_0$, where $a_0 = 5.292 \times 10^{-11}$ m (0.529 Å) is the Bohr radius, but it failed for atoms with more electrons and was replaced by quantum mechanics.[^c2e62]

## Advanced (L3)

- **Where orbitals come from.** Orbitals are the solutions of the Schrödinger equation $\hat H \psi = E \psi$ for an electron in the Coulomb field of the nucleus; quantum numbers arise as the conditions for physically acceptable solutions.[^c2e63][^5111] For hydrogen the energies are $E_n = -k/n^2$ with $k = 2.179 \times 10^{-18}$ J, and the 1s orbital is $\psi_{1s}(r) = (\pi a_0^3)^{-1/2} e^{-r/a_0}$.[^c2e62][^5111]
- **The orbital approximation.** For more than one electron the equation has no exact solution; assigning each electron its own hydrogen-like orbital is an approximation that works well enough to explain the [[Periodic Table]]. Quantum chemistry methods refine it numerically ([[Molecular Orbital Theory]]).
- **Orbitals in bonds.** Combining atomic orbitals on neighboring atoms gives hybrid orbitals ([[Orbital Hybridization]]) and molecular orbitals; π orbitals delocalized over rings explain the flat, stacking, UV-absorbing nucleobases and aromatic side chains.

## Mathematical representation

- An orbital is $\psi_{n,l,m_l}(\mathbf r)$, with normalization $\int_{\mathbb R^3} |\psi(\mathbf r)|^2 \, d^3 r = 1$: $|\psi|^2$ is a probability density in 3D.
- Allowed labels: $n \in \mathbb N^{*}$, $l \in \{0, \dots, n-1\}$, $m_l \in \{-l, \dots, l\}$, $m_s \in \{\pm\frac12\}$. Number of orbitals in shell $n$: $\sum_{l=0}^{n-1} (2l + 1) = n^2$; electrons: $2n^2$.
- Hydrogen 1s, with $\rho = r/a_0$: radial distribution $P(\rho) = 4\rho^2 e^{-2\rho}$ (in units of $1/a_0$) and cumulative probability
$$F(R) = P(r < R a_0) = 1 - e^{-2R}\left(1 + 2R + 2R^2\right),$$
obtained by integrating $P$ by parts.

## Computational representation

Quantum numbers are a small combinatorial object: enumerate them, and the shell capacities of the periodic table follow.

```python
SUBSHELL = "spdf"

def orbitals(n: int) -> list[tuple[int, int, int]]:
    """All allowed (n, l, m_l) for shell n."""
    return [(n, l, m) for l in range(n) for m in range(-l, l + 1)]

for n in range(1, 5):
    subshells = [f"{n}{SUBSHELL[l]}({2 * l + 1})" for l in range(n)]
    print(n, " ".join(subshells), "orbitals:", len(orbitals(n)),
          "electrons:", 2 * len(orbitals(n)))
print(orbitals(2))
```

```text
1 1s(1) orbitals: 1 electrons: 2
2 2s(1) 2p(3) orbitals: 4 electrons: 8
3 3s(1) 3p(3) 3d(5) orbitals: 9 electrons: 18
4 4s(1) 4p(3) 4d(5) 4f(7) orbitals: 16 electrons: 32
[(2, 0, 0), (2, 1, -1), (2, 1, 0), (2, 1, 1)]
```

The capacities 2, 8, 18, 32 are the lengths of the rows of the [[Periodic Table]] (2, 8, 8, 18, 18, 32, 32), once the energy ordering of subshells is taken into account.[^c2e64]

## Worked example

> [!example] Labeling the orbitals of the second shell
> 1. $n = 2$, so $l \in \{0, 1\}$: subshells 2s and 2p.
> 2. $l = 0$: $m_l = 0$, one 2s orbital (sphere with one radial node, since $n - l - 1 = 1$).
> 3. $l = 1$: $m_l \in \{-1, 0, 1\}$, three 2p orbitals, conventionally $2p_x, 2p_y, 2p_z$, each with one nodal plane.
> 4. Total: $1 + 3 = 4 = 2^2$ orbitals, room for 8 electrons: the eight valence electrons of neon, and the "octet" that carbon, nitrogen and oxygen complete when they bond ([[Electron Configuration]]).

## Common misconceptions

> [!warning] "An orbital is the path the electron follows"
> An orbital is a probability distribution, not a trajectory; the planetary orbits of the Bohr model were abandoned.[^c2e63][^c2e62]

> [!warning] "The lobes of a p orbital are two places the electron jumps between"
> The two lobes are one orbital, a single probability distribution. The nodal plane has zero density, but $\psi$ is a wave, and a wave can have opposite signs on either side of a node without the electron "crossing" anything.

> [!warning] "Plus and minus lobes mean positive and negative charge"
> The sign is the phase of the wavefunction, not an electric charge. Both lobes hold the same kind of probability density $|\psi|^2 \ge 0$ for the same (negatively charged) electron; the sign only matters when orbitals combine.[^c2e63]

## Exercises

> [!question] Exercise 1 (L1)
> Which of these $(n, l, m_l)$ are allowed: $(2, 2, 0)$, $(3, 1, -1)$, $(1, 0, 0)$, $(3, 2, 3)$? Name the subshell of the allowed ones.

> [!success]- Solution
> $(2, 2, 0)$: no, $l \le n - 1 = 1$. $(3, 1, -1)$: yes, 3p. $(1, 0, 0)$: yes, 1s. $(3, 2, 3)$: no, $|m_l| \le l = 2$. The shell $n = 3$ holds 3s, 3p and 3d: $1 + 3 + 5 = 9$ orbitals, 18 electrons.

> [!question] Exercise 2 (L2)
> Give the number of radial and angular nodes of 3s, 3p and 3d.

> [!success]- Solution
> Radial $n - l - 1$, angular $l$: 3s: 2 and 0; 3p: 1 and 1; 3d: 0 and 2. Every $n = 3$ orbital has $n - 1 = 2$ nodes in total.

> [!question] Exercise 3 (L2)
> Show that the radial distribution $P(\rho) = 4\rho^2 e^{-2\rho}$ of hydrogen 1s is maximal at $\rho = 1$, i.e. at $r = a_0$.

> [!success]- Solution
> $P'(\rho) = 4 e^{-2\rho}(2\rho - 2\rho^2) = 8\rho(1 - \rho) e^{-2\rho}$, zero at $\rho = 0$ and $\rho = 1$, positive between and negative after: a maximum at $r = a_0 = 0.529$ Å, Bohr's radius, recovered as the *most probable* distance rather than a fixed orbit.

> [!question] Exercise 4 (L3, Python)
> Using $F(R)$ from the Mathematical representation, find by bisection the radius of the sphere containing 50%, 90% and 99% of the 1s probability, in units of $a_0$ and in ångström. What is $F(1)$?

> [!success]- Solution
> ```python
> from math import exp
>
> def p_inside(R: float) -> float:
>     """P(r < R) for the hydrogen 1s electron, R in units of a0."""
>     return 1 - exp(-2 * R) * (1 + 2 * R + 2 * R**2)
>
> def radius_containing(prob: float) -> float:
>     lo, hi = 0.0, 20.0
>     for _ in range(60):  # bisection: p_inside is increasing
>         mid = (lo + hi) / 2
>         lo, hi = (mid, hi) if p_inside(mid) < prob else (lo, mid)
>     return lo
>
> A0 = 0.529  # Bohr radius in angstrom
> for prob in (0.5, 0.9, 0.99):
>     R = radius_containing(prob)
>     print(prob, round(R, 3), "a0 =", round(R * A0, 2), "A")
> print(round(p_inside(1.0), 3))
> ```
> ```text
> 0.5 1.337 a0 = 0.71 A
> 0.9 2.661 a0 = 1.41 A
> 0.99 4.203 a0 = 2.22 A
> 0.323
> ```
> Only 32% of the probability lies inside the most probable radius $a_0$: the distribution has a long tail. The "size" of an orbital depends on the probability chosen for its boundary surface, exactly like a quantile of any distribution.

## Mastery checklist

- [ ] 1 Recognized: I can name the four quantum numbers and the shapes of s, p and d orbitals.
- [ ] 2 Understood: I can explain an orbital as a probability density, and nodes and phase signs without the planetary picture.
- [ ] 3 Practiced: I can list allowed quantum numbers, count orbitals and nodes, and compute cumulative radial probabilities in Python.
- [ ] 4 Applied: I used orbital shapes to explain the geometry of a real biomolecule (tetrahedral Cα, planar base) seen in a structure viewer.
- [ ] 5 Explained: I can explain where orbitals come from (Schrödinger equation), the orbital approximation and its limits.

## References

[^c2e62]: [[Chemistry 2e (OpenStax)]], ch. 6, §6.2 "The Bohr Model".
[^c2e63]: [[Chemistry 2e (OpenStax)]], ch. 6, §6.3 "Development of Quantum Theory".
[^c2e64]: [[Chemistry 2e (OpenStax)]], ch. 6, §6.4 "Electronic Structure of Atoms (Electron Configurations)".
[^c2e6]: [[Chemistry 2e (OpenStax)]], ch. 6 "Electronic Structure and Periodic Properties of Elements".
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], Unit I "The Atom" (lecture not verified).
