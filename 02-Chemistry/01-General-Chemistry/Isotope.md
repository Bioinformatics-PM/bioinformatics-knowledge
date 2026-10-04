---
aliases:
  - Isotopes
  - Isotopic Abundance
  - Isotope Labeling
  - Isotope Envelope
tags:
  - type/concept
  - domain/chemistry
  - domain/physics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Atom]]"
  - "[[Binomial Distribution]]"
related:
  - "[[Monoisotopic Mass]]"
  - "[[Mass Spectrometry]]"
  - "[[Mass Spectrum]]"
  - "[[DNA Replication]]"
  - "[[Radioactive Decay]]"
  - "[[Label-Based Quantification]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[NIST Atomic Weights and Isotopic Compositions]]"
  - "[[Steen 2004 - The ABC's and XYZ's of Peptide Sequencing]]"
  - "[[Meselson 1958 - The Replication of DNA in Escherichia coli]]"
  - "[[Biochemistry (Berg)]]"
---

# Isotope

> [!abstract]
> Isotopes are atoms of one element with different numbers of neutrons: same chemistry, different mass. That is why atomic masses are averages, why a peptide shows a cluster of peaks in a mass spectrum, and why heavy nitrogen could tell old DNA strands from new ones.

## Definition

**Isotopes** are atoms with the same atomic number $Z$ (the same element) but different numbers of neutrons, hence different mass numbers $A$.[^c2e23] Most elements occur as a mixture of isotopes; the mole fraction of each isotope is its **natural abundance** (isotopic composition). The **average atomic mass** (atomic weight) of an element is the abundance-weighted mean of its isotopic masses.[^c2e23][^nist]

## Why it matters

- **Mass spectra are isotope patterns.** A mass spectrometer weighs individual ions, each with a definite isotopic composition, so one peptide gives a cluster of peaks, not one peak at its average mass.[^steen] Picking the monoisotopic peak, reading the charge from the peak spacing and computing the [[Monoisotopic Mass]] are the first steps of every [[Peptide-Spectrum Match|database search]]; confusing monoisotopic and average mass shifts every match (by 0.12 u already for a tripeptide).
- **Labels that do not change chemistry.** A "heavy" molecule behaves like the normal one but can be told apart by mass or density: ¹⁵N density labeling in the Meselson-Stahl experiment,[^meselson] isotope labels in quantitative proteomics ([[Label-Based Quantification]]), radioactive ³²P and ³⁵S tracers ([[Radioactive Decay]]).

## Core (L1)

**Same element, different nucleus.** $^{12}$C and $^{13}$C both have 6 protons and 6 electrons; they differ by one neutron. Chemistry is done by electrons ([[Atom]]), so isotopes of an element have nearly identical chemical behavior; they differ in mass and, for unstable nuclei, in radioactivity.[^c2e23][^c2e]

**The stable isotopes of the elements of life**:[^nist]

| Isotope | Relative atomic mass (u) | Abundance |
|---|---:|---:|
| ¹H / ²H | 1.00782503223 / 2.01410177812 | 0.999885 / 0.000115 |
| ¹²C / ¹³C | 12 (exact) / 13.00335483507 | 0.9893 / 0.0107 |
| ¹⁴N / ¹⁵N | 14.00307400443 / 15.00010889888 | 0.99636 / 0.00364 |
| ¹⁶O / ¹⁷O / ¹⁸O | 15.99491461957 / 16.99913175650 / 17.99915961286 | 0.99757 / 0.00038 / 0.00205 |
| ³¹P | 30.97376199842 | 1 |
| ³²S / ³³S / ³⁴S / ³⁶S | 31.9720711744 / 32.9714589098 / 33.967867004 / 35.96708071 | 0.9499 / 0.0075 / 0.0425 / 0.0001 |

**Why atomic masses are not integers.** Two independent reasons.

