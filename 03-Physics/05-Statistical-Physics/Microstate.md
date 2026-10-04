---
aliases:
  - Microscopic State
  - Macrostate
  - Multiplicity
  - Statistical Weight
  - Micro-état
  - Macro-état
tags:
  - type/concept
  - domain/physics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Combinatorics]]"
  - "[[Binomial Coefficient]]"
  - "[[Probability Distribution]]"
  - "[[Thermodynamic System]]"
related:
  - "[[Boltzmann Entropy]]"
  - "[[Boltzmann Distribution]]"
  - "[[Statistical Ensemble]]"
  - "[[Random Walk]]"
  - "[[Freely Jointed Chain]]"
  - "[[Helix-Coil Transition]]"
  - "[[RNA Secondary Structure Prediction]]"
  - "[[Shannon Entropy]]"
projects: []
sources:
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[University Physics (OpenStax)]]"
  - "[[Mathematics for Computer Science (Lehman)]]"
  - "[[MIT 8.592J - Statistical Physics in Biology]]"
  - "[[Zuker 1981 - Optimal Computer Folding of Large RNA Sequences]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
---

# Microstate

> [!abstract]
> A microstate is one complete, detailed configuration of a system (every coin face, every bond direction of a chain); a macrostate is what you measure (how many heads, how far apart the chain ends are), and the number of microstates behind a macrostate, its multiplicity, decides how likely it is.

## Definition

A **microstate** is a complete specification of the microscopic configuration of a system: the state of every one of its parts (the position and velocity of each molecule, the face of each coin, the direction of each bond of a chain). A **macrostate** is specified by a few macroscopic quantities (total energy, number of heads, end-to-end distance). The **multiplicity** $W$ of a macrostate is the number of microstates compatible with it.[^pboc6][^up] For an isolated system at equilibrium, statistical mechanics postulates that all accessible microstates are equally probable (the principle of equal a priori probabilities), so the probability of a macrostate is proportional to its multiplicity.[^pboc]

## Why it matters

- **Every statistical-physics quantity starts from a count.** [[Boltzmann Entropy]] is the logarithm of a multiplicity, and the [[Boltzmann Distribution]] gives each microstate a weight: a wrong count gives a wrong entropy and wrong populations.
- **Biopolymers have astronomically many conformations.** The microstates of a chain are its conformations; how many there are, and how many survive when the chain folds or binds, is the conformational entropy of [[Protein Folding]] and binding.
- **RNA structure prediction works on an ensemble of microstates.** The secondary structures of an RNA are far too many to list (Exercise 5), which is why folding algorithms use [[Dynamic Programming]] over nested structures instead of enumeration,[^zuker] and why statistical physics treats them as an ensemble.[^8592] See [[RNA Secondary Structure Prediction]].
- **Sequences are microstates too.** A DNA sequence of length $L$ is one of $4^L$ microstates; summarizing it by its GC count or a motif score defines a macrostate, and the multiplicities of such summaries are the null models of sequence statistics ([[Combinatorics]], [[GC Content]]).

## Core (L1)

### Coins: the simplest two-state system

Four coins, each H or T: $2^4 = 16$ microstates. Group them by the number of heads $n$, the macrostate:

| Macrostate $n$ | Microstates | $W(n)$ | $P(n)$ |
|---:|---|---:|---:|
| 0 | TTTT | 1 | 1/16 |
| 1 | HTTT, THTT, TTHT, TTTH | 4 | 4/16 |
| 2 | HHTT, HTHT, HTTH, THHT, THTH, TTHH | 6 | 6/16 |
| 3 | THHH, HTHH, HHTH, HHHT | 4 | 4/16 |
| 4 | HHHH | 1 | 1/16 |

$W(n) = \binom{N}{n}$ ([[Binomial Coefficient]]), and the multiplicities add up to $2^N$. Every microstate, HHHH as well as HTHT, has probability 1/16; the macrostate $n = 2$ is the most probable only because it gathers the most microstates.

The same arithmetic describes any set of independent two-state units of equal energy: ion channels open or closed, residues helical or not, sites bound or empty. Unequal energies enter with the [[Boltzmann Distribution]].

### Large numbers make the most probable macrostate overwhelming

With $N = 100$ coins, the single most probable macrostate ($n = 50$) has probability only 0.080, but 96.5 % of all microstates have between 40 and 60 heads (computed below), and the relative width of the peak shrinks as $N$ grows (L2). For the $\sim 10^{23}$ molecules of a macroscopic sample, the macrostate with the largest multiplicity is in practice the only one ever observed: this is the statistical reading of the second law ([[Laws of Thermodynamics]]).[^up] Exercise 3 makes it concrete with a gas gathering in half of its box.

