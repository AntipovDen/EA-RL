from matplotlib import pyplot as plt
from scipy.misc import factorial, comb



# Lines: k in [2..6]. columns: n in [20..100], step = 10.
with open('data/ea_1p1_xdk_merged.txt', 'r') as f:
    ea_1p1_xdk = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/ea_2p2_xdk_merged.txt', 'r') as f:
    ea_2p2_xdk = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earl_1p1_xdkom_merged.txt', 'r') as f:
    earl_1p1_xdkom = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earl_2p2_xdkom_merged.txt', 'r') as f:
    earl_2p2_xdkom = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earl_2p2_xdkomzm_merged.txt', 'r') as f:
    earl_2p2_xdkomzm = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earlmod_1p1_xdkomzm_merged.txt', 'r') as f:
    earlmod_1p1_xdkomzm = [[float(s) for s in line.split()] for line in f.readlines()]

n_range = list(range(20, 101, 10))
for k in range(2, 7):
    plt.semilogy(n_range[:len(ea_1p1_xdk[k - 2])], ea_1p1_xdk[k - 2], 'ro-', label='$(1 + 1)$-EA')
    plt.semilogy(n_range, ea_2p2_xdk[k - 2], 'bo-', label='$(2 + 2)$-EA')
    plt.semilogy(n_range, earl_1p1_xdkom[k - 2], 'g^-', label='$(1 + 1)$-EA+RL (OneMax)')
    plt.semilogy(n_range, earl_2p2_xdkom[k - 2], 'y^-', label='$(2 + 2)$-EA+RL (OneMax)')
    plt.semilogy(n_range, earl_2p2_xdkomzm[k - 2], 'k^-', label='$(2 + 2)$-EA+RL (OneMax, ZeroMax)')
    plt.semilogy(n_range, earlmod_1p1_xdkomzm[k - 2], 'm^-', label='modif. $(1 + 1)$-EA+RL (OneMax, ZeroMax)')
    plt.legend(loc=4)
    plt.xlabel('$n$')
    plt.ylabel('Среднее число итераций')
    plt.title('$k = {}$'.format(k))
    plt.savefig('pic/k{}_iters.png'.format(k), orientation='landscape')
    plt.clf()

for k in range(2, 7):
    plt.semilogy(n_range[:len(ea_1p1_xdk[k - 2])], ea_1p1_xdk[k - 2], 'ro-', label='$(1 + 1)$-EA')
    plt.semilogy(n_range, [2 * x for x in ea_2p2_xdk[k - 2]], 'bo-', label='$(2 + 2)$-EA')
    plt.semilogy(n_range, earl_1p1_xdkom[k - 2], 'g^-', label='$(1 + 1)$-EA+RL (OneMax)')
    plt.semilogy(n_range, [2 * x for x in earl_2p2_xdkom[k - 2]], 'y^-', label='$(2 + 2)$-EA+RL (OneMax)')
    plt.semilogy(n_range, [2 * x for x in earl_2p2_xdkomzm[k - 2]], 'k^-', label='$(2 + 2)$-EA+RL (OneMax, ZeroMax)')
    plt.semilogy(n_range, earlmod_1p1_xdkomzm[k - 2], 'm^-', label='modif. $(1 + 1)$-EA+RL (OneMax, ZeroMax)')
    plt.legend(loc=4)
    plt.xlabel('$n$')
    plt.ylabel('Среднее число вычислений фитнеса')
    plt.title('$k = {}$'.format(k))
    plt.savefig('pic/k{}_evals.png'.format(k), orientation='landscape')
    plt.clf()
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
