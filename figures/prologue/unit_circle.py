"""图 3：同一个单位圆的三种看法（序章第三节）。"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, FancyArrowPatch, Polygon

from common import C, save


def _panel(ax, title: str, captions: list[str]) -> None:
    ax.set_xlim(-1.55, 1.55)
    ax.set_ylim(-2.2, 1.55)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=13, fontweight="bold", pad=4)
    for i, text in enumerate(captions):
        ax.text(0, -1.62 - i * 0.3, text, ha="center", va="center", fontsize=9.5, color=C["muted"])


def _algebra(ax) -> None:
    _panel(ax, "代数", [r"$z^6=1$ 的六个根", "构成正六边形，也构成一个群"])
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(t), np.sin(t), color=C["accent"], lw=2)
    roots = np.exp(2j * np.pi * np.arange(6) / 6)
    ax.add_patch(
        Polygon(np.c_[roots.real, roots.imag], closed=True, fc=C["accent_soft"], ec=C["line"], lw=1)
    )
    ax.plot(roots.real, roots.imag, "o", ms=6, color=C["accent_strong"], zorder=3)
    ax.text(1.12, 0, "$1$", va="center", fontsize=12)
    ax.text(np.cos(np.pi / 3) + 0.08, np.sin(np.pi / 3) + 0.1, r"$\omega$", fontsize=12)


def _analysis(ax) -> None:
    _panel(ax, "分析", [r"$e^{i\theta}=\cos\theta+i\sin\theta$", "圆上的函数可展开成傅里叶级数"])
    ax.annotate("", (1.4, 0), (-1.4, 0), arrowprops=dict(arrowstyle="-|>", color=C["line"], lw=1))
    ax.annotate("", (0, 1.4), (0, -1.4), arrowprops=dict(arrowstyle="-|>", color=C["line"], lw=1))
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(t), np.sin(t), color=C["accent"], lw=2)
    th = np.deg2rad(50)
    px, py = np.cos(th), np.sin(th)
    ax.plot([0, px], [0, py], color=C["ink"], lw=1.4)
    ax.plot([px, px], [0, py], color=C["muted"], lw=1, ls=(0, (3, 3)))
    ax.plot([0, px], [py, py], color=C["muted"], lw=1, ls=(0, (3, 3)))
    ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=0, theta2=50, color=C["ink"], lw=1))
    ax.text(0.3, 0.1, r"$\theta$", fontsize=12)
    ax.plot(px, py, "o", ms=6, color=C["accent_strong"], zorder=3)
    ax.text(px + 0.08, py + 0.1, r"$e^{i\theta}$", fontsize=12)
    ax.text(px / 2, -0.2, r"$\cos\theta$", ha="center", fontsize=10, color=C["muted"])
    ax.text(-0.08, py / 2, r"$\sin\theta$", ha="right", va="center", fontsize=10, color=C["muted"])


def _topology(ax) -> None:
    _panel(ax, "几何/拓扑", [r"拉伸、弯曲后仍是同一个 $S^1$", r"绕圈数是整数：$\pi_1(S^1)\cong\mathbb{Z}$"])
    t = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(t), np.sin(t), color=C["line"], lw=1, ls=(0, (3, 3)))
    rr = 1 + 0.22 * np.sin(2 * t + 0.6) + 0.12 * np.cos(3 * t)
    x, y = rr * np.cos(t) * 1.05, rr * np.sin(t) * 0.92
    ax.plot(x, y, color=C["accent"], lw=2)
    i = 60
    ax.add_patch(
        FancyArrowPatch(
            (x[i], y[i]), (x[i + 6], y[i + 6]),
            arrowstyle="-|>", mutation_scale=14, color=C["accent_strong"], lw=0,
        )
    )
    ax.text(0, 0, "$S^1$", ha="center", va="center", fontsize=14)


def main() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(7.4, 3.0))
    fig.subplots_adjust(wspace=0.12)
    _algebra(axes[0])
    _analysis(axes[1])
    _topology(axes[2])
    save(fig, "prologue/unit-circle")