1. **Averaging over isotopes.** The atomic weight of carbon mixes ¹²C and ¹³C: $0.9893 \times 12 + 0.0107 \times 13.00335 = 12.0107$ u. This number describes a population; no carbon atom weighs 12.0107 u.
2. **Isotopic masses are not integers either.** Only ¹²C is exactly 12 u, by definition of the unit. A nucleus weighs less than its separated protons and neutrons: the particles of ¹³C add up to $6(1.00727) + 7(1.00866) + 6(0.00055) = 13.1075$ u,[^c2e23] but the atom weighs 13.00335 u. The missing 0.104 u (the **mass defect**) corresponds to the nuclear binding energy, by $E = mc^2$.[^c2e] Hence ¹H = 1.00783 u and ¹⁶O = 15.99491 u.

## Deeper (L2)

### Monoisotopic and average mass

- **Monoisotopic mass**: the sum of the masses of the lightest isotope of each atom (¹²C, ¹H, ¹⁴N, ¹⁶O, ³¹P, ³²S, which for these elements are also the most abundant). It is the mass of a real molecule, the one carrying no heavy isotope, and the first peak of the isotope cluster.[^steen]
- **Average mass**: the sum of average atomic masses: the mean over the whole population of molecules, close to the centroid of the cluster, the relevant value when the isotope peaks are not resolved (large proteins, low resolution).[^steen]
- Water: 18.01056 u (monoisotopic) versus 18.01529 u (average). Residue masses, termini and charges for peptides are covered in [[Monoisotopic Mass]].

### The isotope envelope is a binomial distribution

Each carbon atom is ¹³C independently with probability $p = 0.0107$. In a molecule with $n$ carbon atoms, the number $K$ of ¹³C atoms follows a [[Binomial Distribution]], $K \sim \mathrm{Bin}(n, p)$, and the peak "M+$k$" (molecules carrying $k$ heavy carbons) has relative intensity $P(K = k)$.

![[isotope-envelope-carbon-binomial.svg]]

- $P(K = 0) = (1 - p)^n$ decays geometrically with size: 0.918 for 8 carbons, 0.068 for 250.
- The envelope shifts right and widens: $E[K] = np$, $\mathrm{Var}(K) = np(1 - p)$. M+1 overtakes M+0 from 93 carbons on (Exercise 3); for a large protein the monoisotopic peak is too small to see, so the average mass is what gets measured.
- Carbon dominates M+1 because it is numerous and 1.07% heavy; ¹⁵N (0.364%) and ²H (0.0115%) add less. Sulfur adds a visible M+2 through ³⁴S (4.25%).[^nist]

**Reading the charge from the spacing.** A mass spectrometer measures the mass-to-charge ratio $m/z$.[^steen] Neighboring peaks of a cluster differ by one ¹³C, $\Delta m = 13.00335 - 12 = 1.00335$ u, so they are $1.00335/z$ apart on the $m/z$ axis: 1.003 for a 1+ ion, 0.502 for 2+, 0.334 for 3+. The spacing gives $z$, and $z \times m/z$ gives the mass (the proton correction is in [[Monoisotopic Mass]]).

**¹⁵N density labeling (Meselson-Stahl).** Meselson and Stahl grew *E. coli* with ¹⁵N as the nitrogen source, so the nitrogen atoms of its DNA were ¹⁵N, then shifted the cells to ¹⁴N and separated the DNA by density in a cesium chloride gradient.[^meselson] Each ¹⁵N adds $15.00011 - 14.00307 = 0.99703$ u. Counting nitrogens in the bases (adenine C₅H₅N₅, thymine C₅H₆N₂O₂, guanine C₅H₅N₅O, cytosine C₄H₅N₃O),[^berg] an A·T pair carries 7 N and a G·C pair 8, so fully labeled DNA is about 7.5 u heavier per base pair for the same volume: denser. What the bands proved is in [[DNA Replication]].

