"""
stochastic_searches.py

Code taken from other repos must follow their liscencing as well as be cited properly.

Bear!

"""


# Based on the randomized depth first search described here:
# https://en.wikipedia.org/wiki/Maze_generation_algorithm#Iterative_implementation_(with_stack)
#
def random_depth_first_search(starting_node, ending_node):
    # begin at the starting node
    node_list = [starting_node]
    visited = [starting_node.id]
    # main loop
    while len(node_list) > 0:
        # if node_list[0] == ending_node, exit loop
        # get node_list[0] neighbours
        # check if visited
        # if unvisited, randomly pick one and add to start of node_list and visited
        # if all visited, removed node_list[0] from node_list
        break
    # node_list contains a solution or is empty if ending_node not found
    return node_list

