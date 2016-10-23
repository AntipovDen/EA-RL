from math import log
from random import randint

def jump_nl(om, n, l):
    if om > l and om < n - l:
        return om
    if om == n:
        return n
    return 0

def rb_nl(om, n, l):
    if om >= n - l:
        return om
    return 0

def lb_nl(om, n, l):
    if om <= l:
        return om
    return 0



class Evolutionary_algorithm:
    def __init__(self, n, l, target_obj, restart_counter):
        self.n, self.l, self.target_obj, self.restart_counter = n, l, target_obj, restart_counter
        self.om = 0
        self.iterations = 0
        self.iterations_without_change = 0

    def iteration(self, objective):
        i = randint(0, self.n - 1)
        if i < self.om and objective(self.om) <= objective(self.om - 1):
            reward = self.target_obj(self.om - 1) - self.target_obj(self.om)
            self.om -= 1
        elif i >= self.om and objective(self.om) <= objective(self.om + 1):
            reward = self.target_obj(self.om + 1) - self.target_obj(self.om)
            self.om += 1
        else:
            reward = 0
            self.iterations_without_change += 1
            if self.iterations_without_change >= self.restart_counter:
                return 0, -self.iterations
        self.iterations += 1
        return reward, self.target_obj(self.om)

class Learning_agent:
    def __init__(self, n, l):
        self.q = [[[0, lambda om: rb_nl(om, n, l)],
                   [0, lambda om: jump_nl(om, n, l)],
                   [0, lambda om: lb_nl(om, n, l)]] for _ in range(n)]
        self.state = 0
        self.alpha = 0.8
        self.gamma = 0.2
        self.last_action = -1

    def modify(self, reward, new_state):
        self.q[self.state][self.last_action][0] = (1 - self.alpha) * self.q[self.state][self.last_action][0] + self.alpha * (reward + self.gamma * max([self.q[new_state][i][0] for i in range(3)]))
        self.state = new_state

    def select(self):
        m = max([self.q[self.state][i][0] for i in range(3)])
        indecies = [i for i in range(3) if self.q[self.state][i][0] == m]
        self.last_action = indecies[randint(0, len(indecies) - 1)]
        return self.q[self.state][self.last_action][1]


def run_without_restarts(n, l):
    ea = Evolutionary_algorithm(n, l, lambda om: jump_nl(om, n, l), 4.85 * n * (log(n) + 1))
    la = Learning_agent(n, l)
    while True:
        reward, state = ea.iteration(la.select())
        if state < 0:
            #restart
            if la.state == 0 and la.q[0][0][0] == 0 and la.q[0][1][0] == 0:
                print("restart after {} iterations on the 1st phase".format(-state))
            elif la.state != 0:
                if la.state != n - l - 1:
                    print("restart after {} iterations on the 2nd phase in the state {}".format(-state, la.state))
                elif la.q[0][1][0] > 0: #wrong function has been chosen
                    falls = int(la.q[n - l - 1][0][0] < 0 and  la.q[n - l - 1][2][0] < 0 + \
                            la.q[n - l - 1][0][0] < 0 or  la.q[n - l - 1][2][0] < 0)
                    print("restart after {} iterations on the 2nd phase in the end of the phase, {} falls detected, wrong function selected".format(-state, falls))
                elif la.q[n - l - 1][0][0] < 0 and  la.q[n - l - 1][2][0] < 0: #two fall backs before falling forward
                    print("restart after {} iterations on the 2nd phase in the end of the phase, 2 falls detected".format(-state))
            elif ea.om >= n - l:
                if la.q[0][1][0] > 0:
                    print("restart after {} iterations on the 3d phase, wrong function selected".format(-state))
                else:
                    print("restart after {} iterations on the 3d phase, appropriate function selected".format(-state))
            return False
        if state == n:
            print("Optimum found in {} iterations".format(ea.iterations))
            return True
        la.modify(reward, state)

def run(n, l):
    while not run_without_restarts(n, l):
        pass

for n in [10, 20, 100, 1000, 10000]:
    for l in [n // 2 - 1, n // 4, 1]:
        for run_number in range(100):
            print('Run n{}l{} number {}'.format(n, l, run_number + 1))
            run(n, l)
            print()
