"""Entry for make.fun "Rejected Olympic Sports" (u-motasimfuad-rejected-olympic-sports-9d83e7da).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
"""
import os

LINE = 'Competitive apologizing: athletes say sorry for bumping into each other until one of them means it.'

def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
