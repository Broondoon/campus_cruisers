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
        # check if ending_node found
        if node_list[0].id == ending_node.id:
            break
        # get node_list[0] neighbours
        neighbours = node_list[0].get_neighbours()
        # check if visited
        next_node_options = []
        for node in neighbours:
            if neighbours.count(node.id) == 0:
                next_node_options.append(node)
        # at least one unvisited node
        if len(next_node_options) > 0:
            randpick = random.randrange(len(next_node_options))
            node_list.insert(0, next_node_options[randpick])
            visited.append(next_node_options[randpick].id)
        # all neighbours visited
        else:
            node_list.pop(0)
    # node_list contains a solution or is empty if ending_node not found
    return node_list

