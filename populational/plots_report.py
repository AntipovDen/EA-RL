from matplotlib import pyplot as plt
from scipy.misc import factorial, comb
from math import e



# Lines: k in [2..6]. columns: n in [20..100], step = 10.
with open('data/ea_1p1_xdk_merged.txt', 'r') as f:
    ea_1p1_xdk = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/ea_2p2_xdk_merged.txt', 'r') as f:
    ea_2p2_xdk = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earl_1p1_xdkom_merged.txt', 'r') as f:
    earl_1p1_xdkom = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earlmod_1p1_xdkomzm_merged.txt', 'r') as f:
    earlmod_1p1_xdkomzm = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earl_2p2_xdkom_merged.txt', 'r') as f:
    earl_2p2_xdkom = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earl_2p2_xdkomzm_merged.txt', 'r') as f:
    earl_2p2_xdkomzm = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earl_2p2n_xdkom_merged.txt', 'r') as f:
    earl_2p2n_xdkom = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earl_2p2n_xdkomzm_merged.txt', 'r') as f:
    earl_2p2n_xdkomzm = [[float(s) for s in line.split()] for line in f.readlines()]

earl_2p2n_xdkom_theory = [[((2 * e / (e - 1)) ** k / (2 * k) + 1) * n for n in range(20, 101, 10)] for k in range(2, 7)]
earl_2p2n_xdkomzm_theory = [[((3 * e / (e - 1)) ** k / (2 * k) + 1) * n for n in range(20, 101, 10)] for k in range(2, 7)]

n_range = list(range(20, 101, 10))

for with_zm in True, False:

    for k in range(2, 7):
        plt.subplot(229 + k)
        plt.semilogy(n_range[:len(ea_1p1_xdk[k - 2])], ea_1p1_xdk[k - 2], 'ro-',
                     label='$(1 + 1)$-EA')
        plt.semilogy(n_range, ea_2p2_xdk[k - 2], 'bs-',
                     label='$(2 + 2)$-EA')

        if not with_zm:
            plt.semilogy(n_range, earl_1p1_xdkom[k - 2], 'g^-',
                         label='$(1 + 1)$-EA+RL')
            plt.semilogy(n_range, list(map(lambda x: x * 2, earl_2p2_xdkom[k - 2])), 'yv-',
                         label='$(2 + 2)$-EA+RL')
            plt.semilogy(n_range, list(map(lambda x, y: 2 * x * y, earl_2p2n_xdkom[k - 2], n_range)), 'cd-',
                         label='$(2 + 2n)$-EA+RL')
            plt.semilogy(n_range, list(map(lambda x, y: 2 * x * y, earl_2p2n_xdkom_theory[k - 2], n_range)), 'mx--',
                         label='$(2 + 2n)$-EA+RL (Теория)')
        else:
            plt.semilogy(n_range, earlmod_1p1_xdkomzm[k - 2], 'g^-',
                         label='modif. $(1 + 1)$-EA+RL')
            plt.semilogy(n_range, list(map(lambda x: x * 2, earl_2p2_xdkomzm[k - 2])), 'yv-',
                         label='$(2 + 2)$-EA+RL')
            plt.semilogy(n_range, list(map(lambda x, y: 2 * x * y, earl_2p2n_xdkomzm[k - 2], n_range)), 'cd-',
                         label='$(2 + 2n)$-EA+RL')
            plt.semilogy(n_range, list(map(lambda x, y: 2 * x * y, earl_2p2n_xdkomzm_theory[k - 2], n_range)), 'mx--',
                         label='$(2 + 2n)$-EA+RL (Теория)')

        plt.xlabel('$n$, размер особи')
        plt.ylabel('Время работы,\nвычислений фитнеса')
        plt.title('$k = {}$'.format(k))
        plt.xlim(15, 105)

    plt.subplots_adjust(wspace=0.4,
                        hspace=0.5,
                        left=0.2,
                        right=1.5,
                        top=0.7,
                        bottom=0
                        )
    plt.savefig('pic/xdkom{}_evals_report.png'.format('zm' if with_zm else ''),
                bbox_extra_artists=(plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.),),
                bbox_inches='tight',
                dpi=200)
    plt.clf()
