from math import log, e
from random import sample, randint
# from matplotlib import pyplot as plt
from sys import argv, stdout

n = 60
alpha = 0.9
gamma = 0.1
k = 5


class LearningAgent:
    def __init__(self, number_of_states, actions):
        self.Q = [{a: 0 for a in actions} for _ in range(number_of_states)]
        self.state = 0
        self.action = actions[0]

    def update(self, r, new_state):
        # We should multiply Q by (1 - alpha) factor, however we do not do it to avoid oblivion
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
                 lam=1,  # number of offsprings that we create on every iteration from each parent
                 mod=False,
                 population_measure=None,
                 state_def=None):
        self.population = initial_population
        self.lam = lam
        self.offsprings = [None] * (len(initial_population) * lam)
        self.target_objective = target_objective
        self.mutate = mutation_operator
        self.select_parents = selection_operator_parents
        self.select_next_gen = lambda pop, aux_obj: selection_operator_next_gen(pop, aux_obj, self.target_objective) \
            if aux_obj is not None else selection_operator_next_gen(pop, self.target_objective)
        if population_measure is None:
            self.measure = lambda pop: sum(self.target_objective(x) for x in pop) / len(pop)
        else:
            self.measure = population_measure
        if state_def is None:
            self.state = lambda: max(self.target_objective(x) for x in self.population)
        else:
            self.state = state_def
        self.pop_measure = self.measure(self.population)
        self.mod = mod

    def gen_offsprings(self):
        j = 0
        for x in self.select_parents(self.population):
            for i in range(self.lam):
                self.offsprings[j] = self.mutate(x)
                j += 1
        return self.offsprings

    def perform_iteration(self, aux_objective=None):
        pop = self.select_next_gen(self.population + self.gen_offsprings(), aux_objective)
        r = self.measure(pop) - self.pop_measure
        if not self.mod or r >= 0:
            self.population = pop
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

    def tracked_run(self):
        target_values = {xdivk_mod(x) for x in range(n)}
        plateau_runtimes = {x: 0 for x in target_values}
        plateau_learning = {x: None for x in target_values}
        aux_obj = self.rl.update(0, self.ea.state())

        current_plateau = self.ea.state()
        current_plateau_learned = False

        while current_plateau != n:
            aux_obj = self.rl.update(*self.ea.perform_iteration(aux_obj))
            plateau_runtimes[current_plateau] += 1
            if not current_plateau_learned:
                if max(map(abs, self.rl.Q[current_plateau].values())) > 0 and current_plateau == self.ea.state():
                    plateau_learning[current_plateau] = [obj.__name__ for obj, q in self.rl.Q[current_plateau].items() if q > 0]
                    current_plateau_learned = True
            else:
                if max(map(abs, self.rl.Q[current_plateau].values())) == 0 and plateau_learning[current_plateau][-1] != 'OBLIVION':
                    plateau_learning[current_plateau].append('OBLIVION')

            if self.ea.state() > current_plateau:
                current_plateau_learned = False
                current_plateau = self.ea.state()

        # for plateau in sorted(list(target_values)):
        #     print('{}\t{}\t{}'.format(plateau, plateau_runtimes[plateau], plateau_learning[plateau]))

        return plateau_runtimes, plateau_learning

    def logged_run(self, file):
        iterations = 0
        aux_obj = self.rl.update(0, self.ea.state())
        current_state = self.ea.state()

        while current_state != n:
            file.write('iteration:  {}\n'.format(iterations))
            file.write('parents:    {} {}\n'.format(*self.ea.population))
            file.write('objective:  {}\n'.format(aux_obj.__name__))
            file.write('Q:          {}\n'.format(' '.join(['{}--{}'.format(f.__name__, q) for f, q in self.rl.Q[self.ea.state()].items()])))
            aux_obj = self.rl.update(*self.ea.perform_iteration(aux_obj))
            file.write('offsprings: {}\n'.format(sorted(self.ea.offsprings)))
            if current_state != self.ea.state():
                file.write(''.join(['-'] * 100))
                file.write('\n')
                current_state = self.ea.state()
            else:
                file.write('\n')
            iterations += 1




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

