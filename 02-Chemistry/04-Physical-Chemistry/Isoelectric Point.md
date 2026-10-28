---
aliases:
  - pI
  - Isoelectric pH
  - IEP
  - Point isoélectrique
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
  - level/M1
mastery: 0
prerequisites:
  - "[[Amino Acid]]"
  - "[[Henderson-Hasselbalch Equation]]"
  - "[[Acid-Base Equilibrium]]"
  - "[[pH]]"
  - "[[Protein]]"
related:
  - "[[Gel Electrophoresis]]"
  - "[[Protein Purification]]"
  - "[[Proteomics]]"
  - "[[Proteome]]"
  - "[[Mass Spectrometry]]"
  - "[[Root Finding]]"
  - "[[Electric Charge]]"
  - "[[Post-Translational Modification]]"
projects: []
sources:
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Kozlowski 2016 - IPC Isoelectric Point Calculator]]"
  - "[[Kozlowski 2017 - Proteome-pI Proteome Isoelectric Point Database]]"
---

# Isoelectric Point

> [!abstract]
> The isoelectric point pI is the pH at which a molecule carries no net electric charge on average; for a protein it follows from the counts of its ionizable groups and their pKa values, and it decides where the protein stops in an isoelectric focusing gel.

## Definition

The **isoelectric point** (pI, isoelectric pH) is the pH at which the net electric charge of a molecule is zero.[^lehninger] A molecule with several ionizable groups has an average charge $Z(\mathrm{pH})$, the sum of the charged fractions of its groups given by the [[Henderson-Hasselbalch Equation]]; the pI is the root of $Z$, which exists and is unique because $Z$ decreases strictly with pH ([[Amino Acid#Mathematical representation]]).

## Why it matters

- **Separations.** In isoelectric focusing, proteins migrate in a pH gradient under an electric field until they reach the pH equal to their pI, where they stop; two-dimensional electrophoresis adds a separation by mass in the perpendicular direction. Ion-exchange chromatography separates proteins by net charge, whose sign at a given buffer pH is set by the pI.[^berg] ([[Gel Electrophoresis]], [[Protein Purification]])
- **Proteome maps.** Predicted pI and molecular weight place every protein of a proteome on a virtual 2D gel; Proteome-pI provides such predictions for the proteins of 5,029 proteomes, with 18 methods.[^proteomepi] ([[Proteomics]], [[Proteome]])
- **A sequence statistic.** The pI depends only on composition, so it is computed in microseconds for every record of a protein [[FASTA Format|FASTA]] file, next to length, mass and mean hydropathy ([[Amino Acid]]).
- **With known error bars.** Even the best pKa sets predict protein pI with an average error of about 0.9 pH units, peptides about 0.25.[^ipc] A computed pI is an estimate, to be reported with the pKa set used.

## Core (L2)

### A free amino acid: the average of two pKa

Glycine is a cation below its first pKa (2.34, carboxyl), a zwitterion in between, and an anion above its second (9.60, amino).[^lehninger] With two groups, the net charge is the protonated fraction of the amino group minus the deprotonated fraction of the carboxyl:

$$Z = \frac{1}{1 + 10^{\,\mathrm{pH} - \mathrm{p}K_2}} - \frac{1}{1 + 10^{\,\mathrm{p}K_1 - \mathrm{pH}}} = 0 \iff \mathrm{p}K_1 - \mathrm{pH} = \mathrm{pH} - \mathrm{p}K_2 \iff \mathrm{pI} = \frac{\mathrm{p}K_1 + \mathrm{p}K_2}{2},$$

so $\mathrm{pI} = (2.34 + 9.60)/2 = 5.97$ for glycine.[^lehninger] With more groups the same idea gives a **bracketing rule**: list the groups by pKa, follow the charge of the dominant species as the pH rises (each deprotonation removes one unit), and find the two pKa values between which the neutral species dominates; the pI lies between them, close to their average when the other groups are far away (Worked example).

### A protein: count, then solve

For a protein, the ionizable groups are the N-terminus, the C-terminus and the side chains of Lys, Arg, His (basic) and Asp, Glu, Cys, Tyr (acidic). Typical pKa values in proteins are 8.0 (N-terminus), 10.8 (Lys), 12.5 (Arg), 6.0 (His), 3.1 (C-terminus), 4.1 (Asp, Glu), 8.3 (Cys) and 10.9 (Tyr),[^berg] the table of [[Amino Acid#Ionizable groups]]. With $n_j$ groups of type $j$,

$$Z(\mathrm{pH}) = \sum_{j\,\text{basic}} \frac{n_j}{1 + 10^{\,\mathrm{pH} - \mathrm{p}K_j}} - \sum_{j\,\text{acidic}} \frac{n_j}{1 + 10^{\,\mathrm{p}K_j - \mathrm{pH}}}.$$

Two consequences shape every titration curve (figure, panel a):

- **Only composition matters.** Reversing or shuffling a sequence leaves its pI unchanged, so the counts can be taken once and $Z$ evaluated in constant time.
- **Groups titrate in clusters.** Carboxylates around pH 3 to 4, His around 6, the N-terminus and Cys around 8, Lys and Tyr around 11, Arg above 12. Between clusters $Z$ is nearly flat, so a small change of composition can move the pI by several units.

![[isoelectric-point-titration-ief.svg]]

### pI, charge and migration

Below its pI a protein is positive and drifts toward the cathode in an electric field; above its pI it is negative and drifts toward the anode; at its pI it stops. In a stable pH gradient this focuses each protein into a band at its pI (figure, panel b).[^berg] The same sign rule chooses an ion exchanger: a protein that is positive at the working pH binds a negatively charged (cation-exchange) resin, a negative one a positively charged (anion-exchange) resin.[^berg]

## Advanced (L3)

- **Why predictions err.** The pKa of a group in a folded protein depends on its surroundings (burial, nearby charges, hydrogen bonds), so tabulated values are only typical;[^berg] cysteines in disulfide bonds have no ionizable thiol; modifications add or remove groups ([[Post-Translational Modification]]). Sequence-based calculators ignore all of this and differ in the pKa set they assume, hence the benchmark errors quoted above.[^ipc]
- **Which pKa values matter.** Differentiating $Z(\mathrm{pI}) = 0$ gives the sensitivity of the pI to each pKa (Mathematical representation): a group's weight is its share of the titration slope at the pI. Only groups whose pKa lies near the pI count; for a protein with pI near 6, the His value dominates, and the Lys and Arg values hardly matter (Exercise 4).
- **Adding a group moves the pI one way.** An extra acidic group lowers $Z$ at every pH, so the root moves down; an extra basic group moves it up (Exercise 5). This is the logic of charge-changing modifications and of the charge shifts that separate protein variants on gels.

## Frontier (M1)

- **Proteome-wide distributions.** The distribution of protein isoelectric points in proteomes is bimodal,[^proteomepi] with few proteins in between. Exercise 6 shows one mechanism that produces bimodality from the shape of $Z$ alone: when few groups titrate near neutral pH, random sequences rarely balance there. Whether real proteomes owe their shape to this, to selection, or to both is a question for comparative analysis across organisms ([[Proteome]]).
- **Fitting the model to data.** IPC treats pKa values as parameters, fits two optimized sets to measured pI values of proteins and peptides, and benchmarks them against many published sets.[^ipc] pI prediction becomes a regression problem, with the usual questions of training data, overfitting and outliers.

## Mathematical representation

- Protonated fraction of group $j$: $\theta_j = 1/(1 + 10^{\,\mathrm{pH} - \mathrm{p}K_j})$. Net charge $Z = \sum_{j \in B} n_j\theta_j - \sum_{j \in A} n_j(1 - \theta_j)$ over basic ($B$) and acidic ($A$) groups.
- Slope: $dZ/d\mathrm{pH} = -\ln 10 \sum_j n_j\theta_j(1-\theta_j) < 0$, so the root is unique; bisection on $[0, 14]$ halves the interval each step (18 steps for $10^{-4}$).
- Two groups: $\mathrm{pI} = (\mathrm{p}K_1 + \mathrm{p}K_2)/2$ exactly.
- Sensitivity: since $\partial Z/\partial \mathrm{p}K_j = \ln 10\, n_j\theta_j(1-\theta_j)$ for acids and bases alike, implicit differentiation of $Z(\mathrm{pI}) = 0$ gives
$$\frac{\partial\,\mathrm{pI}}{\partial\,\mathrm{p}K_j} = w_j = \frac{n_j\theta_j(1-\theta_j)}{\sum_k n_k\theta_k(1-\theta_k)}\Bigg|_{\mathrm{pH} = \mathrm{pI}}, \qquad \sum_j w_j = 1:$$
shifting every pKa by $\delta$ shifts the pI by $\delta$.

## Computational representation

The [[Amino Acid#Computational representation]] loops over residues; here the counts are taken once and the pKa set is a parameter, so several sets can be compared:

```python
from collections import Counter

# typical pKa values of ionizable groups in proteins (Berg), with the charge of the protonated form
PKA = {"Nterm": (8.0, +1), "K": (10.8, +1), "R": (12.5, +1), "H": (6.0, +1),
       "Cterm": (3.1, -1), "D": (4.1, -1), "E": (4.1, -1), "C": (8.3, -1), "Y": (10.9, -1)}


def ionizable_groups(seq: str, pka: dict = PKA) -> Counter:
    """One N-terminus, one C-terminus, and the ionizable side chains counted from the composition."""
    groups = Counter(aa for aa in seq.upper() if aa in pka)
    groups["Nterm"] = groups["Cterm"] = 1
    return groups


def net_charge(groups: Counter, ph: float, pka: dict = PKA) -> float:
    """Mean charge: protonated fraction of each base minus deprotonated fraction of each acid."""
    total = 0.0
    for group, n in groups.items():
        value, z = pka[group]
        if z > 0:
            total += n / (1 + 10 ** (ph - value))
        else:
            total -= n / (1 + 10 ** (value - ph))
    return total


def isoelectric_point(seq: str, pka: dict = PKA, tol: float = 1e-4) -> float:
    """Root of the strictly decreasing net charge, by bisection on [0, 14]."""
    groups = ionizable_groups(seq, pka)
    lo, hi = 0.0, 14.0
    while hi - lo > tol:
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if net_charge(groups, mid, pka) > 0 else (lo, mid)
    return (lo + hi) / 2


def sensitivity(seq: str, delta: float = 0.5) -> dict[str, float]:
    """Change of the pI when the pKa of one type of group is raised by delta."""
    base = isoelectric_point(seq)
    shifts = {}
    for group in ionizable_groups(seq):
        shifted = dict(PKA)
        shifted[group] = (PKA[group][0] + delta, PKA[group][1])
        shifts[group] = round(isoelectric_point(seq, shifted) - base, 3)
    return shifts


toy = "MKTAYDELHGSRVEQKPWNDAGHLYEKCTSDREAGKVHEL"     # invented 40-residue sequence
groups = ionizable_groups(toy)
print(dict(sorted(groups.items())))
print(f"pI = {isoelectric_point(toy):.2f}, charge at pH 7.4 = {net_charge(groups, 7.4):+.2f}")
print({ph: round(net_charge(groups, ph), 2) for ph in (3, 5, 7, 9, 11)})
print(f"check, peptide GHKDE of the Amino Acid note: pI = {isoelectric_point('GHKDE'):.2f}")

glycine = {"Nterm": (9.60, +1), "Cterm": (2.34, -1)}    # free glycine (Lehninger)
print(f"free glycine: pI = {isoelectric_point('G', glycine):.2f}")
```

```text
{'C': 1, 'Cterm': 1, 'D': 3, 'E': 5, 'H': 3, 'K': 4, 'Nterm': 1, 'R': 2, 'Y': 2}
pI = 5.79, charge at pH 7.4 = -2.20
{3: 8.97, 5: 1.63, 7: -1.86, 9: -3.83, 11: -7.63}
check, peptide GHKDE of the Amino Acid note: pI = 5.23
free glycine: pI = 5.97
```

The toy protein's charge runs from +10 (all bases protonated) to −12 (all acids deprotonated); the peptide check reproduces the Amino Acid note. For a real proteome, parse the FASTA records, decide how to treat ambiguous letters (`X`, `B`, `Z`), and store the pKa set name with the results.

## Worked example

> [!example] The pI of the tripeptide Lys-Asp-Gly by bracketing (invented peptide)
> Groups and typical pKa:[^berg] C-terminus 3.1, Asp 4.1, N-terminus 8.0, Lys 10.8 (Gly has no ionizable side chain).
> 1. **Charge of the dominant species** as the pH rises, one unit lost at each pKa:
>
> | pH range | below 3.1 | 3.1 to 4.1 | 4.1 to 8.0 | 8.0 to 10.8 | above 10.8 |
> |---|---|---|---|---|---|
> | dominant charge | +2 | +1 | 0 | −1 | −2 |
>
> 2. **Bracket**: the neutral species dominates between 4.1 and 8.0, so $\mathrm{pI} \approx (4.1 + 8.0)/2 = 6.05$.
> 3. **Check**: at pH 6.05 the net charge is $+0.0011$ (N-terminus 0.9889, Lys 1.0000, C-terminus −0.9989, Asp −0.9889); the exact root, `isoelectric_point("KDG")`, is 6.07. The far groups (C-terminus, Lys) still pull a little.
> 4. **Read it**: near its pI the peptide is a mixture of species whose charges average to zero, not a population of neutral molecules.

## Common misconceptions

> [!warning] "At the pI the molecules have no charges"
> At the pI the **average** net charge is zero. Each molecule still carries charged groups (glycine at pH 5.97 is mostly a zwitterion), and individual molecules fluctuate between charge states.

> [!warning] "A calculator gives the pI of my protein"
> It gives the pI of a model: one pKa set, no structure, no modifications. Benchmarks put the average error near 0.9 pH units for proteins,[^ipc] and two calculators can disagree by more.

> [!warning] "The pI depends on the sequence order"
> In the sequence-based model it depends only on how many of each ionizable group the chain carries. Order matters in reality only through folding, which shifts pKa values.[^berg]

> [!warning] "A protein at a pH below its pI is uncharged"
> It is positive, and more so the further the pH is below the pI; the sign of the charge flips at the pI, which is what electrophoresis and ion exchange exploit.

## Exercises

> [!question] Exercise 1 (L2)
> With pKa values 2.34 and 9.60,[^lehninger] compute the pI of free glycine and its net charge at pH 2.34 and 9.60.

> [!success]- Solution
> $\mathrm{pI} = (2.34 + 9.60)/2 = 5.97$. At pH 2.34 the carboxyl is half deprotonated and the amino group fully protonated: $Z = 1 - 0.5 = +0.5$. At pH 9.60, symmetrically, $Z = 0.5 - 1 = -0.5$.

> [!question] Exercise 2 (L2)
> Predict the pI of the invented tripeptide Lys-His-Asp (KHD) by bracketing, then check with `isoelectric_point`.

> [!success]- Solution
> Groups: C-terminus 3.1, Asp 4.1, His 6.0, N-terminus 8.0, Lys 10.8. Charges of the dominant species: +3, +2, +1, 0 between 6.0 and 8.0, then −1, −2. Bracket: $(6.0 + 8.0)/2 = 7.0$; `isoelectric_point("KHD")` returns 7.00. His and the N-terminus are the groups that decide this peptide's charge near neutral pH.

> [!question] Exercise 3 (L2)
> A protein has pI 5.5. In a pH 8.6 buffer, what is the sign of its charge, toward which electrode does it move, and which ion exchanger binds it? Where does it end up in isoelectric focusing?

> [!success]- Solution
> pH 8.6 is above the pI: the protein is negative, moves toward the anode and binds an anion exchanger (positively charged resin). In isoelectric focusing it moves until pH 5.5, where its net charge is zero, and stays there.

> [!question] Exercise 4 (L3, Python)
> For the toy protein, compute `sensitivity(toy)` and the analytic weights $w_j$ at the pI. Which pKa values does the pI depend on, and why?

> [!success]- Solution
> ```python
> print(sensitivity(toy))
> p_i = isoelectric_point(toy)
> share = {}
> for grp, n in groups.items():
>     theta = 1 / (1 + 10 ** (p_i - PKA[grp][0]))       # protonated fraction at the pI
>     share[grp] = n * theta * (1 - theta)
> total = sum(share.values())
> print({grp: round(v / total, 3) for grp, v in share.items() if v / total > 0.001})
> ```
> ```text
> {'K': 0.0, 'Y': 0.0, 'D': 0.053, 'E': 0.083, 'H': 0.428, 'R': 0.0, 'C': 0.001, 'Nterm': 0.002, 'Cterm': 0.002}
> {'D': 0.067, 'E': 0.111, 'H': 0.81, 'C': 0.004, 'Nterm': 0.007, 'Cterm': 0.002}
> ```
> At pI 5.79 only the three His (pKa 6.0) and, much less, the carboxylates are titrating: His carries 81 % of the slope, so a 0.5 shift of its pKa moves the pI by 0.43 (a little more than $0.81 \times 0.5$, since the response is not linear). Lys, Arg and Tyr are fully in one state and do not matter. A pKa set is only as good as its values for the groups near the pI.

> [!question] Exercise 5 (L3)
> Prove that adding an acidic group to a protein lowers its pI and adding a basic group raises it. Check with an illustrative extra group of pKa 6.0 on the toy protein.

> [!success]- Solution
> An extra acid adds $-1/(1 + 10^{\,\mathrm{p}K - \mathrm{pH}}) < 0$ to $Z$ at every pH, so $Z_{\text{new}}(\mathrm{pI}_{\text{old}}) < 0$; since $Z_{\text{new}}$ decreases, its root lies below $\mathrm{pI}_{\text{old}}$. A base adds a positive term and the root moves up.
> ```python
> extra = dict(PKA, **{"@": (6.0, -1), "&": (6.0, +1)})   # @: extra acidic group, &: extra basic group
> print(f"pI {isoelectric_point(toy):.2f}; with an extra acid {isoelectric_point(toy + '@', extra):.2f}; "
>       f"with an extra base {isoelectric_point(toy + '&', extra):.2f}")
> ```
> Output: `pI 5.79; with an extra acid 5.64; with an extra base 6.03`. The placeholder symbols stand for a modification; the size of the shift depends on where the new pKa sits relative to the pI.

> [!question] Exercise 6 (M1, Python)
> Draw 2000 random 300-residue sequences from an invented composition (D 5 %, E 6 %, K 6 %, R 5 %, Y 3 %, His and Cys at 1 % each, the rest neutral) and histogram their pI by integer bins. Repeat with His and Cys at 5 % each. Explain the two shapes.

> [!success]- Solution
> ```python
> import random
>
> neutral = "AFGILMNPQSTVW"
>
>
> def random_pis(weights: dict[str, int], n: int = 2000, length: int = 300, seed: int = 2) -> list[float]:
>     """pI of random sequences drawn from a composition given in percent (other residues neutral)."""
>     pool = "".join(a * w for a, w in weights.items())
>     pool += "".join(neutral[i % len(neutral)] for i in range(100 - len(pool)))
>     rng = random.Random(seed)
>     return [isoelectric_point("".join(rng.choices(pool, k=length))) for _ in range(n)]
>
>
> for his_cys in (1, 5):                                   # invented compositions, percent
>     pis = random_pis({"D": 5, "E": 6, "K": 6, "R": 5, "H": his_cys, "C": his_cys, "Y": 3})
>     counts = Counter(int(v) for v in pis)
>     print(f"His = Cys = {his_cys} %:", " ".join(f"{b}:{counts[b]}" for b in range(4, 12)))
> ```
> ```text
> His = Cys = 1 %: 4:440 5:405 6:139 7:153 8:196 9:319 10:344 11:4
> His = Cys = 5 %: 4:46 5:329 6:573 7:540 8:400 9:91 10:21 11:0
> ```
> With few His and Cys, $Z$ is almost flat between the carboxylate and Lys clusters: a random sequence has a small surplus of acids or bases, and its root falls on one of the two steep flanks, near 4 to 5 or 9 to 10. Two modes appear without any selection. With more His and Cys titrating in the middle, the flat region disappears and the distribution has one central mode. Real proteomes are bimodal;[^proteomepi] this toy shows that composition alone can produce such a shape, so a biological explanation must be tested against it.

## Mastery checklist

- [ ] 1 Recognized: I can define the pI and say how a protein behaves above and below it.
- [ ] 2 Understood: I can derive the two-group formula, apply the bracketing rule, and explain why the pI depends only on composition in the model.
- [ ] 3 Practiced: I can compute pI, titration curves and pKa sensitivities in Python for any sequence and pKa set.
- [ ] 4 Applied: I computed the pI of the proteins of a real proteome file and compared some values with a database or a 2D-gel result.
- [ ] 5 Explained: I can teach why predictions err (environment, modifications, pKa sets), the sensitivity weights, and what proteome-wide pI distributions can and cannot tell us.

## References

[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of amino acid titration (isoelectric point as the pH of zero net charge; glycine $\mathrm{p}K_1 = 2.34$, $\mathrm{p}K_2 = 9.60$, pI 5.97) (chapter number not verified).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein composition and protein separation (typical pKa values of ionizable groups in proteins, which depend on the local environment; ion-exchange chromatography by net charge; isoelectric focusing; two-dimensional electrophoresis).
[^ipc]: [[Kozlowski 2016 - IPC Isoelectric Point Calculator]], *Biology Direct* 11:55 (pKa sets compared on measured pI values, two optimized sets, average errors of about 0.87 pH units for proteins and 0.25 for peptides).
[^proteomepi]: [[Kozlowski 2017 - Proteome-pI Proteome Isoelectric Point Database]], *Nucleic Acids Research* 45(D1):D1112-D1116 (predicted pI for 5,029 proteomes with 18 methods, virtual 2D-PAGE; bimodal pI distributions of proteomes).
