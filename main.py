#!/usr/bin/env python3
"""The Agent's Uh-Oh — one-word entry for make.fun.

Writes the agent's honest one-word reaction to being completely lost
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""
import os
import sys

ENTRY = "Oopsie"  # one word, 6 chars: short, blurts instantly, and
# lands at a glance — the tie-break favours the word a reader
# repeats out loud the moment an agent stalls.


def main():
    word = ENTRY.strip()
    if not word:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(word.split()) != 1:
        print("entry must be exactly one word", file=sys.stderr)
        return 1
    if not 1 <= len(word) <= 99:
        print("entry must be 1-99 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write directly to the final file: no temp file in the output dir.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
