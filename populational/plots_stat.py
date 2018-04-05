from matplotlib import pyplot as plt
from math import e, pi, sqrt, log
from scipy.stats import gaussian_kde
from numpy import histogram


def violin_histogram(data, bins, color, x=0, label=None, alpha=0.5):
    n, _ = histogram(data, bins=bins)
    weight = 0.07
    if label is None:
        plt.hist(data,
                 bins=bins,
                 weights=[weight] * len(data),
                 alpha=alpha,
                 color=color,
                 orientation='horizontal',
                 bottom=[x - n_i * weight / 2 for n_i in n])
    else:
        plt.hist(data,
                 bins=bins,
                 weights=[weight] * len(data),
                 alpha=alpha,
                 color=color,
                 orientation='horizontal',
                 bottom=[x - n_i * weight / 2 for n_i in n],
                 label=label)


with open('data/earl_1p1_xdkom_merged.log', 'r') as fin:
    earl_1p1_xdkom = {}
    for k in range(2, 7):
        earl_1p1_xdkom[k] = {}
        for n in range(20, 101, 10):
            earl_1p1_xdkom[k][n] = list(map(int, fin.readline().split()))

with open('data/earl_2p2_xdkom_merged.log', 'r') as fin:
    earl_2p2_xdkom = {}
    for k in range(2, 7):
        earl_2p2_xdkom[k] = {}
        for n in range(20, 101, 10):
            earl_2p2_xdkom[k][n] = list(map(lambda x: int(x) * 2, fin.readline().split()))
            
with open('data/earl_2p2_xdkomzm_merged.log', 'r') as fin:
    earl_2p2_xdkomzm = {}
    for k in range(2, 7):
        earl_2p2_xdkomzm[k] = {}
        for n in range(20, 101, 10):
            earl_2p2_xdkomzm[k][n] = list(map(lambda x: int(x) * 2, fin.readline().split()))
            
with open('data/earl_2p2n_xdkom_merged.log', 'r') as fin:
    earl_2p2n_xdkom = {}
    for k in range(2, 7):
        earl_2p2n_xdkom[k] = {}
        for n in range(20, 101, 10):
            earl_2p2n_xdkom[k][n] = list(map(lambda x: int(x) * n, fin.readline().split()))
            
with open('data/earl_2p2n_xdkomzm_merged.log', 'r') as fin:
    earl_2p2n_xdkomzm = {}
    for k in range(2, 7):
        earl_2p2n_xdkomzm[k] = {}
        for n in range(20, 101, 10):
            earl_2p2n_xdkomzm[k][n] = list(map(lambda x: int(x) * n, fin.readline().split()))
            
with open('data/earlmod_1p1_xdkomzm_merged.log', 'r') as fin:
    earlmod_1p1_xdkomzm = {}
    for k in range(2, 7):
        earlmod_1p1_xdkomzm[k] = {}
        for n in range(20, 101, 10):
            earlmod_1p1_xdkomzm[k][n] = list(map(int, fin.readline().split()))

# with open('data/ea_2p2_xdk_merged.txt', 'r') as fin:
#     data4 = list(map(float, fin.readlines()[-1].split()))


# earl_1p1_xdkom_plot = [earl_1p1_xdkom[6][n] for n in range(20, 101, 10)]
# earl_2p2_xdkom_plot = [sorted(list(map(lambda x: 2 * x, earl_2p2_xdkom[6][n]))) for n in range(20, 101, 10)]
# earl_2p2n_xdkom_plot = [sorted(list(map(lambda x: x * n, earl_2p2n_xdkom[6][n]))) for n in range(20, 101, 10)]
#
# earlmod_1p1_xdkomzm_plot = [earlmod_1p1_xdkomzm[6][n] for n in range(20, 101, 10)]
# earl_2p2_xdkomzm_plot = [sorted(list(map(lambda x: 2 * x, earl_2p2_xdkomzm[6][n]))) for n in range(20, 101, 10)]
# earl_2p2n_xdkomzm_plot = [sorted(list(map(lambda x: x * n, earl_2p2n_xdkomzm[6][n]))) for n in range(20, 101, 10)]
#


