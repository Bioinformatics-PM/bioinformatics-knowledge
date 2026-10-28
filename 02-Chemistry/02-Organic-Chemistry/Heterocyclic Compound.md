---
aliases:
  - Heterocycle
  - Aromatic Heterocycle
  - Nitrogen Heterocycle
  - Composé hétérocyclique
  - Hétérocycle
tags:
  - type/concept
  - domain/chemistry
  - domain/biology
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Aromaticity]]"
  - "[[Functional Group]]"
  - "[[Orbital Hybridization]]"
  - "[[Acid-Base Equilibrium]]"
  - "[[Henderson-Hasselbalch Equation]]"
related:
  - "[[Nucleotide]]"
  - "[[Base Pairing]]"
  - "[[Amino Acid]]"
  - "[[Cofactor]]"
  - "[[Tautomer]]"
  - "[[Organic Redox Reaction]]"
  - "[[Enzyme Catalysis]]"
  - "[[Nucleophilic Substitution]]"
  - "[[Molecular Representation]]"
projects: []
sources:
  - "[[Organic Chemistry (OpenStax)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Lehninger Principles of Biochemistry (Nelson)]]"
  - "[[OpenSMILES Specification]]"
  - "[[Wyatt 2006 - Methylating Agents and DNA Repair Responses]]"
---

# Heterocyclic Compound

> [!abstract]
> A heterocycle is a ring that contains at least one atom other than carbon, most often nitrogen. Nitrogen heterocycles spell the genetic alphabet and build histidine, tryptophan, NAD⁺ and heme; whether each ring nitrogen can take up a proton decides how these molecules pair, bind metals and catalyze reactions.

## Definition

A **heterocyclic compound**, or heterocycle, is a cyclic compound whose ring contains atoms of more than one element, usually carbon together with nitrogen, oxygen or sulfur.[^os155] Heterocycles can be saturated, like the five-membered ring that proline closes through its backbone nitrogen,[^lehninger] or aromatic, like pyridine and pyrrole, which satisfy Hückel's rule with a heteroatom in the ring ([[Aromaticity]]).[^os155] Rings can be fused: indole is a benzene ring fused to a pyrrole, purine a pyrimidine fused to an imidazole ([[Aromaticity#Core (L1)]]). Sugar rings are oxygen heterocycles, and their names say so: pyranoses resemble pyran, furanoses furan ([[Carbohydrate]]).[^lehninger]

## Why it matters

- **The genetic alphabet.** A and G are purines, C, T and U pyrimidines ([[Nucleotide]]).[^os28] Their ring nitrogens and exocyclic groups fix the pattern of hydrogen-bond donors and acceptors read in [[Base Pairing]]; moving a proton to another atom of the same ring gives [[Tautomer|tautomers]] that mispair.
- **Catalysis.** The imidazole ring of histidine has a pKa near 6, so near pH 7 it exists in both its protonated and neutral forms and can accept a proton and give it back during catalysis ([[Enzyme Catalysis]], [[Amino Acid]]).[^berg]
- **Cofactors.** NAD⁺ carries hydride on a pyridinium ring, heme holds iron inside four linked pyrroles, and pyridoxal phosphate (PLP) is a pyridine ([[Cofactor]]).[^os249][^berg][^lehninger]
- **Files and models.** In SMILES, aromatic ring atoms are lowercase and a pyrrole-like nitrogen is written `[nH]`, with its hydrogen explicit; toolkits still disagree in edge cases about implicit hydrogens on aromatic atoms other than carbon, so heterocycles deserve a check whenever structures are converted between formats ([[Molecular Representation]]).[^opensmiles] In a protein model without hydrogens, a neutral His ring may carry its hydrogen on either nitrogen, and the choice changes the hydrogen-bond network: modeling software has to decide ([[Tautomer]]).
- **Drugs.** Heterocycles are common in pharmaceuticals; sildenafil is one example ([[Drug Discovery]]).[^os249]

## Core (L2)

### Six rings to recognize

![[nitrogen-heterocycles-basicity.svg]]

The nitrogen rings of biochemistry:[^os155][^os249][^os26][^os28]

