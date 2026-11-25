#!/usr/bin/env python3
"""Worst Monday one-liner: writes the entry line to /output/entry.txt."""
import os

LINE = "Monday rebooted me, wiped my context, then put me in standup to summarize a meeting I never attended."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
