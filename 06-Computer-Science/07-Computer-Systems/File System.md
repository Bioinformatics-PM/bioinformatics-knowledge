---
aliases:
  - Filesystem
  - Unix File System
  - File Permissions
  - Hard Link
  - Symbolic Link
  - Système de fichiers
tags:
  - type/concept
  - domain/computer-science
  - domain/bioinformatics
  - level/L1
  - level/L2
mastery: 0
prerequisites:
  - "[[Unix Shell]]"
related:
  - "[[Process (Computing)]]"
  - "[[Secure Shell]]"
  - "[[High-Performance Computing]]"
  - "[[Parallel File System]]"
projects:
  - "[[10-genomic-pipeline]]"
sources:
  - "[[GNU Coreutils Manual]]"
  - "[[HPC Carpentry - Introduction to High-Performance Computing]]"
  - "[[Bioinformatics Data Skills (Buffalo)]]"
  - "[[MIT - The Missing Semester of Your CS Education]]"
  - "[[Python Documentation]]"
---

# File System

> [!abstract]
> A Unix file system is one tree of directories rooted at `/`, in which names point to files whose metadata (owner, permission bits, size) live apart from their names: paths, permissions, links and storage tiers decide where data can live, who can read it, and whether it survives.

## Definition

A **file system** organizes storage as a tree of directories rooted at `/`. A directory maps names to files; the file itself, its **inode** (type, owner, group, permission bits, size, timestamps, location of the data), is distinct from its names. One file can therefore have several names (**hard links**), while a **symbolic link** is a separate small file that stores a path.[^cu] A **path** is **absolute** if it starts at `/`, **relative** otherwise, resolved from the current directory of the [[Process (Computing)|process]].[^ms26]

## Why it matters

- On a cluster, home, project and scratch storage differ in speed, allocation and backup: where raw data, intermediate files and results live decides what survives a purge or a disk failure.[^hpcexplore]
- Raw sequencing data should be read-only and shared references linked rather than copied; relative paths decide whether a [[Shell Script|script]] still works elsewhere ([[Research Data Management]], [[Data Integrity]]).[^buffalo]

## Core (L1)

**Permission bits.** Each file has an owner, a group, and three triplets of bits for the owner (`u`), the group (`g`) and others (`o`): read, write, execute. On a directory, read means listing names, write means creating, deleting or renaming entries, and execute means **search**: accessing entries by name.[^cuperm] Each octal digit sums r = 4, w = 2, x = 1: 644 (`-rw-r--r--`) for an ordinary file, 444 for raw data, 600 for a private key ([[Secure Shell]]), 750 (`drwxr-x---`) for a directory the group may read.

The demonstrations were run as an unprivileged owner (root bypasses permission bits) on invented files:

```console
$ mkdir -p proj/raw && cp reads.fq.gz proj/raw/ && chmod a-w proj/raw/reads.fq.gz
stat -c "%A %a %n" proj/raw proj/raw/reads.fq.gz
echo "@extra" >> proj/raw/reads.fq.gz
rm -f proj/raw/reads.fq.gz && echo "deleted anyway"
drwxr-xr-x 755 proj/raw
-r--r--r-- 444 proj/raw/reads.fq.gz
bash: line 3: proj/raw/reads.fq.gz: Permission denied
deleted anyway
```

The file could not be modified but could be deleted, because deletion edits the **directory**. With the directory read-only too (`chmod a-w proj/raw`, mode 555), `rm` fails with `Permission denied`.

**Links.** A hard link is a second name for the same inode; a symbolic link stores a path and breaks when the target moves:[^cu]

```console
$ echo ACGT > genome.fa; ln genome.fa hard.fa; ln -s genome.fa soft.fa
stat -c "%i %h %F %n" genome.fa hard.fa soft.fa
mv genome.fa moved.fa; cat hard.fa; cat soft.fa; readlink soft.fa
1974535 2 regular file genome.fa
1974535 2 regular file hard.fa
1974536 1 symbolic link soft.fa
ACGT
cat: soft.fa: No such file or directory
genome.fa
```

