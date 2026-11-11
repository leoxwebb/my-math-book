"""图 4：三大主干与它们的交汇处（序章第三节）。"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

from common import C, save

R = 1.45
CIRCLES = [
    ((-0.8, 0.5), "blue"),
    ((0.8, 0.5), "orange"),
    ((0.0, -0.8), "green"),
]
TRUNKS = [((-1.45, 1.0), "代数"), ((1.45, 1.0), "分析"), ((0, -1.75), "几何/拓扑")]
# Label positions are the centroids of each intersection region (computed numerically).
REGIONS = [
    ((0, 1.03), ["泛函分析", "调和分析"]),
    ((-0.83, -0.4), ["代数几何", "代数拓扑"]),
    ((0.83, -0.4), ["微分几何", "几何分析"]),
    ((0, 0.08), ["李群", "朗兰兹纲领"]),
]


def main() -> None:
    fig, ax = plt.subplots(figsize=(5.0, 4.8))
    ax.set_xlim(-2.3, 2.3)
    ax.set_ylim(-2.3, 2.0)
    ax.set_aspect("equal")
    ax.axis("off")

    for center, color in CIRCLES:
        ax.add_patch(Circle(center, R, fc=C[color], alpha=0.14, ec="none"))
        ax.add_patch(Circle(center, R, fill=False, ec=C[color], lw=1.8))
    for (x, y), name in TRUNKS:
        ax.text(x, y, name, ha="center", va="center", fontsize=15, fontweight="bold")
    for (x, y), lines in REGIONS:
        for i, line in enumerate(lines):
            ax.text(x, y + 0.11 - i * 0.22, line, ha="center", va="center", fontsize=9.5)

    save(fig, "prologue/three-trunks")
