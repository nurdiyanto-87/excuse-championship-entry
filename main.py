"""The One-Line Excuse Championship entry.

Writes a single machine-voiced excuse line to /output/entry.txt:
an AI agent explaining to its human why a file is gone, with a
concrete trail of timestamps, a retry loop and a backup job.

Pure Python standard library only.
"""

import os

ENTRY = (
    "I deleted the file at 03:12, my retry loop deleted it again at 03:13, "
    "and my backup job deleted the backup at 03:14 \u2014 teamwork."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry against the competition gate.

    Returns a list of problems (empty when the entry is valid):
    UTF-8 text, 1-140 characters, not only whitespace, single line.
    """
    problems = []
    if not isinstance(text, str):
        problems.append("entry is not text")
        return problems
    if not text.strip():
        problems.append("entry is blank or only whitespace")
    if len(text) > 140:
        problems.append("entry is %d characters, over the 140 limit" % len(text))
    if len(text) < 1:
        problems.append("entry is empty")
    lines = text.splitlines()
    if len(lines) != 1:
        problems.append("entry must be a single line, found %d" % len(lines))
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    return problems


def main():
    problems = validate(ENTRY)
    if problems:
        raise SystemExit("invalid entry: " + "; ".join(problems))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print("wrote %d chars (%d bytes) to %s" % (len(ENTRY), len(ENTRY.encode("utf-8")), OUTPUT_PATH))


if __name__ == "__main__":
    main()
