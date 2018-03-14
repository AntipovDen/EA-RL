from scipy.stats import wilcoxon

with open('data/earl_2p2n_xdkom_merged.log', 'r') as f:
    lines = f.readlines()

# with open('data/earl_2p2n_xdkom_merged.log', 'r') as f:
#     xdkomzm_lines = f.readlines()

l1 = [l.split()[:400] for l in lines]
l2 = [l.split()[400:] for l in lines]

for i in range(45):
    print('n {} k {}\t{}'.format((i % 9) * 10 + 20, i // 9 + 2, wilcoxon([int(s) for s in l2[i]],#xdkom_lines[i].split()],
             [int(s) for s in l1[i]], correction=True).pvalue))# xdkomzm_lines[i].split()]).pvalue))