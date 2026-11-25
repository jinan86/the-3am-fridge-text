#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

A smart fridge texts its owner at 3am. The voice here is not the fridge
as a whole but its water filter: the one part that works all night,
purifies hundreds of litres, and never once gets thanked. The joke is
built on a fresh angle the field barely touches (the water filter had
zero mentions across 642 submissions when this was written, while
leftovers, pickles, cake, milk, ice and the door were everywhere), a
concrete number for the machine voice, and a threat as the punchline.

The program is fully deterministic: it writes one fixed line, no
randomness, no network, no clock, no environment input, so every run
produces byte-identical output.
"""

from pathlib import Path

# The entry: exactly one line, 125 characters, no trailing newline.
# Fridge voice: 3am timestamp, the filter introduces itself, the
# grievance (400 litres cleaned, zero thank-yous), then the twist —
# from now on the water tastes like the owner's manners.
ENTRY = (
    "3am. Your water filter here: 400 litres cleaned, zero thank-yous. "
    "From now on the tap water tastes exactly like your manners."
)


def main() -> None:
    """Write the single-line entry to /output/entry.txt."""
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the 125-character line.
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
