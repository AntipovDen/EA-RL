from matplotlib import pyplot as plt
from math import e, pi, sqrt, log
from scipy.stats import gaussian_kde
from numpy import histogram


def violin_histogram(data, bins, color, x=0):
    n, _ = histogram(data, bins=bins)
    weight = 0.07
    plt.hist(data,
             bins=bins,
             weights=[weight] * len(data),
             alpha=0.5,
             color=color,
             orientation='horizontal',
             bottom=[x - n_i * weight / 2 for n_i in n])


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
            earl_2p2_xdkom[k][n] = list(map(int, fin.readline().split()))
            
with open('data/earl_2p2_xdkomzm_merged.log', 'r') as fin:
    earl_2p2_xdkomzm = {}
    for k in range(2, 7):
        earl_2p2_xdkomzm[k] = {}
        for n in range(20, 101, 10):
            earl_2p2_xdkomzm[k][n] = list(map(int, fin.readline().split()))
            
with open('data/earl_2p2n_xdkom_merged.log', 'r') as fin:
    earl_2p2n_xdkom = {}
    for k in range(2, 7):
        earl_2p2n_xdkom[k] = {}
        for n in range(20, 101, 10):
            earl_2p2n_xdkom[k][n] = list(map(int, fin.readline().split()))
            
with open('data/earl_2p2n_xdkomzm_merged.log', 'r') as fin:
    earl_2p2n_xdkomzm = {}
    for k in range(2, 7):
        earl_2p2n_xdkomzm[k] = {}
        for n in range(20, 101, 10):
            earl_2p2n_xdkomzm[k][n] = list(map(int, fin.readline().split()))
            
with open('data/earlmod_1p1_xdkomzm_merged.log', 'r') as fin:
    earlmod_1p1_xdkomzm = {}
    for k in range(2, 7):
        earlmod_1p1_xdkomzm[k] = {}
        for n in range(20, 101, 10):
            earlmod_1p1_xdkomzm[k][n] = list(map(int, fin.readline().split()))

with open('data/ea_2p2_xdk_merged.txt', 'r') as fin:
    data4 = list(map(float, fin.readlines()[-1].split()))


data1 = [earl_1p1_xdkom[6][n] for n in range(20, 101, 10)]
data2 = [sorted(list(map(lambda x: 2 * x, earl_2p2_xdkom[6][n]))) for n in range(20, 101, 10)]
data3 = [sorted(list(map(lambda x: x * n, earl_2p2n_xdkom[6][n]))) for n in range(20, 101, 10)]


# plt.plot(range(800), data3[6], 'bo')
# worst = 1
# plt.plot(range(20, 101, 10), [sum(d[-worst:])/worst for d in data2], 'bo-')
# plt.plot(range(20, 101, 10), data4, 'ro-')
# plt.yscale('log')
#
# plt.show()
# exit(0)

scale = 5
for i in range(9):
    violin_histogram(data3[i],
                     color='green',
                     bins=[2 ** (i / scale) for i in range(scale * int(log(max(data3[6]), 2) + 2))],
                     x=i * 10 + 20)
    # violin_histogram(data2[i],
    #                  color='red',
    #                  bins=[2 ** (i / scale) for i in range(scale * int(log(max(data2[6]), 2) + 2))],
    #                  x=i * 10 + 20)
    # violin_histogram(data1[i],
    #                  color='blue',
    #                  bins=[2 ** (i / scale) for i in range(scale * int(log(max(data1[6]), 2) + 2))],
    #                  x=i * 10 + 20)
# plt.plot(range(20, 101, 10), [sum(data1[i]) / len(data1[i]) for i in range(len(data1))], 'bo-')
# plt.plot(range(20, 101, 10), [sum(data2[i]) / len(data2[i]) for i in range(len(data2))], 'ro-')
plt.plot(range(20, 101, 10), [sum(data3[i]) / len(data3[i]) for i in range(len(data3))], 'go-')
plt.yscale('log')
plt.show()
exit(0)


parts = plt.violinplot(data1, showmeans=True, showextrema=True, points=800, bw_method=0.5)
for p in parts['bodies']:
    p.set_facecolor('red')
    p.set_alpha(0.2)
    p.set_linewidths(10)
parts['cmeans'].set_color('red')
parts['cmins'].set_color('red')
parts['cmaxes'].set_color('red')
parts['cbars'].set_color('red')

parts = plt.violinplot(data2, showmeans=True, showextrema=True)
for p in parts['bodies']:
    p.set_facecolor('blue')
    p.set_alpha(0.2)
    p.set_linewidths(10)
parts['cmeans'].set_color('blue')
parts['cmins'].set_color('blue')
parts['cmaxes'].set_color('blue')
parts['cbars'].set_color('blue')

parts = plt.violinplot(data3, showmeans=True, showextrema=True, positions=list(map(lambda x: x + 1, range(9))))
for p in parts['bodies']:
    p.set_facecolor('green')
    p.set_alpha(0.2)
    p.set_linewidths(10)
parts['cmeans'].set_color('green')
parts['cmins'].set_color('green')
parts['cmaxes'].set_color('green')
parts['cbars'].set_color('green')

plt.yscale('log')
plt.xticks(range(1, 10), [str(i) for i in range(20, 101, 10)])
plt.show()
# plt.legend(loc='')
exit(0)

plt.subplots_adjust(wspace=0.2,
                    hspace=0.3,
                    left=0.1,
                    right=2.5,
                    top=1.2,
                    bottom=0
                    )

plt.savefig('pic/xdkom_violin.png',
            bbox_extra_artists=(plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.),),
            bbox_inches='tight',
            dpi=200)
# else:
#     plt.savefig('pic/k{}_iters_box.png'.format(k),
#                 bbox_inches='tight')
# plt.clf()
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.show()
