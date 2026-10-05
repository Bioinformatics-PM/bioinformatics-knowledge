---
aliases:
  - Henderson-Hasselbalch
  - HH Equation
  - Protonated Fraction
  - Équation de Henderson-Hasselbalch
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[pH]]"
  - "[[Acid-Base Equilibrium]]"
  - "[[Chemical Equilibrium]]"
  - "[[Logarithm]]"
related:
  - "[[Buffer Solution]]"
  - "[[Amino Acid]]"
  - "[[Isoelectric Point]]"
  - "[[Enzyme Catalysis]]"
  - "[[Partition Coefficient]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Biochemistry (Berg)]]"
---

# Henderson-Hasselbalch Equation

> [!abstract]
> The Henderson-Hasselbalch equation tells you, from the pH and the pKa alone, what fraction of an acidic or basic group carries its proton, and therefore its charge.

## Definition

For a weak acid $\mathrm{HA} \rightleftharpoons \mathrm{H^+} + \mathrm{A^-}$ with acid dissociation constant $K_a$, the **Henderson-Hasselbalch equation** is the logarithmic form of the equilibrium expression:[^chem14][^leh]

$$\mathrm{pH} = \mathrm{p}K_a + \log_{10}\frac{[\mathrm{A^-}]}{[\mathrm{HA}]}.$$

When $\mathrm{pH} = \mathrm{p}K_a$, the acid and its conjugate base are equally abundant: the pKa is the pH at which the group is half dissociated.[^leh]

## Why it matters

- **Charge from sequence.** Summing the charged fractions of all ionizable groups gives a protein's net charge at any pH and its [[Isoelectric Point]], standard sequence statistics; the pKa table lives in [[Amino Acid]].
- **Catalysis and binding.** Whether an active-site histidine can accept or give a proton, or whether a ligand is charged when it is docked, is a protonated-fraction question ([[Enzyme Catalysis]], [[Molecular Docking]]).
- **Buffers.** The same equation gives the acid/base ratio needed to make a [[Buffer Solution]] at a target pH.
- **Neutral fraction.** The uncharged fraction of a drug-like molecule, which this equation gives, enters estimates of how it distributes between water and membranes ([[Partition Coefficient]]).

## Core (L1)

**Derivation.** Start from $K_a = [\mathrm{H^+}][\mathrm{A^-}]/[\mathrm{HA}]$ ([[Acid-Base Equilibrium]]), take $-\log_{10}$ of both sides and use $\mathrm{pH} = -\log_{10}[\mathrm{H^+}]$ and $\mathrm{p}K_a = -\log_{10} K_a$ ([[pH]], [[Logarithm]]):

$$-\log_{10} K_a = -\log_{10}[\mathrm{H^+}] - \log_{10}\frac{[\mathrm{A^-}]}{[\mathrm{HA}]} \;\Rightarrow\; \mathrm{pH} = \mathrm{p}K_a + \log_{10}\frac{[\mathrm{A^-}]}{[\mathrm{HA}]}.$$

**Reading it.** Each pH unit away from the pKa changes the ratio $[\mathrm{A^-}]/[\mathrm{HA}]$ tenfold. Two units below the pKa the group is 99 % protonated, two units above it 99 % deprotonated:

| $\mathrm{pH} - \mathrm{p}K_a$ | −2 | −1 | 0 | +1 | +2 |
|---|---:|---:|---:|---:|---:|
| fraction protonated | 0.990 | 0.909 | 0.500 | 0.091 | 0.010 |

**Protonated fraction.** Solving for the fraction $\theta$ of molecules in the protonated form, $\theta = [\mathrm{HA}]/([\mathrm{HA}] + [\mathrm{A^-}])$:

$$\theta = \frac{1}{1 + 10^{\,\mathrm{pH} - \mathrm{p}K_a}}.$$

The same formula serves acids and bases, as long as "HA" means the protonated form: for a carboxyl group the protonated form is neutral, so its mean charge is $-(1 - \theta)$; for an amino or imidazole group the protonated form is positive, so its mean charge is $+\theta$.

![[henderson-hasselbalch-protonated-fraction.svg]]

**Bio: histidine near pH 7.** With a typical side-chain pKa of 6.0 in proteins,[^berg] histidine is 50 % protonated at pH 6.0, 24 % at 6.5, 9.1 % at 7.0 and 3.8 % at 7.4. Aspartate (pKa 4.1) is fully negative and lysine (pKa 10.8) fully positive over the same range.[^berg] Histidine is the side chain whose charge changes appreciably across physiological pH, which is why it often shuttles protons in active sites.[^berg]

## Deeper (L2)

**The pKa belongs to a group in a place.** Tabulated pKa values are typical; nearby charges, hydrogen bonds or a nonpolar pocket shift them inside a folded protein.[^berg] The equation is unchanged, but its input moves, and near pH 7 a histidine is very sensitive to that shift:

| His pKa | 6.0 | 6.5 | 7.0 |
|---|---:|---:|---:|
| fraction protonated at pH 7.0 | 0.091 | 0.240 | 0.500 |