### Bio: the conformations of a chain

![[lattice-chain-microstates.svg]]

Model a polymer as beads on a square lattice joined by bonds of length 1. A microstate is the list of bond directions.

- **Free chain** (any step allowed, even back onto the previous bead): $4^N$ conformations for $N$ bonds.
- **No immediate reversal**: $4 \cdot 3^{N-1}$.
- **Self-avoiding** (no site occupied twice, the lattice version of the fact that two monomers cannot overlap):[^pboc] fewer. With 3 bonds there is no room to collide, so all $4 \cdot 3^2 = 36$ non-reversing walks are self-avoiding; the figure shows their 9 shapes with the first bond fixed, grouped by the macrostate $R^2$, the squared end-to-end distance. From $N = 4$ on, walks that close a square are excluded: 100 instead of 108.

Even this toy chain shows the general pattern: the counts grow exponentially with length (4, 12, 36, 100, ..., 44,100 for $N = 10$), and the extended macrostate ($R^2 = 9$) holds only 4 of the 36 microstates. An unconstrained chain is almost never straight.

## Deeper (L2)

### Multiplicities multiply

If a system consists of two independent parts with $W_A$ and $W_B$ microstates, every pairing is a microstate of the whole: $W = W_A W_B$. Multiplicities of large systems are products of many factors, and only their logarithm is an additive, manageable quantity: this is why entropy is defined as $k_B \ln W$ ([[Boltzmann Entropy]]).

### Stirling's approximation

Multiplicities contain factorials of huge numbers. Stirling's formula, $n! \sim \sqrt{2\pi n}\,(n/e)^n$,[^lehman] gives
$$\ln n! \approx n \ln n - n,$$
with a relative error of 0.9 % at $n = 100$ and $6 \times 10^{-7}$ at $n = 10^6$ (computed below). Applied to the binomial multiplicity, with $x = n/N$:
$$\ln \binom{N}{n} \approx N\,h(x), \qquad h(x) = -x \ln x - (1 - x)\ln(1 - x).$$
$h$ is the [[Shannon Entropy]] of a coin of bias $x$, in nats: counting and information theory meet here. Expanding $h$ to second order around its maximum $h(1/2) = \ln 2$ gives $W(n) \approx W(N/2)\, e^{-2(n - N/2)^2 / N}$, a Gaussian peak of width $\sim \sqrt{N}$, so of relative width $\sim 1/\sqrt{N}$: $10^{-12}$ for $N = 10^{24}$.

### Molecules in a volume

Divide a volume into $\Omega$ cells, each able to hold any number of molecules: $N$ molecules have $W = \Omega^N$ positional microstates. Doubling the volume doubles $\Omega$ and multiplies $W$ by $2^N$, which [[Boltzmann Entropy]] turns into the entropy of expansion of an ideal gas. The cell size is arbitrary, but it cancels in every ratio of multiplicities, which is all that physics uses.

## Advanced (L3)

- **Excluded volume swells chains.** For a free lattice walk, the steps are independent with zero mean, so $\langle R^2 \rangle = N$ exactly (bond length 1): 3.0 for $N = 3$. Forbidding overlaps removes compact walks that fold back on themselves: the 36 self-avoiding 3-bond walks have $\langle R^2 \rangle = 41/9 \approx 4.56$. Ideal-chain models ([[Random Walk]], [[Freely Jointed Chain]]) ignore excluded volume; adding it makes the chain more extended.
- **Conformations grow by a constant factor per monomer.** The ratio of successive self-avoiding counts below falls from 3 to about 2.7 at $N = 10$: each added bond multiplies the number of conformations by a factor smaller than the 3 forward choices. $\ln W$ is then proportional to $N$, so the conformational entropy a chain loses on folding grows with its length ([[Boltzmann Entropy]]).
- **RNA secondary structures grow exponentially.** If any two bases could pair, with hairpin loops of at least 3 bases, a 30-nt RNA would have about $2.4 \times 10^8$ secondary structures and a 100-nt RNA about $6 \times 10^{32}$ (Exercise 5). Real sequences allow fewer pairs, but still exponentially many. Dynamic programming over nested structures finds the minimum free energy structure without listing them,[^zuker] and the same recursions summed with Boltzmann weights give the [[Partition Function]] of the structure ensemble.
- **What counts as a microstate is a modeling choice.** Atoms with continuous coordinates, rotamers, residues on a lattice or whole secondary structures: each level of description has its own microstates. Multiplicities are meaningful as ratios between macrostates **within one model**, never as absolute numbers to compare across models.

