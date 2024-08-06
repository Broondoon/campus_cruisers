"""
combine_solns.py

Contains methods for crossover and mutation.

"""
import random
from . import data_types as dt

# Input: a Solution object, an int representing /100 odds to mutate
# Output: a pair of Node IDs, the first being the one to replace, and the second being the replacement
def select_mutation(soln, odds):

    print("\nPath under mutation:", soln.nodes)
    
    if (odds > 100) or (odds < 0):
        print("Err - invalid odds; must be within 0-100")
        return None
    
    nodes = soln.nodes
    could_mutate = []
    # Range is funky so as to skip mutating the first and last nodes
    for i in range(1, len(nodes) - 1):
        left_node = nodes[i-1]
        curr_node = nodes[i]
        right_node = nodes[i+1]

        l_neighbours = left_node.get_neighbours()

        node_options = []
        for neighbour in l_neighbours:
            # print("Neighbour neighbours:", neighbour.get_neighbours())
            if neighbour in right_node.get_neighbours() and neighbour not in nodes:
                # print("Curr node:", curr_node, "replacement:", neighbour)
                node_options.append(neighbour)

        if len(node_options) > 0:
            could_mutate.append((i, node_options))

    # Don't roll the dice if there's nothing to mutate
    if len(could_mutate) == 0:
        print("No room for mutation along the path...\n\n")
        return None

    # Reminder: [0] is the id of the node to replace
    # [1] is the list of options to replace it with

    # Randomly choose (potentially more than 1, but k = 1 rn so only one)
    # This currently is hardcoded to only select 1. If you want more, get rid of [0] and add a for loop.
    node_to_mutate = random.choices(could_mutate, k = 1)[0] # weights=([odds] * len(could_mutate)), k = 1)[0]

    print(">> Debug - List of nodes to mutate:", node_to_mutate)

    # replacement_node is a Node object
    replacement_node = node_to_mutate[1][random.randrange(0, len(node_to_mutate[1]))]

    # print("ID to replace:", nodes[node_to_mutate[0]].id, "ID of replacement:", replacement_node.id)

    print("Path Before:", nodes[node_to_mutate[0]-2], nodes[node_to_mutate[0]-1], nodes[node_to_mutate[0]], nodes[node_to_mutate[0]+1], nodes[node_to_mutate[0]+2])
    print("New Mutated Path:" , nodes[node_to_mutate[0]-2], nodes[node_to_mutate[0]-1], replacement_node, nodes[node_to_mutate[0]+1], nodes[node_to_mutate[0]+2])

    return nodes[node_to_mutate[0]].id, replacement_node.id

# Input: Two solution objects
# Output: None or the two children from calling the crossover method
def select_crossover(soln_a : dt.Solution, soln_b : dt.Solution):
    # (index_a, index_b, extra_node_list, case)
    # note that extra_node_list will have 0 or 1 nodes
    # note case can be "same" or "first_cousin" or "second_cousin"
    crosspoints = []
    # a_nodes = soln_a.nodes
    for i, node_a in enumerate(soln_a.nodes):
        neighbours_a = node_a.get_neighbours()
        # b_nodes = soln_b.nodes
        for j, node_b in enumerate(soln_b.nodes):
            neighbours_b = node_b.get_neighbours()
            if node_a == node_b:
                # the solutions cross paths here
                crosspoints.append((i, j, [], "same"))
            for neighbour_a in neighbours_a:
                if node_b == neighbour_a:
                    # the solutions are directly next to each other here
                    crosspoints.append((i, j, [], "first_cousin"))
                for neighbour_b in neighbours_b:
                    if neighbour_b == neighbour_a:
                        # the solutions are seperated here by a single node
                        crosspoints.append((i, j, [neighbour_a], "second_cousin"))
                        pass
                    if node_a == neighbour_b:
                        # the solutions are directly next to each other here
                        crosspoints.append((i, j, [], "first_cousin"))
    num_options = len(crosspoints)
    if num_options == 0:
        # there are no crossover options
        return None
    selection = random.randint(0, num_options)
    index_a, index_b, extra_node_list, case = crosspoints[selection]
    return soln_a.crossover(soln_b, index_a, index_b, extra_node_list, case)

