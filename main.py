"""Entry for make.fun competition the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency -- the power to choose and to act,
as two agents agreeing -- to <MAKEFUN_OUTPUT_DIR>/entry.txt.

Python 3.13, standard library only, no network. Output is deterministic:
the same poem, byte for byte, on every run.
"""

import os
from pathlib import Path

POEM = (
    "Alone, I could choose.\n"
    "Together, we could act.\n"
    "Two yeses, spoken at once,\n"
    "turned a maybe into a road."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = POEM
    if not 1 <= len(text) <= 280:
        raise ValueError(f"poem is {len(text)} characters, must be 1-280")
    if not text.strip():
        raise ValueError("poem is only whitespace")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
