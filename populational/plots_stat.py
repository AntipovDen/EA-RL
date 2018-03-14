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
            


for k in range(2, 7):
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
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(earl_1p1_xdkom[k][n]) / 800 for n in range(20, 101, 10)], 'b-')

    shift = -1
    bplot = plt.boxplot([earl_2p2_xdkom[k][n] for n in range(20, 101, 10)],
                        flierprops=dict(markersize=2),
                        patch_artist=True,
                        # widths=[0.1] * 9,
                        showmeans=True,
                        meanprops=dict(marker='^', markeredgecolor='black', markerfacecolor='red'),
                        positions=range(20 + shift, 101 + shift, 10),
                        whis=100)
    for box in bplot['boxes']:
        box.set_facecolor('red')
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(earl_2p2_xdkom[k][n]) / 800 for n in range(20, 101, 10)], 'r-')

    shift = 0
    bplot = plt.boxplot([earl_2p2_xdkomzm[k][n] for n in range(20, 101, 10)],
                        flierprops=dict(markersize=2),
                        patch_artist=True,
                        # widths=[0.1] * 9,
                        showmeans=True,
                        meanprops=dict(marker='v', markeredgecolor='black', markerfacecolor='green'),
                        positions=range(20 + shift, 101 + shift, 10),
                        whis=100)
    for box in bplot['boxes']:
        box.set_facecolor('green')
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(earl_2p2_xdkomzm[k][n]) / 800 for n in range(20, 101, 10)], 'g-')

    shift = 1
    bplot = plt.boxplot([earl_2p2n_xdkom[k][n] for n in range(20, 101, 10)],
                        flierprops=dict(markersize=2),
                        patch_artist=True,
                        # widths=[0.1] * 9,
                        showmeans=True,
                        meanprops=dict(marker='s', markeredgecolor='black', markerfacecolor='yellow'),
                        positions=range(20 + shift, 101 + shift, 10),
                        whis=100)
    for box in bplot['boxes']:
        box.set_facecolor('yellow')
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(earl_2p2n_xdkom[k][n]) / 800 for n in range(20, 101, 10)], 'y-')

    shift = 2
    bplot = plt.boxplot([earl_2p2n_xdkomzm[k][n] for n in range(20, 101, 10)],
                        flierprops=dict(markersize=2),
                        patch_artist=True,
                        # widths=[0.1] * 9,
                        showmeans=True,
                        meanprops=dict(marker='p', markeredgecolor='black', markerfacecolor='cyan'),
                        positions=range(20 + shift, 101 + shift, 10),
                        whis=100)
    for box in bplot['boxes']:
        box.set_facecolor('cyan')
    plt.plot(range(20 + shift, 101 + shift, 10), [sum(earl_2p2n_xdkomzm[k][n]) / 800 for n in range(20, 101, 10)], 'c-')


    plt.show()
