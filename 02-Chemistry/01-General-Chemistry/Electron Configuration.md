---
aliases:
  - Configuration électronique
  - Aufbau Principle
  - Valence Electron
tags:
  - type/concept
  - domain/chemistry
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Atom]]"
  - "[[Atomic Orbital]]"
related:
  - "[[Periodic Table]]"
  - "[[Electronegativity]]"
  - "[[Covalent Bond]]"
  - "[[Lewis Structure]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
---

# Electron Configuration

> [!abstract]
> An electron configuration lists which orbitals an atom's electrons occupy, filled from the lowest energy up; its outermost (valence) electrons explain why carbon makes four bonds, nitrogen three and oxygen two.

## Definition

The **electron configuration** of an atom is the distribution of its electrons among its orbitals, written as subshells with superscript electron counts: oxygen is $1s^2\,2s^2\,2p^4$. The ground-state configuration follows three rules:[^c2e64]

1. **Aufbau principle**: electrons fill the lowest-energy orbitals available first.
2. **Pauli exclusion principle**: no two electrons in an atom have the same four quantum numbers, so an orbital holds at most two electrons, with opposite spins.
3. **Hund's rule**: in a set of orbitals of equal energy (such as the three 2p), electrons occupy separate orbitals with parallel spins before pairing.

**Valence electrons** are those in the outermost shell, which take part in bonding; the others are **core electrons**.[^c2e64]

## Why it matters

- **Bonding rules of biomolecules.** Counting valence electrons predicts the number of bonds each atom of a biomolecule forms (C 4, N 3, O 2, H 1): the bookkeeping behind every structural formula of an amino acid or a nucleotide, and behind any program that checks one ([[Lewis Structure]], [[Covalent Bond]]).
- **Lone pairs make hydrogen bonds.** The non-bonding pairs left on N and O are the hydrogen-bond acceptors of proteins and nucleic acids; the polar N-H and O-H bonds are the donors ([[Electronegativity]], [[Hydrogen Bond]]).
- **Ions and metals.** Configurations predict the charges of the ions that cells use (Na⁺, K⁺, Mg²⁺, Cl⁻) and the d-electron counts of metal cofactors such as Fe²⁺ and Zn²⁺ ([[Ionic Bond]], [[Coordination Complex]]).

## Core (L1)

**Filling order.** Subshell energies do not follow $n$ alone: 4s fills before 3d.[^c2e64] Capacities: s holds 2, p 6, d 10, f 14 electrons ($2(2l+1)$, from [[Atomic Orbital]] counting and Pauli).

```mermaid
flowchart LR
    s1["1s"] --> s2["2s"] --> p2["2p"] --> s3["3s"] --> p3["3p"] --> s4["4s"] --> d3["3d"] --> p4["4p"] --> s5["5s"] --> d4["4d"] --> p5["5p"] --> s6["6s"]
```

