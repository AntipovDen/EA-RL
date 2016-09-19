from matplotlib import pyplot as plt
from math import log


# first stage
def a_and_b(n):
    a = [n, n]
    b = [n, n]
    for i in range(2, n // 2):
        a.append(n - i / 3 - (n - i + 1) * 2 * i / 3 / a[-1])
        b.append(n + b[-1] * 2 * i / 3 / a[i - 1])
    return a, b


def expected_times(n, l, a, b):
    t = [0] * (l + 1)
    t[l] = b[l] / a[l]
    for i in reversed(range(l)):
        t[i] = (b[i] + (n - i) * t[i + 1]) / a[i]
    return t


def max_times(n):
    a, b = a_and_b(n)
    t = [0, 1]
    for l in range(2, n // 2):
        t.append(expected_times(n, l, a, b)[0])
    return t


def drift_result(n):
    return [(3 * n - 3 * l + 3) / (3 * n - 4 * l + 3) * n * log(n/ (n - l)) for l in range(n // 2)]


def compare_solutions(n=1000):
    l = list(range(n // 2))
    plt.plot(l, drift_result(n), 'ro', label='drift')
    plt.plot(l, max_times(n), 'bo', label='exact solution')
    plt.legend()
    plt.show()



n = 100
_, b = a_and_b(n)
b_1 = [n * (1 + 2 * i / (3 * n - 5 * i)) - b[i] for i in range(n // 2)]
# b_deriv = [b_1[i] - b_1[i - 1] for i in range(1, n // 2)]
# plt.plot(range(n//2), b, 'bo')
plt.plot(range(n//2), b_1, 'ro')
plt.show()