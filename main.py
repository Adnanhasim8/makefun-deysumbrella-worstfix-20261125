#!/usr/bin/env python3
"""Write one commit message to /output/entry.txt.

A bug fix that made everything worse, as a single line of at most
100 characters. Python 3.13 standard library only; no network.
"""

from pathlib import Path

ENTRY = "fix: seal the login hole, now only the hacker can log in"


def main() -> None:
    # Gate assertions: exactly one line, 1-100 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert not ENTRY.isspace(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 100, "entry must be 1-100 characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    # Verify what was written matches the gate too.
    written = out.read_text(encoding="utf-8")
    assert written == ENTRY
    assert 1 <= len(written) <= 100 and "\n" not in written


if __name__ == "__main__":
    main()
