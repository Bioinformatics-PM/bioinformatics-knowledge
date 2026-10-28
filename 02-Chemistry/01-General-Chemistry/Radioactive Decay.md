---
aliases:
  - Radioactivity
  - Radioactive Half-Life
  - Decay Constant
  - Radiolabel
  - Becquerel
  - Curie
  - Désintégration radioactive
tags:
  - type/concept
  - domain/chemistry
  - domain/physics
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Isotope]]"
  - "[[Atom]]"
  - "[[Rate Law]]"
  - "[[Exponential Function]]"
  - "[[Logarithm]]"
related:
  - "[[Exponential Growth]]"
  - "[[Exponential Distribution]]"
  - "[[Poisson Distribution]]"
  - "[[Bacteriophage]]"
  - "[[Sanger Sequencing]]"
  - "[[Gel Electrophoresis]]"
  - "[[Nucleic Acid Hybridization]]"
  - "[[Endomembrane System]]"
  - "[[Label-Based Quantification]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[University Physics (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Molecular Cell Biology (Lodish)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Sanger 1977 - DNA Sequencing with Chain-Terminating Inhibitors]]"
---

# Radioactive Decay

> [!abstract]
> An unstable nucleus has a fixed chance per unit time of decaying, so a radioactive sample shrinks exponentially with a characteristic half-life; counting its decays is how ³²P and ³⁵S labels made DNA and proteins visible in the classic experiments of molecular biology.

## Definition

**Radioactive decay** is the spontaneous transformation of an unstable nucleus into another nuclide, with emission of radiation. It follows **first-order kinetics**: the number of radioactive nuclei falls as $N(t) = N_0 e^{-\lambda t}$, with $\lambda$ the **decay constant**, and each radionuclide has a characteristic, constant **half-life** $t_{1/2}$, the time for half of the atoms of a sample to decay.[^c2e213] The **activity** $A = \lambda N$ is the number of decays per unit time;[^up] it is measured in becquerels (1 Bq = 1 disintegration per second) or curies (1 Ci = 3.7 × 10¹⁰ disintegrations per second).[^c2e216]

## Why it matters

- **Labels that tell molecules apart.** Proteins contain sulfur (in Met and Cys) and nucleic acids contain phosphorus, so ³⁵S marks proteins and ³²P marks DNA and RNA ([[Atom]], [[Isotope]]).[^berg][^lodish] The Hershey-Chase experiment, the first dideoxy sequencing gels, radioactive hybridization probes and pulse-chase experiments all read such labels ([[Bacteriophage]], [[Sanger Sequencing]], [[Nucleic Acid Hybridization]], [[Endomembrane System]]).[^os14][^sanger][^alberts][^lodish4]
- **Planning and correcting measurements.** A ³²P reagent loses half its activity in two weeks: how much to use on a given day, how long a probe stays useful and how to compare samples counted on different days are half-life calculations (Worked example).
- **Counting data.** Decay counts are Poisson-distributed, so their noise is known before the experiment: the simplest model of count data, sequencing reads included ([[Poisson Distribution]]).
- **One equation, many processes.** First-order loss also models mRNA and protein turnover ([[Rate Law]]); radioactive decay is its cleanest physical instance, with a rate constant that nothing in the experiment changes.

## Core (L2)

### What decays, and into what

Isotopes of an element differ only in their number of neutrons ([[Isotope]]), and some combinations of protons and neutrons are unstable. In **β⁻ decay**, a neutron of the nucleus becomes a proton and an electron, the β particle, is emitted: the atomic number rises by one and the mass number stays the same.[^c2e213] The classic labels of molecular biology are β emitters:[^alberts]

| Label | Half-life | Decays to (β⁻ rule) | What it marks |
|---|---|---|---|
| ³²P | 14.3 days | ³²S | DNA, RNA, nucleotides |
| ³⁵S | 87.4 days | ³⁵Cl | proteins, through Met and Cys |
| ³H | 12.3 years | ³He | almost any organic molecule |

³²P-labelled phosphate compounds and ³⁵S-labelled methionine and cysteine are standard reagents.[^lodish]

### First-order decay

Every nucleus has the same probability per unit time, $\lambda$, of decaying, whatever its age, so the population obeys $dN/dt = -\lambda N$, the first-order [[Rate Law]] (solved there by separating variables). Hence:

- $N(t) = N_0 e^{-\lambda t} = N_0\,(1/2)^{t/t_{1/2}}$ with $t_{1/2} = \ln 2/\lambda$: after $n$ half-lives, $(1/2)^n$ is left, whatever $N_0$ (figure);
- the activity $A = \lambda N$ falls with the same half-life,[^up] so a counter reading tracks the number of labelled atoms;
- the mean lifetime of a nucleus is $\tau = 1/\lambda = t_{1/2}/\ln 2$, and individual lifetimes are exponentially distributed ([[Exponential Distribution]]).

![[radioactive-decay-p32-s35-curves.svg]]

### Activity and specific activity

- 1 Bq is one decay per second and 1 Ci = 3.7 × 10¹⁰ Bq,[^c2e216] so 1 mCi = 37 MBq and 1 µCi = 37 kBq.
- **Specific activity** is activity per amount of labelled substance, often in Ci/mmol. For the pure isotope it is $\lambda N_A$, so the shorter the half-life, the higher the specific activity:[^lodish] about 9,100 Ci/mmol for ³²P, 1,500 for ³⁵S and 29 for ³H (code below). A short-lived label gives strong signals from few molecules, and does not keep.

### Bio: labels that changed molecular biology

- **Hershey and Chase (1952).** Phage T2 grown with ³⁵S had labelled protein coats; phage grown with ³²P had labelled DNA. After infection, blending and centrifugation, the ³²P was found with the bacteria and most of the ³⁵S in the supernatant with the empty coats: DNA, not protein, enters the cell and directs new phage, so DNA is the genetic material.[^os14][^griffiths] The design works because each element labels only one class of molecule (Exercise 3).
- **Sequencing gels.** The chain-termination reactions of Sanger, Nicklen and Coulson (1977) were read by autoradiography: radioactively labelled products separated on a gel exposed a film ([[Sanger Sequencing]], [[Gel Electrophoresis]]).[^sanger]
- **Following molecules in time.** In a pulse-chase experiment, cells take up a radioactive precursor for a short pulse, then the label is followed through the cell; this is how the secretory route of proteins was traced ([[Endomembrane System]]).[^lodish4]

## Advanced (L3)

### Counting statistics

A sample of $N$ radioactive atoms counted for $\Delta t \ll t_{1/2}$ yields a number of decays that is binomial with $p = 1 - e^{-\lambda \Delta t}$; with $N$ huge and $p$ tiny, it is Poisson with mean $\mu = Np \approx A\,\Delta t$ ([[Poisson Distribution]]). The variance equals the mean, so a count $n$ has standard deviation $\sqrt n$ and relative precision $1/\sqrt n$: 10,000 counts give 1 %. A background counted separately adds its variance to the net count (Exercise 4). If a detector registers a fraction $\varepsilon$ of decays, its counts per minute (cpm) are $\varepsilon$ times the disintegrations per minute (dpm): compare cpm only between samples counted the same way.

### Estimating a half-life from counts

On a log scale, $\ln n_i = \ln(\varepsilon A_0 \Delta t) - \lambda t_i$ is a straight line ([[Logarithm]], [[Linear Regression]]). Since $\mathrm{Var}(\ln n) \approx 1/n$, each point is weighted by its count; the slope gives $\hat\lambda$, and the delta method gives $\mathrm{SE}(\hat t_{1/2}) = \hat t_{1/2}\,\mathrm{SE}(\hat\lambda)/\hat\lambda$. On simulated counts of a ³²P source (code below), the fit recovers the half-life to 0.5 %.

### Two clocks at once

When the cell also degrades a labelled molecule with rate constant $k$, the two first-order losses add: $k_{\text{obs}} = k + \lambda$. For a protein of 20 h half-life labelled with ³⁵S, the label's decay is negligible (apparent half-life 19.8 h); for an RNA of 3 days labelled with ³²P, ignoring $\lambda$ makes the RNA look 17 % shorter-lived than it is (Exercise 5). Dilution by cell growth adds to the decay constant in the same way ([[Rate Law]]).

## Mathematical representation

