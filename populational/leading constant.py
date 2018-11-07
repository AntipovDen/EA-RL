from math import e
from matplotlib import pyplot as plt


with open('data/earl_2p2n_xdkom_merged.txt', 'r') as f:
    earl_2p2n_xdkom = [[float(s) for s in line.split()] for line in f.readlines()]

with open('data/earl_2p2n_xdkomzm_merged.txt', 'r') as f:
    earl_2p2n_xdkomzm = [[float(s) for s in line.split()] for line in f.readlines()]

earl_2p2n_xdkom_theory = [[n / k * (e / (e - 1) + (2 * e / (e - 1)) ** k / 2 + k + 450) for n in range(20, 101, 10)] for k in range(2, 7)]
earl_2p2n_xdkomzm_theory = [[n / k * (5 * e / (3 * (e - 1)) + (3 ** k + 2 ** k) * (e / (e - 1)) ** k / 2 + 2 * k + 900) for n in range(20, 101, 10)] for k in range(2, 7)]


nrange = range(20, 101, 10)
ratio_xdkom = [[earl_2p2n_xdkom_theory[k][n] / earl_2p2n_xdkom[k][n] for n in range(9)] for k in range(5)]
ratio_xdkomzm = [[earl_2p2n_xdkomzm_theory[k][n] / earl_2p2n_xdkomzm[k][n] for n in range(9)] for k in range(5)]


print('$k$ & minimal ratio for \XdKOM & maximal ratio for \XdKOM & minimal ratio for \XdKOMZM & maximal ratio for \XdKOMZM \\\\')
for k in range(5):
    print('{} & {:.2f} & {:.2f} & {:.2f} & {:.2f} \\\\'.format(k + 2, min(ratio_xdkom[k]), max(ratio_xdkom[k]), min(ratio_xdkomzm[k]), max(ratio_xdkomzm[k])))
    # print('xdkom min {} max {}'.format(min(ratio_xdkom[k]), max(ratio_xdkom[k])))
    # print('xdkomzm min {} max {}'.format(min(ratio_xdkomzm[k]), max(ratio_xdkomzm[k])))
    plt.subplot(231 + k)
    plt.plot(nrange, ratio_xdkom[k], 'bo-', label='(XdivK, OneMax)')
    plt.plot(nrange, ratio_xdkomzm[k], 'ro-', label='(XdivK, OneMax, ZeroMax)')
    plt.xlabel('$n$, individual size')
    plt.ylabel('ratio')
    plt.title('k = {}'.format(k + 2))

plt.subplots_adjust(wspace=0.4,
                    hspace=0.6,
                    left=0,
                    right=1,
                    top=0.6,
                    bottom=0)
plt.savefig('pic/ratio_appendix.png',
            bbox_extra_artists=(plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.),),
            bbox_inches='tight',
            dpi=200)