from math import log
from random import randint, choice, randrange
from time import time

MIN = 2.2250738585072014e-308


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


def sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    return 0


class Evolutionary_algorithm:
    def __init__(self, n, l, target_obj, restart_counter):
        self.n, self.l, self.target_obj, self.restart_counter = n, l, target_obj, restart_counter
        self.om = 0
        self.iterations = 0
        self.iterations_without_change = 0

    def iteration(self, objective):
        global t1_2
        t= time()
        i = randrange(self.n)
        obj = objective(self.om)
        if i < self.om and obj <= objective(self.om - 1):
            reward = self.target_obj(self.om - 1) - self.target_obj(self.om)
            self.iterations_without_change = 0
            self.om -= 1
        elif i >= self.om and obj <= objective(self.om + 1):
            reward = self.target_obj(self.om + 1) - self.target_obj(self.om)
            self.iterations_without_change = 0
            self.om += 1
        else:
            reward = 0
            self.iterations_without_change += 1
            if self.iterations_without_change >= self.restart_counter:
                return 0, -self.iterations
        self.iterations += 1
        t1_2 += time() - t
        return reward, self.target_obj(self.om)

    def clear(self):
        self.om = 0
        self.iterations = 0
        self.iterations_without_change = 0


class Learning_agent:
    def __init__(self, n, l):
        self.q = [[[0, lambda om: rb_nl(om, n, l)],
                   [0, lambda om: jump_nl(om, n, l)],
                   [0, lambda om: lb_nl(om, n, l)]] for _ in range(n)]
        self.state = 0
        self.alpha = 0.8
        self.gamma = 0.2
        self.last_action = -1
        self.choice_array = [0, 0, 0]
        self.candidates = 0

    def modify(self, reward, new_state):
        if reward != 0 or new_state != self.state:
            self.q[self.state][self.last_action][0] = (1 - self.alpha) * self.q[self.state][self.last_action][0] + self.alpha * (reward + self.gamma * max([self.q[new_state][i][0] for i in range(3)]))
            self.state = new_state
        else:
            self.q[self.state][self.last_action][0] = max(MIN, (1 - self.alpha * (1 - self.gamma)) * abs(self.q[self.state][self.last_action][0])) * sign(self.q[self.state][self.last_action][0])

    def select(self):
        global t1_1
        t = time()
        m = max(self.q[self.state][0][0], self.q[self.state][1][0], self.q[self.state][2][0])
        if self.q[self.state][0][0] == m:
            self.choice_array[self.candidates] = 0
            self.candidates += 1
        if self.q[self.state][1][0] == m:
            self.choice_array[self.candidates] = 1
            self.candidates += 1
        if self.q[self.state][2][0] == m:
            self.choice_array[self.candidates] = 2
            self.candidates += 1
        self.last_action = self.choice_array[randrange(self.candidates)]
        self.candidates = 0
        t1_1 += time() - t
        return self.q[self.state][self.last_action][1]

    def clear(self):
        for state in self.q:
            for action in state:
                action[0] = 0
        self.state = 0
        self.last_action = -1


t1_1 = 0
t1_2 = 0
t2 = 0
t3 = 0

def run_without_restarts(n, l):
    global ea, la, t2, t3
    while True:
        reward, state = ea.iteration(la.select())
        t = time()
        if state < 0:
            #restart
            if la.state == 0 and la.q[0][0][0] == 0 and la.q[0][1][0] == 0:
                print("r 1 i {}".format(-state)) #restart on the first phase
            elif la.state != 0:
                if la.state != n - l - 1:
                    print("r 2 i {} s {}".format(-state, la.state)) #restart during the second phase
                elif la.q[0][1][0] > 0: #wrong function has been chosen
                    falls = int(la.q[n - l - 1][0][0] < 0 and  la.q[n - l - 1][2][0] < 0 + \
                            la.q[n - l - 1][0][0] < 0 or  la.q[n - l - 1][2][0] < 0)
                    print("r 2 i {} s {} f {} wf".format(-state, n - l - 1, falls))
                elif la.q[n - l - 1][0][0] < 0 and  la.q[n - l - 1][2][0] < 0: #two fall backs before falling forward
                    print("r 2 i {} s {} f 2".format(-state, n - l - 1))
            elif ea.om >= n - l:
                if la.q[0][1][0] > 0:
                    print("r 3 i {} wf".format(-state))
                else:
                    print("r 3 i {}".format(-state))
            return False
        if state == n:
            print("s {} ".format(ea.iterations))
            return True
        t2 += time() - t
        t = time()
        la.modify(reward, state)
        t3 += time() - t

def run(n, l):
    global ea, la, t1_1, t1_2, t2, t3
    while not run_without_restarts(n, l):
        ea.clear()
        la.clear()
        print(t1_1, t1_2, t2, t3)
        t1_1 = t1_2 = t2 = t3 = 0


n = 10000
l = 1

ea = Evolutionary_algorithm(n, l, lambda om: jump_nl(om, n, l), 4.85 * n * (log(n) + 1))
la = Learning_agent(n, l)
for run_number in range(1000):
    print('n {} l {} r {}'.format(n, l, run_number + 1))
    run(n, l)
    print()
