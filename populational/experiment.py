from random import sample, randint

n = 10
alpha = 0.9
gamma = 0.1


class LearningAgent:
    def __init__(self, number_of_states, actions):
        self.Q = [{a: 0 for a in actions} for _ in range(number_of_states)]
        self.state = 0
        self.action = None

    def recalculate_quality(self, r, new_state):
        self.Q[self.state][self.action] = (1 - alpha) * self.Q[self.state][self.action] + alpha * (r + gamma * max(self.Q[new_state].values()))
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

    def perform_iteration(self, aux_objective):
        # to calculate reward after the iteration
        r0 = sum(self.target_objective(x) for x in self.population)
        # creating children
        self.population += [self.mutate(x) for x in self.population]
        # finding the individual with the best auxiliary objective value and moving it into new population
        max_aux_value = max(aux_objective(x) for x in self.population)
        next_population = sample([x for x in self.population if aux_objective(x) == max_aux_value])
        self.population.remove(next_population[0])
        # finding the individual with the best target objective among individuals that left in the population
        max_target_value = max(self.target_objective(x) for x in self.population)
        next_population += sample([x for x in self.population if self.target_objective(x) == max_target_value])
        self.population = next_population
        # returning reward and new state
        return sum(self.target_objective(x) for x in self.population) - r0, max(self.target_objective(x) for x in self.population)


class EARL:
    def __init__(self):
        self.evolutionary_algorihm = EvolutionaryAlgorithm(rls_mutation, one_max)
        self.learning_agent = LearningAgent(n + 1, [one_max, zero_max])

    def run(self):
        aux_obj = self.learning_agent.recalculate_quality(0, self.evolutionary_algorihm.get_state())




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


la = LearningAgent(n, [one_max, zero_max], n // 2)
la.print_q()

print(la.choose_criteria().__name__)
la.get_reward(1, n // 2 + 1)
la.print_q()

print(la.choose_criteria().__name__)
la.get_reward(-1, n // 2)
la.print_q()