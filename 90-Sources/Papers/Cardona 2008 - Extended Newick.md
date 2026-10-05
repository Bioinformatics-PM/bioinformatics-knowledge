---
aliases:
  - Extended Newick paper
  - "Extended Newick: it is time for a standard representation of phylogenetic networks"
tags:
  - type/source
  - domain/bioinformatics
  - domain/computer-science
  - level/L2
  - level/L3
kind: paper
tier: B
authors:
  - Gabriel Cardona
  - Francesc Rosselló
  - Gabriel Valiente
journal: BMC Bioinformatics
year: 2008
url: "https://doi.org/10.1186/1471-2105-9-532"
access: free
---

# Cardona 2008 - Extended Newick

> [!abstract]
> A proposal to represent phylogenetic networks by extending the Newick format, the parenthesized text format in which phylogenetic trees are exchanged and stored.

## Why this source

Peer-reviewed and open access. It states the role of the Newick format for trees (the format in which specialized databases provide phylogenetic trees) before extending it to networks that show reticulate events such as recombination, hybridization or lateral gene transfer. It is therefore a citable description of both the tree format and its network extension.

## Coverage

Citation: Cardona G, Rosselló F, Valiente G. "Extended Newick: it is time for a standard representation of phylogenetic networks". *BMC Bioinformatics* 9:532 (2008). doi:10.1186/1471-2105-9-532.

| Part | Content | Vault notes |
|---|---|---|
| Background | Newick as the format of phylogenetic trees: nested parentheses enclosing comma-separated children, node labels, a terminating semicolon | [[Newick Format]], [[Stack]] |
| Proposal | Extended Newick, a parenthesized representation of phylogenetic networks | [[Phylogenetic Network]] |

Cited in [[Stack]].

## How to use it

- L2: read the background together with [[Newick Format]] before writing a tree parser.
- L3: read the proposal when a tree cannot represent the history (reticulation, [[Phylogenetic Network]]).

## Caveats

- The paper's subject is networks; for plain trees it is a secondary description of a format agreed outside the peer-reviewed literature.
- Verified in this pass: authors, title, journal, volume, article number, year, DOI and abstract (by search). The background's description of the Newick syntax was not checked line by line.
