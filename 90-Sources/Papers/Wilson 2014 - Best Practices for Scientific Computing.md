---
aliases:
  - Best Practices for Scientific Computing
tags:
  - type/source
  - domain/computer-science
  - domain/scientific-practice
  - level/L1
  - level/L2
kind: paper
tier: S
authors:
  - Greg Wilson
  - D. A. Aruliah
  - C. Titus Brown
  - Neil P. Chue Hong
  - Matt Davis
  - Richard T. Guy
journal: PLoS Biology
year: 2014
url: "https://doi.org/10.1371/journal.pbio.1001745"
access: free
---

# Wilson 2014 - Best Practices for Scientific Computing

> [!abstract]
> A short, widely cited paper that distills software-engineering experience into practices any scientist who writes code can adopt, grouped under eight topics.

## Why this source

Written for researchers rather than software engineers, it justifies each practice by the errors it prevents in scientific results. It is the reference behind the Lab's habits of assertions, automated tests and purpose-oriented documentation, and its companion paper [[Wilson 2017 - Good Enough Practices in Scientific Computing]] lowers the bar for beginners.

## Coverage

Citation: Wilson G, Aruliah DA, Brown CT, Chue Hong NP, Davis M, Guy RT, et al. "Best Practices for Scientific Computing". *PLoS Biology* 12(1):e1001745 (2014). doi:10.1371/journal.pbio.1001745. Free at PMC3886731; preprint arXiv:1210.0530.

| Part | Content | Vault notes |
|---|---|---|
| Plan for mistakes | Add assertions (the program halts as soon as something goes wrong; assertions are executable documentation); use an off-the-shelf unit testing library; unit, integration and regression tests run by the computer | [[Defensive Programming]], [[Unit Testing]] |
| Document design and purpose, not mechanics | Documentation explains why and what, not a paraphrase of the code | [[Software Documentation]] |

Cited in [[Unit Testing]], [[Defensive Programming]] and [[Software Documentation]].

## How to use it

- L1: read it in one sitting at the start of [[Software Engineering]]; turn each practice into a line of the checklist of [[01-dna-engine]].
- L2: reread "Plan for mistakes" before [[Numerical Testing]].

## Caveats

- Recommendations, not an empirical study: each practice is argued from experience and cited literature.
- Tools named in the paper date from 2012 to 2014; the practices have not changed.
- Verified in this pass: journal, volume, article number, DOI, PMC and arXiv records, the first six authors (the author list is truncated here), the organization in eight topics with 24 practices, and the content of the "Plan for mistakes" and documentation recommendations summarized above.
