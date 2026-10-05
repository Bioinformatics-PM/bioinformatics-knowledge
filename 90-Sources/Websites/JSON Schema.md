---
aliases:
  - JSON Schema Specification
  - JSON Schema 2020-12
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
kind: website
tier: A
authors:
  - Austin Wright
  - Henry Andrews
  - Ben Hutton
institution: JSON Schema project
year: 2022
edition: "2020-12"
url: "https://json-schema.org/draft/2020-12/draft-bhutton-json-schema-validation-00"
access: free
---

# JSON Schema

> [!abstract]
> The specification of JSON Schema, a JSON vocabulary for describing what a valid JSON document looks like (types, required fields, allowed values, patterns) so that documents can be validated automatically.

## Why this source

JSON itself has no way to say that a record must contain an integer `start` or a strand among `+`, `-` and `.`; JSON Schema does, and it is the format used to publish API and metadata contracts. The 2020-12 release is the current dialect implemented by mainstream validators (for Python, the `jsonschema` package), and its two documents (Core, Validation) define every keyword precisely.

## Coverage

The 2020-12 release consists of "JSON Schema Core" (`draft-bhutton-json-schema-00`) and "JSON Schema Validation" (`draft-bhutton-json-schema-validation-00`), published as IETF Internet-Drafts in June 2022; the dialect's meta-schema is `https://json-schema.org/draft/2020-12/schema`.

| Document | Content | Vault notes |
|---|---|---|
| Core | `$schema`, `$id`, `$ref`; vocabularies; applicator keywords (`properties`, `additionalProperties`, `items`, `allOf`, `anyOf`, `oneOf`, `not`) | [[Data Serialization]] |
| Validation | `type`, `enum`, `const`; numeric (`minimum`, `maximum`), string (`pattern`, `minLength`), array and object (`required`) assertions; `format` as annotation by default, as assertion only with the format-assertion vocabulary | [[Data Serialization]] |

Cited in [[Data Serialization]].

## How to use it

- L1: read the keyword list of the Validation document, then write a schema for one record type of your own (a sample, an interval).
- L2: read the Core sections on applicators and `$ref` when schemas need composition or reuse.

## Caveats

- Internet-Drafts, not RFCs: the specification is maintained by the JSON Schema project and versioned by dialect (draft-04, draft-07, 2019-09, 2020-12); always declare `$schema`, since validators apply the rules of the declared dialect.
- `format` (dates, e-mail addresses) is not checked by default in 2020-12; validators need an explicit option.
- Verified in this pass: the 2020-12 Validation document (title, June 2022 Internet-Draft), the meta-schema URI, and the keywords `type`, `required`, `properties`, `additionalProperties` and `enum` in this dialect.
