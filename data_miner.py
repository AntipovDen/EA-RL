# we need to find:
# - mean number of restarts
# - mean number of iterations for the run with restart
# - percentage of the reasons of restart (1st phase, 2nd phase, wrong function, 2 falls, 3d phase)
# - mean number of iterations for the run without restart
# - mean total runtime
from math import log, e

TF = 'two falls'
WF = 'wrong_function'


class Run:
    def __init__(self, param_string):
        st = param_string.split()
        if st[0] == 's':
            self.restart = False
            self.iterations = int(st[1])
        else:
            self.restart = True
            self.last_phase = int(st[1])
            self.iterations = int(st[3])
            self.last_state = int(st[5])
            if self.last_phase == 2:
                if int(st[7]) == 2:
                    self.reason = TF
                elif st[-1] == 'wf':
                    self.reason = WF
                else:
                    self.reason = None
            else:
                self.reason = None


class GlobalRun:
    def __init__(self):
        self.runs = []

    def runtime(self):
        return sum([i.iterations for i in self.runs])

files = ['data/experiment{}.out'.format(i) for i in range(1, 11)]
runs = {n: {n // 2 - 1: [], n // 4: [], 1: []} for n in [10, 20, 100, 1000, 10000]}

for file in files:
    with open(file, 'r') as f:
        while True:
            s = f.readline()
            if s == '':
                break
            s = s.split()
            n, l = int(s[1]), int(s[3])
            global_run = GlobalRun()
            while True:
                s = f.readline()
                if s == '':
                    break
                run = Run(s)
                global_run.runs.append(run)
                if not run.restart:
                    break
            runs[n][l].append(global_run)
            s = f.readline()


for n in [10, 20, 100, 1000, 10000]:
    for l in [n // 2 - 1, n // 4, 1]:
        if l == n // 2 - 1:
            print("\multirow{{3}}{{*}}{{{}}} & {} & ".format(n, l), end='')
        else:
            print(" & {} & ".format(l), end='')

        # count mean restarts for each n and l:
        c = 3.85
        p_restart = (1 - e ** (-c)) * (1 - e ** (- 2 * c / 3 + 1 / 3)) * (1 - (n - l - 1) ** 2 / n ** 2) * (
            1 - e ** (-c) / n ** (c + 1)) / 3 ** (5 / log(n))
        restarts = 1/p_restart - 1
        print("{0:.2f} ({1:.2f}) & ".format(sum([len(gb.runs) - 1 for gb in runs[n][l]]) / len(runs[n][l]), restarts), end='')

        # count mean number of ierations in the restarted run:
        s = 0
        r = 0
        for gb in runs[n][l]:
            r += len(gb.runs) - 1
            for run in gb.runs[:-1]:
                s += run.iterations

        # reasons of restart:
        p1, p2, p3, tf, wf = 0, 0, 0, 0, 0
        for gb in runs[n][l]:
            for run in gb.runs[:-1]:
                if run.last_phase == 1:
                    p1 += 1
                elif run.last_phase == 2:
                    if run.reason is None:
                        p2 += 1
                    elif run.reason == TF:
                        tf += 1
                    else:
                        wf += 1
                else:
                    p3 += 1
        # print("Restarts:")
        # print("Phase 1: {}".format(p1 * 100/r))
        # print("Phase 2: {}".format(p2 * 100/r))
        # print("Two fal: {}".format(tf * 100/r))
        print("{0:.2f} & ".format(wf * 100/r), end='')
        # print("Phase 3: {}".format(p3 * 100/r))
        tr = 3 * n * (log(l) + 1) / 2 + 5 * n * log((n - l) / (l + 1)) + 3 * n + 4.85 * n * (log(n) + 1)
        print("{0:.2f} ({1:.2f})& ".format(s / r, tr), end='')

        # count mean number of ierations in the run without restart:
        ts = 5 * n * (log(l) + 1) / 2 + 5 * n * log((n - l) / (l + 1)) + n
        print("{0:.2f} ({1:.2f})& ".format(sum([gb.runs[-1].iterations for gb in runs[n][l]]) / len(runs[n][l]), ts), end='')

        # mean total runtime
        print("{0:.2f} ({1:.2f}) \\\\ ".format(sum([gb.runtime() for gb in runs[n][l]]) / len(runs[n][l]), (restarts * tr + ts)), end='')

        if l == 1:
            print('\hline')
        elif n == 10000 and l == 2500:
            print('\hline')
            exit(0)
        else:
            print('\cline{2-7}')
