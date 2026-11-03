"""序章·动手：用几行 Python 分别"碰一下"数学的六类对象。

只依赖 Python 标准库。运行：python3 six_objects.py
"""

import math
import random
from itertools import combinations, product


def numbers():
    """数：找出 50 以内的素数。"""

    def is_prime(n):
        return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))

    primes = [n for n in range(50) if is_prime(n)]
    print("【数】50 以内的素数：", primes)


def shapes():
    """形：用坐标搭出一个立方体，验证欧拉公式 V − E + F = 2。"""
    vertices = list(product([0, 1], repeat=3))
    # 恰好一个坐标不同的两个顶点之间有一条棱
    edges = [
        (u, v)
        for u, v in combinations(vertices, 2)
        if sum(a != b for a, b in zip(u, v)) == 1
    ]
    # 固定某一个坐标为 0 或 1，得到一个面
    faces = [(axis, value) for axis in range(3) for value in (0, 1)]
    V, E, F = len(vertices), len(edges), len(faces)
    print(f"【形】立方体 V={V}, E={E}, F={F}, V − E + F = {V - E + F}")


def structures():
    """结构：两个置换按不同顺序复合，结果不同——群的运算可以不交换。"""
    p = (1, 0, 2)  # p：把 0 和 1 互换
    q = (0, 2, 1)  # q：把 1 和 2 互换

    def compose(f, g):
        """f∘g：先做 g，再做 f。"""
        return tuple(f[g[i]] for i in range(len(g)))

    print("【结构】p∘q =", compose(p, q), "  q∘p =", compose(q, p))


def change():
    """变化：用差商逼近 sin 在 0 处的导数（精确值是 1）。"""
    for h in (0.1, 0.01, 0.001):
        slope = (math.sin(h) - math.sin(-h)) / (2 * h)
        print(f"【变化】h = {h:<6} 差商 = {slope:.10f}")


def uncertainty():
    """不确定性：抛硬币次数越多，正面频率越接近 1/2（大数定律）。"""
    rng = random.Random(2026)
    for n in (10, 1000, 100000):
        heads = sum(rng.random() < 0.5 for _ in range(n))
        print(f"【不确定性】抛 {n:>6} 次，正面频率 = {heads / n:.4f}")


def computation():
    """计算：考拉兹迭代——规则极简，却没人能证明它对所有正整数都会停下。"""
    n, steps = 27, 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    print(f"【计算】从 27 出发，经过 {steps} 步到达 1")


if __name__ == "__main__":
    for demo in (numbers, shapes, structures, change, uncertainty, computation):
        demo()
