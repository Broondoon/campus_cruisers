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

