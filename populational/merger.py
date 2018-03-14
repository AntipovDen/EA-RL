merge_logs = True


def mean_of_arrays(arrays):
    return " ".join([str(sum(arrays[i][j] for i in range(len(arrays))) / len(arrays)) for j in range(len(arrays[0]))])


def mean_of_lines(lines):
    return mean_of_arrays([[float(x) for x in line.split()] for line in lines])


for filename in 'earl_1p1_xdkom', 'earl_2p2_xdkom', 'earl_2p2_xdkomzm', 'earl_2p2n_xdkom', 'earl_2p2n_xdkomzm':
    n = 8  # number of files
    if merge_logs:
        data = [[] for _ in range(9 * 5)]  # each array for one of nine values of n and one of four values of k
        for i in range(1, n + 1):
            with open('data/{}/{}_{}.log'.format(filename, filename, i), 'r') as fin:
                runs = fin.readlines()
                for j in range(45):
                    data[j] += runs[101 * j + 1: 101 * j + 101]
        with open('data/{}_merged.log'.format(filename), 'w') as fout:
            for line in data:
                for run in line:
                    fout.write('{} '.format(run[:-1]))
                fout.write('\n')

    else:
        data = []
        for i in range(2, n + 1):
            with open('data/{}/{}_{}.txt'.format(filename, filename, i), 'r') as fin:
                data.append(fin.readlines())

        with open('data/{}_merged.txt'.format(filename), 'w') as fout:
            lines = len(data[0])
            for line in range(0, lines):
                if data[0][line][0] != '#':
                    fout.write(mean_of_lines([data[i][line] for i in range(len(data))]))
                    fout.write('\n')
