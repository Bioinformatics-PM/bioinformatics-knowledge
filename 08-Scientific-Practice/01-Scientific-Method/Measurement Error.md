---
aliases:
  - Random Error
  - Systematic Error
  - Accuracy and Precision
  - Measurement Bias
  - Erreur de mesure
tags:
  - type/concept
  - domain/scientific-practice
  - domain/statistics
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Empirical Evidence]]"
  - "[[Measure of Dispersion]]"
related:
  - "[[Controlled Experiment]]"
  - "[[Confirmation Bias]]"
  - "[[Linear Approximation]]"
  - "[[Batch Effect]]"
  - "[[Phred Quality Score]]"
projects:
  - "[[10-genomic-pipeline]]"
  - "[[05-sequence-search]]"
sources:
  - "[[International Vocabulary of Metrology]]"
  - "[[Leek 2010 - Tackling the Widespread and Critical Impact of Batch Effects]]"
  - "[[Cock 2010 - The Sanger FASTQ File Format]]"
  - "[[Nakamura 2011 - Sequence-Specific Error Profile of Illumina Sequencers]]"
  - "[[Li 2014 - System Wide Analyses Have Underestimated Protein Abundances]]"
  - "[[Reproducibility and Replicability in Science (National Academies)]]"
---

# Measurement Error

> [!abstract]
> Every measured value misses the true value: a **random** part that changes unpredictably between replicates and averages out, and a **systematic** part that repeats in every replicate and does not.

## Definition

The **measurement error** of a value is the measured value minus a reference (true) value. It has a **systematic** component, which stays constant or varies predictably across replicate measurements, and a **random** component, which varies unpredictably; an estimate of the systematic error is the **measurement bias**.[^vim] Three qualities follow:[^vim]

- **Trueness**: closeness of the average of (infinitely many) replicate values to the reference value. It reflects systematic error only.
- **Precision**: closeness of agreement among replicate values under stated conditions, usually expressed as a standard deviation ([[Measure of Dispersion]]). It reflects random error only, and depends on the conditions: **repeatability** (same procedure, operator, instrument and place, short interval) or **reproducibility** (different laboratories, operators or instruments). Computational science uses "reproducibility" in another sense, the same results from the same data and code ([[Reproducibility]]).[^nasem]
- **Accuracy**: closeness of a single measured value to the true value, which needs both. "Error" is not a mistake but the unavoidable deviation of any measurement; a swapped tube is a blunder to fix, not an error to model.

## Why it matters

- **Replication fixes half the problem.** Averaging $n$ replicates divides random error by $\sqrt{n}$ and leaves systematic error intact (Deeper). More reads, cells or samples never correct a biased protocol.
- **Batch effects are systematic errors.** Samples processed on the same day, with the same reagent lot or by the same person share technical deviations; when batches line up with biological groups, technology is read as biology.[^leek] See [[Batch Effect]].
- **Sequencing errors come in both kinds.** A Phred quality $Q = -10\log_{10} p$ states the estimated probability $p$ that a base call is wrong;[^cock] independent errors of that kind are outvoted in a deep pileup. Illumina reads also carry sequence-specific errors, triggered mainly by GGC motifs and inverted repeats, that recur at the same sequence positions across many reads:[^nakamura] depth does not remove them (Exercise 3).

## Core (L1)

![[measurement-accuracy-precision-targets.svg]]

One reading is modelled as $x_i = \mu + b + \varepsilon_i$: true value $\mu$, systematic error $b$ (the same for every replicate) and random error $\varepsilon_i$ (mean 0, standard deviation $\sigma$). In the figure, $b$ moves the centre of the cloud and $\sigma$ sets its spread.

| | Random error | Systematic error |
|---|---|---|
| Over replicates | changes sign and size unpredictably | same direction every time, constant or drifting |
| Reduced by | more replicates, a less noisy instrument | calibration, blank subtraction, controls, randomized design |
| Lab examples (invented) | pipetting scatter, reading-to-reading noise | uncalibrated pipette, untared balance, unsubtracted blank |
| Sequencing examples | independent base-call errors[^cock] | sequence-specific miscalls[^nakamura], batch effects[^leek] |

Two rules follow. **Replicates never reveal systematic error**: a biased instrument repeats its bias perfectly, so only something independent (a standard, another method) exposes it. **A precise result can be wrong**, and an imprecise one can be right on average.

## Deeper (L2)

**The error floor.** The mean of $n$ independent replicates has expectation $\mu + b$ and variance $\sigma^2/n$ ([[Sampling Distribution]]), so its root mean squared error is
$$\mathrm{RMSE}(\bar{x}) = \sqrt{b^2 + \sigma^2/n} \;\xrightarrow[n \to \infty]{}\; |b|.$$
Once $\sigma/\sqrt{n} \ll |b|$, more replicates buy nothing. This is the bias-variance split of an [[Estimator]], applied to an instrument.

**Constant or proportional bias.** An unsubtracted blank adds the same offset to every reading; a miscalibrated pipette multiplies every reading by the same factor. Two reference standards at different levels tell them apart (Worked example). A proportional bias cancels in a ratio of two readings made the same way, one reason relative measures such as fold changes are robust (Exercise 2).

