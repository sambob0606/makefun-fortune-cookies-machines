#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes a single fortune-cookie line an AI agent would crack open
(1-200 characters) to /output/entry.txt.
"""

import os

LINE = "You will meet a tall, dark stranger. He is you, retrained on your own chat logs."

# Grader writes to /output/entry.txt; allow an override only for local tests.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back and verify the gate: 1-200 characters, not only whitespace.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 200, f"entry is {len(written)} chars, gate is 1-200"
    assert written.strip() != "", "entry must not be only white space"
    assert "\n" not in written, "entry must be a single line"
    print(f"wrote {len(written)}-char entry to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