- $\dfrac{dN}{dt} = -\lambda N \;\Rightarrow\; N(t) = N_0 e^{-\lambda t}$, $\quad t_{1/2} = \dfrac{\ln 2}{\lambda}$, $\quad \tau = \dfrac{1}{\lambda}$, $\quad A(t) = \lambda N(t) = A_0 e^{-\lambda t}$.
- Specific activity of the pure isotope: $\lambda N_A$ in Bq/mol, or $\lambda N_A / (10^3 \times 3.7 \times 10^{10})$ in Ci/mmol, with $N_A = 6.022 \times 10^{23}$ mol⁻¹.[^c2e31]
- Decay correction to a reference time: $A_{\text{ref}} = A_{\text{measured}}\, e^{\lambda \Delta t} = A_{\text{measured}}\, 2^{\Delta t / t_{1/2}}$.
- Counting: $n \sim \mathrm{Poisson}(\mu)$, $\mathrm{SD}(n) = \sqrt\mu \approx \sqrt n$; net counts $n_g - n_b$ have variance $n_g + n_b$.
- Competing first-order losses: $k_{\text{obs}} = \sum_j k_j$ and $t_{1/2,\text{obs}} = \ln 2 / k_{\text{obs}}$.

## Computational representation

Half-lives, remaining fractions and specific activities with the standard library:

```python
import math

N_A = 6.022e23                      # Avogadro constant, 1/mol
CI = 3.7e10                         # 1 curie in becquerels (decays per second)
DAY = 86400.0
YEAR = 365.25 * DAY
HALF_LIFE = {"P-32": 14.3 * DAY, "S-35": 87.4 * DAY, "H-3": 12.3 * YEAR}   # seconds


def decay_constant(t_half: float) -> float:
    """lambda = ln 2 / t_half (per second)."""
    return math.log(2) / t_half


def fraction_left(t: float, t_half: float) -> float:
    """Fraction of nuclei, and of activity, remaining after time t."""
    return 0.5 ** (t / t_half)


def max_specific_activity(t_half: float) -> float:
    """Ci per mmol of the pure isotope: A = lambda * N with N = N_A / 1000."""
    return decay_constant(t_half) * N_A / 1000 / CI


for iso, th in HALF_LIFE.items():
    print(f"{iso}: lambda = {decay_constant(th):.2e} /s, left after 30 d = "
          f"{fraction_left(30 * DAY, th):.3f}, pure isotope = {max_specific_activity(th):,.0f} Ci/mmol")
```

```text
P-32: lambda = 5.61e-07 /s, left after 30 d = 0.234, pure isotope = 9,131 Ci/mmol
S-35: lambda = 9.18e-08 /s, left after 30 d = 0.788, pure isotope = 1,494 Ci/mmol
H-3: lambda = 1.79e-09 /s, left after 30 d = 0.995, pure isotope = 29 Ci/mmol
```

Simulated counts and a weighted log-linear fit (NumPy draws the Poisson counts):

```python
import numpy as np

t = np.arange(0, 43, 3.0)                          # one 1-min count every 3 days for 6 weeks (invented design)


def fit_half_life(n0: float, t_half: float = 14.3, seed: int = 7):
    """Simulate Poisson counts of a decaying source, fit ln(n) = a - lambda*t weighted by n.
    Returns (counts, estimated half-life, its standard error), in days."""
    n = np.random.default_rng(seed).poisson(n0 * 0.5 ** (t / t_half))
    y, w = np.log(n), n.astype(float)              # Var(ln n) ~ 1/n, so weight each point by n
    t_bar, y_bar = np.average(t, weights=w), np.average(y, weights=w)
    sxx = np.sum(w * (t - t_bar) ** 2)
    slope = np.sum(w * (t - t_bar) * (y - y_bar)) / sxx
    return n, math.log(2) / -slope, math.log(2) / slope ** 2 / math.sqrt(sxx)   # delta method for the SE


n, est, se = fit_half_life(20_000)
print("counts:", n[:5].tolist(), "...", n[-2:].tolist())
print(f"estimated half-life = {est:.2f} +/- {se:.2f} days")
```

```text
counts: [20051, 17405, 14881, 13036, 11118] ... [2999, 2667]
estimated half-life = 14.30 +/- 0.07 days
```

## Worked example

