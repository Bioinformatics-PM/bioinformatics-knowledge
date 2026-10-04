---
aliases:
  - The DOI Handbook
  - Digital Object Identifier Handbook
tags:
  - type/source
  - domain/scientific-practice
  - level/L1
  - level/L2
  - level/L3
kind: website
tier: A
authors: []
institution: International DOI Foundation
year: 2026
edition:
url: https://www.doi.org/doi-handbook/HTML/doi-name-syntax2.html
access: free
---

# DOI Handbook

> [!abstract]
> The International DOI Foundation's reference manual for the Digital Object Identifier (DOI) system: the syntax of a DOI name, how names are assigned, and how they resolve.

## Why this source

Every paper cited in this vault carries a DOI in its `url`. The Handbook is the normative text for what a DOI name is, which matters as soon as DOIs are compared, deduplicated or validated in code ([[Reference Management]], [[Persistent Identifier]]).

## Coverage

Verified in this pass: section 2.2 (DOI name syntax).

| Part | Content | Vault notes |
|---|---|---|
| 2.2.1 General characteristics | A DOI name is a prefix and a suffix separated by a forward slash; it is case-insensitive and may use any printable Unicode characters | [[Reference Management]] |
| 2.2.2 Prefix | Directory indicator `10`, a full stop, then the registrant code | [[Reference Management]], [[Persistent Identifier]] |
| Suffix | Unique within its prefix; no length limit set by the DOI system | [[Reference Management]] |
| Resolution | How a DOI name resolves to the current location of the object | [[Persistent Identifier]] |

## How to use it

- **L1**: read section 2.2 to split any DOI into prefix and suffix.
- **L2**: apply case-insensitivity when matching references from different exports.
- **L3**: read the resolution chapters before minting DOIs for data or software ([[Data Repository]], [[Software Release]]).

## Caveats

- The `url` points to the name-syntax section; the Handbook is a living document and `year` is the version consulted.
- Only section 2.2 was checked in this pass; resolution and registration details are cited at Handbook level only.
