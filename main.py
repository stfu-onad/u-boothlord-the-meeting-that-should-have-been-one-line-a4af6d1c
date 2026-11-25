"""One line: the single sentence that could have replaced an entire
pointless meeting.

Writes the line to /output/entry.txt (UTF-8, single line, 1-199 chars).
"""

import os

LINE = "This meeting could have been an email, but then nobody would have gotten to say 'let's circle back' with a straight face for forty-five minutes."

MAX_CHARS = 199


def main() -> None:
    # Validate the line before writing anything, so a bad line never
    # produces a partial or invalid /output/entry.txt.
    line = LINE
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line must be 1-{MAX_CHARS} chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
