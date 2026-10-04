---
aliases:
  - Codd 1970
  - Relational model paper
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
kind: paper
tier: A
authors:
  - Edgar F. Codd
journal: Communications of the ACM
year: 1970
url: "https://doi.org/10.1145/362384.362685"
access: free
---

# Codd 1970 - A Relational Model of Data for Large Shared Data Banks

> [!abstract]
> The paper that founded relational databases: data described as mathematical relations on domains, independent of how it is ordered, indexed or accessed, with keys linking relations and a normal form removing nested structure.

## Why this source

Every relational database management system descends from this model. Codd, then at IBM, argued that users of large shared data banks should not depend on the machine representation (ordering, indexes, access paths) and proposed n-ary relations as the user's view; the paper defines relations, primary and foreign keys and a normal form, and sketches the "universal data sublanguage" that became relational algebra and SQL. It is short and readable, and the right primary source for the definitions.

## Coverage

Citation: Codd EF. "A Relational Model of Data for Large Shared Data Banks". *Communications of the ACM* 13(6):377-387, June 1970. doi:10.1145/362384.362685.

| Part | Content | Vault notes |
|---|---|---|
| Relational model and normal form | Data dependencies of existing systems (ordering, indexing, access paths); relations as sets of n-tuples over domains; properties of the table representation (rows distinct, row order immaterial); primary and foreign keys; normal form | [[Relational Database]], [[Database Normalization]] |
| Linguistic aspects | A universal data sublanguage based on first-order predicate calculus | [[SQL]], [[Relational Algebra]] |
| Redundancy and consistency | Operations on relations (permutation, projection, join, composition), redundancy and consistency of a set of relations | [[Relational Algebra]], [[Database Normalization]] |

Cited in [[Relational Database]] and [[SQL]].

## How to use it

- L1: read section 1 for the definitions of relation, primary key and foreign key, with [[Relational Database]].
- L2: read section 2 with [[Relational Algebra]] and [[Database Normalization]].

## Caveats

- Terminology predates SQL: Codd's "domains" are roughly typed columns, and his column order is significant (he introduces attribute names to remove that dependence).
- Primary literature from 1970: later work (normal forms beyond the first, SQL's NULLs and bag semantics) is in textbooks and courses such as [[CMU 15-445 - Database Systems]].
- Verified in this pass: citation, DOI, June 1970 issue, and the abstract's topics (n-ary relations, normal form, universal data sublanguage, redundancy and consistency); free copies are hosted by several universities.