n = 80
k = 6
with open('earl_2p2n_xdkom_run.log', 'w') as f:
    EARL(EvolutionaryAlgorithm(init_pop(2),
                               xdivk_mod,
                               mutation_rls,
                               parent_selector_each_parent,
                               offspring_selector_one_best_plus_one_best,
                               lam=n,
                               mod=False),
         LearningAgent(n + 1, [xdivk_mod, one_max])).logged_run(f)
exit()

runs = 1000
for k in range(2, 7):
    for n in range(80, 81, 10):
        target_values = {xdivk_mod(x) for x in range(n)}
        plateau_runtimes = {x: {'None': 0, 'xdivk_mod': 0, 'one_max': 0, 'xdivk_mod_OBLIVION': 0, 'one_max_OBLIVION': 0} for x in target_values}
        plateau_learning = {x: {'None': 0, 'xdivk_mod': 0, 'one_max': 0, 'xdivk_mod_OBLIVION': 0, 'one_max_OBLIVION': 0} for x in target_values}

        for _ in range(runs):
            res_runtimes, res_learnings = EARL(EvolutionaryAlgorithm(init_pop(2),
                                                                     xdivk_mod,
                                                                     mutation_rls,
                                                                     parent_selector_each_parent,
                                                                     offspring_selector_one_best_plus_one_best,
                                                                     lam=n,
                                                                     mod=False),
                                               LearningAgent(n + 1, [xdivk_mod, one_max])).tracked_run()
            for x in target_values:
                result = 'None' if res_learnings[x] is None else '_'.join(res_learnings[x])
                plateau_runtimes[x][result] += res_runtimes[x]
                plateau_learning[x][result] += 1
        for x in target_values:
            for key in plateau_runtimes[x].keys():
                plateau_runtimes[x][key] /= max(1, plateau_learning[x][key])

        objectives = list(plateau_runtimes[n - k].keys())
        print('Plateau ' + ''.join([s.ljust(20) for s in objectives]))
        for plateau in sorted(list(target_values)):
            print(str(plateau).ljust(8), end='')
            for obj in objectives:
                print('{}{}'.format('{:.2f}'.format(plateau_runtimes[plateau][obj]).ljust(12), str(plateau_learning[plateau][obj]).ljust((8))), end='')
            print()
exit(0)


if '-h' in argv or '-help' in argv:
    print('Usage: python experiment.py [-t thread_number] [-r number_of_runs] [-a ea|earl|earlmod] [-m rls|sbm] '
          '[-e pop_size] [-l offsprings_size|n] [-p xdk|om|xdkom|xdkomzm|omzm]')
    exit(0)

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

if '-l' in argv:
    lam = argv[argv.index('-l') + 1]
    lambda_flag = lam == 'n'
    if not lambda_flag:
        lam = int(lam)
else:
    lambda_flag = False
    lam = 1


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

with open('{}_{}p{}_{}{}.log'.format(algorithm, pop_size, str(pop_size) + 'n' if lambda_flag else lam * pop_size,
                                     problem, thread_number), 'w') as f:
    for k in range(2, 7):
        for n in range(20, 101, 10):
            f.write('n {} k {}\n'.format(n, k))
            if lambda_flag:
                lam = n
            if 'rl' in algorithm:
                for _ in range(runs):
                    f.write('{}\n'.format(EARL(EvolutionaryAlgorithm(init_pop(pop_size),
                                                                     target_obj,
                                                                     mutation_operator,
                                                                     parent_selector_each_parent,
                                                                     offspring_selector,
                                                                     lam,
                                                                     mod='mod' in algorithm),
                                               LearningAgent(n + 1, aux_obj)).run()))
                    f.flush()
            else:
                for _ in range(runs):
                    f.write('{}\n'.format(EvolutionaryAlgorithm(init_pop(pop_size),
                                                                target_obj,
                                                                mutation_operator,
                                                                parent_selector_each_parent,
                                                                offspring_selector,
                                                                lam).run()))
                    f.flush()

