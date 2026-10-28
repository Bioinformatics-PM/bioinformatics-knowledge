---
aliases:
  - Wickham 2014
  - Tidy Data paper
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
year: 2014
url: "https://doi.org/10.18637/jss.v059.i10"
access: free
---

# Wickham 2014 - Tidy Data

> [!abstract]
> The paper that defined tidy data: each variable forms a column, each observation forms a row, and each type of observational unit forms a table; such datasets are easy to manipulate, model and visualize, and a small set of tools turns messy datasets into tidy ones.

## Why this source

It gives the standard vocabulary for how a data table should be laid out before analysis, the layout that data frame libraries, plotting libraries and model formulas expect. The three rules are short enough to check on every sample sheet and results table. Peer-reviewed and open access.

## Coverage

Citation: Wickham H. "Tidy Data". *Journal of Statistical Software* 59(10):1-23 (2014). doi:10.18637/jss.v059.i10.

| Part | Content | Vault notes |
|---|---|---|
| Definition | Variables in columns, observations in rows, one table per type of observational unit | [[Tidy Data]], [[Data Frame]] |
| Tidying | A small set of tools restructures messy datasets into tidy ones | [[Tidy Data]], [[Split-Apply-Combine]] |
| Analysis | Tidy datasets are easy to manipulate, model and visualize | [[Data Visualization]] |

## How to use it

- L2: read the definition with [[Tidy Data]] and [[Data Frame]], then classify the tables of a real project (sample sheet, count table, results table) against the three rules.
- L3: read the tidying case studies alongside the reshaping operations of [[Split-Apply-Combine]].

## Caveats

- Examples are in R, with the packages of 2014; the reshaping functions have been renamed since in both R and Python.
- Verified in this pass: author, title, journal, volume, issue, pages, year and DOI; the abstract's definition (the three rules) and its claims about tidy datasets and tools. Later formulations of the definition by the same author were not checked.
