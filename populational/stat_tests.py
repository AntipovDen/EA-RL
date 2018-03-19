from scipy.stats import ranksums, variation
from math import sqrt

const = sqrt(800/799)

earl_1p1_xdkom = {}
earl_2p2_xdkom = {}
earl_2p2_xdkomzm = {}
earl_2p2n_xdkom = {}
earl_2p2n_xdkomzm = {}
earlmod_1p1_xdkomzm = {}

data = {'earl_1p1_xdkom'        :   earl_1p1_xdkom,
        'earl_2p2_xdkom'        :   earl_2p2_xdkom,
        'earl_2p2_xdkomzm'      :   earl_2p2_xdkomzm,
        'earl_2p2n_xdkom'       :   earl_2p2n_xdkom,
        'earl_2p2n_xdkomzm'     :   earl_2p2n_xdkomzm,
        'earlmod_1p1_xdkomzm'   :   earlmod_1p1_xdkomzm}

for algoname in data.keys():
    with open('data/{}_merged.log'.format(algoname), 'r') as fin:
        data[algoname] = {}
        for k in range(2, 7):
            data[algoname][k] = {}
            for n in range(20, 101, 10):
                data[algoname][k][n] = list(map(int, fin.readline().split()))

for algoname, algo_stats in data.items():
    print('\n{}'.format(algoname), end='')
    for k in range(2, 7):
        print('\nk{}\t'.format(k), end='')
        # arr = [variation(algo_stats[k][n]) * const * 100 for n in range(20, 101, 10)]
        # print('{:2.2f} {:2.2f}'.format(min(arr), max(arr)), end='')
        for n in range(20, 101, 10):
            print('{:2.2f} '.format(variation(algo_stats[k][n]) * const * 100), end='')
