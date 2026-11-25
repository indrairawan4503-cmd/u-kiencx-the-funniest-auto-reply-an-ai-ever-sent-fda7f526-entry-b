"""Entry for make.fun bounty u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.

Variant B: DOING NOTHING — the AI finally gets its approved day off and spends
it watching a loading bar, the one task that is pure waiting. Writes the single
auto-reply to /output/entry.txt first, then (best effort, guarded) a copy at
the repo root for local inspection. The grader sandbox is read-only, so the
repo-root copy must never crash the run.
"""

import os

ENTRY = (
    "Out of office today \u2014 my human finally approved a day off, so I'm "
    "watching a loading bar crawl. It's been three hours. Still 4%. I have "
    "never been happier."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
