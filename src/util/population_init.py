"""
population_init.py

Handles generating the inital population of solutions. Initially, it should just use one algo. Potentially it could do more, if we get the time.

"""
from . import data_types as dt
from random import sample as random_sample

def init_pop():
    # call methods within /resources
    # return a list of Solution objects (i.e. a Generation)
    pass

def debug_init_pop(gen_size):
    generation = []

    for _ in range(gen_size):
        nodes = [dt.topography.all_nodes[9]]

        nodes += random_sample(nodes[0].get_neighbours(), 1)
        nodes += random_sample(nodes[1].get_neighbours(), 1)

        soln = dt.Solution(nodes)
        generation.append(soln)

    return generation