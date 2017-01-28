from matplotlib import pyplot as plt
from matplotlib import rc


# [number of перезапуски, exp, percents, iters_restart, exp, iters_ok, exp, total, exp]
map = {10: {4: 0, 2: 1, 1: 2},
       20: {9: 3, 5: 4, 1: 5},
       100: {49: 6, 25: 7, 1: 8},
       1000: {499: 9, 250: 10, 1: 11},
       10000: {4999: 12, 2500: 13, 1: 14}}

data = [[1.63,    2.05,    79.42, 178.59,       258.32,     33.05,      100.24,     324.69,         629.80   ], #n = 10 l = 4
        [2.81,    3.49,    67.11, 185.39,       293.02,     34.83,      129.83,     555.03,         1152.47   ], #n = 10 l = 2
        [4.01,    5.36,    58.57, 193.34,       313.89,     35.57,      146.64,     810.29,         1829.09   ], #n = 10 l = 1
        [1.80,    2.05,    79.74, 419.11,       585.66,     79.54,      220.13,     832.68,         1420.73   ], # n = 20 l = 9
        [2.83,    3.49,    67.91, 433.08,       655.07,     83.65,      279.32,     1307.54,        2565.51   ], # n = 20 l = 5
        [9.23,    11.05,   55.21, 482.12,       757.10,     102.58,     359.38,     4553.00,        8725.33   ], # n = 20 l = 1
        [1.58,    2.05,    80.10, 2848.88,      3874.31,    556.69,     1443.01,    5052.22,        9385.35   ], # n = 100 l = 49
        [3.45,    4.06,    65.36, 2955.17,      4299.21,    612.19,     1802.51,    10816.38,       19257.30   ], # n = 100 l = 25
        [49.20,   56.80,   50.94, 3614.28,      5337.39,    943.67,     2584.20,    178748.02,      305747.95   ], # n = 100 l = 1
        [1.77,    2.05,    80.32, 39504.30,     53193.53,   7770.18,    20051.52,   77613.77,       129098.26   ], #n = 1000 l = 499
        [3.62,    4.21,    63.72, 40761.64,     57626.22,   8519.73,    23795.06,   156280.67,      266401.45   ], #n = 1000 l = 250
        [510.02,  571.77,  50.01, 54060.66,     75974.36,   16253.47,   37310.90,   27588219.22,    43477170.72   ], #n = 1000 l = 1
        [1.72,    2.05,    81.69, 506216.58,    677978.41,  101739.72,  257944.83,  969901.15,      1647800.57   ], # n = 10000 l = 4999
        [3.51,    4.23,    64.36, 519302.88,    722491.15,  108604.45,  295530.10,  1931357.58,     3351667.66   ], # n = 10000 l = 2500
        [5001.79, 5721.51, 50.02, 721175.11,    986467.37,  230637.24,  488193.34,  3607397798.02,  5644571115.47   ]] # n = 10000 l = 1

# font = {'family': 'Verdana',
#         'weight': 'normal'}
# rc('font', **font)

x = [10, 20, 100, 1000, 10000]
print(u'перезапуски')
plt.figure(1)
plt.subplot(131)
plt.semilogx(x, [data[3 * i][0] for i in range(5)], 'r-^', label=u'Experiment')
plt.semilogx(x, [data[3 * i][1] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend()
plt.xlabel('n')
plt.ylabel(u'restarts')
plt.title('$l = \\frac{n}{2} - 1$')

plt.subplot(132)
plt.semilogx(x, [data[3 * i + 1][0] for i in range(5)], 'r-^', label=u'Experiment')
plt.semilogx(x, [data[3 * i + 1][1] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend()
plt.xlabel('n')
plt.ylabel(u'restarts')
plt.title('$l = \\frac{n}{4}$')

plt.subplot(133)
plt.loglog(x, [data[3 * i + 2][0] for i in range(5)], 'r-^', label=u'Experiment')
plt.loglog(x, [data[3 * i + 2][1] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel(u'restarts')
plt.title('$l = 1$')
plt.show()

print(u'неудачные запуски')
plt.figure(2)
plt.subplot(131)
plt.loglog(x, [data[3 * i][3] for i in range(5)], 'r-^', label=u'Experiment')
plt.loglog(x, [data[3 * i][4] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel(u'iterations')
plt.title('$l = \\frac{n}{2} - 1$')


plt.subplot(132)
plt.loglog(x, [data[3 * i + 1][3] for i in range(5)], 'r-^', label=u'Experiment')
plt.loglog(x, [data[3 * i + 1][4] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel(u'iterations')
plt.title('$l = \\frac{n}{4}$')


plt.subplot(133)
plt.loglog(x, [data[3 * i + 2][3] for i in range(5)], 'r-^', label=u'Experiment')
plt.loglog(x, [data[3 * i + 2][4] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel(u'iterations')
plt.title('$l = 1$')
plt.show()


print(u'удачные запуски')
plt.figure(3)
plt.subplot(131)
plt.loglog(x, [data[3 * i][5] for i in range(5)], 'r-^', label=u'Experiment')
plt.loglog(x, [data[3 * i][6] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel(u'iterations')
plt.title('$l = \\frac{n}{2} - 1$')

plt.subplot(132)
plt.loglog(x, [data[3 * i + 1][5] for i in range(5)], 'r-^', label=u'Experiment')
plt.loglog(x, [data[3 * i + 1][6] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel(u'iterations')
plt.title('$l = \\frac{n}{4}$')

plt.subplot(133)
plt.loglog(x, [data[3 * i + 2][5] for i in range(5)], 'r-^', label=u'Experiment')
plt.loglog(x, [data[3 * i + 2][6] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel(u'iterations')
plt.title('$l = 1$')
plt.show()


print(u'всего итераций')
plt.figure(4)
plt.subplot(131)
plt.loglog(x, [data[3 * i][7] for i in range(5)], 'r-^', label=u'Experiment')
plt.loglog(x, [data[3 * i][8] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel(u'iterations')
plt.title('$l = \\frac{n}{2} - 1$')


plt.subplot(132)
plt.loglog(x, [data[3 * i + 1][7] for i in range(5)], 'r-^', label=u'Experiment')
plt.loglog(x, [data[3 * i + 1][8] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel(u'iterations')
plt.title('$l = \\frac{n}{4}$')


plt.subplot(133)
plt.loglog(x, [data[3 * i + 2][7] for i in range(5)], 'r-^', label=u'Experiment')
plt.loglog(x, [data[3 * i + 2][8] for i in range(5)], 'b-o', label=u'Upper bound')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel(u'iterations')
plt.title('$l = 1$')
plt.show()