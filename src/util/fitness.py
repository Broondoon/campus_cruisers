"""
fitness.py

Contains the fitness function and terminating condition methods for our genetic algorithm.

For ECE 470 group project. Summer 2024.
"""
from . import data_types as dt


# Moved to data_types.py
"""
# Takes a solution object and evaluates its fitness.
# Input: solution object of potential solution, the lookup_table
# Output: the total distance from start to end of the path
def fitness_check(potential_solution: dt.Solution, lookup_table):
    # variables used in calculation
    running_sum = 0
    prev = None
    # loop through nodes in solution
    for node in potential_solution.nodes:
        # add distance from the previous node
        if prev:
            running_sum += lookup_table.array[prev.id][node.id]
        # set the previous node to the current node
        prev = node
    # prepare answer
    total_distance = running_sum

    # return the calculated finess
    return total_distance
"""


# Checks if the algorithm should terminate now.
# Input: fitness history, max rounds of no change before term, max deviation
# Ex: check_terminate([82m, 83m, 84m, 82m, 83m], 5, 2)
# Output: bool
def check_terminate(fitness_history, stagnation_limit, max_dev):
    # check history length
    if len(fitness_history) < stagnation_limit:
        # algorithm has not run long enough to terminate
        return False
    # assign true
    should_terminate = True
    # get most recent value
    latest_val = fitness_history[0]
    # compare to values up to limit
    for i in [1, stagnation_limit-1]:
        # check if difference is more then accepted deviation
        if abs(latest_val - fitness_history[i]) > max_dev:
            # assign false 
            should_terminate = False
    # return false if more than max deviation within the generation number limit
    # return true otherwise
    return should_terminate


# Adds the current best solution to the solution history. Do before calling check_terminate.
# Input: list of solutions fitnesses, list of previous best solutions
# Output: an updated list of previous best solutions
def add_to_history(curr_generation, fitness_history):
    # get the best value from the current generation
    new_best = min(curr_generation)
    # add the best value to the start of the history list
    fitness_history.insert(0, new_best)
    # return the history list
    return fitness_history