## Mathematical representation

- $\mathcal{S}$: the set of microstates; $|\mathcal{S}|$ its size.
- $M : \mathcal{S} \to \mathcal{M}$: the macroscopic observable (number of heads, $R^2$, energy), mapping each microstate to a macrostate $m \in \mathcal{M}$.
- Multiplicity: $W(m) = |M^{-1}(m)| = |\{s \in \mathcal{S} : M(s) = m\}|$, with $\sum_{m \in \mathcal{M}} W(m) = |\mathcal{S}|$.
- Equal a priori probabilities (isolated system): $P(s) = 1/|\mathcal{S}|$ for every $s$, hence $P(m) = W(m)/|\mathcal{S}|$.
- $N$ two-state units, macrostate $n$ = number in state 1: $|\mathcal{S}| = 2^N$, $W(n) = \binom{N}{n}$.
- Lattice chains of $N$ bonds with coordination number $z$ ($z = 4$ on the square lattice): $W_{\text{free}} = z^N$, $W_{\text{non-rev}} = z(z-1)^{N-1}$, and $W_{\text{SAW}} \le z(z-1)^{N-1}$, with equality up to $N = 3$ on the square lattice.

## Computational representation

A microstate is a tuple (coin faces, the list of lattice sites of a chain); a macrostate is a function of that tuple; multiplicities are a `Counter` keyed by macrostate. Exact enumeration works for small systems; large ones need formulas (`math.comb`, and `math.lgamma(n + 1)` for $\ln n!$ without overflow) or sampling.

```python
from collections import Counter
from itertools import product
from math import comb, lgamma, log, pi

# Microstates of N = 4 two-state units (H or T); macrostate = number of heads
N = 4
micro = list(product("HT", repeat=N))
W = Counter(state.count("H") for state in micro)
print(len(micro), dict(sorted(W.items())))      # W(n) = comb(4, n)

# Equal a priori probabilities: P(macrostate) = W / 2^N, here for N = 100
N = 100
print(round(comb(N, 50) / 2**N, 4),
      round(sum(comb(N, n) for n in range(40, 61)) / 2**N, 4))

# Stirling: ln N! ~ N ln N - N, refined by + 0.5 ln(2 pi N)
for n in (10, 100, 1000, 10**6):
    exact = lgamma(n + 1)                       # ln n!
    crude = n * log(n) - n
    print(n, round(exact, 2), round(crude, 2),
          f"rel. error {(exact - crude) / exact:.1e}",
          round(crude + 0.5 * log(2 * pi * n), 2))
```

```text
16 {0: 1, 1: 4, 2: 6, 3: 4, 4: 1}
0.0796 0.9648
10 15.1 13.03 rel. error 1.4e-01 15.1
100 363.74 360.52 rel. error 8.9e-03 363.74
1000 5912.13 5907.76 rel. error 7.4e-04 5912.13
1000000 12815518.38 12815510.56 rel. error 6.1e-07 12815518.38
```

Enumerating lattice chains, with the squared end-to-end distance as macrostate:

```python
from collections import Counter

STEPS = ((1, 0), (-1, 0), (0, 1), (0, -1))     # square lattice, bond length 1


def chain_conformations(n_bonds: int, rule: str) -> Counter:
    """Conformations of an n_bonds chain counted by R^2; rule: 'free', 'nonreversal' or 'saw' (self-avoiding)."""
    by_r2 = Counter()

    def grow(path):
        x, y = path[-1]
        if len(path) == n_bonds + 1:
            by_r2[x * x + y * y] += 1           # macrostate: squared end-to-end distance
            return
        for dx, dy in STEPS:
            site = (x + dx, y + dy)
            if rule == "nonreversal" and len(path) > 1 and site == path[-2]:
                continue
            if rule == "saw" and site in path:
                continue
            grow(path + [site])

    grow([(0, 0)])
    return by_r2


for n in range(1, 11):
    free, nonrev, saw = (sum(chain_conformations(n, r).values())
                         for r in ("free", "nonreversal", "saw"))
    print(n, free, nonrev, saw)
```

```text
1 4 4 4
2 16 12 12
3 64 36 36
4 256 108 100
5 1024 324 284
6 4096 972 780
7 16384 2916 2172
8 65536 8748 5916
9 262144 26244 16268
10 1048576 78732 44100
```

