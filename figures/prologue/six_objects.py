"""图 1：数学研究的六类对象（序章第一节）。"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch

from common import C, save

NODES = [
    ("数", ["第 3 章", "第二部分"]),
    ("形", ["第五部分"]),
    ("结构", ["第三部分、第 29 章", "第十部分"]),
    ("变化", ["第四部分"]),
    ("不确定性", ["第七部分"]),
    ("计算", ["第 35 章", "第九部分"]),
]


def main() -> None:
    fig, ax = plt.subplots(figsize=(6.8, 5.8))
    ax.set_xlim(-3.55, 3.55)
    ax.set_ylim(-3.0, 3.0)
    ax.set_aspect("equal")
    ax.axis("off")

    r = 2.2
    ax.add_patch(Circle((0, 0), r, fill=False, ec=C["line"], lw=1.2, ls=(0, (4, 4))))

    angles = np.deg2rad(90 - 60 * np.arange(len(NODES)))
    for (name, parts), a in zip(NODES, angles):
        x, y = r * np.cos(a), r * np.sin(a)
        ax.plot([0, x], [0, y], color=C["line"], lw=1, zorder=1)
        w, h = 1.86, 0.9
        ax.add_patch(
            FancyBboxPatch(
                (x - w / 2, y - h / 2), w, h,
                boxstyle="round,pad=0,rounding_size=0.12",
                fc=C["paper"], ec=C["accent"], lw=1.6, zorder=2,
            )
        )
        n = len(parts)
        ax.text(x, y + 0.08 * n + 0.04, name, ha="center", va="center", fontsize=14, fontweight="bold", zorder=3)
        for i, p in enumerate(parts):
            ax.text(
                x, y + 0.08 * n - 0.26 - i * 0.2,
                p, ha="center", va="center", fontsize=9, color=C["muted"], zorder=3,
            )

    ax.add_patch(Circle((0, 0), 0.72, fc=C["accent_soft"], ec=C["accent"], lw=1.8, zorder=2))
    ax.text(0, 0.1, "逻辑与集合", ha="center", va="center", fontsize=12, fontweight="bold", zorder=3)
    ax.text(0, -0.2, "第一部分", ha="center", va="center", fontsize=9, color=C["muted"], zorder=3)

    save(fig, "prologue/six-objects")
