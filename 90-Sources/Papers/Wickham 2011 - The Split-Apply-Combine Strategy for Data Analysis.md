---
aliases:
  - Wickham 2011
  - plyr paper
tags:
  - type/source
  - domain/statistics
  - domain/computer-science
  - level/L2
  - level/L3
kind: paper
tier: A
authors:
  - Hadley Wickham
journal: Journal of Statistical Software
year: 2011
url: "https://www.jstatsoft.org/v40/i01"
access: free
---

# Wickham 2011 - The Split-Apply-Combine Strategy for Data Analysis

> [!abstract]
> The paper that named the split-apply-combine strategy: break a large problem into manageable pieces, operate on each piece independently, then put the pieces back together; it presents the R package plyr, which implements the strategy.

## Why this source

It is the primary reference for the name and the pattern behind every group-by operation in data analysis. pandas' group operations are introduced with this term, credited to Wickham ([[Python for Data Analysis (McKinney)]]), so the paper is the origin of the vocabulary used in Python as well as in R. Peer-reviewed and open access.

## Coverage

Citation: Wickham H. "The Split-Apply-Combine Strategy for Data Analysis". *Journal of Statistical Software* 40(1):1-29 (2011).

| Part | Content | Vault notes |
|---|---|---|
| Strategy | Split a problem into pieces, operate on each independently, combine the results | [[Split-Apply-Combine]] |
| Software | The plyr package for R | [[R Programming]] |
| Case studies | Batting records of veteran baseball players; a large 3-D spatio-temporal array of ozone measurements | [[Split-Apply-Combine]] |

## How to use it

- L2: read the introduction and the description of the strategy with [[Split-Apply-Combine]], then map each step to pandas `groupby` and SQL `GROUP BY` ([[SQL]]).
- L3: read the case studies to see the same strategy applied to data frames and to multidimensional arrays.

## Caveats

- Examples are in R, with the plyr package of 2011; current R and Python libraries use other function names for the same operations.
- Verified in this pass: author, title, journal, volume, issue, pages, year and journal URL; the abstract's description of the strategy, of plyr and of the two case studies.
