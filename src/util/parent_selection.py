"""
parent_selection.py


"""
import random
from . import data_types as dt
# Tournament hosting
# Input: a subset of of Solutions, and a fitness method
# Output: the winning Solution
def trial_by_combat(soln_subset : list[dt.Solution]):
    print("\n\n >>> Soln:   ", soln_subset)
    return min(soln_subset, key = lambda soln: soln.get_fitness())

# Tournament selection
def select_parents(generation : "list[dt.Solution]", subset_size : int):
    aspirants = generation[:]
    parents = []
    num_tournaments = len(generation) // subset_size

    print("> Tournament begins! Players:", len(aspirants), "\n")

    for i in range(num_tournaments):
        subset = [] # random.sample(aspirants, subset_size)
        for _ in range(subset_size):
            subset.append(aspirants.pop(random.randrange(len(aspirants))))

        print("Iter:", i, "Subset size:", len(subset))

        # aspirants = [soln for soln in aspirants if soln not in subset]

        print("> Remaining aspirants:", len(aspirants), "\n")
        
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