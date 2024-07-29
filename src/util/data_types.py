"""
dataType.py

Contains the definition for the node() object class.

We could also update this file to have any/all custom objects/classes.

"""

class Solution: 
    nodes = []
    fitness = None

    def __init__(self, nodes, fitness = None):
        self.nodes = nodes
        self.fitness = fitness

    # def mutate(self):
    #     self.nodes = combine_solns.mutate()

class Node:
    name = None
    id = None
    xy = None

    soln_parent = None

    def __init__(self, name, id, coordinate):
        self.name = name
        self.id = id
        self.xy = coordinate

    def get_neighbours(self):

        # Defining empty list and adding values to it
        neighbour_list = []

        for i in range(len(globals.topography)):    # removed hardcoded value
            for j in range(len(globals.topography)):
                if (i == self.xy[0]) or (j == self.xy[1]):
                    neighbour_list.add(globals.topography[i][j])

        return neighbour_list
    
    def set_parent(self, parent):
        self.soln_parent = parent