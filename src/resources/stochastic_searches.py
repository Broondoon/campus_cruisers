"""
stochastic_searches.py

Code taken from other repos must follow their liscencing as well as be cited properly.

Bear!

"""

import random
import sys
sys.path.append("../src")
from util import data_types as dt

# Based on the randomized depth first search described here:
# https://en.wikipedia.org/wiki/Maze_generation_algorithm#Iterative_implementation_(with_stack)
#
def random_depth_first_search(starting_node : dt.Node, ending_node: dt.Node):
    # begin at the starting node
    node_list = [starting_node]
    visited = [starting_node.id]
    # main loop
    while len(node_list) > 0:
        # check if ending_node found
        if node_list[0].id == ending_node.id:
            break
        # get node_list[0] neighbours
        neighbours = node_list[0].get_neighbours()
        # check if visited
        next_node_options = []
        for node in neighbours:
            if visited.count(node.id) == 0:
                next_node_options.append(node)
        # at least one unvisited node
        if len(next_node_options) > 0:
            randpick = random.randint(0, len(next_node_options)-1)
            node_list.insert(0, next_node_options[randpick])
            visited.append(next_node_options[randpick].id)
        # all neighbours visited
        else:
            node_list.pop(0)
    # node_list contains a solution or is empty if ending_node not found
    # reverse before returning because it is backwards
    node_list.reverse()
    return node_list


def init_stochastic(start_node, end_node, pop_size):
    population = []

    for _ in range(pop_size):
        population.append(random_depth_first_search(start_node, end_node))

    return population