## Advanced (L3)

- **The exact envelope is a convolution.** Every element contributes its own isotope distribution, and the distribution of the molecule's mass shifts is the convolution of all atom distributions (a product of generating functions, below). The carbon-only binomial overestimates M+0 (0.918 instead of 0.895 for Gly-Ala-Ser) because ²H, ¹⁵N, ¹⁷O and ¹⁸O also contribute (Exercise 5). Convolving one atom at a time and truncating at M+$k_{\max}$ costs $O(N k_{\max})$ for $N$ atoms.
- **Isotopic fine structure.** "M+1" is not one mass: a ¹³C substitution adds 1.003355 u, a ¹⁵N substitution 0.997035 u, a difference of 0.0063 u. Separating them in a 1,000 u peptide requires a resolving power $m/\Delta m \approx 1000/0.0063 \approx 1.6 \times 10^5$; at lower resolution they merge into one peak at their weighted mean.
- **Abundances vary in nature.** Isotopic compositions are representative values, and IUPAC gives the atomic weight of some elements as an interval: [1.00784, 1.00811] for hydrogen.[^nist] Average masses are uncertain in their last digits; monoisotopic masses are not, one more reason high-resolution proteomics works with monoisotopic masses.

## Mathematical representation

For element $e$ with isotopes $i = 0, 1, \dots$ (lightest first), masses $m_{e,i}$, mass numbers $A_{e,i}$ and abundances $f_{e,i}$ with $\sum_i f_{e,i} = 1$, the average atomic mass is $\bar m_e = \sum_i f_{e,i}\, m_{e,i}$. For a molecule with $n_e$ atoms of each element:

$$M_{\text{mono}} = \sum_e n_e\, m_{e,0}, \qquad M_{\text{avg}} = \sum_e n_e\, \bar m_e, \qquad M_{\text{avg}} - M_{\text{mono}} = \sum_e n_e (\bar m_e - m_{e,0}) \ge 0,$$

a difference linear in molecular size. The distribution of nominal mass shifts is encoded by the generating function

$$G(x) = \prod_e \Big( \sum_i f_{e,i}\, x^{A_{e,i} - A_{e,0}} \Big)^{n_e},$$

whose coefficient of $x^k$ is $P(\text{M}+k)$. Keeping only carbon gives $\big((1-p) + p x\big)^{n_C}$, the binomial.

## Computational representation

Isotope tables are dictionaries of (mass, abundance) pairs, from a cited reference table, never retyped from memory.

```python
from math import comb

# NIST: (relative atomic mass, isotopic composition) of each stable isotope, lightest first.
ISOTOPES = {
    "H": [(1.00782503223, 0.999885), (2.01410177812, 0.000115)],
    "C": [(12.0, 0.9893), (13.00335483507, 0.0107)],
    "N": [(14.00307400443, 0.99636), (15.00010889888, 0.00364)],
    "O": [(15.99491461957, 0.99757), (16.99913175650, 0.00038),
          (17.99915961286, 0.00205)],
    "P": [(30.97376199842, 1.0)],
    "S": [(31.9720711744, 0.9499), (32.9714589098, 0.0075),
          (33.967867004, 0.0425), (35.96708071, 0.0001)],
}

def monoisotopic_mass(formula: dict[str, int]) -> float:
    """Every atom is its lightest isotope (12C, 1H, 14N, 16O, 31P, 32S)."""
    return sum(n * ISOTOPES[el][0][0] for el, n in formula.items())

def average_mass(formula: dict[str, int]) -> float:
    """Every atom contributes its abundance-weighted mean mass."""
    return sum(n * sum(m * f for m, f in ISOTOPES[el]) for el, n in formula.items())

def carbon_envelope(n_carbon: int, p: float = 0.0107, kmax: int = 4) -> list[float]:
    """P(k atoms of 13C among n_carbon), k = 0..kmax: Binomial(n_carbon, p)."""
    return [comb(n_carbon, k) * p**k * (1 - p)**(n_carbon - k) for k in range(kmax + 1)]

gas = {"C": 8, "H": 15, "N": 3, "O": 5}  # Gly-Ala-Ser, C8H15N3O5
print(round(monoisotopic_mass(gas), 5), round(average_mass(gas), 5))
for n in (8, 50, 250):
    print(n, [round(x, 3) for x in carbon_envelope(n)])
```

