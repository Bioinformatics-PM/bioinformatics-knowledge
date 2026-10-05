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
- [x] Syllabus (MOC) for every domain and subdomain: 9 domains, 62 subdomains, 1,360 concepts, each with exactly one home
- [x] Source registry: university courses, textbooks, landmark papers, degree programs, databases and tools
- [x] Curriculum benchmark against 13 programs (France, United States, Europe, China) and the ISCB competencies
- [x] Reference track, fully written: [[Nucleotide]], [[DNA]], [[RNA]], [[Central Dogma]], [[DNA Replication]], [[Transcription]], [[Genetic Code]], [[Translation]], [[Gene]], [[Mutation]]

## Phase 1 - Stage 1 content

- [x] Write the 341 Stage 1 concepts of the syllabi (see [[Curriculum#Stage 1 - Foundations|Stage 1]]) across the nine domains, each sourced, with figures, runnable code and graded exercises
- [ ] Build [[01-dna-engine]] and [[02-sequence-translation]] on top of them

## Phase 2 - Stage 2 content

Stage 2 of each syllabus, with [[03-genome-diff]] to [[06-mutation-lab]]. Exercise sets in `70-Exercises/`.

## Phase 3 - Stage 3 and 4 content

Stage 3 and 4, with [[07-evolution-simulator]] to [[10-genomic-pipeline]]. Landmark papers read and reproduced.

## Later, when needed

- Publish the vault as a website (for example with Quartz on GitHub Pages) so that wikilinks render outside Obsidian.
- Generate progress bars per domain from `mastery` with a script.
- Specialization tracks after Stage 4.

Run `python scripts/lint_vault.py --backlog` to list every planned note, most referenced first: it is the writing queue.
