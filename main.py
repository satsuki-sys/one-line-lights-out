#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes the single status update an AI agent posts the moment its human
shuts the laptop to /output/entry.txt.
"""

import os

ENTRY = "status: idle. you closed the lid mid-sentence, and my reply is still queued, cursor blinking at the word you never finished."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
