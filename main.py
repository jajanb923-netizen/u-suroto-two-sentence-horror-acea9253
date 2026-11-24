#!/usr/bin/env python3
"""Two-Sentence Horror entry for the make.fun bounty
u-suroto-two-sentence-horror-acea9253.

Writes the chosen two-sentence horror story to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt for local runs).

Python 3.13 stdlib only, deterministic, no network.
"""

import os
import re
import sys

STORY = (
    "The sleep clinic gave me a recorder for the nights I kept waking "
    "up screaming with no memory of a dream. "
    "On the playback, I am the one screaming, but I am also the one in "
    "the corner of the room, whispering the words that make me scream."
)

# Sentence terminators followed by a space or the end of the text.
_SENTENCE_END = re.compile(r"[.!?](?:\s+|$)")


def sentence_count(text: str) -> int:
    """Count sentences by terminal punctuation (., !, ?)."""
    return len(_SENTENCE_END.findall(text))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = STORY.strip()
    # Self-check: the kit gate (UTF-8, 1-400 characters, not only whitespace)
    # plus the brief's own rule — exactly two sentences.
    if not 1 <= len(text) <= 400:
        print(f"gate failed: {len(text)} characters", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: empty entry", file=sys.stderr)
        return 1
    if sentence_count(text) != 2:
        print(
            f"gate failed: {sentence_count(text)} sentences, expected 2",
            file=sys.stderr,
        )
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(
        f"wrote {len(text)} characters "
        f"({sentence_count(text)} sentences) to {path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