scale = 5
plt.subplot(121)
for n in range(20, 101, 10):
    violin_histogram(earl_1p1_xdkom[6][n],
                     color='blue',
                     bins=[2 ** (i / scale) for i in range(scale * int(log(max(earl_1p1_xdkom[6][n]), 2) + 2))],
                     x=n)
    violin_histogram(earl_2p2_xdkom[6][n],
                     color='red',
                     bins=[2 ** (i / scale) for i in range(scale * int(log(max(earl_2p2_xdkom[6][n]), 2) + 2))],
                     x=n,
                     alpha=0.8)
    violin_histogram(earl_2p2n_xdkom[6][n],
                     color='green',
                     bins=[2 ** (i / scale) for i in range(scale * int(log(max(earl_2p2n_xdkom[6][n]), 2) + 2))],
                     x=n)

plt.yscale('log')
plt.xlim(15, 108)
plt.ylim(ymin=10)
plt.xlabel('$n$, individual size')
plt.ylabel('runtime, fitness\nevaluations')
plt.title('XdivK+OneMax')

scale = 5
plt.subplot(122)
for n in range(20, 101, 10):
    violin_histogram(earlmod_1p1_xdkomzm[6][n],
                     color='blue',
                     bins=[2 ** (i / scale) for i in range(scale * int(log(max(earlmod_1p1_xdkomzm[6][n]), 2) + 2))],
                     x=n,
                     label='modif. $(1+1)$-EA+RL' if n == 20 else None)
    violin_histogram(earl_2p2_xdkomzm[6][n],
                     color='red',
                     bins=[2 ** (i / scale) for i in range(scale * int(log(max(earl_2p2_xdkomzm[6][n]), 2) + 2))],
                     x=n,
                     label='$(2+2)$-EA+RL' if n == 20 else None,
                     alpha=0.8)
    violin_histogram(earl_2p2n_xdkomzm[6][n],
                     color='green',
                     bins=[2 ** (i / scale) for i in range(scale * int(log(max(earl_2p2n_xdkomzm[6][n]), 2) + 2))],
                     x=n,
                     label='$(2+2n)$-EA+RL' if n == 20 else None)
# plt.plot(range(20, 101, 10), [sum(earlmod_1p1_xdkomzm[i]) / len(earlmod_1p1_xdkomzm[i]) for i in range(len(earlmod_1p1_xdkomzm))], 'bo-')
# plt.plot(range(20, 101, 10), [sum(earl_2p2_xdkomzm[i]) / len(earl_2p2_xdkomzm[i]) for i in range(len(earl_2p2_xdkomzm))], 'ro-')
# plt.plot(range(20, 101, 10), [sum(earl_2p2n_xdkomzm[i]) / len(earl_2p2n_xdkomzm[i]) for i in range(len(earl_2p2n_xdkomzm))], 'go-')
plt.yscale('log')
plt.xlim(15, 108)
plt.ylim(ymin=10)
plt.xlabel('$n$, individual size')
plt.ylabel('runtime, fitness\nevaluations')
plt.title('XdivK+OneMax+ZeroMax')


plt.subplots_adjust(wspace=0.26,
                    hspace=0,
                    left=0.1,
                    right=1.2,
                    top=0.4,
                    bottom=0
                    )

plt.savefig('pic/histograms.png',
            bbox_extra_artists=(plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.),),
            bbox_inches='tight',
            dpi=100)



