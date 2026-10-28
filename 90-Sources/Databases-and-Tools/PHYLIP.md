---
aliases:
  - Phylogeny Inference Package
  - The Newick tree format
  - Newick's 8:45 Tree Format Standard
tags:
  - type/source
  - domain/bioinformatics
  - domain/biology
  - level/L2
  - level/L3
kind: tool
tier: B
authors:
  - Joseph Felsenstein
institution: University of Washington
year:
edition: "website pages read in 2026: The Newick tree format; Gary Olsen's interpretation of the Newick's 8:45 standard (1990)"
url: "https://phylipweb.github.io/phylip/"
access: free
---

# PHYLIP

> [!abstract]
> Joseph Felsenstein's package of phylogeny programs, whose website hosts the reference descriptions of the Newick tree format: Felsenstein's own page and Gary Olsen's 1990 grammar of the standard.

## Why this source

The Newick standard was never formally published: the description on the PHYLIP website, written by the person who convened the committee that adopted it, and Olsen's grammar hosted next to it are the closest thing to a specification. Peer-reviewed papers, such as [[Cardona 2008 - Extended Newick]], describe the format only in passing.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| "The Newick tree format" (Felsenstein) | Nested parentheses (Cayley's correspondence between trees and parentheses); interior nodes as matched parentheses enclosing comma-separated descendants; tip names (no blanks, colons, semicolons, parentheses or square brackets; underscore read as a blank; empty names allowed); multifurcations; branch lengths after a colon; interior node names after the right parenthesis; terminating semicolon; examples; non-uniqueness (order of descendants, arbitrary rooting of unrooted trees); NEXUS and PhyloXML as alternatives; origin (adopted 26 June 1986 by an informal committee, named after Newick's restaurant in Dover, New Hampshire; generalization of Christopher Meacham's 1984 format); no formal publication | [[Newick Format]] |
| "Newick's 8:45" Tree Format Standard (Gary Olsen, 30 August 1990) | Grammar of tree, descendant list, subtree, labels and branch lengths; quoted labels with doubled single quotes; underscores converted to blanks in unquoted labels; whitespace and newline rules; comments in square brackets; notes on PAUP (nested comments), TreeAlign (root branch length 0.0) and PHYLIP (unrooted trees begin with a trifurcation) | [[Newick Format]] |

Cited in [[Newick Format]].

## How to use it

- L2: read Felsenstein's page with [[Newick Format]] before writing a parser; keep Olsen's grammar at hand for quoting and comments.
- L3: use the non-uniqueness section when comparing trees produced by different programs ([[Phylogenetic Tree]]).

## Caveats

- Tool documentation, tier B because its author convened the committee and the standard has no formal publication; programs implement dialects (quoting, underscores, comments, root branch length), so test files from each program you use.
- Search results report that another PHYLIP page dates the adoption 24 June 1986, against 26 June on the Newick page; the vault cites the Newick page.
- Verified in this pass: both pages read in the website's source repository (phylipweb/phylip on GitHub), whose pages are served at the URL above.
