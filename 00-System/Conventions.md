---
aliases:
  - Vault Rules
  - Style Guide
tags:
  - type/system
---

# Conventions

The rules of this vault. Every note follows them; `scripts/lint_vault.py` enforces the mechanical parts in CI.

> [!abstract] The model in one line
> **Folder = home domain. Tags = classification. Properties = state and relations. Links = knowledge graph.**

## 1. Folder architecture

```text
00-System/                      how the vault works (this file, Home, Curriculum, dashboards)
01-Biology/                     ┐
02-Chemistry/                   │
03-Physics/                     │
04-Mathematics/                 │  knowledge domains
05-Probability-and-Statistics/  │  (one folder per domain,
06-Computer-Science/            │   numbered subfolders per subdomain)
07-Bioinformatics/              │
08-Scientific-Practice/         │
09-Industry-and-Innovation/     ┘
70-Exercises/                   problem sets too large to live inside a concept note
80-Projects/                    one note per Bioinformatics Lab repository
90-Sources/                     every external source (courses, books, papers, curricula, tools)
98-Assets/                      images and SVG diagrams
99-Templates/                   note templates (Obsidian core Templates plugin)
```

Rules:

- **One home per note.** A note lives in exactly one folder: the domain where the concept is *defined*. Other domains link to it, they never copy it. Example: `Dynamic Programming` lives in Computer Science; the Bioinformatics syllabus links to it.
- **Numbered folders** (`01-`, `02-`) exist only to control order in the file explorer. Notes themselves are never numbered (except project notes, which mirror repository names).
- **Every domain and subdomain folder has one MOC** (Map of Content) named after the folder without its number: `01-Biology/Biology.md`, `01-Biology/02-Molecular-Biology/Molecular Biology.md`. The MOC is the syllabus of that folder.
- Gaps in numbering (`10` to `69`) are reserved for future domains.

## 2. Note types

| Type | Tag | Purpose | Template |
|---|---|---|---|
| Map of Content | `type/moc` | Syllabus of a domain or subdomain: ordered learning path | [[Template - MOC]] |
| Concept | `type/concept` | One idea, explained from L1 to L3 | [[Template - Concept]] |
| Algorithm | `type/algorithm` | One algorithm: problem, recurrence, complexity, implementation | [[Template - Algorithm]] |
| Technique | `type/technique` | One experimental or analytical technique (PCR, RNA-seq) | [[Template - Technique]] |
| Exercise set | `type/exercise` | A problem set in `70-Exercises/` | [[Template - Exercise Set]] |
| Source | `type/source` | One external source in `90-Sources/` | [[Template - Source]] |
| Project | `type/project` | One Bioinformatics Lab repository | [[Template - Project]] |
| System | `type/system` | Vault infrastructure (`00-System/`) | none |

## 3. File naming

- **English, Title Case, singular**: `Nucleotide`, `Sequence Alignment`, `Hidden Markov Model`.
- **Full name first**, acronym as alias: file `Polymerase Chain Reaction`, alias `PCR`. Exception: when the acronym *is* the universal name (`DNA`, `RNA`, `ATP`, `BLAST`).
- **Unique across the whole vault.** Obsidian resolves `[[links]]` by file name, so two notes must never share a name.
- **Forbidden characters**: `/ \ : * ? " < > | # ^ [ ]`. Replace a colon with ` - `.
- **Sources** follow a fixed pattern:

| Kind | Pattern | Example |
|---|---|---|
| Book | `Title (First-Author Surname)` | `Molecular Biology of the Cell (Alberts)` |
| Course | `Institution Code - Title` | `MIT 6.047 - Computational Biology` |
| Course without code | `Institution - Title` | `EMBL-EBI - Introductory Bioinformatics` |
| Curriculum | `Institution - Program` | `Université Paris-Saclay - Licence Sciences de la Vie` |
| Paper | `Surname Year - Short Title` | `Watson 1953 - Molecular Structure of Nucleic Acids` |
| Database, tool, website | Official name | `NCBI GenBank`, `Rosalind`, `Biopython` |

- **Templates**: `Template - <Type>`. **Assets**: lowercase kebab-case, `dna-double-helix.svg`.

## 4. Properties (YAML front matter)

Properties hold **state and relations**. Links inside properties are wikilinks in quotes (`"[[DNA]]"`) so Obsidian indexes them in the graph and backlinks.

| Property | Types | Values | Meaning |
|---|---|---|---|
| `aliases` | all | list of text | Other names, acronyms, French name if useful for search |
| `tags` | all | controlled list (section 5) | Classification |
| `mastery` | concept, algorithm, technique | integer `0` to `5` | Your learning state (section 6) |
| `prerequisites` | concept, algorithm, technique, moc | list of links | What to know **before** this note |
| `related` | concept, algorithm, technique | list of links | Lateral links (same level, other angle) |
| `projects` | concept, algorithm, technique, moc | list of links to `80-Projects` | Lab repositories that implement it |
| `sources` | all content types | list of links to `90-Sources` | Sources used to write the note |
| `kind` | source | `course` `book` `paper` `curriculum` `database` `tool` `website` | Source kind |
| `tier` | source | `S` `A` `B` `C` `D` | Source quality (section 8) |
| `authors` | source | list of text | Authors or instructors |
| `institution` | source | text | University or organization |
| `year` | source | integer | Year of the edition or course run used |
| `edition` | source (book) | text | Edition used |
| `url` | source, project | text | Canonical URL, verified |
| `access` | source | `free` `partial` `paid` | Can the reader open it without paying |
| `repository` | project | text | GitHub URL of the repository |
| `status` | project | `planned` `active` `done` | Project state |

