---
aliases:
  - GNU Coreutils
  - Core GNU Utilities
  - coreutils
tags:
  - type/source
  - domain/computer-science
  - level/L1
  - level/L2
kind: website
tier: A
authors:
  - David MacKenzie et al.
institution: GNU Project, Free Software Foundation
year:
url: "https://www.gnu.org/software/coreutils/manual/"
access: free
---

# GNU Coreutils Manual

> [!abstract]
> The official manual of the GNU core utilities, the file, text and shell commands of every Linux system (`ls`, `cp`, `chmod`, `ln`, `cut`, `sort`, `uniq`, `join`, `md5sum`, `sha256sum`, `nohup` and others), one "invocation" section per command.

## Why this source

Man pages summarize options; this manual explains behaviour and its pitfalls, such as how `sort` depends on the locale, why `uniq` and `join` need sorted input, and how file permission bits apply to directories. It is the normative description of the GNU implementation found on Linux servers; read it after the command-line chapters of [[Bioinformatics Data Skills (Buffalo)]].

## Coverage

Sections verified in this pass are named; the manual documents every coreutils command.

| Part | Content | Vault notes |
|---|---|---|
| "sort invocation" | Keys, numeric and other orderings, temporary files; output depends on the locale, `LC_ALL=C` for byte order | [[Unix Text Processing]], [[Sorting]] |
| "uniq invocation" | Only adjacent repeated lines are detected | [[Unix Text Processing]] |
| "join invocation" | Both inputs must be sorted on the join fields | [[Unix Text Processing]] |
| "md5sum invocation" (and the other checksum commands) | Computing digests and checking them against a list with `--check` | [[Secure Shell]], [[Data Integrity]] |
| "nohup invocation" | Running a command immune to hangups; output to `nohup.out` when stdout is a terminal | [[Process (Computing)]] |
| "File permissions": "Mode Structure", "Conditional Executability" | Permission bits for user, group and others; execute (search) permission on directories; `chmod`'s `X` | [[File System]] |
| Other chapters (not checked section by section) | `cut`, `paste`, `comm`, `ln`, `df`, `du`, `timeout`, `stat` | [[Unix Text Processing]], [[File System]], [[Process (Computing)]] |

## How to use it

- L1: read "sort invocation" fully once; it prevents the most common silent errors of command-line data work.
- Look up a command's invocation section whenever a one-liner will be reused in a script.
- `info coreutils 'sort invocation'` opens the same text offline on a GNU system.

## Caveats

- Describes GNU coreutils; macOS and BSD ship different implementations with different options (for example, `stat -c` is GNU syntax).
- Options change across versions; check `sort --version` on the server.
- Verified in this pass: URL, "sort invocation" (locale advice), "uniq invocation" (adjacent lines), "join invocation" (sorted input), "md5sum invocation" (`--check`), "nohup invocation" (`nohup.out`), "Mode Structure" (directory search permission) and "Conditional Executability".
