---
aliases:
  - Back-of-the-Envelope Estimate
  - Fermi Estimate
  - Fermi Problem
  - Biology by the Numbers
  - Estimation d'ordre de grandeur
tags:
  - type/concept
  - domain/physics
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Dimensional Analysis]]"
  - "[[Mole]]"
  - "[[Molar Concentration]]"
  - "[[Logarithm]]"
  - "[[Cell]]"
related:
  - "[[Diffusion]]"
  - "[[Membrane Potential]]"
  - "[[Prokaryote]]"
  - "[[Bacterial Growth]]"
  - "[[Poisson Distribution]]"
  - "[[Variance]]"
  - "[[Ligand Binding]]"
  - "[[FASTQ Format]]"
projects: []
sources:
  - "[[Physical Biology of the Cell (Phillips)]]"
  - "[[NIST Reference on Constants, Units, and Uncertainty]]"
  - "[[NIST Atomic Weights and Isotopic Compositions]]"
  - "[[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Microbiology (OpenStax)]]"
  - "[[Nurk 2022 - The Complete Sequence of a Human Genome]]"
  - "[[Cock 2010 - The Sanger FASTQ File Format]]"
---

# Order-of-Magnitude Estimation

> [!abstract]
> Order-of-magnitude estimation finds a quantity to the nearest power of ten from a few remembered numbers and a simple model, so that you know whether a number about a cell is plausible before you compute it carefully or believe it.

## Definition

An **order-of-magnitude estimate** gives a quantity to the nearest power of ten on a logarithmic scale, that is, within a factor of about three. It is built by writing the quantity as a product of factors (sizes, densities, rates, counts), giving each factor a rounded value and multiplying. *Physical Biology of the Cell* opens with this habit, "biology by the numbers": estimating sizes, copy numbers, concentrations and rates in cells to test whether a model or a claim is quantitatively sensible.[^pboc1]

## Why it matters

- **Reading papers and data.** A reported concentration, copy number or rate can be checked in one line: a protein "at 1 µM" in a bacterium means hundreds of copies, not ten. Factor-of-1000 slips (nM for µM, fL for pL) are common and are caught this way.
- **Single-cell data.** In a bacterium-sized volume, nanomolar species exist as a handful of molecules, so counts per cell are small and noisy ([[Cell]], [[Poisson Distribution]]).
- **Model parameters.** Copy numbers, rate constants and diffusion coefficients in a [[Biochemical Kinetic Model]] or a simulation should be checked against an estimate before fitting anything ([[Diffusion]], [[Diffusion-Limited Reaction]]).
- **Computing scale.** The same reasoning sizes data and compute: how many bytes a sequencing run produces, how long a job will run (Exercise 5).

## Core (L1)

### The procedure

```mermaid
flowchart LR
    Q["Define the quantity<br/>and its unit"] --> F["Split it into factors<br/>you can estimate"]
    F --> R["Round each factor<br/>(1, 3, 10, 30 ...)"]
    R --> M["Multiply:<br/>add the exponents"]
    M --> C{"Units right? Agrees with<br/>an independent estimate?"}
    C -- "no, off by more than 10x" --> F
    C -- "yes" --> U["Use it: compare,<br/>decide, design"]
```

Units are carried through every step ([[Dimensional Analysis]]). Working in µm, seconds and molecules keeps cell-scale numbers close to 1.

### The *E. coli* standard ruler

A few remembered numbers do most of the work. *E. coli* is a rod about 2 µm long and 1 µm in diameter, with a volume of about 1 µm³ (1 fL), the reference volume for bacterial estimates.[^pboc] Its chromosome has 4,639,221 bp, about 5 × 10⁶,[^blattner] which it copies in about 42 minutes;[^os14] under optimal conditions it divides every 20 minutes.[^m91]

Cells are mostly water,[^pboc] so take the density of water, 1 g/cm³. Since 1 µm³ = 10⁻¹² cm³, an *E. coli* cell weighs about **1 pg** (10⁻¹² g).

### 1 nM is about one molecule

The number of molecules $N$ of a species at molar concentration $c$ in a volume $V$ is $N = c\,V\,N_A$, with $N_A = 6.022\,140\,76 \times 10^{23}$ mol⁻¹ ([[Mole]]).[^nist] Converting the volume, $1\ \mu\text{m}^3 = (10^{-5}\ \text{dm})^3 = 10^{-15}$ dm³ $= 10^{-15}$ L. For $c = 1$ nM in one *E. coli*:

