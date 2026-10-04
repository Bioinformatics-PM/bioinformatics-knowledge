---
aliases:
  - Acid Dissociation Constant
  - Ka
  - pKa
  - Kb
  - Weak Acid
  - Équilibre acido-basique
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Acid-Base Reaction]]"
  - "[[pH]]"
  - "[[Chemical Equilibrium]]"
  - "[[Logarithm]]"
related:
  - "[[Henderson-Hasselbalch Equation]]"
  - "[[Buffer Solution]]"
  - "[[Amino Acid]]"
  - "[[Isoelectric Point]]"
  - "[[Gibbs Free Energy]]"
  - "[[Enzyme Catalysis]]"
  - "[[Partition Coefficient]]"
projects: []
sources:
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[MIT 5.111SC - Principles of Chemical Science]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
---

# Acid-Base Equilibrium

> [!abstract]
> A weak acid gives up its proton only partly; its acid dissociation constant Ka (or pKa = −log Ka) measures how readily, and comparing pKa with the pH tells whether a group, such as an amino acid side chain, carries its proton and its charge.

## Definition

For a weak acid HA in water, $\mathrm{HA + H_2O \rightleftharpoons H_3O^+ + A^-}$, the **acid ionization (dissociation) constant** is $K_a = [\mathrm{H_3O^+}][\mathrm{A^-}]/[\mathrm{HA}]$, and $\mathrm{p}K_a = -\log_{10} K_a$. For a weak base, $\mathrm{B + H_2O \rightleftharpoons BH^+ + OH^-}$, $K_b = [\mathrm{BH^+}][\mathrm{OH^-}]/[\mathrm{B}]$. For a conjugate acid-base pair, $K_a K_b = K_w$, so $\mathrm{p}K_a + \mathrm{p}K_b = 14.00$ at 25 °C. The larger $K_a$ (the smaller the pKa), the stronger the acid and the weaker its conjugate base.[^chem14][^5111]

## Why it matters

- **Charges of biomolecules.** Seven amino acid side chains and the two termini are weak acids or bases; their pKa values decide the charge of a protein at a given pH ([[Amino Acid]], [[Isoelectric Point]]). Isoelectric focusing and pI calculators are acid-base equilibria at scale.
- **Catalysis.** Groups with pKa near 7, histidine above all, can donate and accept protons at physiological pH, which is how many enzymes perform acid-base catalysis ([[Enzyme Catalysis]]).[^berg]
- **Phosphates everywhere.** Nucleic acids, ATP and metabolites carry phosphate groups whose protonation sets their charge; phosphate itself buffers the cytoplasm ([[ATP]], [[Buffer Solution]]).[^lehninger]
- **Drug behavior.** Whether a drug is ionized at the pH of a compartment changes how it partitions between water and membranes ([[Partition Coefficient]], [[Drug Discovery]]).

## Core (L1)

### Ka and pKa

| Acid (25 °C) | $K_a$ | pKa |
|---|---:|---:|
| Phosphoric acid, $\mathrm{H_3PO_4}$ | $7.5 \times 10^{-3}$ | 2.12 |
| Acetic acid, $\mathrm{CH_3COOH}$ | $1.8 \times 10^{-5}$ | 4.74 |
| Dihydrogen phosphate, $\mathrm{H_2PO_4^-}$ | $6.2 \times 10^{-8}$ | 7.21 |
| Ammonium, $\mathrm{NH_4^+}$ (from $K_b$ of $\mathrm{NH_3}$, $1.8 \times 10^{-5}$) | $5.6 \times 10^{-10}$ | 9.26 |
| Hydrogen phosphate, $\mathrm{HPO_4^{2-}}$ | $4.2 \times 10^{-13}$ | 12.38 |

$K_a$ values from Chemistry 2e;[^chem14] pKa computed. A pKa is a pH: the group is half dissociated when $\mathrm{pH} = \mathrm{p}K_a$; below it the protonated form dominates, above it the deprotonated form ([[Henderson-Hasselbalch Equation]]).

### Conjugate pairs

Multiplying the $K_a$ expression of HA by the $K_b$ expression of $\mathrm{A^-}$ gives $[\mathrm{H_3O^+}][\mathrm{OH^-}] = K_w$: $K_a K_b = K_w$.[^chem14] A pair has one constant, written either way. Biochemistry tables always give the pKa of the **acid form**: for lysine, the pKa of $\mathrm{-NH_3^+}$ losing its proton, not a $K_b$.

