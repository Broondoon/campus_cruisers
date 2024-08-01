""" Tests for the functionality in the stochastic_searches file. """

# imports
import unittest
import sys
sys.path.append("../src/")
from resources.stochastic_searches import random_depth_first_search


# test class def
class test_node_class:
    def __init__(self, testid, testneighbours = []):
        self.id = testid
        self.neighbours = testneighbours
    def get_neighbours(self):
        return self.neighbours
    def set_neighbours(self, neighbours):
        self.neighbours = neighbours


# test cases for random_depth_first_search
class TestRandomDFS(unittest.TestCase):
    def test_nopath(self):
        startnode = test_node_class("start")
        endnode = test_node_class("end")
        self.assertEqual([], random_depth_first_search(startnode, endnode))

    def test_onlyonenode(self):
        onenode = test_node_class("start and end")
        randompath = random_depth_first_search(onenode, onenode)
        self.assertEqual(1, len(randompath))
        self.assertEqual(onenode.id, randompath[0].id)
    
    def test_simplepath(self):
        startnode = test_node_class("start")
        endnode = test_node_class("end")
        startnode.set_neighbours([endnode])
        endnode.set_neighbours([startnode])
        randompath = random_depth_first_search(startnode, endnode)
        self.assertEqual(2, len(randompath))
        self.assertEqual(startnode.id, randompath[0].id)
        self.assertEqual(endnode.id, randompath[1].id)
    
    def test_pathwithdeadend(self):
        startnode = test_node_class("start")
        endnode = test_node_class("end")
        wrongwaynode = test_node_class("oops")
        startnode.set_neighbours([endnode, wrongwaynode])
        endnode.set_neighbours([startnode])
        wrongwaynode.set_neighbours([startnode])
        randompath = random_depth_first_search(startnode, endnode)
        self.assertEqual(2, len(randompath))
        self.assertEqual(startnode.id, randompath[0].id)
        self.assertEqual(endnode.id, randompath[1].id)
    
    def test_pathwithchoice(self):
        startnode = test_node_class("start")
        endnode = test_node_class("end")
        extranode = test_node_class("another route")
        startnode.set_neighbours([endnode, extranode])
        endnode.set_neighbours([startnode, extranode])
        extranode.set_neighbours([startnode, endnode])
        randompath = random_depth_first_search(startnode, endnode)
        pathlen = len(randompath)
        self.assertEqual(True, (pathlen == 2) or (pathlen == 3))
        self.assertEqual(startnode.id, randompath[0].id)
        self.assertEqual(endnode.id, randompath[-1].id)
    

# to run tests
if __name__ == '__main__':
    unittest.main()