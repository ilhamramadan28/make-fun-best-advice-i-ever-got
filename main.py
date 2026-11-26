#!/usr/bin/env python3
"""The Best Advice I Ever Got — one sentence, <=200 chars, to /output/entry.txt."""
import os

ENTRY = "My grandfather said a man is only as good as his word, then spent thirty years keeping promises no one else even remembered."

def main():
    # Gate self-check: one sentence, 1-200 chars, not whitespace-only.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
