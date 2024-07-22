""" For ECE 470 group project. Summer 2024. """

# Takes a solution object and evaluates its fitness.
def fitness(potential_solution, lookup_table):
    # variables used in calculation
    running_sum = 0
    prev = None
    # loop through nodes in solution
    for node in potential_solution.nodes:
        # add distance from the previous node
        if prev:
            running_sum += lookup_table[prev.id][node.id]
        # set the previous node to the current node
        prev = node
    # prepare answer
    total_distance = running_sum
    # consider if we want to represent as a ratio to straight line distance
    # return the calculated finess
    answer = total_distance
    return answer

"""
Scratchwork:

terminate on 5 rounds of no change (stagnation limit)
max deviation = 2m (max_dev)

[82m, 83m, 84m, 82m, 83m] <--- best fitness from previous gen
standard deviation? There's definitely a math.py function to quick calc
"""

# Input: list of solutions (curr_generation), fitness history, max rounds of no change before term, max deviation
# Ex: check_terminate([92m, 83m, 88m, 86m], ,82m, 83m, 84m, 82m, 83m], 5, 2)
# Output: bool
def check_terminate(curr_generation, fitness_history, stagnation_limit, max_dev):
    pass

    # best_soln = curr_generation.max <-- there's definitely a python function to grab biggest #

