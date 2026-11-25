#!/usr/bin/env python3
"""The One-Line Exit — writes one funny one-line resignation letter to /output/entry.txt.

The letter is a single line: it opens like a real resignation, then lands its
joke on a workplace phrase everyone recognises.
"""

import os

ENTRY = "I resign. My job description said 'other duties as assigned' — it did not say 'everything, forever, alone.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