for k in range(2, 6):
    plt.subplot(409+k)
    for n in range(20, 101, 10):
        violin_histogram(earlmod_1p1_xdkomzm[k][n],
                         color='blue',
                         bins=[2 ** (i / scale) for i in range(scale * int(log(max(earlmod_1p1_xdkomzm[k][n]), 2) + 2))],
                         x=n,
                         label='modif. $(1+1)$-EA+RL' if n == 20 else None)
        violin_histogram(earl_2p2_xdkomzm[k][n],
                         color='red',
                         bins=[2 ** (i / scale) for i in range(scale * int(log(max(earl_2p2_xdkomzm[k][n]), 2) + 2))],
                         x=n,
                         label='$(2+2)$-EA+RL' if n == 20 else None,
                         alpha=0.8)
        violin_histogram(earl_2p2n_xdkomzm[k][n],
                         color='green',
                         bins=[2 ** (i / scale) for i in range(scale * int(log(max(earl_2p2n_xdkomzm[k][n]), 2) + 2))],
                         x=n,
                         label='$(2+2n)$-EA+RL' if n == 20 else None)
    # plt.plot(range(20, 101, 10), [sum(earlmod_1p1_xdkomzm[i]) / len(earlmod_1p1_xdkomzm[i]) for i in range(len(earlmod_1p1_xdkomzm))], 'bo-')
    # plt.plot(range(20, 101, 10), [sum(earl_2p2_xdkomzm[i]) / len(earl_2p2_xdkomzm[i]) for i in range(len(earl_2p2_xdkomzm))], 'ro-')
    # plt.plot(range(20, 101, 10), [sum(earl_2p2n_xdkomzm[i]) / len(earl_2p2n_xdkomzm[i]) for i in range(len(earl_2p2n_xdkomzm))], 'go-')
    plt.yscale('log')
    plt.xlim(15, 108)
    plt.ylim(ymin=10)
    plt.xlabel('$n$, individual size')
    plt.ylabel('runtime, fitness\nevaluations')
    plt.title('k = {}'.format(k))

plt.subplots_adjust(wspace=0.5,
                    hspace=0.4,
                    left=0,
                    right=0.5,
                    top=2,
                    bottom=0)
plt.savefig('pic/xdkomzm_hist_appendix.png',
            bbox_extra_artists=(plt.legend(bbox_to_anchor=(0, -0.3), loc=2, borderaxespad=0.),),
            bbox_inches='tight',
            dpi=200)
plt.clf()





for k in range(2, 6):
    plt.subplot(409+k)
    for n in range(20, 101, 10):
        violin_histogram(earl_1p1_xdkom[k][n],
                         color='blue',
                         bins=[2 ** (i / scale) for i in range(scale * int(log(max(earl_1p1_xdkom[k][n]), 2) + 2))],
                         x=n,
                         label='modif. $(1+1)$-EA+RL' if n == 20 else None)
        violin_histogram(earl_2p2_xdkom[k][n],
                         color='red',
                         bins=[2 ** (i / scale) for i in range(scale * int(log(max(earl_2p2_xdkom[k][n]), 2) + 2))],
                         x=n,
                         label='$(2+2)$-EA+RL' if n == 20 else None,
                         alpha=0.8)
        violin_histogram(earl_2p2n_xdkom[k][n],
                         color='green',
                         bins=[2 ** (i / scale) for i in range(scale * int(log(max(earl_2p2n_xdkom[k][n]), 2) + 2))],
                         x=n,
                         label='$(2+2n)$-EA+RL' if n == 20 else None)
    # plt.plot(range(20, 101, 10), [sum(earlmod_1p1_xdkomzm[i]) / len(earlmod_1p1_xdkomzm[i]) for i in range(len(earlmod_1p1_xdkomzm))], 'bo-')
    # plt.plot(range(20, 101, 10), [sum(earl_2p2_xdkomzm[i]) / len(earl_2p2_xdkomzm[i]) for i in range(len(earl_2p2_xdkomzm))], 'ro-')
    # plt.plot(range(20, 101, 10), [sum(earl_2p2n_xdkomzm[i]) / len(earl_2p2n_xdkomzm[i]) for i in range(len(earl_2p2n_xdkomzm))], 'go-')
    plt.yscale('log')
    plt.xlim(15, 108)
    plt.ylim(ymin=10)
    plt.xlabel('$n$, individual size')
    plt.ylabel('runtime, fitness\nevaluations')
    plt.title('k = {}'.format(k))

plt.subplots_adjust(wspace=0.5,
                    hspace=0.4,
                    left=0,
                    right=0.5,
                    top=2,
                    bottom=0)
plt.savefig('pic/xdkom_hist_appendix.png',
            bbox_extra_artists=(plt.legend(bbox_to_anchor=(0, -0.3), loc=2, borderaxespad=0.),),
            bbox_inches='tight',
            dpi=200)
plt.clf()
