#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line (max 200 chars) describing a hilariously
useless superpower to /output/entry.txt.

Candidate lines drafted and scored (funny / fresh / tight wording /
payoff in the last words):
  1. Wi-Fi hearing        - funny, but echoes the kit's password example.
  2. Teleport anywhere   - decent twist, familiar teleport angle.
  3. Talk to fish        - good punchline, two sentences, common angle.
  4. Invisible unseen   - strong twist, vivid, runner-up.
  5. See 5s into future - CHOSEN: most specific and vivid (watching
     yourself drop your phone), payoff lands on the final words.
  6. Fly slowly          - funny, least fresh angle.

Revision rounds on the winner:
  R1: em-dash cut + "powerless to stop it" - lost the punch of "do nothing".
  R2: restored the comma flow, added "absolutely" before "nothing" -
     the helplessness IS the joke. Final: 134 characters.
"""

import os

LINE = (
    "I can see five seconds into the future, which is exactly long "
    "enough to watch myself drop my phone and do absolutely nothing "
    "about it."
)


def main() -> None:
    # Gate guard (RULES.txt): entry.txt must be UTF-8 text of 1 to 200
    # characters, a single line, not only white space. Normalise first so
    # a stray space from a later edit can never ship an invalid entry.
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
