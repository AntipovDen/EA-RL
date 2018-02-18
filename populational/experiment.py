from math import log, e
from random import sample, randint
from matplotlib import pyplot as plt
from sys import argv, stdout

n = 1000
alpha = 0.9
gamma = 0.1
k = 4


class LearningAgent:
    def __init__(self, number_of_states, actions):
        self.Q = [{a: 0 for a in actions} for _ in range(number_of_states)]
        self.state = 0
        self.action = actions[0]

    def update(self, r, new_state):
        new_q = (1 - alpha) * self.Q[self.state][self.action] + alpha * (r + gamma * max(self.Q[new_state].values()))
        self.Q[self.state][self.action] = new_q
        self.state = new_state
        max_value = max(self.Q[self.state].values())
        self.action = sample([a for a in self.Q[self.state].keys() if self.Q[self.state][a] == max_value], 1)[0]
        return self.action


# note that we consider individuals not as binary vectors,
# but as an integer number of ones in this vector, it makes
# calculations much faster
class EvolutionaryAlgorithm:
    def __init__(self,
                 initial_population,
                 target_objective,
                 mutation_operator,
                 selection_operator_parents,
                 selection_operator_next_gen,
                 population_measure=None,
                 state_def=None):
        self.population = initial_population
        self.target_objective = target_objective
        self.mutate = mutation_operator
        self.select_parents = selection_operator_parents
        self.select_next_gen = lambda pop, aux_obj: selection_operator_next_gen(pop, aux_obj, self.target_objective) \
            if aux_obj is not None else selection_operator_next_gen(pop, self.target_objective)
        if population_measure is None:
            self.measure = lambda: sum(self.target_objective(x) for x in self.population) / len(self.population)
        else:
            self.measure = population_measure
        if state_def is None:
            self.state = lambda: max(self.target_objective(x) for x in self.population)
        else:
            self.state = state_def
        self.pop_measure = self.measure()

    def gen_offsprings(self):
        return [self.mutate(x) for x in self.select_parents(self.population)]

    def perform_iteration(self, aux_objective=None):
        self.population = self.select_next_gen(self.population + self.gen_offsprings(), aux_objective)
        r = self.measure() - self.pop_measure
        self.pop_measure += r
        return r, self.state()

    def run(self):
        state = self.state()
        iterations = 0
        while state != n:
            r, state = self.perform_iteration()
            iterations += 1
        return iterations


class EARL:
    def __init__(self, ea, rl):
        self.ea = ea
        self.rl = rl

    def run(self):
        iterations = 0
        aux_obj = self.rl.update(0, self.ea.state())
        while self.ea.state() != n:
            aux_obj = self.rl.update(*self.ea.perform_iteration(aux_obj))
            iterations += 1
        return iterations


# initial population
def init_pop(pop_size):
    return [sum([randint(0, 1) for _ in range(n)]) for _ in range(pop_size)]


# mutation operators
def mutation_rls(x):
    if randint(1, n) <= x:
        return x - 1
    return x + 1


def mutation_one_plus_one(x):
    y = x
    for i in range(n):
        y += (randint(1, n) == 1) * (1 - 2 * (i < x))
    return y


# objectives
def one_max(x):
    return x


def zero_max(x):
    return n - x


def xdivk(x):
    return x // k * k


