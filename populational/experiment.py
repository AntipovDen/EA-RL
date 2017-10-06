from math import log
from random import sample, randint
# from matplotlib import pyplot as plt
from sys import argv, stdout

n = 1000
alpha = 0.9
gamma = 0.1
k = 4

class LearningAgent:
    def __init__(self, number_of_states, actions, track_rl=False):
        self.Q = [{a: 0 for a in actions} for _ in range(number_of_states)]
        self.state = 0
        self.action = actions[0]
        # to see, how much learned states there are
        self.tracking = track_rl
        if track_rl:
            self.learning_track = [0]
        else:
            self.learning_track = None

    def recalculate_quality(self, r, new_state):
        new_q = (1 - alpha) * self.Q[self.state][self.action] + alpha * (r + gamma * max(self.Q[new_state].values()))

        if self.tracking:
            if self.action == zero_max and new_q < 0 and self.Q[self.state][self.action] >= 0:
                self.learning_track.append(self.learning_track[-1] + 1)
            else:
                self.learning_track.append(self.learning_track[-1])

        self.Q[self.state][self.action] = new_q
        self.state = new_state
        max_value = max(self.Q[self.state].values())
        self.action = sample([a for a in self.Q[self.state].keys() if self.Q[self.state][a] == max_value], 1)[0]
        return self.action

    # just for debug purposes
    def print_q(self):
        actions = list(self.Q[0].keys())
        for a in actions:
            print('{: <10}'.format(a.__name__), end='')
        print()

        for state in self.Q:
            for a in actions:
                print('{:3.5f} '.format(state[a]), end='')
            print()

    def get_learning_track(self):
        return self.learning_track


# note that we consider individuals not as binary vectors,
# but as an integer number of ones in this vector, it makes
# calculations much faster
class EvolutionaryAlgorithm:
    def __init__(self, mutation_operator, target_objective):
        self.population = [gen_individual(), gen_individual()]
        self.mutate = mutation_operator
        self.target_objective = target_objective

    def get_state(self):
        return max(self.target_objective(x) for x in self.population)

    def get_population(self):
        return self.population

    def get_distance(self):
        return max(self.population) - min(self.population)

    def perform_iteration(self, aux_objective):
        # to calculate reward after the iteration
        r0 = sum(self.target_objective(x) for x in self.population)
        # creating children
        self.population += [self.mutate(x) for x in self.population]
        # finding the individual with the best auxiliary objective value and moving it into new population
        max_aux_value = max(aux_objective(x) for x in self.population)
        next_population = sample([x for x in self.population if aux_objective(x) == max_aux_value], 1)
        self.population.remove(next_population[0])
        # finding the individual with the best target objective among individuals that left in the population
        max_target_value = max(self.target_objective(x) for x in self.population)
        next_population += sample([x for x in self.population if self.target_objective(x) == max_target_value], 1)
        self.population = next_population
        # returning reward and new state
        return sum(self.target_objective(x) for x in self.population) - r0, max(self.target_objective(x) for x in self.population)

    def run(self):
        iterations = 0
        while True:
            self.population += [self.mutate(x) for x in self.population]
            max_value = max(self.target_objective(x) for x in self.population)
            if max_value == n:
                return iterations
            if len([x for x in self.population if self.target_objective(x) == max_value]) == 1:
                second_max = max(self.target_objective(x) for x in self.population if self.target_objective(x) != max_value)
                self.population = [x for x in self.population if self.target_objective(x) == max_value] + sample([x for x in self.population if self.target_objective(x) == second_max], 1)
            else:
                self.population = sample([x for x in self.population if self.target_objective(x) == max_value], 2)
            iterations += 1


class EARL:
    def __init__(self, track_state=False, track_distance=False):
        self.evolutionary_algorihm = EvolutionaryAlgorithm(rls_mutation, xdivk_mod)
        self.learning_agent = LearningAgent(n + 1, [xdivk_mod, one_max])
        # wether we should track the current state, or just count the number of iterations
        self.state_tracking = track_state
        self.distance_tracking = track_distance

    def run(self):
        aux_obj = self.learning_agent.recalculate_quality(0, self.evolutionary_algorihm.get_state())
        if self.state_tracking:
            states = []
        else:
            iterations = 0
        if self.distance_tracking:
            distances = []
        while True:
            reward, state = self.evolutionary_algorihm.perform_iteration(aux_obj)
            if self.state_tracking:
                states.append(state)
            else:
                iterations += 1
            if self.distance_tracking:
                distances.append(self.evolutionary_algorihm.get_distance())
            if state == n:
                if self.distance_tracking:
                    if self.state_tracking:
                        return states, distances
                    return iterations, distances
                if self.state_tracking:
                    return states
                return iterations
            aux_obj = self.learning_agent.recalculate_quality(reward, state)

    def get_learning_track(self):
        return self.learning_agent.get_learning_track()

    def print_q(self):
        self.learning_agent.print_q()




def gen_individual():
    s = 0
    for i in range(n):
        if randint(0, 1):
            s += 1
    return s


def rls_mutation(x):
    if randint(1, n) <= x:
        return x - 1
    return x + 1


def one_max(x):
    return x


def zero_max(x):
    return n - x



def xdivk(x):
    return x // k * k


# stopping criteria -- xdivk_mod(x) == n
def xdivk_mod(x):
    return n - k - ((n - x - 1) // k) * k



if len(argv) <= 1:
    thread_number = ''
else:
    thread_number = argv[1]

if len(argv) <= 2:
    runs = 100
else:
    try:
        runs = int(argv[2])
    except ValueError:
        runs = 100

# n = 20
# k = 3
# for _ in range(10):
#     print(EvolutionaryAlgorithm(rls_mutation, xdivk_mod).run())
# exit(0)


if argv[-1] == 'earl':
    with open('earl_{}.txt'.format(thread_number), 'w') as f:
        f.write('Average runtime of EA+RL on XdivK + OneMax over 100 runs. Lines: k in [2..6]. columns: n in [20..100], step = 10.\n')
        for k in range(2, 7):
            for n in range(20, 101, 10):
                print(n , k)
                f.write('{:.2f} '.format(sum(EARL().run() / runs for _ in range(runs))))
                f.flush()
            f.write('\n')
else:
    with open('ea_{}.txt'.format(thread_number), 'w') as f:
        f.write(
            'Average runtime of (2 + 2)-EA on XdivK over 100 runs. Lines: k in [2..6]. columns: n in [20..100], step = 10.\n')
        for k in range(2, 7):
            for n in range(20, 101, 10):
                print(n, k)
                f.write('{:.2f} '.format(sum(EvolutionaryAlgorithm(rls_mutation, xdivk_mod).run() / runs for _ in range(runs))))
                f.flush()
            f.write('\n')