A half-unit shift more than doubles the charge, so a charge or pI computed from a sequence is an estimate that depends on the pKa table chosen ([[Isoelectric Point]]).

**Concentrations at equilibrium, not amounts added.** The equation is exact for equilibrium concentrations. Using the amounts of acid and salt weighed into a buffer instead is an approximation: it assumes that the acid's own dissociation, and water's, change those amounts negligibly, which fails for very dilute solutions or for acids that are not weak.

**Many groups.** A protein or a polyprotic acid (phosphoric acid has three dissociable protons) carries several groups. Treating each one independently with its own pKa and summing their mean charges is the standard model, and also its main limitation: groups close in space influence each other's protonation.

## Mathematical representation

With $x = \mathrm{pH} - \mathrm{p}K_a$:

$$\theta(x) = \frac{1}{1 + 10^{x}} = \frac{1}{1 + e^{x \ln 10}},$$

a logistic (sigmoid) curve in pH, centred at the pKa, symmetric about $\theta = 1/2$, with slope $d\theta/d\mathrm{pH} = -\ln 10\,\theta(1-\theta)$, steepest at the pKa ($-\ln 10/4 \approx -0.576$ per pH unit). Its inverse and its linear form are

$$\mathrm{pH} = \mathrm{p}K_a + \log_{10}\frac{1-\theta}{\theta}, \qquad \log_{10}\frac{\theta}{1-\theta} = \mathrm{p}K_a - \mathrm{pH}.$$

The linear form predicts a straight line of slope exactly $-1$ against pH: a fit with a clearly different slope means the data are not one independent group (Exercise 5).

## Computational representation

```python
import math

def fraction_protonated(pH: float, pKa: float) -> float:
    """Fraction of a group in its protonated (acid) form."""
    return 1 / (1 + 10 ** (pH - pKa))

def pH_for_fraction(theta: float, pKa: float) -> float:
    """pH at which a fraction theta of the group is protonated (inverse of the above)."""
    return pKa + math.log10((1 - theta) / theta)

def charge(pH: float, pKa: float, kind: str) -> float:
    """Mean charge of one group: a base (protonated form +1) or an acid (deprotonated form -1)."""
    theta = fraction_protonated(pH, pKa)
    return theta if kind == "base" else -(1 - theta)

for d in (-2, -1, 0, 1, 2):
    print(f"pH - pKa = {d:+d}: {fraction_protonated(d, 0):.3f} protonated")
print("His (pKa 6.0):", [round(charge(pH, 6.0, "base"), 3) for pH in (6.0, 6.5, 7.0, 7.4)])
print("Asp (pKa 4.1) at 7.0:", round(charge(7.0, 4.1, "acid"), 4))
print("pH where His is 90 % protonated:", round(pH_for_fraction(0.9, 6.0), 2))
```

```text
pH - pKa = -2: 0.990 protonated
pH - pKa = -1: 0.909 protonated
pH - pKa = +0: 0.500 protonated
pH - pKa = +1: 0.091 protonated
pH - pKa = +2: 0.010 protonated
His (pKa 6.0): [0.5, 0.24, 0.091, 0.038]
Asp (pKa 4.1) at 7.0: -0.9987
pH where His is 90 % protonated: 5.05
```

Writing $10^{\mathrm{pH} - \mathrm{p}K_a}$ rather than computing $[\mathrm{H^+}]$ and $K_a$ separately avoids underflow-prone tiny numbers; with NumPy the same function applies to a whole array of pH values at once.

## Worked example

> [!example] Charge of a histidine side chain at pH 7.4 (pKa 6.0)
> 1. $\mathrm{pH} - \mathrm{p}K_a = 1.4$, so $[\mathrm{A^-}]/[\mathrm{HA}] = 10^{1.4} \approx 25.1$: about 25 neutral imidazoles for each protonated one.
> 2. $\theta = 1/(1 + 25.1) \approx 0.038$.
> 3. Histidine is a base whose protonated form is positive, so its mean charge is $+0.038$.
> 4. Interpretation: in a population of molecules, about 1 histidine in 26 carries a proton at any instant; a single molecule switches between both states. If the local pKa were 7.0 instead (L2), $\theta = 1/(1 + 10^{0.4}) \approx 0.28$, about seven times more.

## Common misconceptions

> [!warning] "At pH = pKa the group is fully protonated"
> It is exactly half protonated. Full protonation (99 %) needs a pH about 2 units below the pKa.

> [!warning] "The pKa of histidine is a constant"
> The tabulated value is typical. In a folded protein the environment shifts it, sometimes by more than a unit, and the charge changes with it.[^berg]

> [!warning] "A residue is either charged or neutral"
> A fractional charge such as +0.04 is a population average: each molecule is in one state at a time, and the fraction of molecules in each state is what the equation gives.

> [!warning] "The ratio is protonated over deprotonated"
> In $\mathrm{pH} = \mathrm{p}K_a + \log_{10}([\mathrm{A^-}]/[\mathrm{HA}])$ the base form is on top. Check with a limit: at high pH the base form dominates, so the log term must be positive.