$$N = 10^{-9}\ \tfrac{\text{mol}}{\text{L}} \times 10^{-15}\ \text{L} \times 6.0 \times 10^{23}\ \tfrac{1}{\text{mol}} = 0.6.$$

Conversely, one molecule in an *E. coli* cell is a concentration of $1/(V N_A) \approx 1.7$ nM. Hence the rule of thumb: **in an *E. coli* cell, 1 nM is about one molecule.**[^pboc1] The rule belongs to the volume, not to the concentration:

| Concentration | Molecules in 1 µm³ (*E. coli*) | Molecules in 1000 µm³ (an assumed eukaryotic cell) |
|---|---:|---:|
| 1 nM | 0.6 | 600 |
| 1 µM | 600 | 6 × 10⁵ |
| 1 mM | 6 × 10⁵ | 6 × 10⁸ |

A "nanomolar" regulator in a bacterium is therefore a few molecules, whose number varies by chance from cell to cell ([[Cell#Mathematical representation]]).

### A copy number: proteins per cell

Write the quantity as a product, $N_\text{prot} = m_\text{cell} \times f_\text{dry} \times f_\text{prot} / m_\text{protein}$, and round each factor. Rounded inputs: dry mass about 30 % of cell mass, protein about half of the dry mass, a typical protein about 300 amino acids of about 110 Da each.[^pboc]

1. Protein mass per cell: $10^{-12} \times 0.3 \times 0.5 = 1.5 \times 10^{-13}$ g.
2. One protein: $300 \times 110 = 3.3 \times 10^4$ Da, i.e. $3.3 \times 10^4$ g/mol, so $3.3 \times 10^4 / N_A = 5.5 \times 10^{-20}$ g.
3. $N_\text{prot} \approx 1.5 \times 10^{-13} / 5.5 \times 10^{-20} \approx 3 \times 10^6$: **a few million proteins per bacterium.**

Cross-check: spread over the 4,288 protein-coding genes,[^blattner] that is about 600 copies per gene product, or about 1 µM on average, comfortably between the rare (nM) and the abundant.

## Deeper (L2)

### Rounding on a logarithmic scale

Write $x = m \times 10^k$ with $1 \le m < 10$. The order of magnitude is $k$ if $m < \sqrt{10} \approx 3.16$ and $k + 1$ otherwise: rounding is done on $\log_{10} x$ ([[Logarithm]]). So $2.7 \times 10^6$ is of order $10^6$ and $4 \times 10^6$ of order $10^7$. Estimators use 3 as a half step (1, 3, 10, 30...), since $3 \approx \sqrt{10}$.

### Why a chain of rough factors still works

In a product, errors are multiplicative, so they add in log space: $\ln Q = \sum_i \ln x_i$. If factor $i$ is known within a factor $f_i$ (take $\ln x_i$ to have standard deviation $\sigma_i = \ln f_i$) and the errors are independent, the variances add ([[Variance]]):

$$\sigma_{\ln Q}^2 = \sum_i \sigma_i^2 \quad\Longrightarrow\quad f_Q = \exp\Big(\sqrt{\textstyle\sum_i (\ln f_i)^2}\Big).$$

Four factors each uncertain by a factor 2 give $f_Q = 2^{\sqrt{4}} = 4$, not $2^4 = 16$: over- and underestimates partly cancel. The cancellation fails when the errors are correlated, for example when the same biased assumption enters several factors.

### Rates and consistency checks

Rates are amounts divided by times. Replication: $4.64 \times 10^6$ bp copied by two forks in 42 min gives $4.64 \times 10^6 / (2 \times 2520\ \text{s}) \approx 920$ nucleotides per second per fork, of order $10^3$.[^blattner][^os14] The estimate also exposes a paradox: a 20-minute doubling is shorter than a 42-minute replication, so fast-growing cells must start new rounds of replication before the previous ones end ([[Bacterial Growth]]).

**Comparing timescales.** When two processes compete, the ratio of their times says which one limits. A protein crosses *E. coli* by diffusion in about 50 ms ([[Diffusion]]); in a 20-minute generation (1200 s) that is $1200 / 0.05 \approx 2 \times 10^4$ crossings, so for most purposes the cell's interior is well mixed.

## Advanced (L3)

- **Estimates as hypotheses.** An estimate is a model with explicit assumptions. When a measurement disagrees with it by more than a factor of ten, one of the assumptions is wrong, which points to a mechanism worth studying (for instance, a protein diffusing far slower than estimated may be bound to DNA or a membrane).[^pboc1]
- **From counts to noise.** At copy number $\lambda$, a Poisson model gives relative fluctuations $1/\sqrt{\lambda}$ and a probability $e^{-\lambda}$ of zero copies ([[Poisson Distribution]]). At 1 nM in *E. coli* ($\lambda \approx 0.6$), more than half of the cells hold none (Exercise 6): zeros in single-cell data are expected even without any biological difference.
- **Estimates for computation.** Before launching a pipeline, estimate the data volume (Exercise 5), the memory of the index and the run time as (number of items) × (time per item). Two minutes of arithmetic decide whether a job fits on a laptop or needs a cluster.
- **Dimensionless ratios.** Physics turns estimation into model selection by forming ratios of times, lengths or forces; when a ratio is far from 1, one term can be dropped from the model ([[Dimensional Analysis]], [[Reynolds Number]]).

## Mathematical representation

- **Order of magnitude** of $x > 0$: $n(x) = \operatorname{round}(\log_{10} x)$.
- **Product estimate**: $Q = \prod_i x_i$, so $\log_{10} Q = \sum_i \log_{10} x_i$: multiplying numbers is adding exponents.
- **Error propagation in log space**: with $\ln x_i = \ln \hat{x}_i + \varepsilon_i$, independent $\varepsilon_i$ of standard deviation $\sigma_i = \ln f_i$, the combined factor is $f_Q = \exp(\sqrt{\sum_i \sigma_i^2})$.
- **Counting molecules**: $N = c\,V\,N_A$ ($c$ in mol L⁻¹, $V$ in L, $N_A$ in mol⁻¹); the concentration of a single molecule is $c_1 = 1/(V N_A)$.
- **Unit identities**: 1 µm³ = 10⁻¹⁵ L = 1 fL; 1 Da = 1 g/mol per molecule; 1 g/cm³ = 1 pg/µm³.

## Computational representation

Constants live in one place, with their source; every function states its units.

```python
import math

N_A = 6.02214076e23      # mol^-1, Avogadro constant (exact since the 2019 SI)
UM3_IN_L = 1e-15         # 1 µm^3 = 1e-15 L


def molecules(conc_M: float, volume_um3: float) -> float:
    """Expected number of molecules at a molar concentration in a volume given in µm^3."""
    return conc_M * volume_um3 * UM3_IN_L * N_A


def concentration_of_one(volume_um3: float) -> float:
    """Molar concentration that corresponds to a single molecule in the volume."""
    return 1 / (volume_um3 * UM3_IN_L * N_A)


def order_of_magnitude(x: float) -> int:
    """Nearest power of ten, rounding on the logarithmic scale."""
    return round(math.log10(x))


def fermi_product(factors: list[tuple[float, float]]) -> tuple[float, float]:
    """Multiply (estimate, uncertainty factor) pairs; independent errors add in quadrature in log space."""
    value = math.prod(v for v, _ in factors)
    spread = math.exp(math.sqrt(sum(math.log(f) ** 2 for _, f in factors)))
    return value, spread


V_ECOLI = 1.0                                   # µm^3
for label, c in [("1 nM", 1e-9), ("1 µM", 1e-6), ("1 mM", 1e-3)]:
    print(f"{label:>5} -> {molecules(c, V_ECOLI):.2g} molecules per cell")
print(f"1 molecule per cell = {concentration_of_one(V_ECOLI) * 1e9:.2f} nM")

mass_g = V_ECOLI * 1e-12                        # 1 µm^3 at the density of water = 1 pg
protein_g = 300 * 110 / N_A                     # 300 residues x 110 Da, in grams
n, spread = fermi_product([(mass_g, 1.5), (0.3, 1.5), (0.5, 1.5), (1 / protein_g, 2)])
print(f"proteins per cell ~ {n:.1e} (within a factor {spread:.1f}), order 10^{order_of_magnitude(n)}")
```

```text
 1 nM -> 0.6 molecules per cell
 1 µM -> 6e+02 molecules per cell
 1 mM -> 6e+05 molecules per cell
1 molecule per cell = 1.66 nM
proteins per cell ~ 2.7e+06 (within a factor 2.7), order 10^6
```

The uncertainty factors (1.5 and 2) are assumptions, stated so that the reader can change them. Printing two significant digits is deliberate: more would claim a precision the inputs do not have.

## Worked example

> [!example] Is this claim plausible? (invented claim)
> "The repressor is present at 10 copies per *E. coli* cell and binds its operator with $K_d = 1$ µM; it keeps the gene off."
> 1. **Copies to concentration.** One molecule is 1.66 nM, so 10 copies are about 17 nM.
> 2. **Occupancy.** For one site, $K_d = [\text{P}][\text{L}]/[\text{PL}]$ gives the bound fraction $\theta = [\text{L}]/([\text{L}] + K_d)$ ([[Ligand Binding]]). With $[\text{L}] \approx 17$ nM (one site barely depletes the repressor): $\theta = 17/(17 + 1000) \approx 1.7\,\%$.
> 3. **Verdict.** The operator would be free about 98 % of the time: the claim is off by about two orders of magnitude.
> 4. **What would make it consistent.** A $K_d$ near 1 nM gives $\theta = 17/18 \approx 94\,\%$. Either the affinity is much higher than stated or the copy number is much larger; the estimate says which measurement to recheck.

## Common misconceptions

> [!warning] "An estimate is just a guess"
> Each factor is an explicit, checkable assumption, and the result carries an uncertainty. A guess has neither.

> [!warning] "More digits make a better estimate"
> From inputs known within a factor 2, "2.7 × 10⁶ proteins" means "a few million". Writing 2,718,281 suggests a precision the model cannot have.

> [!warning] "1 nM is one molecule in any cell"
> Only in a volume of about 1 µm³. In a 1000 µm³ cell, 1 nM is about 600 molecules; the conversion must be redone for every volume.

> [!warning] "Errors multiply, so a long chain of factors is useless"
> Independent errors add in quadrature in log space: four factors uncertain by 2 give a factor 4, not 16. Only shared (correlated) biases accumulate fully.

## Exercises

> [!question] Exercise 1 (L1)
> How many molecules does an *E. coli* cell contain at 100 nM? What concentration is one molecule in a spherical cell 20 µm in diameter (an assumed size), and how many molecules is 1 nM there?

> [!success]- Solution
> At 0.6 molecules per nM: 100 nM ≈ 60 molecules. Sphere: $V = \frac{4}{3}\pi (10\ \mu\text{m})^3 \approx 4.2 \times 10^3$ µm³, so $c_1 = 1.66\ \text{nM} / 4189 \approx 0.4$ pM, and 1 nM ≈ 2500 molecules. Same concentration, 4000 times more molecules.

> [!question] Exercise 2 (L1)
> Estimate the number of water molecules in an *E. coli* cell, assuming that 70 % of its 1 pg is water. Water has a molar mass of 18.0 g/mol (2 × 1.008 + 15.999).[^nistaw]

> [!success]- Solution
> Water mass $0.7 \times 10^{-12}$ g; moles $0.7 \times 10^{-12} / 18.0 = 3.9 \times 10^{-14}$; molecules $3.9 \times 10^{-14} \times 6.0 \times 10^{23} \approx 2 \times 10^{10}$. Compared with about $3 \times 10^6$ proteins: roughly $10^4$ water molecules per protein.

> [!question] Exercise 3 (L2)
> The *E. coli* chromosome (4,639,221 bp) is copied by two forks in about 42 minutes. Estimate the speed of one fork, then explain what a 20-minute doubling time implies.

> [!success]- Solution
> Each fork copies half the circle: $4{,}639{,}221 / 2 / (42 \times 60\ \text{s}) \approx 920$ nt/s, about $10^3$ nt/s. If the cell divides every 20 minutes but replication takes 42, a round of replication must start before the previous one finishes, so fast-growing cells carry overlapping replication rounds ([[Bacterial Growth]]).

> [!question] Exercise 4 (L2)
> An estimate is a product of four factors, each known within a factor 2. Give the combined uncertainty if the errors are independent, then if all four share the same bias.

> [!success]- Solution
> Independent: $\sigma_{\ln Q} = \sqrt{4} \ln 2 = 2 \ln 2$, so $f_Q = e^{2 \ln 2} = 4$. Same bias: the log-errors add linearly, $4 \ln 2$, so $f_Q = 2^4 = 16$. Checking an estimate by a second, independent route protects against the shared-bias case.

> [!question] Exercise 5 (L3, Python)
> Estimate the uncompressed size of the FASTQ files of a 30× whole-genome sequencing run of a human genome of $3.055 \times 10^9$ bp,[^nurk] with 150-nt reads and 50-character title lines (assumptions). A FASTQ record has a title line, the sequence, a `+` line and a quality string as long as the sequence.[^cock] Compare with the genome stored at 2 bits per base.

> [!success]- Solution
> ```python
> G = 3.055e9                     # bp, human genome (T2T-CHM13)
> coverage, read_len, header = 30, 150, 50   # assumptions: 30x, 150 nt reads, 50-character headers
>
> bases = coverage * G
> reads = bases / read_len
> bytes_per_read = (header + 1) + (read_len + 1) + 2 + (read_len + 1)   # 4 lines with newlines
> print(f"{bases:.1e} bases in {reads:.1e} reads")
> print(f"FASTQ ~ {reads * bytes_per_read / 1e9:.0f} GB uncompressed; genome at 2 bits/base ~ {G * 2 / 8 / 1e6:.0f} MB")
> ```
> Output: `9.2e+10 bases in 6.1e+08 reads`, then `FASTQ ~ 217 GB uncompressed; genome at 2 bits/base ~ 764 MB`. About 2.4 bytes per sequenced base: a few hundred gigabytes per genome, nearly 300 times the packed reference. That number, not the genome size, sizes the storage and transfer of a sequencing project ([[FASTQ Format]]).

> [!question] Exercise 6 (L3)
> A protein is present at an average of 1 nM in *E. coli*. Assuming Poisson-distributed copy numbers, what fraction of cells contain no copy, and what does it imply for a single-cell measurement?

> [!success]- Solution
> $\lambda = 0.6$, so $P(0) = e^{-0.6} \approx 0.55$: more than half of the cells have none, about a third have one ($0.6\,e^{-0.6} \approx 0.33$). Identical cells would look like "expressing" and "non-expressing" subpopulations. Zeros alone are not evidence of two cell states; compare the observed zero fraction with the Poisson prediction first ([[Poisson Distribution]]).

## Mastery checklist

- [ ] 1 Recognized: I can say what an order of magnitude is and quote the *E. coli* reference numbers (1 µm³, 1 pg, 1 nM ≈ 1 molecule, about 5 × 10⁶ bp).
- [ ] 2 Understood: I can derive 1 nM ≈ 1 molecule and explain why a chain of rough factors lands within a factor of a few.
- [ ] 3 Practiced: I can estimate copy numbers, masses, rates and data volumes with units, and code the conversions.
- [ ] 4 Applied: I sanity-checked the numbers of a real paper or dataset (concentrations, copy numbers, read counts, file sizes) before analyzing it.
- [ ] 5 Explained: I can teach estimation as hypothesis testing, including when log-errors do not cancel and why 1 nM is not one molecule in every cell.

## References

[^pboc1]: [[Physical Biology of the Cell (Phillips)]], 2nd ed., ch. 1 "Why: Biology by the Numbers".
[^pboc]: [[Physical Biology of the Cell (Phillips)]], 2nd ed. (2012), estimates for *E. coli*: dimensions and volume, water and dry mass, protein content, typical protein size.
[^nist]: [[NIST Reference on Constants, Units, and Uncertainty]], CODATA: Avogadro constant $6.022\,140\,76 \times 10^{23}$ mol⁻¹, exact since the 2019 SI.
[^nistaw]: [[NIST Atomic Weights and Isotopic Compositions]]: standard atomic weights of hydrogen and oxygen.
[^blattner]: [[Blattner 1997 - The Complete Genome Sequence of Escherichia coli K-12]], *Science* (4,639,221 bp; 4,288 protein-coding genes).
[^os14]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function" (replication of the *E. coli* chromosome from one origin in about 42 minutes).
[^m91]: [[Microbiology (OpenStax)]], section 9.1 "How Microbes Grow" (*E. coli* doubling in about 20 minutes under optimal conditions).
[^nurk]: [[Nurk 2022 - The Complete Sequence of a Human Genome]], *Science* (T2T-CHM13, about $3.055 \times 10^9$ bp).
[^cock]: [[Cock 2010 - The Sanger FASTQ File Format]], *Nucleic Acids Research* (record layout: title line, sequence, `+` line, quality string of the same length).