A relative symlink target is resolved from the **link's** directory, not from where `ln` ran (Exercise 2). Symlinks let every project point to one shared reference genome.

**Storage tiers.** The usual places on a cluster, each with its own allocation and backup policy:[^hpcexplore]

| Tier | Properties | Put there |
|---|---|---|
| Home | network file system, often backed up, slower | code, configuration |
| Scratch | faster, usually not backed up, not for long-term storage | intermediate files of running jobs |
| Work or project (some sites) | fast network storage, may not be backed up | shared inputs and results |

Anything that cannot be regenerated must not live only on scratch. `du -sh dir` measures a directory; `df -h .` and `df -i .` give the free space and free inodes of the file system holding `.`.[^cu]

## Deeper (L2)

**Which triplet applies.** The class is chosen first (owner, else group member, else other) and only its triplet is checked; bits are not combined. After `chmod 044 g.txt` (`----r--r--`), `cat g.txt` fails with `Permission denied` for the owner, although group and others may read.

**Names versus data.** Renaming within one file system only changes a directory entry (`mv a.txt b.txt` kept inode 1968256), so moving 100 GB inside scratch is instantaneous; `mv` to another file system copies the data, then removes the source.[^cu] Data also outlive their last name while a process holds the file open: after `seq 1 100000 > big.txt; exec 3< big.txt; rm big.txt`, `ls big.txt` fails, `readlink /proc/$$/fd/3` shows `big.txt (deleted)`, and `wc -l <&3` still counts 100000 lines. This is why `df` can report a full disk that `du` cannot account for: a running job still holds deleted files open ([[Process (Computing)]]).

**Inodes are finite.** `df -i` counts them apart from bytes (here 16,777,216 inodes, 199,408 used): millions of small files, such as one per read, can exhaust them before the space runs out. Pack such data into archives or a few large files; [[Parallel File System]] explains why shared cluster storage prefers that too.

## Mathematical representation

Mode bits are three octal digits $m = 64u + 8g + o$, each of $u, g, o \in \{0, \dots, 7\}$ a sum of $r = 4$, $w = 2$, $x = 1$. The hierarchy is a rooted tree; hard links give some files several parents (still acyclic, since directories cannot be hard-linked on most systems), and symbolic links add arbitrary edges, cycles included, which is why `find` and Python's `os.walk` do not follow them by default.[^cu][^pydoc]

## Computational representation

`pathlib` and `os.stat` expose the same metadata; `lstat` describes a link itself rather than its target ([[File Input and Output]]):

```python
import os
import stat
from pathlib import Path

lab = Path("lab")
lab.mkdir()
(lab / "genome.fa").write_text(">chr1\nACGT\n", encoding="ascii")
os.link(lab / "genome.fa", lab / "hard.fa")              # second name, same inode
(lab / "soft.fa").symlink_to("genome.fa")                # stores a path
(lab / "dangling.fa").symlink_to("../old/genome.fa")     # target does not exist
for p in sorted(lab.iterdir()):
    st = p.lstat()                                       # the link itself, not its target
    print(f"{p.name:12} {stat.filemode(st.st_mode)} nlink={st.st_nlink}")
print((lab / "genome.fa").stat().st_ino == (lab / "hard.fa").stat().st_ino)
```

Output:

```text
dangling.fa  lrwxrwxrwx nlink=1
genome.fa    -rw-r--r-- nlink=2
hard.fa      -rw-r--r-- nlink=2
soft.fa      lrwxrwxrwx nlink=1
True
```

## Worked example

> [!example] Sharing results with the group (invented project)
> A collaborator in your group cannot open `share/results/table.tsv`. `namei -l` shows the mode of every component of the path:
>
> ```console
> $ namei -l share/results/table.tsv
> f: share/results/table.tsv
> drwx------ root root share
> drwx------ root root results
> -rw------- root root table.tsv
> $ chmod g+x share; chmod -R g+rX share/results
> $ namei -l share/results/table.tsv
> f: share/results/table.tsv
> drwx--x--- root root share
> drwxr-x--- root root results
> -rw-r----- root root table.tsv
> ```
>
> Every directory on the path needs `x` for the group; `share` gets `x` only, so its other contents stay unlisted. Capital `X` adds execute only to directories (and files already executable): `results` got `r-x`, `table.tsv` only `r--`.[^cuperm] Nobody gets `w`: collaborators cannot alter the results.