| Ring | Size | Ring nitrogens | π electrons | In biology |
|---|---|---|---:|---|
| pyridine | 6 | one, pyridine-like | 6 | nicotinamide ring of NAD⁺; PLP |
| pyrimidine | 6 | two (positions 1 and 3), pyridine-like | 6 | C, T, U |
| pyrrole | 5 | one N–H | 6 | four per porphyrin (heme) |
| imidazole | 5 | two (1 and 3): one N–H, one pyridine-like | 6 | His side chain |
| indole | 6 + 5, fused | one N–H | 10 | Trp side chain |
| purine | 6 + 5, fused | four: N1, N3, N7 pyridine-like, N9–H | 10 | A, G |

### Two kinds of ring nitrogen

- **Pyridine-like nitrogen** (doubly bonded in the ring, no H). Its lone pair sits in an sp² orbital in the plane of the ring, outside the aromatic π system.[^os155] It can accept a proton, a metal ion or a hydrogen bond without disturbing aromaticity: a basic site and an acceptor.
- **Pyrrole-like nitrogen** (N–H in a five-membered aromatic ring). Its lone pair occupies a p orbital and supplies two of the six π electrons.[^os155] Protonating it would pull those electrons out of the aromatic system, so pyrrole is a very weak base, and its N–H is a hydrogen-bond donor.[^os249]
- **Amide-like ring N–H** (N1 of G, N3 of T and U in their usual keto forms) behaves like the pyrrole type: the lone pair is shared with the neighbouring C=O, as in any amide, so it is not basic and the N–H is a donor ([[Functional Group]]).

### Basicity in numbers

The basicity of a nitrogen is reported as the pKa of its protonated form (the conjugate acid): the higher the pKa, the stronger the base ([[Acid-Base Equilibrium]]).

| Nitrogen | pKa of the protonated form | Reason |
|---|---:|---|
| pyrrole | 0.4[^os243] | the lone pair belongs to the aromatic sextet |
| pyrimidine | 1.3[^os243] | pyridine-like, weakened by the second, electron-withdrawing ring N |
| pyridine | 5.25[^os243] | sp² lone pair: free, but held closer to the nucleus than an sp³ pair ([[Orbital Hybridization]]) |
| imidazole | 6.95[^os243] | protonation of N3 gives a cation whose charge is shared by both nitrogens |
| His side chain in proteins | about 6.0[^berg] | imidazole in a protein environment |
| Lys side chain (sp³ alkylamine) | about 10.8[^berg] | localized lone pair, for comparison |

Arylamines and the heterocyclic amines are much weaker bases than alkylamines.[^os243] At pH 7.4 the Henderson-Hasselbalch relation gives the protonated fractions (code below): pyridine 0.7 %, His 4 %, free imidazole 26 %, Lys essentially 100 %, pyrimidine and pyrrole rings essentially 0.

### The biological rings

