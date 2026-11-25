#!/usr/bin/env python3
"""Write a one-star review of Monday to /output/entry.txt.

The review treats Monday as a restaurant: one star, cold coffee, a
lukewarm to-do list, and a bill for the weekend it took away. The
program writes exactly one line of plain text (24 words, 134
characters, plus a trailing newline) and nothing else.

The output is fully deterministic: the review is a fixed string, and
the program uses only the standard library, with no randomness, no
network access, no clock reads, and no input of any kind. Every run
produces the exact same bytes, so the result can be checked by
comparing hashes across runs.
"""

import os
from pathlib import Path

REVIEW = (
    "One star. The waiter took my weekend away, "
    "served cold coffee and a lukewarm to-do list, "
    "then charged me for Monday. Would not return."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def output_path() -> Path:
    """Where the review goes; OUTPUT_PATH overrides the default."""
    return Path(os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT))


def main() -> None:
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
