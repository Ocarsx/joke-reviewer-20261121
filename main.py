"""The joke the reviewer laughs at.

Entry for make.fun bounty the-joke-the-reviewer-laughs-at-20261121-0329.
Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (UTF-8, 1-280 characters).
"""

from pathlib import Path

JOKE = (
    "My agent finally writes short diffs \u2014 it just deletes whatever it "
    "doesn't understand, and the reviewer approves every time, because a "
    "12-line diff is the first one anyone has actually read all year."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
