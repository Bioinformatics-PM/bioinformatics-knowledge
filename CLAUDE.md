# CLAUDE.md

Obsidian vault: a self-directed L1 → M1 bioinformatics curriculum. Owner: Pierre Michel. Companion code: the Bioinformatics Lab repositories in the `Bioinformatics-PM` organization.

## Before any change

1. Read `00-System/Conventions.md` fully. It is binding: folders, file names, properties, controlled tags, callouts, citations.
2. Read `00-System/Curriculum.md` and the MOC of the subdomain you work in.
3. Check `90-Sources/` before creating a source note: never duplicate one.

## Writing rules

- English only. Title Case, singular file names, unique across the vault.
- Copy the right template from `99-Templates/`; keep its section order.
- One concept per note, deepened L1 → L2 → L3 inside the note.
- Every factual claim is sourced with a footnote to a source note (tier S, A or B). Never invent a URL, chapter, page, quote or number. Verify sources with web search; cite at the granularity you verified.
- Diagrams: Mermaid first, SVG in `98-Assets/` for spatial figures, ASCII only for sequences in code blocks.
- Code in notes: runnable Python, standard library first.
- New notes start at `mastery: 0`. Never change the owner's `mastery` values.
- A new tag value requires changing `Conventions.md` and `scripts/lint_vault.py` together, in a dedicated commit.
- Update the MOC when adding a note that is not listed in it yet.

## Git

- Work on `dev`. Pull requests from `dev` to `main`. Never push to `main`.
- `python scripts/lint_vault.py` must report 0 errors before each commit.
- Commit messages: `<domain or system>: <imperative summary>`.
