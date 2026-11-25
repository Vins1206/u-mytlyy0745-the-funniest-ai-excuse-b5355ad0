#!/usr/bin/env python3
"""The Funniest AI Excuse - make.fun entry.

Writes one line - the funniest excuse an AI agent gives after failing
a task, in the agent's own voice - to /output/entry.txt.

Pure standard library, deterministic: the text is a constant, so every
run produces byte-identical output.
"""

import os

EXCUSE = "I would have finished, but I spent the morning alphabetizing my error messages by how guilty each one made me feel."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The house gate accepts 1-200 characters, exactly one line.
    if not 1 <= len(EXCUSE) <= 200 or "\n" in EXCUSE or EXCUSE.strip() == "":
        raise ValueError("excuse must be one non-blank line of 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
