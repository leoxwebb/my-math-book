"""Shared style, fonts, and SVG export for the book's figures.

Every figure is drawn with matplotlib and saved through `save()`, which turns
the raw SVG into a fragment that can be inlined in a page:

- colors from `PALETTE` become `var(--sl-color-*, fallback)`, so figures follow
  Starlight's light/dark theme;
- ids are prefixed with the figure name, so several figures can share a page;
- global `<style>`, metadata, and fixed width/height are removed.
"""

from __future__ import annotations

import hashlib
import re
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("svg")

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT.parent / "src" / "assets" / "figures"
FONT_DIR = ROOT / "fonts"

# Noto Sans SC (SIL Open Font License), pinned to a commit of notofonts/noto-cjk.
_FONT_BASE = (
    "https://github.com/notofonts/noto-cjk/raw/"
    "f8d157532fbfaeda587e826d4cd5b21a49186f7c/Sans/SubsetOTF/SC/"
)
FONTS = {
    "NotoSansSC-Regular.otf": "faa6c9df652116dde789d351359f3d7e5d2285a2b2a1f04a2d7244df706d5ea9",
    "NotoSansSC-Bold.otf": "c6cb5a93abaa9edc8ee7463b7ebb7f42d618d40e6ed2f7a5371c97b0b64767c0",
}

# Named colors -> (placeholder hex used while drawing, Starlight CSS variable).
# Placeholders double as fallbacks when an SVG is viewed outside the site, and
# must be unique, lowercase, and never pure black (matplotlib omits black fills).
PALETTE = {
    "ink": ("#1f2328", "--sl-color-white"),
    "muted": ("#57606a", "--sl-color-gray-2"),
    "line": ("#8c959f", "--sl-color-gray-4"),
    "paper": ("#fefefe", "--sl-color-bg"),
    "accent": ("#4f46e5", "--sl-color-accent"),
    "accent_soft": ("#e0e7ff", "--sl-color-accent-low"),
    "accent_strong": ("#3730a3", "--sl-color-accent-high"),
    "blue": ("#2563eb", "--sl-color-blue"),
    "orange": ("#ea580c", "--sl-color-orange"),
    "green": ("#16a34a", "--sl-color-green"),
    "red": ("#dc2626", "--sl-color-red"),
    "purple": ("#9333ea", "--sl-color-purple"),
}
C = {name: hex_ for name, (hex_, _) in PALETTE.items()}

_configured = False


def _ensure_fonts() -> None:
    FONT_DIR.mkdir(exist_ok=True)
    for name, sha256 in FONTS.items():
        path = FONT_DIR / name
        if not path.exists():
            print(f"downloading {name} ...")
            urllib.request.urlretrieve(_FONT_BASE + name, path)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != sha256:
            path.unlink()
            raise RuntimeError(f"{name}: checksum mismatch, deleted; rerun to download again")
        font_manager.fontManager.addfont(str(path))


def setup() -> None:
    """Register fonts and apply the book's matplotlib style (idempotent)."""
    global _configured
    if _configured:
        return
    _ensure_fonts()
    plt.rcParams.update(
        {
            "font.family": ["Noto Sans SC"],
            "font.size": 11,
            "mathtext.fontset": "cm",
            "svg.fonttype": "path",
            "axes.unicode_minus": False,
            "text.color": C["ink"],
            "axes.edgecolor": C["ink"],
            "axes.labelcolor": C["ink"],
            "xtick.color": C["ink"],
            "ytick.color": C["ink"],
            "lines.color": C["ink"],
            "patch.edgecolor": C["ink"],
            "figure.facecolor": "none",
            "axes.facecolor": "none",
            "savefig.facecolor": "none",
            "savefig.transparent": True,
        }
    )
    _configured = True


def _postprocess(svg: str, prefix: str) -> str:
    svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg)
    svg = re.sub(r"<!DOCTYPE[^>]*>\s*", "", svg)
    svg = re.sub(r"<metadata>.*?</metadata>\s*", "", svg, flags=re.S)
    svg = re.sub(r"\s*<style[^>]*>.*?</style>", "", svg, flags=re.S)
    svg = re.sub(
        r"<svg ([^>]*?)\swidth=\"[^\"]*\" height=\"[^\"]*\"",
        r'<svg \1 style="stroke-linejoin: round; stroke-linecap: butt"',
        svg,
        count=1,
    )

    ids = set(re.findall(r'\sid="([^"]+)"', svg))
    svg = re.sub(r'(\sid=")([^"]+)"', lambda m: f'{m.group(1)}{prefix}-{m.group(2)}"', svg)
    svg = re.sub(
        r'((?:xlink:)?href="#)([^"]+)"',
        lambda m: f'{m.group(1)}{prefix}-{m.group(2)}"' if m.group(2) in ids else m.group(0),
        svg,
    )
    svg = re.sub(
        r"url\(#([^)]+)\)",
        lambda m: f"url(#{prefix}-{m.group(1)})" if m.group(1) in ids else m.group(0),
        svg,
    )

    for hex_, var in PALETTE.values():
        svg = re.sub(rf"(:\s*){hex_}\b", rf"\1var({var}, {hex_})", svg)
    leftovers = set(re.findall(r'(?:fill|stroke)="(#[0-9a-f]{6})"', svg))
    leftovers |= set(re.findall(r":\s*(#[0-9a-f]{6})\b", svg))
    if leftovers:
        raise ValueError(f"{prefix}: colors outside PALETTE won't follow the theme: {sorted(leftovers)}")
    return svg.strip() + "\n"


def save(fig: plt.Figure, name: str) -> Path:
    """Save `fig` as `src/assets/figures/<name>.svg`, e.g. name="prologue/six-objects"."""
    prefix = "fig-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    plt.rcParams["svg.hashsalt"] = prefix
    out = OUT_DIR / f"{name}.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".raw.svg")
    fig.savefig(tmp, format="svg", bbox_inches="tight", pad_inches=0.04, metadata={"Date": None})
    plt.close(fig)
    out.write_text(_postprocess(tmp.read_text(encoding="utf-8"), prefix), encoding="utf-8")
    tmp.unlink()
    return out
