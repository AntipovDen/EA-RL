from matplotlib import pyplot as plt
from scipy.misc import factorial, comb


# merge_files
def mean_of_arrays(arrays):
    return " ".join([str(sum(arrays[i][j] for i in range(len(arrays))) / len(arrays)) for j in range(len(arrays[0]))])


def mean_of_lines(lines):
    return mean_of_arrays([[float(x) for x in line.split()] for line in lines])


merge_files = False
if merge_files:
    for filename in ['ea_opo']:  # , 'earl_', 'ea_opo':
        with open('data/{}_merged.txt'.format(filename), 'w') as fout:
            data = []
            for i in range(1, 5):
                with open('data/{}{}.txt'.format(filename, i), 'r') as fin:
                    data.append(fin.readlines())

            lines = len(data[0])
            for line in range(1, lines):
                if data[0][line][0] != '#':
                    # floated_data = [[float(number) for number in data[i][line].split()] for i in range(8)]
                    # for j in range(len(floated_data[0])):
                    #     fout.write('{} '.format(sum([floated_data[i][j] for i in range(8)]) / 8))
                    fout.write(mean_of_lines([data[i][line] for i in range(len(data))]))
                    fout.write('\n')


# Lines: k in [2..6]. columns: n in [20..100], step = 10.
with open('ea_tpt.txt', 'r') as f:
    ea_tpt = [float(s) for s in f.readline().split()]

with open('earl_tpt.txt', 'r') as f:
    earl_tpt = [float(s) for s in f.readline().split()]

with open('ea_opo.txt', 'r') as f:
    ea_opo = [float(s) for s in f.readline().split()]

with open('earl_opo.txt', 'r') as f:
    earl_opo = [float(s) for s in f.readline().split()]


n_range = list(range(20, 101, 10))
for k in range(2, 3):
    plt.semilogy(n_range, ea_opo, 'ro-', label='$(1 + 1)$-EA')
    plt.semilogy(n_range, ea_tpt, 'bo-', label='$(2 + 2)$-EA')
    plt.semilogy(n_range, earl_opo, 'g^-', label='EA+RL $(1 + 1)$')
    plt.semilogy(n_range, earl_tpt, 'y^-', label='EA+RL $(2 + 2)$')
    plt.legend(loc=2)
    plt.xlabel('$n$')
    plt.ylabel('Среднее число итераций')
    plt.title('$k = {}$'.format(k))
    plt.show()
    # plt.savefig('pic/k{}_iters.png'.format(k), orientation='landscape')
    # plt.clf()

for k in range(2, 3):
    plt.semilogy(n_range, ea_opo, 'ro-', label='$(1 + 1)$-EA')
    plt.semilogy(n_range, [x * 2 for x in ea_tpt], 'bo-', label='$(2 + 2)$-EA')
    plt.semilogy(n_range, earl_opo, 'g^-', label='EA+RL $(1 + 1)$')
    plt.semilogy(n_range, [x * 2 for x in earl_tpt], 'y^-', label='EA+RL $(2 + 2)$')
    plt.legend(loc=2)
    plt.xlabel('$n$')
    plt.ylabel('Среднее число вычислений фитнеса')
    plt.title('$k = {}$'.format(k))
    plt.show()
    # plt.savefig('pic/k{}_evals.png'.format(k), orientation='landscape')
    # plt.clf()
exit(0)

for k in range(2, 7):
    plt.plot(n_range, [ea_tpt[k - 2][i] / ea_rl[k - 2][i] for i in range(len(n_range))], 'bo-')
    # plt.legend(loc=2)
    plt.xlabel('$n$')
    plt.ylabel('Отношение среднего числа итераций $(2 + 2)$-EA\n к среднему числу итераций EA+RL')
    plt.title('$k = {}$'.format(k))
    #plt.show()
    plt.savefig('pic/k{}_ratio.png'.format(k), orientation='landscape')
    plt.clf()
