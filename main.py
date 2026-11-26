#!/usr/bin/env python3
"""Real-life patch note: the brain's 3am replay bug.

Writes one patch-note line (at most 160 characters) to /output/entry.txt.
No dependencies, no network, deterministic.
"""
import os

LINE = "v3.1.0: fixed a bug where the brain replayed embarrassing moments from 2009 at 3am instead of sleeping."

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
