---
aliases:
  - Periodic Table of the Elements
  - Tableau périodique
  - Periodic Trends
tags:
  - type/concept
  - domain/chemistry
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Atom]]"
  - "[[Electron Configuration]]"
related:
  - "[[Atomic Orbital]]"
  - "[[Electronegativity]]"
  - "[[Ionic Bond]]"
  - "[[Covalent Bond]]"
  - "[[Ion Channel]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Biochemistry (Berg)]]"
---

# Periodic Table

> [!abstract]
> The periodic table orders the elements by atomic number so that elements with the same outer electrons fall in the same column; from an element's position alone you can predict its size, how easily it loses an electron, and how many bonds it usually makes.

## Definition

The **periodic table** arranges the elements in order of increasing atomic number $Z$, in rows called **periods** and columns called **groups** (numbered 1 to 18). Elements of the same group have analogous valence electron configurations and therefore similar chemical properties.[^c2e2][^c2e64] The table divides into **blocks** named after the subshell being filled: s (groups 1-2), p (13-18), d (3-12) and f.[^c2e64]

## Why it matters

- **Position predicts bonding.** The group gives the number of valence electrons, hence the usual valence: the bond counts of C, N, O and S and the charges of Na⁺, Mg²⁺ and Cl⁻ can be read off the table ([[Electron Configuration]]).
- **Same group, similar chemistry, different size.** Selenium sits below sulfur, and selenocysteine is cysteine with Se in place of S.[^berg] K⁺ sits below Na⁺: same charge, one more shell, and potassium channels discriminate the two ions by size ([[Ion Channel]]).[^berg]
- **Trends feed later notes.** Size and electron-attracting power set [[Electronegativity]], which sets bond polarity, [[Hydrogen Bond|hydrogen bonds]] and the solvent behavior of [[Water]].

## Core (L1)

![[periodic-table-trends-elements-of-life.svg]]

**Reading a position.**[^c2e64]

- The **period** is the principal quantum number $n$ of the valence shell: carbon (period 2) has its valence electrons in $n = 2$.
- The **group** gives the valence configuration: group 1 ends in $ns^1$, group 2 in $ns^2$, groups 13-18 in $ns^2 np^{1\text{-}6}$. For main-group elements, valence electrons = group number (groups 1-2) or group number − 10 (groups 13-18).
- The six elements of biomolecules are all in periods 1-3 and in the p block, except hydrogen.

**Three trends.**[^c2e65]

| Property | Across a period (left → right) | Down a group | Why |
|---|---|---|---|
| Atomic radius | decreases | increases | across: more protons pull the same shell closer; down: a new, larger shell |
| First ionization energy | increases | decreases | an electron closer to a more effective nuclear charge is harder to remove |
| Usual valence | 1, 2, 3, 4, 3, 2, 1, 0 | constant | number of electrons to lose, share or gain to reach an octet |

The **first ionization energy** is the energy needed to remove the most loosely bound electron from a gaseous atom, $\text{X(g)} \rightarrow \text{X}^{+}\text{(g)} + e^-$.[^c2e65]

