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
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be blank"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
