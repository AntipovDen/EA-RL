from matplotlib import pyplot as plt


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
            

# Everything about boxplots was commented
for k in range(2, 7):
    plt.subplot(229 + k)
    shift = -2
    bplot = plt.boxplot([earl_1p1_xdkom[k][n] for n in range(20, 101, 10)],
                        flierprops=dict(markersize=2),
                        patch_artist=True,
                        # widths=[0.1] * 9,
                        showmeans=True,
                        meanprops=dict(marker='o', markeredgecolor='black', markerfacecolor='blue'),
                        positions=range(20 + shift, 101 + shift, 10),
                        whis=100)
    for box in bplot['boxes']:
        box.set_facecolor('blue')
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(earl_1p1_xdkom[k][n]) / 800 for n in range(20, 101, 10)], 'bo-', label='(1 + 1)-EA, XdivK+OneMax')

    shift = -1
    bplot = plt.boxplot([list(map(lambda x: 2 * x, earl_2p2_xdkom[k][n])) for n in range(20, 101, 10)],
                        flierprops=dict(markersize=2),
                        patch_artist=True,
                        # widths=[0.1] * 9,
                        showmeans=True,
                        meanprops=dict(marker='^', markeredgecolor='black', markerfacecolor='red'),
                        positions=range(20 + shift, 101 + shift, 10),
                        whis=100)
    for box in bplot['boxes']:
        box.set_facecolor('red')
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(list(map(lambda x: 2 * x, earl_2p2_xdkom[k][n]))) / 800 for n in range(20, 101, 10)], 'r^-', label='(2 + 2)-EA, XdivK+OneMax')

    shift = 0
    bplot = plt.boxplot([list(map(lambda x: 2 * x, earl_2p2_xdkomzm[k][n])) for n in range(20, 101, 10)],
                        flierprops=dict(markersize=2),
                        patch_artist=True,
                        # widths=[0.1] * 9,
                        showmeans=True,
                        meanprops=dict(marker='v', markeredgecolor='black', markerfacecolor='green'),
                        positions=range(20 + shift, 101 + shift, 10),
                        whis=100)
    for box in bplot['boxes']:
        box.set_facecolor('green')
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(list(map(lambda x: 2 * x, earl_2p2_xdkomzm[k][n]))) / 800 for n in range(20, 101, 10)], 'gv-', label='(2 + 2)-EA, XdivK+OneMax+ZeroMax')

    shift = 1
    bplot = plt.boxplot([list(map(lambda x: 2 * n * x, earl_2p2n_xdkom[k][n])) for n in range(20, 101, 10)],
                        flierprops=dict(markersize=2),
                        patch_artist=True,
                        # widths=[0.1] * 9,
                        showmeans=True,
                        meanprops=dict(marker='s', markeredgecolor='black', markerfacecolor='yellow'),
                        positions=range(20 + shift, 101 + shift, 10),
                        whis=100)
    for box in bplot['boxes']:
        box.set_facecolor('yellow')
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(list(map(lambda x: 2 * n * x, earl_2p2n_xdkom[k][n]))) / 800 for n in range(20, 101, 10)], 'ys-', label='(2 + 2n)-EA, XdivK+OneMax')

    shift = 2
    bplot = plt.boxplot([list(map(lambda x: 2 * n * x, earl_2p2n_xdkomzm[k][n])) for n in range(20, 101, 10)],
                        flierprops=dict(markersize=2),
                        patch_artist=True,
                        # widths=[0.1] * 9,
                        showmeans=True,
                        meanprops=dict(marker='p', markeredgecolor='black', markerfacecolor='cyan'),
                        positions=range(20 + shift, 101 + shift, 10),
                        whis=100)
    for box in bplot['boxes']:
        box.set_facecolor('cyan')
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(list(map(lambda x: 2 * n * x, earl_2p2n_xdkomzm[k][n]))) / 800 for n in range(20, 101, 10)], 'cp-', label='(2 + 2n)-EA, XdivK+OneMax+ZeroMax')

    shift = -3
    bplot = plt.boxplot([earlmod_1p1_xdkomzm[k][n] for n in range(20, 101, 10)],
                        flierprops=dict(markersize=2),
                        patch_artist=True,
                        # widths=[0.1] * 9,
                        showmeans=True,
                        meanprops=dict(marker='d', markeredgecolor='black', markerfacecolor='magenta'),
                        positions=range(20 + shift, 101 + shift, 10),
                        whis=100)
    for box in bplot['boxes']:
        box.set_facecolor('magenta')
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(earlmod_1p1_xdkomzm[k][n]) / 800 for n in range(20, 101, 10)], 'md-', label='Mod. (1 + 1)-EA, XdivK+OneMax+ZeroMax')


    plt.yscale('log')
    plt.xlabel('$n$, individual size')
    plt.ylabel('runtime, iterations')
    plt.title('$k = {}$'.format(k))
    plt.xticks(range(20, 101, 10), [str(i) for i in range(20, 101, 10)])
    plt.xlim(15, 105)
plt.subplots_adjust(wspace=0.2,
                    hspace=0.3,
                    left=0.1,
                    right=2.5,
                    top=1.2,
                    bottom=0
                    )

plt.savefig('pic/xdkom.png',
            bbox_extra_artists=(plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.),),
            bbox_inches='tight',
            dpi=200)
# else:
#     plt.savefig('pic/k{}_iters_box.png'.format(k),
#                 bbox_inches='tight')
# plt.clf()
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.show()
