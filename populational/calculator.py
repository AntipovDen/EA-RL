from numpy import prod
from matplotlib import pyplot as plt
from scipy.misc import comb
from math import log

n = 100
k = 2

def runtime(lam):
    return (2 * lam / (lam + 2)) ** k * sum(prod([((i - 1) * k + n / lam + j) / ((i - 1) * k + j) for j in range(1, k + 1)])   for i in range(1, n // k + 1))


def improve_in_the_plateau_beginning(p, lam):
    if p == 1:
        return 1 - 2 / ((2 * lam + 1) * (2 * lam + 2))
    s = 0.0
    a = (1 - p) ** (2 * lam)
    for i in range(1, 2 * lam + 1):
        a *= (2 * lam - i + 1) / i * p / (1 - p)
        s += a * (1 - 2 / ((i + 1) * (i + 2)))
    return s

def improve_in_the_plateau_beginning_depr(p, lam):
    res = 0
    for i in range(2 * lam + 1):
        res += p ** i * (1 - p) ** (2 * lam - i) * comb(2 * lam, i) * (1 - 2 / ((i + 1) * (i + 2)))
    return res




probs = [j / n for j in range(1, n + 1)]
for lam in 1, 10, 100:
    plt.plot(probs, [improve_in_the_plateau_beginning(p, lam) for p in probs], 'bo-')
    plt.plot(probs, [p * lam / (1 + p * lam) for p in probs], 'ro-')
    plt.show()


