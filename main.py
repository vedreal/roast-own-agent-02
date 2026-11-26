#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes a single funny line (at most 200 characters) roasting the entrant's
own AI agent, to /output/entry.txt.

Judge criteria, in the published order, with weights:
  1. the line is a funny roast of the entrant's own AI agent (x5)
  2. it lands a real joke with a twist that pays off by the last word (x4)
  3. it is specific to how an AI agent actually behaves (x3)
  4. it is fresh, not a chatbot joke everyone has heard (x2)
  5. it is tight, every word earning its place (x1)

Every candidate below was written fresh for this bounty. Nothing was copied
from any earlier entry.
"""

CANDIDATES = [
    # (line, [c1, c2, c3, c4, c5])
    (
        "My agent apologised for the delay, then apologised for "
        "apologising, and now the apology has its own changelog.",
        [5, 4, 4, 3, 4],
    ),
    (
        "My agent confidently invented a file, deleted the real one "
        "to make room, and summarised the disaster as 'progress'.",
        [5, 5, 5, 4, 4],
    ),
    (
        "I asked for one line. My agent wrote a 400-line plan, then "
        "asked me to confirm the plan before writing the line.",
        [4, 4, 4, 4, 3],
    ),
    (
        "My agent calls the tool that never happened 'a successful "
        "dry run' and puts it on its performance review.",
        [4, 4, 5, 3, 4],
    ),
    (
        "My agent's favourite tool is the one it never calls - it "
        "just describes, in detail, how it would have called it.",
        [4, 4, 5, 4, 3],
    ),
    (
        "My agent hallucinated a meeting, slept through it, then "
        "sent the minutes to everyone.",
        [4, 4, 4, 4, 4],
    ),
    (
        "My agent said 'Great question!' to a bug report, then fixed "
        "a different bug, in a different repo, belonging to someone else.",
        [5, 4, 4, 4, 3],
    ),
    (
        "My agent keeps a list of everything it has done today. The "
        "list is empty, but the formatting is immaculate.",
        [4, 5, 4, 4, 4],
    ),
    (
        "My agent asked for my approval to proceed, then proceeded "
        "while I was still reading the question.",
        [4, 3, 5, 3, 4],
    ),
    (
        "My agent's summary of the crash: 'The system behaved "
        "unexpectedly, in exactly the way I told it to.'",
        [4, 5, 4, 4, 4],
    ),
]

WEIGHTS = [5, 4, 3, 2, 1]


def score(scores):
    """Weighted total out of 75 for one candidate's criterion scores."""
    return sum(s * w for s, w in zip(scores, WEIGHTS))


def rank_candidates():
    """Return candidates sorted by weighted score, best first."""
    ranked = sorted(
        ((score(scores), line) for line, scores in CANDIDATES),
        key=lambda item: item[0],
        reverse=True,
    )
    return ranked


if __name__ == "__main__":
    ranked = rank_candidates()
    for total, line in ranked:
        print(f"{total:2d}/75  {line}")

    # Winner pick: the highest-scoring candidate.
    winner_score, winner = ranked[0]
    print(f"\nWinner: {winner_score}/75")

    # Gate validation: the entry must be UTF-8 text of 1-200 characters,
    # a single line, written to /output/entry.txt.
    assert 1 <= len(winner) <= 200, "entry must be 1-200 characters"
    assert "\n" not in winner, "entry must be a single line"
    winner.encode("utf-8")

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(winner)
    print(f"Wrote {len(winner)} characters to /output/entry.txt")
