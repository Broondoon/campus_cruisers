"""
population_init.py

Handles generating the inital population of solutions. Initially, it should just use one algo. Potentially it could do more, if we get the time.

"""
from . import data_types as dt
from random import sample as random_sample
# from .. import resources

def init_pop(start_node : dt.Node, end_node : dt.Node, pop_size : int) -> "list[dt.Solution]":
    population = []

    for _ in range(pop_size):
        pass #population.append(resources.random_depth_first_search(start_node, end_node))

    return population
    

def debug_init_pop(gen_size):
    generation = []

    for _ in range(gen_size):
        nodes = [dt.topography.all_nodes[9]]

        nodes += random_sample(nodes[0].get_neighbours(), 1)
        nodes += random_sample(nodes[1].get_neighbours(), 1)

        soln = dt.Solution(nodes)
        generation.append(soln)

    return generation