"""One-line office joke entry.

Writes a single short joke about office life to /output/entry.txt
(exactly one line, no trailing newline). Stdlib only.
"""

import os

JOKE = "My out-of-office says I'm on holiday. My calendar says I'm in three meetings. Both are true."


def main():
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(JOKE))
    if "\n" in JOKE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