```text
233.10117 233.22213
8 [0.918, 0.079, 0.003, 0.0, 0.0]
50 [0.584, 0.316, 0.084, 0.014, 0.002]
250 [0.068, 0.184, 0.247, 0.221, 0.148]
```

Average atomic masses recomputed this way are H 1.00794, C 12.01074, N 14.0067, O 15.9994, S 32.06479. Production tools ship their own element tables; check which values (and which abundances) they use before comparing masses at the fourth decimal.

## Worked example

> [!example] Masses and envelope of the tripeptide Gly-Ala-Ser
> 1. **Formula.** Gly (C₂H₅NO₂) + Ala (C₃H₇NO₂) + Ser (C₃H₇NO₃), minus two waters for two [[Peptide Bond|peptide bonds]]: C₈H₁₅N₃O₅.[^berg]
> 2. **Monoisotopic mass.** $8(12) + 15(1.007825) + 3(14.003074) + 5(15.994915) = 96 + 15.117375 + 42.009222 + 79.974573 = 233.10117$ u.
> 3. **Average mass.** $8(12.01074) + 15(1.00794) + 3(14.0067) + 5(15.9994) = 233.2221$ u, 0.121 u heavier.
> 4. **Envelope (carbon only).** $P(\text{M}+0) = 0.9893^8 = 0.918$, $P(\text{M}+1) = 8 \times 0.0107 \times 0.9893^7 = 0.079$: a dominant peak at 233.10, a small one at 234.10. A high-resolution search must use 233.10117; the average 233.22 lies in no peak at all.

## Common misconceptions

> [!warning] "The monoisotopic peak is the tallest peak"
> Only for small molecules. Beyond about 93 carbon atoms M+1 is taller than M+0, and for large proteins the monoisotopic peak can vanish into the noise (Exercise 3).

> [!warning] "A heavy isotope changes the molecule's chemistry"
> Isotopes share their electron configuration, so labeled and unlabeled molecules behave nearly identically.[^c2e23] That is the whole point of isotope labeling: same behavior, different mass.

## Exercises

> [!question] Exercise 1 (L1)
> From the table, compute the average atomic mass of nitrogen. Are ¹⁴C and ¹⁴N isotopes?

> [!success]- Solution
> $0.99636 \times 14.00307 + 0.00364 \times 15.00011 = 14.0067$ u, close to 14 because ¹⁴N dominates. ¹⁴C and ¹⁴N share $A = 14$ but have $Z = 6$ and $Z = 7$: different elements, not isotopes.

> [!question] Exercise 2 (L2)
> The peaks of an isotope cluster are 0.334 apart on the $m/z$ axis and the first peak is at $m/z = 500.25$. Give the charge and the approximate mass of the ion.

> [!success]- Solution
> $z = 1.00335 / 0.334 \approx 3$. Mass of the ion $\approx 3 \times 500.25 = 1500.75$ u. The neutral peptide's mass needs the protons subtracted ([[Monoisotopic Mass]]).

> [!question] Exercise 3 (L2)
> Using the binomial model, find the smallest number of carbon atoms for which the M+1 peak is at least as tall as M+0.

> [!success]- Solution
> $\dfrac{P(K = 1)}{P(K = 0)} = \dfrac{n p (1-p)^{n-1}}{(1-p)^n} = \dfrac{np}{1-p} \ge 1 \iff n \ge \dfrac{1-p}{p} = \dfrac{0.9893}{0.0107} = 92.46$. So $n = 93$ carbon atoms.

