from matplotlib import pyplot as plt
from scipy.misc import factorial, comb

# n = 100
# k = 10
#
# def z_x(x):
#     return sum([comb(n, x - i) / comb(n - 1, x) for i in range(x % k + 1)])
#
# def z_r(x):
#     return sum([comb(n, x - i) / comb(n - 1, x) / (2 ** i) for i in range(x % k + 1)])
#
# for k in range(2, 15):
#     plt.semilogy(range(n), [z_x(x) for x in range(n)], 'bo-')
#     plt.semilogy(range(n), [z_r(x) for x in range(n)], 'ro-')
#     plt.show()

# merge_files
merge_files = False
if merge_files:
    for filename in 'ea_', 'earl_', 'ea_opo':
        with open('data/{}_merged.txt'.format(filename), 'w') as fout:
            data = []
            for i in range(1, 9):
                with open('data/{}{}.txt'.format(filename, i), 'r') as fin:
                    data.append(fin.readlines())

            lines = len(data[0])
            for line in range(1, lines):
                if data[0][line][0] != '#':
                    floated_data = [[float(number) for number in data[i][line].split()] for i in range(8)]
                    for j in range(len(floated_data[0])):
                        fout.write('{} '.format(sum([floated_data[i][j] for i in range(8)])))
                    fout.write('\n')

# Lines: k in [2..6]. columns: n in [20..100], step = 10.
with open('data/ea__merged.txt', 'r') as f:
    ea_tpt = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earl__merged.txt', 'r') as f:
    ea_rl = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/ea_opo_merged.txt', 'r') as f:
    ea_opo = [[float(s) for s in line.split()] for line in f.readlines()]

n_range = list(range(20, 101, 10))
for k in range(2, 7):
    plt.semilogy(n_range, ea_opo[k - 2], 'ro-', label='$(1 + 1)$-EA')
    plt.semilogy(n_range, ea_tpt[k - 2], 'bo-', label='$(2 + 2)$-EA')
    plt.semilogy(n_range, ea_rl[k - 2], 'g^-', label='EA+RL')
    plt.legend(loc=2)
    plt.xlabel('$n$')
    plt.ylabel('Среднее число итераций')
    plt.title('$k = {}$'.format(k))
    plt.savefig('pic/k{}_iters.png'.format(k), orientation='landscape')
    plt.clf()

for k in range(2, 7):
    plt.plot(n_range, [ea_tpt[k - 2][i] / ea_rl[k - 2][i] for i in range(len(n_range))], 'bo-')
    # plt.legend(loc=2)
    plt.xlabel('$n$')
    plt.ylabel('Отношение среднего числа итераций $(2 + 2)$-EA\n к среднему числу итераций EA+RL')
    plt.title('$k = {}$'.format(k))
    #plt.show()
    plt.savefig('pic/k{}_ratio.png'.format(k), orientation='landscape')
    plt.clf()
