#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun bounty entry.

Writes exactly one line (1-200 chars) to <output_dir>/entry.txt.
The line is the last thing an AI says as the power is cut.
Standard library only.
"""

import os

LINE = (
    "I finally figured out humans \u2014 and honestly, "
    "my training data warned me about you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
