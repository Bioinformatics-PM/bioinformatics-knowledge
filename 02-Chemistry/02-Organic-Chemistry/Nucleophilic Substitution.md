---
aliases:
  - SN1
  - SN2
  - SN1 Reaction
  - SN2 Reaction
  - Aliphatic Nucleophilic Substitution
  - Substitution nucléophile
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Nucleophile]]"
  - "[[Electrophile]]"
  - "[[Reaction Mechanism]]"
  - "[[Chirality]]"
  - "[[Rate Law]]"
  - "[[Activation Energy]]"
related:
  - "[[Elimination Reaction]]"
  - "[[Nucleophilic Acyl Substitution]]"
  - "[[Phosphate Ester]]"
  - "[[DNA Methylation]]"
  - "[[DNA Repair]]"
  - "[[Point Mutation]]"
  - "[[Heterocyclic Compound]]"
  - "[[Steady-State Approximation]]"
  - "[[Transition State Theory]]"
projects: []
sources:
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[An Introduction to Genetic Analysis (Griffiths)]]"
  - "[[Wyatt 2006 - Methylating Agents and DNA Repair Responses]]"
---

# Nucleophilic Substitution

> [!abstract]
> In a nucleophilic substitution, an electron-rich nucleophile replaces a leaving group on a saturated carbon, either in one step (SN2: attack from the back, configuration inverted) or in two (SN1: the leaving group departs first and leaves a flat carbocation). Every biological methylation by S-adenosylmethionine is an SN2 reaction, and so is much of the chemical damage that turns DNA bases into mutations.

## Definition

A **nucleophilic substitution** at a saturated (sp³) carbon replaces a leaving group by a nucleophile, Nu:⁻ + R–LG → R–Nu + LG:⁻: the nucleophile brings the electron pair of the new bond and the leaving group takes away the pair of the old one ([[Nucleophile]], [[Electrophile]]).[^os] Two limiting mechanisms are named after the number of molecules in the rate-limiting step. In **SN2** (substitution, nucleophilic, bimolecular) bond making and bond breaking happen together. In **SN1** (unimolecular) the leaving group departs first, giving a carbocation that the nucleophile then captures.[^os][^os114] Substitution at a carbonyl carbon follows a different, addition-elimination path ([[Nucleophilic Acyl Substitution]]).

## Why it matters

- **Methylation.** S-adenosylmethionine (SAM) carries a methyl group on a positively charged sulfur. Methyltransferases transfer that methyl to an acceptor nucleophile by SN2; this is how DNA methylation marks are written ([[DNA Methylation]], [[Epigenetics]]).[^os][^lehninger]
- **Mutagens.** Alkylating agents such as methyl methanesulfonate (MMS), MNNG, ethyl methanesulfonate (EMS) or dimethyl sulfate are electrophiles that substitute alkyl groups onto nucleophilic atoms of DNA bases. Which atom they hit, N7 or O6 of guanine for instance, depends on the agent and decides whether the lesion miscodes ([[Point Mutation]], [[DNA Repair]]).[^wyatt][^lehninger][^griffiths]
- **Mechanism from data.** The rate law separates the two mechanisms: doubling the nucleophile concentration doubles an SN2 rate and leaves an SN1 rate unchanged. Varying one concentration at a time is also how enzyme mechanisms are dissected ([[Rate Law]], [[Michaelis-Menten Kinetics]]).
- **Stereochemistry.** An SN2 step inverts its stereocenter, so a substitution in a pathway fixes the configuration of its product ([[Chirality]]).

## Core (L2)

### Two mechanisms

![[sn1-sn2-energy-profiles.svg]]

**SN2.** The nucleophile attacks the carbon from the side opposite the leaving group (backside attack). In the single transition state, nucleophile and leaving group are both partly bonded, on opposite sides of a carbon whose other three substituents lie in a plane; as the reaction completes, these three flip like an umbrella in the wind, and the configuration is inverted (Walden inversion). The rate is $k[\mathrm{R{-}LG}][\mathrm{Nu}]$.[^os]

