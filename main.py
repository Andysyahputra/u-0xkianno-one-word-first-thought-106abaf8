"""One Word, First Thought.

Writes exactly one word to /output/entry.txt: the first word that
came to mind.
"""

import os

WORD = "Marmalade"


def _is_valid(word: str) -> bool:
    """Mirror the competition gate: one word, 1-24 chars, not only whitespace."""
    return 1 <= len(word) <= 24 and word.strip() != "" and " " not in word.strip()


def main() -> None:
    if not _is_valid(WORD):
        raise ValueError(f"word fails the gate: {WORD!r}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
