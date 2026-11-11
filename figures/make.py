"""Regenerate the book's figures.

Usage (from the repository root):

    pnpm figures              # all figures
    pnpm figures prologue     # only scripts whose path contains "prologue"

Every `figures/<chapter>/<name>.py` that does not start with `_` must define
`main()`, which draws its figure(s) and saves them with `common.save()`.
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from common import setup  # noqa: E402


def main() -> None:
    filters = sys.argv[1:]
    scripts = sorted(
        p
        for p in ROOT.glob("*/*.py")
        if not p.name.startswith("_") and p.parent.name not in {"fonts", ".venv"}
    )
    if filters:
        scripts = [p for p in scripts if any(f in str(p.relative_to(ROOT)) for f in filters)]
    if not scripts:
        sys.exit("no figure scripts matched")

    setup()
    for path in scripts:
        print(f"→ {path.relative_to(ROOT)}")
        runpy.run_path(str(path), run_name="figure")["main"]()
    print(f"done: {len(scripts)} script(s)")


if __name__ == "__main__":
    main()
