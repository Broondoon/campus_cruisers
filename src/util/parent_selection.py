"""
parent_selection.py


"""

# Tournment selection
# Input: a list of Solutions (i.e. a generation), size of each tournament, any other params you can think of
# Output: a list of successful parents
# Parents are chosen by making several subsets of the generation, so that part can go in another function
# Nodes chosen to partake in a tournament should be chosen randomly
def select_parents(generation, subset_size):
    # something something
    # loop N times, where N = len(generation) / subset_size
    # do host_tournament() with subset
    # add results of host_tournament() to a list or something of the best ones
    # return parents
    pass

# Tournament hosting
# Input: a subset of of Solutions
# Output: 
def host_tournament():
    pass

