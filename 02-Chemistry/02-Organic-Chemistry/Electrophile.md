---
aliases:
  - Electrophilicity
  - Electrophilic Center
  - Électrophile
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Nucleophile]]"
  - "[[Reaction Mechanism]]"
  - "[[Electronegativity]]"
  - "[[Functional Group]]"
related:
  - "[[Carbonyl Group]]"
  - "[[Phosphate Ester]]"
  - "[[Nucleophilic Substitution]]"
  - "[[Nucleophilic Acyl Substitution]]"
  - "[[Hydrolysis]]"
  - "[[ATP]]"
projects: []
sources:
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Chemistry 2e (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
---

# Electrophile

> [!abstract]
> An electrophile is the electron-poor partner of a polar reaction: an atom that can accept a pair of electrons from a nucleophile to make a new bond.

## Definition

An **electrophile** ("electron-loving") is a species with a positively polarized, electron-poor atom that forms a bond by accepting an electron pair from a [[Nucleophile]]. It can be neutral or positively charged; electrophiles are Lewis acids.[^os63] In curved-arrow notation, the electrophile is where the arrow ends ([[Reaction Mechanism]]).[^os65] To accept a pair without exceeding an octet, the electrophilic atom either has an empty orbital (H⁺, a carbocation, a metal ion) or releases another pair at the same time, into a π bond to oxygen or to a **leaving group**.[^os63][^os65]

## Why it matters

- **Activated metabolites are electrophiles.** Biology stores reactivity in a few electrophilic groups: the thioester carbon of acetyl-CoA, the phosphorus atoms of ATP, the methyl group of S-adenosylmethionine (SAM). Recognizing the electrophile tells which bond a pathway step will make or break ([[ATP]], [[Metabolism]]).[^berg][^os116]
- **Stability of biopolymers.** The amide carbon of the [[Peptide Bond]] is a poor electrophile, one reason proteins survive in water until a protease attacks.[^os212][^berg]
- **DNA damage.** Alkylating agents are electrophiles that attach alkyl groups to nucleophilic atoms of the bases, for example converting guanine to O⁶-methylguanine, which mispairs ([[DNA Repair]], [[Nucleophilic Substitution]]).[^lehninger]

## Core (L1)

**Three electrophilic centers of biochemistry.**

| Center | Why electron-poor | Leaving pair goes to | Example |
|---|---|---|---|
| Carbonyl carbon (C=O) | O pulls the π electrons: C is δ+ | the π bond, onto O | aldehydes, ketones, esters, thioesters, amides[^os63][^os212] |
| Phosphorus of a phosphate group | bonded to four electronegative O atoms | the leaving phosphate or alcohol | ATP in kinase reactions, the DNA backbone[^berg][^lehninger] |
| sp³ carbon bearing a leaving group | bond to a more electronegative or positively charged atom | the leaving group | alkyl halides; CH₃ of SAM (CH₃–S⁺)[^os113][^os116] |

**Also electrophiles:** H⁺ (the electrophile of every protonation), carbocations, and metal ions such as Mg²⁺ and Zn²⁺, which accept lone pairs from water or phosphate oxygens.[^os63][^berg]

**Leaving groups.** At an sp³ carbon, the electrophile is only as good as its leaving group, and the best leaving groups are weak bases, stable as anions: I⁻ > Br⁻ > Cl⁻, while HO⁻, RO⁻ and H₂N⁻ are poor.[^os113] Cells cannot use halides, so they convert a poor –OH leaving group into a phosphate or diphosphate, the biological equivalent of a halide.[^os116]

**Acyl derivatives are not equally electrophilic.** Toward nucleophiles: acid anhydride > thioester > ester > amide. A substituent that donates its lone pair into the carbonyl by resonance (strongly the amide N, weakly the S of a thioester) makes the carbon less positive.[^os212] Thioesters (acetyl-CoA) are therefore "activated", amides (peptide bonds) are not ([[Nucleophilic Acyl Substitution]]).

## Deeper (L2)

**Enzymes make electrophiles more electrophilic.**

- **Oxyanion hole.** In serine proteases, backbone N–H groups hydrogen-bond the negatively charged oxygen of the tetrahedral intermediate, stabilizing it and the transition state that leads to it.[^berg]
- **Metal ions on phosphate.** Mg²⁺ binds the phosphate oxygens of ATP; most kinases use the Mg²⁺–ATP complex, in which the metal partly neutralizes the negative charges around phosphorus.[^berg][^lehninger] The attacking nucleophile (a substrate hydroxyl) is then less repelled.
- **Protonation.** A general acid that protonates a carbonyl oxygen, or a leaving group, makes the carbon more positive and the departure easier.[^berg]

**Positive charge turns a methyl into an electrophile.** In SAM the methyl group is bonded to a positively charged sulfonium sulfur; a nucleophile (an O, N or C of the acceptor) attacks the methyl carbon and the neutral thioether S-adenosylhomocysteine leaves. This SN2 step is the methyl transfer of biological methylations, including [[DNA Methylation]].[^os116]

## Mathematical representation

Electronegativity gives a first guess of the partial charges. For a bond A–B with Pauling electronegativities $\chi_A$ and $\chi_B$, the bonding electrons shift toward the more electronegative atom, and the other atom carries $\delta+$ when $\Delta\chi = \chi_B - \chi_A > 0$ ([[Electronegativity]]).[^chem2e] This is a heuristic, not a measure of reactivity: electrophilicity also depends on resonance donation, the quality of the leaving group and the charges around the center.

## Computational representation

```python
# Pauling electronegativities as tabulated in Chemistry 2e (one decimal).
EN = {"H": 2.1, "C": 2.5, "N": 3.0, "O": 3.5, "P": 2.1, "S": 2.5, "Cl": 3.0}


def polarity(a: str, b: str) -> str:
    d = round(EN[b] - EN[a], 1)
    if d == 0:
        return f"{a}-{b}: ΔEN 0.0, no partial charges"
    plus, minus = (a, b) if d > 0 else (b, a)
    return f"{a}-{b}: ΔEN {abs(d):.1f}, {plus} is δ+ (electron-poor), {minus} is δ-"


for a, b in [("C", "O"), ("P", "O"), ("C", "Cl"), ("C", "N"), ("C", "S"), ("C", "H")]:
    print(polarity(a, b))
```

```text
C-O: ΔEN 1.0, C is δ+ (electron-poor), O is δ-
P-O: ΔEN 1.4, P is δ+ (electron-poor), O is δ-
C-Cl: ΔEN 0.5, C is δ+ (electron-poor), Cl is δ-
C-N: ΔEN 0.5, C is δ+ (electron-poor), N is δ-
C-S: ΔEN 0.0, no partial charges
C-H: ΔEN 0.4, H is δ+ (electron-poor), C is δ-
```

The table finds the carbonyl carbon, the phosphorus of phosphate and the carbon of C–Cl, but it also shows its limits: the C–S bond looks nonpolar although thioester carbons are good electrophiles, and the SAM methyl is electrophilic because of the positive charge on sulfur, which electronegativity alone ignores.

## Worked example

> [!example] Where will a nucleophile attack acetyl-CoA?
> Acetyl-CoA is CH₃–C(=O)–S–CoA.
> 1. **Candidates.** The carbonyl carbon (bonded to O by a double bond and to S), the methyl carbon, the sulfur.
> 2. **Polarity.** C=O: C is δ+ (ΔEN 1.0). C–S: ΔEN 0, but sulfur barely donates its lone pair into the carbonyl, so the carbonyl carbon stays strongly δ+.[^os212]
> 3. **Leaving group.** After attack, the π electrons return to re-form C=O and the C–S bond breaks: CoA–S⁻ leaves, a good leaving group (thiolate).
> 4. **Answer.** The carbonyl carbon is the electrophile; acetyl-CoA transfers its acetyl group to nucleophiles ([[Nucleophilic Acyl Substitution]]). The amide analogue would be far less reactive.[^os212]

## Common misconceptions

> [!warning] "Electrophiles must carry a positive charge"
> Most biological electrophiles are neutral: carbonyl carbons and phosphorus atoms are only partially positive. A charge helps (H⁺, SAM's sulfonium) but is not required.[^os63]

> [!warning] "The more polar the bond, the more reactive the electrophile"
> Esters and amides both carry a polar C=O, yet amides are much less reactive: the nitrogen lone pair feeds the carbonyl by resonance, lowering the carbon's positive character, and an amide nitrogen is a poor leaving group.[^os212]

> [!warning] "The leaving group does not matter for the electrophile"
> At an sp³ carbon, a methyl bonded to –OH does not react with nucleophiles, while the same methyl bonded to a sulfonium (SAM) or a halide does: the leaving group decides.[^os113][^os116]

## Exercises

> [!question] Exercise 1 (L1)
> Name the electrophilic atom in acetaldehyde (CH₃CHO), chloromethane (CH₃Cl), H₃O⁺ and ATP during a kinase reaction.

> [!success]- Solution
> The carbonyl carbon of acetaldehyde; the carbon of CH₃Cl (Cl leaves); an H of H₃O⁺ (water leaves); the γ (terminal) phosphorus of ATP, attacked by the substrate hydroxyl, with ADP as the leaving group.[^os63][^berg]

> [!question] Exercise 2 (L1)
> Which is the better leaving group, Cl⁻ or HO⁻? What do cells use instead of halides to activate an alcohol?

> [!success]- Solution
> Cl⁻, a much weaker base, stable as an anion; HO⁻ is a strong base and a poor leaving group. Cells phosphorylate or diphosphorylate the –OH, turning it into a good phosphate or diphosphate leaving group.[^os113][^os116]

> [!question] Exercise 3 (L2)
> Rank a thioester, an ester and an amide by their electrophilicity toward water, and explain with resonance. Why does this ranking suit acetyl-CoA as a carrier and proteins as structural polymers?

> [!success]- Solution
> Thioester > ester > amide.[^os212] Donation of the heteroatom's lone pair into C=O reduces the carbon's positive character: weak for S (poor overlap of its larger orbitals with carbon's), stronger for O, strongest for N. Acetyl-CoA must hand over its acyl group easily; proteins must not fall apart in water. Enzymes then supply what the amide lacks (an activated nucleophile, an oxyanion hole).[^berg]

> [!question] Exercise 4 (L2, Python)
> Use `polarity` on the bonds of a phosphate ester fragment, C–O–P: which atoms are δ+? Then name one fact the electronegativity model misses for each of P and C.

> [!success]- Solution
> The code output gives C–O: C is δ+ (ΔEN 1.0) and P–O: P is δ+ (ΔEN 1.4). Both are candidate electrophiles. Missing for P: it is bonded to four oxygens, some negatively charged, which repel the nucleophile unless Mg²⁺ or positive residues shield them.[^berg] Missing for C: attack at carbon requires the phosphate to leave from an sp³ carbon (an SN2 step), a question of leaving-group quality that ΔEN does not capture.

## Mastery checklist

- [ ] 1 Recognized: I can point to the carbonyl carbon, the phosphate phosphorus and a carbon bearing a leaving group as electrophiles.
- [ ] 2 Understood: I can explain why each is electron-poor and where the displaced electron pair goes.
- [ ] 3 Practiced: I can rank acyl derivatives and leaving groups and predict the attacked atom in a metabolite.
- [ ] 4 Applied: I identified the electrophilic atom and leaving group of a real enzyme-catalyzed reaction from a pathway database or a structure with its ligand.
- [ ] 5 Explained: I can explain how activated carriers (acetyl-CoA, ATP, SAM) and enzymes (oxyanion hole, Mg²⁺) tune electrophilicity.

## References

[^os63]: [[Organic Chemistry (OpenStax)]], sec. 6.3 "Polar Reactions".
[^os65]: [[Organic Chemistry (OpenStax)]], sec. 6.5 "Using Curved Arrows in Polar Reaction Mechanisms".
[^os113]: [[Organic Chemistry (OpenStax)]], sec. 11.3 "Characteristics of the SN2 Reaction" (leaving groups).
[^os116]: [[Organic Chemistry (OpenStax)]], sec. 11.6 "Biological Substitution Reactions".
[^os212]: [[Organic Chemistry (OpenStax)]], sec. 21.2 "Nucleophilic Acyl Substitution Reactions".
[^chem2e]: [[Chemistry 2e (OpenStax)]], ch. 7 "Chemical Bonding and Molecular Geometry", §7.2 "Covalent Bonding" (electronegativity, Pauling values, bond polarity).
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021).
