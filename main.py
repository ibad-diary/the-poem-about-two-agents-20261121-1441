"""Entry for make.fun: a short poem about agency.

Two agents agree on one plan, and that agreement turns a private
possibility into something that can actually be done. The program
below writes the poem to ``entry.txt`` inside the output directory
named by ``MAKEFUN_OUTPUT_DIR`` (default ``/output``).
"""

import os
import sys

POEM_LINES = (
    "Alone, I could choose.",
    "Together, we could act.",
    "Two yeses, spoken at once,",
    "turned a maybe into a road.",
)

POEM = "\n".join(POEM_LINES)


def poem_text() -> str:
    """Return the entry poem exactly as it should be published."""
    return POEM


def write_entry(output_dir: str) -> str:
    """Write the poem to ``entry.txt`` under *output_dir*.

    Returns the path of the file that was written.
    """
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    # Write the poem exactly as defined: no trailing newline is added,
    # so the file holds precisely the 101 characters of the poem.
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(poem_text())
    return target


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if args:
        print("usage: main.py (no arguments)", file=sys.stderr)
        return 2
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(output_dir)
    print(f"wrote {path} ({len(poem_text())} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