**Orbital diagrams** (boxes are orbitals, arrows are electrons; Hund's rule spreads the 2p electrons):

```text
    1s     2s     2p                 unpaired   valence e-   usual bonds
C   [↑↓]   [↑↓]   [↑ ][↑ ][  ]          2           4             4  (CH4)
N   [↑↓]   [↑↓]   [↑ ][↑ ][↑ ]          3           5             3  (NH3, +1 lone pair)
O   [↑↓]   [↑↓]   [↑↓][↑ ][↑ ]          2           6             2  (H2O, +2 lone pairs)
```

**Why carbon makes four bonds, nitrogen three, oxygen two.** Atoms of the second period tend to gain, lose or share electrons until they are surrounded by eight valence electrons, the configuration of the next noble gas (the **octet rule**; hydrogen, with only the 1s orbital, completes a "duet" like helium).[^c2e7] Each shared pair (a [[Covalent Bond]]) adds one electron to the count, so:

| Atom | Valence electrons | Bonds to reach 8 | Lone pairs | In biomolecules |
|---|---:|---:|---:|---|
| C | 4 | 4 | 0 | backbone of every organic molecule |
| N | 5 | 3 | 1 | amines, amides, nucleobases |
| O | 6 | 2 | 2 | water, hydroxyls, carbonyls, phosphates |
| H | 1 | 1 (duet) | 0 | terminal atom |

Sulfur, below oxygen, has the same 6 valence electrons ($[\text{Ne}]\,3s^2\,3p^4$) and makes two bonds in cysteine and methionine; phosphorus, below nitrogen, has 5 but in phosphate binds four oxygens (see [[Lewis Structure]] for formal charges).

**Noble-gas shorthand.** Core electrons are abbreviated by the preceding noble gas: P is $[\text{Ne}]\,3s^2\,3p^3$.[^c2e64]

## Deeper (L2)

- **Why 4s before 3d.** In a many-electron atom, an orbital's energy depends on $l$ as well as $n$: s electrons penetrate closer to the nucleus and are less shielded by inner electrons than p or d electrons of the same shell, so 4s ends up below 3d.[^c2e64][^5111] Sorting subshells by $n + l$, then by $n$, reproduces the textbook order (see the code).
- **Ions.** Main-group atoms form ions with noble-gas configurations: Na ($[\text{Ne}]\,3s^1$) loses one electron to Na⁺ ($[\text{Ne}]$), Cl ($[\text{Ne}]\,3s^2 3p^5$) gains one to Cl⁻ ($[\text{Ar}]$). Transition metals lose their 4s electrons before their 3d electrons: Fe is $[\text{Ar}]\,3d^6 4s^2$ and Fe²⁺ is $[\text{Ar}]\,3d^6$.[^c2e64]
- **Exceptions.** A few elements deviate from the aufbau prediction, such as chromium ($[\text{Ar}]\,3d^5 4s^1$) and copper ($[\text{Ar}]\,3d^{10} 4s^1$), where half-filled or filled d subshells are favored.[^c2e64] The rules are a model, not a law.
- **Unpaired electrons.** Hund's rule determines how many electrons are unpaired; atoms and molecules with unpaired electrons are paramagnetic and often reactive (radicals), a theme taken up by [[Molecular Orbital Theory]] and [[Redox Reaction|redox chemistry]].[^c2e]

## Mathematical representation

Let subshells be pairs $(n, l)$ with capacity $c(l) = 2(2l + 1)$, ordered by the key $(n + l,\, n)$. For an atom with $Z$ electrons, the aufbau configuration is the greedy filling $k_j = \min\!\big(c(l_j),\, Z - \sum_{i<j} k_i\big)$ along that order. For a subshell with $k$ electrons in $o = 2l + 1$ orbitals, Hund's rule gives $u = k$ unpaired electrons if $k \le o$, else $u = 2o - k$. For a main-group atom with $v$ valence electrons, the octet rule predicts $b = v$ bonds if $v \le 4$ and $b = 8 - v$ otherwise.

## Computational representation

```python
L = "spdf"
# Subshells in filling order: sort by n + l, then by n (reproduces the textbook order).
ORDER = sorted(((n, l) for n in range(1, 8) for l in range(min(n, 4))),
               key=lambda nl: (nl[0] + nl[1], nl[0]))

def configuration(z: int) -> list[tuple[int, int, int]]:
    """Ground-state (n, l, electrons) by aufbau; Pauli caps a subshell at 2(2l+1)."""
    conf, left = [], z
    for n, l in ORDER:
        if left == 0:
            break
        k = min(left, 2 * (2 * l + 1))
        conf.append((n, l, k))
        left -= k
    return conf

def notation(conf) -> str:
    return " ".join(f"{n}{L[l]}{k}" for n, l, k in conf)

def valence_electrons(conf) -> int:
    """Main-group elements: s + p electrons of the outermost shell."""
    n_max = max(n for n, _, _ in conf)
    return sum(k for n, l, k in conf if n == n_max and l <= 1)

print(" ".join(f"{n}{L[l]}" for n, l in ORDER[:12]))
for sym, z in [("H", 1), ("C", 6), ("N", 7), ("O", 8), ("P", 15), ("S", 16), ("Cl", 17)]:
    conf = configuration(z)
    v = valence_electrons(conf)
    bonds = v if v <= 4 else 8 - v  # octet rule (H: duet)
    print(f"{sym:2} Z={z:2}  {notation(conf):24} valence={v} usual bonds={bonds}")
```

```text
1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s
H  Z= 1  1s1                      valence=1 usual bonds=1
C  Z= 6  1s2 2s2 2p2              valence=4 usual bonds=4
N  Z= 7  1s2 2s2 2p3              valence=5 usual bonds=3
O  Z= 8  1s2 2s2 2p4              valence=6 usual bonds=2
P  Z=15  1s2 2s2 2p6 3s2 3p3      valence=5 usual bonds=3
S  Z=16  1s2 2s2 2p6 3s2 3p4      valence=6 usual bonds=2
Cl Z=17  1s2 2s2 2p6 3s2 3p5      valence=7 usual bonds=1
```

`configuration(24)` returns `... 4s2 3d4` for chromium, not the observed $3d^5 4s^1$: a reminder that the greedy rule is a model.

## Worked example

> [!example] Sulfur, from $Z$ to bonds
> 1. $Z = 16$. Fill: $1s^2$ (2), $2s^2$ (4), $2p^6$ (10), $3s^2$ (12), $3p^4$ (16). Shorthand: $[\text{Ne}]\,3s^2\,3p^4$.
> 2. Valence shell $n = 3$: $2 + 4 = 6$ valence electrons, like oxygen in the same column.
> 3. Hund: four 3p electrons in three orbitals give $\uparrow\downarrow, \uparrow, \uparrow$: 2 unpaired electrons.
> 4. Octet: $8 - 6 = 2$ bonds and 2 lone pairs: the C-S-H of cysteine and the C-S-C of methionine; two cysteine sulfurs can also bond to each other (a disulfide).

## Common misconceptions

> [!warning] "Shells fill strictly in order of n"
> 4s fills before 3d, and 5s before 4d. Orbital energies in many-electron atoms depend on $l$ as well as $n$.[^c2e64]

> [!warning] "Transition metal ions lose their last-filled electrons first"
> 4s fills before 3d, but 4s electrons are also removed first: Fe²⁺ is $[\text{Ar}]\,3d^6$, not $[\text{Ar}]\,3d^4 4s^2$.[^c2e64]

> [!warning] "The octet rule always holds"
> It works very well for C, N and O. Third-period atoms can exceed it (PCl₅ and SF₆ put 10 and 12 electrons around P and S), and odd-electron molecules (radicals) cannot satisfy it ([[Lewis Structure]]).[^c2e7]

## Exercises

> [!question] Exercise 1 (L1)
> Write the full and noble-gas configurations of N, O and P, and give the number of valence electrons of each.

> [!success]- Solution
> N: $1s^2 2s^2 2p^3$ = $[\text{He}]\,2s^2 2p^3$, 5. O: $1s^2 2s^2 2p^4$ = $[\text{He}]\,2s^2 2p^4$, 6. P: $1s^2 2s^2 2p^6 3s^2 3p^3$ = $[\text{Ne}]\,3s^2 3p^3$, 5. N and P share a column, hence the same valence count.

> [!question] Exercise 2 (L2)
> Give the configurations of Mg²⁺ ($Z = 12$), Fe²⁺ and Zn²⁺ ($Z = 30$).

> [!success]- Solution
> Mg: $[\text{Ne}]\,3s^2$, so Mg²⁺ = $[\text{Ne}]$. Fe ($Z = 26$): $[\text{Ar}]\,3d^6 4s^2$, so Fe²⁺ = $[\text{Ar}]\,3d^6$. Zn: $[\text{Ar}]\,3d^{10} 4s^2$, so Zn²⁺ = $[\text{Ar}]\,3d^{10}$, a full d subshell. Both transition metals lose 4s first.

> [!question] Exercise 3 (L3, Python)
> Write `unpaired(z)` applying Hund's rule to every subshell of `configuration(z)`. Print the counts for $Z = 1$ to $10$, then for P, S and Fe.

> [!success]- Solution
> ```python
> def unpaired(z: int) -> int:
>     """Hund's rule: spread the electrons of each subshell over its orbitals."""
>     total = 0
>     for n, l, k in configuration(z):
>         orbitals = 2 * l + 1
>         total += k if k <= orbitals else 2 * orbitals - k
>     return total
>
> print([unpaired(z) for z in range(1, 11)])
> print([unpaired(z) for z in (15, 16, 26)])
> ```
> Output: `[1, 0, 1, 0, 1, 2, 3, 2, 1, 0]` then `[3, 2, 4]`. Across period 2 the count rises to 3 at nitrogen (half-filled 2p) and falls back to 0 at neon. Fe has 4 unpaired 3d electrons in the free atom.

## Mastery checklist

- [ ] 1 Recognized: I can read $1s^2 2s^2 2p^4$ and name the aufbau, Pauli and Hund rules.
- [ ] 2 Understood: I can explain the filling order, valence versus core electrons and the octet rule.
- [ ] 3 Practiced: I can write configurations, orbital diagrams and ion configurations, and generate them in Python.
- [ ] 4 Applied: I predicted bond counts and lone pairs for the atoms of a real amino acid or nucleobase and checked them against its structure.
- [ ] 5 Explained: I can explain why 4s fills before 3d, the exceptions (Cr, Cu), and where the octet rule fails (P, S, radicals).

## References

[^c2e64]: [[Chemistry 2e (OpenStax)]], ch. 6, §6.4 "Electronic Structure of Atoms (Electron Configurations)".
[^c2e7]: [[Chemistry 2e (OpenStax)]], ch. 7 "Chemical Bonding and Molecular Geometry".
[^c2e]: [[Chemistry 2e (OpenStax)]] (paramagnetism and radicals; chapter not verified).
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], Unit I "The Atom" (lecture not verified).