The columns are $N$, $4^N$, $4 \cdot 3^{N-1}$ and the self-avoiding count; `chain_conformations(4, "saw")` returns `{2: 16, 4: 24, 8: 24, 10: 32, 16: 4}`, and the 8 non-reversing walks it excludes all have $R^2 = 0$ (they go around a unit square). Enumeration costs time proportional to the number of conformations, which grows exponentially: it checks formulas for small $N$, it is not a method for real chains.

## Worked example

> [!example] Macrostates of the 3-bond chain (the figure)
> 1. **Count microstates.** First bond: 4 directions. Each later bond: 3 directions (not back). With 3 bonds no overlap is possible, so $W = 4 \times 3 \times 3 = 36$.
> 2. **Fix the first bond along +x** (divide by 4): 9 shapes, named by the turns at bonds 2 and 3 (S straight, L left, R right).
> 3. **Compute $R^2$ for each shape.** SS ends at (3, 0): $R^2 = 9$. LL ends at (0, 1) and RR at (0, −1): $R^2 = 1$. The six others (SL, SR, LS, LR, RS, RL) end at distance $\sqrt{5}$: $R^2 = 5$.
> 4. **Multiplicities** (× 4 orientations): $W(9) = 4$, $W(5) = 24$, $W(1) = 8$; total 36.
> 5. **Probabilities** (equal a priori): $P(R^2 = 5) = 24/36 = 2/3$ and $P(\text{straight}) = 1/9$. Mean: $\langle R^2 \rangle = (9 \cdot 4 + 5 \cdot 24 + 1 \cdot 8)/36 = 164/36 = 4.56$, versus exactly 3 for the free walk (L3).

## Common misconceptions

> [!warning] "The most probable macrostate is made of more probable microstates"
> All microstates of an isolated system are equally probable: HHHH is exactly as likely as HTHT. A macrostate wins only by the **number** of its microstates.

> [!warning] "A chain of N bonds on a lattice with z neighbors has z^N conformations"
> That count includes steps straight back onto the previous bead and walks that cross themselves, which a real chain cannot do. Excluded volume removes a fraction that grows with length: 100 of 108 non-reversing walks survive at $N = 4$, 44,100 of 78,732 at $N = 10$.

> [!warning] "Microstates are always equally probable"
> Only in an isolated system at fixed energy. At constant temperature, microstates are weighted by $e^{-E/k_BT}$; equal weights return only when the energies are equal ([[Boltzmann Distribution]]).

> [!warning] "The number of microstates is a property of the molecule"
> It is a property of the model: discretizing positions and angles more finely changes $W$. Ratios of multiplicities between macrostates of one model, not absolute counts, carry physical meaning.

## Exercises

> [!question] Exercise 1 (L1)
> Five independent two-state ion channels are each open or closed with equal probability. How many microstates are there? Give the multiplicity and the probability of the macrostate "exactly 3 open".

> [!success]- Solution
> $2^5 = 32$ microstates. $W(3) = \binom{5}{3} = 10$ (choose which 3 channels are open), so $P = 10/32 = 0.3125$.

> [!question] Exercise 2 (L1)
> Toy model (invented): each residue of a 10-residue peptide can adopt 3 backbone conformations, one of which is helical. How many microstates does the peptide have? What is the multiplicity of the macrostate "exactly $k$ residues helical"? Compare $k = 10$ with $k = 0$.

> [!success]- Solution
> $3^{10} = 59{,}049$ microstates. Choose the $k$ helical residues, then give each of the $10 - k$ others one of its 2 non-helical conformations: $W(k) = \binom{10}{k}\, 2^{10-k}$. $W(10) = 1$, $W(0) = 2^{10} = 1024$, and the most populated macrostate is $k = 3$ ($W = 15{,}360$). With equal energies a fully helical peptide is rare: helix formation must be paid for by favorable interactions, the starting point of the [[Helix-Coil Transition]].

> [!question] Exercise 3 (L1)
> $N$ gas molecules move independently in a box; each is equally likely to be in the left or the right half. What is the probability that all of them are in the left half, for $N = 10$, $N = 100$ and one mole ($N_A = 6.022\,140\,76 \times 10^{23}$)?[^nist]