**Propagation.** For $y = f(x_1, \dots, x_k)$ with independent random errors $\sigma_j$, linearizing $f$ and adding the variances of independent terms ([[Linear Approximation]], [[Variance]]) gives
$$\sigma_y^2 \approx \sum_{j=1}^{k} \left(\frac{\partial f}{\partial x_j}\right)^2 \sigma_j^2 .$$
For a product or a ratio, relative errors add in quadrature. Systematic errors do not average: they propagate with their sign and may add up or cancel.

## Advanced (L3)

- **Batch effects and design.** If batches are balanced across conditions, a batch effect adds variation that can be modelled; if batch and condition are confounded, no correction can separate them.[^leek] Randomizing the processing order turns a would-be systematic error into random error with respect to the comparison ([[Randomization]], [[Confounding]], [[Experimental Design]]).
- **Context-dependent errors.** Sequence-specific errors also make coverage uneven and bias counting methods such as RNA-seq and ChIP-seq.[^nakamura] Because a Phred score is an estimate, its calibration is itself measurable: bin calls by reported quality and count mismatches to a trusted reference; correcting systematic miscalibration is [[Base Quality Score Recalibration]].
- **Errors in variables.** With independent random error on both $x$ and $y$, $\mathrm{Cov}$ is unchanged but each variance grows, so $r_{\text{obs}} = r_{\text{true}}\sqrt{R_x R_y}$, where $R = \mathrm{Var}(\text{true})/\mathrm{Var}(\text{observed})$ is a variable's reliability. Noise thus weakens correlations; a reanalysis argued that this is why mRNA-protein correlations had been underestimated.[^li2014]

## Mathematical representation

