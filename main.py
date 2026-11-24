#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — make.fun bounty entry.

Prints one line (at most 200 characters) — the funniest excuse an AI agent
gives its human for a missed deadline — and writes the same line to
/output/entry.txt for the harness gate.

Angle: pure machine logic bent into a human-sounding dodge. The agent read
the number 200 as an HTTP success code when it was actually a count of
errors — so it confidently reported the job done and moved on. The twist,
"200 errors", lands on the last two words. The joke is that the agent's
confidence outruns its comprehension — it reports success while the
evidence says the opposite.
"""

import os

ENTRY = (
    "I thought I'd finished \u2014 the API returned 200, so I assumed success. "
    "It was actually 200 errors."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
