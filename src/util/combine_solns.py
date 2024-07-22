"""
combine_solns.py

Contains methods for crossover and mutation.

"""
import random

# dummy_lookup_table = [0, 0][0, 0]

class Solution():
    nodes = []

    def __init__(self, nodes):
        self.nodes = nodes

def select_mutation(soln):
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
        
    # Randomly choose which valid node to mutate
    node_to_mutate = random.randrange(0, len(could_mutate))
    index = node_to_mutate[0]

    # Randomly choose which mutation to take
    replacement = node_to_mutate[1][random.randrange(0, len(node_to_mutate[1]))]

    return(index, replacement)


# TODO: add this to solution class
def mutate(self):
    pass
    # soln.replace_node(index, replacement)
        

# soln = Solution()
# select_mutation(soln)
        


    
    
        

