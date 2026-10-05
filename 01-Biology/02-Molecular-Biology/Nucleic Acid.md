---
aliases:
  - Nucleic Acids
  - Polynucleotide
  - Sugar-Phosphate Backbone
  - Acide nucléique
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
  - "[[Covalent Bond]]"
  - "[[Phosphate Ester]]"
related:
  - "[[DNA]]"
  - "[[RNA]]"
  - "[[Base Pairing]]"
  - "[[Reverse Complement]]"
  - "[[DNA Replication]]"
  - "[[Hydrolysis]]"
  - "[[Gel Electrophoresis]]"
  - "[[Genomic Coordinate System]]"
projects:
  - "[[01-dna-engine]]"
  - "[[bio-core]]"
sources:
  - "[[Biochemistry (Berg)]]"
  - "[[Biology 2e (OpenStax)]]"
  - "[[Molecular Biology of the Cell (Alberts)]]"
  - "[[Watson 1953 - Molecular Structure of Nucleic Acids]]"
  - "[[Sanger 1977 - DNA Sequencing with Chain-Terminating Inhibitors]]"
---

# Nucleic Acid

> [!abstract]
> A nucleic acid is a chain of nucleotides hooked head to tail by one repeated sugar-phosphate link: the backbone is uniform, the bases carry the message, and the way the links are made gives every chain a direction, from its 5' end to its 3' end.

## Definition

A **nucleic acid** is a polymer of [[Nucleotide|nucleotides]] (a **polynucleotide**) in which a phosphate group joins the 3' carbon of one sugar to the 5' carbon of the next, a **3'-5' phosphodiester bond**. The alternating sugars and phosphates form a **backbone** that is identical all along the chain; one base hangs off each sugar. The two nucleic acids of cells are [[DNA]], built on deoxyribose, and [[RNA]], built on ribose.[^berg][^openstax][^alberts]

## Why it matters

- **Direction is part of the data.** A sequence file stores one strand as text written 5' → 3' ([[FASTA Format]]). `ACG` and `GCA` are different molecules, and nothing in the letters says which way a string was written: only the convention, a label or a strand field does.
- **Strands and coordinates.** Annotations give each feature a strand (`+` or `-`), that is, the direction of the backbone that carries it relative to the reference ([[Genomic Coordinate System]], [[GFF Format]]). "Upstream" and "downstream" are defined by that direction.
- **Enzymes are directional.** Polymerases only extend a free 3' end, which dictates how primers are designed and in which direction reads grow ([[Polymerase Chain Reaction]], [[DNA Sequencing]]).[^alberts][^sanger]
- **A charged backbone.** The phosphates make every nucleic acid strongly negative, which is what [[Gel Electrophoresis]] uses to move DNA fragments and sort them by length.[^alberts]

## Core (L1)

![[nucleic-acid-backbone-polarity.svg]]

**The backbone.** A nucleotide carries its phosphate on the 5' carbon of its sugar and a free hydroxyl on the 3' carbon ([[Nucleotide]]). Polymerization links the 3'-OH of one nucleotide to the 5' phosphate of the next, so the chain reads sugar, phosphate, sugar, phosphate. Every link is the same; only the bases, attached to the 1' carbons, differ. The information of a nucleic acid is therefore the **order of its bases**, and the backbone is the constant scaffold that carries it.[^berg][^openstax]

**Why a strand has a direction.** Each link is asymmetric: it leaves one sugar from its 3' carbon and enters the next at its 5' carbon. Walking along the chain one way you always go 5' → 3', the other way always 3' → 5', and the two ends are chemically different:[^berg][^alberts]