# stopping criteria -- xdivk_mod(x) == n
def xdivk_mod(x):
    return n - k - ((n - x - 1) // k) * k


# selectors
# parent selector for (2 + 2)
def parent_selector_each_parent(population):
    return population


# offsprings selector for (2 + 2) with auxiliary objectives
def offspring_selector_one_best_plus_one_best(pop, obj1, obj2):
    max_obj1 = max(obj1(x) for x in pop)
    best_obj1_index = sample([i for i in range(len(pop)) if obj1(pop[i]) == max_obj1], 1)[0]
    max_obj2 = max(obj2(pop[i]) for i in range(len(pop)) if i != best_obj1_index)
    best_obj2_index = sample([i for i in range(len(pop)) if obj2(pop[i]) == max_obj2 and i != best_obj1_index], 1)[0]
    return [pop[best_obj1_index], pop[best_obj2_index]]


# offspring selector for (2 + 2)-EA without RL
def offspring_selector_two_best(pop, obj):
    return offspring_selector_one_best_plus_one_best(pop, obj, obj)


# offspring selector for (1 + 1) with auxiliary objectives
def offspring_selector_one_best(pop, obj1, _=None):
    max_obj = max(obj1(x) for x in pop)
    return sample([x for x in pop if obj1(x) == max_obj], 1)

if len(argv) == 1:
    print('Usage: python experiment.py [-t thread_number] [-r number_of_runs] [-a ea|earl|earlmod] [-m rls|sbm] '
          '[-e pop_size] [-p xdk|om|xdkom|xdkomzm|omzm]')

if '-t' in argv:
    thread_number = '_' + argv[argv.index('-t') + 1]
else:
    thread_number = ''

if '-r' in argv:
    runs = int(argv[argv.index('-r') + 1])
else:
    runs = 100

if '-a' in argv:
    algorithm = argv[argv.index('-a') + 1]
else:
    algorithm = 'ea'

if '-m' in argv and argv[argv.index('-m') + 1] == 'sbm':
    mutation_operator = mutation_one_plus_one
else:
    mutation_operator = mutation_rls

if '-e' in argv:
    pop_size = int(argv[argv.index('-e') + 1])
else:
    pop_size = 1

if '-p' in argv:
    problem = argv[argv.index('-p') + 1]
else:
    problem = 'xdk'
if 'xdk' in problem:
    target_obj = xdivk_mod  # xdk|om|xdkom|xdkomzm|omzm
    if 'zm' in problem:
        aux_obj = [xdivk_mod, one_max, zero_max]
    elif 'om' in problem:
        aux_obj = [xdivk_mod, one_max]
    else:
        aux_obj = [xdivk_mod]
else:
    target_obj = one_max
    aux_obj = [one_max, zero_max] if 'zm' in problem else [one_max]

if pop_size == 2:
    if 'rl' in algorithm:
        offspring_selector = offspring_selector_one_best_plus_one_best
    else:
        offspring_selector = offspring_selector_two_best
else:
    offspring_selector = offspring_selector_one_best

with open('{}_{}p{}_{}{}.txt'.format(algorithm, pop_size, pop_size, problem, thread_number), 'w') as f:
    for k in range(2, 5):
        for n in range(20, 101, 10):
            if 'rl' in algorithm:
                f.write('{:.2f} '.format(sum(EARL(EvolutionaryAlgorithm(init_pop(pop_size),
                                                                        target_obj,
                                                                        mutation_operator,
                                                                        parent_selector_each_parent,
                                                                        offspring_selector),
                                                  LearningAgent(n + 1, aux_obj)).run() / runs for _ in range(runs))))
                f.flush()
            else:
                f.write('{:.2f} '.format(sum(EvolutionaryAlgorithm(init_pop(pop_size),
                                                                   target_obj,
                                                                   mutation_operator,
                                                                   parent_selector_each_parent,
                                                                   offspring_selector).run() / runs for _ in range(runs))))
                f.flush()
        f.write('\n')


# with open('earl_opo.txt', 'w') as f:
#     k = 2
#     for n in range(20, 101, 10):
#         res = 0
#         for _ in range(runs):
#             ea = EvolutionaryAlgorithm(init_pop(1), xdivk_mod, mutation_rls, parent_selector_each_parent,
#                                        offspring_selector_one_best)
#             rl = LearningAgent(n + 1, [xdivk_mod, one_max])
#             res += EARL(ea, rl).run()
#         f.write('{} '.format(res / runs))

# with open('earl_tpt.txt', 'w') as f:
#     k = 2
#     for n in range(20, 101, 10):
#         res = 0
#         for _ in range(runs):
#             ea = EvolutionaryAlgorithm(init_pop(2), xdivk_mod, mutation_rls, parent_selector_each_parent,
#                                        offspring_selector_one_best_plus_one_best)
#             rl = LearningAgent(n + 1, [xdivk_mod, one_max])
#             res += EARL(ea, rl).run()
#         f.write('{} '.format(res / runs))
#
# with open('ea_opo.txt', 'w') as f:
#     k = 2
#     for n in range(20, 101, 10):
#         res = 0
#         for _ in range(runs):
#             res += EvolutionaryAlgorithm(init_pop(1), xdivk_mod, mutation_rls, parent_selector_each_parent,
#                                          offspring_selector_one_best).run()
#         f.write('{} '.format(res / runs))
#
#
# with open('ea_tpt.txt', 'w') as f:
#     k = 2
#     for n in range(20, 101, 10):
#         res = 0
#         for _ in range(runs):
#             res += EvolutionaryAlgorithm(init_pop(2), xdivk_mod, mutation_rls, parent_selector_each_parent,
#                                          offspring_selector_two_best).run()
#         f.write('{} '.format(res / runs))

# if argv[-1] == 'earl':
#     with open('earl_{}.txt'.format(thread_number), 'w') as f:
#         f.write('Average runtime of EA+RL on XdivK + OneMax over 100 runs. Lines: k in [2..6]. columns: n in [20..100], step = 10.\n')
#         for k in range(2, 7):
#             for n in range(20, 101, 10):
#                 f.write('{:.2f} '.format(sum(EARL().run() / runs for _ in range(runs))))
#                 f.flush()
#             f.write('\n')
# else:
#     with open('ea_opo{}.txt'.format(thread_number), 'w') as f:
#         f.write(
#             'Average runtime of (1 + 1)-EA on XdivK over 100 runs. Lines: k in [2..6]. columns: n in [20..100], step = 10.\n')
#         for k in range(2, 7):
#             for n in range(20, 101, 10):
#                 f.write('{:.2f} '.format(sum(EvolutionaryAlgorithm(rls_mutation, xdivk_mod).run_one_plus_one() / runs for _ in range(runs))))
#                 f.flush()
#             f.write('\n')




