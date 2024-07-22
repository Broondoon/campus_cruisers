""" Tests for the fitness functionality. """

# imports
import unittest
import sys
sys.path.append("../src/util/")
import fitness

# test class defs
class test_solution_class:
    def __init__(self, nodes):
        self.nodes = nodes
class test_node_class:
    def __init__(self, testid, x = 0, y = 0):
        self.id = testid
        self.x = x
        self.y = y

# test data
test_lookup_table = [[0, 1],[1, 0]]

# test cases
class TestFitness(unittest.TestCase):
    def test_empty(self):
        nodeless = test_solution_class([])
        self.assertEqual(0, fitness.fitness(nodeless, test_lookup_table))
    
    def test_onenode(self):
        node0 = test_node_class(0)
        onenode = test_solution_class([node0])
        self.assertEqual(0, fitness.fitness(onenode, test_lookup_table))
    
    def test_twonodes(self):
        node0 = test_node_class(0)
        node1 = test_node_class(1)
        twonodes = test_solution_class([node0, node1])
        self.assertEqual(1, fitness.fitness(twonodes, test_lookup_table))

# to run tests
if __name__ == '__main__':
    unittest.main()