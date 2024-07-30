"""
parent_selection.py


"""
import random

# Tournament hosting
# Input: a subset of of Solutions, and a fitness method
# Output: the winning Solution
def trial_by_combat(soln_subset):
    return min(soln_subset, key = lambda soln: soln.get_fitness())

# Tournament selection
def select_parents(generation, subset_size):
    aspirants = generation[:]
    parents = []
    num_tournaments = len(generation) // subset_size

    print("> Tournament begins! Players:", aspirants, "\n")

    for _ in range(num_tournaments):
        subset = random.sample(aspirants, subset_size)
        aspirants = [soln for soln in aspirants if soln not in subset]

        print("> Remaining aspirants:", aspirants, "\n")
        
        winner = trial_by_combat(subset)
        parents.append(winner)

    return parents

# Input: list of solutions
# Output: list of tuples containing paired parents
def mix_n_mingle(parents):
    singles = parents[:]
    matches = []

    if len(singles) % 2 == 1:
        print("!!!\n!!! ERRR - Odd number of parents in the mix-n-mingle! Bad.\n!!!")
        return -1

    while len(singles) > 0:
        
        soln_a = singles.pop(random.randrange(len(singles)))
        soln_b = singles.pop(random.randrange(len(singles)))

        matches.append((soln_a, soln_b))

    print("Pairs:", matches)
    return matches