> [!example] Planning a ³²P labelling (invented stock and counts)
> A vial of ³²P-labelled nucleotide is calibrated at 10 mCi/mL on day 0, and each labelling reaction needs 50 µCi.
> 1. **Day 9.** Fraction left $(1/2)^{9/14.3} = 0.646$: 6.46 mCi/mL, so take 7.7 µL instead of 5.0 µL.
> 2. **Day 28.6, two half-lives.** 2.50 mCi/mL: 20.0 µL. Every further half-life doubles the volume.
> 3. **Comparing counts across days.** A blot counted on day 3 gives 12,000 cpm. Corrected to day 0: $12{,}000 \times 2^{3/14.3} = 13{,}878$ cpm, the number to compare with samples counted on day 0.
> 4. **The same plan with ³⁵S.** After 9 days, $(1/2)^{9/87.4} = 0.931$ of the activity remains: a ³⁵S reagent lasts months, a ³²P reagent weeks.

## Common misconceptions

> [!warning] "After two half-lives, everything has decayed"
> Each half-life halves what is left: a quarter remains after two, about 0.1 % after ten. In the model the activity never reaches zero; it falls below what a counter can detect.

> [!warning] "One nucleus decays after one half-life"
> The half-life describes a population. A single nucleus has a constant chance of decaying per unit time and no memory of its age: its lifetime is exponentially distributed, with mean $t_{1/2}/\ln 2$ ([[Exponential Distribution]]).

> [!warning] "Diluting or warming a sample changes its decay rate"
> Dilution changes the counts per microlitre, not the half-life, which is a characteristic constant of each nuclide;[^c2e213] the temperature or the buffer of a biology experiment does not change $\lambda$, unlike the rate constant of a chemical reaction.

## Exercises

> [!question] Exercise 1 (L2)
> What fraction of a ³²P label remains after 28.6 days and after 100 days, and of a ³⁵S label after 100 days?

> [!success]- Solution
> $(1/2)^{t/t_{1/2}}$: 28.6 days is two half-lives of ³²P, 0.25; 100 days is 7.0 half-lives, 0.0079; for ³⁵S, 100/87.4 = 1.14 half-lives, 0.4525 (`fraction_left` gives `0.25`, `0.0079`, `0.4525`).

> [!question] Exercise 2 (L2, Python)
> Convert 1 µCi into Bq and 250 µCi into MBq. How much activity does 1 ng of pure ³²P carry (molar mass about 32 g/mol)?

> [!success]- Solution
> ```python
> atoms = 1e-9 / 32 * N_A                            # 1 ng of pure 32P, molar mass about 32 g/mol
> activity = decay_constant(HALF_LIFE["P-32"]) * atoms
> print(1e-6 * CI, 250e-6 * CI / 1e6, f"{atoms:.2e} atoms, {activity:.2e} Bq = {activity / CI * 1e3:.3f} mCi")
> ```
> Output: `37000.0 9.25 1.88e+13 atoms, 1.06e+07 Bq = 0.285 mCi`. One nanogram of pure ³²P is about 0.3 mCi: a radiolabel is detectable at quantities far below what a balance or an absorbance reading can measure.

> [!question] Exercise 3 (L2)
> In the Hershey-Chase design: (a) if protein were the genetic material, where would each label have ended up? (b) Why would ¹⁴C, or the ¹⁵N used by Meselson and Stahl, not have answered the question?

> [!success]- Solution
> (a) The ³⁵S of the coats would have entered the bacteria, and most ³²P would have stayed outside with the coats. (b) Carbon and nitrogen are in both protein and DNA, so a label on either element marks both molecules and cannot say which one entered. The experiment needs an element unique to each class: S for protein, P for DNA. (¹⁵N is moreover stable, detected by density, not by decay: [[Isotope]].)

> [!question] Exercise 4 (L3)
> A sample gives 100 cpm gross and the background is 50 cpm. Counting each for 25 min, what is the relative standard deviation of the net count? How long must each be counted to reach 2 %?

> [!success]- Solution
> Net $= (100 - 50) \times 25 = 1250$, $\mathrm{SD} = \sqrt{(100 + 50) \times 25} = 61$: 4.9 %. For a time $T$ each, the relative SD is $\sqrt{150T}/(50T) = 0.245/\sqrt T$, which reaches 2 % at $T = 150$ min (net 7500, SD 150). For comparison, 400 cpm with no background reaches 1.0 % in 25 min. Low signals over background are expensive: the required time grows with $1/\text{precision}^2$.

