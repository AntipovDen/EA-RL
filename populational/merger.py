filename = 'earl_1p1_xdkom'
n = 8  # number of files


def mean_of_arrays(arrays):
    return " ".join([str(sum(arrays[i][j] for i in range(len(arrays))) / len(arrays)) for j in range(len(arrays[0]))])


def mean_of_lines(lines):
    return mean_of_arrays([[float(x) for x in line.split()] for line in lines])



with open('data/{}_merged.txt'.format(filename), 'w') as fout:
    data = []
    for i in range(1, n + 1):
        with open('data/{}_{}.txt'.format(filename, i), 'r') as fin:
            data.append(fin.readlines())

    lines = len(data[0])
    for line in range(0, lines):
        if data[0][line][0] != '#':
            fout.write(mean_of_lines([data[i][line] for i in range(len(data))]))
            fout.write('\n')