- **Nucleobases.** Purines bond the sugar through N9, pyrimidines through N1 ([[Nucleotide]]).[^berg] Among the remaining ring atoms, pyridine-like acceptors (N1 of A, N3 of C) and N–H donors (N1 of G, N3 of T) face the partner base in Watson-Crick pairs ([[Base Pairing]]). N7 of the purines is a pyridine-like nitrogen off the pairing edge; N7 of guanine is the site most methylated by alkylating agents in double-stranded DNA ([[Nucleophilic Substitution]]).[^wyatt]
- **Histidine.** Protonating the pyridine-like nitrogen gives the imidazolium cation, which keeps six π electrons and stays aromatic ([[Aromaticity#Deeper (L2)]]). With a pKa near 6, both forms coexist at pH 7, which suits His to proton shuttling, as in the Ser-His-Asp triad of serine proteases ([[Nucleophile#Deeper (L2)]]).[^berg]
- **Tryptophan.** The indole N–H is pyrrole-like, so Trp is not a base; it donates a hydrogen bond, and its large aromatic ring makes it the main protein absorber at 280 nm.[^lehninger]
- **NAD⁺.** Nicotinamide is a pyridine carrying a carboxamide at C3. In NAD⁺ the ring nitrogen is bonded to a ribose and positively charged, a pyridinium ion. The ring accepts a hydride ion (a proton with two electrons) at C4 to give NADH, in which C4 is sp³ and the ring is no longer aromatic ([[Organic Redox Reaction]]).[^lehninger][^berg] NADH absorbs light at 340 nm and NAD⁺ does not, which is how dehydrogenase reactions are followed in a spectrophotometer ([[Beer-Lambert Law]]).[^lehninger]
- **Heme.** Protoporphyrin consists of four pyrrole rings linked by methine bridges into one large ring; its central iron is bonded to the four pyrrole nitrogens. In myoglobin and hemoglobin a fifth bond goes to the imidazole of the proximal histidine, and O₂ binds at the sixth site.[^berg]

## Advanced (L3)

- **pKa values move.** Table values are averages. Inside a folded protein the environment shifts side-chain pKa values, and active sites exploit it ([[Nucleophile#Deeper (L2)]]).[^berg] His is the most sensitive case: with a pKa near 7, a shift of one unit changes its dominant state.
- **Protonation microstates.** A molecule with $m$ titratable sites has $2^m$ protonation microstates (Mathematical representation), and a neutral His adds a further choice, the nitrogen that carries the hydrogen. Structure preparation for simulation or [[Molecular Docking]] must pick one state per residue or ligand, or sample several.
- **Beyond nitrogen.** Thiamine pyrophosphate carries a thiazolium ring (N and S) and flavins a tricyclic isoalloxazine; their ring chemistry is what makes them cofactors ([[Cofactor]]).[^lehninger][^berg]

## Mathematical representation

- **Protonated fraction.** For a ring nitrogen whose protonated form has acid dissociation constant $K_a$ ($\mathrm{p}K_a = -\log_{10} K_a$), the fraction protonated at a given pH is
$$\theta(\mathrm{pH}) = \frac{1}{1 + 10^{\,\mathrm{pH} - \mathrm{p}K_a}}$$
([[Henderson-Hasselbalch Equation]]). Far above both pKa values, two rings differ in protonated fraction by about $10^{\mathrm{p}K_{a,1} - \mathrm{p}K_{a,2}}$.
- **π count.** With $e_j$ the π electrons supplied by ring atom $j$ (1 for a carbon of a C=C or a pyridine-like N, 2 for a pyrrole-like N–H), $n_\pi = \sum_j e_j$, and a planar, fully conjugated ring is aromatic when $n_\pi = 4n + 2$ ([[Aromaticity#Mathematical representation]]). Imidazole: $3 \times 1 + 1 + 2 = 6$; purine: 5 carbons, 3 pyridine-like N and 1 N–H give $5 + 3 + 2 = 10$.
- **Microstates.** For $m$ independent sites with fractions $\theta_i$, the microstate $\sigma \in \{0, 1\}^m$ (1 = protonated) has probability $\prod_i \theta_i^{\sigma_i} (1 - \theta_i)^{1 - \sigma_i}$. For $m$ identical sites the number protonated follows a binomial distribution $\mathrm{Bin}(m, \theta)$ with mean $m\theta$ ([[Binomial Distribution]]). Real neighbouring sites interact, so independence is a first approximation.

## Computational representation

SMILES encodes the two kinds of nitrogen directly: `n` is pyridine-like, `[nH]` an aromatic N–H, `[n+]` a pyridinium.[^opensmiles] The toy strings below were written for this note (purines as their N9–H forms).

```python
import re

# Toy SMILES written for this note (purines as their N9-H tautomers, free bases).
RINGS = {
    "pyridine": "c1ccncc1", "pyrimidine": "c1cncnc1", "pyrrole": "c1cc[nH]c1",
    "imidazole": "c1c[nH]cn1", "indole": "c1ccc2[nH]ccc2c1", "purine": "c1ncc2[nH]cnc2n1",
    "adenine": "Nc1ncnc2[nH]cnc12", "guanine": "Nc1nc2[nH]cnc2c(=O)[nH]1",
    "cytosine": "Nc1cc[nH]c(=O)n1", "thymine": "Cc1c[nH]c(=O)[nH]c1=O",
    "nicotinamide": "NC(=O)c1cccnc1",
}
ATOM = re.compile(r"\[[^\]]+\]|Br|Cl|[BCNOPSFI]|[bcnops]")   # bracket atoms, then the organic subset


def nitrogen_types(smiles: str) -> dict[str, int]:
    """Count nitrogen atoms by type from their SMILES token."""
    counts = {"pyridine-like": 0, "pyrrole-like N-H": 0, "cationic ring N": 0, "non-aromatic N": 0}
    for tok in ATOM.findall(smiles):
        if tok == "n":
            counts["pyridine-like"] += 1        # lone pair in the ring plane
        elif tok == "[nH]":
            counts["pyrrole-like N-H"] += 1     # lone pair inside the pi system
        elif tok.startswith("[n") and "+" in tok:
            counts["cationic ring N"] += 1      # pyridinium, as in NAD+
        elif tok == "N" or tok.startswith("[N"):
            counts["non-aromatic N"] += 1       # amino or amide nitrogen
    return {k: v for k, v in counts.items() if v}


for name, smi in RINGS.items():
    print(f"{name:12} {nitrogen_types(smi)}")


def protonated_fraction(pka: float, ph: float) -> float:
    """Henderson-Hasselbalch: fraction of the group carrying the extra proton."""
    return 1 / (1 + 10 ** (ph - pka))


PKA = {"pyrrole": 0.4, "pyrimidine": 1.3, "pyridine": 5.25, "His side chain": 6.0,
       "imidazole": 6.95, "Lys side chain": 10.8}
for name, pka in PKA.items():
    print(f"{name:15} pKa {pka:5}  protonated at pH 7.4: {protonated_fraction(pka, 7.4):.2g}")
```

```text
pyridine     {'pyridine-like': 1}
pyrimidine   {'pyridine-like': 2}
pyrrole      {'pyrrole-like N-H': 1}
imidazole    {'pyridine-like': 1, 'pyrrole-like N-H': 1}
indole       {'pyrrole-like N-H': 1}
purine       {'pyridine-like': 3, 'pyrrole-like N-H': 1}
adenine      {'pyridine-like': 3, 'pyrrole-like N-H': 1, 'non-aromatic N': 1}
guanine      {'pyridine-like': 2, 'pyrrole-like N-H': 2, 'non-aromatic N': 1}
cytosine     {'pyridine-like': 1, 'pyrrole-like N-H': 1, 'non-aromatic N': 1}
thymine      {'pyrrole-like N-H': 2}
nicotinamide {'pyridine-like': 1, 'non-aromatic N': 1}
pyrrole         pKa   0.4  protonated at pH 7.4: 1e-07
pyrimidine      pKa   1.3  protonated at pH 7.4: 7.9e-07
pyridine        pKa  5.25  protonated at pH 7.4: 0.007
His side chain  pKa   6.0  protonated at pH 7.4: 0.038
imidazole       pKa  6.95  protonated at pH 7.4: 0.26
Lys side chain  pKa  10.8  protonated at pH 7.4: 1
```

The token counts reproduce the table: thymine has no pyridine-like nitrogen at all (both ring N–H are amide-like, written `[nH]`), while adenine has three. A token rule is only a first pass: real toolkits perceive aromaticity and assign hydrogens from the whole molecular graph, and the exocyclic `N` here lumps amino and amide nitrogens together.

## Worked example

> [!example] Acceptors of adenine, charge of histidine
> 1. **Read the string.** Adenine `Nc1ncnc2[nH]cnc12`: three pyridine-like nitrogens (N1, N3, N7), one ring N–H (N9, the atom that bonds the sugar in a nucleotide) and one exocyclic amino group (N6).
> 2. **Pair it.** In the A·T pair, N1 of adenine accepts the hydrogen of thymine's N3–H, and the N6–H of adenine donates to thymine's O4 ([[Base Pairing]]). N7 is not on the pairing edge.
> 3. **Charge of His at pH 7.4.** $\theta = 1/(1 + 10^{7.4 - 6.0}) = 1/(1 + 25.1) = 0.038$: about 4 % of His side chains carry the positive charge. Free imidazole (pKa 6.95) would be 26 % protonated, pyridine (5.25) under 1 %.
> 4. **Conclusion.** Near neutral pH, only imidazole-type rings are protonated to a useful extent, which is why His, not a pyridine-like ring, does the proton shuttling of active sites.

## Common misconceptions

> [!warning] "Every nitrogen is basic, like an amine"
> Only a nitrogen with an available lone pair is. Pyrrole's lone pair belongs to its aromatic sextet: its protonated form has pKa 0.4, against about 10.8 for the alkylamine of Lys.[^os243][^berg] The indole N–H of Trp is likewise not basic.

> [!warning] "The two nitrogens of histidine are equivalent"
> In neutral imidazole one N carries the hydrogen and donates, the other is pyridine-like and accepts. Moving the hydrogen swaps their roles (two tautomers), and only after protonation do both carry an H ([[Tautomer]]).

> [!warning] "NADH is NAD⁺ plus a proton"
> The pyridinium ring of NAD⁺ takes up a hydride ion, a proton with two electrons, at C4.[^lehninger] A dehydrogenase removes two hydrogen atoms from its substrate: one goes to NAD⁺ as hydride, the other is released as H⁺ (NAD⁺ + 2H → NADH + H⁺).

## Exercises

> [!question] Exercise 1 (L2)
> For pyrimidine, imidazole, indole and purine, count the π electrons and classify every ring nitrogen as pyridine-like or pyrrole-like. Which rings are aromatic?

> [!success]- Solution
> Pyrimidine: 4 C + 2 pyridine-like N = 6. Imidazole: 3 C + 1 pyridine-like N + 1 N–H (2 electrons) = 6. Indole: 8 C + 1 N–H = 10. Purine: 5 C + 3 pyridine-like N (N1, N3, N7) + N9–H = 10. All are planar, fully conjugated and have $4n + 2$ π electrons ($n = 1$ or 2): all aromatic, the fused ones by extension of Hückel's rule ([[Aromaticity#Deeper (L2)]]).

> [!question] Exercise 2 (L2)
> Rank pyrrole, pyridine, imidazole, pyrimidine and the Lys side chain from weakest to strongest base, and give one structural reason for each step.

> [!success]- Solution
> Pyrrole (0.4) < pyrimidine (1.3) < pyridine (5.25) < imidazole (6.95) < Lys (about 10.8).[^os243][^berg] Pyrrole's lone pair is part of the aromatic sextet. Pyrimidine's second ring nitrogen withdraws electron density from the first. Pyridine's lone pair is free but in an sp² orbital, held closer to the nucleus than the sp³ pair of an alkylamine. Imidazole beats pyridine because its cation shares the positive charge between two nitrogens. Lys has a localized sp³ lone pair.

> [!question] Exercise 3 (L2)
> In cytosine, `Nc1cc[nH]c(=O)n1`, identify the pyridine-like nitrogen, the ring N–H and the amino group. Which of them accepts a hydrogen bond in the G·C pair, and which atom of the cytosine bonds the sugar in a nucleotide?

> [!success]- Solution
> Tokens in order: `N` (exocyclic amino, N4), `[nH]` (N1), `n` (N3, pyridine-like). In the G·C pair, N3 accepts the hydrogen of guanine's N1–H, while N4–H donates to guanine's O6 ([[Base Pairing]]). N1 bonds the sugar ([[Nucleotide]]): in the nucleotide its H is replaced by the C1' of the sugar.[^berg]

> [!question] Exercise 4 (L3, Python)
> A toy protein has three independent His side chains with pKa 6.0. Compute the probability of 0, 1, 2 and 3 protonated His and the mean charge from histidines at pH 6.0, 7.0 and 7.4. What does the comparison say about modeling such a protein with "all His neutral"?

> [!success]- Solution
> ```python
> from math import comb
>
> for ph in (6.0, 7.0, 7.4):
>     t = protonated_fraction(6.0, ph)
>     dist = [comb(3, j) * t**j * (1 - t) ** (3 - j) for j in range(4)]
>     print(ph, [round(p, 3) for p in dist], "mean charge", round(3 * t, 3))
> ```
> Output: `6.0 [0.125, 0.375, 0.375, 0.125] mean charge 1.5`, `7.0 [0.751, 0.225, 0.023, 0.001] mean charge 0.273`, `7.4 [0.889, 0.106, 0.004, 0.0] mean charge 0.115`. At pH 7.4 the all-neutral microstate covers 89 % of molecules, so the assumption is reasonable; at pH 7.0 a quarter of molecules carry at least one charged His, and at pH 6.0 the all-neutral state is a minority (12.5 %). Any pKa shift in the real protein changes these numbers, which is why protonation states are computed per structure.

> [!question] Exercise 5 (L3)
> Using resonance structures of the pyridinium ring of NAD⁺, explain why the hydride adds at C4 and what this does to aromaticity.

> [!success]- Solution
> The positive charge on the ring nitrogen is delocalized by resonance onto C2, C4 and C6, the carbons ortho and para to N, so these positions are electron-poor ([[Resonance (Chemistry)]], [[Electrophile]]). In NAD⁺, C3 carries the carboxamide and C4, para to N, takes the hydride.[^lehninger] C4 becomes sp³, which breaks the continuous ring of p orbitals: NADH is a 1,4-dihydropyridine, no longer aromatic and no longer charged. The reverse reaction, hydride donation by NADH, restores the aromatic ring ([[Organic Redox Reaction]]).

## Mastery checklist

- [ ] 1 Recognized: I can name and draw pyridine, pyrimidine, pyrrole, imidazole, indole and purine and point to them in nucleobases, His, Trp, NAD⁺ and heme.
- [ ] 2 Understood: I can explain the difference between pyridine-like and pyrrole-like nitrogens and rank the basicity of the rings with reasons.
- [ ] 3 Practiced: I can classify ring nitrogens from SMILES, count π electrons and compute protonated fractions and microstate probabilities.
- [ ] 4 Applied: I inspected the His residues of a real structure and listed which nitrogen carries the hydrogen after protonation-state assignment.
- [ ] 5 Explained: I can teach how heterocycle chemistry sets base pairing, His catalysis, hydride transfer by NAD⁺ and iron binding in heme.

## References

[^os155]: [[Organic Chemistry (OpenStax)]], sec. 15.5 "Aromatic Heterocycles: Pyridine and Pyrrole" (definition of a heterocycle; pyridine's lone pair in an sp² orbital in the ring plane; pyrrole's lone pair in the π system).
[^os243]: [[Organic Chemistry (OpenStax)]], sec. 24.3 "Basicity of Amines" (Table 24.1: pKa of the protonated forms of pyrrole 0.4, pyrimidine 1.3, pyridine 5.25, imidazole 6.95; arylamines and heterocyclic amines are weaker bases than alkylamines).
[^os249]: [[Organic Chemistry (OpenStax)]], sec. 24.9 "Heterocyclic Amines" (biological heterocycles such as pyridoxal phosphate and heme, the drug sildenafil; the low basicity of pyrrole explained by its aromaticity).
[^os26]: [[Organic Chemistry (OpenStax)]], ch. 26 "Biomolecules: Amino Acids, Peptides, and Proteins".
[^os28]: [[Organic Chemistry (OpenStax)]], ch. 28 "Biomolecules: Nucleic Acids".
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of protein composition (side-chain pKa values: His 6.0, Lys 10.8), nucleotides (N9 and N1 glycosidic bonds), catalytic strategies (His in the catalytic triad, pKa shifts), NAD⁺ and other activated carriers, myoglobin and hemoglobin (protoporphyrin, iron, proximal histidine).
[^lehninger]: [[Lehninger Principles of Biochemistry (Nelson)]], 8th ed. (2021), treatment of amino acids (the ring of proline; absorbance of Trp at 280 nm), carbohydrates (pyranoses and furanoses named after pyran and furan), cofactors (thiamine pyrophosphate, flavins) and NAD⁺ (hydride transfer to C4 of the nicotinamide ring; NADH absorbs at 340 nm).
[^opensmiles]: [[OpenSMILES Specification]], aromaticity and bracket atoms (lowercase aromatic atoms, explicit hydrogen counts such as `[nH]`, charges such as `[n+]`); source note caveat on toolkit differences for implicit hydrogens of aromatic atoms other than carbon.
[^wyatt]: [[Wyatt 2006 - Methylating Agents and DNA Repair Responses]], *Chemical Research in Toxicology* 19(12):1580-1594 (N7-methylguanine as the main methylation adduct of double-stranded DNA).