> [!question] Exercise 5 (L3)
> A protein with a 20 h half-life is followed with ³⁵S-methionine, and an RNA with a 3-day half-life with ³²P. What half-life does each experiment measure if the label's own decay is ignored?

> [!success]- Solution
> $t_{\text{obs}} = \ln 2/(\ln 2/t_{\text{bio}} + \ln 2/t_{\text{label}})$: 19.81 h for the protein (87.4 days = 2098 h barely matters), 2.48 days for the RNA, 17 % too short. Correct for the label's decay whenever the experiment lasts a sizeable fraction of its half-life.

> [!question] Exercise 6 (L3, Python)
> With `fit_half_life`, start the source at 2,000 and 200 counts per reading instead of 20,000. How does the standard error of the half-life change, and why?

> [!success]- Solution
> ```python
> for n0 in (20_000, 2_000, 200):
>     _, est, se = fit_half_life(n0)
>     print(n0, round(est, 2), round(se, 2))
> ```
> Output: `20000 14.3 0.07`, `2000 14.3 0.22`, `200 14.31 0.69`. Each tenfold drop in counts multiplies the standard error by about $\sqrt{10} = 3.16$, because Poisson noise on $\ln n$ has variance $1/n$. Ten times fewer counts can be compensated by counting ten times longer.

## Mastery checklist

- [ ] 1 Recognized: I can define half-life, decay constant and activity and name the labels ³²P, ³⁵S and ³H with what they mark.
- [ ] 2 Understood: I can explain why decay is first order, why activity tracks the number of labelled atoms, and the logic of the Hershey-Chase experiment.
- [ ] 3 Practiced: I can compute remaining fractions, decay corrections, specific activities and counting errors, by hand and in Python.
- [ ] 4 Applied: I can plan the use of a real radiolabelled reagent from its calibration date, or estimate a half-life with its uncertainty from counting data.
- [ ] 5 Explained: I can teach counting statistics, the combination of label decay with biological turnover, and why element-specific labels answered questions that others could not.

## References

[^c2e213]: [[Chemistry 2e (OpenStax)]], ch. 21 "Nuclear Chemistry", §21.3 "Radioactive Decay" (types of decay, including β⁻ decay of a neutron into a proton and an electron; first-order kinetics; characteristic, constant half-life; $N = N_0 e^{-\lambda t}$).
[^c2e216]: [[Chemistry 2e (OpenStax)]], ch. 21, §21.6 "Biological Effects of Radiation" (becquerel, 1 Bq = 1 disintegration per second; curie, 1 Ci = 3.7 × 10¹⁰ disintegrations per second).
[^c2e31]: [[Chemistry 2e (OpenStax)]], ch. 3, §3.1 "Formula Mass and the Mole Concept" (Avogadro's number, 6.022 × 10²³).
[^up]: [[University Physics (OpenStax)]], Volume 3, §10.3 "Radioactive Decay" (decay law, decay constant, half-life and activity).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of radioisotopes as tracers (β-emitting isotopes in common use and their half-lives: ³²P 14.3 days, ³⁵S 87.4 days, ³H 12.3 years; autoradiography) and of hybridization with radioactive DNA probes (chapter numbers not verified).
[^lodish]: [[Molecular Cell Biology (Lodish)]], 8th ed., ch. 3, section "Radioisotopes Are Indispensable Tools for Detecting Biological Molecules" (³⁵S-labelled methionine and cysteine to label cellular proteins; phosphate compounds labelled with ³²P; the shorter the half-life, the higher the specific activity). Checked online in the 8th edition; the source note describes the free 4th edition.
[^lodish4]: [[Molecular Cell Biology (Lodish)]], 4th ed. (2000), treatment of protein secretion (pulse-chase labelling with a radioactive amino acid).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002) (sulfur in Cys and Met; phosphorus in the nucleic acid backbone).
[^os14]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function" (the Hershey-Chase experiment of 1952: ³⁵S-labelled protein, ³²P-labelled DNA, blending and centrifugation).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of DNA as the genetic material (the Hershey-Chase experiment).
[^sanger]: [[Sanger 1977 - DNA Sequencing with Chain-Terminating Inhibitors]], *PNAS* 74(12):5463-5467 (radioactively labelled chain-terminated products separated on acrylamide gels and read from autoradiographs).