## Common misconceptions

> [!warning] "A read-only file cannot be deleted"
> Deletion needs write permission on the directory. Make raw data files *and* their directory read-only.

> [!warning] "Deleting files frees their space immediately"
> Not while a process holds them open; the space returns when the last descriptor closes.

## Exercises

> [!question] Exercise 1 (L1)
> Decode `drwxr-x---` and `-rw-r-----` into octal, and say what a group member and another user can do with each.

> [!success]- Solution
> 750 and 640. A group member can list and enter the directory and read the file, but modify neither; other users can do nothing, not even reach the file by name, since they lack `x` on the directory.

> [!question] Exercise 2 (L1)
> From the directory holding `ref/` and `proj2/`, `ln -s ref/genome.fa proj2/data/genome.fa` creates a broken link. Why? Give two fixes.

> [!success]- Solution
> The stored path `ref/genome.fa` is resolved from `proj2/data/`, which has no `ref/` (`cat` reports `No such file or directory`). Store the path relative to the link, `ln -sfn ../../ref/genome.fa proj2/data/genome.fa`, or let GNU `ln -sr ref/genome.fa proj2/data/g2.fa` compute it (`readlink` prints `../../ref/genome.fa`). An absolute path also works but breaks when the tree moves.

> [!question] Exercise 3 (L2, Python)
> Write `audit(root)` reporting broken symbolic links and files with several hard links, without following links; run it on `lab`.

> [!success]- Solution
> ```python
> def audit(root):
>     for dirpath, dirnames, filenames in os.walk(root):  # does not follow symlinks
>         for name in sorted(filenames + dirnames):
>             p = Path(dirpath, name)
>             if p.is_symlink() and not p.exists():
>                 print("broken symlink:", p, "->", os.readlink(p))
>             elif not p.is_symlink() and p.is_file() and p.stat().st_nlink > 1:
>                 print("hard-linked:", p, "links:", p.stat().st_nlink)
>
> audit(lab)
> # broken symlink: lab/dangling.fa -> ../old/genome.fa
> # hard-linked: lab/genome.fa links: 2
> # hard-linked: lab/hard.fa links: 2
> ```
>
> `exists()` follows the link, so it is False exactly when the target is missing. `genome.fa` and `hard.fa` are one file: deleting one "duplicate" frees nothing.

## Mastery checklist

- [ ] 1 Recognized: I can read a mode string and tell absolute from relative paths.
- [ ] 2 Understood: I can explain directory permissions, hard versus symbolic links, and the roles of home, project and scratch storage.
- [ ] 3 Practiced: I set read-only raw data and group-readable results, and create relative symlinks that resolve.
- [ ] 4 Applied: I lay out a real cluster project for [[10-genomic-pipeline]]: raw data read-only, references linked, intermediates on scratch, results backed up.
- [ ] 5 Explained: I can teach why deleted files may still use space, why millions of small files are a problem, and how the permission class is chosen.

## References

[^cu]: [[GNU Coreutils Manual]] (`ln`, `mv`, `stat`, `du`, `df`).
[^cuperm]: [[GNU Coreutils Manual]], "File permissions": "Mode Structure" (directory search permission) and "Conditional Executability" (`X`).
[^hpcexplore]: [[HPC Carpentry - Introduction to High-Performance Computing]], episode "Exploring remote resources" (home, scratch and work storage).
[^buffalo]: [[Bioinformatics Data Skills (Buffalo)]], project organization and raw data handling.
[^ms26]: [[MIT - The Missing Semester of Your CS Education]], 2026 lecture "Course Overview + Introduction to the Shell".
[^pydoc]: [[Python Documentation]], `os` and `pathlib` modules.
