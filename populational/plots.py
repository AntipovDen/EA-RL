from matplotlib import pyplot as plt
from scipy.misc import factorial, comb



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
