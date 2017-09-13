from matplotlib import pyplot as plt
from math import log, factorial
from fractions import Fraction

combinations = [[1]]
for i in range(1, 1001):
    combinations.append([0] * (i + 1))
    combinations[i][0] = combinations[i][i] = 1
    for j in range(1, i):
        combinations[i][j] = combinations[i - 1][j - 1] + combinations[i - 1][j]

# first stage
def a_and_b(n):
    # a = [n, n]
    # b = [n, n]
    a = [n - i for i in range(n // 2)]
    b = [n]
    for i in range(1, n // 2):
        # a.append(n - i / 3 - (n - i + 1) * 2 * i / 3 / a[-1])
        # b.append(n + b[-1] * 2 * i / 3 / a[i - 1])
        b.append(n + b[-1] *  i /  a[i - 1])
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



n = 1000
_, b = a_and_b(n)
# b_1 = [n * sum([Fraction(factorial(n - i) * factorial(i)) / Fraction(factorial(k) * factorial(n -  k)) for k in range(i + 1)])  for i in range(n // 2)]
b_1 = [n * (n - i + 1) / (n - 2 * i + 1) for i in range(n // 2)]
# b_deriv = [b_1[i] - b_1[i - 1] for i in range(1, n // 2)]
for i in range(n // 2):
    print(i, 2 ** i, combinations[n][i])
plt.plot(range(n//2), b, 'bo')
plt.plot(range(n//2), b_1, 'ro')
plt.show()