> [!question] Exercise 4 (L2)
> A 1,000 bp DNA fragment with 50% GC content is fully labeled with ¹⁵N. By how much does its mass increase?

> [!success]- Solution
> 500 A·T pairs × 7 N + 500 G·C pairs × 8 N = 7,500 nitrogen atoms. $\Delta M = 7500 \times 0.99703 = 7477.8$ u. The volume barely changes, so the density rises: the basis of the separation in [[DNA Replication]].

> [!question] Exercise 5 (L3, Python)
> Compute the full envelope (M+0 to M+4, all elements) by convolution, for Gly-Ala-Ser and for an invented peptide-like formula C₂₅₀H₄₀₀N₇₀O₇₅S₂. Compare with `carbon_envelope`.

> [!success]- Solution
> ```python
> def isotope_envelope(formula: dict[str, int], kmax: int = 4) -> list[float]:
>     """P(M+0..M+kmax): convolve the molecule, one atom at a time."""
>     dist = [1.0]
>     for el, n in formula.items():
>         a0 = round(ISOTOPES[el][0][0])
>         atom = {round(m) - a0: f for m, f in ISOTOPES[el]}  # nominal shift -> abundance
>         for _ in range(n):
>             new = [0.0] * (kmax + 1)
>             for i, a in enumerate(dist):
>                 for shift, f in atom.items():
>                     if i + shift <= kmax:
>                         new[i + shift] += a * f
>             dist = new
>     return dist
>
> for f in ({"C": 8, "H": 15, "N": 3, "O": 5},
>           {"C": 250, "H": 400, "N": 70, "O": 75, "S": 2}):
>     print([round(x, 3) for x in isotope_envelope(f)],
>           [round(x, 3) for x in carbon_envelope(f["C"])])
> ```
> Output (with `ISOTOPES` and `carbon_envelope` from above):
> ```text
> [0.895, 0.091, 0.013, 0.001, 0.0] [0.918, 0.079, 0.003, 0.0, 0.0]
> [0.038, 0.115, 0.184, 0.205, 0.177] [0.068, 0.184, 0.247, 0.221, 0.148]
> ```
> The other elements lower M+0 and shift the envelope right; M+2 of the tripeptide is four times the carbon-only value because of ¹⁸O. Rounding masses to integers bins the fine structure (L3) into nominal peaks.

## Mastery checklist

- [ ] 1 Recognized: I can define an isotope and read the notation ¹³C.
- [ ] 2 Understood: I can give both reasons atomic masses are not integers and tell monoisotopic from average mass.
- [ ] 3 Practiced: I can compute monoisotopic and average masses and a binomial isotope envelope in Python from a cited isotope table.
- [ ] 4 Applied: I read the charge and monoisotopic peak of real peptide clusters in a spectrum and matched them to computed masses.
- [ ] 5 Explained: I can explain the convolution model, isotopic fine structure, abundance variability, and how labeling (¹⁵N, heavy amino acids) exploits "same chemistry, different mass".

## References

[^c2e23]: [[Chemistry 2e (OpenStax)]], ch. 2 "Atoms, Molecules, and Ions", §2.3 "Atomic Structure and Symbolism" (isotopes, average atomic mass; Table 2.1 for particle masses).
[^c2e]: [[Chemistry 2e (OpenStax)]] (nuclear binding energy and mass defect; chapter not verified).
[^nist]: [[NIST Atomic Weights and Isotopic Compositions]], relative atomic masses, isotopic compositions and the standard atomic weight of hydrogen.
[^steen]: [[Steen 2004 - The ABC's and XYZ's of Peptide Sequencing]], *Nature Reviews Molecular Cell Biology*.
[^meselson]: [[Meselson 1958 - The Replication of DNA in Escherichia coli]], *PNAS*.
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002).
