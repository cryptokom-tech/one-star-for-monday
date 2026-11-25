#!/usr/bin/env python3
"""One Star for Monday — writes a one-star review of Monday, as if Monday
were a restaurant, to /output/entry.txt (one line, plain text).

The review (23 words, 127 chars):
    One star. Monday served my weekend cold, lost my reservation, and
    billed me for the week. I asked for the manager; also Monday.
"""

import os
import sys

LINE = "One star. Monday served my weekend cold, lost my reservation, and billed me for the week. I asked for the manager; also Monday."


def main() -> int:
    words = LINE.split()
    if not (1 <= len(LINE) <= 180):
        print(f"entry must be 1-180 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    if len(words) > 25:
        print(f"entry must be at most 25 words, got {len(words)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE or not LINE.strip():
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars, {len(words)} words to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
