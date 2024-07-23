""" Tests for the functionality in the fitness file. """

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


# test cases for fitness function
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

# test cases for check_terminate function
class TestCheckTerminate(unittest.TestCase):
    def test_inadequatehistorylength(self):
        self.assertEqual(False, fitness.check_terminate([], 1, 1))
    
    def test_shouldnotterminate(self):
        self.assertEqual(False, fitness.check_terminate([42, 45], 2, 1))
    
    def test_shouldterminate(self):
        self.assertEqual(True, fitness.check_terminate([42, 45], 2, 5))

# test cases for add_to_history function
class TestAddToHistory(unittest.TestCase):
    def test_firstadd(self):
        self.assertEqual([42], fitness.add_to_history([45, 72, 42, 66], []))
    
    def test_addsame(self):
        self.assertEqual([42, 42], fitness.add_to_history([45, 72, 42, 66], [42]))
    
    def test_adddifferent(self):
        self.assertEqual([45, 42, 42], fitness.add_to_history([45, 72, 47, 66], [42, 42]))


# to run tests
if __name__ == '__main__':
    unittest.main()