> [!success]- Solution
> Counting only which half each molecule occupies, "all left" is 1 microstate out of $2^N$: $P = 2^{-N}$. $N = 10$: $9.8 \times 10^{-4}$; $N = 100$: $7.9 \times 10^{-31}$; one mole: $\log_{10} P = -N_A \log_{10} 2 = -1.81 \times 10^{23}$. A gas never gathers in half its box: not because it is forbidden, but because that macrostate is outnumbered.

> [!question] Exercise 4 (L2)
> Using Stirling's approximation, estimate $\ln \binom{100}{50}$ in two ways: $N h(1/2) = N \ln 2$, and with the correction from the $\sqrt{2\pi n}$ factors, $N \ln 2 - \frac{1}{2}\ln(\pi N/2)$. Compare with the exact value.

> [!success]- Solution
> Exact: $\ln \binom{100}{50} = 66.784$. Leading term: $100 \ln 2 = 69.315$, 4 % too high because it counts all $2^{100}$ microstates as if they sat in the peak. Corrected: $69.315 - \frac{1}{2}\ln(50\pi) = 66.786$. The leading term is proportional to $N$ (extensive), the correction only logarithmic, which is why $N h(x)$ suffices for macroscopic systems.

> [!question] Exercise 5 (L3, Python)
> Count the secondary structures of an RNA of length $n$ when any two bases may pair (an upper bound), with at least 3 unpaired bases in each hairpin loop and no pseudoknots. Recursion: either the last base is unpaired, or it pairs with a base $k$, which splits the segment into the part left of $k$ and the part enclosed by the pair. Find the smallest $n$ with more than $10^6$ and more than $10^9$ structures.

> [!success]- Solution
> ```python
> def count_structures(n: int, min_loop: int = 3) -> list[int]:
>     """S[j] = number of secondary structures of a j-base segment when any two bases
>     may pair (an upper bound for a real sequence), hairpin loops >= min_loop bases."""
>     S = [1] * (n + 1)
>     for j in range(1, n + 1):
>         total = S[j - 1]                                  # base j unpaired
>         for k in range(1, j - min_loop):                  # base j paired with base k
>             total += S[k - 1] * S[j - k - 1]              # left part x enclosed part
>         S[j] = total
>     return S
>
>
> S = count_structures(100)
> print([S[n] for n in (5, 10, 20, 30)])
> print(f"{S[50]:.3e} {S[100]:.3e}", round(S[100] / S[99], 3))
> print(next(n for n in range(101) if S[n] > 10**6), next(n for n in range(101) if S[n] > 10**9))
> ```
> Output: `[2, 65, 106633, 240944076]`, then `1.815e+15 6.320e+32 2.255` and `23 32`. The count grows by a factor of about 2.3 per added base, so 32 nucleotides already exceed $10^9$ structures. Real sequences allow only complementary pairs, which lowers the factor but keeps the growth exponential. Algorithms therefore never list structures: they combine sub-results ([[Dynamic Programming]]) exactly as this counting recursion does, and replacing "count 1 per structure" by "add the Boltzmann weight of each structure" turns it into a partition-function algorithm ([[Partition Function]]).

## Mastery checklist

- [ ] 1 Recognized: I can define microstate, macrostate and multiplicity, with an example of each for coins and for a chain.
- [ ] 2 Understood: I can explain why the macrostate of largest multiplicity dominates for large $N$, and why equal microstate probabilities require an isolated system.
- [ ] 3 Practiced: I can count multiplicities with binomial coefficients and Stirling's approximation, and enumerate lattice conformations in Python.
- [ ] 4 Applied: I can estimate the number of conformations or secondary structures in a biopolymer model and explain why prediction tools use dynamic programming instead of enumeration.
- [ ] 5 Explained: I can teach how counting leads to entropy and the second law, and why multiplicities depend on the level of description.

## References

[^pboc6]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), ch. 6 "Entropy Rules!".
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), treatment of statistical mechanics (equal a priori probabilities, lattice models, Boltzmann weights).
[^up]: [[University Physics (OpenStax)]], Volume 2, ch. 4 "The Second Law of Thermodynamics", section 4.7 "Entropy on a Microscopic Scale".
[^lehman]: [[Mathematics for Computer Science (Lehman)]], 2017 revision, treatment of asymptotics (Stirling's formula).
[^8592]: [[MIT 8.592J - Statistical Physics in Biology]]: biopolymers part (RNA secondary structure treated with statistical physics).
[^zuker]: [[Zuker 1981 - Optimal Computer Folding of Large RNA Sequences]], *Nucleic Acids Research* 9(1):133-148.
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA recommended values (Avogadro constant, exact since the 2019 SI revision).
