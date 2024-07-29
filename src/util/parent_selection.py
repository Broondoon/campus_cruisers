"""
parent_selection.py


"""
import random

# Tournament hosting
# Input: a subset of of Solutions, and a fitness method
# Output: the winning Solution
def host_tournament(soln_subset, fitness_method):
    return min(soln_subset, key = fitness_method)

# Tournament selection
def select_parents(generation, subset_size, fitness_method):
    aspirants = generation[:]
    parents = []
    num_tournaments = len(generation) // subset_size

    for _ in range(num_tournaments):
        subset = random.sample(aspirants, subset_size)
        aspirants = [soln for soln in aspirants if soln not in subset]
        
        winner = host_tournament(subset, fitness_method)
        parents.append(winner)

    return parents

# Input: list of solutions
# Output: list of tuples containing paired parents
def mix_n_mingle(parents):
    singles = parents[:]
    while len(parents)