No `created` or `updated` properties: git history is the single source of truth for dates.

## 5. Tags: controlled vocabulary

Tags **classify**; they never hold state. Only the tags below are allowed. Everything else is a link or a property. Three facets, always nested:

| Facet | Allowed values | Cardinality |
|---|---|---|
| `type/` | `moc` `concept` `algorithm` `technique` `exercise` `source` `project` `system` | exactly 1 |
| `domain/` | `biology` `chemistry` `physics` `mathematics` `statistics` `computer-science` `bioinformatics` `scientific-practice` `industry` | 1 or more (not for `type/system`) |
| `level/` | `L1` `L2` `L3` `M1` | 1 or more (not for `type/system`, `type/project`) |

- `domain/`: the home domain **first**, then every other domain the note genuinely belongs to. `Sequence Alignment` → `domain/bioinformatics`, `domain/computer-science`.
- `level/`: every level the note **covers**. A note taking DNA from L1 to L3 carries `level/L1`, `level/L2`, `level/L3`.
- **Never** create topic tags (`#dna`, `#genomics`). Topics are notes; link to them.
- Tags go in the `tags` property, never inline in the body.

Useful searches: `tag:#domain/biology tag:#level/L1`, or `[mastery:0]` for everything not yet started.

## 6. Mastery scale

`mastery` records **your** progress, not the note's completeness. Every note starts at `0`.

| Value | Label | You can… |
|---:|---|---|
| 0 | Unseen | nothing yet |
| 1 | Recognized | recognize the term and give a rough definition |
| 2 | Understood | explain it correctly without notes |
| 3 | Practiced | solve the exercises, or implement it in code |
| 4 | Applied | use it on a real problem or real data (Lab project) |
| 5 | Explained | teach it, including limits and edge cases |

The note's **Mastery checklist** tells you what each step means for that specific concept. [[Dashboard.base|Dashboard]] aggregates mastery per domain.

## 7. Note body

### Levels inside one note

A concept is written **once**, deepening from L1 to L3, instead of three notes. Level sections are headed `## Core (L1)`, `## Deeper (L2)`, `## Advanced (L3)` (and `## Frontier (M1)` when relevant). Omit a level that adds nothing.

### Links

- Wikilinks `[[Note]]`, with display text when needed: `[[Deoxyribose|the sugar]]`.
- Link a concept the **first time** it appears in a section, not every time.
- Links to notes not written yet are allowed and intended: they are the **backlog**. MOCs deliberately list planned notes.
- Headings and blocks: `[[DNA#Core (L1)]]`.

### Callouts (a closed set)

| Callout | Use |
|---|---|
| `> [!abstract]` | One-sentence summary at the top of every note |
| `> [!example]` | Worked example |
| `> [!question]` | Exercise statement |
| `> [!success]-` | Solution, **folded** by default (`-`) so you try first |
| `> [!warning]` | Misconception, pitfall, or model limitation |
| `> [!tip]` | Study advice, mnemonic |
| `> [!info]` | Side fact, history, context |

### Mathematics

LaTeX: inline `$GC = \frac{G + C}{N}$`, display `$$ ... $$`. Define every symbol the first time.

### Diagrams and images

1. **Mermaid** first (flows, pipelines, hierarchies, timelines): renders in Obsidian and on GitHub.
2. **SVG** in `98-Assets/` for spatial figures (structures, genome tracks), embedded with `![[file.svg]]`. Author them by hand or with code; keep them readable on light and dark themes (no pure black or white fills; use mid-tone strokes).
3. **ASCII** only inside code blocks for sequences and alignments, where monospace is the point.
4. External images only with a compatible license (public domain, CC BY, CC BY-SA), credited in the caption.

### Code

Python in fenced blocks, runnable as written, standard library first. Libraries (NumPy, Biopython) only after the concept has been implemented by hand once.

## 8. Sources and citations

**Everything factual is sourced.** No source, no claim.

### Tiers

| Tier | Definition | Example |
|---|---|---|
| S | Complete course or reference textbook from a leading institution, with syllabus and exercises | MIT OCW full course, *Molecular Biology of the Cell* |
| A | Recognized university or scientific organization, excellent targeted resource | EMBL-EBI Training, OpenStax, NCBI Bookshelf |
| B | Recognized educator or author, peer-reviewed tutorial | Rosalind, *Bioinformatics Algorithms* companion site |
| C | Complementary documentation | Tool documentation, Wikipedia for orientation |
| D | Popularization | YouTube, blogs |

Claims in concept notes are backed by **S, A or B** sources. C and D may appear as *further reading*, never as the only support.

### Citation format

Footnotes, pointing to the source note, at the finest granularity you can **verify** (book, then chapter, then section):

```markdown
DNA strands are antiparallel.[^mboc4]

[^mboc4]: [[Molecular Biology of the Cell (Alberts)]], 4th ed., ch. 4 "DNA and Chromosomes".
```

- Every footnote target also appears in the `sources` property.
- Never invent a chapter, page, URL or quote. If the precise location is not verified, cite the source without it.
- Primary literature (papers) is cited for historical or landmark results.

## 9. Mapping to the Bioinformatics Lab

Each concept that a Lab repository implements lists it in `projects`. Each project note in `80-Projects/` lists the concepts it requires. That two-way link is the bridge **theory → implementation**.

## 10. Git workflow

- Work on `dev`; merge to `main` through pull requests only.
- Run `python scripts/lint_vault.py` before every commit.
- Commit messages: imperative, scoped: `biology: add DNA replication`, `system: add algorithm template`.
- Obsidian workspace files are ignored (`.gitignore`); shared settings in `.obsidian/app.json` and `.obsidian/templates.json` are versioned.
