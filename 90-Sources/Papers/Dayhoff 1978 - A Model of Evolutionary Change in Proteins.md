---
aliases:
  - PAM paper
  - Dayhoff matrix
  - PAM250
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: paper
tier: S
authors:
  - Margaret O. Dayhoff
  - Robert M. Schwartz
  - Bruce C. Orcutt
journal: Atlas of Protein Sequence and Structure
year: 1978
url: "https://bioinformaticaupf.crg.eu/T2/Dayhoff1978a.pdf"
access: free
---

# Dayhoff 1978 - A Model of Evolutionary Change in Proteins

> [!abstract]
> The chapter that defined the PAM (point accepted mutation) matrices: a one-step amino acid replacement matrix estimated from closely related proteins, extrapolated to any evolutionary distance by matrix multiplication.

## Why this source

The first widely used empirical model of amino acid replacement, and the origin of the PAM250 matrix that dominated protein database searching before BLOSUM. For a learner it is the cleanest biological example of a Markov chain: one matrix for one unit of evolution, and its powers for longer times.

## Coverage

Citation: Dayhoff MO, Schwartz RM, Orcutt BC. "A model of evolutionary change in proteins". *Atlas of Protein Sequence and Structure* 5(3):345-352 (1978), a supplement volume of the Atlas.

| Part | Content | Vault notes |
|---|---|---|
| Data | Accepted replacements counted on phylogenetic trees of families of closely related proteins (alignments at least 85 % identical) | [[Substitution Matrix]], [[Protein Substitution Model]] |
| Model | PAM1: replacement probabilities for an evolutionary distance of 1 accepted point mutation per 100 residues; each change independent of earlier ones (a Markov chain) | [[Markov Chain]], [[Transition Matrix]] |
| Extrapolation | PAMn as the n-th power of PAM1 (successive matrix multiplication); log-odds scoring matrices such as PAM250 for distant relationships | [[Matrix Multiplication]] |

Cited in [[Matrix]] and [[Matrix Multiplication]].

## How to use it

- L2: read the definition of the 1-PAM unit and of the mutation probability matrix, then compute a few powers of a toy matrix ([[Matrix Multiplication]]).
- L3: compare the PAM extrapolation with the direct counting of [[Henikoff 1992 - Amino Acid Substitution Matrices from Protein Blocks]], and with continuous-time models $P(t) = e^{Qt}$ ([[Matrix Exponential]]).

## Caveats

- Based on the few protein families sequenced by the 1970s; later matrices (BLOSUM, JTT, WAG, LG) use far more data.
- Verified in this pass (web search, secondary descriptions and course material): authors, title, volume, supplement, pages and year; the 1-PAM unit (1 % of residues changed); PAMn obtained by successive multiplication of PAM1; the Markov assumption; the 85 % identity threshold of the alignments. Counts of observed mutations and families quoted in secondary sources were not checked in the chapter.
- The URL is a course-hosted scan (Universitat Pompeu Fabra), not opened in this pass (web fetching blocked); the chapter has no DOI.
