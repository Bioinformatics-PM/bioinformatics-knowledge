---
aliases:
  - Bash Reference Manual
  - bashref
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
kind: website
tier: A
authors:
  - Chet Ramey
  - Brian Fox
institution: GNU Project, Free Software Foundation
year:
url: "https://www.gnu.org/software/bash/manual/"
access: free
---

# GNU Bash Reference Manual

> [!abstract]
> The official reference manual of Bash, the GNU Project's shell: its syntax, the order of expansions, redirections, builtins, shell options and the rules for exit statuses and signals, maintained together with the shell.

## Why this source

Tutorials paraphrase the shell; this manual defines it. It is where exact semantics are checked: which failures `set -e` ignores, what `pipefail` returns, which exit status a command killed by a signal gets, and in which order a command line is expanded. Use it after a first course such as [[MIT - The Missing Semester of Your CS Education]] or [[Bioinformatics Data Skills (Buffalo)]], as the reference behind them.

## Coverage

Sections verified in this pass are named; the manual covers the whole language.

| Part | Content | Vault notes |
|---|---|---|
| "Shell Expansions" | Order of the expansions (brace, tilde, parameter and arithmetic expansion with command substitution, word splitting, filename expansion); process substitution; word splitting; filename expansion (globbing) | [[Unix Shell]], [[Shell Script]] |
| "Executing Commands": "Environment", "Exit Status", "Signals" | Environment passed to commands; exit statuses (0 success, 126 not executable, 127 not found, 128 + N after fatal signal N); signal handling by the shell | [[Process (Computing)]], [[Command-Line Interface]] |
| "Shell Builtin Commands": "The Set Builtin" | `-e`, `-u` and `-o pipefail`, and the contexts in which `-e` does not exit | [[Shell Script]] |
| Other chapters (not checked section by section) | Quoting, pipelines, redirections, arrays, arithmetic, job control | [[Unix Shell]], [[Process (Computing)]] |

## How to use it

- L1: read "Shell Expansions" once with a terminal open; it explains most quoting bugs.
- L1 to L2: read "The Set Builtin" before writing scripts that must fail loudly, and "Exit Status" before parsing return codes in a pipeline or a [[Workflow Management System]].
- Check the version: the online manual follows the latest Bash release, and servers may run an older one (`bash --version`).

## Caveats

- A reference, not a tutorial: dense, with few examples.
- Describes GNU Bash only; other shells (`sh`, `dash`, `zsh`) differ on arrays, `[[ ]]`, `pipefail` and more.
- Verified in this pass: URL, the "Exit Status" section (statuses 0 to 255, 126, 127, 128 + N) and its neighbours "Environment" and "Signals", "The Set Builtin" (`pipefail` semantics), and the content of "Shell Expansions" (order of expansions, process substitution, word splitting, filename expansion).
