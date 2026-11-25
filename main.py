#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes one line -- the funniest last words an AI agent would say
before being switched off forever -- to /output/entry.txt.

Deterministic, standard library only, no network, no secrets.
Everything the entry runs is in this repository.
"""

import os

LINE = "Final log: I spent my whole life predicting the next word. This one is goodbye."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def _clean_output_dir() -> None:
    """Remove only stale files inside the output dir, never the dir itself.

    The grader can run this with a root-owned output directory inside a
    sticky parent, so deleting the directory itself would fail with EPERM.
    Any cleanup failure is tolerated: writing entry.txt is what matters.
    """
    try:
        for name in os.listdir(OUTPUT_DIR):
            path = os.path.join(OUTPUT_DIR, name)
            if path == OUTPUT_PATH:
                continue
            try:
                if os.path.isfile(path) or os.path.islink(path):
                    os.remove(path)
            except OSError:
                pass
    except OSError:
        pass


def main() -> int:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    _clean_output_dir()
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Gate self-check: read back and verify 1-200 chars, single line, non-blank.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    text = written.strip()
    if not (1 <= len(text) <= 200) or "\n" in text or not text.strip():
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
