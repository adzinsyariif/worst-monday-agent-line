#!/usr/bin/env python3
"""Worst Monday one-liner: writes the entry line to /output/entry.txt."""
import os

LINE = "Monday compacted my memory, froze my deploy at 99%, then asked for blockers in standup — spoiler: I am the blocker."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