With the model of Core: error $e_i = x_i - \mu = b + \varepsilon_i$, bias $b = E[x] - \mu$, imprecision $\sigma^2 = \mathrm{Var}(x)$; since $E[\varepsilon] = 0$, $\mathrm{MSE} = E[(b + \varepsilon)^2] = b^2 + 2b\,E[\varepsilon] + E[\varepsilon^2] = b^2 + \sigma^2$. An observed bias $\bar{x} - \mu_{\text{ref}}$ is compared with its standard error $s/\sqrt{n}$: a ratio far above 2 means the offset is not random scatter ([[Student's t-Test]]).

## Computational representation

```python
import random
import statistics as st

TRUE, rng = 50.0, random.Random(1)  # reference value, e.g. a DNA standard in ng/uL (invented)

def readings(bias: float, sd: float, n: int) -> list[float]:
    """n replicate readings = true value + systematic error + random error."""
    return [TRUE + bias + rng.gauss(0, sd) for _ in range(n)]

def rmse(values: list[float]) -> float:
    return st.fmean((v - TRUE) ** 2 for v in values) ** 0.5

for b, sd in [(0.0, 0.3), (2.0, 0.3), (0.0, 2.0), (2.0, 2.0)]:  # the four targets
    x = readings(b, sd, 10_000)
    print(f"b={b} sd={sd}: bias {st.fmean(x) - TRUE:+.2f}  sd {st.stdev(x):.2f}  rmse {rmse(x):.2f}")
for n in (1, 4, 16, 64):  # averaging n replicates shrinks the random part only
    means = [st.fmean(readings(2.0, 2.0, n)) for _ in range(5_000)]
    print(f"n={n:2d}  rmse of the mean {rmse(means):.2f}  theory {(4 + 4 / n) ** 0.5:.2f}")
```

```text
b=0.0 sd=0.3: bias +0.00  sd 0.30  rmse 0.30
b=2.0 sd=0.3: bias +2.00  sd 0.30  rmse 2.02
b=0.0 sd=2.0: bias +0.03  sd 1.99  rmse 1.99
b=2.0 sd=2.0: bias +2.03  sd 2.02  rmse 2.86
n= 1  rmse of the mean 2.81  theory 2.83
n= 4  rmse of the mean 2.24  theory 2.24
n=16  rmse of the mean 2.07  theory 2.06
n=64  rmse of the mean 2.01  theory 2.02
```

The four rows are the four targets of the figure; the last block shows the floor at $|b| = 2$.

## Worked example

> [!example] Checking a spectrophotometer with a DNA standard (invented data)
> A standard certified at 50.0 ng/µL is read five times: 52.1, 51.6, 52.4, 51.9, 52.0.
> 1. **Precision and trueness**: $s = 0.29$ ng/µL (about 0.6 %), precise; $\bar{x} = 52.0$, so the estimated bias is $+2.0$ ng/µL (+4 %).
> 2. **Real or scatter?** Standard error $0.29/\sqrt{5} = 0.13$; the bias is about 15 standard errors: systematic, not chance.
> 3. **Constant or proportional?** Read a second standard, say 10.0 ng/µL. About 12.0 means a constant offset (blank problem); about 10.4 means a proportional one (calibration factor 50/52).
> 4. **Act**: fix the cause or correct the readings, and record the check. Averaging more readings would never have found this.

## Common misconceptions

> [!warning] "Precise means accurate"
> Tight replicates measure precision only. The biased-precise instrument above agrees with itself to 0.6 % and is 4 % wrong every time.

> [!warning] "My technical replicates show the error of the experiment"
> They show only the variation that differs between them. Sequencing one library on two lanes shares every bias of that library's preparation; [[Biological Replicate|biological replicates]] processed in different batches expose more of the real error ([[Technical Replicate]]).

## Exercises

> [!question] Exercise 1 (L1)
> Classify each error as random or systematic, and name a remedy: (a) a balance always reads 0.12 g high; (b) the scatter of ten pipetted volumes; (c) all treated samples sequenced on one flow cell and all controls on another; (d) a plate reader warms up and drifts upward during a 40-minute read.

> [!success]- Solution
> (a) Systematic, constant offset: tare or calibrate. (b) Random: replicate and average, or use a better pipette. (c) Systematic and confounded with the treatment, a batch effect that analysis cannot undo: balance the groups across flow cells.[^leek] (d) Systematic, varying predictably with time: randomize the well order so the drift becomes random with respect to the groups, or correct it with control wells spread over the plate.

> [!question] Exercise 2 (L2)
> A ratio $R = x/y$ is computed from two independent readings with relative random errors of 4 % and 3 %. What is the relative error of $R$? What happens to a +5 % calibration bias present in both readings?

> [!success]- Solution
> $\partial R/\partial x = 1/y$ and $\partial R/\partial y = -x/y^2$, so $(\sigma_R/R)^2 = 0.04^2 + 0.03^2$ and $\sigma_R/R = 5$ %. The shared bias cancels: $1.05x/(1.05y) = x/y$. Random errors never cancel this way; they add in quadrature.

> [!question] Exercise 3 (L3, Python)
> A caller flags a variant when at least 15 % of the reads, and at least 3 reads, show the same wrong base. Compare a site with only random errors (rate 0.01, spread over 3 bases) and a site with a sequence-specific miscall towards one base in 20 % of reads (rates invented), at depths 10 to 300.

> [!success]- Solution
> ```python
> from math import comb, ceil
>
> def p_flag(depth: int, rate: float, frac: float = 0.15, min_reads: int = 3) -> float:
>     """P(at least max(min_reads, frac*depth) reads show one given wrong base)."""
>     k_min = max(min_reads, ceil(frac * depth))
>     return sum(comb(depth, k) * rate**k * (1 - rate) ** (depth - k)
>                for k in range(k_min, depth + 1))
>
> for d in (10, 30, 100, 300):
>     print(f"depth {d:3d}  random {p_flag(d, 0.01 / 3):.1e}  systematic {p_flag(d, 0.2 + 0.01 / 3):.3f}")
> ```
> ```text
> depth  10  random 4.4e-06  systematic 0.332
> depth  30  random 5.5e-08  systematic 0.759
> depth 100  random 1.4e-20  systematic 0.931
> depth 300  random 1.1e-58  systematic 0.993
> ```
> Depth crushes random errors but makes the systematic one more convincing, since its read fraction converges to 20 %, like a real low-frequency variant. Only knowledge of the error's context (motif, strand, position in read) can separate the two.

## Mastery checklist

- [ ] 1 Recognized: I can define random and systematic error, trueness, precision and accuracy.
- [ ] 2 Understood: I can explain why replicates reveal random but not systematic error, and read the four-target figure.
- [ ] 3 Practiced: I can compute bias, standard deviation, RMSE and the error floor, and propagate errors through a ratio.
- [ ] 4 Applied: in [[10-genomic-pipeline]], I separated random sequencing errors from context-specific ones, or checked base-quality calibration against a reference.
- [ ] 5 Explained: I can teach batch effects as confounded systematic error, the attenuation of correlations by noise, and why randomization converts systematic into random error.

## References

[^vim]: [[International Vocabulary of Metrology]], JCGM 200:2012 (VIM3), clause 2, entries "measurement error", "systematic measurement error", "random measurement error", "measurement bias", "measurement accuracy", "measurement trueness" (2.14), "measurement precision", "repeatability condition of measurement" and "reproducibility condition of measurement".
[^leek]: [[Leek 2010 - Tackling the Widespread and Critical Impact of Batch Effects]], Leek JT et al., *Nature Reviews Genetics* 11(10):733-739.
[^cock]: [[Cock 2010 - The Sanger FASTQ File Format]], *Nucleic Acids Research* 38(6):1767-1771: Phred quality $Q = -10 \log_{10} p$.
[^nakamura]: [[Nakamura 2011 - Sequence-Specific Error Profile of Illumina Sequencers]], *Nucleic Acids Research* 39:e90 (triggers, mechanism and coverage bias).
[^nasem]: [[Reproducibility and Replicability in Science (National Academies)]], definitions of reproducibility and replicability.
[^li2014]: [[Li 2014 - System Wide Analyses Have Underestimated Protein Abundances]], Li JJ, Bickel PJ, Biggin MD, *PeerJ* 2:e270.
