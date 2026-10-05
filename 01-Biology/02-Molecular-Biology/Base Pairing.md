---
aliases:
  - Complementary Base Pairing
  - Watson-Crick Base Pairing
  - Complementarity
  - Base Pair
  - Appariement des bases
tags:
  - type/concept
  - domain/biology
  - domain/chemistry
  - domain/bioinformatics
  - level/L1
  - level/L2
  - level/L3
mastery: 0
prerequisites:
  - "[[Nucleotide]]"
  - "[[Nucleic Acid]]"
  - "[[Hydrogen Bond]]"
related:
  - "[[DNA]]"
  - "[[RNA]]"
  - "[[Reverse Complement]]"
  - "[[DNA Replication]]"
  - "[[Transcription]]"
  - "[[Nucleic Acid Hybridization]]"
  - "[[Polymerase Chain Reaction]]"
  - "[[RNA Secondary Structure]]"
  - "[[Transfer RNA]]"
  - "[[Hamming Distance]]"
projects:
  - "[[01-dna-engine]]"
sources:
  - "[[Watson 1953 - Molecular Structure of Nucleic Acids]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Biochemistry (Berg)]]"
  - "[[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]]"
  - "[[Saiki 1988 - Primer-Directed Enzymatic Amplification of DNA]]"
  - "[[Rosalind]]"
---

# Base Pairing

> [!abstract]
> Base pairing is the rule that A sticks to T (or U in RNA) and G sticks to C across two antiparallel strands, so knowing one strand tells you the other, letter by letter.

## Definition

**Base pairing** is the specific association, through hydrogen bonds, of a base on one nucleic acid strand with a base on an antiparallel strand, or on another region of the same strand: **adenine with thymine** (uracil in RNA) and **guanine with cytosine**. Each of these Watson-Crick pairs joins a purine to a pyrimidine. Two sequences that can pair base for base along their whole length are **complementary**.[^watson][^openstax][^alberts]

## Why it matters

- **The other strand.** Deriving the complementary strand is the first operation of sequence analysis and a classic first exercise ("Complementing a Strand of DNA" on Rosalind).[^rosalind] Every search over both strands of a genome relies on it ([[Reverse Complement]]).
- **Copying.** [[DNA Replication]], [[Transcription]] and [[Reverse Transcription]] all build a new strand by pairing incoming nucleotides with a template.[^alberts]
- **Hybridization technologies.** A PCR primer, a probe or a microarray spot finds its target by pairing with it; designing one means predicting where a short sequence can pair and how stably ([[Polymerase Chain Reaction]], [[Nucleic Acid Hybridization]], [[Microarray]]).[^saiki][^alberts]
- **Recognition in the cell.** Codons are read by pairing with tRNA anticodons ([[Transfer RNA]], [[Genetic Code]]), and an RNA folds by pairing with itself ([[RNA Secondary Structure]]).

## Core (L1)

**The rules.**[^watson][^openstax][^berg]

| Pair | Where | Hydrogen bonds |
|---|---|---:|
| A-T | DNA | 2 |
| G-C | DNA and RNA | 3 |
| A-U | RNA, and RNA paired with DNA | 2 |

Each pair joins a two-ring purine (A, G) to a one-ring pyrimidine (C, T, U), so every rung of a double helix has the same width. Watson and Crick found that only these specific pairs fit their model, and noted that if the sequence of one chain is given, the sequence of the other is automatically determined.[^watson]

**Why these partners.** The edge of each base that faces its partner carries a fixed pattern of hydrogen-bond donors (N-H groups) and acceptors (oxygens and ring nitrogens). A-T and G-C are the combinations in which every donor faces an acceptor; Watson and Crick's pairing assumes each base in its usual (keto) tautomeric form.[^watson][^berg]

![[watson-crick-pair-hydrogen-bonds.svg]]

**Deriving the complementary strand**, the procedure to apply to any sequence:

1. Write the given strand 5' → 3'.
2. Under each base, write its partner: A → T (or U if the new strand is RNA), T or U → A, G → C, C → G.
3. Label the new strand **3' → 5'**: the strands are antiparallel ([[Nucleic Acid]]).
4. To report it, read the new strand from its 5' end, that is, right to left. The result is the reverse complement.

```text
given        5'-ATGGCTTAC-3'
                |||||||||
partner      3'-TACCGAATG-5'
reported     5'-GTAAGCCAT-3'
```

**Across alphabets.** The same pairing rules connect DNA and RNA; only the letter used for the partner of A changes:

| Given strand | New strand | Biological case | Example (toy) |
|---|---|---|---|
| DNA | DNA | the other strand of a duplex, replication | `ATGGCTTAC` → `GTAAGCCAT` |
| DNA | RNA | transcription, the DNA serving as template | `ATGGCTTAC` → `GUAAGCCAU` |
| RNA | DNA | cDNA made by reverse transcription | `AUGGCUUAC` → `GTAAGCCAT` |
| RNA | RNA | an RNA duplex or an RNA stem | `AUGGCUUAC` → `GUAAGCCAU` |

## Deeper (L2)

**Counting hydrogen bonds.** A duplex of $n$ base pairs has $2 \times$ (number of A-T pairs) $+ 3 \times$ (number of G-C pairs) hydrogen bonds, so G-C-rich duplexes have more of them. But the hydrogen bonds are not the main source of stability: stacking between neighbouring base pairs contributes more, and it also depends on the sequence ([[DNA#Deeper (L2)]], [[GC Content]]).[^yakovchuk]

**Mismatches.** A non-complementary pair in a duplex (a **mismatch**) fits poorly and weakens it. During replication, DNA polymerase selects correctly paired nucleotides and proofreads; a mismatch that escapes both becomes a mutation in one daughter molecule after the next round of replication ([[DNA Replication]], [[DNA Repair]], [[Mutation]]).[^alberts]

**Wobble.** In RNA, G also pairs with U. G-U pairs are common inside RNA helices and at the third position of codon-anticodon pairing ([[RNA#Deeper (L2)]], [[Genetic Code#Deeper (L2)]]).[^alberts] With wobble, an RNA no longer has a unique partner (Mathematical representation).

**Partial complementarity.** Two strands need not match perfectly to pair: a probe can bind a target that differs by a few bases. The fewer the mismatches and the longer and more G-C-rich the duplex, the more stable it is; hybridization conditions, mainly temperature and salt, set how many mismatches are tolerated (the **stringency**).[^alberts]

**Pairing within one strand.** If a strand contains a segment followed, further along, by its reverse complement, the strand can fold back and pair with itself into a hairpin: this is how RNA stems form, and why a PCR primer must not contain such a segment ([[RNA Secondary Structure]]).[^alberts]

## Advanced (L3)

- **Redundancy as a copy and repair mechanism.** Because each strand determines the other, a duplex stores its information twice: replication uses each strand as a template, and repair enzymes restore a damaged base using the intact partner strand ([[DNA Repair]]).[^watson][^alberts]
- **Complementarity search is string search.** A probe pairs with a site exactly when the site equals the reverse complement of the probe; with mismatches, when the [[Hamming Distance]] between them is small. Finding primer or probe sites is therefore [[Exact Pattern Matching]] or [[Approximate Pattern Matching]] against $\mathrm{rc}(\text{probe})$ on both strands (Exercise 6). Target prediction for small regulatory RNAs uses the same principle, with wobble allowed ([[MicroRNA]]).
- **Primer dimers.** A polymerase extends any 3' end paired to a template ([[Nucleic Acid]]), including a primer paired to another primer.[^saiki][^alberts] Primer design therefore checks each primer against itself and its partner for complementary stretches, especially at the 3' ends (Exercise 5).
- **Ambiguous letters.** Degenerate primers written with IUPAC codes pair with every sequence they stand for; their complement is the code of the complemented set ([[Nucleotide#Computational representation]], [[IUPAC Nucleotide Code]]).

## Mathematical representation

- A **pairing relation** is a set $P \subseteq \Sigma \times \Sigma$ of allowed pairs. For DNA, $P_{WC} = \{(A,T), (T,A), (G,C), (C,G)\}$, the graph of the complement map $c$ of [[Nucleotide#Mathematical representation]]. For RNA, $P_{RNA} = \{(A,U), (U,A), (G,C), (C,G)\} \cup \{(G,U), (U,G)\}$, the last two being wobble pairs.
- **Antiparallel duplex.** Two strands $s, t \in \Sigma^n$, both written 5' → 3', pair perfectly iff
$$(s_i,\, t_{n+1-i}) \in P \quad \text{for all } i = 1, \dots, n,$$
because position $i$ of $s$ faces position $n + 1 - i$ of $t$. With $P_{WC}$, this holds iff $t = \mathrm{rc}(s)$: the partner strand exists and is unique.
- **Mismatches.** The number of mismatches is $m(s, t) = |\{i : (s_i, t_{n+1-i}) \notin P_{WC}\}| = d_H(t, \mathrm{rc}(s))$, the [[Hamming Distance]] between $t$ and the perfect partner.
- **Partners with wobble.** Let $w(x) = |\{y : (x, y) \in P_{RNA}\}|$, so $w(A) = w(C) = 1$ and $w(G) = w(U) = 2$. The number of RNA strands that pair perfectly with $s$ is $\prod_{i=1}^{n} w(s_i)$.
- **Hydrogen bonds.** With $N_x$ the count of base $x$ in $s$ and $\mathrm{GC}(s) = (N_G + N_C)/n$, the perfect DNA duplex of $s$ has
$$H(s) = 2(N_A + N_T) + 3(N_G + N_C) = 2n + N_G + N_C = n\,\big(2 + \mathrm{GC}(s)\big).$$

## Computational representation

Pairing tables are dictionaries; drawing a duplex means aligning one strand with the other reversed:

```python
PARTNER = {"DNA": {"A": "T", "T": "A", "U": "A", "G": "C", "C": "G"},
           "RNA": {"A": "U", "T": "A", "U": "A", "G": "C", "C": "G"}}
WATSON_CRICK = {("A", "T"), ("T", "A"), ("A", "U"), ("U", "A"), ("G", "C"), ("C", "G")}
WOBBLE = {("G", "U"), ("U", "G")}


def complementary_strand(seq: str, make: str = "DNA") -> str:
    """Strand that pairs with seq (DNA or RNA), built as DNA or RNA and written 5'->3'."""
    return "".join(PARTNER[make][b] for b in reversed(seq.upper()))


def duplex(top: str, bottom: str, wobble: bool = False) -> str:
    """Draw top (5'->3') over bottom (given 5'->3', drawn 3'->5'): | pair, : wobble, x mismatch."""
    under = bottom[::-1]
    marks = "".join("|" if (a, b) in WATSON_CRICK else ":" if wobble and (a, b) in WOBBLE else "x"
                    for a, b in zip(top, under))
    return f"5'-{top}-3'\n   {marks}\n3'-{under}-5'"


def hydrogen_bonds(seq: str) -> int:
    """Hydrogen bonds in the perfect duplex of seq with its complement: 2 per A-T/A-U, 3 per G-C."""
    s = seq.upper()
    return 2 * sum(s.count(b) for b in "ATU") + 3 * sum(s.count(b) for b in "GC")


gene = "ATGGCTTAC"                             # invented DNA strand
print(complementary_strand(gene))              # other DNA strand
print(complementary_strand(gene, "RNA"))       # RNA made on gene as template
print(complementary_strand("AUGGCUUAC"))       # cDNA made on an RNA
print(duplex(gene, complementary_strand(gene)))
print(duplex("GGUCAC", "GUGGCC", wobble=True))
print(hydrogen_bonds(gene))
```

```text
GTAAGCCAT
GUAAGCCAU
GTAAGCCAT
5'-ATGGCTTAC-3'
   |||||||||
3'-TACCGAATG-5'
5'-GGUCAC-3'
   ||:|||
3'-CCGGUG-5'
22
```

The last duplex is an RNA stem with one G-U wobble pair. For DNA alone, `str.translate` followed by `[::-1]` is faster ([[DNA#Computational representation]]); the dictionary version above makes the choice of alphabet explicit.

## Worked example

> [!example] One toy strand, its partners and its duplex
> Given `5'-ATGGCTTAC-3'` (invented).
> 1. **Pair base by base**: A→T, T→A, G→C, G→C, C→G, T→A, T→A, A→T, C→G gives `TACCGAATG`, labeled 3' → 5'.
> 2. **Report 5' → 3'**: `GTAAGCCAT`.
> 3. **RNA on this template**: same pairing with U opposite A: `5'-GUAAGCCAU-3'`.
> 4. **Hydrogen bonds**: the strand has A 2, T 3, G 2, C 2. A-T pairs: 5, G-C pairs: 4, so $H = 2 \times 5 + 3 \times 4 = 22$. Check with the formula: $n = 9$, $\mathrm{GC} = 4/9$, $9 \times (2 + 4/9) = 22$.
> 5. **Check**: the partner of the partner is the original strand, $\mathrm{rc}(\mathrm{rc}(s)) = s$: `complementary_strand("GTAAGCCAT")` returns `ATGGCTTAC`.

## Common misconceptions

> [!warning] "Any purine can pair with any pyrimidine"
> A-C and G-T are also purine-pyrimidine combinations of the right width, but their donor and acceptor patterns clash (see the bottom of the figure): in Watson-Crick geometry only A-T and G-C place every donor opposite an acceptor.[^berg]

> [!warning] "In RNA, A pairs with T" or "U pairs with T"
> RNA contains U instead of T, so A pairs with U. When an RNA pairs with DNA, the RNA's A faces a T of the DNA and the RNA's U faces an A.[^openstax]

> [!warning] "Base pairing needs two molecules"
> One strand can pair with itself wherever it contains a segment and its reverse complement: RNA hairpins and stems, DNA hairpins, and self-complementary primers all do.[^alberts]

> [!warning] "Two strands pair only if they are perfectly complementary"
> Imperfect duplexes form too, with stability decreasing with each mismatch. This is why probes can cross-hybridize and primers can bind off-target sites unless the hybridization conditions are stringent enough.[^alberts]

## Exercises

> [!question] Exercise 1 (L1)
> For `5'-GATTACA-3'`, write (a) the complementary DNA strand with its labels, then in the conventional 5' → 3' form, (b) the RNA that would be made using it as template, (c) the number of hydrogen bonds in the DNA duplex.

> [!success]- Solution
> (a) Under each base: `3'-CTAATGT-5'`, reported `5'-TGTAATC-3'`. (b) Same pairing with U opposite A: `5'-UGUAAUC-3'`. (c) A 3, T 2 (5 A-T pairs) and G 1, C 1 (2 G-C pairs): $2 \times 5 + 3 \times 2 = 16$. `hydrogen_bonds("GATTACA")` returns 16.

> [!question] Exercise 2 (L1)
> Draw the duplex formed by `5'-ACGTTAGC-3'` and `5'-GCTAACCT-3'` and locate the mismatch.

> [!success]- Solution
> Write the second strand reversed under the first:
> ```text
> 5'-ACGTTAGC-3'
>    |x||||||
> 3'-TCCAATCG-5'
> ```
> Position 2 of the top strand, C, faces C: a mismatch. The perfect partner would be `5'-GCTAACGT-3'`, the reverse complement of the top strand.

> [!question] Exercise 3 (L2)
> Prove that the perfect duplex of a strand $s$ of length $n$ has $H(s) = n(2 + \mathrm{GC}(s))$ hydrogen bonds. Two 20-mers have GC contents of 0.40 and 0.55: compute $H$ for each. Does the one with more hydrogen bonds necessarily melt at a higher temperature?

> [!success]- Solution
> Every position is either A/T (2 bonds) or G/C (3 bonds): $H = 2(n - N_{GC}) + 3N_{GC} = 2n + N_{GC} = n(2 + N_{GC}/n)$. For the 20-mers: $20 \times 2.40 = 48$ and $20 \times 2.55 = 51$. Higher GC content usually does raise stability, but the hydrogen-bond count is not the explanation: stacking between neighbouring pairs contributes more, and it depends on the order of the bases, not only on composition.[^yakovchuk]

> [!question] Exercise 4 (L2)
> Allowing G-U wobble, how many different RNA strands can pair perfectly with `5'-GUGCA-3'`? List them.

> [!success]- Solution
> $w(G) \, w(U) \, w(G) \, w(C) \, w(A) = 2 \times 2 \times 2 \times 1 \times 1 = 8$. Reading the partner 5' → 3' (it faces A, C, G, U, G from its own 5' end): U, G, {C, U}, {A, G}, {C, U}, giving `UGCAC UGCAU UGCGC UGCGU UGUAC UGUAU UGUGC UGUGU`. Only `UGCAC` is the Watson-Crick partner.

> [!question] Exercise 5 (L3, Python)
> Two invented PCR primers are `AGCTTGACCTGAGGATCC` (forward) and `TTCAGGTACGGATCCTCA` (reverse). Find the longest run of consecutive Watson-Crick pairs they can form with each other and with themselves. Why is the location of these runs worrying?

> [!success]- Solution
> A segment of primer $a$ pairs with primer $b$ exactly when it also occurs in $\mathrm{rc}(b)$, so the task is a longest common substring, solved by [[Dynamic Programming]].
> ```python
> COMPLEMENT = str.maketrans("ACGT", "TGCA")
>
>
> def reverse_complement(s: str) -> str:
>     return s.translate(COMPLEMENT)[::-1]
>
>
> def longest_pairing(a: str, b: str) -> tuple[int, str]:
>     """Longest run of consecutive Watson-Crick pairs when a and b (both 5'->3') lie antiparallel.
>     A segment of a pairs with b exactly when it also occurs in reverse_complement(b),
>     so this is a longest-common-substring problem, solved by dynamic programming in O(|a||b|)."""
>     r = reverse_complement(b)
>     best, end = 0, 0
>     prev = [0] * (len(r) + 1)
>     for i in range(1, len(a) + 1):
>         cur = [0] * (len(r) + 1)
>         for j in range(1, len(r) + 1):
>             if a[i - 1] == r[j - 1]:
>                 cur[j] = prev[j - 1] + 1
>                 if cur[j] > best:
>                     best, end = cur[j], i
>         prev = cur
>     return best, a[end - best:end]
>
>
> forward = "AGCTTGACCTGAGGATCC"      # invented primers
> reverse = "TTCAGGTACGGATCCTCA"
> print(longest_pairing(forward, reverse))
> print(longest_pairing(forward, forward))   # self-dimer
> ```
> Output: `(9, 'TGAGGATCC')` and `(6, 'GGATCC')`. The 9-base run is the 3' end of the forward primer, and it pairs with the 3' end of the reverse primer (`GGATCCTCA`). With both 3' ends paired, the polymerase can extend each primer on the other and amplify a short primer dimer instead of the target. The forward primer can also pair with itself through `GGATCC`, a reverse palindrome ([[DNA#Advanced (L3)]]).

> [!question] Exercise 6 (L3, Python)
> Write `hybridization_sites(probe, target, max_mismatches)` returning the windows of a target strand where a probe can pair with at most `max_mismatches` mismatches. Test the invented probe `GTAAGCCATG` on the invented target `TTGACGCATGGCTTACGGATCCGCATGACTTACGTA` with 0 and 2 allowed mismatches.

> [!success]- Solution
> The probe pairs with a window exactly where the window matches $\mathrm{rc}(\text{probe})$, and the number of mismatches is their Hamming distance (`reverse_complement` as in Exercise 5).
> ```python
> def hybridization_sites(probe: str, target: str, max_mismatches: int = 1) -> list[tuple[int, int]]:
>     """Windows of target (0-based start) where probe can pair antiparallel with at most
>     max_mismatches non-Watson-Crick pairs = Hamming distance to reverse_complement(probe)."""
>     site, k = reverse_complement(probe), len(probe)
>     hits = []
>     for i in range(len(target) - k + 1):
>         d = sum(a != b for a, b in zip(target[i:i + k], site))
>         if d <= max_mismatches:
>             hits.append((i, d))
>     return hits
>
>
> target = "TTGACGCATGGCTTACGGATCCGCATGACTTACGTA"   # invented target strand
> probe = "GTAAGCCATG"                                # invented probe, 5'->3'
> print(reverse_complement(probe))
> print(hybridization_sites(probe, target, 0), hybridization_sites(probe, target, 2))
> ```
> Output: `CATGGCTTAC`, then `[(6, 0)]` and `[(6, 0), (23, 1)]`. At low stringency the probe also binds position 23 (`CATGACTTAC`, one mismatch): a cross-hybridization site. The scan costs $O(nk)$; a realistic version would also scan the other strand of the target and weigh mismatches by position and stacking.

## Mastery checklist

- [ ] 1 Recognized: I can state the A-T (A-U) and G-C rules and the number of hydrogen bonds of each pair.
- [ ] 2 Understood: I can explain why only these pairs fit (purine-pyrimidine width, donor-acceptor patterns) and why the partner strand is written reversed.
- [ ] 3 Practiced: I can derive the complementary DNA or RNA strand of any sequence by hand and in code, count mismatches and hydrogen bonds, and solve the exercises.
- [ ] 4 Applied: in [[01-dna-engine]], my complement functions handle DNA, RNA, lowercase and IUPAC input, with tests such as $\mathrm{rc}(\mathrm{rc}(s)) = s$.
- [ ] 5 Explained: I can teach wobble, mismatches, stringency, and how complementarity search underlies primer, probe and small-RNA target design.

## References

[^watson]: [[Watson 1953 - Molecular Structure of Nucleic Acids]], *Nature*.
[^openstax]: [[Biology 2e (OpenStax)]], ch. 14 "DNA Structure and Function" and ch. 15 "Genes and Proteins".
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002), treatment of DNA structure, replication fidelity and repair, RNA structure, and nucleic acid hybridization methods.
[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of the Watson-Crick base pairs.
[^yakovchuk]: [[Yakovchuk 2006 - Base-Stacking and Base-Pairing Contributions into Thermal Stability of the DNA Double Helix]], *Nucleic Acids Research*.
[^saiki]: [[Saiki 1988 - Primer-Directed Enzymatic Amplification of DNA]], *Science* (primer annealing and extension by a thermostable polymerase).
[^rosalind]: [[Rosalind]], problem "Complementing a Strand of DNA" (REVC).