| End | Terminal sugar | Usually carries |
|---|---|---|
| **5' end** | its 5' carbon is not linked to another nucleotide | a phosphate group |
| **3' end** | its 3' carbon is not linked to another nucleotide | a free hydroxyl (3'-OH) |

**The writing convention.** Sequences are written with the 5' end on the left and the 3' end on the right, and an unlabeled sequence is read 5' → 3'. `ACG` means `5'-ACG-3'`: A carries the free 5' end, G the free 3' end.[^berg]

**Direction in action.**

- A new nucleotide is always added to the free 3'-OH of the growing chain, so every strand is synthesized 5' → 3' ([[DNA Replication]], [[Transcription]]).[^alberts]
- In a double helix the two strands run in opposite directions (antiparallel), which is why the partner strand, written 5' → 3', is the *reverse* complement ([[DNA]], [[Base Pairing]]).[^watson]
- Ribosomes read a messenger RNA from its 5' end toward its 3' end ([[Translation]]).[^alberts]

**Sizes.** DNA and RNA backbones differ only at the 2' carbon of the sugar ([[Nucleotide]]). Chains range from short synthetic **oligonucleotides**, used as primers and probes, to chromosomes of millions of nucleotides ([[Genome]]).[^alberts]

## Deeper (L2)

**Why "phosphodiester".** Each internal phosphate is esterified twice, once to the 3' oxygen of one sugar and once to the 5' oxygen of the next ([[Phosphate Ester]]). At cellular pH these phosphates are negatively charged, so a nucleic acid is a polyanion with about one negative charge per nucleotide. In the nucleus the charge is partly neutralized by histones, proteins rich in positively charged amino acids ([[Chromatin]]).[^berg][^alberts]

**Stability.** Breaking the DNA backbone ([[Hydrolysis]]) is slow without enzymes, whereas the 2'-OH of ribose makes RNA far easier to hydrolyse (details in [[RNA#Deeper (L2)]]).[^berg]

**Directional enzymes.** Nucleases are named by where and in which direction they cut:[^alberts]

- **exonucleases** remove nucleotides one at a time from an end, either 5' → 3' or 3' → 5'; the proofreading activity of DNA polymerases is a 3' → 5' exonuclease that clips a mismatched nucleotide off the growing 3' end ([[DNA Replication]]);
- **endonucleases** cut inside the chain; [[Restriction Enzyme|restriction enzymes]] are endonucleases that cut at specific sequences.

**Chain termination.** Each new link needs the 3'-OH of the last nucleotide, so a nucleotide lacking it, a 2',3'-dideoxynucleotide, ends the chain. Sanger sequencing used such terminators to produce fragments ending at every position of a template ([[Sanger Sequencing]]).[^sanger]

**Circular molecules.** Linking the 3' end of a strand to its own 5' end gives a circle with no free ends; bacterial chromosomes and [[Plasmid|plasmids]] are circular double-stranded DNA.[^alberts] A circle keeps its direction (each link is still 3' → 5') but has no first nucleotide, so a sequence file must cut it at an arbitrary point.

**Not always a double helix.** Many [[Virus|viruses]] have single-stranded DNA or double-stranded RNA genomes ([[Baltimore Classification]]).[^alberts] "DNA = double, RNA = single" describes cells, not all nucleic acids.

## Advanced (L3)

- **Direction is metadata.** `ACG` is a valid sequence read either way, so a string written 3' → 5' by mistake is undetectable from its letters. Pipelines therefore fix one convention (5' → 3'), convert at input, and carry the strand in a separate field; a reverse primer or a `-` strand feature is stored as its own 5' → 3' string, the reverse complement of the reference ([[Reverse Complement]]).
- **Order-dependent statistics.** Anything computed on neighbours ([[K-mer]] counts, dinucleotide frequencies, [[Sequence Motif|motifs]]) changes when a string is reversed: the step `CG` read backwards is `GC`. This matters because CG is the dinucleotide depleted in vertebrate genomes, a consequence of the mutability of methylated cytosine ([[Nucleotide#Advanced (L3)]], [[CpG Island]]).[^alberts] A reversed string would attribute the depletion to GC (Worked example).
- **Upstream and downstream.** Relative to a gene, positions toward the 5' end of its coding strand are upstream and numbered negatively from the transcription start site, +1 ([[Transcription]]).[^os15] For a gene on the `-` strand, upstream therefore lies at *higher* genome coordinates.
- **Primers.** A polymerase extends a primer only from a 3' end paired to the template, so a primer's 3' end is its critical part and every primer is written 5' → 3' ([[Base Pairing]], [[Polymerase Chain Reaction]]).[^alberts]
- **Circular sequences.** Two records of the same plasmid can start at different positions and even describe different strands; comparing them means comparing rotations of both strands (Exercise 5).

## Mathematical representation

- A linear strand of length $n$ is a word $s = s_1 s_2 \dots s_n \in \Sigma^n$ over the nucleotide alphabet $\Sigma$, written 5' → 3': $s_1$ carries the 5' end and $s_n$ the 3' end.
- **Backbone as a directed graph.** The vertices are the positions $\{1, \dots, n\}$; each phosphodiester bond is an arc $(i, i+1)$ from the nucleotide linked through its 3' carbon to the one linked through its 5' carbon. A linear strand is a directed path with $n - 1$ arcs; a circular strand adds the arc $(n, 1)$ and becomes a directed cycle with $n$ arcs.
- **Reversal.** Let $\rho(s)_i = s_{n+1-i}$. The word $\rho(s)$ labeled 3' → 5' denotes the same molecule as $s$; labeled 5' → 3' it denotes another molecule unless $\rho(s) = s$. $\rho$ is an involution, $\rho(\rho(s)) = s$.
- **Steps.** The dinucleotide steps of $s$ are the $n - 1$ words $s_i s_{i+1}$, one per arc, drawn from $|\Sigma|^2 = 16$ ordered pairs. Writing $N_{xy}(s)$ for the number of steps equal to $xy$, reversal swaps the order: $N_{xy}(\rho(s)) = N_{yx}(s)$. Only the four steps $xx$ are unaffected.
- **Circular equivalence.** Two words $u, v \in \Sigma^n$ denote the same circular strand iff $v$ is a rotation of $u$: $v = u_{k+1} \dots u_n u_1 \dots u_k$ for some $k \in \{0, \dots, n-1\}$.
- **Charge.** With one negative elementary charge per internal phosphate and no terminal phosphate, a linear strand carries $q(s) = -(n-1)$; the charge per nucleotide tends to $-1$ whatever the sequence.

## Computational representation

Store every strand as a 5' → 3' string, convert anything else at input, and derive bonds and steps from the string:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Strand:
    """One nucleic acid strand, always stored 5'->3' (the chemical direction of the backbone)."""
    seq: str
    circular: bool = False

    @classmethod
    def from_3_to_5(cls, written: str, circular: bool = False) -> "Strand":
        """Build a strand from letters written 3'->5' (as for the lower strand of a duplex)."""
        return cls(written[::-1], circular)

    def __str__(self) -> str:
        return f"circular 5'-{self.seq}-3'" if self.circular else f"5'-{self.seq}-3'"

    def bonds(self) -> list[tuple[int, int]]:
        """Phosphodiester links (i, j), 1-based: 3' carbon of nucleotide i to 5' carbon of j."""
        n = len(self.seq)
        links = [(i, i + 1) for i in range(1, n)]
        return links + [(n, 1)] if self.circular and n > 1 else links

    def steps(self) -> list[str]:
        """Dinucleotide steps read 5'->3', one per phosphodiester bond."""
        s = self.seq + (self.seq[0] if self.circular else "")
        return [s[i:i + 2] for i in range(len(s) - 1)]


figure = Strand.from_3_to_5("TAGCCA")      # toy strand printed 3'->5' in a figure
print(figure, figure.bonds())
print(figure.steps(), "CG" in figure.steps(), "GC" in figure.steps())
ring = Strand("ACGT", circular=True)        # toy circular strand
print(ring, len(ring.bonds()), ring.steps())
```

```text
5'-ACCGAT-3' [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
['AC', 'CC', 'CG', 'GA', 'AT'] True False
circular 5'-ACGT-3' 4 ['AC', 'CG', 'GT', 'TA']
```

A frozen dataclass makes the strand an immutable value ([[Value Object]]), the design [[bio-core]] uses for sequences: once normalized, a strand cannot be flipped by accident.

## Worked example

> [!example] A strand printed backwards (invented toy sequence)
> A figure shows a single strand as `3'-TAGCCA-5'`.
> 1. **Normalize.** Read it from the 5' label: `5'-ACCGAT-3'`. Only this string may enter code.
> 2. **Ends.** A (on the right in the figure) carries the free 5' phosphate; T carries the free 3'-OH, so a polymerase would add the next nucleotide after T.
> 3. **Bonds.** 6 nucleotides, 5 phosphodiester bonds: A→C, C→C, C→G, G→A, A→T, each from a 3' carbon to the next 5' carbon.
> 4. **Steps.** Read 5' → 3', the strand contains the step CG once and no GC. Counting on the printed string `TAGCCA` would find GC and no CG: the reversal swaps them, $N_{CG}(\rho(s)) = N_{GC}(s)$.
> 5. **Different molecule.** `5'-TAGCCA-3'`, the printed letters taken at face value, is a real but different molecule: same composition, opposite order.

## Common misconceptions

> [!warning] "5' → 3' is only a writing convention"
> The convention says which end is written first, but the two ends are chemically different: a phosphate at one, a 3'-OH at the other. Polymerases, exonucleases and ribosomes all tell them apart, and `5'-ACG-3'` and `5'-GCA-3'` are different molecules.[^berg][^alberts]

> [!warning] "Reversing a sequence gives the other strand"
> Reversal gives the **same** strand read 3' → 5'. The partner strand of a duplex is obtained by reversing **and** complementing ([[Base Pairing]], [[Reverse Complement]]). The opposite error, complementing without reversing, is discussed in [[DNA#Common misconceptions]].

> [!warning] "The backbone carries the genetic information"
> The sugar-phosphate backbone is the same repeating unit everywhere; the information is the order of the bases attached to it.[^berg]

> [!warning] "A nucleic acid is either a double-stranded DNA or a single-stranded RNA"
> That describes cellular genomes and most cellular RNAs. Viral genomes also come as single-stranded DNA and double-stranded RNA, and RNA strands pair with themselves into double-stranded stems ([[RNA]]).[^alberts]

## Exercises

> [!question] Exercise 1 (L1)
> A strand is printed `3'-GGATC-5'`. Rewrite it 5' → 3', name the nucleotides at the 5' and 3' ends, and count its phosphodiester bonds.

> [!success]- Solution
> Reading from the 5' label: `5'-CTAGG-3'`. The 5' end is C (free phosphate), the 3' end is G (free 3'-OH). Five nucleotides in a linear chain: $n - 1 = 4$ phosphodiester bonds.

> [!question] Exercise 2 (L1)
> Which of these denote the same molecule as `5'-ATGC-3'`? (a) `3'-CGTA-5'` (b) `5'-CGTA-3'` (c) `3'-ATGC-5'` (d) `ATGC`, unlabeled.

> [!success]- Solution
> (a) yes: the same strand read from its 3' end. (b) no: A and C have swapped ends. (c) no: read 5' → 3' it is `CGTA`, the molecule of (b). (d) yes, by the convention that unlabeled sequences are written 5' → 3'.

> [!question] Exercise 3 (L2)
> A DNA polymerase has just added a wrong nucleotide at the 3' end of `5'-ACGTTC-3'` (the final C). (a) Which activity removes it, and which bond is broken? (b) If the final C were a dideoxynucleotide instead, could the polymerase continue? Why?

> [!success]- Solution
> (a) The proofreading 3' → 5' exonuclease removes the terminal C by hydrolysing the phosphodiester bond between the T at position 5 and the C at position 6, which leaves a free 3'-OH on the T for synthesis to resume. (b) No: a dideoxynucleotide has no 3'-OH, so no phosphodiester bond can be made to the next nucleotide. This is the principle of chain termination.[^sanger]

> [!question] Exercise 4 (L2, Python)
> A paper prints a strand 3' → 5' as `TACGCGTTCG`. Count its CG and GC steps from the string as printed, then correctly. Explain the difference.

> [!success]- Solution
> ```python
> from collections import Counter
>
> written_3_to_5 = "TACGCGTTCG"          # invented, as printed 3'->5'
> strand = written_3_to_5[::-1]           # the same molecule written 5'->3'
>
>
> def step_counts(s: str) -> Counter:
>     return Counter(s[i:i + 2] for i in range(len(s) - 1))
>
>
> wrong, right = step_counts(written_3_to_5), step_counts(strand)
> print(strand, len(strand) - 1, "steps")
> print("read as printed: CG", wrong["CG"], "GC", wrong["GC"])
> print("read 5'->3':     CG", right["CG"], "GC", right["GC"])
> ```
> Output: `GCTTGCGCAT 9 steps`, then `CG 3 GC 1` as printed and `CG 1 GC 3` correctly. Reversal maps every step $xy$ to $yx$, so the counts of CG and GC are exchanged.

> [!question] Exercise 5 (L3, Python)
> Three records describe a circular double-stranded toy plasmid: `GATTACAGGC`, `CAGGCGATTA`, and the reverse complement of `TACAGGCGAT`. Write `canonical_circle(s)` returning one representative for all descriptions of the same circular duplex, and test it. What is the running time?

> [!success]- Solution
> A circular duplex can be cut at any of $n$ positions and read on either strand: $2n$ descriptions. Take the smallest.
> ```python
> COMPLEMENT = str.maketrans("ACGT", "TGCA")
>
>
> def reverse_complement(s: str) -> str:
>     return s.translate(COMPLEMENT)[::-1]
>
>
> def canonical_circle(s: str) -> str:
>     """One representative for a circular duplex: the smallest rotation of either strand."""
>     candidates = [t[i:] + t[:i] for t in (s, reverse_complement(s)) for i in range(len(s))]
>     return min(candidates)
>
>
> a = "GATTACAGGC"                  # invented circular sequence, cut after position 0
> b = "CAGGCGATTA"                  # same strand, cut elsewhere
> c = reverse_complement("TACAGGCGAT")   # the other strand, cut elsewhere
> print(canonical_circle(a), canonical_circle(b), canonical_circle(c))
> print(canonical_circle(a) == canonical_circle(b) == canonical_circle(c))
> print(canonical_circle("GATTACAGGA") == canonical_circle(a))
> ```
> Output: `AATCGCCTGT` three times, `True`, then `False` for a sequence differing by one base. Building $2n$ strings of length $n$ and comparing them costs $O(n^2)$ time and memory ([[Big O Notation]]): instant for a plasmid of a few thousand base pairs, about $2 \times (4.6 \times 10^6)^2 \approx 4 \times 10^{13}$ character operations for a 4.6 Mb bacterial chromosome, where a smarter method is needed.

> [!question] Exercise 6 (L3)
> In [[Gel Electrophoresis]], DNA fragments move toward the positive electrode and short fragments travel farther. Using the charge model of the Mathematical representation, explain why the charge alone cannot sort fragments by length, and what does.

> [!success]- Solution
> The charge grows as $-(n-1)$ and the mass also grows linearly with $n$, so the charge per unit length is nearly the same for every fragment: the electric force per nucleotide does not depend on length. What separates fragments is the gel, a porous matrix that slows long chains more than short ones.[^alberts] Charge makes all fragments move in the same direction; the sieve orders them by size.

## Mastery checklist

- [ ] 1 Recognized: I can define a nucleic acid, name the phosphodiester bond and say which end is 5' and which is 3'.
- [ ] 2 Understood: I can explain why the chain has a direction, why synthesis is 5' → 3', and why reversing a string changes the molecule.
- [ ] 3 Practiced: I can normalize strands to 5' → 3', count bonds and steps, and compare circular sequences in Python.
- [ ] 4 Applied: in [[01-dna-engine]] and [[bio-core]], my sequence objects store a single orientation and reject or convert anything else, with tests for strand errors.
- [ ] 5 Explained: I can teach how directionality shapes enzymes (polymerases, exonucleases, chain terminators), file conventions and strand-aware statistics.

## References

[^berg]: [[Biochemistry (Berg)]], 5th ed. (2002), treatment of nucleic acid structure (bases linked to a sugar-phosphate backbone, chain polarity, sequence convention).
[^openstax]: [[Biology 2e (OpenStax)]], Unit 1 "The Chemistry of Life" (nucleic acids) and ch. 14 "DNA Structure and Function".
[^os15]: [[Biology 2e (OpenStax)]], ch. 15 "Genes and Proteins" (numbering around the transcription start site).
[^alberts]: [[Molecular Biology of the Cell (Alberts)]], 4th ed. (2002).
[^watson]: [[Watson 1953 - Molecular Structure of Nucleic Acids]], *Nature*.
[^sanger]: [[Sanger 1977 - DNA Sequencing with Chain-Terminating Inhibitors]], *PNAS*.
