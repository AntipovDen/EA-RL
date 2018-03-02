from numpy import prod
from matplotlib import pyplot as plt

n = 1000
k = 2

def runtime(lam):
    return (2 * lam / (lam + 2)) ** k * sum(prod([((i - 1) * k + n / lam + j) / ((i - 1) * k + j) for j in range(1, k + 1)])   for i in range(1, n // k + 1))

color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
lams = range(1, n + 1)
for k in range(2, 10):
    plt.plot(lams, [1 / runtime(x) for x in lams], '{}o-'.format('b'), label='$k = {}$'.format(k))
    plt.show()