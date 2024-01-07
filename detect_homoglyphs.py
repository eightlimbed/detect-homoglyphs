"""
Reads a file and detects homoglyphs that might be confusing to
people who communicate using the English language.
"""
import sys


if len(sys.argv) != 2:
    print(f"Usage: python detect_homoglyphs PATH")
    sys.exit(1)

PATH = sys.argv[1]

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

for word in content.split():
    for char in word:
        if ord(char) > 128:
            print(f'Found non-ASCII character: "{char}". Unicode point {ord(char)} found in {word}')
            sys.exit(1)
