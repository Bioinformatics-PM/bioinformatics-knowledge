#!/usr/bin/env python3
"""Lint the Obsidian vault against 00-System/Conventions.md.

Errors (exit code 1): broken front matter, tags outside the controlled
vocabulary, invalid properties, duplicate or illegal file names, notes in the
wrong folder, undefined footnotes.

Warnings: links to notes that do not exist yet. They are the backlog, so they
never fail the build; `--backlog` lists them by number of references.

Usage:
    python scripts/lint_vault.py            # lint
    python scripts/lint_vault.py --backlog  # lint, then list planned notes
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

IGNORED_DIRS = {".git", ".github", ".obsidian", ".trash", "scripts", "99-Templates"}
ASSET_SUFFIXES = {".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".base"}

TYPES = {"moc", "concept", "algorithm", "technique", "exercise", "source", "project", "system"}
DOMAINS = {
    "biology",
    "chemistry",
    "physics",
    "mathematics",
    "statistics",
    "computer-science",
    "bioinformatics",
    "scientific-practice",
    "industry",
}
LEVELS = {"L1", "L2", "L3", "M1"}

MASTERY_TYPES = {"concept", "algorithm", "technique"}
LINK_PROPERTIES = ("prerequisites", "related", "projects", "sources")
SOURCE_KINDS = {"course", "book", "paper", "curriculum", "database", "tool", "website"}
SOURCE_TIERS = {"S", "A", "B", "C", "D"}
SOURCE_ACCESS = {"free", "partial", "paid"}
PROJECT_STATUS = {"planned", "active", "done"}

TYPE_FOLDERS = {
    "system": "00-System",
    "exercise": "70-Exercises",
    "project": "80-Projects",
    "source": "90-Sources",
}

FORBIDDEN_NAME_CHARS = re.compile(r'[/\\:*?"<>|#^\[\]]')
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FENCED_CODE = re.compile(r"^(```|~~~).*?^\1", re.DOTALL | re.MULTILINE)
INLINE_CODE = re.compile(r"`[^`\n]*`")
WIKILINK = re.compile(r"!?\[\[([^\]\n]+?)\]\]")
FOOTNOTE_REF = re.compile(r"\[\^([^\]\s]+)\](?!:)")
FOOTNOTE_DEF = re.compile(r"^\[\^([^\]\s]+)\]:", re.MULTILINE)
PROPERTY_LINK = re.compile(r"^\[\[[^\]]+\]\]$")


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, path: Path, message: str) -> None:
        self.errors.append(f"{path.relative_to(ROOT)}: {message}")


def vault_files() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if not path.is_file() or rel.parts[0] in IGNORED_DIRS:
            continue
        if len(rel.parts) == 1 and path.suffix == ".md":
            continue  # README.md, CLAUDE.md: repository files, not notes
        files.append(path)
    return files


def link_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    return Path(target).name if "/" in target else target


def strip_code(text: str) -> str:
    return INLINE_CODE.sub("", FENCED_CODE.sub("", text))


def check_tags(path: Path, tags: object, report: Report) -> str | None:
    if not isinstance(tags, list) or not tags:
        report.error(path, "`tags` must be a non-empty list")
        return None
    facets: dict[str, list[str]] = defaultdict(list)
    for tag in tags:
        facet, _, value = str(tag).partition("/")
        allowed = {"type": TYPES, "domain": DOMAINS, "level": LEVELS}.get(facet)
        if allowed is None or value not in allowed:
            report.error(path, f"tag `{tag}` is not in the controlled vocabulary")
            continue
        facets[facet].append(value)
    if len(facets["type"]) != 1:
        report.error(path, "exactly one `type/` tag is required")
        return None
    note_type = facets["type"][0]
    if note_type != "system" and not facets["domain"]:
        report.error(path, "at least one `domain/` tag is required")
    if note_type not in {"system", "project"} and not facets["level"]:
        report.error(path, "at least one `level/` tag is required")
    for facet, values in facets.items():
        if len(values) != len(set(values)):
            report.error(path, f"duplicate `{facet}/` tag")
    return note_type


def check_properties(path: Path, note_type: str, meta: dict, report: Report) -> None:
    if note_type in MASTERY_TYPES:
        mastery = meta.get("mastery")
        if not isinstance(mastery, int) or isinstance(mastery, bool) or not 0 <= mastery <= 5:
            report.error(path, "`mastery` must be an integer from 0 to 5")
    for name in LINK_PROPERTIES:
        value = meta.get(name)
        if value is None:
            continue
        if not isinstance(value, list) or not all(
            isinstance(item, str) and PROPERTY_LINK.match(item) for item in value
        ):
            report.error(path, f"`{name}` must be a list of quoted wikilinks")
    if note_type == "source":
        for name, allowed in (("kind", SOURCE_KINDS), ("tier", SOURCE_TIERS), ("access", SOURCE_ACCESS)):
            if meta.get(name) not in allowed:
                report.error(path, f"`{name}` must be one of {sorted(allowed)}")
        if not meta.get("url"):
            report.error(path, "`url` is required for a source")
    if note_type == "project" and meta.get("status") not in PROJECT_STATUS:
        report.error(path, f"`status` must be one of {sorted(PROJECT_STATUS)}")
    folder = TYPE_FOLDERS.get(note_type)
    if folder and path.relative_to(ROOT).parts[0] != folder:
        report.error(path, f"`type/{note_type}` notes belong in `{folder}/`")


def property_links(meta: dict) -> list[str]:
    links = []
    for value in meta.values():
        items = value if isinstance(value, list) else [value]
        for item in items:
            if isinstance(item, str):
                links.extend(WIKILINK.findall(item))
    return links


def lint(show_backlog: bool) -> int:
    report = Report()
    files = vault_files()
    names: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        key = path.stem if path.suffix == ".md" else path.name
        names[key.lower()].append(path)
        if FORBIDDEN_NAME_CHARS.search(path.stem):
            report.error(path, "file name contains a forbidden character")
    for paths in names.values():
        if len(paths) > 1:
            listed = ", ".join(str(p.relative_to(ROOT)) for p in paths)
            report.errors.append(f"duplicate note name: {listed}")

    templates = {p.stem.lower() for p in (ROOT / "99-Templates").glob("*.md")}
    resolvable = set(names) | templates
    backlog: Counter[str] = Counter()
    for path in files:
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        match = FRONT_MATTER.match(text)
        if not match:
            report.error(path, "missing YAML front matter")
            continue
        try:
            meta = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as exc:
            report.error(path, f"invalid YAML: {exc.problem if hasattr(exc, 'problem') else exc}")
            continue
        if not isinstance(meta, dict):
            report.error(path, "front matter must be a mapping")
            continue
        note_type = check_tags(path, meta.get("tags"), report)
        if note_type:
            check_properties(path, note_type, meta, report)

        body = strip_code(text[match.end():])
        refs = set(FOOTNOTE_REF.findall(body))
        defs = set(FOOTNOTE_DEF.findall(body))
        for missing in sorted(refs - defs):
            report.error(path, f"footnote [^{missing}] is referenced but not defined")

        for raw in WIKILINK.findall(body) + property_links(meta):
            target = link_target(raw)
            if not target:
                continue  # same-note heading link: [[#Heading]]
            if target.lower() not in resolvable:
                backlog[target] += 1

    for error in report.errors:
        print(f"ERROR   {error}")
    print(
        f"\n{len(files)} files, {len(report.errors)} errors, "
        f"{len(backlog)} planned notes (unresolved links, {sum(backlog.values())} references)"
    )
    if show_backlog:
        print("\nBacklog (planned notes by number of references):")
        for target, count in backlog.most_common():
            print(f"  {count:4d}  {target}")
    return 1 if report.errors else 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--backlog", action="store_true", help="list planned notes")
    sys.exit(lint(parser.parse_args().backlog))


if __name__ == "__main__":
    main()
