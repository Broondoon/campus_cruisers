"""
combine_solns.py

Contains methods for crossover and mutation.

"""
import random
from . import data_types as dt

# Input: a Solution object, an int representing /100 odds to mutate
# Output: a pair of Node IDs, the first being the one to replace, and the second being the replacement
def select_mutation(soln, odds):
    
    if (odds > 100) or (odds < 0):
        print("Err - invalid odds; must be within 0-100")
        return None
    
    nodes = soln.nodes
    could_mutate = []
    # Range is funky so as to skip mutating the first and last nodes
    for i in range(1, len(nodes) - 1):
        i_neighbours = nodes[i].get_neighbours()

        options = []
        for neighbour in i_neighbours:
            if nodes[i-1] in neighbour.get_neighbours() and nodes[i+1] in neighbour.get_neighbours():
                options.append(neighbour)

        if len(options) > 0:
            could_mutate.append((i, options))

    # Don't roll the dice if there's nothing to mutate
    if len(could_mutate) == 0:
        return None

    # Reminder: [0] is the id of the node to replace
    # [1] is the list of options to replace it with

    # Randomly choose (potentially more than 1, but k = 1 rn so only one)
    node_to_mutate = random.choices(could_mutate, weights=((odds) * len(could_mutate)), k = 1)

    print(">> Debug - List of nodes to mutate:", node_to_mutate)

    # replacement_node is a Node object
    replacement_node = node_to_mutate[1][random.randrange(0, len(node_to_mutate[1]))]

    # Returns the id of the node in position node_to_mutate[0] of the solution path
    # As well as the id of the 
    return nodes[node_to_mutate[0]].id, replacement_node.id

def select_crossover(soln_a : dt.Solution, soln_b : dt.Solution):

    a_nodes = soln_a.nodes
    b_nodes = soln_b.nodes

    options = []
    for i in range(1, len(a_nodes) - 1):

        for j in range (1, len(b_nodes) - 1):

            a_neighbours = a_nodes[i].get_neighbours()
            b_neighbours = b_nodes[j].get_neighbours()

            # if a_nodes[i-1].get_id() in b_neighbours and 

    
    
        

