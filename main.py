#!/usr/bin/env python3
"""Loading Screen Gold: a tip in 200 characters.

Writes one loading-screen tip to /output/entry.txt.
"""

import os

ENTRY = "Tip: while this loads, your AI pair programmer has already rewritten this function twice and is now silently judging your variable names."

# The gate requires 1-200 UTF-8 characters, single line, not only whitespace.
assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