## Exercises

> [!question] Exercise 1 (L1)
> A carboxyl group has pKa 4.1. What fraction is deprotonated, and what is its mean charge, at pH 3.1, 4.1 and 7.1?

> [!success]- Solution
> $\theta = 1/(1 + 10^{\mathrm{pH} - 4.1})$ gives 0.909, 0.5 and 0.001 protonated, so 0.091, 0.5 and 0.999 deprotonated. The deprotonated carboxylate is negative: mean charges −0.091, −0.5 and −0.999.

> [!question] Exercise 2 (L1)
> At what pH is a histidine side chain (pKa 6.0) 90 % protonated? 10 % protonated?

> [!success]- Solution
> $\mathrm{pH} = \mathrm{p}K_a + \log_{10}((1 - \theta)/\theta)$: for $\theta = 0.9$, $6.0 + \log_{10}(1/9) = 5.05$; for $\theta = 0.1$, $6.0 + \log_{10} 9 = 6.95$. Going from 90 % to 10 % protonated takes about 2 pH units, centred on the pKa.

> [!question] Exercise 3 (L2)
> A peptide carries a histidine whose side chain is studied at pH 7.2 (a cytosol-like pH) and pH 5.0 (an acidic compartment, see [[pH]]). With pKa 6.0, compute its protonated fraction at both pH values and explain what changes for the peptide when it moves between them.

> [!success]- Solution
> At pH 7.2: $1/(1 + 10^{1.2}) = 0.059$. At pH 5.0: $1/(1 + 10^{-1}) = 0.909$. The histidine goes from mostly neutral to mostly positive: a 15-fold increase in charge from a 2.2-unit pH drop. Histidine-rich sequences therefore become more positively charged in acidic compartments, which changes their interactions with membranes and other molecules.

> [!question] Exercise 4 (L2)
> Using `charge` from the code above, compute the net charge at pH 7.0 of a free dipeptide His-Asp, with N-terminus pKa 8.0 (base), C-terminus 3.1 (acid), His 6.0 (base), Asp 4.1 (acid). Which group's pKa uncertainty matters most for the result?

> [!success]- Solution
> N-terminus $+1/(1 + 10^{-1}) = +0.909$; His $+0.091$; Asp $-0.9987$; C-terminus $-0.9999$. Net $\approx -0.999$. The termini are typical peptide values, so this is an estimate. The groups whose pKa lies within about one unit of pH 7 (the N-terminus and His) dominate the uncertainty: a 0.5 shift of the His pKa changes its charge from 0.09 to 0.24, while the same shift for Asp changes almost nothing. This is the per-group computation behind [[Isoelectric Point]].

> [!question] Exercise 5 (L2, Python)
> Invented titration data for one group: pH 5.0, 5.5, 6.0, 6.5, 7.0, 7.5 with measured protonated fractions 0.95, 0.86, 0.66, 0.39, 0.17, 0.06. Estimate the pKa with the linear form, and check that the data behave like a single group.

> [!success]- Solution
> ```python
> import math, statistics
> pH = [5.0, 5.5, 6.0, 6.5, 7.0, 7.5]
> theta = [0.95, 0.86, 0.66, 0.39, 0.17, 0.06]          # invented measurements
> y = [math.log10(t / (1 - t)) for t in theta]           # = pKa - pH in the model
> slope, intercept = statistics.linear_regression(pH, y)
> print(round(slope, 3), round(intercept, 2), round(-intercept / slope, 2))
> print(round(statistics.fmean(p + v for p, v in zip(pH, y)), 2))
> # -0.988 6.22 6.3
> # 6.3
> ```
>
> The fitted slope is −0.99, close to the −1 predicted for one independent group, and the line crosses $y = 0$ (half protonation) at pH 6.30. Fixing the slope at −1 gives the same pKa, 6.30, as the mean of $\mathrm{pH} + y$. A value 0.3 above the typical 6.0 is the kind of environmental shift described in L2.

## Mastery checklist

- [ ] 1 Recognized: I can write the equation and say that pH = pKa means half protonated.
- [ ] 2 Understood: I can derive it from $K_a$ and explain the tenfold change per pH unit and the sign of acid and base charges.
- [ ] 3 Practiced: I can compute protonated fractions, charges and the pH for a given fraction, by hand and in Python.
- [ ] 4 Applied: I can compute a peptide's net charge with a stated pKa table and fit a pKa from titration data.
- [ ] 5 Explained: I can teach why histidine is special near pH 7, why pKa values shift in proteins and what the independent-group model ignores.

## References

[^chem14]: [[Chemistry 2e (OpenStax)]], ch. 14 "Acid-Base Equilibria" (acid ionization constants and pKa, buffers and the Henderson-Hasselbalch equation).
[^leh]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of water, weak acids and buffers (titration curves, the Henderson-Hasselbalch equation, pKa as the pH of half dissociation) (chapter number not verified).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein composition and enzyme mechanisms (typical pKa values of ionizable groups in proteins, histidine as a proton donor and acceptor, environmental shifts of pKa).
