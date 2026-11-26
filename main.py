#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun entry.

Writes exactly one museum label (1-200 characters) for an ordinary
object from today, as a museum in the year 3000 would display it,
to entry.txt in the output directory.

The label's object is the CAPTCHA checkbox: the year-3000 curator
takes it at face value as a daily humanity test, and the punchline
is that the robots passed it too. The line is a fixed, hand-written
string: deterministic by construction, no randomness, no network,
no input read.
"""

import os

LINE = (
    "CAPTCHA checkbox, c. 2025. Citizens proved they were human "
    "by ticking this box. The robots ticked it too."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
