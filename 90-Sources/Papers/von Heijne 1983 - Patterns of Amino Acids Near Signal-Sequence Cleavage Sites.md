---
aliases:
  - (-3,-1) rule
  - von Heijne rule
tags:
  - type/source
  - domain/biology
  - domain/bioinformatics
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Gunnar von Heijne
journal: European Journal of Biochemistry
year: 1983
url: "https://garfield.library.upenn.edu/classics1989/A1989R818600002.pdf"
access: partial
---

# von Heijne 1983 - Patterns of Amino Acids Near Signal-Sequence Cleavage Sites

> [!abstract]
> The statistical study of signal peptide cleavage sites that established the (−3,−1) rule: only small, uncharged amino acids occur at positions −3 and −1 before the cut.

## Why this source

It is the origin of the first sequence rule for where signal peptidase cuts, a rule still used to explain predictions and still cited as a requirement for correct cleavage. It shows how a statistical observation on known cleavage sites became a design constraint for later predictors such as SignalP.

## Coverage

Citation: von Heijne G. "Patterns of amino acids near signal-sequence cleavage sites". *European Journal of Biochemistry* 133:17-21 (1983).

| Part | Content | Vault notes |
|---|---|---|
| (−3,−1) rule | Only small, uncharged residues at positions −3 and −1 relative to the cleavage site | [[Protein Targeting]] |
| Context | A paper by Perlman and Halvorson with essentially the same message appeared within a few weeks; the rule is cited by the first SignalP paper (1997) as a condition for correct cleavage | [[Protein Targeting]] |

## How to use it

- **L2**: apply the rule by hand to a signal peptide whose cleavage site is annotated in [[UniProt]].
- **L3**: compare the hard rule with a position-specific score ([[Position Weight Matrix]]) and with a modern predictor ([[Teufel 2022 - SignalP 6.0 Predicts All Five Types of Signal Peptides Using Protein Language Models]]).

## Caveats

- The `url` is von Heijne's 1989 "Citation Classic" commentary on this paper (Current Contents), the only page about it verified in this pass; the article itself is on the publisher's site, whose access terms were not checked.
- Verified in this pass (web search): the citation (journal, volume, pages, year), the rule, the Perlman and Halvorson note, and the citation of the rule in the 1997 SignalP paper. The dataset size and statistics of the paper were not verified.