**Exceptions with a reason.** Ionization energy dips from Be to B and from N to O. Boron's electron is the first in a 2p orbital, higher in energy than 2s; oxygen's fourth 2p electron is the first paired one, pushed out by repulsion from its partner ([[Electron Configuration]], Hund's rule).[^c2e65]

## Deeper (L2)

- **Effective nuclear charge.** A valence electron feels the nuclear charge $Z$ reduced by the shielding of the electrons between it and the nucleus: $Z_{\text{eff}} = Z - S$. Across a period $Z$ grows faster than shielding, so $Z_{\text{eff}}$ rises; down a group $n$ grows. These two effects explain all three trends.[^c2e65][^5111]
- **Successive ionization energies.** Removing electrons one after another costs more each time, with a large jump when the first core electron is reached.[^c2e65] This is why Na forms Na⁺ (one valence electron) and Mg forms Mg²⁺, and never Na²⁺ or Mg³⁺ in cells: the next electron would come from the $n = 2$ core.
- **Ion sizes.** Cations are smaller than their parent atoms and anions larger, since losing electrons removes repulsion (or a whole shell) and gaining them adds repulsion.[^c2e65] Size and charge together decide which ion fits a binding site or channel.[^berg]
- **Same column is not same behavior.** The first element of a group often stands apart: hydrogen is placed in group 1 for its $1s^1$ configuration but is a nonmetal that forms covalent bonds, unlike the alkali metals.[^c2e2]

## Mathematical representation

Write $\pi(X) = (p, g)$ for the period and group of element $X$. Position predicts atomic radius $r$ only as a **partial order**:

$$r(a) > r(b) \quad \text{predicted if} \quad p_a \ge p_b,\; g_a \le g_b,\; (p_a, g_a) \ne (p_b, g_b),$$

and the reverse order for the first ionization energy. Pairs where one element is lower and further right (N and S) are incomparable: the two trends conflict and only data can decide. For main-group elements, with $v$ valence electrons ($v = g$ if $g \le 2$, $v = g - 10$ if $g \ge 13$), the usual valence is $v$ for $v \le 4$ and $8 - v$ otherwise.

## Computational representation

The table can be computed rather than stored: period and group follow from the aufbau configuration of [[Electron Configuration]].

```python
SYMBOLS = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar "
           "K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr").split()
ORDER = sorted(((n, l) for n in range(1, 8) for l in range(min(n, 4))),
               key=lambda nl: (nl[0] + nl[1], nl[0]))  # aufbau order

def configuration(z: int) -> list[tuple[int, int, int]]:
    conf, left = [], z
    for n, l in ORDER:
        k = min(left, 2 * (2 * l + 1))
        if k == 0:
            break
        conf.append((n, l, k))
        left -= k
    return conf

def position(z: int) -> tuple[int, int, str]:
    """(period, group 1-18, block) from the configuration (no f block)."""
    conf = configuration(z)
    period = max(n for n, _, _ in conf)
    outer = {l: sum(k for n, ll, k in conf if n == period and ll == l) for l in (0, 1)}
    l_last = conf[-1][1]
    if l_last == 0:
        return period, (18 if z == 2 else outer[0]), "s"
    if l_last == 1:
        return period, 10 + outer[0] + outer[1], "p"
    d = sum(k for n, l, k in conf if n == period - 1 and l == 2)
    return period, d + outer[0], "d"

def usual_valence(group: int) -> int | None:
    """Bonds formed, or charge of the usual ion, for main-group elements."""
    if group <= 2:
        return group
    if group >= 13:
        v = group - 10
        return v if v <= 4 else 8 - v
    return None  # transition metals: variable

for sym in ["H", "C", "N", "O", "Na", "Mg", "P", "S", "Cl", "K", "Fe", "Zn"]:
    period, group, block = position(SYMBOLS.index(sym) + 1)
    print(f"{sym:2} period={period} group={group:2} block={block} valence={usual_valence(group)}")
```

```text
H  period=1 group= 1 block=s valence=1
C  period=2 group=14 block=p valence=4
N  period=2 group=15 block=p valence=3
O  period=2 group=16 block=p valence=2
Na period=3 group= 1 block=s valence=1
Mg period=3 group= 2 block=s valence=2
P  period=3 group=15 block=p valence=3
S  period=3 group=16 block=p valence=2
Cl period=3 group=17 block=p valence=1
K  period=4 group= 1 block=s valence=1
Fe period=4 group= 8 block=d valence=None
Zn period=4 group=12 block=d valence=None
```

All 36 elements of periods 1-4 land in the right cell (the figure above was drawn from this function). Chromium and copper get the right group despite their configuration exceptions, because the group counts $d + s$ electrons, which the exceptions do not change.

## Worked example

> [!example] Ranking Na, Mg, K and Cl
> 1. **Positions.** Na (3, 1), Mg (3, 2), Cl (3, 17), K (4, 1).
> 2. **Radius.** K is below Na: K > Na. Along period 3, left is larger: Na > Mg > Cl. K is also lower and further left than Mg and Cl, so the order is total: K > Na > Mg > Cl.
> 3. **First ionization energy.** The reverse: Cl > Mg > Na > K.
> 4. **Usual ions.** Group 1 gives K⁺ and Na⁺, group 2 Mg²⁺, group 17 Cl⁻: the four main ions of cell physiology ([[Ionic Bond]]).

## Common misconceptions

> [!warning] "Atoms get bigger as Z increases"
> Only down a group. Across a period, atoms shrink while $Z$ increases, because the added electrons enter the same shell and are pulled in by a larger nuclear charge.[^c2e65]

> [!warning] "Ionization energy rises smoothly across a period"
> It dips at B (and Al) and at O (and S), where a new subshell starts or electrons begin to pair.[^c2e65]

> [!warning] "Same group and same charge means interchangeable"
> Na⁺ and K⁺ are both +1, yet cells keep them on opposite sides of the membrane and channels select one over the other by size.[^berg]

## Exercises

> [!question] Exercise 1 (L1)
> Give the period, group, number of valence electrons and usual valence of Mg, P and Cl.

> [!success]- Solution
> Mg: period 3, group 2, 2, forms Mg²⁺. P: period 3, group 15, 5, three bonds (more in phosphate, see [[Lewis Structure]]). Cl: period 3, group 17, 7, one bond or Cl⁻.

> [!question] Exercise 2 (L2)
> Using orbital diagrams, explain why the first ionization energy of oxygen is lower than that of nitrogen, although O has more protons.

> [!success]- Solution
> N: $2p^3$, one electron in each 2p orbital. O: $2p^4$, one 2p orbital holds a pair. The paired electron is repelled by its partner, so removing it costs less than removing one of nitrogen's unpaired electrons, despite oxygen's larger nuclear charge. After removal, O⁺ is $2p^3$, the half-filled arrangement.

> [!question] Exercise 3 (L2)
> Why do cells contain Mg²⁺ but never Mg³⁺?

> [!success]- Solution
> Mg is $[\text{Ne}]\,3s^2$. The first two electrons come from the $n = 3$ valence shell; a third would come from the $n = 2$ core, closer to the nucleus and far less shielded, which costs a large jump in ionization energy.

> [!question] Exercise 4 (L3, Python)
> Write `larger_atom(a, b)` implementing the partial order of the Mathematical representation, returning `None` when the trends conflict. Which pairs of H, C, N, O, P, S does it leave undecided?

> [!success]- Solution
> ```python
> from itertools import combinations
>
> def larger_atom(a: str, b: str) -> str | None:
>     """Predict which atom is larger from position alone; None if the trends conflict."""
>     (pa, ga, _), (pb, gb, _) = (position(SYMBOLS.index(x) + 1) for x in (a, b))
>     if (pa, ga) == (pb, gb):
>         return None
>     if pa >= pb and ga <= gb:
>         return a
>     if pb >= pa and gb <= ga:
>         return b
>     return None
>
> life = ["H", "C", "N", "O", "P", "S"]
> print([(a, b) for a, b in combinations(life, 2) if larger_atom(a, b) is None])
> ```
> Output: `[('H', 'C'), ('H', 'N'), ('H', 'O'), ('H', 'P'), ('H', 'S'), ('C', 'P'), ('C', 'S'), ('N', 'S')]`. Hydrogen is incomparable with everything because group 1 puts it "left" while period 1 puts it "up": its placement reflects its configuration, not its size. C/P, C/S and N/S are diagonal pairs. Seven of the 15 pairs are decided, eight need measured radii: trends are a partial order, and turning them into numbers requires data.

## Mastery checklist

- [ ] 1 Recognized: I can find periods, groups and blocks and place C, H, N, O, P, S and the main biological ions.
- [ ] 2 Understood: I can explain the radius and ionization energy trends with shells and effective nuclear charge, including the B and O exceptions.
- [ ] 3 Practiced: I can predict valence, ion charge and size or ionization order from position, and compute positions from $Z$ in Python.
- [ ] 4 Applied: I explained a real biological choice of element (K⁺ versus Na⁺, Se in selenocysteine) from periodic position.
- [ ] 5 Explained: I can explain why trends give only a partial order, and where position-based predictions fail (H, diagonal pairs, transition metals).

## References

[^c2e2]: [[Chemistry 2e (OpenStax)]], ch. 2 "Atoms, Molecules, and Ions" (the periodic table; section not verified).
[^c2e64]: [[Chemistry 2e (OpenStax)]], ch. 6, §6.4 "Electronic Structure of Atoms (Electron Configurations)".
[^c2e65]: [[Chemistry 2e (OpenStax)]], ch. 6, §6.5 "Periodic Variations in Element Properties".
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], Unit I "The Atom" (lecture not verified).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002).
