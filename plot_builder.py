from matplotlib import pyplot as plt


# [number of restarts, exp, percents, iters_restart, exp, iters_ok, exp, total, exp]
map = {10: {4: 0, 2: 1, 1: 2},
       20: {9: 3, 5: 4, 1: 5},
       100: {49: 6, 25: 7, 1: 8},
       1000: {499: 9, 250: 10, 1: 11},
       10000: {4999: 12, 2500: 13, 1: 14}}

data = [[1.63, 15.58, 79.42, 178.59, 235.09, 33.05, 78.77, 324.69, 3741.26],
        [2.81, 23.38, 67.11, 185.39, 264.61, 34.83, 101.37, 555.03, 6288.42],
        [4.01, 33.54, 58.57, 193.34, 280.38, 35.57, 110.20, 810.29, 9514.21],
        [1.80, 8.55, 79.74, 419.11, 553.03, 79.54, 189.39, 832.68, 4915.93],
        [2.83, 13.04, 67.91, 433.08, 617.50, 83.65, 242.10, 1307.54, 8293.69],
        [9.23, 36.68, 55.21, 482.12, 702.72, 102.58, 295.13, 4553.00, 26073.37],
        [1.58, 4.03, 80.10, 2848.88, 3762.18, 556.69, 1332.86, 5052.22, 16493.21],
        [3.45, 7.34, 65.36, 2955.17, 4181.03, 612.19, 1684.41, 10816.38, 32366.15],
        [49.20, 94.26, 50.94, 3614.28, 5119.49, 943.67, 2300.99, 178748.02, 484858.86],
        [1.77, 2.38, 80.32, 39504.30, 52181.51, 7770.18, 19041.51, 77613.77, 143211.92],
        [3.62, 4.77, 63.72, 40761.64, 56607.91, 8519.73, 22776.75, 156280.67, 293011.24],
        [510.02, 633.31, 50.01, 54060.66, 73920.65, 16253.47, 34568.04, 27588219.22, 46849015.80],
        [1.72, 1.77, 81.69, 506216.58, 667966.40, 101739.72, 247934.83, 969901.15, 1430430.56],
        [3.51, 3.75, 64.36, 519302.88, 712472.82, 108604.45, 285511.77, 1931357.58, 2955464.32],
        [5001.79, 5193.82, 50.02, 721175.11, 966056.17, 230637.24, 460854.66, 3607397798.02, 5017980191.65]]



x = [10, 20, 100, 1000, 10000]
print('restarts')
plt.figure(1)
plt.subplot(131)
plt.semilogx(x, [data[3 * i][0] for i in range(5)], 'r-o', label='Experiment')
plt.semilogx(x, [data[3 * i][1] for i in range(5)], 'b-o', label='Theory')
plt.legend()
plt.xlabel('n')
plt.ylabel('restarts')
plt.title('$l = \\frac{n}{2} - 1$')

plt.subplot(132)
plt.semilogx(x, [data[3 * i + 1][0] for i in range(5)], 'r-o', label='Experiment')
plt.semilogx(x, [data[3 * i + 1][1] for i in range(5)], 'b-o', label='Theory')
plt.legend()
plt.xlabel('n')
plt.ylabel('restarts')
plt.title('$l = \\frac{n}{4}$')

plt.subplot(133)
plt.loglog(x, [data[3 * i + 2][0] for i in range(5)], 'r-o', label='Experiment')
plt.loglog(x, [data[3 * i + 2][1] for i in range(5)], 'b-o', label='Theory')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel('restarts')
plt.title('$l = 1$')
plt.show()

print('unsuccessful runs')
plt.figure(2)
plt.subplot(131)
plt.loglog(x, [data[3 * i][3] for i in range(5)], 'r-o', label='Experiment')
plt.loglog(x, [data[3 * i][4] for i in range(5)], 'b-o', label='Theory')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel('iterations')
plt.title('$l = \\frac{n}{2} - 1$')


plt.subplot(132)
plt.loglog(x, [data[3 * i + 1][3] for i in range(5)], 'r-o', label='Experiment')
plt.loglog(x, [data[3 * i + 1][4] for i in range(5)], 'b-o', label='Theory')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel('iterations')
plt.title('$l = \\frac{n}{4}$')


plt.subplot(133)
plt.loglog(x, [data[3 * i + 2][3] for i in range(5)], 'r-o', label='Experiment')
plt.loglog(x, [data[3 * i + 2][4] for i in range(5)], 'b-o', label='Theory')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel('iterations')
plt.title('$l = 1$')
plt.show()


print('successful runs')
plt.figure(3)
plt.subplot(131)
plt.loglog(x, [data[3 * i][5] for i in range(5)], 'r-o', label='Experiment')
plt.loglog(x, [data[3 * i][6] for i in range(5)], 'b-o', label='Theory')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel('iterations')
plt.title('$l = \\frac{n}{2} - 1$')

plt.subplot(132)
plt.loglog(x, [data[3 * i + 1][5] for i in range(5)], 'r-o', label='Experiment')
plt.loglog(x, [data[3 * i + 1][6] for i in range(5)], 'b-o', label='Theory')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel('iterations')
plt.title('$l = \\frac{n}{4}$')

plt.subplot(133)
plt.loglog(x, [data[3 * i + 2][5] for i in range(5)], 'r-o', label='Experiment')
plt.loglog(x, [data[3 * i + 2][6] for i in range(5)], 'b-o', label='Theory')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel('iterations')
plt.title('$l = 1$')
plt.show()


print('total iterations')
plt.figure(4)
plt.subplot(131)
plt.loglog(x, [data[3 * i][7] for i in range(5)], 'r-o', label='Experiment')
plt.loglog(x, [data[3 * i][8] for i in range(5)], 'b-o', label='Theory')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel('iterations')
plt.title('$l = \\frac{n}{2} - 1$')


plt.subplot(132)
plt.loglog(x, [data[3 * i + 1][7] for i in range(5)], 'r-o', label='Experiment')
plt.loglog(x, [data[3 * i + 1][8] for i in range(5)], 'b-o', label='Theory')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel('iterations')
plt.title('$l = \\frac{n}{4}$')


plt.subplot(133)
plt.loglog(x, [data[3 * i + 2][7] for i in range(5)], 'r-o', label='Experiment')
plt.loglog(x, [data[3 * i + 2][8] for i in range(5)], 'b-o', label='Theory')
plt.legend(loc=2)
plt.xlabel('n')
plt.ylabel('iterations')
plt.title('$l = 1$')
plt.show()