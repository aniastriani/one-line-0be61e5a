#!/usr/bin/env python3
"""One Line, One Laugh -- a single funny line, written to /output/entry.txt.

The program is deliberately tiny and deterministic: it holds one
self-contained joke, checks it against the competition gate (one line of
UTF-8 text, 1 to 140 characters, not only whitespace), and writes exactly
those bytes to ``entry.txt`` inside the output directory. No network, no
randomness, no third-party imports -- pure standard library, so the same
bytes come out on every run.
"""

import os
import sys

# The line. One joke, one breath, one twist at the end: the narrator
# automates himself out of his own job, only to end up as his own boss's
# only employee -- he manages himself now, and he is a terrible manager.
LINE = (
    "I replaced myself at work with an AI agent. "
    "It spends all day asking me for permission \u2014 so now I manage me."
)

MAX_CHARS = 140


def validate(line: str) -> None:
    """Enforce the competition gate before anything is written."""
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(line))
        )


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the line, no trailing newline: the gate counts the
    # file's characters, so nothing extra rides along.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
