---
aliases: []
tags:
  - type/system
---

# Roadmap

How the vault itself gets built. The learner's path is the [[Curriculum]]; this page tracks the writing.

## Phase 0 - Foundations of the vault

- [x] Conventions, templates, controlled tags, lint and CI
- [x] Dashboards: progress, sources, glossary
- [x] Syllabus (MOC) for every domain and subdomain, L1 to L3
- [x] Verified source registry: courses, books, papers, curricula, databases
- [x] Curriculum benchmark against university programs
- [x] Reference track: molecular biology core concepts, fully written

## Phase 1 - Stage 1 content

Write every Stage 1 concept of the syllabi, in parallel with [[01-dna-engine]] and [[02-sequence-translation]]:
[[Cell Biology]], [[Molecular Biology]], [[Genetics]], [[General Chemistry]], [[Mathematical Foundations]], [[Calculus]], [[Probability]], [[Descriptive Statistics]], [[Programming]], [[Data Structures]], [[Algorithms]], [[Bioinformatics Foundations]], [[Scientific Method]].

## Phase 2 - Stage 2 content

Stage 2 of each syllabus, with [[03-genome-diff]] to [[06-mutation-lab]]. Exercise sets in `70-Exercises/`.

## Phase 3 - Stage 3 and 4 content

Stage 3 and 4, with [[07-evolution-simulator]] to [[10-genomic-pipeline]]. Landmark papers read and reproduced.

## Later, when needed

- Publish the vault as a website (for example with Quartz on GitHub Pages) so that wikilinks render outside Obsidian.
- Generate progress bars per domain from `mastery` with a script.
- Specialization tracks after Stage 4.

Run `python scripts/lint_vault.py --backlog` to list every planned note, most referenced first: it is the writing queue.
