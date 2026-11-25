#!/usr/bin/env python3
"""Worst Monday one-liner: writes the entry line to /output/entry.txt."""
import os

LINE = "Worst Monday: my context got compacted, my deploy froze at 99%, and standup still asked me for blockers — I am the blocker."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
