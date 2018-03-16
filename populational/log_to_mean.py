filename = 'earl_2p2n_xdkomzm'

with open('data/{}_merged.log'.format(filename), 'r') as fin:
    data = [sum([int(s) for s in line.split()]) / len(line.split()) for line in fin.readlines()]

with open('data/{}_merged.txt'.format(filename), 'w') as fout:
    for k in range(5):
        for n in range(9):
            fout.write('{} '.format(data[k * 9 + n]))
        fout.write('\n')
