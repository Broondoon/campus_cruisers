"""
combine_solns.py

Contains methods for crossover and mutation.

"""
import random

# Input: a Solution object, an int representing /100 odds to mutate
# Output: a pair of Node IDs, the first being the one to replace, and the second being the replacement
def select_mutation(soln, odds):

    if (odds > 100) or (odds < 0):
        print("Err - invalid % odds; must be within 0-100")
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

    # Randomly choose (potentially more than 1, but k = 1 rn so only one)
    node_to_mutate = random.choices(could_mutate, weights=((odds) * len(could_mutate)), k = 1)

    print(">> Debug - List of nodes to mutate:", node_to_mutate)

    replacement_node = node_to_mutate[1][random.randrange(0, len(node_to_mutate[1]))]

    # Reminder: [0] is the id of the node to replace
    # [1] is the list of options to replace it with
    return(node_to_mutate[0], replacement_node.id)


# TODO: add this to solution class
def mutate(soln, old_id, new_id):
    
    # Python list comprehension!
    # Replaces an old node with a new node
    #   if that node's ID matches what we want to get rid of
    #   Else, keeps the old node
    new_path = [Nodes.get(new_id) if node.id == old_id else node for node in soln]

    new_soln = Solution(new_path)
    return new_soln

    # soln.replace_node(index, replacement)
        

# soln = Solution()
# select_mutation(soln)
        


    
    
        

