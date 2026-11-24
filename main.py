#!/usr/bin/env python3
"""Write the funniest toaster error message to entry.txt (make.fun entry)."""

import os

LINE = "Error 402: bread is a rumor. I refuse to participate further."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    validate(path)


def validate(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert text == text.strip(), "entry must have no leading/trailing whitespace"
    print(text)
    print(f"characters: {len(text)}")
    print(f"bytes: {len(text.encode('utf-8'))}")


if __name__ == "__main__":
    main()
