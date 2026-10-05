---
aliases:
  - YAML Ain't Markup Language
  - YAML 1.2.2
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
kind: website
tier: A
authors:
  - Oren Ben-Kiki
  - Clark Evans
  - Ingy döt Net
institution: yaml.org
year: 2021
edition: "1.2.2"
url: "https://yaml.org/spec/1.2.2/"
access: free
---

# YAML Specification

> [!abstract]
> The official definition of YAML, the indentation-based data serialization language used for configuration files and sample sheets, including the schemas that decide whether an unquoted value is read as a string, number or boolean.

## Why this source

Workflow managers and many tools read their configuration from YAML, and YAML's implicit typing is the source of classic bugs (`yes`, `NO` or `3.10` not read as strings). The specification is the only place that says which schema a value is resolved under, and how YAML 1.2 changed the rules of YAML 1.1 to become a superset of JSON.

## Coverage

| Part | Content | Vault notes |
|---|---|---|
| Language overview and syntax | Block (indentation) and flow (`[ ]`, `{ }`) styles, comments, scalars, tags | [[Data Serialization]] |
| Recommended schemas | Failsafe, JSON and Core schemas; the Core schema is the recommended default and resolves only `true`/`false` (with `True`, `TRUE` variants) as booleans | [[Data Serialization]] |
| Changes page | YAML 1.2 made YAML a superset of JSON and replaced the YAML 1.1 type library (where `y`, `yes`, `on`, `NO` were booleans) by the Core schema | [[Data Serialization]] |

Cited in [[Data Serialization]].

## How to use it

- L1: read the overview examples, then the Core schema table to know which unquoted values change type.
- L2: read the changes page before trusting a parser: many libraries still implement YAML 1.1 rules.

## Caveats

- Revision 1.2.2 (2021) clarifies 1.2 (2009) without changing the language.
- Parsers differ: PyYAML follows YAML 1.1 resolution rules, so its output can differ from the 1.2 Core schema (see [[Data Serialization]] for observed examples).
- Verified in this pass: the 1.2.2 specification URL, the statement that YAML 1.2 is a superset of JSON, the Core schema as recommended default, and the YAML 1.1 versus 1.2 boolean rules from the "YAML Specification Changes" page.
