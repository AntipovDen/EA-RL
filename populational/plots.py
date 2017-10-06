from matplotlib import pyplot as plt
from scipy.misc import factorial, comb

n = 100
k = 10

def z_x(x):
    return sum([comb(n, x - i) / comb(n - 1, x) for i in range(x % k + 1)])

def z_r(x):
    return sum([comb(n, x - i) / comb(n - 1, x) / (2 ** i) for i in range(x % k + 1)])

for k in range(2, 15):
    plt.semilogy(range(n), [z_x(x) for x in range(n)], 'bo-')
    plt.semilogy(range(n), [z_r(x) for x in range(n)], 'ro-')
    plt.show()