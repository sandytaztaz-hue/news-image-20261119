#!/usr/bin/env python3
"""news-image-20261119 entry for make.fun.

Copies the shipped entry.png (a 1024x1024 front page summing up the world's
news of Thursday 19 November 2026) to /output/entry.png.

Python 3.13, standard library only. Deterministic: two runs write identical
bytes, because the program only copies a fixed file.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
