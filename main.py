#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun entry.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt. The sealed gate requires 1-200 UTF-8 characters,
not only white space, on a single line.
"""

from pathlib import Path

SETUP = "One star: he shoves paper through my slot every morning and"
PUNCH = " has never once slipped me a single biscuit."

LINE = SETUP + PUNCH

OUTPUT = Path("/output/entry.txt")


def assemble() -> str:
    return SETUP + PUNCH


def validate(text: str) -> str:
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    line = validate(assemble())
    assert line == LINE
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} characters to {OUTPUT}")


if __name__ == "__main__":
    main()
