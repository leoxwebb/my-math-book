"""图 1：实质蕴含排除的唯一一种赋值。"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from common import C, save


def main() -> None:
    fig, ax = plt.subplots(figsize=(6.2, 4.1))
    ax.set_xlim(-0.65, 4.15)
    ax.set_ylim(-0.55, 3.65)
    ax.set_aspect("equal")
    ax.axis("off")

    for row, p in enumerate((True, False)):
        for col, q in enumerate((True, False)):
            x, y = 0.55 + col * 1.65, 1.65 - row * 1.5
            fails = p and not q
            ax.add_patch(
                Rectangle(
                    (x, y), 1.5, 1.3,
                    facecolor=C["paper"] if fails else C["accent_soft"],
                    edgecolor=C["red"] if fails else C["line"],
                    linewidth=2.2 if fails else 1,
                )
            )
            if fails:
                ax.plot(
                    [x + 0.12, x + 1.38], [y + 0.12, y + 1.18],
                    color=C["red"], linewidth=1.5,
                )
            ax.text(
                x + 0.75, y + 0.78,
                "不满足" if fails else "满足",
                ha="center", va="center", fontsize=13,
                color=C["red"] if fails else C["accent_strong"],
                bbox=dict(facecolor=C["paper"] if fails else C["accent_soft"], edgecolor="none", pad=2),
            )
            ax.text(
                x + 0.75, y + 0.34,
                "唯一反例" if fails else ("前件为假" if not p else "规则兑现"),
                ha="center", va="center", fontsize=9, color=C["muted"],
            )

    for col, label in enumerate(("Q 真：门开", "Q 假：门未开")):
        ax.text(1.3 + col * 1.65, 3.22, label, ha="center", va="center", fontsize=11)
    for row, label in enumerate(("P 真\n刷卡成功", "P 假\n刷卡未成功")):
        ax.text(0.35, 2.3 - row * 1.5, label, ha="right", va="center", fontsize=10)
    ax.text(
        2.1, -0.3, r"$P\Rightarrow Q$：不允许“刷卡成功，门却未开”",
        ha="center", va="center", fontsize=10, color=C["muted"],
    )
    save(fig, "classical-logic/implication-grid")