### pH of a weak acid solution

For HA at total concentration $C$, let $x = [\mathrm{H_3O^+}] = [\mathrm{A^-}]$ (neglecting water's own ions). Then $K_a = x^2/(C - x)$. If $x \ll C$, $x \approx \sqrt{K_a C}$; check afterward that the **percent ionization** $100\,x/C$ is below about 5 %.[^chem14]

0.10 M acetic acid: $x \approx \sqrt{1.8 \times 10^{-5} \times 0.10} = 1.34 \times 10^{-3}$ M, pH 2.87, 1.3 % ionized: most molecules keep their proton. A weak base works the same way with $K_b$ and $[\mathrm{OH^-}]$ (Exercise 4).

### Bio: ionizable groups of proteins

Acidic groups (C-terminus, Asp, Glu, Cys, Tyr) are neutral as HA and negative as $\mathrm{A^-}$; basic groups (N-terminus, His, Lys, Arg) are positive as $\mathrm{BH^+}$ and neutral as B. Their typical pKa values in proteins (Asp and Glu 4.1, His 6.0, Lys 10.8, Arg 12.5, and others) are tabulated in [[Amino Acid#Ionizable groups]] from Berg.[^berg] Against the pH of the cell's compartments:

![[ph-scale-compartments-side-chain-pka.svg]]

At cytosolic pH, carboxylates are negative and Lys and Arg positive; His, with its pKa near 6, is the group whose charge changes over the physiological range.[^berg] The fraction calculation is the [[Henderson-Hasselbalch Equation]].

## Deeper (L2)

### Polyprotic acids

An acid with several dissociable protons loses them one at a time, each step with its own constant, and $K_{a1} > K_{a2} > K_{a3}$: removing a proton from an already negative species is harder.[^chem14] Phosphoric acid has three pKa values, so at a given pH at most two of its four species are abundant. Near pH 7 the pair $\mathrm{H_2PO_4^-}/\mathrm{HPO_4^{2-}}$ dominates, which is why phosphate buffers cells.[^lehninger] Sources differ on that middle pKa: 7.21 from Chemistry 2e's $K_{a2}$, 6.86 in Lehninger.[^chem14][^lehninger] A pKa depends on the conditions of measurement (temperature, ionic strength), so state which value a calculation uses: here the choice changes the $\mathrm{HPO_4^{2-}}/\mathrm{H_2PO_4^-}$ ratio at pH 7.2 from 1.0 to 2.2 (Exercise 5).

### When the shortcut fails

$x \approx \sqrt{K_a C}$ assumes small ionization and negligible water ionization. For dilute or stronger acids, solve exactly: the charge balance $[\mathrm{H_3O^+}] = [\mathrm{A^-}] + [\mathrm{OH^-}]$ with $[\mathrm{A^-}] = C K_a/([\mathrm{H_3O^+}] + K_a)$ gives one equation in $[\mathrm{H_3O^+}]$ (Mathematical representation). For acetic acid at $10^{-5}$ M the shortcut gives pH 4.87 against the exact 5.15: at high dilution a weak acid is mostly ionized (72 %).

### pKa values move in proteins

Tabulated side-chain pKa values are typical values; inside a folded protein, nearby charges, hydrogen bonds or a buried, nonpolar position shift them, sometimes by several units.[^berg] A carboxylate buried away from water is harder to ionize (its pKa rises); a lysine near other positive charges loses its proton more easily (its pKa falls). Sequence-based charge and pI calculations ignore these shifts ([[Isoelectric Point]]).

## Advanced (L3)

- **pKa is a free energy.** Since $K_a$ is an equilibrium constant, $\Delta G^\circ_{\text{deprot}} = -RT\ln K_a = 2.303\,RT\,\mathrm{p}K_a$, that is $5.71 \times \mathrm{p}K_a$ kJ/mol at 25 °C ([[Gibbs Free Energy]]). A shift of one pKa unit means the environment stabilizes one protonation state by 5.7 kJ/mol relative to the other (Exercise 6).
- **Linked equilibria.** When a ligand binds only one protonation state of a group, or a protein folds better in one, protonation and binding (or folding) are coupled: affinity and stability then depend on pH, and binding shifts the group's apparent pKa. This is the logic of the Bohr effect ([[Le Chatelier's Principle#Advanced (L3)]]) and of pH-dependent drug binding.
- **Predicting pKa from structure.** Because shifts come from the electrostatic environment, they can be estimated from a 3D structure with electrostatic models of each group's surroundings ([[Poisson-Boltzmann Equation]], [[Structural Bioinformatics]]); the predicted protonation states are then an input of docking and molecular simulation, and a source of error when wrong.

## Mathematical representation

- $K_a = \dfrac{h\,a}{c_{\mathrm{HA}}}$ with $h = [\mathrm{H_3O^+}]$, $a = [\mathrm{A^-}]$; $\mathrm{p}K_a = -\log_{10} K_a$; $K_a K_b = K_w$.
- **Mass balance** $C = [\mathrm{HA}] + [\mathrm{A^-}]$ gives $[\mathrm{A^-}] = \dfrac{C K_a}{h + K_a}$ and $[\mathrm{HA}] = \dfrac{C h}{h + K_a}$ (the [[Henderson-Hasselbalch Equation]] in fraction form).
- **Charge balance** for HA in water: $h = \dfrac{C K_a}{h + K_a} + \dfrac{K_w}{h}$. The function $f(h) = h - \dfrac{CK_a}{h + K_a} - \dfrac{K_w}{h}$ is strictly increasing ($f'(h) = 1 + \dfrac{CK_a}{(h+K_a)^2} + \dfrac{K_w}{h^2} > 0$), so the root is unique.
- **Polyprotic acid** $\mathrm{H}_n\mathrm{A}$ with constants $K_1, \dots, K_n$: the fraction carrying $n - j$ protons is
$$\alpha_j = \frac{h^{\,n-j}\prod_{i=1}^{j} K_i}{\sum_{m=0}^{n} h^{\,n-m}\prod_{i=1}^{m} K_i}, \qquad j = 0, \dots, n.$$

## Computational representation

```python
import math

KW = 1.0e-14   # 25 C
# Ionization constants at 25 C (Chemistry 2e)
KA = {"acetic acid": 1.8e-5, "H3PO4": 7.5e-3, "H2PO4-": 6.2e-8, "HPO4^2-": 4.2e-13,
      "NH4+ (from Kb of NH3)": KW / 1.8e-5}
for name, ka in KA.items():
    print(f"{name:22s} Ka = {ka:.1e}  pKa = {-math.log10(ka):.2f}")


def weak_acid_ph(c: float, ka: float, kw: float = KW) -> float:
    """Exact pH of a weak monoprotic acid HA at total concentration c.

    Charge balance h = [A-] + [OH-] = c*ka/(h + ka) + kw/h; the difference
    f(h) = h - c*ka/(h + ka) - kw/h increases with h, so bisection on log10(h) works.
    """
    f = lambda h: h - c * ka / (h + ka) - kw / h
    lo, hi = -14.0, 1.0                     # log10 bounds for h
    for _ in range(100):
        mid = (lo + hi) / 2
        if f(10 ** mid) > 0:
            hi = mid
        else:
            lo = mid
    return -(lo + hi) / 2


def approx_ph(c: float, ka: float) -> float:
    """Textbook shortcut h = sqrt(ka * c), valid when ionization is small."""
    return -math.log10(math.sqrt(ka * c))


for c in (0.1, 1e-3, 1e-5):
    ph = weak_acid_ph(c, 1.8e-5)
    pct = 100 * 1.8e-5 / (10 ** -ph + 1.8e-5)   # percent ionized = [A-]/c
    print(f"acetic acid {c:.0e} M: exact pH {ph:.2f}, shortcut {approx_ph(c, 1.8e-5):.2f}, ionized {pct:.1f} %")
```

```text
acetic acid            Ka = 1.8e-05  pKa = 4.74
H3PO4                  Ka = 7.5e-03  pKa = 2.12
H2PO4-                 Ka = 6.2e-08  pKa = 7.21
HPO4^2-                Ka = 4.2e-13  pKa = 12.38
NH4+ (from Kb of NH3)  Ka = 5.6e-10  pKa = 9.26
acetic acid 1e-01 M: exact pH 2.88, shortcut 2.87, ionized 1.3 %
acetic acid 1e-03 M: exact pH 3.90, shortcut 3.87, ionized 12.5 %
acetic acid 1e-05 M: exact pH 5.15, shortcut 4.87, ionized 71.6 %
```

Bisecting on $\log_{10} h$ rather than $h$ handles the 15 orders of magnitude of possible concentrations evenly. Store pKa values (not $K_a$) in tables, with the temperature and source, as biochemistry databases do.

## Worked example

> [!example] A weak acid at three concentrations
> Acetic acid, $K_a = 1.8 \times 10^{-5}$.[^chem14]
> 1. **0.10 M**: $x = \sqrt{1.8 \times 10^{-6}} = 1.34 \times 10^{-3}$ M; $x/C = 1.3$ % < 5 %, approximation valid; pH 2.87 (exact 2.88).
> 2. **1.0 × 10⁻³ M**: shortcut pH 3.87, but $x/C$ would be 13 %: solve the quadratic instead, $x = (-K_a + \sqrt{K_a^2 + 4K_aC})/2 = 1.26 \times 10^{-4}$ M, pH 3.90.
> 3. **1.0 × 10⁻⁵ M**: the shortcut predicts more $\mathrm{H_3O^+}$ ($1.34 \times 10^{-5}$ M) than there is acid. The exact solution: 72 % ionized, pH 5.15.
> 4. **Read it**: dilution increases the fraction ionized ([[Le Chatelier's Principle]]: one particle becomes two), so "weak" describes $K_a$, not the ionized fraction at every concentration.

## Common misconceptions

> [!warning] "A weak acid is a dilute acid"
> Weak (small $K_a$) and dilute (small $C$) are independent. 0.10 M acetic acid is concentrated and weak; $10^{-5}$ M acetic acid is dilute and mostly ionized.

> [!warning] "A low pKa means a weak acid"
> The reverse: low pKa means large $K_a$, a stronger acid. Phosphoric acid (pKa 2.12) gives up its first proton far more readily than ammonium (9.26).[^chem14]

> [!warning] "The pKa of a basic side chain is the pH where it becomes basic"
> The pKa of lysine (10.8) refers to $\mathrm{-NH_3^+} \rightleftharpoons \mathrm{-NH_2 + H^+}$: below 10.8 lysine is mostly protonated and positive.[^berg] Every tabulated pKa describes the acid form losing a proton.

> [!warning] "A side chain has one fixed pKa"
> The tabulated value is typical; the environment inside a protein shifts it.[^berg]

## Exercises

> [!question] Exercise 1 (L1)
> $K_b$ of ammonia is $1.8 \times 10^{-5}$ at 25 °C.[^chem14] Compute $K_a$ and pKa of the ammonium ion, and say whether $\mathrm{NH_4^+}$ is mostly protonated at pH 7.4.

> [!success]- Solution
> $K_a = K_w/K_b = 10^{-14}/1.8 \times 10^{-5} = 5.6 \times 10^{-10}$, pKa 9.26. At pH 7.4, about 1.9 units below the pKa, ammonium is mostly protonated ($\mathrm{NH_4^+}$, about 99 %).

> [!question] Exercise 2 (L1)
> Rank the acid forms of the Asp side chain (pKa 4.1), the His side chain (6.0) and the Lys side chain (10.8) from strongest to weakest acid. Which conjugate base is the strongest?

> [!success]- Solution
> Strongest acid: Asp (lowest pKa), then His, then Lys (protonated amine). The strongest conjugate base belongs to the weakest acid: the neutral lysine amine $\mathrm{-NH_2}$ binds a proton most avidly, which is why lysine is protonated at all physiological pH values.

> [!question] Exercise 3 (L2)
> Compute the pH and percent ionization of 0.10 M acetic acid with the shortcut, and justify the approximation.

> [!success]- Solution
> $x = \sqrt{1.8 \times 10^{-5} \times 0.10} = 1.34 \times 10^{-3}$ M, pH 2.87, ionization 1.3 %. Because $x$ is 1.3 % of $C$, neglecting it in $C - x$ changes $x$ by under 1 %; the exact solver gives 2.88.

> [!question] Exercise 4 (L2)
> Compute the pH of 0.10 M ammonia at 25 °C.

> [!success]- Solution
> $\mathrm{NH_3 + H_2O \rightleftharpoons NH_4^+ + OH^-}$: $[\mathrm{OH^-}] \approx \sqrt{1.8 \times 10^{-5} \times 0.10} = 1.34 \times 10^{-3}$ M, pOH 2.87, pH $= 14.00 - 2.87 = 11.13$.

> [!question] Exercise 5 (L3, Python)
> Write `species_fractions(ph, kas)` for a polyprotic acid and compute the fractions of the four phosphate species with Chemistry 2e's constants at pH 4.75 (lysosome), 7.2 (cytosol), 7.4 and 7.98 (mitochondrial matrix). Then compare the $\mathrm{HPO_4^{2-}}/\mathrm{H_2PO_4^-}$ ratio at pH 7.2 with pKa2 = 7.21 and with 6.86.

> [!success]- Solution
> ```python
> def species_fractions(ph: float, kas: list[float]) -> list[float]:
>     """Fractions of H_nA, H_(n-1)A-, ..., A^n- for a polyprotic acid with constants Ka1 > Ka2 > ..."""
>     h, n = 10 ** (-ph), len(kas)
>     terms, prod = [h ** n], 1.0
>     for j, k in enumerate(kas, start=1):
>         prod *= k
>         terms.append(h ** (n - j) * prod)
>     total = sum(terms)
>     return [t / total for t in terms]
>
> PHOSPHATE = [7.5e-3, 6.2e-8, 4.2e-13]
> for ph in (4.75, 7.2, 7.4, 7.98):
>     print(ph, [round(x, 3) for x in species_fractions(ph, PHOSPHATE)])
> for pka2 in (7.21, 6.86):
>     print(pka2, round(10 ** (7.2 - pka2), 2))
> ```
> ```text
> 4.75 [0.002, 0.994, 0.003, 0.0]
> 7.2 [0.0, 0.504, 0.496, 0.0]
> 7.4 [0.0, 0.391, 0.609, 0.0]
> 7.98 [0.0, 0.144, 0.855, 0.0]
> 7.21 0.98
> 6.86 2.19
> ```
> In the lysosome phosphate is almost entirely $\mathrm{H_2PO_4^-}$; in the cytosol it is split between $\mathrm{H_2PO_4^-}$ and $\mathrm{HPO_4^{2-}}$; in the matrix $\mathrm{HPO_4^{2-}}$ dominates. $\mathrm{H_3PO_4}$ and $\mathrm{PO_4^{3-}}$ are negligible everywhere in the cell. The choice of pKa2 doubles the predicted ratio at pH 7.2: a model is only as good as its constants.

> [!question] Exercise 6 (L3)
> A lysine buried near positive charges has its pKa lowered from 10.8 to 7.8. What free energy does this shift represent at 25 °C, and how does it change the protonated fraction at pH 7.0?

> [!success]- Solution
> $\Delta\Delta G = 2.303\,RT \times 3 = 5.71 \times 3 = 17.1$ kJ/mol: the environment destabilizes the charged $\mathrm{-NH_3^+}$ form by that much relative to the neutral one. Protonated fraction $1/(1 + 10^{\,\mathrm{pH} - \mathrm{p}K_a})$: 0.9998 at pKa 10.8, 0.863 at 7.8. About one lysine in seven is now neutral at pH 7.0, enough to matter for a catalytic mechanism or a salt bridge.

## Mastery checklist

- [ ] 1 Recognized: I can write $K_a$ and $K_b$ expressions and convert between $K_a$ and pKa.
- [ ] 2 Understood: I can explain conjugate pairs ($K_aK_b = K_w$), why low pKa means a strong acid, and which side-chain forms are charged.
- [ ] 3 Practiced: I can compute the pH of weak acid and base solutions, check the approximation, and solve exactly in Python, including polyprotic speciation.
- [ ] 4 Applied: I can predict the protonation state of side chains and phosphates in a given compartment and choose pKa values with their source and conditions.
- [ ] 5 Explained: I can teach pKa as a free energy, why pKa values shift inside proteins, and how protonation couples to binding and folding.

## References

[^chem14]: [[Chemistry 2e (OpenStax)]], ch. 14 "Acid-Base Equilibria" (ionization constants $K_a$ and $K_b$, $K_aK_b = K_w$, relative strengths of conjugate pairs, percent ionization and the small-$x$ approximation, polyprotic acids with $K_{a1} > K_{a2} > K_{a3}$, ionization constants of acetic acid, ammonia and phosphoric acid).
[^5111]: [[MIT 5.111SC - Principles of Chemical Science]], course description (acid-base equilibria among the course topics).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein composition and enzyme mechanisms (typical pKa values of ionizable groups in proteins, environment-dependent pKa shifts, histidine as an acid-base catalyst near neutral pH).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of water, weak acids and buffers (the phosphate system of the cytoplasm, pKa 6.86 for $\mathrm{H_2PO_4^-}$) (chapter number not verified).
