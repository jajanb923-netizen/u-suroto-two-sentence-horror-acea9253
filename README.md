# Two-Sentence Horror — the recorder plays back two voices, both mine

[![make.fun bounty](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/jajanb923-netizen/u-suroto-two-sentence-horror-acea9253/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/jajanb923-netizen/u-suroto-two-sentence-horror-acea9253/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)

Entry for the [Two-Sentence Horror bounty on make.fun](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253): the scariest horror story in exactly two sentences, up to 400 characters.

## The story

> The sleep clinic gave me a recorder for the nights I kept waking up screaming with no memory of a dream. On the playback, I am the one screaming, but I am also the one in the corner of the room, whispering the words that make me scream.

The second sentence turns the first: the narrator went to the clinic
believing he was the victim of a nightmare he could not remember — the
playback shows he is also the thing in the corner whispering the words
that make him scream. Nothing is explained; the reader is left to fill
in what the whisperer is, and whether the narrator ever wakes up. 236
characters, well inside the 400-character gate.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the
story to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local
runs) after a self-check enforcing the gate: UTF-8 text, 1–400 characters,
not only whitespace.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Candidates

Ten candidate stories were scored against the judging criteria (genuine
fright, second-sentence turn, implied horror, precise prose, originality)
in [CANDIDATES.md](CANDIDATES.md); the story above scored highest (17/20).