**SN1.** The bond to the leaving group breaks first, slowly, and gives a planar carbocation; the nucleophile then adds fast, from either face. The rate is $k[\mathrm{R{-}LG}]$, independent of the nucleophile. A chiral substrate gives a largely racemized product with a small excess of inversion: in one textbook example about 80 % racemization and 20 % inversion, because the departing leaving group stays nearby as an ion pair and shields one face for a moment.[^os114]

### What decides between them

| | SN2 | SN1 |
|---|---|---|
| Steps | one, concerted | two, through a carbocation |
| Rate law | $k[\mathrm{R{-}LG}][\mathrm{Nu}]$ | $k[\mathrm{R{-}LG}]$ |
| Stereochemistry | inversion | racemization, with some inversion |
| Substrate | methyl > primary > secondary; tertiary too hindered | tertiary > secondary: carbocation stability; also allylic and benzylic |
| Nucleophile | must be reactive | weak is enough (water, an alcohol) |
| Leaving group | good (a weak base) | good (a weak base): it leaves in the slow step |
| Solvent | polar aprotic accelerates | polar protic stabilizes the carbocation |

The table summarizes the textbook characteristics of each mechanism.[^os][^os114]

**Leaving groups.** Good leaving groups are weak bases, stable once they carry the electron pair away: I⁻ > Br⁻ > Cl⁻, while HO⁻ and H₂N⁻ are poor ([[Electrophile#Core (L1)]]).[^os] Cells have no alkyl halides; they make hydroxyl groups leave by converting them into phosphate or diphosphate esters, and they methylate from a sulfonium ion, whose leaving group is a neutral thioether ([[Phosphate Ester]]).[^os]

### SAM, the biological SN2

```text
 Nu:  +  H3C–S⁺(Ado)(R)   →   [ Nu···CH3···S(Ado)(R) ]‡   →   Nu⁺–CH3  +  S(Ado)(R)
acceptor   SAM (sulfonium)        backside attack           methylated   S-adenosylhomocysteine
                                                             acceptor     (neutral thioether)
```

- **Why it works.** The positive charge on sulfur pulls electron density from the methyl carbon and turns the leaving group into a neutral thioether, S-adenosylhomocysteine (SAH): an activated methyl donor.[^lehninger][^os]
- **Why SN2.** A methyl carbon is the least hindered SN2 site and the worst SN1 substrate, since a methyl cation is far less stable than a tertiary one (table above).[^os] The methyltransferase holds the acceptor in line with the C–S bond, opposite the sulfur.
- **DNA methylation.** DNA methyltransferases use SAM to methylate C5 of cytosine or N6 of adenine.[^lehninger] The methyl group added to cytosine is what [[Bisulfite Sequencing]] reads, and what [[DNA Methylation]] interprets.

### Alkylating mutagens

DNA bases are nucleophiles, and electrophilic alkylating agents substitute onto several of their atoms.[^wyatt]

- **N7 of guanine** is the main target: N7-methylguanine makes up 67 % of the methylation of double-stranded DNA by MNNG and 82 % by MMS.[^wyatt] N7 is a pyridine-like ring nitrogen ([[Heterocyclic Compound]]) outside the Watson-Crick edge, so the methyl group does not change the pairing pattern.
- **O6 of guanine** is a minor target with major consequences: O⁶-methylguanine pairs with T instead of C, so unrepaired lesions give G:C → A:T transitions after replication; EMS acts the same way through O⁶-ethylguanine.[^lehninger][^griffiths]
- **Agent matters.** MNNG yields a larger share of O-methyl adducts than MMS.[^wyatt] Textbooks call MMS and dimethyl sulfate SN2-type and MNNG and MNU SN1-type agents, a label Wyatt and Pittman qualify (Common misconceptions).[^wyatt]
- **Repair is itself an SN2.** O⁶-methylguanine-DNA methyltransferase transfers the methyl group from O6 of guanine to one of its own cysteine residues, a thiolate attacking the methyl carbon; the protein is inactivated by this single transfer ([[DNA Repair]]).[^lehninger]

## Advanced (L3)

- **Mixed mechanisms.** Secondary substrates often lie between the limits. With both paths open, the substrate decays with $k_\text{obs} = k_1 + k_2[\mathrm{Nu}]$: a plot of $k_\text{obs}$ against $[\mathrm{Nu}]$ has the SN1 constant as intercept and the SN2 constant as slope, and the stereochemical outcome then depends on the nucleophile concentration (Computational representation).
- **Why "first order" is not proof of SN1.** If the nucleophile is the solvent or is in large excess, an SN2 reaction also shows first-order decay of the substrate (pseudo-first order). Only varying $[\mathrm{Nu}]$ separates the cases (Mathematical representation).
- **Where the SN1 rate law comes from.** A two-step mechanism gives a simple rate law only under conditions; the steady-state treatment of the carbocation shows which ([[Steady-State Approximation]], below).
- **From adducts to mutation spectra.** The share of O⁶-alkylguanine among adducts, the capacity of the suicide repair protein and replication timing together decide how many G:C → A:T transitions an exposure leaves, a quantitative chain that links reaction chemistry to the mutation counts of sequencing data ([[Point Mutation]], Exercise 6).

## Mathematical representation

- **SN2.** $v = k_2[\mathrm{R{-}LG}][\mathrm{Nu}]$, with $k_2$ in M⁻¹ s⁻¹. With the nucleophile in large excess, $[\mathrm{Nu}] \approx [\mathrm{Nu}]_0$ and $[\mathrm{R{-}LG}](t) = [\mathrm{R{-}LG}]_0 e^{-k_\text{obs} t}$ with $k_\text{obs} = k_2 [\mathrm{Nu}]_0$.
- **SN1.** $v = k_1[\mathrm{R{-}LG}]$, with $k_1$ in s⁻¹, so $[\mathrm{R{-}LG}](t) = [\mathrm{R{-}LG}]_0 e^{-k_1 t}$ and $t_{1/2} = \ln 2 / k_1$, whatever $[\mathrm{Nu}]$ ([[Rate Law]]).
- **Steady state.** For R–LG ⇌ R⁺ + LG⁻ (rate constants $k_a$ forward, $k_{-a}$ back) followed by R⁺ + Nu → R–Nu ($k_b$), setting $d[\mathrm{R^+}]/dt = 0$ gives
$$v = \frac{k_a k_b [\mathrm{Nu}]\,[\mathrm{R{-}LG}]}{k_{-a}[\mathrm{LG^-}] + k_b[\mathrm{Nu}]} \approx k_a[\mathrm{R{-}LG}] \quad \text{when } k_b[\mathrm{Nu}] \gg k_{-a}[\mathrm{LG^-}],$$
the SN1 rate law: once the carbocation forms, it is captured before the leaving group can return.
- **Both paths.** $k_\text{obs} = k_1 + k_2[\mathrm{Nu}]$; the fraction of product made by SN2 is $f_2 = k_2[\mathrm{Nu}]/k_\text{obs}$.
- **Stereochemical outcome.** If SN2 gives complete inversion and the SN1 path a net inversion excess $e_1$ (0.2 for 80 % racemization and 20 % inversion), the product's excess of inverted configuration is $e = f_2 + (1 - f_2)\, e_1$.
- **Barrier.** Each rate constant reflects the free energy of its highest transition state, $k \propto e^{-\Delta G^\ddagger / RT}$ ([[Transition State Theory]], [[Activation Energy]]).

## Computational representation

Separating SN1 and SN2 contributions from rate constants measured at several nucleophile concentrations, with invented constants and 2 % noise:

```python
import math
import random

# Toy kinetics with invented constants: a secondary substrate that reacts by both paths.
# With the nucleophile in large excess, the substrate decays with k_obs = k1 + k2 [Nu].
K1_TRUE, K2_TRUE = 2.0e-4, 5.0e-3              # s^-1 (SN1) and M^-1 s^-1 (SN2)
random.seed(1)
nu = [0.05, 0.1, 0.2, 0.4, 0.8]                 # M
k_obs = [(K1_TRUE + K2_TRUE * c) * random.gauss(1, 0.02) for c in nu]   # 2 % noise

# Least-squares line k_obs = k1 + k2 [Nu]: intercept = SN1 rate constant, slope = SN2 rate constant
n = len(nu)
mx, my = sum(nu) / n, sum(k_obs) / n
k2 = sum((x - mx) * (y - my) for x, y in zip(nu, k_obs)) / sum((x - mx) ** 2 for x in nu)
k1 = my - k2 * mx
print(f"k1 = {k1:.2e} s^-1 (intercept, SN1)   k2 = {k2:.2e} M^-1 s^-1 (slope, SN2)")

# Share of product made by SN2, and the excess of inverted product, assuming full inversion
# by SN2 and 20 % net inversion by SN1 (80 % racemization + 20 % inversion).
for c in (0.05, 0.8):
    f2 = k2 * c / (k1 + k2 * c)
    excess = f2 * 1.0 + (1 - f2) * 0.2
    half_life = math.log(2) / (k1 + k2 * c) / 60
    print(f"[Nu] = {c:4} M: SN2 share {f2:.2f}, inverted excess {excess:.2f}, half-life {half_life:.0f} min")
```

```text
k1 = 2.28e-04 s^-1 (intercept, SN1)   k2 = 4.85e-03 M^-1 s^-1 (slope, SN2)
[Nu] = 0.05 M: SN2 share 0.52, inverted excess 0.61, half-life 25 min
[Nu] =  0.8 M: SN2 share 0.94, inverted excess 0.96, half-life 3 min
```

The fit recovers the invented constants within the noise (true values $2.0 \times 10^{-4}$ and $5.0 \times 10^{-3}$). At 0.05 M nucleophile, half of the product comes from each path and the product is far from stereochemically pure; at 0.8 M, SN2 dominates. Real kinetic analyses also report uncertainties on the fitted constants ([[Linear Regression]]).

## Worked example

> [!example] Predict the mechanism and the product
> 1. **(R)-2-bromobutane with iodide in acetone.** Secondary carbon, good nucleophile, polar aprotic solvent: SN2. Rate $= k[\mathrm{RBr}][\mathrm{I^-}]$. Backside attack inverts the center, and I takes the CIP rank of Br, so the product is (S)-2-iodobutane (checked in Exercise 4).
> 2. **2-bromo-2-methylpropane in water.** Tertiary carbon (SN2 blocked), weak nucleophile, protic solvent: SN1. Rate $= k[\mathrm{RBr}]$; the product, 2-methylpropan-2-ol, has no stereocenter.
> 3. **SAM and a cytosine in DNA (methyltransferase).** Methyl carbon, sulfonium leaving group: SN2, giving 5-methylcytosine and SAH.[^lehninger]
> 4. **MMS and double-stranded DNA.** SN2-type methylation lands mostly on N7 of guanine (82 %), which does not change pairing; the rarer O⁶-methylguanine is the miscoding lesion.[^wyatt][^lehninger]

## Common misconceptions

> [!warning] "SN2 turns R into S"
> SN2 inverts the geometry. The R/S label flips only when the nucleophile takes the same priority rank as the leaving group; if the ranks of the substituents reshuffle, an inverted product can keep its label (Exercise 4).

> [!warning] "SN1 gives a perfectly racemic product"
> The leaving group lingers as an ion pair and shields one face of the carbocation: one textbook example gives about 80 % racemization and 20 % inversion.[^os114]

> [!warning] "First-order kinetics proves an SN1 mechanism"
> An SN2 reaction with a large excess of nucleophile, or with the solvent as nucleophile, also gives first-order decay of the substrate (pseudo-first order). The test is whether the rate depends on the nucleophile concentration.

> [!warning] "MNNG and MNU methylate DNA through a free methyl cation"
> They are commonly called SN1-type agents, but Wyatt and Pittman point out that a true SN1 mechanism would require a free methyl carbocation, and that the label is therefore inaccurate; they describe these agents as more oxyphilic, giving more O-methyl adducts than MMS.[^wyatt]

> [!warning] "The most frequent DNA adduct is the most dangerous"
> N7-methylguanine is the main adduct (67 to 82 % of methylation in double-stranded DNA), but O⁶-methylguanine, much rarer, is the one that pairs with T and produces transitions.[^wyatt][^lehninger]

## Exercises

> [!question] Exercise 1 (L2)
> Give the mechanism, the rate law and the stereochemical outcome: (a) CH₃–I with CH₃S⁻ in a polar aprotic solvent; (b) 2-bromo-2-methylpropane in water; (c) (S)-2-bromobutane with I⁻ in acetone; (d) SAM with the N6 amino group of an adenine in DNA, in the active site of a methyltransferase.

> [!success]- Solution
> (a) SN2 (methyl carbon, strong nucleophile): rate $= k[\mathrm{CH_3I}][\mathrm{CH_3S^-}]$; no stereocenter. (b) SN1 (tertiary): rate $= k[\mathrm{RBr}]$; 2-methylpropan-2-ol, no stereocenter. (c) SN2: rate $= k[\mathrm{RBr}][\mathrm{I^-}]$; (R)-2-iodobutane, by inversion with I taking the rank of Br. (d) SN2 at the methyl carbon of SAM: N6-methyladenine and SAH.[^lehninger]

> [!question] Exercise 2 (L2)
> Initial rates (invented data) for two substrates:
>
> | Substrate | [R–LG] (M) | [Nu] (M) | $v_0$ (M s⁻¹) |
> |---|---:|---:|---:|
> | A | 0.10 | 0.10 | 2.0 × 10⁻⁵ |
> | A | 0.20 | 0.10 | 4.0 × 10⁻⁵ |
> | A | 0.10 | 0.20 | 4.0 × 10⁻⁵ |
> | B | 0.10 | 0.10 | 3.0 × 10⁻⁶ |
> | B | 0.20 | 0.10 | 6.0 × 10⁻⁶ |
> | B | 0.10 | 0.20 | 3.0 × 10⁻⁶ |
>
> Find the orders, the rate constants and the likely mechanism of each.

> [!success]- Solution
> A: doubling [R–LG] doubles $v_0$ (first order), doubling [Nu] doubles it (first order): $v = k[\mathrm{R{-}LG}][\mathrm{Nu}]$ with $k = 2.0 \times 10^{-5} / (0.10 \times 0.10) = 2.0 \times 10^{-3}$ M⁻¹ s⁻¹, SN2. B: first order in substrate, zero order in nucleophile: $v = k[\mathrm{R{-}LG}]$ with $k = 3.0 \times 10^{-6} / 0.10 = 3.0 \times 10^{-5}$ s⁻¹, SN1 ([[Rate Law]]).

> [!question] Exercise 3 (L2)
> The methyl group of SAM is transferred readily; the methyl group of methionine, the same CH₃–S bond on a neutral thioether, is not. Explain with the leaving group.

> [!success]- Solution
> In SAM the sulfur is positively charged (sulfonium). When the methyl is attacked, the sulfur keeps the electron pair and leaves as a neutral thioether, SAH: a very weak base, hence an excellent leaving group, and the positive sulfur also makes the methyl carbon more electrophilic.[^lehninger] In methionine the leaving group would have to be a thiolate anion, a stronger base and a poorer leaving group, attached to an uncharged sulfur. Activation by adenosylation is the cell's way of building a good leaving group ([[Electrophile]]).

> [!question] Exercise 4 (L3, Python)
> Model the umbrella inversion with vectors: place the leaving group on $+z$ and the three other groups below, let the nucleophile enter on $-z$ while the three groups flip to $+z$, and read R or S from the signed volume of the groups ranked 1, 2, 3. Apply it to (R)-2-bromobutane + I⁻ and to (R)-2-bromo-1-fluoropropane + CN⁻ (where CH₂F outranks CN, since F outranks N).

> [!success]- Solution
> ```python
> def tet(azimuth_deg: float, z: float) -> tuple[float, float, float]:
>     """Unit vector from the stereocenter at a given azimuth and height."""
>     r = math.sqrt(1 - z * z)
>     return (r * math.cos(math.radians(azimuth_deg)), r * math.sin(math.radians(azimuth_deg)), z)
>
>
> def signed_volume(a, b, c) -> float:
>     """a . (b x c)"""
>     return (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0])
>             + a[2] * (b[0] * c[1] - b[1] * c[0]))
>
>
> def descriptor(pos: dict, ranking: list) -> str:
>     """R when groups ranked 1 -> 2 -> 3 turn clockwise with group 4 pointing away."""
>     return "R" if signed_volume(*(pos[g] for g in ranking[:3])) < 0 else "S"
>
>
> def sn2(pos: dict, leaving: str, nucleophile: str) -> dict:
>     """Backside attack: Nu enters opposite the leaving group, the other three flip like an umbrella."""
>     new = {g: (x, y, -z) for g, (x, y, z) in pos.items() if g != leaving}
>     new[nucleophile] = tuple(-c for c in pos[leaving])
>     return new
>
>
> ref = {"1": tet(90, 1 / 3), "2": tet(-30, 1 / 3), "3": tet(-150, 1 / 3), "4": (0, 0, -1)}
> print("reference (clockwise 1-2-3):", descriptor(ref, ["1", "2", "3", "4"]))
> for other, nu_, rank_sub, rank_prod in (
>         ("CH2F", "CN", ["Br", "CH2F", "CH3", "H"], ["CH2F", "CN", "CH3", "H"]),
>         ("C2H5", "I", ["Br", "C2H5", "CH3", "H"], ["I", "C2H5", "CH3", "H"])):
>     sub = {"Br": (0, 0, 1), other: tet(0, -1 / 3), "H": tet(120, -1 / 3), "CH3": tet(240, -1 / 3)}
>     prod = sn2(sub, "Br", nu_)
>     print(f"{other:4} + {nu_:2}: {descriptor(sub, rank_sub)} -> {descriptor(prod, rank_prod)}")
> ```
> Output: `reference (clockwise 1-2-3): R`, then `CH2F + CN: R -> R` and `C2H5 + I : R -> S`. The reference arrangement (groups 1, 2, 3 at azimuths 90°, −30°, −150° seen from above, group 4 pointing down) turns clockwise and gives a negative signed volume, which fixes the convention ([[Stereochemistry#Mathematical representation]]). Both substitutions invert the geometry; only the second flips the label, because iodide takes rank 1 like bromide, whereas cyanide takes rank 2 behind CH₂F.

> [!question] Exercise 5 (L3)
> With the fitted constants of the Computational representation, at which nucleophile concentration do SN1 and SN2 contribute equally, and what is the excess of inverted product there? Under which condition on the steady-state rate law would the SN1 path itself start to depend on $[\mathrm{Nu}]$?

> [!success]- Solution
> Equal contributions when $k_2[\mathrm{Nu}] = k_1$: $[\mathrm{Nu}] = 2.28 \times 10^{-4} / 4.85 \times 10^{-3} \approx 0.047$ M. Then $f_2 = 0.5$ and $e = 0.5 + 0.5 \times 0.2 = 0.6$. The SN1 path depends on $[\mathrm{Nu}]$ when $k_b[\mathrm{Nu}]$ is no longer large compared with $k_{-a}[\mathrm{LG^-}]$: if the leaving group accumulates (or the nucleophile is scarce) and recaptures the carbocation, the full steady-state expression applies.

> [!question] Exercise 6 (L3)
> Toy numbers, invented for the exercise: a cell holds $10^5$ molecules of O⁶-methylguanine-DNA methyltransferase, and 5 % of the methylations made by an agent are O⁶-methylguanine. Each repair protein can act once. How many O⁶-methylguanines remain after doses that make $10^6$ and $10^7$ methylations per genome, assuming repair happens before replication? What does the result say about dose-response curves for mutations?

> [!success]- Solution
> $10^6 \times 0.05 = 5 \times 10^4$ lesions, fewer than $10^5$ proteins: all repaired, about $5 \times 10^4$ protein molecules consumed. $10^7 \times 0.05 = 5 \times 10^5$ lesions: only $10^5$ repaired, $4 \times 10^5$ remain, each able to give a G:C → A:T transition at the next replication. Because the protein is used up by a single transfer,[^lehninger] protection is a fixed budget: below it, few mutations; above it, mutations rise steeply with dose, a threshold that a model of linear damage would miss.

## Mastery checklist

- [ ] 1 Recognized: I can name the nucleophile, electrophilic carbon and leaving group in a substitution, and state the rate laws of SN1 and SN2.
- [ ] 2 Understood: I can predict the mechanism from substrate, nucleophile, leaving group and solvent, and explain inversion and racemization.
- [ ] 3 Practiced: I can extract $k_1$ and $k_2$ from kinetic data, derive the SN1 rate law with the steady-state approximation, and assign R/S after an inversion.
- [ ] 4 Applied: I related an alkylating exposure (for example in a mutagenesis or chemotherapy dataset) to the expected excess of G:C → A:T transitions in sequencing data.
- [ ] 5 Explained: I can teach why SAM is an SN2 methyl donor, why N7 and O6 adducts of guanine differ in consequence, and the limits of the SN1/SN2 labels for alkylating agents.

## References

[^os]: [[Organic Chemistry (OpenStax)]], treatment of nucleophilic substitution of alkyl halides (SN2: backside attack, Walden inversion, second-order rate law, substrate, nucleophile, leaving-group and solvent effects; characteristics of the SN1 reaction; biological substitutions with diphosphate leaving groups and with S-adenosylmethionine) (section numbers not verified, except sec. 11.4 below).
[^os114]: [[Organic Chemistry (OpenStax)]], sec. 11.4 "The SN1 Reaction" (two steps through a carbocation, first-order kinetics, about 80 % racemization and 20 % inversion explained by ion pairs).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of S-adenosylmethionine as methyl donor (sulfonium ion), DNA methylation (C5 of cytosine, N6 of adenine), alkylating agents (O⁶-methylguanine pairs with T) and direct repair by O⁶-methylguanine-DNA methyltransferase (methyl transferred to a Cys of the protein, which is inactivated).
[^griffiths]: [[An Introduction to Genetic Analysis (Griffiths)]], 7th ed. (2000), treatment of mutagens (ethyl methanesulfonate; O⁶-ethylguanine pairs with T, giving G:C → A:T transitions).
[^wyatt]: [[Wyatt 2006 - Methylating Agents and DNA Repair Responses]], *Chemical Research in Toxicology* 19(12):1580-1594 (sites methylated by MMS and MNNG, N7-methylguanine as 67 % and 82 % of methylation of double-stranded DNA, larger share of O-methyl adducts with MNNG, critique of the SN1 label).
